# -*- coding: utf-8 -*-
from flask import current_app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from flask_login import UserMixin, AnonymousUserMixin
from .. import db
from .. import login_manager


# 能源互联岛需求调查表模型
class EnergyIslandRequirement(db.Model):
    # 表名
    __tablename__ = 'energy_island_requirement'
    __table_args__ = {'comment': u'能源互联岛需求调查表'}
    # 自增id(主键)
    id = db.Column(db.Integer, primary_key=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    '''项目信息'''
    # 项目所在地
    type_wind_power = db.Column(db.String(16))
    # 项目类型
    eir_proj_type = db.Column(db.String(16))
    # 光伏类型
    eir_proj_photovoltaic_type = db.Column(db.String(16))
    # 地热及干热岩类型
    eir_proj_terrestrial_heat_hdr_type = db.Column(db.String(16))
    # 气象条件
    eir_proj_weather_conditions = db.Column(db.String(16))
    # 水质条件
    eir_proj_water_quality_condition = db.Column(db.String(16))
    '''运行信息'''
    # 年生产期
    eir_work_year = db.Column(db.String(16))
    eir_work_year_from = db.Column(db.String(16))
    eir_work_year_to = db.Column(db.String(16))
    # 年检修计划
    eir_work_year_maintain = db.Column(db.String(16))
    # 每天生产时间
    eir_work_day = db.Column(db.String(16))
    eir_work_day_from = db.Column(db.String(16))
    eir_work_day_to = db.Column(db.String(16))
    # 供冷季
    eir_work_cool = db.Column(db.String(16))
    eir_work_cool_from = db.Column(db.String(16))
    eir_work_cool_to = db.Column(db.String(16))
    # 供暖季
    eir_work_heat = db.Column(db.String(16))
    eir_work_heat_from = db.Column(db.String(16))
    eir_work_heat_to = db.Column(db.String(16))
    '''能源成本'''
    # 电价-峰
    eir_cost_electrovalence_peak_unit = db.Column(db.String(16))
    eir_cost_electrovalence_peak_duration = db.Column(db.String(48))
    eir_cost_electrovalence_peak_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电价-平
    eir_cost_electrovalence_average_unit = db.Column(db.String(16))
    eir_cost_electrovalence_average_duration = db.Column(db.String(48))
    eir_cost_electrovalence_average_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电价-谷
    eir_cost_electrovalence_valley_unit = db.Column(db.String(16))
    eir_cost_electrovalence_valley_duration = db.Column(db.String(48))
    eir_cost_electrovalence_valley_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电价-尖峰
    eir_cost_electrovalence_spike_unit = db.Column(db.String(16))
    eir_cost_electrovalence_spike_duration = db.Column(db.String(48))
    eir_cost_electrovalence_spike_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 燃气价格-冬
    eir_cost_gas_price_winter_unit = db.Column(db.String(16))
    eir_cost_gas_price_winter_duration = db.Column(db.String(48))
    eir_cost_gas_price_winter_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 燃气价格-夏
    eir_cost_gas_price_summer_unit = db.Column(db.String(16))
    eir_cost_gas_price_summer_duration = db.Column(db.String(48))
    eir_cost_gas_price_summer_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 工业水价
    eir_cost_industry_water_price_unit = db.Column(db.String(16))
    eir_cost_industry_water_price_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 生活水价
    eir_cost_domestic_water_price_unit = db.Column(db.String(16))
    eir_cost_domestic_water_price_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 供暖价格
    eir_cost_heat_price_unit = db.Column(db.String(16))
    eir_cost_heat_price_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 蒸汽价格
    eir_cost_steam_price_unit = db.Column(db.String(16))
    eir_cost_steam_price_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 供热水价格
    eir_cost_hot_water_price_unit = db.Column(db.String(16))
    eir_cost_hot_water_price_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 供冷价格
    eir_cost_cool_price_unit = db.Column(db.String(16))
    eir_cost_cool_price_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 污水处理价
    eir_cost_sewage_price_unit = db.Column(db.String(16))
    eir_cost_sewage_price_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 政策补贴
    eir_cost_subsidy_unit = db.Column(db.String(16))
    eir_cost_subsidy_value = db.Column(db.NUMERIC(precision=15, scale=5))
    '''现有情况'''
    # 市电等级
    eir_available_city_power_level_1_unit = db.Column(db.String(16))
    eir_available_city_power_level_2_unit = db.Column(db.String(16))
    # 数值1
    eir_available_city_power_level_1_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_city_power_level_2_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 数值2
    eir_available_city_power_level_1_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_city_power_level_2_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 总降变压器
    eir_available_down_transformer_1_unit = db.Column(db.String(16))
    eir_available_down_transformer_2_unit = db.Column(db.String(16))
    # 数值1
    eir_available_down_transformer_1_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_down_transformer_2_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 数值2
    eir_available_down_transformer_1_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_down_transformer_2_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 并网点
    eir_available_synchronization_point_1_unit = db.Column(db.String(16))
    eir_available_synchronization_point_2_unit = db.Column(db.String(16))
    # 数值1
    eir_available_synchronization_point_1_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_synchronization_point_2_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 数值2
    eir_available_synchronization_point_1_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_synchronization_point_2_2_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 自有蒸汽锅炉
    # 台数
    eir_available_steam_boiler_num_1_unit = db.Column(db.String(16))
    eir_available_steam_boiler_num_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_steam_boiler_num_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_steam_boiler_num_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 规模
    eir_available_steam_boiler_scale_1_unit = db.Column(db.String(16))
    eir_available_steam_boiler_scale_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_steam_boiler_scale_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_steam_boiler_scale_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 温度
    eir_available_steam_boiler_temperature_1_unit = db.Column(db.String(16))
    eir_available_steam_boiler_temperature_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_steam_boiler_temperature_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_steam_boiler_temperature_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 压力
    eir_available_steam_boiler_pressure_1_unit = db.Column(db.String(16))
    eir_available_steam_boiler_pressure_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_steam_boiler_pressure_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_steam_boiler_pressure_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 给水温度
    eir_available_steam_boiler_feed_water_temperature_1_unit = db.Column(
        db.String(16))
    eir_available_steam_boiler_feed_water_temperature_2_unit = db.Column(
        db.String(16))
    # 用途1
    eir_available_steam_boiler_feed_water_temperature_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_steam_boiler_feed_water_temperature_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 燃料
    eir_available_steam_boiler_fuel_1_unit = db.Column(db.String(16))
    eir_available_steam_boiler_fuel_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_steam_boiler_fuel_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_steam_boiler_fuel_2_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 外部汽源
    # 台数
    eir_available_external_steam_source_num_1_unit = db.Column(db.String(16))
    eir_available_external_steam_source_num_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_external_steam_source_num_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_steam_source_num_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 规模
    eir_available_external_steam_source_scale_1_unit = db.Column(db.String(16))
    eir_available_external_steam_source_scale_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_external_steam_source_scale_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_steam_source_scale_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 温度
    eir_available_external_steam_source_temperature_1_unit = db.Column(
        db.String(16))
    eir_available_external_steam_source_temperature_2_unit = db.Column(
        db.String(16))
    # 用途1
    eir_available_external_steam_source_temperature_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_steam_source_temperature_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 压力
    eir_available_external_steam_source_pressure_1_unit = db.Column(
        db.String(16))
    eir_available_external_steam_source_pressure_2_unit = db.Column(
        db.String(16))
    # 用途1
    eir_available_external_steam_source_pressure_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_steam_source_pressure_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 回水温度
    eir_available_external_steam_source_return_water_temp_1_unit = db.Column(
        db.String(16))
    eir_available_external_steam_source_return_water_temp_2_unit = db.Column(
        db.String(16))
    # 用途1
    eir_available_external_steam_source_return_water_temp_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_steam_source_return_water_temp_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 自有热水锅炉
    # 台数
    eir_available_own_water_boiler_num_1_unit = db.Column(db.String(16))
    eir_available_own_water_boiler_num_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_own_water_boiler_num_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_own_water_boiler_num_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 规模
    eir_available_own_water_boiler_scale_1_unit = db.Column(db.String(16))
    eir_available_own_water_boiler_scale_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_own_water_boiler_scale_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_own_water_boiler_scale_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 供温度
    eir_available_own_water_boiler_provide_temperature_1_unit = db.Column(
        db.String(16))
    eir_available_own_water_boiler_provide_temperature_2_unit = db.Column(
        db.String(16))
    # 用途1
    eir_available_own_water_boiler_provide_temperature_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_own_water_boiler_provide_temperature_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 压力
    eir_available_own_water_boiler_pressure_1_unit = db.Column(db.String(16))
    eir_available_own_water_boiler_pressure_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_own_water_boiler_pressure_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_own_water_boiler_pressure_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 回水温度
    eir_available_own_water_boiler_return_water_temperature_1_unit = db.Column(
        db.String(16))
    eir_available_own_water_boiler_return_water_temperature_2_unit = db.Column(
        db.String(16))
    # 用途1
    eir_available_own_water_boiler_return_water_temperature_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_own_water_boiler_return_water_temperature_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 燃料
    eir_available_own_water_boiler_fuel_1_unit = db.Column(db.String(16))
    eir_available_own_water_boiler_fuel_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_own_water_boiler_fuel_1_value = db.Column(db.String(16))
    # 用途2
    eir_available_own_water_boiler_fuel_2_value = db.Column(db.String(16))

    # 外部供热设备
    # 台数
    eir_available_external_heating_num_1_unit = db.Column(db.String(16))
    eir_available_external_heating_num_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_external_heating_num_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_heating_num_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 规模
    eir_available_external_heating_scale_1_unit = db.Column(db.String(16))
    eir_available_external_heating_scale_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_external_heating_scale_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_heating_scale_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 供温度
    eir_available_external_heating_provide_temperature_1_unit = db.Column(
        db.String(16))
    eir_available_external_heating_provide_temperature_2_unit = db.Column(
        db.String(16))
    # 用途1
    eir_available_external_heating_provide_temperature_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_heating_provide_temperature_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 压力
    eir_available_external_heating_pressure_1_unit = db.Column(db.String(16))
    eir_available_external_heating_pressure_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_external_heating_pressure_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_heating_pressure_2_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 回水温度
    eir_available_external_heating_return_water_temperature_1_unit = db.Column(
        db.String(16))
    eir_available_external_heating_return_water_temperature_2_unit = db.Column(
        db.String(16))
    # 用途1
    eir_available_external_heating_return_water_temperature_1_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_heating_return_water_temperature_2_value = db.Column(
        db.NUMERIC(precision=15, scale=5))
    # 燃料
    eir_available_external_heating_fuel_1_unit = db.Column(db.String(16))
    eir_available_external_heating_fuel_2_unit = db.Column(db.String(16))
    # 用途1
    eir_available_external_heating_fuel_1_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用途2
    eir_available_external_heating_fuel_2_value = db.Column(db.NUMERIC(precision=15, scale=5))

    # 现有制冷设备
    # 台数
    eir_available_cooling_equipment_1_num = db.Column(db.String(16))
    eir_available_cooling_equipment_2_num = db.Column(db.String(16))
    eir_available_cooling_equipment_3_num = db.Column(db.String(16))
    # 设备类型
    eir_available_cooling_equipment_1_type = db.Column(db.String(16))
    eir_available_cooling_equipment_2_type = db.Column(db.String(16))
    eir_available_cooling_equipment_3_type = db.Column(db.String(16))
    # 冷功率kw
    eir_available_cooling_equipment_1_cool_power = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_cooling_equipment_2_cool_power = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_cooling_equipment_3_cool_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电功率kw
    eir_available_cooling_equipment_1_power = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_cooling_equipment_2_power = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_cooling_equipment_3_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 热功率kw
    eir_available_cooling_equipment_1_heat_power = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_cooling_equipment_2_heat_power = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_cooling_equipment_3_heat_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 电功率kw
    eir_available_cooling_equipment_1_power_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_cooling_equipment_2_power_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_cooling_equipment_3_power_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 供冷末端形式
    eir_available_cold_end_form = db.Column(db.String(32))
    # 供暖末端形式
    eir_available_heat_end_form = db.Column(db.String(32))
    # 风电
    # 名称
    eir_available_wind_name_1 = db.Column(db.String(16))
    eir_available_wind_name_2 = db.Column(db.String(16))
    eir_available_wind_name_3 = db.Column(db.String(16))
    eir_available_wind_name_4 = db.Column(db.String(16))
    eir_available_wind_name_5 = db.Column(db.String(16))
    # 近30年平均风速
    eir_available_wind_ave_speed_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_wind_ave_speed_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_wind_ave_speed_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_wind_ave_speed_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_wind_ave_speed_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 近30年最大风速
    eir_available_wind_max_speed_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_wind_max_speed_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_wind_max_speed_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_wind_max_speed_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_wind_max_speed_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 相应风向频率
    eir_available_wind_wind_direction_frequency_1 = db.Column(db.String(16))
    eir_available_wind_wind_direction_frequency_2 = db.Column(db.String(16))
    eir_available_wind_wind_direction_frequency_3 = db.Column(db.String(16))
    eir_available_wind_wind_direction_frequency_4 = db.Column(db.String(16))
    eir_available_wind_wind_direction_frequency_5 = db.Column(db.String(16))

    # 光伏
    # 名称
    eir_available_photovoltaic_name_1 = db.Column(db.String(16))
    eir_available_photovoltaic_name_2 = db.Column(db.String(16))
    eir_available_photovoltaic_name_3 = db.Column(db.String(16))
    eir_available_photovoltaic_name_4 = db.Column(db.String(16))
    eir_available_photovoltaic_name_5 = db.Column(db.String(16))
    # 有效面积㎡
    eir_available_photovoltaic_area_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_area_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_area_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_area_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_area_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 倾斜角
    eir_available_photovoltaic_angle_inclination_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_angle_inclination_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_angle_inclination_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_angle_inclination_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_angle_inclination_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 均布承载力
    eir_available_photovoltaic_bearing_capacity_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_bearing_capacity_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_bearing_capacity_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_bearing_capacity_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_photovoltaic_bearing_capacity_5 = db.Column(db.NUMERIC(precision=15, scale=5))

    # 生活污水
    eir_available_domestic_sewage_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 处理方式
    eir_available_domestic_sewage_process_mode = db.Column(db.String(16))
    # 排放标准
    eir_available_domestic_sewage_emission_standard = db.Column(db.String(16))
    # 工业污水
    eir_available_industry_sewage_value = db.Column(db.NUMERIC(precision=15, scale=5))
    # 处理方式
    eir_available_industry_sewage_process_mode = db.Column(db.String(16))
    # 排放标准
    eir_available_industry_sewage_emission_standard = db.Column(db.String(16))

    # 储能设备
    # 类型
    eir_available_energy_storage_equipment_type = db.Column(db.String(16))
    # 规模
    eir_available_energy_storage_equipment_scale = db.Column(db.String(16))
    # 数量
    eir_available_energy_storage_equipment_num = db.Column(db.NUMERIC(precision=15, scale=5))

    # 空压站
    eir_available_air_compression_station_num_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_air_compression_station_flow_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_air_compression_station_pressure_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_air_compression_station_num_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_air_compression_station_flow_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_air_compression_station_pressure_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_air_compression_station_num_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_air_compression_station_flow_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_available_air_compression_station_pressure_3 = db.Column(db.NUMERIC(precision=15, scale=5))

    # 空压站余热利用
    # 进水温度℃
    eir_available_air_compression_in_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 出水温度℃
    eir_available_air_compression_out_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流量t/h
    eir_available_air_compression_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 回收用途
    eir_available_air_compression_recovery_usage = db.Column(db.String(16))

    # 固废处理
    # 处理量t/d
    eir_available_solid_waste_throughput = db.Column(db.NUMERIC(precision=15, scale=5))
    # 处理方式
    eir_available_solid_process_mode = db.Column(db.String(16))

    # 工业用水
    # 补水量t/h
    eir_available_industry_water_additional_water_amount = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用水量t/d
    eir_available_industry_water_water_consumption_td = db.Column(db.NUMERIC(precision=15, scale=5))
    # 用水量t/a
    eir_available_industry_water_water_consumption_ta = db.Column(db.NUMERIC(precision=15, scale=5))

    # 可利用的绿化面积
    eir_available_greening_space = db.Column(db.NUMERIC(precision=15, scale=5))

    # 未回收余热情况
    # 余量来源
    eir_available_afterheat_source = db.Column(db.String(16))
    # 余热量kW
    eir_available_afterheat_power = db.Column(db.NUMERIC(precision=15, scale=5))

    # 能源岛可利用场地
    eir_available_available_space = db.Column(db.String(16))
    # 扩建需求
    eir_available_expansion_demand = db.Column(db.String(16))

    '''典型日对应的季节'''
    eir_season_typical_day_1 = db.Column(db.String(16))
    eir_season_typical_day_2 = db.Column(db.String(16))
    eir_season_typical_day_3 = db.Column(db.String(16))
    eir_season_typical_day_4 = db.Column(db.String(16))

    '''热负荷'''
    # 热负荷
    # 建筑名称
    eir_thermal_load_building_name_1 = db.Column(db.String(16))
    eir_thermal_load_building_name_2 = db.Column(db.String(16))
    eir_thermal_load_building_name_3 = db.Column(db.String(16))
    eir_thermal_load_building_name_4 = db.Column(db.String(16))
    eir_thermal_load_building_name_5 = db.Column(db.String(16))
    # 建筑面积
    eir_thermal_load_building_area_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_building_area_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_building_area_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_building_area_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_building_area_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 热指标
    eir_thermal_load_heating_index_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_heating_index_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_heating_index_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_heating_index_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_heating_index_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 热负荷
    eir_thermal_load_thermal_load_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_thermal_load_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_thermal_load_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_thermal_load_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_thermal_load_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 各个时间点的热负荷
    eir_thermal_load_0_1_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_1_2_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_2_3_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_3_4_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_4_5_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_5_6_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_6_7_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_7_8_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_8_9_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_9_10_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_10_11_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_11_12_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_12_13_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_13_14_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_14_15_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_15_16_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_16_17_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_17_18_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_18_19_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_19_20_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_20_21_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_21_22_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_22_23_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_23_24_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_thermal_load_0_1_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_1_2_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_2_3_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_3_4_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_4_5_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_5_6_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_6_7_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_7_8_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_8_9_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_9_10_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_10_11_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_11_12_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_12_13_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_13_14_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_14_15_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_15_16_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_16_17_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_17_18_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_18_19_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_19_20_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_20_21_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_21_22_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_22_23_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_23_24_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_thermal_load_0_1_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_1_2_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_2_3_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_3_4_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_4_5_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_5_6_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_6_7_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_7_8_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_8_9_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_9_10_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_10_11_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_11_12_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_12_13_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_13_14_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_14_15_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_15_16_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_16_17_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_17_18_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_18_19_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_19_20_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_20_21_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_21_22_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_22_23_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_23_24_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_thermal_load_0_1_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_1_2_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_2_3_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_3_4_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_4_5_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_5_6_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_6_7_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_7_8_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_8_9_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_9_10_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_10_11_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_11_12_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_12_13_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_13_14_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_14_15_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_15_16_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_16_17_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_17_18_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_18_19_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_19_20_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_20_21_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_21_22_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_22_23_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_thermal_load_23_24_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 总计
    eir_thermal_load_total = db.Column(db.NUMERIC(precision=15, scale=5))

    # 冷负荷
    # 建筑名称
    eir_cooling_load_building_name_1 = db.Column(db.String(16))
    eir_cooling_load_building_name_2 = db.Column(db.String(16))
    eir_cooling_load_building_name_3 = db.Column(db.String(16))
    eir_cooling_load_building_name_4 = db.Column(db.String(16))
    eir_cooling_load_building_name_5 = db.Column(db.String(16))
    # 建筑面积
    eir_cooling_load_building_area_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_building_area_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_building_area_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_building_area_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_building_area_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冷指标
    eir_cooling_load_heating_index_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_heating_index_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_heating_index_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_heating_index_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_heating_index_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冷负荷
    eir_cooling_load_cooling_load_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_cooling_load_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_cooling_load_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_cooling_load_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_cooling_load_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 各个时间点的冷指标-工艺
    eir_cooling_load_technology_0_1_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_1_2_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_2_3_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_3_4_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_4_5_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_5_6_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_6_7_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_7_8_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_8_9_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_9_10_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_10_11_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_11_12_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_12_13_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_13_14_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_14_15_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_15_16_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_16_17_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_17_18_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_18_19_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_19_20_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_20_21_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_21_22_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_22_23_day_1 = db.Column(db.String(16))
    eir_cooling_load_technology_23_24_day_1 = db.Column(db.String(16))

    eir_cooling_load_technology_0_1_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_1_2_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_2_3_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_3_4_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_4_5_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_5_6_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_6_7_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_7_8_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_8_9_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_9_10_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_10_11_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_11_12_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_12_13_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_13_14_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_14_15_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_15_16_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_16_17_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_17_18_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_18_19_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_19_20_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_20_21_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_21_22_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_22_23_day_2 = db.Column(db.String(16))
    eir_cooling_load_technology_23_24_day_2 = db.Column(db.String(16))

    eir_cooling_load_technology_0_1_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_1_2_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_2_3_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_3_4_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_4_5_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_5_6_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_6_7_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_7_8_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_8_9_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_9_10_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_10_11_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_11_12_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_12_13_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_13_14_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_14_15_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_15_16_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_16_17_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_17_18_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_18_19_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_19_20_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_20_21_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_21_22_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_22_23_day_3 = db.Column(db.String(16))
    eir_cooling_load_technology_23_24_day_3 = db.Column(db.String(16))

    eir_cooling_load_technology_0_1_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_1_2_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_2_3_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_3_4_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_4_5_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_5_6_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_6_7_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_7_8_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_8_9_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_9_10_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_10_11_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_11_12_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_12_13_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_13_14_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_14_15_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_15_16_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_16_17_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_17_18_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_18_19_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_19_20_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_20_21_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_21_22_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_22_23_day_4 = db.Column(db.String(16))
    eir_cooling_load_technology_23_24_day_4 = db.Column(db.String(16))
    # 各个时间点的冷指标-舒适度
    eir_cooling_load_comfort_0_1_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_1_2_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_2_3_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_3_4_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_4_5_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_5_6_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_6_7_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_7_8_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_8_9_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_9_10_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_10_11_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_11_12_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_12_13_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_13_14_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_14_15_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_15_16_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_16_17_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_17_18_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_18_19_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_19_20_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_20_21_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_21_22_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_22_23_day_1 = db.Column(db.String(16))
    eir_cooling_load_comfort_23_24_day_1 = db.Column(db.String(16))

    eir_cooling_load_comfort_0_1_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_1_2_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_2_3_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_3_4_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_4_5_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_5_6_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_6_7_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_7_8_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_8_9_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_9_10_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_10_11_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_11_12_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_12_13_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_13_14_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_14_15_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_15_16_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_16_17_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_17_18_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_18_19_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_19_20_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_20_21_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_21_22_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_22_23_day_2 = db.Column(db.String(16))
    eir_cooling_load_comfort_23_24_day_2 = db.Column(db.String(16))

    eir_cooling_load_comfort_0_1_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_1_2_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_2_3_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_3_4_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_4_5_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_5_6_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_6_7_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_7_8_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_8_9_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_9_10_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_10_11_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_11_12_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_12_13_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_13_14_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_14_15_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_15_16_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_16_17_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_17_18_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_18_19_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_19_20_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_20_21_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_21_22_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_22_23_day_3 = db.Column(db.String(16))
    eir_cooling_load_comfort_23_24_day_3 = db.Column(db.String(16))

    eir_cooling_load_comfort_0_1_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_1_2_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_2_3_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_3_4_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_4_5_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_5_6_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_6_7_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_7_8_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_8_9_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_9_10_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_10_11_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_11_12_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_12_13_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_13_14_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_14_15_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_15_16_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_16_17_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_17_18_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_18_19_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_19_20_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_20_21_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_21_22_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_22_23_day_4 = db.Column(db.String(16))
    eir_cooling_load_comfort_23_24_day_4 = db.Column(db.String(16))
    # 各个时间点的冷负荷
    eir_cooling_load_0_1_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_1_2_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_2_3_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_3_4_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_4_5_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_5_6_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_6_7_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_7_8_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_8_9_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_9_10_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_10_11_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_11_12_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_12_13_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_13_14_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_14_15_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_15_16_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_16_17_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_17_18_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_18_19_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_19_20_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_20_21_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_21_22_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_22_23_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_23_24_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_cooling_load_0_1_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_1_2_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_2_3_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_3_4_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_4_5_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_5_6_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_6_7_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_7_8_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_8_9_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_9_10_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_10_11_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_11_12_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_12_13_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_13_14_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_14_15_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_15_16_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_16_17_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_17_18_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_18_19_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_19_20_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_20_21_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_21_22_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_22_23_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_23_24_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_cooling_load_0_1_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_1_2_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_2_3_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_3_4_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_4_5_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_5_6_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_6_7_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_7_8_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_8_9_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_9_10_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_10_11_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_11_12_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_12_13_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_13_14_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_14_15_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_15_16_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_16_17_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_17_18_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_18_19_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_19_20_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_20_21_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_21_22_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_22_23_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_23_24_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_cooling_load_0_1_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_1_2_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_2_3_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_3_4_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_4_5_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_5_6_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_6_7_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_7_8_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_8_9_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_9_10_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_10_11_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_11_12_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_12_13_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_13_14_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_14_15_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_15_16_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_16_17_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_17_18_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_18_19_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_19_20_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_20_21_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_21_22_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_22_23_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_cooling_load_23_24_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 总计
    eir_cooling_load_total = db.Column(db.NUMERIC(precision=15, scale=5))

    # 蒸汽需求
    # 压力
    eir_steam_demand_pressure_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_pressure_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_pressure_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_pressure_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_pressure_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 温度
    eir_steam_demand_temperature_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_temperature_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_temperature_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_temperature_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_temperature_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流量MAX
    eir_steam_demand_flow_max_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_max_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_max_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_max_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_max_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流量MIN
    eir_steam_demand_flow_min_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_min_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_min_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_min_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_min_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 流量RATED
    eir_steam_demand_flow_rated_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_rated_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_rated_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_rated_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_rated_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 凝结水回收率
    eir_steam_demand_condensate_recovery_percentage_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_condensate_recovery_percentage_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_condensate_recovery_percentage_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_condensate_recovery_percentage_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_condensate_recovery_percentage_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 总计
    eir_steam_demand_total_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_total_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_total_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_total_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_total_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 回水水质
    eir_steam_demand_backwater_quality_1 = db.Column(db.String(16))
    eir_steam_demand_backwater_quality_2 = db.Column(db.String(16))
    eir_steam_demand_backwater_quality_3 = db.Column(db.String(16))
    eir_steam_demand_backwater_quality_4 = db.Column(db.String(16))
    eir_steam_demand_backwater_quality_5 = db.Column(db.String(16))
    # 各个时间点的流量
    eir_steam_demand_flow_0_1_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_1_2_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_2_3_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_3_4_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_4_5_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_5_6_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_6_7_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_7_8_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_8_9_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_9_10_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_10_11_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_11_12_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_12_13_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_13_14_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_14_15_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_15_16_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_16_17_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_17_18_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_18_19_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_19_20_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_20_21_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_21_22_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_22_23_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_23_24_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_steam_demand_flow_0_1_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_1_2_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_2_3_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_3_4_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_4_5_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_5_6_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_6_7_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_7_8_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_8_9_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_9_10_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_10_11_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_11_12_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_12_13_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_13_14_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_14_15_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_15_16_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_16_17_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_17_18_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_18_19_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_19_20_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_20_21_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_21_22_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_22_23_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_23_24_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_steam_demand_flow_0_1_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_1_2_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_2_3_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_3_4_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_4_5_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_5_6_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_6_7_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_7_8_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_8_9_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_9_10_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_10_11_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_11_12_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_12_13_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_13_14_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_14_15_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_15_16_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_16_17_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_17_18_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_18_19_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_19_20_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_20_21_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_21_22_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_22_23_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_23_24_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_steam_demand_flow_0_1_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_1_2_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_2_3_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_3_4_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_4_5_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_5_6_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_6_7_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_7_8_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_8_9_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_9_10_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_10_11_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_11_12_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_12_13_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_13_14_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_14_15_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_15_16_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_16_17_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_17_18_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_18_19_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_19_20_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_20_21_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_21_22_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_22_23_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_steam_demand_flow_23_24_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))

    '''电力需求'''
    # 电力需求
    # 最大负荷
    eir_power_demand_peak_load = db.Column(db.NUMERIC(precision=15, scale=5))
    # 平均负荷
    eir_power_demand_average_load = db.Column(db.NUMERIC(precision=15, scale=5))
    # 最小负荷
    eir_power_demand_minimum_load = db.Column(db.NUMERIC(precision=15, scale=5))
    # 日用电量
    eir_power_demand_power_consumption_day = db.Column(db.NUMERIC(precision=15, scale=5))
    # 年用电量
    eir_power_demand_power_consumption_year = db.Column(db.NUMERIC(precision=15, scale=5))
    # 各个时间点的电荷量kwh
    eir_power_demand_quantity_0_1_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_1_2_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_2_3_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_3_4_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_4_5_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_5_6_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_6_7_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_7_8_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_8_9_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_9_10_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_10_11_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_11_12_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_12_13_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_13_14_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_14_15_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_15_16_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_16_17_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_17_18_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_18_19_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_19_20_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_20_21_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_21_22_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_22_23_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_23_24_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_power_demand_quantity_0_1_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_1_2_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_2_3_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_3_4_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_4_5_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_5_6_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_6_7_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_7_8_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_8_9_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_9_10_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_10_11_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_11_12_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_12_13_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_13_14_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_14_15_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_15_16_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_16_17_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_17_18_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_18_19_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_19_20_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_20_21_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_21_22_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_22_23_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_23_24_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_power_demand_quantity_0_1_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_1_2_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_2_3_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_3_4_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_4_5_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_5_6_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_6_7_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_7_8_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_8_9_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_9_10_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_10_11_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_11_12_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_12_13_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_13_14_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_14_15_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_15_16_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_16_17_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_17_18_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_18_19_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_19_20_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_20_21_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_21_22_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_22_23_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_23_24_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_power_demand_quantity_0_1_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_1_2_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_2_3_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_3_4_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_4_5_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_5_6_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_6_7_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_7_8_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_8_9_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_9_10_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_10_11_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_11_12_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_12_13_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_13_14_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_14_15_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_15_16_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_16_17_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_17_18_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_18_19_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_19_20_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_20_21_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_21_22_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_22_23_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_power_demand_quantity_23_24_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))

    '''热水需求'''
    # 热水需求
    # 供水温度
    eir_hot_water_demand_supply_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 回水温度
    eir_hot_water_demand_return_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5))
    # 小时供水量
    eir_hot_water_demand_supply_water_hour = db.Column(db.NUMERIC(precision=15, scale=5))
    # 日供水量
    eir_hot_water_demand_supply_water_day = db.Column(db.NUMERIC(precision=15, scale=5))
    # 年供水量
    eir_hot_water_demand_supply_water_year = db.Column(db.NUMERIC(precision=15, scale=5))
    # 各个时间点的热水流量
    eir_hot_water_demand_quantity_0_1_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_1_2_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_2_3_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_3_4_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_4_5_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_5_6_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_6_7_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_7_8_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_8_9_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_9_10_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_10_11_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_11_12_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_12_13_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_13_14_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_14_15_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_15_16_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_16_17_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_17_18_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_18_19_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_19_20_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_20_21_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_21_22_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_22_23_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_23_24_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_hot_water_demand_quantity_0_1_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_1_2_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_2_3_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_3_4_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_4_5_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_5_6_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_6_7_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_7_8_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_8_9_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_9_10_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_10_11_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_11_12_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_12_13_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_13_14_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_14_15_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_15_16_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_16_17_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_17_18_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_18_19_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_19_20_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_20_21_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_21_22_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_22_23_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_23_24_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_hot_water_demand_quantity_0_1_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_1_2_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_2_3_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_3_4_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_4_5_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_5_6_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_6_7_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_7_8_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_8_9_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_9_10_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_10_11_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_11_12_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_12_13_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_13_14_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_14_15_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_15_16_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_16_17_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_17_18_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_18_19_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_19_20_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_20_21_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_21_22_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_22_23_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_23_24_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_hot_water_demand_quantity_0_1_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_1_2_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_2_3_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_3_4_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_4_5_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_5_6_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_6_7_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_7_8_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_8_9_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_9_10_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_10_11_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_11_12_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_12_13_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_13_14_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_14_15_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_15_16_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_16_17_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_17_18_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_18_19_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_19_20_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_20_21_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_21_22_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_22_23_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_hot_water_demand_quantity_23_24_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))

    '''供气需求'''
    # 供气需求
    # 供气类型
    eir_air_supply_demand_technology_type = db.Column(db.String(16))
    eir_air_supply_demand_meter_type = db.Column(db.String(16))
    # 供气压力
    eir_air_supply_demand_technology_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_meter_pressure = db.Column(db.NUMERIC(precision=15, scale=5))
    # 供气流量
    eir_air_supply_demand_technology_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_meter_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 各个时间点的供气流量
    eir_air_supply_demand_quantity_0_1_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_1_2_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_2_3_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_3_4_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_4_5_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_5_6_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_6_7_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_7_8_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_8_9_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_9_10_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_10_11_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_11_12_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_12_13_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_13_14_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_14_15_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_15_16_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_16_17_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_17_18_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_18_19_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_19_20_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_20_21_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_21_22_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_22_23_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_23_24_day_1 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_air_supply_demand_quantity_0_1_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_1_2_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_2_3_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_3_4_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_4_5_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_5_6_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_6_7_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_7_8_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_8_9_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_9_10_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_10_11_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_11_12_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_12_13_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_13_14_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_14_15_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_15_16_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_16_17_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_17_18_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_18_19_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_19_20_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_20_21_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_21_22_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_22_23_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_23_24_day_2 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_air_supply_demand_quantity_0_1_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_1_2_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_2_3_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_3_4_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_4_5_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_5_6_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_6_7_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_7_8_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_8_9_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_9_10_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_10_11_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_11_12_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_12_13_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_13_14_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_14_15_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_15_16_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_16_17_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_17_18_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_18_19_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_19_20_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_20_21_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_21_22_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_22_23_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_23_24_day_3 = db.Column(db.NUMERIC(precision=15, scale=5))

    eir_air_supply_demand_quantity_0_1_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_1_2_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_2_3_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_3_4_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_4_5_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_5_6_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_6_7_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_7_8_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_8_9_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_9_10_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_10_11_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_11_12_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_12_13_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_13_14_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_14_15_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_15_16_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_16_17_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_17_18_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_18_19_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_19_20_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_20_21_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_21_22_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_22_23_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    eir_air_supply_demand_quantity_23_24_day_4 = db.Column(db.NUMERIC(precision=15, scale=5))

    # 添加/更新需求
    # param: requirement 需求实例
    @staticmethod
    def insert_requirement(requirement):
        try:
            db.session.add(requirement)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print(
                "Insert/Update requirement<id=%s, requirement_identity=%s> in database" %
                (requirement.id, requirement.id))

    # 删除需求
    # param: requirement 需求实例
    @staticmethod
    def delete_requirement(requirement):
        try:
            db.session.delete(requirement)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete requirement<id=%s, requirement_identity=%s> in database" %
                  (requirement.id, requirement.id))

    @staticmethod
    def batch_delete_requirement(plan_id):
        requirement = EnergyIslandRequirement.query.filter_by(plan_id=plan_id).one_or_none()
        db.session.delete(requirement)

    # 查找需求
    # param: id 需求主键
    # return: result 查找到的需求
    @staticmethod
    def search_requirement_by_id(id):
        result = EnergyIslandRequirement.query.filter_by(id=id).one_or_none()
        return result

    # 查找需求
    # param: plan_id 方案ID
    # return: result 查找到的需求
    @staticmethod
    def search_requirement_by_plan_id(plan_id):
        result = EnergyIslandRequirement.query.filter_by(plan_id=plan_id).one_or_none()
        return result


