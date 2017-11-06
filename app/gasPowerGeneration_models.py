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

# 煤气发电 循环水系统 circulating_water_system
class GPGCirculatingWaterSystem(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_circulating_water_system'

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 冬季乏汽流量
    steam_exhaust_flux_winter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 夏季乏汽流量
    steam_exhaust_flux_summer = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选定乏汽流量
    steam_exhaust_flux_selected = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冬季循环倍率
    circulation_ratio_winter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 夏季循环倍率
    circulation_ratio_summer = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冬季循环水量
    circulation_water_flow_winter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 夏季循环水量
    circulation_water_flow_summer = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冬季辅机冷却水量
    auxiliary_cooling_water_flow_winter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 夏季辅机冷却水量
    auxiliary_cooling_water_flow_summer = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冬季总循环水量
    total_circulation_water_flow_winter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 夏季总循环水量
    total_circulation_water_flow_summer = db.Column(db.NUMERIC(precision=15, scale=5))

    # 总循环水量-选定
    selected_total_circulation_water_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 喷淋密度
    spray_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 喷淋面积
    spray_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 进、出水口温差
    in_out_water_temperature_difference = db.Column(db.NUMERIC(precision=15, scale=5))
    # 干球温度
    dry_bulb_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # K
    dry_bulb_k_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 蒸发损失率
    evaporation_loss_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 蒸发损失
    evaporation_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风吹损失率
    wind_blow_loss_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风吹损失
    wind_blow_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 浓缩倍率
    concentration_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排污损失率
    discharge_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 排污量
    discharge_capacity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 补充水量
    supply_water_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水池15-25分钟循环水量
    circulating_pool_water_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水池尺寸-深
    circulating_pool_size_deep = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水池尺寸-长
    circulating_pool_size_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水池尺寸-宽
    circulating_pool_size_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 校核循环水池尺寸
    circulating_pool_size_checked = db.Column(db.NUMERIC(precision=15, scale=5))

    # 凝汽器循环水进水工作压力
    condenser_circulating_water_inlet_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 凝汽器阻力
    condenser_friction = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水回水压力
    circulating_backwater_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水吸水池压力
    circulating_water_reservoir_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 循环水泵出口与凝汽器循环水进水口高度差
    circulation_pump_outlet_to_condenser_inlet_height_difference = db.Column(db.NUMERIC(precision=15, scale=5))
    # 吸水池与水泵入口高度差
    reservoir_to_pump_inlet_height_difference = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道损失
    pipe_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # Y型过滤器损失
    y_filter_loss = db.Column(db.NUMERIC(precision=15, scale=5))
    # 总扬程
    total_pumping_lift = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流量
    pump_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 泵效率
    pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 机械传动效率
    pump_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    pump_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机备用系数
    pump_motor_spare_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 配套电机功率
    pump_matching_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用型号-功率
    selected_pump_model_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用型号-流量
    selected_pump_model_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用型号-扬程
    selected_pump_model_lift = db.Column(db.NUMERIC(precision=15, scale=5))




# 煤气发电 风阻力
class GPGWindResistance(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_wind_resistance'

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 推荐流速(送风机进出口冷风道)
    recommend_velocity_coldwind = db.Column(db.NUMERIC(precision=15, scale=5))
    # 推荐流速(热风道)
    recommend_velocity_hotwind = db.Column(db.NUMERIC(precision=15, scale=5))

    '''冷风道(吸风口至空预器）'''
    # 计算温度
    intake_to_preheater_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风量
    intake_to_preheater_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 密度
    intake_to_preheater_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    intake_to_preheater_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 动压头
    intake_to_preheater_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5))

    '''风机进口'''
    # 风管截面积
    fan_inlet_duct_section_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长
    fan_inlet_duct_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽
    fan_inlet_duct_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管周长
    fan_inlet_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道当量直径
    fan_inlet_duct_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 气体运动粘度
    fan_inlet_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 雷诺数
    fan_inlet_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁绝对粗糙度
    fan_inlet_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁相对粗糙度
    fan_inlet_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 560/△1
    fan_inlet_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 判别式
    fan_inlet_discriminant = db.Column(db.NUMERIC(precision=15, scale=5))

    # 摩擦阻力
    fan_inlet_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 摩擦阻力系数
    fan_inlet_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 单位长度摩擦阻力
    fan_inlet_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管长度
    fan_inlet_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力
    fan_inlet_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力系数
    fan_inlet_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1个吸风口局部阻力系数
    fan_inlet_single_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1个风机进口风箱
    fan_inlet_single_bellows = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1个进口挡板门
    fan_inlet_single_damper = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机进口段总阻力
    fan_inlet_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    '''风机出口至空预器'''
    # 摩擦阻力
    fan_outlet_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 单位长度摩擦阻力
    fan_outlet_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管长度
    fan_outlet_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力
    fan_outlet_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力系数
    fan_outlet_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1只出口渐扩管
    fan_outlet_single_increase_pipe = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1只90度等截面急转弯头/（二次风2只）
    fan_outlet_90_section_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 空预器接头扩散管
    fan_outlet_preheater_diffuser_pipe = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机出口至空预器总阻力
    fan_outlet_to_preheater_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    '''热风道（空预器出口至锅炉风室）'''
    # 计算温度
    preheater_to_boiler_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风量
    preheater_to_boiler_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 密度
    preheater_to_boiler_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    preheater_to_boiler_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 动压头
    preheater_to_boiler_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管截面积（热风管分两路进入风室）
    preheater_outlet_duct_section_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 圆管直径(一、二次热风为圆管）
    preheater_outlet_duct_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长
    preheater_outlet_duct_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽
    preheater_outlet_duct_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管周长
    preheater_outlet_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道当量直径
    preheater_outlet_duct_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 气体运动粘度
    preheater_outlet_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 雷诺数
    preheater_outlet_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁绝对粗糙度
    preheater_outlet_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁相对粗糙度
    preheater_outlet_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 560/△1
    preheater_outlet_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 判别式
    preheater_outlet_discriminant = db.Column(db.NUMERIC(precision=15, scale=5))

    # 摩擦阻力
    preheater_outlet_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 摩擦阻力系数
    preheater_outlet_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 单位长度摩擦阻力
    preheater_outlet_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管长度
    preheater_outlet_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力
    preheater_outlet_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力系数
    preheater_outlet_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))

    # 1个空预器出口收缩管
    preheater_outlet_shrink_pipe = db.Column(db.NUMERIC(precision=15, scale=5))
    # 6只90度等截面急转弯头
    preheater_outlet_90_sharp_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 弯头数量
    preheater_outlet_90_sharp_turn_elbow_count = db.Column(db.NUMERIC(precision=15, scale=5))
    # 弯头局部阻力系统(焊接圆管）
    preheater_outlet_90_sharp_turn_elbow_resistance = db.Column(db.NUMERIC(precision=15, scale=5))

    # 1个热一次风进风室风门
    preheater_outlet_air_intake_gate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1个热一次风进燃烧室风门
    preheater_outlet_combustor_gate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 空预器出口至锅炉风室总阻力
    preheater_outlet_to_boiler_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风道总阻力
    windhole_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

