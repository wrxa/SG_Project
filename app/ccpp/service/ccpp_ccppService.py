# -*- coding: utf-8 -*-
"""
ccpp_ccpp：sheet的服务处理程序
"""
from sqlalchemy import and_
from app.energy_island.models import Device
from base import FieldCalculation
from app.ccpp.models.device_dictEntity import DeviceDict
from app.ccpp.models.ccpp_ccpp_calculateModel import Ccpp_ccpp
from app.ccpp.models.ccpp_turbineModel import CcppTurbine
from app.ccpp.models.constantModel import CcppConstant
import json
from app.ccpp import gl
from ccpp_calculate_calculation import Ccpp_EXEC, Ccpp_PlanList
from app.ccpp.service.ccpp_equipmentService import CcppEquipments
import copy
from app.main.service.turbine.turbine_foctory import Factory
from app.ccpp.models.ccpp_ccpp_economicModel import Ccpp_ccpp_economic
from app import db
from app.ccpp.models.ccpp_biomassModel import CcppCHPWaterTreatment
from app.ccpp.models.ccpp_chimney_calculateModel import CcppChimneyCalculate
from flask import current_app
from app.ccpp.service.ccpp_chimney_strategy import Ccpp_chimney_calculateBefore


"""
燃机选择处理模块
"""


