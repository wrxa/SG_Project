# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from app import db
from app import login_manager


# 生物质热电联产常量表
class BiomassCHPconstant(db.Model):
    # 表名
    __tablename__ = 'biomasschp_constant'
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
    calculate = db.Column(db.Text())
    # 备注
    remark = db.Column(db.Text())
    # 默认值
    default_value = db.Column(db.String(200))
    # 是否可以输入
    disable = db.Column(db.String(10))

    @staticmethod
    def create_biomassCHPconstant(module_name, name_eng, name, symbol, unit,
                               calculate, remark, default_value, disable):
        biomassCHPconstant = BiomassCHPconstant()
        biomassCHPconstant.module_name = module_name
        biomassCHPconstant.name_eng = name_eng
        biomassCHPconstant.name = name
        biomassCHPconstant.symbol = symbol
        biomassCHPconstant.unit = unit
        biomassCHPconstant.calculate = calculate
        biomassCHPconstant.remark = remark
        biomassCHPconstant.default_value = default_value
        biomassCHPconstant.disable = disable

        return biomassCHPconstant

    @staticmethod
    def insert_biomassCHPconstant(biomassCHPconstant):
        try:
            db.session.add(biomassCHPconstant)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print(
                "Insert/Update biomassCHPconstant<id=%s, module_name=%s>"
                % (biomassCHPconstant.id, biomassCHPconstant.module_name))

    @staticmethod
    def search_biomassCHPconstant(module_name):
        result = BiomassCHPconstant.query.order_by(BiomassCHPconstant.id.asc()).filter_by(
            module_name=module_name).all()
        return result

    def __repr__(self):
        return '<biomassCHPconstant %r>' % self.module_name

# 生物质热电皮带宽度表
class BiomassCHPBeltWidth(db.Model):
    # 表名
    __tablename__ = 'biomasschp_belt_width'
    # id， 自动生成
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 皮带宽度
    width = db.Column(db.String(50))
    # 断面系数
    coefficient = db.Column(db.String(50)) 

    @staticmethod
    def create_biomassCHPBeltWidth(width, coefficient):
        biomassCHPBeltWidth = BiomassCHPBeltWidth()
        biomassCHPBeltWidth.width = width
        biomassCHPBeltWidth.coefficient = coefficient

        return biomassCHPBeltWidth

    @staticmethod
    def insert_biomassCHPBeltWidth(biomassCHPBeltWidth):
        try:
            db.session.add(biomassCHPBeltWidth)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print(
                "Insert/Update biomassCHPBeltWidth<id=%s>"
                % (biomassCHPBeltWidth.id))

    @staticmethod
    def search_biomassCHPBeltWidth():
        result = BiomassCHPBeltWidth.query.all()
        return result

    # 根据id查找实体
    @staticmethod
    def search_biomassCHPSort(width):
        result = BiomassCHPBeltWidth.query.filter_by(
            width=width).one_or_none()
        return result

    def __repr__(self):
        return '<BiomassCHPBeltWidth %r>' % self.name

# 生物质热电联产需求调查表
class BiomassCHPNeedsQuestionnaire(db.Model):
    # 表名
    __tablename__ = 'biomasschp_needs_questionnaire'
    __table_args__ = {'comment': u'生物质热电联产需求调查表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))
    # 设计燃料
    s_fuel_design = db.Column(db.String(100), comment=u"设计燃料")
    # 校核燃料
    s_fuel_check = db.Column(db.String(100), comment=u"校核燃料")

    # 燃料收到基的元素分析
    # 基碳设计数值
    s_carbon_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基碳设计数值")
    # 基碳校核数值
    s_carbon_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基碳校核数值")
    # 基氢设计数值
    s_hydrogen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基氢设计数值")
    # 基氢校核数值
    s_hydrogen_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基氢校核数值")
    # 基氧设计数值
    s_oxygen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基氧设计数值")
    # 基氧校核数值
    s_oxygen_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基氧校核数值")
    # 基氮设计数值
    s_nitrogen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基氮设计数值")
    # 基氮校核数值
    s_nitrogen_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基氮校核数值")
    # 基硫设计数值
    s_sulfur_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基硫设计数值")
    # 基硫校核数值
    s_sulfur_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基硫校核数值")
    # 基全水份设计数值
    s_total_moisture_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基全水份设计数值")
    # 基全水份校核数值
    s_total_moisture_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基全水份校核数值")
    # 基灰设计数值
    s_grey_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基灰设计数值")
    # 基灰校核数值
    s_grey_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基灰校核数值")
    # 灰分设计数值
    s_daf_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰分设计数值")
    # 灰分校核数值
    s_daf_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰分校核数值")
    # 固定碳设计数值
    s_grindability_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"固定碳设计数值")
    # 固定碳校核数值
    s_grindability_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"固定碳校核数值")
    # 收到基低位发热量设计数值
    s_quantity_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量设计数值")
    # 收到基低位发热量校核数值
    s_quantity_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量校核数值")

    # 燃料灰熔融性分析
    # 变形温度设计数值
    s_deformation_design  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"变形温度设计数值")
    # 变形温度校核数值
    s_deformation_check  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"变形温度校核数值")
    # 软化温度设计数值
    s_softening_design  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"软化温度设计数值")
    # 软化温度校核数值
    s_softening_check  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"软化温度校核数值")
    # 半球温度设计数值
    s_hemispherical_design  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"半球温度设计数值")
    # 半球温度校核数值
    s_hemispherical_check  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"半球温度校核数值")
    # 流动温度设计数值
    s_flow_design  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"流动温度设计数值")
    # 流动温度校核数值
    s_flow_check  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"流动温度校核数值")

    # 堆积密度
    # 燃料堆积密度设计数值
    s_fuel_density_design  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃料堆积密度设计数值")
    # 燃料堆积密度校核数值
    s_fuel_density_check  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃料堆积密度校核数值")    
    # 飞灰堆积密度设计数值
    s_ash_density_design  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"飞灰堆积密度设计数值")
    # 飞灰堆积密度校核数值
    s_ash_density_check  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"飞灰堆积密度校核数值")

    # 当地气象及地址条件
    # 当地平均海拔
    l_altitude  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地平均海拔")
    # 历年平均气压
    l_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"历年平均气压")
    # 历年平均气温
    l_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"历年平均气温")
    # 历年极端最高气温
    l_max_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"历年极端最高气温")
    # 历年极端最低气温
    l_min_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"历年极端最低气温")
    # 历年平均相对湿度
    l_humidity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"历年平均相对湿度")

    # 工业热负荷
    # 蒸汽压力等级
    t_pressure_grade = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽压力等级")
    # 蒸汽温度等级
    t_temperature_grade = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽温度等级")
    # 用汽时段
    t_steam_time = db.Column(db.String(100), comment=u"用汽时段")
    # 近期蒸汽流量范围
    t_recent_steam_flow_range = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"近期蒸汽流量范围")
    # 远期蒸汽流量范围
    t_forward_steam_flow_range = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"远期蒸汽流量范围")
    # 凝结水含铁量
    t_condensate_water_iron = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水含铁量")
    # 凝结水回收率
    t_condensate_water_recovery_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回收率")

    # 采暖热负荷
    # 采暖场合类型
    t_hhl_heating_occasions_type = db.Column(db.String(100), comment=u"采暖场合类型")
    # 全年采暖天数
    t_year_heating_days = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"全年采暖天数")
    # 近期采暖面积
    t_recent_heating_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"近期采暖面积")
    # 远期采暖面积
    t_forward_heating_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"远期采暖面积")

    # 项目选址情况
    # 规划占地面积
    o_planning_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"规划占地面积")
    # 规划扩建容量
    o_planned_expansion_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"规划扩建容量")
    # 当地水源条件
    o_local_water_condition = db.Column(db.String(100), comment=u"当地水源条件")

    # 电力系统接入条件
    # 上级变电压等级
    o_higher_voltage_level = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上级变电压等级")
    # 厂区距上级变距离
    o_plant_distance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"厂区距上级变距离")

    # 当地环保要求
    # 烟气SOX排放限值
    o_flue_gas_sox_limits = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气SOX排放限值")
    # 烟气NOX排放限值
    o_flue_gas_nox_limits = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气NOX排放限值")
    # 烟气烟尘排放限值
    o_flue_gas_dust_limits = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气烟尘排放限值")

    def __init__(self, **kwargs):
        super(BiomassCHPNeedsQuestionnaire, self).__init__(**kwargs)

    @staticmethod
    def insert_questionnaire(BiomassCHPNeedsQuestionnaire):
        try:
            db.session.add(BiomassCHPNeedsQuestionnaire)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update BiomassCHPNeedsQuestionnaire"
                  "<id=%s> in database" %
                  (BiomassCHPNeedsQuestionnaire.id))

    # 根据id查找实体
    @staticmethod
    def search_questionnaire(plan_id):
        result = BiomassCHPNeedsQuestionnaire.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_questionnaire(plan_id):
        questionnaire = BiomassCHPNeedsQuestionnaire.search_questionnaire(plan_id)
        try:
            db.session.delete(questionnaire)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete questionnaire<id=%s, plan_id=%s> in database" %
                  (questionnaire.id, questionnaire.plan_id))


