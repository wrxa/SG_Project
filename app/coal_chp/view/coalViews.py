# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session, redirect, \
 url_for, flash
from flask_login import login_required, current_user
from . import coalviews
from ...models import Plan, Company, User
from app.coal_chp.model.coalchpModels import CoalCHPComponent, \
    CoalCHPConstant, \
    CoalCHPNeedsQuestionnaire, CoalCHPFurnaceCalculation,\
    CoalCHPCoalHandingSystem, CoalCHPRemovalAshSlag, CoalCHPDesulfurization,\
    CoalCHPCirculatingWater, CoalCHPSmokeAirSystem, CoalCHPBoilerAuxiliaries
from ..service.coalService import ToCoalCHP


# 所有方案管理頁面
@coalviews.route('/coalPlanList')
@login_required
def coalPlanList():
    session['coalCHPPlanId'] = None
    plans = Plan.search_plan_all()
    # plans_distinct = Plan.search_distinct_user()
    companys = Company.search_company()
    users = User.select_all()
    return render_template(
        'page/coalCHP/coalPlanList.html',
        plans=plans,
        companys=companys,
        users=users,
        # plans_distinct=plans_distinct,
        menuSelect='coalPlanList')


# 按查询条件检索方案
@coalviews.route('/queryPlans', methods=['POST'])
@login_required
def queryPlans():
    company_id = request.values.get('company_id')
    user_id = request.values.get('user_id')
    plans = Plan.search_planByParams(company_id, user_id)
    companys = Company.search_company()
    users = User.select_all()
    plansJson = ToCoalCHP.to_planJson(plans)
    companyJson = ToCoalCHP.to_companyJson(companys)
    userJson = ToCoalCHP.to_userJson(users)
    return jsonify({
        'newPlans': plansJson,
        'companys': companyJson,
        'users': userJson
    })


# 删除方案
@coalviews.route('/deleteCoalPlan/<int:planId>', methods=['GET', 'POST'])
@login_required
def deleteCoalPlan(planId):
    ToCoalCHP.drop_plan(planId)
    flash(u'用户删除成功', 'success')
    return redirect(url_for('coalviews.coalPlanList'))


# 新增或修改方案进入
@coalviews.route('/coalQuestionnaire/<int:id>')
@login_required
def coalQuestionnaire(id):
    coalCHPComponent = CoalCHPComponent.search_coalCHPComponent()
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_questionnaire")
    # 查询已有方案
    plans = Plan.search_plan(current_user.id)
    companys = Company.search_company()
    if id > 0:
        session['coalCHPPlanId'] = id
    elif not session['coalCHPPlanId']:
        session['coalCHPPlanId'] = None
    return render_template(
        'page/coalCHP/coalQuestionnaire.html',
        coalsort=coalCHPComponent,
        constants=coalCHPConstant,
        plans=plans,
        companys=companys)


# 初始化需求调查表数据
@coalviews.route('/initQuestionnaire', methods=['POST'])
@login_required
def initQuestionnaire():
    questionnaireData = "null"
    if session.get('coalCHPPlanId'):
        questionnaire = CoalCHPNeedsQuestionnaire.search_questionnaire(
            session.get('coalCHPPlanId'))
        questionnaireData = ToCoalCHP.to_questionnaireJson(questionnaire)
    return jsonify({'questionnaire': questionnaireData})


@coalviews.route('/coalSort', methods=['POST'])
@login_required
def coalSort():
    id = request.values.get('id')
    datas = ToCoalCHP.to_coalCHPComponentJson(id)

    return jsonify({'coalSort': datas})


@coalviews.route('/formData', methods=['POST'])
@login_required
def formData():
    companyName = request.form.get('company_name')
    companyLocation = request.form.get('company_location')

    plan_id = ToCoalCHP.create_plan(companyName, companyLocation)

    questionnaire = ToCoalCHP.to_questionnaire(request.form, plan_id)

    CoalCHPNeedsQuestionnaire.insert_questionnaire(questionnaire)
    session['coalCHPPlanId'] = plan_id
    return jsonify({'planId': plan_id})


@coalviews.route('/initFurnace', methods=['POST'])
@login_required
def initFurnace():
    furnace = CoalCHPFurnaceCalculation.search_furnace_calculation(
        session.get('coalCHPPlanId'))
    furnaceData = ToCoalCHP.to_furnaceJson(furnace)
    return jsonify({'furnace': furnaceData})


