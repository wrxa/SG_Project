# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import db
from . import login_manager
from datetime import datetime


# 用户种别
class Permission:
    # 查询
    QUERY = 0x01
    # 审核
    REVIEW = 0x02
    # 管理
    ADMINISTER = 0x80


# 公司表
class Company(db.Model):
    # 表名
    __tablename__ = 'company'
    __table_args__ = {'comment': u'客户信息'}

    # 公司ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 公司名称
    company_name = db.Column(db.String(200), comment=u"客户单位名称")
    # 公司性质
    company_nature = db.Column(db.String(200), comment=u"")
    # 备注
    remarks = db.Column(db.Text(), comment=u"")

    # 初始化公司表
    @staticmethod
    def init_company():
        company = Company(
            company_name=u'陕鼓动力分布式小组', company_nature=u'陕鼓分公司', remarks='国企')
        db.session.add(company)
        db.session.commit()

    def __init__(self, **kwargs):
        super(Company, self).__init__(**kwargs)

    # 新增公司
    @staticmethod
    def insert_company(company):
        try:
            db.session.add(company)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update company<id=%s>" % (company.id))

    # 查询当前用户的所有方案
    @staticmethod
    def search_company():
        result = Company.query.all()
        return result

    # 通过companyId查询公司信息
    @staticmethod
    def search_companyById(companyId):
        result = Company.query.filter_by(id=companyId).one_or_none()
        return result

    # 通过companyName查询公司信息
    @staticmethod
    def search_companyByName(companyName):
        company = Company.query.filter_by(
            company_name=companyName).one_or_none()
        return company


# 方案文本逻辑表
class Textlogic(db.Model):
    # 表名
    __tablename__ = 'textlogic'
    __table_args__ = {'comment': u'方案文本逻辑表'}

    # 文本逻辑ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 文本逻辑键
    textlogickey = db.Column(db.String(200))
    # 文本逻辑代码
    textlogicvalue = db.Column(db.Text())
    # 文本逻辑描述
    textlogicremarks = db.Column(db.Text())
    # 模块name(燃煤热电联产：1、生物质热电：2、煤气发电：3、燃气蒸汽联合循环(ccpp)：4)
    module_name = db.Column(db.String(200), index=True)
    # 模板id(预留字段)
    template_id = db.Column(db.Integer)
    # 方案id(预留字段)
    plan_id = db.Column(db.Integer)

    @staticmethod
    def create_constant(textlogickey, textlogicvalue, textlogicremarks, module_name):
        textlogic = Textlogic()
        textlogic.textlogickey = textlogickey
        textlogic.textlogicvalue = textlogicvalue
        textlogic.textlogicremarks = textlogicremarks
        textlogic.module_name = module_name
        return textlogic

    @staticmethod
    def insert_constant(textlogic):
        try:
            db.session.add(textlogic)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update textlogic<id=%s, module_name=%s>" %
                  (textlogic.id, textlogic.module_name))

    # 查询所有逻辑
    @staticmethod
    def search_logic_all():
        result = Textlogic.query.all()
        return result

    # 按模块查询所有模板
    @staticmethod
    def search_by_module(moduleName):
        result = Textlogic.query.filter_by(module_name=moduleName).all()
        return result


