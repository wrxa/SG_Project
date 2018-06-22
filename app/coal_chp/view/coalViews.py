# -*- coding: utf-8 -*-
import json
from flask import render_template, jsonify, request, session, current_app
from flask_login import login_required, current_user
from . import coalviews
from ...models import Plan, Company, Module, EquipmentList, \
     EquipmentListTemplate
from app.coal_chp.model.coalchpModels import CoalCHPComponent, \
    CoalCHPConstant, CoalCHPNeedsQuestionnaire, CoalCHPFurnaceCalculation,\
    CoalCHPCoalHandingSystem, CoalCHPRemovalAshSlag, CoalCHPDesulfurization,\
    CoalCHPCirculatingWater, CoalCHPSmokeAirSystem, CoalCHPBoilerAuxiliaries,\
    CoalCHPTurbineBackpressure, CoalCHPEconomicIndicators, \
    CoalCHPChemicalWater, CoalCHPChimney, CoalchpTurbineAuxiliary,\
    CoalCHPOfficialProcess, CoalCHPHeatSupply
from ..service.coalService import ToCoalCHP, format_value
from util.iapws_if97 import seuif97
from app.main.service.mainService import MainService


# 跳转到方案的燃煤需求调查表详情页面
# 本模块面包屑中专用，区别与main.editPlan
@coalviews.route('/coalQuestionnaire/<int:id>')
@login_required
def coalQuestionnaire(id):
    '''
    跳转到方案的燃煤需求调查表详情页面
    本模块面包屑中专用，区别与main.editPlan
    方案id
    '''
    coalCHPComponent = CoalCHPComponent.search_coalCHPComponent()
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_questionnaire")
    # 查询已有方案
    plans = Plan.search_plan(current_user.id)
    companys = Company.search_company()
    if id > 0:
        session['planId'] = id
    elif not session['planId']:
        session['planId'] = None
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
    if session.get('planId'):
        questionnaire = CoalCHPNeedsQuestionnaire.search_questionnaire(
            session.get('planId'))
        questionnaireData = ToCoalCHP.to_questionnaireJson(questionnaire)
    return jsonify({'questionnaire': questionnaireData})


# 选择煤种
@coalviews.route('/coalSort', methods=['POST'])
@login_required
def coalSort():
    id = request.values.get('id')
    datas = ToCoalCHP.to_coalCHPComponentJson(id)

    return jsonify({'coalSort': datas})


# 提交需求调查表数据
@coalviews.route('/formData', methods=['POST'])
@login_required
def formData():
    companyName = request.form.get('company_name')
    plan_name = request.form.get('plan_name')
    state = "1"
    # 修改
    if session.get('planId'):
        companyLocation = request.form.get('company_location')
        plan_id = ToCoalCHP.create_plan(companyName, plan_name, companyLocation, None)
        questionnaire = ToCoalCHP.to_questionnaire(request.form, plan_id)
        CoalCHPNeedsQuestionnaire.insert_questionnaire(questionnaire)
        ToCoalCHP.update_plan_date(plan_id)
        session['planId'] = plan_id
    # 如果是新增方案
    else:
        # 判断数据库中是否有相同的方案名的方案
        plan = Plan.search_planByParams(companyName, '', Module.coalCHP)
        # 数据库存在则不做操作直接给用户提示
        # 避免取到重名覆盖掉原来的数据
        if plan:
            state = "0"
        else:
            companyLocation = request.form.get('company_location')
            plan_id = ToCoalCHP.create_plan(companyName, companyLocation, None)
            questionnaire = ToCoalCHP.to_questionnaire(request.form, plan_id)
            CoalCHPNeedsQuestionnaire.insert_questionnaire(questionnaire)
            ToCoalCHP.update_plan_date(plan_id)
            session['planId'] = plan_id

    return jsonify({'state': state})


@coalviews.route('/initFurnace', methods=['POST'])
@login_required
def initFurnace():
    furnace = CoalCHPFurnaceCalculation.search_furnace_calculation(
        session.get('planId'))
    furnaceData = ToCoalCHP.to_furnaceJson(furnace)
    return jsonify({'furnace': furnaceData})


@coalviews.route('/formDataFurnace', methods=['POST'])
@login_required
def formDataFurnace():

    furnaceData = ToCoalCHP.to_furnace(request.form, session.get('planId'))

    CoalCHPFurnaceCalculation.insert_furnace_calculation(furnaceData)
    ToCoalCHP.update_plan_date(session.get('planId'))
    newData = CoalCHPFurnaceCalculation.search_furnace_calculation(
        session.get('planId'))
    datas = ToCoalCHP.to_furnaceJson(newData)

    return jsonify({'newDatas': datas})


