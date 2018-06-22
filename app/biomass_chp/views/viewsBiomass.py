# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash,\
     abort, jsonify, request, session, send_from_directory
from flask_login import login_required, current_user
from . import biomassviews
from app.biomass_chp.models.modelsBiomass import BiomassCHPconstant, \
     BiomassCHPBeltWidth, \
     BiomassCHPNeedsQuestionnaire, \
     BiomassCHPBoilerCalculation,\
     BiomassCHPFuelStorageTransportation,\
     BiomassCHPDesulfurizationAndDenitrification, \
     BiomassCHPBoilerAuxiliaries, BiomassCHPDASRemove,\
     BiomassCHPOfficialProcess, BiomassCHPTurbineBackpressure, \
     BiomassCHPWaterTreatment, BiomassCHPHeatSupply, BiomassCHPChimney,\
     BiomassCHPCirculatingWater, BiomasschpTurbineAuxiliary,\
     BiomasschpEconomicIndicators, BiomassCHPFuelComponent
# from app.biomass_chp.service.biomassService import ToBiomassCHP
from app.biomass_chp.service.execution_strategy import NeedsAfter
from app.models import Plan, Company, EquipmentList, EquipmentListTemplate, Module
from app.biomass_chp.service.biomassService import ToBiomassCHP, \
     BiomassImgService, BiomassEquipmentService
from util.iapws_if97 import seuif97
import os
from config import config
import json
from app.main.service.mainService import MainService
from flask import current_app


# ##############生物质热电联产 start###############
# **************需求调查表 start**************
# @biomassviews.route('/biomassQuestionnaire')
# @login_required
# def biomassQuestionnaire():
#     biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
#         "biomassCHP_questionnaire")
#     # 查询已有方案
#     plans = Plan.search_plan(current_user.id)
#     companys = Company.search_company()
#     return render_template(
#         'page/BiomassCHP/biomassQuestionnaire.html',
#         menuSelect='biomassQuestionnaire',
#         constants=biomassCHPConstant,
#         plans=plans,
#         companys=companys)


# 新增或修改方案进入
@biomassviews.route('/biomassQuestionnaire/<int:id>')
@login_required
def biomassQuestionnaire(id):
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "biomassCHP_questionnaire")
    biomassCHPComponent = BiomassCHPFuelComponent.search_biomassCHPComponent()

    # 查询已有方案
    plans = Plan.search_plan(current_user.id)
    companys = Company.search_company()
    if id > 0:
        session['planId'] = id
    elif not session['planId']:
        session['planId'] = None
    return render_template(
        'page/BiomassCHP/biomassQuestionnaire.html',
        constants=biomassCHPConstant,
        fuelsort=biomassCHPComponent,
        plans=plans,
        companys=companys)



# 初始化需求调查表数据
@biomassviews.route('/initBiomassQuestionnaire', methods=['POST'])
@login_required
def initBiomassQuestionnaire():
    questionnaireData = "null"
    if session.get('planId'):
        questionnaire = BiomassCHPNeedsQuestionnaire.search_questionnaire(
            session.get('planId'))
        questionnaireData = ToBiomassCHP.to_questionnaireJson(questionnaire)
    return jsonify({'questionnaire': questionnaireData})

# 选择燃料
@biomassviews.route('/fuelSort', methods=['POST'])
@login_required
def fuelSort():
    id = request.values.get('id')
    datas = ToBiomassCHP.to_fuelCHPComponentJson(id)

    return jsonify({'fuelSort': datas})


# 保存需求调查表数据
@biomassviews.route('/biomassFormData', methods=['POST'])
@login_required
def biomassFormData():
    plan_name = request.form.get('plan_name')
    companyName = request.form.get('company_name')
    companyLocation = request.form.get('company_location')
    plan_id = ToBiomassCHP.create_plan(companyName, plan_name, companyLocation, None)
    questionnaire = ToBiomassCHP.to_questionnaire(request.form, plan_id)
    BiomassCHPNeedsQuestionnaire.insert_questionnaire(questionnaire)

    # 锅炉熵焓值计算
    NeedsAfter().specialCalculation(plan_id)

    ToBiomassCHP.update_plan_date(plan_id)
    session['planId'] = plan_id
    session['quantityDesign'] = request.form.get('s_quantity_design')
    session['quantityCheck'] = request.form.get('s_quantity_check')
    return jsonify({'planId': plan_id})


