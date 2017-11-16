# -*- coding: utf-8 -*-
from ..gasPowerGeneration_models import GasPowerGenerationNeedsQuestionnaire,\
    GPGBoilerOfPTS, GPGFlueGasAirSystem, GPGSmokeResistance, GPGWindResistance, \
    GPGCirculatingWaterSystem, GPGSmokeAirCalculate
from flask_login import current_user
from ..models import Company, Plan, Module
from ..observer_calculate.execution_strategy import Furnace_calculationBefore

list_smoke_air_calculate = [
    'component_h2',
    'component_co',
    'component_ch4',
    'component_c2h4',
    'component_c3h8',
    'component_c4h10',
    'component_n2',
    'component_o2',
    'component_co2',
    'component_h2s',
    'component_cmhn',
    'hl_h2',
    'hl_co',
    'hl_ch4',
    'hl_c2h4',
    'hl_c3h8',
    'hl_c4h10',
    'hl_n2',
    'hl_o2',
    'hl_co2',
    'hl_h2s',
    'hl_cmhn',
    'hh_h2',
    'hh_co',
    'hh_ch4',
    'hh_c2h4',
    'hh_c3h8',
    'hh_c4h10',
    'hh_n2',
    'hh_o2',
    'hh_co2',
    'hh_h2s',
    'hh_cmhn',
    'cpsh_h2',
    'cpsh_co',
    'cpsh_ch4',
    'cpsh_c2h4',
    'cpsh_c3h8',
    'cpsh_c4h10',
    'cpsh_n2',
    'cpsh_o2',
    'cpsh_co2',
    'cpsh_h2s',
    'cpsh_cmhn',
    'constant_need_air_amonut_per_m3',
    'constant_air_density',
    'constant_need_air_mass_per_m3',
    'excessive_air_coefficient',
    'actual_need_air_amonut',
    'constant_gas_humidity_per_m3',
    'constant_air_humidity_per_m3',
    'actual_air_amount_in_wet',
    'constant_ro2_amonut_per_m3',
    'constant_n2_amonut_per_m3',
    'constant_actual_n2_amonut_per_m3',
    'constant_h2o_amonut_per_m3',
    'constant_actual_h2o_amonut_per_m3',
    'constant_o2_amonut_per_m3',
    'actual_burning_gas_amonut',
    'theory_burning_gas_amonut',
    'net_calorific_value',
    'gross_heating_value',
    'gas_init_temperature',
    'air_init_temperature',
    'gas_average_cpvh',
    'gas_h2o_average_cpvh',
    'air_average_cpvh',
    'air_h2o_average_cpvh',
    'hy_adiabatic_calorimeter_temperature',
    'smoke_ro2_average_cpvh',
    'smoke_h2o_average_cpvh',
    'smoke_n2_average_cpvh',
    'smoke_o2_average_cpvh',
    'calc_adiabatic_calorimeter_temperature',
    'deviation_check',
    'incomplete_combustion_loss_coefficient',
    'incomplete_combustion_loss',
    'heat_loss_coefficient',
    'heat_loss',
    'calc_theory_burning_temperature',
    'high_temperature_coefficient',
    'coefficient_actual_temperature',
    'calc_actual_temperature',
    'ro2_volume_enthalpy',
    'n2_volume_enthalpy',
    'h2o_volume_enthalpy',
    'air_volume_enthalpy',
    'dust_volume_enthalpy',
    'theory_smoke_volume_enthalpy',
    'theory_air_volume_enthalpy',
    'theory_dust_volume_enthalpy',
    'smoke_enthalpy',
    'qd_net',
    'qar_net',
    'unknown_need_air_amonut_b_10500',
    'unknown_need_air_amonut_a_10500',
    'unknown_need_air_amonut_gas',
    'unknown_need_air_amonut_lng',
    'unknown_excessive_air_coefficient',
    'unknown_actual_need_air_amonut',
    'unknown_theory_burning_amonut_gas',
    'unknown_theory_burning_amonut_oag',
    'unknown_theory_burning_amonut_lng',
    'unknown_theory_burning_amonut_cog',
    'unknown_theory_burning_amonut_b_12600',
    'unknown_actual_burning_gas_amonut',
    'unknown_boiler_actual_burning_gas_amonut',
    'unknown_gas_actual_burning_gas_amonut',
    'exp_gas_qnet',
    'exp_gas_theory_air_amount_a_35799',
    'exp_gas_theory_air_amount_b_35799',
    'exp_gas_excessive_air_coefficient',
    'exp_gas_actual_amonut_a_35799',
    'exp_gas_actual_amonut_b_35799',
    'exp_boiler_qnet',
    'exp_boiler_excessive_air_coefficient',
    'exp_liquid_fuel_qnet',
    'exp_liquid_fuel_theory_air_amount',
    'exp_liquid_fuel_excessive_air_coefficient',
    'exp_liquid_fuel_actual_amonut',
    'exp_coal_qnet',
    'exp_coal_theory_air_amount',
    'exp_coal_excessive_air_coefficient',
    'exp_coal_actual_amonut',
    'exp_wood_peat_qnet',
    'exp_wood_peat_water_content',
    'exp_wood_peat_theory_air_amount',
    'exp_wood_peat_excessive_air_coefficient',
    'exp_wood_peat_best_water_content',
    'exp_wood_peat_actual_amonut',
    'exp_boiler_theory_air_amount_a_12561',
    'exp_boiler_theory_air_amount_b_12561',
    'exp_boiler_actual_amonut_a_12561',
    'exp_boiler_actual_amonut_b_12561'
]

