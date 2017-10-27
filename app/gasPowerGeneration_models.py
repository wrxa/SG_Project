# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import db
from . import login_manager


# 煤气发电常量表
class GasPowerGenerationConstant(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_constant'
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
    def create_gasPowerGenerationConstant(module_name, name_eng, name, symbol, unit,
                               calculate, remark):
        gasPowerGenerationConstant = GasPowerGenerationConstant()
        gasPowerGenerationConstant.module_name = module_name
        gasPowerGenerationConstant.name_eng = name_eng
        gasPowerGenerationConstant.name = name
        gasPowerGenerationConstant.symbol = symbol
        gasPowerGenerationConstant.unit = unit
        gasPowerGenerationConstant.calculate = calculate
        gasPowerGenerationConstant.remark = remark

        return gasPowerGenerationConstant

    @staticmethod
    def insert_gasPowerGenerationConstant(gasPowerGenerationConstant):
        try:
            db.session.add(gasPowerGenerationConstant)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gasPowerGenerationConstant<id=%s, module_name=%s>" %
                  (gasPowerGenerationConstant.id, gasPowerGenerationConstant.module_name))

    @staticmethod
    def search_gasPowerGenerationConstant(module_name):
        result = GasPowerGenerationConstant.query.filter_by(module_name=module_name).all()
        return result

    def __repr__(self):
        return '<gasPowerGenerationConstant %r>' % self.module_name


'''
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
'''

# 煤气发电需求调查表
class GasPowerGenerationNeedsQuestionnaire(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_needsquestionnaire'

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 富余的煤气流量_BFG
    surplus_gas_bfg = db.Column(db.NUMERIC(precision=15, scale=5))

    # 富余的煤气流量_LDG
    surplus_gas_ldg = db.Column(db.NUMERIC(precision=15, scale=5))

    # 富余的煤气流量_COG
    surplus_gas_cog = db.Column(db.NUMERIC(precision=15, scale=5))

    # 煤气温度
    gas_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # 煤气压力
    gas_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # 煤气热值
    gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 对外供蒸汽量
    provide_steam_amount = db.Column(db.NUMERIC(precision=15, scale=5))

    # 对外供蒸汽压
    provide_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # H2
    h2_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # CO
    co_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # CH4
    ch4_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # C2H4
    c2h4_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # C3H8
    c3h8_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # C4H10
    c4h10_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # N2
    n2_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # O2
    o2_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # CO2
    co2_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # H2S
    h2s_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # CmHn
    cmhn_content = db.Column(db.NUMERIC(precision=15, scale=5))

    # 大气温度
    atmosphere_temperature_h = db.Column(db.NUMERIC(precision=15, scale=5))
    atmosphere_temperature_a = db.Column(db.NUMERIC(precision=15, scale=5))
    atmosphere_temperature_l = db.Column(db.NUMERIC(precision=15, scale=5))

    # 大气压力
    atmosphere_pressure_h = db.Column(db.NUMERIC(precision=15, scale=5))
    atmosphere_pressure_a = db.Column(db.NUMERIC(precision=15, scale=5))
    atmosphere_pressure_l = db.Column(db.NUMERIC(precision=15, scale=5))

    # 相对湿度
    relative_humidity_h = db.Column(db.NUMERIC(precision=15, scale=5))
    relative_humidity_a = db.Column(db.NUMERIC(precision=15, scale=5))
    relative_humidity_l = db.Column(db.NUMERIC(precision=15, scale=5))

    # 室外风速
    outside_wind_speed_h = db.Column(db.NUMERIC(precision=15, scale=5))
    outside_wind_speed_a = db.Column(db.NUMERIC(precision=15, scale=5))
    outside_wind_speed_l = db.Column(db.NUMERIC(precision=15, scale=5))

    # 抗震设防烈度
    seismic_fortification_intensity_h = db.Column(db.NUMERIC(precision=15, scale=5))
    seismic_fortification_intensity_a = db.Column(db.NUMERIC(precision=15, scale=5))
    seismic_fortification_intensity_l = db.Column(db.NUMERIC(precision=15, scale=5))

    # 水压力
    water_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # 水温度
    water_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # PH值
    water_ph = db.Column(db.NUMERIC(precision=15, scale=5))

    # 悬浮物
    water_suspended_matter = db.Column(db.NUMERIC(precision=15, scale=5))

    # 氯离子
    water_cl = db.Column(db.NUMERIC(precision=15, scale=5))

    # 氮气纯度
    nitrogen_purity = db.Column(db.NUMERIC(precision=15, scale=5))

    # 氮气压力范围
    nitrogen_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # 氮气温度
    nitrogen_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # 压缩空气压力范围
    compressed_air_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # 压缩空气温度
    compressed_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # 并网电压
    grid_voltage = db.Column(db.NUMERIC(precision=15, scale=5))

    # 最大短路容量
    max_short_circuit_capacity = db.Column(db.NUMERIC(precision=15, scale=5))

    # 拟建厂区坐标点和高程的地形图
    factory_location_elevation = db.Column(db.Text())

    # 能源介质接点位置、标高、管径、路由
    dielectric_position_height_caliber_route = db.Column(db.Text())

    # 全水质分析报告
    water_quality_analysis_report = db.Column(db.Text())

    # 冷却方式及冷却塔形式	
    cooling_tower = db.Column(db.Text())

    # 项目立项及环评手续
    project_approval_eia = db.Column(db.Boolean, default=False)



    def __init__(self, **kwargs):
        super(GasPowerGenerationNeedsQuestionnaire, self).__init__(**kwargs)

    @staticmethod
    def insert_questionnaire(gasPowerGenerationNeedsQuestionnaire):
        try:
            db.session.add(gasPowerGenerationNeedsQuestionnaire)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gasPowerGenerationNeedsQuestionnaire"
                  "<id=%s> in database" % (gasPowerGenerationNeedsQuestionnaire.id))

    # 根据id查找实体
    @staticmethod
    def search_questionnaire(id):
        result = GasPowerGenerationNeedsQuestionnaire.query.filter_by(id=id).one_or_none()
        return result