# 模板表
class ReportTemplate(db.Model):
    # 表名
    __tablename__ = 'report_template'
    # 模板ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 模板名称
    template_name = db.Column(db.String(200), index=True)
    # 模块id(燃煤热电联产：1、生物质热电：2、煤气发电：3、燃气蒸汽联合循环(ccpp)：4)
    module_id = db.Column(db.String(200), index=True)
    # 创建人(用户表主键)
    user_id = db.Column(db.Integer())
    # 模板创建时间
    template_create_date = db.Column(db.DateTime, nullable=False)
    # 模板修改时间
    template_update_date = db.Column(db.DateTime, nullable=False)
    # 模板状态(0创建完成，1创建中)
    template_state = db.Column(db.Integer, default=0)
    # 报告左meun
    template__left_menu = db.Column(db.Text())
    # 报告左menu内容
    template_left_content = db.Column(db.Text())
    # 报告预留字段
    template_reserve = db.Column(db.Text())
    # 报告md内容
    template_content = db.Column(db.Text())
    # 模板地址
    template_location = db.Column(db.String(200))

    def __init__(self, **kwargs):
        super(ReportTemplate, self).__init__(**kwargs)

    @staticmethod
    def create_constant(template_name, module_id, user_id, template_create_date,
                        template_update_date, template__left_menu,
                        template_state, template_left_content, template_content):
        reportTemplate = ReportTemplate()
        reportTemplate.template_name = template_name
        reportTemplate.module_id = module_id
        reportTemplate.user_id = user_id
        reportTemplate.template_create_date = template_create_date
        reportTemplate.template_update_date = template_update_date
        reportTemplate.template__left_menu = template__left_menu
        reportTemplate.template_state = template_state
        reportTemplate.template_left_content = template_left_content
        reportTemplate.template_content = template_content
        return reportTemplate

    @staticmethod
    def insert_constant(reportTemplate):
        try:
            db.session.add(reportTemplate)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update reportTemplate<id=%s, module_id=%s>" %
                  (reportTemplate.id, reportTemplate.module_id))

    # 新增模板
    @staticmethod
    def insert_template(template):
        if template is not None and (template.id is None or template.id == ''):
            template.template_create_date = datetime.now()
        template.template_update_date = datetime.now()
        try:
            db.session.add(template)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update template<id=%s, module_id=%s>" %
                  (template.id, template.module_id))

    # 查询所有模板
    @staticmethod
    def search_template_all():
        result = ReportTemplate.query.all()
        return result

    # 按模块查询所有模板
    @staticmethod
    def search_by_module(moduleName):
        result = ReportTemplate.query.filter_by(module_id=moduleName).all()
        return result

    # 按模块和user_id查询所有模板
    @staticmethod
    def search_by_module_userid(moduleName, user_id=1):
        result = ReportTemplate.query.filter_by(module_id=moduleName).all()
        resultlist = []
        for re in result:
            # if re.user_id != user_id:
            #     resultlist.append(re)
            resultlist.append(re)
        return resultlist

    # 根据方案创建人查询去过重复的所有模板
    @staticmethod
    def search_distinct_user():
        result = Plan.query.distinct(ReportTemplate.user_id).all()
        return result

    # 通过templateId查询模板
    @staticmethod
    def search_templateById(templateId):
        result = ReportTemplate.query.filter_by(id=templateId).one_or_none()
        return result

    # 通过templateName查询模板
    @staticmethod
    def search_templateName(templateName):
        result = ReportTemplate.query.filter_by(template_name=templateName).one_or_none()
        return result

    # 通过templateName查询模板
    @staticmethod
    def search_templateNamelist(templateName):
        result = ReportTemplate.query.filter_by(template_name=templateName).all()
        return result

    @staticmethod
    def search_templateByNameAndUser(templateName, userName, moduleName):
        result = ReportTemplate()
        user = User.search_userByName(userName)
        if user is not None:
            userId = user.id
        else:
            userId = -1

        if templateName != '' and userName != '':
            result = ReportTemplate.query.filter_by(
                template_name=templateName, user_id=userId,
                module_id=moduleName).all()
        elif templateName == '' and userName != '':
            result = ReportTemplate.query.filter_by(
                user_id=userId, module_id=moduleName).all()
        elif templateName != '' and userName == '':
            result = ReportTemplate.query.filter_by(
                template_name=templateName, module_id=moduleName).all()
        else:
            result = ReportTemplate.search_by_module(moduleName)
        resultlist = []
        for re in result:
            # if re.user_id != 1:
            resultlist.append(re)
        return resultlist

    @staticmethod
    def search_templateByNameAndUserId(templateName, userId, moduleName):
        result = ReportTemplate()
        teportTemplate = ReportTemplate.query.filter_by(template_name=templateName, user_id=userId, module_id=moduleName).one_or_none()
        if teportTemplate is not None:
            result = teportTemplate
        return result

    # 根据templateId删除实体
    @staticmethod
    def delete_Template(templateId):
        template = ReportTemplate.search_templateById(templateId)
        try:
            db.session.delete(template)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete template<id=%s, > in database" % (template.id))


# 设备清单模板表
class EquipmentListTemplate(db.Model):
    # 表名
    __tablename__ = 'equipment_list_template'
    __table_args__ = {'comment': u'设备清单模板表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    module_name = db.Column(db.Text(), comment=u'模块名')
    equipment_template = db.Column(db.Text(), comment=u'')

    def __init__(self, **kwargs):
        super(EquipmentListTemplate, self).__init__(**kwargs)
                  
    @staticmethod
    def insert_EquipmentListTemplate(equipment_list_template):
        try:
            db.session.add(equipment_list_template)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update equipment_list_template"
                  "<id=%s> in database" % (equipment_list_template.module_name))

    # 根据moduleName查找实体
    @staticmethod
    def search_EquipmentListTemplate(moduleName):
        result = EquipmentListTemplate.query.filter_by(module_name=moduleName).one_or_none()
        return result

    # 根据moduleName删除实体
    @staticmethod
    def delete_EquipmentListTemplate(moduleName):
        equipment_list_template = EquipmentListTemplate.search_EquipmentListTemplate(moduleName)
        try:
            db.session.delete(equipment_list_template)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete equipment_list_template<id=%s, plan_id=%s> in database" %
                  (equipment_list_template.id, equipment_list_template.module_name))


