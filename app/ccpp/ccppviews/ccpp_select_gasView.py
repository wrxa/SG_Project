# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
from app.ccpp.service.ccpp_ccppService import SelectGasTurbineService
from app.ccpp import gl
from flask import current_app


# 进入选择方案页面
@ccppviews.route('/toSelectGasTurbine')
@login_required
def toSelectGasTurbine():
    '''
    从当前表(ccpp_ccpp sheet)获得需求功率,达到可修改的目的
    获得需求功率上下浮动10%的全部方案
    '''
    planId = session.get('planId')
    engine_demand_power = gl.format_value(SelectGasTurbineService().getEngine_demand_power(planId))
    engine_demand_power = int(engine_demand_power)
    try:
        ccppmodellist, ccppturbinelist = SelectGasTurbineService().getGasTurbine(engine_demand_power, planId)
    except Exception as e:
        print("Error %s" % e)
        current_app.logger.error(u'操作者：%d,生成方案非汽轮机异常%s', current_user.id, e.message)
        return render_template(
            'page/ccpp/ccpp_select_device.html',
            need_engine_demand_power=engine_demand_power,
            ccppturbinelist=[],
            countturbine=0,
            count=0,
            ccppmodellist=[])
    else:
        return render_template(
            'page/ccpp/ccpp_select_device.html',
            need_engine_demand_power=engine_demand_power,
            ccppturbinelist=ccppturbinelist,
            countturbine=len(ccppturbinelist),
            count=len(ccppmodellist),
            ccppmodellist=ccppmodellist)


# 燃机选择处理
@ccppviews.route('/selectGasDealwith', methods=['POST'])
@login_required
def selectGasDealwith():
    '''
    1、将当前方案中：燃机数量、所需燃机数据存储在ccpp_ccpp表中
    2、提示成功。
    '''
    attrid = request.form.get('deviceid')
    devicenum = request.form.get('devicenum')
    SelectGasTurbineService().saveGasTurbineData(
        attrid, devicenum, session.get('planId'))
    return jsonify(
        {'message': u'成功选择方案！'})
