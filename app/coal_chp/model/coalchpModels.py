# -*- coding: utf-8 -*-
from ... import db


# 燃煤热电联产常量表
class CoalCHPConstant(db.Model):
    # 表名
    __tablename__ = 'coalchp_constant'
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
    # 默认值
    default_value = db.Column(db.String(200))
    # 是否为disable(t可修改，f不可修改)
    disable = db.Column(db.String(2))

    @staticmethod
    def create_coalCHPConstant(module_name, name_eng, name, symbol, unit,
                               calculate, remark, default_value, disable):
        coalCHPconstant = CoalCHPConstant()
        coalCHPconstant.module_name = module_name
        coalCHPconstant.name_eng = name_eng
        coalCHPconstant.name = name
        coalCHPconstant.symbol = symbol
        coalCHPconstant.unit = unit
        coalCHPconstant.calculate = calculate
        coalCHPconstant.remark = remark
        coalCHPconstant.default_value = default_value
        coalCHPconstant.disable = disable

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
    __tablename__ = 'coalchp_coal_component'
    # __table_args__ = {'comment': u'燃煤热电联产-产煤成分数据表'}

    # 煤种id， 自动生成
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 煤种名称
    name = db.Column(db.String(50), comment=u"煤种名称")
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
    # 收到基灰份
    grey = db.Column(db.String(50), comment=u"收到基灰份")
    # 干燥无灰基挥发分
    daf = db.Column(db.String(50), comment=u"干燥无灰基挥发分")
    # 收到可磨系数
    grindability = db.Column(db.String(50), comment=u"收到可磨系数")
    # 收到基低位发热量
    low = db.Column(db.String(50), comment=u"收到基低位发热量")

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
    __tablename__ = 'coalchp_needs_questionnaire'
    __table_args__ = {'comment': u'燃煤热电联产-需求调查表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 模块一，燃料情况status缩写（S）
    # s_modul_name = db.Column(db.String(100), nullable=True)
    # 设计燃料
    s_fuel_design = db.Column(db.String(100), nullable=True, comment=u"设计燃料")
    # 校核燃料
    s_fuel_check = db.Column(db.String(100), nullable=True, comment=u"校核燃料")

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
    s_water_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基全水份设计数值")
    # 基全水份校核数值
    s_water_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基全水份校核数值")

    # 基灰设计数值
    s_grey_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基灰设计数值")
    # 基灰校核数值
    s_grey_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"基灰校核数值")

    # 干燥无灰基挥发分设计数值
    s_daf_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干燥无灰基挥发分设计数值")
    # 干燥无灰基挥发分校核数值
    s_daf_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干燥无灰基挥发分校核数值")

    # 哈式可磨性系数设计数值
    s_grindability_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"哈式可磨性系数设计数值")
    # 哈式可磨性系数校核数值
    s_grindability_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"哈式可磨性系数校核数值")

    # 收到基低位发热量设计数值
    s_low_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量设计数值")
    # 收到基低位发热量校核数值
    s_low_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量校核数值")

    # 模块二 当地气象及地址条件weather 缩写W
    # w_modul_name = db.Column(db.String(100), nullable=True)
    # 当地平均海拔数值
    w_altitude_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地平均海拔数值")

    # 年平均温度数值
    w_mean_annual_temperature_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"年平均温度数值")

    # 夏季平均温度数值
    w_mean_summer_temperature_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"夏季平均温度数值")

    # 冬季平均温度数值
    w_mean_winter_temperature_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"冬季平均温度数值")

    # 极端最高温度
    w_extreme_high_temperature_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"极端最高温度")

    # 极端最低温度 
    w_extreme_low_temperature_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"极端最低温度")

    # 年平均大气压力数值
    w_mean_annual_barometric_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"年平均大气压力数值")

    # 夏季大气压力数值
    w_mean_summer_barometric_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"夏季大气压力数值")

    # 冬季大气压力数值
    w_mean_winter_barometric_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"冬季大气压力数值")

    # 年平均相对湿度数值
    w_annual_average_relative_humidity_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"年平均相对湿度数值")

    # 全年最热月平均相对湿度
    w_mean_summer_relative_humidity_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"全年最热月平均相对湿度")
    # 全年最冷月平均相对湿度
    w_mean_winter_relative_humidity_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"全年最冷月平均相对湿度")

    # 模块三  工业热负荷(Industrial heat load)缩写ihl   采暖热负荷（heating heat load）需求情况缩写hhl
    # 一级模块
    # h_modul_name = db.Column(db.String(100), nullable=True)
    # 二级模块
    # ihl_modul_name = db.Column(db.String(100), nullable=True)
    # 蒸汽压力等级数值
    ihl_steam_pressure_level_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"蒸汽压力等级")

    # 蒸汽温度等级数值
    ihl_steam_temperature_level_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"蒸汽温度等级")

    # 用汽时段校核数值
    ihl_steam_time_value = db.Column(db.Text(), comment=u"用汽时段")

    # 近期蒸汽流量范围数值
    ihl_recent_steam_flow_range_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"近期蒸汽流量范围")

    # 远期蒸汽流量范围数值
    ihl_forward_steam_flow_range_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"远期蒸汽流量范围")

    # 凝结水含铁量数值
    ihl_condensate_water_iron_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"凝结水含铁量")

    # 凝结水回收率数值
    ihl_condensate_water_recovery_rate_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"凝结水回收率")

    # hhl_modul_name = db.Column(db.String(100), nullable=True)
    # 采暖场合类型数值
    hhl_heating_occasions_type_value = db.Column(db.Text(), comment=u"采暖场合类型")

    # 全年采暖天数数值
    hhl_year_heating_days_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"全年采暖天数")

    # 近期采暖面积数值
    hhl_recent_heating_area_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"近期采暖面积")

    # 远期采暖面积数值
    hhl_forward_heating_area_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"远期采暖面积")

    # 模块四 其它情况others缩写O
    # 一级模块
    # o_modul_name = db.Column(db.String(100), nullable=True)
    # 二级模块 项目选址情况site
    # os_modul_name = db.Column(db.String(100), nullable=True)
    # 规划占地面积数值
    os_planning_area_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"规划占地面积")

    # 规划扩建容量数值
    os_planned_expansion_capacity_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"规划扩建容量")

    # 当地水源条件数值
    os_local_water_condition_value = db.Column(db.Text(), comment=u"当地水源条件")

    # 二级模块 电力系统electric
    # oe_modul_name = db.Column(db.String(100), nullable=True)
    # 电负荷需求数值
    oe_electrical_load_demand_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"电负荷需求")

    # 上级变电压等级数值
    oe_higher_voltage_level_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"上级变电压等级")

    # 厂区距上级变距离校值
    oe_plant_distance_higher_change_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"厂区距上级变距离")

    # 是否上网校值
    oe_is_internet_access_value = db.Column(db.Text(), comment=u"")

    # 是否孤网运行数值
    oe_is_isolated_network_value = db.Column(db.Text(), comment=u"")

    # 二级模块 当地环保要求Environmental Protection
    # op_modul_name = db.Column(db.String(100), nullable=True)
    # 烟气SOX排放限值数值
    op_flue_gas_sox_limits_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气SOX排放限值")

    # 烟气NOX排放限值数值
    op_flue_gas_nox_limits_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气NOX排放限值")

    # 烟气烟尘排放限值数值
    op_flue_gas_dust_limits_value = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"烟气烟尘排放限值")

    # 二级模块脱硫脱硝 Desulfurization and denitrification
    # od_modul_name = db.Column(db.String(100), nullable=True)
    # 拟采用脱硫形式数值
    od_use_desulfurization_form_value = db.Column(db.Text(), comment=u"拟采用脱硫形式")

    # 拟采用脱硝形式数值
    od_use_denitration_form_value = db.Column(db.Text(), comment=u"拟采用脱硝形式")

    # 石灰石供应情况数值
    od_limestone_supply_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石供应情况")

    # 尿素/氨水供应情况数值
    od_urea_or_ammonia_water_supply_value = db.Column(db.Text(), comment=u"尿素/氨水供应情况")

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
    def search_questionnaire(plan_id):
        result = CoalCHPNeedsQuestionnaire.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_questionnaire(plan_id):
        questionnaire = CoalCHPNeedsQuestionnaire.search_questionnaire(plan_id)
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

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        questionnaire = CoalCHPNeedsQuestionnaire.search_questionnaire(plan_id)
        db.session.delete(questionnaire)