# 跳转锅炉本体页面
@coalviews.route('/coalFurnace')
@login_required
def coalFurnace():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_furnaceCalculation")
    return render_template(
        'page/coalCHP/coalFurnace.html', constants=coalCHPConstant)


# 脱硫脱硝Desulfurization and denitrification
@coalviews.route('/coalDesulfurization')
@login_required
def coalDesulfurization():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_desulfurization")
    # 查询含硫量和锅炉的过热蒸汽总量
    s_sulfur_design = format_value(
        "number",
        CoalCHPDesulfurization.search_desulfurization(
            session.get('planId')).s_sulfur_design)
    f_steam_flow_design = format_value(
        "number",
        CoalCHPFurnaceCalculation.search_furnace_calculation(
            session.get('planId')).f_steam_flow_design)
    return render_template(
        'page/coalCHP/coalDesulfurization.html',
        constants=coalCHPConstant,
        s_sulfur_design=s_sulfur_design,
        f_steam_flow_design=f_steam_flow_design)


# 初始化脱硫脱硝数据
@coalviews.route('/initDesulfurization', methods=['POST'])
@login_required
def initDesulfurization():
    desulfurization = CoalCHPDesulfurization.search_desulfurization(
        session.get('planId'))
    desulfurizationData = ToCoalCHP.to_desulfurizationJson(desulfurization)
    return jsonify({'desulfurization': desulfurizationData})


# 提交脱硫脱硝页面值
@coalviews.route('/formDesulfurization', methods=['POST'])
@login_required
def formDesulfurization():
    desulfurization = ToCoalCHP.to_desulfurization(request.form,
                                                   session.get('planId'))
    ToCoalCHP.update_plan_date(session.get('planId'))
    CoalCHPDesulfurization.insert_desulfurization(desulfurization)
    newData = CoalCHPDesulfurization.search_desulfurization(
        session.get('planId'))
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
        session.get('planId'))
    handingSystemData = ToCoalCHP.to_handingSystemJson(handingSystem)
    return jsonify({'handingSystem': handingSystemData})


# 提交输煤系统页面值
@coalviews.route('/formDataHandingSystem', methods=['POST'])
@login_required
def formDataHandingSystem():
    handingSystem = ToCoalCHP.to_handingSystem(request.form,
                                               session.get('planId'))
    ToCoalCHP.update_plan_date(session.get('planId'))
    CoalCHPCoalHandingSystem.insert_handing_system(handingSystem)

    newData = CoalCHPCoalHandingSystem.search_handing_system(
        session.get('planId'))
    datas = ToCoalCHP.to_handingSystemJson(newData)
    return jsonify({'newDatas': datas})


# 锅炉辅机
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
        session.get('planId'))
    boilerAuxiliariesData = ToCoalCHP.to_boilerAuxiliariesJson(
        boilerAuxiliaries)
    return jsonify({'boilerAuxiliaries': boilerAuxiliariesData})


# 提交锅炉辅机系统页面值
@coalviews.route('/formDataBoilerAuxiliaries', methods=['POST'])
@login_required
def formDataBoilerAuxiliaries():
    boilerAuxiliaries = ToCoalCHP.to_boilerAuxiliaries(request.form,
                                                       session.get('planId'))
    ToCoalCHP.update_plan_date(session.get('planId'))
    CoalCHPBoilerAuxiliaries.insert_boiler_auxiliaries(boilerAuxiliaries)
    newData = CoalCHPBoilerAuxiliaries.search_boiler_auxiliaries(
        session.get('planId'))
    datas = ToCoalCHP.to_boilerAuxiliariesJson(newData)
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
        session.get('planId'))
    removalAshSlagData = ToCoalCHP.to_removalAshSlagJson(removalAshSlag)
    return jsonify({'removalAshSlag': removalAshSlagData})


# 提交除灰除渣页面值
@coalviews.route('/formRemovalAshSlag', methods=['POST'])
@login_required
def formRemovalAshSlag():
    removalAshSlag = ToCoalCHP.to_removalAshSlag(request.form,
                                                 session.get('planId'))
    ToCoalCHP.update_plan_date(session.get('planId'))
    CoalCHPRemovalAshSlag.insert_removal_ash_slag(removalAshSlag)
    newData = CoalCHPRemovalAshSlag.search_removal_ash_slag(
        session.get('planId'))
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
        session.get('planId'))
    circulatingWaterData = ToCoalCHP.to_circulatingWaterJson(circulatingWater)
    return jsonify({'circulatingWater': circulatingWaterData})