list_questionnaire = [
    'surplus_gas_bfg', 'surplus_gas_ldg', 'surplus_gas_cog',
    'bfg_gas_temperature', 'ldg_gas_temperature', 'cog_gas_temperature',
    'bfg_gas_pressure', 'ldg_gas_pressure', 'cog_gas_pressure',
    'bfg_gas_calorific_value', 'ldg_gas_calorific_value', 'cog_gas_calorific_value',
    'provide_steam_amount', 'provide_steam_pressure',
    'h2_content', 'co_content', 'ch4_content', 'c2h4_content',
    'c3h8_content', 'c4h10_content', 'n2_content',
    'o2_content', 'co2_content', 'h2s_content', 'cmhn_content',
    'atmosphere_temperature_h', 'atmosphere_temperature_a', 'atmosphere_temperature_l',
    'atmosphere_pressure_h', 'atmosphere_pressure_a', 'atmosphere_pressure_l',
    'relative_humidity_h', 'relative_humidity_a', 'relative_humidity_l',
    'outside_wind_speed_h', 'outside_wind_speed_a', 'outside_wind_speed_l',
    'seismic_fortification_intensity_h', 'seismic_fortification_intensity_a',
    'seismic_fortification_intensity_l',
    'water_pressure', 'water_temperature', 'water_ph',
    'water_suspended_matter', 'water_cl',
    'nitrogen_purity', 'nitrogen_pressure', 'nitrogen_temperature',
    'compressed_air_pressure', 'compressed_air_temperature',
    'grid_voltage', 'max_short_circuit_capacity', 'factory_location_elevation',
    'dielectric_position_height_caliber_route', 'water_quality_analysis_report',
    'cooling_tower', 'project_approval_eia'
]

list_boiler_of_pts = [
    'surplus_gas_bfg', 'surplus_gas_ldg', 'surplus_gas_cog',
    'bfg_gas_calorific_value', 'ldg_gas_calorific_value', 'cog_gas_calorific_value',
    'boiler_efficiency', 'superheated_steam_outlet_pressure',
    'superheated_steam_temperature', 'superheated_steam_enthalpy', 'excess_air_coefficient',
    'air_temperature', 'air_enthalpy', 'air_need_for_combustion', 'boiler_feed_water_temperature',
    'feedwater_enthalpy', 'rate_of_blowdown', 'saturation_water_temperature',
    'saturation_water_enthalpy', 'steam_output'
]