# **************需求调查表 end**************


# **************锅炉计算 start**************
@biomassviews.route('/biomassFurnace')
@login_required
def biomassFurnace():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "boiler_calculation")
    return render_template(
        'page/BiomassCHP/biomassFurnace.html',
        menuSelect='biomassFurnace',
        constants=biomassCHPConstant)
    

# 初期化锅炉页面
@biomassviews.route('/biomassInitFurnace', methods=['POST'])
@login_required
def biomassInitFurnace():
    planId = request.values.get('planId')
    furnace = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
    furnaceData = ToBiomassCHP.to_furnaceJson(furnace)
    return jsonify({'furnace': furnaceData})


# 保存锅炉页面信息
@biomassviews.route('/biomassFormDataFurnace', methods=['POST'])
@login_required
def biomassFormDataFurnace():
    furnaceData = ToBiomassCHP.to_furnace(request.form,
                                          session.get('planId'))
    BiomassCHPBoilerCalculation.insert_furnace_calculation(furnaceData)

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


#查找已知方案
@biomassviews.route('/biomassFindPlan', methods=['POST'])
@login_required
def biomassFindPlan():
    planId = request.values.get('planId')
    if (planId == '0'):
        questionnaireData = {}
        return jsonify({'questionnaire': questionnaireData})
    else:
        questionnaire = BiomassCHPNeedsQuestionnaire.search_questionnaire(
            planId)
        questionnaireData = ToBiomassCHP.to_questionnaireJson(questionnaire)
        session['planId'] = planId
        session['quantityDesign'] = questionnaireData['s_quantity_design']
        session['quantityCheck'] = questionnaireData['s_quantity_check']
        return jsonify({'questionnaire': questionnaireData})


# **************锅炉计算 end**************


# **************燃料存储及输送 start**************
@biomassviews.route('/biomassFuelStorTran')
@login_required
def biomassFuelStorTran():
    biomassCHPBeltWidth = BiomassCHPBeltWidth.search_biomassCHPBeltWidth()
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "fuel_ST")
    return render_template(
        'page/BiomassCHP/biomassFuelStorTran.html',
        menuSelect='biomassFuelStorTran',
        beltsort=biomassCHPBeltWidth,
        constants=biomassCHPConstant)


# 初期化燃料存储及输送
@biomassviews.route('/biomassInitSortTran', methods=['POST'])
@login_required
def biomassInitSortTran():
    planId = request.values.get('planId')
    sorttran = BiomassCHPFuelStorageTransportation.search_storage_transportation(
        planId)
    sorttranData = ToBiomassCHP.to_sorttranJson(sorttran)
    return jsonify({'sorttran': sorttranData})


# 获得锅炉类型
@biomassviews.route('/biomassGetAnnualHours', methods=['POST'])
@login_required
def biomassGetAnnualHours():
    planId = request.values.get('planId')
    boilerData = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
    boilerType = getattr(boilerData, 'boiler_type')
    return jsonify({'boilerType': boilerType})


# 获得过热蒸汽额定流量
@biomassviews.route('/biomassGetDuplexNumber', methods=['POST'])
@login_required
def biomassGetDuplexNumber():
    planId = request.values.get('planId')
    boilerData = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
    steamFlow = str(getattr(boilerData, 'f_steam_flow_design'))
    return jsonify({'steamFlow': steamFlow})