# 提交循环水系统页面值
@coalviews.route('/formCirculatingWater', methods=['POST'])
@login_required
def formCirculatingWater():
    circulatingWater = ToCoalCHP.to_circulatingWater(request.form,
                                                     session.get('planId'))
    ToCoalCHP.update_plan_date(session.get('planId'))
    CoalCHPCirculatingWater.insert_circulating_water(circulatingWater)
    newData = CoalCHPCirculatingWater.search_circulating_water(
        session.get('planId'))
    datas = ToCoalCHP.to_circulatingWaterJson(newData)
    return jsonify({'newDatas': datas})


# 烟风系统
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
        session.get('planId'))
    circulatingWaterData = ToCoalCHP.to_smokeAirSystemJson(smokeAirSystem)
    return jsonify({'smokeAirSystem': circulatingWaterData})


# 提交烟风系统页面值
@coalviews.route('/formSmokeAirSystem', methods=['POST'])
@login_required
def formSmokeAirSystem():
    smokeAirSystem = ToCoalCHP.to_smokeAirSystem(request.form,
                                                 session.get('planId'))
    ToCoalCHP.update_plan_date(session.get('planId'))
    CoalCHPSmokeAirSystem.insert_smoke_air_system(smokeAirSystem)
    newData = CoalCHPSmokeAirSystem.search_smoke_air_system(
        session.get('planId'))
    datas = ToCoalCHP.to_smokeAirSystemJson(newData)
    return jsonify({'newDatas': datas})


# **************汽轮机计算start*******************
@coalviews.route('/coalSteamTurbine')
@login_required
def coalSteamTurbine():
    planId = session.get('planId')
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "turbine_backpressure")
    steamturbine = CoalCHPTurbineBackpressure.search_turbineBackpressure(
        planId)

    # 抽汽部分压力加入回热系统中时，按照压力排序
    sortPressureAfter = ToCoalCHP.sortPressure(steamturbine)

    return render_template(
        'page/coalCHP/coalSteamTurbine.html',
        constants=coalCHPConstant,
        steamturbineData=steamturbine,
        sortPressure=sortPressureAfter)


# 初期化汽轮机计算
@coalviews.route('/coalinitSteamTurbine', methods=['POST'])
@login_required
def coalinitSteamTurbine():
    planId = request.values.get('planId')
    turbineBackpressure = CoalCHPTurbineBackpressure.search_turbineBackpressure(
        planId)
    turbineBackpressureData = ToCoalCHP.to_steamJson(turbineBackpressure)
    return jsonify({'steamturbine': turbineBackpressureData})


# 保存汽轮机计算页面信息
@coalviews.route('/coalFormDataSteamTurbine', methods=['POST'])
@login_required
def coalFormDataSteamTurbine():
    # steamData = ToCoalCHP.to_steam(request.form, session.get('planId'))

    steamOldData = CoalCHPTurbineBackpressure.query.filter_by(
            plan_id=session.get('planId')).first()
    if getattr(steamOldData, 's_parameter_flg') == '1':
        # 已经存在旧记录的场合，先清理旧记录
        steamNewData = ToCoalCHP.steamClear(session.get('planId'))
        CoalCHPTurbineBackpressure.insert_turbineBackpressure(steamNewData)

    pointPower0, steamData = ToCoalCHP.to_steam(request.form,
                                                session.get('planId'))

    setattr(steamData, 's_parameter_flg', '1')
    setattr(steamData, 'i_total_power0', pointPower0)
    CoalCHPTurbineBackpressure.insert_turbineBackpressure(steamData)

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# 根据压力查询温度
@coalviews.route('/coalByPressure', methods=['POST'])
@login_required
def coalByPressure():
    datas = {}
    pressure_data = request.form.get('e_exhaust_point_pressure')
    temperature_data = seuif97.tsat_p((float(pressure_data) * 10))
    datas['temperature'] = temperature_data

    return jsonify({'temperature': datas})


# 根据压力和熵查询温度
@coalviews.route('/byPressureEntropy', methods=['POST'])
@login_required
def byPressureEntropy():
    datas = {}
    pressure_data = request.form.get('e_exhaust_point_pressure')
    entropy_data = request.form.get('e_exhaust_point_entropy')
    temperature_data = seuif97.ps2t((float(pressure_data)),
                                    float(entropy_data))

    datas['temperature'] = temperature_data

    return jsonify({'temperature': datas})