list_gas_air_system = [
    "c2s_condition_temperature_air", "c2s_condition_flux_air",
    "c2s_local_atmosphere_air", "c2s_standard_temperature_air",
    "c2s_standard_pressure_air", "c2s_standard_flux_air",
    "c2s_condition_temperature_smoke", "c2s_condition_flux_smoke",
    "c2s_local_atmosphere_smoke", "c2s_standard_temperature_smoke",
    "c2s_standard_pressure_smoke", "c2s_standard_flux_smoke",
    "s2c_standard_temperature_air", "s2c_standard_pressure_air",
    "s2c_standard_flux_air", "s2c_condition_temperature_air",
    "s2c_local_atmosphere_air", "s2c_condition_flux_air",
    "s2c_standard_temperature_smoke", "s2c_standard_pressure_smoke",
    "s2c_standard_flux_smoke", "s2c_condition_temperature_smoke",
    "s2c_local_atmosphere_smoke", "s2c_condition_flux_smoke",
    "s2c_standard_temperature_gas", "s2c_standard_pressure_gas",
    "s2c_standard_flux_gas", "s2c_condition_temperature_gas",
    "s2c_local_atmosphere_gas", "s2c_condition_flux_gas",
    "blower_air_temperature", "blower_wind_resistance",
    "blower_local_atmosphere", "blower_condition_smoke_flux",
    "blower_fan_temperature", "blower_fan_total_pressure",
    "blower_fan_selected_total_pressure", "blower_fan_selected_flux",
    "blower_fan_pressure_efficiency", "blower_transmission_efficiency",
    "blower_motor_efficiency", "blower_fan_shaft_power",
    "blower_motor_safe_margin", "blower_motor_power",
    "blower_specification_power", "blower_specification_flux",
    "induced_smoke_temperature", "induced_local_atmosphere",
    "induced_condition_smoke_flux", "induced_fan_temperature",
    "induced_smoke_density", "induced_fan_total_pressure",
    "induced_fan_selected_total_pressure", "induced_fan_selected_flux",
    "induced_fan_efficiency", "induced_transmission_efficiency",
    "induced_motor_efficiency", "induced_fan_shaft_power",
    "induced_motor_safe_margin", "induced_motor_power",
    "induced_specification_power", "induced_specification_flux",
    "gas_tube_medium_flux", "gas_tube_medium_temperature",
    "gas_tube_flow_velocity", "gas_tube_calculated_cross_sectional_area",
    "gas_tube_calculated_diameter", "gas_tube_selected_diameter",
    "gas_tube_selected_thickness", "coldwind_tube_medium_flux",
    "coldwind_tube_medium_temperature", "coldwind_tube_flow_velocity",
    "coldwind_tube_calculated_cross_sectional_area",
    "coldwind_tube_calculated_diameter", "coldwind_tube_length",
    "coldwind_tube_width", "coldwind_tube_specification",
    "hotwind_tube_medium_flux", "hotwind_tube_medium_temperature",
    "hotwind_tube_flow_velocity",
    "hotwind_tube_calculated_cross_sectional_area",
    "hotwind_tube_calculated_diameter", "hotwind_tube_length",
    "hotwind_tube_width", "hotwind_tube_specification",
    "total_smoke_tube_medium_flux", "total_smoke_tube_medium_temperature",
    "total_smoke_tube_flow_velocity",
    "total_smoke_tube_calculated_cross_sectional_area",
    "total_smoke_tube_calculated_diameter", "total_smoke_tube_length",
    "total_smoke_tube_width", "total_smoke_tube_specification",
    "branch_smoke_tube_medium_flux", "branch_smoke_tube_medium_temperature",
    "branch_smoke_tube_flow_velocity",
    "branch_smoke_tube_calculated_cross_sectional_area",
    "branch_smoke_tube_calculated_diameter", "branch_smoke_tube_length",
    "branch_smoke_tube_width", "branch_smoke_tube_specification",
    "main_hotwind_tube_medium_flux", "main_hotwind_tube_medium_temperature",
    "main_hotwind_tube_flow_velocity",
    "main_hotwind_tube_calculated_cross_sectional_area",
    "main_hotwind_tube_calculated_diameter",
    "main_hotwind_tube_selected_diameter",
    "main_hotwind_tube_selected_thickness", "branch_hotwind_tube_medium_flux",
    "branch_hotwind_tube_medium_temperature",
    "branch_hotwind_tube_flow_velocity",
    "branch_hotwind_tube_calculated_cross_sectional_area",
    "branch_hotwind_tube_calculated_diameter",
    "branch_hotwind_tube_selected_diameter",
    "branch_hotwind_tube_selected_thickness", "chimney_height",
    "local_atmosphere", "standard_air_density",
    "standard_average_smoke_density", "standard_calculated_smoke_density",
    "outdoor_air_temperature", "chimney_inlet_temperature",
    "chimney_temperature_drop_per_meter", "chimney_average_temperature",
    "chimney_draft", "smoke_amount", "chimney_outlet_temperature",
    "chimney_outlet_flow", "chimney_outlet_inner_diameter",
    "chimney_outlet_selected_inner_diameter",
    "chimney_experience_base_diameter", "low_load_smoke_amount",
    "low_load_smoke_temperature", "low_load_flow_30_percent",
    "chimney_resistance_coefficient", "chimney_average_velocity",
    "chimney_average_diameter", "chimney_friction_resistance",
    "chimney_outlet_resistance_coefficient", "chimney_outlet_resistance",
    "chimney_total_resistance", "induced_total_pressure"
]

