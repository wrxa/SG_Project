# -*- coding:UTF-8 -*-
import sys
from imgInfoModel import ImageInfo
from app.coal_chp.model.coalchpModels import CoalCHPFurnaceCalculation, \
     CoalCHPCoalHandingSystem, CoalCHPSmokeAirSystem, \
     CoalCHPBoilerAuxiliaries, CoalCHPTurbineBackpressure, \
     CoalCHPCirculatingWater, CoalCHPChemicalWater, \
     CoalCHPRemovalAshSlag


# 格式化数据库取出的值
def format_value(flag, values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if not values or values == "null" or values == "None":
        result = ""
    elif values == "0":
        result = "0"
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        result = round(float(str(float(values)).rstrip('0')), 3)
    else:
        result = values
    return str(result)


class GetimgInfoList():
    def searchImgData(self, plan_id):
        furnaceCalculation = CoalCHPFurnaceCalculation.search_furnace_calculation(
            plan_id)
        handingSystem = CoalCHPCoalHandingSystem.search_handing_system(plan_id)
        smokeAirSystem = CoalCHPSmokeAirSystem.search_smoke_air_system(plan_id)
        boilerAuxiliaries = CoalCHPBoilerAuxiliaries.search_boiler_auxiliaries(
            plan_id)
        turbineBackpressure = CoalCHPTurbineBackpressure.search_turbineBackpressure(
            plan_id)
        circulatingWater = CoalCHPCirculatingWater.search_circulating_water(
            plan_id)
        removalAshSlag = CoalCHPRemovalAshSlag.search_removal_ash_slag(plan_id)
        chemicalWater = CoalCHPChemicalWater.search_chemical_water(plan_id)
        funcName = sys._getframe().f_back.f_code.co_name
        if funcName == "rl_p1_a_List" or funcName == "rl_p1_b_List":
            return handingSystem
        if funcName == "p1_cfb_dry_List" or funcName == "p2_cfb_wet_List":
            return furnaceCalculation, smokeAirSystem
        if funcName in ["p1_a_List", "p1_b_List", "p2_a_List", "p2_b_List", "p3_a_List", "p3_b_List", "p4_a_List", "p4_b_List", "p5_a_List", "p5_b_List"]:
            return furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater
        if funcName == "p1_chemical_List" or funcName == "p2_chemical_List":
            return chemicalWater
        if funcName == "p_ash_List" or funcName == "p_slag_List":
            return removalAshSlag

    def rl_p1_a_List(self, plan_id):
        handingSystem = GetimgInfoList().searchImgData(plan_id)
        return [
            # F27 有效容积-计算e_effective_cubage_calculated_design
            ImageInfo(
                '0', (934, 2945),
                format_value(
                    "number",
                    str(handingSystem.e_effective_cubage_calculated_design)) +
                u" m³", 50),
            # F53 带宽s_belt_width_design
            ImageInfo(
                '0', (6447, 2217),
                format_value("number", str(handingSystem.s_belt_width_design))
                + u" mm", 50),
            # F55 带速s_belt_speed_design
            ImageInfo(
                '0', (6449, 2349),
                format_value("number", str(handingSystem.s_belt_speed_design))
                + u" m/s", 50),
            # F55 带速s_belt_speed_design
            ImageInfo(
                '0', (7563, 3341),
                format_value("number", str(handingSystem.s_belt_speed_design))
                + u" m/s", 50),
            # F53 带宽s_belt_width_design
            ImageInfo(
                '0', (7565, 3211),
                format_value("number", str(handingSystem.s_belt_width_design))
                + u" mm", 50),
            # F22 煤场面积c_coalyard_area_design
            ImageInfo('0', (7803, 1485),
                      format_value("number",
                                   str(handingSystem.c_coalyard_area_design)) +
                      u" m²", 50),
            # F15 煤的储备日数c_coal_store_days_design
            ImageInfo('0', (7875, 1593),
                      format_value("number",
                                   str(handingSystem.c_coal_store_days_design))
                      + u" 天", 50)
        ]

    def rl_p1_b_List(self, plan_id):
        handingSystem = GetimgInfoList().searchImgData(plan_id)
        return [
            # F27 有效容积-计算e_effective_cubage_calculated_design
            ImageInfo(
                '0', (914, 2942),
                format_value(
                    "number",
                    str(handingSystem.e_effective_cubage_calculated_design)) +
                u" m³", 50),
            # F53 带宽s_belt_width_design
            ImageInfo(
                '0', (7562, 3208),
                format_value("number", str(handingSystem.s_belt_width_design))
                + u" mm", 50),
            # F55 带速s_belt_speed_design
            ImageInfo(
                '0', (7562, 3341),
                format_value("number", str(handingSystem.s_belt_speed_design))
                + u" m/s", 50),
            # F22 煤场面积c_coalyard_area_design
            ImageInfo('0', (7802, 1484),
                      format_value("number",
                                   str(handingSystem.c_coalyard_area_design)) +
                      u" m²", 50),
            # F15 煤的储备日数c_coal_store_days_design
            ImageInfo('0', (7845, 1593),
                      format_value("number",
                                   str(handingSystem.c_coal_store_days_design))
                      + u" 天", 50)
        ]

    def p1_cfb_dry_List(self, plan_id):
        furnaceCalculation, smokeAirSystem = GetimgInfoList().searchImgData(
            plan_id)
        i_reault = ""
        if smokeAirSystem.i_fan_total_pressure and smokeAirSystem.i_resistance_desulfurization_fan and smokeAirSystem.i_duct_resistance and smokeAirSystem.i_duster and smokeAirSystem.i_denitration:
            i_reault = smokeAirSystem.i_fan_total_pressure - smokeAirSystem.i_resistance_desulfurization_fan - smokeAirSystem.i_duct_resistance - smokeAirSystem.i_duster - smokeAirSystem.i_denitration

        f_fan_reduce_f_boiler = ""
        if smokeAirSystem.f_fan_total_pressure and smokeAirSystem.f_boiler_body_resistance:
            f_fan_reduce_f_boiler = smokeAirSystem.f_fan_total_pressure - smokeAirSystem.f_boiler_body_resistance

        s_fan_reduce_f_boiler = ""
        if smokeAirSystem.s_fan_total_pressure and smokeAirSystem.s_boiler_body_resistance:
            s_fan_reduce_f_boiler = smokeAirSystem.s_fan_total_pressure - smokeAirSystem.s_boiler_body_resistance
        return [
            # G78 风机全压  r_fan_total_pressure pa
            ImageInfo('0', (1968, 4101),
                      format_value("number",
                                   str(smokeAirSystem.r_fan_total_pressure)),
                      50),
            # G76 烟风流量（工况） r_smoke_flow_rate_condition m³/h
            ImageInfo('0', (2259, 4180),
                      format_value(
                          "number",
                          str(smokeAirSystem.r_smoke_flow_rate_condition)),
                      50),
            # G72 空气温度	t	℃  r_air_temperature
            ImageInfo('0', (2260, 4098),
                      format_value("number",
                                   str(smokeAirSystem.r_air_temperature)), 50),
            # G27风机全压 f_fan_total_pressure-G22锅炉本体阻力 f_boiler_body_resistance
            ImageInfo('0', (2379, 3639),
                      format_value("number", str(f_fan_reduce_f_boiler)), 50),
            # G43风机全压 s_fan_total_pressure-G38锅炉本体阻力 s_boiler_body_resistance
            ImageInfo('0', (2708, 3291),
                      format_value("number", str(s_fan_reduce_f_boiler)), 50),
            # G100热一次风温度 a_first_hwind_temperatue_design
            ImageInfo(
                '0', (2725, 3641),
                format_value(
                    "number",
                    str(furnaceCalculation.a_first_hwind_temperatue_design)),
                50),
            # G101热一次风量（湿-实态） a_first_hwind_flow_design
            ImageInfo('0', (2726, 3723),
                      format_value(
                          "number",
                          str(furnaceCalculation.a_first_hwind_flow_design)),
                      50),
            # G112热二次风温度 a_second_hwind_temperatue_design
            ImageInfo(
                '0', (3056, 3291),
                format_value(
                    "number",
                    str(furnaceCalculation.a_second_hwind_temperatue_design)),
                50),
            # G113热二次风量（湿-实态） a_second_hwind_flow_design
            ImageInfo('0', (3058, 3373),
                      format_value(
                          "number",
                          str(furnaceCalculation.a_second_hwind_flow_design)),
                      50),
            # G27风机全压 f_fan_total_pressure
            ImageInfo('0', (3807, 3119),
                      format_value("number",
                                   str(smokeAirSystem.f_fan_total_pressure)),
                      50),
            # G43风机全压 s_fan_total_pressure
            ImageInfo('0', (3807, 3935),
                      format_value("number",
                                   str(smokeAirSystem.s_fan_total_pressure)),
                      50),
            # G41 烟风流量（工况） s_smoke_flow_rate_condition
            ImageInfo('0', (4099, 4017),
                      format_value(
                          "number",
                          str(smokeAirSystem.s_smoke_flow_rate_condition)),
                      50),
            # G25烟风流量（工况） f_smoke_flow_rate_condition
            ImageInfo('0', (4100, 3197),
                      format_value(
                          "number",
                          str(smokeAirSystem.f_smoke_flow_rate_condition)),
                      50),
            # G21空气温度 f_air_temperature
            ImageInfo('0', (4101, 3117),
                      format_value("number",
                                   str(smokeAirSystem.f_air_temperature)), 50),
            # G37空气温度 s_air_temperature
            ImageInfo('0', (4101, 3935),
                      format_value("number",
                                   str(smokeAirSystem.s_air_temperature)), 50),
            # G62-G58-G57-G56-G55风机全压-风机后脱硫塔及烟囱烟道阻力-风道阻力-除尘器-脱硝
            # i_fan_total_pressure-i_resistance_desulfurization_fan-i_duct_resistance-i_duster-i_denitration
            ImageInfo('0', (4574, 3070),
                      format_value("number", str(i_reault)), 50),
            # G123空预器出口烟气容积量(实态） h_smoke_volume_design
            ImageInfo('0', (5107, 3150),
                      format_value(
                          "number",
                          str(furnaceCalculation.h_smoke_volume_design)), 50),
            # G122锅炉空预器出口排烟温度 h_smoke_temperature_design
            ImageInfo('0', (5110, 3070),
                      format_value(
                          "number",
                          str(furnaceCalculation.h_smoke_temperature_design)),
                      50),
            # G62 风机全压 i_fan_total_pressure
            ImageInfo('0', (7607, 3195),
                      format_value("number",
                                   str(smokeAirSystem.i_fan_total_pressure)),
                      50),
            # G53 i_air_temperature
            ImageInfo('0', (7899, 3191),
                      format_value("number",
                                   str(smokeAirSystem.i_air_temperature)), 50),
            # G60烟风流量（工况）i_smoke_flow_rate_condition
            ImageInfo('0', (7899, 3273),
                      format_value(
                          "number",
                          str(smokeAirSystem.i_smoke_flow_rate_condition)), 50),
            ImageInfo('0', (1973, 4191), '--', 50),
            ImageInfo('0', (2385, 3731), '--', 50),
            ImageInfo('0', (2709, 3371), '--', 50),
            ImageInfo('0', (3813, 3207), '--', 50),
            ImageInfo('0', (3813, 4019), '--', 50),
            ImageInfo('0', (4581, 3155), '--', 50),
            ImageInfo('0', (7609, 3279), '--', 50)
        ]

    def p2_cfb_wet_List(self, plan_id):
        furnaceCalculation, smokeAirSystem = GetimgInfoList().searchImgData(
            plan_id)
        i_reault = ""
        if smokeAirSystem.i_fan_total_pressure and smokeAirSystem.i_resistance_desulfurization_fan and smokeAirSystem.i_duct_resistance and smokeAirSystem.i_duster and smokeAirSystem.i_denitration:
            i_reault = smokeAirSystem.i_fan_total_pressure - smokeAirSystem.i_resistance_desulfurization_fan - smokeAirSystem.i_duct_resistance - smokeAirSystem.i_duster - smokeAirSystem.i_denitration

        f_fan_reduce_f_boiler = ""
        if smokeAirSystem.f_fan_total_pressure and smokeAirSystem.f_boiler_body_resistance:
            f_fan_reduce_f_boiler = smokeAirSystem.f_fan_total_pressure - smokeAirSystem.f_boiler_body_resistance

        s_fan_reduce_f_boiler = ""
        if smokeAirSystem.s_fan_total_pressure and smokeAirSystem.s_boiler_body_resistance:
            s_fan_reduce_f_boiler = smokeAirSystem.s_fan_total_pressure - smokeAirSystem.s_boiler_body_resistance

        return [
            # G78  风机全压  r_fan_total_pressure pa
            ImageInfo('0', (1979, 4100),
                      format_value("number",
                                   str(smokeAirSystem.r_fan_total_pressure)),
                      50),
            # G72 空气温度	t	℃  r_air_temperature
            ImageInfo('0', (2273, 4102),
                      format_value("number",
                                   str(smokeAirSystem.r_air_temperature)), 50),
            # G76 烟风流量（工况） r_smoke_flow_rate_condition m³/h
            ImageInfo('0', (2273, 4186),
                      format_value(
                          "number",
                          str(smokeAirSystem.r_smoke_flow_rate_condition)),
                      50),
            # G27-G22 G27风机全压 f_fan_total_pressure-G22锅炉本体阻力 f_boiler_body_resistance
            ImageInfo('0', (2417, 3648),
                      format_value("number", str(f_fan_reduce_f_boiler)), 50),
            # G43-G38 G43风机全压 s_fan_total_pressure-G38锅炉本体阻力 s_boiler_body_resistance
            ImageInfo('0', (2703, 3288),
                      format_value("number", str(s_fan_reduce_f_boiler)), 50),
            # G101热一次风量（湿-实态） a_first_hwind_flow_design
            ImageInfo('0', (2757, 3730),
                      format_value(
                          "number",
                          str(furnaceCalculation.a_first_hwind_flow_design)),
                      50),
            # G100热一次风温度 a_first_hwind_temperatue_design
            ImageInfo(
                '0', (2761, 3648),
                format_value(
                    "number",
                    str(furnaceCalculation.a_first_hwind_temperatue_design)),
                50),
            # G113热二次风量（湿-实态） a_second_hwind_flow_design
            ImageInfo('0', (3045, 3376),
                      format_value(
                          "number",
                          str(furnaceCalculation.a_second_hwind_flow_design)),
                      50),
            # G112热二次风温度 a_second_hwind_temperatue_design
            ImageInfo(
                '0', (3047, 3290),
                format_value(
                    "number",
                    str(furnaceCalculation.a_second_hwind_temperatue_design)),
                50),
            # G27风机全压 f_fan_total_pressure
            ImageInfo('0', (3815, 3120),
                      format_value("number",
                                   str(smokeAirSystem.f_fan_total_pressure)),
                      50),
            # G43风机全压 s_fan_total_pressure
            ImageInfo('0', (3817, 3937),
                      format_value("number",
                                   str(smokeAirSystem.s_fan_total_pressure)),
                      50),
            # G41 烟风流量（工况） s_smoke_flow_rate_condition
            ImageInfo('0', (4107, 4019),
                      format_value(
                          "number",
                          str(smokeAirSystem.s_smoke_flow_rate_condition)),
                      50),
            # G37空气温度 s_air_temperature
            ImageInfo('0', (4109, 3937),
                      format_value("number",
                                   str(smokeAirSystem.s_air_temperature)), 50),
            # G25烟风流量（工况） f_smoke_flow_rate_condition
            ImageInfo('0', (4111, 3120),
                      format_value(
                          "number",
                          str(smokeAirSystem.f_smoke_flow_rate_condition)),
                      50),
            # G21空气温度 f_air_temperature
            ImageInfo('0', (4111, 3202),
                      format_value("number",
                                   str(smokeAirSystem.f_air_temperature)), 50),
            # G62-G57-G56风机全压--风道阻力-除尘器
            # i_fan_total_pressure-i_duct_resistance-i_duster
            ImageInfo('0', (4227, 1883),
                      format_value("number", str(i_reault)), 50),
            # G123空预器出口烟气容积量(实态） h_smoke_volume_design
            ImageInfo('0', (4751, 1957),
                      format_value(
                          "number",
                          str(furnaceCalculation.h_smoke_volume_design)), 50),
            # G122锅炉空预器出口排烟温度 h_smoke_temperature_design
            ImageInfo('0', (4755, 1883),
                      format_value(
                          "number",
                          str(furnaceCalculation.h_smoke_temperature_design)),
                      50),
            # G62 风机全压 i_fan_total_pressure
            ImageInfo('0', (6086, 3195),
                      format_value("number",
                                   str(smokeAirSystem.i_fan_total_pressure)),
                      50),
            # G60烟风流量（工况）i_smoke_flow_rate_condition
            ImageInfo('0', (6379, 3277),
                      format_value(
                          "number",
                          str(smokeAirSystem.i_smoke_flow_rate_condition)),
                      50),
            # G53 i_air_temperature
            ImageInfo('0', (6380, 3197),
                      format_value("number",
                                   str(smokeAirSystem.i_air_temperature)), 50)
        ]

    # 原则性热力系统图--3JD+
    def p1_a_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_four = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_four = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount+turbineBackpressure.i_steam_exhaust_flow
        plus_three = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount
        plus_36_37 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_36_37 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount
        plus_32_33 = ""
        if turbineBackpressure.hh1_extraction_amount and turbineBackpressure.hh2_extraction_amount:
            plus_32_33 = turbineBackpressure.hh1_extraction_amount + turbineBackpressure.hh2_extraction_amount
        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        multiply_f33_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        return [

            # 汽轮机-三级低加F33 hh2_saturated_water_enthalpy
            ImageInfo('0', (757, 2575), format_value("number", str(turbineBackpressure.hh2_saturated_water_enthalpy)), 50),
            # 锅炉辅机G58 p_inlet_pressure
            ImageInfo('0', (757, 1664), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 50),
            # 汽轮机-三级低加C32 hh1_water_enthalpy
            ImageInfo('0', (757, 1760), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 50),
            # 汽轮机-三级低加F32 hh1_saturated_water_enthalpy
            ImageInfo('0', (757, 2067), format_value("number", str(turbineBackpressure.hh1_saturated_water_enthalpy)), 50),
            # 锅炉辅机F33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (758, 3077), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 50),
            # 锅炉辅机F32 c_drum_pressure
            ImageInfo('0', (759, 2977), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 50),
            # 锅炉辅机F31/1000 c_sewage_quantity/1000
            ImageInfo('0', (977, 3072), format_value("number", str(sewage_quantity)), 50),
            # 汽轮机-三级低加K32 hh1_extraction_amount
            ImageInfo('0', (1048, 2067), format_value("number", str(turbineBackpressure.hh1_extraction_amount)), 50),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1048, 1760), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 50),
            # 汽轮机-三级低加K32+K33 hh1_extraction_amount+hh2_extraction_amount
            ImageInfo('0', (1048, 2574), format_value("number", str(plus_32_33)), 50),
            # 汽轮机-三级低加E32 hh1_saturated_water_temperature
            ImageInfo('0', (1049, 1971), format_value("number", str(turbineBackpressure.hh1_saturated_water_temperature)), 50),
            # 汽轮机-三级低加E33  hh2_saturated_water_temperature
            ImageInfo('0', (1049, 2480), format_value("number", str(turbineBackpressure.hh2_saturated_water_temperature)), 50),
            # 汽轮机-三级低加B32 hh1_water_temperature
            ImageInfo('0', (1051, 1665), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 50),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1279, 920), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 50),
            # 汽轮机-三级低加G35 d_work_pressure
            ImageInfo('0', (1687, 3984), format_value("number", str(turbineBackpressure.d_work_pressure)), 50),
            # 汽轮机-三级低加C35 d_water_enthalpy
            ImageInfo('0', (1687, 4081), format_value("number", str(turbineBackpressure.d_water_enthalpy)), 50),
            # 汽轮机-三级低加i35 d_extraction_pressure
            ImageInfo('0', (1953, 2355), format_value("number", str(turbineBackpressure.d_extraction_pressure)), 50),
            # 汽轮机-三级低加J35 d_extraction_enthalpy
            ImageInfo('0', (1953, 2447), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)), 50),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1993, 4085), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 50),
            # 汽轮机-三级低加 B35 d_water_temperature
            ImageInfo('0', (1995, 3989), format_value("number", str(turbineBackpressure.d_water_temperature)), 50),
            # 汽轮机-三级低加k35 d_extraction_amount
            ImageInfo('0', (2239, 2447), format_value("number", str(turbineBackpressure.d_extraction_amount)), 50),
            # 汽轮机-三级低加J32 hh1_extraction_enthalpy
            ImageInfo('0', (2353, 1665), format_value("number", str(turbineBackpressure.hh1_extraction_enthalpy)), 50),
            # 汽轮机-三级低加i32 hh1_extraction_pressure
            ImageInfo('0', (2355, 1567), format_value("number", str(turbineBackpressure.hh1_extraction_pressure)), 50),
            # 汽轮机-三级低加J33 hh2_extraction_enthalpy
            ImageInfo('0', (2355, 1988), format_value("number", str(turbineBackpressure.hh2_extraction_enthalpy)), 50),
            # 汽轮机-三级低加i33 hh2_extraction_pressure
            ImageInfo('0', (2358, 1888), format_value("number", str(turbineBackpressure.hh2_extraction_pressure)), 50),
            # 锅炉计算G22 f_steam_enthalpy_design
            ImageInfo('0', (2552, 464), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)), 50),
            # 锅炉计算G20 f_steam_pressure_design
            ImageInfo('0', (2553, 365), format_value("number", str(furnaceCalculation.f_steam_pressure_design)), 50),
            # 汽轮机-三级低加F34  h_pressure
            ImageInfo('0', (2591, 4126), format_value("number", str(turbineBackpressure.h_pressure)), 50),
            # 汽轮机-三级低加H34 h_enthalpy
            ImageInfo('0', (2592, 4223), format_value("number", str(turbineBackpressure.h_enthalpy)), 50),
            # 汽轮机-三级低加K32 hh1_extraction_amount
            ImageInfo('0', (2641, 1666), format_value("number", str(turbineBackpressure.hh1_extraction_amount)), 50),
            # 汽轮机-三级低加K33 hh2_extraction_amount
            ImageInfo('0', (2641, 1986), format_value("number", str(turbineBackpressure.hh2_extraction_amount)), 50),
            # 汽轮机-三级低加C36 lh1_water_enthalpy
            ImageInfo('0', (2671, 3268), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 50),
            # 汽轮机-三级低加F26 e_throttle_flow
            ImageInfo('0', (2770, 464), format_value("number", str(turbineBackpressure.e_throttle_flow)), 50),
            # 锅炉计算G21 f_steam_temperature_design
            ImageInfo('0', (2772, 365), format_value("number", str(furnaceCalculation.f_steam_temperature_design)), 50),
            # 汽轮机-三级低加B36 lh1_water_temperature
            ImageInfo('0', (2887, 3168), format_value("number", str(turbineBackpressure.lh1_water_temperature)), 50),
            # 汽轮机-三级低加K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2889, 3270), format_value("number", str(plus_four)), 50),
            # 汽轮机-三级低加I36 lh1_extraction_pressure
            ImageInfo('0', (2914, 2361), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)), 50),
            # 汽轮机-三级低加J36 lh1_extraction_enthalpy
            ImageInfo('0', (2918, 2463), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)), 50),
            # 锅炉计算G19*汽轮机-三级低加J34 h_amount
            ImageInfo('0', (2953, 4221), format_value("number", str(multiply_f33_g19)), 50),
            # 汽轮机-三级低加D34 h_temperature
            ImageInfo('0', (2958, 4131), format_value("number", str(turbineBackpressure.h_temperature)), 50),
            # 汽轮机-三级低加F36  lh1_saturated_water_enthalpy
            ImageInfo('0', (3119, 3527), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)), 50),
            # 汽轮机-三级低加K36 lh1_extraction_amount
            ImageInfo('0', (3141, 2462), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 50),
            # 汽轮机-三级低加C37 lh2_water_enthalpy
            ImageInfo('0', (3208, 3263), format_value("number", str(turbineBackpressure.lh2_water_enthalpy)), 50),
            # 汽轮机-三级低加K36 lh1_extraction_amount
            ImageInfo('0', (3351, 3525), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 50),
            # 汽轮机-三级低加E36 lh1_saturated_water_temperature
            ImageInfo('0', (3352, 3425), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)), 50),
            # 汽轮机-三级低加J37 lh2_extraction_enthalpy
            ImageInfo('0', (3421, 2459), format_value("number", str(turbineBackpressure.lh2_extraction_enthalpy)), 50),
            # 汽轮机-三级低加K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3421, 3259), format_value("number", str(plus_four)), 50),
            # 汽轮机-三级低加i37 lh2_extraction_pressure
            ImageInfo('0', (3423, 2365), format_value("number", str(turbineBackpressure.lh2_extraction_pressure)), 50),
            # 汽轮机-三级低加B37 lh2_water_temperature
            ImageInfo('0', (3423, 3164), format_value("number", str(turbineBackpressure.lh2_water_temperature)), 50),
            # 汽轮机-三级低加k37 lh2_extraction_amount
            ImageInfo('0', (3651, 2464), format_value("number", str(turbineBackpressure.lh2_extraction_amount)), 50),
            # 汽轮机-三级低加F37 lh2_saturated_water_enthalpy
            ImageInfo('0', (3651, 3530), format_value("number", str(turbineBackpressure.lh2_saturated_water_enthalpy)), 50),
            # 汽轮机-三级低加F24 e_steam_extraction_select
            ImageInfo('0', (3652, 1426), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 50),
            # 汽轮机-三级低加c38 lh3_water_enthalpy
            ImageInfo('0', (3715, 3262), format_value("number", str(turbineBackpressure.lh3_water_enthalpy)), 50),
            # 汽轮机-三级低加E37 lh2_saturated_water_temperature
            ImageInfo('0', (3883, 3436), format_value("number", str(turbineBackpressure.lh2_saturated_water_temperature)), 50),
            # 汽轮机-三级低加k36+K37 lh1_extraction_amount+lh2_extraction_amount
            ImageInfo('0', (3885, 3531), format_value("number", str(plus_36_37)), 50),
            # 汽轮机-三级低加b38 lh3_water_temperature
            ImageInfo('0', (3929, 3167), format_value("number", str(turbineBackpressure.lh3_water_temperature)), 50),
            # 汽轮机-三级低加K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3931, 3265), format_value("number", str(plus_four)), 50),
            # 汽轮机-三级低加j38 lh3_extraction_enthalpy
            ImageInfo('0', (3935, 2460), format_value("number", str(turbineBackpressure.lh3_extraction_enthalpy)), 50),
            # 汽轮机-三级低加I38 lh3_extraction_pressure
            ImageInfo('0', (3941, 2367), format_value("number", str(turbineBackpressure.lh3_extraction_pressure)), 50),
            # 汽轮机-三级低加f69 i_exhaust_point_pressure
            ImageInfo('0', (3969, 1098), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)), 50),
            # 汽轮机-三级低加f72 i_exhaust_point_enthalpy
            ImageInfo('0', (3970, 1202), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)), 50),
            # 汽轮机-三级低加k38 lh3_extraction_amount
            ImageInfo('0', (4157, 2463), format_value("number", str(turbineBackpressure.lh3_extraction_amount)), 50),
            # 汽轮机-三级低加f38 lh3_saturated_water_enthalpy
            ImageInfo('0', (4193, 3527), format_value("number", str(turbineBackpressure.lh3_saturated_water_enthalpy)), 50),
            # 汽轮机-三级低加f70 i_exhaust_point_temperature
            ImageInfo('0', (4206, 1102), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)), 50),
            # 汽轮机-三级低加f73 i_exhaust_point_flow
            ImageInfo('0', (4206, 1199), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)), 50),
            # 汽轮机-三级低加C39 c_water_enthalpy
            ImageInfo('0', (4224, 3256), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 50),
            # 汽轮机-三级低加K36+K37+K38+F100  lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (4394, 3261), format_value("number", str(plus_four)), 50),
            # 汽轮机-三级低加B39 c_water_temperature
            ImageInfo('0', (4396, 3166), format_value("number", str(turbineBackpressure.c_water_temperature)), 50),
            # 汽轮机-三级低加K36+K37+K38  lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount
            ImageInfo('0', (4420, 3529), format_value("number", str(plus_three)), 50),
            # 汽轮机-三级低加E38 lh3_saturated_water_temperature
            ImageInfo('0', (4422, 3434), format_value("number", str(turbineBackpressure.lh3_saturated_water_temperature)), 50),
            # 汽轮机-三级低加f93 i_steam_exhaust_pressure
            ImageInfo('0', (4955, 1860), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)), 50),
            # 汽轮机-三级低加f96 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4957, 1962), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 50),
            # 汽轮机-三级低加f100 i_steam_exhaust_flow
            ImageInfo('0', (5215, 1954), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)), 50),
            # 汽轮机-三级低加f24 e_steam_extraction_select
            ImageInfo('0', (5373, 1478), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 50),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5502, 2666), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 50),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5750, 1960), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 50),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6228, 1222), format_value("number", str(circulatingWater.v_evaporation_loss)), 50),
            # 循环水E19 v_circulating_pool_size
            ImageInfo('0', (6614, 3427), format_value("number", str(circulatingWater.v_circulating_pool_size)), 50),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (7173, 1230), format_value("number", str(circulatingWater.v_partial_blow_loss)), 50),
            # 循环水E20 v_circulating_pool_long
            ImageInfo('0', (8192, 3274), format_value("number", str(circulatingWater.v_circulating_pool_long)), 50),
        ]

