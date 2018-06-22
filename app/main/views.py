# -*- coding: utf-8 -*-
import os
import threading
import json
from datetime import datetime
import time
from flask import render_template, redirect, url_for, flash,\
    abort, jsonify, request, session, send_from_directory
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, ChangePasswordForm,\
    ChangeEmailForm, UpdateUserForm, RegistrationForm
from .. import db
from ..models import User, Company, Plan, Module, ReportTemplate, Role, MyException
from ..decorators import admin_required
from app.coal_chp.model.coalchpModels import CoalCHPComponent, CoalCHPConstant
from app.ccpp.service.ccpp_questionService import QuestionService
from app.ccpp.service.ccpp_ccppService import CcppCalculateService
from app.main.service.mainService import MainService
from app.main.service.templateAnalyzeService import TemplateDealwithService
from app.main.service.parseMD import ganMenu, addAnchorMark, convertdel,\
     tempFile, createMD
from app.coal_chp.service.coalService import ToCoalCHP
from app.biomass_chp.service.biomassService import ToBiomassCHP
from app.biomass_chp.models.modelsBiomass import BiomassCHPconstant, BiomassCHPFuelComponent
from app.gpg.model.gasPowerGeneration_models import GasPowerGenerationConstant
from app.gpg.service.gasPowerGeneration_Service import ToGPG
from app.energy_island.energyisland_service import EnergyIslandService
from werkzeug.utils import secure_filename
import copy
from config import config
from util.get_all_path import GetPath
from flask import current_app

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 显示主页
# 必要条件：用户需先登录
# Returns：返回主页面
@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    session['menuSelect'] = "collapsed index"
    count = Plan.search_checkedCount(current_user.role_id)
    # 更新每条方案的主要设备参数字段
    plans = Plan.search_plan_all()
    for plan in plans:
        if plan.main_equipment_para is None:
            if plan.module_id == Module.coalCHP:
                plan.main_equipment_para = ToCoalCHP().getMainEquipmentPara(plan.id)
            if plan.module_id == Module.biomassCHP:
                plan.main_equipment_para = ToBiomassCHP().getMainEquipmentPara(plan.id)
            if plan.module_id == Module.CCPP:
                plan.main_equipment_para = CcppCalculateService().getMainEquipmentPara(plan.id)
            if plan.module_id == Module.gasPowerGeneration:
                plan.main_equipment_para = ToGPG().getMainEquipmentPara(plan.id)
            Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
    session['checkedPlanCount'] = count
    return render_template('index.html')


# 显示用户主页
# 必要条件： 用户需先登录
# Returns：用户个人主页面
@main.route('/home')
@login_required
def home():
    return render_template('home.html')


# 显示用户信息
# 必要条件： 用户需先登录
# Returns：用户个人主信息页面
@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(user_name=username).first()
    if user is None:
        abort(404)
    return render_template('user_info.html', user=user)


# 编辑用户个人信息
# 必要条件： 用户需先登录
# Returns：显示更改用户个人信息页面；若提交更改个人信息表单，则返回用户个人信息页面
@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    # 提交更改信息
    if form.validate_on_submit():
        current_user.user_tel = form.tel.data
        db.session.add(current_user)
        flash(u'您的信息已更新', 'success')
        return redirect(url_for('.user', username=current_user.user_name))
    # 显示用户信息
    form.tel.data = current_user.user_tel
    # return render_template('edit_profile.html', form=form)
    return render_template('page_profile.html', form=form)


# 显示用户主页
# 必要条件： 用户需先登录
#           用户类型需是管理员
# Returns：显示管理员更改用户个人信息页面；若提交管理员更改用户信息表单则返回用
#          户个人信息页面
@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    # 提交更改信息
    if form.validate_on_submit():
        user.user_name = form.username.data
        user.user_tel = form.tel.data
        db.session.add(user)
        flash(u'用户信息已被更新', 'success')
        return redirect(url_for('.user', username=user.user_name))
    # 显示用户信息
    form.username.data = user.user_name
    form.tel.data = user.user_tel
    return render_template('edit_profile_admin.html', form=form, user=user)


# 用户更改密码
# Returns: 返回更改密码页面；若用户提交更改密码表单，返回主页；
@main.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    '''
    用户修改密码
    hash_password 用户新密码
    update_dateTime 用户表更新当前操作时间
    修改成功进入首页，失败留在当页面
    '''
    form = ChangePasswordForm()
    if form.validate_on_submit():
        # 检验密码是否正确
        if current_user.verify_password(form.old_password.data):
            current_user.hash_password = form.password.data
            current_user.update_dateTime = datetime.now()
            db.session.add(current_user)
            flash(u'密码已更新', 'success')
            return redirect(
                url_for('main.index', username=current_user.user_name))
        else:
            flash(u'密码不正确', 'danger')
    return render_template("page/change_password.html", form=form)