# 根据温度查询压力
@coalviews.route('/byTemperatureBack', methods=['POST'])
@login_required
def byTemperatureBack():
    datas = {}
    temperature_data = request.form.get('e_backpressure_temperature')
    pressure_data = seuif97.psat_t((float(temperature_data))) * 0.1
    datas['pressure'] = pressure_data

    return jsonify({'pressure': datas})


# 根据压力查询温度
@coalviews.route('/byPressureBack', methods=['POST'])
@login_required
def byPressureBack():
    datas = {}
    pressure_data = request.form.get('e_backpressure_pressure')
    temperature_data = seuif97.tsat_p((float(pressure_data) * 10))
    datas['temperature'] = temperature_data

    return jsonify({'temperature': datas})


# 根据压力和熵查询焓
@coalviews.route('/byPressureEntropyBack', methods=['POST'])
@login_required
def byPressureEntropyBack():
    datas = {}
    pressure_data = request.form.get('e_backpressure_pressure')
    entropy_data = request.form.get('e_exhaust_after_entropy')
    enthalpy_data = seuif97.ps2h((float(pressure_data)), float(entropy_data))

    datas['enthalpy'] = enthalpy_data

    return jsonify({'enthalpy': datas})


# 根据温度和熵查询焓
@coalviews.route('/byTemperatureEntropyBack', methods=['POST'])
@login_required
def byTemperatureEntropyBack():
    datas = {}
    temperature_data = request.form.get('e_backpressure_temperature')
    entropy_data = request.form.get('e_exhaust_after_entropy')
    enthalpy_data = seuif97.ts2h((float(temperature_data)),
                                 float(entropy_data))

    datas['enthalpy'] = enthalpy_data

    return jsonify({'enthalpy': datas})


# **************汽轮机计算 end*******************


# **************主要技术经济指标处理 start*******************
@coalviews.route('/coalEconomicIndicators')
@login_required
def coalEconomicIndicators():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "economic_indicators")
    return render_template(
        'page/coalCHP/coalEconomicIndicators.html',
        menuSelect='coalEconomicIndicators',
        constants=coalCHPConstant)


@coalviews.route('/coalChooseTemplate/<int:planId>')
@login_required
def coalChooseTemplate(planId):
    session['planId'] = planId
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "economic_indicators")
    return render_template(
        'page/coalCHP/coalEconomicIndicators.html',
        menuSelect='coalEconomicIndicators',
        constants=coalCHPConstant)


# 主要技术经济指标初期化处理
@coalviews.route('/coalInitEconomic', methods=['POST'])
@login_required
def coalInitEconomic():
    planId = request.values.get('planId')
    economic = CoalCHPEconomicIndicators.search_economic_indicators(planId)
    economicData = ToCoalCHP.to_economicJson(economic)
    return jsonify({'economic': economicData})


# 保存主要技术经济指标页面信息
@coalviews.route('/coalFormDataEconomic', methods=['POST'])
@login_required
def coalFormDataEconomic():
    economicData = ToCoalCHP.to_economic(request.form, session.get('planId'))
    CoalCHPEconomicIndicators.insert_economic_indicators(economicData)

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# **************主要技术经济指标处理 end*******************
# **************化学水系统 start*******************
@coalviews.route('/coalChemicalWater')
@login_required
def coalChemicalWater():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_chemicalWater")
    return render_template(
        'page/coalCHP/coalChemicalWater.html', constants=coalCHPConstant)


# 化学水系统初期化处理
@coalviews.route('/initChemicalWater', methods=['POST'])
@login_required
def initChemicalWater():
    chemicalWater = CoalCHPChemicalWater.search_chemical_water(
        session.get('planId'))
    chemicalWaterData = ToCoalCHP.to_chemicalWaterJson(chemicalWater)
    return jsonify({'chemicalWater': chemicalWaterData})


# 保存化学水系统页面信息
@coalviews.route('/chemicalWaterData', methods=['POST'])
@login_required
def chemicalWaterData():
    chemicalWaterData = ToCoalCHP.to_chemicalWater(request.form,
                                                   session.get('planId'))
    CoalCHPChemicalWater.insert_chemical_water(chemicalWaterData)
    newData = CoalCHPChemicalWater.search_chemical_water(session.get('planId'))
    datas = ToCoalCHP.to_chemicalWaterJson(newData)
    return jsonify({'newDatas': datas})