# 煤气发电 烟阻力
class GPGSmokeResistance(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_smoke_resistance'

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 推荐流速
    recommend_velocity = db.Column(db.NUMERIC(precision=15, scale=5))

    '''空预器出口至除尘器入口'''
    # 计算温度(空预器出口)
    air_preheater_outlet_calculated_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟量(空预器出口)
    air_preheater_outlet_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 密度
    air_preheater_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    air_preheater_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 动压头
    air_preheater_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟管截面积
    air_preheater_smoke_tube_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长
    air_preheater_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽
    air_preheater_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管周长
    air_preheater_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道当量直径
    air_preheater_tube_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 气体运动粘度
    air_preheater_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 雷诺数
    air_preheater_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁绝对粗糙度
    air_preheater_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁相对粗糙度
    air_preheater_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 560/△1
    air_preheater_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 判别式
    air_preheater_discriminant = db.Column(db.Text())

    # 摩擦阻力
    air_preheater_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 摩擦阻力系数
    air_preheater_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 单位长度摩擦阻力
    air_preheater_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管长度
    air_preheater_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力
    air_preheater_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力系数
    air_preheater_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))

    '''90度空预器出口变径急转弯头'''
    # 1个90度空预器出口变径急转弯头
    air_preheater_90_outlet_sharp_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉气体局部阻力系数
    air_preheater_sharp_turn_elbow_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 纯空气弯头局部阻力系数
    air_preheater_sharp_turn_elbow_air_elbow_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉浓度修正系数
    air_preheater_sharp_turn_elbow_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))

    '''90度等截面缓转弯头'''
    # 1个90度等截面缓转弯头
    air_preheater_90_section_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉气体局部阻力系数
    air_preheater_slow_turn_elbow_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 纯空气弯头局部阻力系数
    air_preheater_slow_turn_elbow_air_elbow_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉浓度修正系数
    air_preheater_slow_turn_elbow_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1个渐缩管
    air_preheater_reducer_tube = db.Column(db.NUMERIC(precision=15, scale=5))
    # 空预器出口至除尘器入口总阻力
    air_preheater_to_deduster_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5))

    '''除尘器出口至引风机入口'''
    # 计算温度(除尘器出口)
    deduster_outlet_calculated_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟量(除尘器出口)
    deduster_outlet_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 密度
    deduster_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    deduster_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 动压头
    deduster_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟管截面积
    deduster_smoke_tube_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长
    deduster_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽
    deduster_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管周长
    deduster_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道当量直径
    deduster_tube_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 气体运动粘度
    deduster_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 雷诺数
    deduster_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁绝对粗糙度
    deduster_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁相对粗糙度
    deduster_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 560/△1
    deduster_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 判别式
    deduster_discriminant = db.Column(db.Text())

    # 摩擦阻力
    deduster_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 摩擦阻力系数
    deduster_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 单位长度摩擦阻力
    deduster_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管长度
    deduster_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力
    deduster_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力系数
    deduster_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))

    '''90度除尘器出口缓转弯头'''
    # 1个90度除尘器出口缓转弯头
    deduster_90_outlet_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉气体局部阻力系数
    deduster_slow_turn_elbow_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 纯空气弯头局部阻力系数
    deduster_slow_turn_elbow_air_elbow_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉浓度修正系数
    deduster_slow_turn_elbow_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))

    ''' 90度等截面缓转弯头 '''
    # 1个90度等截面缓转弯头
    deduster_90_section_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉气体局部阻力系数
    deduster_section_slow_turn_elbow_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 纯空气弯头局部阻力系数
    deduster_section_slow_turn_elbow_air_elbow_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 转弯角度修正系数
    deduster_corrected_turning_angle_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 截面高宽比修正系数
    deduster_section_corrected_height_width_ratio_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 包含管壁粗糙度影响的纯空气下的转弯原始阻力系数
    deduster_section_original_resistance_coefficient_with_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉浓度修正系数
    deduster_section_slow_turn_elbow_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1个进口风箱
    deduster_inlet_bellows = db.Column(db.NUMERIC(precision=15, scale=5))
    # 除尘器出口至引风机入口总阻力
    deduster_to_induced_draft_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5))

    '''引风机出口至烟囱'''
    # 计算温度(引风机进口)
    induced_draft_inlet_calculated_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟量(引风机进口)
    induced_draft_inlet_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 密度
    induced_draft_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    induced_draft_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 动压头
    induced_draft_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟管截面积
    induced_draft_smoke_tube_area = db.Column(db.NUMERIC(precision=15, scale=5)) 
    # 宽
    induced_draft_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 高
    induced_draft_height = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管周长
    induced_draft_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道当量直径
    induced_draft_tube_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 气体运动粘度
    induced_draft_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 雷诺数
    induced_draft_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁绝对粗糙度
    induced_draft_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 管道内壁相对粗糙度
    induced_draft_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 560/△1
    induced_draft_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 判别式
    induced_draft_discriminant = db.Column(db.Text())

    # 摩擦阻力
    induced_draft_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 摩擦阻力系数
    induced_draft_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 单位长度摩擦阻力
    induced_draft_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风管长度
    induced_draft_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力
    induced_draft_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 局部阻力系数
    induced_draft_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))

    # 1个出口插板门
    induced_draft_outlet_plate_gate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1个出口扩散管
    induced_draft_outlet_diffuser_tube = db.Column(db.NUMERIC(precision=15, scale=5))
    # 1个45度缓转弯头（钢烟道）/1个90度缓转弯头（砖烟道）
    induced_draft_45_90_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉气体局部阻力系数
    induced_draft_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 纯空气局部阻力系数
    induced_draft_air_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 转弯角度修正系数
    induced_draft_corrected_turning_angle_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 截面高宽比修正系数
    induced_draft_corrected_height_width_ratio_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 包含管壁粗糙度影响的纯空气下的转弯原始阻力系数
    induced_draft_original_resistance_coefficient_with_roughness = db.Column(db.NUMERIC(precision=15, scale=5))
    # 含粉浓度修正系数
    induced_draft_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))

    # 砖烟道烟囱入口
    brick_chimney_inlet = db.Column(db.NUMERIC(precision=15, scale=5))
    # 引风机出口至烟囱入口总阻力
    induced_draft_to_chimney_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟道总阻力
    smoke_chimney_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5))