# 原则性热力系统图--3JD+
    def p1_b_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_four = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_four = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount+turbineBackpressure.i_steam_exhaust_flow
        plus_three = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount
        plus_36_37 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_36_37 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount
        plus_32_33 = ""
        if turbineBackpressure.hh1_extraction_amount and turbineBackpressure.hh2_extraction_amount:
            plus_32_33 = turbineBackpressure.hh1_extraction_amount + turbineBackpressure.hh2_extraction_amount
        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        multiply_f33_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        return [

            # 锅炉辅机F32 c_drum_pressure
            ImageInfo('0', (387, 2964), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 35),
            # --
            ImageInfo('0', (389, 2477), '--', 35),
            # 锅炉辅机F33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (389, 3062), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 35),
            # 锅炉辅机！G58 p_inlet_pressure
            ImageInfo('0', (390, 1668), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 35),
            # --
            ImageInfo('0', (390, 1974), '--', 35),
            # 汽轮机-三级低加！F33 hh2_saturated_water_enthalpy
            ImageInfo('0', (390, 2572), format_value("number", str(turbineBackpressure.hh2_saturated_water_enthalpy)), 35),
            # 汽轮机-三级低加！C32 hh1_water_enthalpy
            ImageInfo('0', (392, 1769), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 35),
            # 汽轮机-三级低加！F32 hh1_saturated_water_enthalpy
            ImageInfo('0', (392, 2072), format_value("number", str(turbineBackpressure.hh1_saturated_water_enthalpy)), 35),
            # --
            ImageInfo('0', (603, 2966), '--', 35),
            # 锅炉辅机F31/1000 c_sewage_quantity/1000
            ImageInfo('0', (604, 3062), format_value("number", str(sewage_quantity)), 35),
            # 汽轮机-三级低加！E33 hh2_saturated_water_temperature
            ImageInfo('0', (680, 2476), format_value("number", str(turbineBackpressure.hh2_saturated_water_temperature)), 35),
            # 汽轮机-三级低加！B32 hh1_water_temperature
            ImageInfo('0', (681, 1673), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 35),
            # 汽轮机-三级低加！E32 hh1_saturated_water_temperature
            ImageInfo('0', (681, 1976), format_value("number", str(turbineBackpressure.hh1_saturated_water_temperature)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (683, 1772), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机-三级低加！K32 hh1_extraction_amount
            ImageInfo('0', (684, 2073), format_value("number", str(turbineBackpressure.hh1_extraction_amount)), 35),
            # 汽轮机-三级低加K32+K33 hh1_extraction_amount+hh2_extraction_amount
            ImageInfo('0', (685, 2571), format_value("number", str(plus_32_33)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (907, 951), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机-三级低加！G35 d_work_pressure
            ImageInfo('0', (1311, 3964), format_value("number", str(turbineBackpressure.d_work_pressure)), 35),
            # 汽轮机-三级低加！C35 d_water_enthalpy
            ImageInfo('0', (1314, 4058), format_value("number", str(turbineBackpressure.d_water_enthalpy)), 35),
            # 汽轮机-三级低加！I35 d_extraction_pressure
            ImageInfo('0', (1589, 2361), format_value("number", str(turbineBackpressure.d_extraction_pressure)), 35),
            # 汽轮机-三级低加！J35 d_extraction_enthalpy
            ImageInfo('0', (1591, 2459), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)), 35),
            # 汽轮机-三级低加！B35 d_water_temperature
            ImageInfo('0', (1615, 3967), format_value("number", str(turbineBackpressure.d_water_temperature)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1619, 4063), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # --
            ImageInfo('0', (1863, 2363), '--', 35),
            # 汽轮机-三级低加！K35 d_extraction_amount
            ImageInfo('0', (1865, 2457), format_value("number", str(turbineBackpressure.d_extraction_amount)), 35),
            # 汽轮机-三级低加！I32 hh1_extraction_pressure
            ImageInfo('0', (1973, 1584), format_value("number", str(turbineBackpressure.hh1_extraction_pressure)), 35),
            # 汽轮机-三级低加！I33 hh2_extraction_pressure
            ImageInfo('0', (1973, 1900), format_value("number", str(turbineBackpressure.hh2_extraction_pressure)), 35),
            # 汽轮机-三级低加！J32 hh1_extraction_enthalpy
            ImageInfo('0', (1975, 1680), format_value("number", str(turbineBackpressure.hh1_extraction_enthalpy)), 35),
            # 汽轮机-三级低加！J33 hh2_extraction_enthalpy
            ImageInfo('0', (1977, 1998), format_value("number", str(turbineBackpressure.hh2_extraction_enthalpy)), 35),
            # 锅炉计算！G20 f_steam_pressure_design
            ImageInfo('0', (2161, 396), format_value("number", str(furnaceCalculation.f_steam_pressure_design)), 35),
            # 锅炉计算！G22 f_steam_enthalpy_design
            ImageInfo('0', (2165, 494), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)), 35),
            # 汽轮机-三级低加！F34 h_pressure
            ImageInfo('0', (2193, 4100), format_value("number", str(turbineBackpressure.h_pressure)), 35),
            # 汽轮机-三级低加！H34 h_enthalpy
            ImageInfo('0', (2195, 4198), format_value("number", str(turbineBackpressure.h_enthalpy)), 35),
            # --
            ImageInfo('0', (2251, 1582), '--', 35),
            # 汽轮机-三级低加！K32 hh1_extraction_amount
            ImageInfo('0', (2257, 1682), format_value("number", str(turbineBackpressure.hh1_extraction_amount)), 35),
            # --
            ImageInfo('0', (2259, 1900), '--', 35),
            # 汽轮机-三级低加！K33 hh2_extraction_amount
            ImageInfo('0', (2261, 1996), format_value("number", str(turbineBackpressure.hh2_extraction_amount)), 35),
            # --
            ImageInfo('0', (2277, 3152), '--', 35),
            # 汽轮机-三级低加！C36 lh1_water_enthalpy
            ImageInfo('0', (2279, 3247), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 35),
            # 锅炉计算！G21 f_steam_temperature_design
            ImageInfo('0', (2379, 394), format_value("number", str(furnaceCalculation.f_steam_temperature_design)), 35),
            #  汽轮机-三级低加F26 e_throttle_flow
            ImageInfo('0', (2381, 492), format_value("number", str(turbineBackpressure.e_throttle_flow)), 35),
            # 汽轮机-三级低加！B36 lh1_water_temperature
            ImageInfo('0', (2490, 3151), format_value("number", str(turbineBackpressure.lh1_water_temperature)), 35),
            # 汽轮机-三级低加！K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2493, 3249), format_value("number", str(plus_four)), 35),
            # 汽轮机-三级低加！I36 lh1_extraction_pressure
            ImageInfo('0', (2524, 2360), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)), 35),
            # 汽轮机-三级低加！J36 lh1_extraction_enthalpy
            ImageInfo('0', (2527, 2456), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)), 35),
            # 锅炉计算！G19 * 汽轮机-三级低加！J34
            ImageInfo('0', (2556, 4198), format_value("number", str(multiply_f33_g19)), 35),
            # 汽轮机-三级低加！D34 h_temperature
            ImageInfo('0', (2557, 4099), format_value("number", str(turbineBackpressure.h_temperature)), 35),
            # --
            ImageInfo('0', (2722, 3413), '--', 35),
            # 汽轮机-三级低加！F36 lh1_saturated_water_enthalpy
            ImageInfo('0', (2726, 3513), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)), 35),
            # --
            ImageInfo('0', (2745, 2360), '--', 35),
            # 汽轮机-三级低加！K36 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2746, 2457), format_value("number", str(plus_four)), 35),
            # --
            ImageInfo('0', (2807, 3152), '--', 35),
            # 汽轮机-三级低加！C37 lh2_water_enthalpy
            ImageInfo('0', (2809, 3248), format_value("number", str(turbineBackpressure.lh2_water_enthalpy)), 35),
            # 汽轮机-三级低加！E36 lh1_saturated_water_temperature
            ImageInfo('0', (2955, 3416), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)), 35),
            # 汽轮机-三级低加！K36 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2956, 3511), format_value("number", str(plus_four)), 35),
            # 汽轮机-三级低加！K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3023, 3249), format_value("number", str(plus_four)), 35),
            # 汽轮机-三级低加！B37 lh2_water_temperature
            ImageInfo('0', (3025, 2361), format_value("number", str(turbineBackpressure.lh2_water_temperature)), 35),
            # 汽轮机-三级低加！I37 lh2_extraction_pressure
            ImageInfo('0', (3025, 3152), format_value("number", str(turbineBackpressure.lh2_extraction_pressure)), 35),
            # 汽轮机-三级低加！J37 lh2_extraction_enthalpy
            ImageInfo('0', (3027, 2463), format_value("number", str(turbineBackpressure.lh2_extraction_enthalpy)), 35),
            # --
            ImageInfo('0', (3242, 2361), '--', 35),
            # --
            ImageInfo('0', (3244, 3415), '--', 35),
            # 汽轮机-三级低加！K37 lh2_extraction_amount
            ImageInfo('0', (3247, 2460), format_value("number", str(turbineBackpressure.lh2_extraction_amount)), 35),
            # 汽轮机-三级低加！F37 lh2_saturated_water_enthalpy
            ImageInfo('0', (3247, 3510), format_value("number", str(turbineBackpressure.lh2_saturated_water_enthalpy)), 35),
            # 汽轮机计算！F24' e_steam_extraction_select
            ImageInfo('0', (3259, 1462), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # --
            ImageInfo('0', (3308, 3151), '--', 35),
            # 汽轮机-三级低加！C38 lh3_water_enthalpy
            ImageInfo('0', (3312, 3255), format_value("number", str(turbineBackpressure.lh3_water_enthalpy)), 35),
            # 汽轮机-三级低加！E37 lh2_saturated_water_temperature
            ImageInfo('0', (3471, 3414), format_value("number", str(turbineBackpressure.lh2_saturated_water_temperature)), 35),
            # 汽轮机-三级低加！K36+K37 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3474, 3512), format_value("number", str(plus_36_37)), 35),
            # 汽轮机-三级低加！K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3527, 3253), format_value("number", str(plus_four)), 35),
            # 汽轮机-三级低加！B38 lh3_water_temperature
            ImageInfo('0', (3528, 3157), format_value("number", str(turbineBackpressure.lh3_water_temperature)), 35),
            # 汽轮机-三级低加！I38 lh3_extraction_pressure
            ImageInfo('0', (3529, 2361), format_value("number", str(turbineBackpressure.lh3_extraction_pressure)), 35),
            # 汽轮机-三级低加！J38 lh3_extraction_enthalpy
            ImageInfo('0', (3532, 2463), format_value("number", str(turbineBackpressure.lh3_extraction_enthalpy)), 35),
            # 汽轮机-三级低加！F69 i_exhaust_point_pressure
            ImageInfo('0', (3562, 1115), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)), 35),
            # 汽轮机-三级低加！F72 i_exhaust_point_enthalpy
            ImageInfo('0', (3565, 1208), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)), 35),
            # --
            ImageInfo('0', (3754, 2362), '--', 35),
            # 汽轮机-三级低加！K38 lh3_extraction_amount
            ImageInfo('0', (3754, 2457), format_value("number", str(turbineBackpressure.lh3_extraction_amount)), 35),
            # --
            ImageInfo('0', (3781, 3418), '--', 35),
            # 汽轮机-三级低加！F38 lh3_saturated_water_enthalpy
            ImageInfo('0', (3783, 3517), format_value("number", str(turbineBackpressure.lh3_saturated_water_enthalpy)), 35),
            # 汽轮机-三级低加！F70 i_exhaust_point_temperature
            ImageInfo('0', (3796, 1115), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)), 35),
            # 汽轮机-三级低加！F73 i_exhaust_point_flow
            ImageInfo('0', (3800, 1213), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)), 35),
            # --
            ImageInfo('0', (3815, 3151), '--', 35),
            # 汽轮机-三级低加！C39 c_water_enthalpy
            ImageInfo('0', (3816, 3248), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 35),
            # 汽轮机-三级低加！B39 c_water_temperature
            ImageInfo('0', (3979, 3151), format_value("number", str(turbineBackpressure.c_water_temperature)), 35),
            # 汽轮机-三级低加！K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3981, 3246), format_value("number", str(plus_four)), 35),
            # 汽轮机-三级低加！E38 lh3_saturated_water_temperature
            ImageInfo('0', (4009, 3415), format_value("number", str(turbineBackpressure.lh3_saturated_water_temperature)), 35),
            # 汽轮机-三级低加！K36+K37+K38 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (4010, 3511), format_value("number", str(plus_three)), 35),
            # 汽轮机计算！F93 i_steam_exhaust_pressure
            ImageInfo('0', (4532, 1864), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)), 35),
            # 汽轮机计算！F96 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4534, 1961), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 35),
            # --
            ImageInfo('0', (4751, 1864), '--', 35),
            # 汽轮机计算！F100 i_steam_exhaust_flow
            ImageInfo('0', (4751, 1958), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)), 35),
            # --
            ImageInfo('0', (4857, 2562), '--', 35),
            # --
            ImageInfo('0', (4861, 2658), '--', 35),
            # 汽轮机计算！F24 e_steam_extraction_select
            ImageInfo('0', (4952, 1512), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 20/33
            ImageInfo('0', (5073, 2562), '20/33', 35),
            # 循环水系统计算！E9 v_total_circulating_water_select
            ImageInfo('0', (5074, 2657), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            # --
            ImageInfo('0', (5111, 1867), '--', 35),
            # --
            ImageInfo('0', (5115, 1968), '--', 35),
            # 30/43
            ImageInfo('0', (5322, 1863), '30/43', 35),
            # u'循环水系统！E9' v_total_circulating_water_select
            ImageInfo('0', (5324, 1964), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            # u'循环水系统！E14'  v_evaporation_loss
            ImageInfo('0', (6100, 1440), format_value("number", str(circulatingWater.v_evaporation_loss)), 35),
            # u'循环水系统！E19' v_circulating_pool_size
            ImageInfo('0', (6752, 3558), format_value("number", str(circulatingWater.v_circulating_pool_size)), 35),
            # u'循环水系统！F16' v_partial_blow_loss
            ImageInfo('0', (7006, 1442), format_value("number", str(circulatingWater.v_partial_blow_loss)), 35),
            # u'循环水系统！E20' v_circulating_pool_long
            ImageInfo('0', (8616, 3410), format_value("number", str(circulatingWater.v_circulating_pool_long)), 35)
        ]


    # 原则性热力系统图--0JG+
    def p2_a_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_three = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount

        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        plus_35_99 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_35_99 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.i_steam_exhaust_flow
        multiply_f33_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        plus_35_36 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_35_36 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount

        return [
            # 锅炉辅机！G58 p_inlet_pressure
            ImageInfo('0', (753, 1673), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 35),
            # 汽轮机计算-0级高加!C32 hh1_water_enthalpy
            ImageInfo('0', (753, 1765), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 35),
            # 锅炉辅机!E32 c_drum_pressure
            ImageInfo('0', (753, 2981), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 35),
            # 锅炉辅机!E33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (757, 3081), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 35),
            ImageInfo('0', (981, 2981), "--", 35),
            # 锅炉辅机!E31/1000 c_sewage_quantity/1000
            ImageInfo('0', (981, 3077), format_value("number", str(sewage_quantity)), 35),
            # 汽轮机计算-0级高加！B32 hh1_water_temperature
            ImageInfo('0', (1049, 1665), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1053, 1773), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1273, 929), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-0级高加！G34 d_work_pressure
            ImageInfo('0', (1693, 3983), format_value("number", str(turbineBackpressure.d_work_pressure)), 35),
            # 汽轮机计算-0级高加！C34 d_water_enthalpy
            ImageInfo('0', (1693, 4079), format_value("number", str(turbineBackpressure.d_water_enthalpy)), 35),
            # 汽轮机计算-0级高加！J34 d_extraction_enthalpy
            ImageInfo('0', (1957, 2441), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)), 35),
            # 汽轮机计算-0级高加！I34 d_extraction_pressure
            ImageInfo('0', (1961, 2349), format_value("number", str(turbineBackpressure.d_extraction_pressure)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1993, 4079), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-0级高加！B34 d_water_temperature
            ImageInfo('0', (2001, 3995), format_value("number", str(turbineBackpressure.d_water_temperature)), 35),
            ImageInfo('0', (2241, 2361), "--", 35),
            # 汽轮机计算-0级高加！K34 d_extraction_amount
            ImageInfo('0', (2245, 2445), format_value("number", str(turbineBackpressure.d_extraction_amount)), 35),
            # 锅炉计算!G20 f_steam_pressure_design
            ImageInfo('0', (2549, 369), format_value("number", str(furnaceCalculation.f_steam_pressure_design)), 35),
            # 锅炉计算!G22 f_steam_enthalpy_design
            ImageInfo('0', (2549, 469), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)), 35),
            # 汽轮机计算-0级高加！H33 h_enthalpy
            ImageInfo('0', (2577, 4223), format_value("number", str(turbineBackpressure.h_enthalpy)), 35),
            # 汽轮机计算-0级高加！F33 h_pressure
            ImageInfo('0', (2593, 4127), format_value("number", str(turbineBackpressure.h_pressure)), 35),
            # 汽轮机计算-0级高加！C35 lh1_water_enthalpy
            ImageInfo('0', (2601, 3253), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 35),
            ImageInfo('0', (2621, 3149), "--", 35),
            # 锅炉计算!G21 f_steam_temperature_design
            ImageInfo('0', (2765, 369), format_value("number", str(furnaceCalculation.f_steam_temperature_design)), 35),
            # 汽轮机计算-0级高加！F26 e_throttle_flow
            ImageInfo('0', (2765, 465), format_value("number", str(turbineBackpressure.e_throttle_flow)), 35),
            # 汽轮机计算-0级高加！B35 lh1_water_temperature
            ImageInfo('0', (2853, 3145), format_value("number", str(turbineBackpressure.lh1_water_temperature)), 35),
            # lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2857, 3241), format_value("number", str(plus_three)), 35),
            # 锅炉计算G19 * 汽轮机0级高加J33
            ImageInfo('0', (2949, 4219), format_value("number", str(multiply_f33_g19)), 35),
            # 汽轮机计算-0级高加！D33 h_temperature
            ImageInfo('0', (2957, 4123), format_value("number", str(turbineBackpressure.h_temperature)), 35),
            # 汽轮机计算-0级高加！J35 lh1_extraction_enthalpy
            ImageInfo('0', (3241, 2461), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)), 35),
            # 汽轮机计算-0级高加！I35 lh1_extraction_pressure
            ImageInfo('0', (3245, 2361), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)), 35),
            # 汽轮机计算-0级高加！F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (3293, 3539), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)), 35),
            ImageInfo('0', (3296, 3441), "--", 35),

            # 汽轮机计算-0级高加！C36 lh2_water_enthalpy
            ImageInfo('0', (3369, 3245), format_value("number", str(turbineBackpressure.lh2_water_enthalpy)), 35),
            ImageInfo('0', (3373, 3149), "--", 35),
            # 汽轮机0级高加K35 lh1_extraction_amount
            ImageInfo('0', (3477, 2461), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            ImageInfo('0', (3485, 2365), "--", 35),
            # 汽轮机0级高加K35 lh1_extraction_amount
            ImageInfo('0', (3531, 3537), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机计算-0级高加！E35 lh1_saturated_water_temperature
            ImageInfo('0', (3532, 3444), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)), 35),
            # 汽轮机计算-0级高加！B36 lh2_water_temperature 
            ImageInfo('0', (3621, 3149), format_value("number", str(turbineBackpressure.lh2_water_temperature)), 35),
            # 汽轮机计算-0级高加！(K35+K35+F99) lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3621, 3237), format_value("number", str(plus_three)), 35),
            # 汽轮机计算-0级高加！F24 e_steam_extraction_select
            ImageInfo('0', (3653, 1445), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 汽轮机计算-0级高加！J36 lh2_extraction_enthalpy
            ImageInfo('0', (3865, 2465), format_value("number", str(turbineBackpressure.lh2_extraction_enthalpy)), 35),
            # 汽轮机计算-0级高加！I36 lh2_extraction_pressure
            ImageInfo('0', (3869, 2357), format_value("number", str(turbineBackpressure.lh2_extraction_pressure)), 35),
            ImageInfo('0', (3953, 3444), "--", 35),
            # 汽轮机计算-0级高加！F36 lh2_saturated_water_enthalpy
            ImageInfo('0', (3953, 3539), format_value("number", str(turbineBackpressure.lh2_saturated_water_enthalpy)), 35),
            # 汽轮机计算-0级高加！F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3965, 1197), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)), 35),
            # 汽轮机计算-0级高加！F68 i_exhaust_point_pressure
            ImageInfo('0', (3969, 1101), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)), 35),
            ImageInfo('0', (4101, 2369), "--", 35),
            # 汽轮机0级高加K36 lh2_extraction_amount
            ImageInfo('0', (4101, 2461), format_value("number", str(turbineBackpressure.lh2_extraction_amount)), 35),
            # 汽轮机计算-0级高加！C38 c_water_enthalpy
            ImageInfo('0', (4101, 3245), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 35),
            ImageInfo('0', (4113, 3141), "--", 35),
            # 汽轮机计算-0级高加！E36 lh2_saturated_water_temperature
            ImageInfo('0', (4196, 3441), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 35),
            # 汽轮机计算-0级高加！(K35+K36) lh1_extraction_amount+lh2_extraction_amount
            ImageInfo('0', (4197, 3535), format_value("number", str(plus_35_36)), 35),
            # 汽轮机计算-0级高加！F72 i_exhaust_point_flow
            ImageInfo('0', (4201, 1197), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)), 35),
            # 汽轮机计算-0级高加！F69 i_exhaust_point_temperature
            ImageInfo('0', (4213, 1097), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)), 35),
            # 汽轮机计算-0级高加！B38 c_water_temperature
            ImageInfo('0', (4345, 3146), format_value("number", str(turbineBackpressure.c_water_temperature)), 35),
            # 汽轮机计算-0级高加！(K35+K35+F99) lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (4349, 3249), format_value("number", str(plus_three)), 35),
            # 汽轮机计算-0级高加！F95 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4949, 1965), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 35),
            # 汽轮机计算-0级高加！F92 i_steam_exhaust_pressure
            ImageInfo('0', (4957, 1861), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)), 35),
            # 汽轮机计算-0级高加！F99 i_steam_exhaust_flow
            ImageInfo('0', (5213, 1957), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)), 35),
            ImageInfo('0', (5217, 1857), "--", 35),
            ImageInfo('0', (5289, 2569), "--", 35),
            ImageInfo('0', (5289, 2665), "--", 35),
            # 汽轮机计算0级高加!F24 e_steam_extraction_select
            ImageInfo('0', (5363, 1492), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # ImageInfo('0', (5505, 2577), format_value("number", str(turbineBackpressure.)), 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5505, 2669), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            ImageInfo('0', (5537, 1865), "--", 35),
            ImageInfo('0', (5541, 1969), "--", 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5753, 1957), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            ImageInfo('0', (5757, 1865), "30/43", 35),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6221, 1245), format_value("number", str(circulatingWater.v_evaporation_loss)), 35),
            # 循环水K22 p_select_f
            ImageInfo('0', (6361, 2765), format_value("number", str(circulatingWater.p_select_f)), 35),
            # 循环水E19 v_circulating_pool_size
            ImageInfo('0', (6605, 3443), format_value("number", str(circulatingWater.v_circulating_pool_size)), 35),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (7173, 1234), format_value("number", str(circulatingWater.v_partial_blow_loss)), 35),
            # 循环水E20 v_circulating_pool_long
            ImageInfo('0', (8180, 3293), format_value("number", str(circulatingWater.v_circulating_pool_long)), 35),
        ]


    def p2_b_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_three = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount
        plus_35_36 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_35_36 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount

        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        multiply_f33_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design

        return [
            # 锅炉辅机e33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (389, 3063), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 35),
            # 锅炉辅机！E32 c_drum_pressure
            ImageInfo('0', (393, 2973), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 35),
            # 锅炉辅机！G58 p_inlet_pressure
            ImageInfo('0', (395, 1687), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 35),
            # 汽轮机计算-0级高加!C32 hh1_water_enthalpy
            ImageInfo('0', (397, 1771), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 35),
            ImageInfo('0', (611, 2977), "--", 35),
            # 锅炉辅机!E31/1000 c_sewage_quantity/1000
            ImageInfo('0', (613, 3065), format_value("number", str(sewage_quantity)), 35),
            # 汽轮机计算-0级高加！B32 hh1_water_temperature
            ImageInfo('0', (679, 1681), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (685, 1777), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (905, 949), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-0级高加！G34 d_work_pressure
            ImageInfo('0', (1317, 3963), format_value("number", str(turbineBackpressure.d_work_pressure)), 35),
            # 汽轮机计算-0级高加！C34 d_water_enthalpy
            ImageInfo('0', (1319, 4059), format_value("number", str(turbineBackpressure.d_water_enthalpy)), 35),
            # 汽轮机计算-0级高加！I34 d_extraction_pressure
            ImageInfo('0', (1575, 2355), format_value("number", str(turbineBackpressure.d_extraction_pressure)), 35),
            # 汽轮机计算-0级高加！J34 d_extraction_enthalpy
            ImageInfo('0', (1577, 2449), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)), 35),
            # 汽轮机计算-0级高加！B34 d_water_temperature
            ImageInfo('0', (1616, 3966), format_value("number", str(turbineBackpressure.d_water_temperature)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1620, 4059), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-0级高加！K34 d_extraction_amount
            ImageInfo('0', (1861, 2451), format_value("number", str(turbineBackpressure.d_extraction_amount)), 35),
            ImageInfo('0', (1867, 2355), "--", 35),
            # 锅炉计算!G22 f_steam_enthalpy_design
            ImageInfo('0', (2163, 495), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)), 35),
            # 锅炉计算!G20 f_steam_pressure_design
            ImageInfo('0', (2167, 401), format_value("number", str(furnaceCalculation.f_steam_pressure_design)), 35),
            # 汽轮机计算-0级高加！F33 h_pressure
            ImageInfo('0', (2197, 4106), format_value("number", str(turbineBackpressure.h_pressure)), 35),
            # 汽轮机计算-0级高加！H33 h_enthalpy
            ImageInfo('0', (2201, 4200), format_value("number", str(turbineBackpressure.h_enthalpy)), 35),
            # 汽轮机计算-0级高加！C35 lh1_water_enthalpy
            ImageInfo('0', (2213, 3235), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 35),
            ImageInfo('0', (2217, 3147), "--", 35),
            # 汽轮机计算-0级高加！F26 e_throttle_flow
            ImageInfo('0', (2379, 487), format_value("number", str(turbineBackpressure.e_throttle_flow)), 35),
            ImageInfo('0', (2395, 403), "--", 35),
            # 汽轮机计算-0级高加！B35 lh1_water_temperature
            ImageInfo('0', (2457, 3131), format_value("number", str(turbineBackpressure.lh1_water_temperature)), 35),
            # lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2461, 3235), format_value("number", str(plus_three)), 35),
            # 汽轮机计算-0级高加！D33 h_temperature
            ImageInfo('0', (2568, 4106), format_value("number", str(turbineBackpressure.h_temperature)), 35),
            # 锅炉计算G19 * 汽轮机0级高加J33
            ImageInfo('0', (2568, 4196), format_value("number", str(multiply_f33_g19)), 35),
            # 汽轮机计算-0级高加！I35 lh1_extraction_pressure
            ImageInfo('0', (2843, 2365), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)), 35),
            # 汽轮机计算-0级高加！J35 lh1_extraction_enthalpy
            ImageInfo('0', (2847, 2463), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)), 35),
            ImageInfo('0', (2895, 3433), "--", 35),
            # 汽轮机计算-0级高加！F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (2903, 3527), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)), 35),
            # 汽轮机计算-0级高加！C36 lh2_water_enthalpy
            ImageInfo('0', (2972, 3233), format_value("number", str(turbineBackpressure.lh2_water_enthalpy)), 35),
            ImageInfo('0', (2975, 3137), "--", 35),
            ImageInfo('0', (3079, 2367), "--", 35),
            # 汽轮机0级高加K35 lh1_extraction_amount
            ImageInfo('0', (3083, 2461), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机0级高加K35 lh1_extraction_amount
            ImageInfo('0', (3135, 3527), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机计算-0级高加！E35 lh1_saturated_water_temperature
            ImageInfo('0', (3137, 3435), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)), 35),
            # 汽轮机计算-0级高加！(K35+K35+F99) lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3215, 3235), format_value("number", str(plus_three)), 35),
            # 汽轮机计算-0级高加！B36 lh2_water_temperature 
            ImageInfo('0', (3225, 3141), format_value("number", str(turbineBackpressure.lh2_water_temperature)), 35),
            # 汽轮机计算-0级高加！F24 e_steam_extraction_select
            ImageInfo('0', (3253, 1457), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 汽轮机计算-0级高加！J36 lh2_extraction_enthalpy
            ImageInfo('0', (3455, 2461), format_value("number", str(turbineBackpressure.lh2_extraction_enthalpy)), 35),
            # 汽轮机计算-0级高加！I36 lh2_extraction_pressure
            ImageInfo('0', (3463, 2367), format_value("number", str(turbineBackpressure.lh2_extraction_pressure)), 35),
            ImageInfo('0', (3545, 3425), "--", 35),
            # 汽轮机计算-0级高加！F36 lh2_saturated_water_enthalpy
            ImageInfo('0', (3545, 3527), format_value("number", str(turbineBackpressure.lh2_saturated_water_enthalpy)), 35),
            # 汽轮机计算-0级高加！F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3557, 1215), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)), 35),
            # 汽轮机计算-0级高加！F68 i_exhaust_point_pressure
            ImageInfo('0', (3559, 1125), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)), 35),
            # 汽轮机0级高加K36 lh2_extraction_amount
            ImageInfo('0', (3693, 2461), format_value("number", str(turbineBackpressure.lh2_extraction_amount)), 35),
            ImageInfo('0', (3695, 2369), "--", 35),
            # 汽轮机计算-0级高加！C38 c_water_enthalpy
            ImageInfo('0', (3695, 3237), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 35),
            ImageInfo('0', (3697, 3143), "--", 35),
            # 汽轮机计算-0级高加！E36 lh2_saturated_water_temperature
            ImageInfo('0', (3787, 3431), format_value("number", str(turbineBackpressure.lh2_saturated_water_temperature)), 35),
            # 汽轮机计算-0级高加！(K35+K36) lh1_extraction_amount+lh2_extraction_amount
            ImageInfo('0', (3793, 3527), format_value("number", str(plus_35_36)), 35),
            # 汽轮机计算-0级高加！F72 i_exhaust_point_flow
            ImageInfo('0', (3798, 1213), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)), 35),
            # 汽轮机计算-0级高加！F69 i_exhaust_point_temperature
            ImageInfo('0', (3800, 1121), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)), 35),
            # 汽轮机计算-0级高加！B38 c_water_temperature
            ImageInfo('0', (3933, 3141), format_value("number", str(turbineBackpressure.c_water_temperature)), 35),
            # 汽轮机计算-0级高加！(K35+K35+F99) lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3933, 3237), format_value("number", str(plus_three)), 35),
            # 汽轮机计算-0级高加！F92 i_steam_exhaust_pressure
            ImageInfo('0', (4534, 1873), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)), 35),
            # 汽轮机计算-0级高加！F95 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4534, 1957), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 35),
            ImageInfo('0', (4800, 1869), "--", 35),
            # 汽轮机计算-0级高加！F99 i_steam_exhaust_flow
            ImageInfo('0', (4802, 1967), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)), 35),
            ImageInfo('0', (4860, 2575), "--", 35),
            ImageInfo('0', (4864, 2667), "--", 35),
            # 汽轮机计算0级高加!F24 e_steam_extraction_select
            ImageInfo('0', (4944, 1507), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5074, 2665), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            ImageInfo('0', (5082, 2567), "20/23", 35),
            ImageInfo('0', (5112, 1867), "--", 35),
            ImageInfo('0', (5114, 1965), "--", 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5324, 1967), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            ImageInfo('0', (5326, 1871), "30/43", 35),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6088, 1433), format_value("number", str(circulatingWater.v_evaporation_loss)), 35),
            # 循环水K24 p_count
            ImageInfo('0', (6182, 1965), format_value("number", str(circulatingWater.p_count)), 35),
            # 循环水K26 p_select_s
            ImageInfo('0', (6526, 1963), format_value("number", str(circulatingWater.p_select_s)), 35),
            # 循环水E19 v_circulating_pool_size
            ImageInfo('0', (6736, 3543), format_value("number", str(circulatingWater.v_circulating_pool_size)), 35),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (6998, 1431), format_value("number", str(circulatingWater.v_partial_blow_loss)), 35),
            # 循环水E20 v_circulating_pool_long
            ImageInfo('0', (8600, 3403), format_value("number", str(circulatingWater.v_circulating_pool_long)), 35),
        ]

    def p3_a_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_35_93 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_35_93 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.i_steam_exhaust_flow

        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        multiply_f33_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design

        return [
            # 锅炉辅机E33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (753, 3073), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 35),
            # 汽轮机计算-1级高加F32 hh1_saturated_water_enthalpy
            ImageInfo('0', (755, 2575), format_value("number", str(turbineBackpressure.hh1_saturated_water_enthalpy)), 35),
            # 汽轮机计算-1级高加C32 hh1_water_enthalpy
            ImageInfo('0', (759, 1763), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 35),
            # 锅炉辅机E32 c_drum_pressure
            ImageInfo('0', (759, 2977), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 35),
            # 锅炉辅机E58 p_inlet_pressure
            ImageInfo('0', (761, 1669), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 35),
            # --
            ImageInfo('0', (761, 2487), '--', 35),
            # 锅炉辅机E31 c_sewage_quantity/1000
            ImageInfo('0', (975, 3075), format_value("number", str(sewage_quantity)), 35),
            # --
            ImageInfo('0', (981, 2977), '--', 35),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1047, 1767), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-1级高加B32 hh1_water_temperature
            ImageInfo('0', (1057, 1661), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 35),
            # 汽轮机计算-1级高加K32 hh1_extraction_amount
            ImageInfo('0', (1057, 2575), format_value("number", str(turbineBackpressure.hh1_extraction_amount)), 35),
            # 汽轮机计算-1级高加E32 hh1_saturated_water_temperature
            ImageInfo('0', (1059, 2491), format_value("number", str(turbineBackpressure.hh1_saturated_water_temperature)), 35),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1273, 937), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-1级高加C34 d_water_enthalpy
            ImageInfo('0', (1691, 4081), format_value("number", str(turbineBackpressure.d_water_enthalpy)), 35),
            # 汽轮机计算-1级高加G34 d_work_pressure
            ImageInfo('0', (1697, 3981), format_value("number", str(turbineBackpressure.d_work_pressure)), 35),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1993, 4081), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-1级高加B34 d_water_temperature
            ImageInfo('0', (1997, 3979), format_value("number", str(turbineBackpressure.d_water_temperature)), 35),
            # 汽轮机计算-1级高加J32 hh1_extraction_enthalpy
            ImageInfo('0', (2303, 1821), format_value("number", str(turbineBackpressure.hh1_extraction_enthalpy)), 35),
            # 汽轮机计算-1级高加I32 hh1_extraction_pressure
            ImageInfo('0', (2305, 1729), format_value("number", str(turbineBackpressure.hh1_extraction_pressure)), 35),
            # 锅炉计算G20 f_steam_pressure_design
            ImageInfo('0', (2553, 369), format_value("number", str(furnaceCalculation.f_steam_pressure_design)), 35),
            # 锅炉计算G22 f_steam_enthalpy_design
            ImageInfo('0', (2553, 469), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)), 35),
            # 汽轮机计算-1级高加F33 h_pressure
            ImageInfo('0', (2587, 4125), format_value("number", str(turbineBackpressure.h_pressure)), 35),
            # 汽轮机计算-1级高加H33 h_enthalpy
            ImageInfo('0', (2591, 4221), format_value("number", str(turbineBackpressure.h_enthalpy)), 35),
            # 汽轮机计算-1级高加K32 hh1_extraction_amount
            ImageInfo('0', (2593, 1823), format_value("number", str(turbineBackpressure.hh1_extraction_amount)), 35),
            # --
            ImageInfo('0', (2595, 1729), '--', 35),
            # 汽轮机计算-1级高加J34 d_extraction_enthalpy
            ImageInfo('0', (2729, 2447), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)), 35),
            # 汽轮机计算-1级高加I34 d_extraction_pressure
            ImageInfo('0', (2733, 2353), format_value("number", str(turbineBackpressure.d_extraction_pressure)), 35),
            # 汽轮机计算-1级高加C35 lh1_water_enthalpy
            ImageInfo('0', (2771, 3241), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 35),
            # 锅炉计算G21 f_steam_temperature_design
            ImageInfo('0', (2773, 365), format_value("number", str(furnaceCalculation.f_steam_temperature_design)), 35),
            # --
            ImageInfo('0', (2775, 3145), '--', 35),
            # 汽轮机计算-1级高加F26 e_steam_extraction_select
            ImageInfo('0', (2777, 461), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 汽轮机计算-1级高加J33 h_amount * 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (2951, 4215), format_value("number", str(multiply_f33_g19)), 35),
            # 汽轮机计算-1级高加D33 h_temperature
            ImageInfo('0', (2971, 4125), format_value("number", str(turbineBackpressure.h_temperature)), 35),
            # --
            ImageInfo('0', (3013, 2349), '--', 35),
            # 汽轮机计算-1级高加K34 d_extraction_amount
            ImageInfo('0', (3019, 2447), format_value("number", str(turbineBackpressure.d_extraction_amount)), 35),
            # 汽轮机计算-1级高加B35 lh1_water_temperature
            ImageInfo('0', (3053, 3147), format_value("number", str(turbineBackpressure.lh1_water_temperature)), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount+F93 i_steam_exhaust_flow
            ImageInfo('0', (3057, 3243), format_value("number", str(plus_35_93)), 35),
            # 汽轮机计算-1级高加J33 h_amount * 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (3653, 1447), format_value("number", str(multiply_f33_g19)), 35),
            # 汽轮机计算-1级高加F24 e_steam_extraction_select
            ImageInfo('0', (3654, 1447), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 汽轮机计算-1级高加J35 lh1_extraction_enthalpy
            ImageInfo('0', (3654, 2519), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)), 35),
            # 汽轮机计算-1级高加F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (3656, 3235), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)), 35),
            # 汽轮机计算-1级高加I35 lh1_extraction_pressure
            ImageInfo('0', (3658, 2425), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)), 35),
            # --
            ImageInfo('0', (3660, 3141), '--', 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount
            ImageInfo('0', (3934, 2521), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount
            ImageInfo('0', (3936, 3241), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机计算-1级高加E35 lh1_saturated_water_temperature
            ImageInfo('0', (3942, 3145), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)), 35),
            # --
            ImageInfo('0', (3954, 2425), '--', 35),
            # 汽轮机计算-1级高加F68 i_exhaust_point_pressure
            ImageInfo('0', (3965, 1109), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)), 35),
            # 汽轮机计算-1级高加F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3965, 1193), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)), 35),
            # 汽轮机计算-1级高加F69 i_exhaust_point_temperature
            ImageInfo('0', (4201, 1101), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)), 35),
            # 汽轮机计算-1级高加F72 i_exhaust_point_flow
            ImageInfo('0', (4205, 1201), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)), 35),
            # 汽轮机计算-1级高加C38 c_water_enthalpy
            ImageInfo('0', (4428, 3237), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 35),
            # --
            ImageInfo('0', (4432, 3141), '--', 35),
            # 汽轮机计算-1级高加B38 c_water_temperature
            ImageInfo('0', (4710, 3143), format_value("number", str(turbineBackpressure.c_water_temperature)), 35),
            # 汽轮机计算-1级高加K35+F93 lh1_extraction_amount + i_steam_exhaust_flow
            ImageInfo('0', (4716, 3237), format_value("number", str(plus_35_93)), 35),
            # 汽轮机计算-1级高加F93 i_steam_exhaust_flow  -->F86 i_steam_exhaust_pressure
            ImageInfo('0', (4948, 1859), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)), 35),
            # 汽轮机计算-1级高加F96 i_calculation_error -->F89 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4954, 1959), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 35),
            # 汽轮机计算-1级高加F93 i_steam_exhaust_flow
            ImageInfo('0', (5190, 1957), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)), 35),
            # --
            ImageInfo('0', (5192, 1863), '--', 35),
            # --
            ImageInfo('0', (5278, 2669), '--', 35),
            # --
            ImageInfo('0', (5282, 2569), '--', 35),
            # 汽轮机计算-1级高加F24 e_steam_extraction_select
            ImageInfo('0', (5364, 1495), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 循环水系统计算E9 v_total_circulating_water_select
            ImageInfo('0', (5492, 2667), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            # --
            ImageInfo('0', (5502, 2573), u'20/33', 35),
            # --
            ImageInfo('0', (5528, 1951), '--', 35),
            # --
            ImageInfo('0', (5534, 1857), '--', 35),
            # --
            ImageInfo('0', (5748, 1855), u'30/43', 35),
            # 循环水系统计算E9 v_total_circulating_water_select
            ImageInfo('0', (5748, 1951), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            # 循环水系统计算E14 v_evaporation_loss
            ImageInfo('0', (6222, 1239), format_value("number", str(circulatingWater.v_evaporation_loss)), 35),
            # 循环水系统计算K22 p_select_f
            ImageInfo('0', (6334, 2827), format_value("number", str(circulatingWater.p_select_f)), 35),
            # 循环水系统计算E19 v_circulating_pool_size
            ImageInfo('0', (6610, 3441), format_value("number", str(circulatingWater.v_circulating_pool_size)), 35),
            # (循环水系统计算E16) v_partial_blow_loss
            ImageInfo('0', (7170, 1241), format_value("number", str(circulatingWater.v_partial_blow_loss)), 35),
            # 循环水系统计算E20 v_circulating_pool_long
            ImageInfo('0', (8186, 3285), format_value("number", str(circulatingWater.v_circulating_pool_long)), 35)
        ]

    def p3_b_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_35_93 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_35_93 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.i_steam_exhaust_flow

        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        multiply_f33_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        return [
            # 汽轮机计算-1级高加!C32 hh1_water_enthalpy
            ImageInfo('0', (385, 1773), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 35),
            # 汽轮机计算-1级高加F32 hh1_saturated_water_enthalpy
            ImageInfo('0', (391, 2577), format_value("number", str(turbineBackpressure.hh1_saturated_water_enthalpy)), 35),
            # 锅炉辅机F33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (393, 3077), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 35),
            # --
            ImageInfo('0', (395, 2481), '--', 35),
            # 锅炉辅机F32 c_drum_pressure
            ImageInfo('0', (395, 2977), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 35),
            # 锅炉辅机G58 p_inlet_pressure
            ImageInfo('0', (397, 1687), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 35),
            # 锅炉辅机F31/1000 c_sewage_quantity/1000
            ImageInfo('0', (607, 3069), format_value("number", str(sewage_quantity)), 35),
            # --
            ImageInfo('0', (619, 2981), '--', 35),
            # 汽轮机计算-1级高加B32 hh1_water_temperature
            ImageInfo('0', (679, 1683), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 35),
            # 锅炉计算G19 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (681, 1779), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-1级高加E32 hh1_saturated_water_temperature
            ImageInfo('0', (685, 2477), format_value("number", str(turbineBackpressure.hh1_saturated_water_temperature)), 35),
            # 汽轮机计算-1级高加K32 hh1_extraction_amount
            ImageInfo('0', (691, 2579), format_value("number", str(turbineBackpressure.hh1_extraction_amount)), 35),
            # 锅炉计算G19 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (901, 951), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-1级高加C34 d_water_enthalpy
            ImageInfo('0', (1305, 4061), format_value("number", str(turbineBackpressure.d_water_enthalpy)), 35),
            # 汽轮机计算-1级高加G34 d_work_pressure
            ImageInfo('0', (1315, 3963), format_value("number", str(turbineBackpressure.d_work_pressure)), 35),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1611, 4057), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-1级高加B34 d_water_temperature
            ImageInfo('0', (1617, 3961), format_value("number", str(turbineBackpressure.d_water_temperature)), 35),
            # 汽轮机计算-1级高加J32 hh1_extraction_enthalpy
            ImageInfo('0', (1923, 1835), format_value("number", str(turbineBackpressure.hh1_extraction_enthalpy)), 35),
            # 汽轮机计算-1级高加I32 hh1_extraction_pressure
            ImageInfo('0', (1925, 1743), format_value("number", str(turbineBackpressure.hh1_extraction_pressure)), 35),
            # 锅炉计算G22 f_steam_enthalpy_design
            ImageInfo('0', (2163, 495), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)), 35),
            # 锅炉计算G20 f_steam_pressure_design
            ImageInfo('0', (2169, 401), format_value("number", str(furnaceCalculation.f_steam_pressure_design)), 35),
            # 汽轮机计算-1级高加F33 h_pressure
            ImageInfo('0', (2197, 4107), format_value("number", str(turbineBackpressure.h_pressure)), 35),
            # 汽轮机计算-1级高加H33 h_enthalpy
            ImageInfo('0', (2199, 4199), format_value("number", str(turbineBackpressure.h_enthalpy)), 35),
            # 汽轮机计算-1级高加K32 hh1_extraction_amount
            ImageInfo('0', (2213, 1833), format_value("number", str(turbineBackpressure.hh1_extraction_amount)), 35),
            ImageInfo('0', (2221, 1745), '--', 35),
            # 汽轮机计算-1级高加I34 d_extraction_pressure
            ImageInfo('0', (2347, 2353), format_value("number", str(turbineBackpressure.d_extraction_pressure)), 35),
            # 汽轮机计算-1级高加J34 d_extraction_enthalpy
            ImageInfo('0', (2347, 2453), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)), 35),
            # 汽轮机计算-1级高加C35 lh1_water_enthalpy
            ImageInfo('0', (2377, 3229), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 35),
            # 汽轮机计算-1级高加F26 e_steam_extraction_select
            ImageInfo('0', (2379, 497), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 锅炉计算G21 f_steam_temperature_design
            ImageInfo('0', (2383, 401), format_value("number", str(furnaceCalculation.f_steam_temperature_design)), 35),
            # --
            ImageInfo('0', (2383, 3139), '--', 35),
            # 汽轮机计算-1级高加J33 h_amount * 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (2557, 4197), format_value("number", str(multiply_f33_g19)), 35),
            # 汽轮机计算-1级高加D33 h_temperature
            ImageInfo('0', (2563, 4105), format_value("number", str(turbineBackpressure.h_temperature)), 35),
            # --
            ImageInfo('0', (2625, 2361), '--', 35),
            # 汽轮机计算-1级高加K34 d_extraction_amount
            ImageInfo('0', (2631, 2451), format_value("number", str(turbineBackpressure.d_extraction_amount)), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount + 汽轮机计算-1级高加F93 i_steam_exhaust_flow
            ImageInfo('0', (2663, 3229), format_value("number", str(plus_35_93)), 35),
            # 汽轮机计算-1级高加B35 lh1_water_temperature
            ImageInfo('0', (2671, 3137), format_value("number", str(turbineBackpressure.lh1_water_temperature)), 35),
            # 汽轮机计算-1级高加F24 e_steam_extraction_select
            ImageInfo('0', (3251, 1457), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 汽轮机计算-1级高加J35 lh1_extraction_enthalpy
            ImageInfo('0', (3251, 2525), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)), 35),
            # 汽轮机计算-1级高加I35 lh1_extraction_pressure
            ImageInfo('0', (3253, 2427), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)), 35),
            # 汽轮机计算-1级高加F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (3253, 3231), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)), 35),
            # --
            ImageInfo('0', (3261, 3141), '--', 35),
            # --
            ImageInfo('0', (3533, 2431), '--', 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount
            ImageInfo('0', (3535, 3233), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount
            ImageInfo('0', (3537, 2525), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机计算-1级高加E35 lh1_saturated_water_temperature
            ImageInfo('0', (3543, 3137), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)), 35),
            # 汽轮机计算-1级高加F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3559, 1207), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)), 35),
            # 汽轮机计算-1级高加F68 i_exhaust_point_pressure
            ImageInfo('0', (3561, 1117), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)), 35),
            # 汽轮机计算-1级高加F72 i_exhaust_point_flow
            ImageInfo('0', (3795, 1215), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)), 35),
            # 汽轮机计算-1级高加F69 i_exhaust_point_temperature
            ImageInfo('0', (3799, 1119), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)), 35),
            # 汽轮机计算-1级高加C38 c_water_enthalpy
            ImageInfo('0', (4019, 3229), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 35),
            ImageInfo('0', (4023, 3135), '--', 35),
            # 汽轮机计算-1级高加B38 c_water_temperature
            ImageInfo('0', (4301, 3139), format_value("number", str(turbineBackpressure.c_water_temperature)), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount + 汽轮机计算-1级高加F93 i_steam_exhaust_flow
            ImageInfo('0', (4305, 3229), format_value("number", str(plus_35_93)), 35),
            # 汽轮机计算-1级高加F86 i_steam_exhaust_pressure
            ImageInfo('0', (4533, 1867), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)), 35),
            # 汽轮机计算-1级高加F89 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4533, 1961), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 35),
            # 汽轮机计算-1级高加F89 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4773, 1961), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 35),
            # --
            ImageInfo('0', (4777, 1871), '--', 35),
            # --
            ImageInfo('0', (4859, 2577), '--', 35),
            # --
            ImageInfo('0', (4867, 2673), '--', 35),
            # 汽轮机计算-1级高加F24 e_steam_extraction_select
            ImageInfo('0', (4945, 1509), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 常量
            ImageInfo('0', (5077, 2577), '20/33', 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5081, 2661), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            # --
            ImageInfo('0', (5115, 1873), '--', 35),
            # --
            ImageInfo('0', (5115, 1975), '--', 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5327, 1967), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            # --
            ImageInfo('0', (5333, 1871), '30/43', 35),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6089, 1433), format_value("number", str(circulatingWater.v_evaporation_loss)), 35),
            # 循环水K24 p_count
            ImageInfo('0', (6155, 1987), format_value("number", str(circulatingWater.p_count)), 35),
            # 循环水K26 p_select_s
            ImageInfo('0', (6497, 1987), format_value("number", str(circulatingWater.p_select_s)), 35),
            # 循环水E19 v_circulating_pool_size
            ImageInfo('0', (6733, 3549), format_value("number", str(circulatingWater.v_circulating_pool_size)), 35),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (6995, 1437), format_value("number", str(circulatingWater.v_partial_blow_loss)), 35),
            # 循环水E20 v_circulating_pool_long
            ImageInfo('0', (8602, 3399), format_value("number", str(circulatingWater.v_circulating_pool_long)), 35)
        ]


    # 原则性热力系统图--0JG+
    def p5_b_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        plus_35_99 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_35_99 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.i_steam_exhaust_flow
        return [
            # 汽轮机计算0级高加!C32 hh1_water_enthalpy
            ImageInfo('0', (405, 1773), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 50),
            # 锅炉辅机！E32 c_drum_pressure
            ImageInfo('0', (405, 2973), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 50),
            # 锅炉辅机！G58 p_inlet_pressure
            ImageInfo('0', (409, 1683), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 50),
            # 锅炉辅机！E33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (409, 3067), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 50),
            # 锅炉辅机！E31/1000 c_sewage_quantity/1000
            ImageInfo('0', (611, 3069), format_value("number", str(sewage_quantity)), 50),
            # --
            ImageInfo('0', (623, 2977), "--", 50),
            # 汽轮机计算0级高加!B32 hh1_water_temperature
            ImageInfo('0', (689, 1679), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 50),
            # 锅炉计算!G19 f_steam_flow_design
            ImageInfo('0', (691, 1775), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 50),
            # 锅炉计算!G19 f_steam_flow_design
            ImageInfo('0', (909, 949), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 50),
            # 汽轮机计算0级高加!G34 d_work_pressure
            ImageInfo('0', (1313, 3969), format_value("number", str(turbineBackpressure.d_work_pressure)), 50),
            # 汽轮机计算0级高加!C34 d_water_enthalpy
            ImageInfo('0', (1313, 4063), format_value("number", str(turbineBackpressure.d_water_enthalpy)), 50),
            # 汽轮机计算0级高加!I34 d_extraction_pressure
            ImageInfo('0', (1581, 2353), format_value("number", str(turbineBackpressure.d_extraction_pressure)), 50),
            # 汽轮机计算0级高加!J34 d_extraction_enthalpy
            ImageInfo('0', (1585, 2447), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)), 50),
            # 锅炉计算!G19 f_steam_flow_design
            ImageInfo('0', (1619, 4071), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 50),
            # 汽轮机计算0级高加!B34 d_water_temperature
            ImageInfo('0', (1623, 3971), format_value("number", str(turbineBackpressure.d_water_temperature)), 50),
            # 汽轮机计算0级高加!K34 d_extraction_amount
            ImageInfo('0', (1859, 2453), format_value("number", str(turbineBackpressure.d_extraction_amount)), 50),
            # --
            ImageInfo('0', (1865, 2357), "--", 50),
            # 锅炉计算!G20 f_steam_pressure_design
            ImageInfo('0', (2169, 399), format_value("number", str(furnaceCalculation.f_steam_pressure_design)), 50),
            # 锅炉计算!G22 f_steam_enthalpy_design
            ImageInfo('0', (2169, 499), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)), 50),
            # 汽轮机计算0级高加!F33 h_pressure
            ImageInfo('0', (2207, 4107), format_value("number", str(turbineBackpressure.h_pressure)), 50),
            # 汽轮机计算0级高加!H33 h_enthalpy
            ImageInfo('0', (2219, 4201), format_value("number", str(turbineBackpressure.h_enthalpy)), 50),
            # 汽轮机计算0级高加!F26 e_throttle_flow
            ImageInfo('0', (2387, 495), format_value("number", str(turbineBackpressure.e_throttle_flow)), 50),
            # 锅炉计算!G21 f_steam_temperature_design
            ImageInfo('0', (2391, 409), format_value("number", str(furnaceCalculation.f_steam_temperature_design)), 50),
            # --
            ImageInfo('0', (2517, 3145), "--", 50),
            # 汽轮机计算0级高加!C35 lh1_water_enthalpy
            ImageInfo('0', (2521, 3250), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 50),
            ImageInfo('0', (2575, 4113), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 50),
            ImageInfo('0', (2575, 4199), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 50),
            # 汽轮机计算0级高加!B35 lh1_water_temperature
            ImageInfo('0', (2761, 3143), format_value("number", str(turbineBackpressure.lh1_water_temperature)), 50),
            # 汽轮机计算0级高加!K35+F99 lh1_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2761, 3233), format_value("number", str(plus_35_99)), 50),
            # 汽轮机计算0级高加!I35 lh1_extraction_pressure
            ImageInfo('0', (3201, 2369), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)), 50),
            # 汽轮机计算0级高加!J35 lh1_extraction_enthalpy
            ImageInfo('0', (3201, 2463), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)), 50),
            # 汽轮机计算0级高加!F24 e_steam_extraction_select
            ImageInfo('0', (3255, 1461), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 50),
            # 汽轮机计算0级高加!F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (3369, 3529), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)), 50),
            # ---
            ImageInfo('0', (3371, 3439), "--", 50),
            # 汽轮机计算0级高加!K35 lh1_extraction_amount
            ImageInfo('0', (3439, 2461), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 50),
            # --
            ImageInfo('0', (3443, 2367), "--", 50),
            # 汽轮机计算0级高加!F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3565, 1219), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)), 50),
            # 汽轮机计算0级高加!F68 i_exhaust_point_pressure
            ImageInfo('0', (3567, 1125), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)), 50),
            # 汽轮机计算0级高加!E35 lh1_saturated_water_temperature
            ImageInfo('0', (3601, 3445), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)), 50),
            # 汽轮机计算0级高加!K35 lh1_extraction_amount
            ImageInfo('0', (3605, 3531), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 50),
            # --
            ImageInfo('0', (3697, 3147), "--", 50),
            # 汽轮机计算0级高加!C38 c_water_enthalpy
            ImageInfo('0', (3701, 3237), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 50),
            # 汽轮机计算0级高加!F69 i_exhaust_point_temperature
            ImageInfo('0', (3803, 1129), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)), 50),
            # 汽轮机计算0级高加!F72 i_exhaust_point_flow
            ImageInfo('0', (3805, 1217), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)), 50),
            # 汽轮机计算0级高加!B38 c_water_temperature
            ImageInfo('0', (3937, 3145), format_value("number", str(turbineBackpressure.c_water_temperature)), 50),
            # 汽轮机计算0级高加!K35+F99 h1_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3937, 3237), format_value("number", str(plus_35_99)), 50),
            # 汽轮机计算0级高加!F92 i_steam_exhaust_pressure
            ImageInfo('0', (4537, 1879), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)), 50),
            # 汽轮机计算0级高加!F95 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4537, 1975), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 50),
            # 汽轮机计算0级高加!F99 i_steam_exhaust_flow
            ImageInfo('0', (4799, 1971), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)), 50),
            # --
            ImageInfo('0', (4805, 1885), "--", 50),
            # --
            ImageInfo('0', (4861, 2575), "--", 50),
            # --
            ImageInfo('0', (4861, 2665), "--", 50),
            # 汽轮机计算0级高加!F24 e_steam_extraction_select
            ImageInfo('0', (4943, 1507), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 50),
            # 20/33
            ImageInfo('0', (5079, 2575), "20/33", 50),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5081, 2667), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 50),
            # --
            ImageInfo('0', (5117, 1883), "--", 50),
            # --
            ImageInfo('0', (5119, 1979), "--", 50),
            # 30/43
            ImageInfo('0', (5331, 1889), "30/34", 50),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5331, 1971), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 50),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6215, 1439), format_value("number", str(circulatingWater.v_evaporation_loss)), 50),
            # 循环水K24 p_count
            ImageInfo('0', (6225, 1975), format_value("number", str(circulatingWater.p_count)), 50),
            # 循环水K26 p_select_s
            ImageInfo('0', (6358, 1977), format_value("number", str(circulatingWater.p_select_s)), 50),
            # 循环水E19 v_circulating_pool_size
            ImageInfo('0', (6740, 3545), format_value("number", str(circulatingWater.v_circulating_pool_size)), 50),
            # 循环水F16 v_partial_blow_loss
            ImageInfo('0', (6997, 1431), format_value("number", str(circulatingWater.v_partial_blow_loss)), 50),
            # 循环水E20 v_circulating_pool_long
            ImageInfo('0', (8604, 3399), format_value("number", str(circulatingWater.v_circulating_pool_long)), 50),
        ]


