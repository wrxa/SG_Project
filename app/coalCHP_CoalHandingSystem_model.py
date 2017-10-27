# -*- coding: utf-8 -*-
'''
from flask import current_app
from datetime import datetime
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
'''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import db
from . import login_manager

'''---- 表名 燃煤热电联产计算_输煤系统表 ----'''
class CoalCHP_CoalHandingSystem(db.Model):
    # 表名
    __tablename__ = 'coalCHP_CoalHandingSystem'
    # 主ID， 自动生成
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    
    plan_id = db.Column(db.Integer, primary_key=True, nullable=False)

    '''------------------------------锅炉额定耗煤量------------------------------'''
    # 锅炉额定耗煤量 结果-设计（Value Design）
    boiler_rated_coal_capacity_DesignValue = db.Column(db.String(50))
    # 锅炉额定耗煤量 结果-校核（Value Verify）
    boiler_rated_coal_capacity_VerifyValue = db.Column(db.String(50))

    '''------------------------------锅炉日利用小时数------------------------------'''
    # 锅炉日利用小时数 结果-设计（Value Design）
    boiler_daily_utilization_hours_DesignValue = db.Column(db.String(50))
    # 锅炉日利用小时数 结果-校核（Value Verify）
    boiler_daily_utilization_hours_VerifyValue = db.Column(db.String(50))

    '''------------------------------日耗煤量------------------------------'''
    # 日耗煤量 结果-设计（Value Design）
    coal_daily_consumption_DesignValue = db.Column(db.String(50))
    # 日耗煤量 结果-校核（Value Verify）
    coal_daily_consumption_VerifyValue = db.Column(db.String(50))

    '''------------------------------锅炉年利用小时数------------------------------'''
    # 锅炉年利用小时数 结果-设计（Value Design）
    boiler_annual_utilization_hours_DesignValue = db.Column(db.String(50))
    # 锅炉年利用小时数 结果-校核（Value Verify）
    boiler_annual_utilization_hours_VerifyValue = db.Column(db.String(50))

    '''------------------------------年耗煤量------------------------------'''
    # 年耗煤量 结果-设计（Value Design）
    coal_annual_consumption_DesignValue = db.Column(db.String(50))
    # 年耗煤量 结果-校核（Value Verify）
    coal_annual_consumption_VerifyValue = db.Column(db.String(50))

    '''------------------------------日来煤不均衡系数------------------------------'''
    # 日来煤不均衡系数 结果-设计（Value Design）
    daily_coal_unbalanced_coefficient_DesignValue = db.Column(db.String(50))
    # 日来煤不均衡系数 结果-校核（Value Verify）
    daily_coal_unbalanced_coefficient_VerifyValue = db.Column(db.String(50))

    '''------------------------------铁路来煤日计算煤量------------------------------'''
    # 铁路来煤日计算煤量 结果-设计（Value Design）
    daily_rail_coal_amount_DesignValue = db.Column(db.String(50))
    # 铁路来煤日计算煤量 结果-校核（Value Verify）
    daily_rail_coal_amount_VerifyValue = db.Column(db.String(50))

    '''------------------------------汽车来煤日计算煤量------------------------------'''
    # 汽车来煤日计算煤量 结果-设计（Value Design）
    daily_vehicle_coal_amount_DesignValue = db.Column(db.String(50))
    # 汽车来煤日计算煤量 结果-校核（Value Verify）
    daily_vehicle_coal_amount_VerifyValue = db.Column(db.String(50))

    '''------------------------------锅炉每小时最大耗煤量------------------------------'''
    # 锅炉每小时最大耗煤量 结果-设计（Value Design）
    boiler_perhour_coal_max_capacity_DesignValue = db.Column(db.String(50))
    # 锅炉每小时最大耗煤量 结果-校核（Value Verify）
    boiler_perhour_coal_max_capacity_VerifyValue = db.Column(db.String(50))

    '''------------------------------锅炉每日运行时数------------------------------'''
    # 锅炉每日运行时数 结果-设计（Value Design）
    boiler_daily_working_hours_DesignValue = db.Column(db.String(50))
    # 锅炉每日运行时数 结果-校核（Value Verify）
    boiler_daily_working_hours_VerifyValue = db.Column(db.String(50))

    '''------------------------------煤的储备日数------------------------------'''
    # 煤的储备日数 结果-设计（Value Design）
    coal_store_days_DesignValue = db.Column(db.String(50))
    # 煤的储备日数 结果-校核（Value Verify）
    coal_store_days_VerifyValue = db.Column(db.String(50))

    '''------------------------------煤场存储量------------------------------'''
    # 煤场存储量 结果-设计（Value Design）
    coalyard_store_amount_DesignValue = db.Column(db.String(50))
    # 煤场存储量 结果-校核（Value Verify）
    coalyard_store_amount_VerifyValue = db.Column(db.String(50))

    '''------------------------------煤堆通道占用系数------------------------------'''
    # 煤堆通道占用系数 结果-设计（Value Design）
    coal_channel_occupy_coefficient_DesignValue = db.Column(db.String(50))
    # 煤堆通道占用系数 结果-校核（Value Verify）
    coal_channel_occupy_coefficient_VerifyValue = db.Column(db.String(50))

    '''------------------------------煤堆形状系数------------------------------'''
    # 煤堆形状系数 结果-设计（Value Design）
    coal_shape_coefficient_DesignValue = db.Column(db.String(50))
    # 煤堆形状系数 结果-校核（Value Verify）
    coal_shape_coefficient_VerifyValue = db.Column(db.String(50))

    '''------------------------------煤堆高度------------------------------'''
    # 煤堆高度 结果-设计（Value Design）
    coal_height_DesignValue = db.Column(db.String(50))
    # 煤堆高度 结果-校核（Value Verify）
    coal_height_VerifyValue = db.Column(db.String(50))

    '''------------------------------煤的堆密度------------------------------'''
    # 煤的堆密度 结果-设计（Value Design）
    coal_bulk_density_DesignValue = db.Column(db.String(50))
    # 煤的堆密度 结果-校核（Value Verify）
    coal_bulk_density_VerifyValue = db.Column(db.String(50))

    '''------------------------------煤场面积------------------------------'''
    # 煤场面积 结果-设计（Value Design）
    coalyard_area_DesignValue = db.Column(db.String(50))
    # 煤场面积 结果-校核（Value Verify）
    coalyard_area_VerifyValue = db.Column(db.String(50))

    '''------------------------------长------------------------------'''
    # 长 结果-设计（Value Design）
    height_DesignValue = db.Column(db.String(50))
    # 长 结果-校核（Value Verify）
    height_VerifyValue = db.Column(db.String(50))

    '''------------------------------宽------------------------------'''
    # 宽 结果-设计（Value Design）
    width_DesignValue = db.Column(db.String(50))
    # 宽 结果-校核（Value Verify）
    width_VerifyValue = db.Column(db.String(50))

    '''------------------------------有效容积-计算------------------------------'''
    # 有效容积-计算 结果-设计（Value Design）
    effective_cubage_calculated_DesignValue = db.Column(db.String(50))
    # 有效容积-计算 结果-校核（Value Verify）
    effective_cubage_calculated_VerifyValue = db.Column(db.String(50))

    '''------------------------------煤仓个数------------------------------'''
    # 煤仓个数 结果-设计（Value Design）
    coal_bunker_counts_DesignValue = db.Column(db.String(50))
    # 煤仓个数 结果-校核（Value Verify）
    coal_bunker_counts_VerifyValue = db.Column(db.String(50))

    '''------------------------------有效容积-选定------------------------------'''
    # 有效容积-选定 结果-设计（Value Design）
    effective_cubage_selected_DesignValue = db.Column(db.String(50))
    # 有效容积-选定 结果-校核（Value Verify）
    effective_cubage_selected_VerifyValue = db.Column(db.String(50))

    '''------------------------------反推消耗小时------------------------------'''
    # 反推消耗小时 结果-设计（Value Design）
    backstep_consumption_hours_DesignValue = db.Column(db.String(50))
    # 反推消耗小时 结果-校核（Value Verify）
    backstep_consumption_hours_VerifyValue = db.Column(db.String(50))

    '''------------------------------运输不平衡系数------------------------------'''
    # 运输不平衡系数 结果-设计（Value Design）
    transport_unbalanced_coefficient_DesignValue = db.Column(db.String(50))
    # 运输不平衡系数 结果-校核（Value Verify）
    transport_unbalanced_coefficient_VerifyValue = db.Column(db.String(50))

    '''------------------------------运煤系统有效作业时间------------------------------'''
    # 运煤系统有效作业时间 结果-设计（Value Design）
    transportsystem_effective_working_hours_DesignValue = db.Column(db.String(50))
    # 运煤系统有效作业时间 结果-校核（Value Verify）
    transportsystem_effective_working_hours_VerifyValue = db.Column(db.String(50))

    '''------------------------------运煤系统运输量------------------------------'''
    # 运煤系统运输量 结果-设计（Value Design）
    transportsystem_amount_DesignValue = db.Column(db.String(50))
    # 运煤系统运输量 结果-校核（Value Verify）
    transportsystem_amount_VerifyValue = db.Column(db.String(50))

    '''------------------------------车辆名义载重量------------------------------'''
    # 车辆名义载重量 结果-设计（Value Design）
    vehicle_capacity_tonnage_DesignValue = db.Column(db.String(50))
    # 车辆名义载重量 结果-校核（Value Verify）
    vehicle_capacity_tonnage_VerifyValue = db.Column(db.String(50))

    '''------------------------------每昼夜小时------------------------------'''
    # 每昼夜小时 结果-设计（Value Design）
    daily_working_hours_DesignValue = db.Column(db.String(50))
    # 每昼夜小时 结果-校核（Value Verify）
    daily_working_hours_VerifyValue = db.Column(db.String(50))

    '''------------------------------日计算受煤量------------------------------'''
    # 日计算受煤量 结果-设计（Value Design）
    daily_received_coal_amount_DesignValue = db.Column(db.String(50))
    # 日计算受煤量 结果-校核（Value Verify）
    daily_received_coal_amount_VerifyValue = db.Column(db.String(50))

    '''------------------------------每天进厂车次------------------------------'''
    # 每天进厂车次 结果-设计（Value Design）
    vehicle_daily_incoming_times_DesignValue = db.Column(db.String(50))
    # 每天进厂车次 结果-校核（Value Verify）
    vehicle_daily_incoming_times_VerifyValue = db.Column(db.String(50))

    '''------------------------------每小时进场车次------------------------------'''
    # 每小时进场车次 结果-设计（Value Design）
    vehicle_perhour_incoming_times_DesignValue = db.Column(db.String(50))
    # 每小时进场车次 结果-校核（Value Verify）
    vehicle_perhour_incoming_times_VerifyValue = db.Column(db.String(50))

    '''------------------------------多锅炉额定耗煤量------------------------------'''
    # 多锅炉额定耗煤量 结果-设计（Value Design）
    mutil_boiler_rated_coal_capacity_DesignValue = db.Column(db.String(50))
    # 多锅炉额定耗煤量 结果-校核（Value Verify）
    mutil_boiler_rated_coal_capacity_VerifyValue = db.Column(db.String(50))

    '''------------------------------多锅炉日额定耗煤总量------------------------------'''
    # 多锅炉日额定耗煤总量 结果-设计（Value Design）
    mutil_boiler_rated_coal_amount_DesignValue = db.Column(db.String(50))
    # 多锅炉日额定耗煤总量 结果-校核（Value Verify）
    mutil_boiler_rated_coal_amount_VerifyValue = db.Column(db.String(50))

    '''------------------------------输煤系统选定出力------------------------------'''
    # 输煤系统选定出力 结果-设计（Value Design）
    transportsystem_output_DesignValue = db.Column(db.String(50))
    # 输煤系统选定出力 结果-校核（Value Verify）
    transportsystem_output_VerifyValue = db.Column(db.String(50))

    '''------------------------------输煤系统运行小时------------------------------'''
    # 输煤系统运行小时 结果-设计（Value Design）
    transportsystem_working_hours_DesignValue = db.Column(db.String(50))
    # 输煤系统运行小时 结果-校核（Value Verify）
    transportsystem_working_hours_VerifyValue = db.Column(db.String(50))

    '''------------------------------每班运行小时------------------------------'''
    # 每班运行小时 结果-设计（Value Design）
    shift_working_hours_DesignValue = db.Column(db.String(50))
    # 每班运行小时 结果-校核（Value Verify）
    shift_working_hours_VerifyValue = db.Column(db.String(50))

    '''------------------------------带宽------------------------------'''
    # 带宽 结果-设计（Value Design）
    belt_width_DesignValue = db.Column(db.String(50))
    # 带宽 结果-校核（Value Verify）
    belt_width_VerifyValue = db.Column(db.String(50))

    '''------------------------------断面系数------------------------------'''
    # 断面系数 结果-设计（Value Design）
    section_coefficient_DesignValue = db.Column(db.String(50))
    # 断面系数 结果-校核（Value Verify）
    section_coefficient_VerifyValue = db.Column(db.String(50))

    '''------------------------------带速------------------------------'''
    # 带速 结果-设计（Value Design）
    belt_speed_DesignValue = db.Column(db.String(50))
    # 带速 结果-校核（Value Verify）
    belt_speed_VerifyValue = db.Column(db.String(50))

    '''------------------------------物料松散密度------------------------------'''
    # 物料松散密度 结果-设计（Value Design）
    material_bulk_density_DesignValue = db.Column(db.String(50))
    # 物料松散密度 结果-校核（Value Verify）
    material_bulk_density_VerifyValue = db.Column(db.String(50))

    '''------------------------------皮带最大输送能力------------------------------'''
    # 皮带最大输送能力 结果-设计（Value Design）
    belt_max_transport_capacity_DesignValue = db.Column(db.String(50))
    # 皮带最大输送能力 结果-校核（Value Verify）
    belt_max_transport_capacity_VerifyValue = db.Column(db.String(50))

    '''------------------------------台数------------------------------'''
    # 台数 结果-设计（Value Design）
    equipment_sets_DesignValue = db.Column(db.String(50))
    # 台数 结果-校核（Value Verify）
    equipment_sets_VerifyValue = db.Column(db.String(50))

    '''------------------------------富裕量------------------------------'''
    # 富裕量 结果-设计（Value Design）
    surplus_DesignValue = db.Column(db.String(50))
    # 富裕量 结果-校核（Value Verify）
    surplus_VerifyValue = db.Column(db.String(50))

    '''------------------------------单台给煤机出力------------------------------'''
    # 单台给煤机出力 结果-设计（Value Design）
    single_coal_feeder_output_DesignValue = db.Column(db.String(50))
    # 单台给煤机出力 结果-校核（Value Verify）
    single_coal_feeder_output_VerifyValue = db.Column(db.String(50))


    # 匿名用户没有任何权限
    def can(self, permissions):
        return False

    # 匿名用户不是管理员
    def is_admin(self):
        return False

