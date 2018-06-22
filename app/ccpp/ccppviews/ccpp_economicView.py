# -*- coding: utf-8 -*-
from flask import render_template, jsonify, session, request, send_from_directory
from flask_login import login_required, current_user
from . import ccppviews
from app.ccpp.service.ccpp_economicService import EconomicService
import os
from config import config
from util.get_all_path import GetPath
from flask import current_app


# 进入ccpp经济性分析表页面
@ccppviews.route('/toCcppEconomic')
@login_required
def toCcppEconomic():
    '''
    进入经济性分析表页面
    加载字段常量数据
    '''
    ccppConstant = EconomicService.getEconomicConstant()
    return render_template(
        'page/ccpp/ccpp_economic.html',
        constants=ccppConstant)


# 进入ccpp经济性分析表页面
@ccppviews.route('/toChooseTemplate/<int:planId>')
@login_required
def toChooseTemplate(planId):
    '''
    进入经济性分析表页面
    加载字段常量数据
    '''
    session['planId'] = planId
    ccppConstant = EconomicService.getEconomicConstant()
    return render_template(
        'page/ccpp/ccpp_economic.html',
        constants=ccppConstant)


# 加载ccpp计算页面数据
@ccppviews.route('/initEconomicInputData', methods=['POST'])
@login_required
def initEconomicInputData():
    '''
    加载页面input数据
    '''
    planId = session.get('planId')
    # 获得页面的json格式数据
    economicInputData = None
    if planId is not None:
        economicInputData = EconomicService().getEconomicDataJson(planId)
    return jsonify({'planId': planId, 'economicInputData': economicInputData})


# 编辑方案内容页面按下预览按钮打开预览页面
@ccppviews.route('/ccpprepayrefer')
@login_required
def ccpprepayrefer():
    planId = session.get('planId')
    economicInputData = EconomicService().getEconomicDataJson(planId)
    return render_template('page/ccpp/ccpp_repay_refer.html', economicInputData=economicInputData)


# 保存ccpp经济性分析计算数据
@ccppviews.route('/submitEconomicform', methods=['POST'])
@login_required
def submitEconomicform():
    '''
    保存ccpp经济性计算数据
    '''
    try:
        EconomicService().submitEconomicForm(request.form, session.get('planId'))
        ccppinputdata, permissiondata, defaultvaluedata = EconomicService().getInputData(session.get('planId'))
    except ZeroDivisionError as e:
        print("Error %s" % e)
        current_app.logger.error(u'操作者：%d,输入数据有误, 除0情况发生!%s', current_user.id, e.message)
        ccppinputdata, permissiondata, defaultvaluedata = EconomicService().getInputData(session.get('planId'))
        return jsonify({'state': 0, 'message': '输入数据有误, 除0情况发生!', 'ccppinputdata': ccppinputdata, 'permissiondata': permissiondata, 'defaultvaluedata': defaultvaluedata})
    except ValueError as e:
        print("Error %s" % e)
        current_app.logger.error(u'操作者：%d,输入数据有误，转换发生异常!%s', current_user.id, e.message)
        ccppinputdata, permissiondata, defaultvaluedata = EconomicService().getInputData(session.get('planId'))
        return jsonify({'state': 0, 'message': '输入数据有误，转换情况发生!', 'ccppinputdata': ccppinputdata, 'permissiondata': permissiondata, 'defaultvaluedata': defaultvaluedata})
    else:
        return jsonify({'state': 1, 'message': '燃气蒸汽联合循环-经济性分析数据保存成功!', 'ccppinputdata': ccppinputdata, 'permissiondata': permissiondata, 'defaultvaluedata': defaultvaluedata})


# 文件下载
@ccppviews.route("/excleanddownload", methods=['GET'])
@login_required
def excleanddownload():
    planId = session.get('planId')
    EconomicService().getEconomicExcle(planId, current_user.id)
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    dirpath = os.path.join(os.getcwd(), config['excleConfig'].CCPP_EXCLE_ECONOMIC_PATH_RESULT)
    # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    filename = GetPath.getExcleCcppResultFileName(planId, current_user.id)
    # 获取文件名称
    return send_from_directory(dirpath, filename, as_attachment=True)
    # as_attachment=True 一定要写，不然会变成打开，而不是下载