# 表名 燃煤热电联产计算_输煤系统表
class CoalCHPCoalHandingSystem(db.Model):
    # 表名
    __tablename__ = 'coalchp_coal_handingsystem'
    __table_args__ = {'comment': u'燃煤热电联产-输煤系统表'}

    # 主ID， 自动生成
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 锅炉额定耗煤量 结果-设计（Value Design）
    b_boiler_rated_coal_capacity_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉额定耗煤量-设计")
    # 锅炉额定耗煤量 结果-校核（Value Verify）
    b_boiler_rated_coal_capacity_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉额定耗煤量-校核")
    # 锅炉日利用小时数 结果-设计（Value Design）
    b_boiler_daily_utilization_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉日利用小时数-设计")
    # 锅炉日利用小时数 结果-校核（Value Verify）
    b_boiler_daily_utilization_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉日利用小时数-校核")
    # 日耗煤量 结果-设计（Value Design）
    b_coal_daily_consumption_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"日耗煤量-设计")
    # 日耗煤量 结果-校核（Value Verify）
    b_coal_daily_consumption_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"日耗煤量-校核")
    # 锅炉年利用小时数 结果-设计（Value Design）
    b_boiler_annual_utilization_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉年利用小时数-设计")
    # 锅炉年利用小时数 结果-校核（Value Verify）
    b_boiler_annual_utilization_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉年利用小时数-校核")
    # 年耗煤量 结果-设计（Value Design）
    b_coal_annual_consumption_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"年耗煤量-设计")
    # 年耗煤量 结果-校核（Value Verify）
    b_coal_annual_consumption_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"年耗煤量-校核")
    # 日来煤不均衡系数 结果-设计（Value Design）
    b_daily_coal_unbalanced_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"日来煤不均衡系数-设计")
    # 日来煤不均衡系数 结果-校核（Value Verify）
    b_daily_coal_unbalanced_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"日来煤不均衡系数-校核")
    # 铁路来煤日计算煤量 结果-设计（Value Design）
    b_daily_rail_coal_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"铁路来煤日计算煤量-设计")
    # 铁路来煤日计算煤量 结果-校核（Value Verify）
    b_daily_rail_coal_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"铁路来煤日计算煤量-校核")
    # 汽车来煤日计算煤量 结果-设计（Value Design）
    b_daily_vehicle_coal_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"汽车来煤日计算煤量-设计")
    # 汽车来煤日计算煤量 结果-校核（Value Verify）
    b_daily_vehicle_coal_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"汽车来煤日计算煤量-校核")
    # 锅炉每小时最大耗煤量 结果-设计（Value Design）
    c_boiler_hour_coal_capacity_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉每小时最大耗煤量-设计")
    # 锅炉每小时最大耗煤量 结果-校核（Value Verify）
    c_boiler_hour_coal_capacity_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉每小时最大耗煤量-校核")
    # 锅炉每日运行时数 结果-设计（Value Design）
    c_boiler_daily_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉每日运行时数-设计")
    # 锅炉每日运行时数 结果-校核（Value Verify）
    c_boiler_daily_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉每日运行时数-校核")
    # 煤的储备日数 结果-设计（Value Design）
    c_coal_store_days_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤的储备日数-设计")
    # 煤的储备日数 结果-校核（Value Verify）
    c_coal_store_days_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤的储备日数-校核")
    # 煤场存储量 结果-设计（Value Design）
    c_coalyard_store_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤场存储量-设计")
    # 煤场存储量 结果-校核（Value Verify）
    c_coalyard_store_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤场存储量-校核")
    # 煤堆通道占用系数 结果-设计（Value Design）
    c_coal_channel_occupy_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤堆通道占用系数-设计")
    # 煤堆通道占用系数 结果-校核（Value Verify）
    c_coal_channel_occupy_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤堆通道占用系数-校核")
    # 煤堆形状系数 结果-设计（Value Design）
    c_coal_shape_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤堆形状系数-设计")
    # 煤堆形状系数 结果-校核（Value Verify）
    c_coal_shape_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤堆形状系数-校核")
    # 煤堆高度 结果-设计（Value Design）
    c_coal_height_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤堆高度-设计")
    # 煤堆高度 结果-校核（Value Verify）
    c_coal_height_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤堆高度-校核")
    # 煤的堆密度 结果-设计（Value Design）
    c_coal_bulk_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤的堆密度-设计")
    # 煤的堆密度 结果-校核（Value Verify）
    c_coal_bulk_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤的堆密度-校核")
    # 煤场面积 结果-设计（Value Design）
    c_coalyard_area_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤场面积-设计")
    # 煤场面积 结果-校核（Value Verify）
    c_coalyard_area_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤场面积-校核")
    # 长 结果-设计（Value Design）
    c_height_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤场长-设计")
    # 长 结果-校核（Value Verify）
    c_height_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤场长-校核")
    # 宽 结果-设计（Value Design）
    c_width_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤场宽-设计")
    # 宽 结果-校核（Value Verify）
    c_width_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤场宽-校核")
    # 有效容积-计算 结果-设计（Value Design）
    e_effective_cubage_calculated_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤场有效容积-设计")
    # 有效容积-计算 结果-校核（Value Verify）
    e_effective_cubage_calculated_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤场有效容积-校核")
    # 煤仓个数 结果-设计（Value Design）
    e_coal_bunker_counts_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤仓个数-设计")
    # 煤仓个数 结果-校核（Value Verify）
    e_coal_bunker_counts_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤仓个数-校核")
    # 有效容积-选定 结果-设计（Value Design）
    e_effective_cubage_selected_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤仓有效容积-设计")
    # 有效容积-选定 结果-校核（Value Verify）
    e_effective_cubage_selected_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"煤仓有效容积-校核")
    # 反推消耗小时 结果-设计（Value Design）
    e_backstep_consumption_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"反推消耗小时-设计")
    # 反推消耗小时 结果-校核（Value Verify）
    e_backstep_consumption_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"反推消耗小时-校核")
    # 运输不平衡系数 结果-设计（Value Design）
    t_transport_unbalanced_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"运输不平衡系数-设计")
    # 运输不平衡系数 结果-校核（Value Verify）
    t_transport_unbalanced_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"运输不平衡系数-校核")
    # 运煤系统有效作业时间 结果-设计（Value Design）
    t_transportsystem_effective_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"运煤系统有效作业时间-设计")
    # 运煤系统有效作业时间 结果-校核（Value Verify）
    t_transportsystem_effective_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"运煤系统有效作业时间-校核")
    # 运煤系统运输量 结果-设计（Value Design）
    t_transportsystem_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"运煤系统运输量-设计")
    # 运煤系统运输量 结果-校核（Value Verify）
    t_transportsystem_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"运煤系统运输量-校核")
    # 车辆名义载重量 结果-设计（Value Design）
    t_vehicle_capacity_tonnage_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"车辆名义载重量-设计")
    # 车辆名义载重量 结果-校核（Value Verify）
    t_vehicle_capacity_tonnage_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"车辆名义载重量-校核")
    # 每昼夜小时 结果-设计（Value Design）
    t_daily_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"每昼夜小时-设计")
    # 每昼夜小时 结果-校核（Value Verify）
    t_daily_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"每昼夜小时-校核")
    # 日计算受煤量 结果-设计（Value Design）
    t_daily_received_coal_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"日计算受煤量-设计")
    # 日计算受煤量 结果-校核（Value Verify）
    t_daily_received_coal_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"日计算受煤量-校核")
    # 每天进厂车次 结果-设计（Value Design）
    t_vehicle_daily_incoming_times_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"每天进厂车次-设计")
    # 每天进厂车次 结果-校核（Value Verify）
    t_vehicle_daily_incoming_times_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"每天进厂车次-校核")
    # 每小时进场车次 结果-设计（Value Design）
    t_vehicle_perhour_incoming_times_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"每小时进场车次-设计")
    # 每小时进场车次 结果-校核（Value Verify）
    t_vehicle_perhour_incoming_times_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"每小时进场车次-校核")
    # 多锅炉额定耗煤量 结果-设计（Value Design）
    s_mutil_boiler_rated_coal_capacity_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"多锅炉额定耗煤量-设计")
    # 多锅炉额定耗煤量 结果-校核（Value Verify）
    s_mutil_boiler_rated_coal_capacity_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"多锅炉额定耗煤量-校核")
    # 多锅炉日额定耗煤总量 结果-设计（Value Design）
    s_mutil_boiler_rated_coal_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"多锅炉日额定耗煤总量-设计")
    # 多锅炉日额定耗煤总量 结果-校核（Value Verify）
    s_mutil_boiler_rated_coal_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"多锅炉日额定耗煤总量-校核")
    # 输煤系统选定出力 结果-设计（Value Design）
    s_transportsystem_output_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"输煤系统选定出力-设计")
    # 输煤系统选定出力 结果-校核（Value Verify）
    s_transportsystem_output_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"输煤系统选定出力-校核")
    # 输煤系统运行小时 结果-设计（Value Design）
    s_transportsystem_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"输煤系统运行小时-设计")
    # 输煤系统运行小时 结果-校核（Value Verify）
    s_transportsystem_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"输煤系统运行小时-校核")
    # 每班运行小时 结果-设计（Value Design）
    s_shift_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"每班运行小时-设计")
    # 每班运行小时 结果-校核（Value Verify）
    s_shift_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"每班运行小时-校核")
    # 带宽 结果-设计（Value Design）
    s_belt_width_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"传输皮带宽-设计")
    # 带宽 结果-校核（Value Verify）
    s_belt_width_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"传输皮带宽-校核")
    # 断面系数 结果-设计（Value Design）
    s_section_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"断面系数-设计")
    # 断面系数 结果-校核（Value Verify）
    s_section_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"断面系数-校核")
    # 带速 结果-设计（Value Design）
    s_belt_speed_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"传输皮带速-设计")
    # 带速 结果-校核（Value Verify）
    s_belt_speed_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"传输皮带速-校核")
    # 物料松散密度 结果-设计（Value Design）
    s_material_bulk_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"物料松散密度-设计")
    # 物料松散密度 结果-校核（Value Verify）
    s_material_bulk_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"物料松散密度-校核")
    # 皮带最大输送能力 结果-设计（Value Design）
    s_belt_max_transport_capacity_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"皮带最大输送能力-设计")
    # 皮带最大输送能力 结果-校核（Value Verify）
    s_belt_max_transport_capacity_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"皮带最大输送能力-校核")
    # 台数 结果-设计（Value Design）
    g_equipment_sets_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"台数-设计")
    # 台数 结果-校核（Value Verify）
    g_equipment_sets_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"台数-校核")
    # 富裕量 结果-设计（Value Design）
    g_surplus_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富裕量-设计")
    # 富裕量 结果-校核（Value Verify）
    g_surplus_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富裕量-校核")
    # 单台给煤机出力 结果-设计（Value Design）
    g_single_coal_feeder_output_design = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"单台给煤机出力-设计")
    # 单台给煤机出力 结果-校核（Value Verify）
    g_single_coal_feeder_output_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"单台给煤机出力-校核")

    def __init__(self, **kwargs):
        super(CoalCHPCoalHandingSystem, self).__init__(**kwargs)

    @staticmethod
    def insert_handing_system(coalCHPCoalHandingSystem):
        try:
            db.session.add(coalCHPCoalHandingSystem)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPCoalHandingSystem"
                  "<id=%s> in database" % (coalCHPCoalHandingSystem.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_handing_system(plan_id):
        result = CoalCHPCoalHandingSystem.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_handing_system(plan_id):
        handing_system = CoalCHPCoalHandingSystem.search_handing_system(
            plan_id)
        try:
            db.session.delete(handing_system)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete handing_system<id=%s, plan_id=%s> in database" %
                  (handing_system.id, handing_system.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        handing_system = CoalCHPCoalHandingSystem.search_handing_system(
            plan_id)
        db.session.delete(handing_system)


# 锅炉计算表
class CoalCHPFurnaceCalculation(db.Model):
    # 表名
    __tablename__ = 'coalchp_furnace_calculation'
    __table_args__ = {'comment': u'燃煤热电联产-锅炉计算表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 1收到基碳含量:设计
    s_carbon_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基碳含量-设计")
    # 1收到基碳含量:校核
    s_carbon_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基碳含量-校核")
    # 1收到基氢含量:设计
    s_hydrogen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氢含量-设计")
    # 1收到基氢含量:校核
    s_hydrogen_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氢含量-校核")
    # 1收到基氧含量:设计
    s_oxygen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氧含量-设计")
    # 1收到基氧含量:校核
    s_oxygen_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氧含量-校核")
    # 1收到基氮含量:设计
    s_nitrogen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氮含量-设计")
    # 1收到基氮含量:校核
    s_nitrogen_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基氮含量-校核")
    # 1收到基硫含量:设计
    s_sulfur_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基硫含量-设计")
    # 1收到基硫含量:校核
    s_sulfur_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基硫含量-校核")
    # 1收到基灰分:设计
    s_grey_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基灰分-设计")
    # 1收到基灰分:校核
    s_grey_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基灰分-校核")
    # 1收到基水分:设计
    s_water_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基水分-设计")
    # 1收到基水分:校核
    s_water_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基水分-校核")
    # 1总和:设计
    s_sum_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总和-设计")
    # 1总和:校核
    s_sum_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总和-校核")
    # 干燥无灰基挥发分:设计
    s_daf_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干燥无灰基挥发分-设计")
    # 干燥无灰基挥发分:校核
    s_daf_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干燥无灰基挥发分-校核")
    # 哈氏可磨系数:设计
    s_grindability_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"哈氏可磨系数-设计")
    # 哈氏可磨系数:校核
    s_grindability_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"哈氏可磨系数-校核")
    # 1收到基低位发热量用户提供:设计
    s_low_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量用户提供-设计")
    # 1收到基低位发热量用户提供:校核
    s_low_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量用户提供-校核")
    # 2收到基低位发热量计算得到:设计
    s_low_1_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量计算得到-设计")
    # 2收到基低位发热量计算得到:校核
    s_low_1_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基低位发热量计算得到-校核")
    # 低位发热量估算:设计
    s_low_estimation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低位发热量估算-设计")
    # 低位发热量估算:校核
    s_low_estimation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低位发热量估算-校核")
    # 高位发热量估算:设计
    s_high_estimation_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高位发热量估算-设计")
    # 高位发热量估算:校核
    s_high_estimation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高位发热量估算-校核")
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
    p_heater_type_design = db.Column(db.Text, comment=u"空预器-设计")
    # 6空预器:校核
    p_heater_type_check = db.Column(db.Text, comment=u"空预器-校核")
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
    go_total_combustion_product_vol_check = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"总燃烧产物6%O2干体积-校核")
    # 锅炉参数选择
    boiler_params_select = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"锅炉参数选择")

    def __init__(self, **kwargs):
        super(CoalCHPFurnaceCalculation, self).__init__(**kwargs)

    @staticmethod
    def insert_furnace_calculation(coalCHPFurnaceCalculation):
        try:
            db.session.add(coalCHPFurnaceCalculation)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPFurnaceCalculation"
                  "<id=%s> in database" % (coalCHPFurnaceCalculation.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_furnace_calculation(plan_id):
        result = CoalCHPFurnaceCalculation.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_furnace_calculation(plan_id):
        furnace_calculation = \
            CoalCHPFurnaceCalculation.search_furnace_calculation(plan_id)
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

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        furnace_calculation = \
            CoalCHPFurnaceCalculation.search_furnace_calculation(plan_id)
        db.session.delete(furnace_calculation)


# 脱硫脱硝
class CoalCHPDesulfurization(db.Model):
    # 表名
    __tablename__ = 'coalchp_desulfurization_denitrification'
    __table_args__ = {'comment': u'燃煤热电联产-脱硫脱硝表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 收到基硫份设计值
    s_sulfur_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收到基硫份设计值")
    # 计算耗煤量设计值
    s_calcu_coal_consume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算耗煤量设计值")
    # 燃煤中的含硫量燃烧后氧化成SO2的份额设计值
    s_aflame_generate_so2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃煤中的含硫量燃烧后氧化成SO2的份额设计值")
    # 脱硫前烟气中的SO2含量设计值
    s_desulfrization_before_so2 = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硫前烟气中的SO2含量设计值")
    # 引风机进口烟气容积流量（标况）设计值
    s_fan_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口烟气容积流量（标况）设计值")
    # 未脱硫前SO2浓度（标态）设计值
    s_no_desulfurization_so2 = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"未脱硫前SO2浓度（标态）设计值")
    # 脱硫效率设计值
    s_desulfurization_efficiency = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硫效率设计值")
    # 脱硫后SO2浓度（标态）设计值
    s_desulfrization_after_so2 = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硫后SO2浓度（标态）设计值")
    # 脱硫后SO2排放量（标态）设计值
    s_desulfrization_after_discharge_so2 = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硫后SO2排放量（标态）设计值")
    # 炉内脱硫百分比设计值
    r_furnace_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硫百分比设计值")
    # 炉内脱硫后SO2浓度设计值
    r_furnace_concentration = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硫后SO2浓度设计值")
    # 脱除SO2质量设计值
    r_others_mass = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱除SO2质量设计值")
    # 脱除SO2摩尔量设计值
    r_others_mole = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱除SO2摩尔量设计值")
    # 钙硫摩尔比设计值
    r_calcium_sulfur_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"钙硫摩尔比设计值")
    # 反应所需CaCO3摩尔量设计值
    r_nees_caco3_mole = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"反应所需CaCO3摩尔量设计值")
    # 反应所需CaCO3质量设计值
    r_nees_caco3_mass = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"反应所需CaCO3质量设计值")
    # 参加反应CaCO3质量设计值
    r_use_caco3_mass = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"参加反应CaCO3质量设计值")
    # 反应生成CaSO4质量设计值
    r_generate_coco3_mass = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"反应生成CaSO4质量设计值")
    # 反应后质量增加设计值
    r_add_mass = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"反应后质量增加设计值")
    # 石灰石纯度设计值
    r_caco3_pure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石纯度设计值")
    # 石灰石耗量设计值
    r_coco3_consume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石耗量设计值")
    # 炉内脱硫产生的灰渣量设计值
    r_generate_grey = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硫产生的灰渣量设计值")
    # 石灰石粉仓储存时间设计值
    r_storage_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉仓储存时间设计值")
    # 石灰石粉仓出力设计值
    r_storage_output = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉仓出力设计值")
    # 石灰石粉堆积密度设计值
    r_storage_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉堆积密度设计值")
    # 石灰石粉库充满系数设计值
    r_storage_fullness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉库充满系数设计值")
    # 石灰石粉仓体积设计值
    r_storage_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石粉仓体积设计值")
    # 高设计值
    r_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高设计值")
    # 直径设计值
    r_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"直径设计值")
    # 石灰石纯度设计值
    d_limestone_pure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石纯度设计值")
    # Ca/S（钙硫比）设计值
    d_proportion_ca_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"Ca/S（钙硫比）设计值")
    # 脱硫效率设计值
    d_desulfurization_efficiency = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硫效率设计值")
    # 石灰石消耗量设计值
    d_limestone_consume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"石灰石消耗量设计值")
    # 生成CaSO4量设计值
    d_gengrate_coca4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"生成CaSO4量设计值")
    # 脱硝前NOX浓度设计值
    n_before_nox_concentration = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硝前NOX浓度设计值")
    # 引风机进口烟气容积流量（标况）设计值
    n_input_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机进口烟气容积流量（标况）设计值")
    # 脱硝效率(总效率)设计值
    n_desulfurization_efficiency = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硝效率(总效率)设计值")
    # 脱硝前NOX排放量设计值
    n_before_nox_discharge = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硝前NOX排放量设计值")
    # 脱硝后NOX浓度设计值
    n_after_nox_concentration = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"脱硝后NOX浓度设计值")
    # 环保要求NOX的排放浓度设计值
    n_env_after_nox_concentration = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"环保要求NOX的排放浓度设计值")
    # 脱硝后NOX排放量设计值
    n_after_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硝后NOX排放量设计值")
    # 炉内脱硝百分比设计值
    d_denitration_percentage = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硝百分比设计值")
    # 炉内脱硝量设计值
    d_denitration_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硝量设计值")
    # 炉内脱硝后NOX排放量设计值
    d_after_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硝后NOX排放量设计值")
    # 炉内脱硝摩尔量设计值
    d_denitration_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"炉内脱硝摩尔量设计值")
    # 氨逃逸率设计值
    d_escape_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氨逃逸率设计值")
    # 氨逃逸量设计值
    d_escape_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氨逃逸量设计值")
    # 逃逸氨折算尿素量设计值
    d_escape_quality_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"逃逸氨折算尿素量设计值")
    # NH3/NOX摩尔比设计值
    d_nh3nox_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"NH3/NOX摩尔比设计值")
    # 尿素/NOX摩尔比设计值
    d_urea_nox_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素/NOX摩尔比设计值")
    # 尿素/NOX式量比设计值
    d_urea_nox_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素/NOX式量比设计值")
    # 理论尿素消耗量设计值
    d_theory_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论尿素消耗量设计值")
    # 尿素用量(一台炉)设计值
    d_use_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素用量(一台炉)设计值")
    # 尿素溶液消耗水量(一台炉)设计值
    d_water_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素溶液消耗水量(一台炉)设计值")
    # 尿素仓库天数设计值
    d_days_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素仓库天数设计值")
    # 尿素仓库容量设计值
    d_capacity_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素仓库容量设计值")
    # 烟气脱硝百分比设计值
    g_denitration_percentage = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"烟气脱硝百分比设计值")
    # 烟气脱硝后NOX排放量设计值
    g_after_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气脱硝后NOX排放量设计值")
    # 烟气脱硝量设计值
    g_denitration_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气脱硝量设计值")
    # 氨逃逸率设计值
    g_escape_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氨逃逸率设计值")
    # 氨逃逸量设计值
    g_escape_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氨逃逸量设计值")
    # 逃逸氨折算尿素量设计值
    g_escape_quality_urea = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"逃逸氨折算尿素量设计值")
    # NH3/NOX摩尔比设计值
    g_nh3nox_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"NH3/NOX摩尔比设计值")
    # 尿素/NOX摩尔比设计值
    g_urea_nox_molar = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素/NOX摩尔比设计值")
    # 尿素/NOX式量比设计值
    g_urea_nox_quality = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素/NOX式量比设计值")
    # 理论尿素消耗量设计值
    g_theory_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论尿素消耗量设计值")
    # 尿素用量(一台炉)设计值
    g_use_urea = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"尿素用量(一台炉)设计值")

    def __init__(self, **kwargs):
        super(CoalCHPDesulfurization, self).__init__(**kwargs)

    @staticmethod
    def insert_desulfurization(coalCHPDesulfurization):
        try:
            db.session.add(coalCHPDesulfurization)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPDesulfurization"
                  "<id=%s> in database" % (coalCHPDesulfurization.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_desulfurization(plan_id):
        result = CoalCHPDesulfurization.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_desulfurization(plan_id):
        desulfurization = CoalCHPDesulfurization.search_desulfurization(
            plan_id)
        try:
            db.session.delete(desulfurization)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete desulfurization<id=%s, plan_id=%s> in database" %
                  (desulfurization.id, desulfurization.plan_id))
 
    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        desulfurization = CoalCHPDesulfurization.search_desulfurization(
            plan_id)
        db.session.delete(desulfurization)


