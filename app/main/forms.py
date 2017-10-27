# -*- coding: utf-8 -*-
import re
from flask_wtf import FlaskForm as FlaskForm
from wtforms import StringField, SelectField,\
    SubmitField, PasswordField
from wtforms.validators import Required, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User
from flask_login import current_user


# 用户更改个人信息表单
# 属性：tel 电话，submit 提交
class EditProfileForm(FlaskForm):
    tel = StringField(
        u'电话号码', validators=[Required(), Length(11), Regexp('^[0-9]*$')])
    submit = SubmitField(u'提交')


# 管理员更改用户信息表单
# 属性：username 用户名，confirmed 是否认证账户，role 用户类型，tel 电话，
#       submit 提交
class EditProfileAdminForm(FlaskForm):
    username = StringField(
        u'用户名',
        validators=[
            Required(), Length(1, 64),
            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                   'Usernames must have only letters, '
                   'numbers, dots or underscores')
        ])
    role = SelectField(u'类型', coerce=int)
    tel = StringField(
        u'电话号码', validators=[Required(), Length(11), Regexp('^[0-9]*$')])
    submit = SubmitField(u'提交')

    # 初始化表单，添加性别选项
    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.user = user

    # 验证用户名
    def validate_user_name(self, field):
        if field.data != self.user.user_name and \
                User.query.filter_by(user_name=field.data).first():
            raise ValidationError(u'该用户名已被注册.')


# 用户更改密码表单
class ChangePasswordForm(FlaskForm):
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


# 用户更改邮箱表单
class ChangeEmailForm(FlaskForm):
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


# 用户注册表单
class UpdateUserForm(FlaskForm):
    '''
    管理员修改页面的表单
    '''
    role_id = SelectField(
        u'角色',
        # choices=[(1, u'管理员'), (2, u'专家'), (3, u'用户')],
        choices=[(1, u'管理员'), (3, u'用户')],
        coerce=int)

    submit = SubmitField(u'修改用户信息')


# 用户注册表单
class RegistrationForm(FlaskForm):
    '''
    用户登录页面的表单
    user_email 邮箱
    user_name 用户名
    password 密码
    password2 确认密码
    '''
    # 邮箱
    user_email = StringField(
        u'邮箱',
        validators=[
            Required(u'此输入框是必填项'), Regexp(
                '^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$',
                0, u'请输入正确邮箱')
        ])
    # 用户名
    user_name = StringField(u'用户名', validators=[Required(u'此输入框是必填项')])
    # user_eid = StringField(
    #     u'员工号', validators=[Required(u'此输入框是必填项'), Regexp('^[0-9]{1,20}$', 0, u'请输入1-20位数字')])
    # 密码
    password = PasswordField(
        u'密码',
        validators=[
            Required(u'此输入框是必填项'), Regexp('^[a-zA-Z0-9]{6,10}$', 0,
                                          u'请输入6-10位数字，字母')
        ])
    # 确认密码
    password2 = PasswordField(
        u'确认密码',
        validators=[
            Required(u'此输入框是必填项'), EqualTo('password', message=u'密码不一致')
        ])

    role_id = SelectField(
        u'角色',
        # choices=[(1, u'管理员'), (2, u'专家'), (3, u'用户')],
        choices=[(1, u'管理员'), (3, u'用户')],
        coerce=int)
 
    # user_tel = StringField(
    #     u'电话',
    #     validators=[Required(u'此输入框是必填项'), Regexp('^[0-9]{8,11}$', 0, u'请输入8到11位电话')])
    # gender = SelectField(
    #     u'性别',
    #     choices=[(Sex.MALE, u'男'), (Sex.FEMALE, u'女'), (Sex.OTHER, u'其他')],
    #     coerce=int)
    submit = SubmitField(u'添加用户')

    # 验证邮箱
    def validate_user_email(self, field):
        '''
        验证用户注册邮箱是否被注册
        '''
        if User.query.filter_by(user_email=field.data).first():
            raise ValidationError(u'此邮箱已被注册')

    # 验证用户名
    def validate_user_name(self, field):
        '''
        验证该用户名是否符合规范
        用户名格式：限4-16个字符，支持中英文、数字、下划线
        验证该用户名是否被注册
        '''
        if re.findall(u'[\u4e00-\u9fa5_a-zA-Z0-9]{4,16}', field.data):
            if User.query.filter_by(user_name=field.data).first():
                raise ValidationError(u'此用户名已被注册')
        else:
            raise ValidationError(u'用户名格式：限4-16个字符，支持中英文、数字、下划线')

    # # 验证员工号
    # def validate_user_eid(self, field):
    #     if User.query.filter_by(user_eid=field.data).first():
    #         raise ValidationError(u'此员工号已被注册')

    # # 验证电话号码
    # def validate_user_tel(self, field):
    #     if User.query.filter_by(user_tel=field.data).first():
    #         raise ValidationError(u'电话号码已被注册')
