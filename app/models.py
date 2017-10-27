# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import db
from . import login_manager


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
    # 公司ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 公司名称
    company_name = db.Column(db.String(200))
    # 公司性质
    company_nature = db.Column(db.String(200))
    # 备注
    remarks = db.Column(db.Text())

    # 初始化公司表
    @staticmethod
    def insert_company():
        company = Company(
            company_name=u'陕鼓动力分布式小组', company_nature=u'陕鼓分公司', remarks='国企')
        db.session.add(company)
        db.session.commit()


# 公司方案表
class Plan(db.Model):
    __tablename__ = 'plan'
    # 方案id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 公司ID(公司表主键)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    # 用户ID(用户表主键)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 模块id(燃煤热电联产：1、生物质热电：2、煤气发电：3、燃气蒸汽联合循环(ccpp)：4)
    module_id = db.Column(db.String(200), index=True)
    # 工厂选址
    company_location = db.Column(db.Text())


class Role(db.Model):
    # 表名
    __tablename__ = 'role'
    # 角色ID， 自动生成
    id = db.Column(db.Integer, primary_key=True)
    # 角色名
    name = db.Column(db.String(64), unique=True)
    # 默认
    default = db.Column(db.Boolean, default=False, index=True)
    # 权限
    permissions = db.Column(db.Integer)
    # 用户
    user = db.relationship('User', backref='role', lazy='dynamic')

    # 初始化角色表
    @staticmethod
    def insert_roles():
        roles = {
            'Normal': (Permission.QUERY, True),
            'Expert': (Permission.QUERY | Permission.REVIEW, False),
            'Administrator': (Permission.ADMINISTER, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()


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
        user = User(
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


# 燃煤热电联产常量表
class CoalCHPConstant(db.Model):
    # 表名
    __tablename__ = 'coalCHP_constant'
    # 常量表id， 自动生成
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 模块(页面)id：
    module_name = db.Column(db.String(200), index=True)
    # 字段英文名
    name_eng = db.Column(db.String(200))
    # 字段中文名
    name = db.Column(db.String(200))
    # 表示符号
    symbol = db.Column(db.String(200))
    # 计量单位
    unit = db.Column(db.String(50))
    # 计算公式
    calculate = db.Column(db.String(200))
    # 备注
    remark = db.Column(db.Text())

    @staticmethod
    def create_coalCHPConstant(module_name, name_eng, name, symbol, unit,
                               calculate, remark):
        coalCHPconstant = CoalCHPConstant()
        coalCHPconstant.module_name = module_name
        coalCHPconstant.name_eng = name_eng
        coalCHPconstant.name = name
        coalCHPconstant.symbol = symbol
        coalCHPconstant.unit = unit
        coalCHPconstant.calculate = calculate
        coalCHPconstant.remark = remark

        return coalCHPconstant

    @staticmethod
    def insert_coalCHPConstant(coalCHPConstant):
        try:
            db.session.add(coalCHPConstant)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPconstant<id=%s, module_name=%s>" %
                  (coalCHPConstant.id, coalCHPConstant.module_name))

    @staticmethod
    def search_coalCHPConstant(module_name):
        result = CoalCHPConstant.query.filter_by(module_name=module_name).all()
        return result

    def __repr__(self):
        return '<coalCHPConstant %r>' % self.module_name


# 燃煤热电联产产煤成分数据表
class CoalCHPComponent(db.Model):
    # 表名
    __tablename__ = 'coalCHP_coalComponent'
    # 煤种id， 自动生成
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 煤种名称
    name = db.Column(db.String(50))
    # 收到基碳含量
    carbon = db.Column(db.String(50))
    # 收到基氢含量
    hydrogen = db.Column(db.String(50))
    # 收到基氧含量
    oxygen = db.Column(db.String(50))
    # 收到基氮含量
    nitrogen = db.Column(db.String(50))
    # 收到基硫含量
    sulfur = db.Column(db.String(50))
    # 收到基水份含量
    water = db.Column(db.String(50))
    # 收到基灰份
    grey = db.Column(db.String(50))
    # 干燥无灰基挥发分
    daf = db.Column(db.String(50))
    # 收到可磨系数
    grindability = db.Column(db.String(50))
    # 收到基低位发热量
    low = db.Column(db.String(50))

    @staticmethod
    def create_coalCHPComponent(name, carbon, hydrogen, oxygen, nitrogen,
                                sulfur, water, grey, daf, grindability, low):
        coalCHPComponent = CoalCHPComponent()
        coalCHPComponent.name = name
        coalCHPComponent.carbon = carbon
        coalCHPComponent.hydrogen = hydrogen
        coalCHPComponent.oxygen = oxygen
        coalCHPComponent.nitrogen = nitrogen
        coalCHPComponent.sulfur = sulfur
        coalCHPComponent.water = water
        coalCHPComponent.grey = grey
        coalCHPComponent.daf = daf
        coalCHPComponent.grindability = grindability
        coalCHPComponent.low = low

        return coalCHPComponent

    @staticmethod
    def insert_coalCHPComponent(coalCHPComponent):
        try:
            db.session.add(coalCHPComponent)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPComponent<id=%s>" %
                  (coalCHPComponent.id))

    @staticmethod
    def search_coalCHPComponent():
        result = CoalCHPComponent.query.all()
        return result

    # 根据id查找实体
    @staticmethod
    def search_coalCHPSort(id):
        result = CoalCHPComponent.query.filter_by(id=id).one_or_none()
        return result

    def __repr__(self):
        return '<CoalCHPComponent %r>' % self.name


# 燃煤热电联产需求调查表
class CoalCHPNeedsQuestionnaire(db.Model):
    # 表名
    __tablename__ = 'coalCHP_needsQuestionnaire'

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 模块一，燃料情况status缩写（S）
    # s_modul_name = db.Column(db.String(100), nullable=True)
    # 设计燃料
    s_fuel_design = db.Column(db.String(100), nullable=True)
    # 校核燃料
    s_fuel_check = db.Column(db.String(100), nullable=True)

    # 基碳设计数值
    s_carbon_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 基碳校核数值
    s_carbon_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 基氢设计数值
    s_hydrogen_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 基氢校核数值
    s_hydrogen_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 基氧设计数值
    s_oxygen_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 基氧校核数值
    s_oxygen_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 基氮设计数值
    s_nitrogen_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 基氮校核数值
    s_nitrogen_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 基硫设计数值
    s_sulfur_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 基硫校核数值
    s_sulfur_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 基全水份设计数值
    s_water_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 基全水份校核数值
    s_water_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 基灰设计数值
    s_grey_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 基灰校核数值
    s_grey_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 干燥无灰基挥发分设计数值
    s_daf_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 干燥无灰基挥发分校核数值
    s_daf_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 哈式可磨性系数设计数值
    s_grindability_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 哈式可磨性系数校核数值
    s_grindability_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 收到基低位发热量设计数值
    s_low_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 收到基低位发热量校核数值
    s_low_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 模块二 当地气象及地址条件weather 缩写W
    # w_modul_name = db.Column(db.String(100), nullable=True)
    # 当地平均海拔数值
    w_altitude_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 年平均温度数值
    w_mean_annual_temperature_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 夏季平均温度数值
    w_mean_summer_temperature_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 冬季平均温度数值
    w_mean_winter_temperature_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 年平均大气压力数值
    w_mean_annual_barometric_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 夏季大气压力数值
    w_mean_summer_barometric_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 冬季大气压力数值
    w_mean_winter_barometric_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 年平均相对湿度数值
    w_annual_average_relative_humidity_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 模块三  工业热负荷(Industrial heat load)缩写ihl   采暖热负荷（heating heat load）需求情况缩写hhl
    # 一级模块
    # h_modul_name = db.Column(db.String(100), nullable=True)
    # 二级模块
    # ihl_modul_name = db.Column(db.String(100), nullable=True)
    # 蒸汽压力等级数值
    ihl_steam_pressure_level_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 蒸汽温度等级数值
    ihl_steam_temperature_level_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 用汽时段校核数值
    ihl_steam_time_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 近期蒸汽流量范围数值
    ihl_recent_steam_flow_range_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 远期蒸汽流量范围数值
    ihl_forward_steam_flow_range_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 凝结水含铁量数值
    ihl_condensate_water_iron_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 凝结水回收率数值
    ihl_condensate_water_recovery_rate_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # hhl_modul_name = db.Column(db.String(100), nullable=True)
    # 采暖场合类型数值
    hhl_heating_occasions_type_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 全年采暖天数数值
    hhl_year_heating_days_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 近期采暖面积数值
    hhl_recent_heating_area_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 远期采暖面积数值
    hhl_forward_heating_area_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 模块四 其它情况others缩写O
    # 一级模块
    # o_modul_name = db.Column(db.String(100), nullable=True)
    # 二级模块 项目选址情况site
    # os_modul_name = db.Column(db.String(100), nullable=True)
    # 规划占地面积数值
    os_planning_area_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 规划扩建容量数值
    os_planned_expansion_capacity_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 当地水源条件数值
    os_local_water_condition_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 二级模块 电力系统electric
    # oe_modul_name = db.Column(db.String(100), nullable=True)
    # 电负荷需求数值
    oe_electrical_load_demand_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 上级变电压等级数值
    oe_higher_voltage_level_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 厂区距上级变距离校值
    oe_plant_distance_higher_change_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 是否上网校值
    oe_is_internet_access_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 是否孤网运行数值
    oe_is_isolated_network_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 二级模块 当地环保要求Environmental Protection
    # op_modul_name = db.Column(db.String(100), nullable=True)
    # 烟气SOX排放限值数值
    op_flue_gas_sox_limits_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 烟气NOX排放限值数值
    op_flue_gas_nox_limits_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 烟气烟尘排放限值数值
    op_flue_gas_dust_limits_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 二级模块脱硫脱硝 Desulfurization and denitrification
    # od_modul_name = db.Column(db.String(100), nullable=True)
    # 拟采用脱硫形式数值
    od_use_desulfurization_form_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 拟采用脱硝形式数值
    od_use_denitration_form_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 石灰石供应情况数值
    od_limestone_supply_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 尿素/氨水供应情况数值
    od_urea_or_ammonia_water_supply_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    def __init__(self, **kwargs):
        super(CoalCHPNeedsQuestionnaire, self).__init__(**kwargs)

    @staticmethod
    def insert_questionnaire(coalCHPNeedsQuestionnaire):
        try:
            db.session.add(coalCHPNeedsQuestionnaire)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPNeedsQuestionnaire"
                  "<id=%s> in database" % (coalCHPNeedsQuestionnaire.id))

    # 根据id查找实体
    @staticmethod
    def search_questionnaire(id):
        result = CoalCHPNeedsQuestionnaire.query.filter_by(id=id).one_or_none()
        return result