# 设备清单表
class EquipmentList(db.Model):
    # 表名
    __tablename__ = 'equipment_list'
    __table_args__ = {'comment': u'设备清单表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    equipment_content = db.Column(db.Text(), comment=u'')

    def __init__(self, **kwargs):
        super(EquipmentList, self).__init__(**kwargs)

    @staticmethod
    def insert_equipmentList(equipment_list):
        try:
            db.session.add(equipment_list)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update equipment_list"
                  "<id=%s> in database" % (equipment_list.id))

    # 根据plan id查找实体
    @staticmethod
    def search_equipmentList(planId):
        result = EquipmentList.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_equipmentList(plan_id):
        equipment_list = EquipmentList.search_equipmentList(plan_id)
        try:
            db.session.delete(equipment_list)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete equipment_list<id=%s, plan_id=%s> in database" %
                  (equipment_list.id, equipment_list.plan_id))
    
    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        equipment_list = EquipmentList.search_equipmentList(plan_id)
        db.session.delete(equipment_list)


# 公司方案表
class Plan(db.Model):
    __tablename__ = 'plan'
    __table_args__ = {'comment': u'项目信息'}
    # 方案id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 公司ID(公司表主键)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    # 用户ID(用户表主键)
    user_id = db.Column(db.Integer())
    # 模块id(燃煤热电联产：1、生物质热电：2、煤气发电：3、燃气蒸汽联合循环(ccpp)：4)
    module_id = db.Column(db.String(200), index=True)
    # 模板id
    template_id = db.Column(db.Integer, db.ForeignKey('report_template.id'))
    # 模板地址
    template_location = db.Column(db.String(200))
    # 方案创建时间
    plan_create_date = db.Column(db.DateTime, nullable=False)
    # 方案修改时间
    plan_update_date = db.Column(db.DateTime, nullable=False)
    # 报告md内容
    plan_report_content = db.Column(db.Text())
    # 报告html内容
    plan_report_html = db.Column(db.Text())
    # 方案状态(-1未绑定报告,0未审核，1审核中，2已审核)
    plan_state = db.Column(db.Integer, default=-1)
    # 地址经纬度
    company_lnglat = db.Column(db.String(50))

    # 项目名称
    plan_name = db.Column(db.String(50), comment=u"项目名称")
    # 项目所在地
    company_location = db.Column(db.Text())
    # 主要设备参数(方便检索)、涉及数据的同步：每次点击方案管理时需要将数据更新
    main_equipment_para = db.Column(db.Text())
    # 审批人员
    approver_id = db.Column(db.Integer)
    # 审批时间
    approve_time = db.Column(db.DateTime)
    # 备注
    remarks = db.Column(db.Text())

    def __init__(self, **kwargs):
        super(Plan, self).__init__(**kwargs)

    # 新增方案
    @staticmethod
    def insert_plan(plan):
        if plan is not None and (plan.id is None or plan.id == ''):
            plan.plan_create_date = datetime.now()
        plan.plan_update_date = datetime.now()
        try:
            db.session.add(plan)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update plan<id=%s, module_id=%s>" %
                  (plan.id, plan.module_id))

    # 自动更新方案
    @staticmethod
    def autoupdata_plan(plan):
        try:
            db.session.add(plan)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update plan<id=%s, module_id=%s>" %
                  (plan.id, plan.module_id))

    # 查询所有方案
    @staticmethod
    def search_plan_all():
        result = Plan.query.all()
        return result

    # 按模块查询所有方案
    @staticmethod
    def search_by_module(moduleName):
        result = Plan.query.filter_by(module_id=moduleName).all()
        return result

    # 根据方案创建人查询去过重复的所有方案
    @staticmethod
    def search_distinct_user():
        result = Plan.query.distinct(Plan.user_id).all()
        return result

    # 查询当前用户的所有方案
    @staticmethod
    def search_plan(userId):
        result = Plan.query.filter_by(user_id=userId).all()
        return result

    # 查询当前用户的所有方案
    @staticmethod
    def search_planByUidAndMid(userId, modelId):
        result = Plan.query.filter_by(user_id=userId, module_id=modelId).all()
        return result

    # 通过planId查询方案
    @staticmethod
    def search_planById(planId):
        result = Plan.query.filter_by(id=planId).one_or_none()
        return result
    
    # 通过template_id查询方案
    @staticmethod
    def search_planBytemplateId(template_id):
        result = Plan.query.filter_by(template_id=template_id).all()
        return result

    # 查询已审核方案的个数
    # choices=[(1, u'超级管理员'), (2, u'全能专家'), (3, u'用户'), (4, u'燃煤专家'), (5, u'生物质专家'), (6, u'煤气专家'), (7, u'燃蒸专家'), (8, u'能源岛专家')]
    @staticmethod
    def search_checkedCount(role_id):
        moduleId = []
        if role_id in [1, 2]:
            uncheck = Plan.query.filter_by(plan_state=0).count()
            checking = Plan.query.filter_by(plan_state=1).count()
            return int(uncheck) + int(checking)
        elif role_id == 4:
            moduleId = Module.coalCHP
        elif role_id == 5:
            moduleId = Module.biomassCHP
        elif role_id == 6:
            moduleId = Module.gasPowerGeneration
        elif role_id == 7:
            moduleId = Module.CCPP
        elif role_id == 8:
            moduleId = ''
        uncheck = Plan.query.filter_by(plan_state=0, module_id=moduleId).count()
        checking = Plan.query.filter_by(plan_state=1, module_id=moduleId).count()
        result = int(uncheck) + int(checking)
        return result

    # 通过公司名和用户名查询方案
    @staticmethod
    def search_planByParams(companyName, userName, moduleName):
        company = Company.search_companyByName(companyName)
        user = User.search_userByName(userName)
        if company:
            companyId = company.id
        else:
            companyId = 0
        if user:
            userId = user.id
        else:
            userId = 0
        result = Plan()
        if companyName != '' and userName != '':
            result = Plan.query.filter_by(
                company_id=companyId, user_id=userId,
                module_id=moduleName).all()
        elif companyName == '' and userName != '':
            result = Plan.query.filter_by(
                user_id=userId, module_id=moduleName).all()
        elif companyName != '' and userName == '':
            result = Plan.query.filter_by(
                company_id=companyId, module_id=moduleName).all()
        else:
            result = Plan.search_by_module(moduleName)
        return result
    
    # 通过用户名查询方案
    @staticmethod
    def search_planByUserName(userName):
        user = User.search_userByName(userName)
        if user:
            userId = user.id
        else:
            userId = 0
        result = Plan()
        if userName != '':
            result = Plan.query.filter_by(
                user_id=userId).all()
        return result

    # 通过公司名查询方案
    @staticmethod
    def search_planByCompanyName(companyName):
        company = Company.search_companyByName(companyName)
        if company:
            companyId = company.id
        else:
            companyId = 0
        result = Plan()
        if companyName != '':
            result = Plan.query.filter_by(
                company_id=companyId).all()
        return result

    # 按模块查询所有方案
    @staticmethod
    def search_by_planName(name):
        result = Plan.query.filter_by(plan_name=name).all()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_plan(plan_id):
        plan = Plan.search_planById(
            plan_id)
        try:
            db.session.delete(plan)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete plan<id=%s, > in database" % (plan.id))
    
    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        plan = Plan.search_planById(plan_id)
        db.session.delete(plan)


