# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
from app.ccpp.models.ccpp_biomassModel import CcppCHPWaterTreatment
from app.ccpp.models.constantModel import CcppConstant
from app.ccpp.service.ccpp_biomassService import BiomassService
from flask import current_app


# **************化学水处理 start*******************
@ccppviews.route('/biomassWaterTreatment')
@login_required
def biomassWaterTreatment():
    current_app.logger.warning(u'操作者：%d,化学水处理 start', current_user.id)
    biomassCHPConstant = CcppConstant.search_ccppConstant(
        "water_treatment")
    return render_template(
        'page/ccpp/ccpp_biomass_water_treatment.html',
        constants=biomassCHPConstant)


# 初期化化学水处理
@ccppviews.route('/biomassinitWater', methods=['POST'])
@login_required
def biomassinitWater():
    planId = request.values.get('planId')
    water = CcppCHPWaterTreatment.search_water(planId)
    waterData = BiomassService.to_waterJson(water)
    return jsonify({'water': waterData})


# 保存化学水处理页面信息
@ccppviews.route('/biomassFormDataWater', methods=['POST'])
@login_required
def biomassFormDataWater():
    try:
        waterData = BiomassService.to_water(request.form, session.get('planId'))
    except ValueError as e:
        current_app.logger.error(u'操作者：%d,保存化学水处理页面信息异常%s', current_user.id, e.message)
        return jsonify({'flag': "fail", 'info': "看来是专业人士，数据输入有误！"})
    else:
        CcppCHPWaterTreatment.insert_water(waterData)
        return jsonify({'flag': "success"})

# **************化学水处理 end*******************
