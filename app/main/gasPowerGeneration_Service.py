# -*- coding: utf-8 -*-
from ..gasPowerGeneration_models import GasPowerGenerationNeedsQuestionnaire,\
    GPGBoilerOfPTS, GPGFlueGasAirSystem
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
    "chimney_total_resistance"
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

    #返回烟风系统值
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