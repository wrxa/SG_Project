# -*- coding: utf-8 -*-
from app.ccpp.models.constantModel import CcppConstant
from app.models import Plan
from app.ccpp.models.ccpp_turbineModel import CcppTurbine
from app.ccpp import gl
from datetime import datetime
from app import db
from app.main.service.turbine import turbine_foctory


list_column_turbine = [
    'e_turbine_efficiency',
    'e_mechanical_efficiency', 'e_generator_efficiency',
    'e_steam_pressure', 'e_steam_temperature', 'e_steam_flow',
    'e_steam_entropy', 'e_steam_enthalpy', 'e_exhaust_point_pressure',
    'e_exhaust_point_temperature', 'e_exhaust_point_entropy',
    'e_exhaust_point_enthalpy', 'e_exhaust_point_flow',
    'e_exhaust_after_steam', 'e_exhaust_after_pressure',
    'e_exhaust_after_enthalpy', 'e_exhaust_after_entropy',
    'e_steam_exhaust_pressure', 'e_steam_exhaust_enthalpy',
    'e_backpressure_pressure', 'e_backpressure_temperature',
    'e_backpressure_enthalpy', 'e_backpressure_flow', 'e_gross_generation',
    'e_hot_data', 'e_steam_extraction', 'e_steam_extraction_select',
    'e_steam_water_loss', 'e_throttle_flow', 'h_temperature',
    'h_pressure', 'h_enthalpy', 'h_amount', 'hh1_water_temperature',
    'hh1_water_enthalpy', 'hh1_top_difference',
    'hh1_saturated_water_temperature', 'hh1_saturated_water_enthalpy',
    'hh1_work_pressure', 'hh1_pressure_loss', 'hh1_extraction_pressure',
    'hh1_extraction_enthalpy', 'hh1_extraction_amount',
    'hh2_water_temperature', 'hh2_water_enthalpy', 'hh2_top_difference',
    'hh2_saturated_water_temperature', 'hh2_saturated_water_enthalpy',
    'hh2_work_pressure', 'hh2_pressure_loss', 'hh2_extraction_pressure',
    'hh2_extraction_enthalpy', 'hh2_extraction_amount',
    'hh3_water_temperature', 'hh3_water_enthalpy', 'hh3_top_difference',
    'hh3_saturated_water_temperature', 'hh3_saturated_water_enthalpy',
    'hh3_work_pressure', 'hh3_pressure_loss', 'hh3_extraction_pressure',
    'hh3_extraction_enthalpy', 'hh3_extraction_amount', 'd_water_temperature',
    'd_water_enthalpy', 'd_work_pressure', 'd_pressure_loss',
    'd_extraction_pressure', 'd_extraction_enthalpy', 'd_extraction_amount',
    'lh1_water_temperature', 'lh1_water_enthalpy', 'lh1_top_difference',
    'lh1_saturated_water_temperature', 'lh1_saturated_water_enthalpy',
    'lh1_work_pressure', 'lh1_pressure_loss', 'lh1_extraction_pressure',
    'lh1_extraction_enthalpy', 'lh1_extraction_amount',
    'lh2_water_temperature', 'lh2_water_enthalpy', 'lh2_top_difference',
    'lh2_saturated_water_temperature', 'lh2_saturated_water_enthalpy',
    'lh2_work_pressure', 'lh2_pressure_loss', 'lh2_extraction_pressure',
    'lh2_extraction_enthalpy', 'lh2_extraction_amount',
    'lh3_water_temperature', 'lh3_water_enthalpy', 'lh3_top_difference',
    'lh3_saturated_water_temperature', 'lh3_saturated_water_enthalpy',
    'lh3_work_pressure', 'lh3_pressure_loss', 'lh3_extraction_pressure',
    'lh3_extraction_enthalpy', 'lh3_extraction_amount', 'c_water_temperature',
    'c_water_enthalpy', 'c_work_pressure', 'c_pressure_loss',
    'c_extraction_pressure', 'c_extraction_enthalpy', 'c_extraction_amount',
    'i_turbine_efficiency', 'i_mechanical_efficiency',
    'i_generator_efficiency', 'i_steam_pressure', 'i_steam_temperature',
    'i_steam_flow', 'i_steam_entropy', 'i_steam_enthalpy', 'i_high1_pressure',
    'i_high1_entropy', 'i_high1_temperature', 'i_high1_enthalpy',
    'i_high1_flow', 'i_steam_hh1_power', 'i_high2_pressure', 'i_high2_entropy',
    'i_high2_temperature', 'i_high2_enthalpy', 'i_high2_flow',
    'i_hh1_hh2_power', 'i_deoxidize_pressure', 'i_deoxidize_entropy',
    'i_deoxidize_temperature', 'i_deoxidize_enthalpy', 'i_deoxidize_flow',
    'i_hh2_deoxidize_power', 'i_exhaust_point_pressure',
    'i_exhaust_point_temperature', 'i_exhaust_point_entropy',
    'i_exhaust_point_enthalpy', 'i_exhaust_point_flow',
    'i_deoxidize_exhaust_power', 'i_low1_pressure', 'i_low1_entropy',
    'i_low1_temperature', 'i_low1_enthalpy', 'i_low1_flow',
    'i_exhaust_lh1_power', 'i_low2_pressure', 'i_low2_entropy',
    'i_low2_temperature', 'i_low2_enthalpy', 'i_low2_flow', 'i_lh1_lh2_power',
    'i_steam_exhaust_pressure', 'i_steam_exhaust_entropy',
    'i_steam_exhaust_enthalpy', 'i_steam_exhaust_enthalpy_actual',
    'i_steam_exhaust_enthalpy_steam', 'i_steam_exhaust_enthalpy_water',
    'i_steam_exhaust_dry', 'i_steam_exhaust_flow', 'i_lh2_steam_power',
    'i_total_power', 'i_calculation_error', 'e_steam_plus_enthalpy'
]
list_column_steamClear = [
    # 'i_turbine_efficiency',
    # 'i_mechanical_efficiency',
    # 'i_generator_efficiency',
    # 'i_steam_pressure',
    # 'i_steam_temperature',
    # 'i_steam_flow',
    'i_steam_entropy',
    'i_steam_enthalpy',
    'i_high1_pressure',
    'i_high1_entropy',
    'i_high1_temperature',
    'i_high1_enthalpy',
    'i_high1_flow',
    'i_steam_hh1_power',
    'i_high2_pressure',
    'i_high2_entropy',
    'i_high2_temperature',
    'i_high2_enthalpy',
    'i_high2_flow',
    'i_hh1_hh2_power',
    'i_deoxidize_pressure',
    'i_deoxidize_entropy',
    'i_deoxidize_temperature',
    'i_deoxidize_enthalpy',
    'i_deoxidize_flow',
    'i_hh2_deoxidize_power',
    'i_exhaust_point_pressure',
    'i_exhaust_point_temperature',
    'i_exhaust_point_entropy',
    'i_exhaust_point_enthalpy',
    'i_exhaust_point_flow',
    'i_deoxidize_exhaust_power',
    'i_low1_pressure',
    'i_low1_entropy',
    'i_low1_temperature',
    'i_low1_enthalpy',
    'i_low1_flow',
    'i_exhaust_lh1_power',
    'i_low2_pressure',
    'i_low2_entropy',
    'i_low2_temperature',
    'i_low2_enthalpy',
    'i_low2_flow',
    'i_lh1_lh2_power',
    'i_low3_pressure',
    'i_low3_entropy',
    'i_low3_temperature',
    'i_low3_enthalpy',
    'i_low3_flow',
    'i_lh2_lh3_power',
    'i_steam_exhaust_pressure',
    'i_steam_exhaust_entropy',
    'i_steam_exhaust_enthalpy',
    'i_steam_exhaust_enthalpy_actual',
    'i_steam_exhaust_enthalpy_steam',
    'i_steam_exhaust_enthalpy_water',
    'i_steam_exhaust_dry',
    'i_steam_exhaust_flow',
    'i_lh2_steam_power',
    'i_total_power',
    'i_calculation_error'
]