@coalviews.route('/formDataFurnace', methods=['POST'])
@login_required
def formDataFurnace():

    furnaceData = ToCoalCHP.to_furnace(request.form,
                                       session.get('coalCHPPlanId'))

    CoalCHPFurnaceCalculation.insert_furnace_calculation(furnaceData)
    newData = CoalCHPFurnaceCalculation.search_furnace_calculation(
        session.get('coalCHPPlanId'))
    datas = ToCoalCHP.to_furnaceJson(newData)

    return jsonify({'newDatas': datas})


@coalviews.route('/findPlan', methods=['POST'])
@login_required
def findPlan():
    planId = request.values.get('planId')
    questionnaire = CoalCHPNeedsQuestionnaire.search_questionnaire(planId)
    questionnaireData = ToCoalCHP.to_questionnaireJson(questionnaire)
    session['coalCHPPlanId'] = planId
    return jsonify({'questionnaire': questionnaireData})


@coalviews.route('/coalFurnace')
@login_required
def coalFurnace():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_furnaceCalculation")
    return render_template(
        'page/coalCHP/coalFurnace.html',
        constants=coalCHPConstant)


@coalviews.route('/coalSteamTurbine')
@login_required
def coalSteamTurbine():
    return render_template(
        'page/coalCHP/coalSteamTurbine.html')


# 脱硫脱硝Desulfurization and denitrification
@coalviews.route('/coalDesulfurization')
@login_required
def coalDesulfurization():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_desulfurization")
    return render_template(
        'page/coalCHP/coalDesulfurization.html',
        constants=coalCHPConstant)


# 初始化脱硫脱硝数据
@coalviews.route('/initDesulfurization', methods=['POST'])
@login_required
def initDesulfurization():
    desulfurization = CoalCHPDesulfurization.search_desulfurization(
        session.get('coalCHPPlanId'))
    desulfurizationData = ToCoalCHP.to_desulfurizationJson(desulfurization)
    return jsonify({'desulfurization': desulfurizationData})


# 提交脱硫脱硝页面值
@coalviews.route('/formDesulfurization', methods=['POST'])
@login_required
def formDesulfurization():
    desulfurization = ToCoalCHP.to_desulfurization(
        request.form, session.get('coalCHPPlanId'))
    CoalCHPDesulfurization.insert_desulfurization(desulfurization)
    newData = CoalCHPDesulfurization.search_desulfurization(
        session.get('coalCHPPlanId'))
    datas = ToCoalCHP.to_desulfurizationJson(newData)
    return jsonify({'newDatas': datas})


# 输煤系统
@coalviews.route('/coalHandingSystem')
@login_required
def coalHandingSystem():
    coalHandingSystemConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_CoalHandingSystem")
    return render_template(
        'page/coalCHP/coalHandingSystem.html',
        constants=coalHandingSystemConstant)


# 初始化输煤系统数据
@coalviews.route('/initHandingSystem', methods=['POST'])
@login_required
def initHandingSystem():
    handingSystem = CoalCHPCoalHandingSystem.search_handing_system(
        session.get('coalCHPPlanId'))
    handingSystemData = ToCoalCHP.to_handingSystemJson(handingSystem)
    return jsonify({'handingSystem': handingSystemData})


# 提交输煤系统页面值
@coalviews.route('/formDataHandingSystem', methods=['POST'])
@login_required
def formDataHandingSystem():
    handingSystem = ToCoalCHP.to_handingSystem(request.form,
                                               session.get('coalCHPPlanId'))
    CoalCHPCoalHandingSystem.insert_handing_system(handingSystem)

    newData = CoalCHPCoalHandingSystem.search_handing_system(
        session.get('coalCHPPlanId'))
    datas = ToCoalCHP.to_handingSystemJson(newData)
    return jsonify({'newDatas': datas})


@coalviews.route('/coalBoilerAuxiliaries')
@login_required
def coalBoilerAuxiliaries():
    coalHandingSystemConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_boilerAuxiliaries")
    return render_template(
        'page/coalCHP/coalBoilerAuxiliaries.html',
        constants=coalHandingSystemConstant)


# 初始化锅炉辅机系统数据
@coalviews.route('/initBoilerAuxiliaries', methods=['POST'])
@login_required
def initBoilerAuxiliaries():
    boilerAuxiliaries = CoalCHPBoilerAuxiliaries.search_boiler_auxiliaries(
        session.get('coalCHPPlanId'))
    boilerAuxiliariesData = ToCoalCHP.to_boilerAuxiliariesJson(
        boilerAuxiliaries)
    return jsonify({'boilerAuxiliaries': boilerAuxiliariesData})


