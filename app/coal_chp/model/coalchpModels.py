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
    __tablename__ = 'coalchp_needs_questionnaire'

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


# 表名 燃煤热电联产计算_输煤系统表
class CoalCHPCoalHandingSystem(db.Model):
    # 表名
    __tablename__ = 'coalchp_coal_handingsystem'
    # 主ID， 自动生成
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 锅炉额定耗煤量 结果-设计（Value Design）
    b_boiler_rated_coal_capacity_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉额定耗煤量 结果-校核（Value Verify）
    b_boiler_rated_coal_capacity_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉日利用小时数 结果-设计（Value Design）
    b_boiler_daily_utilization_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉日利用小时数 结果-校核（Value Verify）
    b_boiler_daily_utilization_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日耗煤量 结果-设计（Value Design）
    b_coal_daily_consumption_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日耗煤量 结果-校核（Value Verify）
    b_coal_daily_consumption_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉年利用小时数 结果-设计（Value Design）
    b_boiler_annual_utilization_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉年利用小时数 结果-校核（Value Verify）
    b_boiler_annual_utilization_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 年耗煤量 结果-设计（Value Design）
    b_coal_annual_consumption_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 年耗煤量 结果-校核（Value Verify）
    b_coal_annual_consumption_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日来煤不均衡系数 结果-设计（Value Design）
    b_daily_coal_unbalanced_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日来煤不均衡系数 结果-校核（Value Verify）
    b_daily_coal_unbalanced_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 铁路来煤日计算煤量 结果-设计（Value Design）
    b_daily_rail_coal_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 铁路来煤日计算煤量 结果-校核（Value Verify）
    b_daily_rail_coal_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 汽车来煤日计算煤量 结果-设计（Value Design）
    b_daily_vehicle_coal_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 汽车来煤日计算煤量 结果-校核（Value Verify）
    b_daily_vehicle_coal_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉每小时最大耗煤量 结果-设计（Value Design）
    c_boiler_hour_coal_capacity_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉每小时最大耗煤量 结果-校核（Value Verify）
    c_boiler_hour_coal_capacity_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉每日运行时数 结果-设计（Value Design）
    c_boiler_daily_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 锅炉每日运行时数 结果-校核（Value Verify）
    c_boiler_daily_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤的储备日数 结果-设计（Value Design）
    c_coal_store_days_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 煤的储备日数 结果-校核（Value Verify）
    c_coal_store_days_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 煤场存储量 结果-设计（Value Design）
    c_coalyard_store_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤场存储量 结果-校核（Value Verify）
    c_coalyard_store_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤堆通道占用系数 结果-设计（Value Design）
    c_coal_channel_occupy_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤堆通道占用系数 结果-校核（Value Verify）
    c_coal_channel_occupy_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤堆形状系数 结果-设计（Value Design）
    c_coal_shape_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤堆形状系数 结果-校核（Value Verify）
    c_coal_shape_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤堆高度 结果-设计（Value Design）
    c_coal_height_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 煤堆高度 结果-校核（Value Verify）
    c_coal_height_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 煤的堆密度 结果-设计（Value Design）
    c_coal_bulk_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤的堆密度 结果-校核（Value Verify）
    c_coal_bulk_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤场面积 结果-设计（Value Design）
    c_coalyard_area_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 煤场面积 结果-校核（Value Verify）
    c_coalyard_area_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长 结果-设计（Value Design）
    c_height_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长 结果-校核（Value Verify）
    c_height_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽 结果-设计（Value Design）
    c_width_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽 结果-校核（Value Verify）
    c_width_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 有效容积-计算 结果-设计（Value Design）
    e_effective_cubage_calculated_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 有效容积-计算 结果-校核（Value Verify）
    e_effective_cubage_calculated_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤仓个数 结果-设计（Value Design）
    e_coal_bunker_counts_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 煤仓个数 结果-校核（Value Verify）
    e_coal_bunker_counts_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 有效容积-选定 结果-设计（Value Design）
    e_effective_cubage_selected_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 有效容积-选定 结果-校核（Value Verify）
    e_effective_cubage_selected_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 反推消耗小时 结果-设计（Value Design）
    e_backstep_consumption_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 反推消耗小时 结果-校核（Value Verify）
    e_backstep_consumption_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运输不平衡系数 结果-设计（Value Design）
    t_transport_unbalanced_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运输不平衡系数 结果-校核（Value Verify）
    t_transport_unbalanced_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运煤系统有效作业时间 结果-设计（Value Design）
    t_transportsystem_effective_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运煤系统有效作业时间 结果-校核（Value Verify）
    t_transportsystem_effective_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运煤系统运输量 结果-设计（Value Design）
    t_transportsystem_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 运煤系统运输量 结果-校核（Value Verify）
    t_transportsystem_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 车辆名义载重量 结果-设计（Value Design）
    t_vehicle_capacity_tonnage_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 车辆名义载重量 结果-校核（Value Verify）
    t_vehicle_capacity_tonnage_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每昼夜小时 结果-设计（Value Design）
    t_daily_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每昼夜小时 结果-校核（Value Verify）
    t_daily_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日计算受煤量 结果-设计（Value Design）
    t_daily_received_coal_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 日计算受煤量 结果-校核（Value Verify）
    t_daily_received_coal_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每天进厂车次 结果-设计（Value Design）
    t_vehicle_daily_incoming_times_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每天进厂车次 结果-校核（Value Verify）
    t_vehicle_daily_incoming_times_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每小时进场车次 结果-设计（Value Design）
    t_vehicle_perhour_incoming_times_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每小时进场车次 结果-校核（Value Verify）
    t_vehicle_perhour_incoming_times_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 多锅炉额定耗煤量 结果-设计（Value Design）
    s_mutil_boiler_rated_coal_capacity_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 多锅炉额定耗煤量 结果-校核（Value Verify）
    s_mutil_boiler_rated_coal_capacity_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 多锅炉日额定耗煤总量 结果-设计（Value Design）
    s_mutil_boiler_rated_coal_amount_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 多锅炉日额定耗煤总量 结果-校核（Value Verify）
    s_mutil_boiler_rated_coal_amount_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 输煤系统选定出力 结果-设计（Value Design）
    s_transportsystem_output_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 输煤系统选定出力 结果-校核（Value Verify）
    s_transportsystem_output_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 输煤系统运行小时 结果-设计（Value Design）
    s_transportsystem_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 输煤系统运行小时 结果-校核（Value Verify）
    s_transportsystem_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每班运行小时 结果-设计（Value Design）
    s_shift_working_hours_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 每班运行小时 结果-校核（Value Verify）
    s_shift_working_hours_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 带宽 结果-设计（Value Design）
    s_belt_width_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 带宽 结果-校核（Value Verify）
    s_belt_width_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 断面系数 结果-设计（Value Design）
    s_section_coefficient_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 断面系数 结果-校核（Value Verify）
    s_section_coefficient_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 带速 结果-设计（Value Design）
    s_belt_speed_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 带速 结果-校核（Value Verify）
    s_belt_speed_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 物料松散密度 结果-设计（Value Design）
    s_material_bulk_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 物料松散密度 结果-校核（Value Verify）
    s_material_bulk_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 皮带最大输送能力 结果-设计（Value Design）
    s_belt_max_transport_capacity_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 皮带最大输送能力 结果-校核（Value Verify）
    s_belt_max_transport_capacity_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 台数 结果-设计（Value Design）
    g_equipment_sets_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 台数 结果-校核（Value Verify）
    g_equipment_sets_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 富裕量 结果-设计（Value Design）
    g_surplus_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 富裕量 结果-校核（Value Verify）
    g_surplus_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 单台给煤机出力 结果-设计（Value Design）
    g_single_coal_feeder_output_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 单台给煤机出力 结果-校核（Value Verify）
    g_single_coal_feeder_output_check = db.Column(
        db.NUMERIC(precision=15, scale=5))

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


