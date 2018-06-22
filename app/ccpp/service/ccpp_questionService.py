# -*- coding: utf-8 -*-
"""
ccpp需求调查表：sheet的服务处理程序
"""
from app.ccpp.models.constantModel import CcppConstant
from app.models import Plan, Company
from flask_login import current_user
from app.models import Module
from ..models.ccpp_questionnaireModel import Questionnaire
from ..models.ccpp_ccpp_economicModel import Ccpp_ccpp_economic
from app.ccpp import gl
from app import db


class QuestionService():
    '''
    进入需求调查表页面
    加载字段常量数据、加载已有方案、加载公司信息
    '''
    @staticmethod
    def getQuestionnaireConstant():
        ccppConstant = CcppConstant.search_ccppConstant('ccpp_questionnaire')
        # 查询已有方案
        plans = Plan.search_planByUidAndMid(current_user.id, Module.CCPP)
        companys = Company.search_company()
        gl.listsort(ccppConstant)
        return ccppConstant, plans, companys

    '''
    如果公司存在，则直接在计划表中查找当前用户对CCPP模块的方案
    如果查找不到则新建方案再返回方案ID，如果查找到则直接返回方案ID
    '''
    def submitQuestionnaire(self, form, companyName, planName, company_location, planId, company_lnglat):
        if form is None:
            form = gl.getQuestionName_engDict()
            form['company_name'] = companyName
            form['plan_name'] = planName
            form['company_location'] = company_location
        plan = Plan.search_planById(planId)
        # 修改需求调研表
        if plan is not None:
            return self.updata_questionnaire(form, planId)
        # 创建需求调研表
        else:
            companyName = form.get('company_name')
            company_location = form.get('company_location')
            plan_name = form.get('plan_name')
            if companyName == '' or company_location == '' or plan_name == '':
                return None
            # 新增公司信息
            company = Company.query.filter_by(company_name=companyName).first()
            if not company:
                company = Company()
                company.company_name = companyName
                Company.insert_company(company)
            newCompany = Company.query.filter_by(company_name=companyName).first()
            companyId = newCompany.id
            # 创建方案：只有公司、模块、操作人、项目名称均不一致时才会创建
            plan = Plan.query.filter_by(company_id=companyId, module_id=Module.CCPP, plan_name=plan_name).first()
            if not plan:
                plan = Plan()
                plan.plan_name = plan_name
                plan.user_id = current_user.id
                plan.company_id = companyId
                plan.module_id = Module.CCPP
                plan.company_location = company_location
                plan.company_lnglat = company_lnglat
                Plan.insert_plan(plan)
            newPlan = Plan.query.filter_by(company_id=companyId, module_id=Module.CCPP, plan_name=plan_name).first()
            # 将表单中的数据更新到需求表中
            return self.updata_questionnaire(form, newPlan.id)

    def updata_questionnaire(self, form, plan_id):
        '''
        将表单中的数据更新到需求表中
        '''
        questionnaire = Questionnaire.query.filter_by(
            plan_id=plan_id).first()
        # 构造列
        list_column_questionnaire = gl.getQuestionName_engList()
        # 为模型赋值
        for index in range(len(list_column_questionnaire)):
            formdata = form.get(list_column_questionnaire[index])
            if formdata is not None and formdata != '':
                setattr(questionnaire, list_column_questionnaire[index], formdata)
            else:
                setattr(questionnaire, list_column_questionnaire[index],
                        None)
        # 更新数据
        Questionnaire.updata_questionnaire(questionnaire)
        # 同步数据到经济分析表
        # 将字段：天然气价格、电价格、蒸汽价格、采暖价格（如果采用上网用电取上网用电）同步
        ccpp_ccpp_economic = Ccpp_ccpp_economic.search_economic(plan_id)
        ccpp_ccpp_economic.natural_gas_price = questionnaire.price_design
        ccpp_ccpp_economic.energy_supply_steam_price = questionnaire.steam_price_1
        ccpp_ccpp_economic.energy_supply_for_heating = questionnaire.heating_load_price
        ccpp_ccpp_economic.energy_supply_price = questionnaire.net_electricity_price if questionnaire.surf_internet_flage == '1' else questionnaire.personal_electricity_price
        Ccpp_ccpp_economic.updata_ccppeconomic(ccpp_ccpp_economic)
        return questionnaire

    def getQuestionnaireDataJson(self, planId):
        '''
        将模型questionnaire中的数据转换为json格式
        '''
        questionnaire = Questionnaire.search_questionnaire(planId)
        datas = {}
        planId = getattr(questionnaire, 'plan_id')
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        plan_name = plan.plan_name
        list_column_questionnaire = gl.getQuestionName_engList()
        for index in range(len(list_column_questionnaire)):
            datas[list_column_questionnaire[index]] = gl.format_value(
                getattr(questionnaire, list_column_questionnaire[index]))
        datas['company_name'] = companyName
        datas['plan_name'] = plan_name
        datas['company_location'] = companyLocation
        datas['planId'] = planId
        return datas

    def deletebyPlanId(self, planId):
        questionnaire = Questionnaire.search_questionnaire(planId)
        db.session.delete(questionnaire)

    def findbyPlanId(self, planId):
        return Questionnaire.search_questionnaire(planId)
        