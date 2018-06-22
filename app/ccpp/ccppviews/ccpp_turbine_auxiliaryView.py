# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
from app.biomass_chp.service.biomassService import ToBiomassCHP
from app.biomass_chp.models.modelsBiomass import BiomassCHPconstant, BiomasschpTurbineAuxiliary
from app.ccpp.service.ccpp_equipmentService import CcppEquipments
from flask import current_app


# ************** 汽机辅机 start*******************
@ccppviews.route('/biomassTurbineAuxiliary')
@login_required
def biomassTurbineAuxiliary():
    current_app.logger.warning(u'操作者：%d,汽机辅机', current_user.id)
    biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant(
        "turbine_auxiliary")
    return render_template(
        'page/ccpp/ccpp_turbine_auxiliary.html',
        menuSelect='biomassBoilerAuxiliaries',
        constants=biomassCHPConstant)


# 初期化汽机辅机
@ccppviews.route('/biomassinitTurbineAuxiliary', methods=['POST'])
@login_required
def biomassinitTurbineAuxiliary():
    planId = session.get('planId')
    turbineAuxiliary = BiomasschpTurbineAuxiliary.search_turbine_auxiliary(
        planId)
    turbineAuxiliaryData = ToBiomassCHP.to_turbineAuxiliaryJson(
        turbineAuxiliary, planId)
    return jsonify({'turbineAuxiliaryData': turbineAuxiliaryData})


# 保存汽机辅机页面信息
@ccppviews.route('/biomassFormTurbineAuxiliary', methods=['POST'])
@login_required
def biomassFormTurbineAuxiliary():
    current_app.logger.warning(u'操作者：%d, 保存汽机辅机数据', current_user.id)
    turbineAuxiliary = ToBiomassCHP.to_turbineAuxiliary(
        request.form, session.get('planId'))
    BiomasschpTurbineAuxiliary.insert_turbine_auxiliary(turbineAuxiliary)
    CcppEquipments().replaceTurbineAuxiliary(session.get('planId'), turbineAuxiliary)
    newData = BiomasschpTurbineAuxiliary.search_turbine_auxiliary(
        session.get('planId'))
    datas = ToBiomassCHP.to_turbineAuxiliaryJson(newData,
                                                 session.get('planId'))

    return jsonify({'newDatas': datas})
# ************** 汽机辅机 end*******************