# 锅炉计算表
class CoalCHPFurnaceCalculation(db.Model):
    # 表名
    __tablename__ = 'coalchp_furnace_calculation'

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 1收到基碳含量:设计
    s_carbon_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基碳含量:校核
    s_carbon_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基氢含量:设计
    s_hydrogen_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基氢含量:校核
    s_hydrogen_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基氧含量:设计
    s_oxygen_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基氧含量:校核
    s_oxygen_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基氮含量:设计
    s_nitrogen_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基氮含量:校核
    s_nitrogen_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基硫含量:设计
    s_sulfur_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基硫含量:校核
    s_sulfur_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基灰分:设计
    s_grey_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基灰分:校核
    s_grey_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基水分:设计
    s_water_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基水分:校核
    s_water_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1总和:设计
    s_sum_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1总和:校核
    s_sum_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 干燥无灰基挥发分:设计
    s_daf_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 干燥无灰基挥发分:校核
    s_daf_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 哈氏可磨系数:设计
    s_grindability_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 哈氏可磨系数:校核
    s_grindability_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基低位发热量用户提供:设计
    s_low_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1收到基低位发热量用户提供:校核
    s_low_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2收到基低位发热量计算得到:设计
    s_low_1_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2收到基低位发热量计算得到:校核
    s_low_1_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 低位发热量估算:设计
    s_low_estimation_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 低位发热量估算:校核
    s_low_estimation_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 高位发热量估算:设计
    s_high_estimation_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 高位发热量估算:校核
    s_high_estimation_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2过热蒸汽额定流量:设计
    f_steam_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2过热蒸汽额定流量:校核
    f_steam_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2过热蒸汽出口压力:设计
    f_steam_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2过热蒸汽出口压力:校核
    f_steam_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2过热蒸汽温度:设计
    f_steam_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2过热蒸汽温度:校核
    f_steam_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2过热蒸汽焓值:设计
    f_steam_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2过热蒸汽焓值:校核
    f_steam_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2锅筒压力:设计
    f_boiler_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2锅筒压力:校核
    f_boiler_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2汽包内饱和水焓值:设计
    f_saturated_water_enthalpy_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 2汽包内饱和水焓值:校核
    f_saturated_water_enthalpy_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 2给水温度:设计
    f_water_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2给水温度:校核
    f_water_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2给水焓值:设计
    f_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2给水焓值:校核
    f_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2锅炉效率:设计
    f_boiler_efficiency_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2锅炉效率:校核
    f_boiler_efficiency_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2机械未燃烧损失:设计
    f_unburned_loss_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2机械未燃烧损失:校核
    f_unburned_loss_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2锅炉排污率:设计
    f_blowdown_rate_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2锅炉排污率:校核
    f_blowdown_rate_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2锅炉燃料消耗量:设计
    f_boiler_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2锅炉燃料消耗量:校核
    f_boiler_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 2计算燃料消耗量:设计
    f_calculation_consumption_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 2计算燃料消耗量:校核
    f_calculation_consumption_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 3灰渣总量:设计
    d_total_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3灰渣总量:校核
    d_total_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3炉内喷钙灰渣总量:设计
    d_boiler_total_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3炉内喷钙灰渣总量:校核
    d_boiler_total_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3飞灰份额:设计
    d_ash_share_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3飞灰份额:校核
    d_ash_share_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3底渣份额:设计
    d_dust_share_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3底渣份额:校核
    d_dust_share_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3灰量:设计
    d_ash_total_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3灰量:校核
    d_ash_total_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3渣量:设计
    d_dust_total_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 3渣量:校核
    d_dust_total_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4理论干空气量:设计
    a_air_volumn_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4理论干空气量:校核
    a_air_volumn_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4最热月平均气温:设计
    a_hot_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4最热月平均气温:校核
    a_hot_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4多年平均相对湿度:设计
    a_humidity_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4多年平均相对湿度:校核
    a_humidity_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4多年平均气压:设计
    a_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4多年平均气压:校核
    a_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4多年平均气温:设计
    a_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4多年平均气温:校核
    a_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4多年平均气温下的饱和压力:设计
    a_saturation_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4多年平均气温下的饱和压力:校核
    a_saturation_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4水蒸气分压力:设计
    a_steam_perssure_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4水蒸气分压力:校核
    a_steam_perssure_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4空气的绝对湿度（含湿量）:设计
    a_air_humidity_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4空气的绝对湿度（含湿量）:校核
    a_air_humidity_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4标况下湿空气密度:设计
    a_standard_air_humidity_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 4标况下湿空气密度:校核
    a_standard_air_humidity_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 4理论湿空气量:设计
    a_wet_air_volumn_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 4理论湿空气量:校核
    a_wet_air_volumn_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5理论氮气容积:设计
    s_nitrogen_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5理论氮气容积:校核
    s_nitrogen_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5理论二氧化物容积:设计
    s_dioxide_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5理论二氧化物容积:校核
    s_dioxide_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5理论水蒸汽容积:设计
    s_steam_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5理论水蒸汽容积:校核
    s_steam_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5理论烟气容积:设计
    s_smoke_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5理论烟气容积:校核
    s_smoke_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 51kg燃料生成理论湿烟气的重量:设计
    s_1kg_weight_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 51kg燃料生成理论湿烟气的重量:校核
    s_1kg_weight_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5标况下理论湿烟气密度:设计
    s_wet_smoke_density_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 5标况下理论湿烟气密度:校核
    s_wet_smoke_density_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6炉膛出口过剩空气系数:设计
    p_boiler_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6炉膛出口过剩空气系数:校核
    p_boiler_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6旋风分离器漏风系数:设计
    p_wind_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6旋风分离器漏风系数:校核
    p_wind_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6旋风分离器出口过剩空气系数:设计
    p_wind_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6旋风分离器出口过剩空气系数:校核
    p_wind_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6高过漏风系数:设计
    p_high_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6高过漏风系数:校核
    p_high_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6高过出口过剩空气系数:设计
    p_hign_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6高过出口过剩空气系数:校核
    p_hign_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6低过漏风系数:设计
    p_low_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6低过漏风系数:校核
    p_low_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6低过出口过剩空气系数:设计
    p_low_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6低过出口过剩空气系数:校核
    p_low_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6省燃料器漏风系数:设计
    p_fule_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6省燃料器漏风系数:校核
    p_fule_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6省燃料器出口过剩空气系数:设计
    p_fule_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6省燃料器出口过剩空气系数:校核
    p_fule_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器漏风系数:设计
    p_heater_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器漏风系数:校核
    p_heater_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器出口过剩空气系数:设计
    p_heater_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器出口过剩空气系数:校核
    p_heater_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空予器至除尘器烟道漏风系数:设计
    p_plus_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空予器至除尘器烟道漏风系数:校核
    p_plus_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6除尘器进口过剩空气系数:设计
    p_dust_exit_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6除尘器进口过剩空气系数:校核
    p_dust_exit_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6除尘器漏风系数:设计
    p_dust_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6除尘器漏风系数:校核
    p_dust_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6除尘器出口过剩空气系数:设计
    p_dust_entry_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6除尘器出口过剩空气系数:校核
    p_dust_entry_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6除尘器出口至引风机烟道漏风系数:设计
    p_plus_dust_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6除尘器出口至引风机烟道漏风系数:校核
    p_plus_dust_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6引风机入口过剩空气系数:设计
    p_fans_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6引风机入口过剩空气系数:校核
    p_fans_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 61Kg燃料产生的空预器出口湿烟气容积:设计
    p_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 61Kg燃料产生的空预器出口湿烟气容积:校核
    p_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 61Kg燃料产生的空预器出口湿烟气质量:设计
    p_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 61Kg燃料产生的空预器出口湿烟气质量:校核
    p_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器:设计
    p_heater_type_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器:校核
    p_heater_type_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器一次风进口温度:设计
    p_heater_first_entry_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器一次风进口温度:校核
    p_heater_first_entry_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器二次风进口温度:设计
    p_heater_second_entry_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器二次风进口温度:校核
    p_heater_second_entry_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器一次风出口温度:设计
    p_heater_first_exit_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器一次风出口温度:校核
    p_heater_first_exit_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器二次风出口温度:设计
    p_heater_second_exit_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6空预器二次风出口温度:校核
    p_heater_second_exit_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6锅炉排烟温度:设计
    p_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6锅炉排烟温度:校核
    p_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7理论空气量（体积,湿）:设计
    a_theory_air_quality_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7理论空气量（体积,湿）:校核
    a_theory_air_quality_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7炉膛出口过剩空气系数:设计
    a_boiler_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7炉膛出口过剩空气系数:校核
    a_boiler_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7实际空气量（体积,湿）:设计
    a_actual_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7实际空气量（体积,湿）:校核
    a_actual_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7计算燃料消耗量:设计
    a_calculation_consumption_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7计算燃料消耗量:校核
    a_calculation_consumption_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7实际空气总量（体积，湿）:设计
    a_actual_air_total_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7实际空气总量（体积，湿）:校核
    a_actual_air_total_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7一次风份额:设计
    a_first_wind_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7一次风份额:校核
    a_first_wind_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷风温度（计算温度）:设计
    a_cwind_temperature_calculation_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7冷风温度（计算温度）:校核
    a_cwind_temperature_calculation_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7当地年平均气压:设计
    a_local_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7当地年平均气压:校核
    a_local_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷一次风量（湿-标准态）:设计
    a_first_cwind_standard_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7冷一次风量（湿-标准态）:校核
    a_first_cwind_standard_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷一次风量（湿-实态）:设计
    a_first_cwind_actual_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷一次风量（湿-实态）:校核
    a_first_cwind_actual_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7标况下湿空气密度1:设计
    a_first_standard_air_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7标况下湿空气密度1:校核
    a_first_standard_air_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7冷一次风量（质量流量）:设计
    a_first_cwind_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷一次风量（质量流量）:校核
    a_first_cwind_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷一次风湿空气密度（湿-实态）:设计
    a_first_cwind_density_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷一次风湿空气密度（湿-实态）:校核
    a_first_cwind_density_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7校核:设计
    a_check_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7校核:校核
    a_check_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7热一次风温度:设计
    a_first_hwind_temperatue_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7热一次风温度:校核
    a_first_hwind_temperatue_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7热一次风量（湿-实态）:设计
    a_first_hwind_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7热一次风量（湿-实态）:校核
    a_first_hwind_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7湿空气密度（湿-实态）1:设计
    a_first_wet_air_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7湿空气密度（湿-实态）1:校核
    a_first_wet_air_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7二次风份额:设计
    a_second_wind_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7二次风份额:校核
    a_second_wind_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷风温度:设计
    a_cwind_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷风温度:校核
    a_cwind_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷二次风量（湿-标准态）:设计
    a_second_cwind_standard_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7冷二次风量（湿-标准态）:校核
    a_second_cwind_standard_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7冷二次风量（湿-实态）:设计
    a_second_cwind_actual_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷二次风量（湿-实态）:校核
    a_second_cwind_actual_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7标况下湿空气密度2:设计
    a_second_standard_air_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7标况下湿空气密度2:校核
    a_second_standard_air_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7冷二次风量（质量流量）:设计
    a_second_cwind_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷二次风量（质量流量）:校核
    a_second_cwind_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7冷二次风湿空气密度（湿-实态）:设计
    a_second_cwind_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7冷二次风湿空气密度（湿-实态）:校核
    a_second_cwind_density_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7热二次风温度:设计
    a_second_hwind_temperatue_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7热二次风温度:校核
    a_second_hwind_temperatue_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7热二次风量（湿-实态）:设计
    a_second_hwind_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7热二次风量（湿-实态）:校核
    a_second_hwind_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 7湿空气密度（湿-实态）2:设计
    a_second_wet_air_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 7湿空气密度（湿-实态）2:校核
    a_second_wet_air_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 8标况下空预器出口1Kg燃料湿烟气容积:设计
    h_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8标况下空预器出口1Kg燃料湿烟气容积:校核
    h_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8空预器出口1Kg燃料产生的湿烟气质量:设计
    h_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8空预器出口1Kg燃料产生的湿烟气质量:校核
    h_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8计算燃料消耗量:设计
    h_calculation_consumption_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 8计算燃料消耗量:校核
    h_calculation_consumption_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 8标况下空预器出口烟气容积流量:设计
    h_standard_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8标况下空预器出口烟气容积流量:校核
    h_standard_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8空预器出口烟气质量流量:设计
    h_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8空预器出口烟气质量流量:校核
    h_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8锅炉空预器出口排烟温度:设计
    h_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8锅炉空预器出口排烟温度:校核
    h_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8空预器出口烟气容积量(实态）:设计
    h_smoke_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8空预器出口烟气容积量(实态）:校核
    h_smoke_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8烟气密度（实态）:设计
    h_smoke_density_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 8烟气密度（实态）:校核
    h_smoke_density_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9空预器出口过剩空气系数:设计
    d_exit_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9空预器出口过剩空气系数:校核
    d_exit_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9空预器至除尘器烟道漏风系数:设计
    d_wind_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9空预器至除尘器烟道漏风系数:校核
    d_wind_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口过剩空气系数:设计
    d_entry_air_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口过剩空气系数:校核
    d_entry_air_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9冷空气温度:设计
    d_cold_air_temperature_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 9冷空气温度:校核
    d_cold_air_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口处烟气温度:设计
    d_entry_somke_temperature_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口处烟气温度:校核
    d_entry_somke_temperature_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 9标况下除尘器进口处1kg燃料湿烟气容积:设计
    d_standard_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9标况下除尘器进口处1kg燃料湿烟气容积:校核
    d_standard_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口处1kg燃料湿烟气质量:设计
    d_entry_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口处1kg燃料湿烟气质量:校核
    d_entry_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9标况下除尘器进口烟气容积流量:设计
    d_standard_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9标况下除尘器进口烟气容积流量:校核
    d_standard_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口处烟气质量流量:设计
    d_entry_somke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口处烟气质量流量:校核
    d_entry_somke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口处烟气容积流量(实态）:设计
    d_entry_smoke_actual_flow_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 9除尘器进口处烟气容积流量(实态）:校核
    d_entry_smoke_actual_flow_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 10除尘器漏风系数:设计
    e_wind_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器漏风系数:校核
    e_wind_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口过剩空气系数:设计
    e_air_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口过剩空气系数:校核
    e_air_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口烟气温度:设计
    e_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口烟气温度:校核
    e_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10标况下除尘器出口处1kg燃料湿烟气容积:设计
    e_standard_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10标况下除尘器出口处1kg燃料湿烟气容积:校核
    e_standard_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口处1kg燃料湿烟气质量:设计
    e_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口处1kg燃料湿烟气质量:校核
    e_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10标况下除尘器出口湿烟气容积流量:设计
    e_standard_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10标况下除尘器出口湿烟气容积流量:校核
    e_standard_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口处湿烟气质量流量:设计
    e_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口处湿烟气质量流量:校核
    e_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口处湿烟气容积流量(实态）:设计
    e_smoke_actual_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10除尘器出口处湿烟气容积流量(实态）:校核
    e_smoke_actual_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 10烟气密度（实态）:设计
    e_smoke_actual_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 10烟气密度（实态）:校核
    e_smoke_actual_density_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11除尘器出口至引风机烟道漏风系数:设计
    i_wind_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11除尘器出口至引风机烟道漏风系数:校核
    i_wind_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机入口过剩空气系数:设计
    i_air_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机入口过剩空气系数:校核
    i_air_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机入口烟气温度:设计
    i_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机入口烟气温度:校核
    i_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11标况下引风机进口处1kg燃料湿烟气容积:设计
    i_standard_1kg_volume_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11标况下引风机进口处1kg燃料湿烟气容积:校核
    i_standard_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机进口处1kg燃料湿烟气质量:设计
    i_1kg_quality_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机进口处1kg燃料湿烟气质量:校核
    i_1kg_quality_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11标况下引风机进口湿烟气容积流量1:设计
    i_standard_smoke_flow1_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 11标况下引风机进口湿烟气容积流量1:校核
    i_standard_smoke_flow1_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11标况下引风机进口湿烟气容积流量2:设计
    i_standard_smoke_flow2_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 11标况下引风机进口湿烟气容积流量2:校核
    i_standard_smoke_flow2_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机进口处湿烟气质量流量:设计
    i_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机进口处湿烟气质量流量:校核
    i_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机进口处湿烟气容积流量(实态）1:设计
    i_smoke_actual_flow1_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机进口处湿烟气容积流量(实态）1:校核
    i_smoke_actual_flow1_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机进口处湿烟气容积流量(实态）2:设计
    i_smoke_actual_flow2_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机进口处湿烟气容积流量(实态）2:校核
    i_smoke_actual_flow2_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11烟气密度（实态）:设计
    i_smoke_actual_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 11烟气密度（实态）:校核
    i_smoke_actual_density_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 11引风机处计算湿烟气密度（标况）:设计
    i_wet_smoke_actual_density_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 11引风机处计算湿烟气密度（标况）:校核
    i_wet_smoke_actual_density_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 12烟气中的氧量:设计
    go_oxygen_vol_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12烟气中的氧量:校核
    go_oxygen_vol_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12理论干烟气容积:设计
    go_theoretica_vol_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12理论干烟气容积:校核
    go_theoretica_vol_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12理论干空气量:设计
    go_theoretica_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12理论干空气量:校核
    go_theoretica_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12计算燃料消耗量:设计
    go_calculation_consumption_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 12计算燃料消耗量:校核
    go_calculation_consumption_check = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 12引风机入口过剩空气系数:设计
    go_air_parameter_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12引风机入口过剩空气系数:校核
    go_air_parameter_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 121Kg燃料产生的引风机进口干烟气容积:设计
    go_standard_1kg_volume_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 121Kg燃料产生的引风机进口干烟气容积:校核
    go_standard_1kg_volume_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12引风机进口干烟气容积流量:设计
    go_smoke_flow_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12引风机进口干烟气容积流量:校核
    go_smoke_flow_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12干烟气中含氧量:设计
    go_drygas_oxygen_vol_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12干烟气中含氧量:校核
    go_drygas_oxygen_vol_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 12总燃烧产物6%O2干体积:设计
    go_total_combustion_product_vol_design = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 12总燃烧产物6%O2干体积:校核
    go_total_combustion_product_vol_check = db.Column(
        db.NUMERIC(precision=15, scale=5))

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


# 脱硫脱硝
class CoalCHPDesulfurization(db.Model):
    # 表名
    __tablename__ = 'coalchp_desulfurization_denitrification'
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 收到基硫份设计值
    s_sulfur_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算耗煤量设计值
    s_calcu_coal_consume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 燃煤中的含硫量燃烧后氧化成SO2的份额设计值
    s_aflame_generate_so2 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 脱硫前烟气中的SO2含量设计值
    s_desulfrization_before_so2 = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 引风机进口烟气容积流量（标况）设计值
    s_fan_smoke_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 未脱硫前SO2浓度（标态）设计值
    s_no_desulfurization_so2 = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 脱硫效率设计值
    s_desulfurization_efficiency = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 脱硫后SO2浓度（标态）设计值
    s_desulfrization_after_so2 = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 脱硫后SO2排放量（标态）设计值
    s_desulfrization_after_discharge_so2 = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 炉内脱硫百分比设计值
    r_furnace_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 炉内脱硫后SO2浓度设计值
    r_furnace_concentration = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 脱除SO2质量设计值
    r_others_mass = db.Column(db.NUMERIC(precision=15, scale=5))
    # 脱除SO2摩尔量设计值
    r_others_mole = db.Column(db.NUMERIC(precision=15, scale=5))
    # 钙硫摩尔比设计值
    r_calcium_sulfur_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 反应所需CaCO3摩尔量设计值
    r_nees_caco3_mole = db.Column(db.NUMERIC(precision=15, scale=5))
    # 反应所需CaCO3质量设计值
    r_nees_caco3_mass = db.Column(db.NUMERIC(precision=15, scale=5))
    # 参加反应CaCO3质量设计值
    r_use_caco3_mass = db.Column(db.NUMERIC(precision=15, scale=5))
    # 反应生成CaSO4质量设计值
    r_generate_coco3_mass = db.Column(db.NUMERIC(precision=15, scale=5))
    # 反应后质量增加设计值
    r_add_mass = db.Column(db.NUMERIC(precision=15, scale=5))
    # 石灰石纯度设计值
    r_caco3_pure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 石灰石耗量设计值
    r_coco3_consume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 炉内脱硫产生的灰渣量设计值
    r_generate_grey = db.Column(db.NUMERIC(precision=15, scale=5))
    # 石灰石粉仓储存时间设计值
    r_storage_time = db.Column(db.NUMERIC(precision=15, scale=5))
    # 石灰石粉仓出力设计值
    r_storage_output = db.Column(db.NUMERIC(precision=15, scale=5))
    # 石灰石粉堆积密度设计值
    r_storage_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 石灰石粉库充满系数设计值
    r_storage_fullness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 石灰石粉仓体积设计值
    r_storage_volume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 高设计值
    r_height = db.Column(db.NUMERIC(precision=15, scale=5))
    # 直径设计值
    r_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 石灰石纯度设计值
    d_limestone_pure = db.Column(db.NUMERIC(precision=15, scale=5))
    # Ca/S（钙硫比）设计值
    d_proportion_ca_s = db.Column(db.NUMERIC(precision=15, scale=5))
    # 脱硫效率设计值
    d_desulfurization_efficiency = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 石灰石消耗量设计值
    d_limestone_consume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 生成CaSO4量设计值
    d_gengrate_coca4 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 脱硝前NOX浓度设计值
    n_before_nox_concentration = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 引风机进口烟气容积流量（标况）设计值
    n_input_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 脱硝效率(总效率)设计值
    n_desulfurization_efficiency = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 脱硝前NOX排放量设计值
    n_before_nox_discharge = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 脱硝后NOX浓度设计值
    n_after_nox_concentration = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 环保要求NOX的排放浓度设计值
    n_env_after_nox_concentration = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 脱硝后NOX排放量设计值
    n_after_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5))
    # 炉内脱硝百分比设计值
    d_denitration_percentage = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 炉内脱硝量设计值
    d_denitration_quality = db.Column(db.NUMERIC(precision=15, scale=5))
    # 炉内脱硝后NOX排放量设计值
    d_after_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5))
    # 炉内脱硝摩尔量设计值
    d_denitration_molar = db.Column(db.NUMERIC(precision=15, scale=5))
    # 氨逃逸率设计值
    d_escape_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 氨逃逸量设计值
    d_escape_quality = db.Column(db.NUMERIC(precision=15, scale=5))
    # 逃逸氨折算尿素量设计值
    d_escape_quality_urea = db.Column(db.NUMERIC(precision=15, scale=5))
    # NH3/NOX摩尔比设计值
    d_nh3nox_molar = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素/NOX摩尔比设计值
    d_urea_nox_molar = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素/NOX式量比设计值
    d_urea_nox_quality = db.Column(db.NUMERIC(precision=15, scale=5))
    # 理论尿素消耗量设计值
    d_theory_urea = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素用量(一台炉)设计值
    d_use_urea = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素溶液消耗水量(一台炉)设计值
    d_water_urea = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素仓库天数设计值
    d_days_urea = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素仓库容量设计值
    d_capacity_urea = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟气脱硝百分比设计值
    g_denitration_percentage = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 烟气脱硝后NOX排放量设计值
    g_after_nox_discharge = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟气脱硝量设计值
    g_denitration_quality = db.Column(db.NUMERIC(precision=15, scale=5))
    # 氨逃逸率设计值
    g_escape_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 氨逃逸量设计值
    g_escape_quality = db.Column(db.NUMERIC(precision=15, scale=5))
    # 逃逸氨折算尿素量设计值
    g_escape_quality_urea = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # NH3/NOX摩尔比设计值
    g_nh3nox_molar = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素/NOX摩尔比设计值
    g_urea_nox_molar = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素/NOX式量比设计值
    g_urea_nox_quality = db.Column(db.NUMERIC(precision=15, scale=5))
    # 理论尿素消耗量设计值
    g_theory_urea = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尿素用量(一台炉)设计值
    g_use_urea = db.Column(db.NUMERIC(precision=15, scale=5))

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


# 锅炉辅机系统表
class CoalCHPBoilerAuxiliaries(db.Model):
    # 表名
    __tablename__ = 'coalchp_boiler_auxiliaries'
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 定期排污扩容器 
    # 锅炉蒸发量
    r_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排放时间
    r_emission_time = db.Column(db.NUMERIC(precision=15, scale=5))
    # 定期排污率
    r_emission_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 定期排污水量
    r_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽包压力
    r_drum_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽包压力下的饱和水焓
    r_drum_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 排污扩容器工作压力
    r_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 扩容器压力下饱和水焓
    r_work_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 扩容器压力下汽化潜热
    r_work_latentheat_vaporization = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 扩容器单位容积润许极限强度
    r_ultimate_strength = db.Column(db.NUMERIC(precision=15, scale=5))
    # 富裕系数
    r_affluence_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排污扩容容积
    r_volume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 扩容器规格选取
    r_specifications = db.Column(db.NUMERIC(precision=15, scale=5))

    # 连续排污扩容器
    # 锅炉蒸发量
    c_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5))
    # 连续排污率
    c_emission_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 连续排污水量
    c_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽包压力
    c_drum_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽包压力下的饱和水焓
    c_drum_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 排污扩容器工作压力
    c_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 扩容器压力下饱和水焓
    c_work_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 扩容器压力下蒸汽比容
    c_work_steam_pecificvolume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 扩容器压力下汽化潜热
    c_work_latentheat_vaporization = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 扩容器蒸汽干度
    c_steam_dryness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 扩容器单位容积润许极限强度
    c_ultimate_strength = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排污水汽化量
    c_vaporization_capacity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 富裕系数
    c_affluence_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排污扩容汽容积
    c_volume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 扩容器规格选取
    c_specifications = db.Column(db.NUMERIC(precision=15, scale=5))

    # 磷酸盐加药装置
    # 锅炉水系统容积
    d_boiler_watersystem_volume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 应维持的磷酸根含量
    d_phosphate_content = db.Column(db.NUMERIC(precision=15, scale=5))
    # 给水硬度（原水）
    d_water_hardness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 纯度
    d_purity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉启动时加药量
    d_boiler_dosage_startup = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉给水量
    d_boiler_water_supply = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉排污量
    d_boiler_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 运行时加药量
    d_boiler_dosage_run = db.Column(db.NUMERIC(precision=15, scale=5))
    # 磷酸钠浓度
    d_na3po4_concentration = db.Column(db.NUMERIC(precision=15, scale=5))
    # 在C浓度下的磷酸三钠密度
    d_na3po4_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 运行时汽包内加入的溶液量
    d_solution_quantity_run = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水泵
    # 锅炉设计使用压力
    p_boiler_design_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 省煤器入口进水压力
    p_inlet_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除氧器工作压力
    p_deaerator_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 给水管阻力（以压头计）
    p_water_supply_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 进水管阻力（以压头计）
    p_water_inlet_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 水泵中心至汽包正常水位的几何高度差
    p_center_altitude_difference = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除氧器最低水位至水泵中心几何高度差（给水泵进口静水头）
    p_deaerator_altitude_difference = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 给水泵总扬程
    p_feedpump_total_head = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流量
    p_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 泵效率
    p_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 机械传动效率
    p_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    p_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机备用系数
    p_motor_reserve_factor = db.Column(db.NUMERIC(precision=15, scale=5))
    # 配套电机功率
    p_auxiliary_motor_power = db.Column(db.String(20))
    # 给水泵选用规格
    p_specifications = db.Column(db.NUMERIC(precision=15, scale=5))

    # 锅炉补给水处理能力
    # 锅炉蒸发量
    m_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5))
    # 补汽量
    m_makeup_steam = db.Column(db.NUMERIC(precision=15, scale=5))
    # 厂内汽水循环损失
    m_steamwater_cycle_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排污损失
    m_pollution_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 凝结水量
    m_condensing_capacity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 换热凝结水损失
    m_condensate_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉正常补水量
    m_boiler_normal_watersupply = db.Column(db.NUMERIC(precision=15, scale=5))
    # 启动或事故增加损失
    m_increase_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉最大补水量
    m_boiler_max_watersupply = db.Column(db.NUMERIC(precision=15, scale=5))

    # 除氧水箱/凝结水箱 共用
    # 锅炉蒸发
    s_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5))
    # 储水时间
    s_storage_time = db.Column(db.NUMERIC(precision=15, scale=5))
    # 容积
    s_volume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尺寸 长
    s_size_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 尺寸 直径
    s_size_diameter = db.Column(db.NUMERIC(precision=15, scale=5))

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