# 设备表模型
class Device(db.Model):
    # 表名
    __tablename__ = 'devices'
    __table_args__ = {'comment': u'能源互联岛设备表'}
    # 自增id(主键)
    id = db.Column(db.Integer, primary_key=True)
    # 设备大类(对应excel文件的sheet)
    device_class = db.Column(db.String(16))
    # 设备小类(对应excel文件单个sheet中的不同种设备)
    device_type = db.Column(db.String(16))
    # 设备型号
    device_code = db.Column(db.String(32))
    # key-value表示属性名、属性值
    main_prop_name_1 = db.Column(db.String(16))
    main_prop_value_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    main_prop_unit_1 = db.Column(db.String(16))
    main_prop_name_eng_1 = db.Column(db.String(16))

    main_prop_name_2 = db.Column(db.String(16))
    main_prop_value_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    main_prop_unit_2 = db.Column(db.String(16))
    main_prop_name_eng_2 = db.Column(db.String(16))

    main_prop_name_3 = db.Column(db.String(16))
    main_prop_value_3 = db.Column(db.NUMERIC(precision=15, scale=5))
    main_prop_unit_3 = db.Column(db.String(16))
    main_prop_name_eng_3 = db.Column(db.String(16))

    main_prop_name_4 = db.Column(db.String(16))
    main_prop_value_4 = db.Column(db.NUMERIC(precision=15, scale=5))
    main_prop_unit_4 = db.Column(db.String(16))
    main_prop_name_eng_4 = db.Column(db.String(16))

    main_prop_name_5 = db.Column(db.String(16))
    main_prop_value_5 = db.Column(db.NUMERIC(precision=15, scale=5))
    main_prop_unit_5 = db.Column(db.String(16))
    main_prop_name_eng_5 = db.Column(db.String(16))

    props_json = db.Column(db.Text())

    # 添加索引
    # __table_args__ = (
    #     db.Index('index_id', 'device_identity', ),
    #     db.Index('index_unit_1', 'device_identity', 'io_type', ),
    #     db.Index('index_unit_2', 'device_number', ),
    #     db.Index('index_unit_3', 'io_type', 'device_type', 'carrier_key', ),
    # )

    # 实例化
    # param: tuple 除了能量属性以外所有参数组成的元祖
    #               需要按照顺序写入
    # param: **kw 以字典的方式传入能量属性，key: 属性英文名，value: 属性值
    # return device实例
    @staticmethod
    def create_device(
        device_class,
        device_type,
        device_code,
        main_prop_name_1="",
        main_prop_value_1=0,
        main_prop_unit_1="",
        main_prop_name_eng_1="",
        main_prop_name_2="",
        main_prop_value_2=0,
        main_prop_unit_2="",
        main_prop_name_eng_2="",
        main_prop_name_3="",
        main_prop_value_3=0,
        main_prop_unit_3="",
        main_prop_name_eng_3="",
        main_prop_name_4="",
        main_prop_value_4=0,
        main_prop_unit_4="",
        main_prop_name_eng_4="",
        main_prop_name_5="",
        main_prop_value_5=0,
        main_prop_unit_5="",
        main_prop_name_eng_5="",
        props_json=""
    ):
        device = Device()
        device.device_class = device_class
        device.device_type = device_type
        device.device_code = device_code
        device.main_prop_name_1 = main_prop_name_1
        device.main_prop_value_1 = main_prop_value_1
        device.main_prop_unit_1 = main_prop_unit_1
        device.main_prop_name_eng_1 = main_prop_name_eng_1
        device.main_prop_name_2 = main_prop_name_2
        device.main_prop_value_2 = main_prop_value_2
        device.main_prop_unit_2 = main_prop_unit_2
        device.main_prop_name_eng_2 = main_prop_name_eng_2
        device.main_prop_name_3 = main_prop_name_3
        device.main_prop_value_3 = main_prop_value_3
        device.main_prop_unit_3 = main_prop_unit_3
        device.main_prop_name_eng_3 = main_prop_name_eng_3
        device.main_prop_name_4 = main_prop_name_4
        device.main_prop_value_4 = main_prop_value_4
        device.main_prop_unit_4 = main_prop_unit_4
        device.main_prop_name_eng_4 = main_prop_name_eng_4
        device.main_prop_name_5 = main_prop_name_5
        device.main_prop_value_5 = main_prop_value_5
        device.main_prop_unit_5 = main_prop_unit_5
        device.main_prop_name_eng_5 = main_prop_name_eng_5
        device.props_json = props_json
        return device

    # 添加/更新
    # param: device 设备实例
    @staticmethod
    def insert_device(device):
        try:
            db.session.add(device)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update insert_device<id=%s> in database" % (device.id))

    # 删除设备
    # param: device 设备实例
    @staticmethod
    def delete_device(id):
        device = Device.search_deviceById(id)
        try:
            db.session.delete(device)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete device<id=%s> in database" % (device.id))

    # 根据id查找实体
    @staticmethod
    def search_deviceById(id):
        result = Device.query.filter_by(
            id=id).one_or_none()
        return result