# 提交锅炉辅机系统页面值
@coalviews.route('/formDataBoilerAuxiliaries', methods=['POST'])
@login_required
def formDataBoilerAuxiliaries():
    boilerAuxiliaries = ToCoalCHP.to_boilerAuxiliaries(
        request.form, session.get('coalCHPPlanId'))
    CoalCHPBoilerAuxiliaries.insert_boiler_auxiliaries(boilerAuxiliaries)
    newData = CoalCHPBoilerAuxiliaries.search_boiler_auxiliaries(
        session.get('coalCHPPlanId'))
    datas = ToCoalCHP.to_boilerAuxiliariesJson(
        newData)
    return jsonify({'newDatas': datas})


# 除灰除渣
@coalviews.route('/coalRemovalAshSlag')
@login_required
def coalRemovalAshSlag():
    coalHandingSystemConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_removalAshSlag")
    return render_template(
        'page/coalCHP/coalRemovalAshSlag.html',
        constants=coalHandingSystemConstant)


# 初始化除灰除渣数据
@coalviews.route('/initRemovalAshSlag', methods=['POST'])
@login_required
def initRemovalAshSlag():
    removalAshSlag = CoalCHPRemovalAshSlag.search_removal_ash_slag(
        session.get('coalCHPPlanId'))
    removalAshSlagData = ToCoalCHP.to_removalAshSlagJson(removalAshSlag)
    return jsonify({'removalAshSlag': removalAshSlagData})


# 提交除灰除渣页面值
@coalviews.route('/formRemovalAshSlag', methods=['POST'])
@login_required
def formRemovalAshSlag():
    removalAshSlag = ToCoalCHP.to_removalAshSlag(request.form,
                                                 session.get('coalCHPPlanId'))
    CoalCHPRemovalAshSlag.insert_removal_ash_slag(removalAshSlag)
    newData = CoalCHPRemovalAshSlag.search_removal_ash_slag(
        session.get('coalCHPPlanId'))
    datas = ToCoalCHP.to_removalAshSlagJson(newData)
    return jsonify({'newDatas': datas})


# 循环水系统页面 
@coalviews.route('/coalCirculatingWater')
@login_required
def coalCirculatingWater():
    coalHandingSystemConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_circulatingWater")
    return render_template(
        'page/coalCHP/coalCirculatingWater.html',
        constants=coalHandingSystemConstant)


# 初始化循环水系统数据
@coalviews.route('/initCirculatingWater', methods=['POST'])
@login_required
def initCirculatingWater():
    circulatingWater = CoalCHPCirculatingWater.search_circulating_water(
        session.get('coalCHPPlanId'))
    circulatingWaterData = ToCoalCHP.to_circulatingWaterJson(circulatingWater)
    return jsonify({'circulatingWater': circulatingWaterData})


# 提交循环水系统页面值
@coalviews.route('/formCirculatingWater', methods=['POST'])
@login_required
def formCirculatingWater():
    circulatingWater = ToCoalCHP.to_circulatingWater(
        request.form, session.get('coalCHPPlanId'))
    CoalCHPCirculatingWater.insert_circulating_water(circulatingWater)
    newData = CoalCHPCirculatingWater.search_circulating_water(
        session.get('coalCHPPlanId'))
    datas = ToCoalCHP.to_circulatingWaterJson(newData)
    return jsonify({'newDatas': datas})


@coalviews.route('/coalSmokeAirSystem')
@login_required
def coalSmokeAirSystem():
    coalHandingSystemConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_smokeAirSystem")
    return render_template(
        'page/coalCHP/coalSmokeAirSystem.html',
        constants=coalHandingSystemConstant)


# 初始化烟风系统数据
@coalviews.route('/initSmokeAirSystem', methods=['POST'])
@login_required
def initSmokeAirSystem():
    smokeAirSystem = CoalCHPSmokeAirSystem.search_smoke_air_system(
        session.get('coalCHPPlanId'))
    circulatingWaterData = ToCoalCHP.to_smokeAirSystemJson(smokeAirSystem)
    return jsonify({'smokeAirSystem': circulatingWaterData})


# 提交烟风系统页面值
@coalviews.route('/formSmokeAirSystem', methods=['POST'])
@login_required
def formSmokeAirSystem():
    smokeAirSystem = ToCoalCHP.to_smokeAirSystem(
        request.form, session.get('coalCHPPlanId'))
    CoalCHPSmokeAirSystem.insert_smoke_air_system(smokeAirSystem)
    newData = CoalCHPSmokeAirSystem.search_smoke_air_system(
        session.get('coalCHPPlanId'))
    datas = ToCoalCHP.to_smokeAirSystemJson(newData)
    return jsonify({'newDatas': datas})
