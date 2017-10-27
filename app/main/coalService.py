# -*- coding: utf-8 -*-
from ..models import CoalCHPNeedsQuestionnaire, CoalCHPComponent
from flask_login import current_user
from ..models import Company, Plan, Module

lists = [
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

        for index in range(len(lists)):
            if form.get(lists[index]) != '':
                setattr(questionnaire, lists[index], form.get(lists[index]))
        return questionnaire

    @staticmethod
    def to_questionnaireJson(questionnaire):
        datas = {}
        planId = getattr(questionnaire, 'plan_id')
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        for index in range(len(lists)):
            datas[lists[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(questionnaire, lists[index])))
        datas['company_name'] = companyName
        datas['company_location'] = companyLocation
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