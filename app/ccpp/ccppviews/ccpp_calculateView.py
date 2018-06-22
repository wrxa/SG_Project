# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
from app.ccpp.service.ccpp_ccppService import CcppCalculateService
from flask import current_app


# 进入ccpp_ccpp参数调研界面
@ccppviews.route('/toCcppParaResearch')
@login_required
def toCcppParaResearch():
    '''
    1、加载页面常量数据
    2、加载全部燃机数据
    '''
    ccppConstant = CcppCalculateService().getCcppConstantData()
    ccppallGasTurbine = CcppCalculateService().getAllGasTurbine()
    current_app.logger.warning(u'操作者：%d,加载锅炉计算参数设置页面常量数据,加载全部燃机数据', current_user.id)
    return render_template(
        'page/ccpp/ccpp_para_research.html',
        constants=ccppConstant,
        ccppallGasTurbine=ccppallGasTurbine)


# 进入ccpp_ccpp计算页面带数据
@ccppviews.route('/toCcppCalculate')
@login_required
def toCcppCalculate():
    '''
    1、加载页面常量数据
    2、加载全部燃机数据
    '''
    ccppConstant = CcppCalculateService().getCcppConstantData()
    ccppallGasTurbine = CcppCalculateService().getAllGasTurbine()
    current_app.logger.warning(u'操作者：%d,加载锅炉计算页面常量数据,加载全部燃机数据', current_user.id)
    return render_template(
        'page/ccpp/ccpp_calculate.html',
        constants=ccppConstant,
        ccppallGasTurbine=ccppallGasTurbine)


# 加载ccpp计算页面数据
@ccppviews.route('/initInputData', methods=['POST'])
@login_required
def initInputData():
    '''
    加载页面input数据
    '''
    ccppinputdata, permissiondata, defaultvaluedata = CcppCalculateService().getCcppInputData(
        session.get('planId'))
    return jsonify({'ccppinputdata': ccppinputdata, 'permissiondata': permissiondata, 'defaultvaluedata': defaultvaluedata})


# 通过id获得一条燃机数据
@ccppviews.route('/findgasTurbineById', methods=['POST'])
@login_required
def findgasTurbineById():
    '''
    用户进入ccpp计算页面后对生成的方案不满意，自己选择燃机机型
    '''
    deviceid = request.form.get('deviceid')
    ccpp_ccpp = CcppCalculateService().getGasTurbineById(deviceid, 0)
    current_app.logger.warning(u'操作者：%d,尝试修改燃机数据', current_user.id)
    return jsonify({'ccpp_ccpp': ccpp_ccpp, 'message': 'success!'})


# 保存ccpp计算表单数据
@ccppviews.route('/submitCalculateform', methods=['POST'])
@login_required
def submitCalculateform():
    '''
    保存ccpp计算表单数据
    '''
    try:
        current_app.logger.warning(u'操作者：%d,保存ccpp计算表单数据', current_user.id)
        CcppCalculateService().submitCcppCalculateForm(request.form, session.get('planId'))
    except ZeroDivisionError as e:
        print("Error %s" % e)
        current_app.logger.error(u'操作者：%d,输入数据有误除0发生!%s', current_user.id, e.message)
        return jsonify({'state': 1, 'message': '输入数据有误除0发生!'})
    except Exception as e:
        current_app.logger.error(u'操作者：%d,输入数据有误，转换发生!%s', current_user.id, e.message)
        return jsonify({'state': 1, 'message': '输入数据有误，转换发生!'})
    else:
        ccppinputdata, permissiondata, defaultvaluedata = CcppCalculateService().getCcppInputData(session.get('planId'))
        ccppinputdata['engine_exhuast_gas_energy_design']
        return jsonify({'state': 0, 'message': '燃气蒸汽联合循环-余热锅炉数据保存成功!', 'ccppinputdata': ccppinputdata, 'permissiondata': permissiondata, 'defaultvaluedata': defaultvaluedata})