# 烟风系统烟风系统
class CoalCHPSmokeAirSystem(db.Model):
    # 表名
    __tablename__ = 'coalchp_smoke_air_system'
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 海拔
    a_altitude = db.Column(db.NUMERIC(precision=15, scale=5))
    # 大气压
    a_atmospheric_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # 标况温度
    p_the_case_temperature_f = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况压力
    p_standard_of_pressure_f = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况流量
    p_standard_of_flow_f = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况温度
    p_temperature_case_f = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    p_local_atmosphere_f = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况流量
    p_operational_point_flow_f = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况温度
    p_the_case_temperature_s = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况压力
    p_standard_of_pressure_s = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况流量
    p_standard_of_flow_s = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况温度
    p_temperature_case_s = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    p_local_atmosphere_s = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况流量
    p_operational_point_flow_s = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况温度
    p_the_case_temperature_t = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况压力
    p_standard_of_pressure_t = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况流量
    p_standard_of_flow_t = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况温度
    p_temperature_case_t = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    p_local_atmosphere_t = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况流量
    p_operational_point_flow_t = db.Column(db.NUMERIC(precision=15, scale=5))

    # 名称
    f_name = db.Column(db.NUMERIC(precision=15, scale=5))
    # 空气温度
    f_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉本体阻力
    f_boiler_body_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风道阻力
    f_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    f_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟风流量（工况）
    f_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5))
    # 铭牌介质温度
    f_nameplate_medium_temperature = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 风机全压
    f_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用全压
    f_fan_select_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用流量
    f_fan_selection_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机效率
    f_fan_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    f_electric_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机轴功率
    f_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机安全裕量
    f_fan_security_volumn = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机功率
    f_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))

    # 名称
    s_name = db.Column(db.NUMERIC(precision=15, scale=5))
    # 空气温度
    s_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉本体阻力
    s_boiler_body_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风道阻力
    s_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    s_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟风流量（工况）
    s_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5))
    # 铭牌介质温度
    s_nameplate_medium_temperature = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 风机全压
    s_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用全压
    s_fan_select_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用流量
    s_fan_selection_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机效率
    s_fan_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    s_electric_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机轴功率
    s_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机安全裕量
    s_fan_security_volumn = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机功率
    s_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))

    # 名称
    i_name = db.Column(db.NUMERIC(precision=15, scale=5))
    # 空气温度
    i_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉本体阻力
    i_boiler_body_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 脱硝
    i_denitration = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除尘器
    i_duster = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风道阻力
    i_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机后脱硫塔及烟囱烟道阻力
    i_resistance_desulfurization_fan = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    i_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟风流量（工况）
    i_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风道阻力
    i_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    i_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟风流量（工况）
    i_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5))
    # 铭牌介质温度
    i_nameplate_medium_temperature = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 风机全压
    i_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用全压
    i_fan_select_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用流量
    i_fan_selection_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机效率
    i_fan_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    i_electric_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机轴功率
    i_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机安全裕量
    i_fan_security_volumn = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机功率
    i_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))

    # 名称
    r_name = db.Column(db.NUMERIC(precision=15, scale=5))
    # 空气温度
    r_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉本体阻力
    r_boiler_body_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风道阻力
    r_duct_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    r_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟风流量（工况）
    r_smoke_flow_rate_condition = db.Column(db.NUMERIC(precision=15, scale=5))
    # 铭牌介质温度
    r_nameplate_medium_temperature = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 风机全压
    r_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用全压
    r_fan_select_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用流量
    r_fan_selection_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机效率
    r_fan_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    r_electric_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机轴功率
    r_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机安全裕量
    r_fan_security_volumn = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机功率
    r_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))

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