# 保存燃料存储页面信息
@biomassviews.route('/biomassFormDataStorTran', methods=['POST'])
@login_required
def biomassFormDataStorTran():
    storTranData = ToBiomassCHP.to_stortran(request.form,
                                            session.get('planId'))
    BiomassCHPFuelStorageTransportation.insert_storage_transportation(
        storTranData)

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# 匹配断面系数
@biomassviews.route('/beltSort', methods=['POST'])
@login_required
def beltSort():
    id = request.values.get('id')
    datas = {}
    biomassCHPBeltWidth = BiomassCHPBeltWidth.search_biomassCHPSort(id)
    datas['width'] = biomassCHPBeltWidth.width
    datas['coefficient'] = biomassCHPBeltWidth.coefficient

    return jsonify({'beltSort': datas})


# **************燃料存储及输送 end**************


# **************脱硫脱硝系统 start**************
@biomassviews.route('/biomassDesulDenit')
@login_required
def biomassDesulDenit():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "desulfurization_denitrification")
    return render_template(
        'page/BiomassCHP/biomassDesulDenit.html',
        menuSelect='biomassDesulDenit',
        constants=biomassCHPConstant)


# 初期化脱硫脱硝
@biomassviews.route('/biomassInitDesulDenit', methods=['POST'])
@login_required
def biomassInitDesulDenit():
    planId = request.values.get('planId')
    desuldenit = BiomassCHPDesulfurizationAndDenitrification.search_des_den(
        planId)
    desuldenitData = ToBiomassCHP.to_desuldenitJson(desuldenit)
    return jsonify({'desuldenit': desuldenitData})


#保存脱硫脱硝页面信息
@biomassviews.route('/biomassFormDataDesulDenit', methods=['POST'])
@login_required
def biomassFormDataDesulDenit():
    desuldenitData = ToBiomassCHP.to_desuldenit(
        request.form, session.get('planId'))
    BiomassCHPDesulfurizationAndDenitrification.insert_des_den(desuldenitData)

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# **************脱硫脱硝系统 end**************


# **************除尘除灰除渣系统 start**************
@biomassviews.route('/biomassDASRemove')
@login_required
def biomassDASRemove():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "das_remove")
    return render_template(
        'page/BiomassCHP/biomassDASRemove.html',
        menuSelect='biomassDASRemove',
        constants=biomassCHPConstant)


# 初期化除尘除灰
@biomassviews.route('/biomassinitDASRemove', methods=['POST'])
@login_required
def biomassinitDASRemove():
    planId = request.values.get('planId')
    dasremove = BiomassCHPDASRemove.search_dasRemove(planId)
    dasremoveData = ToBiomassCHP.to_dasRemoveJson(dasremove)
    return jsonify({'dasremove': dasremoveData})


#保存除尘除灰页面信息
@biomassviews.route('/biomassFormDataDASRemove', methods=['POST'])
@login_required
def biomassFormDataDASRemove():
    dasremoveData = ToBiomassCHP.to_dasRemove(request.form,
                                              session.get('planId'))
    BiomassCHPDASRemove.insert_dasRemove(dasremoveData)

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# **************除尘除灰除渣系统 end**************


# **************锅炉辅机 start*******************
@biomassviews.route('/biomassBoilerAuxiliaries')
@login_required
def biomassBoilerAuxiliaries():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "boiler_auxiliaries")
    return render_template(
        'page/BiomassCHP/biomassBoilerAuxiliaries.html',
        menuSelect='biomassBoilerAuxiliaries',
        constants=biomassCHPConstant)


# 初期化锅炉辅机
@biomassviews.route('/biomassinitAuxiliaries', methods=['POST'])
@login_required
def biomassinitAuxiliaries():
    planId = request.values.get('planId')
    auxiliaries = BiomassCHPBoilerAuxiliaries.search_auxiliaries(planId)
    auxiliariesData = ToBiomassCHP.to_auxiliariesJson(auxiliaries)
    return jsonify({'auxiliaries': auxiliariesData})