# ***************************化学水系统 end************************


# ************** 烟囱计算 start*******************
@coalviews.route('/coalChimney')
@login_required
def coalChimney():
    planId = session.get('planId')
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant("coalCHP_chimney")
    chimney = CoalCHPChimney.search_coalCHPChimney(planId)
    return render_template(
        'page/coalCHP/coalChimney.html',
        constants=coalCHPConstant,
        steamturbineData=chimney)


@coalviews.route('/getcoalChimneyData', methods=['POST'])
@login_required
def getcoalChimneyData():
    planId = session.get('planId')
    ChimneyData = CoalCHPChimney.search_coalCHPChimney(planId)
    ChimneyJson = ToCoalCHP.to_ChimneyJson(ChimneyData)
    return jsonify({'ChimneyJson': ChimneyJson})


@coalviews.route('/coalSaveChimneyData', methods=['POST'])
@login_required
def coalSaveChimneyData():
    plan_id = session.get('planId')
    ChimneyData = ToCoalCHP.to_ChimneyData(request.form, plan_id)
    CoalCHPChimney.insert_coalCHPChimney(ChimneyData)
    session['planId'] = plan_id
    newData = CoalCHPChimney.search_coalCHPChimney(plan_id)
    datas = ToCoalCHP.to_ChimneyJson(newData)
    return jsonify({'newDatas': datas})


# ************** 烟囱计算 end*******************


# ************** 汽机辅机 start*******************
@coalviews.route('/coalTurbineAuxiliary')
@login_required
def coalTurbineAuxiliary():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "turbine_auxiliary")
    return render_template(
        'page/coalCHP/coalTurbineAuxiliary.html',
        menuSelect='coalBoilerAuxiliaries',
        constants=coalCHPConstant)


# 初期化汽机辅机
@coalviews.route('/coalinitTurbineAuxiliary', methods=['POST'])
@login_required
def coalinitTurbineAuxiliary():
    planId = session.get('planId')
    turbineAuxiliary = CoalchpTurbineAuxiliary.search_turbine_auxiliary(planId)
    turbineAuxiliaryData = ToCoalCHP.to_turbineAuxiliaryJson(
        turbineAuxiliary, planId)
    return jsonify({'turbineAuxiliaryData': turbineAuxiliaryData})


# 保存汽机辅机页面信息
@coalviews.route('/coalFormTurbineAuxiliary', methods=['POST'])
@login_required
def coalFormTurbineAuxiliary():
    turbineAuxiliary = ToCoalCHP.to_turbineAuxiliary(request.form,
                                                     session.get('planId'))
    CoalchpTurbineAuxiliary.insert_turbine_auxiliary(turbineAuxiliary)
    newData = CoalchpTurbineAuxiliary.search_turbine_auxiliary(
        session.get('planId'))
    datas = ToCoalCHP.to_turbineAuxiliaryJson(newData, session.get('planId'))

    return jsonify({'newDatas': datas})


# ************** 汽机辅机 end*******************


# **************公用工程 start*******************
@coalviews.route('/coalOfficialProcess')
@login_required
def coalOfficialProcess():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "official_process")
    return render_template(
        'page/coalCHP/coalOfficialProcess.html',
        menuSelect='coalOfficialProcess',
        constants=coalCHPConstant)


# 初期化公用工程
@coalviews.route('/coalinitOfficial', methods=['POST'])
@login_required
def coalinitOfficial():
    planId = request.values.get('planId')
    official = CoalCHPOfficialProcess.search_official(planId)
    officialData = ToCoalCHP.to_officialJson(official)
    return jsonify({'official': officialData})


# 保存公用工程页面信息
@coalviews.route('/coalFormDataOfficial', methods=['POST'])
@login_required
def coalFormDataOfficial():
    officialData = ToCoalCHP.to_official(request.form, session.get('planId'))
    CoalCHPOfficialProcess.insert_official(officialData)

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# 计算供油泵
@coalviews.route('/coalOilPumpCal', methods=['POST'])
@login_required
def coalOilPumpCal():
    oilPumpData = {}
    planId = request.values.get('planId')
    # 获得锅炉计算的低位发热量估算，锅炉燃料消耗量
    datas = CoalCHPFurnaceCalculation.search_furnace_calculation(planId)
    oilPumpData = ToCoalCHP.to_oilPumpJson(datas)

    return jsonify({'oilPumpData': oilPumpData})


# **************公用工程 end*******************