# 锅炉计算表
class BiomassCHPBoilerCalculation (db.Model):
    # 表名
    __tablename__ = 'biomasschp_boiler_calculation' 
    __table_args__ = {'comment': u'生物质热电锅炉计算表'} 

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))

    # 1收到基碳含量:设计
    c_carbon_content_received_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基碳含量-设计")
    # 1收到基碳含量:校核
    c_carbon_content_received_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基碳含量-校核")
    # 1收到基氢含量:设计
    c_hydrogen_content_received_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氢含量-设计")
    # 1收到基氢含量:校核
    c_hydrogen_content_received_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氢含量-校核")
    # 1收到基氧含量:设计
    c_oxygen_content_received_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氧含量-设计")
    # 1收到基氧含量:校核
    c_oxygen_content_received_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氧含量-校核")
    # 1收到基氮含量:设计
    c_nitrogen_content_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氮含量-设计")
    # 1收到基氮含量:校核
    c_nitrogen_content_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氮含量-校核")
    # 1收到基硫含量:设计
    c_sulfur_content_received_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基硫含量-设计")
    # 1收到基硫含量:校核
    c_sulfur_content_received_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基硫含量-校核")
    # 1收到基灰分:设计
    c_ash_content_received_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基灰分-设计")
    # 1收到基灰分:校核
    c_ash_content_received_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基灰分-校核")
    # 1收到基水分:设计
    c_water_content_received_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基水分-设计")
    # 1收到基水分:校核
    c_water_content_received_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基水分-校核")
    # 1总和:设计
    c_sum_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总和-设计")
    # 1总和:校核
    c_sum_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总和-校核")
    # 1收到基挥发分:设计
    c_base_volatile_obtained_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基挥发分-设计")
    # 1收到基挥发分:校核
    c_base_volatile_obtained_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基挥发分-校核")
    # 1干燥无灰基挥发分:设计
    c_daf_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干燥无灰基挥发分-设计")
    # 1干燥无灰基挥发分:校核
    c_daf_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干燥无灰基挥发分-校核")
    # 1收到基低位发热量用户提供:设计
    c_base_heat_received_user_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量用户提供-设计")
    # 1收到基低位发热量用户提供:校核
    c_base_heat_received_user_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量用户提供-校核")
    # 1收到基低位发热量计算得到:设计
    c_base_heat_received_calculation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量计算得到-设计")
    # 1收到基低位发热量计算得到:校核
    c_base_heat_received_calculation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量计算得到-校核")
    # 1低位发热量估算:设计
    c_low_calorific_value_estimation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低位发热量估算-设计")
    # 1低位发热量估算:校核
    c_low_calorific_value_estimation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低位发热量估算-校核")
    # 1高位发热量估算:设计
    c_high_calorific_value_estimation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高位发热量估算-设计")
    # 1高位发热量估算:校核
    c_high_calorific_value_estimation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高位发热量估算-校核")
    # 2过热蒸汽额定流量:设计
    f_steam_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽额定流量-设计")
    # 2过热蒸汽额定流量:校核
    f_steam_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽额定流量-校核")
    # 2过热蒸汽出口压力:设计
    f_steam_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽出口压力-设计")
    # 2过热蒸汽出口压力:校核
    f_steam_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽出口压力-校核")
    # 2过热蒸汽温度:设计
    f_steam_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽温度-设计")
    # 2过热蒸汽温度:校核
    f_steam_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽温度-校核")
    # 2过热蒸汽焓值:设计
    f_steam_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽焓值-设计")
    # 2过热蒸汽焓值:校核
    f_steam_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽焓值-校核")
    # 2锅筒压力:设计
    f_boiler_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅筒压力-设计")
    # 2锅筒压力:校核
    f_boiler_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅筒压力-校核")
    # 2汽包内饱和水焓值:设计
    f_saturated_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽包内饱和水焓值-设计")
    # 2汽包内饱和水焓值:校核
    f_saturated_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽包内饱和水焓值-校核")
    # 2给水温度:设计
    f_water_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水温度-设计")
    # 2给水温度:校核
    f_water_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水温度-校核")
    # 2给水焓值:设计
    f_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水焓值-设计")
    # 2给水焓值:校核
    f_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水焓值-校核")
    # 2锅炉效率:设计
    f_boiler_efficiency_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉效率-设计")
    # 2锅炉效率:校核
    f_boiler_efficiency_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉效率-校核")
    # 2机械未燃烧损失:设计
    f_unburned_loss_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机械未燃烧损失-设计")
    # 2机械未燃烧损失:校核
    f_unburned_loss_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机械未燃烧损失-校核")
    # 2锅炉排污率:设计
    f_blowdown_rate_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉排污率-设计")
    # 2锅炉排污率:校核
    f_blowdown_rate_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉排污率-校核")
    # 2锅炉燃料消耗量:设计
    f_boiler_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料消耗量-设计")
    # 2锅炉燃料消耗量:校核
    f_boiler_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料消耗量-校核")
    # 2计算燃料消耗量:设计
    f_calculation_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算燃料消耗量-设计")
    # 2计算燃料消耗量:校核
    f_calculation_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算燃料消耗量-校核")
    # 3灰渣总量:设计
    d_total_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰渣总量-设计")
    # 3灰渣总量:校核
    d_total_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰渣总量-校核")
    # 3炉内喷钙灰渣总量:设计
    d_boiler_total_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内喷钙灰渣总量-设计")
    # 3炉内喷钙灰渣总量:校核
    d_boiler_total_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内喷钙灰渣总量-校核")
    # 3飞灰份额:设计
    d_ash_share_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"飞灰份额-设计")
    # 3飞灰份额:校核
    d_ash_share_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"飞灰份额-校核")
    # 3底渣份额:设计
    d_dust_share_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"底渣份额-设计")
    # 3底渣份额:校核
    d_dust_share_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"底渣份额-校核")
    # 3灰量:设计
    d_ash_total_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰量-设计")
    # 3灰量:校核
    d_ash_total_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰量-校核")
    # 3渣量:设计
    d_dust_total_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"渣量-设计")
    # 3渣量:校核
    d_dust_total_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"渣量-校核")
    # 4理论干空气量:设计
    a_air_volumn_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论干空气量-设计")
    # 4理论干空气量:校核
    a_air_volumn_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论干空气量-校核")
    # 4最热月平均气温:设计
    a_hot_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"最热月平均气温-设计")
    # 4最热月平均气温:校核
    a_hot_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"最热月平均气温-校核")
    # 4多年平均相对湿度:设计
    a_humidity_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"多年平均相对湿度-设计")
    # 4多年平均相对湿度:校核
    a_humidity_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"多年平均相对湿度-校核")
    # 4多年平均气压:设计
    a_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"多年平均气压-设计")
    # 4多年平均气压:校核
    a_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"多年平均气压-校核")
    # 4多年平均气温:设计
    a_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"多年平均气温-设计")
    # 4多年平均气温:校核
    a_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"多年平均气温-校核")
    # 4多年平均气温下的饱和压力:设计
    a_saturation_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"多年平均气温下的饱和压力-设计")
    # 4多年平均气温下的饱和压力:校核
    a_saturation_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"多年平均气温下的饱和压力-校核")
    # 4水蒸气分压力:设计
    a_steam_perssure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"水蒸气分压力-设计")
    # 4水蒸气分压力:校核
    a_steam_perssure_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"水蒸气分压力-校核")
    # 4空气的绝对湿度（含湿量）:设计
    a_air_humidity_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气的绝对湿度（含湿量）-设计")
    # 4空气的绝对湿度（含湿量）:校核
    a_air_humidity_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气的绝对湿度（含湿量）-校核")
    # 4标况下湿空气密度:设计
    a_standard_air_humidity_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下湿空气密度-设计")
    # 4标况下湿空气密度:校核
    a_standard_air_humidity_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下湿空气密度")
    # 4理论湿空气量:设计
    a_wet_air_volumn_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论湿空气量-设计")
    # 4理论湿空气量:校核
    a_wet_air_volumn_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论湿空气量-校核")
    # 5理论氮气容积:设计
    s_nitrogen_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论氮气容积-设计")
    # 5理论氮气容积:校核
    s_nitrogen_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论氮气容积-校核")
    # 5理论二氧化物容积:设计
    s_dioxide_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论二氧化物容积-设计")
    # 5理论二氧化物容积:校核
    s_dioxide_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论二氧化物容积-校核")
    # 5理论水蒸汽容积:设计
    s_steam_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论水蒸汽容积-设计")
    # 5理论水蒸汽容积:校核
    s_steam_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论水蒸汽容积-校核")
    # 5理论烟气容积:设计
    s_smoke_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论烟气容积-设计")
    # 5理论烟气容积:校核
    s_smoke_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论烟气容积-校核")
    # 51kg燃料生成理论湿烟气的重量:设计
    s_1kg_weight_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"1kg燃料生成理论湿烟气的重量-设计")
    # 51kg燃料生成理论湿烟气的重量:校核
    s_1kg_weight_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"1kg燃料生成理论湿烟气的重量-校核")
    # 5标况下理论湿烟气密度:设计
    s_wet_smoke_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下理论湿烟气密度-设计")
    # 5标况下理论湿烟气密度:校核
    s_wet_smoke_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下理论湿烟气密度-校核")
    # 6炉膛出口过剩空气系数:设计
    p_boiler_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉膛出口过剩空气系数-设计")
    # 6炉膛出口过剩空气系数:校核
    p_boiler_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉膛出口过剩空气系数-校核")
    # 6旋风分离器漏风系数:设计
    p_wind_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"旋风分离器漏风系数-设计")
    # 6旋风分离器漏风系数:校核
    p_wind_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"旋风分离器漏风系数-校核")
    # 6旋风分离器出口过剩空气系数:设计
    p_wind_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"旋风分离器出口过剩空气系数-设计")
    # 6旋风分离器出口过剩空气系数:校核
    p_wind_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"旋风分离器出口过剩空气系数-校核")
    # 6高过漏风系数:设计
    p_high_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高过漏风系数-设计")
    # 6高过漏风系数:校核
    p_high_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高过漏风系数-校核")
    # 6高过出口过剩空气系数:设计
    p_hign_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高过出口过剩空气系数-设计")
    # 6高过出口过剩空气系数:校核
    p_hign_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高过出口过剩空气系数-校核")
    # 6低过漏风系数:设计
    p_low_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低过漏风系数-设计")
    # 6低过漏风系数:校核
    p_low_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低过漏风系数-校核")
    # 6低过出口过剩空气系数:设计
    p_low_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低过出口过剩空气系数-设计")
    # 6低过出口过剩空气系数:校核
    p_low_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低过出口过剩空气系数-校核")
    # 6省燃料器漏风系数:设计
    p_fule_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"省燃料器漏风系数-设计")
    # 6省燃料器漏风系数:校核
    p_fule_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"省燃料器漏风系数-校核")
    # 6省燃料器出口过剩空气系数:设计
    p_fule_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"省燃料器出口过剩空气系数-设计")
    # 6省燃料器出口过剩空气系数:校核
    p_fule_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"省燃料器出口过剩空气系数-校核")
    # 6空预器漏风系数:设计
    p_heater_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器漏风系数-设计")
    # 6空预器漏风系数:校核
    p_heater_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器漏风系数-校核")
    # 6空预器出口过剩空气系数:设计
    p_heater_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口过剩空气系数-设计")
    # 6空预器出口过剩空气系数:校核
    p_heater_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口过剩空气系数-校核")
    # 6空予器至除尘器烟道漏风系数:设计
    p_plus_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空予器至除尘器烟道漏风系数-设计")
    # 6空予器至除尘器烟道漏风系数:校核
    p_plus_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空予器至除尘器烟道漏风系数-校核")
    # 6除尘器进口过剩空气系数:设计
    p_dust_exit_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口过剩空气系数-设计")
    # 6除尘器进口过剩空气系数:校核
    p_dust_exit_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口过剩空气系数-校核")
    # 6除尘器漏风系数:设计
    p_dust_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器漏风系数-设计")
    # 6除尘器漏风系数:校核
    p_dust_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器漏风系数-校核")
    # 6除尘器出口过剩空气系数:设计
    p_dust_entry_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口过剩空气系数-设计")
    # 6除尘器出口过剩空气系数:校核
    p_dust_entry_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口过剩空气系数-校核")
    # 6除尘器出口至引风机烟道漏风系数:设计
    p_plus_dust_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口至引风机烟道漏风系数-设计")
    # 6除尘器出口至引风机烟道漏风系数:校核
    p_plus_dust_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口至引风机烟道漏风系数-校核")
    # 6引风机入口过剩空气系数:设计
    p_fans_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机入口过剩空气系数-设计")
    # 6引风机入口过剩空气系数:校核
    p_fans_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机入口过剩空气系数-校核")
    # 61Kg燃料产生的空预器出口湿烟气容积:设计
    p_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"1Kg燃料产生的空预器出口湿烟气容积-设计")
    # 61Kg燃料产生的空预器出口湿烟气容积:校核
    p_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"1Kg燃料产生的空预器出口湿烟气容积-校核")
    # 61Kg燃料产生的空预器出口湿烟气质量:设计
    p_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"1Kg燃料产生的空预器出口湿烟气质量-设计")
    # 61Kg燃料产生的空预器出口湿烟气质量:校核
    p_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"1Kg燃料产生的空预器出口湿烟气质量-校核")
    # 6空预器:设计
    p_heater_type_design = db.Column(db.String(50), comment=u"空预器-设计")
    # 6空预器:校核
    p_heater_type_check = db.Column(db.String(50), comment=u"空预器-校核")
    # 6空预器一次风进口温度:设计
    p_heater_first_entry_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器一次风进口温度-设计")
    # 6空预器一次风进口温度:校核
    p_heater_first_entry_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器一次风进口温度-校核")
    # 6空预器二次风进口温度:设计
    p_heater_second_entry_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器二次风进口温度-设计")
    # 6空预器二次风进口温度:校核
    p_heater_second_entry_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器二次风进口温度-校核")
    # 6空预器一次风出口温度:设计
    p_heater_first_exit_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器一次风出口温度-设计")
    # 6空预器一次风出口温度:校核
    p_heater_first_exit_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器一次风出口温度-校核")
    # 6空预器二次风出口温度:设计
    p_heater_second_exit_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器二次风出口温度-设计")
    # 6空预器二次风出口温度:校核
    p_heater_second_exit_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器二次风出口温度-校核")
    # 6锅炉排烟温度:设计
    p_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉排烟温度-设计")
    # 6锅炉排烟温度:校核
    p_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉排烟温度-校核")
    # 7理论空气量（体积,湿）:设计
    a_theory_air_quality_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论空气量（体积,湿）-设计")
    # 7理论空气量（体积,湿）:校核
    a_theory_air_quality_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论空气量（体积,湿）-校核")
    # 7炉膛出口过剩空气系数:设计
    a_boiler_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉膛出口过剩空气系数-设计")
    # 7炉膛出口过剩空气系数:校核
    a_boiler_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉膛出口过剩空气系数-校核")
    # 7实际空气量（体积,湿）:设计
    a_actual_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际空气量（体积,湿）-设计")
    # 7实际空气量（体积,湿）:校核
    a_actual_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际空气量（体积,湿）-校核")
    # 7计算燃料消耗量:设计
    a_calculation_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算燃料消耗量-设计")
    # 7计算燃料消耗量:校核
    a_calculation_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算燃料消耗量-校核")
    # 7实际空气总量（体积，湿）:设计
    a_actual_air_total_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际空气总量（体积，湿）-设计")
    # 7实际空气总量（体积，湿）:校核
    a_actual_air_total_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际空气总量（体积，湿）-校核")
    # 7一次风份额:设计
    a_first_wind_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"一次风份额-设计")
    # 7一次风份额:校核
    a_first_wind_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"一次风份额-校核")
    # 7冷风温度（计算温度）:设计
    a_cwind_temperature_calculation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风温度（计算温度）-设计")
    # 7冷风温度（计算温度）:校核
    a_cwind_temperature_calculation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风温度（计算温度）-校核")
    # 7当地年平均气压:设计
    a_local_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地年平均气压-设计")
    # 7当地年平均气压:校核
    a_local_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地年平均气压-校核")
    # 7冷一次风量（湿-标准态）:设计
    a_first_cwind_standard_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风量（湿-标准态）-设计")
    # 7冷一次风量（湿-标准态）:校核
    a_first_cwind_standard_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风量（湿-标准态）-校核")
    # 7冷一次风量（湿-实态）:设计
    a_first_cwind_actual_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风量（湿-实态）-设计-校核")
    # 7冷一次风量（湿-实态）:校核
    a_first_cwind_actual_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风量（湿-实态）-校核")
    # 7标况下湿空气密度1:设计
    a_first_standard_air_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风标况下湿空气密度-设计")
    # 7标况下湿空气密度1:校核
    a_first_standard_air_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风标况下湿空气密度-校核")
    # 7冷一次风量（质量流量）:设计
    a_first_cwind_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风量（质量流量）-设计")
    # 7冷一次风量（质量流量）:校核
    a_first_cwind_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风量（质量流量）-校核")
    # 7冷一次风湿空气密度（湿-实态）:设计
    a_first_cwind_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风湿空气密度（湿-实态）-设计")
    # 7冷一次风湿空气密度（湿-实态）:校核
    a_first_cwind_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷一次风湿空气密度（湿-实态）-校核")
    # 7校核:设计
    a_check_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"校核值-设计")
    # 7校核:校核
    a_check_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"校核值-校核")
    # 7热一次风温度:设计
    a_first_hwind_temperatue_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热一次风温度-设计")
    # 7热一次风温度:校核
    a_first_hwind_temperatue_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热一次风温度-校核")
    # 7热一次风量（湿-实态）:设计
    a_first_hwind_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热一次风量（湿-实态）-设计")
    # 7热一次风量（湿-实态）:校核
    a_first_hwind_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热一次风量（湿-实态）-校核")
    # 7湿空气密度（湿-实态）1:设计
    a_first_wet_air_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热一次风湿空气密度（湿-实态）-设计")
    # 7湿空气密度（湿-实态）1:校核
    a_first_wet_air_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热一次风湿空气密度（湿-实态）-校核")
    # 7二次风份额:设计
    a_second_wind_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"二次风份额-设计")
    # 7二次风份额:校核
    a_second_wind_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"二次风份额-校核")
    # 7冷风温度:设计
    a_cwind_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风温度-设计")
    # 7冷风温度:校核
    a_cwind_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风温度-校核")
    # 7冷二次风量（湿-标准态）:设计
    a_second_cwind_standard_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风量（湿-标准态）-设计")
    # 7冷二次风量（湿-标准态）:校核
    a_second_cwind_standard_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风量（湿-标准态）-校核")
    # 7冷二次风量（湿-实态）:设计
    a_second_cwind_actual_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风量（湿-实态）-设计")
    # 7冷二次风量（湿-实态）:校核
    a_second_cwind_actual_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风量（湿-实态）-校核")
    # 7标况下湿空气密度2:设计
    a_second_standard_air_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风标况下湿空气密度-设计")
    # 7标况下湿空气密度2:校核
    a_second_standard_air_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风标况下湿空气密度-校核")
    # 7冷二次风量（质量流量）:设计
    a_second_cwind_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风标况下湿空气密度-设计")
    # 7冷二次风量（质量流量）:校核
    a_second_cwind_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风标况下湿空气密度-校核")
    # 7冷二次风湿空气密度（湿-实态）:设计
    a_second_cwind_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风湿空气密度（湿-实态）-设计")
    # 7冷二次风湿空气密度（湿-实态）:校核
    a_second_cwind_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷二次风湿空气密度（湿-实态）-校核")
    # 7热二次风温度:设计
    a_second_hwind_temperatue_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热二次风温度-设计")
    # 7热二次风温度:校核
    a_second_hwind_temperatue_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热二次风温度-校核")
    # 7热二次风量（湿-实态）:设计
    a_second_hwind_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热二次风量（湿-实态）-设计")
    # 7热二次风量（湿-实态）:校核
    a_second_hwind_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热二次风量（湿-实态）-校核")
    # 7湿空气密度（湿-实态）2:设计
    a_second_wet_air_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热二次风湿空气密度（湿-实态）-设计")
    # 7湿空气密度（湿-实态）2:校核
    a_second_wet_air_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热二次风湿空气密度（湿-实态）-校核")
    # 8标况下空预器出口1Kg燃料湿烟气容积:设计
    h_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下空预器出口1Kg燃料湿烟气容积-设计")
    # 8标况下空预器出口1Kg燃料湿烟气容积:校核
    h_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下空预器出口1Kg燃料湿烟气容积-校核")
    # 8空预器出口1Kg燃料产生的湿烟气质量:设计
    h_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口1Kg燃料产生的湿烟气质量-设计")
    # 8空预器出口1Kg燃料产生的湿烟气质量:校核
    h_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口1Kg燃料产生的湿烟气质量-校核")
    # 8计算燃料消耗量:设计
    h_calculation_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算燃料消耗量-设计")
    # 8计算燃料消耗量:校核
    h_calculation_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算燃料消耗量-校核")
    # 8标况下空预器出口烟气容积流量:设计
    h_standard_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下空预器出口烟气容积流量-设计")
    # 8标况下空预器出口烟气容积流量:校核
    h_standard_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下空预器出口烟气容积流量-校核")
    # 8空预器出口烟气质量流量:设计
    h_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口烟气质量流量-设计")
    # 8空预器出口烟气质量流量:校核
    h_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口烟气质量流量-校核")
    # 8锅炉空预器出口排烟温度:设计
    h_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉空预器出口排烟温度-设计")
    # 8锅炉空预器出口排烟温度:校核
    h_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉空预器出口排烟温度-校核")
    # 8空预器出口烟气容积量(实态）:设计
    h_smoke_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口烟气容积量(实态）-设计")
    # 8空预器出口烟气容积量(实态）:校核
    h_smoke_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口烟气容积量(实态）-校核")
    # 8烟气密度（实态）:设计
    h_smoke_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气密度（实态）-设计")
    # 8烟气密度（实态）:校核
    h_smoke_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气密度（实态）-校核")
    # 9空预器出口过剩空气系数:设计
    d_exit_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口过剩空气系数-设计")
    # 9空预器出口过剩空气系数:校核
    d_exit_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器出口过剩空气系数-校核")
    # 9空预器至除尘器烟道漏风系数:设计
    d_wind_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器至除尘器烟道漏风系数-设计")
    # 9空预器至除尘器烟道漏风系数:校核
    d_wind_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空预器至除尘器烟道漏风系数-校核")
    # 9除尘器进口过剩空气系数:设计
    d_entry_air_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口过剩空气系数-设计")
    # 9除尘器进口过剩空气系数:校核
    d_entry_air_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口过剩空气系数-校核")
    # 9冷空气温度:设计
    d_cold_air_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷空气温度-设计")
    # 9冷空气温度:校核
    d_cold_air_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷空气温度-校核")
    # 9除尘器进口处烟气温度:设计
    d_entry_somke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气温度-设计")
    # 9除尘器进口处烟气温度:校核
    d_entry_somke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气温度-校核")
    # 9标况下除尘器进口处1kg燃料湿烟气容积:设计
    d_standard_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器进口处1kg燃料湿烟气容积-设计")
    # 9标况下除尘器进口处1kg燃料湿烟气容积:校核
    d_standard_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器进口处1kg燃料湿烟气容积-校核")
    # 9除尘器进口处1kg燃料湿烟气质量:设计
    d_entry_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处1kg燃料湿烟气质量-设计")
    # 9除尘器进口处1kg燃料湿烟气质量:校核
    d_entry_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处1kg燃料湿烟气质量-校核")
    # 9标况下除尘器进口烟气容积流量:设计
    d_standard_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器进口烟气容积流量-设计")
    # 9标况下除尘器进口烟气容积流量:校核
    d_standard_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器进口烟气容积流量-校核")
    # 9除尘器进口处烟气质量流量:设计
    d_entry_somke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气质量流量-设计")
    # 9除尘器进口处烟气质量流量:校核
    d_entry_somke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气质量流量-校核")
    # 9除尘器进口处烟气容积流量(实态）:设计
    d_entry_smoke_actual_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气容积流量(实态）-设计")
    # 9除尘器进口处烟气容积流量(实态）:校核
    d_entry_smoke_actual_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气容积流量(实态）-校核")
    # 10除尘器漏风系数:设计
    e_wind_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器漏风系数-设计")
    # 10除尘器漏风系数:校核
    e_wind_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器漏风系数-校核")
    # 10除尘器出口过剩空气系数:设计
    e_air_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口过剩空气系数-设计")
    # 10除尘器出口过剩空气系数:校核
    e_air_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口过剩空气系数-校核")
    # 10除尘器出口烟气温度:设计
    e_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口烟气温度-设计")
    # 10除尘器出口烟气温度:校核
    e_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口烟气温度-校核")
    # 10标况下除尘器出口处1kg燃料湿烟气容积:设计
    e_standard_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器出口处1kg燃料湿烟气容积-设计")
    # 10标况下除尘器出口处1kg燃料湿烟气容积:校核
    e_standard_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器出口处1kg燃料湿烟气容积-校核")
    # 10除尘器出口处1kg燃料湿烟气质量:设计
    e_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口处1kg燃料湿烟气质量-设计")
    # 10除尘器出口处1kg燃料湿烟气质量:校核
    e_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口处1kg燃料湿烟气质量-校核")
    # 10标况下除尘器出口湿烟气容积流量:设计
    e_standard_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器出口湿烟气容积流量-设计")
    # 10标况下除尘器出口湿烟气容积流量:校核
    e_standard_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器出口湿烟气容积流量-校核")
    # 10除尘器出口处湿烟气质量流量:设计
    e_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口处湿烟气质量流量-设计")
    # 10除尘器出口处湿烟气质量流量:校核
    e_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口处湿烟气质量流量-校核")
    # 10除尘器出口处湿烟气容积流量(实态）:设计
    e_smoke_actual_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口处湿烟气容积流量(实态）-设计")
    # 10除尘器出口处湿烟气容积流量(实态）:校核
    e_smoke_actual_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口处湿烟气容积流量(实态）-校核")
    # 10烟气密度（实态）:设计
    e_smoke_actual_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气密度（实态）-设计")
    # 10烟气密度（实态）:校核
    e_smoke_actual_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气密度（实态）-校核")
    # 11除尘器出口至引风机烟道漏风系数:设计
    i_wind_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口至引风机烟道漏风系数-设计")
    # 11除尘器出口至引风机烟道漏风系数:校核
    i_wind_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器出口至引风机烟道漏风系数-校核")
    # 11引风机入口过剩空气系数:设计
    i_air_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机入口过剩空气系数-设计")
    # 11引风机入口过剩空气系数:校核
    i_air_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机入口过剩空气系数-校核")
    # 11引风机入口烟气温度:设计
    i_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机入口烟气温度-设计")
    # 11引风机入口烟气温度:校核
    i_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机入口烟气温度-校核")
    # 11标况下引风机进口处1kg燃料湿烟气容积:设计
    i_standard_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下引风机进口处1kg燃料湿烟气容积-设计")
    # 11标况下引风机进口处1kg燃料湿烟气容积:校核
    i_standard_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下引风机进口处1kg燃料湿烟气容积-校核")
    # 11引风机进口处1kg燃料湿烟气质量:设计
    i_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口处1kg燃料湿烟气质量-设计")
    # 11引风机进口处1kg燃料湿烟气质量:校核
    i_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口处1kg燃料湿烟气质量-校核")
    # 11标况下引风机进口湿烟气容积流量1:设计
    i_standard_smoke_flow1_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下引风机进口湿烟气容积流量-设计")
    # 11标况下引风机进口湿烟气容积流量1:校核
    i_standard_smoke_flow1_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下引风机进口湿烟气容积流量-校核")
    # 11标况下引风机进口湿烟气容积流量2:设计
    i_standard_smoke_flow2_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下引风机进口湿烟气容积流量Nm3/s-设计")
    # 11标况下引风机进口湿烟气容积流量2:校核
    i_standard_smoke_flow2_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下引风机进口湿烟气容积流量Nm3/s-校核")
    # 11引风机进口处湿烟气质量流量:设计
    i_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口处湿烟气质量流量-设计")
    # 11引风机进口处湿烟气质量流量:校核
    i_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口处湿烟气质量流量-校核")
    # 11引风机进口处湿烟气容积流量(实态）1:设计
    i_smoke_actual_flow1_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口处湿烟气容积流量(实态）-设计")
    # 11引风机进口处湿烟气容积流量(实态）1:校核
    i_smoke_actual_flow1_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口处湿烟气容积流量(实态）-校核")
    # 11引风机进口处湿烟气容积流量(实态）2:设计
    i_smoke_actual_flow2_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口处湿烟气容积流量(实态）Vxfc-设计")
    # 11引风机进口处湿烟气容积流量(实态）2:校核
    i_smoke_actual_flow2_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口处湿烟气容积流量(实态）Vxfc-校核")
    # 11烟气密度（实态）:设计
    i_smoke_actual_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气密度（实态）-设计")
    # 11烟气密度（实态）:校核
    i_smoke_actual_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气密度（实态）-校核")
    # 11引风机处计算湿烟气密度（标况）:设计
    i_wet_smoke_actual_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机处计算湿烟气密度（标况）-设计")
    # 11引风机处计算湿烟气密度（标况）:校核
    i_wet_smoke_actual_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机处计算湿烟气密度（标况）-校核")
    # 12烟气中的氧量:设计
    go_oxygen_vol_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中的氧量-设计")
    # 12烟气中的氧量:校核
    go_oxygen_vol_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中的氧量-校核")
    # 12理论干烟气容积:设计
    go_theoretica_vol_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论干烟气容积-设计")
    # 12理论干烟气容积:校核
    go_theoretica_vol_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论干烟气容积-校核")
    # 12理论干空气量:设计
    go_theoretica_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论干空气量-设计")
    # 12理论干空气量:校核
    go_theoretica_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论干空气量-校核")
    # 12计算燃料消耗量:设计
    go_calculation_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算燃料消耗量-设计")
    # 12计算燃料消耗量:校核
    go_calculation_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算燃料消耗量-校核")
    # 12引风机入口过剩空气系数:设计
    go_air_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机入口过剩空气系数-设计")
    # 12引风机入口过剩空气系数:校核
    go_air_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机入口过剩空气系数-校核")
    # 121Kg燃料产生的引风机进口干烟气容积:设计
    go_standard_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"1Kg燃料产生的引风机进口干烟气容积-设计")
    # 121Kg燃料产生的引风机进口干烟气容积:校核
    go_standard_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"1Kg燃料产生的引风机进口干烟气容积-校核")
    # 12引风机进口干烟气容积流量:设计
    go_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口干烟气容积流量-设计")
    # 12引风机进口干烟气容积流量:校核
    go_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口干烟气容积流量-校核")
    # 12干烟气中含氧量:设计
    go_drygas_oxygen_vol_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干烟气中含氧量-设计")
    # 12干烟气中含氧量:校核
    go_drygas_oxygen_vol_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干烟气中含氧量-校核")
    # 12总燃烧产物6%O2干体积:设计
    go_total_combustion_product_vol_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总燃烧产物6%O2干体积-设计")
    # 12总燃烧产物6%O2干体积:校核
    go_total_combustion_product_vol_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总燃烧产物6%O2干体积-校核")
    # 锅炉种类
    boiler_type = db.Column(db.String(100), comment=u"锅炉种类")
    # 压力温度
    pressure_temperature = db.Column(db.String(100), comment=u"压力温度")

    def __init__(self, **kwargs):
        super(BiomassCHPBoilerCalculation, self).__init__(**kwargs)

    @staticmethod
    def insert_furnace_calculation(biomassCHPFurnaceCalculation):
        try:
            db.session.add(biomassCHPFurnaceCalculation)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassCHPFurnaceCalculation"
                  "<id=%s> in database" % (biomassCHPFurnaceCalculation.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_furnace_calculation(plan_id):
        result = BiomassCHPBoilerCalculation.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_furnace_calculation(plan_id):
        furnace_calculation = \
            BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
        try:
            db.session.delete(furnace_calculation)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete furnace_calculation<id=%s, plan_id=%s> in database" %
                  (furnace_calculation.id, furnace_calculation.plan_id))


# 燃料存储及输送系统表
class BiomassCHPFuelStorageTransportation  (db.Model):
    # 表名
    __tablename__ = 'biomasschp_fuel_st'  
    __table_args__ = {'comment': u'生物质热电燃料存储及输送系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))

    # 1锅炉额定燃料耗量:设计
    b_rated_fuel_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-锅炉额定燃料耗量-设计")
    # 1锅炉额定燃料耗量:校核
    b_rated_fuel_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-锅炉额定燃料耗量-校核")
    # 1锅炉日利用小时数:设计
    b_saily_use_hours_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-锅炉日利用小时数-设计")
    # 1锅炉日利用小时数:校核
    b_saily_use_hours_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-锅炉日利用小时数-校核")
    # 1日耗量:设计
    b_daily_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-日耗量-设计")
    # 1日耗量:校核
    b_daily_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-日耗量-校核")
    # 1锅炉年利用小时数:设计
    b_annual_use_hours_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-锅炉年利用小时数-设计")
    # 1锅炉年利用小时数:校核
    b_annual_use_hours_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-锅炉年利用小时数-校核")
    # 1年耗量:设计
    b_year_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-年耗量-设计")
    # 1年耗量:校核
    b_year_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-年耗量-校核")
    # 1不均衡系数:设计
    b_unbalance_coefficient_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-不均衡系数-设计")
    # 1不均衡系数:校核
    b_unbalance_coefficient_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-不均衡系数-校核")
    # 1日进厂燃料量:设计
    b_daily_fuel_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-日进厂燃料量-设计")
    # 1日进厂燃料量:校核
    b_daily_fuel_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-日进厂燃料量-校核")
    # 1运载车辆载重:设计
    b_carrying_vehicle_load_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-运载车辆载重-设计")
    # 1运载车辆载重:校核
    b_carrying_vehicle_load_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-运载车辆载重-校核")
    # 1日进厂车辆:设计
    b_daily_vehicle_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-日进厂车辆-设计")
    # 1日进厂车辆:校核
    b_daily_vehicle_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉燃料耗量-日进厂车辆-校核")
    # 2燃料的储备日数:设计
    s_fuel_reserve_days_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-燃料的储备日数-设计")
    # 2燃料的储备日数:校核
    s_fuel_reserve_days_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-燃料的储备日数-校核")
    # 2燃料可存储量:设计
    s_fuel_available_reserves_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-燃料可存储量-设计")
    # 2燃料可存储量:校核
    s_fuel_available_reserves_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-燃料可存储量-校核")
    # 2计算堆料系数:设计
    s_aggregate_coefficient_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-计算堆料系数-设计")
    # 2计算堆料系数:校核
    s_aggregate_coefficient_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-计算堆料系数-校核")
    # 2平均堆高:设计
    s_average_stack_height_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-平均堆高-设计")
    # 2平均堆高:校核
    s_average_stack_height_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-平均堆高-校核")
    # 2燃料堆积密度:设计
    s_fuel_bulk_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-燃料堆积密度-设计")
    # 2燃料堆积密度:校核
    s_fuel_bulk_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-燃料堆积密度-校核")
    # 2原料堆场面积:设计
    s_yardarea_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-设计")
    # 2原料堆场面积:校核
    s_yardarea_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"原料堆场面积-校核")
    # 3燃料的储备日数:设计
    d_fuel_reserve_days_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-燃料的储备日数-设计")
    # 3燃料的储备日数:校核
    d_fuel_reserve_days_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-燃料的储备日数-校核")
    # 3燃料可存储量:设计
    d_fuel_available_reserves_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-燃料可存储量-设计")
    # 3燃料可存储量:校核
    d_fuel_available_reserves_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-燃料可存储量-校核")
    # 3计算堆料系数:设计
    d_aggregate_coefficient_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-计算堆料系数-设计")
    # 3计算堆料系数:校核
    d_aggregate_coefficient_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-计算堆料系数-校核")
    # 3平均堆高:设计
    d_average_stack_height_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-平均堆高-设计")
    # 3平均堆高:校核
    d_average_stack_height_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-平均堆高-校核")
    # 3燃料堆积密度:设计
    d_fuel_bulk_density_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-燃料堆积密度-设计")
    # 3燃料堆积密度:校核
    d_fuel_bulk_density_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-燃料堆积密度-校核")
    # 3原料堆场面积:设计
    d_yardarea_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-原料堆场面积-设计")
    # 3原料堆场面积:校核
    d_yardarea_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干料棚面积-原料堆场面积-校核")
    # 4锅炉额定燃料耗量:设计
    t_rated_fuel_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-锅炉额定燃料耗量-设计")
    # 4锅炉额定燃料耗量:校核
    t_rated_fuel_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-锅炉额定燃料耗量-校核")
    # 4消耗小时数:设计
    t_hourage_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-消耗小时数-设计")
    # 4消耗小时数:校核
    t_hourage_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-消耗小时数-校核")
    # 4料仓数量:设计
    t_bin_quantity_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-料仓数量-设计")
    # 4料仓数量:校核
    t_bin_quantity_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-料仓数量-校核")
    # 4总有效容积:设计
    t_total_effective_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-总有效容积-设计")
    # 4总有效容积:校核
    t_total_effective_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-总有效容积-校核")
    # 4单个料仓有效容积-计算:设计
    t_single_effective_volume_calculation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-单个料仓有效容积-计算-设计")
    # 4单个料仓有效容积-计算:校核
    t_single_effective_volume_calculation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-单个料仓有效容积-计算-校核")
    # 4单个料仓有效容积-选定:设计
    t_single_effective_volume_selected_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-单个料仓有效容积-选定-设计")
    # 4单个料仓有效容积-选定:校核
    t_single_effective_volume_selected_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-单个料仓有效容积-选定-校核")
    # 4反推消耗小时数:设计
    t_consumption_hours_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-反推消耗小时数-设计")
    # 4反推消耗小时数:校核
    t_consumption_hours_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部料仓有效容积-反推消耗小时数-校核")
    # 5锅炉额定燃料耗量:设计
    f_rated_fuel_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-锅炉额定燃料耗量-设计")
    # 5锅炉额定燃料耗量:校核
    f_rated_fuel_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-锅炉额定燃料耗量-校核")
    # 5双螺旋给料机组数:设计
    f_duplex_number_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-双螺旋给料机组数-设计")
    # 5双螺旋给料机组数:校核
    f_duplex_number_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-双螺旋给料机组数-校核")
    # 5富裕量:设计
    f_flushness_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-富裕量-设计")
    # 5富裕量:校核
    f_flushness_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-富裕量-校核")
    # 5双螺旋给料机总出力:设计
    f_duplex_output_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-双螺旋给料机总出力-设计")
    # 5双螺旋给料机总出力:校核
    f_duplex_output_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-双螺旋给料机总出力-校核")
    # 5单组双螺旋给料机出力:设计
    f_single_duplex_output_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-单组双螺旋给料机出力-设计")
    # 5单组双螺旋给料机出力:校核
    f_single_duplex_output_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尾部螺旋给料机-单组双螺旋给料机出力-校核")
    # 5单台锅炉额定耗煤量:设计
    f_single_rated_fuel_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上料系统-单台锅炉额定耗煤量-设计")
    # 5单台锅炉额定耗煤量:校核
    f_single_rated_fuel_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上料系统-单台锅炉额定耗煤量-校核")
    # 5日耗量:设计
    f_daily_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上料系统-日耗量-设计")
    # 5日耗量:校核
    f_daily_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上料系统-日耗量-校核")
    # 5上料系统出力—计算:设计
    f_feeding_output_calculation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上料系统出力—计算-设计")
    # 5上料系统出力—计算:校核
    f_feeding_output_calculation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上料系统出力—计算-校核")
    # 5上料系统出力—选定:设计
    f_feeding_output_selected_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上料系统出力—选定-设计")
    # 5上料系统出力—选定:校核
    f_feeding_output_selected_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上料系统出力—选定-校核")
    # 5皮带宽度:设计
    f_belt_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"皮带宽度")
    # 5断面系数:设计
    f_section_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"断面系数")
    # 5皮带速度:设计
    f_belt_speed = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"皮带速度")
    # 5物料松散密度:设计
    f_loose_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"物料松散密度")
    # 5皮带最大输送能力:设计
    f_belt_max_delivery = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"皮带最大输送能力")
    # 5皮带单路/双路
    f_belt_number = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"皮带单双路")

    # 6锅炉额定燃料耗量:设计
    bs_rated_fuel_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-锅炉额定燃料耗量-设计")
    # 6锅炉额定燃料耗量:校核
    bs_rated_fuel_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-锅炉额定燃料耗量-校核")
    # 6消耗小时数:设计
    b_hourage_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-消耗小时数-设计")
    # 6消耗小时数:校核
    b_hourage_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-消耗小时数-校核")
    # 6料仓数量:设计
    b_bin_quantity_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-料仓数量-设计")
    # 6料仓数量:校核
    b_bin_quantity_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-料仓数量-校核")
    # 6总有效容积:设计
    b_total_effective_volume_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-总有效容积-设计")
    # 6总有效容积:校核
    b_total_effective_volume_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-总有效容积-校核")
    # 6单个料仓有效容积-计算:设计
    b_single_effective_volume_calculation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-单个料仓有效容积-计算-设计")
    # 6单个料仓有效容积-计算:校核
    b_single_effective_volume_calculation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-单个料仓有效容积-计算-校核")
    # 6单个料仓有效容积-选定:设计
    b_single_effective_volume_selected_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-单个料仓有效容积-选定-设计")
    # 6单个料仓有效容积-选定:校核
    b_single_effective_volume_selected_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-单个料仓有效容积-选定-校核")
    # 6反推消耗小时数:设计
    b_consumption_hours_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-反推消耗小时数-设计")
    # 6反推消耗小时数:校核
    b_consumption_hours_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前料仓-反推消耗小时数-校核")
    # 7锅炉额定燃料耗量:设计
    s_rated_fuel_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-锅炉额定燃料耗量-设计")
    # 7锅炉额定燃料耗量:校核
    s_rated_fuel_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-锅炉额定燃料耗量-校核")
    # 7双螺旋给料机组数:设计
    s_duplex_number_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-双螺旋给料机组数-设计")
    # 7双螺旋给料机组数:校核
    s_duplex_number_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-双螺旋给料机组数-校核")
    # 7富裕量:设计
    s_flushness_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-富裕量-设计")
    # 7富裕量:校核
    s_flushness_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-富裕量-校核")
    # 7双螺旋给料机总出力:设计
    s_duplex_output_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-双螺旋给料机总出力-设计")
    # 7双螺旋给料机总出力:校核
    s_duplex_output_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-双螺旋给料机总出力-校核")
    # 7单组双螺旋给料机出力:设计
    s_single_duplex_output_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-单组双螺旋给料机出力-设计")
    # 7单组双螺旋给料机出力:校核
    s_single_duplex_output_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉前螺旋给料机-单组双螺旋给料机出力-校核")
    
    def __init__(self, **kwargs):
        super(BiomassCHPFuelStorageTransportation, self).__init__(**kwargs)

    @staticmethod
    def insert_storage_transportation(biomassCHPFuelStorTran):
        try:
            db.session.add(biomassCHPFuelStorTran)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassCHPFuelStorTran"
                  "<id=%s> in database" % (biomassCHPFuelStorTran.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_storage_transportation(plan_id):
        result = BiomassCHPFuelStorageTransportation.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_storage_transportation(plan_id):
        storage_transportation = \
            BiomassCHPFuelStorageTransportation.search_storage_transportation(plan_id)
        try:
            db.session.delete(storage_transportation)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete storage_transportation<id=%s, plan_id=%s> in database" %
                  (storage_transportation.id, storage_transportation.plan_id))


# 脱硫脱硝系统表
class BiomassCHPDesulfurizationAndDenitrification(db.Model):
    # 表名
    __tablename__ = 'biomasschp_des_den'  
    __table_args__ = {'comment': u'生物质热电燃料脱硫脱硝系统表'} 

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))
    
    # 1收到基硫份:设计
    s_sulfur_content_received = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基硫份")
    # 1计算耗料量:设计
    s_feed_consumption = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算耗料量")
    # 1燃料中的含硫量燃烧后氧化成SO2的份额:设计
    s_fuel_so2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃料中的含硫量燃烧后氧化成SO2的份额")
    # 1脱硫前烟气中的SO2含量:设计
    s_before_so2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硫前烟气中的SO2含量")
    # 1引风机进口烟气容积流量（标况）:设计
    s_input_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口烟气容积流量（标况）")
    # 1未脱硫前SO2浓度（标态）:设计
    s_no_before_so2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"未脱硫前SO2浓度（标态）")
    # 1脱硫效率:设计
    s_desulfurization_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硫效率")
    # 1脱硫后SO2浓度（标态）:设计
    s_after_so2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硫后SO2浓度（标态）")
    # 1环保要求SO2的排放浓度:设计
    s_env_after_so2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"环保要求SO2的排放浓度")
    # 1脱硫后SO2排放量（标态）:设计
    s_after_so2_discharge = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硫后SO2排放量（标态）")
    # 2炉内脱硫百分比:设计
    c_desulfurization_percentage = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硫百分比")
    # 2炉内脱硫后SO2浓度:设计
    c_after_so2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硫后SO2浓度")
    # 2脱除SO2质量:设计
    c_so2_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱除SO2质量")
    # 2脱除SO2摩尔量:设计
    c_so2_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱除SO2摩尔量")
    # 2钙硫摩尔比:设计
    c_sulfur_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"钙硫摩尔比")
    # 2反应所需CaCO3摩尔量:设计
    c_caco3_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"反应所需CaCO3摩尔量")
    # 2反应所需CaCO3质量:设计
    c_caco3_quality_require = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"反应所需CaCO3质量")
    # 2参加反应CaCO3质量:设计
    c_caco3_quality_reaction = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"参加反应CaCO3质量")
    # 2反应生成CaSO4质量:设计
    c_caso4_quality_generation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"反应生成CaSO4质量")
    # 2反应后质量增加:设计
    c_after_quality_add = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"反应后质量增加")
    # 2石灰石纯度:设计
    c_limestone_purity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石纯度")
    # 2石灰石耗量:设计
    c_limestone_consumption = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石耗量")
    # 2炉内脱硫产生的灰渣量:设计
    c_ash = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硫产生的灰渣量")
    # 2石灰石粉仓储存时间:设计
    c_limestone_storage_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉仓储存时间")
    # 2石灰石粉仓出力:设计
    c_limestone_output = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉仓出力")
    # 2石灰石粉堆积密度:设计
    c_limestone_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉堆积密度")
    # 2石灰石粉仓充满系数:设计
    c_limestone_fullness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉仓充满系数")
    # 2石灰石粉仓体积:设计
    c_limestone_volumn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉仓体积")
    # 2高:设计
    c_limestone_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高")
    # 2直径:设计
    c_limestone_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"直径")
    # 3脱硝前NOX浓度:设计
    n_before_nox_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硝前NOX浓度")
    # 3引风机进口烟气容积流量（标况）:设计
    n_input_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口烟气容积流量（标况）")
    # 3脱硝效率(总效率):设计
    n_desulfurization_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硝效率(总效率)")
    # 3脱硝前NOX排放量:设计
    n_before_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硝前NOX排放量")
    # 3脱硝后NOX浓度:设计
    n_after_nox_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硝后NOX浓度")
    # 3环保要求NOX的排放浓度:设计
    n_env_after_nox_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"环保要求NOX的排放浓度")
    # 3脱硝后NOX排放量:设计
    n_after_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硝后NOX排放量")
    # 4炉内脱硝百分比:设计
    d_denitration_percentage = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硝百分比")
    # 4炉内脱硝量:设计
    d_denitration_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硝量")
    # 4炉内脱硝后NOX排放量:设计
    d_after_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硝后NOX排放量")
    # 4炉内脱硝摩尔量:设计
    d_denitration_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硝摩尔量")
    # 4氨逃逸率:设计
    d_escape_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氨逃逸率")
    # 4氨逃逸量:设计
    d_escape_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氨逃逸量")
    # 4逃逸氨折算尿素量:设计
    d_escape_quality_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"逃逸氨折算尿素量")
    # 4NH3/NOX摩尔比:设计
    d_nh3nox_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"NH3/NOX摩尔比")
    # 4尿素/NOX摩尔比:设计
    d_urea_nox_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素/NOX摩尔比")
    # 4尿素/NOX式量比:设计
    d_urea_nox_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素/NOX式量比")
    # 4理论尿素消耗量:设计
    d_theory_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论尿素消耗量")
    # 4尿素用量(一台炉):设计
    d_use_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素用量(一台炉)")
    # 4尿素溶液消耗水量(一台炉):设计
    d_water_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素溶液消耗水量(一台炉)")
    # 4尿素仓库天数:设计
    d_days_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素仓库天数")
    # 4尿素仓库容量:设计
    d_capacity_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素仓库容量")

    def __init__(self, **kwargs):
        super(BiomassCHPDesulfurizationAndDenitrification, self).__init__(**kwargs)

    @staticmethod
    def insert_des_den(biomassCHPDesDen):
        try:
            db.session.add(biomassCHPDesDen)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassCHPDesDen"
                  "<id=%s> in database" % (biomassCHPDesDen.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_des_den(plan_id):
        result = BiomassCHPDesulfurizationAndDenitrification.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_des_den(plan_id):
        des_den = \
            BiomassCHPDesulfurizationAndDenitrification.search_des_den(plan_id)
        try:
            db.session.delete(des_den)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete des_den<id=%s, plan_id=%s> in database" %
                  (des_den.id, des_den.plan_id))