#保存锅炉辅机页面信息
@biomassviews.route('/biomassFormDataAuxiliaries', methods=['POST'])
@login_required
def biomassFormDataAuxiliaries():
    auxiliariesData = ToBiomassCHP.to_auxiliaries(
        request.form, session.get('planId'))
    BiomassCHPBoilerAuxiliaries.insert_auxiliaries(auxiliariesData)

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# **************锅炉辅机 end*******************


# **************化学水处理 start*******************
@biomassviews.route('/biomassWaterTreatment')
@login_required
def biomassWaterTreatment():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "water_treatment")
    return render_template(
        'page/BiomassCHP/biomassWaterTreatment.html',
        menuSelect='biomassWaterTreatment',
        constants=biomassCHPConstant)

# 初期化化学水处理
@biomassviews.route('/biomassinitWater', methods=['POST'])
@login_required
def biomassinitWater():
    planId = request.values.get('planId')
    water = BiomassCHPWaterTreatment.search_water(planId)
    waterData = ToBiomassCHP.to_waterJson(water)
    return jsonify({'water': waterData})

#保存化学水处理页面信息
@biomassviews.route('/biomassFormDataWater', methods=['POST'])
@login_required
def biomassFormDataWater():
    waterData = ToBiomassCHP.to_water(request.form,
                                            session.get('planId'))
    BiomassCHPWaterTreatment.insert_water(waterData)

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})

# **************化学水处理 end*******************



# **************公用工程 start*******************
@biomassviews.route('/biomassOfficialProcess')
@login_required
def biomassOfficialProcess():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "official_process")
    return render_template(
        'page/BiomassCHP/biomassOfficialProcess.html',
        menuSelect='biomassOfficialProcess',
        constants=biomassCHPConstant)


# 初期化公用工程
@biomassviews.route('/biomassinitOfficial', methods=['POST'])
@login_required
def biomassinitOfficial():
    planId = request.values.get('planId')
    official = BiomassCHPOfficialProcess.search_official(planId)
    officialData = ToBiomassCHP.to_officialJson(official)
    return jsonify({'official': officialData})


#保存公用工程页面信息
@biomassviews.route('/biomassFormDataOfficial', methods=['POST'])
@login_required
def biomassFormDataOfficial():
    officialData = ToBiomassCHP.to_official(request.form,
                                            session.get('planId'))
    BiomassCHPOfficialProcess.insert_official(officialData)

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# 计算供油泵
@biomassviews.route('/biomassOilPumpCal', methods=['POST'])
@login_required
def biomassOilPumpCal():
    oilPumpData = {}
    planId = request.values.get('planId')
    # 获得锅炉计算的低位发热量估算，锅炉燃料消耗量
    datas = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
    oilPumpData = ToBiomassCHP.to_oilPumpJson(datas)

    return jsonify({'oilPumpData': oilPumpData})
# **************公用工程 end*******************


# **************采暖供热系统start*****************
@biomassviews.route('/biomassHeatSupply')
@login_required
def biomassHeatSupply():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "heat_supply")
    return render_template(
        'page/BiomassCHP/biomassHeatSupply.html',
        menuSelect='biomassHeatSupply',
        constants=biomassCHPConstant)

# 初期化采暖供热系统
@biomassviews.route('/biomassinitHeat', methods=['POST'])
@login_required
def biomassinitHeat():
    planId = request.values.get('planId')
    heat = BiomassCHPHeatSupply.search_heatSupply(planId)
    heatData = ToBiomassCHP.to_heatJson(heat)
    return jsonify({'heat': heatData})

#保存采暖供热系统页面信息
@biomassviews.route('/biomassFormDataHeat', methods=['POST'])
@login_required
def biomassFormDataHeat():
    heatData = ToBiomassCHP.to_heat(request.form,
                                    session.get('planId'))
    BiomassCHPHeatSupply.insert_heatSupply(heatData)

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})

# **************采暖供热系统end*******************

# **************循环水 start*******************
@biomassviews.route('/biomassCirculatingWater')
@login_required
def biomassCirculatingWater():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "biomassCHP_circulatingWater")
    return render_template(
        'page/BiomassCHP/biomassCirculatingWater.html',
        menuSelect='biomassBoilerAuxiliaries',
        constants=biomassCHPConstant)


