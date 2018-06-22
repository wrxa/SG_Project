# -*- coding: utf-8 -*-
from app.main.service.turbine import turbine_calculation01cn, turbine_calculation11by, turbine_calculation11cn, \
                                     turbine_calculation01by, turbine_calculation02cn, turbine_calculation02by, \
                                     turbine_calculation03cn, turbine_calculation03by, turbine_calculation12cn, \
                                     turbine_calculation12by, turbine_calculation13cn, turbine_calculation13by, \
                                     turbine_calculation21cn, turbine_calculation21by, turbine_calculation22cn, \
                                     turbine_calculation22by, turbine_calculation23cn, turbine_calculation23by, \
                                     turbine_calculation01bn, turbine_calculation02bn, turbine_calculation03bn, \
                                     turbine_calculation11bn, turbine_calculation12bn, turbine_calculation13bn, \
                                     turbine_calculation21bn, turbine_calculation22bn, turbine_calculation23bn


class Factory():
    def execute(self, dbobj, form):
        s_hh_grade = float(dbobj.s_hh_grade)
        s_lh_grade = float(dbobj.s_lh_grade)
        # 数据库的汽轮机类型
        s_steam_type_test = float(dbobj.s_steam_type_test)
        # 页面上的汽轮机类型
        s_steam_type_test_from = form.get('s_steam_type_test')       
        
        # s_steam_type_test == '1':抽凝 s_steam_type_test == '2':背压 s_steam_type_test == '3':补凝
        if s_steam_type_test == 1 and s_hh_grade == 0 and s_lh_grade == 1:
            result = turbine_calculation01cn.Turbine_EXEC().specialCalculation(dbobj, form)

            # 如果汽轮机类型被变更，需要重新输入页面上的必需值后，再做sortPressure计算
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None

            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 1 and s_hh_grade == 0 and s_lh_grade == 2:
            result = turbine_calculation02cn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None

            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 1 and s_hh_grade == 0 and s_lh_grade == 3:
            result = turbine_calculation03cn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None

            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 1 and s_hh_grade == 1 and s_lh_grade == 1:
            result = turbine_calculation11cn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 1 and s_hh_grade == 1 and s_lh_grade == 2:
            result = turbine_calculation12cn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 1 and s_hh_grade == 1 and s_lh_grade == 3:
            result = turbine_calculation13cn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 1 and s_hh_grade == 2 and s_lh_grade == 1:
            result = turbine_calculation21cn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 1 and s_hh_grade == 2 and s_lh_grade == 2:
            result = turbine_calculation22cn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 1 and s_hh_grade == 2 and s_lh_grade == 3:
            result = turbine_calculation23cn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
                       
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 0 and s_lh_grade == 1:
            result = turbine_calculation01by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 0 and s_lh_grade == 2:
            result = turbine_calculation02by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 0 and s_lh_grade == 3:
            result = turbine_calculation03by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 1 and s_lh_grade == 1:
            result = turbine_calculation11by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 1 and s_lh_grade == 2:
            result = turbine_calculation12by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 1 and s_lh_grade == 3:
            result = turbine_calculation13by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 2 and s_lh_grade == 1:
            result = turbine_calculation21by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 2 and s_lh_grade == 2:
            result = turbine_calculation22by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 2 and s_hh_grade == 2 and s_lh_grade == 3:
            result = turbine_calculation23by.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
               
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)

        elif s_steam_type_test == 3 and s_hh_grade == 0 and s_lh_grade == 1:
            result = turbine_calculation01bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None

            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 0 and s_lh_grade == 2:
            result = turbine_calculation02bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
             
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 0 and s_lh_grade == 3:
            result = turbine_calculation03bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
             
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 1 and s_lh_grade == 1:
            result = turbine_calculation11bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
             
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 1 and s_lh_grade == 2:
            result = turbine_calculation12bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
             
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 1 and s_lh_grade == 3:
            result = turbine_calculation13bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
             
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 2 and s_lh_grade == 1:
            result = turbine_calculation21bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
             
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 2 and s_lh_grade == 2:
            result = turbine_calculation22bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
             
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 2 and s_lh_grade == 3:
            result = turbine_calculation23bn.Turbine_EXEC().specialCalculation(dbobj, form)
            if float(s_steam_type_test) != float(s_steam_type_test_from):
                result.i_exhaust_point_flow = None
             
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)

        else:
            return 0, dbobj
            print("输入有误！！！！！！！！！！！！！！！")

    def executePlanlist(self, dbobj):
        result = None
        s_hh_grade = dbobj.s_hh_grade
        # form.get('s_hh_grade')
        s_lh_grade = dbobj.s_lh_grade
        # form.get('s_lh_grade')
        s_steam_type_test = dbobj.s_steam_type_test
        # s_steam_type_test == '1':抽凝 s_steam_type_test == '2':背压
        if s_steam_type_test == 1 and s_hh_grade == 0 and s_lh_grade == 1:
            result = turbine_calculation01cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 1 and s_hh_grade == 0 and s_lh_grade == 2:
            result = turbine_calculation02cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 1 and s_hh_grade == 0 and s_lh_grade == 3:
            result = turbine_calculation03cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 1 and s_hh_grade == 1 and s_lh_grade == 1:
            result = turbine_calculation11cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 1 and s_hh_grade == 1 and s_lh_grade == 2:
            result = turbine_calculation12cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 1 and s_hh_grade == 1 and s_lh_grade == 3:
            result = turbine_calculation13cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 1 and s_hh_grade == 2 and s_lh_grade == 1:
            result = turbine_calculation21cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 1 and s_hh_grade == 2 and s_lh_grade == 2:
            result = turbine_calculation22cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 1 and s_hh_grade == 2 and s_lh_grade == 3:
            result = turbine_calculation23cn.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 0 and s_lh_grade == 1:
            result = turbine_calculation01by.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 0 and s_lh_grade == 2:
            result = turbine_calculation02by.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 0 and s_lh_grade == 3:
            result = turbine_calculation03by.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 1 and s_lh_grade == 1:
            result = turbine_calculation11by.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 1 and s_lh_grade == 2:
            result = turbine_calculation12by.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 1 and s_lh_grade == 3:
            result = turbine_calculation13by.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 2 and s_lh_grade == 1:
            result = turbine_calculation21by.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 2 and s_lh_grade == 2:
            result = turbine_calculation22by.Turbine_PlanList().specialCalculation(dbobj)
        elif s_steam_type_test == 2 and s_hh_grade == 2 and s_lh_grade == 3:
            result = turbine_calculation23by.Turbine_PlanList().specialCalculation(dbobj)
        
        elif s_steam_type_test == 3 and s_hh_grade == 0 and s_lh_grade == 1:
            result = turbine_calculation01bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 0 and s_lh_grade == 2:
            result = turbine_calculation02bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 0 and s_lh_grade == 3:
            result = turbine_calculation03bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 1 and s_lh_grade == 1:
            result = turbine_calculation11bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 1 and s_lh_grade == 2:
            result = turbine_calculation12bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 1 and s_lh_grade == 3:
            result = turbine_calculation13bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 2 and s_lh_grade == 1:
            result = turbine_calculation21bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 2 and s_lh_grade == 2:
            result = turbine_calculation22bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        elif s_steam_type_test == 3 and s_hh_grade == 2 and s_lh_grade == 3:
            result = turbine_calculation23bn.Turbine_PlanList().specialCalculation(dbobj)
            return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)
        else:
            result = dbobj
            print("汽轮机输入有误！！！！！！！！！！！！！！！")
        return sortPressure(result, 0, 2), sortPressure(result, result.i_exhaust_point_flow, 1)