# 煤气发电 烟风系统
class GPGFlueGasAirSystem(db.Model):
     # 表名
    __tablename__ = 'gaspowergeneration_gas_air_system'

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    '''工况--标况'''
    # 工况温度-风
    c2s_condition_temperature_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况流量-风
    c2s_condition_flux_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压-风
    c2s_local_atmosphere_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况温度-风
    c2s_standard_temperature_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况压力-风
    c2s_standard_pressure_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况流量-风
    c2s_standard_flux_air = db.Column(db.NUMERIC(precision=15, scale=5))

    # 工况温度-烟
    c2s_condition_temperature_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况流量-烟
    c2s_condition_flux_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压-烟
    c2s_local_atmosphere_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况温度-烟
    c2s_standard_temperature_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况压力-烟
    c2s_standard_pressure_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况流量-烟
    c2s_standard_flux_smoke = db.Column(db.NUMERIC(precision=15, scale=5))

    '''标况--工况'''
    # 标况温度-风
    s2c_standard_temperature_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况压力-风
    s2c_standard_pressure_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况流量-风
    s2c_standard_flux_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况温度-风
    s2c_condition_temperature_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压-风
    s2c_local_atmosphere_air = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况流量-风
    s2c_condition_flux_air = db.Column(db.NUMERIC(precision=15, scale=5))

    # 标况温度-烟
    s2c_standard_temperature_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况压力-烟
    s2c_standard_pressure_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况流量-烟
    s2c_standard_flux_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况温度-烟
    s2c_condition_temperature_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压-烟
    s2c_local_atmosphere_smoke = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况流量-烟
    s2c_condition_flux_smoke = db.Column(db.NUMERIC(precision=15, scale=5))

    # 标况温度-煤气
    s2c_standard_temperature_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况压力-煤气
    s2c_standard_pressure_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标况流量-煤气
    s2c_standard_flux_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况温度-煤气
    s2c_condition_temperature_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压-煤气
    s2c_local_atmosphere_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工况流量-煤气
    s2c_condition_flux_gas = db.Column(db.NUMERIC(precision=15, scale=5))

    '''送风机'''
    # 空气温度
    blower_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风阻力
    blower_wind_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    blower_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟风流量（工况）
    blower_condition_smoke_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机温度
    blower_fan_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机全压
    blower_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用全压
    blower_fan_selected_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用流量
    blower_fan_selected_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机全压头效率
    blower_fan_pressure_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 机械传动效率
    blower_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    blower_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机轴功率
    blower_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机安全裕量
    blower_motor_safe_margin = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机功率
    blower_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用规格功率
    blower_specification_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用规格流量
    blower_specification_flux = db.Column(db.NUMERIC(precision=15, scale=5))

    '''引风机'''
    # 烟风温度
    Induced_smoke_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 全压
    Induced_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    Induced_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟风流量（工况）
    Induced_condition_smoke_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机温度
    Induced_fan_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟气密度
    Induced_smoke_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机全压
    Induced_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用全压
    Induced_fan_selected_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机选用流量
    Induced_fan_selected_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机效率
    Induced_fan_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 机械传动效率
    Induced_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电动机效率
    Induced_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))
    # 风机轴功率
    Induced_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机安全裕量
    Induced_motor_safe_margin = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电机功率
    Induced_motor_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用规格功率
    Induced_specification_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用规格流量
    Induced_specification_flux = db.Column(db.NUMERIC(precision=15, scale=5))

    '''煤气总管道计算'''
    # 介质流量
    gas_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 介质温度
    gas_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    gas_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算截面积
    gas_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算管道直径
    gas_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选取直径
    gas_tube_selected_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选取壁厚
    gas_tube_selected_thickness = db.Column(db.NUMERIC(precision=15, scale=5))

    '''冷风管道计算'''
    # 介质流量
    coldwind_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 介质温度
    coldwind_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    coldwind_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算截面积
    coldwind_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算当量管道直径
    coldwind_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长
    coldwind_tube_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽
    coldwind_tube_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用规格
    coldwind_tube_specification = db.Column(db.Text())

    '''热风管道计算-空预器出口方管'''
    # 介质流量
    hotwind_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 介质温度
    hotwind_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    hotwind_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算截面积
    hotwind_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算当量管道直径
    hotwind_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长
    hotwind_tube_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽
    hotwind_tube_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用规格
    hotwind_tube_specification = db.Column(db.Text())

    '''烟管道计算-总'''
    # 介质流量
    total_smoke_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 介质温度
    total_smoke_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    total_smoke_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算截面积
    total_smoke_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算当量管道直径
    total_smoke_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长
    total_smoke_tube_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽
    total_smoke_tube_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用规格
    total_smoke_tube_specification = db.Column(db.Text())

    '''烟管道计算-支'''
    # 介质流量
    branch_smoke_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 介质温度
    branch_smoke_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    branch_smoke_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算截面积
    branch_smoke_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算当量管道直径
    branch_smoke_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 长
    branch_smoke_tube_length = db.Column(db.NUMERIC(precision=15, scale=5))
    # 宽
    branch_smoke_tube_width = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选用规格
    branch_smoke_tube_specification = db.Column(db.Text())

    '''热风管道计算-母管'''
    # 介质流量
    main_hotwind_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 介质温度
    main_hotwind_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    main_hotwind_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算截面积
    main_hotwind_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算管道直径
    main_hotwind_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选取直径
    main_hotwind_tube_selected_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选取壁厚
    main_hotwind_tube_selected_thickness = db.Column(db.NUMERIC(precision=15, scale=5))

    '''热风管道计算-入口支管'''
    # 介质流量
    branch_hotwind_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5))
    # 介质温度
    branch_hotwind_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流速
    branch_hotwind_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算截面积
    branch_hotwind_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算管道直径
    branch_hotwind_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选取直径
    branch_hotwind_tube_selected_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选取壁厚
    branch_hotwind_tube_selected_thickness = db.Column(db.NUMERIC(precision=15, scale=5))

    '''烟囱抽力计算'''
    # 烟囱高度
    chimney_height = db.Column(db.NUMERIC(precision=15, scale=5))
    # 当地大气压
    local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标态下空气密度
    standard_air_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标态下平均烟气密度
    standard_average_smoke_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 标态下计算烟气密度
    standard_calculated_smoke_density = db.Column(db.NUMERIC(precision=15, scale=5))
    # 室外空气温度
    outdoor_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱进口处烟温
    chimney_inlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱每米高度的温度降
    chimney_temperature_drop_per_meter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱内平均温度
    chimney_average_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱抽力
    chimney_draft = db.Column(db.NUMERIC(precision=15, scale=5))

    '''烟囱出口内径计算及低负荷校核'''
    # 烟气量
    smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱出口温度
    chimney_outlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱出口流速
    chimney_outlet_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱出口内径
    chimney_outlet_inner_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 选取烟囱出口内径
    chimney_outlet_selected_inner_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 经验烟囱基础内径
    chimney_experience_base_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 低负荷下烟气量
    low_load_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 低负荷下排烟温度
    low_load_smoke_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 30%低负荷校核流速
    low_load_flow_30_percent = db.Column(db.NUMERIC(precision=15, scale=5))

    '''烟囱阻力计算'''
    # 烟囱阻力系数
    chimney_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱内平均流速
    chimney_average_velocity = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱平均直径
    chimney_average_diameter = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱摩擦阻力
    chimney_friction_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱出口阻力系数
    chimney_outlet_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱出口阻力
    chimney_outlet_resistance = db.Column(db.NUMERIC(precision=15, scale=5))
    # 烟囱总阻力
    chimney_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5))


