# -*- coding: utf-8 -*-
from datetime import datetime
from flask_login import current_user
from .models import EnergyIslandRequirement
from app.energy_island.models import Device, DeviceProperties, Hikari, MarkData
from sqlalchemy import or_, not_, and_
from decimal import Decimal
import json
import urllib
import copy
from app.models import Company, Plan, Module

all_list_column = []


list_column_eir_work = [
    {'column': 'eir_work_year', 'unit': ['个月', '月'], 'name': '年生产期', 'from': None, 'to': None},
    {'column': 'eir_work_year_from', 'unit': ['个月', '月'], 'name': '年生产期开始时段', 'from': None, 'to': None},
    {'column': 'eir_work_year_to', 'unit': ['个月', '月'], 'name': '年生产期截止时段', 'from': None, 'to': None},
    {'column': 'eir_work_year_maintain', 'unit': None, 'name': '年检修计划'},
    {'column': 'eir_work_day', 'unit': ['个小时', '小时'], 'name': '每天生产时间', 'from': None, 'to': None},
    {'column': 'eir_work_day_from', 'unit': ['个小时', '小时'], 'name': '每天生产时间开始时段', 'from': None, 'to': None},
    {'column': 'eir_work_day_to', 'unit': ['个小时', '小时'], 'name': '每天生产时间截止时段', 'from': None, 'to': None},
    {'column': 'eir_work_cool', 'unit': ['个月', '月', '日'], 'name': '供冷季', 'from': None, 'to': None},
    {'column': 'eir_work_heat', 'unit': ['个月', '月', '日'], 'name': '供暖季', 'from': None, 'to': None}
]

list_column_eir_cost = [
    {'column': 'eir_cost_electrovalence_peak', 'unit': '元/kWh', 'duration': None, 'value': None, 'name': '电价-峰'},
    {'column': 'eir_cost_electrovalence_average', 'unit': '元/kWh', 'duration': None, 'value': None, 'name': '电价-平'},
    {'column': 'eir_cost_electrovalence_valley', 'unit': '元/kWh', 'duration': None, 'value': None, 'name': '电价-谷'},
    {'column': 'eir_cost_electrovalence_spike', 'unit': '元/kWh', 'duration': None, 'value': None, 'name': '电价-尖峰'},
    {'column': 'eir_cost_gas_price_winter', 'unit': '元/Nm³', 'duration': None, 'value': None, 'name': '燃气价格-冬'},
    {'column': 'eir_cost_gas_price_summer', 'unit': '元/Nm³', 'duration': None, 'value': None, 'name': '燃气价格-夏'},
    {'column': 'eir_cost_industry_water_price_value', 'unit': '元/t', 'value': None, 'name': '工业水价'},
    {'column': 'eir_cost_domestic_water_price_value', 'unit': '元/t', 'value': None, 'name': '生活水价'},
    {'column': 'eir_cost_heat_price_value', 'unit': '元/GJ', 'value': None, 'name': '供暖价格'},
    {'column': 'eir_cost_steam_price_value', 'unit': '元/t', 'value': None, 'name': '蒸汽价格'},
    {'column': 'eir_cost_hot_water_price_value', 'unit': '元/t', 'value': None, 'name': '供热水价格'},
    {'column': 'eir_cost_cool_price_value', 'unit': '元/GJ', 'value': None, 'name': '供冷价格'},
    {'column': 'eir_cost_sewage_price_value', 'unit': '元/t', 'value': None, 'name': '污水处理价'},
    {'column': 'eir_cost_subsidy_value', 'unit': '元', 'value': None, 'name': '政策补贴'},
]

list_column_eir_available = [
    # 市电等级
    # 数值1
    {'column': 'eir_available_city_power_level_1_1_value', 'unit': '路', 'value': None, 'name': '数值1', 'type': '市电等级'},
    {'column': 'eir_available_city_power_level_2_1_value', 'unit': 'kV', 'value': None, 'name': '数值1', 'type': '市电等级'},
    # 数值2
    {'column': 'eir_available_city_power_level_1_2_value', 'unit': '路', 'value': None, 'name': '数值2', 'type': '市电等级'},
    {'column': 'eir_available_city_power_level_2_2_value', 'unit': 'kV', 'value': None, 'name': '数值2', 'type': '市电等级'},
    # 总降变压器
    # 数值1
    {'column': 'eir_available_down_transformer_1_1_value', 'unit': '个', 'value': None, 'name': '数值1', 'type': '总降变压器'},
    {'column': 'eir_available_down_transformer_2_1_value', 'unit': 'kVA', 'value': None, 'name': '数值1', 'type': '总降变压器'},
    # 数值2
    {'column': 'eir_available_down_transformer_1_2_value', 'unit': '个', 'value': None, 'name': '数值2', 'type': '总降变压器'},
    {'column': 'eir_available_down_transformer_2_2_value', 'unit': 'kVA', 'value': None, 'name': '数值2', 'type': '总降变压器'},
    # 并网点
    # 数值1
    {'column': 'eir_available_synchronization_point_1_1_value', 'unit': 'kV', 'value': None, 'name': '数值1', 'type': '并网点'},
    {'column': 'eir_available_synchronization_point_2_1_value', 'unit': '距离', 'value': None, 'name': '数值1', 'type': '并网点'},
    # 数值2
    {'column': 'eir_available_synchronization_point_1_2_value', 'unit': 'kV', 'value': None, 'name': '数值2', 'type': '并网点'},
    {'column': 'eir_available_synchronization_point_2_2_value', 'unit': '距离', 'value': None, 'name': '数值2', 'type': '并网点'},
    # index = 12
    # 自有蒸汽锅炉
    # 台数
    {'column': 'eir_available_steam_boiler_num_1_unit', 'unit': '台', 'value': None, 'name': '台数', 'type': '自有蒸汽锅炉'},
    # 用途1
    {'column': 'eir_available_steam_boiler_num_1_value', 'unit': '台', 'value': None, 'name': '台数', 'type': '自有蒸汽锅炉'},
    # 用途2
    {'column': 'eir_available_steam_boiler_num_2_value', 'unit': '台', 'value': None, 'name': '台数', 'type': '自有蒸汽锅炉'},
    # 规模
    {'column': 'eir_available_steam_boiler_scale_1_unit', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '自有蒸汽锅炉'},
    # 用途1
    {'column': 'eir_available_steam_boiler_scale_1_value', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '自有蒸汽锅炉'},
    # 用途2
    {'column': 'eir_available_steam_boiler_scale_2_value', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '自有蒸汽锅炉'},
    # 温度
    {'column': 'eir_available_steam_boiler_temperature_1_unit', 'unit': '℃', 'value': None, 'name': '温度', 'type': '自有蒸汽锅炉'},
    # 用途1
    {'column': 'eir_available_steam_boiler_temperature_1_value', 'unit': '℃', 'value': None, 'name': '温度', 'type': '自有蒸汽锅炉'},
    # 用途2
    {'column': 'eir_available_steam_boiler_temperature_2_value', 'unit': '℃', 'value': None, 'name': '温度', 'type': '自有蒸汽锅炉'},
    # 压力
    {'column': 'eir_available_steam_boiler_pressure_1_unit', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '自有蒸汽锅炉'},
    # 用途1
    {'column': 'eir_available_steam_boiler_pressure_1_value', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '自有蒸汽锅炉'},
    # 用途2
    {'column': 'eir_available_steam_boiler_pressure_2_value', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '自有蒸汽锅炉'},
    # 给水温度
    {'column': 'eir_available_steam_boiler_feed_water_temperature_1_unit', 'unit': '℃', 'value': None, 'name': '给水温度', 'type': '自有蒸汽锅炉'},
    # 用途1
    {'column': 'eir_available_steam_boiler_feed_water_temperature_1_value', 'unit': '℃', 'value': None, 'name': '给水温度', 'type': '自有蒸汽锅炉'},
    # 用途2
    {'column': 'eir_available_steam_boiler_feed_water_temperature_2_value', 'unit': '℃', 'value': None, 'name': '给水温度', 'type': '自有蒸汽锅炉'},
    # index = 27
    # 燃料
    [
        {'column': 'eir_available_steam_boiler_fuel_1_unit', 'unit': [{'name': 't/h(煤)', 'value': 't/h'}, {'name': 'm³/h（天然气）', 'value': 'm³/h'}, {'name': 'kWh（电）', 'value': 'kWh'}], 'value': None, 'name': '燃料', 'type': '自有蒸汽锅炉'},
        {'column': 'eir_available_steam_boiler_fuel_2_unit', 'unit': [{'name': 't/h(煤)', 'value': 't/h'}, {'name': 'm³/h（天然气）', 'value': 'm³/h'}, {'name': 'kWh（电）', 'value': 'kWh'}], 'value': None, 'name': '燃料', 'type': '自有蒸汽锅炉'}
    ],
    # 用途1
    {'column': 'eir_available_steam_boiler_fuel_1_value', 'unit': [{'name': 't/h(煤)', 'value': 't/h'}, {'name': 'm³/h（天然气）', 'value': 'm³/h'}, {'name': 'kWh（电）', 'value': 'kWh'}], 'value': None, 'name': '燃料', 'type': '自有蒸汽锅炉'},
    # 用途2
    {'column': 'eir_available_steam_boiler_fuel_2_value', 'unit': [{'name': 't/h(煤)', 'value': 't/h'}, {'name': 'm³/h（天然气）', 'value': 'm³/h'}, {'name': 'kWh（电）', 'value': 'kWh'}], 'value': None, 'name': '燃料', 'type': '自有蒸汽锅炉'},
    # index = 30
    # 外部汽源
    # 台数
    {'column': 'eir_available_external_steam_source_num_1_unit', 'unit': '台', 'value': None, 'name': '台数', 'type': '外部汽源'},
    {'column': 'eir_available_external_steam_source_num_2_unit', 'unit': '台', 'value': None, 'name': '台数', 'type': '外部汽源'},
    # 用途1
    {'column': 'eir_available_external_steam_source_num_1_value', 'unit': '台', 'value': None, 'name': '台数', 'type': '外部汽源'},
    # 用途2
    {'column': 'eir_available_external_steam_source_num_2_value', 'unit': '台', 'value': None, 'name': '台数', 'type': '外部汽源'},
    # 规模
    {'column': 'eir_available_external_steam_source_scale_1_unit', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '外部汽源'},
    {'column': 'eir_available_external_steam_source_scale_2_unit', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '外部汽源'},
    # 用途1
    {'column': 'eir_available_external_steam_source_scale_1_value', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '外部汽源'},
    # 用途2
    {'column': 'eir_available_external_steam_source_scale_2_value', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '外部汽源'},
    # 温度
    {'column': 'eir_available_external_steam_source_temperature_1_unit', 'unit': '℃', 'value': None, 'name': '温度', 'type': '外部汽源'},
    {'column': 'eir_available_external_steam_source_temperature_2_unit', 'unit': '℃', 'value': None, 'name': '温度', 'type': '外部汽源'},
    # 用途1
    {'column': 'eir_available_external_steam_source_temperature_1_value', 'unit': '℃', 'value': None, 'name': '温度', 'type': '外部汽源'},
    # 用途2
    {'column': 'eir_available_external_steam_source_temperature_2_value', 'unit': '℃', 'value': None, 'name': '温度', 'type': '外部汽源'},
    # 压力
    {'column': 'eir_available_external_steam_source_pressure_1_unit', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '外部汽源'},
    {'column': 'eir_available_external_steam_source_pressure_2_unit', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '外部汽源'},
    # 用途1
    {'column': 'eir_available_external_steam_source_pressure_1_value', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '外部汽源'},
    # 用途2
    {'column': 'eir_available_external_steam_source_pressure_2_value', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '外部汽源'},
    # 回水温度
    {'column': 'eir_available_external_steam_source_return_water_temp_1_unit', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '外部汽源'},
    {'column': 'eir_available_external_steam_source_return_water_temp_2_unit', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '外部汽源'},
    # 用途1
    {'column': 'eir_available_external_steam_source_return_water_temp_1_value', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '外部汽源'},
    # 用途2
    {'column': 'eir_available_external_steam_source_return_water_temp_2_value', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '外部汽源'},
    # index = 50
    # 自有热水锅炉
    # 台数
    {'column': 'eir_available_own_water_boiler_num_1_unit', 'unit': '台', 'value': None, 'name': '台数', 'type': '自有热水锅炉'},
    {'column': 'eir_available_own_water_boiler_num_2_unit', 'unit': '台', 'value': None, 'name': '台数', 'type': '自有热水锅炉'},
    # 用途1
    {'column': 'eir_available_own_water_boiler_num_1_value', 'unit': '台', 'value': None, 'name': '台数', 'type': '自有热水锅炉'},
    # 用途2
    {'column': 'eir_available_own_water_boiler_num_2_value', 'unit': '台', 'value': None, 'name': '台数', 'type': '自有热水锅炉'},
    # 规模
    {'column': 'eir_available_own_water_boiler_scale_1_unit', 'unit': 'MW', 'value': None, 'name': '规模', 'type': '自有热水锅炉'},
    {'column': 'eir_available_own_water_boiler_scale_2_unit', 'unit': 'MW', 'value': None, 'name': '规模', 'type': '自有热水锅炉'},
    # 用途1
    {'column': 'eir_available_own_water_boiler_scale_1_value', 'unit': 'MW', 'value': None, 'name': '规模', 'type': '自有热水锅炉'},
    # 用途2
    {'column': 'eir_available_own_water_boiler_scale_2_value', 'unit': 'MW', 'value': None, 'name': '规模', 'type': '自有热水锅炉'},
    # 供温度
    {'column': 'eir_available_own_water_boiler_provide_temperature_1_unit', 'unit': '℃', 'value': None, 'name': '供温度', 'type': '自有热水锅炉'},
    {'column': 'eir_available_own_water_boiler_provide_temperature_2_unit', 'unit': '℃', 'value': None, 'name': '供温度', 'type': '自有热水锅炉'},
    # 用途1
    {'column': 'eir_available_own_water_boiler_provide_temperature_1_value', 'unit': '℃', 'value': None, 'name': '供温度', 'type': '自有热水锅炉'},
    # 用途2
    {'column': 'eir_available_own_water_boiler_provide_temperature_2_value', 'unit': '℃', 'value': None, 'name': '供温度', 'type': '自有热水锅炉'},
    # 压力
    {'column': 'eir_available_own_water_boiler_pressure_1_unit', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '自有热水锅炉'},
    {'column': 'eir_available_own_water_boiler_pressure_2_unit', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '自有热水锅炉'},
    # 用途1
    {'column': 'eir_available_own_water_boiler_pressure_1_value', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '自有热水锅炉'},
    # 用途2
    {'column': 'eir_available_own_water_boiler_pressure_2_value', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '自有热水锅炉'},
    # 回水温度
    {'column': 'eir_available_own_water_boiler_return_water_temperature_1_unit', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '自有热水锅炉'},
    {'column': 'eir_available_own_water_boiler_return_water_temperature_2_unit', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '自有热水锅炉'},
    # 用途1
    {'column': 'eir_available_own_water_boiler_return_water_temperature_1_value', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '自有热水锅炉'},
    # 用途2
    {'column': 'eir_available_own_water_boiler_return_water_temperature_2_value', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '自有热水锅炉'},
    # index = 70
    # 燃料
    [
        {'column': 'eir_available_own_water_boiler_fuel_1_unit', 'unit': [{'name': 't/h(煤)', 'value': 't/h'}, {'name': 'm³/h（天然气）', 'value': 'm³/h'}, {'name': 'kWh（电）', 'value': 'kWh'}], 'value': None, 'name': '燃料', 'type': '自有热水锅炉'},
        {'column': 'eir_available_own_water_boiler_fuel_2_unit', 'unit': [{'name': 't/h(煤)', 'value': 't/h'}, {'name': 'm³/h（天然气）', 'value': 'm³/h'}, {'name': 'kWh（电）', 'value': 'kWh'}], 'value': None, 'name': '燃料', 'type': '自有热水锅炉'}
    ],
    # 用途1
    {'column': 'eir_available_own_water_boiler_fuel_1_value', 'unit': [{'name': 't/h(煤)', 'value': 't/h'}, {'name': 'm³/h（天然气）', 'value': 'm³/h'}, {'name': 'kWh（电）', 'value': 'kWh'}], 'value': None, 'name': '燃料', 'type': '自有热水锅炉'},
    # 用途2
    {'column': 'eir_available_own_water_boiler_fuel_2_value', 'unit': [{'name': 't/h(煤)', 'value': 't/h'}, {'name': 'm³/h（天然气）', 'value': 'm³/h'}, {'name': 'kWh（电）', 'value': 'kWh'}], 'value': None, 'name': '燃料', 'type': '自有热水锅炉'},
    # index = 73
    # 外部供热设备
    # 台数
    {'column': 'eir_available_external_heating_num_1_unit', 'unit': '台', 'value': None, 'name': '台数', 'type': '外部供热设备'},
    {'column': 'eir_available_external_heating_num_2_unit', 'unit': '台', 'value': None, 'name': '台数', 'type': '外部供热设备'},
    # 用途1
    {'column': 'eir_available_external_heating_num_1_value', 'unit': '台', 'value': None, 'name': '台数', 'type': '外部供热设备'},
    # 用途2
    {'column': 'eir_available_external_heating_num_2_value', 'unit': '台', 'value': None, 'name': '台数', 'type': '外部供热设备'},
    # 规模
    {'column': 'eir_available_external_heating_scale_1_unit', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '外部供热设备'},
    {'column': 'eir_available_external_heating_scale_2_unit', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '外部供热设备'},
    # 用途1
    {'column': 'eir_available_external_heating_scale_1_value', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '外部供热设备'},
    # 用途2
    {'column': 'eir_available_external_heating_scale_2_value', 'unit': 't/h', 'value': None, 'name': '规模', 'type': '外部供热设备'},
    # 供温度
    {'column': 'eir_available_external_heating_provide_temperature_1_unit', 'unit': '℃', 'value': None, 'name': '供温度', 'type': '外部供热设备'},
    {'column': 'eir_available_external_heating_provide_temperature_2_unit', 'unit': '℃', 'value': None, 'name': '供温度', 'type': '外部供热设备'},
    # 用途1
    {'column': 'eir_available_external_heating_provide_temperature_1_value', 'unit': '℃', 'value': None, 'name': '供温度', 'type': '外部供热设备'},
    # 用途2
    {'column': 'eir_available_external_heating_provide_temperature_2_value', 'unit': '℃', 'value': None, 'name': '供温度', 'type': '外部供热设备'},
    # 压力
    {'column': 'eir_available_external_heating_pressure_1_unit', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '外部供热设备'},
    {'column': 'eir_available_external_heating_pressure_2_unit', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '外部供热设备'},
    # 用途1
    {'column': 'eir_available_external_heating_pressure_1_value', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '外部供热设备'},
    # 用途2
    {'column': 'eir_available_external_heating_pressure_2_value', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '外部供热设备'},
    # 回水温度
    {'column': 'eir_available_external_heating_return_water_temperature_1_unit', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '外部供热设备'},
    {'column': 'eir_available_external_heating_return_water_temperature_2_unit', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '外部供热设备'},
    # 用途1
    {'column': 'eir_available_external_heating_return_water_temperature_1_value', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '外部供热设备'},
    # 用途2
    {'column': 'eir_available_external_heating_return_water_temperature_2_value', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '外部供热设备'}
    # index = 93
]