list_smoke_resistance = [
    "air_preheater_outlet_calculated_temperature",
    "air_preheater_outlet_smoke_amount", "air_preheater_density",
    "air_preheater_flow_velocity", "air_preheater_dynamic_pressure_head",
    "air_preheater_smoke_tube_area", "air_preheater_length",
    "air_preheater_width", "air_preheater_duct_perimeter",
    "air_preheater_tube_equivalent_diameter",
    "air_preheater_gas_kinetic_viscosity", "air_preheater_reynolds_number",
    "air_preheater_absolute_tube_roughness",
    "air_preheater_relative_tube_roughness",
    "air_preheater_560_relative_tube_roughness", "air_preheater_discriminant",
    "air_preheater_frictional_resistance",
    "air_preheater_frictional_resistance_coefficient",
    "air_preheater_unit_length_frictional_resistance",
    "air_preheater_ducting_length", "air_preheater_local_resistance",
    "air_preheater_local_resistance_coefficient",
    "air_preheater_90_outlet_sharp_turn_elbow",
    "air_preheater_powder_local_resistance_coefficient",
    "air_preheater_air_elbow_local_resistance_coefficient",
    "air_preheater_powder_concentration_corrected_coefficient",
    "air_preheater_90_section_slow_turn_elbow",
    "air_preheater_slow_powder_local_resistance_coefficient",
    "air_preheater_slow_air_local_resistance_coefficient",
    "air_preheater_slow_powder_concentration_corrected_coefficient",
    "air_preheater_reducer_tube", "air_preheater_to_deduster_total_resistance",
    "deduster_outlet_calculated_temperature", "deduster_outlet_smoke_amount",
    "deduster_density", "deduster_flow_velocity",
    "deduster_dynamic_pressure_head", "deduster_smoke_tube_area",
    "deduster_length", "deduster_width", "deduster_duct_perimeter",
    "deduster_tube_equivalent_diameter", "deduster_gas_kinetic_viscosity",
    "deduster_reynolds_number", "deduster_absolute_tube_roughness",
    "deduster_relative_tube_roughness", "deduster_560_relative_tube_roughness",
    "deduster_discriminant", "deduster_frictional_resistance",
    "deduster_frictional_resistance_coefficient",
    "deduster_unit_length_frictional_resistance", "deduster_ducting_length",
    "deduster_local_resistance", "deduster_local_resistance_coefficient",
    "deduster_90_outlet_slow_turn_elbow",
    "deduster_slow_powder_local_resistance_coefficient",
    "deduster_slow_air_local_resistance_coefficient",
    "deduster_slow_powder_concentration_corrected_coefficient",
    "deduster_90_section_slow_turn_elbow",
    "deduster_section_slow_powder_local_resistance_coefficient",
    "deduster_section_slow_air_local_resistance_coefficient",
    "deduster_corrected_turning_angle_coefficient",
    "deduster_section_corrected_height_width_ratio_coefficient",
    "deduster_section_original_resistance_coefficient_with_roughness",
    "deduster_section_slow_powder_corrected_coefficient",
    "deduster_inlet_bellows", "deduster_to_induced_draft_total_resistance",
    "induced_draft_inlet_calculated_temperature",
    "induced_draft_inlet_smoke_amount", "induced_draft_density",
    "induced_draft_flow_velocity", "induced_draft_dynamic_pressure_head",
    "induced_draft_smoke_tube_area", "induced_draft_width",
    "induced_draft_height", "induced_draft_duct_perimeter",
    "induced_draft_tube_equivalent_diameter",
    "induced_draft_gas_kinetic_viscosity", "induced_draft_reynolds_number",
    "induced_draft_absolute_tube_roughness",
    "induced_draft_relative_tube_roughness",
    "induced_draft_560_relative_tube_roughness", "induced_draft_discriminant",
    "induced_draft_frictional_resistance",
    "induced_draft_frictional_resistance_coefficient",
    "induced_draft_unit_length_frictional_resistance",
    "induced_draft_ducting_length", "induced_draft_local_resistance",
    "induced_draft_local_resistance_coefficient",
    "induced_draft_outlet_plate_gate", "induced_draft_outlet_diffuser_tube",
    "induced_draft_45_90_slow_turn_elbow",
    "induced_draft_powder_local_resistance_coefficient",
    "induced_draft_air_local_resistance_coefficient",
    "induced_draft_corrected_turning_angle_coefficient",
    "induced_draft_corrected_height_width_ratio_coefficient",
    "induced_draft_original_resistance_coefficient_with_roughness",
    "induced_draft_powder_concentration_corrected_coefficient",
    "brick_chimney_inlet", "induced_draft_to_chimney_total_resistance",
    "smoke_chimney_total_resistance"
]