# 初期化循环水
@biomassviews.route('/biomassinitCirculatingWater', methods=['POST'])
@login_required
def biomassinitCirculatingWater():
    planId = session.get('planId')
    circulatingWater = BiomassCHPCirculatingWater.search_circulating_water(
        planId)
    circulatingWaterData = ToBiomassCHP.to_circulatingWaterJson(
        circulatingWater, planId)
    return jsonify({'circulatingWaterData': circulatingWaterData})


# 保存循环水页面信息
@biomassviews.route('/biomassFormCirculatingWater', methods=['POST'])
@login_required
def biomassFormCirculatingWater():
    circulatingWater = ToBiomassCHP.to_circulatingWater(
        request.form, session.get('planId'))
    BiomassCHPCirculatingWater.insert_circulating_water(circulatingWater)
    newData = BiomassCHPCirculatingWater.search_circulating_water(
        session.get('planId'))
    datas = ToBiomassCHP.to_circulatingWaterJson(newData,
                                                 session.get('planId'))

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    return jsonify({'newDatas': datas})


# **************循环水 end*******************


# **************汽轮机计算start*******************
@biomassviews.route('/biomassSteamTurbine')
@login_required
def biomassSteamTurbine():
    planId = session.get('planId')
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "turbine_backpressure")
    steamturbine = BiomassCHPTurbineBackpressure.search_turbineBackpressure(planId)

    # 抽汽部分压力加入回热系统中时，按照压力排序
    sortPressureAfter = ToBiomassCHP.sortPressure(steamturbine)

    return render_template(
        'page/BiomassCHP/biomassSteamTurbine.html',
        menuSelect='biomassSteamTurbine',
        constants=biomassCHPConstant,
        steamturbineData=steamturbine,
        sortPressure=sortPressureAfter)

# 初期化汽轮机计算
@biomassviews.route('/biomassinitSteamTurbine', methods=['POST'])
@login_required
def biomassinitSteamTurbine():
    planId = request.values.get('planId')
    turbineBackpressure = BiomassCHPTurbineBackpressure.search_turbineBackpressure(planId)
    turbineBackpressureData = ToBiomassCHP.to_steamJson(turbineBackpressure)
    return jsonify({'steamturbine': turbineBackpressureData})


# 保存汽轮机计算页面信息
@biomassviews.route('/biomassFormDataSteamTurbine', methods=['POST'])
@login_required
def biomassFormDataSteamTurbine():
    steamOldData = BiomassCHPTurbineBackpressure.query.filter_by(
            plan_id=session.get('planId')).first()
    if getattr(steamOldData, 's_parameter_flg') == '1':
        # 已经存在旧记录的场合，先清理旧记录
        steamNewData = ToBiomassCHP.steamClear(session.get('planId'))
        BiomassCHPTurbineBackpressure.insert_turbineBackpressure(steamNewData)

    pointPower0, steamData = ToBiomassCHP.to_steam(request.form, session.get('planId'))
    setattr(steamData, 's_parameter_flg', '1')
    setattr(steamData, 'i_total_power0', pointPower0)
    BiomassCHPTurbineBackpressure.insert_turbineBackpressure(steamData)

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})

# 根据压力查询温度
@biomassviews.route('/biomassByPressure', methods=['POST'])
@login_required
def biomassByPressure():
    datas = {}
    pressure_data = request.form.get('e_exhaust_point_pressure')
    temperature_data = seuif97.tsat_p((float(pressure_data)*10))
    datas['temperature'] = temperature_data

    return jsonify({'temperature': datas})

# 根据压力和熵查询温度
@biomassviews.route('/byPressureEntropy', methods=['POST'])
@login_required
def byPressureEntropy():
    datas = {}
    pressure_data = request.form.get('e_exhaust_point_pressure')
    entropy_data = request.form.get('e_exhaust_point_entropy')
    temperature_data = seuif97.ps2t((float(pressure_data)),float(entropy_data))

    datas['temperature'] = temperature_data

    return jsonify({'temperature': datas})