# 用户更改邮箱
# Returns：返回更改邮箱页面；若用户提交有效更改邮箱表单，返回主页；
@main.route('/change-email', methods=['GET', 'POST'])
@login_required
def change_email():
    '''
    用户更改邮箱
    user_email 用户新邮箱
    update_dateTime 用户表更新当前操作时间
    修改成功进入首页，失败留在当页面
    '''
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            current_user.user_email = form.email.data
            current_user.update_dateTime = datetime.now()
            db.session.add(current_user)
            flash(u'邮箱已更改', 'success')
            current_app.logger.warning(u'操作者：%d,当前用户邮箱已更改', current_user.id)
            return redirect(
                url_for('main.index', username=current_user.user_name))
        else:
            flash(u'邮箱或密码不正确', 'danger')
    return render_template("page/change_email.html", form=form)


# manage_user
@main.route('/list_user', methods=['GET', 'POST'])
@login_required
@admin_required
def list_user():
    users = User.select_all()
    roles = Role.search_plan_all()
    return render_template('page/manage_user.html', users=users, roles=roles)


# delete_user
@main.route('/delete_user/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    User.delete_user(user)
    flash(u'用户删除成功', 'success')
    current_app.logger.warning(u'操作者：%d,用户删除成功%d', current_user.id, user.id)
    return redirect(url_for('main.list_user'))


@main.route('/edit_user/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(id):
    user = User.query.get_or_404(id)
    form = UpdateUserForm(user=user)
    if form.validate_on_submit():
        user.role_id = form.role_id.data
        user.update_dateTime = datetime.now()
        db.session.add(current_user)
        flash(u'用户信息已更改成功', 'success')
        current_app.logger.warning(u'操作者：%d,用户信息已更改成功%d', current_user.id, user.id)
        return redirect(url_for('main.list_user'))
    user_name = user.user_name
    user_eid = user.user_eid
    form.role_id.data = user.role_id
    return render_template(
        "page/admin_edit_user.html",
        form=form,
        name=user_name,
        eid=user_eid)


@main.route('/register', methods=['GET', 'POST'])
@login_required
@admin_required
def register():
    '''
    用户提交注册信息
    user_email 用户注册邮箱
    user_name 用户注册名称
    hash_password 用户密码
    update_dateTime 用户表更新当前操作时间
    注册成功后进入首页，失败留在当页面
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        # 添加用户到数据库
        user = User(
            user_eid=form.user_eid.data,
            user_email=form.user_email.data,
            user_name=form.user_name.data,
            hash_password=form.password.data,
            company_id=1,
            role_id=form.role_id.data,
            reg_dateTime=datetime.now(),

            update_dateTime=datetime.now()
        )
        db.session.add(user)
        db.session.commit()
        flash(u'添加新用户成功', 'success')
        return redirect(url_for('main.list_user'))
    return render_template('page/add_user.html', form=form)


# #####################################方案管理共通开始#############################################################
# 所有方案管理頁面
@main.route('/planList/<moduleName>')
@login_required
def planList(moduleName):
    # 清空当前session中的方案ID信息
    session['planId'] = None
    plans = Plan.search_by_module(moduleName)
    plans_distinct = Plan.search_distinct_user()
    companys = Company.search_company()
    users = User.select_all()
    if moduleName == Module.coalCHP:
        # 更新燃煤热电联产中每条方案的主要设备参数字段
        for plan in plans:
            if plan.main_equipment_para is None:
                plan.main_equipment_para = ToCoalCHP().getMainEquipmentPara(plan.id)
                Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
        session['menuSelect'] = "coalCHPplanList"
    elif moduleName == Module.biomassCHP:
        # 更新生物质中每条方案的主要设备参数字段
        for plan in plans:
            if plan.main_equipment_para is None:
                plan.main_equipment_para = ToBiomassCHP().getMainEquipmentPara(plan.id)
                Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
        session['menuSelect'] = "biomassplanList"
    elif moduleName == Module.CCPP:
        # 更新ccpp中每条方案的主要设备参数字段
        for plan in plans:
            if plan.main_equipment_para is None:
                plan.main_equipment_para = CcppCalculateService().getMainEquipmentPara(plan.id)
                Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
        session['menuSelect'] = "ccppplanList"
    elif moduleName == Module.gasPowerGeneration:
        # 更新汽机中每条方案的主要设备参数字段
        for plan in plans:
            if plan.main_equipment_para is None:
                plan.main_equipment_para = ToGPG().getMainEquipmentPara(plan.id)
                Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
        session['menuSelect'] = "gpgplanList"
    elif moduleName == Module.energyIsland:
        session['menuSelect'] = "energyIslandplanList"

    session['moduleName'] = moduleName
    # plans = Plan.search_by_module(moduleName)

    return render_template(
        'page/planList.html',
        plans=plans,
        companys=companys,
        users=users,
        plans_distinct=plans_distinct,
        moduleName=moduleName,
        pageFlag="planList")


# 获取公司和用户名称的补全
@main.route('/getAutoComplete', methods=['GET'])
@login_required
def getAutoComplete():
    companysComplete, usersComplete, templateComplete = MainService.getPlanComplete()
    return jsonify({
        'companysComplete': companysComplete,
        'usersComplete': usersComplete,
        'templateComplete': templateComplete
    })


# 根据id查询主要设备参数字段
@main.route('/getmainequipemntpara', methods=['POST'])
@login_required
def getmainequipemntpara():
    planId = request.values.get('planId')
    plan = Plan.search_planById(planId)
    return jsonify({
        'main_equipment_para': plan.main_equipment_para
    })


# 更新主要设备参数
@main.route('/updatamainequipemntpara', methods=['POST'])
@login_required
def updatamainequipemntpara():
    planId = request.values.get('planId')
    main_equipment_para = request.values.get('main_equipment_para')
    moduleName = session.get('moduleName')
    plan = Plan.search_planById(planId)
    if main_equipment_para is not None and main_equipment_para == '' or main_equipment_para == '\n':
        # 更新成数据库原始数据
        if moduleName == Module.coalCHP:
            plan.main_equipment_para = ToCoalCHP().getMainEquipmentPara(planId)
        elif moduleName == Module.biomassCHP:
            # 更新生物质中每条方案的主要设备参数字段
            plan.main_equipment_para = ToBiomassCHP().getMainEquipmentPara(planId)
        elif moduleName == Module.CCPP:
            # 更新ccpp中每条方案的主要设备参数字段
            plan.main_equipment_para = CcppCalculateService().getMainEquipmentPara(plan.id)
        elif moduleName == Module.gasPowerGeneration:
            # 更新汽机中每条方案的主要设备参数字段
            plan.main_equipment_para = ToGPG().getMainEquipmentPara(plan.id)
        elif moduleName == Module.energyIsland:
            # 更新能源互联岛中每条方案的主要设备参数字段
            plan.main_equipment_para = ""
    else:
        plan.main_equipment_para = main_equipment_para
    Plan.insert_plan(plan)
    current_app.logger.warning(u'操作者：%d,更新主要设备参数', current_user.id)
    return jsonify({
        'state': 'success'
    })


# 按查询条件检索方案
@main.route('/queryPlans', methods=['POST'])
@login_required
def queryPlans():
    company_id = request.values.get('company_id')
    user_id = request.values.get('user_id')
    moduleName = request.values.get('moduleName')
    plans = Plan.search_planByParams(company_id, user_id, moduleName)
    companys = Company.search_company()
    users = User.select_all()
    plansJson = MainService.to_planJson(plans)
    companyJson = MainService.to_companyJson(companys)
    userJson = MainService.to_userJson(users)
    return jsonify({
        'newPlans': plansJson,
        'companys': companyJson,
        'users': userJson
    })


# 删除方案
@main.route('/deletePlan', methods=['POST'])
@login_required
def deletePlan():
    planId = request.values.get('planId')
    company_id = request.values.get('company_id')
    user_id = request.values.get('user_id')
    moduleName = request.values.get('moduleName')
    companys = Company.search_company()
    companyJson = MainService.to_companyJson(companys)
    users = User.select_all()
    userJson = MainService.to_userJson(users)
    if moduleName == Module.coalCHP:
        MainService.drop_plan_coalchp(planId)
    elif moduleName == Module.biomassCHP:
        MainService.drop_plan_biomass(planId)
    elif moduleName == Module.CCPP:
        MainService.drop_plan_ccpp(planId, current_user.id)
    elif moduleName == Module.gasPowerGeneration:
        MainService.drop_plan_gpg(planId)
    elif moduleName == Module.energyIsland:
        MainService.drop_plan_energyIsland(planId)
    plans = Plan.search_planByParams(company_id, user_id, moduleName)
    plansJson = MainService.to_planJson(plans)
    MainService.deleteFile(planId, current_user.id)
    current_app.logger.warning(u'操作者：%d,删除方案%s', current_user.id, planId)
    return jsonify({
        'newPlans': plansJson,
        'companys': companyJson,
        'users': userJson
    })


# 新增或修改方案进入
# 各个模块入口
@main.route('/editPlan/<int:planId><moduleName>')
@login_required
def editPlan(planId, moduleName):
    session['moduleName'] = moduleName
    # 燃煤热电联产
    if moduleName == Module.coalCHP:
        coalCHPComponent = CoalCHPComponent.search_coalCHPComponent()
        coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
            "coalCHP_questionnaire")
        # 查询已有方案
        plans = Plan.search_plan(current_user.id)
        companys = Company.search_company()
        # 如果是修改（id>0修改，id=0新增）
        if planId > 0:
            session['planId'] = planId
        return render_template(
            'page/coalCHP/coalQuestionnaire.html',
            coalsort=coalCHPComponent,
            constants=coalCHPConstant,
            plans=plans,
            companys=companys)
    if moduleName == Module.CCPP:
        if planId > 0:
            # 点击的是修改
            session['planId'] = planId
        ccppConstant, plans, companys = QuestionService.getQuestionnaireConstant()
        return render_template(
            'page/ccpp/ccpp_questionnaire.html',
            constants=ccppConstant,
            plans=plans,
            companys=companys)
    # 生物质热电
    if moduleName == Module.biomassCHP:
        biomassCHPConstant = BiomassCHPconstant.search_biomassCHPconstant("biomassCHP_questionnaire")
        biomassCHPComponent = BiomassCHPFuelComponent.search_biomassCHPComponent()
        # 查询已有方案
        plans = Plan.search_plan(current_user.id)
        companys = Company.search_company()
        if planId > 0:
            session['planId'] = planId
        elif not session['planId']:
            session['planId'] = None
        return render_template(
            'page/BiomassCHP/biomassQuestionnaire.html',
            fuelsort=biomassCHPComponent,
            constants=biomassCHPConstant,
            plans=plans,
            companys=companys)
    # 煤气发电
    if moduleName == Module.gasPowerGeneration:
        GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant("GPG_questionnaire")
        plans = Plan.search_plan(current_user.id)
        companys = Company.search_company()
        if planId > 0:
            session['planId'] = planId
        elif not session['planId']:
            session['planId'] = None
        return render_template(
            'page/GasPowerGeneration/GPG_Questionnaire.html',
            menuSelect='GPG_Questionnaire',
            constants=GPGConstant,
            plans=plans,
            companys=companys)

    # 能源互联
    if moduleName == Module.energyIsland:
        eir_work_list = EnergyIslandService().get_list_eir_work()
        eir_cost_list = EnergyIslandService().get_list_eir_cost()
        eir_available_list = EnergyIslandService().get_list_eir_available()
        eir_available_list_2 = EnergyIslandService().get_list_eir_available_2()
        eir_heat_list = EnergyIslandService().get_list_eir_heat()
        eir_cool_list = EnergyIslandService().get_list_eir_cool()
        eir_steam_list = EnergyIslandService().get_list_eir_steam()
        eir_electric_list = EnergyIslandService().get_list_eir_electric()
        eir_hot_water_list = EnergyIslandService().get_list_eir_hot_water()
        eir_air_supply_list = EnergyIslandService().get_list_eir_air_supply()
        eir_season_typical_day = EnergyIslandService().get_list_eir_season_typical_day()
        time_list = EnergyIslandService().get_list_time()
        month_list = EnergyIslandService().get_list_month()
        companys = Company.search_company()
        plans = Plan.search_plan(current_user.id)
        if planId > 0:
            session['planId'] = planId
        elif not session['planId']:
            session['planId'] = None
        session['menuSelect'] = "energyIslandplanList"
        return render_template(
            'page/energyisland/energyisland_questionnaire.html',
            eir_work_list=eir_work_list,
            eir_cost_list=eir_cost_list,
            eir_available_list=eir_available_list,
            eir_available_list_2=eir_available_list_2,
            eir_heat_list=eir_heat_list,
            eir_cool_list=eir_cool_list,
            eir_steam_list=eir_steam_list,
            eir_electric_list=eir_electric_list,
            eir_hot_water_list=eir_hot_water_list,
            eir_air_supply_list=eir_air_supply_list,
            eir_season_typical_day=eir_season_typical_day,
            time_list=time_list,
            month_list=month_list,
            plans=plans,
            companys=companys)

# #####################################方案管理共通结束#############################################################
# 专家修改审核状态


@main.route('/planState', methods=['POST'])
@login_required
def planState():
    if current_user.role_id not in [1, 2, 4, 5, 6, 7]:
        return jsonify({'state': 0})
    planId = request.form.get('planId')
    planState = request.form.get('planState')
    plan = Plan.search_planById(planId)
    plan.plan_state = int(planState)
    plan.approve_time = datetime.now()
    plan.approver_id = current_user.id
    Plan.insert_plan(plan)
    current_app.logger.warning(u'操作者：%d,专家修改审核状态%s', current_user.id, planId)
    count = Plan.search_checkedCount(current_user.role_id)
    session['checkedPlanCount'] = count
    return jsonify({'state': 1})


@main.route('/report/<moduleName>')
@login_required
def report(moduleName):
    session['planId'] = None
    plans = Plan.search_by_module(moduleName)
    plans_distinct = Plan.search_distinct_user()
    companys = Company.search_company()
    users = User.select_all()
    if moduleName == Module.coalCHP:
        for plan in plans:
            if plan.main_equipment_para is None:
                plan.main_equipment_para = ToCoalCHP().getMainEquipmentPara(plan.id)
                Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
        session['menuSelect'] = "coalCHPreport"
    elif moduleName == Module.biomassCHP:
        for plan in plans:
            if plan.main_equipment_para is None:
                plan.main_equipment_para = ToBiomassCHP().getMainEquipmentPara(plan.id)
                Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
        session['menuSelect'] = "biomassreport"
    elif moduleName == Module.CCPP:
        # 更新ccpp中每条方案的主要设备参数字段
        for plan in plans:
            if plan.main_equipment_para is None:
                plan.main_equipment_para = CcppCalculateService().getMainEquipmentPara(plan.id)
                Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
        session['menuSelect'] = "ccppreport"
    elif moduleName == Module.gasPowerGeneration:
        for plan in plans:
            if plan.main_equipment_para is None:
                plan.main_equipment_para = ToGPG().getMainEquipmentPara(plan.id)
                Plan.autoupdata_plan(plan)
            plan.main_equipment_para_list = MainService.splitStringToList(plan.main_equipment_para, '\n')
        session['menuSelect'] = "gpgreport"
    elif moduleName == Module.energyIsland:
        session['menuSelect'] = "energyIslandreport"
    session['moduleName'] = moduleName
    
    return render_template(
        'page/reportList.html',
        plans=plans,
        companys=companys,
        users=users,
        plans_distinct=plans_distinct,
        moduleName=moduleName,
        pageFlag="report")


@main.route('/prepreviewdealwith', methods=['POST'])
@login_required
def prepreviewdealwith():
    planId = request.form.get('planId')
    try:
        reportTemplate = TemplateDealwithService().templateDealwithMian(planId, current_user.id)
    except UnicodeDecodeError as e:
        current_app.logger.error(u'操作者：%d,预览解析模板编码出现问题啦，快找服务器管理员。!%s', current_user.id, e.message)
        return jsonify({'mdcontent': None, 'exceptionInfo': u"编码出现问题啦，快找服务器管理员。"})
    except MyException as e:
        current_app.logger.error(u'操作者：%d, %s, %s', (current_user.id, e.exceptioninfoforself, e.message))
        print(e.exceptionName, e.exceptioninfoforself)
        return jsonify({'mdcontent': None, 'exceptionInfo': e.exceptioninfoforkh})
    else:
        return jsonify({'mdcontent': reportTemplate, 'exceptionInfo': None})


@main.route('/gethtmlandmd', methods=['POST'])
@login_required
def gethtmlandmd():
    planId = request.form.get('planId')
    plan = Plan.search_planById(planId)
    htmlcontent = request.form.get('htmlcontent')
    mdcontent = request.form.get('mdcontent')
    plan.plan_report_content = mdcontent
    plan.plan_report_html = htmlcontent
    Plan.insert_plan(plan)
    return jsonify({'state': 1})


# 编辑方案内容页面按下预览按钮打开预览页面
@main.route('/converMD/<planId>')
@login_required
def converMD(planId):
    plan = Plan.search_planById(planId)
    return render_template(
        'page/converttToc.html', menuSelect='ccppFurnace', plan=plan)


# 编辑方案内容页面按下预览按钮打开预览页面初始化加载页面数据
@main.route('/initializeMD', methods=['POST'])
@login_required
def initializeMD():
    planId = request.form.get('planId')
    plan = Plan.search_planById(planId)
    tempFile(plan.plan_report_content.encode("utf-8"),
             plan.plan_report_html.encode("utf-8"),
             planId, current_user.id)
    titles = ganMenu(planId, current_user.id)
    data = {}
    data['tbFuncDic'] = titles
    anchorMarkHtml = addAnchorMark(titles, planId, current_user.id)
    return jsonify({'data': data, "html": anchorMarkHtml})


# ###################  模板管理template_report.html  ########################################
@main.route('/getTemplateByModule', methods=['POST'])
@login_required
def getTemplateByModule():
    moduleName = session.get('moduleName')
    # plan = Plan.search_planById(planId)
    # moduleName = plan.module_id
    reportTemplatelist = ReportTemplate.search_by_module(moduleName)
    reportTemplateJson = []
    for retemplate in reportTemplatelist:
        data_format = {
            "template_id": retemplate.id,
            "template_name": retemplate.template_name
        }
        reportTemplateJson.append(data_format)
    return jsonify({'reportTemplateJson': reportTemplateJson})


@main.route('/setPlanReportTemplate', methods=['POST'])
@login_required
def setPlanReportTemplate():
    planId = session.get('planId')
    template_id = request.values.get('template_id')
    # template_name = request.values.get('template_name')
    plan = Plan.search_planById(planId)
    plan.template_id = template_id
    plan.plan_state = 0
    Plan.insert_plan(plan)
    count = Plan.search_checkedCount(current_user.role_id)
    session['checkedPlanCount'] = count
    return jsonify({'message': '成功选择方案模板!'})


@main.route('/getColumnNameByTable', methods=['POST'])
@login_required
def getColumnNameByTable():
    tableName = request.values.get('tableName')
    # print(tableName)
    columnNameJson = {}
    columnNameJson = MainService.toColumnNameJson(tableName)
    print(columnNameJson)
    return jsonify({'columnNameJson': columnNameJson})


@main.route('/getTableNameByModule', methods=['POST'])
@login_required
def getTableNameByModule():
    moduleName = session.get('moduleName')
    tableNameJson = []
    tableNameJson = MainService.toTableNameJson(moduleName)
    return jsonify({'tableNameJson': tableNameJson})


@main.route('/getLogicByModule', methods=['POST'])
@login_required
def getLogicByModule():
    moduleName = session.get('moduleName')
    logicJson = []
    logicJson = MainService.getlogicJson(moduleName)
    return jsonify({'logicJson': logicJson})


# 进入模板管理(列表)
@main.route('/templatelist/<moduleName>')
@login_required
def templatelist(moduleName):
    templates = ReportTemplate.search_by_module_userid(moduleName)
    if moduleName == Module.coalCHP:
        session['menuSelect'] = "coalCHPreporttemplateList"
    elif moduleName == Module.biomassCHP:
        session['menuSelect'] = "biomassreporttemplateList"
    elif moduleName == Module.CCPP:
        session['menuSelect'] = "ccppreporttemplateList"
    elif moduleName == Module.gasPowerGeneration:
        session['menuSelect'] = "gpgreporttemplateList"
    elif moduleName == Module.energyIsland:
        session['menuSelect'] = "energyIslandtemplateList"

    session['moduleName'] = moduleName
    users = User.select_all()
    return render_template(
        'page/template_list.html',
        templates=templates,
        moduleName=moduleName,
        users=users,
        pageFlag="template")


# 创建模板
@main.route('/creattemplate', methods=['GET'])
@login_required
def creattemplate():
    moduleName = session.get('moduleName')
    session['action'] = 'add'
    return render_template(
        'page/edit_template_report.html',
        moduleName=moduleName,
        pageFlag="creattemplate")


# 编辑模板
@main.route('/edittemplate/<templateId>')
@login_required
def edittemplate(templateId):
    session['action'] = 'edit'
    moduleName = session.get('moduleName')
    if moduleName:
        return render_template(
            'page/edit_template_report.html',
            templateId=templateId,
            pageFlag="edittemplate")
    return redirect(url_for("main.index"))


# copy模板
@main.route('/copytemplate/<templateId>')
@login_required
def copytemplate(templateId):
    session['action'] = 'add'
    moduleName = session.get('moduleName')
    if moduleName:
        return render_template(
            'page/edit_template_report.html',
            templateId=templateId,
            pageFlag="edittemplate")
    return redirect(url_for("main.index"))


# 初始化编辑模板页面数据
@main.route('/initTemplate', methods=['POST'])
@login_required
def initTemplate():
    templateId = request.form.get('templateId')
    reportTemplate = ReportTemplate.search_templateById(
        int(templateId) if templateId != '' and templateId is not None else 0)
    if reportTemplate:
        menu = json.loads(reportTemplate.template__left_menu, strict=False)
        template_name = reportTemplate.template_name
        contents = json.loads(reportTemplate.template_left_content, strict=False)
        return jsonify({
            'state': '1',
            "menu": menu,
            "template_name": template_name,
            "contents": contents
        })
    return jsonify({'state': '0'})


# 保存模板
@main.route('/savetemplate', methods=['POST'])
@login_required
def savetemplate():
    if request.method == 'POST':
        templateName = request.form.get('template_name')
        templateId = request.form.get('templateId')
        moduleName = session.get('moduleName')
        teportTemplatelist = ReportTemplate.search_templateNamelist(templateName)
        templateIdList = []
        for trp in teportTemplatelist:
            templateIdList.append(str(trp.id))
        userid = current_user.id
        action = session.get('action')
        if action == 'add':
            if len(templateIdList) != 0:
                return jsonify({'state': '3'})
            else:
                templateId = None
        else:
            if templateId in templateIdList and len(templateIdList) == 1 or len(templateIdList) == 0:
                pass
            else:
                return jsonify({'state': '3'})
        session['action'] = 'edit'
        contents = request.form.get('content')
        menu = request.form.get('menu')
        md = createMD(json.loads(menu), json.loads(contents))
        reportTemplate = ReportTemplate.search_templateById(
            int(templateId) if templateId != '' and templateId is not None else 0)
        if reportTemplate is None:
            reportTemplate = ReportTemplate.search_templateByNameAndUserId(templateName, userid, moduleName)
        # 模板名称
        reportTemplate.template_name = templateName
        # md内容
        reportTemplate.template_content = md
        # meun
        reportTemplate.template__left_menu = menu
        # meun内容
        reportTemplate.template_left_content = contents
        # 所属模块
        reportTemplate.module_id = session.get('moduleName')
        # 创建者
        reportTemplate.user_id = current_user.id
        ReportTemplate.insert_template(reportTemplate)
        template = ReportTemplate.search_templateName(templateName)
        return jsonify({'state': '1', 'md': md, 'templateId': template.id})
    return jsonify({'state': '0'})


@main.route('/deleteTemplate', methods=['POST'])
@login_required
def deleteTemplate():
    templateId = request.values.get('templateId')
    moduleName = request.values.get('moduleName')
    template = ReportTemplate.search_templateById(templateId)
    if template is not None:
        # if User.search_userById(template.user_id).id != current_user.id:
        #     return jsonify({'state': '1', 'massage': u'不能删除别人创建的模板！'})
        planlist = Plan.search_planBytemplateId(templateId)
        if len(planlist) != 0:
            return jsonify({'state': '1', 'massage': u'该模板正在被使用，无法删除！'})
        else:
            ReportTemplate.delete_Template(templateId)
            users = User.select_all()
            userJson = MainService.to_userJson(users)
            templateList = ReportTemplate.search_by_module_userid(moduleName)
            templateListJson = MainService.to_templateJson(templateList)
            current_app.logger.warning(u'操作者：%d,deleteTemplate%s', current_user.id, templateId)
            return jsonify({
                'templateListJson': templateListJson,
                'users': userJson,
                'state': '0', 'massage': u'模板删除成功！'
            })
    else:
        return jsonify({'state': '-1', 'massage': u'模板已被删除，尝试刷新页面！'})


@main.route('/queryTemplate', methods=['POST'])
@login_required
def queryTemplate():
    template_name = request.values.get('template_name')
    user_name = request.values.get('user_name')
    moduleName = request.values.get('moduleName')
    templates = ReportTemplate.search_templateByNameAndUser(template_name, user_name, moduleName)
    templateListJson = MainService.to_templateJson(templates)
    users = User.select_all()
    userJson = MainService.to_userJson(users)
    return jsonify({
        'templateListJson': templateListJson,
        'users': userJson
    })
# ###################  markdown-docx  ########################################


@main.route('/editPlanReport/<int:planId>')
@login_required
def editPlanReport(planId):
    plan = Plan.search_planById(planId)
    planCopy = copy.deepcopy(plan)
    moduleName = planCopy.module_id
    companys = Company.search_company()
    if planCopy.plan_report_content is None:
        if moduleName is not None:
            planCopy.plan_report_content = MainService.findMDTemplate(moduleName, planId)
        else:
            planCopy.plan_report_content = u"未找到模板"
    return render_template(
        'page/editPlanReport.html',
        plan=planCopy,
        companys=companys)


# 文件上传
@main.route('/upload_file', methods=['POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.getcwd(), config['imgConfig'].MAIN_IMG_PATH, filename))
            return jsonify({'data': GetPath.getImgMainNet(filename), 'state': '0', 'message': '上传成功!'})
        return jsonify({'data': GetPath.getImgMainNet(filename), 'state': '1', 'message': '上传失败!'})


# 文件下载
@main.route("/download_file/<planId>", methods=['GET'])
@login_required
def download_file(planId):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    dirpath = os.path.join(os.getcwd(), config['markToDocx'].MAIN_OUTFILE_FOR_DOWNLOAD_DOCX_PATH)
    # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    filename = GetPath.getDocxTemplateResultFilename(planId, current_user.id)
    return send_from_directory(dirpath, filename, as_attachment=True)
    # as_attachment=True 一定要写，不然会变成打开，而不是下载


# 文件预览
@main.route('/uploaded_file/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(
        os.path.join(os.getcwd(), config['imgConfig'].MAIN_IMG_PATH, ""), filename)


# 文件转换调用，开启线程
@main.route('/convertHtmltoDocx', methods=['POST'])
def convertHtmltoDocx():
    planId = request.form.get('planId')
    current_app.logger.warning(u'操作者：%d,文件转换调用，为方案%s开启线程', current_user.id, planId)
    # 恢复文件
    plan = Plan.search_planById(planId)
    thr = threading.Thread(
        target=convertdel, args=[planId, current_user.id, plan.plan_report_content.encode("utf-8"), plan.plan_report_html.encode("utf-8")])
    thrname = str(int(round(time.time() * 1000)))
    session['convertHtmltoDocxstate'] = thrname
    thr.setName(thrname)
    thr.start()
    return jsonify({'filename': '1.docx', 'state': '0', 'message': '转换成功!'})


# 文本保存
@main.route('/saveMd', methods=['POST'])
@login_required
def saveMd():
    if request.method == 'POST':
        textarea = request.form.get('flask-pagedown-body')
        htmldata = request.form.get('htmldata')
        planId = request.form.get('planId')
        plan = Plan.search_planById(planId)
        if plan is not None:
            plan.plan_report_content = textarea
            plan.plan_report_html = htmldata
            Plan.insert_plan(plan)
            return jsonify({'state': '1', 'message': '保存成功!'})
    return jsonify({'state': '0', 'message': '保存失败!'})


# 只保存左侧md内容
@main.route('/saveContent', methods=['POST'])
@login_required
def saveContent():
    if request.method == 'POST':
        textarea = request.form.get('flask-pagedown-body')
        planId = request.form.get('planId')
        plan = Plan.search_planById(planId)
        if plan is not None:
            plan.plan_report_content = textarea
            Plan.insert_plan(plan)
            return jsonify({'state': '1'})
    return jsonify({'state': '0'})


# 从首页地图创建新方案
# 必要条件： 用户需先登录
@main.route('/new_project', methods=['POST'])
@login_required
def new_project():
    state = 1
    module_name = request.values.get('module_name')
    planName = request.values.get('plan_name')
    if planName is not None:
        planName = planName.strip()
    companyName = request.values.get('company_name')
    if companyName is not None:
        companyName = companyName.strip()
    companyLocation = request.values.get('company_location')
    if companyLocation is not None:
        companyLocation = companyLocation.strip()
    company_lnglat = request.values.get('company_lnglat')
    planId = None
    # 判断数据库中是否有相同的方案名的方案
    plan = Plan.search_planByParams(companyName, '', module_name)
    # 数据库存在则不做操作直接给用户提示
    # 避免取到重名覆盖掉原来的数据
    if plan:
        state = "0"
    else:
        if module_name == Module.coalCHP:
            planId = ToCoalCHP.create_plan(companyName, planName, companyLocation, company_lnglat)
            MainService.getEquipmentTemplate(planId, module_name)
        elif module_name == Module.biomassCHP:
            planId = ToBiomassCHP.create_plan(companyName, planName, companyLocation, company_lnglat)
            MainService.getEquipmentTemplate(planId, module_name)
        elif module_name == Module.CCPP:
            questionnaire = QuestionService().submitQuestionnaire(None, companyName, planName, companyLocation, None, company_lnglat)
            planId = questionnaire.plan_id
            MainService.getEquipmentTemplate(planId, module_name)
        elif module_name == Module.gasPowerGeneration:
            planId = ToGPG.create_plan(companyName, planName, companyLocation, company_lnglat)
            MainService.getEquipmentTemplate(planId, module_name)
        elif module_name == Module.energyIsland:
            planId = EnergyIslandService().create_plan(companyName, planName, companyLocation, company_lnglat)
            
        session['planId'] = planId
        session['moduleName'] = module_name
    return jsonify({'state': state})


# 从首页地图获取所有方案的经纬度
# 必要条件： 用户需先登录
@main.route('/planLngLats', methods=['GET'])
@login_required
def planLngLats():
    plans = Plan.search_plan_all()
    lngLats = MainService.getLngLats(plans)
    autoComplete = MainService.getComplete()
    return jsonify({'lngLats': lngLats, 'autoCompletes': autoComplete})


# 从首页地图关键字查询符合的结果
# 必要条件： 用户需先登录
@main.route('/getKeyResult', methods=['POST'])
@login_required
def getKeyResult():
    keywords = request.values.get('keywords')
    keywordResults = MainService.getKeywordResults(keywords)
    return jsonify({'keywordResults': keywordResults})


# 获得转换word状态
@main.route('/getConvertHtmltoDocxState', methods=['POST'])
@login_required
def getConvertHtmltoDocxState():
    for thread in threading.enumerate():
        if thread.getName() == session.get('convertHtmltoDocxstate') and thread.isAlive():
            current_app.logger.warning(u'操作者：%d,获得转换word状态%d', current_user.id, 1)
            return jsonify({'convertHtmltoDocxSate': "1"})
    ccppresult_path = GetPath.getDocxTemplateResult(request.values.get('planId'), current_user.id)
    current_app.logger.warning(ccppresult_path)
    if os.path.exists(ccppresult_path):
        current_app.logger.warning(u'操作者：%d,获得转换word状态%d', current_user.id, 0)
        return jsonify({'convertHtmltoDocxSate': "0"})
    else:
        current_app.logger.warning(u'操作者：%d,获得转换word状态%d但是文件没有生成！！！！！！', current_user.id, 1)
        return jsonify({'convertHtmltoDocxSate': "1"})


# 燃料维护
@main.route('/biomassFuelMaintain')
@login_required
def biomassFuelMaintain():
    biomassCHPComponent = BiomassCHPFuelComponent.search_biomassCHPComponent()
    session['menuSelect'] = "biomassFuelMaintain"
    return render_template(
        'page/fuelMaintain.html',
        fuelsort=biomassCHPComponent)


# 选择燃料
@main.route('/fuelSort', methods=['POST'])
@login_required
def fuelSort():
    id = request.values.get('id')
    datas = ToBiomassCHP.to_fuelCHPComponentJson2(id)
    return jsonify({'fuelSort': datas})


# 保存新增或修改后的燃料数据
@main.route('/biomassFuelMaintainSave', methods=['POST'])
@login_required
def biomassFuelMaintainSave():
    fuelData = ToBiomassCHP.to_fuel(request.form)
    BiomassCHPFuelComponent.insert_biomassCHPComponent(fuelData)
    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})


# 保存后刷新数据
@main.route('/initFuel', methods=['POST'])
@login_required
def initFuel():
    # initData = BiomassCHPFuelComponent.search_biomassCHPSort("1")

    initData = ToBiomassCHP.to_fuelCHPComponentJson2("1")

    return jsonify({'fuelInit': initData})    