# 锅炉辅机系统表
class CoalCHPBoilerAuxiliaries(db.Model):
    # 表名
    __tablename__ = 'coalchp_boiler_auxiliaries'
    __table_args__ = {'comment': u'燃煤热电联产-锅炉辅机系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

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
    r_drum_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-汽包压力下的饱和水焓")
    # 排污扩容器工作压力
    r_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污扩容器工作压力")
    # 扩容器压力下饱和水焓
    r_work_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器压力下饱和水焓")
    # 扩容器压力下汽化潜热
    r_work_latentheat_vaporization = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器压力下汽化潜热")
    # 扩容器单位容积润许极限强度
    r_ultimate_strength = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器单位容积润许极限强度")
    # 富裕系数
    r_affluence_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-富裕系数")
    # 排污扩容容积
    r_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污扩容容积")
    # 扩容器规格选取
    r_specifications = db.Column(db.String(200), comment=u"定期排污扩容器-扩容器规格选取")

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
    c_drum_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-汽包压力下的饱和水焓")
    # 排污扩容器工作压力
    c_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污扩容器工作压力")
    # 扩容器压力下饱和水焓
    c_work_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下饱和水焓")
    # 扩容器压力下蒸汽比容
    c_work_steam_pecificvolume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下蒸汽比容")
    # 扩容器压力下汽化潜热
    c_work_latentheat_vaporization = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下汽化潜热")
    # 扩容器蒸汽干度
    c_steam_dryness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器蒸汽干度")
    # 扩容器单位容积润许极限强度
    c_ultimate_strength = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器单位容积润许极限强度")
    # 排污水汽化量
    c_vaporization_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污水汽化量")
    # 富裕系数
    c_affluence_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-富裕系数")
    # 排污扩容汽容积
    c_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污扩容汽容积")
    # 扩容器规格选取
    c_specifications = db.Column(db.String(200), comment=u"连续排污扩容器-扩容器规格选取")

    # 磷酸盐加药装置
    # 锅炉水系统容积
    d_boiler_watersystem_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-锅炉水系统容积")
    # 应维持的磷酸根含量
    d_phosphate_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-应维持的磷酸根含量")
    # 给水硬度（原水）
    d_water_hardness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-给水硬度（原水）")
    # 纯度
    d_purity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-纯度")
    # 锅炉启动时加药量
    d_boiler_dosage_startup = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-锅炉启动时加药量")
    # 锅炉给水量
    d_boiler_water_supply = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-锅炉给水量")
    # 锅炉排污量
    d_boiler_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-锅炉排污量")
    # 运行时加药量
    d_boiler_dosage_run = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-运行时加药量")
    # 磷酸钠浓度
    d_na3po4_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-磷酸钠浓度")
    # 在C浓度下的磷酸三钠密度
    d_na3po4_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-在C浓度下的磷酸三钠密度")
    # 运行时汽包内加入的溶液量
    d_solution_quantity_run = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-运行时汽包内加入的溶液量")

    # 给水泵
    # 锅炉设计使用压力
    p_boiler_design_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-锅炉设计使用压力")
    # 省煤器入口进水压力
    p_inlet_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-省煤器入口进水压力")
    # 除氧器工作压力
    p_deaerator_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-除氧器工作压力")
    # 给水管阻力（以压头计）
    p_water_supply_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-给水管阻力（以压头计）")
    # 进水管阻力（以压头计）
    p_water_inlet_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-进水管阻力（以压头计）")
    # 水泵中心至汽包正常水位的几何高度差
    p_center_altitude_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-水泵中心至汽包正常水位的几何高度差")
    # 除氧器最低水位至水泵中心几何高度差（给水泵进口静水头）
    p_deaerator_altitude_difference = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"给水泵-除氧器最低水位至水泵中心几何高度差（给水泵进口静水头）")
    # 给水泵总扬程
    p_feedpump_total_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-给水泵总扬程")
    # 流量
    p_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-流量")
    # 泵效率
    p_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-泵效率")
    # 机械传动效率
    p_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-机械传动效率")
    # 电动机效率
    p_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-电动机效率")
    # 电动机备用系数
    p_motor_reserve_factor = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-电动机备用系数")
    # 配套电机功率
    p_auxiliary_motor_power = db.Column(db.String(20), comment=u"给水泵-配套电机功率")
    # 给水泵选用规格
    p_specifications = db.Column(db.String(200), comment=u"给水泵-给水泵选用规格")

    # 除氧水箱/凝结水箱 共用
    # 锅炉蒸发
    s_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-锅炉蒸发")
    # 储水时间
    s_storage_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-储水时间")
    # 容积
    s_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-容积")
    # 尺寸 长
    s_size_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-尺寸 长")
    # 尺寸 直径
    s_size_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-尺寸 直径")

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


    def __init__(self, **kwargs):
        super(CoalCHPBoilerAuxiliaries, self).__init__(**kwargs)

    @staticmethod
    def insert_boiler_auxiliaries(coalCHPBoilerAuxiliaries):
        try:
            db.session.add(coalCHPBoilerAuxiliaries)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPBoilerAuxiliaries"
                  "<id=%s> in database" % (coalCHPBoilerAuxiliaries.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_boiler_auxiliaries(plan_id):
        result = CoalCHPBoilerAuxiliaries.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_boiler_auxiliaries(plan_id):
        boiler_auxiliaries = \
            CoalCHPBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
        try:
            db.session.delete(boiler_auxiliaries)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete boiler_auxiliaries<id=%s, plan_id=%s> in database" %
                  (boiler_auxiliaries.id, boiler_auxiliaries.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        boiler_auxiliaries = \
            CoalCHPBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
        db.session.delete(boiler_auxiliaries)

# 烟风系统
class CoalCHPSmokeAirSystem(db.Model):
    # 表名
    __tablename__ = 'coalchp_smoke_air_system'
    __table_args__ = {'comment': u'燃煤热电联产-烟风系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 海拔
    a_altitude = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"海拔")
    # 大气压
    a_atmospheric_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压")

    # 标况温度
    p_the_case_temperature_f = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度-一次风")
    # 标况压力
    p_standard_of_pressure_f = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力-一次风")
    # 标况流量
    p_standard_of_flow_f = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况流量-一次风")
    # 工况温度
    p_temperature_case_f = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度-一次风")
    # 当地大气压
    p_local_atmosphere_f = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压-一次风")
    # 工况流量
    p_operational_point_flow_f = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量-一次风")
    # 标况温度
    p_the_case_temperature_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度-二次风")
    # 标况压力
    p_standard_of_pressure_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力-二次风")
    # 标况流量
    p_standard_of_flow_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况流量-二次风")
    # 工况温度
    p_temperature_case_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度-二次风")
    # 当地大气压
    p_local_atmosphere_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压-二次风")
    # 工况流量
    p_operational_point_flow_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量-二次风")
    # 标况温度
    p_the_case_temperature_t = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况温度-烟")
    # 标况压力
    p_standard_of_pressure_t = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况压力-烟")
    # 标况流量
    p_standard_of_flow_t = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况流量-烟")
    # 工况温度
    p_temperature_case_t = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况温度-烟")
    # 当地大气压
    p_local_atmosphere_t = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压-烟")
    # 工况流量
    p_operational_point_flow_t = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"工况流量-烟")

    # 名称
    f_name = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"名称-一次风")
    # 空气温度
    f_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气温度-一次风")
    # 锅炉本体阻力
    f_boiler_body_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉本体阻力-一次风")
    # 风道阻力
    f_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风道阻力-一次风")
    # 当地大气压
    f_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压-一次风")
    # 烟风流量（工况）
    f_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟风流量（工况）-一次风")
    # 风比
    f_wind_Proportion = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风比-一次风")
    # 台数
    f_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"台数-一次风")
    # 铭牌介质温度
    f_nameplate_medium_temperature = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"铭牌介质温度-一次风")
    # 风机全压
    f_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机全压-一次风")
    # 风机选用全压
    f_fan_select_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用全压-一次风")
    # 风机选用流量
    f_fan_selection_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用流量-一次风")
    # 风机效率
    f_fan_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机效率-一次风")
    # 电动机效率
    f_electric_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率-一次风")
    # 风机轴功率
    f_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机轴功率-一次风")
    # 电机安全裕量
    f_fan_security_volumn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机安全裕量-一次风")
    # 电机功率
    f_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机功率-一次风")
    # 选型
    f_lectotype = db.Column(db.String(200), comment=u"选型-一次风")

    # 名称
    s_name = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"名称-二次风")
    # 空气温度
    s_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气温度-二次风")
    # 锅炉本体阻力
    s_boiler_body_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉本体阻力-二次风")
    # 风道阻力
    s_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风道阻力-二次风")
    # 当地大气压
    s_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压-二次风")
    # 烟风流量（工况）
    s_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟风流量（工况）-二次风")
    # 台数
    s_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"台数-二次风")
    # 铭牌介质温度
    s_nameplate_medium_temperature = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"铭牌介质温度-二次风")
    # 风机全压
    s_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机全压-二次风")
    # 风机选用全压
    s_fan_select_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用全压-二次风")
    # 风机选用流量
    s_fan_selection_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用流量-二次风")
    # 风机效率
    s_fan_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机效率-二次风")
    # 电动机效率
    s_electric_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率-二次风")
    # 风机轴功率
    s_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机轴功率-二次风")
    # 电机安全裕量
    s_fan_security_volumn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机安全裕量-二次风")
    # 电机功率
    s_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机功率-二次风")
    # 选型
    s_lectotype = db.Column(db.String(200), comment=u"选型-二次风")

    # 名称
    i_name = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"名称-引风机")
    # 烟气温度
    i_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气温度-引风机")
    # 锅炉本体阻力
    i_boiler_body_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉本体阻力-引风机")
    # 脱硝
    i_denitration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"脱硝-引风机")
    # 除尘器
    i_duster = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器-引风机")
    # 风道阻力
    i_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风道阻力-引风机")
    # 风机后脱硫塔及烟囱烟道阻力
    i_resistance_desulfurization_fan = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"风机后脱硫塔及烟囱烟道阻力-引风机")
    # 当地大气压
    i_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压-引风机")
    # 烟风流量（工况）
    i_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟风流量（工况）-引风机")
    # 台数
    i_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"台数-引风机")
    # 铭牌介质温度
    i_nameplate_medium_temperature = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"铭牌介质温度-引风机")
    # 风机全压
    i_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机全压-引风机")
    # 风机选用全压
    i_fan_select_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用全压-引风机")
    # 风机选用流量
    i_fan_selection_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用流量-引风机")
    # 风机效率
    i_fan_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机效率-引风机")
    # 电动机效率
    i_electric_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率-引风机")
    # 风机轴功率
    i_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机轴功率-引风机")
    # 电机安全裕量
    i_fan_security_volumn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机安全裕量-引风机")
    # 电机功率
    i_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机功率-引风机")
    # 选型
    i_lectotype = db.Column(db.String(200), comment=u"选型-引风机")

    # 名称
    r_name = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"名称-返料风机")
    # 空气温度
    r_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气温度-返料风机")
    # 锅炉本体阻力
    r_boiler_body_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉本体阻力-返料风机")
    # 风道阻力
    r_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风道阻力-返料风机")
    # 当地大气压
    r_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地大气压-返料风机")
    # 烟风流量（工况）
    r_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟风流量（工况）-返料风机")
    # 铭牌介质温度
    r_nameplate_medium_temperature = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"铭牌介质温度-返料风机")
    # 风机全压
    r_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机全压-返料风机")
    # 风机选用全压
    r_fan_select_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用全压-返料风机")
    # 风机选用流量
    r_fan_selection_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机选用流量-返料风机")
    # 风机效率
    r_fan_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机效率-返料风机")
    # 电动机效率
    r_electric_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率-返料风机")
    # 风机轴功率
    r_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风机轴功率-返料风机")
    # 电机安全裕量
    r_fan_security_volumn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机安全裕量-返料风机")
    # 电机功率
    r_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电机功率-返料风机")
    # 选型
    r_lectotype = db.Column(db.String(200), comment=u"选型-返料风机")

    def __init__(self, **kwargs):
        super(CoalCHPSmokeAirSystem, self).__init__(**kwargs)

    @staticmethod
    def insert_smoke_air_system(coalCHPSmokeAirSystem):
        try:
            db.session.add(coalCHPSmokeAirSystem)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPSmokeAirSystem"
                  "<id=%s> in database" % (coalCHPSmokeAirSystem.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_smoke_air_system(plan_id):
        result = CoalCHPSmokeAirSystem.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_smoke_air_system(plan_id):
        smoke_air_system = \
            CoalCHPSmokeAirSystem.search_smoke_air_system(plan_id)
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

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        smoke_air_system = \
            CoalCHPSmokeAirSystem.search_smoke_air_system(plan_id)
        db.session.delete(smoke_air_system)

# 除灰除渣系统
class CoalCHPRemovalAshSlag(db.Model):
    # 表名
    __tablename__ = 'coalchp_removal_ash_slag_system'
    __table_args__ = {'comment': u'燃煤热电联产-除灰除渣系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 灰渣总量(炉内脱硫后)
    a_total_ash_residue_after = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰渣总量(炉内脱硫后)")
    # 飞灰份额
    a_fly_ash_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"飞灰份额")
    # 除尘器入口（锅炉出口）飞灰量
    a_dust_collector_inlet_ = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器入口（锅炉出口）飞灰量")
    # 标况下除尘器进口烟气容积流量
    a_the_imported_smoke_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器进口烟气容积流量")
    # 除尘器进口处烟气容积流量(实态）
    a_the_smoke_volume_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气容积流量(实态）")
    # 标况下除尘器进口烟气浓度
    a_the_smoke_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况下除尘器进口烟气浓度")
    # 除尘器进口处烟气浓度(实态）
    a_the_smoke_concentration_solid = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"除尘器进口处烟气浓度(实态）")
    # 除尘效率
    a_collection_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘效率")
    # 除尘器（烟囱）出口烟气浓度（标况）
    a_the_smoke_concentration_chimney = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"除尘器（烟囱）出口烟气浓度（标况）")
    # 除尘器（烟囱）出口烟气飞灰量（标况）
    a_dust_collector_stack = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器（烟囱）出口烟气飞灰量（标况）")
    # 除尘器下灰量
    a_ash_under_dust_collector = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除尘器下灰量")
    # 引风机进口烟气容积量(实态）
    a_the_imported_smoke_real_state = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"引风机进口烟气容积量(实态）")
    # 烟囱出口烟气浓度（实态）
    a_flue_gas_concentratio = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口烟气浓度（实态）")

    # 出力系数
    r_removal_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"出力系数")
    # 除灰系统出力
    r_removal_the_ash_system = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除灰系统出力")
    # 干灰堆积密度
    r_dry_ash_accumulation_density = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"干灰堆积密度")
    # 渣库充满系数
    r_slag_accumulation_coefficient = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"渣库充满系数")
    # 存灰时间
    r_stored_ash = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"存灰时间")
    # 灰库有效体积
    r_effective_volume_ash_storage = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"灰库有效体积")
    # 直径
    r_dia = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰库直径")
    # 高度
    r_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰库高度")

    # 灰气比
    g_grey_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"灰气比")
    # 输灰系统耗气量
    g_air_transport_ash_system = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"输灰系统耗气量")

    # 渣量
    s_slag_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"渣量")
    # 冷渣机的出力（单台）
    s_output_cold_single_stage = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷渣机的出力（单台）")
    # 冷渣机台数
    s_cold_single_stage_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷渣机台数")
    # 除渣系统出力
    s_slag_removal_system = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除渣系统出力")
    # 耐高温带式输送机出力
    s_high_temperature_belt_conveyor = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"耐高温带式输送机出力")
    # 冷渣堆积密度
    s_cold_slag_accumulation_density = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"冷渣堆积密度")
    # 渣库充满系数
    s_slag_accumulation_coefficient = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"渣库充满系数")
    # 存渣时间
    s_sludge_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"存渣时间")
    # 渣库有效体积
    s_slag_storage_volume_effective = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"渣库有效体积")
    # 直径
    s_dia = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"渣库直径")
    # 高度
    s_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"渣库高度")

    def __init__(self, **kwargs):
        super(CoalCHPRemovalAshSlag, self).__init__(**kwargs)

    @staticmethod
    def insert_removal_ash_slag(coalCHPRemovalAshSlag):
        try:
            db.session.add(coalCHPRemovalAshSlag)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPRemovalAshSlag"
                  "<id=%s> in database" % (coalCHPRemovalAshSlag.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_removal_ash_slag(plan_id):
        result = CoalCHPRemovalAshSlag.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_removal_ash_slag(plan_id):
        removal_ash_slag = \
            CoalCHPRemovalAshSlag.search_removal_ash_slag(plan_id)
        try:
            db.session.delete(removal_ash_slag)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete removal_ash_slag<id=%s, plan_id=%s> in database" %
                  (removal_ash_slag.id, removal_ash_slag.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        removal_ash_slag = \
            CoalCHPRemovalAshSlag.search_removal_ash_slag(plan_id)
        db.session.delete(removal_ash_slag)

# 循环水系统
class CoalCHPCirculatingWater(db.Model):
    # 表名
    __tablename__ = 'coalchp_circulating_water'
    __table_args__ = {'comment': u'燃煤热电联产-循环水系统表'}

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
    # 分吹损失
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
    # 循环水池尺寸(长)
    v_circulating_pool_long = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池深")
    # 循环水池尺寸（宽）
    v_circulating_pool_wide = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池长")
    # 循环水池尺寸（高）
    v_circulating_pool_hight = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池宽")
    # 校核循环水池尺寸
    v_check_circulating_pool_size = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"校核循环水池尺寸")

    circleWaterSelect = db.Column(db.NUMERIC(precision=15, scale=5))

    # 方案一 自然通风双曲线冷却塔
    # 喷淋密度
    p_spray_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"自然通风双曲线冷却塔喷淋密度")
    # 喉部喷淋面积
    p_spray_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"自然通风双曲线冷却塔喷淋面积")
    # 选型
    p_select_f = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"自然通风双曲线冷却塔选型")

    # 方案二 机力通风冷却塔
    # 数量
    p_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机力通风冷却塔数量")
    # 单台冷却水量
    p_single_cold_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机力通风冷却塔水量")
    # 选型
    p_select_s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机力通风冷却塔选型")

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
        super(CoalCHPCirculatingWater, self).__init__(**kwargs)

    @staticmethod
    def insert_circulating_water(coalCHPCirculatingWater):
        try:
            db.session.add(coalCHPCirculatingWater)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPCirculatingWater"
                  "<id=%s> in database" % (coalCHPCirculatingWater.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_circulating_water(plan_id):
        result = CoalCHPCirculatingWater.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_circulating_water(plan_id):
        circulating_water = \
            CoalCHPCirculatingWater.search_circulating_water(plan_id)
        try:
            db.session.delete(circulating_water)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete circulating_water<id=%s, plan_id=%s> in database" %
                  (circulating_water.id, circulating_water.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        circulating_water = \
            CoalCHPCirculatingWater.search_circulating_water(plan_id)
        db.session.delete(circulating_water)

# 汽轮机计算表
class CoalCHPTurbineBackpressure (db.Model):
    # 表名
    __tablename__ = 'coalchp_turbine_backpressure'
    __table_args__ = {'comment': u'燃煤热电联产-汽轮机计算表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

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
        super(CoalCHPTurbineBackpressure, self).__init__(**kwargs)

    @staticmethod
    def insert_turbineBackpressure(coapTurbineBackpressure):
        try:
            db.session.add(coapTurbineBackpressure)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coapTurbineBackpressure"
                  "<id=%s> in database" % (coapTurbineBackpressure.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_turbineBackpressure(plan_id):
        result = CoalCHPTurbineBackpressure.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result


    # 根据plan_id删除实体
    @staticmethod
    def delete_turbineBackpressure(plan_id):
        turbineBackpressure = \
            CoalCHPTurbineBackpressure.search_turbineBackpressure(plan_id)
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

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        turbineBackpressure = \
            CoalCHPTurbineBackpressure.search_turbineBackpressure(plan_id)
        db.session.delete(turbineBackpressure)

# 主要技术经济指标
class CoalCHPEconomicIndicators(db.Model):
    # 表名
    __tablename__ = 'coalchp_economic_indicators'
    __table_args__ = {'comment': u'燃煤热电联产-主要技术经济指标表'}

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
        super(CoalCHPEconomicIndicators, self).__init__(**kwargs)

    @staticmethod
    def insert_economic_indicators(CoalCHPEconomicIndicators):
        try:
            db.session.add(CoalCHPEconomicIndicators)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update CoalCHPEconomicIndicators"
                  "<id=%s> in database" % (CoalCHPEconomicIndicators.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_economic_indicators(plan_id):
        result = CoalCHPEconomicIndicators.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_economic_indicators(plan_id):
        economic_indicators = \
            CoalCHPEconomicIndicators.search_economic_indicators(plan_id)
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

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        economic_indicators = \
            CoalCHPEconomicIndicators.search_economic_indicators(plan_id)
        db.session.delete(economic_indicators)

# 化学水系统
class CoalCHPChemicalWater(db.Model):
    # 表名
    __tablename__ = 'coalchp_chemical_water'
    __table_args__ = {'comment': u'燃煤热电联产-化学水系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 锅炉补给水处理能力
    # 工艺路线
    m_process_route = db.Column(db.NUMERIC(precision=15, scale=5))
    # # 锅炉蒸发量
    m_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-锅炉蒸发量")
    # 补汽量
    m_makeup_steam = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-补汽量")
    # 厂内汽水循环损失
    m_steamwater_cycle_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-厂内汽水循环损失")
    # 排污损失
    m_pollution_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-排污损失")
    # 凝结水量
    m_condensing_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-凝结水量")
    # 换热凝结水损失
    m_condensate_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-换热凝结水损失")
    # 锅炉正常补水量
    m_boiler_normal_watersupply = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-锅炉正常补水量")
    # 启动或事故增加损失
    m_increase_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-启动或事故增加损失")
    # 锅炉最大补水量
    m_boiler_max_watersupply = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-锅炉最大补水量")
    # 选取水处理设备出力
    m_output = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-选取水处理设备出力")
    # 除盐水箱有效容积
    m_remove_salt_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-除盐水箱有效容积")


    def __init__(self, **kwargs):
        super(CoalCHPChemicalWater, self).__init__(**kwargs)

    # CoalCHPChemicalWater
    @staticmethod
    def insert_chemical_water(coalCHPChemicalWater):
        try:
            db.session.add(coalCHPChemicalWater)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPChemicalWater"
                  "<id=%s> in database" % (coalCHPChemicalWater.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_chemical_water(plan_id):
        result = CoalCHPChemicalWater.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_chemical_water(plan_id):
        chemical_water = \
            CoalCHPChemicalWater.search_chemical_water(plan_id)
        try:
            db.session.delete(chemical_water)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete chemical_water<id=%s, plan_id=%s> in database" %
                  (chemical_water.id, chemical_water.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        chemical_water = \
            CoalCHPChemicalWater.search_chemical_water(plan_id)
        db.session.delete(chemical_water)

# 烟囱表
class CoalCHPChimney(db.Model):
    # 表名
    __tablename__ = 'coalchp_chimney'
    __table_args__ = {'comment': u'燃煤热电联产-烟囱表'}

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
        super(CoalCHPChimney, self).__init__(**kwargs)

    @staticmethod
    def insert_coalCHPChimney(coalCHPChimney):
        try:
            db.session.add(coalCHPChimney)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPChimney"
                  "<id=%s> in database" % (coalCHPChimney.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_coalCHPChimney(plan_id):
        result = CoalCHPChimney.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_coalCHPChimney(plan_id):
        coalCHPChimney = CoalCHPChimney.search_coalCHPChimney(plan_id)
        try:
            db.session.delete(coalCHPChimney)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete coalCHPChimney<id=%s, plan_id=%s> in database" %
                  (coalCHPChimney.id, coalCHPChimney.plan_id))
    
    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        coalCHPChimney = CoalCHPChimney.search_coalCHPChimney(plan_id)
        db.session.delete(coalCHPChimney)

# 汽机辅机
class CoalchpTurbineAuxiliary(db.Model):
    # 表名
    __tablename__ = 'coalchp_turbine_auxiliary'
    __table_args__ = {'comment': u'燃煤热电联产-汽机辅机系统表'}

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
        super(CoalchpTurbineAuxiliary, self).__init__(**kwargs)

    @staticmethod
    def insert_turbine_auxiliary(coalchpTurbineAuxiliary):
        try:
            db.session.add(coalchpTurbineAuxiliary)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalchpTurbineAuxiliary"
                  "<id=%s> in database" % (coalchpTurbineAuxiliary.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_turbine_auxiliary(plan_id):
        result = CoalchpTurbineAuxiliary.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_turbine_auxiliary(plan_id):
        turbine_auxiliary = \
            CoalchpTurbineAuxiliary.search_turbine_auxiliary(plan_id)
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

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        turbine_auxiliary = \
            CoalchpTurbineAuxiliary.search_turbine_auxiliary(plan_id)
        db.session.delete(turbine_auxiliary)

# 采暖供热系统表
class CoalCHPHeatSupply(db.Model):
    # 表名
    __tablename__ = 'coalchp_heat_supply'
    __table_args__ = {'comment': u'燃煤热电联产-采暖供热系统表'}

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
        super(CoalCHPHeatSupply, self).__init__(**kwargs)

    @staticmethod
    def insert_heatSupply(coalCHPHeatSupply):
        try:
            db.session.add(coalCHPHeatSupply)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalCHPHeatSupply"
                  "<id=%s> in database" % (coalCHPHeatSupply.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_heatSupply(plan_id):
        result = CoalCHPHeatSupply.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result


    # 根据plan_id删除实体
    @staticmethod
    def delete_heatSupply(plan_id):
        heatSupply = \
            CoalCHPHeatSupply.search_heatSupply(plan_id)
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

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        heatSupply = \
            CoalCHPHeatSupply.search_heatSupply(plan_id)
        db.session.delete(heatSupply)

# 公用工程表
class CoalCHPOfficialProcess(db.Model):
    # 表名
    __tablename__ = 'coalchp_official_process'
    __table_args__ = {'comment': u'燃煤热电联产-公用工程表'}

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


    def __init__(self, **kwargs):
        super(CoalCHPOfficialProcess, self).__init__(**kwargs)

    @staticmethod
    def insert_official(coalOfficial):
        try:
            db.session.add(coalOfficial)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update coalOfficial"
                  "<id=%s> in database" % (coalOfficial.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_official(plan_id):
        result = CoalCHPOfficialProcess.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result


    # 根据plan_id删除实体
    @staticmethod
    def delete_official(plan_id):
        official = \
            CoalCHPOfficialProcess.search_official(plan_id)
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

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        official = \
            CoalCHPOfficialProcess.search_official(plan_id)
        db.session.delete(official)