# 根据温度查询压力
@biomassviews.route('/byTemperatureBack', methods=['POST'])
@login_required
def byTemperatureBack():
    datas = {}
    temperature_data = request.form.get('e_backpressure_temperature')
    pressure_data = seuif97.psat_t((float(temperature_data)))*0.1
    datas['pressure'] = pressure_data

    return jsonify({'pressure': datas})

# 根据压力查询温度
@biomassviews.route('/byPressureBack', methods=['POST'])
@login_required
def byPressureBack():
    datas = {}
    pressure_data = request.form.get('e_backpressure_pressure')
    temperature_data = seuif97.tsat_p((float(pressure_data)*10))
    datas['temperature'] = temperature_data

    return jsonify({'temperature': datas})

# 根据压力和熵查询焓
@biomassviews.route('/byPressureEntropyBack', methods=['POST'])
@login_required
def byPressureEntropyBack():
    datas = {}
    pressure_data = request.form.get('e_backpressure_pressure')
    entropy_data = request.form.get('e_exhaust_after_entropy')
    enthalpy_data = seuif97.ps2h((float(pressure_data)),float(entropy_data))

    datas['enthalpy'] = enthalpy_data

    return jsonify({'enthalpy': datas})

# 根据温度和熵查询焓
@biomassviews.route('/byTemperatureEntropyBack', methods=['POST'])
@login_required
def byTemperatureEntropyBack():
    datas = {}
    temperature_data = request.form.get('e_backpressure_temperature')
    entropy_data = request.form.get('e_exhaust_after_entropy')
    enthalpy_data = seuif97.ts2h((float(temperature_data)),float(entropy_data))

    datas['enthalpy'] = enthalpy_data

    return jsonify({'enthalpy': datas})

# **************汽轮机计算 end*******************

# ************** 烟囱计算 start*******************
@biomassviews.route('/biomassChimney')
@login_required
def biomassChimney():
    planId = session.get('planId')
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "biomassCHP_chimney")
    chimney = BiomassCHPChimney.search_biomassCHPChimney(planId)
    return render_template(
        'page/BiomassCHP/biomassChimney.html',
        menuSelect='biomassChimney',
        constants=biomassCHPConstant,
        steamturbineData=chimney)

@biomassviews.route('/getBiomassChimneyData', methods=['POST'])
@login_required
def getBiomassChimneyData():
    planId = session.get('planId')
    ChimneyData = BiomassCHPChimney.search_biomassCHPChimney(planId)
    ChimneyJson = ToBiomassCHP.to_ChimneyJson(ChimneyData)
    return jsonify({'ChimneyJson': ChimneyJson})

@biomassviews.route('/BiomassSaveChimneyData', methods=['POST'])
@login_required
def BiomassSaveChimneyData():
    plan_id = session.get('planId')
    ChimneyData = ToBiomassCHP.to_ChimneyData(request.form, plan_id)
    ToBiomassCHP.update_plan_date(plan_id)
    BiomassCHPChimney.insert_biomassCHPChimney(ChimneyData)

    session['planId'] = plan_id
    newData = BiomassCHPChimney.search_biomassCHPChimney(plan_id)
    datas = ToBiomassCHP.to_ChimneyJson(newData)

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(plan_id)

    return jsonify({'newDatas': datas})
# ************** 烟囱计算 end*******************

# ************** 汽机辅机 start*******************
@biomassviews.route('/biomassTurbineAuxiliary')
@login_required
def biomassTurbineAuxiliary():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "turbine_auxiliary")
    return render_template(
        'page/BiomassCHP/biomassTurbineAuxiliary.html',
        menuSelect='biomassBoilerAuxiliaries',
        constants=biomassCHPConstant)


