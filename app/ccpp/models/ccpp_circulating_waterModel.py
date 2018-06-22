# -*- coding: utf-8 -*-
from app import db


# 循环水系统
class CcppCirculatingWater(db.Model):
    # 表名
    __tablename__ = 'ccpp_circulating_water'
    __table_args__ = {'comment': u'燃气蒸汽联合循环-循环水系统数据'}
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
    v_circulating_pool_long = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池长")
    # 循环水池尺寸（宽）
    v_circulating_pool_wide = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池宽")
    # 循环水池尺寸（高）
    v_circulating_pool_hight = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池高")
    # 校核循环水池尺寸
    v_check_circulating_pool_size = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"校核循环水池尺寸")


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
        super(CcppCirculatingWater, self).__init__(**kwargs)

    @staticmethod
    def updata_circulating_water(CcppCirculatingWater):
        try:
            db.session.add(CcppCirculatingWater)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update CcppCirculatingWater"
                  "<id=%s> in database" % (CcppCirculatingWater.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_circulating_water(plan_id):
        result = CcppCirculatingWater.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_circulating_water(plan_id):
        circulating_water = \
            CcppCirculatingWater.search_circulating_water(plan_id)
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
