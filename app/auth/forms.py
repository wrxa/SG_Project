# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm as Form
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Required, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


# 用户登录表单
class LoginForm(Form):
    '''
    用户登录页面的表单
    email 邮箱
    password 密码
    remember_me 是否记住密码
    '''
    # 邮箱
    email = StringField(
        u'邮箱',
        validators=[
            Required(u'此输入框是必填项'), Regexp(
                '^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$',
                0, u'请输入正确邮箱')
        ],
        render_kw={"placeholder": u"邮箱"})
    # 密码
    password = PasswordField(u'密码', validators=[Required(u'此输入框是必填项')])
    # 是否下次自动登录
    remember_me = BooleanField(u'下次自动登录')
    submit = SubmitField(u'登录')


# 用户更改密码表单
class ChangePasswordForm(Form):
    '''
    用户更改密码表单
    old_password 旧密码
    password 新密码
    password2 确认新密码
    '''
    # 原始密码
    old_password = PasswordField(u'请输入密码', validators=[Required(u'此输入框是必填项')])
    # 新密码
    password = PasswordField(u'新密码', validators=[Required(u'此输入框是必填项')])
    # 确认新密码
    password2 = PasswordField(
        u'确认新密码',
        validators=[
            Required(u'此输入框是必填项'), EqualTo('password', message=u'密码不一致')
        ])
    submit = SubmitField(u'更改密码')


# 用户找回密码请求表单
class PasswordResetRequestForm(Form):
    '''
    用户找回密码请求表单
    email 用户邮箱
    '''
    # 邮箱
    email = StringField(
        u'邮箱',
        validators=[
            Required(u'此输入框是必填项'), Regexp(
                '^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$',
                0, u'请输入正确邮箱')
        ])
    submit = SubmitField(u'重置密码')


# 用户重置密码表单
class PasswordResetForm(Form):
    '''
    用户重置密码表单
    email 用户邮箱
    password 新密码
    password2 确认新密码
    '''
    # 邮箱
    email = StringField(
        u'邮箱',
        validators=[
            Required(u'此输入框是必填项'), Regexp(
                '^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$',
                0, u'请输入正确邮箱')
        ])
    # 重置密码
    password = PasswordField(
        u'新密码',
        validators=[
            Required(u'此输入框是必填项'), EqualTo('password2', message=u'密码不一致')
        ])
    # 确认重置密码
    password2 = PasswordField(u'确认新密码', validators=[Required(u'此输入框是必填项')])
    submit = SubmitField(u'重置密码')

    # 验证邮箱
    def validate_email(self, field):
        '''
        重置密码时验证邮箱
        验证邮箱是否能查到
        '''
        if User.query.filter_by(user_email=field.data).first() is None:
            raise ValidationError(u'无法识别此邮箱')


# 用户更改邮箱表单
class ChangeEmailForm(Form):
    '''
    用户更改邮箱表单
    email 用户邮箱
    password 用户密码
    '''
    # 新邮箱
    email = StringField(
        u'新邮箱',
        validators=[
            Required(u'此输入框是必填项'), Length(1, 64), Regexp(
                '^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$',
                0, u'请输入正确邮箱')
        ])
    # 密码
    password = PasswordField(u'密码', validators=[Required(u'此输入框是必填项')])
    submit = SubmitField(u'更新邮箱')

    # 验证邮箱
    def validate_email(self, field):
        '''
        在修改邮箱时验证邮箱
        邮箱与原邮箱相比是否有变化
        此邮箱是否已经被注册
        '''
        if current_user.user_email == field.data:
            raise ValidationError(u'邮箱与原邮箱相比未做更改')
        elif User.query.filter_by(user_email=field.data).first():
            raise ValidationError(u'此邮箱已被注册')
