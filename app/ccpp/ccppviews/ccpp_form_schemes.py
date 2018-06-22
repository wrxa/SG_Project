# -*- coding: utf-8 -*-
from flask import render_template, session
from flask_login import login_required
from . import ccppviews
from app.ccpp.models.constantModel import CcppConstant
from app.ccpp.service.ccpp_ccppService import CcppCalculateService
from app.ccpp.service.ccpp_circulating_waterService import CirculatingWaterService
from app.ccpp.models.ccpp_turbineModel import CcppTurbine
from app.ccpp.models.ccpp_ccpp_calculateModel import Ccpp_ccpp
from app.ccpp.service.ccpp_turbineService import CcppTurbineService
from flask import current_app


# 方案一览页面
@ccppviews.route('/allformschemes')
@login_required
def allformschemes():
    current_app.logger.warning(u'方案一览页面 (%d planId)', session.get('planId'))
    # 化学水
    biomassCHPConstant = CcppConstant.search_ccppConstant("water_treatment")
    ccpp = Ccpp_ccpp.search_ccpp_ccpp(session.get('planId'))
    # ccpp计算
    ccppConstant = CcppCalculateService().getCcppConstantData()
    # 循环水
    ccppHandingSystemConstant = CirculatingWaterService.getCirculatingWaterConstant()
    # 汽轮机
    CcppTurbineConstant = CcppTurbineService.getTurbineConstant()
    ccpp_Turbine = CcppTurbine.search_CcppTurbine(session.get('planId'))
    array_group_check = CcppTurbineService.sortPressure(ccpp_Turbine)
    return render_template(
        '/page/ccpp/ccpp_form_allschemes.html',
        constants=CcppTurbineConstant,
        steamturbineData=ccpp_Turbine,
        sortPressure=array_group_check,
        ccppHandingSystemConstant=ccppHandingSystemConstant,
        biomassCHPConstant=biomassCHPConstant,
        ccppConstant=ccppConstant,
        ccppboilertype=ccpp.boiler_single_or_dula_pressure_design)