# 能源互联岛设备表属性模型
class DeviceProperties(db.Model):
    # 表名
    __tablename__ = 'device_properties'
    __table_args__ = {'comment': u'能源互联岛设备属性表'}
    # 自增id(主键)
    id = db.Column(db.Integer, primary_key=True)
    # 设备大类(对应excel文件的sheet)
    device_class = db.Column(db.String(16))
    # 设备小类(对应excel文件单个sheet中的不同种设备)
    device_type = db.Column(db.String(16))
    # 属性json(包含属性名、属性单位，以字符串形式储存)
    props_json = db.Column(db.Text())

    # 实例化
    # param: device_class, device_type, props_json
    # return: properties实例
    @staticmethod
    def create_device_properties(device_class, device_type, props_json):
        device_properties = DeviceProperties()
        device_properties.device_class = device_class
        device_properties.device_type = device_type
        device_properties.props_json = props_json
        return device_properties

    # 添加/更新
    # param: device_properties 设备属性实例
    @staticmethod
    def insert_device_properties(device_properties):
        try:
            db.session.add(device_properties)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update device_properties<id=%s> in database" % (device_properties.id))


# 光照时间表模型
class Hikari(db.Model):
    # 表名
    __tablename__ = 'hikari'
    __table_args__ = {'comment': u'能源互联岛光照时间表'}
    # 自增id(主键)
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(32))
    province = db.Column(db.String(32))
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    start_hour = db.Column(db.Integer)
    start_min = db.Column(db.Integer)
    end_hour = db.Column(db.Integer)
    end_min = db.Column(db.Integer)

    def __init__(self, city, province, month, day, start_hour, start_min, end_hour, end_min):
        self.city = city
        self.province = province
        self.month = month
        self.day = day
        self.start_hour = start_hour
        self.start_min = start_min
        self.end_hour = end_hour
        self.end_min = end_min

    # 添加/更新
    # param: hikari_time 光照时间实例
    @staticmethod
    def insert_hikari_time(hikari_time):
        try:
            db.session.add(hikari_time)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update hikari_time<id=%s> in database" % (hikari_time.id))