class SelectGasTurbineService(FieldCalculation):

    '''
    获得电负荷需求:存在则得到，不存在则返回0
    '''
    def getEngine_demand_power(self, planId):
        ccpp_ccpp = Ccpp_ccpp.search_ccpp_ccpp(planId)
        if ccpp_ccpp is not None and ccpp_ccpp.engine_demand_power_design is not None:
            return ccpp_ccpp.engine_demand_power_design
        return 0

    """
    根据传入的需求功率按照上下浮动10%的方式查找是否存在nx落入浮动区间
    入参：燃机需求功率engine_demand_power
    出参：[{device:设备,max_n:设备个数最大值,min_n:设备个数最小值},{},{}]设备组
    """
    def getGasTurbine(self, engine_demand_power, plan_id):
        engine_demand_power = float(engine_demand_power)
        deviceDictList = []
        device_list_all = Device.query.filter(and_(Device.device_class == '4', Device.device_type == '1', Device.main_prop_value_1 <= engine_demand_power * 1.1)).all()
        for device in device_list_all:
            max_device = (engine_demand_power * 1.1) / float(device.main_prop_value_1)
            min_device = (engine_demand_power * 0.9) / float(device.main_prop_value_1)
            max_device_number = int(max_device)
            min_device_number = int(min_device)
            if max_device_number - min_device_number > 0:
                if min_device - min_device_number > 0:
                    for i in range(min_device_number + 1, max_device_number + 1):
                        if i > 4:
                            continue
                        deviceDictList.append(
                            DeviceDict(
                                device=device,
                                need_engine_demand_power=engine_demand_power,
                                number=i
                            )
                        )
                else:
                    for i in range(min_device_number, max_device_number + 1):
                        if i > 4:
                            continue
                        deviceDictList.append(DeviceDict(device=device, need_engine_demand_power=engine_demand_power, number=i))
        ccppmodellist = []
        ccppturbinelist = []
        # 遍历deviceDictList计算获取数据库中设置好的参数分别计算每一条最终方案
        oldccpp = Ccpp_ccpp.search_ccpp_ccpp(plan_id)   
        # 查询汽轮机原始数据
        oldccppTurbine = CcppTurbine.search_CcppTurbine(plan_id)
        list_column_furnace = gl.getCcppName_engList()
        list_column_turbine = gl.getTurbineName_engList()

        for deviceDict in deviceDictList:
            ccpp_ccpp = copy.deepcopy(oldccpp)
            # 保存汽轮机原始数据
            ccppTurbine = copy.deepcopy(oldccppTurbine)
            print(deviceDict.device.id)
            # 填充燃机数据
            CcppCalculateService().setCcppGasTurbineData(ccpp_ccpp, deviceDict.device.id, deviceDict.number)
            # 计算全部
            ccpp_ccpp = Ccpp_PlanList().specialCalculation(ccpp_ccpp)
            try:
                # 根据ccpp计算出来的主蒸汽：压力、温度、产气量传入汽轮机计算汽轮机数据。
                # 填充汽轮机的主蒸汽：温度、压力、流量
                ccppTurbine = CcppCalculateService().tbdataturbine(ccpp_ccpp, ccppTurbine)
                # 计算汽轮机的计算if97
                pointPower0, ccppTurbine = Factory().executePlanlist(ccppTurbine)
                ccpp_ccpp.high_steam_pressure_design
                # 刷新
                ccppmodellist.append(copy.deepcopy(ccpp_ccpp))
                setattr(ccppTurbine, 'i_total_power0', pointPower0)
                ccppTurbine.e_steam_flow
                # 追加在模型后面。
                ccppturbinelist.append(copy.deepcopy(ccppTurbine))
            except Exception as e:
                current_app.logger.error(u'操作者：%d,生成方案过程中汽轮机计算发生异常%s', current_app.id, e.message)
                print("Error %s" % e)
        # 格式化ccpp数据
        for ccppmodel in ccppmodellist:
            for index in range(len(list_column_furnace)):
                if hasattr(ccppmodel, list_column_furnace[index]):
                    var = getattr(ccppmodel, list_column_furnace[index])
                    setattr(ccppmodel, list_column_furnace[index], gl.format_value(var))
        # # 格式化汽轮机数据
        for turbinemodel in ccppturbinelist:
            for index in range(len(list_column_turbine)):
                if hasattr(turbinemodel, list_column_turbine[index]):
                    var = getattr(turbinemodel, list_column_turbine[index])
                    setattr(turbinemodel, list_column_turbine[index], gl.format_value(var))
        return ccppmodellist, ccppturbinelist

    '''
    根据用户选择的方案：
    1、将燃机数据保存在ccpp_ccpp表结构中
    2、将前台传过来的主蒸汽：进气温度、进气压力、进气流量更新到汽轮机表中。
    '''
    def saveGasTurbineData(self, id, num, planId):
        ccpp_ccpp = Ccpp_ccpp.search_ccpp_ccpp(planId)
        ccppTurbine = CcppTurbine.search_CcppTurbine(planId)
        # 填充燃机数据
        CcppCalculateService().setCcppGasTurbineData(ccpp_ccpp, id, num)
        # ccpp计算
        ccpp_ccpp = Ccpp_PlanList().specialCalculation(ccpp_ccpp)
        Ccpp_ccpp.updata_ccpp(ccpp_ccpp)

        # ccpp同步数据到汽轮机
        ccppTurbine = CcppCalculateService().tbdataturbine(ccpp_ccpp, ccppTurbine)

        # 汽轮机的计算
        pointPower0, ccppTurbine = Factory().executePlanlist(ccppTurbine)
        setattr(ccppTurbine, 'i_total_power0', pointPower0)
        CcppTurbine.insert_CcppTurbine(ccppTurbine)
        # 同步ccpp计算数据到设备列表中
        CcppEquipments().tbdataequipmentlist(ccpp_ccpp, planId)
        # 同步汽轮机数据到设备列表中
        CcppEquipments().replaceTurbineTurbine(planId, ccppTurbine)
        # 同步数据到化学水中
        biomassmodel = CcppCHPWaterTreatment.search_water(planId)
        CcppCalculateService().tbdatatowater_treatment(ccpp_ccpp, biomassmodel)
        # 同步数据到烟囱中
        chimney = CcppChimneyCalculate.search_chimney_calculate(planId)
        CcppCalculateService().tbdatachimney(ccpp_ccpp, chimney)
        # 同步数据到经济性分析中
        CcppCalculateService().tbdata(planId)


'''
该模块为ccpp_ccppView提供服务
'''


