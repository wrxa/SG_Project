# -*- coding: utf-8 -*-
from app.models import Company, Plan
from app.biomass_chp.models.modelsBiomass import BiomassCHPNeedsQuestionnaire, \
                     BiomassCHPBoilerCalculation,\
                     BiomassCHPFuelStorageTransportation, \
                     BiomassCHPDesulfurizationAndDenitrification,\
                     BiomassCHPDASRemove, BiomassCHPBoilerAuxiliaries, \
                     BiomassCHPOfficialProcess, BiomassCHPTurbineBackpressure, \
                     BiomassCHPDesulfurizationAndDenitrification, BiomassCHPChimney, \
                     BiomasschpTurbineAuxiliary, BiomassCHPCirculatingWater, \
                     BiomassCHPHeatSupply


# 格式化数据库取出的值
def format_value(values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if values == "null" or values == "None" or values is None:
        result = 0
    elif str(type(values)) == "<type 'unicode'>":
        result = values
    elif str(type(values)) == "<type 'int'>":
        result = values
    elif str(type(values)) == "<type 'str'>":
        result = values
    elif abs(values) <= 0.00001:
        result = 0
    else:
        # 只有数字类型的需要取出多余的0
        result = float(str(float(values)).rstrip('0'))
    return result


def getBiomassPlanData(planId):
    plandocxcolumdir = {'company.company_name': '',
                        'biomasschp_boiler_auxiliaries.c_specifications': '',
                        'biomasschp_boiler_auxiliaries.i_duster': '',
                        'biomasschp_boiler_auxiliaries.r_specifications': '',
                        'biomasschp_boiler_calculation.boiler_type': '',
                        'biomasschp_boiler_calculation.c_ash_content_received_check': '',
                        'biomasschp_boiler_calculation.c_ash_content_received_design': '',
                        'biomasschp_boiler_calculation.c_base_heat_received_calculation_check': '',
                        'biomasschp_boiler_calculation.c_base_heat_received_calculation_design': '',
                        'biomasschp_boiler_calculation.c_base_heat_received_user_check': '',
                        'biomasschp_boiler_calculation.c_base_heat_received_user_design': '',
                        'biomasschp_boiler_calculation.c_carbon_content_received_check': '',
                        'biomasschp_boiler_calculation.c_carbon_content_received_design': '',
                        'biomasschp_boiler_calculation.c_daf_check': '',
                        'biomasschp_boiler_calculation.c_daf_design': '',
                        'biomasschp_boiler_calculation.c_hydrogen_content_received_check': '',
                        'biomasschp_boiler_calculation.c_hydrogen_content_received_design': '',
                        'biomasschp_boiler_calculation.c_nitrogen_content_check': '',
                        'biomasschp_boiler_calculation.c_nitrogen_content_design': '',
                        'biomasschp_boiler_calculation.c_oxygen_content_received_check': '',
                        'biomasschp_boiler_calculation.c_oxygen_content_received_design': '',
                        'biomasschp_boiler_calculation.c_sulfur_content_received_check': '',
                        'biomasschp_boiler_calculation.c_sulfur_content_received_design': '',
                        'biomasschp_boiler_calculation.c_water_content_received_check': '',
                        'biomasschp_boiler_calculation.c_water_content_received_design': '',
                        'biomasschp_boiler_calculation.d_ash_total_design': '',
                        'biomasschp_boiler_calculation.d_dust_total_design': '',
                        'biomasschp_boiler_calculation.d_entry_somke_temperature_design': '',
                        'biomasschp_boiler_calculation.d_total_design': '',
                        'biomasschp_boiler_calculation.f_blowdown_rate_design': '',
                        'biomasschp_boiler_calculation.f_boiler_efficiency_design': '',
                        'biomasschp_boiler_calculation.f_steam_flow_design': '',
                        'biomasschp_boiler_calculation.f_steam_pressure_design': '',
                        'biomasschp_boiler_calculation.f_steam_temperature_design': '',
                        'biomasschp_boiler_calculation.f_water_temperature_design': '',
                        'biomasschp_boiler_calculation.h_smoke_temperature_design': '',
                        'biomasschp_boiler_calculation.h_smoke_volume_design': '',
                        'biomasschp_boiler_calculation.p_smoke_temperature_design': '',
                        'biomasschp_boiler_calculation.pressure_temperature': '',
                        'biomasschp_das_remove.a_gas_consumption': '',
                        'biomasschp_das_remove.d_tun_exit_smoke_concentration': '',
                        'biomasschp_das_remove.a_remove_output': '',
                        'biomasschp_das_remove.a_storage_time': '',
                        'biomasschp_das_remove.a_volumn': '',
                        'biomasschp_das_remove.d_dust_remove_efficiency': '',
                        'biomasschp_das_remove.d_dust_wiper_flow': '',
                        'biomasschp_das_remove.s_bulk_density': '',
                        'biomasschp_das_remove.s_diameter': '',
                        'biomasschp_das_remove.s_slag_output': '',
                        'biomasschp_das_remove.s_storage_time': '',
                        'biomasschp_das_remove.s_volumn': '',
                        'biomasschp_fuel_st.b_annual_use_hours_check': '',
                        'biomasschp_fuel_st.b_annual_use_hours_check': '',
                        'biomasschp_fuel_st.b_annual_use_hours_design': '',
                        'biomasschp_fuel_st.b_annual_use_hours_design': '',
                        'biomasschp_fuel_st.b_bin_quantity_design': '',
                        'biomasschp_fuel_st.b_carrying_vehicle_load_design': '',
                        'biomasschp_fuel_st.b_daily_consumption_check': '',
                        'biomasschp_fuel_st.b_daily_consumption_check': '',
                        'biomasschp_fuel_st.b_daily_consumption_design': '',
                        'biomasschp_fuel_st.b_daily_consumption_design': '',
                        'biomasschp_fuel_st.b_daily_fuel_consumption_design': '',
                        'biomasschp_fuel_st.b_daily_vehicle_design': '',
                        'biomasschp_fuel_st.b_rated_fuel_consumption_check': '',
                        'biomasschp_fuel_st.b_rated_fuel_consumption_design': '',
                        'biomasschp_fuel_st.b_rated_fuel_consumption_design': '',
                        'biomasschp_fuel_st.b_saily_use_hours_design': '',
                        'biomasschp_fuel_st.b_single_effective_volume_selected_design': '',
                        'biomasschp_fuel_st.b_total_effective_volume_design': '',
                        'biomasschp_fuel_st.b_unbalance_coefficient_design': '',
                        'biomasschp_fuel_st.b_year_consumption_check': '',
                        'biomasschp_fuel_st.b_year_consumption_design': '',
                        'biomasschp_fuel_st.b_year_consumption_design': '',
                        'biomasschp_fuel_st.d_average_stack_height_design': '',
                        'biomasschp_fuel_st.d_fuel_available_reserves_design': '',
                        'biomasschp_fuel_st.d_fuel_bulk_density_design': '',
                        'biomasschp_fuel_st.d_fuel_reserve_days_design': '',
                        'biomasschp_fuel_st.d_yardarea_design': '',
                        'biomasschp_fuel_st.f_belt_max_delivery': '',
                        'biomasschp_fuel_st.f_belt_number': '',
                        'biomasschp_fuel_st.f_belt_speed': '',
                        'biomasschp_fuel_st.f_belt_width': '',
                        'biomasschp_fuel_st.s_average_stack_height_design': '',
                        'biomasschp_fuel_st.s_duplex_number_design': '',
                        'biomasschp_fuel_st.s_fuel_available_reserves_design': '',
                        'biomasschp_fuel_st.s_fuel_bulk_density_check': '',
                        'biomasschp_fuel_st.s_fuel_bulk_density_design': '',
                        'biomasschp_fuel_st.s_fuel_reserve_days_design': '',
                        'biomasschp_fuel_st.s_single_duplex_output_design': '',
                        'biomasschp_fuel_st.s_yardarea_design': '',
                        'biomasschp_fuel_st.t_single_effective_volume_selected_design': '',
                        'biomasschp_needs_questionnaire.l_altitude': '',
                        'biomasschp_needs_questionnaire.l_humidity': '',
                        'biomasschp_needs_questionnaire.l_max_temperature': '',
                        'biomasschp_needs_questionnaire.l_min_temperature': '',
                        'biomasschp_needs_questionnaire.l_pressure': '',
                        'biomasschp_needs_questionnaire.l_temperature': '',
                        'biomasschp_needs_questionnaire.s_ash_density_check': '',
                        'biomasschp_needs_questionnaire.s_ash_density_design': '',
                        'biomasschp_needs_questionnaire.s_deformation_check': '',
                        'biomasschp_needs_questionnaire.s_deformation_design': '',
                        'biomasschp_needs_questionnaire.s_flow_check': '',
                        'biomasschp_needs_questionnaire.s_flow_design': '',
                        'biomasschp_needs_questionnaire.s_grindability_check': '',
                        'biomasschp_needs_questionnaire.s_grindability_design': '',
                        'biomasschp_needs_questionnaire.s_hemispherical_check': '',
                        'biomasschp_needs_questionnaire.s_hemispherical_design': '',
                        'biomasschp_needs_questionnaire.s_softening_check': '',
                        'biomasschp_needs_questionnaire.s_softening_design': '',
                        'biomasschp_needs_questionnaire.t_year_heating_days': '',
                        'biomasschp_official_process.o_boiler_blowdown_loss': '',
                        'biomasschp_official_process.o_boiler_type': '',
                        'biomasschp_official_process.o_boiler_water_max': '',
                        'biomasschp_official_process.o_boiler_water_normal': '',
                        'biomasschp_official_process.o_boiler_water_system': '',
                        'biomasschp_official_process.o_loss_factory': '',
                        'biomasschp_official_process.o_oil_pump': '',
                        'biomasschp_official_process.o_oil_pump_pressure': '',
                        'biomasschp_official_process.o_salt_water_tank': '',
                        'biomasschp_official_process.o_start_accident_increase_loss': '',
                        'biomasschp_official_process.o_water_consumption': '',
                        'biomasschp_turbine_backpressure.e_exhaust_point_flow': '',
                        'biomasschp_turbine_backpressure.e_exhaust_point_flow': '',
                        'biomasschp_turbine_backpressure.e_exhaust_point_pressure': '',
                        'biomasschp_turbine_backpressure.e_exhaust_point_temperature': '',
                        'biomasschp_turbine_backpressure.e_generator_efficiency': '',
                        'biomasschp_turbine_backpressure.e_steam_exhaust_pressure': '',
                        'biomasschp_turbine_backpressure.e_steam_extraction_select': '',
                        'biomasschp_turbine_backpressure.e_steam_flow': '',
                        'biomasschp_turbine_backpressure.e_steam_temperature': '',
                        'biomasschp_turbine_backpressure.e_throttle_flow': '',
                        'biomasschp_turbine_backpressure.i_exhaust_point_flow': '',
                        'biomasschp_turbine_backpressure.i_exhaust_point_pressure': '',
                        'biomasschp_turbine_backpressure.i_exhaust_point_temperature': '',
                        'biomasschp_turbine_backpressure.i_steam_exhaust_flow': '',
                        'biomasschp_des_den.s_desulfurization_efficiency':'',
                        'biomasschp_des_den.c_limestone_purity':'',
                        'biomasschp_des_den.c_sulfur_molar':'',
                        'biomasschp_des_den.s_after_so2':'',
                        'biomasschp_des_den.s_after_so2_discharge':'',
                        'biomasschp_des_den.c_limestone_consumption':'',
                        'biomasschp_des_den.c_limestone_storage_time':'',
                        'biomasschp_des_den.c_limestone_volumn':'',
                        'biomasschp_des_den.c_limestone_output':'',
                        'biomasschp_des_den.n_after_nox_concentration':'',
                        'biomasschp_des_den.n_after_nox_discharge':'',
                        'biomasschp_des_den.d_use_urea':'',
                        'biomasschp_des_den.d_water_urea':'',
                        'biomasschp_des_den.d_days_urea':'',
                        'biomasschp_des_den.d_capacity_urea':'',
                        'biomasschp_chimney.chimney_height':'',
                        'biomasschp_chimney.chimney_outlet_inner_diameter':'',
                        'biomasschp_boiler_auxiliaries.f_flow':'',
                        'biomasschp_boiler_auxiliaries.f_pump_total_head':'',
                        'biomasschp_boiler_auxiliaries.f_auxiliary_motor_power':'',
                        'biomasschp_boiler_auxiliaries.f_boiler_evaporation':'',
                        'biomasschp_turbine_backpressure.d_work_pressure':'',
                        'biomasschp_turbine_backpressure.d_water_temperature':'',
                        'biomasschp_boiler_auxiliaries.f_effective_volume':'',
                        'biomasschp_turbine_auxiliary.m_area_cooling_surface':'',
                        'biomasschp_turbine_auxiliary.m_circulating_water':'',
                        'biomasschp_turbine_auxiliary.m_cooling_water_inlet_temperature':'',
                        'biomasschp_turbine_auxiliary.m_cooling_outlet_temperature':'',
                        'biomasschp_turbine_auxiliary.w_flow_amount':'',
                        'biomasschp_turbine_auxiliary.w_condensate_pump_lift':'',
                        'biomasschp_turbine_auxiliary.w_auxiliary_motor_power':'',
                        'biomasschp_turbine_auxiliary.f_air_ejector_pressure':'',
                        'biomasschp_turbine_auxiliary.f_flow_amount':'',
                        'biomasschp_turbine_auxiliary.f_total_lift':'',
                        'biomasschp_turbine_auxiliary.f_auxiliary_motor_power':'',
                        'biomasschp_turbine_auxiliary.f_water_tank_pressure':'',
                        'biomasschp_boiler_auxiliaries.c_work_pressure':'',
                        'biomasschp_boiler_auxiliaries.c_volume':'',
                        'biomasschp_boiler_auxiliaries.r_work_pressure':'',
                        'biomasschp_boiler_auxiliaries.r_volume':'',
                        'biomasschp_circulating_water.v_circulating_ratio_summer':'',
                        'biomasschp_circulating_water.v_circulating_ratio_winter':'',
                        'biomasschp_circulating_water.v_circulating_water_summer':'',
                        'biomasschp_circulating_water.v_circulating_water_winter':'',
                        'biomasschp_circulating_water.v_auxiliary_engine_cooling_winter':'',
                        'biomasschp_circulating_water.v_total_circulating_water_summer':'',
                        'biomasschp_circulating_water.v_total_circulating_water_winter':'',
                        'biomasschp_circulating_water.p_select_f':'',
                        'biomasschp_circulating_water.p_count':'',
                        'biomasschp_circulating_water.p_select_s':'',
                        'biomasschp_circulating_water.c_flow':'',
                        'biomasschp_circulating_water.c_pumping_head':'',
                        'biomasschp_circulating_water.c_supporting_motor_power':'',
                        'biomasschp_circulating_water.v_evaporation_loss':'',
                        'biomasschp_circulating_water.v_blowing_loss_rate':'',
                        'biomasschp_circulating_water.v_discharge_capacity':'',
                        'biomasschp_circulating_water.v_amount_of_makeup_water':'',
                        'biomasschp_heat_supply.hot_turbine_flow':'',
                        'biomasschp_needs_questionnaire.t_condensate_water_recovery_rate':''                    
                        }
    questionnaire = BiomassCHPNeedsQuestionnaire.search_questionnaire(planId)
    auxiliaries = BiomassCHPBoilerAuxiliaries.search_auxiliaries(planId)
    boiler = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
    das_remove = BiomassCHPDASRemove.search_dasRemove(planId)
    fuel_st = BiomassCHPFuelStorageTransportation.search_storage_transportation(planId)
    official = BiomassCHPOfficialProcess.search_official(planId)
    turbine = BiomassCHPTurbineBackpressure.search_turbineBackpressure(planId)

    des_den = BiomassCHPDesulfurizationAndDenitrification.search_des_den(planId)
    chimney = BiomassCHPChimney.search_biomassCHPChimney(planId)
    turbine_auxiliary = BiomasschpTurbineAuxiliary.search_turbine_auxiliary(planId)
    circulating_water = BiomassCHPCirculatingWater.search_circulating_water(planId)
    heatSupply = BiomassCHPHeatSupply.search_heatSupply(planId)

    plan = Plan.search_planById(planId)
    company = Company.search_companyById(plan.company_id)
    plandocxcolumdir['company.company_name'] = company.company_name
    for key in plandocxcolumdir:
        if hasattr(questionnaire, key.split(".")[1]):
            value = getattr(questionnaire, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = format_value(value)
            else:
                plandocxcolumdir[key] = 0
                
    for key in plandocxcolumdir:
        if hasattr(auxiliaries, key.split(".")[1]):
            value = getattr(auxiliaries, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = format_value(value)
            else:
                plandocxcolumdir[key] = 0

    for key in plandocxcolumdir:
        if hasattr(boiler, key.split(".")[1]):
            value = getattr(boiler, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = format_value(value)
            else:
                plandocxcolumdir[key] = 0

    for key in plandocxcolumdir:
        if hasattr(das_remove, key.split(".")[1]):
            value = getattr(das_remove, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = format_value(value)
            else:
                plandocxcolumdir[key] = 0

    for key in plandocxcolumdir:
        if hasattr(fuel_st, key.split(".")[1]):
            value = getattr(fuel_st, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = format_value(value)
            else:
                plandocxcolumdir[key] = 0
                
    for key in plandocxcolumdir:
        if hasattr(official, key.split(".")[1]):
            value = getattr(official, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = format_value(value)
            else:
                plandocxcolumdir[key] = 0


    for key in plandocxcolumdir:
        if hasattr(turbine, key.split(".")[1]):
            value = getattr(turbine, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = round(format_value(value), 0)
            else:
                plandocxcolumdir[key] = 0

    for key in plandocxcolumdir:
        if hasattr(des_den, key.split(".")[1]):
            value = getattr(des_den, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = round(format_value(value), 0)
            else:
                plandocxcolumdir[key] = 0

    for key in plandocxcolumdir:
        if hasattr(chimney, key.split(".")[1]):
            value = getattr(chimney, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = round(format_value(value), 0)
            else:
                plandocxcolumdir[key] = 0

    for key in plandocxcolumdir:
        if hasattr(turbine_auxiliary, key.split(".")[1]):
            value = getattr(turbine_auxiliary, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = round(format_value(value), 0)
            else:
                plandocxcolumdir[key] = 0

    for key in plandocxcolumdir:
        if hasattr(circulating_water, key.split(".")[1]):
            value = getattr(circulating_water, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = round(format_value(value), 0)
            else:
                plandocxcolumdir[key] = 0

    for key in plandocxcolumdir:
        if hasattr(heatSupply, key.split(".")[1]):
            value = getattr(heatSupply, key.split(".")[1])
            if value:
                plandocxcolumdir[key] = round(format_value(value), 0)
            else:
                plandocxcolumdir[key] = 0

    # 追加需要判断或计算的项目
    # 温度压力种类
    if plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '1':
        plandocxcolumdir['biomasschp_boiler_calculation.report_pressure_temperature'] = u'高温高压'
    elif plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '2':
        plandocxcolumdir['biomasschp_boiler_calculation.report_pressure_temperature'] = u'次高温次高压'
    elif plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '3':
        plandocxcolumdir['biomasschp_boiler_calculation.report_pressure_temperature'] = u'中温中压'
    else:
        plandocxcolumdir['biomasschp_boiler_calculation.report_pressure_temperature'] = u''

    # 锅炉种类
    if plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '1':
        plandocxcolumdir['biomasschp_boiler_calculation.boiler_report'] = u'生物质常规循环流化床'
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '2':
        plandocxcolumdir['biomasschp_boiler_calculation.boiler_report'] = u'高低差速循环流化床'
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '3':
        plandocxcolumdir['biomasschp_boiler_calculation.boiler_report'] = u'联合炉排炉'
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '4':
        plandocxcolumdir['biomasschp_boiler_calculation.boiler_report'] = u'水冷振动炉排炉'
    else:
        plandocxcolumdir['biomasschp_boiler_calculation.boiler_report'] = u''

    # 凝汽式/抽凝式汽轮发电机组
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow_report'] = u'凝汽式'
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
        plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow_report'] = u'抽凝式'
    else:
        plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow_report'] = u''

    # 生物质发电/热电联产项目
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_biomass_report'] = u'生物质发电'
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
        plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_biomass_report'] = u'生物质热电联产'
    else:
        plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_biomass_report'] = u''

    # 单路/双路皮带
    if plandocxcolumdir['biomasschp_fuel_st.f_belt_number'] == 1:
        plandocxcolumdir['biomasschp_fuel_st.f_belt_number_report'] = u'单路'
    elif plandocxcolumdir['biomasschp_fuel_st.f_belt_number'] == 2:
        plandocxcolumdir['biomasschp_fuel_st.f_belt_number_report'] = u'双路'
    else:
        plandocxcolumdir['biomasschp_fuel_st.f_belt_number_report'] = u''

    # 日排灰量
    plandocxcolumdir['biomasschp_boiler_calculation.d_ash_report_daily'] = plandocxcolumdir['biomasschp_fuel_st.b_saily_use_hours_design'] * plandocxcolumdir['biomasschp_boiler_calculation.d_ash_total_design']
    # 日排渣量
    plandocxcolumdir['biomasschp_boiler_calculation.d_dust_report_daily'] = plandocxcolumdir['biomasschp_fuel_st.b_saily_use_hours_design'] * plandocxcolumdir['biomasschp_boiler_calculation.d_dust_total_design']
    # 日排灰渣总量
    plandocxcolumdir['biomasschp_boiler_calculation.d_total_dust_report_daily'] = plandocxcolumdir['biomasschp_fuel_st.b_saily_use_hours_design'] * plandocxcolumdir['biomasschp_boiler_calculation.d_total_design']

    # 年排灰量
    plandocxcolumdir['biomasschp_boiler_calculation.d_ash_report_year'] = plandocxcolumdir['biomasschp_fuel_st.b_annual_use_hours_design'] * plandocxcolumdir['biomasschp_boiler_calculation.d_ash_total_design']
    # 年排渣量
    plandocxcolumdir['biomasschp_boiler_calculation.d_dust_report_year'] = plandocxcolumdir['biomasschp_fuel_st.b_annual_use_hours_design'] * plandocxcolumdir['biomasschp_boiler_calculation.d_dust_total_design']
    # 年排灰渣总量
    plandocxcolumdir['biomasschp_boiler_calculation.d_total_dust_report_year'] = plandocxcolumdir['biomasschp_fuel_st.b_annual_use_hours_design'] * plandocxcolumdir['biomasschp_boiler_calculation.d_total_design']

    # 1.5.2实现集中供热、热电联产是我国的基本国策
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        # 生物质发电无此内容
        plandocxcolumdir['content1.5.2'] = u''
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
        plandocxcolumdir['content1.5.2'] = u'国内纯冷凝发电厂热效率小于43%，而采用热电联产、集中供热的热电厂平均热效率可达65%以上，节能效果十分显著。我国既是能源消耗大国，又是能源缺乏的国家，因此，国家鼓励节约能源，提倡集中供热、热电联产。'
    else:
        plandocxcolumdir['content1.5.2'] = u''

    # 1.5.4环境保护的需要
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        # 生物质发电无此内容
        plandocxcolumdir['content1.5.4'] = u''
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
        plandocxcolumdir['content1.5.4'] = u'由小锅炉供热，不仅设备热效率低、除尘设备简陋、烟气含尘量严重超标，更谈不上对SO2、NOx排放的治理，对环境造成极大的污染。采用热电联产后，大容量锅炉的热效率大为提高，既可减少燃料消耗量，又可减少污染物的排放量，加之热电联产有条件采用高效除尘装置，大大降低了烟尘的排放量。'
    else:
        plandocxcolumdir['content1.5.4'] = u''

    # 1.5.4环境保护的需要
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        # 生物质发电无此内容
        plandocxcolumdir['content3.2_days'] = u''
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
        plandocxcolumdir['content3.2_days'] = u'冬季采暖期天数：XX d'
    else:
        plandocxcolumdir['content3.2_days'] = u''

    # 冬季采暖室外计算温度
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
         # 生物质发电无此内容
         plandocxcolumdir['content3.2_cal_temperature'] = u''
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
         plandocxcolumdir['content3.2_cal_temperature'] = u'冬季采暖室外计算温度：XX℃'
    else:
         plandocxcolumdir['content3.2_cal_temperature'] = u''

    # 采暖期室外平均温度
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
         # 生物质发电无此内容
         plandocxcolumdir['content3.2_average_temperature'] = u''
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
         plandocxcolumdir['content3.2_average_temperature'] = u'采暖期室外平均温度：XX℃'
    else:
         plandocxcolumdir['content3.2_average_temperature'] = u''

    # 3.9辅料供应
    if plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '1' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '2':
        plandocxcolumdir['content3.9_text'] = u'锅炉点火及稳燃用油为#0号（夏季）或#-20（冬季）轻柴油。'  
        plandocxcolumdir['content3.9_1row'] = u'| 序号 |油种 |0#轻柴油 |-20#轻柴油 |'
        plandocxcolumdir['content3.9_2row'] = u'|:------|:------|:------|:------|' 
        plandocxcolumdir['content3.9_3row'] = u'| 1 |恩氏粘度〔20℃时〕 |1.2～1.67ºE |1.15～1.67ºE |' 
        plandocxcolumdir['content3.9_4row'] = u'| 2 |灰份Ay |0.025% |0.025% |'
        plandocxcolumdir['content3.9_5row'] = u'| 3 |水份Wy |痕迹 | |'
        plandocxcolumdir['content3.9_6row'] = u'| 4 |硫份Sy |< 0.2% |< 0.2% |'
        plandocxcolumdir['content3.9_7row'] = u'| 5 |机械杂质 |无 | |'
        plandocxcolumdir['content3.9_8row'] = u'| 6 |凝固点 |不高于0℃ |不高于-20℃ |'
        plandocxcolumdir['content3.9_9row'] = u'| 7 |开口闪点 |不低于62～68℃ |不低于65℃ |'
        plandocxcolumdir['content3.9_10row'] = u'| 8 |比重 |0.84 t/m3 | |'
        plandocxcolumdir['content3.9_11row'] = u'| 9 |低位发热值QyDW |41031～41870 kJ/kg |41031～41870 kJ/kg |'
    else:
        plandocxcolumdir['content3.9_text'] = u''  
        plandocxcolumdir['content3.9_1row'] = u''
        plandocxcolumdir['content3.9_2row'] = u'' 
        plandocxcolumdir['content3.9_3row'] = u'' 
        plandocxcolumdir['content3.9_4row'] = u''
        plandocxcolumdir['content3.9_5row'] = u''
        plandocxcolumdir['content3.9_6row'] = u''
        plandocxcolumdir['content3.9_7row'] = u''
        plandocxcolumdir['content3.9_8row'] = u''
        plandocxcolumdir['content3.9_9row'] = u''
        plandocxcolumdir['content3.9_10row'] = u''
        plandocxcolumdir['content3.9_11row'] = u''

    # 炉底渣处理系统，灰渣比
    if plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '1' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '2':
        plandocxcolumdir['content5.5_text1'] = u'锅炉排渣经冷渣器冷却后，通过链斗输渣机输送到渣库， 然后装车外运至综合利用点，如要作为锅炉补充床料可运至床料堆场。'
        plandocxcolumdir['content5.5_text2'] = u'9:1'
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '3' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '4':
        plandocxcolumdir['content5.5_text1'] = u'从锅炉出渣口出来的炉渣，经捞渣机冷却后，提升至渣仓储存。渣仓存储一定渣量时，通过渣仓出口设置的设备装车外运。'
        plandocxcolumdir['content5.5_text2'] = u'6:4'
    else:
        plandocxcolumdir['content5.5_text1'] = u''
        plandocxcolumdir['content5.5_text2'] = u''

    # 5.5.1除渣系统
    if plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '1' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '2':
        plandocxcolumdir['content5.5.1_text1'] = u'本系统采用干式除渣，排渣量为'
        plandocxcolumdir['content5.5.1_text2'] = plandocxcolumdir['biomasschp_boiler_calculation.d_dust_total_design']
        plandocxcolumdir['content5.5.1_text3'] = u't/h，系统出力考虑一定的备用，按'
        plandocxcolumdir['content5.5.1_text4'] = plandocxcolumdir['biomasschp_das_remove.s_slag_output']
        plandocxcolumdir['content5.5.1_text5'] = u't/h考虑。'
    else:
        plandocxcolumdir['content5.5.1_text1'] = u''
        plandocxcolumdir['content5.5.1_text2'] = u''
        plandocxcolumdir['content5.5.1_text3'] = u''
        plandocxcolumdir['content5.5.1_text4'] = u''
        plandocxcolumdir['content5.5.1_text5'] = u''


    # 5.8.1主蒸汽系统
    if plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '1':
        plandocxcolumdir['content5.8.1'] = u'12Cr1MoVG'
    elif plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '2' or plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '3':
        plandocxcolumdir['content5.8.1'] = u'15CrMoG'
    else:
        plandocxcolumdir['content5.8.1'] = u''

    # 5.8.4抽汽回热系统
    if plandocxcolumdir['biomasschp_boiler_calculation.f_water_temperature_design'] == 150:
        plandocxcolumdir['content5.8.4_1grade'] = u'3'
        plandocxcolumdir['content5.8.4_2grade'] = u'1'
        plandocxcolumdir['content5.8.4_3grade'] = u'2'
        plandocxcolumdir['content5.8.4_4grade'] = u'3'
        plandocxcolumdir['content5.8.4_5grade'] = u'2'
    elif plandocxcolumdir['biomasschp_boiler_calculation.f_water_temperature_design'] == 158:
        plandocxcolumdir['content5.8.4_1grade'] = u'3'
        plandocxcolumdir['content5.8.4_2grade'] = u''
        plandocxcolumdir['content5.8.4_3grade'] = u'1'
        plandocxcolumdir['content5.8.4_4grade'] = u'2、3'
        plandocxcolumdir['content5.8.4_5grade'] = u'1'
    elif plandocxcolumdir['biomasschp_boiler_calculation.f_water_temperature_design'] == 215:
        plandocxcolumdir['content5.8.4_1grade'] = u'6'
        plandocxcolumdir['content5.8.4_2grade'] = u'1、2'
        plandocxcolumdir['content5.8.4_3grade'] = u'3'
        plandocxcolumdir['content5.8.4_4grade'] = u'4、5、6'
        plandocxcolumdir['content5.8.4_5grade'] = u'3'
    else:
        plandocxcolumdir['content5.8.4_1grade'] = u''
        plandocxcolumdir['content5.8.4_2grade'] = u''
        plandocxcolumdir['content5.8.4_3grade'] = u''
        plandocxcolumdir['content5.8.4_4grade'] = u''
        plandocxcolumdir['content5.8.4_5grade'] = u''

    # 5.9.1水源水质
    if plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '1':
        plandocxcolumdir['content5.9.1_boiler_1text'] = u'高温高压参数：'
        plandocxcolumdir['content5.9.1_boiler_2text'] = u'溶解氧             ≤7μg/L'
        plandocxcolumdir['content5.9.1_boiler_3text'] = u'铁                 ≤30μg/L'
        plandocxcolumdir['content5.9.1_boiler_4text'] = u'铜                 ≤5μg/L'
        plandocxcolumdir['content5.9.1_boiler_5text'] = u'氢电导率(25℃)      ≤0.3μS/cm'
        plandocxcolumdir['content5.9.1_boiler_6text'] = u'二氧化硅（SiO2 ）  ≤15μg/kg'
        plandocxcolumdir['content5.9.1_boiler_7text'] = u'TOC               ≤500μg/L'

        plandocxcolumdir['content5.9.1_steam_1text'] = u'高温高压参数：'
        plandocxcolumdir['content5.9.1_steam_2text'] = u'铁                ≤15μg/kg'
        plandocxcolumdir['content5.9.1_steam_3text'] = u'铜                ≤3μg/kg'
        plandocxcolumdir['content5.9.1_steam_4text'] = u'钠                ≤5μg/kg'
        plandocxcolumdir['content5.9.1_steam_5text'] = u'二氧化硅          ≤15μg/kg'
        plandocxcolumdir['content5.9.1_steam_6text'] = u'氢电导率(25℃)     ≤0.15μS/cm'

        plandocxcolumdir['content5.9.1_water_1text'] = u'高温高压参数：'
        plandocxcolumdir['content5.9.1_water_2text'] = u'磷酸根          2～10mg/L'
        plandocxcolumdir['content5.9.1_water_3text'] = u'PH(25℃)        9～10.5'
        plandocxcolumdir['content5.9.1_water_4text'] = u'二氧化硅        ≤2.0mg/L'
        plandocxcolumdir['content5.9.1_water_5text'] = u'电导率(25℃)    ≤50μS/cm'

        plandocxcolumdir['content5.9.1_condensate _1text'] = u'高温高压参数：'
        plandocxcolumdir['content5.9.1_condensate _2text'] = u'硬度              ≈0μmol/L'
        plandocxcolumdir['content5.9.1_condensate _3text'] = u'溶解氧            ≤50μg/L'
        plandocxcolumdir['content5.9.1_condensate _4text'] = u'氢电导率(25℃)    ≤0.3μS/cm'

    elif plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '2' or plandocxcolumdir['biomasschp_boiler_calculation.pressure_temperature'] == '3':
        plandocxcolumdir['content5.9.1_boiler_1text'] = u'中温中压/次高温次高压参数：'
        plandocxcolumdir['content5.9.1_boiler_2text'] = u'硬度            ≈2.0μmol/L'
        plandocxcolumdir['content5.9.1_boiler_3text'] = u'溶氧            ≤15μg/L'
        plandocxcolumdir['content5.9.1_boiler_4text'] = u'铁              ≤50μg/L'
        plandocxcolumdir['content5.9.1_boiler_5text'] = u'铜              ≤10μg/L'
        plandocxcolumdir['content5.9.1_boiler_6text'] = u'PH              8.8~9.2(加氨调节后)'
        plandocxcolumdir['content5.9.1_boiler_7text'] = u''

        plandocxcolumdir['content5.9.1_steam_1text'] = u'中温中压/次高温次高压参数：'
        plandocxcolumdir['content5.9.1_steam_2text'] = u'钠              ≤15μg/kg'
        plandocxcolumdir['content5.9.1_steam_3text'] = u'氢电导率	≤0.3μS/cm（25℃）'
        plandocxcolumdir['content5.9.1_steam_4text'] = u'二氧化硅	≤20μg/kg'
        plandocxcolumdir['content5.9.1_steam_5text'] = u'铁              ≤20μg/ kg'
        plandocxcolumdir['content5.9.1_steam_6text'] = u'铜              ≤5μg/ kg L'

        plandocxcolumdir['content5.9.1_water_1text'] = u'中温中压/次高温次高压参数：'
        plandocxcolumdir['content5.9.1_water_2text'] = u'PH               9 ~11'
        plandocxcolumdir['content5.9.1_water_3text'] = u'磷酸根        5~15mg/L'
        plandocxcolumdir['content5.9.1_water_4text'] = u''
        plandocxcolumdir['content5.9.1_water_5text'] = u''

        plandocxcolumdir['content5.9.1_condensate _1text'] = u'中温中压/次高温次高压参数：'
        plandocxcolumdir['content5.9.1_condensate _2text'] = u'硬度          ≤2.0μmol/L'
        plandocxcolumdir['content5.9.1_condensate _3text'] = u'溶氧          ≤50μg/L'
        plandocxcolumdir['content5.9.1_condensate _4text'] = u''
    else:
        plandocxcolumdir['content5.9.1_boiler_1text'] = u''
        plandocxcolumdir['content5.9.1_boiler_2text'] = u''
        plandocxcolumdir['content5.9.1_boiler_3text'] = u''
        plandocxcolumdir['content5.9.1_boiler_4text'] = u''
        plandocxcolumdir['content5.9.1_boiler_5text'] = u''
        plandocxcolumdir['content5.9.1_boiler_6text'] = u''
        plandocxcolumdir['content5.9.1_boiler_7text'] = u''

        plandocxcolumdir['content5.9.1_steam_1text'] = u''
        plandocxcolumdir['content5.9.1_steam_2text'] = u''
        plandocxcolumdir['content5.9.1_steam_3text'] = u''
        plandocxcolumdir['content5.9.1_steam_4text'] = u''
        plandocxcolumdir['content5.9.1_steam_5text'] = u''
        plandocxcolumdir['content5.9.1_steam_6text'] = u''

        plandocxcolumdir['content5.9.1_water_1text'] = u''
        plandocxcolumdir['content5.9.1_water_2text'] = u''
        plandocxcolumdir['content5.9.1_water_3text'] = u''
        plandocxcolumdir['content5.9.1_water_4text'] = u''
        plandocxcolumdir['content5.9.1_water_5text'] = u''

        plandocxcolumdir['content5.9.1_condensate _1text'] = u''
        plandocxcolumdir['content5.9.1_condensate _2text'] = u''
        plandocxcolumdir['content5.9.1_condensate _3text'] = u''
        plandocxcolumdir['content5.9.1_condensate _4text'] = u''

    # 外供汽损失
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        # 生物质发电无此内容
        plandocxcolumdir['content5.9.2_title_loss'] = u''
        plandocxcolumdir['content5.9.2_value_loss'] = u''
        plandocxcolumdir['content5.9.2_uint_loss'] = u''
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
        plandocxcolumdir['content5.9.2_title_loss'] = u'5）外供汽损失：                     '
        plandocxcolumdir['content5.9.2_value_loss'] = plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] * (100-plandocxcolumdir['biomasschp_needs_questionnaire.t_condensate_water_recovery_rate']) * 0.01
        plandocxcolumdir['content5.9.2_uint_loss'] = u't/h'
    else:
        plandocxcolumdir['content5.9.2_title_loss'] = u''
        plandocxcolumdir['content5.9.2_value_loss'] = u''
        plandocxcolumdir['content5.9.2_uint_loss'] = u''


    # 10.1.2工程投资
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        # 生物质发电无此内容
        plandocxcolumdir['content10.1.2_text'] = u''
    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
        plandocxcolumdir['content10.1.2_text'] = u'（2）未包括热力网费用。'
    else:
        plandocxcolumdir['content10.1.2_text'] = u''

    # 5.1.2主要设备参数-型式
    if plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '1' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '2':
        plandocxcolumdir['conten5.1.2_type'] = u'露天布置/紧身封闭布置、自然循环、单锅筒、单炉膛、集中下降管、П型布置、平衡通风、固态排渣、全钢架悬吊结构，主要以农林废弃物为混合燃料。'
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '3':
        plandocxcolumdir['conten5.1.2_type'] = u'露天布置/紧身封闭布置、自然循环、单锅筒、单炉膛、集中下降管、M型布置、平衡通风、固态排渣、全钢构架、底部支撑结构，主要以农林废弃物为混合燃料。'
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '4':
        plandocxcolumdir['conten5.1.2_type'] = u'露天布置/紧身封闭布置、自然循环、单锅筒、单炉膛、集中下降管、M型布置、平衡通风、固态排渣、全钢构架、底部支撑结构，主要以黄色秸秆/灰色秸秆为燃料。'
    else:
        plandocxcolumdir['conten5.1.2_type'] = u''

    # 5.1.2主要设备参数-过热汽温调节方式
    if plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '1' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '2':
        plandocxcolumdir['conten5.1.2_method'] = u'三级加热两级给水喷水减温'
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '3' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '4':
        plandocxcolumdir['conten5.1.2_method'] = u'四级加热三级给水喷水减温'
    else:
        plandocxcolumdir['conten5.1.2_method'] = u''

    # 5.1.2主要设备参数-额定抽汽
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        # 生物质发电无此内容
        plandocxcolumdir['conten5.1.2_title_prated'] = u''
        plandocxcolumdir['conten5.1.2_title_trated'] = u''
        plandocxcolumdir['conten5.1.2_title_frated'] = u''
        plandocxcolumdir['conten5.1.2_value_prated'] = u''
        plandocxcolumdir['conten5.1.2_value_trated'] = u''
        plandocxcolumdir['conten5.1.2_value_frated'] = u''
        plandocxcolumdir['conten5.1.2_unit_prated'] = u''
        plandocxcolumdir['conten5.1.2_unit_trated'] = u''
        plandocxcolumdir['conten5.1.2_unit_frated'] = u''

    elif plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] > 0:
        plandocxcolumdir['conten5.1.2_title_prated'] = u'额定抽汽压力：         '
        plandocxcolumdir['conten5.1.2_title_trated'] = u'额定抽汽温度：         '
        plandocxcolumdir['conten5.1.2_title_frated'] = u'额定抽汽流量：         '

        plandocxcolumdir['conten5.1.2_value_prated'] = plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_pressure']
        plandocxcolumdir['conten5.1.2_value_trated'] = plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_temperature']
        plandocxcolumdir['conten5.1.2_value_frated'] = plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow']

        plandocxcolumdir['conten5.1.2_unit_prated'] = u'MPa（a）'
        plandocxcolumdir['conten5.1.2_unit_trated'] = u'℃'
        plandocxcolumdir['conten5.1.2_unit_frated'] = u't/h'
    else:
        plandocxcolumdir['conten5.1.2_title_prated'] = u''
        plandocxcolumdir['conten5.1.2_title_trated'] = u''
        plandocxcolumdir['conten5.1.2_title_frated'] = u''
        plandocxcolumdir['conten5.1.2_value_prated'] = u''
        plandocxcolumdir['conten5.1.2_value_trated'] = u''
        plandocxcolumdir['conten5.1.2_value_frated'] = u''
        plandocxcolumdir['conten5.1.2_unit_prated'] = u''
        plandocxcolumdir['conten5.1.2_unit_trated'] = u''
        plandocxcolumdir['conten5.1.2_unit_frated'] = u''

    # 5.1.2主要设备参数-给水回热级数
    if plandocxcolumdir['biomasschp_boiler_calculation.f_water_temperature_design'] == 150:
        plandocxcolumdir['conten5.1.2_grade'] = u'共3级（1级GJ＋1级CY＋1级DJ）'
    elif plandocxcolumdir['biomasschp_boiler_calculation.f_water_temperature_design'] == 158:
        plandocxcolumdir['conten5.1.2_grade'] = u'共3级（1级CY＋2级DJ）'
    elif plandocxcolumdir['biomasschp_boiler_calculation.f_water_temperature_design'] == 215:
        plandocxcolumdir['conten5.1.2_grade'] = u'共6级（2级GJ＋1级CY＋3级DJ）'
    else:
        plandocxcolumdir['conten5.1.2_grade'] = u''

    # 5.3点火系统
    if plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '1' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '2':
        plandocxcolumdir['content5.3_text1'] = u'锅炉启动点火考虑采用床下点火，在锅炉风室侧布置2台点火器，点火油枪夏季使用0#轻柴油，冬季使用-20#轻柴油，采用汽车运输到厂。单只喷油量'
        plandocxcolumdir['content5.3_text2'] = plandocxcolumdir['biomasschp_official_process.o_oil_pump']
        plandocxcolumdir['content5.3_text3'] = u'kg/h，油压'
        plandocxcolumdir['content5.3_text4'] = plandocxcolumdir['biomasschp_official_process.o_oil_pump_pressure']
        plandocxcolumdir['content5.3_text5'] = u'MPa，点火启动时间不超过6h。'

    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '3' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '4':
        plandocxcolumdir['content5.3_text1'] = u'锅炉启动点火考虑采用人工点火，即火把点火。'
        plandocxcolumdir['content5.3_text2'] = u''
        plandocxcolumdir['content5.3_text3'] = u''
        plandocxcolumdir['content5.3_text4'] = u''
        plandocxcolumdir['content5.3_text5'] = u''
    else:
        plandocxcolumdir['content5.3_text1'] = u''
        plandocxcolumdir['content5.3_text2'] = u''
        plandocxcolumdir['content5.3_text3'] = u''
        plandocxcolumdir['content5.3_text4'] = u''
        plandocxcolumdir['content5.3_text5'] = u''

    # 5.4燃烧系统
    if plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '1':
        plandocxcolumdir['content5.4_text1'] = u'每台炉还配置二台高压风机，从高压风机出来的高压风一路进入分离器返料管，一路作为给料机密封风。'
        plandocxcolumdir['content5.4_text2'] = u''
        plandocxcolumdir['content5.4_text3'] = u''
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '2':
        plandocxcolumdir['content5.4_text1'] = u''
        plandocxcolumdir['content5.4_text2'] = u'随烟气飞出炉膛的细小颗粒通过两个绝热旋风分离器被分离下来，从返料阀返回炉膛再次实现循环燃烧。分离后，比较洁净的烟气在二燃室内进行二次燃尽并依次通过布置在二燃室内的蒸发受热面、过热器受热面，然后经省煤器及空气预热器后从尾部烟道排出。'
        plandocxcolumdir['content5.4_text3'] = u''
    elif plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '3' or plandocxcolumdir['biomasschp_boiler_calculation.boiler_type'] == '4':
        plandocxcolumdir['content5.4_text1'] = u''
        plandocxcolumdir['content5.4_text2'] = u''
        plandocxcolumdir['content5.4_text3'] = u'生物质燃料从锅炉前墙进入炉膛，一次风由炉底下一次风箱进入炉膛，二次风布置在炉排上方附近。生物质燃料在进入炉排后，逐渐被加热、着火、燃烧，产生的挥发分与一次风强烈混合燃烧。燃烧生成的高温烟气通过炉膛水冷壁、过热器、省煤器及空气预热器各受热面放热冷却后排入炉后烟气系统。锅炉配置一次风机、二次风机各一台，热风约按的比例分配为一、二次风。一次风送入炉排下部风箱，经炉排送入炉膛燃烧。二次风送入炉排上方附近助燃。锅炉尾部排出的烟气经除尘净化后由引风机升压送至烟囱排出。'
    else:
        plandocxcolumdir['content5.4_text1'] = u''
        plandocxcolumdir['content5.4_text2'] = u''
        plandocxcolumdir['content5.4_text3'] = u''

    # 7热力网
    if plandocxcolumdir['biomasschp_turbine_backpressure.e_exhaust_point_flow'] == 0:
        plandocxcolumdir['content7_title'] = u'# 7热力网（生物质发电项目无此部分内容）'
        plandocxcolumdir['content7.1_text1'] = u''
        plandocxcolumdir['content7.1_text2'] = u''
        plandocxcolumdir['content7.1_text3'] = u''
        plandocxcolumdir['content7.1_text4'] = u''
        plandocxcolumdir['content7.1_text5'] = u''

        plandocxcolumdir['content7.2_text1'] = u''
        plandocxcolumdir['content7.2_text2'] = u''
        plandocxcolumdir['content7.2_text3'] = u''
        plandocxcolumdir['content7.2_text4'] = u''
        plandocxcolumdir['content7.2_text5'] = u''
        plandocxcolumdir['content7.2_text6'] = u''
        plandocxcolumdir['content7.2_text7'] = u''
        plandocxcolumdir['content7.2_text8'] = u''
        plandocxcolumdir['content7.2_text9'] = u''
        plandocxcolumdir['content7.2_10text'] = u''
        plandocxcolumdir['content7.2_11text'] = u''
        plandocxcolumdir['content7.2_12text'] = u''

        plandocxcolumdir['content7.3_text1'] = u''
        plandocxcolumdir['content7.3_text2'] = u''
        plandocxcolumdir['content7.3_text3'] = u''
        plandocxcolumdir['content7.3_text4'] = u''
        plandocxcolumdir['content7.3_text5'] = u''
        plandocxcolumdir['content7.3_text6'] = u''
        plandocxcolumdir['content7.3_text7'] = u''
        plandocxcolumdir['content7.3_text8'] = u''
        plandocxcolumdir['content7.3_text9'] = u''

        plandocxcolumdir['content7.4_text1'] = u''
        plandocxcolumdir['content7.4_text2'] = u''

        plandocxcolumdir['content7.5_text1'] = u''
        plandocxcolumdir['content7.5_text2'] = u''
        plandocxcolumdir['content7.5_text3'] = u''

        plandocxcolumdir['content7.6_text1'] = u''
        plandocxcolumdir['content7.6_text2'] = u''
        plandocxcolumdir['content7.6_text3'] = u''
        plandocxcolumdir['content7.6_text4'] = u''
        plandocxcolumdir['content7.6_text5'] = u''
        plandocxcolumdir['content7.6_text6'] = u''
        plandocxcolumdir['content7.6_text7'] = u''
        plandocxcolumdir['content7.6_text8'] = u''
        plandocxcolumdir['content7.6_text9'] = u''

        plandocxcolumdir['content7.7_text1'] = u''
        plandocxcolumdir['content7.7_text2'] = u''
        plandocxcolumdir['content7.7_text3'] = u''
        plandocxcolumdir['content7.7_text4'] = u''
        plandocxcolumdir['content7.7_text5'] = u''

        plandocxcolumdir['content7.8_text1'] = u''
        plandocxcolumdir['content7.8_text2'] = u''
        plandocxcolumdir['content7.8_text3'] = u''
        plandocxcolumdir['content7.8_text4'] = u''
        plandocxcolumdir['content7.8_text5'] = u''
        plandocxcolumdir['content7.8_text6'] = u''
        plandocxcolumdir['content7.8_text7'] = u''
        plandocxcolumdir['content7.8_text8'] = u''
        plandocxcolumdir['content7.8_text9'] = u''
        plandocxcolumdir['content7.8_10text'] = u''

        plandocxcolumdir['content7.9_text1'] = u''
        plandocxcolumdir['content7.9_text2'] = u''

        plandocxcolumdir['content7.10_text1'] = u''
        plandocxcolumdir['content7.10_text2'] = u''
        plandocxcolumdir['content7.10_text3'] = u''
        plandocxcolumdir['content7.10_text4'] = u''
        plandocxcolumdir['content7.10_text5'] = u''
        plandocxcolumdir['content7.10_text6'] = u''
        plandocxcolumdir['content7.10_text7'] = u''
        plandocxcolumdir['content7.10_text8'] = u''
        plandocxcolumdir['content7.10_text9'] = u''
        plandocxcolumdir['content7.10_10text'] = u''
    else:
        plandocxcolumdir['content7_title'] = u'# 7热力网'
        plandocxcolumdir['content7.1_text1'] = u'## 7.1概述'
        plandocxcolumdir['content7.1_text2'] = u'##### 本工程规模为1×'
        plandocxcolumdir['content7.1_text3'] = plandocxcolumdir['biomasschp_turbine_backpressure.e_steam_extraction_select']
        plandocxcolumdir['content7.1_text4'] = u'MW汽轮发电机组，外供热负荷主要为工业热负荷，工业热负荷采用蒸汽供热。'
        plandocxcolumdir['content7.1_text5'] = u'##### 本工程蒸汽供热管网采用架空敷设，机组抽汽由主厂房引出，送到厂区分汽包处，采用蒸汽的热用户由分汽包处接入，直接进行供热。'

        plandocxcolumdir['content7.2_text1'] = u'## 7.2供热介质的确定'
        plandocxcolumdir['content7.2_text2'] = u'##### 根据现场调查，本生物质热电工程是工业热负荷，用汽压力都在XX～XXMPa之间，温度为饱和温度即可。并考虑将来园区建设规模，最大供汽半径拟为X（取值≤10）km，经核算，热源厂供汽压力'
        plandocxcolumdir['content7.2_text3'] = plandocxcolumdir['biomasschp_turbine_backpressure.i_exhaust_point_pressure']
        plandocxcolumdir['content7.2_text4'] = u'MPa蒸汽就能满足用户需要，温度'
        plandocxcolumdir['content7.2_text5'] = plandocxcolumdir['biomasschp_turbine_backpressure.i_exhaust_point_temperature']
        plandocxcolumdir['content7.2_text6'] = u'℃，用户根据自己需要可通过减压阀和温控阀进行必要的调整。因此确定供热参数为——蒸汽：流量'
        plandocxcolumdir['content7.2_text7'] = plandocxcolumdir['biomasschp_heat_supply.hot_turbine_flow']
        plandocxcolumdir['content7.2_text8'] = u't/h，压力'
        plandocxcolumdir['content7.2_text9'] = plandocxcolumdir['biomasschp_turbine_backpressure.i_exhaust_point_pressure']
        plandocxcolumdir['content7.2_10text'] = u'MPa，温度'
        plandocxcolumdir['content7.2_11text'] = plandocxcolumdir['biomasschp_turbine_backpressure.i_exhaust_point_temperature']
        plandocxcolumdir['content7.2_12text'] = u'℃。'

        plandocxcolumdir['content7.3_text1'] = u'## 7.3管网走向及敷设方式'
        plandocxcolumdir['content7.3_text2'] = u'### 7.3.1管网走向'
        plandocxcolumdir['content7.3_text3'] = u'##### 根据热用户的分布，蒸汽管网供热区域为以热源点为中心，半径X（取值≤10）km范围内。'
        plandocxcolumdir['content7.3_text4'] = u'##### 厂区外管线敷设方式按以下原则考虑：蒸汽管网在主要马路两侧采用直埋，在次要马路上，在不影响交通的情况下考虑采用架空敷设。'
        plandocxcolumdir['content7.3_text5'] = u'### 7.3.2热网敷设方式的比较'
        plandocxcolumdir['content7.3_text6'] = u'##### 蒸汽管网有地沟、架空、直埋三种敷设方式。'
        plandocxcolumdir['content7.3_text7'] = u'##### 蒸汽管网，由于地沟敷设方式防水性能差，而且造价较高，本工程不宜采用，为保证管网敷设既节省投资又较少影响城区美观，本管网敷设除在城区主要干道上采用塑套钢蒸汽直埋外，其余均采用架空敷设。'
        plandocxcolumdir['content7.3_text8'] = u'### 7.3.3管道跨越河流、公路的方案'
        plandocxcolumdir['content7.3_text9'] = u'##### 蒸汽管网跨越河流均采用架空敷设，蒸汽管道跨越公路及主要干道时，采用套管敷设，当必须采用架空敷设时，管道下底标高距地面应大于4.5米。'

        plandocxcolumdir['content7.4_text1'] = u'## 7.4连接方式'
        plandocxcolumdir['content7.4_text2'] = u'##### 蒸汽管网与热用户采用直接连接，根据热用户的用汽参数确定是否采用减压装置。'

        plandocxcolumdir['content7.5_text1'] = u'## 7.5热网调节方式'
        plandocxcolumdir['content7.5_text2'] = u'### 7.5.1蒸汽网的调节和监测'
        plandocxcolumdir['content7.5_text3'] = u'##### 蒸汽管网在各热用户入口设置流量、压力、温度测量装置，并设置上述参数的远传装置，将上述参数远传到热电厂主控室监测，由运行管理人员根据热负荷的需要统一调度，在满足生产用热要求的前提下，尽可能降低热电厂出口蒸汽压力，以提高节能效益。'

        plandocxcolumdir['content7.6_text1'] = u'## 7.6水力计算'
        plandocxcolumdir['content7.6_text2'] = u'### 7.6.1水力计算'
        plandocxcolumdir['content7.6_text3'] = u'##### 1）比摩阻：考虑整个管网的经济性，比摩阻取值主要在30～70Pa/m之间。'
        plandocxcolumdir['content7.6_text4'] = u'##### 2）蒸汽管网：管内绝对粗糙度为0.2mm。'
        plandocxcolumdir['content7.6_text5'] = u'##### 3）蒸汽管道按满足末端用户的用汽参数和控制蒸汽流速为依据选择管径。'
        plandocxcolumdir['content7.6_text6'] = u'### 7.6.2凝结水回收'
        plandocxcolumdir['content7.6_text7'] = u'##### 凝结水回收率约为'
        plandocxcolumdir['content7.6_text8'] = plandocxcolumdir['biomasschp_needs_questionnaire.t_condensate_water_recovery_rate']
        plandocxcolumdir['content7.6_text9'] = u'%，凝结水经除铁等除杂装置处理后，补入除氧器中。'

        plandocxcolumdir['content7.7_text1'] = u'## 7.7保温防腐'
        plandocxcolumdir['content7.7_text2'] = u'### 7.7.1管道敷设方式及保温结构'
        plandocxcolumdir['content7.7_text3'] = u'##### 蒸汽管道采用架空敷设时，保温材料采用高温玻璃棉，外保护壳采用彩钢板，直埋敷设时采用钢套管直埋预制保温管。'
        plandocxcolumdir['content7.7_text4'] = u'### 7.7.2管道防腐'
        plandocxcolumdir['content7.7_text5'] = u'##### 蒸汽管道采用无机富锌漆防腐。'

        plandocxcolumdir['content7.8_text1'] = u'## 7.8结构设计'
        plandocxcolumdir['content7.8_text2'] = u'### 7.8.1主要建筑材料'
        plandocxcolumdir['content7.8_text3'] = u'##### 1）水泥：采用普通硅酸盐水泥；'
        plandocxcolumdir['content7.8_text4'] = u'##### 2）钢材：型钢及钢板主要采用Q235B碳素结构钢；在材质的选用上，管径DN200及以上，设计选用螺旋缝电焊钢管，材质为Q235B；DN200以下，设计选用无缝钢管，材质为20#钢；'
        plandocxcolumdir['content7.8_text5'] = u'##### 3）钢筋：构造钢筋用I级钢，主要受力钢筋用II级钢；。'
        plandocxcolumdir['content7.8_text6'] = u'##### 4）混凝土：垫层C15，支架C25。'
        plandocxcolumdir['content7.8_text7'] = u'### 7.8.2结构形式'
        plandocxcolumdir['content7.8_text8'] = u'##### 在满足工艺要求的前提下，主要采用架空与直埋敷设，架空支架与直埋支架均采用现浇钢筋砼结构。'
        plandocxcolumdir['content7.8_text9'] = u'### 7.8.3特殊部位的支架'
        plandocxcolumdir['content7.8_10text'] = u'##### 跨越河流的管道根据河的宽度，采用架空支架直接跨越或钢桁架形式跨越；跨越铁路的管道采用套管敷设；跨越公路的管道考虑采用高架空、直埋或套管敷设。'

        plandocxcolumdir['content7.9_text1'] = u'## 7.9生产组织及施工进度'
        plandocxcolumdir['content7.9_text2'] = u'##### 热力网由生物质热电厂统一管理。'

        plandocxcolumdir['content7.10_text1'] = u'## 7.10主要经济指标'
        plandocxcolumdir['content7.10_text2'] = u'##### 1）供汽参数：                       '
        plandocxcolumdir['content7.10_text3'] = plandocxcolumdir['biomasschp_turbine_backpressure.i_exhaust_point_pressure']
        plandocxcolumdir['content7.10_text4'] = u'MPa，'
        plandocxcolumdir['content7.10_text5'] = plandocxcolumdir['biomasschp_turbine_backpressure.i_exhaust_point_temperature']
        plandocxcolumdir['content7.10_text6'] = u'℃'
        plandocxcolumdir['content7.10_text7'] = u'##### 2）额定供汽量：                    '
        plandocxcolumdir['content7.10_text8'] = plandocxcolumdir['biomasschp_turbine_backpressure.i_exhaust_point_flow']
        plandocxcolumdir['content7.10_text9'] = u't/h'
        plandocxcolumdir['content7.10_10text'] = u'##### 3）最大供热半径：                  X（取值≤10）km'


    return plandocxcolumdir