# 指标数值表
class MarkData(db.Model):
    # 表名
    __tablename__ = 'mark_data'
    __table_args__ = {'comment': u'能源互联岛指标表'}
    # 自增id(主键)
    id = db.Column(db.Integer, primary_key=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 年平均能源综合利用率
    col_1_W = db.Column(db.NUMERIC(precision=15, scale=5))
    col_1_Q1 = db.Column(db.NUMERIC(precision=15, scale=5))
    col_1_Q2 = db.Column(db.NUMERIC(precision=15, scale=5))
    col_1_B = db.Column(db.NUMERIC(precision=15, scale=5))
    col_1_QL = db.Column(db.NUMERIC(precision=15, scale=5))
    col_1_nu = db.Column(db.NUMERIC(precision=15, scale=5))
    # 冬季供热工况节能率
    col_2_Pe = db.Column(db.NUMERIC(precision=15, scale=5))
    col_2_ita_e = db.Column(db.NUMERIC(precision=15, scale=5))
    col_2_Qh = db.Column(db.NUMERIC(precision=15, scale=5))
    col_2_electric_ita_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    col_2_electric_ita_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    col_2_ita_b = db.Column(db.NUMERIC(precision=15, scale=5))
    col_2_nu = db.Column(db.NUMERIC(precision=15, scale=5))
    # 夏季供冷工况节能率（余热吸收式制冷+发电厂电制冷）
    col_3_Pe = db.Column(db.NUMERIC(precision=15, scale=5))
    col_3_ita_e = db.Column(db.NUMERIC(precision=15, scale=5))
    col_3_Qc = db.Column(db.NUMERIC(precision=15, scale=5))
    col_3_electric_ita_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    col_3_electric_ita_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    col_3_ita_b = db.Column(db.NUMERIC(precision=15, scale=5))
    col_3_nu = db.Column(db.NUMERIC(precision=15, scale=5))
    # 夏季供冷工况节能率（余热吸收式制冷+自发电制冷）
    col_4_Pe = db.Column(db.NUMERIC(precision=15, scale=5))
    col_4_ita_e = db.Column(db.NUMERIC(precision=15, scale=5))
    col_4_Qc = db.Column(db.NUMERIC(precision=15, scale=5))
    col_4_electric_ita_1 = db.Column(db.NUMERIC(precision=15, scale=5))
    col_4_electric_ita_2 = db.Column(db.NUMERIC(precision=15, scale=5))
    col_4_COPe = db.Column(db.NUMERIC(precision=15, scale=5))
    col_4_ita_h = db.Column(db.NUMERIC(precision=15, scale=5))
    col_4_COPa = db.Column(db.NUMERIC(precision=15, scale=5))
    col_4_nu = db.Column(db.NUMERIC(precision=15, scale=5))
    # 一次能源综合利用率
    col_5_heat = db.Column(db.NUMERIC(precision=15, scale=5))
    col_5_cool = db.Column(db.NUMERIC(precision=15, scale=5))
    col_5_electric = db.Column(db.NUMERIC(precision=15, scale=5))
    col_5_fuel = db.Column(db.NUMERIC(precision=15, scale=5))
    col_5_fuel_q = db.Column(db.NUMERIC(precision=15, scale=5))
    col_5_buy_electric = db.Column(db.NUMERIC(precision=15, scale=5))
    col_5_ita_ce = db.Column(db.NUMERIC(precision=15, scale=5))
    # 热电比
    col_6_heat = db.Column(db.NUMERIC(precision=15, scale=5))
    col_6_electric = db.Column(db.NUMERIC(precision=15, scale=5))
    col_6_heat_electric_ratio = db.Column(db.NUMERIC(precision=15, scale=5))
    # 减排量
    # CO2
    col_7_1_electric = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_coal = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_electric_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_gas_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_coal_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_electric_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_gas_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_coal_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_1_ita = db.Column(db.NUMERIC(precision=15, scale=5))
    # SO2
    col_7_2_electric = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_coal = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_electric_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_gas_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_coal_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_electric_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_gas_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_coal_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_2_ita = db.Column(db.NUMERIC(precision=15, scale=5))
    # NOx
    col_7_3_electric = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_gas = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_coal = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_electric_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_gas_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_coal_d = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_electric_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_gas_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_coal_c = db.Column(db.NUMERIC(precision=15, scale=5))
    col_7_3_ita = db.Column(db.NUMERIC(precision=15, scale=5))

    # 添加/更新
    # param: mark_data 光照时间实例
    @staticmethod
    def insert_mark_data(mark_data):
        try:
            db.session.add(mark_data)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update mark_data<id=%s> in database" % (mark_data.id))