# 除灰除渣系统
class CoalCHPRemovalAshSlag(db.Model):
    # 表名
    __tablename__ = 'coalchp_removal_ash_slag_system'
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 灰渣总量(炉内脱硫后)
    a_total_ash_residue_after = db.Column(db.NUMERIC(precision=15, scale=5))
    # 飞灰份额
    a_fly_ash_content = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除尘器入口（锅炉出口）飞灰量
    a_dust_collector_inlet_ = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况下除尘器进口烟气容积流量
    a_the_imported_smoke_volume = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除尘器进口处烟气容积流量(实态）
    a_the_smoke_volume_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况下除尘器进口烟气浓度
    a_the_smoke_concentration = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除尘器进口处烟气浓度(实态）
    a_the_smoke_concentration_solid = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 除尘效率
    a_collection_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除尘器（烟囱）出口烟气浓度（标况）
    a_the_smoke_concentration_chimney = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 除尘器（烟囱）出口烟气飞灰量（标况）
    a_dust_collector_stack = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除尘器下灰量
    a_ash_under_dust_collector = db.Column(db.NUMERIC(precision=15, scale=5))
    # 引风机进口烟气容积量(实态）
    a_the_imported_smoke_real_state = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 烟囱出口烟气浓度（实态）
    a_flue_gas_concentratio = db.Column(db.NUMERIC(precision=15, scale=5))

    # 出力系数
    r_removal_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除灰系统出力
    r_removal_the_ash_system = db.Column(db.NUMERIC(precision=15, scale=5))
    # 干灰堆积密度
    r_dry_ash_accumulation_density = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 渣库充满系数
    r_slag_accumulation_coefficient = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 存灰时间
    r_stored_ash = db.Column(db.NUMERIC(precision=15, scale=5))
    # 灰库有效体积
    r_effective_volume_ash_storage = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 直径
    r_dia = db.Column(db.NUMERIC(precision=15, scale=5))
    # 高度
    r_height = db.Column(db.NUMERIC(precision=15, scale=5))

    # 灰气比
    g_grey_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    # 输灰系统耗气量
    g_air_transport_ash_system = db.Column(db.NUMERIC(precision=15, scale=5))

    # 渣量
    s_slag_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冷渣机的出力（单台）
    s_output_cold_single_stage = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冷渣机台数
    s_cold_single_stage_count = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除渣系统出力
    s_slag_removal_system = db.Column(db.NUMERIC(precision=15, scale=5))
    # 耐高温带式输送机出力
    s_high_temperature_belt_conveyor = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 冷渣堆积密度
    s_cold_slag_accumulation_density = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 渣库充满系数
    s_slag_accumulation_coefficient = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 存渣时间
    s_sludge_time = db.Column(db.NUMERIC(precision=15, scale=5))
    # 渣库有效体积
    s_slag_storage_volume_effective = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 直径
    s_dia = db.Column(db.NUMERIC(precision=15, scale=5))
    # 高度
    s_height = db.Column(db.NUMERIC(precision=15, scale=5))

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
    def delete_smoke_air_system(plan_id):
        smoke_air_system = \
            CoalCHPRemovalAshSlag.search_removal_ash_slag(plan_id)
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


# 循环水系统
class CoalCHPCirculatingWater(db.Model):
    # 表名
    __tablename__ = 'coalchp_circulating_water'
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 乏汽流量(冬季)
    v_steam_exhaust_flow_winter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 乏汽流量(夏季)
    v_steam_exhaust_flow_summer = db.Column(db.NUMERIC(precision=15, scale=5))
    # 乏汽流量(选择)
    v_steam_exhaust_flow_select = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环倍率(冬季)
    v_circulating_ratio_winter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环倍率(夏季)
    v_circulating_ratio_summer = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水量(冬季)
    v_circulating_water_winter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水量(夏季)
    v_circulating_water_summer = db.Column(db.NUMERIC(precision=15, scale=5))
    # 辅机冷却水量(冬季)
    v_auxiliary_engine_cooling_winter = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 辅机冷却水量(夏季)
    v_auxiliary_engine_cooling_summer = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 总循环水量(冬季)
    v_total_circulating_water_winter = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 总循环水量(夏季)
    v_total_circulating_water_summer = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 总循环水量(选择)
    v_total_circulating_water_select = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 进、出水口温差
    v_enter_the_outlet_temperature_difference = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 干球温度
    v_dry_bulb_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # K
    v_k = db.Column(db.NUMERIC(precision=15, scale=5))
    # 蒸发损失率
    v_evaporation_loss_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 蒸发损失
    v_evaporation_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风吹损失率
    v_blowing_loss_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 分吹损失
    v_partial_blow_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 浓缩倍率
    v_concentrate_ratio = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排污损失率
    v_discharge_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排污量
    v_discharge_capacity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 补充水量（冬季）
    v_amount_of_makeup_water_winter = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 补充水量(夏季)
    v_amount_of_makeup_water_summer = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 循环水池尺寸
    v_circulating_pool_size = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水池尺寸(长)
    v_circulating_pool_long = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水池尺寸（宽）
    v_circulating_pool_wide = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水池尺寸（高）
    v_circulating_pool_hight = db.Column(db.NUMERIC(precision=15, scale=5))
    # 校核循环水池尺寸
    v_check_circulating_pool_size = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 凝汽器循环水进水工作压力
    c_pressure_condenser = db.Column(db.NUMERIC(precision=15, scale=5))
    # 凝汽器阻力
    c_condenser_tube_friction = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水回水压力
    c_circulating_water_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水吸水池压力
    c_circulating_pool_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水泵出口与凝汽器循环水进水口高度差
    c_circulation_height_difference = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 吸水池与水泵入口高度差
    c_height_difference_inlet = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道损失
    c_pipe_losses = db.Column(db.NUMERIC(precision=15, scale=5))
    # Y型过滤器损失
    c_y_losses = db.Column(db.NUMERIC(precision=15, scale=5))
    # 总扬程
    c_pumping_head = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流量
    c_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 泵效率
    c_pump_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 机械传动效率
    c_mechine_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    c_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机备用系数
    c_motor_backup_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 配套电机功率
    c_supporting_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用型号功率
    c_forklift_parameters_power = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 选用型号流量
    c_forklift_parameters_flow = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 选用型号扬程
    c_forklift_parameters_lift = db.Column(
        db.NUMERIC(precision=15, scale=5))

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
        smoke_air_system = \
            CoalCHPCirculatingWater.search_circulating_water(plan_id)
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
