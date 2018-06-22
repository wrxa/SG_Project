# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
from app.ccpp.models.ccpp_turbineModel import CcppTurbine
from app.ccpp.service.ccpp_turbineService import CcppTurbineService
from util.iapws_if97 import seuif97
from app.ccpp.models.ccpp_ccpp_economicModel import Ccpp_ccpp_economic
from app.ccpp.service.ccpp_ccppService import CcppCalculateService
from app.ccpp.service.ccpp_equipmentService import CcppEquipments
from app.ccpp import gl
from flask import current_app


@ccppviews.route('/toCcppTurbine')
@login_required
def toCcppTurbine():
    current_app.logger.warning(u'操作者：%d,进入汽轮机页面', current_user.id)
    CcppTurbineConstant = CcppTurbineService.getTurbineConstant()
    steamturbineData = CcppTurbine.search_CcppTurbine(session.get('planId'))
    array_group_check = CcppTurbineService.sortPressure(steamturbineData)
    return render_template(
        '/page/ccpp/ccpp_turbine.html',
        menuSelect='toCcppTurbine',
        constants=CcppTurbineConstant,
        steamturbineData=steamturbineData,
        sortPressure=array_group_check)


@ccppviews.route('/toCcppTurbineParaResearch')
@login_required
def toCcppTurbineParaResearch():
    current_app.logger.warning(u'操作者：%d,进入汽轮机参数设置页面', current_user.id)
    CcppTurbineConstant = CcppTurbineService.getTurbineConstant()
    steamturbineData = CcppTurbine.search_CcppTurbine(session.get('planId'))
    return render_template(
        '/page/ccpp/ccpp_turbine_para_research.html',
        menuSelect='toCcppTurbineParaResearch',
        constants=CcppTurbineConstant,
        steamturbineData=steamturbineData)


# 初期化汽轮机计算
@ccppviews.route('/initTurbineData', methods=['POST'])
@login_required
def initTurbineData():
    planId = session.get('planId')
    gpg_TurbineData = CcppTurbine.search_CcppTurbine(planId)
    TurbineJson = CcppTurbineService().to_TurbineJson(gpg_TurbineData)
    return jsonify({'steamturbine': TurbineJson})


# 获得主蒸汽压力和温度
@ccppviews.route('/getpressureandtemperature', methods=['POST'])
@login_required
def getpressureandtemperature():
    planId = session.get('planId')
    gpg_TurbineData = CcppTurbine.search_CcppTurbine(planId)
    e_steam_pressure = gpg_TurbineData.e_steam_pressure
    e_steam_temperature = gpg_TurbineData.e_steam_temperature
    return jsonify({'e_steam_pressure': gl.format_value(e_steam_pressure),
                    'e_steam_temperature': gl.format_value(e_steam_temperature)})


# 保存汽轮机页面信息
@ccppviews.route('/submitTurbineData', methods=['POST'])
@login_required
def submitTurbineData():
    plan_id = session.get('planId')
    current_app.logger.warning(u'操作者：%d,保存汽轮机页面', current_user.id)
    steamOldData = CcppTurbine.query.filter_by(plan_id=plan_id).first()
    if getattr(steamOldData, 's_parameter_flg') == '1':
        # 已经存在旧记录的场合，先清理旧记录
        steamNewData = CcppTurbineService().steamClear(session.get('planId'))
        CcppTurbine.insert_CcppTurbine(steamNewData)
    try:
        pointPower0, TurbineData = CcppTurbineService().to_steam(request.form, session.get('planId'))
        jumpflag = TurbineData.s_parameter_flg
        setattr(TurbineData, 'i_total_power0', pointPower0)
        setattr(TurbineData, 's_parameter_flg', '1')
        # 判断是第一次进入：第一次进入需要将数据的字段传入，第二次进入走此流程
        # 更新时间
        CcppTurbineService().update_plan_date(plan_id)
        CcppTurbine.insert_CcppTurbine(TurbineData)
        if request.form.get('tubineparahtml') != 'tubineparahtml':
            ccpp_ccpp_economic = CcppCalculateService().tbdata(plan_id)
            Ccpp_ccpp_economic.updata_ccppeconomic(ccpp_ccpp_economic)
            # 同步汽轮机数据到设备列表中
            CcppEquipments().replaceTurbineTurbine(plan_id, TurbineData)
            # 同步结束
        session['planId'] = plan_id
        newData = CcppTurbine.search_CcppTurbine(plan_id)
        datas = CcppTurbineService().to_TurbineJson(newData)
    except ZeroDivisionError as e:
        print("Error %s" % e)
        current_app.logger.error(u'操作者：%d,保存汽轮机页面信息异常%s', current_user.id, e.message)
        return jsonify({'state': 1, 'message': '输入数据有误!', 'newDatas': [], 'jumpflag': 0})
    else:
        return jsonify({'state': 0, 'message': '燃气蒸汽联合循环-汽轮机系统数据保存成功！', 'newDatas': datas, 'jumpflag': jumpflag})


# 根据压力查询温度
@ccppviews.route('/byPressure', methods=['POST'])
@login_required
def byPressure():
    datas = {}
    pressure_data = request.form.get('e_exhaust_point_pressure')
    temperature_data = seuif97.tsat_p((float(pressure_data) * 10))
    datas['temperature'] = temperature_data
    return jsonify({'temperature': datas})


# 根据压力和熵查询温度
@ccppviews.route('/byPressureEntropy', methods=['POST'])
@login_required
def byPressureEntropy():
    datas = {}
    pressure_data = request.form.get('e_exhaust_point_pressure')
    entropy_data = request.form.get('e_exhaust_point_entropy')
    temperature_data = seuif97.ps2t((float(pressure_data)), float(entropy_data))
    datas['temperature'] = temperature_data
    return jsonify({'temperature': datas})


# 根据温度查询压力
@ccppviews.route('/byTemperatureBack', methods=['POST'])
@login_required
def byTemperatureBack():
    datas = {}
    temperature_data = request.form.get('e_backpressure_temperature')
    pressure_data = seuif97.psat_t((float(temperature_data))) * 0.1
    datas['pressure'] = pressure_data
    return jsonify({'pressure': datas})


# 根据压力查询温度
@ccppviews.route('/byPressureBack', methods=['POST'])
@login_required
def byPressureBack():
    datas = {}
    pressure_data = request.form.get('e_backpressure_pressure')
    temperature_data = seuif97.tsat_p((float(pressure_data) * 10))
    datas['temperature'] = temperature_data
    return jsonify({'temperature': datas})


# 根据压力和熵查询焓
@ccppviews.route('/byPressureEntropyBack', methods=['POST'])
@login_required
def byPressureEntropyBack():
    datas = {}
    pressure_data = request.form.get('e_backpressure_pressure')
    entropy_data = request.form.get('e_exhaust_after_entropy')
    enthalpy_data = seuif97.ps2h((float(pressure_data)), float(entropy_data))
    datas['enthalpy'] = enthalpy_data
    return jsonify({'enthalpy': datas})


# 根据温度和熵查询焓
@ccppviews.route('/byTemperatureEntropyBack', methods=['POST'])
@login_required
def byTemperatureEntropyBack():
    datas = {}
    temperature_data = request.form.get('e_backpressure_temperature')
    entropy_data = request.form.get('e_exhaust_after_entropy')
    enthalpy_data = seuif97.ts2h((float(temperature_data)), float(entropy_data))
    datas['enthalpy'] = enthalpy_data
    return jsonify({'enthalpy': datas})