def sortPressure(dbobj, point_flow, flg):

    if (dbobj.e_turbine_efficiency is not None and dbobj.e_turbine_efficiency != "") and \
        (dbobj.e_mechanical_efficiency is not None and dbobj.e_mechanical_efficiency != "") and \
        (dbobj.e_generator_efficiency is not None and dbobj.e_generator_efficiency != "") and \
        (dbobj.e_steam_pressure is not None and dbobj.e_steam_pressure != "") and \
        (dbobj.e_steam_temperature is not None and dbobj.e_steam_temperature != "") and \
        (dbobj.e_steam_flow is not None and dbobj.e_steam_flow != "") and \
        (dbobj.e_exhaust_point_pressure is not None and dbobj.e_exhaust_point_pressure != "") and \
        (dbobj.e_exhaust_point_temperature is not None and dbobj.e_exhaust_point_temperature != "") and \
        (dbobj.e_exhaust_point_flow is not None and dbobj.e_exhaust_point_flow != "") and \
        ((dbobj.e_steam_exhaust_pressure is not None and dbobj.e_steam_exhaust_pressure != "") or ((dbobj.e_backpressure_pressure is not None and dbobj.e_backpressure_pressure != "") and (dbobj.e_backpressure_temperature is not None and dbobj.e_backpressure_temperature != ""))) and \
        (dbobj.e_hot_data is not None and dbobj.e_hot_data != "") and \
        (dbobj.e_steam_water_loss is not None and dbobj.e_steam_water_loss != "") and \
        (dbobj.e_throttle_flow is not None and dbobj.e_throttle_flow != "") and \
        (dbobj.hh1_water_temperature is not None and dbobj.hh1_water_temperature != "") and \
        (dbobj.i_steam_flow is not None and dbobj.i_steam_flow != "") and \
        (dbobj.h_temperature is not None and dbobj.h_temperature != "") and \
        (point_flow is not None and point_flow != ""):
        # 按照压力排序（从大到小）
        dict_group_check = [
            {
            'index': float(dbobj.i_high1_pressure) if dbobj.i_high1_pressure else 0,
            'pressure': dbobj.i_high1_pressure,
            'i_high1_entropy': dbobj.i_high1_entropy,
            'i_high1_temperature': dbobj.i_high1_temperature,
            'enthalpy': dbobj.i_high1_enthalpy,
            'flow': dbobj.i_high1_flow,
            'power': dbobj.i_steam_hh1_power},

            {'index': float(dbobj.i_high2_pressure) if dbobj.i_high2_pressure else 0,
            'pressure': dbobj.i_high2_pressure,
            'i_high2_entropy': dbobj.i_high2_entropy,
            'i_high2_temperature': dbobj.i_high2_temperature,
            'enthalpy': dbobj.i_high2_enthalpy,
            'flow': dbobj.i_high2_flow,
            'power': dbobj.i_hh1_hh2_power},

            {'index': float(dbobj.i_deoxidize_pressure) if dbobj.i_deoxidize_pressure else 0,
            'pressure': dbobj.i_deoxidize_pressure,
            'i_deoxidize_entropy': dbobj.i_deoxidize_entropy,
            'i_deoxidize_temperature': dbobj.i_deoxidize_temperature,
            'enthalpy': dbobj.i_deoxidize_enthalpy,
            'flow': dbobj.i_deoxidize_flow,
            'power': dbobj.i_hh2_deoxidize_power},

            {'index': float(dbobj.i_exhaust_point_pressure) if dbobj.i_exhaust_point_pressure else 0,
            'pressure': dbobj.i_exhaust_point_pressure,
            'i_exhaust_point_temperature': dbobj.i_exhaust_point_temperature,
            'i_exhaust_point_entropy': dbobj.i_exhaust_point_entropy,
            'enthalpy': dbobj.i_exhaust_point_enthalpy,
            #'flow': dbobj.i_exhaust_point_flow,
            'flow': point_flow,
            'power': dbobj.i_deoxidize_exhaust_power},

            {'index': float(dbobj.i_low1_pressure) if dbobj.i_low1_pressure else 0,
            'pressure': dbobj.i_low1_pressure,
            'i_low1_entropy': dbobj.i_low1_entropy,
            'i_low1_temperature': dbobj.i_low1_temperature,
            'enthalpy': dbobj.i_low1_enthalpy,
            'flow': dbobj.i_low1_flow,
            'power': dbobj.i_exhaust_lh1_power},

            {'index': float(dbobj.i_low2_pressure) if dbobj.i_low2_pressure else 0,
            'pressure': dbobj.i_low2_pressure,
            'i_low2_entropy': dbobj.i_low2_entropy,
            'i_low2_temperature': dbobj.i_low2_temperature,
            'enthalpy': dbobj.i_low2_enthalpy,
            'flow': dbobj.i_low2_flow,
            'power': dbobj.i_lh1_lh2_power},

            {'index': float(dbobj.i_low3_pressure) if dbobj.i_low3_pressure else 0,
            'pressure': dbobj.i_low3_pressure,
            'i_low3_entropy': dbobj.i_low3_entropy,
            'i_low3_temperature': dbobj.i_low3_temperature,
            'enthalpy': dbobj.i_low3_enthalpy,
            'flow': dbobj.i_low3_flow,
            'power': dbobj.i_lh2_lh3_power}
        ]
        
        array_group_check = []
        for item in dict_group_check:
            if not (item['index'] is None or item['index'] == '' or item['index'] == 0):
                array_group_check.append(item)

        array_group_check.sort(cmp=lambda x, y: cmp(y['index'], x['index']))
        constant_eff = float(dbobj.i_turbine_efficiency) * float(dbobj.i_mechanical_efficiency) * float(dbobj.i_generator_efficiency) / 3.6
        array_group_check[0]['power'] = float(dbobj.i_steam_flow) * (float(dbobj.i_steam_enthalpy) - float(array_group_check[0]['enthalpy']) ) * constant_eff
        test(array_group_check[0], dbobj)
        length_array = len(array_group_check)

        for i in range(1, length_array):
            sigma_flow = 0
            for j in range(0, i):
                sigma_flow = sigma_flow + float(array_group_check[j]['flow'])
            array_group_check[i]['power'] = (float(dbobj.i_steam_flow) - sigma_flow) * (float(array_group_check[i - 1]['enthalpy']) - float(array_group_check[i]['enthalpy'])) * constant_eff
            test(array_group_check[i], dbobj)

        dbobj.i_steam_exhaust_enthalpy_actual = float(array_group_check[length_array - 1]['enthalpy']) - (float(array_group_check[length_array - 1]['enthalpy']) - float(dbobj.i_steam_exhaust_enthalpy)) * float(dbobj.i_turbine_efficiency)
        # dbobj.i_steam_exhaust_flow = float(dbobj.i_steam_flow) - sigma_flow - float(array_group_check[length_array - 1]['flow']) + float(point_flow) * 2
        dbobj.i_steam_exhaust_flow = float(dbobj.i_steam_flow) - sigma_flow - float(array_group_check[length_array - 1]['flow']) 
        dbobj.i_lh2_steam_power = (float(dbobj.i_steam_flow) - sigma_flow - float(array_group_check[length_array - 1]['flow'])) * (float(array_group_check[length_array - 1]['enthalpy']) - float(dbobj.i_steam_exhaust_enthalpy_actual)) * constant_eff

        sigma_power = 0
        for i in range(0, length_array):
            sigma_power = sigma_power + float(array_group_check[i]['power'])    

        # 总功率
        if flg == 2:
            total_power0 = sigma_power + dbobj.i_lh2_steam_power
        else:
            dbobj.i_total_power = sigma_power + dbobj.i_lh2_steam_power
        # 计算误差
        if flg == 1 and dbobj.e_steam_extraction_select != 0.0:
            dbobj.i_calculation_error = (dbobj.i_total_power - dbobj.e_steam_extraction_select * 1000)/dbobj.e_steam_extraction_select/1000

        front_page_list = []
        for item in array_group_check:
            front_page_list.append(item.keys())
        if flg == 2:
            return total_power0
        else:
            return dbobj
    else:
        if flg == 2:
            return 0
        else:
            return dbobj

def test(ele, result):
    if 'i_high1_entropy' in ele:
        result.i_steam_hh1_power = ele['power']
    elif 'i_high2_entropy' in ele:
        result.i_hh1_hh2_power = ele['power']
    elif 'i_deoxidize_entropy' in ele:
        result.i_hh2_deoxidize_power = ele['power']
    elif 'i_exhaust_point_entropy' in ele:
        result.i_deoxidize_exhaust_power = ele['power']
    elif 'i_low1_entropy' in ele:
        result.i_exhaust_lh1_power = ele['power']
    elif 'i_low2_entropy' in ele:
        result.i_lh1_lh2_power = ele['power']
    elif 'i_low3_entropy' in ele:
        result.i_lh2_lh3_power = ele['power']