list_column_eir_available_2 = [
    # 现有制冷设备
    # 台数
    {'column': 'eir_available_cooling_equipment_1_num', 'unit': '台', 'value': None, 'name': '台数', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_2_num', 'unit': '台', 'value': None, 'name': '台数', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_3_num', 'unit': '台', 'value': None, 'name': '台数', 'type': '现有制冷设备'},
    # 设备类型
    {'column': 'eir_available_cooling_equipment_1_type', 'unit': '', 'value': None, 'name': '设备类型', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_2_type', 'unit': '', 'value': None, 'name': '设备类型', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_3_type', 'unit': '', 'value': None, 'name': '设备类型', 'type': '现有制冷设备'},
    # 冷功率kw
    {'column': 'eir_available_cooling_equipment_1_cool_power', 'unit': 'kW', 'value': None, 'name': '冷功率', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_2_cool_power', 'unit': 'kW', 'value': None, 'name': '冷功率', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_3_cool_power', 'unit': 'kW', 'value': None, 'name': '冷功率', 'type': '现有制冷设备'},
    # 电功率kw
    {'column': 'eir_available_cooling_equipment_1_power', 'unit': 'kW', 'value': None, 'name': '电功率', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_2_power', 'unit': 'kW', 'value': None, 'name': '电功率', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_3_power', 'unit': 'kW', 'value': None, 'name': '电功率', 'type': '现有制冷设备'},
    # 热功率kw
    {'column': 'eir_available_cooling_equipment_1_heat_power', 'unit': 'kW', 'value': None, 'name': '热功率', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_2_heat_power', 'unit': 'kW', 'value': None, 'name': '热功率', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_3_heat_power', 'unit': 'kW', 'value': None, 'name': '热功率', 'type': '现有制冷设备'},
    # 电功率kw
    {'column': 'eir_available_cooling_equipment_1_power_2', 'unit': 'kW', 'value': None, 'name': '电功率', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_2_power_2', 'unit': 'kW', 'value': None, 'name': '电功率', 'type': '现有制冷设备'},
    {'column': 'eir_available_cooling_equipment_3_power_2', 'unit': 'kW', 'value': None, 'name': '电功率', 'type': '现有制冷设备'},
    # index = 18
    # 风电
    # 名称
    {'column': 'eir_available_wind_name_1', 'unit': '', 'value': None, 'name': '名称', 'type': '风电'},
    {'column': 'eir_available_wind_name_2', 'unit': '', 'value': None, 'name': '名称', 'type': '风电'},
    {'column': 'eir_available_wind_name_3', 'unit': '', 'value': None, 'name': '名称', 'type': '风电'},
    {'column': 'eir_available_wind_name_4', 'unit': '', 'value': None, 'name': '名称', 'type': '风电'},
    {'column': 'eir_available_wind_name_5', 'unit': '', 'value': None, 'name': '名称', 'type': '风电'},
    # 近30年平均风速
    {'column': 'eir_available_wind_ave_speed_1', 'unit': '距离', 'value': None, 'name': '近30年平均风速', 'type': '风电'},
    {'column': 'eir_available_wind_ave_speed_2', 'unit': '距离', 'value': None, 'name': '近30年平均风速', 'type': '风电'},
    {'column': 'eir_available_wind_ave_speed_3', 'unit': '距离', 'value': None, 'name': '近30年平均风速', 'type': '风电'},
    {'column': 'eir_available_wind_ave_speed_4', 'unit': '距离', 'value': None, 'name': '近30年平均风速', 'type': '风电'},
    {'column': 'eir_available_wind_ave_speed_5', 'unit': '距离', 'value': None, 'name': '近30年平均风速', 'type': '风电'},
    # 近30年最大风速
    {'column': 'eir_available_wind_max_speed_1', 'unit': '距离', 'value': None, 'name': '近30年最大风速', 'type': '风电'},
    {'column': 'eir_available_wind_max_speed_2', 'unit': '距离', 'value': None, 'name': '近30年最大风速', 'type': '风电'},
    {'column': 'eir_available_wind_max_speed_3', 'unit': '距离', 'value': None, 'name': '近30年最大风速', 'type': '风电'},
    {'column': 'eir_available_wind_max_speed_4', 'unit': '距离', 'value': None, 'name': '近30年最大风速', 'type': '风电'},
    {'column': 'eir_available_wind_max_speed_5', 'unit': '距离', 'value': None, 'name': '近30年最大风速', 'type': '风电'},
    # 相应风向频率
    {'column': 'eir_available_wind_wind_direction_frequency_1', 'unit': '距离', 'value': None, 'name': '相应风向频率', 'type': '风电'},
    {'column': 'eir_available_wind_wind_direction_frequency_2', 'unit': '距离', 'value': None, 'name': '相应风向频率', 'type': '风电'},
    {'column': 'eir_available_wind_wind_direction_frequency_3', 'unit': '距离', 'value': None, 'name': '相应风向频率', 'type': '风电'},
    {'column': 'eir_available_wind_wind_direction_frequency_4', 'unit': '距离', 'value': None, 'name': '相应风向频率', 'type': '风电'},
    {'column': 'eir_available_wind_wind_direction_frequency_5', 'unit': '距离', 'value': None, 'name': '相应风向频率', 'type': '风电'},
    # index = 38
    # 光伏
    # 名称
    {'column': 'eir_available_photovoltaic_name_1', 'unit': '', 'value': None, 'name': '名称', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_name_2', 'unit': '', 'value': None, 'name': '名称', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_name_3', 'unit': '', 'value': None, 'name': '名称', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_name_4', 'unit': '', 'value': None, 'name': '名称', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_name_5', 'unit': '', 'value': None, 'name': '名称', 'type': '光伏'},
    # 有效面积㎡
    {'column': 'eir_available_photovoltaic_area_1', 'unit': '㎡', 'value': None, 'name': '有效面积', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_area_2', 'unit': '㎡', 'value': None, 'name': '有效面积', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_area_3', 'unit': '㎡', 'value': None, 'name': '有效面积', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_area_4', 'unit': '㎡', 'value': None, 'name': '有效面积', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_area_5', 'unit': '㎡', 'value': None, 'name': '有效面积', 'type': '光伏'},
    # 倾斜角
    {'column': 'eir_available_photovoltaic_angle_inclination_1', 'unit': '距离', 'value': None, 'name': '倾斜角', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_angle_inclination_2', 'unit': '距离', 'value': None, 'name': '倾斜角', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_angle_inclination_3', 'unit': '距离', 'value': None, 'name': '倾斜角', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_angle_inclination_4', 'unit': '距离', 'value': None, 'name': '倾斜角', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_angle_inclination_5', 'unit': '距离', 'value': None, 'name': '倾斜角', 'type': '光伏'},
    # 均布承载力
    {'column': 'eir_available_photovoltaic_bearing_capacity_1', 'unit': '距离', 'value': None, 'name': '均布承载力', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_bearing_capacity_2', 'unit': '距离', 'value': None, 'name': '均布承载力', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_bearing_capacity_3', 'unit': '距离', 'value': None, 'name': '均布承载力', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_bearing_capacity_4', 'unit': '距离', 'value': None, 'name': '均布承载力', 'type': '光伏'},
    {'column': 'eir_available_photovoltaic_bearing_capacity_5', 'unit': '距离', 'value': None, 'name': '均布承载力', 'type': '光伏'},
    # index = 58
    # 生活污水
    {'column': 'eir_available_domestic_sewage_value', 'unit': 't/d', 'value': None, 'name': '生活污水', 'type': '生活污水'},
    # 处理方式
    {'column': 'eir_available_domestic_sewage_process_mode', 'unit': '', 'value': None, 'name': '处理方式', 'type': '处理方式'},
    # 排放标准
    {'column': 'eir_available_domestic_sewage_emission_standard', 'unit': '', 'value': None, 'name': '排放标准', 'type': '排放标准'},
    # 工业污水
    {'column': 'eir_available_industry_sewage_value', 'unit': 't/d', 'value': None, 'name': '工业污水', 'type': '工业污水'},
    # 处理方式
    {'column': 'eir_available_industry_sewage_process_mode', 'unit': '', 'value': None, 'name': '处理方式', 'type': '处理方式'},
    # 排放标准
    {'column': 'eir_available_industry_sewage_emission_standard', 'unit': '', 'value': None, 'name': '排放标准', 'type': '排放标准'},
    # index = 64
    # 储能设备
    # 类型
    {'column': 'eir_available_energy_storage_equipment_type', 'unit': '距离', 'value': None, 'name': '类型', 'type': '储能设备'},
    # 规模
    {'column': 'eir_available_energy_storage_equipment_scale', 'unit': '距离', 'value': None, 'name': '规模', 'type': '储能设备'},
    # 数量
    {'column': 'eir_available_energy_storage_equipment_num', 'unit': '距离', 'value': None, 'name': '数量', 'type': '储能设备'},
    # index = 67
    # 空压站
    {'column': 'eir_available_air_compression_station_num_1', 'unit': '台', 'value': None, 'name': '台数', 'type': '空压站'},
    {'column': 'eir_available_air_compression_station_num_2', 'unit': '台', 'value': None, 'name': '台数', 'type': '空压站'},
    {'column': 'eir_available_air_compression_station_num_3', 'unit': '台', 'value': None, 'name': '台数', 'type': '空压站'},
    {'column': 'eir_available_air_compression_station_flow_1', 'unit': 'm³/min', 'value': None, 'name': '流量', 'type': '空压站'},
    {'column': 'eir_available_air_compression_station_flow_2', 'unit': 'm³/min', 'value': None, 'name': '流量', 'type': '空压站'},
    {'column': 'eir_available_air_compression_station_flow_3', 'unit': 'm³/min', 'value': None, 'name': '流量', 'type': '空压站'},
    {'column': 'eir_available_air_compression_station_pressure_1', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '空压站'},
    {'column': 'eir_available_air_compression_station_pressure_2', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '空压站'},
    {'column': 'eir_available_air_compression_station_pressure_3', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '空压站'},
    # index = 76
    # 空压站余热利用
    # 进水温度℃
    {'column': 'eir_available_air_compression_in_water_temperature', 'unit': '℃', 'value': None, 'name': '进水温度', 'type': '空压站余热利用'},
    # 出水温度℃
    {'column': 'eir_available_air_compression_out_water_temperature', 'unit': '℃', 'value': None, 'name': '出水温度℃', 'type': '空压站余热利用'},
    # 流量t/h
    {'column': 'eir_available_air_compression_flow', 'unit': 't/h', 'value': None, 'name': '流量', 'type': '空压站余热利用'},
    # 回收用途
    {'column': 'eir_available_air_compression_recovery_usage', 'unit': '距离', 'value': None, 'name': '回收用途', 'type': '空压站余热利用'},
    # index = 80
    # 固废处理
    # 处理量t/d
    {'column': 'eir_available_solid_waste_throughput', 'unit': 't/d', 'value': None, 'name': '处理量', 'type': '固废处理'},
    # 处理方式
    {'column': 'eir_available_solid_process_mode', 'unit': '距离', 'value': None, 'name': '处理方式', 'type': '固废处理'},
    # index = 82
    # 工业用水
    # 补水量t/h
    {'column': 'eir_available_industry_water_additional_water_amount', 'unit': 't/h', 'value': None, 'name': '补水量', 'type': '工业用水'},
    # 用水量t/d
    {'column': 'eir_available_industry_water_water_consumption_td', 'unit': 't/d', 'value': None, 'name': '用水量', 'type': '工业用水'},
    # 用水量t/a
    {'column': 'eir_available_industry_water_water_consumption_ta', 'unit': 't/a', 'value': None, 'name': '用水量', 'type': '工业用水'},
    # index = 85
    # 可利用的绿化面积
    {'column': 'eir_available_greening_space', 'unit': '距离', 'value': None, 'name': '可利用的绿化面积', 'type': '可利用的绿化面积'},
    # index = 86
    # 未回收余热情况
    # 余量来源
    {'column': 'eir_available_afterheat_source', 'unit': '距离', 'value': None, 'name': '余量来源', 'type': '未回收余热情况'},
    # 余热量kW
    {'column': 'eir_available_afterheat_power', 'unit': 'kW', 'value': None, 'name': '余热量', 'type': '未回收余热情况'},

    # 能源岛可利用场地
    {'column': 'eir_available_available_space', 'unit': '距离', 'value': None, 'name': '能源岛可利用场地', 'type': '能源岛可利用场地'},
    # 扩建需求
    {'column': 'eir_available_expansion_demand', 'unit': '距离', 'value': None, 'name': '扩建需求', 'type': '扩建需求'}
    # index = 90
]

list_column_eir_heat = [
    # 热负荷
    # 建筑名称
    {'column': 'eir_thermal_load_building_name_1', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '热负荷'},
    {'column': 'eir_thermal_load_building_name_2', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '热负荷'},
    {'column': 'eir_thermal_load_building_name_3', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '热负荷'},
    {'column': 'eir_thermal_load_building_name_4', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '热负荷'},
    {'column': 'eir_thermal_load_building_name_5', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '热负荷'},
    # 建筑面积
    {'column': 'eir_thermal_load_building_area_1', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '热负荷'},
    {'column': 'eir_thermal_load_building_area_2', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '热负荷'},
    {'column': 'eir_thermal_load_building_area_3', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '热负荷'},
    {'column': 'eir_thermal_load_building_area_4', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '热负荷'},
    {'column': 'eir_thermal_load_building_area_5', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '热负荷'},
    # 热指标
    {'column': 'eir_thermal_load_heating_index_1', 'unit': 'W/㎡', 'value': None, 'name': '热指标', 'type': '热负荷'},
    {'column': 'eir_thermal_load_heating_index_2', 'unit': 'W/㎡', 'value': None, 'name': '热指标', 'type': '热负荷'},
    {'column': 'eir_thermal_load_heating_index_3', 'unit': 'W/㎡', 'value': None, 'name': '热指标', 'type': '热负荷'},
    {'column': 'eir_thermal_load_heating_index_4', 'unit': 'W/㎡', 'value': None, 'name': '热指标', 'type': '热负荷'},
    {'column': 'eir_thermal_load_heating_index_5', 'unit': 'W/㎡', 'value': None, 'name': '热指标', 'type': '热负荷'},
    # 热负荷
    {'column': 'eir_thermal_load_thermal_load_1', 'unit': 'kW', 'value': None, 'name': '热负荷', 'type': '热负荷'},
    {'column': 'eir_thermal_load_thermal_load_2', 'unit': 'kW', 'value': None, 'name': '热负荷', 'type': '热负荷'},
    {'column': 'eir_thermal_load_thermal_load_3', 'unit': 'kW', 'value': None, 'name': '热负荷', 'type': '热负荷'},
    {'column': 'eir_thermal_load_thermal_load_4', 'unit': 'kW', 'value': None, 'name': '热负荷', 'type': '热负荷'},
    {'column': 'eir_thermal_load_thermal_load_5', 'unit': 'kW', 'value': None, 'name': '热负荷', 'type': '热负荷'},
    # index=20
    # 各个时间点的热负荷
    {'column': 'eir_thermal_load_0_1_day_1', 'unit': 'kW', 'value': None, 'name': '0:00—1:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_1_2_day_1', 'unit': 'kW', 'value': None, 'name': '1:00—2:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_2_3_day_1', 'unit': 'kW', 'value': None, 'name': '2:00—3:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_3_4_day_1', 'unit': 'kW', 'value': None, 'name': '3:00—4:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_4_5_day_1', 'unit': 'kW', 'value': None, 'name': '4:00—5:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_5_6_day_1', 'unit': 'kW', 'value': None, 'name': '5:00—6:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_6_7_day_1', 'unit': 'kW', 'value': None, 'name': '6:00—7:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_7_8_day_1', 'unit': 'kW', 'value': None, 'name': '7:00—8:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_8_9_day_1', 'unit': 'kW', 'value': None, 'name': '8:00—9:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_9_10_day_1', 'unit': 'kW', 'value': None, 'name': '9:00—10:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_10_11_day_1', 'unit': 'kW', 'value': None, 'name': '10:00—11:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_11_12_day_1', 'unit': 'kW', 'value': None, 'name': '11:00—12:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_12_13_day_1', 'unit': 'kW', 'value': None, 'name': '12:00—13:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_13_14_day_1', 'unit': 'kW', 'value': None, 'name': '13:00—14:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_14_15_day_1', 'unit': 'kW', 'value': None, 'name': '14:00—15:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_15_16_day_1', 'unit': 'kW', 'value': None, 'name': '15:00—16:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_16_17_day_1', 'unit': 'kW', 'value': None, 'name': '16:00—17:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_17_18_day_1', 'unit': 'kW', 'value': None, 'name': '17:00—18:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_18_19_day_1', 'unit': 'kW', 'value': None, 'name': '19:00—19:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_19_20_day_1', 'unit': 'kW', 'value': None, 'name': '19:00—20:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_20_21_day_1', 'unit': 'kW', 'value': None, 'name': '20:00—21:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_21_22_day_1', 'unit': 'kW', 'value': None, 'name': '21:00—22:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_22_23_day_1', 'unit': 'kW', 'value': None, 'name': '22:00—23:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_23_24_day_1', 'unit': 'kW', 'value': None, 'name': '23:00—24:00', 'type': '热负荷'},
    # index=44
    {'column': 'eir_thermal_load_0_1_day_2', 'unit': 'kW', 'value': None, 'name': '0:00—1:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_1_2_day_2', 'unit': 'kW', 'value': None, 'name': '1:00—2:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_2_3_day_2', 'unit': 'kW', 'value': None, 'name': '2:00—3:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_3_4_day_2', 'unit': 'kW', 'value': None, 'name': '3:00—4:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_4_5_day_2', 'unit': 'kW', 'value': None, 'name': '4:00—5:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_5_6_day_2', 'unit': 'kW', 'value': None, 'name': '5:00—6:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_6_7_day_2', 'unit': 'kW', 'value': None, 'name': '6:00—7:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_7_8_day_2', 'unit': 'kW', 'value': None, 'name': '7:00—8:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_8_9_day_2', 'unit': 'kW', 'value': None, 'name': '8:00—9:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_9_10_day_2', 'unit': 'kW', 'value': None, 'name': '9:00—10:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_10_11_day_2', 'unit': 'kW', 'value': None, 'name': '10:00—11:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_11_12_day_2', 'unit': 'kW', 'value': None, 'name': '11:00—12:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_12_13_day_2', 'unit': 'kW', 'value': None, 'name': '12:00—13:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_13_14_day_2', 'unit': 'kW', 'value': None, 'name': '13:00—14:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_14_15_day_2', 'unit': 'kW', 'value': None, 'name': '14:00—15:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_15_16_day_2', 'unit': 'kW', 'value': None, 'name': '15:00—16:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_16_17_day_2', 'unit': 'kW', 'value': None, 'name': '16:00—17:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_17_18_day_2', 'unit': 'kW', 'value': None, 'name': '17:00—18:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_18_19_day_2', 'unit': 'kW', 'value': None, 'name': '19:00—19:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_19_20_day_2', 'unit': 'kW', 'value': None, 'name': '19:00—20:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_20_21_day_2', 'unit': 'kW', 'value': None, 'name': '20:00—21:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_21_22_day_2', 'unit': 'kW', 'value': None, 'name': '21:00—22:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_22_23_day_2', 'unit': 'kW', 'value': None, 'name': '22:00—23:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_23_24_day_2', 'unit': 'kW', 'value': None, 'name': '23:00—24:00', 'type': '热负荷'},
    # index=68
    {'column': 'eir_thermal_load_0_1_day_3', 'unit': 'kW', 'value': None, 'name': '0:00—1:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_1_2_day_3', 'unit': 'kW', 'value': None, 'name': '1:00—2:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_2_3_day_3', 'unit': 'kW', 'value': None, 'name': '2:00—3:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_3_4_day_3', 'unit': 'kW', 'value': None, 'name': '3:00—4:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_4_5_day_3', 'unit': 'kW', 'value': None, 'name': '4:00—5:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_5_6_day_3', 'unit': 'kW', 'value': None, 'name': '5:00—6:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_6_7_day_3', 'unit': 'kW', 'value': None, 'name': '6:00—7:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_7_8_day_3', 'unit': 'kW', 'value': None, 'name': '7:00—8:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_8_9_day_3', 'unit': 'kW', 'value': None, 'name': '8:00—9:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_9_10_day_3', 'unit': 'kW', 'value': None, 'name': '9:00—10:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_10_11_day_3', 'unit': 'kW', 'value': None, 'name': '10:00—11:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_11_12_day_3', 'unit': 'kW', 'value': None, 'name': '11:00—12:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_12_13_day_3', 'unit': 'kW', 'value': None, 'name': '12:00—13:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_13_14_day_3', 'unit': 'kW', 'value': None, 'name': '13:00—14:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_14_15_day_3', 'unit': 'kW', 'value': None, 'name': '14:00—15:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_15_16_day_3', 'unit': 'kW', 'value': None, 'name': '15:00—16:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_16_17_day_3', 'unit': 'kW', 'value': None, 'name': '16:00—17:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_17_18_day_3', 'unit': 'kW', 'value': None, 'name': '17:00—18:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_18_19_day_3', 'unit': 'kW', 'value': None, 'name': '19:00—19:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_19_20_day_3', 'unit': 'kW', 'value': None, 'name': '19:00—20:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_20_21_day_3', 'unit': 'kW', 'value': None, 'name': '20:00—21:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_21_22_day_3', 'unit': 'kW', 'value': None, 'name': '21:00—22:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_22_23_day_3', 'unit': 'kW', 'value': None, 'name': '22:00—23:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_23_24_day_3', 'unit': 'kW', 'value': None, 'name': '23:00—24:00', 'type': '热负荷'},
    # index=92
    {'column': 'eir_thermal_load_0_1_day_4', 'unit': 'kW', 'value': None, 'name': '0:00—1:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_1_2_day_4', 'unit': 'kW', 'value': None, 'name': '1:00—2:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_2_3_day_4', 'unit': 'kW', 'value': None, 'name': '2:00—3:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_3_4_day_4', 'unit': 'kW', 'value': None, 'name': '3:00—4:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_4_5_day_4', 'unit': 'kW', 'value': None, 'name': '4:00—5:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_5_6_day_4', 'unit': 'kW', 'value': None, 'name': '5:00—6:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_6_7_day_4', 'unit': 'kW', 'value': None, 'name': '6:00—7:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_7_8_day_4', 'unit': 'kW', 'value': None, 'name': '7:00—8:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_8_9_day_4', 'unit': 'kW', 'value': None, 'name': '8:00—9:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_9_10_day_4', 'unit': 'kW', 'value': None, 'name': '9:00—10:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_10_11_day_4', 'unit': 'kW', 'value': None, 'name': '10:00—11:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_11_12_day_4', 'unit': 'kW', 'value': None, 'name': '11:00—12:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_12_13_day_4', 'unit': 'kW', 'value': None, 'name': '12:00—13:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_13_14_day_4', 'unit': 'kW', 'value': None, 'name': '13:00—14:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_14_15_day_4', 'unit': 'kW', 'value': None, 'name': '14:00—15:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_15_16_day_4', 'unit': 'kW', 'value': None, 'name': '15:00—16:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_16_17_day_4', 'unit': 'kW', 'value': None, 'name': '16:00—17:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_17_18_day_4', 'unit': 'kW', 'value': None, 'name': '17:00—18:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_18_19_day_4', 'unit': 'kW', 'value': None, 'name': '19:00—19:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_19_20_day_4', 'unit': 'kW', 'value': None, 'name': '19:00—20:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_20_21_day_4', 'unit': 'kW', 'value': None, 'name': '20:00—21:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_21_22_day_4', 'unit': 'kW', 'value': None, 'name': '21:00—22:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_22_23_day_4', 'unit': 'kW', 'value': None, 'name': '22:00—23:00', 'type': '热负荷'},
    {'column': 'eir_thermal_load_23_24_day_4', 'unit': 'kW', 'value': None, 'name': '23:00—24:00', 'type': '热负荷'},
    # index=116
    # 总计
    {'column': 'eir_thermal_load_total', 'unit': 'kW', 'value': None, 'name': '总计', 'type': '热负荷'}
]

list_column_eir_cool = [
    # 冷负荷
    # 建筑名称
    {'column': 'eir_cooling_load_building_name_1', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_building_name_2', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_building_name_3', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_building_name_4', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_building_name_5', 'unit': '', 'value': None, 'name': '建筑名称', 'type': '冷负荷'},
    # 建筑面积
    {'column': 'eir_cooling_load_building_area_1', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_building_area_2', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_building_area_3', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_building_area_4', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_building_area_5', 'unit': '㎡', 'value': None, 'name': '建筑面积', 'type': '冷负荷'},
    # 冷指标
    {'column': 'eir_cooling_load_heating_index_1', 'unit': 'W/㎡', 'value': None, 'name': '冷指标', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_heating_index_2', 'unit': 'W/㎡', 'value': None, 'name': '冷指标', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_heating_index_3', 'unit': 'W/㎡', 'value': None, 'name': '冷指标', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_heating_index_4', 'unit': 'W/㎡', 'value': None, 'name': '冷指标', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_heating_index_5', 'unit': 'W/㎡', 'value': None, 'name': '冷指标', 'type': '冷负荷'},
    # 冷负荷
    {'column': 'eir_cooling_load_cooling_load_1', 'unit': 'kW', 'value': None, 'name': '冷负荷', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_cooling_load_2', 'unit': 'kW', 'value': None, 'name': '冷负荷', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_cooling_load_3', 'unit': 'kW', 'value': None, 'name': '冷负荷', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_cooling_load_4', 'unit': 'kW', 'value': None, 'name': '冷负荷', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_cooling_load_5', 'unit': 'kW', 'value': None, 'name': '冷负荷', 'type': '冷负荷'},
    # index=20
    # 各个时间点的冷指标-工艺
    {'column': 'eir_cooling_load_technology_0_1_day_1', 'unit': '距离', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_1_2_day_1', 'unit': '距离', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_2_3_day_1', 'unit': '距离', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_3_4_day_1', 'unit': '距离', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_4_5_day_1', 'unit': '距离', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_5_6_day_1', 'unit': '距离', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_6_7_day_1', 'unit': '距离', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_7_8_day_1', 'unit': '距离', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_8_9_day_1', 'unit': '距离', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_9_10_day_1', 'unit': '距离', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_10_11_day_1', 'unit': '距离', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_11_12_day_1', 'unit': '距离', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_12_13_day_1', 'unit': '距离', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_13_14_day_1', 'unit': '距离', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_14_15_day_1', 'unit': '距离', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_15_16_day_1', 'unit': '距离', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_16_17_day_1', 'unit': '距离', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_17_18_day_1', 'unit': '距离', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_18_19_day_1', 'unit': '距离', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_19_20_day_1', 'unit': '距离', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_20_21_day_1', 'unit': '距离', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_21_22_day_1', 'unit': '距离', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_22_23_day_1', 'unit': '距离', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_23_24_day_1', 'unit': '距离', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_technology_0_1_day_2', 'unit': '距离', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_1_2_day_2', 'unit': '距离', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_2_3_day_2', 'unit': '距离', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_3_4_day_2', 'unit': '距离', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_4_5_day_2', 'unit': '距离', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_5_6_day_2', 'unit': '距离', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_6_7_day_2', 'unit': '距离', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_7_8_day_2', 'unit': '距离', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_8_9_day_2', 'unit': '距离', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_9_10_day_2', 'unit': '距离', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_10_11_day_2', 'unit': '距离', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_11_12_day_2', 'unit': '距离', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_12_13_day_2', 'unit': '距离', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_13_14_day_2', 'unit': '距离', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_14_15_day_2', 'unit': '距离', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_15_16_day_2', 'unit': '距离', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_16_17_day_2', 'unit': '距离', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_17_18_day_2', 'unit': '距离', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_18_19_day_2', 'unit': '距离', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_19_20_day_2', 'unit': '距离', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_20_21_day_2', 'unit': '距离', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_21_22_day_2', 'unit': '距离', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_22_23_day_2', 'unit': '距离', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_23_24_day_2', 'unit': '距离', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_technology_0_1_day_3', 'unit': '距离', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_1_2_day_3', 'unit': '距离', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_2_3_day_3', 'unit': '距离', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_3_4_day_3', 'unit': '距离', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_4_5_day_3', 'unit': '距离', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_5_6_day_3', 'unit': '距离', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_6_7_day_3', 'unit': '距离', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_7_8_day_3', 'unit': '距离', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_8_9_day_3', 'unit': '距离', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_9_10_day_3', 'unit': '距离', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_10_11_day_3', 'unit': '距离', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_11_12_day_3', 'unit': '距离', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_12_13_day_3', 'unit': '距离', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_13_14_day_3', 'unit': '距离', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_14_15_day_3', 'unit': '距离', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_15_16_day_3', 'unit': '距离', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_16_17_day_3', 'unit': '距离', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_17_18_day_3', 'unit': '距离', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_18_19_day_3', 'unit': '距离', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_19_20_day_3', 'unit': '距离', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_20_21_day_3', 'unit': '距离', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_21_22_day_3', 'unit': '距离', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_22_23_day_3', 'unit': '距离', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_23_24_day_3', 'unit': '距离', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_technology_0_1_day_4', 'unit': '距离', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_1_2_day_4', 'unit': '距离', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_2_3_day_4', 'unit': '距离', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_3_4_day_4', 'unit': '距离', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_4_5_day_4', 'unit': '距离', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_5_6_day_4', 'unit': '距离', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_6_7_day_4', 'unit': '距离', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_7_8_day_4', 'unit': '距离', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_8_9_day_4', 'unit': '距离', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_9_10_day_4', 'unit': '距离', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_10_11_day_4', 'unit': '距离', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_11_12_day_4', 'unit': '距离', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_12_13_day_4', 'unit': '距离', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_13_14_day_4', 'unit': '距离', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_14_15_day_4', 'unit': '距离', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_15_16_day_4', 'unit': '距离', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_16_17_day_4', 'unit': '距离', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_17_18_day_4', 'unit': '距离', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_18_19_day_4', 'unit': '距离', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_19_20_day_4', 'unit': '距离', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_20_21_day_4', 'unit': '距离', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_21_22_day_4', 'unit': '距离', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_22_23_day_4', 'unit': '距离', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_technology_23_24_day_4', 'unit': '距离', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},
    # index=116
    # 各个时间点的冷指标-舒适度
    {'column': 'eir_cooling_load_comfort_0_1_day_1', 'unit': '距离', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_1_2_day_1', 'unit': '距离', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_2_3_day_1', 'unit': '距离', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_3_4_day_1', 'unit': '距离', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_4_5_day_1', 'unit': '距离', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_5_6_day_1', 'unit': '距离', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_6_7_day_1', 'unit': '距离', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_7_8_day_1', 'unit': '距离', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_8_9_day_1', 'unit': '距离', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_9_10_day_1', 'unit': '距离', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_10_11_day_1', 'unit': '距离', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_11_12_day_1', 'unit': '距离', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_12_13_day_1', 'unit': '距离', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_13_14_day_1', 'unit': '距离', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_14_15_day_1', 'unit': '距离', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_15_16_day_1', 'unit': '距离', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_16_17_day_1', 'unit': '距离', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_17_18_day_1', 'unit': '距离', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_18_19_day_1', 'unit': '距离', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_19_20_day_1', 'unit': '距离', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_20_21_day_1', 'unit': '距离', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_21_22_day_1', 'unit': '距离', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_22_23_day_1', 'unit': '距离', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_23_24_day_1', 'unit': '距离', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_comfort_0_1_day_2', 'unit': '距离', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_1_2_day_2', 'unit': '距离', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_2_3_day_2', 'unit': '距离', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_3_4_day_2', 'unit': '距离', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_4_5_day_2', 'unit': '距离', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_5_6_day_2', 'unit': '距离', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_6_7_day_2', 'unit': '距离', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_7_8_day_2', 'unit': '距离', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_8_9_day_2', 'unit': '距离', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_9_10_day_2', 'unit': '距离', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_10_11_day_2', 'unit': '距离', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_11_12_day_2', 'unit': '距离', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_12_13_day_2', 'unit': '距离', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_13_14_day_2', 'unit': '距离', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_14_15_day_2', 'unit': '距离', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_15_16_day_2', 'unit': '距离', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_16_17_day_2', 'unit': '距离', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_17_18_day_2', 'unit': '距离', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_18_19_day_2', 'unit': '距离', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_19_20_day_2', 'unit': '距离', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_20_21_day_2', 'unit': '距离', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_21_22_day_2', 'unit': '距离', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_22_23_day_2', 'unit': '距离', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_23_24_day_2', 'unit': '距离', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_comfort_0_1_day_3', 'unit': '距离', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_1_2_day_3', 'unit': '距离', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_2_3_day_3', 'unit': '距离', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_3_4_day_3', 'unit': '距离', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_4_5_day_3', 'unit': '距离', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_5_6_day_3', 'unit': '距离', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_6_7_day_3', 'unit': '距离', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_7_8_day_3', 'unit': '距离', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_8_9_day_3', 'unit': '距离', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_9_10_day_3', 'unit': '距离', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_10_11_day_3', 'unit': '距离', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_11_12_day_3', 'unit': '距离', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_12_13_day_3', 'unit': '距离', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_13_14_day_3', 'unit': '距离', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_14_15_day_3', 'unit': '距离', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_15_16_day_3', 'unit': '距离', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_16_17_day_3', 'unit': '距离', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_17_18_day_3', 'unit': '距离', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_18_19_day_3', 'unit': '距离', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_19_20_day_3', 'unit': '距离', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_20_21_day_3', 'unit': '距离', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_21_22_day_3', 'unit': '距离', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_22_23_day_3', 'unit': '距离', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_23_24_day_3', 'unit': '距离', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_comfort_0_1_day_4', 'unit': '距离', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_1_2_day_4', 'unit': '距离', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_2_3_day_4', 'unit': '距离', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_3_4_day_4', 'unit': '距离', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_4_5_day_4', 'unit': '距离', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_5_6_day_4', 'unit': '距离', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_6_7_day_4', 'unit': '距离', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_7_8_day_4', 'unit': '距离', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_8_9_day_4', 'unit': '距离', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_9_10_day_4', 'unit': '距离', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_10_11_day_4', 'unit': '距离', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_11_12_day_4', 'unit': '距离', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_12_13_day_4', 'unit': '距离', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_13_14_day_4', 'unit': '距离', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_14_15_day_4', 'unit': '距离', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_15_16_day_4', 'unit': '距离', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_16_17_day_4', 'unit': '距离', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_17_18_day_4', 'unit': '距离', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_18_19_day_4', 'unit': '距离', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_19_20_day_4', 'unit': '距离', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_20_21_day_4', 'unit': '距离', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_21_22_day_4', 'unit': '距离', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_22_23_day_4', 'unit': '距离', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_comfort_23_24_day_4', 'unit': '距离', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},
    # index=212
    # 各个时间点的冷负荷
    {'column': 'eir_cooling_load_0_1_day_1', 'unit': 'kW', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_1_2_day_1', 'unit': 'kW', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_2_3_day_1', 'unit': 'kW', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_3_4_day_1', 'unit': 'kW', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_4_5_day_1', 'unit': 'kW', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_5_6_day_1', 'unit': 'kW', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_6_7_day_1', 'unit': 'kW', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_7_8_day_1', 'unit': 'kW', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_8_9_day_1', 'unit': 'kW', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_9_10_day_1', 'unit': 'kW', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_10_11_day_1', 'unit': 'kW', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_11_12_day_1', 'unit': 'kW', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_12_13_day_1', 'unit': 'kW', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_13_14_day_1', 'unit': 'kW', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_14_15_day_1', 'unit': 'kW', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_15_16_day_1', 'unit': 'kW', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_16_17_day_1', 'unit': 'kW', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_17_18_day_1', 'unit': 'kW', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_18_19_day_1', 'unit': 'kW', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_19_20_day_1', 'unit': 'kW', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_20_21_day_1', 'unit': 'kW', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_21_22_day_1', 'unit': 'kW', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_22_23_day_1', 'unit': 'kW', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_23_24_day_1', 'unit': 'kW', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_0_1_day_2', 'unit': 'kW', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_1_2_day_2', 'unit': 'kW', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_2_3_day_2', 'unit': 'kW', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_3_4_day_2', 'unit': 'kW', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_4_5_day_2', 'unit': 'kW', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_5_6_day_2', 'unit': 'kW', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_6_7_day_2', 'unit': 'kW', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_7_8_day_2', 'unit': 'kW', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_8_9_day_2', 'unit': 'kW', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_9_10_day_2', 'unit': 'kW', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_10_11_day_2', 'unit': 'kW', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_11_12_day_2', 'unit': 'kW', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_12_13_day_2', 'unit': 'kW', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_13_14_day_2', 'unit': 'kW', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_14_15_day_2', 'unit': 'kW', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_15_16_day_2', 'unit': 'kW', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_16_17_day_2', 'unit': 'kW', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_17_18_day_2', 'unit': 'kW', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_18_19_day_2', 'unit': 'kW', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_19_20_day_2', 'unit': 'kW', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_20_21_day_2', 'unit': 'kW', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_21_22_day_2', 'unit': 'kW', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_22_23_day_2', 'unit': 'kW', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_23_24_day_2', 'unit': 'kW', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_0_1_day_3', 'unit': 'kW', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_1_2_day_3', 'unit': 'kW', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_2_3_day_3', 'unit': 'kW', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_3_4_day_3', 'unit': 'kW', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_4_5_day_3', 'unit': 'kW', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_5_6_day_3', 'unit': 'kW', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_6_7_day_3', 'unit': 'kW', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_7_8_day_3', 'unit': 'kW', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_8_9_day_3', 'unit': 'kW', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_9_10_day_3', 'unit': 'kW', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_10_11_day_3', 'unit': 'kW', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_11_12_day_3', 'unit': 'kW', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_12_13_day_3', 'unit': 'kW', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_13_14_day_3', 'unit': 'kW', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_14_15_day_3', 'unit': 'kW', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_15_16_day_3', 'unit': 'kW', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_16_17_day_3', 'unit': 'kW', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_17_18_day_3', 'unit': 'kW', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_18_19_day_3', 'unit': 'kW', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_19_20_day_3', 'unit': 'kW', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_20_21_day_3', 'unit': 'kW', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_21_22_day_3', 'unit': 'kW', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_22_23_day_3', 'unit': 'kW', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_23_24_day_3', 'unit': 'kW', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},

    {'column': 'eir_cooling_load_0_1_day_4', 'unit': 'kW', 'value': None, 'name': '0:00—1:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_1_2_day_4', 'unit': 'kW', 'value': None, 'name': '1:00—2:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_2_3_day_4', 'unit': 'kW', 'value': None, 'name': '2:00—3:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_3_4_day_4', 'unit': 'kW', 'value': None, 'name': '3:00—4:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_4_5_day_4', 'unit': 'kW', 'value': None, 'name': '4:00—5:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_5_6_day_4', 'unit': 'kW', 'value': None, 'name': '5:00—6:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_6_7_day_4', 'unit': 'kW', 'value': None, 'name': '6:00—7:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_7_8_day_4', 'unit': 'kW', 'value': None, 'name': '7:00—8:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_8_9_day_4', 'unit': 'kW', 'value': None, 'name': '8:00—9:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_9_10_day_4', 'unit': 'kW', 'value': None, 'name': '9:00—10:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_10_11_day_4', 'unit': 'kW', 'value': None, 'name': '10:00—11:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_11_12_day_4', 'unit': 'kW', 'value': None, 'name': '11:00—12:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_12_13_day_4', 'unit': 'kW', 'value': None, 'name': '12:00—13:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_13_14_day_4', 'unit': 'kW', 'value': None, 'name': '13:00—14:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_14_15_day_4', 'unit': 'kW', 'value': None, 'name': '14:00—15:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_15_16_day_4', 'unit': 'kW', 'value': None, 'name': '15:00—16:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_16_17_day_4', 'unit': 'kW', 'value': None, 'name': '16:00—17:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_17_18_day_4', 'unit': 'kW', 'value': None, 'name': '17:00—18:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_18_19_day_4', 'unit': 'kW', 'value': None, 'name': '19:00—19:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_19_20_day_4', 'unit': 'kW', 'value': None, 'name': '19:00—20:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_20_21_day_4', 'unit': 'kW', 'value': None, 'name': '20:00—21:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_21_22_day_4', 'unit': 'kW', 'value': None, 'name': '21:00—22:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_22_23_day_4', 'unit': 'kW', 'value': None, 'name': '22:00—23:00', 'type': '冷负荷'},
    {'column': 'eir_cooling_load_23_24_day_4', 'unit': 'kW', 'value': None, 'name': '23:00—24:00', 'type': '冷负荷'},
    # index=308
    # 总计
    {'column': 'eir_cooling_load_total', 'unit': 'kW', 'value': None, 'name': '总计', 'type': '冷负荷'}
]

list_column_eir_steam = [
    # 蒸汽需求
    # 压力
    {'column': 'eir_steam_demand_pressure_1', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_pressure_2', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_pressure_3', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_pressure_4', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_pressure_5', 'unit': 'Mpa', 'value': None, 'name': '压力', 'type': '蒸汽需求'},
    # 温度
    {'column': 'eir_steam_demand_temperature_1', 'unit': '℃', 'value': None, 'name': '温度', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_temperature_2', 'unit': '℃', 'value': None, 'name': '温度', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_temperature_3', 'unit': '℃', 'value': None, 'name': '温度', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_temperature_4', 'unit': '℃', 'value': None, 'name': '温度', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_temperature_5', 'unit': '℃', 'value': None, 'name': '温度', 'type': '蒸汽需求'},
    # 流量MAX
    {'column': 'eir_steam_demand_flow_max_1', 'unit': 't/h', 'value': None, 'name': '流量MAX', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_max_2', 'unit': 't/h', 'value': None, 'name': '流量MAX', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_max_3', 'unit': 't/h', 'value': None, 'name': '流量MAX', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_max_4', 'unit': 't/h', 'value': None, 'name': '流量MAX', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_max_5', 'unit': 't/h', 'value': None, 'name': '流量MAX', 'type': '蒸汽需求'},
    # 流量MIN
    {'column': 'eir_steam_demand_flow_min_1', 'unit': 't/h', 'value': None, 'name': '流量MIN', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_min_2', 'unit': 't/h', 'value': None, 'name': '流量MIN', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_min_3', 'unit': 't/h', 'value': None, 'name': '流量MIN', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_min_4', 'unit': 't/h', 'value': None, 'name': '流量MIN', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_min_5', 'unit': 't/h', 'value': None, 'name': '流量MIN', 'type': '蒸汽需求'},
    # index=20
    # 流量RATED
    {'column': 'eir_steam_demand_flow_rated_1', 'unit': 't/h', 'value': None, 'name': '流量RATED', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_rated_2', 'unit': 't/h', 'value': None, 'name': '流量RATED', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_rated_3', 'unit': 't/h', 'value': None, 'name': '流量RATED', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_rated_4', 'unit': 't/h', 'value': None, 'name': '流量RATED', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_rated_5', 'unit': 't/h', 'value': None, 'name': '流量RATED', 'type': '蒸汽需求'},
    # 凝结水回收率
    {'column': 'eir_steam_demand_condensate_recovery_percentage_1', 'unit': '%', 'value': None, 'name': '凝结水回收率', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_condensate_recovery_percentage_2', 'unit': '%', 'value': None, 'name': '凝结水回收率', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_condensate_recovery_percentage_3', 'unit': '%', 'value': None, 'name': '凝结水回收率', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_condensate_recovery_percentage_4', 'unit': '%', 'value': None, 'name': '凝结水回收率', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_condensate_recovery_percentage_5', 'unit': '%', 'value': None, 'name': '凝结水回收率', 'type': '蒸汽需求'},
    # 总计
    {'column': 'eir_steam_demand_total_1', 'unit': 't/h', 'value': None, 'name': '总计', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_total_2', 'unit': 't/h', 'value': None, 'name': '总计', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_total_3', 'unit': 't/h', 'value': None, 'name': '总计', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_total_4', 'unit': 't/h', 'value': None, 'name': '总计', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_total_5', 'unit': 't/h', 'value': None, 'name': '总计', 'type': '蒸汽需求'},
    # 回水水质
    {'column': 'eir_steam_demand_backwater_quality_1', 'unit': '', 'value': None, 'name': '回水水质', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_backwater_quality_2', 'unit': '', 'value': None, 'name': '回水水质', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_backwater_quality_3', 'unit': '', 'value': None, 'name': '回水水质', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_backwater_quality_4', 'unit': '', 'value': None, 'name': '回水水质', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_backwater_quality_5', 'unit': '', 'value': None, 'name': '回水水质', 'type': '蒸汽需求'},
    # index=40
    # 各个时间点的流量
    {'column': 'eir_steam_demand_flow_0_1_day_1', 'unit': 't', 'value': None, 'name': '0:00—1:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_1_2_day_1', 'unit': 't', 'value': None, 'name': '1:00—2:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_2_3_day_1', 'unit': 't', 'value': None, 'name': '2:00—3:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_3_4_day_1', 'unit': 't', 'value': None, 'name': '3:00—4:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_4_5_day_1', 'unit': 't', 'value': None, 'name': '4:00—5:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_5_6_day_1', 'unit': 't', 'value': None, 'name': '5:00—6:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_6_7_day_1', 'unit': 't', 'value': None, 'name': '6:00—7:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_7_8_day_1', 'unit': 't', 'value': None, 'name': '7:00—8:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_8_9_day_1', 'unit': 't', 'value': None, 'name': '8:00—9:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_9_10_day_1', 'unit': 't', 'value': None, 'name': '9:00—10:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_10_11_day_1', 'unit': 't', 'value': None, 'name': '10:00—11:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_11_12_day_1', 'unit': 't', 'value': None, 'name': '11:00—12:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_12_13_day_1', 'unit': 't', 'value': None, 'name': '12:00—13:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_13_14_day_1', 'unit': 't', 'value': None, 'name': '13:00—14:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_14_15_day_1', 'unit': 't', 'value': None, 'name': '14:00—15:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_15_16_day_1', 'unit': 't', 'value': None, 'name': '15:00—16:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_16_17_day_1', 'unit': 't', 'value': None, 'name': '16:00—17:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_17_18_day_1', 'unit': 't', 'value': None, 'name': '17:00—18:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_18_19_day_1', 'unit': 't', 'value': None, 'name': '19:00—19:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_19_20_day_1', 'unit': 't', 'value': None, 'name': '19:00—20:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_20_21_day_1', 'unit': 't', 'value': None, 'name': '20:00—21:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_21_22_day_1', 'unit': 't', 'value': None, 'name': '21:00—22:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_22_23_day_1', 'unit': 't', 'value': None, 'name': '22:00—23:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_23_24_day_1', 'unit': 't', 'value': None, 'name': '23:00—24:00', 'type': '蒸汽需求'},

    {'column': 'eir_steam_demand_flow_0_1_day_2', 'unit': 't', 'value': None, 'name': '0:00—1:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_1_2_day_2', 'unit': 't', 'value': None, 'name': '1:00—2:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_2_3_day_2', 'unit': 't', 'value': None, 'name': '2:00—3:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_3_4_day_2', 'unit': 't', 'value': None, 'name': '3:00—4:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_4_5_day_2', 'unit': 't', 'value': None, 'name': '4:00—5:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_5_6_day_2', 'unit': 't', 'value': None, 'name': '5:00—6:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_6_7_day_2', 'unit': 't', 'value': None, 'name': '6:00—7:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_7_8_day_2', 'unit': 't', 'value': None, 'name': '7:00—8:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_8_9_day_2', 'unit': 't', 'value': None, 'name': '8:00—9:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_9_10_day_2', 'unit': 't', 'value': None, 'name': '9:00—10:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_10_11_day_2', 'unit': 't', 'value': None, 'name': '10:00—11:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_11_12_day_2', 'unit': 't', 'value': None, 'name': '11:00—12:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_12_13_day_2', 'unit': 't', 'value': None, 'name': '12:00—13:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_13_14_day_2', 'unit': 't', 'value': None, 'name': '13:00—14:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_14_15_day_2', 'unit': 't', 'value': None, 'name': '14:00—15:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_15_16_day_2', 'unit': 't', 'value': None, 'name': '15:00—16:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_16_17_day_2', 'unit': 't', 'value': None, 'name': '16:00—17:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_17_18_day_2', 'unit': 't', 'value': None, 'name': '17:00—18:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_18_19_day_2', 'unit': 't', 'value': None, 'name': '19:00—19:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_19_20_day_2', 'unit': 't', 'value': None, 'name': '19:00—20:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_20_21_day_2', 'unit': 't', 'value': None, 'name': '20:00—21:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_21_22_day_2', 'unit': 't', 'value': None, 'name': '21:00—22:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_22_23_day_2', 'unit': 't', 'value': None, 'name': '22:00—23:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_23_24_day_2', 'unit': 't', 'value': None, 'name': '23:00—24:00', 'type': '蒸汽需求'},

    {'column': 'eir_steam_demand_flow_0_1_day_3', 'unit': 't', 'value': None, 'name': '0:00—1:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_1_2_day_3', 'unit': 't', 'value': None, 'name': '1:00—2:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_2_3_day_3', 'unit': 't', 'value': None, 'name': '2:00—3:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_3_4_day_3', 'unit': 't', 'value': None, 'name': '3:00—4:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_4_5_day_3', 'unit': 't', 'value': None, 'name': '4:00—5:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_5_6_day_3', 'unit': 't', 'value': None, 'name': '5:00—6:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_6_7_day_3', 'unit': 't', 'value': None, 'name': '6:00—7:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_7_8_day_3', 'unit': 't', 'value': None, 'name': '7:00—8:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_8_9_day_3', 'unit': 't', 'value': None, 'name': '8:00—9:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_9_10_day_3', 'unit': 't', 'value': None, 'name': '9:00—10:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_10_11_day_3', 'unit': 't', 'value': None, 'name': '10:00—11:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_11_12_day_3', 'unit': 't', 'value': None, 'name': '11:00—12:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_12_13_day_3', 'unit': 't', 'value': None, 'name': '12:00—13:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_13_14_day_3', 'unit': 't', 'value': None, 'name': '13:00—14:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_14_15_day_3', 'unit': 't', 'value': None, 'name': '14:00—15:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_15_16_day_3', 'unit': 't', 'value': None, 'name': '15:00—16:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_16_17_day_3', 'unit': 't', 'value': None, 'name': '16:00—17:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_17_18_day_3', 'unit': 't', 'value': None, 'name': '17:00—18:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_18_19_day_3', 'unit': 't', 'value': None, 'name': '19:00—19:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_19_20_day_3', 'unit': 't', 'value': None, 'name': '19:00—20:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_20_21_day_3', 'unit': 't', 'value': None, 'name': '20:00—21:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_21_22_day_3', 'unit': 't', 'value': None, 'name': '21:00—22:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_22_23_day_3', 'unit': 't', 'value': None, 'name': '22:00—23:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_23_24_day_3', 'unit': 't', 'value': None, 'name': '23:00—24:00', 'type': '蒸汽需求'},

    {'column': 'eir_steam_demand_flow_0_1_day_4', 'unit': 't', 'value': None, 'name': '0:00—1:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_1_2_day_4', 'unit': 't', 'value': None, 'name': '1:00—2:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_2_3_day_4', 'unit': 't', 'value': None, 'name': '2:00—3:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_3_4_day_4', 'unit': 't', 'value': None, 'name': '3:00—4:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_4_5_day_4', 'unit': 't', 'value': None, 'name': '4:00—5:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_5_6_day_4', 'unit': 't', 'value': None, 'name': '5:00—6:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_6_7_day_4', 'unit': 't', 'value': None, 'name': '6:00—7:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_7_8_day_4', 'unit': 't', 'value': None, 'name': '7:00—8:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_8_9_day_4', 'unit': 't', 'value': None, 'name': '8:00—9:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_9_10_day_4', 'unit': 't', 'value': None, 'name': '9:00—10:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_10_11_day_4', 'unit': 't', 'value': None, 'name': '10:00—11:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_11_12_day_4', 'unit': 't', 'value': None, 'name': '11:00—12:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_12_13_day_4', 'unit': 't', 'value': None, 'name': '12:00—13:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_13_14_day_4', 'unit': 't', 'value': None, 'name': '13:00—14:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_14_15_day_4', 'unit': 't', 'value': None, 'name': '14:00—15:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_15_16_day_4', 'unit': 't', 'value': None, 'name': '15:00—16:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_16_17_day_4', 'unit': 't', 'value': None, 'name': '16:00—17:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_17_18_day_4', 'unit': 't', 'value': None, 'name': '17:00—18:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_18_19_day_4', 'unit': 't', 'value': None, 'name': '19:00—19:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_19_20_day_4', 'unit': 't', 'value': None, 'name': '19:00—20:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_20_21_day_4', 'unit': 't', 'value': None, 'name': '20:00—21:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_21_22_day_4', 'unit': 't', 'value': None, 'name': '21:00—22:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_22_23_day_4', 'unit': 't', 'value': None, 'name': '22:00—23:00', 'type': '蒸汽需求'},
    {'column': 'eir_steam_demand_flow_23_24_day_4', 'unit': 't', 'value': None, 'name': '23:00—24:00', 'type': '蒸汽需求'}
    # index=64
    # 总计
    # {'column': 'eir_steam_demand_flow_total', 'unit': 't', 'value': None, 'name': '总计', 'type': '蒸汽需求'}
]

list_column_eir_electric = [
    # 电力需求
    # 最大负荷
    {'column': 'eir_power_demand_peak_load', 'unit': 'kW', 'value': None, 'name': '最大负荷', 'type': '电力需求'},
    # 平均负荷
    {'column': 'eir_power_demand_average_load', 'unit': 'kW', 'value': None, 'name': '平均负荷', 'type': '电力需求'},
    # 最小负荷
    {'column': 'eir_power_demand_minimum_load', 'unit': 'kW', 'value': None, 'name': '最小负荷', 'type': '电力需求'},
    # 日用电量
    {'column': 'eir_power_demand_power_consumption_day', 'unit': 'kWh', 'value': None, 'name': '日用电量', 'type': '电力需求'},
    # 年用电量
    {'column': 'eir_power_demand_power_consumption_year', 'unit': '万kWh', 'value': None, 'name': '年用电量', 'type': '电力需求'},
    # index=5
    # 各个时间点的电荷量kWh
    {'column': 'eir_power_demand_quantity_0_1_day_1', 'unit': 'kWh', 'value': None, 'name': '0:00—1:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_1_2_day_1', 'unit': 'kWh', 'value': None, 'name': '1:00—2:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_2_3_day_1', 'unit': 'kWh', 'value': None, 'name': '2:00—3:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_3_4_day_1', 'unit': 'kWh', 'value': None, 'name': '3:00—4:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_4_5_day_1', 'unit': 'kWh', 'value': None, 'name': '4:00—5:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_5_6_day_1', 'unit': 'kWh', 'value': None, 'name': '5:00—6:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_6_7_day_1', 'unit': 'kWh', 'value': None, 'name': '6:00—7:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_7_8_day_1', 'unit': 'kWh', 'value': None, 'name': '7:00—8:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_8_9_day_1', 'unit': 'kWh', 'value': None, 'name': '8:00—9:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_9_10_day_1', 'unit': 'kWh', 'value': None, 'name': '9:00—10:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_10_11_day_1', 'unit': 'kWh', 'value': None, 'name': '10:00—11:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_11_12_day_1', 'unit': 'kWh', 'value': None, 'name': '11:00—12:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_12_13_day_1', 'unit': 'kWh', 'value': None, 'name': '12:00—13:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_13_14_day_1', 'unit': 'kWh', 'value': None, 'name': '13:00—14:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_14_15_day_1', 'unit': 'kWh', 'value': None, 'name': '14:00—15:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_15_16_day_1', 'unit': 'kWh', 'value': None, 'name': '15:00—16:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_16_17_day_1', 'unit': 'kWh', 'value': None, 'name': '16:00—17:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_17_18_day_1', 'unit': 'kWh', 'value': None, 'name': '17:00—18:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_18_19_day_1', 'unit': 'kWh', 'value': None, 'name': '19:00—19:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_19_20_day_1', 'unit': 'kWh', 'value': None, 'name': '19:00—20:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_20_21_day_1', 'unit': 'kWh', 'value': None, 'name': '20:00—21:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_21_22_day_1', 'unit': 'kWh', 'value': None, 'name': '21:00—22:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_22_23_day_1', 'unit': 'kWh', 'value': None, 'name': '22:00—23:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_23_24_day_1', 'unit': 'kWh', 'value': None, 'name': '23:00—24:00', 'type': '电力需求'},

    {'column': 'eir_power_demand_quantity_0_1_day_2', 'unit': 'kWh', 'value': None, 'name': '0:00—1:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_1_2_day_2', 'unit': 'kWh', 'value': None, 'name': '1:00—2:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_2_3_day_2', 'unit': 'kWh', 'value': None, 'name': '2:00—3:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_3_4_day_2', 'unit': 'kWh', 'value': None, 'name': '3:00—4:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_4_5_day_2', 'unit': 'kWh', 'value': None, 'name': '4:00—5:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_5_6_day_2', 'unit': 'kWh', 'value': None, 'name': '5:00—6:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_6_7_day_2', 'unit': 'kWh', 'value': None, 'name': '6:00—7:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_7_8_day_2', 'unit': 'kWh', 'value': None, 'name': '7:00—8:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_8_9_day_2', 'unit': 'kWh', 'value': None, 'name': '8:00—9:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_9_10_day_2', 'unit': 'kWh', 'value': None, 'name': '9:00—10:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_10_11_day_2', 'unit': 'kWh', 'value': None, 'name': '10:00—11:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_11_12_day_2', 'unit': 'kWh', 'value': None, 'name': '11:00—12:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_12_13_day_2', 'unit': 'kWh', 'value': None, 'name': '12:00—13:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_13_14_day_2', 'unit': 'kWh', 'value': None, 'name': '13:00—14:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_14_15_day_2', 'unit': 'kWh', 'value': None, 'name': '14:00—15:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_15_16_day_2', 'unit': 'kWh', 'value': None, 'name': '15:00—16:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_16_17_day_2', 'unit': 'kWh', 'value': None, 'name': '16:00—17:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_17_18_day_2', 'unit': 'kWh', 'value': None, 'name': '17:00—18:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_18_19_day_2', 'unit': 'kWh', 'value': None, 'name': '19:00—19:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_19_20_day_2', 'unit': 'kWh', 'value': None, 'name': '19:00—20:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_20_21_day_2', 'unit': 'kWh', 'value': None, 'name': '20:00—21:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_21_22_day_2', 'unit': 'kWh', 'value': None, 'name': '21:00—22:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_22_23_day_2', 'unit': 'kWh', 'value': None, 'name': '22:00—23:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_23_24_day_2', 'unit': 'kWh', 'value': None, 'name': '23:00—24:00', 'type': '电力需求'},

    {'column': 'eir_power_demand_quantity_0_1_day_3', 'unit': 'kWh', 'value': None, 'name': '0:00—1:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_1_2_day_3', 'unit': 'kWh', 'value': None, 'name': '1:00—2:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_2_3_day_3', 'unit': 'kWh', 'value': None, 'name': '2:00—3:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_3_4_day_3', 'unit': 'kWh', 'value': None, 'name': '3:00—4:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_4_5_day_3', 'unit': 'kWh', 'value': None, 'name': '4:00—5:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_5_6_day_3', 'unit': 'kWh', 'value': None, 'name': '5:00—6:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_6_7_day_3', 'unit': 'kWh', 'value': None, 'name': '6:00—7:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_7_8_day_3', 'unit': 'kWh', 'value': None, 'name': '7:00—8:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_8_9_day_3', 'unit': 'kWh', 'value': None, 'name': '8:00—9:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_9_10_day_3', 'unit': 'kWh', 'value': None, 'name': '9:00—10:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_10_11_day_3', 'unit': 'kWh', 'value': None, 'name': '10:00—11:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_11_12_day_3', 'unit': 'kWh', 'value': None, 'name': '11:00—12:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_12_13_day_3', 'unit': 'kWh', 'value': None, 'name': '12:00—13:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_13_14_day_3', 'unit': 'kWh', 'value': None, 'name': '13:00—14:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_14_15_day_3', 'unit': 'kWh', 'value': None, 'name': '14:00—15:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_15_16_day_3', 'unit': 'kWh', 'value': None, 'name': '15:00—16:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_16_17_day_3', 'unit': 'kWh', 'value': None, 'name': '16:00—17:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_17_18_day_3', 'unit': 'kWh', 'value': None, 'name': '17:00—18:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_18_19_day_3', 'unit': 'kWh', 'value': None, 'name': '19:00—19:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_19_20_day_3', 'unit': 'kWh', 'value': None, 'name': '19:00—20:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_20_21_day_3', 'unit': 'kWh', 'value': None, 'name': '20:00—21:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_21_22_day_3', 'unit': 'kWh', 'value': None, 'name': '21:00—22:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_22_23_day_3', 'unit': 'kWh', 'value': None, 'name': '22:00—23:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_23_24_day_3', 'unit': 'kWh', 'value': None, 'name': '23:00—24:00', 'type': '电力需求'},

    {'column': 'eir_power_demand_quantity_0_1_day_4', 'unit': 'kWh', 'value': None, 'name': '0:00—1:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_1_2_day_4', 'unit': 'kWh', 'value': None, 'name': '1:00—2:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_2_3_day_4', 'unit': 'kWh', 'value': None, 'name': '2:00—3:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_3_4_day_4', 'unit': 'kWh', 'value': None, 'name': '3:00—4:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_4_5_day_4', 'unit': 'kWh', 'value': None, 'name': '4:00—5:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_5_6_day_4', 'unit': 'kWh', 'value': None, 'name': '5:00—6:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_6_7_day_4', 'unit': 'kWh', 'value': None, 'name': '6:00—7:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_7_8_day_4', 'unit': 'kWh', 'value': None, 'name': '7:00—8:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_8_9_day_4', 'unit': 'kWh', 'value': None, 'name': '8:00—9:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_9_10_day_4', 'unit': 'kWh', 'value': None, 'name': '9:00—10:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_10_11_day_4', 'unit': 'kWh', 'value': None, 'name': '10:00—11:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_11_12_day_4', 'unit': 'kWh', 'value': None, 'name': '11:00—12:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_12_13_day_4', 'unit': 'kWh', 'value': None, 'name': '12:00—13:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_13_14_day_4', 'unit': 'kWh', 'value': None, 'name': '13:00—14:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_14_15_day_4', 'unit': 'kWh', 'value': None, 'name': '14:00—15:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_15_16_day_4', 'unit': 'kWh', 'value': None, 'name': '15:00—16:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_16_17_day_4', 'unit': 'kWh', 'value': None, 'name': '16:00—17:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_17_18_day_4', 'unit': 'kWh', 'value': None, 'name': '17:00—18:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_18_19_day_4', 'unit': 'kWh', 'value': None, 'name': '19:00—19:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_19_20_day_4', 'unit': 'kWh', 'value': None, 'name': '19:00—20:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_20_21_day_4', 'unit': 'kWh', 'value': None, 'name': '20:00—21:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_21_22_day_4', 'unit': 'kWh', 'value': None, 'name': '21:00—22:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_22_23_day_4', 'unit': 'kWh', 'value': None, 'name': '22:00—23:00', 'type': '电力需求'},
    {'column': 'eir_power_demand_quantity_23_24_day_4', 'unit': 'kWh', 'value': None, 'name': '23:00—24:00', 'type': '电力需求'}
    # index=29
]

list_column_eir_hot_water = [
    # 热水需求
    # 供水温度
    {'column': 'eir_hot_water_demand_supply_water_temperature', 'unit': '℃', 'value': None, 'name': '供水温度', 'type': '热水需求'},
    # 回水温度
    {'column': 'eir_hot_water_demand_return_water_temperature', 'unit': '℃', 'value': None, 'name': '回水温度', 'type': '热水需求'},
    # 小时供水量
    {'column': 'eir_hot_water_demand_supply_water_hour', 'unit': 't/h', 'value': None, 'name': '小时供水量', 'type': '热水需求'},
    # 日供水量
    {'column': 'eir_hot_water_demand_supply_water_day', 'unit': 't/d', 'value': None, 'name': '日供水量', 'type': '热水需求'},
    # 年供水量
    {'column': 'eir_hot_water_demand_supply_water_year', 'unit': 't/a', 'value': None, 'name': '年供水量', 'type': '热水需求'},
    # index=5
    # 各个时间点的热水流量
    {'column': 'eir_hot_water_demand_quantity_0_1_day_1', 'unit': 'm³', 'value': None, 'name': '0:00—1:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_1_2_day_1', 'unit': 'm³', 'value': None, 'name': '1:00—2:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_2_3_day_1', 'unit': 'm³', 'value': None, 'name': '2:00—3:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_3_4_day_1', 'unit': 'm³', 'value': None, 'name': '3:00—4:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_4_5_day_1', 'unit': 'm³', 'value': None, 'name': '4:00—5:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_5_6_day_1', 'unit': 'm³', 'value': None, 'name': '5:00—6:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_6_7_day_1', 'unit': 'm³', 'value': None, 'name': '6:00—7:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_7_8_day_1', 'unit': 'm³', 'value': None, 'name': '7:00—8:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_8_9_day_1', 'unit': 'm³', 'value': None, 'name': '8:00—9:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_9_10_day_1', 'unit': 'm³', 'value': None, 'name': '9:00—10:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_10_11_day_1', 'unit': 'm³', 'value': None, 'name': '10:00—11:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_11_12_day_1', 'unit': 'm³', 'value': None, 'name': '11:00—12:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_12_13_day_1', 'unit': 'm³', 'value': None, 'name': '12:00—13:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_13_14_day_1', 'unit': 'm³', 'value': None, 'name': '13:00—14:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_14_15_day_1', 'unit': 'm³', 'value': None, 'name': '14:00—15:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_15_16_day_1', 'unit': 'm³', 'value': None, 'name': '15:00—16:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_16_17_day_1', 'unit': 'm³', 'value': None, 'name': '16:00—17:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_17_18_day_1', 'unit': 'm³', 'value': None, 'name': '17:00—18:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_18_19_day_1', 'unit': 'm³', 'value': None, 'name': '19:00—19:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_19_20_day_1', 'unit': 'm³', 'value': None, 'name': '19:00—20:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_20_21_day_1', 'unit': 'm³', 'value': None, 'name': '20:00—21:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_21_22_day_1', 'unit': 'm³', 'value': None, 'name': '21:00—22:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_22_23_day_1', 'unit': 'm³', 'value': None, 'name': '22:00—23:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_23_24_day_1', 'unit': 'm³', 'value': None, 'name': '23:00—24:00', 'type': '热水需求'},

    {'column': 'eir_hot_water_demand_quantity_0_1_day_2', 'unit': 'm³', 'value': None, 'name': '0:00—1:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_1_2_day_2', 'unit': 'm³', 'value': None, 'name': '1:00—2:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_2_3_day_2', 'unit': 'm³', 'value': None, 'name': '2:00—3:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_3_4_day_2', 'unit': 'm³', 'value': None, 'name': '3:00—4:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_4_5_day_2', 'unit': 'm³', 'value': None, 'name': '4:00—5:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_5_6_day_2', 'unit': 'm³', 'value': None, 'name': '5:00—6:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_6_7_day_2', 'unit': 'm³', 'value': None, 'name': '6:00—7:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_7_8_day_2', 'unit': 'm³', 'value': None, 'name': '7:00—8:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_8_9_day_2', 'unit': 'm³', 'value': None, 'name': '8:00—9:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_9_10_day_2', 'unit': 'm³', 'value': None, 'name': '9:00—10:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_10_11_day_2', 'unit': 'm³', 'value': None, 'name': '10:00—11:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_11_12_day_2', 'unit': 'm³', 'value': None, 'name': '11:00—12:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_12_13_day_2', 'unit': 'm³', 'value': None, 'name': '12:00—13:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_13_14_day_2', 'unit': 'm³', 'value': None, 'name': '13:00—14:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_14_15_day_2', 'unit': 'm³', 'value': None, 'name': '14:00—15:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_15_16_day_2', 'unit': 'm³', 'value': None, 'name': '15:00—16:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_16_17_day_2', 'unit': 'm³', 'value': None, 'name': '16:00—17:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_17_18_day_2', 'unit': 'm³', 'value': None, 'name': '17:00—18:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_18_19_day_2', 'unit': 'm³', 'value': None, 'name': '19:00—19:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_19_20_day_2', 'unit': 'm³', 'value': None, 'name': '19:00—20:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_20_21_day_2', 'unit': 'm³', 'value': None, 'name': '20:00—21:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_21_22_day_2', 'unit': 'm³', 'value': None, 'name': '21:00—22:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_22_23_day_2', 'unit': 'm³', 'value': None, 'name': '22:00—23:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_23_24_day_2', 'unit': 'm³', 'value': None, 'name': '23:00—24:00', 'type': '热水需求'},

    {'column': 'eir_hot_water_demand_quantity_0_1_day_3', 'unit': 'm³', 'value': None, 'name': '0:00—1:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_1_2_day_3', 'unit': 'm³', 'value': None, 'name': '1:00—2:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_2_3_day_3', 'unit': 'm³', 'value': None, 'name': '2:00—3:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_3_4_day_3', 'unit': 'm³', 'value': None, 'name': '3:00—4:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_4_5_day_3', 'unit': 'm³', 'value': None, 'name': '4:00—5:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_5_6_day_3', 'unit': 'm³', 'value': None, 'name': '5:00—6:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_6_7_day_3', 'unit': 'm³', 'value': None, 'name': '6:00—7:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_7_8_day_3', 'unit': 'm³', 'value': None, 'name': '7:00—8:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_8_9_day_3', 'unit': 'm³', 'value': None, 'name': '8:00—9:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_9_10_day_3', 'unit': 'm³', 'value': None, 'name': '9:00—10:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_10_11_day_3', 'unit': 'm³', 'value': None, 'name': '10:00—11:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_11_12_day_3', 'unit': 'm³', 'value': None, 'name': '11:00—12:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_12_13_day_3', 'unit': 'm³', 'value': None, 'name': '12:00—13:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_13_14_day_3', 'unit': 'm³', 'value': None, 'name': '13:00—14:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_14_15_day_3', 'unit': 'm³', 'value': None, 'name': '14:00—15:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_15_16_day_3', 'unit': 'm³', 'value': None, 'name': '15:00—16:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_16_17_day_3', 'unit': 'm³', 'value': None, 'name': '16:00—17:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_17_18_day_3', 'unit': 'm³', 'value': None, 'name': '17:00—18:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_18_19_day_3', 'unit': 'm³', 'value': None, 'name': '19:00—19:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_19_20_day_3', 'unit': 'm³', 'value': None, 'name': '19:00—20:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_20_21_day_3', 'unit': 'm³', 'value': None, 'name': '20:00—21:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_21_22_day_3', 'unit': 'm³', 'value': None, 'name': '21:00—22:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_22_23_day_3', 'unit': 'm³', 'value': None, 'name': '22:00—23:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_23_24_day_3', 'unit': 'm³', 'value': None, 'name': '23:00—24:00', 'type': '热水需求'},

    {'column': 'eir_hot_water_demand_quantity_0_1_day_4', 'unit': 'm³', 'value': None, 'name': '0:00—1:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_1_2_day_4', 'unit': 'm³', 'value': None, 'name': '1:00—2:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_2_3_day_4', 'unit': 'm³', 'value': None, 'name': '2:00—3:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_3_4_day_4', 'unit': 'm³', 'value': None, 'name': '3:00—4:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_4_5_day_4', 'unit': 'm³', 'value': None, 'name': '4:00—5:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_5_6_day_4', 'unit': 'm³', 'value': None, 'name': '5:00—6:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_6_7_day_4', 'unit': 'm³', 'value': None, 'name': '6:00—7:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_7_8_day_4', 'unit': 'm³', 'value': None, 'name': '7:00—8:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_8_9_day_4', 'unit': 'm³', 'value': None, 'name': '8:00—9:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_9_10_day_4', 'unit': 'm³', 'value': None, 'name': '9:00—10:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_10_11_day_4', 'unit': 'm³', 'value': None, 'name': '10:00—11:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_11_12_day_4', 'unit': 'm³', 'value': None, 'name': '11:00—12:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_12_13_day_4', 'unit': 'm³', 'value': None, 'name': '12:00—13:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_13_14_day_4', 'unit': 'm³', 'value': None, 'name': '13:00—14:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_14_15_day_4', 'unit': 'm³', 'value': None, 'name': '14:00—15:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_15_16_day_4', 'unit': 'm³', 'value': None, 'name': '15:00—16:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_16_17_day_4', 'unit': 'm³', 'value': None, 'name': '16:00—17:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_17_18_day_4', 'unit': 'm³', 'value': None, 'name': '17:00—18:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_18_19_day_4', 'unit': 'm³', 'value': None, 'name': '19:00—19:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_19_20_day_4', 'unit': 'm³', 'value': None, 'name': '19:00—20:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_20_21_day_4', 'unit': 'm³', 'value': None, 'name': '20:00—21:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_21_22_day_4', 'unit': 'm³', 'value': None, 'name': '21:00—22:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_22_23_day_4', 'unit': 'm³', 'value': None, 'name': '22:00—23:00', 'type': '热水需求'},
    {'column': 'eir_hot_water_demand_quantity_23_24_day_4', 'unit': 'm³', 'value': None, 'name': '23:00—24:00', 'type': '热水需求'}
    # index=29
]

list_column_eir_air_supply = [
    # 供气需求
    # 供气类型
    {'column': 'eir_air_supply_demand_technology_type', 'unit': '工艺用气', 'value': None, 'name': '工艺用气', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_meter_type', 'unit': '仪表用气', 'value': None, 'name': '仪表用气', 'type': '供气需求'},
    # 供气压力
    {'column': 'eir_air_supply_demand_technology_pressure', 'unit': 'Mpa', 'value': None, 'name': '供气压力', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_meter_pressure', 'unit': 'Mpa', 'value': None, 'name': '供气压力', 'type': '供气需求'},
    # 供气流量
    {'column': 'eir_air_supply_demand_technology_flow', 'unit': 'Nm³/h', 'value': None, 'name': '供气流量', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_meter_flow', 'unit': 'Nm³/h', 'value': None, 'name': '供气流量', 'type': '供气需求'},
    # index=6
    # 各个时间点的电荷量kWh
    {'column': 'eir_air_supply_demand_quantity_0_1_day_1', 'unit': 'Nm³', 'value': None, 'name': '0:00—1:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_1_2_day_1', 'unit': 'Nm³', 'value': None, 'name': '1:00—2:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_2_3_day_1', 'unit': 'Nm³', 'value': None, 'name': '2:00—3:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_3_4_day_1', 'unit': 'Nm³', 'value': None, 'name': '3:00—4:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_4_5_day_1', 'unit': 'Nm³', 'value': None, 'name': '4:00—5:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_5_6_day_1', 'unit': 'Nm³', 'value': None, 'name': '5:00—6:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_6_7_day_1', 'unit': 'Nm³', 'value': None, 'name': '6:00—7:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_7_8_day_1', 'unit': 'Nm³', 'value': None, 'name': '7:00—8:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_8_9_day_1', 'unit': 'Nm³', 'value': None, 'name': '8:00—9:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_9_10_day_1', 'unit': 'Nm³', 'value': None, 'name': '9:00—10:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_10_11_day_1', 'unit': 'Nm³', 'value': None, 'name': '10:00—11:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_11_12_day_1', 'unit': 'Nm³', 'value': None, 'name': '11:00—12:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_12_13_day_1', 'unit': 'Nm³', 'value': None, 'name': '12:00—13:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_13_14_day_1', 'unit': 'Nm³', 'value': None, 'name': '13:00—14:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_14_15_day_1', 'unit': 'Nm³', 'value': None, 'name': '14:00—15:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_15_16_day_1', 'unit': 'Nm³', 'value': None, 'name': '15:00—16:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_16_17_day_1', 'unit': 'Nm³', 'value': None, 'name': '16:00—17:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_17_18_day_1', 'unit': 'Nm³', 'value': None, 'name': '17:00—18:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_18_19_day_1', 'unit': 'Nm³', 'value': None, 'name': '19:00—19:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_19_20_day_1', 'unit': 'Nm³', 'value': None, 'name': '19:00—20:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_20_21_day_1', 'unit': 'Nm³', 'value': None, 'name': '20:00—21:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_21_22_day_1', 'unit': 'Nm³', 'value': None, 'name': '21:00—22:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_22_23_day_1', 'unit': 'Nm³', 'value': None, 'name': '22:00—23:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_23_24_day_1', 'unit': 'Nm³', 'value': None, 'name': '23:00—24:00', 'type': '供气需求'},

    {'column': 'eir_air_supply_demand_quantity_0_1_day_2', 'unit': 'Nm³', 'value': None, 'name': '0:00—1:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_1_2_day_2', 'unit': 'Nm³', 'value': None, 'name': '1:00—2:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_2_3_day_2', 'unit': 'Nm³', 'value': None, 'name': '2:00—3:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_3_4_day_2', 'unit': 'Nm³', 'value': None, 'name': '3:00—4:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_4_5_day_2', 'unit': 'Nm³', 'value': None, 'name': '4:00—5:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_5_6_day_2', 'unit': 'Nm³', 'value': None, 'name': '5:00—6:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_6_7_day_2', 'unit': 'Nm³', 'value': None, 'name': '6:00—7:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_7_8_day_2', 'unit': 'Nm³', 'value': None, 'name': '7:00—8:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_8_9_day_2', 'unit': 'Nm³', 'value': None, 'name': '8:00—9:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_9_10_day_2', 'unit': 'Nm³', 'value': None, 'name': '9:00—10:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_10_11_day_2', 'unit': 'Nm³', 'value': None, 'name': '10:00—11:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_11_12_day_2', 'unit': 'Nm³', 'value': None, 'name': '11:00—12:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_12_13_day_2', 'unit': 'Nm³', 'value': None, 'name': '12:00—13:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_13_14_day_2', 'unit': 'Nm³', 'value': None, 'name': '13:00—14:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_14_15_day_2', 'unit': 'Nm³', 'value': None, 'name': '14:00—15:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_15_16_day_2', 'unit': 'Nm³', 'value': None, 'name': '15:00—16:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_16_17_day_2', 'unit': 'Nm³', 'value': None, 'name': '16:00—17:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_17_18_day_2', 'unit': 'Nm³', 'value': None, 'name': '17:00—18:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_18_19_day_2', 'unit': 'Nm³', 'value': None, 'name': '19:00—19:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_19_20_day_2', 'unit': 'Nm³', 'value': None, 'name': '19:00—20:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_20_21_day_2', 'unit': 'Nm³', 'value': None, 'name': '20:00—21:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_21_22_day_2', 'unit': 'Nm³', 'value': None, 'name': '21:00—22:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_22_23_day_2', 'unit': 'Nm³', 'value': None, 'name': '22:00—23:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_23_24_day_2', 'unit': 'Nm³', 'value': None, 'name': '23:00—24:00', 'type': '供气需求'},

    {'column': 'eir_air_supply_demand_quantity_0_1_day_3', 'unit': 'Nm³', 'value': None, 'name': '0:00—1:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_1_2_day_3', 'unit': 'Nm³', 'value': None, 'name': '1:00—2:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_2_3_day_3', 'unit': 'Nm³', 'value': None, 'name': '2:00—3:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_3_4_day_3', 'unit': 'Nm³', 'value': None, 'name': '3:00—4:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_4_5_day_3', 'unit': 'Nm³', 'value': None, 'name': '4:00—5:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_5_6_day_3', 'unit': 'Nm³', 'value': None, 'name': '5:00—6:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_6_7_day_3', 'unit': 'Nm³', 'value': None, 'name': '6:00—7:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_7_8_day_3', 'unit': 'Nm³', 'value': None, 'name': '7:00—8:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_8_9_day_3', 'unit': 'Nm³', 'value': None, 'name': '8:00—9:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_9_10_day_3', 'unit': 'Nm³', 'value': None, 'name': '9:00—10:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_10_11_day_3', 'unit': 'Nm³', 'value': None, 'name': '10:00—11:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_11_12_day_3', 'unit': 'Nm³', 'value': None, 'name': '11:00—12:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_12_13_day_3', 'unit': 'Nm³', 'value': None, 'name': '12:00—13:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_13_14_day_3', 'unit': 'Nm³', 'value': None, 'name': '13:00—14:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_14_15_day_3', 'unit': 'Nm³', 'value': None, 'name': '14:00—15:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_15_16_day_3', 'unit': 'Nm³', 'value': None, 'name': '15:00—16:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_16_17_day_3', 'unit': 'Nm³', 'value': None, 'name': '16:00—17:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_17_18_day_3', 'unit': 'Nm³', 'value': None, 'name': '17:00—18:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_18_19_day_3', 'unit': 'Nm³', 'value': None, 'name': '19:00—19:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_19_20_day_3', 'unit': 'Nm³', 'value': None, 'name': '19:00—20:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_20_21_day_3', 'unit': 'Nm³', 'value': None, 'name': '20:00—21:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_21_22_day_3', 'unit': 'Nm³', 'value': None, 'name': '21:00—22:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_22_23_day_3', 'unit': 'Nm³', 'value': None, 'name': '22:00—23:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_23_24_day_3', 'unit': 'Nm³', 'value': None, 'name': '23:00—24:00', 'type': '供气需求'},

    {'column': 'eir_air_supply_demand_quantity_0_1_day_4', 'unit': 'Nm³', 'value': None, 'name': '0:00—1:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_1_2_day_4', 'unit': 'Nm³', 'value': None, 'name': '1:00—2:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_2_3_day_4', 'unit': 'Nm³', 'value': None, 'name': '2:00—3:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_3_4_day_4', 'unit': 'Nm³', 'value': None, 'name': '3:00—4:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_4_5_day_4', 'unit': 'Nm³', 'value': None, 'name': '4:00—5:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_5_6_day_4', 'unit': 'Nm³', 'value': None, 'name': '5:00—6:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_6_7_day_4', 'unit': 'Nm³', 'value': None, 'name': '6:00—7:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_7_8_day_4', 'unit': 'Nm³', 'value': None, 'name': '7:00—8:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_8_9_day_4', 'unit': 'Nm³', 'value': None, 'name': '8:00—9:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_9_10_day_4', 'unit': 'Nm³', 'value': None, 'name': '9:00—10:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_10_11_day_4', 'unit': 'Nm³', 'value': None, 'name': '10:00—11:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_11_12_day_4', 'unit': 'Nm³', 'value': None, 'name': '11:00—12:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_12_13_day_4', 'unit': 'Nm³', 'value': None, 'name': '12:00—13:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_13_14_day_4', 'unit': 'Nm³', 'value': None, 'name': '13:00—14:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_14_15_day_4', 'unit': 'Nm³', 'value': None, 'name': '14:00—15:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_15_16_day_4', 'unit': 'Nm³', 'value': None, 'name': '15:00—16:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_16_17_day_4', 'unit': 'Nm³', 'value': None, 'name': '16:00—17:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_17_18_day_4', 'unit': 'Nm³', 'value': None, 'name': '17:00—18:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_18_19_day_4', 'unit': 'Nm³', 'value': None, 'name': '19:00—19:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_19_20_day_4', 'unit': 'Nm³', 'value': None, 'name': '19:00—20:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_20_21_day_4', 'unit': 'Nm³', 'value': None, 'name': '20:00—21:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_21_22_day_4', 'unit': 'Nm³', 'value': None, 'name': '21:00—22:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_22_23_day_4', 'unit': 'Nm³', 'value': None, 'name': '22:00—23:00', 'type': '供气需求'},
    {'column': 'eir_air_supply_demand_quantity_23_24_day_4', 'unit': 'Nm³', 'value': None, 'name': '23:00—24:00', 'type': '供气需求'}
    # index=30
]

list_column_eir_season_typical_day = [
    {'column': 'eir_season_typical_day_1', 'unit': '工艺用气', 'value': -1, 'name': '典型日1', 'type': '供气需求'},
    {'column': 'eir_season_typical_day_2', 'unit': '工艺用气', 'value': -1, 'name': '典型日2', 'type': '供气需求'},
    {'column': 'eir_season_typical_day_3', 'unit': '工艺用气', 'value': -1, 'name': '典型日3', 'type': '供气需求'},
    {'column': 'eir_season_typical_day_4', 'unit': '工艺用气', 'value': -1, 'name': '典型日4', 'type': '供气需求'}
]

# 选择设备锅炉页面数据
boilerlist11 = []
boilerlist13 = []
boilerlist14 = []
boilerlist15 = []
# boilerlist11.append({'engname': u'', 'name': u'热负荷', 'unit': u'MW', 'remark': u'', 'value': 2})
boilerlist11.append({'engname': u'', 'name': u'热水压力', 'unit': u'Mpa', 'remark': u'0.7/1.0/1.25', 'value': 0.7})
boilerlist11.append({'engname': u'', 'name': u'热水进水温度', 'unit': u'℃', 'remark': u'70', 'value': 70})
boilerlist11.append({'engname': u'', 'name': u'热水出水温度', 'unit': u'℃', 'remark': u'95/115', 'value': 95})
# boilerlist11.append({'engname': u'', 'name': u'进水焓值', 'unit': u'kJ/kg', 'remark': u'', 'value': 1111})
# boilerlist11.append({'engname': u'', 'name': u'出水焓值', 'unit': u'kJ/kg', 'remark': u'', 'value': 1111})
# boilerlist11.append({'engname': u'', 'name': u'热水量', 'unit': u't/h', 'remark': u'', 'value': 1111})
boilerlist11.append({'engname': u'', 'name': u'燃气热值', 'unit': u'KJ/Nm³', 'remark': u'1Kcal=4.182Kj', 'value': 36000})
boilerlist11.append({'engname': u'', 'name': u'锅炉效率', 'unit': u'-', 'remark': u'0.90~0.93', 'value': 0.91})
# boilerlist11.append({'engname': u'', 'name': u'燃气耗量', 'unit': u'Nm³/h', 'remark': u'', 'value': 1111})
# ====================================================
# boilerlist13.append({'engname': u'', 'name': u'天然气流量', 'unit': u'Nm3/h', 'remark': u'', 'value': 1111})
boilerlist13.append({'engname': u'', 'name': u'天然气热值', 'unit': u'kj/Nm3', 'remark': u'', 'value': 40000})
boilerlist13.append({'engname': u'', 'name': u'锅炉热效率', 'unit': u'%', 'remark': u'', 'value': 0.89})
boilerlist13.append({'engname': u'', 'name': u'汽包压力', 'unit': u'Mpa', 'remark': u'', 'value': 1.25})
boilerlist13.append({'engname': u'', 'name': u'过热蒸汽温度', 'unit': u'℃', 'remark': u'', 'value': 230})
# boilerlist13.append({'engname': u'', 'name': u'过热蒸汽焓值', 'unit': u'kJ/kg', 'remark': u'', 'value': 20})
boilerlist13.append({'engname': u'', 'name': u'过量空气系数', 'unit': u'', 'remark': u'', 'value': 1.15})
boilerlist13.append({'engname': u'', 'name': u'空气温度', 'unit': u'℃', 'remark': u'', 'value': 20})
boilerlist13.append({'engname': u'', 'name': u'空气焓值', 'unit': u'kj/Nm3', 'remark': u'', 'value': 25.974})
# boilerlist13.append({'engname': u'', 'name': u'燃烧所需空气量', 'unit': u'Nm3/h', 'remark': u'', 'value': 1111})
boilerlist13.append({'engname': u'', 'name': u'锅炉给水温度', 'unit': u'℃', 'remark': u'', 'value': 20})
# boilerlist13.append({'engname': u'', 'name': u'给水焓值', 'unit': u'kJ/kg', 'remark': u'', 'value': 1111})
boilerlist13.append({'engname': u'', 'name': u'排污率', 'unit': u'%', 'remark': u'', 'value': 0.02})
# boilerlist13.append({'engname': u'', 'name': u'饱和水温度', 'unit': u'℃', 'remark': u'', 'value': 1111})
# boilerlist13.append({'engname': u'', 'name': u'饱和水焓值', 'unit': u'kj/Nm3', 'remark': u'', 'value': 1111})
# boilerlist13.append({'engname': u'', 'name': u'产汽量', 'unit': u't/h', 'remark': u'', 'value': 4})
# ====================================================
# boilerlist14.append({'engname': u'', 'name': u'烟气流量', 'unit': u'kg/h', 'remark': u'', 'value': ''})
# boilerlist14.append({'engname': u'', 'name': u'烟气进口温度', 'unit': u'℃', 'remark': u'', 'value': ''})
boilerlist14.append({'engname': u'', 'name': u'烟气出口温度', 'unit': u'℃', 'remark': u'90~115', 'value': 90})
boilerlist14.append({'engname': u'', 'name': u'烟气比热', 'unit': u'kj/(kg.℃)', 'remark': u'1.1~1.2', 'value': 1.2})
# boilerlist14.append({'engname': u'', 'name': u'烟气热量', 'unit': u'kj', 'remark': u'q=cm（t1-t2）', 'value': 1111})
boilerlist14.append({'engname': u'', 'name': u'热水压力', 'unit': u'Mpa', 'remark': u'0.7/1.0/1.25', 'value': 0.7})
boilerlist14.append({'engname': u'', 'name': u'热水进水温度', 'unit': u'℃', 'remark': u'70', 'value': 70})
boilerlist14.append({'engname': u'', 'name': u'热水出水温度', 'unit': u'℃', 'remark': u'95/115', 'value': 95})
# boilerlist14.append({'engname': u'', 'name': u'进水焓值', 'unit': u'kJ/kg', 'remark': u'', 'value': 1111})
# boilerlist14.append({'engname': u'', 'name': u'出水焓值', 'unit': u'kJ/kg', 'remark': u'', 'value': 1111})
boilerlist14.append({'engname': u'', 'name': u'锅炉效率', 'unit': u'-', 'remark': u'0.90~0.93', 'value': 0.91})
# boilerlist14.append({'engname': u'', 'name': u'热水量', 'unit': u't/h', 'remark': u'', 'value': 1111})
# ====================================================
# boilerlist15.append({'engname': u'', 'name': u'烟气流量', 'unit': u'kg/h', 'remark': u'', 'value': 1111})
# boilerlist15.append({'engname': u'', 'name': u'烟气进口温度', 'unit': u'℃', 'remark': u'', 'value': 1111})
boilerlist15.append({'engname': u'', 'name': u'烟气出口温度', 'unit': u'℃', 'remark': u'90~115', 'value': 90})
boilerlist15.append({'engname': u'', 'name': u'烟气比热', 'unit': u'kj/(kg.℃)', 'remark': u'1.1~1.2', 'value': 1.2})
# boilerlist15.append({'engname': u'', 'name': u'烟气热量', 'unit': u'kj', 'remark': u'q=cm（t1-t2）', 'value': 1111})
boilerlist15.append({'engname': u'', 'name': u'蒸汽压力', 'unit': u'Mpa', 'remark': u'0.4/0.7/1.0/1.25', 'value': 0.4})
boilerlist15.append({'engname': u'', 'name': u'蒸汽温度', 'unit': u'℃', 'remark': u'183/194', 'value': 190})
# boilerlist15.append({'engname': u'', 'name': u'蒸汽焓值', 'unit': u'kJ/kg', 'remark': u'', 'value': 1111})
# boilerlist15.append({'engname': u'', 'name': u'饱和蒸汽温度', 'unit': u'℃', 'remark': u'饱和蒸汽', 'value': 1111})
boilerlist15.append({'engname': u'', 'name': u'给水温度', 'unit': u'℃', 'remark': u'', 'value': 20})
# boilerlist15.append({'engname': u'', 'name': u'给水焓值', 'unit': u'kJ/kg', 'remark': u'', 'value': 1111})
boilerlist15.append({'engname': u'', 'name': u'锅炉热效率', 'unit': u'%', 'remark': u'89~90', 'value': 0.89})
# boilerlist15.append({'engname': u'', 'name': u'产汽量', 'unit': u't/h', 'remark': u'', 'value': 1111})
# ====================================================

list_column_eir_running_param = [
    {'column': '电力容量备用费', 'unit': '元/kW.月', 'value': 12, 'name': '电力容量备用费', 'type': ''},
    {'column': '维修费', 'unit': '%', 'value': 2.5, 'name': '维修费', 'type': ''},
    {'column': '劳动定员', 'unit': '人', 'value': 30, 'name': '劳动定员', 'type': ''},
    {'column': '年人均工资', 'unit': '元/人.年', 'value': 60000, 'name': '年人均工资', 'type': ''},
    {'column': '设备折旧年限', 'unit': '年', 'value': 15, 'name': '设备折旧年限', 'type': ''},
    {'column': '残值率', 'unit': '%', 'value': 5, 'name': '残值率', 'type': ''},
    {'column': '政策补贴', 'unit': '万元', 'value': 12, 'name': '电力容量备用费', 'type': ''},
    {'column': '原有系统成本', 'unit': '万元/a', 'value': '', 'name': '原有系统成本', 'type': ''},
    # {'column': '电力容量备用费', 'unit': '元/kW.月', 'value': -1, 'name': '电力容量备用费', 'type': ''},
    # {'column': '电力容量备用费', 'unit': '元/kW.月', 'value': -1, 'name': '电力容量备用费', 'type': ''}
]

list_column_eir_running_income = [
    {'column': '供电量', 'unit': 'kWh/a', 'value': -1, 'name': '供电量', 'type': ''},
    {'column': '供热量', 'unit': '万GJ/a', 'value': -1, 'name': '供热量', 'type': ''},
    {'column': '供冷量', 'unit': '万GJ/a', 'value': -1, 'name': '供冷量', 'type': ''},
    {'column': '供热水量', 'unit': '万t/a', 'value': -1, 'name': '供热水量', 'type': ''},
    {'column': '供电收入', 'unit': '万元/a', 'value': -1, 'name': '供电收入', 'type': ''},
    {'column': '供热收入', 'unit': '万元/a', 'value': -1, 'name': '供热收入', 'type': ''},
    {'column': '供热水收入', 'unit': '万元/a', 'value': -1, 'name': '供热水收入', 'type': ''},
    {'column': '供冷收入', 'unit': '万元/a', 'value': -1, 'name': '供冷收入', 'type': ''},
    {'column': '政策补贴收入', 'unit': '万元/a', 'value': -1, 'name': '政策补贴收入', 'type': ''},
    {'column': '总计', 'unit': '万元/a', 'value': -1, 'name': '总计', 'type': ''},
]

list_column_eir_running_cost = [
    {'column': '耗气量', 'unit': '万Nm³/a', 'value': -1, 'name': '耗气量', 'type': ''},
    {'column': '耗水量', 'unit': '万t/a', 'value': -1, 'name': '耗水量', 'type': ''},
    {'column': '耗电量', 'unit': '万kwh/a', 'value': -1, 'name': '耗电量', 'type': ''},
    {'column': '耗气成本', 'unit': '万元/a', 'value': -1, 'name': '耗气成本', 'type': ''},
    {'column': '耗水成本', 'unit': '万元/a', 'value': -1, 'name': '耗水成本', 'type': ''},
    {'column': '耗电成本', 'unit': '万元/a', 'value': -1, 'name': '耗电成本', 'type': ''},
    {'column': '人工成本', 'unit': '万元/a', 'value': -1, 'name': '人工成本', 'type': ''},
    {'column': '维修成本', 'unit': '万元/a', 'value': -1, 'name': '维修成本', 'type': ''},
    {'column': '电力容量备用费', 'unit': '万元/a', 'value': -1, 'name': '电力容量备用费', 'type': ''},
    {'column': '总计', 'unit': '万元/a', 'value': -1, 'name': '总计', 'type': ''},
    {'column': '绝对收益', 'unit': '万元/a', 'value': -1, 'name': '绝对收益', 'type': ''},
    # {'column': '原有系统成本', 'unit': '万元/a', 'value': -1, 'name': '原有系统成本', 'type': ''},
    {'column': '相对收益', 'unit': '万元/a', 'value': -1, 'name': '相对收益', 'type': ''}
]


def form_to_dict_list(formestr):
    '''
    将前台的表单转换成为字典list，将中文字符从url编码转换为unicode编码
    '''
    formestrlist = formestr.split("&")
    resultlist = []
    for yr in formestrlist:
        yrlist = yr.split("=")
        resultlist.append({'column_name': urllib.unquote(str(yrlist[0])).decode('utf-8'), 'column_val': yrlist[1]})
    return resultlist


def strtolist(result):
    if result is not None and result != '':
        result = result.split("#")
        del result[0]
    return result


def getstrcolm(obj):
    if obj is None:
        return ""
    if str(type(obj)) == "<type 'str'>":
        return obj
    return str(float('%.2f' % float(obj) if obj is not None else 0.0))


# 格式化数据库取出的值
def format_value(flag, values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if not values or values == "null" or values == "None":
        result = ""
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        result = float(str(float(values)).rstrip('0'))
    else:
        result = values
    return result


def decimal_to_float(value):
    if value:
        return float(value)
    else:
        return 0.0


# 格式化数据库取出的值
def format_value_ccpp(values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if values == "null" or values == "None" or values is None:
        result = ""
    elif str(type(values)) == "<type 'unicode'>":
        result = values
    elif str(type(values)) == "<type 'int'>":
        result = values
    elif str(type(values)) == "<type 'numeric'>":
        result = values
    elif str(type(values)) == "<type 'integer'>":
        result = values
    elif str(type(values)) == "<type 'str'>":
        result = values
    elif abs(values) <= 0.00001:
        result = 0.0
    else:
        # 只有数字类型的需要取出多余的0
        result = float(str(float(values)).rstrip('0'))
        result = float('%.3f' % result)
    return result


class EnergyIslandService():

    def getQuestionnaireDataJson(self, planId):
        '''
        将模型questionnaire中的数据转换为json格式
        '''
        questionnaire = EnergyIslandRequirement.search_requirement_by_plan_id(planId)
        datas = {}
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        plan_name = plan.plan_name

        list_column_questionnaire = self.get_attr_list()
        for collist in list_column_questionnaire:
            for index in range(len(collist)):
                if hasattr(questionnaire, collist[index]):
                    datas[collist[index]] = format_value_ccpp(
                        getattr(questionnaire, collist[index]))
        datas['company_name'] = companyName
        datas['plan_name'] = plan_name
        datas['company_location'] = companyLocation
        datas['planId'] = planId
        datas['eir_work_year_from_month'] = questionnaire.eir_work_year_from
        datas['eir_work_year_to_month'] = questionnaire.eir_work_year_to
        datas['eir_work_day_from_month'] = questionnaire.eir_work_day_from
        datas['eir_work_day_to_month'] = questionnaire.eir_work_day_to
        eir_cost_gas_price_summer_duration = questionnaire.eir_cost_gas_price_summer_duration
        if eir_cost_gas_price_summer_duration is not None:
            eir_cost_gas_price_summer_durationlenth = len(eir_cost_gas_price_summer_duration.split("~"))
            if eir_cost_gas_price_summer_durationlenth == 2:
                datas['eir_cost_gas_price_summer_duration_start_month'] = eir_cost_gas_price_summer_duration.split("~")[0].split(".")[0]
                datas['eir_cost_gas_price_summer_duration_start_day'] = eir_cost_gas_price_summer_duration.split("~")[0].split(".")[1]
                datas['eir_cost_gas_price_summer_duration_end_month'] = eir_cost_gas_price_summer_duration.split("~")[1].split(".")[0]
                datas['eir_cost_gas_price_summer_duration_end_day'] = eir_cost_gas_price_summer_duration.split("~")[1].split(".")[1]

        eir_cost_gas_price_winter_duration = questionnaire.eir_cost_gas_price_winter_duration
        if eir_cost_gas_price_winter_duration is not None:
            eir_cost_gas_price_winter_durationlenth = len(eir_cost_gas_price_winter_duration.split("~"))
            if eir_cost_gas_price_winter_durationlenth == 2:
                datas['eir_cost_gas_price_winter_duration_start_month'] = eir_cost_gas_price_winter_duration.split("~")[0].split(".")[0]
                datas['eir_cost_gas_price_winter_duration_start_day'] = eir_cost_gas_price_winter_duration.split("~")[0].split(".")[1]
                datas['eir_cost_gas_price_winter_duration_end_month'] = eir_cost_gas_price_winter_duration.split("~")[1].split(".")[0]
                datas['eir_cost_gas_price_winter_duration_end_day'] = eir_cost_gas_price_winter_duration.split("~")[1].split(".")[1]

        if questionnaire.eir_work_cool_from is not None:
            datas['eir_work_cool_from_month'] = questionnaire.eir_work_cool_from.split(".")[0]
            datas['eir_work_cool_from_day'] = questionnaire.eir_work_cool_from.split(".")[1]
        if questionnaire.eir_work_heat_from is not None:
            datas['eir_work_heat_from_month'] = questionnaire.eir_work_heat_from.split(".")[0]
            datas['eir_work_heat_from_day'] = questionnaire.eir_work_heat_from.split(".")[1]

        if questionnaire.eir_work_cool_to is not None:
            datas['eir_work_cool_to_month'] = questionnaire.eir_work_cool_to.split(".")[0]
            datas['eir_work_cool_to_day'] = questionnaire.eir_work_cool_to.split(".")[1]
        if questionnaire.eir_work_heat_to is not None:
            datas['eir_work_heat_to_month'] = questionnaire.eir_work_heat_to.split(".")[0]
            datas['eir_work_heat_to_day'] = questionnaire.eir_work_heat_to.split(".")[1]
        return datas

    '''
    创建方案
    '''
    def create_plan(self, companyName, planName, companyLocation, company_lnglat):
        # 新增公司信息
        company = Company.query.filter_by(company_name=companyName).first()
        if not company:
            company = Company()
            company.company_name = companyName
            Company.insert_company(company)
        newCompany = Company.query.filter_by(company_name=companyName).first()
        companyId = newCompany.id
        # 创建方案
        plan = Plan.query.filter_by(
            company_id=companyId, module_id=Module.energyIsland, plan_name=planName).first()
        if not plan:
            plan = Plan()
            plan.plan_name = planName
            plan.user_id = current_user.id
            plan.company_id = companyId
            plan.module_id = Module.energyIsland
            plan.plan_create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            plan.plan_update_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            plan.company_lnglat = company_lnglat
            Plan.insert_plan(plan)
        plan.company_location = companyLocation
        newPlan = Plan.query.filter_by(
            company_id=companyId, module_id=Module.energyIsland, plan_name=planName).first()
        return newPlan.id

    def get_list_eir_work(self):
        return list_column_eir_work

    def get_list_eir_cost(self):
        return list_column_eir_cost

    def get_list_eir_available(self):
        return list_column_eir_available

    def get_list_eir_available_2(self):
        return list_column_eir_available_2

    def get_list_eir_heat(self):
        return list_column_eir_heat

    def get_list_eir_cool(self):
        return list_column_eir_cool

    def get_list_eir_steam(self):
        return list_column_eir_steam

    def get_list_eir_electric(self):
        return list_column_eir_electric

    def get_list_eir_hot_water(self):
        return list_column_eir_hot_water

    def get_list_eir_air_supply(self):
        return list_column_eir_air_supply

    def get_list_eir_season_typical_day(self):
        return list_column_eir_season_typical_day

    def get_list_eir_running_param(self):
        return list_column_eir_running_param

    def get_list_eir_running_cost(self):
        return list_column_eir_running_cost

    def get_list_eir_running_income(self):
        return list_column_eir_running_income

    def get_list_time(self):
        time_list = []
        for i in range(0, 25):
            if i <= 9:
                time_list.append('0' + str(i) + ':00')
            else:
                time_list.append(str(i) + ':00')
        return time_list

    def get_list_month(self):
        time_list = []
        for i in range(0, 12):
            time_list.append(str(i + 1) + '月')
        return time_list

    def add_value_constant_list(self, energy_island_requirement):
        attr_column_list = self.get_attr_list()
        attr_list = [
            list_column_eir_work, list_column_eir_cost, list_column_eir_available, list_column_eir_available,
            list_column_eir_available, list_column_eir_available, list_column_eir_available,
            list_column_eir_available_2, list_column_eir_heat, list_column_eir_cool,
            list_column_eir_steam, list_column_eir_electric, list_column_eir_hot_water, list_column_eir_air_supply,
            list_column_eir_season_typical_day
        ]
        for sub_list in attr_column_list:
            index_out = attr_column_list.index(sub_list)
            for item in sub_list:
                index_in = sub_list.index(item)
                if index_out == 5:
                    pass
                elif index_out == 6:
                    pass
                else:
                    if index_out == 3:
                        index_in = index_in + 28
                    elif index_out == 4:
                        index_in = index_in + 71
                    if index_out == 1:
                        item_value = getattr(energy_island_requirement, item + '_value')
                    else:
                        item_value = getattr(energy_island_requirement, item)
                    if item_value is not None:
                        attr_list[index_out][index_in]['value'] = item_value
                    else:
                        attr_list[index_out][index_in]['value'] = ''
        return

    def get_attr_list(self):
        '''
        获取调查表model的属性list
        '''
        attr_list = []
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_work[:7])))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_cost[6:])))

        attr_list.append(list(map(lambda x: x['column'], list_column_eir_available[:27:1])))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_available[28:70:1])))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_available[71:93:1])))

        attr_list.append(list(map(lambda x: x['column'], list_column_eir_available[27])))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_available[70])))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_available_2)))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_heat)))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_cool)))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_steam)))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_electric)))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_hot_water)))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_air_supply)))
        attr_list.append(list(map(lambda x: x['column'], list_column_eir_season_typical_day)))

        attr_list.append(['eir_available_steam_boiler_fuel_1_unit', 'eir_available_steam_boiler_fuel_2_unit',
                          'eir_available_own_water_boiler_fuel_1_unit', 'eir_available_own_water_boiler_fuel_2_unit',
                          'eir_proj_type', 'eir_proj_photovoltaic_type', 'type_wind_power', 'eir_proj_terrestrial_heat_hdr_type',
                          'eir_proj_weather_conditions', 'eir_proj_water_quality_condition', 'eir_cost_industry_water_price_value',
                          'eir_cost_domestic_water_price_value', 'eir_cost_heat_price_value', 'eir_cost_steam_price_value',
                          'eir_cost_sewage_price_value', 'eir_cost_subsidy_value', 'eir_cost_electrovalence_peak_duration',
                          'eir_cost_electrovalence_peak_value', 'eir_cost_electrovalence_average_duration', 'eir_cost_electrovalence_average_value',
                          'eir_cost_electrovalence_valley_duration', 'eir_cost_electrovalence_valley_value', 'eir_cost_electrovalence_spike_value',
                          'eir_cost_gas_price_winter_value', 'eir_cost_gas_price_summer_value', 'eir_cost_electrovalence_spike_duration', 'eir_work_cool',
                          'eir_work_heat'])
        return attr_list

    def save_questionnaire(self, planId, form):
        attr_list = self.get_attr_list()
        energy_island_requirement = EnergyIslandRequirement.search_requirement_by_plan_id(planId)
        if energy_island_requirement is None:
            energy_island_requirement = EnergyIslandRequirement()
            energy_island_requirement.plan_id = planId
        for sub_list in attr_list:
            for item in sub_list:
                if form.get(item) != '':
                    setattr(energy_island_requirement, item, form.get(item))
                else:
                    setattr(energy_island_requirement, item, None)
        # self.setcolumndb(energy_island_requirement, 'eir_work_year_from', form.get('eir_work_year_from_month'))
        # self.setcolumndb(energy_island_requirement, 'eir_work_year_to', form.get('eir_work_year_to_month'))
        # self.setcolumndb(energy_island_requirement, 'eir_work_day_from', form.get('eir_work_day_from_month'))
        # self.setcolumndb(energy_island_requirement, 'eir_work_day_to', form.get('eir_work_day_to_month'))
        self.set_price_duration(form, energy_island_requirement, list_column_eir_cost[0:6])
        self.set_work_duration(form, energy_island_requirement, list_column_eir_work[7:9])
        # requirement = EnergyIslandRequirement.query.filter(EnergyIslandRequirement.id == 3).all()[0]
        # arr = self.model_transform_curve(requirement)
        # self.add_value_constant_list(requirement)
        EnergyIslandRequirement.insert_requirement(energy_island_requirement)
        return

    def setcolumndb(self, energy_island_requirement, dbstr, formstr):
        if formstr != '':
            setattr(energy_island_requirement, dbstr, formstr)
        else:
            setattr(energy_island_requirement, dbstr, None)

    def set_work_duration(self, form, energy_island_requirement, list_work):
        '''
        生产信息的时段数据写入model
        '''
        for name in list(map(lambda x: x['column'], list_work[:4])):
            start = form.get(name + '_from_month') + '.' + form.get(name + '_from_day')
            end = form.get(name + '_to_month') + '.' + form.get(name + '_to_day')
            if start != '':
                setattr(energy_island_requirement, name + '_from', start)
            else:
                setattr(energy_island_requirement, name + '_from', None)
            if end != '':
                setattr(energy_island_requirement, name + '_to', end)
            else:
                setattr(energy_island_requirement, name + '_to', None)
            if form.get(name) != '':
                setattr(energy_island_requirement, name, form.get(name))
            else:
                setattr(energy_island_requirement, name, None)
        return energy_island_requirement

    def set_price_duration(self, form, energy_island_requirement, list_time_duration):
        '''
        电价与对应时段写入model，时段的起始以"~"分隔
        '''
        for name in list(map(lambda x: x['column'], list_time_duration[:4])):
            if form.get(name + '_duration') != '':
                setattr(energy_island_requirement, name + '_duration', form.get(name + '_duration'))
            else:
                setattr(energy_island_requirement, name + '_duration', None)
            if form.get(name + '_value') != '':
                setattr(energy_island_requirement, name + '_value', form.get(name + '_value'))
            else:
                setattr(energy_island_requirement, name + '_value', None)
        for name in list(map(lambda x: x['column'], list_time_duration[4:6])):
            start = form.get(name + '_duration_start_month') + '.' + form.get(name + '_duration_start_day')
            end = form.get(name + '_duration_end_month') + '.' + form.get(name + '_duration_end_day')
            setattr(energy_island_requirement, name + '_duration', start + '~' + end)
            if form.get(name + '_value') != '':
                setattr(energy_island_requirement, name + '_value', form.get(name + '_value'))
            else:
                setattr(energy_island_requirement, name + '_value', None)
        return energy_island_requirement

    def get_work_duration(self, data_json, energy_island_requirement, list_work):
        '''
        生产信息的时段数据写入model
        '''
        for name in list(map(lambda x: x['column'], list_work[:4])):
            data_from = getattr(energy_island_requirement, name + '_from')
            data_to = getattr(energy_island_requirement, name + '_to')
            if data_from:
                data_json[name + '_from_month'] = data_from.split('.')[0]
                data_json[name + '_from_day'] = data_from.split('.')[1]
            else:
                data_json[name + '_from_month'] = None
                data_json[name + '_from_day'] = None
            if data_to:
                data_json[name + '_to_month'] = data_to.split('.')[0]
                data_json[name + '_to_day'] = data_to.split('.')[1]
            else:
                data_json[name + '_to_month'] = None
                data_json[name + '_to_day'] = None

    def get_price_duration(self, data_json, energy_island_requirement, list_time_duration):
        '''
        电价与对应时段写入model，时段的起始以"~"分隔
        '''
        for name in list(map(lambda x: x['column'], list_time_duration[:4])):
            duration = getattr(energy_island_requirement, name + '_duration')
            value = getattr(energy_island_requirement, name + '_value')
            data_json[name + '_duration'] = duration
            data_json[name + '_value'] = format_value('number', value)
        for name in list(map(lambda x: x['column'], list_time_duration[4:6])):
            duration_list = getattr(energy_island_requirement, name + '_duration').split('~')
            value = getattr(energy_island_requirement, name + '_value')
            data_json[name + '_duration_start_month'] = duration_list[0].split('.')[0]
            data_json[name + '_duration_start_day'] = duration_list[0].split('.')[1]
            data_json[name + '_duration_end_month'] = duration_list[1].split('.')[0]
            data_json[name + '_duration_end_day'] = duration_list[1].split('.')[1]
            data_json[name + '_value'] = format_value('number', value)
        return energy_island_requirement

    def model_transform(self, plan_id):
        '''
        根据planId获取对应的调查表数据记录
        转换成为算法需要的数据格式
        '''
        requirement = {
            # u'风电曲线': wind_curve,
            # u'负荷曲线': {u'day_1': curve, u'day_2': curve, u'day_3': curve, u'day_4': curve}
        }
        energy_island_requirement = EnergyIslandRequirement.search_requirement_by_plan_id(plan_id)
        requirement[u'电力需求'] = decimal_to_float(energy_island_requirement.eir_power_demand_peak_load)
        requirement[u'热负荷'] = decimal_to_float(energy_island_requirement.eir_thermal_load_total)
        requirement[u'冷负荷'] = decimal_to_float(energy_island_requirement.eir_cooling_load_total)
        requirement[u'蒸汽需求'] = None if not energy_island_requirement.eir_steam_demand_pressure_1 else {
            u'压力': decimal_to_float(energy_island_requirement.eir_steam_demand_pressure_1),
            u'温度': decimal_to_float(energy_island_requirement.eir_steam_demand_temperature_1),
            u'总计': decimal_to_float(energy_island_requirement.eir_steam_demand_total_1),
        }
        requirement[u'热水需求'] = None if not energy_island_requirement.eir_hot_water_demand_supply_water_temperature else {
            u'供水温度': decimal_to_float(energy_island_requirement.eir_hot_water_demand_supply_water_temperature),
            u'回水温度': decimal_to_float(energy_island_requirement.eir_hot_water_demand_return_water_temperature),
            u'流量': decimal_to_float(energy_island_requirement.eir_hot_water_demand_supply_water_hour)
        }
        requirement[u'供气需求'] = None if not energy_island_requirement.eir_air_supply_demand_technology_pressure else {
            u'压力': decimal_to_float(energy_island_requirement.eir_air_supply_demand_technology_pressure),
            u'温度': None,
            u'流量': decimal_to_float(energy_island_requirement.eir_air_supply_demand_technology_flow),
            u'冷却类型': 1
        }
        # TODO
        requirement[u'热泵'] = False
        requirement[u'蓄能'] = None
        requirement[u'光伏'] = self.get_photovoltaic_data(energy_island_requirement, plan_id)
        requirement[u'风电'] = None
        requirement[u'外部资源'] = self.get_out_resource(energy_island_requirement)
        requirement[u'已有电力需求'] = 0
        requirement[u'已有热负荷'] = 0
        requirement[u'天然气耗量(冷)'] = None
        requirement[u'天然气耗量(热)'] = None
        price_array = self.model_transform_get_price(energy_island_requirement)
        requirement[u'价格-夏'] = price_array['price_summer']
        requirement[u'价格-冬'] = price_array['price_winter']
        requirement[u'风电曲线'] = None
        requirement[u'负荷曲线'] = self.model_transform_curve(energy_island_requirement)
        requirement[u'典型日季节'] = self.get_season_typical_day(energy_island_requirement)
        return requirement

    def getselectdeviceboilerdata(self):
        return boilerlist11, boilerlist13, boilerlist14, boilerlist15

    '''
        设备列表device_select_list1:
        [u'\u84b8\u6c7d', u'\u4f9b\u70ed'](设备名称)

        设备列表device_select_list2:
        [{'divice_class':1, (按照excle顺序编号)
        'divice_type':[]
        },
        {'divice_class':2,
        'divice_type':[]
        },
        {'divice_class':8,
        'divice_type':
                        [{'modelnum':1, (按照excle顺序编号由上到下)
                         'modelnumvalue':[{'comname':'热负荷', 'comvalue':'12.68'},
                                          {'comname':'热负荷', 'comvalue':'12.68'},]},
                        {'modelnum':2,
                         'modelnumvalue':[{'comname':'热负荷', 'comvalue':'12.68'},
                                          {'comname':'热负荷', 'comvalue':'12.68'},]},
                        {'modelnum':3,
                         'modelnumvalue':[{'comname':'热负荷', 'comvalue':'12.68'},
                                          {'comname':'热负荷', 'comvalue':'12.68'},]}
                        ]
        },
        {'divice_class':9,
        'divice_type':[]
        },
        ]
    '''

    def createdatatype(self, request):
        device_select_list1 = strtolist(request.values.get('result'))
        # device_select_list1设备列表1的选择数据
        result1 = strtolist(request.values.get('result1'))
        result2 = strtolist(request.values.get('result2'))
        form1list = form_to_dict_list(request.values.get('rsglrqForm'))
        form2list = form_to_dict_list(request.values.get('rqglzqForm'))
        form3list = form_to_dict_list(request.values.get('yrglrsglForm'))
        form4list = form_to_dict_list(request.values.get('yrgldyzqglForm'))
        boilerdatalist = []
        boilerdatalist.append({'modelnum': 1, 'modelnumvalue': form1list}) if u'1' in result2 else ''
        boilerdatalist.append({'modelnum': 2, 'modelnumvalue': form2list}) if u'2' in result2 else ''
        boilerdatalist.append({'modelnum': 3, 'modelnumvalue': form3list}) if u'3' in result2 else ''
        boilerdatalist.append({'modelnum': 4, 'modelnumvalue': form4list}) if u'4' in result2 else ''
        device_select_list2 = []
        # 设备列表2的所有数据
        for re in result1:
            if re == "8":
                device_select_list2.append({'device_class': re, 'device_type': boilerdatalist})
            else:
                device_select_list2.append({'device_class': re, 'device_type': []})
        print(device_select_list1)
        print(device_select_list2)
        return device_select_list1, device_select_list2

    def get_checked_device(self, algo_out_resource_detail, algo_used_devices):
        checked_device_dict = {}
        used_devices_class = []
        used_devices_boiler = []
        if algo_out_resource_detail and algo_out_resource_detail['steam'] and algo_out_resource_detail['steam'][u'自有蒸汽锅炉']:
            used = algo_out_resource_detail['steam'][u'自有蒸汽锅炉']
        else:
            used = 0
        checked_device_dict[u'自有蒸汽锅炉'] = used
        if algo_out_resource_detail and algo_out_resource_detail['steam'] and algo_out_resource_detail['steam'][u'外部汽源']:
            used = algo_out_resource_detail['steam'][u'外部汽源']
        else:
            used = 0
        checked_device_dict[u'外部汽源'] = used
        if algo_out_resource_detail and algo_out_resource_detail['hot_water'] and algo_out_resource_detail['hot_water'][u'空压站余热利用']:
            used = algo_out_resource_detail['hot_water'][u'空压站余热利用']
        else:
            used = 0
        checked_device_dict[u'空压站余热利用'] = used
        if algo_out_resource_detail and algo_out_resource_detail['air'] and algo_out_resource_detail['air'][u'空压站']:
            used = algo_out_resource_detail['air'][u'空压站']
        else:
            used = 0
        checked_device_dict[u'空压站'] = used
        if algo_out_resource_detail and algo_out_resource_detail['cool'] and algo_out_resource_detail['cool'][u'现有制冷设备']:
            used = algo_out_resource_detail['cool'][u'现有制冷设备']
        else:
            used = 0
        checked_device_dict[u'现有制冷设备'] = used
        if algo_out_resource_detail and algo_out_resource_detail['heat'] and algo_out_resource_detail['heat'][u'外部供热设备']:
            used = algo_out_resource_detail['heat'][u'外部供热设备']
        else:
            used = 0
        checked_device_dict[u'外部供热设备'] = used
        if algo_out_resource_detail and algo_out_resource_detail['hot_water'] and algo_out_resource_detail['hot_water'][u'自有热水锅炉']:
            used = algo_out_resource_detail['hot_water'][u'自有热水锅炉']
        else:
            used = 0
        checked_device_dict[u'自有热水锅炉'] = used
        if algo_used_devices:
            used_devices_class = list(map(lambda x: x['device_class'], algo_used_devices))
            for device in algo_used_devices:
                if device['device_class'] == '8':
                    for boiler in device['device_type']:
                        boiler_dict = {}
                        boiler_dict['modelnum'] = boiler[u'modelnum']
                        boiler_modelnumvalue = []
                        for row in boiler[u'modelnumvalue']:
                            boiler_modelnumvalue_dict = {}
                            boiler_modelnumvalue_dict['name'] = row[u'column_name']
                            boiler_modelnumvalue_dict['value'] = str(row[u'column_val'])
                            boiler_modelnumvalue.append(boiler_modelnumvalue_dict)
                        boiler_dict['modelnumvalue'] = boiler_modelnumvalue
                        used_devices_boiler.append(boiler_dict)
        return {'out_resource': checked_device_dict, 'device': used_devices_class, 'boiler': used_devices_boiler}

    def get_select_device_data(self, requirement):
        out_resource_detail_list = []
        out_resource_detail_list.append({'name': u'自有蒸汽锅炉',
                                         'para': u'台数：' + getstrcolm(requirement[u'外部资源'][u'自有蒸汽锅炉'][u'数量']) +
                                                 u'，规模：' + getstrcolm(requirement[u'外部资源'][u'自有蒸汽锅炉'][u'流量']) +
                                                 u'，温度：' + getstrcolm(requirement[u'外部资源'][u'自有蒸汽锅炉'][u'温度']) +
                                                 u'，压力：' + getstrcolm(requirement[u'外部资源'][u'自有蒸汽锅炉'][u'温度']) +
                                                 u'，给水温度：' + getstrcolm(requirement[u'外部资源'][u'自有蒸汽锅炉'][u'给水温度']) +
                                                 u'，燃料：' + getstrcolm(requirement[u'外部资源'][u'自有蒸汽锅炉'][u'燃料'])})

        out_resource_detail_list.append({'name': u'外部汽源',
                                         'para': u'台数：' + getstrcolm(requirement[u'外部资源'][u'外部汽源'][u'数量']) +
                                                 u'，规模：' + getstrcolm(requirement[u'外部资源'][u'外部汽源'][u'流量']) +
                                                 u'，温度：' + getstrcolm(requirement[u'外部资源'][u'外部汽源'][u'温度']) +
                                                 u'，压力：' + getstrcolm(requirement[u'外部资源'][u'外部汽源'][u'压力']) +
                                                 u'，回水温度' + getstrcolm(requirement[u'外部资源'][u'外部汽源'][u'回水温度'])})

        out_resource_detail_list.append({'name': u'自有热水锅炉',
                                         'para': u'台数：' + getstrcolm(requirement[u'外部资源'][u'自有热水锅炉'][u'数量']) +
                                                 u'，规模：' + getstrcolm(requirement[u'外部资源'][u'自有热水锅炉'][u'流量']) +
                                                 u'，温度：' + getstrcolm(requirement[u'外部资源'][u'自有热水锅炉'][u'温度']) +
                                                 u'，压力：' + getstrcolm(requirement[u'外部资源'][u'自有热水锅炉'][u'压力']) +
                                                 u'，回水温度' + getstrcolm(requirement[u'外部资源'][u'自有热水锅炉'][u'回水温度']) +
                                                 u'，燃料：' + getstrcolm(requirement[u'外部资源'][u'自有热水锅炉'][u'燃料'])})

        out_resource_detail_list.append({'name': u'外部供热设备',
                                         'para': u'台数：' + getstrcolm(requirement[u'外部资源'][u'外部供热设备'][u'数量']) +
                                                 u'，规模：' + getstrcolm(requirement[u'外部资源'][u'外部供热设备'][u'流量']) +
                                                 u'，温度：' + getstrcolm(requirement[u'外部资源'][u'外部供热设备'][u'温度']) +
                                                 u'，压力：' + getstrcolm(requirement[u'外部资源'][u'外部供热设备'][u'压力']) +
                                                 u'，回水温度' + getstrcolm(requirement[u'外部资源'][u'外部供热设备'][u'回水温度'])})

        out_resource_detail_list.append({'name': u'现有制冷设备',
                                         'para': u'冷功率：' + getstrcolm(requirement[u'外部资源'][u'现有制冷设备'][u'冷功率']) +
                                                 u'，数量：' + getstrcolm(requirement[u'外部资源'][u'现有制冷设备'][u'数量']) +
                                                 u'，设备类型：' + getstrcolm(requirement[u'外部资源'][u'现有制冷设备'][u'设备类型']) +
                                                 u'，电功率：' + getstrcolm(requirement[u'外部资源'][u'现有制冷设备'][u'电功率'])})

        out_resource_detail_list.append({'name': u'空压站',
                                         'para': u'流量1：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'流量']) +
                                                 u'，压力1：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'压力']) +
                                                 u'，数量1：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'数量']) +
                                                 u'，流量2：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'流量2']) +
                                                 u'，压力2：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'压力2']) +
                                                 u'，数量2：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'数量2']) +
                                                 u'，流量3：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'流量3']) +
                                                 u'，压力3：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'压力3']) +
                                                 u'，数量3：' + getstrcolm(requirement[u'外部资源'][u'空压站'][u'数量3'])})

        out_resource_detail_list.append({'name': u'空压站余热利用',
                                         'para': u'进水温度：' + getstrcolm(requirement[u'外部资源'][u'空压站余热利用'][u'进水温度']) +
                                                 u'，出水温度：' + getstrcolm(requirement[u'外部资源'][u'空压站余热利用'][u'出水温度']) +
                                                 u'，流量：' + getstrcolm(requirement[u'外部资源'][u'空压站余热利用'][u'流量']) +
                                                 u'，回收用途：' + getstrcolm(requirement[u'外部资源'][u'空压站余热利用'][u'回收用途'])})
        return out_resource_detail_list

    def get_need_curve(self, plan_id):
        '''
        前台获取需求曲线数据
        '''
        energy_island_requirement = EnergyIslandRequirement.search_requirement_by_plan_id(plan_id)
        curve_dict = self.model_transform_curve(energy_island_requirement)
        # self.format_curve(energy_island_requirement, 'day_1', curve_dict)
        # self.format_curve(energy_island_requirement, 'day_2', curve_dict)
        # self.format_curve(energy_island_requirement, 'day_3', curve_dict)
        # self.format_curve(energy_island_requirement, 'day_4', curve_dict)
        front_data_day = {u'front_data_day_1': curve_dict['day_1'], u'front_data_day_2': curve_dict['day_2'], u'front_data_day_3': curve_dict['day_3'], u'front_data_day_4': curve_dict['day_4']}
        return front_data_day

    def format_curve(self, energy_island_requirement, typical_day, curve_dict):
        '''
        对曲线进行处理，夏季将热需求置为0，冬季将冷需求置为0
        '''
        season_code = getattr(energy_island_requirement, 'eir_season_typical_' + typical_day)
        if season_code == '1':
            curve_dict[typical_day][u'heat_curve'] = None
        elif season_code == '2':
            curve_dict[typical_day][u'cool_curve'] = None
        else:
            curve_dict = None

    def model_transform_curve(self, energy_island_requirement):
        '''
        获取四个典型日的需求曲线数据
        '''
        if energy_island_requirement.eir_season_typical_day_1 == '-1':
            curve1 = None
        else:
            curve1 = self.model_transform_curve_typical_day(energy_island_requirement, typical_day='1')
        if energy_island_requirement.eir_season_typical_day_2 == '-1':
            curve2 = None
        else:
            curve2 = self.model_transform_curve_typical_day(energy_island_requirement, typical_day='2')
        if energy_island_requirement.eir_season_typical_day_3 == '-1':
            curve3 = None
        else:
            curve3 = self.model_transform_curve_typical_day(energy_island_requirement, typical_day='3')
        if energy_island_requirement.eir_season_typical_day_4 == '-1':
            curve4 = None
        else:
            curve4 = self.model_transform_curve_typical_day(energy_island_requirement, typical_day='4')
        return {u'day_1': curve1, u'day_2': curve2, u'day_3': curve3, u'day_4': curve4}

    def model_transform_curve_typical_day(self, energy_island_requirement, typical_day='1'):
        '''
        解析model，转换成为运行策略使用的数据形式
        获取价格list和各种需求曲线list
        '''
        heat_curve = self.model_transform_get_heat_hour(energy_island_requirement, typical_day)
        cool_curve = self.model_transform_get_cooling_hour(energy_island_requirement, typical_day)
        steam_curve = self.model_transform_get_steam_hour(energy_island_requirement, typical_day)
        electric_curve = self.model_transform_get_electric_hour(energy_island_requirement, typical_day)
        hot_water_curve = self.model_transform_get_hot_water_hour(energy_island_requirement, typical_day)
        air_curve = self.model_transform_get_air_hour(energy_island_requirement)
        curve = {
            u'heat_curve': heat_curve,
            u'cool_curve': cool_curve,
            u'steam_curve': steam_curve,
            u'electric_curve': electric_curve,
            u'hot_water_curve': hot_water_curve,
            u'air_curve': air_curve
        }
        return curve

    def model_transform_get_heat_hour(self, energy_island_requirement, typical_day='1'):
        '''
        各个时间点的热负荷
        '''
        heat_curve = []
        for i in range(0, 24):
            if getattr(energy_island_requirement, 'eir_thermal_load_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day) is None:
                heat_curve = None
                return None
            else:
                heat_curve.append(getattr(energy_island_requirement, 'eir_thermal_load_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day))
        return map(lambda x: float(x) if x else 0, heat_curve)

    def model_transform_get_cooling_hour(self, energy_island_requirement, typical_day='1'):
        '''
        各个时间点的冷负荷
        '''
        cooling_curve = []
        for i in range(0, 24):
            if getattr(energy_island_requirement, 'eir_cooling_load_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day) is None:
                cooling_curve = None
                return None
            else:
                cooling_curve.append(getattr(energy_island_requirement, 'eir_cooling_load_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day))
        return map(lambda x: float(x) if x else 0, cooling_curve)

    def model_transform_get_steam_hour(self, energy_island_requirement, typical_day='1'):
        '''
        各个时间点的蒸汽需求
        '''
        steam_curve = []
        for i in range(0, 24):
            if getattr(energy_island_requirement, 'eir_steam_demand_flow_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day) is None:
                steam_curve = None
                return None
            else:
                steam_curve.append(getattr(energy_island_requirement, 'eir_steam_demand_flow_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day))
        return map(lambda x: float(x) if x else 0, steam_curve)

    def model_transform_get_electric_hour(self, energy_island_requirement, typical_day='1'):
        '''
        各个时间点的电力需求
        '''
        electric_curve = []
        for i in range(0, 24):
            if getattr(energy_island_requirement, 'eir_power_demand_quantity_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day) is None:
                electric_curve = None
                return None
            else:
                electric_curve.append(getattr(energy_island_requirement, 'eir_power_demand_quantity_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day))
        return map(lambda x: float(x) if x else 0, electric_curve)

    def model_transform_get_hot_water_hour(self, energy_island_requirement, typical_day='1'):
        '''
        各个时间点的热水需求
        '''
        hot_water_curve = []
        for i in range(0, 24):
            if getattr(energy_island_requirement, 'eir_hot_water_demand_quantity_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day) is None:
                hot_water_curve = None
                return None
            else:
                hot_water_curve.append(getattr(energy_island_requirement, 'eir_hot_water_demand_quantity_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day))
        return map(lambda x: float(x) if x else 0, hot_water_curve)

    def model_transform_get_air_hour(self, energy_island_requirement, typical_day='1'):
        '''
        各个时间点的供气需求
        '''
        air_curve = []
        for i in range(0, 24):
            if getattr(energy_island_requirement, 'eir_air_supply_demand_quantity_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day) is None:
                air_curve = None
                return None
            else:
                air_curve.append(getattr(energy_island_requirement, 'eir_air_supply_demand_quantity_' + str(i) + '_' + str(i + 1) + '_day_' + typical_day))
        return map(lambda x: float(x) if x else 0, air_curve)

    def model_transform_get_price(self, energy_island_requirement):
        '''
        各个时间段的资源的成本和收入价格
        '''
        price_dict_array_summer = []
        price_dict_array_winter = []
        unit_dict_array = []
        duration_dict_array = []
        peak_duration = [] if energy_island_requirement.eir_cost_electrovalence_peak_duration is None else list(map(lambda x: [float(x[0][:2].rstrip(':')), float(x[1][:2].rstrip(':'))], map(lambda x: x.split('~'), energy_island_requirement.eir_cost_electrovalence_peak_duration.split('/'))))
        average_duration = [] if energy_island_requirement.eir_cost_electrovalence_average_duration is None else list(map(lambda x: [float(x[0][:2].rstrip(':')), float(x[1][:2].rstrip(':'))], map(lambda x: x.split('~'), energy_island_requirement.eir_cost_electrovalence_average_duration.split('/'))))
        valley_duration = [] if energy_island_requirement.eir_cost_electrovalence_valley_duration is None else list(map(lambda x: [float(x[0][:2].rstrip(':')), float(x[1][:2].rstrip(':'))], map(lambda x: x.split('~'), energy_island_requirement.eir_cost_electrovalence_valley_duration.split('/'))))
        spike_duration = [] if energy_island_requirement.eir_cost_electrovalence_spike_duration is None else list(map(lambda x: [float(x[0][:2].rstrip(':')), float(x[1][:2].rstrip(':'))], map(lambda x: x.split('~'), energy_island_requirement.eir_cost_electrovalence_spike_duration.split('/'))))
        duration_arr = [{'key': 'peak', 'value': peak_duration}, {'key': 'average', 'value': average_duration}, {'key': 'valley', 'value': valley_duration}, {'key': 'spike', 'value': spike_duration}]

        for i in range(0, 24):
            price_dict = {'electric': 0, 'gas_winter': 0, 'gas_summer': 0, 'water': 0, 'water_life': 0, 'heat': 0, 'steam': 0, 'sewage': 0, 'subsidy': 0}
            unit_dict = {'electric': None, 'gas_winter': None, 'gas_summer': None, 'water': None, 'water_life': None, 'heat': None, 'steam': None, 'sewage': None, 'subsidy': None}
            duration_dict = {'electric': None, 'gas_winter': None, 'gas_summer': None, 'water': None, 'water_life': None, 'heat': None, 'steam': None, 'sewage': None, 'subsidy': None}
            for sub_duration in duration_arr:
                for duration in sub_duration['value']:
                    if duration[0] <= duration[1]:
                        if i >= duration[0] and i < duration[1]:
                            unit_dict['electric'] = getattr(energy_island_requirement, 'eir_cost_electrovalence_' + sub_duration['key'] + '_unit')
                            duration_dict['electric'] = getattr(energy_island_requirement, 'eir_cost_electrovalence_' + sub_duration['key'] + '_duration')
                            price = getattr(energy_island_requirement, 'eir_cost_electrovalence_' + sub_duration['key'] + '_value')
                            price_dict['electric'] = decimal_to_float(price)
                    else:
                        if (i >= duration[0] and i < 24) or (i >= 0 and i < duration[1]):
                            unit_dict['electric'] = getattr(energy_island_requirement, 'eir_cost_electrovalence_' + sub_duration['key'] + '_unit')
                            duration_dict['electric'] = getattr(energy_island_requirement, 'eir_cost_electrovalence_' + sub_duration['key'] + '_duration')
                            price = getattr(energy_island_requirement, 'eir_cost_electrovalence_' + sub_duration['key'] + '_value')
                            price_dict['electric'] = decimal_to_float(price)
            # 燃气价格
            unit_dict['gas_winter'] = energy_island_requirement.eir_cost_gas_price_winter_unit
            duration_dict['gas_winter'] = energy_island_requirement.eir_cost_gas_price_winter_duration
            price = energy_island_requirement.eir_cost_gas_price_winter_value
            price_dict['gas_winter'] = decimal_to_float(price)
            unit_dict['gas_summer'] = energy_island_requirement.eir_cost_gas_price_summer_unit
            duration_dict['gas_summer'] = energy_island_requirement.eir_cost_gas_price_summer_duration
            price = energy_island_requirement.eir_cost_gas_price_summer_value
            price_dict['gas_summer'] = decimal_to_float(price)
            # 工业水价
            unit_dict['water'] = energy_island_requirement.eir_cost_industry_water_price_unit
            price = energy_island_requirement.eir_cost_industry_water_price_value
            price_dict['water'] = decimal_to_float(price)
            # 生活水价
            unit_dict['water_life'] = energy_island_requirement.eir_cost_domestic_water_price_unit
            price = energy_island_requirement.eir_cost_domestic_water_price_value
            price_dict['water_life'] = decimal_to_float(price)
            # 供暖价格
            unit_dict['heat'] = energy_island_requirement.eir_cost_heat_price_unit
            price = energy_island_requirement.eir_cost_heat_price_value
            price_dict['heat'] = decimal_to_float(price) * 3600. / 10**6
            # 蒸汽价格
            unit_dict['steam'] = energy_island_requirement.eir_cost_steam_price_unit
            price = energy_island_requirement.eir_cost_steam_price_value
            price_dict['steam'] = decimal_to_float(price)
            # 供冷价格
            unit_dict['cool'] = energy_island_requirement.eir_cost_cool_price_unit
            price = energy_island_requirement.eir_cost_cool_price_value
            price_dict['cool'] = decimal_to_float(price) * 3600. / 10**6
            # 热水价格
            unit_dict['hot_water'] = energy_island_requirement.eir_cost_hot_water_price_unit
            price = energy_island_requirement.eir_cost_hot_water_price_value
            price_dict['hot_water'] = decimal_to_float(price)
            # 污水处理价
            unit_dict['sewage'] = energy_island_requirement.eir_cost_sewage_price_unit
            price = energy_island_requirement.eir_cost_sewage_price_value
            price_dict['sewage'] = decimal_to_float(price)
            # 政策补贴
            unit_dict['subsidy'] = energy_island_requirement.eir_cost_subsidy_unit
            price = energy_island_requirement.eir_cost_subsidy_value
            price_dict['subsidy'] = decimal_to_float(price)
            price_dict_summer = copy.deepcopy(price_dict)
            price_dict_summer['gas'] = price_dict_summer['gas_summer']
            price_dict_winter = copy.deepcopy(price_dict)
            price_dict_winter['gas'] = price_dict_winter['gas_winter']
            price_dict_array_summer.append(price_dict_summer)
            price_dict_array_winter.append(price_dict_winter)
            unit_dict_array.append(unit_dict)
            duration_dict_array.append(duration_dict)
        price_array = {'price_summer': price_dict_array_summer, 'price_winter': price_dict_array_winter, 'unit': unit_dict_array, 'duration': duration_dict_array}
        return price_array

    def get_out_resource(self, energy_island_requirement):
        '''
        从model获取外部资源信息
        '''
        # TODO
        out_resource = {
            u'热泵': self.get_heat_pump_data(energy_island_requirement),
            u'外部汽源': {
                u'压力': decimal_to_float(energy_island_requirement.eir_available_external_steam_source_pressure_1_value),
                u'流量': decimal_to_float(energy_island_requirement.eir_available_external_steam_source_scale_1_value),
                u'数量': decimal_to_float(energy_island_requirement.eir_available_external_steam_source_num_1_value),
                u'温度': decimal_to_float(energy_island_requirement.eir_available_external_steam_source_temperature_1_value),
                u'回水温度': decimal_to_float(energy_island_requirement.eir_available_external_steam_source_return_water_temp_1_value)
            },
            u'自有蒸汽锅炉': {
                u'压力': decimal_to_float(energy_island_requirement.eir_available_steam_boiler_pressure_1_value),
                u'流量': decimal_to_float(energy_island_requirement.eir_available_steam_boiler_scale_1_value),
                u'数量': decimal_to_float(energy_island_requirement.eir_available_steam_boiler_num_1_value),
                u'温度': decimal_to_float(energy_island_requirement.eir_available_steam_boiler_temperature_1_value),
                u'给水温度': decimal_to_float(energy_island_requirement.eir_available_steam_boiler_feed_water_temperature_1_value),
                u'燃料': decimal_to_float(energy_island_requirement.eir_available_steam_boiler_fuel_1_value)
            },
            u'自有热水锅炉': {
                u'温度': decimal_to_float(energy_island_requirement.eir_available_own_water_boiler_pressure_1_value),
                u'流量': decimal_to_float(energy_island_requirement.eir_available_own_water_boiler_scale_1_value) / 0.7
                if energy_island_requirement.eir_available_own_water_boiler_scale_1_value else None,
                u'数量': decimal_to_float(energy_island_requirement.eir_available_own_water_boiler_num_1_value),
                u'压力': decimal_to_float(energy_island_requirement.eir_available_own_water_boiler_pressure_1_value),
                u'回水温度': decimal_to_float(energy_island_requirement.eir_available_own_water_boiler_return_water_temperature_1_value),
                u'燃料': decimal_to_float(energy_island_requirement.eir_available_own_water_boiler_fuel_1_value)
            },
            u'外部供热设备': {
                u'温度': decimal_to_float(energy_island_requirement.eir_available_external_heating_pressure_1_value),
                u'流量': decimal_to_float(energy_island_requirement.eir_available_external_heating_scale_1_value / 0.7)
                if energy_island_requirement.eir_available_external_heating_scale_1_value else None,
                u'数量': decimal_to_float(energy_island_requirement.eir_available_external_heating_num_1_value),
                u'压力': decimal_to_float(energy_island_requirement.eir_available_external_heating_pressure_1_value),
                u'回水温度': decimal_to_float(energy_island_requirement.eir_available_external_heating_return_water_temperature_1_value)
            },
            u'现有制冷设备': {
                u'冷功率': decimal_to_float(energy_island_requirement.eir_available_cooling_equipment_1_cool_power),
                u'热功率': decimal_to_float(energy_island_requirement.eir_available_cooling_equipment_1_heat_power),
                u'数量': decimal_to_float(energy_island_requirement.eir_available_cooling_equipment_1_num),
                u'设备类型': decimal_to_float(energy_island_requirement.eir_available_cooling_equipment_1_type),
                u'电功率': decimal_to_float(energy_island_requirement.eir_available_cooling_equipment_1_power)
            },
            u'空压站': {
                u'流量': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_flow_1),
                u'压力': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_pressure_1),
                u'数量': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_num_1),
                u'流量2': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_flow_2),
                u'压力2': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_pressure_2),
                u'数量2': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_num_2),
                u'流量3': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_flow_3),
                u'压力3': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_pressure_3),
                u'数量3': decimal_to_float(energy_island_requirement.eir_available_air_compression_station_num_3)
            },
            u'空压站余热利用': {
                u'进水温度': decimal_to_float(energy_island_requirement.eir_available_air_compression_in_water_temperature),
                u'出水温度': decimal_to_float(energy_island_requirement.eir_available_air_compression_out_water_temperature),
                u'流量': decimal_to_float(energy_island_requirement.eir_available_air_compression_flow),
                u'回收用途': energy_island_requirement.eir_available_air_compression_recovery_usage
            }
        }
        return out_resource

    def get_photovoltaic_data(self, energy_island_requirement, plan_id):
        '''
        从model获取光伏数据
        '''
        # TODO 峰值功率如何计算
        plan = Plan.search_planById(plan_id)
        companyLocation = plan.company_location
        if len(companyLocation) == 0:
            provience = '北京'
        elif len(companyLocation) == 3:
            provience = companyLocation.rstrip(u'市')
        else:
            provience = companyLocation.split(u'省')[0]
        hikari_time = Hikari.query.order_by(Hikari.day.asc()).filter(
            and_(Hikari.province == provience, Hikari.month == 1)
        ).all()
        start_time = str(hikari_time[0].start_hour) + ':' + str(hikari_time[0].start_min)
        end_time = str(hikari_time[0].end_hour) + ':' + str(hikari_time[0].end_min)
        photovoltaic_data = {
            u'名称': energy_island_requirement.eir_available_photovoltaic_name_1,
            u'有效面积㎡': decimal_to_float(energy_island_requirement.eir_available_photovoltaic_area_1),
            u'倾斜角': decimal_to_float(energy_island_requirement.eir_available_photovoltaic_angle_inclination_1),
            u'均布承载力': decimal_to_float(energy_island_requirement.eir_available_photovoltaic_bearing_capacity_1),
            u'峰值功率': 1300,
            u'日出时间': start_time,
            u'日落时间': end_time
        }
        return photovoltaic_data

    def get_heat_pump_data(self, energy_island_requirement):
        '''
        从model获取热泵数据
        '''
        heat_pump = {u'可利用的绿化面积': 0, u'生活污水': 0, u'工业污水': 0, u'类型': -1}
        if energy_island_requirement.eir_proj_terrestrial_heat_hdr_type == '1':
            heat_pump[u'可利用的绿化面积'] = decimal_to_float(energy_island_requirement.eir_available_greening_space)
            heat_pump[u'类型'] = '1'
        elif energy_island_requirement.eir_proj_terrestrial_heat_hdr_type == '2':
            heat_pump[u'生活污水'] = decimal_to_float(energy_island_requirement.eir_available_domestic_sewage_value)
            heat_pump[u'工业污水'] = decimal_to_float(energy_island_requirement.eir_available_industry_sewage_value)
            heat_pump[u'类型'] = '2'
        elif energy_island_requirement.eir_proj_terrestrial_heat_hdr_type == '3':
            heat_pump[u'可利用的绿化面积'] = decimal_to_float(energy_island_requirement.eir_available_greening_space)
            heat_pump[u'类型'] = '3'
        elif energy_island_requirement.eir_proj_terrestrial_heat_hdr_type == '4':
            heat_pump[u'生活污水'] = decimal_to_float(energy_island_requirement.eir_available_domestic_sewage_value)
            heat_pump[u'工业污水'] = decimal_to_float(energy_island_requirement.eir_available_industry_sewage_value)
            heat_pump[u'类型'] = '4'
        else:
            pass
        return heat_pump

    def get_season_typical_day(self, energy_island_requirement):
        '''
        获取典型日曲线对应的季节，确定价格
        '''
        return {
            'day_1': energy_island_requirement.eir_season_typical_day_1,
            'day_2': energy_island_requirement.eir_season_typical_day_2,
            'day_3': energy_island_requirement.eir_season_typical_day_3,
            'day_4': energy_island_requirement.eir_season_typical_day_4
        }

    def get_questionnaire_data_json(self, planId):
        '''
        获取当前planId对应的调查表json数据
        '''
        data_json = {}
        attr_list = self.get_attr_list()
        energy_island_requirement = EnergyIslandRequirement.query.filter(
            or_(
                and_(EnergyIslandRequirement.plan_id == planId)
            )
        ).one_or_none()
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        plan_name = plan.plan_name
        data_json['company_name'] = companyName
        data_json['plan_name'] = plan_name
        data_json['company_location'] = companyLocation
        data_json['planId'] = planId
        if energy_island_requirement is not None:
            self.get_price_duration(data_json, energy_island_requirement, list_column_eir_cost[0:6])
            self.get_work_duration(data_json, energy_island_requirement, list_column_eir_work[7:9])
            for sub_list in attr_list:
                for item in sub_list:
                    data_value = getattr(energy_island_requirement, item)
                    if isinstance(data_value, Decimal):
                        if format_value('number', data_value) != '':
                            data_json[item] = format_value('number', data_value)
                        else:
                            data_json[item] = 0
                    else:
                        data_json[item] = format_value(None, str(getattr(energy_island_requirement, item)))
                # data_json[item] = format_value('number', getattr(energy_island_requirement, item))
        # # requirement = EnergyIslandRequirement.query.filter(EnergyIslandRequirement.id == 3).all()[0]
        # # arr = self.model_transform_curve(requirement)
        # # self.add_value_constant_list(requirement)
        # EnergyIslandRequirement.insert_requirement(energy_island_requirement)
        return data_json

    def save_mark_data(self, planId, request):
        '''
        保存指标数据
        '''
        mark_data = MarkData.query.filter(MarkData.plan_id == planId).one_or_none()
        if not mark_data:
            mark_data = MarkData()
        running_cost_form = form_to_dict_list(request.values.get('running_cost'))
        running_income_form = form_to_dict_list(request.values.get('running_income'))
        running_param_form = form_to_dict_list(request.values.get('running_param'))
        for row in running_cost_form:
            if row['column_name'] == u'耗气量':
                mark_data.col_1_B = row['column_val']
        for row in running_income_form:
            if row['column_name'] == u'供电量':
                mark_data.col_1_W = row['column_val']
                mark_data.col_5_electric = row['column_val']
            if row['column_name'] == u'供热量':
                mark_data.col_1_Q1 = row['column_val']
                mark_data.col_5_heat = row['column_val']
            if row['column_name'] == u'供冷量':
                mark_data.col_1_Q2 = row['column_val']
                mark_data.col_5_cool = row['column_val']
        for row in running_param_form:
            if row['column_name'] == u'耗气量':
                mark_data.col_1_B = row['column_val']
                mark_data.col_5_fuel = row['column_val']
            if row['column_name'] == u'耗电量':
                mark_data.col_2_Pe = row['column_val'] + mark_data.col_1_W
                mark_data.col_3_Pe = row['column_val'] + mark_data.col_1_W
                mark_data.col_4_Pe = row['column_val'] + mark_data.col_1_W
        mark_data.col_2_Qh = 0
        mark_data.col_3_Qh = 0
        mark_data.col_4_Qc = 0
        # 一次能源综合利用率
        mark_data.col_5_buy_electric = 0
        # 热电比
        col_6_heat = db.Column(db.NUMERIC(precision=15, scale=5))
        col_6_electric = db.Column(db.NUMERIC(precision=15, scale=5))
        col_6_heat_electric_ratio = db.Column(db.NUMERIC(precision=15, scale=5))
        return

    # 过滤器
    @staticmethod
    def slice_arr(arr, start, end, delta):
        return arr[int(start):int(end):int(delta)]

    def getDeviceList(self, device_class, device_type):
        deviceList = Device.query.filter(Device.device_class == device_class, Device.device_type == device_type).all()
        result_list = []
        props_json_list = []
        id_list = []
        for device in deviceList:
            device_prop_json = json.loads(device.props_json)
            props_json = json.dumps(device_prop_json)
            props_json_list.append(props_json)
            id_list.append(device.id)

        result_list.append(id_list)
        result_list.append(props_json_list)
        return result_list

    def getDeviceProperty(self, device_class, device_type):
        # 遍历某种设备的属性名与单位
        deviceProperty = DeviceProperties.query.filter(DeviceProperties.device_class == device_class, DeviceProperties.device_type == device_type).all()[0]
        device_prop_json = json.loads(deviceProperty.props_json)
        props_json = json.dumps(device_prop_json)
        return props_json

    def updateDevice(self, oldDev, requestFromData):
        dev = oldDev
        formElementArray = requestFromData.split('&')
        formElementList = []
        for formElement in formElementArray:
            formElementList.append(formElement.split('='))
        formDict = dict(formElementList)

        prop_value = []
        for index in range(len(formElementList) - 2):
            device_prop_index = 'device_property_' + str(index)
            device_prop_value = formDict[device_prop_index]
            url_code_value = urllib.unquote(str(device_prop_value)).decode('utf-8')
            prop_value.append(url_code_value)

        device_prop_json = json.loads(dev.props_json)
        device_prop_json[u'prop_value'] = prop_value
        props_json = json.dumps(device_prop_json)

        if dev.device_class == '1':
            if dev.device_type == '1':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[2]
                dev.main_prop_value_2 = prop_value[7]
                dev.main_prop_value_3 = prop_value[1]
                dev.props_json = props_json

            elif dev.device_type == '2':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[7]
                dev.props_json = props_json
            elif dev.device_type == '3':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[10]
                dev.props_json = props_json
            elif dev.device_type == '4':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[10]
                dev.props_json = props_json
            elif dev.device_type == '5':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[10]
                dev.props_json = props_json
            elif dev.device_type == '6':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[4]
                dev.main_prop_value_3 = prop_value[8]
                dev.main_prop_value_4 = prop_value[9]
                dev.props_json = props_json
            elif dev.device_type == '7':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[4]
                dev.main_prop_value_3 = prop_value[7]
                dev.main_prop_value_4 = prop_value[8]
                dev.props_json = props_json
            elif dev.device_type == '8':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[2]
                dev.main_prop_value_3 = prop_value[5]
                dev.main_prop_value_4 = prop_value[9]
                dev.props_json = props_json
            elif dev.device_type == '9':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[3]
                dev.main_prop_value_3 = prop_value[7]
                dev.main_prop_value_4 = prop_value[12]
                dev.props_json = props_json
            elif dev.device_type == '10':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[2]
                dev.main_prop_value_3 = prop_value[10]
                dev.main_prop_value_4 = prop_value[13]
                dev.main_prop_value_5 = prop_value[16]
                dev.props_json = props_json
        elif dev.device_class == '2':
            if dev.device_type == '1':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[2]
                dev.main_prop_value_2 = prop_value[3]
                dev.main_prop_value_3 = prop_value[1]
                dev.main_prop_value_4 = prop_value[1]
                dev.props_json = props_json
        elif dev.device_class == '3':
            if dev.device_type == '1':
                dev.main_prop_value_1 = prop_value[0]
                dev.main_prop_value_2 = prop_value[6]
                dev.main_prop_value_3 = prop_value[12]
                dev.props_json = props_json
            elif dev.device_type == '2':
                dev.main_prop_value_1 = prop_value[0]
                dev.main_prop_value_2 = prop_value[6]
                dev.props_json = props_json
        elif dev.device_class == '4':
            if dev.device_type == '1':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[1]
                dev.main_prop_value_2 = prop_value[14]
                dev.main_prop_value_3 = prop_value[15]
                dev.props_json = props_json
        elif dev.device_class == '5':
            if dev.device_type == '1':
                dev.device_code = prop_value[1]
                dev.main_prop_value_1 = prop_value[0]
                dev.main_prop_value_2 = prop_value[14]
                dev.main_prop_value_3 = prop_value[15]
                dev.props_json = props_json
        elif dev.device_class == '6':
            if dev.device_type == '1':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[4]
                dev.main_prop_value_2 = prop_value[5]
                dev.props_json = props_json
        elif dev.device_class == '7':
            if dev.device_type == '1':
                dev.device_code = prop_value[3]
                dev.main_prop_value_1 = prop_value[4]
                dev.main_prop_value_2 = prop_value[5]
                dev.main_prop_value_3 = prop_value[2]
                dev.props_json = props_json
        elif dev.device_class == '9':
            if dev.device_type == '1':
                dev.device_code = prop_value[1]
                dev.main_prop_value_1 = prop_value[0]
                dev.props_json = props_json
            elif dev.device_type == '2':
                dev.device_code = prop_value[1]
                dev.main_prop_value_1 = prop_value[0]
                dev.props_json = props_json
        elif dev.device_class == '12':
            if dev.device_type == '1':
                dev.device_code = prop_value[1]
                dev.main_prop_value_1 = prop_value[2]
                dev.props_json = props_json
        elif dev.device_class == '13':
            if dev.device_type == '1':
                dev.device_code = prop_value[0]
                dev.main_prop_value_1 = prop_value[7]
                dev.props_json = props_json

        return dev

    def getDevice(self, requestFromData):
        formElementArray = requestFromData.split('&')
        formElementList = []
        for formElement in formElementArray:
            formElementList.append(formElement.split('='))

        formDict = dict(formElementList)
        deviceClass = formDict['device_class']
        deviceType = formDict['device_type']

        deviceProperty = DeviceProperties.query.filter(DeviceProperties.device_class == deviceClass, DeviceProperties.device_type == deviceType).all()[0]
        device_prop_json = json.loads(deviceProperty.props_json)

        prop_value = []
        for index in range(len(formElementList) - 2):
            device_prop_index = 'device_property_' + str(index)
            device_prop_value = formDict[device_prop_index]
            url_code_value = urllib.unquote(str(device_prop_value)).decode('utf-8')
            prop_value.append(url_code_value)

        prop_name = []
        for name in device_prop_json[u'prop_name']:
            index = device_prop_json[u'prop_name'].index(name)
            prop_name.append(device_prop_json[u'prop_name'][index])

        device_prop_json[u'prop_value'] = prop_value
        props_json = json.dumps(device_prop_json)

        device = None
        if deviceClass == '1':
            if deviceType == '1':
                device = Device.create_device(
                    1, 1, prop_value[0],
                    prop_name[2].encode('utf-8'), prop_value[2], u"kW", u"eng1",
                    prop_name[7].encode('utf-8'), prop_value[7], u"kg/h", u"eng2",
                    prop_name[1].encode('utf-8'), prop_value[1], u"MPa", u"eng3",
                    props_json=props_json
                )
            elif deviceType == '2':
                device = Device.create_device(
                    1, 2, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"10³kcal/h", u"eng1",
                    prop_name[7].encode('utf-8'), prop_value[7], u"ton/h", u"eng2",
                    props_json=props_json
                )
            elif deviceType == '3':
                device = Device.create_device(
                    1, 3, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[10].encode('utf-8'), prop_value[10], u"ton/h", u"eng2",
                    props_json=props_json
                )
            elif deviceType == '4':
                device = Device.create_device(
                    1, 4, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[10].encode('utf-8'), prop_value[10], u"ton/h", u"eng2",
                    props_json=props_json
                )
            elif deviceType == '5':
                device = Device.create_device(
                    1, 5, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[10].encode('utf-8'), prop_value[10], u"ton/h", u"eng2",
                    props_json=props_json
                )
            elif deviceType == '6':
                device = Device.create_device(
                    1, 6, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[4].encode('utf-8'), prop_value[4], u"kW", u"eng2",
                    prop_name[8].encode('utf-8'), prop_value[8], u"℃", u"eng3",
                    prop_name[9].encode('utf-8'), prop_value[9], u"m³/h", u"eng4",
                    props_json=props_json
                )
            elif deviceType == '7':
                device = Device.create_device(
                    1, 7, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[4].encode('utf-8'), prop_value[4], u"kW", u"eng2",
                    prop_name[7].encode('utf-8'), prop_value[7], u"℃", u"eng3",
                    prop_name[8].encode('utf-8'), prop_value[8], u"m³/h", u"eng4",
                    props_json=props_json
                )
            elif deviceType == '8':
                device = Device.create_device(
                    1, 8, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[2].encode('utf-8'), prop_value[2], u"kW", u"eng2",
                    prop_name[5].encode('utf-8'), prop_value[5], u"℃", u"eng3",
                    prop_name[9].encode('utf-8'), prop_value[9], u"kg/h", u"eng4",
                    props_json=props_json
                )
            elif deviceType == '9':
                device = Device.create_device(
                    1, 9, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[3].encode('utf-8'), prop_value[3], u"kW", u"eng2",
                    prop_name[7].encode('utf-8'), prop_value[7], u"℃", u"eng3",
                    prop_name[12].encode('utf-8'), prop_value[12], u"kg/h", u"eng4",
                    props_json=props_json
                )
            elif deviceType == '10':
                device = Device.create_device(
                    1, 10, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[2].encode('utf-8'), prop_value[2], u"kW", u"eng2",
                    prop_name[10].encode('utf-8'), prop_value[10], u"m³/h", u"eng3",
                    prop_name[13].encode('utf-8'), prop_value[13], u"m³/h", u"eng4",
                    prop_name[16].encode('utf-8'), prop_value[16], u"m³/h", u"eng5",
                    props_json=props_json
                )
        elif deviceClass == '2':
            if deviceType == '1':
                device = Device.create_device(
                    2, 1, prop_value[0],
                    prop_name[2].encode('utf-8'), prop_value[2], u"kW", u"eng1",
                    prop_name[3].encode('utf-8'), prop_value[3], u"kW", u"eng2",
                    # ''' 制冷量左？？？'''
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng3",
                    # ''' 制冷量右？？？'''
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng4",
                    props_json=props_json
                )
        elif deviceClass == '3':
            if deviceType == '1':
                device = Device.create_device(
                    3, 1, u'Ground Source Heat Pumps',
                    prop_name[0].encode('utf-8'), prop_value[0], u"kW", u"eng1",
                    prop_name[6].encode('utf-8'), prop_value[6], u"kW", u"eng2",
                    prop_name[12].encode('utf-8'), prop_value[12], u"kW", u"eng3",
                    props_json=props_json
                )
            elif deviceType == '2':
                device = Device.create_device(
                    3, 2, u'Air Source Heat Pumps',
                    prop_name[0].encode('utf-8'), prop_value[0], u"kW", u"eng1",
                    prop_name[6].encode('utf-8'), prop_value[6], u"kW", u"eng2",
                    props_json=props_json
                )
        elif deviceClass == '4':
            if deviceType == '1':
                device = Device.create_device(
                    3, 1, prop_value[0],
                    prop_name[1].encode('utf-8'), prop_value[1], u"kW", u"eng1",
                    prop_name[14].encode('utf-8'), prop_value[14], u"℃", u"eng2",
                    prop_name[15].encode('utf-8'), prop_value[15], u"t/h", u"eng3",
                    props_json=props_json
                )
        elif deviceClass == '5':
            if deviceType == '1':
                device = Device.create_device(
                    5, 1, prop_value[1],
                    prop_name[0].encode('utf-8'), prop_value[0], u"kW", u"eng1",
                    prop_name[14].encode('utf-8'), prop_value[14], u"℃", u"eng2",
                    prop_name[15].encode('utf-8'), prop_value[15], u"kg/h", u"eng3",
                    props_json=props_json
                )
        elif deviceClass == '6':
            if deviceType == '1':
                device = Device.create_device(
                    6, 1, prop_value[0],
                    prop_name[4].encode('utf-8'), prop_value[4], u"W", u"eng1",
                    prop_name[5].encode('utf-8'), prop_value[5], u"%", u"eng2",
                    props_json=props_json
                )
        elif deviceClass == '7':
            if deviceType == '1':
                device = Device.create_device(
                    7, 1, prop_value[3],
                    prop_name[4].encode('utf-8'), prop_value[4], u"Mpa", u"eng1",
                    prop_name[5].encode('utf-8'), prop_value[5], u"m3/min", u"eng2",
                    prop_name[2].encode('utf-8'), prop_value[2], u"unit3", u"eng3",
                    props_json=props_json
                )
        elif deviceClass == '9':
            if deviceType == '1':
                device = Device.create_device(
                    9, 1, prop_value[1],
                    prop_name[0].encode('utf-8'), prop_value[0], u"kW", u"eng1",
                    props_json=props_json
                )
            elif deviceType == '2':
                device = Device.create_device(
                    9, 2, prop_value[1].encode('utf-8'),
                    prop_name[0].encode('utf-8'), prop_value[0], u"kW", u"eng1",
                    props_json=props_json
                )
        elif deviceClass == '12':
            if deviceType == '1':
                device = Device.create_device(
                    12, 1, prop_value[1],
                    prop_name[2].encode('utf-8'), prop_value[2], u"kW", u"eng1",
                    props_json=props_json
                )
        elif deviceClass == '13':
            if deviceType == '1':
                device = Device.create_device(
                    13, 1, prop_value[0],
                    prop_name[7].encode('utf-8'), prop_value[7], u"unit1", u"eng1",
                    props_json=props_json
                )

        return device