class CcppTurbineService():

    '''
    加载字段常量数据
    '''
    @staticmethod
    def getTurbineConstant():
        ccppConstant = CcppConstant.search_ccppConstant('ccpp_Turbine')
        gl.listsort(ccppConstant)
        return ccppConstant

    def to_steam(self, form, plan_id):
        steam = CcppTurbine.query.filter_by(
            plan_id=plan_id).first()

        # if getattr(steam, 's_parameter_flg') == '1':
        for index in range(len(list_column_turbine)):
            if list_column_turbine[index] != 'hh1_water_temperature':
                if form.get(list_column_turbine[index]) != '':
                    setattr(steam, list_column_turbine[index],
                            form.get(list_column_turbine[index]))
                else:
                    setattr(steam, list_column_turbine[index],
                            None)
        # 清理页面上的旧记录
        for index in range(len(list_column_steamClear)):
            setattr(steam, list_column_steamClear[index],
                    None)
        
        if form.get('s_temperature_pressure') != "" and form.get('s_temperature_pressure') is not None:
            setattr(steam, 's_temperature_pressure', form.get('s_temperature_pressure'))
            setattr(steam, 's_hh_grade', form.get('s_hh_grade'))
            setattr(steam, 's_lh_grade', form.get('s_lh_grade'))

            # 汽轮机类型没有变更
            if getattr(steam, 's_steam_type_test') is None:
                setattr(steam, 's_steam_type_test', form.get('s_steam_type_test'))
            else:
                if float(form.get('s_steam_type_test')) == float(getattr(steam, 's_steam_type_test')):
                    setattr(steam, 's_steam_type_test', form.get('s_steam_type_test'))

        setattr(steam, 'e_steam_type', form.get('e_steam_type'))
        setattr(steam, 'h_assume', form.get('h_assume'))
        pointPower = None
        if form.get('tubineparahtml') != 'tubineparahtml':
            pointPower, steam = turbine_foctory.Factory().execute(steam, form)

        # 汽轮机类型变更
        if getattr(steam, 's_steam_type_test') is not None:
            if float(form.get('s_steam_type_test')) != float(getattr(steam, 's_steam_type_test')):
                setattr(steam, 's_steam_type_test', form.get('s_steam_type_test'))

        return pointPower, steam

    # 根据plan_id删除实体
    def deletebyPlanId(self, plan_id):
        Turbine = CcppTurbine.search_CcppTurbine(plan_id)
        db.session.delete(Turbine)

    def to_TurbineJson(self, ccppTurbine):
        datas = {}
        for index in range(len(list_column_turbine)):
            if list_column_turbine[index] == 'e_steam_exhaust_pressure' or list_column_turbine[index] == 'c_work_pressure':
                datas[list_column_turbine[index]] = gl.format_value2(
                # TODO还未过滤特殊字符项
                "number", str(getattr(ccppTurbine, list_column_turbine[index])))
            else:
                datas[list_column_turbine[index]] = gl.format_value(getattr(ccppTurbine, list_column_turbine[index]))
        datas['e_steam_type'] = getattr(ccppTurbine, 'e_steam_type')
        datas['h_assume'] = getattr(ccppTurbine, 'h_assume')
        datas['s_parameter_flg'] = getattr(ccppTurbine, 's_parameter_flg')
        datas['s_steam_type_test'] = getattr(ccppTurbine, 's_steam_type_test')
        datas['s_temperature_pressure'] = getattr(ccppTurbine, 's_temperature_pressure')
        datas['s_hh_grade'] = getattr(ccppTurbine, 's_hh_grade')
        datas['s_lh_grade'] = getattr(ccppTurbine, 's_lh_grade')
        return datas

    # 清理汽轮机旧记录
    def steamClear(self, plan_id):
        steam = CcppTurbine.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_steamClear)):
            setattr(steam, list_column_steamClear[index],
                    None)
        return steam
    
    def to_TurbineData(self, form, plan_id):
        ccppTurbine = CcppTurbine.query.filter_by(
            plan_id=plan_id).first()
        if ccppTurbine.s_parameter_flg != '1':
            # 第一次进入需要将数据的字段传入
            list_column_turbine.remove('e_steam_pressure')
            list_column_turbine.remove('e_steam_temperature')
            list_column_turbine.remove('e_steam_flow')
        for index in range(len(list_column_turbine)):
            if form.get(list_column_turbine[index]) != '' and form.get(list_column_turbine[index]) is not None:
                setattr(ccppTurbine, list_column_turbine[index],
                        form.get(list_column_turbine[index]))
            else:
                setattr(ccppTurbine, list_column_turbine[index],
                        None)
        setattr(ccppTurbine, 'plan_id', plan_id)

        if form.get('s_temperature_pressure') != "" and form.get('s_temperature_pressure') is not None:
            setattr(ccppTurbine, 's_temperature_pressure', form.get('s_temperature_pressure'))
            setattr(ccppTurbine, 's_hh_grade', form.get('s_hh_grade'))
            setattr(ccppTurbine, 's_lh_grade', form.get('s_lh_grade'))
            setattr(ccppTurbine, 's_steam_type_test', form.get('s_steam_type_test'))
        setattr(ccppTurbine, 'e_steam_type', form.get('e_steam_type'))
        setattr(ccppTurbine, 'h_assume', form.get('h_assume'))
        # 第一次进入需要将数据的字段传入
        if ccppTurbine.s_parameter_flg != '1':
            list_column_turbine.append('e_steam_pressure')
            list_column_turbine.append('e_steam_temperature')
            list_column_turbine.append('e_steam_flow')
        return ccppTurbine

    def getDataByPlanId(self, plan_id):
        ccppTurbine = CcppTurbine.query.filter_by(
            plan_id=plan_id).first()
        # for index in range(len(list_column_turbine)):
        #     if hasattr(ccppTurbine, list_column_turbine[index]):
        #         var = getattr(ccppTurbine, list_column_turbine[index])
        #         setattr(ccppTurbine, list_column_turbine[index], gl.format_value(var))
        return ccppTurbine

    def update_plan_date(self, plan_id):
        plan = Plan.query.filter_by(id=plan_id).first()
        plan.plan_update_date = datetime.now()
        Plan.insert_plan(plan)

    @staticmethod
    def sortPressure(steamturbine):
        dict_group_check = [
            [float(steamturbine.i_high1_pressure) if steamturbine.i_high1_pressure else 0,
                'i_high1_pressure',
                'i_high1_entropy',
                'i_high1_temperature',
                'i_high1_enthalpy',
                'i_high1_flow',
                'i_steam_hh1_power',
                'HH1',
                u'1#高压'],

            [float(steamturbine.i_high2_pressure) if steamturbine.i_high2_pressure else 0,
                'i_high2_pressure',
                'i_high2_entropy',
                'i_high2_temperature',
                'i_high2_enthalpy',
                'i_high2_flow',
                'i_hh1_hh2_power',
                'HH2',
                u'2#高压'],

            [float(steamturbine.i_deoxidize_pressure) if steamturbine.i_deoxidize_pressure else 0,
                'i_deoxidize_pressure',
                'i_deoxidize_entropy',
                'i_deoxidize_temperature',
                'i_deoxidize_enthalpy',
                'i_deoxidize_flow',
                'i_hh2_deoxidize_power',
                'D',
                u'D除氧'],

            [float(steamturbine.i_exhaust_point_pressure) if steamturbine.i_exhaust_point_pressure else 0,
                'i_exhaust_point_pressure',
                'i_exhaust_point_temperature',
                'i_exhaust_point_entropy',
                'i_exhaust_point_enthalpy',
                'i_exhaust_point_flow',
                'i_deoxidize_exhaust_power',
                u'抽汽点',
                u'抽汽点'],

            [float(steamturbine.i_low1_pressure) if steamturbine.i_low1_pressure else 0,
                'i_low1_pressure',
                'i_low1_entropy',
                'i_low1_temperature',
                'i_low1_enthalpy',
                'i_low1_flow',
                'i_exhaust_lh1_power',
                'LH1',
                u'1#低加'],

            [float(steamturbine.i_low2_pressure) if steamturbine.i_low2_pressure else 0,
                'i_low2_pressure',
                'i_low2_entropy',
                'i_low2_temperature',
                'i_low2_enthalpy',
                'i_low2_flow',
                'i_lh1_lh2_power',
                'LH2',
                u'2#低加'],

            [float(steamturbine.i_low3_pressure) if steamturbine.i_low3_pressure else 0,
                'i_low3_pressure',
                'i_low3_entropy',
                'i_low3_temperature',
                'i_low3_enthalpy',
                'i_low3_flow',
                'i_lh2_lh3_power',
                'LH3',
                u'3#低加']
        ]

        array_group_check = []
        for item in dict_group_check:
            if not (item[0] is None or item[0] == '' or item[0] == 0):
                array_group_check.append(item)

        array_group_check.sort(cmp=lambda x, y: cmp(y[0], x[0]))

        for item in array_group_check:
            if array_group_check.index(item) == 0:
                item.append(u'主蒸汽至' + item[len(item) - 2] + u'功率')
            else:
                titleFrom = array_group_check[array_group_check.index(item) - 1][len(item) - 2]
                titleTo = item[len(item) - 2]

                if steamturbine.s_steam_type_test == 3:
                    if titleFrom.find(u"抽汽点") != -1:
                        titleFrom = titleFrom.replace(u"抽汽点", u"补汽点")
                    if titleTo.find(u"抽汽点") != -1:
                        titleTo = titleTo.replace(u"抽汽点", u"补汽点")
                
                # item.append(u'' + array_group_check[array_group_check.index(item) - 1][len(item) - 2] + u'至' + item[len(item) - 2] + u'功率')
                item.append(u'' + titleFrom + u'至' + titleTo + u'功率')

        front_page_list = []
        for item in array_group_check:
            front_page_list.append(item)
        return array_group_check