list_wind_resistance = [
    "recommend_velocity_coldwind", "recommend_velocity_hotwind",
    "intake_to_preheater_temperature", "intake_to_preheater_amount",
    "intake_to_preheater_density", "intake_to_preheater_flow_velocity",
    "intake_to_preheater_dynamic_pressure_head", "fan_inlet_duct_section_area",
    "fan_inlet_duct_length", "fan_inlet_duct_width",
    "fan_inlet_duct_perimeter", "fan_inlet_duct_equivalent_diameter",
    "fan_inlet_gas_kinetic_viscosity", "fan_inlet_reynolds_number",
    "fan_inlet_absolute_tube_roughness", "fan_inlet_relative_tube_roughness",
    "fan_inlet_560_relative_tube_roughness", "fan_inlet_discriminant",
    "fan_inlet_frictional_resistance",
    "fan_inlet_frictional_resistance_coefficient",
    "fan_inlet_unit_length_frictional_resistance", "fan_inlet_ducting_length",
    "fan_inlet_local_resistance", "fan_inlet_local_resistance_coefficient",
    "fan_inlet_single_local_resistance_coefficient",
    "fan_inlet_single_bellows", "fan_inlet_single_damper",
    "fan_inlet_total_pressure", "fan_outlet_frictional_resistance",
    "fan_outlet_unit_length_frictional_resistance",
    "fan_outlet_ducting_length", "fan_outlet_local_resistance",
    "fan_outlet_local_resistance_coefficient",
    "fan_outlet_single_increase_pipe", "fan_outlet_90_section_slow_turn_elbow",
    "fan_outlet_preheater_diffuser_pipe",
    "fan_outlet_to_preheater_total_pressure",
    "preheater_to_boiler_temperature", "preheater_to_boiler_amount",
    "preheater_to_boiler_density", "preheater_to_boiler_flow_velocity",
    "preheater_to_boiler_dynamic_pressure_head",
    "preheater_outlet_duct_section_area", "preheater_outlet_duct_diameter",
    "preheater_outlet_duct_length", "preheater_outlet_duct_width",
    "preheater_outlet_duct_perimeter",
    "preheater_outlet_duct_equivalent_diameter",
    "preheater_outlet_gas_kinetic_viscosity",
    "preheater_outlet_reynolds_number",
    "preheater_outlet_absolute_tube_roughness",
    "preheater_outlet_relative_tube_roughness",
    "preheater_outlet_560_relative_tube_roughness",
    "preheater_outlet_discriminant", "preheater_outlet_frictional_resistance",
    "preheater_outlet_frictional_resistance_coefficient",
    "preheater_outlet_unit_length_frictional_resistance",
    "preheater_outlet_ducting_length", "preheater_outlet_local_resistance",
    "preheater_outlet_local_resistance_coefficient",
    "preheater_outlet_shrink_pipe", "preheater_outlet_90_sharp_turn_elbow",
    "preheater_outlet_90_sharp_turn_elbow_count",
    "preheater_outlet_90_sharp_turn_elbow_resistance",
    "preheater_outlet_air_intake_gate", "preheater_outlet_combustor_gate",
    "preheater_outlet_to_boiler_total_pressure", "windhole_total_pressure"
]