# 除尘除灰除渣系统表
class BiomassCHPDASRemove(db.Model):
    # 表名
    __tablename__ = 'biomasschp_das_remove'  
    __table_args__ = {'comment': u'生物质热电联产除尘除灰除渣系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))

    # 1灰渣总量(炉内脱硫后):设计
    d_total_ash = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰渣总量")
    # 1飞灰份额:设计
    d_flyash_fraction = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"飞灰份额")
    # 1除尘器入口（锅炉出口）飞灰量:设计
    d_entry_flyash = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器入口飞灰量")
    # 1标况下除尘器进口烟气容积流量:设计
    d_standard_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器进口烟气容积流量")
    # 1除尘器进口处烟气容积流量(实态）:设计
    d_actual_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气容积流量(实态）")
    # 1标况下除尘器进口烟气浓度:设计
    d_standard_smoke_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器进口烟气浓度")
    # 1除尘器进口处烟气浓度(实态）:设计
    d_actual_smoke_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气浓度(实态）")
    # 1综合除尘效率:设计
    d_dust_remove_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"综合除尘效率")
    # 1除尘器（烟囱）出口烟气浓度（标况）:设计
    d_exit_smoke_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器（烟囱）出口烟气浓度（标况）")
    # 1除尘器（烟囱）出口烟气飞灰量（标况）:设计
    d_exit_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器（烟囱）出口烟气飞灰量（标况）")
    # 1除尘器下灰量:设计
    d_dust_wiper_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器下灰量")
    # 1引风机进口烟气容积量(实态）:设计
    d_entry_smoke_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口烟气容积量(实态）")
    # 1烟囱出口烟气浓度（实态）:设计
    d_tun_exit_smoke_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口烟气浓度（实态）")
    # 1环保要求颗粒物的排放浓度:设计
    d_env_particulate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"环保要求颗粒物的排放浓度")
    # 2除灰系统出力:设计
    a_remove_output = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除灰系统出力")
    # 2干灰堆积密度:设计
    a_bulk_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干灰堆积密度")
    # 2灰仓充满系数:设计
    a_fullness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰仓充满系数")
    # 2存灰时间:设计
    a_storage_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"存灰时间")
    # 2灰仓有效容积:设计
    a_volumn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰仓有效容积")
    # 2直径:设计
    a_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰仓直径")
    # 2高度:设计
    a_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰仓高度")
    # 2灰气比:设计
    a_ratio = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰气比")
    # 2输灰系统耗气量:设计
    a_gas_consumption = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"输灰系统耗气量")
    # 3渣量:设计
    s_slag_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"渣量")
    # 3冷渣机的出力（单台）:设计
    s_yns_output = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷渣机的出力（单台）")
    # 3冷却水量（单台）:设计
    s_coolwater = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水量（单台）")
    # 3冷渣机台数:设计
    s_yns_number = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷渣机台数")
    # 3除渣系统出力:设计
    s_slag_output = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除渣系统出力")
    # 3链斗输送机出力:设计
    s_conveyor_output = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"链斗输送机出力")
    # 3冷渣堆积密度:设计
    s_bulk_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷渣堆积密度")
    # 3渣库充满系数:设计
    s_fullness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"渣库充满系数")
    # 3存渣时间:设计
    s_storage_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"存渣时间")
    # 3钢渣仓有效容积:设计
    s_volumn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"钢渣仓有效容积")
    # 3直径:设计
    s_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"钢渣仓直径")
    # 3高度:设计
    s_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"钢渣仓高度")

    
    def __init__(self, **kwargs):
        super(BiomassCHPDASRemove, self).__init__(**kwargs)

    @staticmethod
    def insert_dasRemove(biomassDASRemove):
        try:
            db.session.add(biomassDASRemove)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassDASRemove"
                  "<id=%s> in database" % (biomassDASRemove.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_dasRemove(plan_id):
        result = BiomassCHPDASRemove.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_dasRemove(plan_id):
        dasRemove = \
            BiomassCHPDASRemove.search_dasRemove(plan_id)
        try:
            db.session.delete(dasRemove)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete dasRemove<id=%s, plan_id=%s> in database" %
                  (dasRemove.id, dasRemove.plan_id))