# 初期化汽机辅机
@biomassviews.route('/biomassinitTurbineAuxiliary', methods=['POST'])
@login_required
def biomassinitTurbineAuxiliary():
    planId = session.get('planId')
    turbineAuxiliary = BiomasschpTurbineAuxiliary.search_turbine_auxiliary(
        planId)
    turbineAuxiliaryData = ToBiomassCHP.to_turbineAuxiliaryJson(
        turbineAuxiliary, planId)
    return jsonify({'turbineAuxiliaryData': turbineAuxiliaryData})


# 保存汽机辅机页面信息
@biomassviews.route('/biomassFormTurbineAuxiliary', methods=['POST'])
@login_required
def biomassFormTurbineAuxiliary():
    turbineAuxiliary = ToBiomassCHP.to_turbineAuxiliary(
        request.form, session.get('planId'))
    BiomasschpTurbineAuxiliary.insert_turbine_auxiliary(turbineAuxiliary)
    newData = BiomasschpTurbineAuxiliary.search_turbine_auxiliary(
        session.get('planId'))
    datas = ToBiomassCHP.to_turbineAuxiliaryJson(newData,
                                                 session.get('planId'))

    # 同步设备清单数据
    BiomassEquipmentService().updateEquipment(session.get('planId'))

    return jsonify({'newDatas': datas})
# ************** 汽机辅机 end*******************



# ########################生物质热电联产 end#################################


@biomassviews.route('/subPages3')
@login_required
def subPages3():
    return render_template('page/elements.3.html', menuSelect='elements3')


@biomassviews.route('/elements')
@login_required
def elements():
    return render_template('page/elements.html', menuSelect='elements')


@biomassviews.route('/charts')
@login_required
def charts():
    return render_template('page/charts.html', menuSelect='charts')


@biomassviews.route('/tables')
@login_required
def tables():
    return render_template('page/tables.html', menuSelect='tables')


@biomassviews.route('/typography')
@login_required
def typography():
    return render_template('page/typography.html', menuSelect='typography')


@biomassviews.route('/icons')
@login_required
def icons():
    return render_template('page/icons.html', menuSelect='icons')


# **************主要技术经济指标处理 start*******************
@biomassviews.route('/biomassEconomicIndicators')
@login_required
def biomassEconomicIndicators():
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "economic_indicators")
    return render_template(
        'page/BiomassCHP/biomassEconomicIndicators.html',
        menuSelect='biomassEconomicIndicators',
        constants=biomassCHPConstant)


@biomassviews.route('/biomassChooseTemplate/<int:planId>')
@login_required
def biomassChooseTemplate(planId):
    session['planId'] = planId
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "economic_indicators")
    return render_template(
        'page/BiomassCHP/biomassEconomicIndicators.html',
        menuSelect='biomassEconomicIndicators',
        constants=biomassCHPConstant)


# 主要技术经济指标初期化处理
@biomassviews.route('/biomassInitEconomic', methods=['POST'])
@login_required
def biomassInitEconomic():
    planId = request.values.get('planId')
    economic = BiomasschpEconomicIndicators.search_economic_indicators(planId)
    economicData = ToBiomassCHP.to_economicJson(economic)
    return jsonify({'economic': economicData})

# 获得锅炉类型
@biomassviews.route('/biomassGetBoilerType', methods=['POST'])
@login_required
def biomassGetBoilerType():
    planId = request.values.get('planId')
    boilerData = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
    boilerType = getattr(boilerData, 'boiler_type')
    return jsonify({'boilerType': boilerType})

#保存主要技术经济指标页面信息
@biomassviews.route('/biomassFormDataEconomic', methods=['POST'])
@login_required
def biomassFormDataEconomic():
    economicData = ToBiomassCHP.to_economic(request.form,
                                            session.get('planId'))
    BiomasschpEconomicIndicators.insert_economic_indicators(economicData)

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})

# **************主要技术经济指标处理 end*******************