list_circulating_water_system = [
    'steam_exhaust_flux_winter', 'steam_exhaust_flux_summer',
    'steam_exhaust_flux_selected', 'circulation_ratio_winter',
    'circulation_ratio_summer', 'circulation_water_flow_winter',
    'circulation_water_flow_summer', 'auxiliary_cooling_water_flow_winter',
    'auxiliary_cooling_water_flow_summer',
    'total_circulation_water_flow_winter',
    'total_circulation_water_flow_summer',
    'selected_total_circulation_water_flow', 'spray_density', 'spray_area',
    'in_out_water_temperature_difference', 'dry_bulb_temperature',
    'dry_bulb_k_coefficient', 'evaporation_loss_rate', 'evaporation_loss',
    'wind_blow_loss_rate', 'wind_blow_loss', 'concentration_rate',
    'discharge_rate', 'discharge_capacity', 'supply_water_amount',
    'circulating_pool_water_amount', 'circulating_pool_size_deep',
    'circulating_pool_size_length', 'circulating_pool_size_width',
    'circulating_pool_size_checked',
    'condenser_circulating_water_inlet_pressure', 'condenser_friction',
    'circulating_backwater_pressure', 'circulating_water_reservoir_pressure',
    'circulation_pump_outlet_to_condenser_inlet_height_difference',
    'reservoir_to_pump_inlet_height_difference', 'pipe_loss', 'y_filter_loss',
    'total_pumping_lift', 'pump_flow', 'pump_efficiency',
    'pump_transmission_efficiency', 'pump_motor_efficiency',
    'pump_motor_spare_coefficient', 'pump_matching_motor_power',
    'selected_pump_model_power', 'selected_pump_model_flow',
    'selected_pump_model_lift'
]

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
    elif values == "True":
        result = True
    elif values == "False":
        result = False
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        result = float(str(float(values)).rstrip('0'))
    else:
        result = values
    return result