class CcppCalculateService():
    '''
    根据planId返回当前方案的主要设备参数字符串
    '''
    def getMainEquipmentPara(self, planId):
        ccpp = Ccpp_ccpp.search_ccpp_ccpp(planId)
        turbine = CcppTurbine.search_CcppTurbine(planId)
        mainEquipmentPara = u''
        # 第一段
        if ccpp.engine_id_design is not None and ccpp.engine_id_design != -1:
            mainEquipmentPara += u'' + gl.getstrcolm(ccpp.engine_num_design) + u'X' + gl.getstrcolm(ccpp.engine_power_design) + u'MW燃汽轮发电机组(' + ccpp.engine_model_design + u')'
            mainEquipmentPara += u'\n'
        # 第二段
        if ccpp.boiler_single_or_dula_pressure_design is not None:
            
            if ccpp.boiler_single_or_dula_pressure_design == u'singlepot':
                mainEquipmentPara += u'1X' + gl.getstrcolm(ccpp.sp_low_gas_production_design) + 't/h'
                mainEquipmentPara += u'单压余热锅炉\n'
            else:
                mainEquipmentPara += u'1X' + gl.getstrcolm(ccpp.high_gas_production_design) + '/' + gl.getstrcolm(ccpp.low_gas_production_design) + 't/h'
                mainEquipmentPara += u'双压余热锅炉\n'
   
        # 第三段
        if turbine.s_steam_type_test is not None:
            mainEquipmentPara += u'1X' + gl.getstrcolm(turbine.e_steam_extraction_select) + u'MW'
            if turbine.s_steam_type_test == 1:
                mainEquipmentPara += u'抽凝汽轮发电机组'
            elif turbine.s_steam_type_test == 2:
                mainEquipmentPara += u'背压汽轮发电机组'
            elif turbine.s_steam_type_test == 3:
                mainEquipmentPara += u'补凝汽轮发电机组'
            else:
                pass
        if mainEquipmentPara == u'':
            return None
        else:
            return mainEquipmentPara

    # 删除方案
    def deletebyPlanId(self, planId):
        ccpp_ccpp = Ccpp_ccpp.search_ccpp_ccpp(planId)
        db.session.delete(ccpp_ccpp)
    '''
    1、加载页面常量数据
    2、加载页面input数据,返回字典的形式数据
    3、加载燃机数据
    '''
    def getCcppConstantData(self):
        # 加载页面常量数据
        ccppConstant = CcppConstant.search_ccppConstant('ccpp_ccpp')
        gl.listsort(ccppConstant)
        return ccppConstant

    def getCcppInputData(self, planId):
        # 加载页面input数据
        ccpp_ccpp = Ccpp_ccpp.search_ccpp_ccpp(planId)
        ccppConstant = CcppConstant.search_ccppConstant('ccpp_ccpp')
        list_column_furnace = gl.getCcppName_engList()
        datas = {}
        permissiondata = {}
        defaultvaluedata = {}
        for index in range(len(list_column_furnace)):
            if hasattr(ccpp_ccpp, list_column_furnace[index]):
                var = getattr(ccpp_ccpp, list_column_furnace[index])
                datas[list_column_furnace[index]] = gl.format_value(var)

        for constant in ccppConstant:
            permissiondata[constant.name_eng + '_design'] = constant.permission
            defaultvaluedata[constant.name_eng + '_design'] = constant.defaultvalue
        if datas['engine_id_design'] is None or datas['engine_id_design'] == '':
            datas['engine_id_design'] = -1
        return datas, permissiondata, defaultvaluedata

    '''
    获得全部燃机
    '''
    def getAllGasTurbine(self):
        deviceDictList = []
        device_list_all = Device.query.filter(and_(Device.device_class == '4', Device.device_type == '1')).all()
        for device in device_list_all:
            deviceDictList.append(DeviceDict(device=device, need_engine_demand_power=0, number=1))
        return deviceDictList

    '''
    通过id获得燃机
    '''
    def getGasTurbineById(self, id, gasnum):
        ccpp_ccpp = Ccpp_ccpp()
        self.setCcppGasTurbineData(ccpp_ccpp, id, gasnum)
        list_column_furnace = gl.getCcppName_engList()
        datas = {}
        for index in range(len(list_column_furnace)):
            if hasattr(ccpp_ccpp, list_column_furnace[index]):
                var = getattr(ccpp_ccpp, list_column_furnace[index])
                datas[list_column_furnace[index]] = gl.format_value(var)
        return datas

    def submitCcppCalculateForm(self, form, plan_id):
        '''
        将表单中的数据更新到ccpp表中
        '''
        ccpp_ccpp = Ccpp_ccpp.query.filter_by(
            plan_id=plan_id).first()
        # 构造列
        list_column_ccpp = gl.getCcppName_engList()
        # 为模型赋值sp_h_blowdown_rate_design，high_blowdown_rate_design
        for index in range(len(list_column_ccpp)):
            formdata = form.get(list_column_ccpp[index])
            if hasattr(ccpp_ccpp, list_column_ccpp[index]):
                if formdata is not None and formdata != '':
                    setattr(ccpp_ccpp, list_column_ccpp[index],
                            formdata)
                else:
                    setattr(ccpp_ccpp, list_column_ccpp[index],
                            None)
        '''
        计算填充
        '''
        if form.get('ccpptargethtml') == 'ccppcalculate':
            ccpp_ccpp = Ccpp_EXEC().specialCalculation(ccpp_ccpp, form)
            # ccpp同步数据到设备列表中
            CcppEquipments().tbdataequipmentlist(ccpp_ccpp, plan_id)
            # ccpp同步数据到汽轮机中
            ccppTurbine = CcppTurbine.search_CcppTurbine(plan_id)
            ccppTurbine = CcppCalculateService().tbdataturbine(ccpp_ccpp, ccppTurbine)
            CcppTurbine.insert_CcppTurbine(ccppTurbine)
            # 同步数据到经济性分析表中
            CcppCalculateService().tbdata(plan_id)
            # 同步数据到化学水中
            biomassmodel = CcppCHPWaterTreatment.search_water(plan_id)
            self.tbdatatowater_treatment(ccpp_ccpp, biomassmodel)
            
            # 同步数据到烟囱中
            chimney = CcppChimneyCalculate.search_chimney_calculate(plan_id)
            self.tbdatachimney(ccpp_ccpp, chimney)
            
        # 更新数据
        Ccpp_ccpp.updata_ccpp(ccpp_ccpp)

    def setCcppGasTurbineData(self, ccpp_ccpp, id, gasnum):
        deviceDict = Device.search_deviceById(id)
        props_json = json.loads(deviceDict.props_json)
        # 燃机个数
        setattr(ccpp_ccpp, 'engine_num_design', gasnum)
        # 设备表的ID
        setattr(ccpp_ccpp, 'engine_id_design', id)
        # 燃机型号
        index = props_json['prop_name'].index(u'然机型号')
        setattr(ccpp_ccpp, 'engine_model_design', props_json['prop_value'][index])
        # 燃机功率
        index = props_json['prop_name'].index(u'燃机出力')
        setattr(ccpp_ccpp, 'engine_power_design', gl.tran_str_float(props_json['prop_value'][index]))
        # 燃机热耗率
        index = props_json['prop_name'].index(u'热耗率')
        setattr(ccpp_ccpp, 'engine_heat_consmption_rate_design', gl.tran_str_float(props_json['prop_value'][index]))
        # 燃机效率
        index = props_json['prop_name'].index(u'燃机效率')
        setattr(ccpp_ccpp, 'engine_efficiency_design', gl.tran_str_float(props_json['prop_value'][index]))
        # 燃机压比
        index = props_json['prop_name'].index(u'压比')
        setattr(ccpp_ccpp, 'engine_pressure_ratio_design', gl.tran_str_float(props_json['prop_value'][index]))
        # 单机天燃气耗量
        index = props_json['prop_name'].index(u'天然气耗量')
        setattr(ccpp_ccpp, 'individual_gas_consumption_design', gl.tran_str_float(props_json['prop_value'][index]))
        # 排烟温度
        index = props_json['prop_name'].index(u'燃机排烟温度')
        setattr(ccpp_ccpp, 'engine_exhuast_gas_temperature_design', gl.tran_str_float(props_json['prop_value'][index]))
        # 排烟流量
        index = props_json['prop_name'].index(u'锅炉烟气流量')
        setattr(ccpp_ccpp, 'engine_exhuast_gas_flux_design', gl.tran_str_float(props_json['prop_value'][index]))

    # ccpp同步数据到汽轮机中
    def tbdataturbine(self, ccpp_ccpp, ccppTurbine):
        # 查询汽轮机数据
        if ccpp_ccpp.boiler_single_or_dula_pressure_design == 'doublepot':
            if ccpp_ccpp.high_steam_temperature_design is not None and float(ccpp_ccpp.high_steam_temperature_design) >= 5:
                setattr(ccppTurbine, 'e_steam_temperature', copy.deepcopy(float(ccpp_ccpp.high_steam_temperature_design) - 5))
            else:
                setattr(ccppTurbine, 'e_steam_temperature', copy.deepcopy(ccpp_ccpp.high_steam_temperature_design))
            if ccpp_ccpp.high_steam_pressure_design is not None and float(ccpp_ccpp.high_steam_pressure_design) >= 0.4:
                setattr(ccppTurbine, 'e_steam_pressure', copy.deepcopy(float(ccpp_ccpp.high_steam_pressure_design) - 0.4))
            else:
                setattr(ccppTurbine, 'e_steam_pressure', copy.deepcopy(ccpp_ccpp.high_steam_pressure_design))
            setattr(ccppTurbine, 'e_steam_flow', copy.deepcopy(float(ccpp_ccpp.high_gas_production_design) * 0.97))
            setattr(ccppTurbine, 'e_throttle_flow', copy.deepcopy(float(ccpp_ccpp.high_gas_production_design) * 0.97))
            setattr(ccppTurbine, 'hh1_water_temperature', copy.deepcopy(float(ccpp_ccpp.low_feedwater_temperature_design)))
            # 锅炉计算给汽轮机同步排污率数据
            setattr(ccppTurbine, 'h_blowdown_rate', copy.deepcopy(float(ccpp_ccpp.high_blowdown_rate_design)))
        elif ccpp_ccpp.boiler_single_or_dula_pressure_design == 'singlepot':
            if ccpp_ccpp.sp_steam_temperature_design is not None and float(ccpp_ccpp.sp_steam_temperature_design) >= 5:
                setattr(ccppTurbine, 'e_steam_temperature', copy.deepcopy(float(ccpp_ccpp.sp_steam_temperature_design) - 5))
            else:
                setattr(ccppTurbine, 'e_steam_temperature', copy.deepcopy(ccpp_ccpp.sp_steam_temperature_design))
            if ccpp_ccpp.sp_steam_pressure_design is not None and float(ccpp_ccpp.sp_steam_pressure_design) >= 0.4:
                setattr(ccppTurbine, 'e_steam_pressure', copy.deepcopy(float(ccpp_ccpp.sp_steam_pressure_design) - 0.4))
            else:
                setattr(ccppTurbine, 'e_steam_pressure', copy.deepcopy(ccpp_ccpp.sp_steam_pressure_design))
            setattr(ccppTurbine, 'e_steam_flow', copy.deepcopy(float(ccpp_ccpp.sp_low_gas_production_design) * 0.97))
            setattr(ccppTurbine, 'e_throttle_flow', copy.deepcopy(float(ccpp_ccpp.sp_low_gas_production_design) * 0.97))
            setattr(ccppTurbine, 'hh1_water_temperature', copy.deepcopy(float(ccpp_ccpp.sp_low_feedwater_temperature_design)))
            # 锅炉计算给汽轮机同步排污率数据
            setattr(ccppTurbine, 'h_blowdown_rate', copy.deepcopy(float(ccpp_ccpp.sp_h_blowdown_rate_design)))
        else:
            pass
        # 更新进气温度、进气压力、进气流量
        ccppTurbine.e_steam_flow
        return ccppTurbine

    # 同步ccpp计算和汽轮机计算数据到经济性分析中
    def tbdata(self, plan_id):
        engine_power_sum = 0.0
        individual_gas_consumption_sum = 0.0
        ccppTurbine = CcppTurbine.search_CcppTurbine(plan_id)
        ccpp_ccpp_economic = Ccpp_ccpp_economic.search_economic(plan_id)
        ccpp_ccpp = ccpp_ccpp = Ccpp_ccpp.query.filter_by(plan_id=plan_id).first()
        e_gross_generation = ccppTurbine.e_gross_generation

        # 将结果数据中的燃机总发电量、汽轮机的总发电量取出不为空则计算同步
        if ccpp_ccpp.engine_num_design is not None and ccpp_ccpp.engine_power_design is not None and e_gross_generation is not None:
            engine_power_sum = (ccpp_ccpp.engine_num_design * ccpp_ccpp.engine_power_design + e_gross_generation) * 8040 / 10000

        # 将结果数据中的燃机天然气总消耗量取出不为空则计算同步
        if ccpp_ccpp.engine_num_design is not None and ccpp_ccpp.individual_gas_consumption_design is not None:
            individual_gas_consumption_sum = ccpp_ccpp.engine_num_design * ccpp_ccpp.individual_gas_consumption_design * 8040 / 10000

        ccpp_ccpp_economic.power_supply_capacity_1 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_2 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_3 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_4 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_5 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_6 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_7 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_8 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_9 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_10 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_11 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_12 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_13 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_14 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_15 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_16 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_17 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_18 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_19 = engine_power_sum
        ccpp_ccpp_economic.power_supply_capacity_20 = engine_power_sum

        ccpp_ccpp_economic.gas_consumption_1 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_2 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_3 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_4 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_5 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_6 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_7 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_8 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_9 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_10 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_11 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_12 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_13 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_14 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_15 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_16 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_17 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_18 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_19 = individual_gas_consumption_sum
        ccpp_ccpp_economic.gas_consumption_20 = individual_gas_consumption_sum
        Ccpp_ccpp_economic.updata_ccppeconomic(ccpp_ccpp_economic)
        return ccpp_ccpp_economic

    # 同步ccpp计算到循环水中
    def tbdatatowater_treatment(self, ccpp_ccpp, biomassmodel):
        if ccpp_ccpp.boiler_single_or_dula_pressure_design == 'doublepot':
            biomassmodel.o_steam_flow = float(ccpp_ccpp.high_gas_production_design) * 0.97
        elif ccpp_ccpp.boiler_single_or_dula_pressure_design == 'singlepot':
            biomassmodel.o_steam_flow = float(ccpp_ccpp.sp_low_gas_production_design) * 0.97
        else:
            pass
        CcppCHPWaterTreatment.insert_water(biomassmodel)
        return biomassmodel

    # 同步ccpp计算到烟囱中
    def tbdatachimney(self, ccpp_ccpp, chimney):
        chimney.engine_num_design = ccpp_ccpp.engine_num_design
        if ccpp_ccpp.boiler_single_or_dula_pressure_design == 'doublepot':
            chimney.flue_gas_quantity = ccpp_ccpp.high_engine_exhuast_gas_flux_design
        elif ccpp_ccpp.boiler_single_or_dula_pressure_design == 'singlepot':
            chimney.flue_gas_quantity = ccpp_ccpp.sp_engine_exhuast_gas_flux_design
        else:
            pass
        Ccpp_chimney_calculateBefore().specialCalculationdb(chimney)
        CcppChimneyCalculate.updata_chimney_calculate(chimney)
        return chimney
    
    
            