# 煤气发电 原则性热力系统锅炉部分 (boiler of Principle Thermodynamic System)
class GPGBoilerOfPTS(db.Model):
     # 表名
    __tablename__ = 'gaspowergeneration_boiler_of_pts'

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

    # BFG煤气热值
    bfg_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # LDG煤气热值
    ldg_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # COG煤气热值
    cog_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 锅炉热效率
    boiler_efficiency = db.Column(db.NUMERIC(precision=15, scale=5))

    # 过热蒸汽出口压力
    superheated_steam_outlet_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # 过热蒸汽温度
    superheated_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # 过热蒸汽焓值
    superheated_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))

    # 过量空气系数
    excess_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5))

    # 空气温度
    air_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # 空气焓值
    air_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃烧所需空气量
    air_need_for_combustion = db.Column(db.NUMERIC(precision=15, scale=5))

    # 锅炉给水温度
    boiler_feed_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水焓值
    feedwater_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))

    # 排污率
    rate_of_blowdown = db.Column(db.NUMERIC(precision=15, scale=5))

    # 饱和水温度
    saturation_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # 饱和水焓值
    saturation_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))

    # 产汽量
    steam_output = db.Column(db.NUMERIC(precision=15, scale=5))



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

    # BFG煤气温度
    bfg_gas_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # LDG煤气温度
    ldg_gas_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # COG煤气温度
    cog_gas_temperature = db.Column(db.NUMERIC(precision=15, scale=5))

    # BFG煤气压力
    bfg_gas_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # LDG煤气压力
    ldg_gas_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # COG煤气压力
    cog_gas_pressure = db.Column(db.NUMERIC(precision=15, scale=5))

    # BFG煤气热值
    bfg_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # LDG煤气热值
    ldg_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # COG煤气热值
    cog_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5))

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