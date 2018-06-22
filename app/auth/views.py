# -*- coding: utf-8 -*-
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm


# 用户登录
# Returns: 返回登录页面；若用户提交登录表单，返回主页；
@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    用户提交登录表单
    登录成功进入主页，登录失败则留在登陆页面
    '''
    form = LoginForm()
    if form.validate_on_submit():
        # user = User.query.filter_by(user_email=form.email.data).first()
        user = User.query.filter_by(user_eid=form.user_eid.data).first()
        # 如果信息对称则登录用户
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(u'工号或密码不正确', 'danger')
    return render_template('auth/page-login.html', form=form)


# 用户登出
# Returns: 返回主页
@auth.route('/logout')
@login_required
def logout():
    '''
    用户点击[登出]按钮后注销用户浏览器当前信息
    并返回到登陆页
    '''
    logout_user()
    flash(u'您已登出', 'info')
    return redirect(url_for('main.index'))