# ************** 文件预览 start**************
@biomassviews.route('/biomassimgpreview/<filename>', methods=['GET'])
def biomassimgpreview(filename):
    return send_from_directory(
        os.path.join(os.getcwd(), config['imgConfig'].BIOMASS_IMG_PATH_RESULT, ""), filename)

@biomassviews.route('/biomassImage')
@login_required
def biomassImage():
    # 生成图纸
    planId = session.get('planId')
    # user_id = current_user.id
    BiomassImgService().imgCreate(planId)

    # 获取地址列表
    imglist = BiomassImgService().getImgList(planId)
    return render_template(
        'page/BiomassCHP/biomassImage.html',
        imglist=imglist,
        imglength=len(imglist))

# ************** 文件预览 end**************

# ************** 设备清单 start*************
@biomassviews.route('/biomassEquipmentList')
@login_required
def biomassEquipmentList():
    return render_template(
        'page/BiomassCHP/biomassEquipmentList.html')

# 同步设备清单数据，并获取最新设备清单
@biomassviews.route('/getBiomassEquipmentList', methods=['POST'])
@login_required
def getBiomassEquipmentList():
    planId = session.get('planId')

    # 同步数据
    # BiomassEquipmentService().updateEquipment(planId)

    # 获取最新设备清单
    equipmentList = EquipmentList.search_equipmentList(planId)
    equipmentList_json = json.loads(equipmentList.equipment_content)
    equipment_json = json.dumps(equipmentList_json)
    return equipment_json

@biomassviews.route('/saveBiomassEquipmentList', methods=['POST'])
@login_required
def saveBiomassEquipmentList():
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


# 获得冷却塔类型和抽汽点流量
@biomassviews.route('/getType', methods=['POST'])
@login_required
def getType():
    planId = request.values.get('planId')
    datas = {}
    circulatingWater = BiomassCHPCirculatingWater.search_circulating_water(
        planId)
    turbineBackpressure = BiomassCHPTurbineBackpressure.search_turbineBackpressure(
        planId)
    # 冷却塔类型
    datas['p_select'] = circulatingWater.p_select
    # 抽汽点流量
    if turbineBackpressure.e_exhaust_point_flow is not None:
        datas['e_exhaust_point_flow'] = str(float(turbineBackpressure.e_exhaust_point_flow))
    else:
        datas['e_exhaust_point_flow'] = None

    return jsonify({'getDatas': datas})

# ************** 设备清单 end***************


# ************** 设备清单模板维护 start***************

@biomassviews.route('/biomassEquipmentTemplate')
@login_required
def biomassEquipmentTemplate():
    session['menuSelect'] = "biomassEquipmentTemplate"
    return render_template(
        'page/BiomassCHP/biomassEquipmentTemplate.html'
    )


@biomassviews.route('/getBiomassEquipmentTemplate', methods=['POST'])
@login_required
def getBiomassEquipmentTemplate():
    current_app.logger.warning(u'操作者：%d,模板设备清单模板初始化', current_user.id)
    equipmentList = EquipmentListTemplate.search_EquipmentListTemplate(Module.biomassCHP)
    equipmentList_json = json.loads(equipmentList.equipment_template)
    equipment_json = json.dumps(equipmentList_json)
    titledir = ToBiomassCHP.getTitleTemplate()
    return jsonify({'titledir': titledir, 'equipment_json': equipment_json})


@biomassviews.route('/saveBiomassEquipmentTemplate', methods=['POST'])
@login_required
def saveBiomassEquipmentTemplate():
    current_app.logger.warning(u'操作者：%d,模板设备清单保存!', current_user.id)
    nameData = request.values.get('nameData')
    uidData = request.values.get('uidData')
    typeData = request.values.get('typeData')
    contentData = request.values.get('contentData')
    unitData = request.values.get('unitData')
    countData = request.values.get('countData')
    remarkData = request.values.get('remarkData')
    Equipment = ToBiomassCHP.saveEquipmentList(uidData, nameData, typeData, contentData, unitData, countData, remarkData)
    if Equipment is not None:
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'error'})

# ************** 设备清单模板维护 end***************