# 烟囱表
class BiomassCHPChimney(db.Model):
    # 表名
    __tablename__ = 'biomasschp_chimney'
    __table_args__ = {'comment': u'生物质热电联产烟囱表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    '''烟囱抽力计算'''
    # 烟囱高度
    chimney_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：烟囱高度")
    # 当地大气压
    local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：当地大气压")
    # 标态下空气密度
    standard_air_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：标态下空气密度")
    # 标态下平均烟气密度
    standard_average_smoke_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：标态下平均烟气密度")
    # 标态下计算烟气密度
    standard_calculated_smoke_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：标态下计算烟气密度")
    # 室外空气温度
    outdoor_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：室外空气温度")
    # 烟囱进口处烟温
    chimney_inlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：烟囱进口处烟温")
    # 烟囱每米高度的温度降
    chimney_temperature_drop_per_meter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：烟囱每米高度的温度降")
    # 烟囱内平均温度
    chimney_average_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：烟囱内平均温度")
    # 烟囱抽力
    chimney_draft = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱抽力")

    '''烟囱出口内径计算及低负荷校核'''
    # 烟气量
    smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气量")
    # 烟囱出口温度
    chimney_outlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口温度")
    # 烟囱出口流速
    chimney_outlet_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口流速")
    # 烟囱出口内径
    chimney_outlet_inner_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口内径")
    # 选取烟囱出口内径
    chimney_outlet_selected_inner_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"选取烟囱出口内径")
    # 经验烟囱基础内径
    chimney_experience_base_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"经验烟囱基础内径")
    # 低负荷下烟气量
    low_load_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低负荷下烟气量")
    # 低负荷下排烟温度
    low_load_smoke_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低负荷下排烟温度")
    # 30%低负荷校核流速
    low_load_flow_30_percent = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"30%低负荷校核流速")

    '''烟囱阻力计算'''
    # 烟囱阻力系数
    chimney_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱阻力系数")
    # 烟囱内平均流速
    chimney_average_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱内平均流速")
    # 烟囱平均直径
    chimney_average_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱平均直径")
    # 烟囱摩擦阻力
    chimney_friction_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱摩擦阻力")
    # 烟囱出口阻力系数
    chimney_outlet_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口阻力系数")
    # 烟囱出口阻力
    chimney_outlet_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口阻力")
    # 烟囱总阻力
    chimney_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱总阻力")

    def __init__(self, **kwargs):
        super(BiomassCHPChimney, self).__init__(**kwargs)

    @staticmethod
    def insert_biomassCHPChimney(biomassCHPChimney):
        try:
            db.session.add(biomassCHPChimney)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassCHPChimney"
                  "<id=%s> in database" % (biomassCHPChimney.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_biomassCHPChimney(plan_id):
        result = BiomassCHPChimney.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_biomassCHPChimney(plan_id):
        biomassCHPChimney = BiomassCHPChimney.search_biomassCHPChimney(plan_id)
        try:
            db.session.delete(biomassCHPChimney)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete biomassCHPChimney<id=%s, plan_id=%s> in database" %
                  (biomassCHPChimney.id, biomassCHPChimney.plan_id))

# # 烟囱表
# class BiomassCHPChimney(db.Model):
#     # 表名
#     __tablename__ = 'biomasschp_chimney'

#     # 表ID,自动生成（主键）
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     # 方案ID(外键)
#     plan_id = db.Column(db.Integer,
#                             db.ForeignKey('plan.id'))
                        
#     # 几何高度:设计
#     c_height = db.Column(db.NUMERIC(precision=15, scale=5))
#     # 烟囱温降:设计
#     c_drop_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
#     # 环境平均温度:设计
#     c_env_mean_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
#     # 烟囱入口温度:设计
#     c_entry_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
#     # 烟囱出口温度:设计
#     c_exit_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
#     # 烟囱内平均温度:设计
#     c_mean_temperature = db.Column(db.NUMERIC(precision=15, scale=5))


# 锅炉辅机表
class BiomassCHPBoilerAuxiliaries(db.Model):
    # 表名
    __tablename__ = 'biomasschp_boiler_auxiliaries'
    __table_args__ = {'comment': u'生物质热电锅炉辅机表'} 

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))

    # 定期排污扩容器 
    # 锅炉蒸发量
    r_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-锅炉蒸发量")
    # 排放时间
    r_emission_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排放时间")
    # 定期排污率
    r_emission_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-定期排污率")
    # 定期排污水量
    r_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-定期排污水量")
    # 汽包压力
    r_drum_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-汽包压力")
    # 汽包压力下的饱和水焓
    r_drum_aturatedwater_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-汽包压力下的饱和水焓")
    # 排污扩容器工作压力
    r_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污扩容器工作压力")
    # 扩容器压力下饱和水焓
    r_work_aturatedwater_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器压力下饱和水焓")
    # 扩容器压力下汽化潜热
    r_work_latentheat_vaporization = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器压力下汽化潜热")
    # 扩容器单位容积润许极限强度
    r_ultimate_strength = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器单位容积润许极限强度")
    # 排污扩容容积
    r_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污扩容容积")
    # 扩容器规格选取
    r_specifications = db.Column(db.String(100), comment=u"定期排污扩容器-扩容器规格选取")

    # 连续排污扩容器
    # 锅炉蒸发量
    c_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-锅炉蒸发量")
    # 连续排污率
    c_emission_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-连续排污率")
    # 连续排污水量
    c_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-连续排污水量")
    # 汽包压力
    c_drum_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-汽包压力")
    # 汽包压力下的饱和水焓
    c_drum_aturatedwater_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-汽包压力下的饱和水焓")
    # 排污扩容器工作压力
    c_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污扩容器工作压力")
    # 扩容器压力下饱和水焓
    c_work_aturatedwater_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下饱和水焓")
    # 扩容器压力下蒸汽比容
    c_work_steam_pecificvolume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下蒸汽比容")
    # 扩容器压力下汽化潜热
    c_work_latentheat_vaporization = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下汽化潜热")
    # 扩容器蒸汽干度
    c_steam_dryness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器蒸汽干度")
    # 扩容器单位容积润许极限强度
    c_ultimate_strength = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器单位容积润许极限强度")
    # 排污水汽化量
    c_vaporization_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污水汽化量")
    # 排污扩容汽容积
    c_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污扩容汽容积")
    # 扩容器规格选取
    c_specifications = db.Column(db.String(100), comment=u"连续排污扩容器-扩容器规格选取")

    # 1海拔:设计
    a_altitude = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"海拔")
    # 1大气压:设计
    a_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压")

    
    # 2工况温度_一次风:设计
    f_working_condition_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度_一次风")
    # 2工况流量_一次风:设计
    f_working_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量_一次风")
    # 2当地大气压_一次风:设计
    f_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_一次风")
    # 2标况温度_一次风:设计
    f_standard_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度_一次风")
    # 2标况压力_一次风:设计
    f_standard_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力_一次风")
    # 2标况压力_一次风:设计
    f_standard_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力_一次风")

    # 3工况温度_二次风:设计
    s_working_condition_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度_二次风")
    # 3工况流量_二次风:设计
    s_working_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量_二次风")
    # 3当地大气压_二次风:设计
    s_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_二次风")
    # 3标况温度_二次风:设计
    s_standard_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度_二次风")
    # 3标况压力_二次风:设计
    s_standard_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力_二次风")
    # 3标况流量_二次风:设计
    s_standard_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况流量_二次风")

    # 4工况温度_烟:设计
    a_working_condition_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度_烟")
    # 4工况流量_烟:设计
    a_working_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量_烟")
    # 4当地大气压_烟:设计
    a_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_烟")
    # 4标况温度_烟:设计
    a_standard_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度_烟")
    # 4标况压力_烟:设计
    a_standard_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力_烟")
    # 4标况流量_烟:设计
    a_standard_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况流量_烟")

    # 标况温度_一次风:设计
    bf_standard_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度_一次风")
    # 标况压力_一次风:设计
    bf_standard_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力_一次风")
    # 标况流量_一次风:设计
    bf_standard_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况流量_一次风")
    # 工况温度_一次风:设计
    bf_working_condition_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度_一次风")
    # 当地大气压_一次风:设计
    bf_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_一次风")
    # 工况流量_一次风:设计
    bf_working_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量_一次风")

    # 标况温度_二次风:设计
    bs_standard_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度_二次风")
    # 标况压力_二次风:设计
    bs_standard_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力_二次风")
    # 标况流量_二次风:设计
    bs_standard_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况流量_二次风")
    # 工况温度_二次风:设计
    bs_working_condition_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度_二次风")
    # 当地大气压_二次风:设计
    bs_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_二次风")
    # 工况流量_二次风:设计
    bs_working_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量_二次风")

    # 标况温度_烟:设计
    ba_standard_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度_烟")
    # 标况压力_烟:设计
    ba_standard_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力_烟")
    # 标况流量_烟:设计
    ba_standard_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况流量_烟")
    # 工况温度_烟:设计
    ba_working_condition_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度_烟")
    # 当地大气压_烟:设计
    ba_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_烟")
    # 工况流量_烟:设计
    ba_working_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量_烟")

    # 5空气温度_一次风:设计
    sf_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气温度_一次风")
    # 5锅炉本体阻力_一次风:设计
    sf_boiler_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉本体阻力_一次风")
    # 5风道阻力_一次风:设计
    sf_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风道阻力_一次风")
    # 5当地大气压_一次风:设计
    sf_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_一次风")
    # 5烟风流量（工况）_一次风:设计
    sf_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟风流量（工况）_一次风")
    # 5铭牌介质温度_一次风:设计
    sf_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"铭牌介质温度_一次风")
    # 5风机全压_一次风:设计
    sf_fan_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机全压_一次风")
    # 5风机选用全压_一次风:设计
    sf_fan_select_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用全压_一次风")
    # 5风机选用流量_一次风:设计
    sf_fan_select_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用流量_一次风")
    # 5风机效率_一次风:设计
    sf_fan_efficiency  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机效率_一次风")
    # 5电动机效率_一次风:设计
    sf_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率_一次风")
    # 5风机轴功率_一次风:设计
    sf_fan_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机轴功率_一次风")
    # 5电机安全裕量_一次风:设计
    sf_motor_safe = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机安全裕量_一次风")
    # 5电机功率_一次风:设计
    sf_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机功率_一次风")
    # 5选型结果_一次风:设计
    sf_select_result = db.Column(db.String(100), comment=u"选型结果_一次风")

    # 6空气温度_二次风:设计
    ss_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气温度_二次风")
    # 6锅炉本体阻力_二次风:设计
    ss_boiler_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉本体阻力_二次风")
    # 6风道阻力_二次风:设计
    ss_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风道阻力_二次风")
    # 6当地大气压_二次风:设计
    ss_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_二次风")
    # 6烟风流量（工况）_二次风:设计
    ss_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟风流量（工况）_二次风")
    # 6铭牌介质温度_二次风:设计
    ss_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"铭牌介质温度_二次风")
    # 6风机全压_二次风:设计
    ss_fan_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机全压_二次风")
    # 6风机选用全压_二次风:设计
    ss_fan_select_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用全压_二次风")
    # 6风机选用流量_二次风:设计
    ss_fan_select_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用流量_二次风")
    # 6风机效率_二次风:设计
    ss_fan_efficiency  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机效率_二次风")
    # 6电动机效率_二次风:设计
    ss_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率_二次风")
    # 6风机轴功率_二次风:设计
    ss_fan_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机轴功率_二次风")
    # 6电机安全裕量_二次风:设计
    ss_motor_safe = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机安全裕量_二次风")
    # 6电机功率_二次风:设计
    ss_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机功率_二次风")
    # 6选型结果_一次风:设计
    ss_select_result = db.Column(db.String(100), comment=u"选型结果_二次风")

    # 7烟气温度_引风机:设计
    i_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气温度_引风机")
    # 7锅炉本体烟气阻力_引风机:设计
    i_boiler_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉本体烟气阻力_引风机")
    # 7脱硝_引风机:设计
    i_denitration  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硝_引风机")
    # 7除尘器_引风机:设计
    i_duster = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器_引风机")
    # 7风道阻力_引风机:设计
    i_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风道阻力_引风机")
    # 7风机后脱硫塔及烟囱烟道阻力_引风机:设计
    i_cduct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机后脱硫塔及烟囱烟道阻力_引风机")
    # 7当地大气压_引风机:设计
    i_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_引风机")
    # 7烟风流量（工况）_引风机:设计
    i_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟风流量（工况）_引风机")
    # 7铭牌介质温度_引风机:设计
    i_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"铭牌介质温度_引风机")
    # 7风机全压_引风机:设计
    i_fan_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机全压_引风机")
    # 7风机选用全压_引风机:设计
    i_fan_select_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用全压_引风机")
    # 7风机选用流量_引风机:设计
    i_fan_select_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用流量_引风机")
    # 7风机效率_引风机:设计
    i_fan_efficiency  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机效率_引风机")
    # 7电动机效率_引风机:设计
    i_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率_引风机")
    # 7风机轴功率_引风机:设计
    i_fan_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机轴功率_引风机")
    # 7电机安全裕量_引风机:设计
    i_motor_safe = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机安全裕量_引风机")
    # 7电机功率_引风机:设计
    i_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机功率_引风机")
    # 7选型结果_一次风:设计
    i_select_result = db.Column(db.String(100), comment=u"选型结果_引风机")

    # 8空气温度_返料风机:设计
    r_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气温度_返料风机")
    # 8风压_返料风机:设计
    r_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风压_返料风机")
    # 8管道阻力_返料风机:设计
    r_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"管道阻力_返料风机")
    # 8当地大气压_返料风机:设计
    r_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压_返料风机")
    # 8烟风流量（工况）_返料风机:设计
    r_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟风流量（工况）_返料风机")
    # 8铭牌介质温度_返料风机:设计
    r_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"铭牌介质温度_返料风机")
    # 8风机全压_返料风机:设计
    r_fan_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机全压_返料风机")
    # 8风机选用全压_返料风机:设计
    r_fan_select_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用全压_返料风机")
    # 8风机选用流量_返料风机:设计
    r_fan_select_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用流量_返料风机")
    # 8风机效率_返料风机:设计
    r_fan_efficiency  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机效率_返料风机")
    # 8电动机效率_返料风机:设计
    r_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率_返料风机")
    # 8风机轴功率_返料风机:设计
    r_fan_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机轴功率_返料风机")
    # 8电机安全裕量_返料风机:设计
    r_motor_safe = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机安全裕量_返料风机")
    # 8电机功率_返料风机:设计
    r_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机功率_返料风机")
    # 8选型结果_一次风:设计
    r_select_result = db.Column(db.String(100), comment=u"选型结果_返料风机")

    # 锅炉设计使用压力
    f_boiler_use_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉设计使用压力")
    # 省煤器入口进水压力
    f_economizer_entry_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"省煤器入口进水压力")
    # 除氧器工作压力
    f_deaerator_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器工作压力")
    # 给水管阻力（以压头计）
    f_pipe_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水管阻力（以压头计）")
    # 进水管阻力（以压头计）
    f_inlet_pipe_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"进水管阻力（以压头计）")
    # 水泵中心至汽包正常水位的几何高度差
    f_center_water = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"水泵中心至汽包正常水位的几何高度差")
    # 除氧器最低水位至水泵中心几何高度差（给水泵进口静水头）
    f_deaerator_center = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器最低水位至水泵中心几何高度差（给水泵进口静水头）")
    # 给水泵总扬程
    f_pump_total_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵总扬程")
    # 流量
    f_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"流量")
    # 泵效率
    f_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"泵效率")
    # 机械传动效率
    f_mechanical_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机械传动效率")
    # 电动机效率
    f_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率")
    # 电动机备用系数
    f_motor_reserve_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机备用系数")
    # 配套电机功率
    f_auxiliary_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"配套电机功率")
    # 给水泵选用规格
    f_pump_selection = db.Column(db.String(100), comment=u"给水泵选用规格")

    # 除氧器处理量
    f_deaerator_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器处理量")
    # 除氧器压力
    f_deaerator_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器压力")
    # 除氧器温度
    f_deaerator_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器温度")
    # 锅炉蒸发量
    f_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉蒸发量")
    # 储水时间
    f_water_storage_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"储水时间")
    # 有效容积
    f_effective_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"有效容积")
    # 长
    f_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"长")
    # 直径
    f_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"直径")

    # 除氧器安装高度核算
    # 最大给水量
    s_max_feedwater_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-最大给水量")
    # 热力除氧压力
    s_de_ox_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-热力除氧压力")
    # 当地大气压
    s_local_atmosphere_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-当地大气压")
    # 当地大气压对应下的密度
    s_local_atmosphere_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-当地大气压对应下的密度")
    # 设计流量
    s_design_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-设计流量")
    # 泵必需汽蚀余量
    s_net_positive_suction_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-泵必需汽蚀余量")
    # 吸入管路的总阻力
    s_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-吸入管路的总阻力")
    # 泵入口流速
    s_inlet_speed = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-泵入口流速")
    # 附加高度
    s_added_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-附加高度")
    # 泵安装高度
    s_pump_install_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-泵安装高度")


    # 减温减压器---已知减温前、后参数求减温水量及减温后量
    # 新蒸汽-温度
    t_new_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-新蒸汽-温度")
    # 新蒸汽-压力
    t_new_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-新蒸汽-压力")
    # 新蒸汽-焓
    t_new_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-新蒸汽-焓")
    # 新蒸汽-流量
    t_new_flow_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-新蒸汽-流量")
    # 减温水-温度
    t_reduce_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水-温度")
    # 减温水-压力
    t_reduce_water_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水-压力")
    # 减温水-焓
    t_reduce_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水-焓")
    # 减温水-流量
    t_reduce_water_flow_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水-流量")
    # 减温后蒸汽-温度
    t_reduce_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温后蒸汽-温度")
    # 减温水-压力
    t_reduce_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水-压力")
    # 减温水-焓
    t_reduce_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水-焓")
    # 减温水-饱和水焓
    t_reduce_enough_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水-饱和水焓")
    # 减温水中未蒸发部分所占份额
    t_reduce_persent = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水中未蒸发部分所占份额")
    # 减温水-流量
    t_rudece_flow_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水-流量")

    # 蓄热器
    # 充热压力
    charging_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热压力")
    # 放热压力
    exothermic_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力")
    # 充热压力下的饱和水焓
    charging_saturation_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热压力下的饱和水焓")
    # 放热压力下的饱和水焓
    exothermic_saturation_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力下的饱和水焓")
    # 充热压力下的饱和汽焓
    charging_saturation_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热压力下的饱和汽焓")
    # 放热压力下的饱和汽焓
    exothermic_saturation_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力下的饱和汽焓")
    # P2压力下产生蒸汽量
    p2_steam_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-P2压力下产生蒸汽量")
    # 充热压力下的饱和水比容
    charging_water_specific_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热压力下的饱和水比容")
    # 单位水容积蓄热量
    unit_water_heat_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-单位水容积蓄热量")
    # 蓄热器热效率
    regenerarot_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器热效率")
    # 充水系数
    water_fill_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充水系数")
    # 蓄热器的蓄热量
    regenerarot_heat_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器的蓄热量")
    # 蓄热器容积
    regenerarot_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器容积")
    # 蓄热器上部蒸汽容积
    regenerarot_top_steam_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器上部蒸汽容积")
    # 锅炉最大负荷
    boiler_max_load = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-锅炉最大负荷")
    # 锅炉平均负荷
    boiler_average_load = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-锅炉平均负荷")
    # 蓄热器最大放汽量
    regenerarot_max_bleed = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器最大放汽量")
    # 质量蒸发强度
    evaporation_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-质量蒸发强度")
    # 放热压力下的质量蒸发强度
    exothermic_evaporation_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力下的质量蒸发强度")
    # 充热状态下的体积
    charging_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热状态下的体积")
    # 放热压力下的饱和水比容
    exothermic_water_specific_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力下的饱和水比容")
    # 放热完了水的体积
    exothermic_water_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热完了水的体积")

    def __init__(self, **kwargs):
        super(BiomassCHPBoilerAuxiliaries, self).__init__(**kwargs)

    @staticmethod
    def insert_auxiliaries(biomassAuxiliaries):
        try:
            db.session.add(biomassAuxiliaries)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassAuxiliaries"
                  "<id=%s> in database" % (biomassAuxiliaries.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_auxiliaries(plan_id):
        result = BiomassCHPBoilerAuxiliaries.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_auxiliaries(plan_id):
        auxiliaries = \
            BiomassCHPBoilerAuxiliaries.search_auxiliaries(plan_id)
        try:
            db.session.delete(auxiliaries)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete auxiliaries<id=%s, plan_id=%s> in database" %
                  (auxiliaries.id, auxiliaries.plan_id))


# 化学水处理表
class BiomassCHPWaterTreatment(db.Model):
    # 表名
    __tablename__ = 'biomasschp_water_treatment'
    __table_args__ = {'comment': u'生物质热电联产化学水处理表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))

    # 4过热蒸汽额定流量
    o_steam_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽额定流量")
    # 5厂内汽水损失
    o_loss_factory = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"厂内汽水损失")
    # 6锅炉排污损失
    o_boiler_blowdown_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉排污损失")
    # 7机组启动或事故增加损失
    o_start_accident_increase_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机组启动或事故增加损失")
    # 8外供汽损失
    o_external_supply_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"外供汽损失")
    # 9自用水量
    o_water_consumption = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"自用水量")
    # 10锅炉补给水系统正常出力
    o_boiler_water_normal = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水系统正常出力")
    # 11锅炉补给水系统最大出力
    o_boiler_water_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水系统最大出力")  
    # 12锅炉补给水系统出力
    o_boiler_water_system = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水系统出力") 
    # 13除盐水箱有效容积
    o_salt_water_tank = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除盐水箱有效容积")
    # 工艺路线
    o_process_route = db.Column(db.String(50), comment=u"锅炉补水系统工艺路线")


    def __init__(self, **kwargs):
        super(BiomassCHPWaterTreatment, self).__init__(**kwargs)

    @staticmethod
    def insert_water(biomassWater):
        try:
            db.session.add(biomassWater)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassWater"
                  "<id=%s> in database" % (biomassWater.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_water(plan_id):
        result = BiomassCHPWaterTreatment.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result


    # 根据plan_id删除实体
    @staticmethod
    def delete_water(plan_id):
        water = \
            BiomassCHPWaterTreatment.search_water(plan_id)
        try:
            db.session.delete(water)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete water<id=%s, plan_id=%s> in database" %
                  (water.id, water.plan_id))


# 公用工程表
class BiomassCHPOfficialProcess(db.Model):
    # 表名
    __tablename__ = 'biomasschp_official_process'
    __table_args__ = {'comment': u'生物质热电联产公用工程表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))

    # 1日用油罐
    o_oil_can = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"日用油罐")
    # 2供油泵-出力Q（单台）
    o_oil_pump = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供油泵-出力")
    # 3供油泵-压力P
    o_oil_pump_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供油泵-压力")
    # 炉型
    o_boiler_type = db.Column(db.String(50), comment=u"炉型")
    # 点火方式
    o_fire_way = db.Column(db.String(50), comment=u"点火方式")
    # 蒸汽参数
    o_steam_parameter = db.Column(db.String(50), comment=u"蒸汽参数")
    # 额定蒸发量
    o_steam_volumn = db.Column(db.String(50), comment=u"额定蒸发量")
    # 燃料类型
    o_fuel_type = db.Column(db.String(50), comment=u"燃料类型")
    # 安装方式
    o_install_way = db.Column(db.String(50), comment=u"安装方式")
    # 锅炉型号
    o_furnace_type = db.Column(db.String(50), comment=u"锅炉型号")


    def __init__(self, **kwargs):
        super(BiomassCHPOfficialProcess, self).__init__(**kwargs)

    @staticmethod
    def insert_official(biomassOfficial):
        try:
            db.session.add(biomassOfficial)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassOfficial"
                  "<id=%s> in database" % (biomassOfficial.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_official(plan_id):
        result = BiomassCHPOfficialProcess.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result


    # 根据plan_id删除实体
    @staticmethod
    def delete_official(plan_id):
        official = \
            BiomassCHPOfficialProcess.search_official(plan_id)
        try:
            db.session.delete(official)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete official<id=%s, plan_id=%s> in database" %
                  (official.id, official.plan_id))

# 汽轮机计算表
class BiomassCHPTurbineBackpressure (db.Model):
    # 表名
    __tablename__ = 'biomasschp_turbine_backpressure'
    __table_args__ = {'comment': u'生物质热电汽轮机计算表'} 

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))

    
    # 参数
    # 是否已经输入参数
    s_parameter_flg = db.Column(db.String(50))
    # 汽轮机类型
    s_steam_type_test = db.Column(db.Integer)
    # 除氧器温度和压力
    s_temperature_pressure = db.Column(db.String(50), comment=u"除氧器温度和压力")
    # 高加级数
    s_hh_grade = db.Column(db.Integer, comment=u"高加级数")
    # 低加级数
    s_lh_grade = db.Column(db.Integer, comment=u"低加级数")

    # 发电功率估算
    # 汽轮机内效率
    e_turbine_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：汽轮机内效率")
    # 机械效率
    e_mechanical_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：机械效率")
    # 发电机效率
    e_generator_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：发电机效率")
    # 汽轮机机组型式
    e_steam_type = db.Column(db.String(50), comment=u"发电功率估算：汽轮机机组型式")
    # 主蒸汽  压力
    e_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-压力")
    # 温度
    e_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-温度")
    # 流量
    e_steam_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-流量")
    # 熵
    e_steam_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-熵")
    # 焓
    e_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-焓")
    # 抽汽点  压力
    e_exhaust_point_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-压力")
    # 温度
    e_exhaust_point_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-温度")
    # 熵
    e_exhaust_point_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-熵")
    # 焓
    e_exhaust_point_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-焓")
    # 流量
    e_exhaust_point_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-流量")
    # 抽汽后蒸汽量
    e_exhaust_after_steam = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后蒸汽量")
    # 压力
    e_exhaust_after_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后压力")
    # 焓
    e_exhaust_after_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后焓")
    # 熵
    e_exhaust_after_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后熵")
    # 乏汽  压力
    e_steam_exhaust_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：乏汽-压力")
    # 焓
    e_steam_exhaust_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：乏汽-焓")

    # 背压  压力
    e_backpressure_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-压力")
    # 背压  温度
    e_backpressure_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-温度")
    # 焓
    e_backpressure_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-焓")
    # 流量
    e_backpressure_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-流量")

    # 追加补汽焓（补凝场合）
    e_steam_plus_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"补汽焓")

    # 总发电量
    e_gross_generation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：总发电量")
    # 回热抽汽经验数据
    e_hot_data = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：回热抽汽经验数据")
    # 去除抽汽后
    e_steam_extraction = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：去除抽汽后")
    # 选定
    e_steam_extraction_select = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：选定")
    # 全厂汽水损失
    e_steam_water_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：全厂汽水损失")
    # 进汽量
    e_throttle_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：进汽量")


    # 汽轮机回热系统计算
    # 假设
    h_assume = db.Column(db.String(100), comment=u"汽轮机回热系统-假设")
    # 温度
    h_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-温度")
    # 压力
    h_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-压力")
    # 焓值
    h_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-焓值")
    # 量
    h_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-量")

    # HH1
    # 给水出水温度
    hh1_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-给水出水温度")
    # 给水出口焓
    hh1_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-给水出口焓")
    # 上端差
    hh1_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-上端差")
    # 饱和水温度
    hh1_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-饱和水温度")
    # 饱和水焓
    hh1_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-饱和水焓")
    # 工作压力
    hh1_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-工作压力")
    # 抽汽管压损
    hh1_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽管压损")
    # 抽汽压力
    hh1_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽压力")
    # 抽汽焓
    hh1_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽焓")
    # 抽汽量
    hh1_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽量")
    
    # HH2
    # 给水出水温度
    hh2_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-给水出水温度")
    # 给水出口焓
    hh2_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-给水出口焓")
    # 上端差
    hh2_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-上端差")
    # 饱和水温度
    hh2_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-饱和水温度")
    # 饱和水焓
    hh2_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-饱和水焓")
    # 工作压力
    hh2_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-工作压力")
    # 抽汽管压损
    hh2_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽管压损")
    # 抽汽压力
    hh2_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽压力")
    # 抽汽焓
    hh2_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽焓")
    # 抽汽量
    hh2_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽量")

    # HH3
    # 给水出水温度
    hh3_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-给水出水温度")
    # 给水出口焓
    hh3_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-给水出口焓")
    # 上端差
    hh3_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-上端差")
    # 饱和水温度
    hh3_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-饱和水温度")
    # 饱和水焓
    hh3_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-饱和水焓")
    # 工作压力
    hh3_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-工作压力")
    # 抽汽管压损
    hh3_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽管压损")
    # 抽汽压力
    hh3_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽压力")
    # 抽汽焓
    hh3_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽焓")
    # 抽汽量
    hh3_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽量")

    # D
    # 给水出水温度
    d_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-给水出水温度")
    # 给水出口焓
    d_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-给水出口焓")
    # 工作压力
    d_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-工作压力")
    # 抽汽管压损
    d_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽管压损")
    # 抽汽压力
    d_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽压力")
    # 抽汽焓
    d_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽焓")
    # 抽汽量
    d_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽量")

    # LH1
    # 给水出水温度
    lh1_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-给水出水温度")
    # 给水出口焓
    lh1_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-给水出口焓")
    # 上端差
    lh1_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-上端差")
    # 饱和水温度
    lh1_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-饱和水温度")
    # 饱和水焓
    lh1_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-饱和水焓")
    # 工作压力
    lh1_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-工作压力")
    # 抽汽管压损
    lh1_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽管压损")
    # 抽汽压力
    lh1_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽压力")
    # 抽汽焓
    lh1_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽焓")
    # 抽汽量
    lh1_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽量")

    # LH2
    # 给水出水温度
    lh2_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-给水出水温度")
    # 给水出口焓
    lh2_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-给水出口焓")
    # 上端差
    lh2_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-上端差")
    # 饱和水温度
    lh2_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-饱和水温度")
    # 饱和水焓
    lh2_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-饱和水焓")
    # 工作压力
    lh2_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-工作压力")
    # 抽汽管压损
    lh2_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽管压损")
    # 抽汽压力
    lh2_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽压力")
    # 抽汽焓
    lh2_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽焓")
    # 抽汽量
    lh2_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽量")

    # LH3
    # 给水出水温度
    lh3_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-给水出水温度")
    # 给水出口焓
    lh3_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-给水出口焓")
    # 上端差
    lh3_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-上端差")
    # 饱和水温度
    lh3_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-饱和水温度")
    # 饱和水焓
    lh3_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-饱和水焓")
    # 工作压力
    lh3_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-工作压力")
    # 抽汽管压损
    lh3_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽管压损")
    # 抽汽压力
    lh3_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽压力")
    # 抽汽焓
    lh3_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽焓")
    # 抽汽量
    lh3_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽量")

    # C
    # 给水出水温度
    c_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-给水出水温度")
    # 给水出口焓
    c_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-给水出口焓")
    # 工作压力
    c_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-工作压力")
    # 抽汽管压损
    c_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽管压损")
    # 抽汽压力
    c_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽压力")
    # 抽汽焓
    c_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽焓")
    # 抽汽量
    c_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽量")

    # 组内功率计算及校核
    # 汽轮机内效率
    i_turbine_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：汽轮机内效率")
    # 机械效率
    i_mechanical_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：机械效率")
    # 发电机效率
    i_generator_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：发电机效率")
    # 主蒸汽  压力
    i_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-压力")
    # 温度
    i_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-温度")
    # 流量
    i_steam_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-流量")
    # 熵
    i_steam_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-熵")
    # 焓
    i_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-焓")
    # 1#高压  压力
    i_high1_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-压力")
    # 熵
    i_high1_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-熵")
    # 温度
    i_high1_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-温度")
    # 焓
    i_high1_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-焓")
    # 流量
    i_high1_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-流量")
    # 主汽至HH1功率
    i_steam_hh1_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主汽至HH1功率")
    # 2#高压  压力
    i_high2_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-压力")
    # 熵
    i_high2_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-熵")
    # 温度
    i_high2_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-温度")
    # 焓
    i_high2_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-焓")
    # 流量
    i_high2_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-流量")
    # HH1至HH2功率
    i_hh1_hh2_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：HH1至HH2功率")
    # D除氧  压力
    i_deoxidize_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-压力")
    # 熵
    i_deoxidize_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-熵")
    # 温度
    i_deoxidize_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-温度")
    # 焓
    i_deoxidize_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-焓")
    # 流量
    i_deoxidize_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-流量")
    # HH2至D功率
    i_hh2_deoxidize_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：HH2至D功率")
    # 抽汽点  压力
    i_exhaust_point_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-压力")
    # 温度
    i_exhaust_point_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-温度")
    # 熵
    i_exhaust_point_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-熵")
    # 焓
    i_exhaust_point_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-焓")
    # 流量
    i_exhaust_point_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-流量")
    # D至抽汽功率
    i_deoxidize_exhaust_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D至抽汽功率")
    # 1#低加  压力
    i_low1_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-压力")
    # 熵
    i_low1_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-熵")
    # 温度
    i_low1_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-温度")
    # 焓
    i_low1_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-焓")
    # 流量
    i_low1_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-流量")
    # 抽汽至LH1功率
    i_exhaust_lh1_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽至LH1功率")
    # 2#低加  压力
    i_low2_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-压力")
    # 熵
    i_low2_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-熵")
    # 温度
    i_low2_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-温度")
    # 焓
    i_low2_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-焓")
    # 流量
    i_low2_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-流量")
    # LH1至LH2功率
    i_lh1_lh2_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH1至LH2功率")
	# 3#低加  压力
    i_low3_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-压力")
    # 熵
    i_low3_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-熵")
    # 温度
    i_low3_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-温度")
    # 焓
    i_low3_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-焓")
    # 流量
    i_low3_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-流量")
    # LH2至LH3功率
    i_lh2_lh3_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH2至LH3功率")

    # 乏汽/背压   压力
    i_steam_exhaust_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-压力")
    # 熵
    i_steam_exhaust_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-熵")
    # 焓
    i_steam_exhaust_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-焓")
    # 实际焓
    i_steam_exhaust_enthalpy_actual = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-实际焓")
    # 饱和蒸汽焓
    i_steam_exhaust_enthalpy_steam = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-饱和蒸汽焓")
    # 饱和水焓
    i_steam_exhaust_enthalpy_water = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-饱和水焓")
    # 干度
    i_steam_exhaust_dry = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-干度")
    # 流量
    i_steam_exhaust_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-流量")
    # LH2至乏汽功率
    i_lh2_steam_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH2至乏汽功率")
    # 总功率
    i_total_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：总功率")
    # 抽汽点为0的总功率
    i_total_power0 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算误差
    i_calculation_error = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：计算误差")
    # 锅炉排污率
    h_blowdown_rate = db.Column(db.NUMERIC(precision=15, scale=5))    


    def __init__(self, **kwargs):
        super(BiomassCHPTurbineBackpressure, self).__init__(**kwargs)

    @staticmethod
    def insert_turbineBackpressure(biomassTurbineBackpressure):
        try:
            db.session.add(biomassTurbineBackpressure)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassTurbineBackpressure"
                  "<id=%s> in database" % (biomassTurbineBackpressure.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_turbineBackpressure(plan_id):
        result = BiomassCHPTurbineBackpressure.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result


    # 根据plan_id删除实体
    @staticmethod
    def delete_turbineBackpressure(plan_id):
        turbineBackpressure = \
            BiomassCHPTurbineBackpressure.search_turbineBackpressure(plan_id)
        try:
            db.session.delete(turbineBackpressure)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete turbineBackpressure<id=%s, plan_id=%s> in database" %
                  (turbineBackpressure.id, turbineBackpressure.plan_id))


# 采暖供热系统表
class BiomassCHPHeatSupply(db.Model):
    # 表名
    __tablename__ = 'biomasschp_heat_supply'
    __table_args__ = {'comment': u'生物质热电联产采暖供热系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer,
                            db.ForeignKey('plan.id'))

    # 采暖面积
    heat_area =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"采暖面积")
    # 采暖热指标
    heat_hot_target =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"采暖热指标")
    # 采暖热负荷
    heat_hot_load =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"采暖热负荷")
    # 汽轮机抽汽压力
    turbine_pressure =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机抽汽压力")
    # 汽轮机抽汽量(采暖)
    heat_turbine_flow =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机抽汽量(采暖)")
    # 汽轮机计算用(hidden项)
    hidden_turbine = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 工业用汽量
    use_flow =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工业用汽量")
    # 供汽同时率
    steam_supply_rate =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供汽同时率")
    # 热网损失
    hot_loss =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热网损失")
    # 汽轮机抽汽量(供热)
    hot_turbine_flow =  db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机抽汽量(供热)")

    def __init__(self, **kwargs):
        super(BiomassCHPHeatSupply, self).__init__(**kwargs)

    @staticmethod
    def insert_heatSupply(biomassCHPHeatSupply):
        try:
            db.session.add(biomassCHPHeatSupply)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassCHPHeatSupply"
                  "<id=%s> in database" % (biomassCHPHeatSupply.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_heatSupply(plan_id):
        result = BiomassCHPHeatSupply.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result


    # 根据plan_id删除实体
    @staticmethod
    def delete_heatSupply(plan_id):
        heatSupply = \
            BiomassCHPHeatSupply.search_heatSupply(plan_id)
        try:
            db.session.delete(heatSupply)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete heatSupply<id=%s, plan_id=%s> in database" %
                  (heatSupply.id, heatSupply.plan_id))

# 循环水系统
class BiomassCHPCirculatingWater(db.Model):
    # 表名
    __tablename__ = 'biomasschp_circulating_water'
    __table_args__ = {'comment': u'生物质热电联产循环水系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 乏汽流量(冬季)
    v_steam_exhaust_flow_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"乏汽流量(冬季)")
    # 乏汽流量(夏季)
    v_steam_exhaust_flow_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"乏汽流量(夏季)")
    # 乏汽流量(选择)
    v_steam_exhaust_flow_select = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"乏汽流量(选择)")
    # 循环倍率(冬季)
    v_circulating_ratio_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环倍率(冬季)")
    # 循环倍率(夏季)
    v_circulating_ratio_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环倍率(夏季)")
    # 循环水量(冬季)
    v_circulating_water_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水量(冬季)")
    # 循环水量(夏季)
    v_circulating_water_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水量(夏季)")
    # 辅机冷却水量(冬季)
    v_auxiliary_engine_cooling_winter = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"辅机冷却水量(冬季)")
    # 辅机冷却水量(夏季)
    v_auxiliary_engine_cooling_summer = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"辅机冷却水量(夏季)")
    # 总循环水量(冬季)
    v_total_circulating_water_winter = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"总循环水量(冬季)")
    # 总循环水量(夏季)
    v_total_circulating_water_summer = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"总循环水量(夏季)")
    # 总循环水量(选择)
    v_total_circulating_water_select = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"总循环水量(选择)")
    # 进、出水口温差
    v_enter_the_outlet_temperature_difference = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"进、出水口温差")
    # 干球温度
    v_dry_bulb_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干球温度")
    # 上区间干球温度
    v_up_dry_bulb_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上区间干球温度")
    # 下区间干球温度
    v_down_dry_bulb_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"下区间干球温度")
    # 上区间K
    v_up_k = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上区间K系数")
    # 下区间K
    v_down_k = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"下区间K系数")
    # K
    v_k = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"K系数")
    # 蒸发损失率
    v_evaporation_loss_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸发损失率")
    # 蒸发损失
    v_evaporation_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸发损失")
    # 风吹损失率
    v_blowing_loss_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风吹损失率")
    # 风吹损失
    v_partial_blow_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风吹损失")
    # 浓缩倍率
    v_concentrate_ratio = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"浓缩倍率")
    # 排污损失率
    v_discharge_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排污损失率")
    # 排污量
    v_discharge_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排污量")
    # 补充水量（冬季）
    v_amount_of_makeup_water = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"补充水量")
    # 循环水池尺寸
    v_circulating_pool_size = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池尺寸")

    # 冷却塔选型
    p_select = db.Column(db.String(100), comment=u"冷却塔选型")

    # 方案一 双曲线自然通风冷却塔选型
    # 喷淋密度
    p_spray_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双曲线自然通风冷却塔喷淋密度")
    # 喉部喷淋面积
    p_spray_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双曲线自然通风冷却塔喷淋面积")
    # 选型
    p_select_f = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双曲线自然通风冷却塔选型")

    # 方案二 逆流式机械通风冷却塔
    # 数量
    p_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"逆流式机械通风冷却塔数量")
    # 单台冷却水量
    p_single_cold_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"逆流式机械通风冷却塔单台冷却水量")
    # 选型
    p_select_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"逆流式机械通风冷却塔选型")

    # 凝汽器循环水进水工作压力
    c_pressure_condenser = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器循环水进水工作压力")
    # 凝汽器阻力
    c_condenser_tube_friction = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器阻力")
    # 循环水回水压力
    c_circulating_water_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水回水压力")
    # 循环水吸水池压力
    c_circulating_pool_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水吸水池压力")
    # 循环水泵出口与凝汽器循环水进水口高度差
    c_circulation_height_difference = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"循环水泵出口与凝汽器循环水进水口高度差")
    # 吸水池与水泵入口高度差
    c_height_difference_inlet = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"吸水池与水泵入口高度差")
    # 管道损失
    c_pipe_losses = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"管道损失")
    # Y型过滤器损失
    c_y_losses = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"Y型过滤器损失")
    # 总扬程
    c_pumping_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总扬程")
    # 流量
    c_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"流量")
    # 泵效率
    c_pump_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"泵效率")
    # 机械传动效率
    c_mechine_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机械传动效率")
    # 电动机效率
    c_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率")
    # 电动机备用系数
    c_motor_backup_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机备用系数")
    # 配套电机功率
    c_supporting_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"配套电机功率")
    # 选用型号功率
    c_forklift_parameters_power = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"选用型号功率")
    # 选用型号流量
    c_forklift_parameters_flow = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"选用型号流量")
    # 选用型号扬程
    c_forklift_parameters_lift = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"选用型号扬程")


    def __init__(self, **kwargs):
        super(BiomassCHPCirculatingWater, self).__init__(**kwargs)

    @staticmethod
    def insert_circulating_water(biomassCHPCirculatingWater):
        try:
            db.session.add(biomassCHPCirculatingWater)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassCHPCirculatingWater"
                  "<id=%s> in database" % (biomassCHPCirculatingWater.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_circulating_water(plan_id):
        result = BiomassCHPCirculatingWater.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_circulating_water(plan_id):
        smoke_air_system = \
            BiomassCHPCirculatingWater.search_circulating_water(plan_id)
        try:
            db.session.delete(smoke_air_system)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete smoke_air_system<id=%s, plan_id=%s> in database" %
                  (smoke_air_system.id, smoke_air_system.plan_id))


    # 根据id查找实体
    @staticmethod
    def searchById(id):
        result = BiomassCHPBoilerCalculation.query.filter_by(id=id).one_or_none()
        return result

    # 更新实体
    @staticmethod
    def updataById(var):
        if var.id != null:
            db.session.add(var)
            db.session.commit()
        return result

# 汽机辅机
class BiomasschpTurbineAuxiliary(db.Model):
    # 表名
    __tablename__ = 'biomasschp_turbine_auxiliary'
    __table_args__ = {'comment': u'生物质热电联产汽机辅机系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 除氧器工作压力
    w_deaerator_working_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器工作压力")
    # 除氧器凝结水入口与凝汽器热井最低水位间的水柱静压差
    w_deaerator_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器凝结水入口与凝汽器热井最低水位间的水柱静压差")
    # 除氧器入口凝结水管喷雾头所需喷雾压力
    w_deaerator_need_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器入口凝结水管喷雾头所需喷雾压力")
    # 凝汽器的最高真空
    w_condenser_higter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器的最高真空")
    # 从热井到除氧器凝结水入口的凝结水管道流动阻力，另加20%裕量
    w_hot_well_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"从热井到除氧器凝结水入口的凝结水管道流动阻力")
    # 凝结水泵的设计扬程
    w_condensate_pump_lift = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵的设计扬程")
    # 流量
    w_flow_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-流量")
    # 泵效率
    w_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-泵效率")
    # 机械传动效率
    w_mechanical_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-机械传动效率")
    # 电动机效率
    w_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-电动机效率")
    # 电动机备用系数
    w_motor_reserve_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-电动机备用系数")
    # 配套电机功率
    w_auxiliary_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-配套电机功率")
    # 选用型号
    w_select = db.Column(db.String(100), comment=u"凝结水泵-选用型号")
    # 凝汽量
    m_condensate_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽量")
    # 凝汽器压力
    m_condenser_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器压力")
    # 汽轮机排汽焓
    m_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机排汽焓")
    # 冷却水进口温度
    m_cooling_water_inlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水进口温度")
    # 特殊处理部分--饱和温度
    m_saturation_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"饱和温度")
    # 过冷度
    m_supercooling = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过冷度")
    # 凝结水温度
    m_condensate_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水温度")
    # 特殊处理部分--凝结水焓
    m_condensate_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水焓")
    # 冷却管的洁净系数
    m_cooling_pipe_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却管的洁净系数")
    # 冷却管材料和壁厚的修正系数
    m_correction_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却管材料和壁厚的修正系数")
    # 计算指数
    m_calculation_index = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算指数")
    # 冷却管内流速
    m_cooling_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却管内流速")
    # 冷却管内径
    m_cooling_type = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却管内径")
    # 凝汽器比蒸汽负荷修正系数
    m_correction_condensers = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器比蒸汽负荷修正系数")
    # 冷却管内流速的修正系数
    m_flow_speed_correction = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却管内流速的修正系数")
    # 冷却水进口温度修正系数
    m_inlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水进口温度修正系数")
    # 冷却水流程数的修正系数
    m_flow_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水流程数的修正系数")
    # 考虑凝汽器蒸汽负荷变化的修正系数
    m_consideration_change = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"考虑凝汽器蒸汽负荷变化的修正系数")
    # 总传热系数
    m_total_heat_transfer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总传热系数")
    # 凝汽器热负荷
    m_condenser_heat_load = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器热负荷")
    # 循环倍率
    m_cycle_ratio = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环倍率")
    # 循环水量
    m_circulating_water = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水量")
    # 冷却水温升 冷却水cp 取4.1868:
    m_cooling_water_rise = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水温升")
    # 冷却水出口温度
    m_cooling_outlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水出口温度")
    # 对数平均温差
    m_logarithmic_mean_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"对数平均温差")
    # 冷却面积
    m_area_cooling_surface = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却面积")
    # 射水抽气器工作压力
    f_air_ejector_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水抽气器工作压力")
    # 射水箱工作压力
    f_water_tank_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱工作压力")
    # 射水抽气器安装高度与射水箱最高水位之差
    f_water_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水抽气器安装高度与射水箱最高水位之差")
    # 射水泵进出口管路损失
    f_ejection_pump_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵进出口管路损失")
    # 总扬程
    f_total_lift = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总扬程")
    # 流量
    f_flow_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"流量")
    # 泵效率
    f_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-泵效率")
    # 机械传动效率
    f_mechanical_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-机械传动效率")
    # 电动机效率
    f_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-电动机效率")
    # 电动机备用系数
    f_motor_reserve_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-电动机备用系数")
    # 配套电机功率
    f_auxiliary_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-配套电机功率")
    # 选用型号
    f_select = db.Column(db.String(100), comment=u"射水泵-选用型号")
    # 射水箱工作压力
    c_water_tank_pressure  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱工作压力")
    # 循环水回水母管压力
    c_recirculating_tube_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水回水母管压力")
    # 射水抽气器安装高度与射水箱最高水位之差
    c_water_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水抽气器安装高度与射水箱最高水位之差")
    # 射水泵进出口管路损失
    c_ejection_pump_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵进出口管路损失")
    # 总扬程
    c_total_lift = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-总扬程")
    # 流量
    c_flow_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-流量")
    # 泵效率
    c_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-泵效率")
    # 机械传动效率
    c_mechanical_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-机械传动效率")
    # 电动机效率
    c_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-电动机效率")
    # 电动机备用系数
    c_motor_reserve_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-电动机备用系数")
    # 配套电机功率
    c_auxiliary_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-配套电机功率")
    # 选用型号
    c_select = db.Column(db.String(100), comment=u"射水箱冷却水泵-选用型号")

    def __init__(self, **kwargs):
        super(BiomasschpTurbineAuxiliary, self).__init__(**kwargs)

    @staticmethod
    def insert_turbine_auxiliary(biomasschpTurbineAuxiliary):
        try:
            db.session.add(biomasschpTurbineAuxiliary)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomasschpTurbineAuxiliary"
                  "<id=%s> in database" % (biomasschpTurbineAuxiliary.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_turbine_auxiliary(plan_id):
        result = BiomasschpTurbineAuxiliary.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_turbine_auxiliary(plan_id):
        turbine_auxiliary = \
            BiomasschpTurbineAuxiliary.search_turbine_auxiliary(plan_id)
        try:
            db.session.delete(turbine_auxiliary)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete turbine_auxiliary<id=%s, plan_id=%s> in database" %
                  (turbine_auxiliary.id, turbine_auxiliary.plan_id))


# 主要技术经济指标
class BiomasschpEconomicIndicators(db.Model):
    # 表名
    __tablename__ = 'biomasschp_economic_indicators'
    __table_args__ = {'comment': u'生物质热电联产主要技术经济指标表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 凝结水回水压力
    condensate_backwater_pressure  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回水压力")
    # 凝结水回水温度
    condensate_backwater_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回水温度")
    # 凝结水回水焓值
    condensate_backwater_enthalpy  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回水焓值")

    # 抽凝工况热耗率
    smoke_heat_consumption_rate  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况热耗率")
    # 纯凝工况热耗率
    heat_consumption_rate  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况热耗率")
    # 抽凝工况汽耗率
    smoke_steam_consumption_rate  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况汽耗率")
    # 纯凝工况汽耗率
    steam_consumption_rate  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况汽耗率")
    # 机组年利用小时数
    annual_useage_hours  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机组年利用小时数")
    # 机组年供热小时数
    annual_heat_hours  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机组年供热小时数")
    # 年供热量
    annual_heat_supply  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年供热量")
    # 年发电量
    annual_power_generation  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年发电量")
    # 厂用电率
    plant_electricity_consumption   = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"厂用电率")
    # 年供电量
    annual_power_supply  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年供电量")
    # 锅炉效率
    boiler_efficiency   = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉效率")
    # 管道效率
    pipeline_efficiency   = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"管道效率")
    # 抽凝工况发电标煤耗率
    smoke_power_coal_consumption  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况发电标煤耗率")
    # 纯凝工况发电标煤耗率
    power_coal_consumption  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况发电标煤耗率")
    # 抽凝工况供电标煤耗率
    smoke_supply_coal_consumption  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况供电标煤耗率")
    # 纯凝工况供电标煤耗率
    supply_coal_consumption  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况供电标煤耗率")
    # 全年平均热电比
    annual_average_thermoelectric_ratio  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"全年平均热电比")
    # 抽凝工况全厂热效率
    smoke_heat_efficiency  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况全厂热效率")
    # 纯凝工况全厂热效率
    heat_efficiency  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况全厂热效率")

    # hidden项
    # 汽轮机 主蒸汽焓F9
    t_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 抽汽点焓F13
    t_point_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 抽汽点流量F15
    t_point_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 进汽量F26
    t_throttle_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 总功率F95
    t_total_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 抽汽点为0的总功率F95
    t_total_power0 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉 收到基低位发热量G14
    t_base_heat_received_user = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉 给水焓值G26
    t_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉 锅炉效率G27
    # t_boiler_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 燃料存储及输送 锅炉额定燃料耗量G3
    t_rated_fuel_consumption = db.Column(db.NUMERIC(precision=15, scale=5))


    def __init__(self, **kwargs):
        super(BiomasschpEconomicIndicators, self).__init__(**kwargs)

    @staticmethod
    def insert_economic_indicators(BiomasschpEconomicIndicators):
        try:
            db.session.add(BiomasschpEconomicIndicators)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update BiomasschpEconomicIndicators"
                  "<id=%s> in database" % (BiomasschpEconomicIndicators.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_economic_indicators(plan_id):
        result = BiomasschpEconomicIndicators.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_economic_indicators(plan_id):
        economic_indicators = \
            BiomasschpEconomicIndicators.search_economic_indicators(plan_id)
        try:
            db.session.delete(economic_indicators)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete economic_indicators<id=%s, plan_id=%s> in database" %
                  (economic_indicators.id, economic_indicators.plan_id))


# 生物质燃料数据表
class BiomassCHPFuelComponent(db.Model):
    # 表名
    __tablename__ = 'biomasschp_fuel_component'
    # __table_args__ = {'comment': u'燃煤热电联产-产煤成分数据表'}

    # 燃料id， 自动生成
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 燃料名称
    name = db.Column(db.String(50), comment=u"燃料名称")
    # 收到基碳含量
    carbon = db.Column(db.String(50), comment=u"收到基碳含量")
    # 收到基氢含量
    hydrogen = db.Column(db.String(50), comment=u"收到基氢含量")
    # 收到基氧含量
    oxygen = db.Column(db.String(50), comment=u"收到基氧含量")
    # 收到基氮含量
    nitrogen = db.Column(db.String(50), comment=u"收到基氮含量")
    # 收到基硫含量
    sulfur = db.Column(db.String(50), comment=u"收到基硫含量")
    # 收到基水份含量
    water = db.Column(db.String(50), comment=u"收到基水份含量")
    # 挥发分
    daf = db.Column(db.String(50), comment=u"干燥无灰基挥发分")
    # 收到基灰份
    grey = db.Column(db.String(50), comment=u"收到基灰份")
    # 固定碳
    grindability = db.Column(db.String(50), comment=u"固定碳")
    # 收到基低位发热量
    low = db.Column(db.String(50), comment=u"收到基低位发热量")

    @staticmethod
    def create_biomassCHPComponent(name, carbon, hydrogen, oxygen, nitrogen,
                                sulfur, water, daf, grey, grindability, low):
        biomassCHPComponent = BiomassCHPFuelComponent()
        biomassCHPComponent.name = name
        biomassCHPComponent.carbon = carbon
        biomassCHPComponent.hydrogen = hydrogen
        biomassCHPComponent.oxygen = oxygen
        biomassCHPComponent.nitrogen = nitrogen
        biomassCHPComponent.sulfur = sulfur
        biomassCHPComponent.water = water
        biomassCHPComponent.daf = daf
        biomassCHPComponent.grey = grey
        biomassCHPComponent.grindability = grindability
        biomassCHPComponent.low = low

        return biomassCHPComponent

    @staticmethod
    def insert_biomassCHPComponent(biomassCHPComponent):
        try:
            db.session.add(biomassCHPComponent)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassCHPComponent<id=%s>" %
                  (biomassCHPComponent.id))

    @staticmethod
    def search_biomassCHPComponent():
        result = BiomassCHPFuelComponent.query.all()
        return result

    # 根据id查找实体
    @staticmethod
    def search_biomassCHPSort(id):
        result = BiomassCHPFuelComponent.query.filter_by(id=id).one_or_none()
        return result

    def __repr__(self):
        return '<BiomassCHPFuelComponent %r>' % self.name


    # 根据id查找实体
    @staticmethod
    def searchById(id):
        result = BiomasschpTurbineAuxiliary.query.filter_by(id=id).one_or_none()
        return result

    # 更新实体
    @staticmethod
    def updataById(var):
        if var.id != null:
            db.session.add(var)
            db.session.commit()
        return result