# 原则性热力系统图--0JG+
    def p5_a_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        plus_35_99 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_35_99 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.i_steam_exhaust_flow
        multiply_f33_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        return [
            # 锅炉辅机！G58 p_inlet_pressure
            ImageInfo('0', (759, 1667), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 35),
            # 汽轮机计算-0级高加!C32 hh1_water_enthalpy
            ImageInfo('0', (759, 1771), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 35),
            # 锅炉辅机!E33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (763, 3077), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 35),
            # 锅炉辅机!E32 c_drum_pressure
            ImageInfo('0', (763, 2983), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 35),
            # 锅炉辅机!E31/1000 c_sewage_quantity/1000
            ImageInfo('0', (983, 3077), format_value("number", str(sewage_quantity)), 35),
            # ————
            ImageInfo('0', (983, 2983), "--", 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1055, 1771), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-0级高加！B32 hh1_water_temperature
            ImageInfo('0', (1055, 1667), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1275, 925), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # 汽轮机计算-0级高加！G34 d_work_pressure
            ImageInfo('0', (1689, 3989), format_value("number", str(turbineBackpressure.d_work_pressure)), 35),
            # 汽轮机计算-0级高加！C34 d_water_enthalpy
            ImageInfo('0', (1691, 4085), format_value("number", str(turbineBackpressure.d_water_enthalpy)), 35),
            # 汽轮机计算-0级高加！J34 d_extraction_enthalpy
            ImageInfo('0', (1953, 2453), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)), 35),
            # 汽轮机计算-0级高加！I34 d_extraction_pressure
            ImageInfo('0', (1955, 2359), format_value("number", str(turbineBackpressure.d_extraction_pressure)), 35),
            # 汽轮机计算-0级高加！B34 d_water_temperature
            ImageInfo('0', (1997, 3989), format_value("number", str(turbineBackpressure.d_water_temperature)), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (2001, 4085), format_value("number", str(furnaceCalculation.f_steam_flow_design)), 35),
            # ---
            ImageInfo('0', (2243, 2355), "--", 35),
            # 汽轮机计算-0级高加！K34 d_extraction_amount
            ImageInfo('0', (2243, 2453), format_value("number", str(turbineBackpressure.d_extraction_amount)), 35),
            # 锅炉计算!G20 f_steam_pressure_design
            ImageInfo('0', (2551, 377), format_value("number", str(furnaceCalculation.f_steam_pressure_design)), 35),
            # 锅炉计算!G22 f_steam_enthalpy_design
            ImageInfo('0', (2551, 465), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)), 35),
            # 汽轮机计算-0级高加！F33 h_pressure
            ImageInfo('0', (2588, 4126), format_value("number", str(turbineBackpressure.h_pressure)), 35),
            # 汽轮机计算-0级高加！H33 h_enthalpy
            ImageInfo('0', (2588, 4226), format_value("number", str(turbineBackpressure.h_enthalpy)), 35),
            # 汽轮机计算-0级高加！F26 e_throttle_flow
            ImageInfo('0', (2777, 469), format_value("number", str(turbineBackpressure.e_throttle_flow)), 35),
            # 锅炉计算!G21 f_steam_temperature_design
            ImageInfo('0', (2777, 375), format_value("number", str(furnaceCalculation.f_steam_temperature_design)), 35),
            # 汽轮机计算-0级高加！C35 lh1_water_enthalpy
            ImageInfo('0', (2903, 3245), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)), 35),
            # ---
            ImageInfo('0', (2909, 3151), "--", 35),
            # 汽轮机计算-0级高加！D33 h_temperature
            ImageInfo('0', (2957, 4127), format_value("number", str(turbineBackpressure.h_temperature)), 35),
            # (汽轮机计算-0级高加！J33) * (锅炉计算!G19) h_amount*f_steam_flow_design
            ImageInfo('0', (2959, 4219), format_value("number", str(multiply_f33_g19)), 35),
            # 汽轮机计算-0级高加！B35 lh1_water_temperature
            ImageInfo('0', (3147, 3155), format_value("number", str(turbineBackpressure.lh1_water_temperature)), 35),
            # 汽轮机计算-0级高加！(K35+F99) lh1_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3147, 3247), format_value("number", str(plus_35_99)), 35),
            # 汽轮机计算-0级高加！I35 lh1_extraction_pressure
            ImageInfo('0', (3601, 2367), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)), 35),
            # 汽轮机计算-0级高加！J35 lh1_extraction_enthalpy
            ImageInfo('0', (3601, 2461), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)), 35),
            # 汽轮机计算-0级高加！F24 e_steam_extraction_select
            ImageInfo('0', (3675, 1441), format_value("number", str(turbineBackpressure.e_steam_extraction_select)), 35),
            # 汽轮机计算-0级高加！F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (3773, 3541), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)), 35),
            # --
            ImageInfo('0', (3775, 3451), "--", 35),
            # --
            ImageInfo('0', (3837, 2375), "--", 35),
            # 汽轮机计算-0级高加！K35 lh1_extraction_amount
            ImageInfo('0', (3839, 2457), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机计算-0级高加！F68 i_exhaust_point_pressure
            ImageInfo('0', (3971, 1101), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)), 35),
            # 汽轮机计算-0级高加！F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3973, 1199), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)), 35),
            # 汽轮机计算-0级高加！K35 lh1_extraction_amount
            ImageInfo('0', (4011, 3537), format_value("number", str(turbineBackpressure.lh1_extraction_amount)), 35),
            # 汽轮机计算-0级高加！E35 lh1_saturated_water_temperature
            ImageInfo('0', (4019, 3453), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)), 35),
            # --
            ImageInfo('0', (4099, 3147), "--", 35),
            # 汽轮机计算-0级高加！C38 c_water_enthalpy
            ImageInfo('0', (4099, 3249), format_value("number", str(turbineBackpressure.c_water_enthalpy)), 35),
            # 汽轮机计算-0级高加！F69 i_exhaust_point_temperature
            ImageInfo('0', (4211, 1105), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)), 35),
            # 汽轮机计算-0级高加！F72 i_exhaust_point_flow
            ImageInfo('0', (4211, 1197), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)), 35),
            # 汽轮机计算-0级高加！B38 c_water_temperature
            ImageInfo('0', (4349, 3151), format_value("number", str(turbineBackpressure.c_water_temperature)), 35),
            # 汽轮机计算-0级高加！(K35+F99) h1_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (4351, 3245), format_value("number", str(plus_35_99)), 35),
            # 汽轮机计算-0级高加！F92 i_steam_exhaust_pressure
            ImageInfo('0', (4953, 1857), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)), 35),
            # 汽轮机计算-0级高加！F95 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4959, 1957), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)), 35),
            # 汽轮机计算-0级高加！F99 i_steam_exhaust_flow
            ImageInfo('0', (5219, 1955), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)), 35),
            # --
            ImageInfo('0', (5221, 1863), "--", 35),
            # --
            ImageInfo('0', (5291, 2573), "--", 35),
            # --
            ImageInfo('0', (5293, 2675), "--", 35),
            # 20/33
            ImageInfo('0', (5503, 2575), "20/33", 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5503, 2667), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            # --
            ImageInfo('0', (5537, 1865), "--", 35),
            # --
            ImageInfo('0', (5541, 1969), "--", 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5753, 1959), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            # 30/43
            ImageInfo('0', (5759, 1869), "30/43", 35),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6225, 1237), format_value("number", str(circulatingWater.v_evaporation_loss)), 35),
            # 循环水K22 p_select_f
            ImageInfo('0', (6301, 2847), format_value("number", str(circulatingWater.p_select_f)), 35),
            # 循环水E19 v_circulating_pool_size
            ImageInfo('0', (6613, 3435), format_value("number", str(circulatingWater.v_circulating_pool_size)), 35),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (7173, 1239), format_value("number", str(circulatingWater.v_partial_blow_loss)), 35),
            # 循环水E20 v_circulating_pool_long
            ImageInfo('0', (8188, 3289), format_value("number", str(circulatingWater.v_circulating_pool_long)), 35),
        ]


