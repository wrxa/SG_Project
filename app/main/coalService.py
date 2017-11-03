# -*- coding: utf-8 -*-
from ..models import CoalCHPNeedsQuestionnaire, CoalCHPComponent,\
     CoalCHPFurnaceCalculation
from flask_login import current_user
from ..models import Company, Plan, Module
from ..observer_calculate.execution_strategy import Furnace_calculationBefore

list_column_questionnaire = [
    's_fuel_design', 's_fuel_check', 's_carbon_design', 's_carbon_check',
    's_hydrogen_design', 's_hydrogen_check', 's_oxygen_design',
    's_oxygen_check', 's_nitrogen_design', 's_nitrogen_check',
    's_sulfur_design', 's_sulfur_check', 's_water_design', 's_water_check',
    's_grey_design', 's_grey_check', 's_daf_design', 's_daf_check',
    's_grindability_design', 's_grindability_check', 's_low_design',
    's_low_check', 'w_altitude_value', 'w_mean_annual_temperature_value',
    'w_mean_summer_temperature_value', 'w_mean_winter_temperature_value',
    'w_mean_annual_barometric_value', 'w_mean_summer_barometric_value',
    'w_mean_winter_barometric_value',
    'w_annual_average_relative_humidity_value',
    'ihl_steam_pressure_level_value', 'ihl_steam_temperature_level_value',
    'ihl_steam_time_value', 'ihl_recent_steam_flow_range_value',
    'ihl_forward_steam_flow_range_value', 'ihl_condensate_water_iron_value',
    'ihl_condensate_water_recovery_rate_value',
    'hhl_heating_occasions_type_value', 'hhl_year_heating_days_value',
    'hhl_recent_heating_area_value', 'hhl_forward_heating_area_value',
    'os_planning_area_value', 'os_planned_expansion_capacity_value',
    'os_local_water_condition_value', 'oe_electrical_load_demand_value',
    'oe_higher_voltage_level_value', 'oe_plant_distance_higher_change_value',
    'oe_is_internet_access_value', 'oe_is_isolated_network_value',
    'op_flue_gas_sox_limits_value', 'op_flue_gas_nox_limits_value',
    'op_flue_gas_dust_limits_value', 'od_use_desulfurization_form_value',
    'od_use_denitration_form_value', 'od_limestone_supply_value',
    'od_urea_or_ammonia_water_supply_value'
]

