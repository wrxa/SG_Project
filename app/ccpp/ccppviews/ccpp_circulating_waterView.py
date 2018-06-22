# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
from app.ccpp.service.ccpp_circulating_waterService import CirculatingWaterService
from flask import current_app


# 循环水系统页面 
@ccppviews.route('/toCcppCirculatingWater')
@login_required
def toCcppCirculatingWater():
    ccppHandingSystemConstant = CirculatingWaterService.getCirculatingWaterConstant()
    return render_template(
        'page/ccpp/ccpp_circulating_water.html',
        constants=ccppHandingSystemConstant)


# 初始化循环水系统数据
@ccppviews.route('/initCirculatingWater', methods=['POST'])
@login_required
def initCirculatingWater():
    circulatingWater = CirculatingWaterService().search_circulating_water(
        session.get('planId'))
    circulatingWaterData = CirculatingWaterService().to_circulatingWaterJson(circulatingWater)
    return jsonify({'circulatingWater': circulatingWaterData})


# 提交循环水系统页面值
@ccppviews.route('/formCirculatingWater', methods=['POST'])
@login_required
def formCirculatingWater():
    circulatingWater = None
    try:
        current_app.logger.warning(u'操作者：%d,提交循环水系统页面值!', current_user.id)
        circulatingWater = CirculatingWaterService().to_circulatingWater(request.form, session.get('planId'))
    except ValueError as e:
        print("Error %s" % e)
        current_app.logger.error(u'操作者：%d,输入数据有误，转换发生异常!%s', current_user.id, e.message)
        return jsonify({'newDatas': None})
    else:
        CirculatingWaterService().update_plan_date(session.get('planId'))
        CirculatingWaterService().updata_circulating_water(circulatingWater)
        newData = CirculatingWaterService().search_circulating_water(
            session.get('planId'))
        datas = CirculatingWaterService().to_circulatingWaterJson(newData)
        return jsonify({'newDatas': datas})