# 表名 燃煤热电联产计算_输煤系统表
class CoalCHP_CoalHandingSystem(db.Model):
    # 表名
    __tablename__ = 'coalCHP_CoalHandingSystem'
    # 主ID， 自动生成
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    '''------------------------------锅炉额定耗煤量------------------------------'''
    # 锅炉额定耗煤量 结果-设计（Value Design）
    boiler_rated_coal_capacity_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉额定耗煤量 结果-校核（Value Verify）
    boiler_rated_coal_capacity_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------锅炉日利用小时数------------------------------'''
    # 锅炉日利用小时数 结果-设计（Value Design）
    boiler_daily_utilization_hours_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉日利用小时数 结果-校核（Value Verify）
    boiler_daily_utilization_hours_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------日耗煤量------------------------------'''
    # 日耗煤量 结果-设计（Value Design）
    coal_daily_consumption_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日耗煤量 结果-校核（Value Verify）
    coal_daily_consumption_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------锅炉年利用小时数------------------------------'''
    # 锅炉年利用小时数 结果-设计（Value Design）
    boiler_annual_utilization_hours_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉年利用小时数 结果-校核（Value Verify）
    boiler_annual_utilization_hours_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------年耗煤量------------------------------'''
    # 年耗煤量 结果-设计（Value Design）
    coal_annual_consumption_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 年耗煤量 结果-校核（Value Verify）
    coal_annual_consumption_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------日来煤不均衡系数------------------------------'''
    # 日来煤不均衡系数 结果-设计（Value Design）
    daily_coal_unbalanced_coefficient_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日来煤不均衡系数 结果-校核（Value Verify）
    daily_coal_unbalanced_coefficient_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------铁路来煤日计算煤量------------------------------'''
    # 铁路来煤日计算煤量 结果-设计（Value Design）
    daily_rail_coal_amount_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 铁路来煤日计算煤量 结果-校核（Value Verify）
    daily_rail_coal_amount_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------汽车来煤日计算煤量------------------------------'''
    # 汽车来煤日计算煤量 结果-设计（Value Design）
    daily_vehicle_coal_amount_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 汽车来煤日计算煤量 结果-校核（Value Verify）
    daily_vehicle_coal_amount_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''-----------------------锅炉每小时最大耗煤量---------------------'''
    # 锅炉每小时最大耗煤量 结果-设计（Value Design）
    boiler_perhour_coal_max_capacity_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉每小时最大耗煤量 结果-校核（Value Verify）
    boiler_perhour_coal_max_capacity_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------锅炉每日运行时数------------------------------'''
    # 锅炉每日运行时数 结果-设计（Value Design）
    boiler_daily_working_hours_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉每日运行时数 结果-校核（Value Verify）
    boiler_daily_working_hours_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------煤的储备日数------------------------------'''
    # 煤的储备日数 结果-设计（Value Design）
    coal_store_days_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 煤的储备日数 结果-校核（Value Verify）
    coal_store_days_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------煤场存储量------------------------------'''
    # 煤场存储量 结果-设计（Value Design）
    coalyard_store_amount_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤场存储量 结果-校核（Value Verify）
    coalyard_store_amount_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------煤堆通道占用系数------------------------------'''
    # 煤堆通道占用系数 结果-设计（Value Design）
    coal_channel_occupy_coefficient_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤堆通道占用系数 结果-校核（Value Verify）
    coal_channel_occupy_coefficient_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------煤堆形状系数------------------------------'''
    # 煤堆形状系数 结果-设计（Value Design）
    coal_shape_coefficient_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤堆形状系数 结果-校核（Value Verify）
    coal_shape_coefficient_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------煤堆高度------------------------------'''
    # 煤堆高度 结果-设计（Value Design）
    coal_height_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 煤堆高度 结果-校核（Value Verify）
    coal_height_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------煤的堆密度------------------------------'''
    # 煤的堆密度 结果-设计（Value Design）
    coal_bulk_density_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤的堆密度 结果-校核（Value Verify）
    coal_bulk_density_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------煤场面积------------------------------'''
    # 煤场面积 结果-设计（Value Design）
    coalyard_area_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 煤场面积 结果-校核（Value Verify）
    coalyard_area_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------长------------------------------'''
    # 长 结果-设计（Value Design）
    height_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长 结果-校核（Value Verify）
    height_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------宽------------------------------'''
    # 宽 结果-设计（Value Design）
    width_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽 结果-校核（Value Verify）
    width_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------有效容积-计算------------------------------'''
    # 有效容积-计算 结果-设计（Value Design）
    effective_cubage_calculated_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 有效容积-计算 结果-校核（Value Verify）
    effective_cubage_calculated_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------煤仓个数------------------------------'''
    # 煤仓个数 结果-设计（Value Design）
    coal_bunker_counts_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤仓个数 结果-校核（Value Verify）
    coal_bunker_counts_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------有效容积-选定------------------------------'''
    # 有效容积-选定 结果-设计（Value Design）
    effective_cubage_selected_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 有效容积-选定 结果-校核（Value Verify）
    effective_cubage_selected_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------反推消耗小时------------------------------'''
    # 反推消耗小时 结果-设计（Value Design）
    backstep_consumption_hours_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 反推消耗小时 结果-校核（Value Verify）
    backstep_consumption_hours_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------运输不平衡系数------------------------------'''
    # 运输不平衡系数 结果-设计（Value Design）
    transport_unbalanced_coefficient_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运输不平衡系数 结果-校核（Value Verify）
    transport_unbalanced_coefficient_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''----------------------运煤系统有效作业时间----------------'''
    # 运煤系统有效作业时间 结果-设计（Value Design）
    transportsystem_effective_working_hours_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运煤系统有效作业时间 结果-校核（Value Verify）
    transportsystem_effective_working_hours_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------运煤系统运输量------------------------------'''
    # 运煤系统运输量 结果-设计（Value Design）
    transportsystem_amount_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运煤系统运输量 结果-校核（Value Verify）
    transportsystem_amount_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------车辆名义载重量------------------------------'''
    # 车辆名义载重量 结果-设计（Value Design）
    vehicle_capacity_tonnage_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 车辆名义载重量 结果-校核（Value Verify）
    vehicle_capacity_tonnage_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------每昼夜小时------------------------------'''
    # 每昼夜小时 结果-设计（Value Design）
    daily_working_hours_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每昼夜小时 结果-校核（Value Verify）
    daily_working_hours_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------日计算受煤量------------------------------'''
    # 日计算受煤量 结果-设计（Value Design）
    daily_received_coal_amount_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日计算受煤量 结果-校核（Value Verify）
    daily_received_coal_amount_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------每天进厂车次------------------------------'''
    # 每天进厂车次 结果-设计（Value Design）
    vehicle_daily_incoming_times_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每天进厂车次 结果-校核（Value Verify）
    vehicle_daily_incoming_times_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------每小时进场车次------------------------------'''
    # 每小时进场车次 结果-设计（Value Design）
    vehicle_perhour_incoming_times_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每小时进场车次 结果-校核（Value Verify）
    vehicle_perhour_incoming_times_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------多锅炉额定耗煤量------------------------------'''
    # 多锅炉额定耗煤量 结果-设计（Value Design）
    mutil_boiler_rated_coal_capacity_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 多锅炉额定耗煤量 结果-校核（Value Verify）
    mutil_boiler_rated_coal_capacity_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''-------------------------多锅炉日额定耗煤总量----------------------'''
    # 多锅炉日额定耗煤总量 结果-设计（Value Design）
    mutil_boiler_rated_coal_amount_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 多锅炉日额定耗煤总量 结果-校核（Value Verify）
    mutil_boiler_rated_coal_amount_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------输煤系统选定出力------------------------------'''
    # 输煤系统选定出力 结果-设计（Value Design）
    transportsystem_output_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 输煤系统选定出力 结果-校核（Value Verify）
    transportsystem_output_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------输煤系统运行小时------------------------------'''
    # 输煤系统运行小时 结果-设计（Value Design）
    transportsystem_working_hours_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 输煤系统运行小时 结果-校核（Value Verify）
    transportsystem_working_hours_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------每班运行小时------------------------------'''
    # 每班运行小时 结果-设计（Value Design）
    shift_working_hours_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每班运行小时 结果-校核（Value Verify）
    shift_working_hours_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------带宽------------------------------'''
    # 带宽 结果-设计（Value Design）
    belt_width_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 带宽 结果-校核（Value Verify）
    belt_width_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------断面系数------------------------------'''
    # 断面系数 结果-设计（Value Design）
    section_coefficient_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 断面系数 结果-校核（Value Verify）
    section_coefficient_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------带速------------------------------'''
    # 带速 结果-设计（Value Design）
    belt_speed_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 带速 结果-校核（Value Verify）
    belt_speed_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------物料松散密度------------------------------'''
    # 物料松散密度 结果-设计（Value Design）
    material_bulk_density_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 物料松散密度 结果-校核（Value Verify）
    material_bulk_density_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------皮带最大输送能力------------------------------'''
    # 皮带最大输送能力 结果-设计（Value Design）
    belt_max_transport_capacity_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 皮带最大输送能力 结果-校核（Value Verify）
    belt_max_transport_capacity_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    '''------------------------------台数------------------------------'''
    # 台数 结果-设计（Value Design）
    equipment_sets_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 台数 结果-校核（Value Verify）
    equipment_sets_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------富裕量------------------------------'''
    # 富裕量 结果-设计（Value Design）
    surplus_DesignValue = db.Column(db.NUMERIC(precision=15, scale=5))
    # 富裕量 结果-校核（Value Verify）
    surplus_VerifyValue = db.Column(db.NUMERIC(precision=15, scale=5))
    '''------------------------------单台给煤机出力------------------------------'''
    # 单台给煤机出力 结果-设计（Value Design）
    single_coal_feeder_output_DesignValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 单台给煤机出力 结果-校核（Value Verify）
    single_coal_feeder_output_VerifyValue = db.Column(
        db.NUMERIC(precision=15, scale=5))