class Role(db.Model):
    # 表名
    __tablename__ = 'role'
    # 角色ID， 自动生成
    id = db.Column(db.Integer, primary_key=True)
    # 角色名
    name = db.Column(db.String(64), unique=True)
    # 默认
    defaults = db.Column(db.Boolean, default=False, index=True)
    # 权限
    permissions = db.Column(db.Integer)
    # 用户
    user = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def create_roles(name, defaults, permissions):
        role = Role()
        role.name = name
        role.defaults = defaults
        role.permissions = permissions
        return role

    @staticmethod
    def insert_roles(role):
        try:
            db.session.add(role)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update role<id=%s>" %
                  (role.id))

    # 查询所有权限列表
    @staticmethod
    def search_plan_all():
        result = Role.query.all()
        return result


# 审批状态
class ApproveStates:
    # 申请
    APPLY = 0x00
    # 受理
    ACCEPT = 0x01
    # 处理中
    DOING = 0x02
    # 通过
    PASS = 0x04
    # 拒绝
    CANCEL = 0x08


# 模块名
class Module:
    # 燃煤热电联产
    coalCHP = "coalCHP"
    # 生物质热电联产
    biomassCHP = "biomassCHP"
    # CCPP
    CCPP = "CCPP"
    # 煤气发电 GasPowerGeneration
    gasPowerGeneration = "gasPowerGeneration"
    # 能源互联岛 energyIsland
    energyIsland = "energyIsland"


