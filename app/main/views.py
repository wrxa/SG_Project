# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, redirect, url_for, flash,\
    abort, jsonify, request
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, ChangePasswordForm,\
    ChangeEmailForm, UpdateUserForm, RegistrationForm
from .. import db
from ..models import User, CoalCHPComponent, CoalCHPConstant,\
    CoalCHPNeedsQuestionnaire
from ..decorators import admin_required
from coalService import ToCoalCHP


# 显示主页
# 必要条件：用户需先登录
# Returns：返回主页面
@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # return render_template('index.html')
    return render_template('index.html', menuSelect='collapsed index')


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
    return render_template('page/manage_user.html', users=users)


# delete_user
@main.route('/delete_user/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    User.delete_user(user)
    flash(u'用户删除成功', 'success')
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
        return redirect(url_for('main.list_user'))
    user_name = user.user_name
    user_email = user.user_email
    form.role_id.data = user.role_id
    return render_template(
        "page/admin_edit_user.html",
        form=form,
        name=user_name,
        email=user_email)


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


# ######################燃煤热电联产例子 start ####################
@main.route('/coalQuestionnaire')
@login_required
def coalQuestionnaire():
    coalCHPComponent = CoalCHPComponent.search_coalCHPComponent()
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_questionnaire")
    return render_template(
        'page/coalCHP/coalQuestionnaire.html',
        menuSelect='coalQuestionnaire',
        coalsort=coalCHPComponent,
        constants=coalCHPConstant)


@main.route('/coalSort', methods=['POST'])
@login_required
def coalSort():
    id = request.values.get('id')
    datas = {}
    coalCHPComponent = CoalCHPComponent.search_coalCHPSort(id)
    datas['carbon'] = coalCHPComponent.carbon
    datas['hydrogen'] = coalCHPComponent.hydrogen
    datas['oxygen'] = coalCHPComponent.oxygen
    datas['nitrogen'] = coalCHPComponent.nitrogen
    datas['sulfur'] = coalCHPComponent.sulfur
    datas['water'] = coalCHPComponent.water
    datas['grey'] = coalCHPComponent.grey
    datas['daf'] = coalCHPComponent.daf
    datas['grindability'] = coalCHPComponent.grindability
    datas['low'] = coalCHPComponent.low

    return jsonify({'coalSort': datas})


@main.route('/formData', methods=['POST'])
@login_required
def formData():
    companyName = request.form.get('company_name')
    companyLocation = request.form.get('company_location')

    plan_id = ToCoalCHP.create_plan(companyName, companyLocation)

    questionnaire = ToCoalCHP.to_questionnaire(request.form, plan_id)

    CoalCHPNeedsQuestionnaire.insert_questionnaire(questionnaire)

    datas = {}
    datas['carbon'] = "77777"

    return jsonify({'coalSort': datas})


@main.route('/coalFurnace')
@login_required
def coalFurnace():
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_furnaceCalculation")
    return render_template(
        'page/coalCHP/coalFurnace.html',
        menuSelect='coalFurnace',
        constants=coalCHPConstant)


@main.route('/coalSteamTurbine')
@login_required
def coalSteamTurbine():
    return render_template(
        'page/coalCHP/coalSteamTurbine.html', menuSelect='coalSteamTurbine')


@main.route('/coalHandingSystem')
@login_required
def coalHandingSystem():
    coalHandingSystemConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_CoalHandingSystem")
    return render_template(
        'page/coalCHP/coalHandingSystem.html',
        menuSelect='coalHandingSystem',
        constants=coalHandingSystemConstant)
# ##################燃煤热电联产 end##################


# ##############生物质热电联产例子 start###############
@main.route('/biomassQuestionnaire')
@login_required
def biomassQuestionnaire():
    coalCHPComponent = CoalCHPComponent.search_coalCHPComponent()
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_questionnaire")
    return render_template(
        'page/BiomassCHP/biomassQuestionnaire.html',
        menuSelect='biomassQuestionnaire',
        coalsort=coalCHPComponent,
        constants=coalCHPConstant)


@main.route('/biomassSteamTurbine')
@login_required
def biomassSteamTurbine():
    return render_template(
        'page/BiomassCHP/biomassSteamTurbine.html',
        menuSelect='biomassSteamTurbine')


@main.route('/biomassFurnace')
@login_required
def biomassFurnace():
    return render_template(
        'page/BiomassCHP/biomassFurnace.html', menuSelect='biomassFurnace')

# ########################生物质热电联产 end#################################


# ##############ccpp例子 start###############
@main.route('/ccppQuestionnaire')
@login_required
def ccppQuestionnaire():
    coalCHPComponent = CoalCHPComponent.search_coalCHPComponent()
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant(
        "coalCHP_questionnaire")
    return render_template(
        'page/CCPP/ccppQuestionnaire.html',
        menuSelect='ccppQuestionnaire',
        coalsort=coalCHPComponent,
        constants=coalCHPConstant)


@main.route('/ccppFurnace')
@login_required
def ccppFurnace():
    return render_template(
        'page/CCPP/ccppFurnace.html', menuSelect='ccppFurnace')


@main.route('/ccppSteamTurbine')
@login_required
def ccppSteamTurbine():
    return render_template(
        'page/CCPP/ccppSteamTurbine.html', menuSelect='ccppSteamTurbine')

# ########################ccpp end#################################


@main.route('/subPages3')
@login_required
def subPages3():
    return render_template('page/elements.3.html', menuSelect='elements3')


@main.route('/elements')
@login_required
def elements():
    return render_template('page/elements.html', menuSelect='elements')


@main.route('/charts')
@login_required
def charts():
    return render_template('page/charts.html', menuSelect='charts')


@main.route('/tables')
@login_required
def tables():
    return render_template('page/tables.html', menuSelect='tables')


@main.route('/typography')
@login_required
def typography():
    return render_template('page/typography.html', menuSelect='typography')


@main.route('/icons')
@login_required
def icons():
    return render_template('page/icons.html', menuSelect='icons')