class ToGPG():
    @staticmethod
    def create_plan(companyName, companyLocation):
        # 新增公司信息
        company = Company.query.filter_by(company_name=companyName).first()
        if not company:
            company = Company()
            company.company_name = companyName
            Company.insert_company(company)
        newCompany = Company.query.filter_by(company_name=companyName).first()
        companyId = newCompany.id
        # 创建方案
        plan = Plan.query.filter_by(company_id=companyId).first()
        if not plan:
            plan = Plan()
            plan.user_id = current_user.id
            plan.company_id = companyId
            plan.module_id = Module.gasPowerGeneration
            Plan.insert_plan(plan)
        plan.company_location = companyLocation
        newPlan = Plan.query.filter_by(company_id=companyId).first()
        return newPlan.id

    @staticmethod
    def to_questionnaire(form, plan_id):
        questionnaire = GasPowerGenerationNeedsQuestionnaire.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_questionnaire)):
            if form.get(list_questionnaire[index]) != '':
                setattr(questionnaire, list_questionnaire[index],
                        form.get(list_questionnaire[index]))
        return questionnaire

    @staticmethod
    def to_questionnaireJson(questionnaire):
        datas = {}
        planId = getattr(questionnaire, 'plan_id')
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        for index in range(len(list_questionnaire)):
            datas[list_questionnaire[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(questionnaire, list_questionnaire[index])))
        datas['company_name'] = companyName
        datas['company_location'] = companyLocation
        datas['planId'] = planId
        return datas

    #返回烟风量计算json值
    @staticmethod
    def to_SmokeAirCalculateJson(SmokeAirCalculateData):
        json = {}
        for index in range(len(list_smoke_air_calculate)):
            json[list_smoke_air_calculate[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(SmokeAirCalculateData, list_smoke_air_calculate[index])))
        return json

    @staticmethod
    def to_SmokeAirCalculateData(form, plan_id):
        SmokeAirCalculateData = GPGSmokeAirCalculate.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_smoke_air_calculate)):
            if form.get(list_smoke_air_calculate[index]) != '':
                setattr(SmokeAirCalculateData, list_smoke_air_calculate[index],
                        form.get(list_smoke_air_calculate[index]))
        return SmokeAirCalculateData

    #返回循环水系统json值
    @staticmethod
    def to_CirculatingWaterJson(CirculatingWaterData):
        json = {}
        for index in range(len(list_circulating_water_system)):
            json[list_circulating_water_system[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(CirculatingWaterData, list_circulating_water_system[index])))
        return json

    @staticmethod
    def to_CirculatingWaterData(form, plan_id):
        CirculatingWaterData = GPGCirculatingWaterSystem.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_circulating_water_system)):
            if form.get(list_circulating_water_system[index]) != '':
                setattr(CirculatingWaterData, list_circulating_water_system[index],
                        form.get(list_circulating_water_system[index]))
        return CirculatingWaterData

    #返回烟风系统json值
    @staticmethod
    def to_GasAirJson(GasAirData):
        json = {}
        for index in range(len(list_gas_air_system)):
            json[list_gas_air_system[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(GasAirData, list_gas_air_system[index])))
        return json

    @staticmethod
    def to_GasAirData(form, plan_id):
        GasAirData = GPGFlueGasAirSystem.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_gas_air_system)):
            if form.get(list_gas_air_system[index]) != '':
                setattr(GasAirData, list_gas_air_system[index],
                        form.get(list_gas_air_system[index]))
        return GasAirData

    #返回烟阻力json值
    @staticmethod
    def to_SmokeResistanceJson(SmokeResistanceData):
        json = {}
        for index in range(len(list_smoke_resistance)):
            json[list_smoke_resistance[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(SmokeResistanceData, list_smoke_resistance[index])))
        return json

    @staticmethod
    def to_SmokeResistanceData(form, plan_id):
        SmokeResistanceData = GPGSmokeResistance.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_smoke_resistance)):
            if form.get(list_smoke_resistance[index]) != '':
                setattr(SmokeResistanceData, list_smoke_resistance[index],
                        form.get(list_smoke_resistance[index]))
        return SmokeResistanceData

    #返回风阻力json值
    @staticmethod
    def to_WindResistanceJson(WindResistanceData):
        json = {}
        for index in range(len(list_wind_resistance)):
            json[list_wind_resistance[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(WindResistanceData, list_wind_resistance[index])))
        return json

    @staticmethod
    def to_WindResistanceData(form, plan_id):
        WindResistanceData = GPGWindResistance.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_wind_resistance)):
            if form.get(list_wind_resistance[index]) != '':
                setattr(WindResistanceData, list_wind_resistance[index],
                        form.get(list_wind_resistance[index]))
        return WindResistanceData


    #返回锅炉页面初期值
    @staticmethod
    def to_BoilerJson(BoilerData):
        json = {}
        for index in range(len(list_boiler_of_pts)):
            json[list_boiler_of_pts[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(BoilerData, list_boiler_of_pts[index])))
        return json

    #获得锅炉页面表单的信息
    @staticmethod
    def to_BoilerOfPTS(form, plan_id):
        boiler = GPGBoilerOfPTS.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_boiler_of_pts)):
            if form.get(list_boiler_of_pts[index]) != '':
                setattr(boiler, list_boiler_of_pts[index],
                        form.get(list_boiler_of_pts[index]))
        return boiler