list_column_furnace = [
    'plan_id', 's_carbon_design', 's_carbon_check', 's_hydrogen_design',
    's_hydrogen_check', 's_oxygen_design', 's_oxygen_check',
    's_nitrogen_design', 's_nitrogen_check', 's_sulfur_design',
    's_sulfur_check', 's_grey_design', 's_grey_check', 's_water_design',
    's_water_check', 's_sum_design', 's_sum_check', 's_daf_design',
    's_daf_check', 's_grindability_design', 's_grindability_check',
    's_low_design', 's_low_check', 's_low_1_design', 's_low_1_check',
    's_low_estimation_design', 's_low_estimation_check',
    's_high_estimation_design', 's_high_estimation_check',
    'f_steam_flow_design', 'f_steam_flow_check', 'f_steam_pressure_design',
    'f_steam_pressure_check', 'f_steam_temperature_design',
    'f_steam_temperature_check', 'f_steam_enthalpy_design',
    'f_steam_enthalpy_check', 'f_boiler_pressure_design',
    'f_boiler_pressure_check', 'f_saturated_water_enthalpy_design',
    'f_saturated_water_enthalpy_check', 'f_water_temperature_design',
    'f_water_temperature_check', 'f_water_enthalpy_design',
    'f_water_enthalpy_check', 'f_boiler_efficiency_design',
    'f_boiler_efficiency_check', 'f_unburned_loss_design',
    'f_unburned_loss_check', 'f_blowdown_rate_design', 'f_blowdown_rate_check',
    'f_boiler_consumption_design', 'f_boiler_consumption_check',
    'f_calculation_consumption_design', 'f_calculation_consumption_check',
    'd_total_design', 'd_total_check', 'd_boiler_total_design',
    'd_boiler_total_check', 'd_ash_share_design', 'd_ash_share_check',
    'd_dust_share_design', 'd_dust_share_check', 'd_ash_total_design',
    'd_ash_total_check', 'd_dust_total_design', 'd_dust_total_check',
    'a_air_volumn_design', 'a_air_volumn_check', 'a_hot_temperature_design',
    'a_hot_temperature_check', 'a_humidity_design', 'a_humidity_check',
    'a_pressure_design', 'a_pressure_check', 'a_temperature_design',
    'a_temperature_check', 'a_saturation_pressure_design',
    'a_saturation_pressure_check', 'a_steam_perssure_design',
    'a_steam_perssure_check', 'a_air_humidity_design', 'a_air_humidity_check',
    'a_standard_air_humidity_design', 'a_standard_air_humidity_check',
    'a_wet_air_volumn_design', 'a_wet_air_volumn_check',
    's_nitrogen_volume_design', 's_nitrogen_volume_check',
    's_dioxide_volume_design', 's_dioxide_volume_check',
    's_steam_volume_design', 's_steam_volume_check', 's_smoke_volume_design',
    's_smoke_volume_check', 's_1kg_weight_design', 's_1kg_weight_check',
    's_wet_smoke_density_design', 's_wet_smoke_density_check',
    'p_boiler_air_design', 'p_boiler_air_check', 'p_wind_design',
    'p_wind_check', 'p_wind_air_design', 'p_wind_air_check', 'p_high_design',
    'p_high_check', 'p_hign_air_design', 'p_hign_air_check', 'p_low_design',
    'p_low_check', 'p_low_air_design', 'p_low_air_check', 'p_fule_design',
    'p_fule_check', 'p_fule_air_design', 'p_fule_air_check', 'p_heater_design',
    'p_heater_check', 'p_heater_air_design', 'p_heater_air_check',
    'p_plus_air_design', 'p_plus_air_check', 'p_dust_exit_design',
    'p_dust_exit_check', 'p_dust_design', 'p_dust_check',
    'p_dust_entry_design', 'p_dust_entry_check', 'p_plus_dust_design',
    'p_plus_dust_check', 'p_fans_air_design', 'p_fans_air_check',
    'p_1kg_volume_design', 'p_1kg_volume_check', 'p_1kg_quality_design',
    'p_1kg_quality_check', 'p_heater_type_design', 'p_heater_type_check',
    'p_heater_first_entry_design', 'p_heater_first_entry_check',
    'p_heater_second_entry_design', 'p_heater_second_entry_check',
    'p_heater_first_exit_design', 'p_heater_first_exit_check',
    'p_heater_second_exit_design', 'p_heater_second_exit_check',
    'p_smoke_temperature_design', 'p_smoke_temperature_check',
    'a_theory_air_quality_design', 'a_theory_air_quality_check',
    'a_boiler_air_design', 'a_boiler_air_check', 'a_actual_air_design',
    'a_actual_air_check', 'a_calculation_consumption_design',
    'a_calculation_consumption_check', 'a_actual_air_total_design',
    'a_actual_air_total_check', 'a_first_wind_volume_design',
    'a_first_wind_volume_check', 'a_cwind_temperature_calculation_design',
    'a_cwind_temperature_calculation_check', 'a_local_pressure_design',
    'a_local_pressure_check', 'a_first_cwind_standard_design',
    'a_first_cwind_standard_check', 'a_first_cwind_actual_design',
    'a_first_cwind_actual_check', 'a_first_standard_air_density_design',
    'a_first_standard_air_density_check', 'a_first_cwind_flow_design',
    'a_first_cwind_flow_check', 'a_first_cwind_density_design',
    'a_first_cwind_density_check', 'a_check_design', 'a_check_check',
    'a_first_hwind_temperatue_design', 'a_first_hwind_temperatue_check',
    'a_first_hwind_flow_design', 'a_first_hwind_flow_check',
    'a_first_wet_air_density_design', 'a_first_wet_air_density_check',
    'a_second_wind_volume_design', 'a_second_wind_volume_check',
    'a_cwind_temperature_design', 'a_cwind_temperature_check',
    'a_second_cwind_standard_design', 'a_second_cwind_standard_check',
    'a_second_cwind_actual_design', 'a_second_cwind_actual_check',
    'a_second_standard_air_density_design',
    'a_second_standard_air_density_check', 'a_second_cwind_flow_design',
    'a_second_cwind_flow_check', 'a_second_cwind_density_design',
    'a_second_cwind_density_check', 'a_second_hwind_temperatue_design',
    'a_second_hwind_temperatue_check', 'a_second_hwind_flow_design',
    'a_second_hwind_flow_check', 'a_second_wet_air_density_design',
    'a_second_wet_air_density_check', 'h_1kg_volume_design',
    'h_1kg_volume_check', 'h_1kg_quality_design', 'h_1kg_quality_check',
    'h_calculation_consumption_design', 'h_calculation_consumption_check',
    'h_standard_smoke_flow_design', 'h_standard_smoke_flow_check',
    'h_smoke_flow_design', 'h_smoke_flow_check', 'h_smoke_temperature_design',
    'h_smoke_temperature_check', 'h_smoke_volume_design',
    'h_smoke_volume_check', 'h_smoke_density_design', 'h_smoke_density_check',
    'd_exit_air_design', 'd_exit_air_check', 'd_wind_parameter_design',
    'd_wind_parameter_check', 'd_entry_air_design', 'd_entry_air_check',
    'd_cold_air_temperature_design', 'd_cold_air_temperature_check',
    'd_entry_somke_temperature_design', 'd_entry_somke_temperature_check',
    'd_standard_1kg_volume_design', 'd_standard_1kg_volume_check',
    'd_entry_1kg_quality_design', 'd_entry_1kg_quality_check',
    'd_standard_smoke_flow_design', 'd_standard_smoke_flow_check',
    'd_entry_somke_flow_design', 'd_entry_somke_flow_check',
    'd_entry_smoke_actual_flow_design', 'd_entry_smoke_actual_flow_check',
    'e_wind_parameter_design', 'e_wind_parameter_check',
    'e_air_parameter_design', 'e_air_parameter_check',
    'e_smoke_temperature_design', 'e_smoke_temperature_check',
    'e_standard_1kg_volume_design', 'e_standard_1kg_volume_check',
    'e_1kg_quality_design', 'e_1kg_quality_check',
    'e_standard_smoke_flow_design', 'e_standard_smoke_flow_check',
    'e_smoke_flow_design', 'e_smoke_flow_check', 'e_smoke_actual_flow_design',
    'e_smoke_actual_flow_check', 'e_smoke_actual_density_design',
    'e_smoke_actual_density_check', 'i_wind_parameter_design',
    'i_wind_parameter_check', 'i_air_parameter_design',
    'i_air_parameter_check', 'i_smoke_temperature_design',
    'i_smoke_temperature_check', 'i_standard_1kg_volume_design',
    'i_standard_1kg_volume_check', 'i_1kg_quality_design',
    'i_1kg_quality_check', 'i_standard_smoke_flow1_design',
    'i_standard_smoke_flow1_check', 'i_standard_smoke_flow2_design',
    'i_standard_smoke_flow2_check', 'i_smoke_flow_design',
    'i_smoke_flow_check', 'i_smoke_actual_flow1_design',
    'i_smoke_actual_flow1_check', 'i_smoke_actual_flow2_design',
    'i_smoke_actual_flow2_check', 'i_smoke_actual_density_design',
    'i_smoke_actual_density_check', 'i_wet_smoke_actual_density_design',
    'i_wet_smoke_actual_density_check', 'go_oxygen_vol_design',
    'go_oxygen_vol_check', 'go_theoretica_vol_design',
    'go_theoretica_vol_check', 'go_theoretica_flow_design',
    'go_theoretica_flow_check', 'go_calculation_consumption_design',
    'go_calculation_consumption_check', 'go_air_parameter_design',
    'go_air_parameter_check', 'go_standard_1kg_volume_design',
    'go_standard_1kg_volume_check', 'go_smoke_flow_design',
    'go_smoke_flow_check', 'go_drygas_oxygen_vol_design',
    'go_drygas_oxygen_vol_check', 'go_total_combustion_product_vol_design',
    'go_total_combustion_product_vol_check'
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
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        result = float(str(float(values)).rstrip('0'))
    else:
        result = values
    return result


class ToCoalCHP():
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
            plan.module_id = Module.coalCHP
            Plan.insert_plan(plan)
        plan.company_location = companyLocation
        newPlan = Plan.query.filter_by(company_id=companyId).first()
        return newPlan.id

    @staticmethod
    def to_questionnaire(form, plan_id):
        questionnaire = CoalCHPNeedsQuestionnaire.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_questionnaire)):
            if form.get(list_column_questionnaire[index]) != '':
                setattr(questionnaire, list_column_questionnaire[index],
                        form.get(list_column_questionnaire[index]))
        return questionnaire

    @staticmethod
    def to_questionnaireJson(questionnaire):
        datas = {}
        planId = getattr(questionnaire, 'plan_id')
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        for index in range(len(list_column_questionnaire)):
            datas[list_column_questionnaire[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(questionnaire, list_column_questionnaire[index])))
        datas['company_name'] = companyName
        datas['company_location'] = companyLocation
        datas['planId'] = planId
        return datas

    @staticmethod
    def to_coalCHPComponentJson(id):
        datas = {}
        coalCHPComponent = CoalCHPComponent.search_coalCHPSort(id)
        datas['s_carbon'] = coalCHPComponent.carbon
        datas['s_hydrogen'] = coalCHPComponent.hydrogen
        datas['s_oxygen'] = coalCHPComponent.oxygen
        datas['s_nitrogen'] = coalCHPComponent.nitrogen
        datas['s_sulfur'] = coalCHPComponent.sulfur
        datas['s_water'] = coalCHPComponent.water
        datas['s_grey'] = coalCHPComponent.grey
        datas['s_daf'] = coalCHPComponent.daf
        datas['s_grindability'] = coalCHPComponent.grindability
        datas['s_low'] = coalCHPComponent.low
        return datas

    @staticmethod
    def to_furnaceJson(furnace):
        datas = {}
        for index in range(len(list_column_furnace)):
            datas[list_column_furnace[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(furnace, list_column_furnace[index])))
        return datas

    @staticmethod
    def to_furnace(form, plan_id):
        furnace = CoalCHPFurnaceCalculation.query.filter_by(
            plan_id=plan_id).first()

        furnace = Furnace_calculationBefore().specialCalculation(furnace, form)

        list_column_furnace.remove('f_steam_enthalpy_design')
        list_column_furnace.remove('f_steam_enthalpy_check')

        list_column_furnace.remove('a_saturation_pressure_design')
        list_column_furnace.remove('a_saturation_pressure_check')

        list_column_furnace.remove('f_water_enthalpy_design')
        list_column_furnace.remove('f_water_enthalpy_check')

        list_column_furnace.remove('f_saturated_water_enthalpy_design')
        list_column_furnace.remove('f_saturated_water_enthalpy_check')
     
        for index in range(len(list_column_furnace)):
            if form.get(list_column_furnace[index]) != '':
                setattr(furnace, list_column_furnace[index],
                        form.get(list_column_furnace[index]))
        setattr(furnace, 'plan_id', plan_id)
        list_column_furnace.append('f_steam_enthalpy_design')
        list_column_furnace.append('f_steam_enthalpy_check')

        list_column_furnace.append('a_saturation_pressure_design')
        list_column_furnace.append('a_saturation_pressure_check')

        list_column_furnace.append('f_water_enthalpy_design')
        list_column_furnace.append('f_water_enthalpy_check')

        list_column_furnace.append('f_saturated_water_enthalpy_design')
        list_column_furnace.append('f_saturated_water_enthalpy_check')
        return furnace