# 性别
class Sex:
    # 男
    MALE = 0x01
    # 女
    FEMALE = 0x02
    # 其他
    OTHER = 0x00

    # 获取性别名称
    @staticmethod
    def get_gender(gender):
        genders = {Sex.MALE: u'男', Sex.FEMALE: u'女', Sex.OTHER: u'其他'}
        return genders[gender]


def enum(**enums):
    return type('Enum', (), enums)


# 用户表
class User(db.Model, UserMixin):
    # 表名
    __tablename__ = 'user'

    # 用户ID,自动生成
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户昵称,不超过20位,不能出现重复
    user_name = db.Column(
        db.String(20), unique=True, index=True, nullable=False)
    # 用户工号
    user_eid = db.Column(db.String(20), unique=True, nullable=True)
    # 用户邮件
    user_email = db.Column(db.String(40), unique=True, nullable=False)
    # 用户电话号码
    user_tel = db.Column(db.String(11), unique=True, nullable=True)
    # 用户密码
    user_pwd_hash = db.Column(db.String(128), nullable=False)
    # 注册时间
    reg_dateTime = db.Column(db.DateTime, nullable=False)
    # 更新时间
    update_dateTime = db.Column(db.DateTime, nullable=False)
    # 公司id(公司表主键)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    # 用户类型
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    # 性别
    gender = db.Column(db.Integer)

    # 初始化管理员用户
    @staticmethod
    def insert_admin():
        # Company.init_company()
        # Role.insert_roles()
        user = User(
            user_eid='0001',
            user_email='admin@qq.com',
            user_name=u'我是管理员',
            role_id=1,
            hash_password='111111',
            company_id=1,
            reg_dateTime='2017-06-16 11:54:31.166',
            update_dateTime='2017-06-16 11:54:45.277')
        db.session.add(user)
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.name

    # 查询所有用户
    @staticmethod
    def select_all():
        return User.query.all()

    # 删除用户
    @staticmethod
    def delete_user(user):
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete user<user_id=%s> in database" % (user.id))

    # 通过userName查询用户信息
    @staticmethod
    def search_userByName(userName):
        user = User.query.filter_by(user_name=userName).one_or_none()
        return user

    # 通过userId查询用户信息
    @staticmethod
    def search_userById(userId):
        user = User.query.filter_by(id=userId).one_or_none()
        return user

    # 密码属性
    @property
    def password(self):
        raise AttributeError('password is not readable')

    # 密码加密
    @password.setter
    def hash_password(self, password):
        self.user_pwd_hash = generate_password_hash(password)

    # 检验密码
    def verify_password(self, password):
        return check_password_hash(self.user_pwd_hash, password)

    # 获取用户ID
    def get_id(self):
        return self.id

    # 检验用户是否拥有权限
    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    # 检验用户是否是管理员类型
    def is_admin(self):
        return self.can(Permission.ADMINISTER)

    # 构造函数，生成用户角色
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        # if self.role is None:
        #     self.role = Role.query.filter_by(default=True).first()

    # 用户回调

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


# 匿名用户
class AnonymousUser(AnonymousUserMixin):
    # 匿名用户没有任何权限
    def can(self, permissions):
        return False

    # 匿名用户不是管理员
    def is_admin(self):
        return False


login_manager.anonymous_user = AnonymousUser


# 自定义异常模型
class MyException(RuntimeError):

    def __init__(self, exceptionName, exceptioninfoforkh, exceptioninfoforself, exceptionpath):
        self.exceptionName = exceptionName
        # 给客户看的异常信息
        self.exceptioninfoforkh = exceptioninfoforkh
        # 给开发人员看的异常信息
        self.exceptioninfoforself = exceptioninfoforself
        self.exceptionpath = exceptionpath

    @staticmethod
    def vaild(valicolumn, notvalicolumnlist, validata, invokefunname, questionnaire, executefun):
        # MyException.vaild(list_column_questionnaire[index],
        #                   ['denitration_form', 'urea_ammonia_water_supply'],
        #                   formdata, 'updata_questionnaire',
        #                   questionnaire,
        #                   setattr
        #                   )
        try:
            if valicolumn not in notvalicolumnlist:
                float(validata)
            else:
                pass
                # 长度验证DataError
        except ValueError as e:
                raise MyException(u"ValueError", u"发生转换错误", valicolumn + u":" + validata, invokefunname)
        except Exception as e:
                raise MyException(u"Exception", u"发生转换错误", valicolumn + u":" + validata + u":" + e.message, invokefunname)
        else:
            executefun(questionnaire, valicolumn, validata)
