# -*- coding: utf-8 -*-
from ..gasPowerGeneration_models import GasPowerGenerationNeedsQuestionnaire,\
    GPGBoilerOfPTS, GPGFlueGasAirSystem, GPGSmokeResistance
from flask_login import current_user
from ..models import Company, Plan, Module
from ..observer_calculate.execution_strategy import Furnace_calculationBefore

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