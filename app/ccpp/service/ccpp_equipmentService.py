# -*- coding: utf-8 -*-
"""
ccpp设备表：sheet的服务处理程序
"""
from app.models import EquipmentList, EquipmentListTemplate, Module
from app.ccpp.models.ccpp_questionnaireModel import Questionnaire
from app.ccpp import gl
from app.ccpp.models.ccpp_turbineModel import CcppTurbine
from app.ccpp.service.ccpp_TurbineAuxiliary import CcppTurbineAuxiliaryService
import urllib
import json


class CcppEquipments():

    # 同步ccpp计算数据到设备列表中
    def tbdataequipmentlist(self, ccpp_ccpp, planId):
        equipmentList = EquipmentList.search_equipmentList(planId)
        questionnaire = Questionnaire.search_questionnaire(planId)
        engine_model_design = u'燃气轮机发电机组类型：' + ccpp_ccpp.engine_model_design + u'；'
        engine_power_design = u'燃机功率:' + gl.getstrcolm(ccpp_ccpp.engine_power_design) + u'kW；'
        # engine_demand_power_design = u'电负荷需求:' + gl.getstrcolm(ccpp_ccpp.engine_demand_power_design) + u''
        higher_voltage_level = u'上级变电压等级:' + gl.getstrcolm(questionnaire.higher_voltage_level) + u'kV；'
        individual_gas_consumption_design = u'燃气消耗:' + gl.getstrcolm(ccpp_ccpp.individual_gas_consumption_design) + u'Nm3/h；'
        engine_exhuast_gas_temperature_design = u'排烟温度:' + gl.getstrcolm(ccpp_ccpp.engine_exhuast_gas_temperature_design) + u'℃；'
        engine_exhuast_gas_flux_design = u'排烟量:' + gl.getstrcolm(ccpp_ccpp.engine_exhuast_gas_flux_design) + u't/h；'
        low_gas_production_design = u'低压产气量:' + gl.getstrcolm(ccpp_ccpp.low_gas_production_design) + u't/h；'

        high_steam_pressure_design = u'中压部分：蒸汽压力:' + gl.getstrcolm(ccpp_ccpp.high_steam_pressure_design) + u'Mpa；'
        high_steam_temperature_design = u'蒸汽温度:' + gl.getstrcolm(ccpp_ccpp.high_steam_temperature_design) + u'℃；'
        high_gas_production_design = u'高压产气量:' + gl.getstrcolm(ccpp_ccpp.high_gas_production_design) + u't/h；'

        low_drum_pressure_design = u'低压部分：蒸汽压力:' + gl.getstrcolm(ccpp_ccpp.low_drum_pressure_design) + u'Mpa；'
        low_superheat_steam_temperature_design = u'蒸汽温度:' + gl.getstrcolm(ccpp_ccpp.low_superheat_steam_temperature_design) + u'℃；'

        sp_low_gas_production_design = gl.getstrcolm(ccpp_ccpp.sp_low_gas_production_design) + u't/h单压余热锅炉；'
        sp_low_drum_pressure_design = u'汽包压力:' + gl.getstrcolm(ccpp_ccpp.sp_low_drum_pressure_design) + u'Mpa；'
        sp_low_superheat_steam_temperature_design = u'蒸汽温度:' + gl.getstrcolm(ccpp_ccpp.sp_low_superheat_steam_temperature_design) + u'℃；'
        sp_low_drum_pressure_design = u'蒸发量:' + gl.getstrcolm(ccpp_ccpp.sp_low_gas_production_design) + u't/h；'

        data = json.loads(equipmentList.equipment_content)
        equipmentCount = len(data['equipment_name'])
        for j in range(0, equipmentCount):
            if data['equipment_uid'][j] == '0':
                data['equipment_content'][j] = engine_model_design + engine_power_design + higher_voltage_level + individual_gas_consumption_design + engine_exhuast_gas_temperature_design + engine_exhuast_gas_flux_design
            elif data['equipment_uid'][j] == '1':
                data['equipment_content'][j] = engine_model_design
            elif data['equipment_uid'][j] == '15':
                data['equipment_content'][j] = engine_power_design + higher_voltage_level
            elif data['equipment_uid'][j] == '34':
                if ccpp_ccpp.boiler_single_or_dula_pressure_design == 'doublepot':
                    data['equipment_name'][j] = u'双压余热锅炉'
                    data['equipment_content'][j] = high_gas_production_design + low_gas_production_design + high_steam_pressure_design + high_steam_temperature_design + high_gas_production_design + low_drum_pressure_design + low_superheat_steam_temperature_design + low_gas_production_design
                elif ccpp_ccpp.boiler_single_or_dula_pressure_design == 'singlepot':
                    data['equipment_name'][j] = u'单压余热锅炉'
                    data['equipment_content'][j] = sp_low_gas_production_design + sp_low_drum_pressure_design + sp_low_superheat_steam_temperature_design + sp_low_drum_pressure_design
                else:
                    pass
            else:
                pass
        equipmentList.equipment_content = json.dumps(data)
        EquipmentList.insert_equipmentList(equipmentList)

    '''
    替换汽轮机表
    '''
    def replaceTurbineTurbine(self, planId, ccppTurbine=None):
        if ccppTurbine is None:
            ccppTurbine = CcppTurbine.search_CcppTurbine(planId)
        equipmentList = EquipmentList.search_equipmentList(planId)
        data = json.loads(equipmentList.equipment_content)
        equipmentCount = len(data['equipment_name'])
        for j in range(0, equipmentCount):
            if data['equipment_uid'][j] == '17':
                # P=（汽轮机计算！F5）MPa，T=（汽轮机计算！F6）℃　Q=（汽轮机计算！F7）t/h
                data['equipment_content'][j] = u"P=" + gl.getstrcolm(ccppTurbine.e_steam_pressure) + u"MPa，T=" + gl.getstrcolm(ccppTurbine.e_steam_temperature) + u"℃　Q=" + gl.getstrcolm(ccppTurbine.e_steam_flow) + u"t/h"
        equipmentList.equipment_content = json.dumps(data)
        EquipmentList.insert_equipmentList(equipmentList)

    '''
    替换汽机辅机表
    '''
    def replaceTurbineAuxiliary(self, planId, turbineAuxiliary=None):
        if turbineAuxiliary is None:
            turbineAuxiliary = CcppTurbineAuxiliaryService.search_turbine_auxiliary(planId)
        equipmentList = EquipmentList.search_equipmentList(planId)
        data = json.loads(equipmentList.equipment_content)
        equipmentCount = len(data['equipment_name'])
        for j in range(0, equipmentCount):
            if data['equipment_uid'][j] == '18':
                # 排汽参数：Q=（汽机辅机计算！G18）t/h，P=（汽机辅机计算！G19）MPa，T=（汽机辅机计算！G21）℃
                data['equipment_content'][j] = u"排汽参数：Q=" + gl.getstrcolm(turbineAuxiliary.m_condenser_pressure) +\
                                               u"t/h，P=" + gl.getstrcolm(turbineAuxiliary.m_steam_enthalpy) + u"MPa，T=" +\
                                               gl.getstrcolm(turbineAuxiliary.m_saturation_temperature) + u"℃"
            elif data['equipment_uid'][j] == '28':
                # Q=（汽机辅机系统！G8）m3/h，H=（汽机辅机系统！G7）
                data['equipment_content'][j] = u"Q=" + gl.getstrcolm(turbineAuxiliary.w_flow_amount) + u"m3/h，H=" + \
                                               gl.getstrcolm(turbineAuxiliary.w_condensate_pump_lift)
            elif data['equipment_uid'][j] == '29':
                # P=（汽机辅机系统！G13）KW
                data['equipment_content'][j] = u"P=" + gl.getstrcolm(turbineAuxiliary.w_auxiliary_motor_power) + u"KW"
            elif data['equipment_uid'][j] == '30':
                # 工作压力：（汽机辅机计算！G44）MPa；扬程：（汽机辅机计算！G48）m；
                data['equipment_content'][j] = u"工作压力：" + gl.getstrcolm(turbineAuxiliary.f_air_ejector_pressure) +\
                                               u"MPa；扬程：" + gl.getstrcolm(turbineAuxiliary.f_total_lift) + u"m"
            elif data['equipment_uid'][j] == '31':
                # （汽机辅机计算！G54）KW
                data['equipment_content'][j] = gl.getstrcolm(turbineAuxiliary.f_auxiliary_motor_power) + u"KW"
            else:
                pass
        equipmentList.equipment_content = json.dumps(data)
        EquipmentList.insert_equipmentList(equipmentList)

    @staticmethod
    def getmdtitledict():
        mdtitledict = {'a': u'燃气轮机发电机组', 'b': u'汽轮发电机组及辅助设备',
                       'c': u'余热锅炉', 'c1': u'余热锅炉辅机', 'd': u'分散控制系统',
                       'e1': u'水系统', 'e2': u'消防水系统',
                       'e3': u'废水处理系统', 'f': u'循环水冷却系统', 'g': u'厂用/仪表用压缩空气系统',
                       'h': u'往复式发动机发电机组', 'i': u'电气设备', 'j': u'实验室设备', 'k': u'其它设备'}
        mdtitletotitle = {'a': u'一', 'b': u'二',
                          'c': u'三', 'c1': u'四', 'd': u'五',
                          'e1': u'六', 'e2': u'七',
                          'e3': u'八', 'f': u'九', 'g': u'十',
                          'h': u'十一', 'i': u'十二', 'j': u'十三', 'k': u'十四'}
        return mdtitledict, mdtitletotitle

    @staticmethod
    def gethtmltitledict():
        htmltitlelist = [{'key': 'a', 'val': u'1、燃气轮机发电机组'}, 
                         {'key': 'c', 'val': u'2、余热锅炉'}, 
                         {'key': 'c1', 'val': u'3、余热锅炉辅机'},
                         {'key': 'b', 'val': u'4、汽轮发电机组及辅助设备'}, 
                         {'key': 'd', 'val': u'5、分散控制系统'}, 
                         {'key': 'e1', 'val': u'6、水系统'},
                         {'key': 'e2', 'val': u'7、消防水系统'}, 
                         {'key': 'e3', 'val': u'8、废水处理系统'}, 
                         {'key': 'f', 'val': u'9、循环水冷却系统'},
                         {'key': 'g', 'val': u'10、厂用/仪表用压缩空气系统'}, 
                         {'key': 'h', 'val': u'11、往复式发动机发电机组'}, 
                         {'key': 'i', 'val': u'12、电气设备'}, 
                         {'key': 'j', 'val': u'13、实验室设备'}, 
                         {'key': 'k', 'val': u'14、其它设备'}]
        return htmltitlelist

    @staticmethod
    def saveEquipmentList(uidData, nameData, typeData, contentData, unitData, countData, remarkData):
        Equipment = None
        try:
            Equipment = EquipmentListTemplate.search_EquipmentListTemplate(Module.CCPP)

            uidElementArray = uidData.split('&')
            uidElementList = []
            for formElement in uidElementArray:
                uidElementList.append(formElement.split('='))

            nameElementArray = nameData.split('&')
            nameElementList = []
            for formElement in nameElementArray:
                nameElementList.append(formElement.split('='))

            typeElementArray = typeData.split('&')
            typeElementList = []
            for formElement in typeElementArray:
                typeElementList.append(formElement.split('='))

            contenteElementArray = contentData.split('&')
            contentElementList = []
            for formElement in contenteElementArray:
                contentElementList.append(formElement.split('='))

            unitElementArray = unitData.split('&')
            unitElementList = []
            for formElement in unitElementArray:
                unitElementList.append(formElement.split('='))

            countElementArray = countData.split('&')
            countElementList = []
            for formElement in countElementArray:
                countElementList.append(formElement.split('='))

            remarkElementArray = remarkData.split('&')
            remarkElementList = []
            for formElement in remarkElementArray:
                remarkElementList.append(formElement.split('='))

            decode_equipment_uid_list = []
            decode_equipment_name_list = []
            decode_equipment_type_list = []
            decode_equipment_content_list = []
            decode_equipment_unit_list = []
            decode_equipment_count_list = []
            decode_equipment_remark_list = []

            for index in range(len(uidElementList)):
                equipment_uid_value = uidElementList[index][1]
                decode_equipment_uid_value = urllib.unquote(str(equipment_uid_value)).decode('utf-8')
                decode_equipment_uid_list.append(decode_equipment_uid_value)

            for index in range(len(nameElementList)):
                equipment_name_value = nameElementList[index][1]
                decode_equipment_name_value = urllib.unquote(str(equipment_name_value)).decode('utf-8')
                decode_equipment_name_list.append(decode_equipment_name_value)

            for index in range(len(typeElementList)):
                equipment_type_value = typeElementList[index][1]
                decode_equipment_type_value = urllib.unquote(str(equipment_type_value)).decode('utf-8')
                decode_equipment_type_list.append(decode_equipment_type_value)
            
            for index in range(len(contentElementList)):
                equipment_content_value = contentElementList[index][1]
                decode_equipment_content_value = urllib.unquote(str(equipment_content_value)).decode('utf-8')
                decode_equipment_content_list.append(decode_equipment_content_value)

            for index in range(len(unitElementList)):
                equipment_unit_value = unitElementList[index][1]
                decode_equipment_unit_value = urllib.unquote(str(equipment_unit_value)).decode('utf-8')
                decode_equipment_unit_list.append(decode_equipment_unit_value)

            for index in range(len(countElementList)):
                equipment_count_value = countElementList[index][1]
                decode_equipment_count_value = urllib.unquote(str(equipment_count_value)).decode('utf-8')
                decode_equipment_count_list.append(decode_equipment_count_value)
            
            for index in range(len(remarkElementList)):
                equipment_remark_value = remarkElementList[index][1]
                decode_equipment_remark_value = urllib.unquote(str(equipment_remark_value)).decode('utf-8')
                decode_equipment_remark_list.append(decode_equipment_remark_value)

            equipment_json = json.loads(Equipment.equipment_template)
            equipment_json[u'equipment_uid'] = decode_equipment_uid_list
            equipment_json[u'equipment_name'] = decode_equipment_name_list
            equipment_json[u'equipment_type'] = decode_equipment_type_list
            equipment_json[u'equipment_content'] = decode_equipment_content_list
            equipment_json[u'equipment_unit'] = decode_equipment_unit_list
            equipment_json[u'equipment_count'] = decode_equipment_count_list
            equipment_json[u'equipment_remark'] = decode_equipment_remark_list

            Equipment.equipment_template = json.dumps(equipment_json)
            EquipmentListTemplate.insert_EquipmentListTemplate(Equipment)
        except Exception:
            Equipment = None
            return Equipment
        else:
            return Equipment

