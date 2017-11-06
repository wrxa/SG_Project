# -*- coding: utf-8 -*-
from ..gasPowerGeneration_models import GasPowerGenerationNeedsQuestionnaire
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