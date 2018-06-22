# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
from ..service.ccpp_questionService import QuestionService
from app.ccpp import gl
from flask import current_app


# 进入ccpp需求调查表页面
@ccppviews.route('/toCcppQuestionnaire')
@login_required
def toCcppQuestionnaire():
    '''
    进入需求调查表页面
    加载字段常量数据、加载已有方案、加载公司信息
    '''
    ccppConstant, plans, companys = QuestionService.getQuestionnaireConstant()
    current_app.logger.warning(u'操作者：%d,进入ccpp需求调查表页面!', current_user.id)
    # current_app.logger.debug('A value for debugging')
    # current_app.logger.warning('A warning occurred (%d apples)', 42)
    # current_app.logger.error('An error occurred')
    return render_template(
        'page/ccpp/ccpp_questionnaire.html',
        constants=ccppConstant,
        plans=plans,
        companys=companys)


# 加载ccpp需求调研表页面数据
@ccppviews.route('/initQuestionnaire', methods=['POST'])
@login_required
def initQuestionnaire():
    '''
    页面select选择公司后加载此程序，传入选择的方案ID
    '''
    planId = session.get('planId')
    # 获得页面的json格式数据
    questionnaireData = None
    if planId is not None:
        questionnaireData = QuestionService().getQuestionnaireDataJson(planId)
    # 将方案ID保存
    return jsonify({'planId': planId, 'questionnaire': questionnaireData})


# 提交ccpp需求调研表
@ccppviews.route('/submitQuestionnaire', methods=['POST'])
@login_required
def submitQuestionnaire():
    '''
    提交方案：如果公司不存在则需要创建公司，
    公司地址和名称不空则能够创建公司则可创建新的方案，返回方案id
    否则创建失败，返回None
    '''
    planId = session.get('planId')
    companyName = request.form.get('company_name')
    planName = request.form.get('plan_name')
    companyLocation = request.form.get('company_location')
    current_app.logger.warning(u'操作者：%d,提交ccpp需求调研表!', current_user.id)
    question = None
    try:
        question = QuestionService().submitQuestionnaire(request.form, companyName, planName, companyLocation, planId, None)
    except Exception as e:
        current_app.logger.error(u'操作者：%d,数据输入有误!%s', current_user.id, e.message)
        return jsonify({'state': 0, 'planId': planId, 'message': u'数据输入有误!'})
    else:
        if question is None:
            current_app.logger.error(u'操作者：%d,您没有填写公司名称，或者项目地址!%s', current_user.id, e.message)
            return jsonify({'state': 0, 'planId': planId, 'message': u'您没有填写公司名称，或者项目地址!'})
        else:
            session['planId'] = question.plan_id
            return jsonify({'total_design': gl.format_value(question.total_design), 'state': 1, 'planId': question.plan_id, 'message': '燃气蒸汽联合循环-需求调查表数据保存成功!'})