# 原则性热力系统图7--抽凝
    def p4_a_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        multiply_f34_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f34_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        plus_32_33 = ""
        if turbineBackpressure.hh1_extraction_amount and turbineBackpressure.hh2_extraction_amount:
            plus_32_33 = turbineBackpressure.hh1_extraction_amount + turbineBackpressure.hh2_extraction_amount
        plus_three = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount
        plus_36_37 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_36_37 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount

        return [
            # u'汽轮机计算-抽凝！F32'
            ImageInfo('0', (750, 2061), format_value("number", str(turbineBackpressure.hh1_saturated_water_enthalpy)), 35),
            # u'锅炉辅机F32'
            ImageInfo('0', (753, 2979), format_value("number", str(boilerAuxiliaries.c_drum_pressure)) , 35),
            # --
            ImageInfo('0', (754, 1966), u'--', 35),
            # u'汽轮机计算-抽凝！F33'
            ImageInfo('0', (755, 2577), format_value("number", str(turbineBackpressure.hh2_saturated_water_enthalpy)), 35),
            # u'锅炉辅机G58'
            ImageInfo('0', (759, 1671), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)) , 35),
            # 
            ImageInfo('0', (759, 1763), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 35),
            #  u'锅炉辅机F33'
            ImageInfo('0', (759, 3079), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)), 35),
            # --
            ImageInfo('0', (763, 2483), u'--', 35),
            # --
            ImageInfo('0', (973, 2979), u'--', 35),
            # u'锅炉辅机F31/1000'
            ImageInfo('0', (975, 3073), format_value("number", str(sewage_quantity)), 35),
            # u'汽轮机计算-抽凝！B32'
            ImageInfo('0', (1047, 1667), format_value("number", str(turbineBackpressure.hh1_water_temperature)), 35),
            # u'汽轮机计算-抽凝K32'
            ImageInfo('0', (1047, 2062), format_value("number", str(turbineBackpressure.hh1_extraction_amount)) , 35),
            #  u'汽轮机计算-抽凝E32'
            ImageInfo('0', (1048, 1966), format_value("number", str(turbineBackpressure.hh1_saturated_water_temperature)), 35),
            # u'汽轮机计算-抽凝E33'
            ImageInfo('0', (1051, 2487), format_value("number", str(turbineBackpressure.hh2_saturated_water_temperature)) , 35),
            # u'锅炉计算G19'
            ImageInfo('0', (1053, 1775), format_value("number", str(furnaceCalculation.f_steam_flow_design)) , 35),
            # u'汽轮机计算-抽凝K32+K33'
            ImageInfo('0', (1053, 2577),  format_value("number", str(plus_32_33)), 35),
            # u'锅炉计算G19'
            ImageInfo('0', (1275, 935), format_value("number", str(furnaceCalculation.f_steam_flow_design)) , 35),
            # u'汽轮机计算-抽凝G35'
            ImageInfo('0', (1687, 3983), format_value("number", str(turbineBackpressure.d_work_pressure)) , 35),
            # u'汽轮机计算-抽凝C35'
            ImageInfo('0', (1689, 4083), format_value("number", str(turbineBackpressure.d_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝I35'
            ImageInfo('0', (1955, 2357), format_value("number", str(turbineBackpressure.d_extraction_pressure)) , 35),
            # u'汽轮机计算-抽凝J35'
            ImageInfo('0', (1955, 2449), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)) , 35),
            # u'汽轮机计算-抽凝B35'
            ImageInfo('0', (1989, 3985), format_value("number", str(turbineBackpressure.d_water_temperature)) , 35),
            # u'锅炉计算G19'
            ImageInfo('0', (1991, 4083), format_value("number", str(furnaceCalculation.f_steam_flow_design)) , 35),
            # u'汽轮机计算-抽凝K35'
            ImageInfo('0', (2239, 2451), format_value("number", str(turbineBackpressure.d_extraction_amount)) , 35),
            # --
            ImageInfo('0', (2241, 2361), u'--', 35),
            # u'汽轮机计算-抽凝J32'
            ImageInfo('0', (2349, 1665), format_value("number", str(turbineBackpressure.hh1_extraction_enthalpy)) , 35),
            # u'汽轮机计算-抽凝I32'
            ImageInfo('0', (2351, 1569), format_value("number", str(turbineBackpressure.hh1_extraction_pressure)) , 35),
            # u'汽轮机计算-抽凝I33'
            ImageInfo('0', (2351, 1895), format_value("number", str(turbineBackpressure.hh2_extraction_pressure)) , 35),
            # u'汽轮机计算-抽凝J33'
            ImageInfo('0', (2353, 1985), format_value("number", str(turbineBackpressure.hh2_extraction_enthalpy)) , 35),
            # u'锅炉计算G22'
            ImageInfo('0', (2551, 477), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)) , 35),
            # u'锅炉计算G20'
            ImageInfo('0', (2557, 377), format_value("number", str(furnaceCalculation.f_steam_pressure_design)) , 35),
            # u'汽轮机计算-抽凝F34'
            ImageInfo('0', (2583, 4123), format_value("number", str(turbineBackpressure.h_pressure)) , 35),
            # u'汽轮机计算-抽凝H34'
            ImageInfo('0', (2585, 4225), format_value("number", str(turbineBackpressure.h_enthalpy)) , 35),
            # --
            ImageInfo('0', (2633, 1575), u'--', 35),
            # --
            ImageInfo('0', (2637, 1901), u'--', 35),
            # u'汽轮机计算-抽凝K32'
            ImageInfo('0', (2639, 1663), format_value("number", str(turbineBackpressure.hh1_extraction_amount)) , 35),
            # u'汽轮机计算-抽凝K33'
            ImageInfo('0', (2641, 1985), format_value("number", str(turbineBackpressure.hh2_extraction_amount)) , 35),
            # u'汽轮机计算-抽凝F26'
            ImageInfo('0', (2769, 473), format_value("number", str(turbineBackpressure.e_throttle_flow)) , 35),
            # u'锅炉计算G21'
            ImageInfo('0', (2773, 377), format_value("number", str(furnaceCalculation.f_steam_temperature_design)) , 35),
            # --
            ImageInfo('0', (2815, 3167), u'--', 35),
            # u'汽轮机计算-抽凝C36'
            ImageInfo('0', (2815, 3263), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝J34 * 锅炉计算G19'
            ImageInfo('0', (2947, 4219), format_value("number", str(multiply_f34_g19)) , 35),
            # u'汽轮机计算-抽凝D34'
            ImageInfo('0', (2951, 4127), format_value("number", str(turbineBackpressure.h_temperature)) , 35),
            # u'汽轮机计算-抽凝B36'
            ImageInfo('0', (3031, 3165), format_value("number", str(turbineBackpressure.lh1_water_temperature)) , 35),
            # u'汽轮机计算-抽凝F99+K36+K37'
            ImageInfo('0', (3033, 3260), format_value("number", str(plus_three)), 35),
            # u'汽轮机计算-抽凝J36'
            ImageInfo('0', (3293, 2459), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)) , 35),
            # u'汽轮机计算-抽凝I36'
            ImageInfo('0', (3297, 2369), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)) , 35),
            # --
            ImageInfo('0', (3401, 3427), u'--', 35),
            # u'汽轮机计算-抽凝F36'
            ImageInfo('0', (3409, 3527), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝K36'
            ImageInfo('0', (3519, 2457), format_value("number", str(turbineBackpressure.lh1_extraction_amount)) , 35),
            # --
            ImageInfo('0', (3527, 2363), u'--', 35),
            # u'汽轮机计算-抽凝C37'
            ImageInfo('0', (3579, 3261), format_value("number", str(turbineBackpressure.lh2_water_enthalpy)) , 35),
            # --
            ImageInfo('0', (3587, 3167), u'--', 35),
            # u'汽轮机计算-抽凝E36'
            ImageInfo('0', (3637, 3427), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)) , 35),
            # u'汽轮机计算-抽凝K36'
            ImageInfo('0', (3637, 3527), format_value("number", str(turbineBackpressure.lh1_extraction_amount)) , 35),

            # u'汽轮机计算-抽凝F24'
            ImageInfo('0', (3650, 1441), format_value("number", str(turbineBackpressure.e_steam_extraction_select)) , 35),
            # u'汽轮机计算-抽凝K36+K37+F99'
            ImageInfo('0', (3806, 3265), format_value("number", str(plus_three)), 35),
            # u'汽轮机计算-抽凝B37'
            ImageInfo('0', (3810, 3161), format_value("number", str(turbineBackpressure.lh2_water_temperature)) , 35),
            # u'汽轮机计算-抽凝J37'
            ImageInfo('0', (3932, 2461), format_value("number", str(turbineBackpressure.lh2_extraction_enthalpy)) , 35),
            # u'汽轮机计算-抽凝I37'
            ImageInfo('0', (3940, 2363), format_value("number", str(turbineBackpressure.lh2_extraction_pressure)) , 35),
            # u'汽轮机计算-抽凝F71'
            ImageInfo('0', (3964, 1199), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)) , 35),
            # u'汽轮机计算-抽凝F68'
            ImageInfo('0', (3970, 1097), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)) , 35),
            # --
            ImageInfo('0', (4082, 3439), u'--', 35),
            # u'汽轮机计算-抽凝F37'
            ImageInfo('0', (4084, 3529), format_value("number", str(turbineBackpressure.lh2_saturated_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝K37'
            ImageInfo('0', (4154, 2461), format_value("number", str(turbineBackpressure.lh2_extraction_amount)) , 35),
            # --
            ImageInfo('0', (4156, 2365), u'--', 35),
            # u'汽轮机计算-抽凝F72'
            ImageInfo('0', (4200, 1197), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)) , 35),
            # u'汽轮机计算-抽凝F69'
            ImageInfo('0', (4208, 1099), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)) , 35),
            # --
            ImageInfo('0', (4226, 3161), u'--', 35),
            # u'汽轮机计算-抽凝C38'
            ImageInfo('0', (4229, 3261), format_value("number", str(turbineBackpressure.c_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝K36+K37'
            ImageInfo('0', (4310, 3525), format_value("number", str(plus_36_37))  , 35),
            # u'汽轮机计算-抽凝E37'
            ImageInfo('0', (4318, 3429), format_value("number", str(turbineBackpressure.lh2_saturated_water_temperature)) , 35),
            # u'汽轮机计算-抽凝K36+K37+F99'
            ImageInfo('0', (4397, 3269), format_value("number", str(plus_three)) , 35),
            # u'汽轮机计算-抽凝B38'
            ImageInfo('0', (4398, 3163), format_value("number", str(turbineBackpressure.c_water_temperature)) , 35),
            # u'汽轮机计算-抽凝F95'
            ImageInfo('0', (4948, 1955), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)) , 35),
            # u'汽轮机计算-抽凝F92'
            ImageInfo('0', (4950, 1861), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)) , 35),
            # u'汽轮机计算-抽凝F99'
            ImageInfo('0', (5210, 1957), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)) , 35),
            # --
            ImageInfo('0', (5220, 1857), u'--', 35),
            # --
            ImageInfo('0', (5280, 2573), u'--', 35),
            # --
            ImageInfo('0', (5284, 2667), u'--', 35),
            # u'汽轮机计算-抽凝F24'
            ImageInfo('0', (5364, 1495), format_value("number", str(turbineBackpressure.e_steam_extraction_select)) , 35),
            # 20/33
            ImageInfo('0', (5498, 2569), u'20/33', 35),
            # '循环水系统计算E9'
            ImageInfo('0', (5500, 2667), format_value("number", str(circulatingWater.v_total_circulating_water_select)) , 35),
            # --
            ImageInfo('0', (5530, 1861), u'--', 35),
            # --
            ImageInfo('0', (5538, 1957), u'--', 35),
            # 30/43
            ImageInfo('0', (5748, 1859), u'30/43', 35),
            # u'循环水系统计算E9'
            ImageInfo('0', (5752, 1951), format_value("number", str(circulatingWater.v_total_circulating_water_select)) , 35),
            # u'循环水系统计算E14'
            ImageInfo('0', (6224, 1237), format_value("number", str(circulatingWater.v_evaporation_loss)) , 35),
            # u'循环水系统计算K22' p_select_f
            ImageInfo('0', (6340, 2815), format_value("number", str(circulatingWater.p_select_f)), 35),
            # u'循环水系统计算E19'
            ImageInfo('0', (6612, 3435), format_value("number", str(circulatingWater.v_discharge_capacity)) , 35),
            # u'循环水系统计算E16'
            ImageInfo('0', (7172, 1232), format_value("number", str(circulatingWater.v_partial_blow_loss)) , 35),
            # u'循环水系统计算E20'
            ImageInfo('0', (8188, 3285), format_value("number", str(circulatingWater.v_amount_of_makeup_water)) , 35)
        ]


    # 原则性热力系统图8--抽凝
    def p4_b_List(self, plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        sewage_quantity = ""
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        multiply_f34_g19 = ""
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f34_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        plus_32_33 = ""
        if turbineBackpressure.hh1_extraction_amount and turbineBackpressure.hh2_extraction_amount:
            plus_32_33 = turbineBackpressure.hh1_extraction_amount + turbineBackpressure.hh2_extraction_amount
        plus_three = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount
        plus_36_37 = ""
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_36_37 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount

        return [
            # u'汽轮机计算-抽凝！F32'
            ImageInfo('0', (389, 2079), format_value("number", str(turbineBackpressure.hh1_saturated_water_enthalpy)), 35),
            #  u'锅炉辅机!F32'
            ImageInfo('0', (389, 2973), format_value("number", str(boilerAuxiliaries.c_drum_pressure)), 35),
            #  u'锅炉辅机！G58'
            ImageInfo('0', (391, 1679), format_value("number", str(boilerAuxiliaries.p_inlet_pressure)), 35),
            #  u'汽轮机计算-抽凝！C32'
            ImageInfo('0', (391, 1777), format_value("number", str(turbineBackpressure.hh1_water_enthalpy)), 35),
            # u'汽轮机计算-抽凝！F33'
            ImageInfo('0', (393, 2577), format_value("number", str(turbineBackpressure.hh2_saturated_water_enthalpy)) , 35),
            # u'锅炉辅机F33'
            ImageInfo('0', (394, 3069), format_value("number", str(boilerAuxiliaries.c_drum_aturatedwater_enthalpy)) , 35),
            # u'--'
            ImageInfo('0', (395, 1989), '--', 35),
            # u'--'
            ImageInfo('0', (395, 2484), '--', 35),
            # u'锅炉辅机F31/1000'
            ImageInfo('0', (608, 3071), format_value("number", str(sewage_quantity)), 35),
            # --
            ImageInfo('0', (611, 2976), '--', 35),
            # u'汽轮机计算-抽凝！B32'
            ImageInfo('0', (681, 1685), format_value("number", str(turbineBackpressure.hh1_water_temperature)) , 35),
            # u'汽轮机计算-抽凝！E32'
            ImageInfo('0', (681, 1987), format_value("number", str(turbineBackpressure.hh1_saturated_water_temperature)) , 35),
            # u'锅炉计算G19'
            ImageInfo('0', (683, 1775), format_value("number", str(furnaceCalculation.f_steam_flow_design)) , 35),
            # u'汽轮机计算-抽凝！K32'
            ImageInfo('0', (685, 2079), format_value("number", str(turbineBackpressure.hh1_extraction_amount)) , 35),
            # u'汽轮机计算-抽凝！E33'
            ImageInfo('0', (685, 2484), format_value("number", str(turbineBackpressure.hh2_saturated_water_temperature)) , 35),
            # u'汽轮机计算-抽凝！K32+K33'
            ImageInfo('0', (687, 2579), format_value("number", str(plus_32_33)), 35),
            # u'锅炉计算G19'
            ImageInfo('0', (901, 945), format_value("number", str(furnaceCalculation.f_steam_flow_design)) , 35),
            # u'汽轮机计算-抽凝！G35'
            ImageInfo('0', (1311, 3967), format_value("number", str(turbineBackpressure.d_work_pressure)) , 35),
            # u'汽轮机计算-抽凝！C35'
            ImageInfo('0', (1311, 4063), format_value("number", str(turbineBackpressure.d_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！J35'
            ImageInfo('0', (1575, 2448), format_value("number", str(turbineBackpressure.d_extraction_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！I35'
            ImageInfo('0', (1578, 2349), format_value("number", str(turbineBackpressure.d_extraction_pressure)) , 35),
            # u'汽轮机计算-抽凝！B35'
            ImageInfo('0', (1616, 3971), format_value("number", str(turbineBackpressure.d_water_temperature)) , 35),
            # u'锅炉计算G19'
            ImageInfo('0', (1617, 4064), format_value("number", str(furnaceCalculation.f_steam_flow_design)) , 35),
            # u'汽轮机计算-抽凝！K35'
            ImageInfo('0', (1856, 2450), format_value("number", str(turbineBackpressure.d_extraction_amount)) , 35),
            # --
            ImageInfo('0', (1858, 2357), u'--', 35),
            # u'汽轮机计算-抽凝！I33'
            ImageInfo('0', (1967, 1895), format_value("number", str(turbineBackpressure.hh2_extraction_pressure)) , 35),
            # u'汽轮机计算-抽凝！I32'
            ImageInfo('0', (1971, 1583), format_value("number", str(turbineBackpressure.hh1_extraction_pressure)) , 35),
            # u'汽轮机计算-抽凝！J32'
            ImageInfo('0', (1973, 1677), format_value("number", str(turbineBackpressure.hh1_extraction_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！J33'
            ImageInfo('0', (1977, 1993), format_value("number", str(turbineBackpressure.hh2_extraction_enthalpy)) , 35),
            # u'锅炉计算G22'
            ImageInfo('0', (2163, 497), format_value("number", str(furnaceCalculation.f_steam_enthalpy_design)) , 35),
            # u'锅炉计算G20'
            ImageInfo('0', (2171, 401), format_value("number", str(furnaceCalculation.f_steam_pressure_design)) , 35),
            # u'汽轮机计算-抽凝F34'
            ImageInfo('0', (2196, 4109), format_value("number", str(turbineBackpressure.h_pressure)) , 35),
            # u'汽轮机计算-抽凝H34'
            ImageInfo('0', (2200, 4203), format_value("number", str(turbineBackpressure.h_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！K33'
            ImageInfo('0', (2249, 1993), format_value("number", str(turbineBackpressure.hh2_extraction_amount)) , 35),
            # --
            ImageInfo('0', (2251, 1903), u'--', 35),
            # --
            ImageInfo('0', (2255, 1589), u'--', 35),
            # u'汽轮机计算-抽凝！K32'
            ImageInfo('0', (2255, 1679), format_value("number", str(turbineBackpressure.hh1_extraction_amount)) , 35),
            # u'汽轮机计算-抽凝！F26'
            ImageInfo('0', (2383, 493), format_value("number", str(turbineBackpressure.e_throttle_flow)) , 35),
            # u'锅炉计算G21'
            ImageInfo('0', (2387, 401), format_value("number", str(furnaceCalculation.f_steam_temperature_design)), 35),
            # u'汽轮机计算-抽凝！C36'
            ImageInfo('0', (2429, 3254), format_value("number", str(turbineBackpressure.lh1_water_enthalpy)) , 35),
            # --
            ImageInfo('0', (2431, 3158), u'--', 35),
            # u'汽轮机计算-抽凝D34'
            ImageInfo('0', (2564, 4107), format_value("number", str(turbineBackpressure.h_temperature)) , 35),
            # u'锅炉计算G19 * 汽轮机计算-抽凝！J34'
            ImageInfo('0', (2564, 4197), format_value("number", str(multiply_f34_g19)) , 35),
            # u'汽轮机计算-抽凝！K36+K37+F99'
            ImageInfo('0', (2640, 3254), format_value("number", str(plus_three)) , 35),
            # u'汽轮机计算-抽凝！B36'
            ImageInfo('0', (2647, 3158), format_value("number", str(turbineBackpressure.lh1_water_temperature)) , 35),
            # u'汽轮机计算-抽凝！J36'
            ImageInfo('0', (2897, 2457), format_value("number", str(turbineBackpressure.lh1_extraction_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！I36'
            ImageInfo('0', (2901, 2358), format_value("number", str(turbineBackpressure.lh1_extraction_pressure)) , 35),
            # --
            ImageInfo('0', (3011, 3424), u'--', 35),
            # u'汽轮机计算-抽凝！F36'
            ImageInfo('0', (3013, 3513), format_value("number", str(turbineBackpressure.lh1_saturated_water_enthalpy)) , 35),
            # --
            ImageInfo('0', (3120, 2364), u'--', 35),
            # u'汽轮机计算-抽凝！K36'
            ImageInfo('0', (3121, 2460), format_value("number", str(turbineBackpressure.lh1_extraction_amount)) , 35),
            # --
            ImageInfo('0', (3187, 3156), u'--', 35),
            # u'汽轮机计算-抽凝！C37'
            ImageInfo('0', (3187, 3255), format_value("number", str(turbineBackpressure.lh2_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！E36'
            ImageInfo('0', (3237, 3422), format_value("number", str(turbineBackpressure.lh1_saturated_water_temperature)) , 35),
            # u'汽轮机计算-抽凝！K36'
            ImageInfo('0', (3242, 3517), format_value("number", str(turbineBackpressure.lh1_extraction_amount)) , 35),
            # u'汽轮机计算-抽凝！F24'
            ImageInfo('0', (3251, 1459), format_value("number", str(turbineBackpressure.e_steam_extraction_select)) , 35),
            # u'汽轮机计算-抽凝！B37'
            ImageInfo('0', (3402, 3159), format_value("number", str(turbineBackpressure.lh2_water_temperature)) , 35),
            # u'汽轮机计算-抽凝！K36+K37+F99'
            ImageInfo('0', (3402, 3251), format_value("number", str(plus_three)) , 35),
            # u'汽轮机计算-抽凝！I37'
            ImageInfo('0', (3528, 2364), format_value("number", str(turbineBackpressure.lh2_extraction_pressure)) , 35),
            # u'汽轮机计算-抽凝！J37'
            ImageInfo('0', (3528, 2462), format_value("number", str(turbineBackpressure.lh2_extraction_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！F71'
            ImageInfo('0', (3565, 1213), format_value("number", str(turbineBackpressure.i_exhaust_point_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！F68'
            ImageInfo('0', (3569, 1121), format_value("number", str(turbineBackpressure.i_exhaust_point_pressure)) , 35),
            # --
            ImageInfo('0', (3676, 3420), u'--', 35),
            # u'汽轮机计算-抽凝！F37'
            ImageInfo('0', (3676, 3512), format_value("number", str(turbineBackpressure.lh2_saturated_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝！K37'
            ImageInfo('0', (3749, 2459), format_value("number", str(turbineBackpressure.lh2_extraction_amount)) , 35),
            # --
            ImageInfo('0', (3755, 2366), u'--', 35),
            # u'汽轮机计算-抽凝！F69'
            ImageInfo('0', (3797, 1121), format_value("number", str(turbineBackpressure.i_exhaust_point_temperature)) , 35),
            # u'汽轮机计算-抽凝！F72'
            ImageInfo('0', (3801, 1213), format_value("number", str(turbineBackpressure.i_exhaust_point_flow)) , 35),
            # --
            ImageInfo('0', (3815, 3155), u'--', 35),
            # u'汽轮机计算-抽凝！C38'
            ImageInfo('0', (3817, 3251), format_value("number", str(turbineBackpressure.c_water_enthalpy)) , 35),
            # u'汽轮机计算-抽凝K36+K37'
            ImageInfo('0', (3905, 3515), format_value("number", str(plus_36_37)), 35),
            # 
            ImageInfo('0', (3909, 3418), format_value("number", str(turbineBackpressure.lh2_saturated_water_temperature)), 35),
            # u'汽轮机计算-抽凝！B38'
            ImageInfo('0', (3980, 3160), format_value("number", str(turbineBackpressure.c_water_temperature)) , 35),
            # u'汽轮机计算-抽凝！K36+K37+F99'
            ImageInfo('0', (3981, 3254), format_value("number", str(plus_three)) , 35),
            # u'汽轮机计算-抽凝！F92'
            ImageInfo('0', (4533, 1869), format_value("number", str(turbineBackpressure.i_steam_exhaust_pressure)) , 35),
            # u'汽轮机计算-抽凝！F95'
            ImageInfo('0', (4535, 1962), format_value("number", str(turbineBackpressure.i_steam_exhaust_enthalpy_actual)) , 35),
            # --
            ImageInfo('0', (4794, 1874), u'--', 35),
            # u'汽轮机计算-抽凝！F99'
            ImageInfo('0', (4795, 1963), format_value("number", str(turbineBackpressure.i_steam_exhaust_flow)) , 35),
            # --
            ImageInfo('0', (4855, 2568), u'--', 35),
            # --
            ImageInfo('0', (4857, 2667), u'--', 35),
            # u'汽轮机计算-抽凝！F24'
            ImageInfo('0', (4942, 1507), format_value("number", str(turbineBackpressure.e_steam_extraction_select)) , 35),
            # u'循环水系统计算！E9'
            ImageInfo('0', (5072, 2664), format_value("number", str(circulatingWater.v_total_circulating_water_select)) , 35),
            ImageInfo('0', (5074, 2571), u'20/33', 35),
            # --
            ImageInfo('0', (5111, 1965), u'---', 35),
            # --
            ImageInfo('0', (5115, 1873), u'---', 35),
            #  u'循环水系统计算！E9'
            ImageInfo('0', (5319, 1962), format_value("number", str(circulatingWater.v_total_circulating_water_select)), 35),
            ImageInfo('0', (5324, 1872), u'30/43', 35),
            # u'循环水系统计算！E14'
            ImageInfo('0', (6088, 1433), format_value("number", str(circulatingWater.v_evaporation_loss)) , 35),
            # u'循环水系统计算！K24' p_count
            ImageInfo('0', (6242, 1990), format_value("number", str(circulatingWater.p_count)), 35),
            # u'循环水系统计算！K26' p_select_s
            ImageInfo('0', (6588, 1993), format_value("number", str(circulatingWater.p_select_s)), 35),
            # u'循环水系统计算！E19'
            ImageInfo('0', (6736, 3543), format_value("number", str(circulatingWater.v_discharge_capacity)) , 35),
            # u'循环水系统计算！E16'
            ImageInfo('0', (6995, 1432), format_value("number", str(circulatingWater.v_partial_blow_loss)) , 35),
            # u'循环水系统计算！E20'
            ImageInfo('0', (8600, 3401), format_value("number", str(circulatingWater.v_amount_of_makeup_water)), 35),
        ]

    # 化学水1
    def p1_chemical_List(self, plan_id):
        chemicalWater = GetimgInfoList().searchImgData(plan_id)
        return [
            ImageInfo('0', (557, 1677), format_value("number", str(chemicalWater.m_output)), 50),
            ImageInfo('0', (1345, 2243), format_value("number", str(chemicalWater.m_remove_salt_volume)), 50),
        ]

    # 化学水2
    def p2_chemical_List(self, plan_id):
        chemicalWater = GetimgInfoList().searchImgData(plan_id)
        return [
            ImageInfo('0', (557, 1677), format_value("number", str(chemicalWater.m_output)), 50),
            ImageInfo('0', (1345, 2243), format_value("number", str(chemicalWater.m_remove_salt_volume)), 50),
        ]

    # 原则性除灰系统图
    def p_ash_List(self, plan_id):
        removalAshSlag = GetimgInfoList().searchImgData(plan_id)
        return [
            ImageInfo('0', (2877, 3891), format_value("number", str(removalAshSlag.g_air_transport_ash_system)), 50),
            ImageInfo('0', (4849, 1865), format_value("number", str(removalAshSlag.r_height)), 50),
            ImageInfo('0', (4861, 1721), format_value("number", str(removalAshSlag.r_dia)), 50),
            ImageInfo('0', (4889, 1437), format_value("number", str(removalAshSlag.r_stored_ash)), 50),
            ImageInfo('0', (4893, 1573), format_value("number", str(removalAshSlag.r_effective_volume_ash_storage)), 50),
        ]


    # 原则性除渣系统图 
    def p_slag_List(self, plan_id):
        removalAshSlag = GetimgInfoList().searchImgData(plan_id)
        return [
            ImageInfo('0', (2553, 2193), format_value("number", str(removalAshSlag.s_output_cold_single_stage)), 50),
            ImageInfo('0', (3241, 2965), format_value("number", str(removalAshSlag.s_high_temperature_belt_conveyor)), 50),
            ImageInfo('0', (4433, 2197), format_value("number", str(removalAshSlag.s_output_cold_single_stage)), 50),
            ImageInfo('0', (6833, 2253), format_value("number", str(removalAshSlag.s_height)), 50),
            ImageInfo('0', (6845, 2153), format_value("number", str(removalAshSlag.s_dia)), 50),
            ImageInfo('0', (6897, 1957), format_value("number", str(removalAshSlag.s_sludge_time)), 50),
            ImageInfo('0', (6897, 2053), format_value("number", str(removalAshSlag.s_slag_storage_volume_effective)), 50),
        ]
