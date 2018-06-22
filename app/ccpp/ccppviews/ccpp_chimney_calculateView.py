# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
from app.ccpp.service.ccpp_chimney_calculateService import ChimneyCalculateService
from flask import current_app


# 烟囱计算页面
@ccppviews.route('/toCcppChimneyCalculate')
@login_required
def toCcppChimneyCalculate():
    chimneyCalculateConstant = ChimneyCalculateService.getChimneyCalculateConstant()
    return render_template(
        'page/ccpp/ccpp_chimney_calculate.html',
        constants=chimneyCalculateConstant)


# 初始化烟囱计算数据
@ccppviews.route('/initChimneyCalculate', methods=['POST'])
@login_required
def initChimneyCalculate():
    chimneyCalculate = ChimneyCalculateService().search_chimney_calculate(
        session.get('planId'))
    chimneyCalculateData = ChimneyCalculateService().to_ChimneyCalculateJson(chimneyCalculate)
    return jsonify({'chimneyCalculateData': chimneyCalculateData})


# 提交烟囱计算页面值
@ccppviews.route('/formChimneyCalculate', methods=['POST'])
@login_required
def formChimneyCalculate():
    ChimneyCalculate = None
    try:
        current_app.logger.warning(u'操作者：%d,提交烟囱计算页面值!', current_user.id)
        ChimneyCalculate = ChimneyCalculateService().to_ChimneyCalculate(request.form, session.get('planId'))
    except ValueError as e:
        print("Error %s" % e)
        current_app.logger.error(u'操作者：%d,输入数据有误，转换发生异常!%s', current_user.id, e.message)
        return jsonify({'newDatas': None, 'message': '输入数据有误，转换发生异常!'})
    else:
        ChimneyCalculateService().update_plan_date(session.get('planId'))
        ChimneyCalculateService().updata_chimney_calculate(ChimneyCalculate)
        newData = ChimneyCalculateService().search_chimney_calculate(
            session.get('planId'))
        datas = ChimneyCalculateService().to_ChimneyCalculateJson(newData)
        return jsonify({'newDatas': datas})