# **************采暖供热系统start*****************
@coalviews.route('/coalHeatSupply')
@login_required
def coalHeatSupply():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant("heat_supply")
    return render_template(
        'page/coalCHP/coalHeatSupply.html',
        menuSelect='coalHeatSupply',
        constants=coalCHPConstant)


# 初期化采暖供热系统
@coalviews.route('/coalinitHeat', methods=['POST'])
@login_required
def coalinitHeat():
    planId = request.values.get('planId')
    heat = CoalCHPHeatSupply.search_heatSupply(planId)
    heatData = ToCoalCHP.to_heatJson(heat)
    return jsonify({'heat': heatData})


# 保存采暖供热系统页面信息
@coalviews.route('/coalFormDataHeat', methods=['POST'])
@login_required
def coalFormDataHeat():
    heatData = ToCoalCHP.to_heat(request.form, session.get('planId'))
    CoalCHPHeatSupply.insert_heatSupply(heatData)

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# **************采暖供热系统end*******************
@coalviews.route('/outputImage')
@login_required
def outputImage():
    # 生成图纸
    planId = session.get('planId')
    ToCoalCHP.generate_img(planId, "", 2)
    # 获取地址列表
    imglist = ToCoalCHP.getPathList(planId, "html")
    return render_template(
        'page/coalCHP/coalImage.html',
        imglist=imglist,
        imglength=len(imglist))


@coalviews.route("/getSurplusImg", methods=['POST'])
@login_required
def getSurplusImg():
    planId = session.get('planId')
    ToCoalCHP.generate_img(planId, "", 0)
    # 生成后续的图像
    imglist = ToCoalCHP.getPathList(planId, "js")
    return jsonify({'imglist': imglist})


# ************** 设备清单 ********************
@coalviews.route('/coalEquipmentList')
@login_required
def coalEquipmentList():
    return render_template(
        'page/coalCHP/coalDevice.html'
    )


@coalviews.route('/getEquipmentList', methods=['POST'])
@login_required
def getEquipmentList():
    planId = session.get('planId')
    # 更新值
    ToCoalCHP.replaceDeviceJson(planId)
    equipmentList = EquipmentList.search_equipmentList(planId)
    equipmentList_json = json.loads(equipmentList.equipment_content)
    equipment_json = json.dumps(equipmentList_json)
    return equipment_json


@coalviews.route('/saveEquipmentList', methods=['POST'])
@login_required
def saveEquipmentList():
    planId = session.get('planId')
    # deleteId = request.values.get('deleteId')
    uidData = request.values.get('uidData')
    nameData = request.values.get('nameData')
    typeData = request.values.get('typeData')
    contentData = request.values.get('contentData')
    unitData = request.values.get('unitData')
    countData = request.values.get('countData')
    remarkData = request.values.get('remarkData')
    # Equipment = EquipmentList.search_equipmentList(planId)

    Equipment = MainService.saveEquipmentList(planId, uidData, nameData, typeData, contentData, unitData, countData, remarkData, None)

    if Equipment is not None:
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'error'})


# ************** 设备清单模板 ********************
@coalviews.route('/toCoalCHPEquipment')
@login_required
def toCoalCHPEquipment():
    session['menuSelect'] = "coalCHPequipmentList"
    return render_template(
        'page/coalCHP/coalDeviceList.html'
    )


@coalviews.route('/getEquipmentTemplate', methods=['POST'])
@login_required
def getEquipmentTemplate():
    current_app.logger.warning(u'操作者：%d,模板设备清单模板初始化', current_user.id)
    equipmentList = EquipmentListTemplate.search_EquipmentListTemplate(Module.coalCHP)
    equipmentList_json = json.loads(equipmentList.equipment_template)
    equipment_json = json.dumps(equipmentList_json)
    return equipment_json


@coalviews.route('/saveEquipmentTemplate', methods=['POST'])
@login_required
def saveEquipmentTemplate():
    current_app.logger.warning(u'操作者：%d,模板设备清单保存!', current_user.id)
    planId = session.get('planId')
    nameData = request.values.get('nameData')
    uidData = request.values.get('uidData')
    typeData = request.values.get('typeData')
    contentData = request.values.get('contentData')
    unitData = request.values.get('unitData')
    countData = request.values.get('countData')
    remarkData = request.values.get('remarkData')
    Equipment = MainService.saveEquipmentList(planId, uidData, nameData, typeData, contentData, unitData, countData, remarkData, Module.coalCHP)
    if Equipment is not None:
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'error'})