# -*- coding:UTF-8 -*-
import json
import math
import numpy
import time
import copy
from scipy.optimize import linprog
from app.energy_island.models import Device
from sqlalchemy import or_, not_, and_
from util.iapws_if97 import seuif97
from decimal import Decimal
from multiprocessing.pool import ThreadPool


'''
能源互联岛逻辑模块
'''

__all__ = [

]

'''
设备方案list
每个元素为一个dict，key值为photovoltaic、wind、electric、out_resource、waste、energy_storage、peak_regulation、auxiliary
分别代表光伏、风电、以及其他发电设备(内燃机、燃气轮机)、外部资源设备、余热设备、蓄能设备、调峰设备、辅机设备
'''
device_list = []
device_list_day_2 = []
device_list_day_3 = []
device_list_day_4 = []

'''
外部资源dict
保存从需求调研表中外部资源转换后得到的对应需求资源
以字典形式保存，key值为u'cool', u'heat', u'hot_water'
对应冷(kW)，热(kW)，热水(t/h)
只保存所有外部资源的总数值
'''
out_resource = {'electric': 0, 'steam': 0, 'cool': 0, 'heat': 0, 'hot_water': 0, 'air': 0}

'''
外部资源dict
保存各种外部资源所能提供的数值的详细信息
'''
out_resource_detail = {'electric': {}, 'steam': {}, 'cool': {}, 'heat': {}, 'hot_water': {}, 'air': {}}

'''
余热设备list
每个元素waste_heat为dict类型，key值为
u'steam', u'cool', u'heat', u'hot_water', u'air', u'mix', u'waste_type'
其中u'mix'保存同时提供的2种及3种需求时所能满足的各个需求的最大数值
u'waste_type'标明了该组余热设备所依赖的设备类型
'1': 蒸汽型余热锅炉(系)
'2': 烟气溴化锂(系)
'3': 余热热水锅炉(系)
'4': 烟气热水型溴化锂(系)
'5': 溴化锂吸收式直燃型三用机(系)
(比如同时供热与热水，则保存只供热时的最大值与只提供热水的时候的最大值)
单位做了统一，steam(t/h), cool(kW), heat(kW), hot_water(t/h), air(Nm³/h), mix参照具体元素的单位
'''
waste_heat_device = []

'''
空压站设备list
'''
air_device = []

'''
调峰设备dict
key值为electric、steam、cool、heat、hot_water、storage
分别代表电、蒸汽、冷、热、生活热水、蓄能
'''
peak_load_regulation_device = []

'''
勾选设备的列表
'''
used_devices = []

'''
锅炉参数
1: 燃气热水锅炉
2: 燃气蒸汽锅炉
3: 余热热水锅炉
4: 余热蒸汽锅炉
'''
boiler_params = {'1': {}, '2': {}, '3': {}, '4': {}}

'''
辅机设备list
'''
auxiliary_device = []

# 已有的负荷信息
available_power = {
    u'electric': 0,
    u'heat': 0,
    u'cool': 0,
    u'steam': 0,
    u'hot_water': 0,
    u'air': 0
}


class AlgoConstants:
    # 板换效率值
    plate_type_heat_exchanger_efficiency = 0.9
    # 热电比
    heat_electric_ratio = 1.5
    # 匹配的设备最大数量
    max_matched_devices_number = 5
    # 匹配的空压站设备最大数量
    max_matched_air_devices_number = 10
    # 排烟可回收功率系数
    exhaust_gas_available_power_coefficient = 1.3
    # 高温水可回收功率系数
    hot_water_available_power_coefficient = 0.9
    # 烟气热水型（补燃型）溴化锂功率系数
    gas_LiBr_afterburning_coefficient = 1.1
    # 热水锅炉吨水电耗5kw/h
    hot_water_boiler_electric_power = 5
    # 蒸汽锅炉吨汽电耗4kw/h
    steam_boiler_electric_power = 4
    # 补水量系数
    supply_water_coefficient = 0.02
    # 设备运行的输出key与对应的list下标
    device_running_dict = {'electric': 0, 'steam': 1, 'cool': 2, 'heat': 3, 'heat_plate': 4, 'hot_water': 5, 'air': 6}
    # 电制冷cop
    electric_cool_cop = 5.
    # 水源热泵制冷cop
    sewage_heat_pump_cool_cop = 5.5
    # 水源热泵供热cop
    sewage_heat_pump_heat_cop = 4.2
    # 地源热泵制冷cop
    ground_heat_pump_cool_cop = 5.5
    # 地源热泵供热cop
    ground_heat_pump_heat_cop = 4.5
    # 蒸汽锅炉/余热锅炉补燃的燃气热值(KJ/Nm³)
    gas_caloricity = 36000
    # 蒸汽锅炉效率
    steam_boiler_efficiency = 0.89
    # 热水锅炉效率
    hot_water_boiler_efficiency = 0.89
    # 补燃量
    afterburning_percentage = 0.2
    # 内燃机自耗电系数
    internal_combustion_engine_electric_coefficient = 0.02
    # 燃气轮机自耗电系数
    gas_turbine_electric_coefficient = 0.04
    # 溴化锂设备补水率
    LiBr_supply_water_coefficient = 0.01


class ChargeDevice:
    def __init__(
        self, electric_charge=False, cool_charge=False, heat_charge=False, heat_pump=False,
        electric_max=2000, cool_max=500, heat_max=2500
    ):
        self.electric_charge = 0
        self.cool_charge = 0
        self.heat_charge = 0
        self.heat_pump = heat_pump
        if electric_charge:
            self.__electric_max = electric_max
        else:
            self.__electric_max = 0
        if cool_charge:
            self.__cool_max = cool_max
        else:
            self.__cool_max = 0
        if heat_charge:
            self.__heat_max = heat_max
        else:
            self.__heat_max = 0

    def charge(self, electric=0, cool=0, heat=0):
        if electric > 0:
            if self.electric_charge + electric <= self.__electric_max:
                self.electric_charge += electric
            else:
                self.electric_charge = self.__electric_max
        if cool > 0:
            if self.cool_charge + cool <= self.__cool_max:
                self.cool_charge += cool
            else:
                self.cool_charge = self.__cool_max
        if heat > 0:
            if self.heat_charge + heat <= self.__heat_max:
                self.heat_charge += heat
            else:
                self.heat_charge = self.__heat_max

    def charge_max(self, electric=True, cool=True, heat=True):
        if electric:
            self.electric_charge = self.__electric_max
        if cool:
            self.cool_charge = self.__cool_max
        if heat:
            self.heat_charge = self.__heat_max

    def release_electric(self, electric=None):
        if electric > self.electric_charge or electric is None:
            electric_release = self.electric_charge
            self.electric_charge = 0
        else:
            electric_release = electric
            self.electric_charge -= electric
        return electric_release

    def release_cool(self, cool=None):
        if cool > self.cool_charge or cool is None:
            cool_release = self.cool_charge
            self.cool_charge = 0
        else:
            cool_release = cool
            self.cool_charge -= cool
        return cool_release

    def release_heat(self, heat=None):
        if heat > self.heat_charge or heat is None:
            heat_release = self.heat_charge
            self.heat_charge = 0
        else:
            heat_release = heat
            self.heat_charge -= heat
        return heat_release

    def to_dict(self):
        return {'electric_charge': self.electric_charge, 'cool_charge': self.cool_charge, 'heat_charge': self.heat_charge}


class PhotovoltaicCurve:
    def __init__(
        self, start_min=0, start_hour=6, end_min=0, end_hour=18, peak_power=2000, ita=1
    ):
        self.start_min = start_min
        self.start_hour = start_hour
        self.end_min = end_min
        self.end_hour = end_hour
        self.peak_power = peak_power
        self.ita = ita
        self.peak_time = 0
        self.curve_list = []

    def create_curve(self, time_min, time_hour, peak_power=None, ita=1):
        start_time = self.start_hour + self.start_min / 60.
        end_time = self.end_hour + self.end_min / 60.
        hours = end_time - start_time
        self.peak_time = hours / 2. + start_time
        now_time = time_hour + time_min / 60.
        if now_time < start_time or now_time > end_time:
            return 0
        elif now_time <= self.peak_time:
            theta = (self.peak_time - now_time) * math.pi / hours
        else:
            theta = (now_time - self.peak_time) * math.pi / hours
        if peak_power:
            power = peak_power * math.cos(theta)
        else:
            power = self.peak_power * math.cos(theta)
        return round(power, ndigits=5)


def need_other_device(device_list, required_load):
    '''
    查看是否还需要别的设备来满足负荷
    '''
    total_load = 0
    for device in device_list:
        if device:
            total_load = total_load + device['load']
    if total_load < required_load:
        return True
    else:
        return False


def get_requirement(requirement_json):
    '''
    根据需求调查表获取需求
    requirement_json 前台传来的json
    '''
    # TODO 返回需要的负荷种类
    return []


def get_available_power(requirement):
    '''
    根据需求调查表获取已有的六种需求
    requirement 需求表信息dict
    '''
    # TODO 需要根据外部资源来判断已有需求
    return {u'已有电力需求': requirement[u'已有电力需求'], u'已有热负荷': requirement[u'已有热负荷']}


def get_curve(requirement):
    '''
    根据需求调查表获得曲线数据
    '''
    start_min = float(requirement[u'光伏'][u'日出时间'].split(':')[1])
    start_hour = float(requirement[u'光伏'][u'日出时间'].split(':')[0])
    end_min = float(requirement[u'光伏'][u'日落时间'].split(':')[1])
    end_hour = float(requirement[u'光伏'][u'日落时间'].split(':')[0])
    phv = PhotovoltaicCurve(start_min=start_min, start_hour=start_hour, end_min=end_min, end_hour=end_hour, peak_power=requirement[u'光伏'][u'峰值功率'])
    photovoltaic_vurve = []
    for i in range(0, 24):
        photovoltaic_vurve.append(phv.create_curve(0, i))
    # if requirement[u'冷负荷'] and requirement[u'热负荷']:
    #     requirement_summer = copy.deepcopy(requirement)
    #     requirement_winter = copy.deepcopy(requirement)
    #     requirement_summer[u'热负荷'] = None
    #     requirement_winter[u'冷负荷'] = None
    #     summer_curve = requirement_summer[u'负荷曲线']['day_1']
    #     winter_curve = requirement_winter[u'负荷曲线']['day_1']
    #     summer_curve['heat_curve'] = None
    #     winter_curve['cool_curve'] = None
    #     return {'day_1': summer_curve, 'day_2': winter_curve, 'day_3': None, 'day_4': None}, photovoltaic_vurve
    return requirement[u'负荷曲线'], photovoltaic_vurve


def get_need_and_price(requirement, typical_day):
    '''
    根据需求调研表中典型日对应的季节获取当前需求、价格
    '''
    requirement_summer = copy.deepcopy(requirement)
    requirement_winter = copy.deepcopy(requirement)
    # requirement_summer[u'热负荷'] = None
    # if requirement_summer[u'负荷曲线'][typical_day]:
    #     requirement_summer[u'负荷曲线'][typical_day]['heat_curve'] = None
    # requirement_winter[u'冷负荷'] = None
    # if requirement_winter[u'负荷曲线'][typical_day]:
    #     requirement_winter[u'负荷曲线'][typical_day]['cool_curve'] = None
    if requirement[u'典型日季节'][typical_day] == '1':
        # 夏季
        price = requirement[u'价格-夏']
        req = requirement_summer
    elif requirement[u'典型日季节'][typical_day] == '2':
        # 冬季
        price = requirement[u'价格-冬']
        req = requirement_winter
    else:
        req = None
        price = None
    return price, req


def set_boiler_params(device_class, device_type, form_data):
    '''
    根据勾选的设备列表设置锅炉参数
    '''
    if device_class == '8':
        for row in form_data:
            if row['column_val']:
                key = row['column_name']
                boiler_params[device_type][key] = float(row['column_val'])
            else:
                key = row['column_name']
                boiler_params[device_type][key] = None


def get_used_devices():
    '''
    获取勾选的设备列表(数据库中的设备)
    '''
    global used_devices, boiler_params
    used_devices_list = []
    for device_class in used_devices:
        if len(device_class['device_type']) > 0:
            boiler_params = {'1': {}, '2': {}, '3': {}, '4': {}}
            for device_type in device_class['device_type']:
                used_device_dict = {}
                used_device_dict['device_class'] = device_class['device_class']
                used_device_dict['device_type'] = str(device_type['modelnum'])
                used_devices_list.append(used_device_dict)
                if device_type['modelnumvalue']:
                    set_boiler_params(device_class['device_class'], str(device_type['modelnum']), device_type['modelnumvalue'])
        else:
            used_device_dict = {}
            used_device_dict['device_class'] = device_class['device_class']
            used_device_dict['device_type'] = None
            used_devices_list.append(used_device_dict)
    return used_devices_list


def get_disabled_devices_conditions(disabled_devices):
    '''
    创建被勾选掉的不使用设备的搜索条件
    '''
    conditions = and_()
    if len(disabled_devices) == 0:
        conditions = and_(Device.device_class == '1', Device.device_class != '1')
    for device in disabled_devices:
        # if device[u'device_type']:
        #     conditions = conditions & and_(Device.device_class != device[u'device_class'], Device.device_type != device[u'device_type'])
        # else:
        #     conditions = conditions & and_(Device.device_class != device[u'device_class'])
        if device[u'device_type']:
            conditions = conditions | and_(Device.device_class == device[u'device_class'], Device.device_type == device[u'device_type'])
        else:
            conditions = conditions | and_(Device.device_class == device[u'device_class'])
    return conditions


def other_power_generating_device_select(photovoltaic_power, wind_power, requirement, available_power, used_devices):
    '''
    根据光伏、风电设备的情况搜索匹配其余的发电设备
    '''
    used_devices_class_list = list(map(lambda x: x['device_class'], used_devices))
    disabled_devices_conditions = get_disabled_devices_conditions(used_devices)
    if u'10' in used_devices_class_list:
        # 有市电的情况
        if need_other_device([photovoltaic_power, wind_power], requirement[u'电力需求'] - available_power[u'已有电力需求']):
            total_load = 0
            if photovoltaic_power:
                total_load = total_load + photovoltaic_power[u'load']
            if wind_power:
                total_load = total_load + wind_power[u'load']
            need_load = requirement[u'电力需求'] - available_power[u'已有电力需求'] - total_load
            matched_devices = []
            if float(requirement[u'热负荷']) / requirement[u'电力需求'] <= AlgoConstants.heat_electric_ratio:
                matched_devices = Device.query.filter(
                    or_(
                        and_(Device.main_prop_name_1 == '电功率', Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number <= need_load, Device.device_class == '5') & disabled_devices_conditions
                    )
                ).all()
            else:
                matched_devices = Device.query.filter(
                    or_(
                        and_(Device.main_prop_name_1 == '燃机出力', Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number <= need_load, Device.device_class == '4') & disabled_devices_conditions
                    )
                ).all()
            for device_other in matched_devices:
                # 向下取整
                number = int(math.floor(Decimal(need_load) / device_other.main_prop_value_1))
                if number >= AlgoConstants.max_matched_devices_number:
                    number = AlgoConstants.max_matched_devices_number
                electric = {u'load': device_other.main_prop_value_1, u'unit': device_other.main_prop_unit_1, u'number': number, u'id': device_other.id, u'class': device_other.device_class, u'props': device_other.props_json, u'waste': None}
                device_list.append({u'photovoltaic': photovoltaic_power, u'wind': wind_power, u'electric': electric})
    else:
        # 无市电的情况
        need_load = requirement[u'电力需求']
        matched_devices = []
        if float(requirement[u'热负荷']) / requirement[u'电力需求'] <= AlgoConstants.heat_electric_ratio:
            matched_devices = Device.query.filter(
                or_(
                    and_(Device.main_prop_name_1 == '电功率', Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number >= need_load, Device.device_class == '5') & disabled_devices_conditions
                )
            ).all()
        else:
            matched_devices = Device.query.filter(
                or_(
                    and_(Device.main_prop_name_1 == '燃机出力', Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number >= need_load, Device.device_class == '4') & disabled_devices_conditions
                )
            ).all()
        for device_other in matched_devices:
            # 向上取整
            number = int(math.ceil(Decimal(need_load) / device_other.main_prop_value_1))
            if number <= AlgoConstants.max_matched_devices_number:
                electric = {u'load': device_other.main_prop_value_1, u'unit': device_other.main_prop_unit_1, u'number': number, u'id': device_other.id, u'class': device_other.device_class, u'props': device_other.props_json, u'waste': None}
                device_list.append({u'photovoltaic': photovoltaic_power, u'wind': wind_power, u'electric': electric})


def other_power_generating_device_select_test(photovoltaic_power, wind_power, requirement, available_power, disabled_devices_conditions):
    '''
    根据光伏、风电设备的情况搜索匹配其余的发电设备
    '''
    if need_other_device([photovoltaic_power, wind_power], requirement[u'电力需求'] - available_power[u'已有电力需求']):
        total_load = 0
        if photovoltaic_power:
            total_load = total_load + photovoltaic_power[u'load']
        if wind_power:
            total_load = total_load + wind_power[u'load']
        need_load = requirement[u'电力需求'] - available_power[u'已有电力需求'] - total_load
        matched_devices = Device.query.filter(
            or_(
                and_(Device.main_prop_name_1 == '电功率', Device.main_prop_value_1 == 2000, Device.device_class == '5') & disabled_devices_conditions
            )
        ).all()
        for device_other in matched_devices:
            # number = int(math.floor(Decimal(need_load) / device_other.main_prop_value_1))
            number = 2
            if number <= AlgoConstants.max_matched_devices_number:
                electric = {u'load': device_other.main_prop_value_1, u'unit': device_other.main_prop_unit_1, u'number': number, u'id': device_other.id, u'class': device_other.device_class, u'props': device_other.props_json, u'waste': None}
                device_list.append({u'photovoltaic': photovoltaic_power, u'wind': wind_power, u'electric': electric})


def power_generating_device_select(requirement, used_devices):
    '''
    添加电负荷设备方案
    device_list的每个元素为一个dict，key值为photovoltaic、wind、electric等等
    分别代表光伏、风电、以及其他发电设备(内燃机、燃气轮机)等等
    每个dict构成一个电负荷方案
    '''
    # 获取已有的负荷信息
    available_power = get_available_power(requirement)
    # 判断是否有光伏需求
    photovoltaic_power = None
    wind_power = None
    if requirement[u'光伏'] and u'光伏' in out_resource_detail['electric'] and out_resource_detail['electric'][u'光伏']['used']:
        load = out_resource_detail['electric'][u'光伏']['load']
        photovoltaic_power = {u'load': load, u'unit': u'kW'}
    if requirement[u'风电'] and u'风电' in out_resource_detail['electric'] and out_resource_detail['electric'][u'风电']['used']:
        load = out_resource_detail['electric'][u'风电']['load']
        wind_power = {u'load': requirement[u'风电'], u'unit': u'kW'}
    # if requirement[u'光伏']:
    #     # 搜索光伏设备
    #     load = requirement[u'光伏'][u'有效面积㎡'] / 10000.0 * 1000
    #     photovoltaic_power = {u'load': load, u'unit': u'kW'}
    # 判断是否有风电需求
    # if requirement[u'风电']:
    #     wind_power = {u'load': requirement[u'风电'], u'unit': u'kW'}
    # 查看是否还需要其余设备，如果需要则添加除光伏设备之外的电负荷设备
    other_power_generating_device_select(photovoltaic_power, wind_power, requirement, available_power, used_devices)


def power_generating_device_select_test(requirement, disabled_devices_conditions):
    '''
    添加电负荷设备方案
    device_list的每个元素为一个dict，key值为photovoltaic、wind、electric等等
    分别代表光伏、风电、以及其他发电设备(内燃机、燃气轮机)等等
    每个dict构成一个电负荷方案
    '''
    # 获取已有的负荷信息
    available_power = get_available_power(requirement)
    photovoltaic_power = {u'load': 595.2, u'unit': u'kW'}
    wind_power = {u'load': 0, u'unit': u'kW'}
    # 查看是否还需要其余设备，如果需要则添加除光伏设备之外的电负荷设备
    other_power_generating_device_select_test(photovoltaic_power, wind_power, requirement, available_power, disabled_devices_conditions)


def get_out_resource_load(load, number, used=1, self_consumption_ele=0, self_consumption_gas=0, self_consumption_water=0):
    '''
    计算外部资源的数值
    used表示该资源是否使用
    '''
    self_consumption = {'electric': self_consumption_ele, 'gas': self_consumption_gas, 'water': self_consumption_water}
    if load and number:
        return {'load': load * number, 'used': used, 'self_consumption': self_consumption}
    return {'load': 0, 'used': used, 'self_consumption': self_consumption}


def out_resource_init():
    '''
    初始化外部资源
    '''
    out_resource_detail['electric'][u'光伏'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['electric'][u'风电'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['cool'][u'热泵'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['heat'][u'热泵'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['steam'][u'外部汽源'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['steam'][u'自有蒸汽锅炉'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['hot_water'][u'自有热水锅炉'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['heat'][u'外部供热设备'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['cool'][u'现有制冷设备'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['heat'][u'现有制冷设备'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['air'][u'空压站'] = get_out_resource_load(0, 0, used=0)
    out_resource_detail['hot_water'][u'空压站余热利用'] = get_out_resource_load(0, 0, used=0)


def set_out_source_used(selected_device_list, requirement):
    '''
    更新out_resource_detail和out_resource，设置使用的外部资源并根据此来计算
    '''
    if requirement[u'外部资源']:
        cool_power = 0
        heat_power = 0
        hot_water = 0
        steam_q = 0
        air_q = 0
        if requirement[u'外部资源'][u'空压站余热利用']:
            out_resource_detail['hot_water'][u'空压站余热利用'] = get_out_resource_load(requirement[u'外部资源'][u'空压站余热利用'][u'流量'], 1, 1 if u'空压站余热利用' in selected_device_list else 0)
            if out_resource_detail['hot_water'][u'空压站余热利用']['used'] == 1:
                hot_water = hot_water + out_resource_detail['hot_water'][u'空压站余热利用']['load']
        if requirement[u'外部资源'][u'空压站']:
            out_resource_detail['air'][u'空压站'] = get_out_resource_load(requirement[u'外部资源'][u'空压站'][u'流量'], requirement[u'外部资源'][u'空压站'][u'数量'], 1 if u'空压站' in selected_device_list else 0)
            if out_resource_detail['air'][u'空压站']['used'] == 1:
                air_q = air_q + out_resource_detail['air'][u'空压站']['load']
        if requirement[u'外部资源'][u'现有制冷设备']:
            out_resource_detail['cool'][u'现有制冷设备'] = get_out_resource_load(requirement[u'外部资源'][u'现有制冷设备'][u'冷功率'], requirement[u'外部资源'][u'现有制冷设备'][u'数量'], 1 if u'现有制冷设备' in selected_device_list else 0)
            if out_resource_detail['cool'][u'现有制冷设备']['used'] == 1:
                cool_power = cool_power + out_resource_detail['cool'][u'现有制冷设备']['load']
            out_resource_detail['heat'][u'现有制冷设备'] = get_out_resource_load(requirement[u'外部资源'][u'现有制冷设备'][u'热功率'], requirement[u'外部资源'][u'现有制冷设备'][u'数量'], 1 if u'现有制冷设备' in selected_device_list else 0)
            if out_resource_detail['heat'][u'现有制冷设备']['used'] == 1:
                heat_power = heat_power + out_resource_detail['heat'][u'现有制冷设备']['load']
        if requirement[u'外部资源'][u'外部供热设备']:
            out_resource_detail['heat'][u'外部供热设备'] = get_out_resource_load(requirement[u'外部资源'][u'外部供热设备'][u'流量'], requirement[u'外部资源'][u'外部供热设备'][u'数量'], 1 if u'外部供热设备' in selected_device_list else 0)
            if out_resource_detail['heat'][u'外部供热设备']['used'] == 1:
                heat_power = heat_power + out_resource_detail['heat'][u'外部供热设备']['load']
        if requirement[u'外部资源'][u'自有热水锅炉']:
            out_resource_detail['hot_water'][u'自有热水锅炉'] = get_out_resource_load(requirement[u'外部资源'][u'自有热水锅炉'][u'流量'], requirement[u'外部资源'][u'自有热水锅炉'][u'数量'], 1 if u'自有热水锅炉' in selected_device_list else 0)
            if out_resource_detail['hot_water'][u'自有热水锅炉']['used'] == 1:
                hot_water = hot_water + out_resource_detail['hot_water'][u'自有热水锅炉']['load']
        if requirement[u'外部资源'][u'自有蒸汽锅炉']:
            out_resource_detail['steam'][u'自有蒸汽锅炉'] = get_out_resource_load(requirement[u'外部资源'][u'自有蒸汽锅炉'][u'流量'], requirement[u'外部资源'][u'自有蒸汽锅炉'][u'数量'], 1 if u'自有蒸汽锅炉' in selected_device_list else 0)
            if out_resource_detail['steam'][u'自有蒸汽锅炉']['used'] == 1:
                steam_q = steam_q + out_resource_detail['steam'][u'自有蒸汽锅炉']['load']
        if requirement[u'外部资源'][u'外部汽源']:
            out_resource_detail['steam'][u'外部汽源'] = get_out_resource_load(requirement[u'外部资源'][u'外部汽源'][u'流量'], requirement[u'外部资源'][u'外部汽源'][u'数量'], 1 if u'外部汽源' in selected_device_list else 0)
            if out_resource_detail['steam'][u'外部汽源']['used'] == 1:
                steam_q = steam_q + out_resource_detail['steam'][u'外部汽源']['load']
        out_resource['cool'] = cool_power
        out_resource['heat'] = heat_power
        out_resource['hot_water'] = hot_water
        out_resource['steam'] = steam_q
        out_resource['air'] = air_q


def set_waste_device_used(used_devices, requirement):
    '''
    设置光伏风电热泵的数据
    '''
    electric_power = 0
    cool_power = 0
    heat_power = 0
    hot_water = 0
    steam_q = 0
    air_q = 0
    used_devices_class_list = list(map(lambda x: x['device_class'], used_devices))
    if requirement[u'光伏']:
        load = requirement[u'光伏'][u'有效面积㎡'] / 10000.0 * 1000
        out_resource_detail['electric'][u'光伏'] = get_out_resource_load(load, 1, 1 if u'6' in used_devices_class_list else 0)
        if out_resource_detail['electric'][u'光伏']['used'] == 1:
            electric_power = electric_power + load
    if requirement[u'风电']:
        load = requirement[u'风电']
        out_resource_detail['electric'][u'风电'] = get_out_resource_load(load, 1, 1 if u'12' in used_devices_class_list else 0)
        if out_resource_detail['electric'][u'风电']['used'] == 1:
            electric_power = electric_power + load
    if requirement[u'外部资源'][u'热泵']:
        if requirement[u'外部资源'][u'热泵'][u'类型'] != -1:
            heat_pump_data = get_heat_pump_data(requirement[u'外部资源'][u'热泵'][u'可利用的绿化面积'], requirement[u'外部资源'][u'热泵'][u'生活污水'] + requirement[u'外部资源'][u'热泵'][u'工业污水'], requirement[u'外部资源'][u'热泵'][u'类型'])
            out_resource_detail['cool'][u'热泵'] = get_out_resource_load(heat_pump_data['cool_power'], 1, used=1 if u'3' in used_devices_class_list else 0, self_consumption_ele=heat_pump_data['ele_power_1'])
            out_resource_detail['heat'][u'热泵'] = get_out_resource_load(heat_pump_data['heat_power'], 1, used=1 if u'3' in used_devices_class_list else 0, self_consumption_ele=heat_pump_data['ele_power_2'])
            if out_resource_detail['cool'][u'热泵']['used'] == 1 or out_resource_detail['heat'][u'热泵']['used'] == 1:
                cool_power = cool_power + heat_pump_data['cool_power']
                heat_power = heat_power + heat_pump_data['heat_power']
    out_resource['electric'] = out_resource['electric'] + electric_power
    out_resource['cool'] = out_resource['cool'] + cool_power
    out_resource['heat'] = out_resource['heat'] + heat_power
    out_resource['hot_water'] = out_resource['hot_water'] + hot_water
    out_resource['steam'] = out_resource['steam'] + steam_q
    out_resource['air'] = out_resource['air'] + air_q


def air_device_select(requirement, device_list, disabled_devices):
    '''
    添加空压站设备方案
    1: 水冷，2: 风冷
    '''
    if requirement is not None and requirement[u'供气需求']:
        disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
        if requirement[u'供气需求'][u'压力'] <= 0.75:
            air_pressure = 0.75
        elif requirement[u'供气需求'][u'压力'] > 0.75 and requirement[u'供气需求'][u'压力'] <= 0.86:
            air_pressure = 0.86
        elif requirement[u'供气需求'][u'压力'] > 0.86 <= 1:
            air_pressure = 1
        else:
            air_pressure = 0
        # matched_device_air_wind_cool = Device.query.order_by(Device.main_prop_value_2.desc()).filter(
        #     and_(
        #         Device.device_class == '7',
        #         Device.main_prop_value_1 == air_pressure,
        #         Device.main_prop_value_2 <= requirement[u'供气需求'][u'流量'] / 60.,
        #         # Device.main_prop_value_2 * AlgoConstants.max_matched_devices_number >= requirement[u'供气需求'][u'流量'] / 60.,
        #         Device.main_prop_value_3 == 2
        #     ) & disabled_devices_conditions
        # ).limit(1)
        # matched_device_air_water_cool = Device.query.order_by(Device.main_prop_value_2.desc()).filter(
        #     and_(
        #         Device.device_class == '7',
        #         Device.main_prop_value_1 == air_pressure,
        #         Device.main_prop_value_2 <= requirement[u'供气需求'][u'流量'] / 60.,
        #         # Device.main_prop_value_2 * AlgoConstants.max_matched_devices_number >= requirement[u'供气需求'][u'流量'] / 60.,
        #         Device.main_prop_value_3 == 1
        #     ) & disabled_devices_conditions
        # ).limit(1)
        for case in device_list:
            new_waste_list = []
            for waste in case['waste']:
                matched_device_air = Device.query.order_by(Device.main_prop_value_2.asc()).filter(
                    and_(
                        Device.device_class == '7',
                        Device.main_prop_value_1 == air_pressure,
                        Device.main_prop_value_2 * AlgoConstants.max_matched_air_devices_number >= requirement[u'供气需求'][u'流量'] / 60.,
                        Device.main_prop_value_3 == requirement[u'供气需求'][u'冷却类型']
                    ) & disabled_devices_conditions
                ).limit(1)
                if matched_device_air.count() != 0:
                    new_waste = copy.deepcopy(waste)
                    number = math.ceil(requirement[u'供气需求'][u'流量'] / 60. / float(matched_device_air[0].main_prop_value_2))
                    new_waste[u'air'] = init_waste_heat_device_dict(
                        matched_device_air[0].device_class, matched_device_air[0].device_type, matched_device_air[0].id,
                        matched_device_air[0].main_prop_value_2 * 60, number=number, props_str=matched_device_air[0].props_json
                    )
                    new_waste_list.append(new_waste)
                # print(matched_device_air[0].main_prop_value_3)
                if matched_device_air.count() == 0:
                    new_waste = copy.deepcopy(waste)
                    new_waste_list.append(new_waste)
            case['waste'] = new_waste_list[:]


def gas_hot_water_boiler(heat_load, hot_water_pressure=0.7, hot_water_in_temperature=70, hot_water_out_temperature=95, gas_heat_value=36000, boiler_thermal_efficiency=0.91):
    '''
    燃气热水锅炉计算
    input (热负荷MW, 热水压力=0.7Mpa, 热水进水温度=70℃, 热水出水温度=95℃, 燃气热值=36000KJ/Nm³, 锅炉效率=91%)
    return (热水量t/h, 燃气耗量Nm³/h, 燃气耗量/热水量比值)
    '''
    water_in_h = seuif97.pt2h(hot_water_pressure, hot_water_in_temperature)
    water_out_h = seuif97.pt2h(hot_water_pressure, hot_water_out_temperature)
    hot_water_yield = heat_load * 3600. / (water_out_h - water_in_h)
    gas_consumption = heat_load * 3600. * 1000 / boiler_thermal_efficiency / gas_heat_value
    gas_hot_water_ratio = 1000. * (water_out_h - water_in_h) / boiler_thermal_efficiency / gas_heat_value
    return (hot_water_yield, gas_consumption, gas_hot_water_ratio)


def gas_steam_boiler(heat_load, steam_pressure=0.4, steam_temperature=190, water_supply_temperature=20, gas_heat_value=36000, boiler_thermal_efficiency=0.89):
    '''
    燃气蒸汽锅炉计算
    input (热负荷MW, 蒸汽压力=0.4Mpa, 蒸汽温度=190℃, 给水温度=20℃, 燃气热值=36000KJ/Nm³, 锅炉热效率=89%)
    return (饱和蒸汽温度℃, 产汽量t/h, 燃气耗量Nm³/h, 燃气耗量/产汽量比值)
    '''
    steam_h = seuif97.pt2h(steam_pressure, steam_temperature)
    steam_t_sat = seuif97.tsat_p(steam_pressure * 10)
    water_supply_h = seuif97.pt2h(steam_pressure, water_supply_temperature)
    steam_production = heat_load * 3600. / (steam_h - water_supply_h)
    gas_consumption = heat_load * 3600. * 1000 / boiler_thermal_efficiency / gas_heat_value
    gas_steam_ratio = 1000. * (steam_h - water_supply_h) / boiler_thermal_efficiency / gas_heat_value
    return (steam_t_sat, steam_production, gas_consumption, gas_steam_ratio)


def gas_steam_boiler_reverse(
    steam_production, steam_pressure=0.4, steam_temperature=190, excess_air_coefficient=1.15, air_temperature=20, air_h=25.974,
    water_supply_temperature=20, gas_heat_value=40000, boiler_thermal_efficiency=0.89, blowdown_rate=0.02
):
    '''
    1.3燃气蒸汽锅炉计算
    input (
        产汽量t/h, 汽包压力=0.4Mpa, 过热蒸汽温度=190℃, 过量空气系数=1.15, 空气温度=20, 空气焓值=25.974,
        锅炉给水温度=20℃, 天燃气热值=36000KJ/Nm³, 锅炉热效率=89%, 排污率=2%
    )
    return (饱和蒸汽温度℃, 燃气耗量Nm³/h, 燃气耗量/产汽量比值)
    '''
    steam_h = seuif97.pt2h(steam_pressure, steam_temperature)
    steam_t_sat = seuif97.tsat_p(steam_pressure * 10)
    water_supply_h = seuif97.pt2h(steam_pressure, water_supply_temperature)
    water_h_sat = seuif97.HL_P(steam_pressure * 10)
    gas_flow = (1000 * ((steam_h - water_supply_h) + blowdown_rate * (water_h_sat - water_supply_h))) * steam_production / boiler_thermal_efficiency / gas_heat_value
    gas_steam_ratio = gas_flow / steam_production
    return (steam_t_sat, gas_flow, gas_steam_ratio)


def steam_waste_heat_boiler(gas_flow, gas_in_temp, gas_out_temp=100, gas_specific_heat=1.2, steam_pressure=0.4, steam_temperature=190, water_supply_temperature=20, boiler_thermal_efficiency=0.89):
    '''
    蒸汽余热锅炉计算
    input (烟气流量kg/h, 烟气进口温度℃, 烟气出口温度=100℃, 烟气比热=1.2kJ/(kg·℃), 蒸汽压力=0.4Mpa, 蒸汽温度=190℃, 给水温度=20℃, 锅炉热效率=89%)
    return (饱和蒸汽温度℃, 饱和蒸汽压力Mpa, 蒸汽焓值kJ/kg, 产汽量t/h)
    '''
    gas_heat = gas_specific_heat * gas_flow * (gas_in_temp - gas_out_temp)
    steam_h = seuif97.pt2h(steam_pressure, steam_temperature)
    steam_t_sat = seuif97.tsat_p(steam_pressure * 10)
    water_supply_h = seuif97.pt2h(steam_pressure, water_supply_temperature)
    steam_production = gas_heat * boiler_thermal_efficiency / (steam_h - water_supply_h) / 1000
    return (steam_t_sat, steam_pressure, steam_h, steam_production)


def hot_water_waste_heat_boiler(gas_flow, gas_in_temp, gas_out_temp=100, gas_specific_heat=1.2, hot_water_pressure=0.7, hot_water_in_temperature=70, hot_water_out_temperature=95, boiler_thermal_efficiency=0.91):
    '''
   余热热水锅炉计算
    input (烟气流量kg/h, 烟气进口温度℃, 烟气出口温度=100℃, 烟气比热=1.2kJ/(kg·℃), 热水压力=0.7Mpa, 热水进水温度=70℃, 热水出水温度=95℃, 锅炉效率=91%)
    return (热水出水温度℃, 热水量t/h, 烟气热量kW)
    '''
    gas_heat = gas_specific_heat * gas_flow * (gas_in_temp - gas_out_temp)
    water_in_h = seuif97.pt2h(hot_water_pressure, hot_water_in_temperature)
    water_out_h = seuif97.pt2h(hot_water_pressure, hot_water_out_temperature)
    hot_water_yield = gas_heat * boiler_thermal_efficiency / (water_out_h - water_in_h) / 1000.0
    return (hot_water_out_temperature, hot_water_yield, gas_heat / 3600.0)


def get_gas_turbine_props(props_str):
    '''
    燃气轮机的烟气参数获取
    input(燃气轮机属性json字符串)
    return(锅炉烟气流量t/h, 燃机排烟温度℃)
    '''
    device_prop_json = json.loads(props_str)
    gas_flow_index = device_prop_json[u'prop_name'].index(u'锅炉烟气流量')
    if device_prop_json[u'prop_value'][gas_flow_index]:
        gas_flow = float(device_prop_json[u'prop_value'][gas_flow_index])
    else:
        gas_flow = 0
    out_temp_index = device_prop_json[u'prop_name'].index(u'燃机排烟温度')
    if device_prop_json[u'prop_value'][out_temp_index]:
        out_temp = float(device_prop_json[u'prop_value'][out_temp_index])
    else:
        out_temp = 0
    return (gas_flow, out_temp)


def gas_boiler_param_calculate(mode=1):
    if mode == 1:
        # 燃气热水锅炉
        if boiler_params['1']:
            return gas_hot_water_boiler(
                1,
                hot_water_pressure=boiler_params['1'][u'热水压力'],
                hot_water_in_temperature=boiler_params['1'][u'热水进水温度'],
                hot_water_out_temperature=boiler_params['1'][u'热水出水温度'],
                gas_heat_value=boiler_params['1'][u'燃气热值'],
                boiler_thermal_efficiency=boiler_params['1'][u'锅炉效率']
            )
        else:
            return (0, 0, 0)
    elif mode == 2:
        # 燃气蒸汽锅炉
        if boiler_params['2']:
            return gas_steam_boiler_reverse(
                1,
                steam_pressure=boiler_params['2'][u'汽包压力'],
                steam_temperature=boiler_params['2'][u'过热蒸汽温度'],
                excess_air_coefficient=boiler_params['2'][u'过量空气系数'],
                air_temperature=boiler_params['2'][u'空气温度'],
                air_h=boiler_params['2'][u'空气焓值'],
                water_supply_temperature=boiler_params['2'][u'锅炉给水温度'],
                gas_heat_value=boiler_params['2'][u'天然气热值'],
                boiler_thermal_efficiency=boiler_params['2'][u'锅炉热效率'],
                blowdown_rate=boiler_params['2'][u'排污率']
            )
        else:
            return (0, 0, 0)
    return


def waste_heat_boiler_calculate(gas_flow, gas_in_temp, mode=1):
    if mode == 1:
        # 余热热水锅炉
        if boiler_params['3']:
            return hot_water_waste_heat_boiler(
                gas_flow, gas_in_temp,
                gas_out_temp=boiler_params['3'][u'烟气出口温度'],
                gas_specific_heat=boiler_params['3'][u'烟气比热'],
                hot_water_pressure=boiler_params['3'][u'热水压力'],
                hot_water_in_temperature=boiler_params['3'][u'热水进水温度'],
                hot_water_out_temperature=boiler_params['3'][u'热水出水温度'],
                boiler_thermal_efficiency=boiler_params['3'][u'锅炉效率']
            )
        else:
            return (0, 0, 0)
    elif mode == 2:
        # 余热蒸汽锅炉
        if boiler_params['4']:
            return steam_waste_heat_boiler(
                gas_flow, gas_in_temp,
                gas_out_temp=boiler_params['4'][u'烟气出口温度'],
                gas_specific_heat=boiler_params['4'][u'烟气比热'],
                steam_pressure=boiler_params['4'][u'蒸汽压力'],
                steam_temperature=boiler_params['4'][u'蒸汽温度'],
                water_supply_temperature=boiler_params['4'][u'给水温度'],
                boiler_thermal_efficiency=boiler_params['4'][u'锅炉热效率'],
            )
        else:
            return (0, 0, 0)
    return


def get_internal_combustion_engine_props(props_str, number=1):
    '''
    内燃机的烟气参数获取
    input(内燃机属性json字符串, 内燃机数量=1)
    return(排烟温度℃, 质量流量，湿kg/h, 排烟可利用功率kW, 高温水可利用功率kW)
    '''
    device_prop_json = json.loads(props_str)
    exhaust_gas_temperature_index = device_prop_json[u'prop_name'].index(u'排烟温度')
    exhaust_gas_temperature = float(device_prop_json[u'prop_value'][exhaust_gas_temperature_index])
    mass_flow_rate_index = device_prop_json[u'prop_name'].index(u'质量流量，湿')
    mass_flow_rate = number * float(device_prop_json[u'prop_value'][mass_flow_rate_index])
    exhaust_gas_available_power_index = device_prop_json[u'prop_name'].index(u'排烟可利用功率')
    exhaust_gas_available_power = number * float(device_prop_json[u'prop_value'][exhaust_gas_available_power_index])
    hot_water_available_power_index = device_prop_json[u'prop_name'].index(u'高温水可利用功率')
    hot_water_available_power = number * float(device_prop_json[u'prop_value'][hot_water_available_power_index])
    return (exhaust_gas_temperature, mass_flow_rate, exhaust_gas_available_power, hot_water_available_power)


def get_heat_pump_data(space, sewage_flow, hp_type, djzd=16, js=120, dmjshrl=50):
    '''
    获取热泵数据dict，包括了地源热泵和水源热泵两种情况，如果类型不是1~4中的一种则返回None
    '''
    heat_pump_data = {'cool_power': 0, 'heat_power': 0, 'ele_power_1': 0, 'ele_power_2': 0}
    if hp_type == '1' or hp_type == '3':
        cool_power, heat_power, electric_N1, electric_N2 = get_ground_source_heat_pump_data(space, dmjshrl, js, djzd)
        heat_pump_data['cool_power'] = cool_power
        heat_pump_data['heat_power'] = heat_power
        heat_pump_data['ele_power_1'] = electric_N1
        heat_pump_data['ele_power_2'] = electric_N2
    elif hp_type == '2':
        cool_Q1, heat_Q2, electric_N1, electric_N2 = get_sewage_source_heat_pump_data(sewage_flow)
        heat_pump_data['cool_power'] = cool_Q1
        heat_pump_data['heat_power'] = heat_Q2
        heat_pump_data['ele_power_1'] = electric_N1
        heat_pump_data['ele_power_2'] = electric_N2
    elif hp_type == '4':
        cool_Q1, heat_Q2, electric_N1, electric_N2 = get_sewage_source_heat_pump_data(sewage_flow)
        heat_pump_data['cool_power'] = cool_Q1
        heat_pump_data['heat_power'] = heat_Q2
        heat_pump_data['ele_power_1'] = electric_N1
        heat_pump_data['ele_power_2'] = electric_N2
    else:
        heat_pump_data = None
    return heat_pump_data


def get_ground_source_heat_pump_data(space, dmjshrl=50, js=120, djzd=16):
    '''
    根据热泵占地面积获取热泵功率数据
    input(占地面积, 单米井深换热量(w), 井深(m),单井占地(㎡))
    '''
    # 空调制冷量(kW)
    cool_power = space / djzd * js * dmjshrl / 1000. / (1 + 0.03) / (1 + 1. / AlgoConstants.ground_heat_pump_cool_cop)
    # 供热量(kW)
    heat_power = space / djzd * js * dmjshrl / 1000. / (1 + 0.03) / (1 + 1. / AlgoConstants.ground_heat_pump_heat_cop)
    # 电功率N1(kW)
    electric_N1 = cool_power / AlgoConstants.ground_heat_pump_cool_cop
    # 电功率N2(kW)
    electric_N2 = heat_power / AlgoConstants.ground_heat_pump_heat_cop
    return cool_power, heat_power, electric_N1, electric_N2


def get_sewage_source_heat_pump_data(sewage_flow):
    '''
    根据污水流量获取污水源热泵数据
    input(污水流量t/h)
    '''
    # 污水放热Q(J)
    sewage_Q = 4180 * sewage_flow * 5 * 1000 / 24.
    # 制冷量Q1(kW)
    cool_Q1 = AlgoConstants.sewage_heat_pump_cool_cop / (AlgoConstants.sewage_heat_pump_cool_cop + 1) * sewage_Q / 3600000.
    # 供热量(kW)
    heat_Q2 = AlgoConstants.sewage_heat_pump_heat_cop / (AlgoConstants.sewage_heat_pump_heat_cop - 1) * sewage_Q / 3600000.
    # 电功率N1(kW)
    electric_N1 = cool_Q1 / AlgoConstants.sewage_heat_pump_cool_cop
    # 电功率N2(kW)
    electric_N2 = heat_Q2 / AlgoConstants.sewage_heat_pump_heat_cop
    return cool_Q1, heat_Q2, electric_N1, electric_N2


def init_waste_heat_device_dict(device_class, device_type, device_id, load, number=1, props_str=None):
    '''
    将余热设备做成dict形式
    input(设备大类, 设备小类, 设备ID, 设备输出, 设备属性json字符串)
    return(dict)
    '''
    return {
        u'device_class': str(device_class) if device_class else None,
        u'device_type': str(device_type) if device_type else None,
        u'device_id': device_id,
        u'load': load,
        u'number': number,
        u'props': props_str
    }


def is_disabled_device(device_class, device_type=None, disabled_devices=[]):
    '''
    判断是否是禁用的设备
    '''
    device_class_list = list(map(lambda x: x['device_class'], disabled_devices))
    device_type_list = list(map(lambda x: x['device_type'], disabled_devices))
    if device_type:
        if str(device_class) in device_class_list and str(device_type) in device_type_list:
            return False
    else:
        if str(device_class) in device_class_list:
            return False
    return True


def get_peak_devices(used_devices_list):
    '''
    获取调峰设备是否勾选
    '''
    global boiler_params
    peak_devices = {}
    used_devices_class_list = list(map(lambda x: x['device_class'], used_devices))
    if u'2' in used_devices_class_list:
        peak_devices['cool'] = True
    else:
        peak_devices['cool'] = False
    if boiler_params['1']:
        peak_devices['hot_water'] = True
        peak_devices['heat'] = True
    else:
        peak_devices['hot_water'] = False
        peak_devices['heat'] = False
    if boiler_params['2']:
        peak_devices['steam'] = True
    else:
        peak_devices['steam'] = False
    if u'10' in used_devices_class_list:
        peak_devices['electric'] = True
    else:
        peak_devices['electric'] = False
    return peak_devices


def create_front_waste_heat_device_dict(waste_type):
    '''
    将余热设备转换成前台能解析的json数据
    input(余热类型)
    return(dict)
    '''
    if waste_type:
        return {
            u'device_class': waste_type['device_class'] if waste_type['device_class'] else None,
            u'device_type': waste_type['device_type'] if waste_type['device_type'] else None,
            u'device_id': waste_type['device_id'],
            u'load': float(waste_type['load']),
            u'number': waste_type['number'],
            u'props': json.loads(waste_type['props']) if waste_type['props'] else None
        }
    else:
        return None


def waste_heat_gas_turbine_steam(steam_production, disabled_devices=[]):
    '''
    燃气轮机
    蒸汽 匹配余热设备
    蒸汽型余热锅炉
    input(产汽量t/h)
    '''
    waste_heat = {
        u'steam': init_waste_heat_device_dict(7, 5, None, steam_production),
        u'cool': None,
        u'heat': None,
        u'heat_plate': None,
        u'hot_water': None,
        u'air': None,
        u'mix': None,
        u'waste_type': '1'
    }
    if not is_disabled_device(7, 5, disabled_devices):
        waste_heat_device.append(waste_heat)


def waste_heat_gas_turbine_steam_cool(steam_p_sat, steam_production, need_cool_power, mode=1, disabled_devices=[]):
    '''
    燃气轮机
    蒸汽&制冷 匹配余热设备
    蒸汽型余热锅炉+蒸汽型溴化锂
    input(饱和蒸汽压力Mpa, 产汽量t/h, 需求冷功率kW, mode=1)
    mode=1 蒸汽+制冷
    mode=2 制冷
    '''
    disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
    min_cool_power_device = Device.query.order_by(Device.main_prop_value_1.asc()).filter(Device.device_class == '1').limit(1)
    if (min_cool_power_device is not None) and (min_cool_power_device[0].main_prop_value_1 > need_cool_power):
        matched_devices_waste_heat = min_cool_power_device
    else:
        matched_devices_waste_heat = Device.query.filter(
            and_(
                Device.device_class == '1',
                or_(
                    and_(
                        Device.main_prop_value_1 <= need_cool_power,
                        Device.main_prop_name_2 == '蒸汽消耗量',
                        Device.main_prop_value_2 <= steam_production * 1000,
                        Device.main_prop_value_3 == steam_p_sat
                    ) & disabled_devices_conditions
                )
            )
        ).all()
    for device in matched_devices_waste_heat:
        number = math.ceil(steam_production * 1000 / float(device.main_prop_value_2))
        if mode == 1:
            steam = steam_production - device.main_prop_value_2 * number / 1000.
            waste_heat = {
                u'steam': init_waste_heat_device_dict(7, 5, None, steam),
                u'cool': init_waste_heat_device_dict(1, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '1'
            }
        if mode == 2:
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(1, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '1'
            }
        if mode == 1:
            if not is_disabled_device(7, 5, disabled_devices):
                waste_heat_device.append(waste_heat)
        else:
            waste_heat_device.append(waste_heat)


def waste_heat_gas_turbine_cool(gas_flow, gas_in_temp, gas_out_temp=120, gas_specific_heat=1.2, mode=1, disabled_devices=[]):
    '''
    燃气轮机
    制冷&供暖 匹配余热设备
    烟气溴化锂
    input (烟气流量t/h, 烟气进口温度℃, 烟气出口温度=120℃, 烟气比热=1.2kJ/(kg·℃), mode=1)
    mode=1 制冷
    mode=2 制冷+供暖
    '''
    # TODO 烟气溴化锂的选择方法，最大输出如果仍不满足则可以超过5台
    disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
    # 燃机排烟烟气需要通过锅炉中计算烟气热量的公式, t/h * ℃ * kJ/(kg·℃)=t*kJ/(h·kg), 乘以系数得到制冷功率
    exhaust_gas_available_power = gas_flow * (gas_in_temp - gas_out_temp) * gas_specific_heat * 1000 / 3600. * AlgoConstants.exhaust_gas_available_power_coefficient
    max_cool_power_device = Device.query.order_by(Device.main_prop_value_1.desc()).filter(
        and_(
            Device.device_class == '1',
            or_(
                and_(
                    Device.device_type == '8',
                    Device.main_prop_name_1 == '制冷量'
                ),
                and_(
                    Device.device_type == '9',
                    Device.main_prop_name_1 == '烟气直燃同时运转'
                )
            )
        ) & disabled_devices_conditions
    ).limit(1)
    if max_cool_power_device and max_cool_power_device[0].main_prop_value_1 * 5 <= exhaust_gas_available_power:
        matched_devices_waste_heat = max_cool_power_device
        if mode == 1:
            for device in matched_devices_waste_heat:
                number = math.ceil(exhaust_gas_available_power / float(device.main_prop_value_1))
                waste_heat = {
                    u'steam': None,
                    u'cool': init_waste_heat_device_dict(1, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                    u'heat': None,
                    u'heat_plate': None,
                    u'hot_water': None,
                    u'air': None,
                    u'mix': None,
                    u'waste_type': '2'
                }
                waste_heat_device.append(waste_heat)
        if mode == 2:
            for device in matched_devices_waste_heat:
                number_cold = math.ceil(exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient / float(device.main_prop_value_1))
                number_heat = math.ceil(exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient / float(device.main_prop_value_2))
                waste_heat = {
                    u'steam': None,
                    u'cool': init_waste_heat_device_dict(1, device.device_type, device.id, device.main_prop_value_1, number=max(number_cold, number_heat), props_str=device.props_json),
                    u'heat': init_waste_heat_device_dict(1, device.device_type, device.id, device.main_prop_value_2, number=max(number_cold, number_heat), props_str=device.props_json),
                    u'heat_plate': None,
                    u'hot_water': None,
                    u'air': None,
                    u'mix': None,
                    u'waste_type': '2'
                }
                waste_heat_device.append(waste_heat)
    else:
        if mode == 1:
            matched_devices_waste_heat = Device.query.filter(
                and_(
                    Device.device_class == '1',
                    or_(
                        and_(
                            Device.device_type == '8',
                            Device.main_prop_name_1 == '制冷量',
                            Device.main_prop_value_1 <= exhaust_gas_available_power,
                            Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number >= exhaust_gas_available_power
                        ) & disabled_devices_conditions,
                        and_(
                            Device.device_type == '9',
                            Device.main_prop_name_1 == '烟气直燃同时运转',
                            Device.main_prop_value_1 <= exhaust_gas_available_power,
                            Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number >= exhaust_gas_available_power
                        ) & disabled_devices_conditions
                    )
                )
            ).all()
            for device in matched_devices_waste_heat:
                number = math.ceil(exhaust_gas_available_power / float(device.main_prop_value_1))
                waste_heat = {
                    u'steam': None,
                    u'cool': init_waste_heat_device_dict(1, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                    u'heat': None,
                    u'heat_plate': None,
                    u'hot_water': None,
                    u'air': None,
                    u'mix': None,
                    u'waste_type': '2'
                }
                waste_heat_device.append(waste_heat)
        if mode == 2:
            matched_devices_waste_heat = Device.query.filter(
                and_(
                    Device.device_class == '1',
                    or_(
                        and_(
                            Device.device_type == '8',
                            Device.main_prop_name_1 == '制冷量',
                            Device.main_prop_value_1 <= exhaust_gas_available_power,
                            Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number >= exhaust_gas_available_power,
                            Device.main_prop_value_2 <= exhaust_gas_available_power,
                        ) & disabled_devices_conditions,
                        and_(
                            Device.device_type == '9',
                            Device.main_prop_name_1 == '烟气直燃同时运转',
                            Device.main_prop_value_1 <= exhaust_gas_available_power,
                            Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number >= exhaust_gas_available_power,
                            Device.main_prop_value_2 <= exhaust_gas_available_power
                        ) & disabled_devices_conditions
                    )
                )
            ).all()
            for device in matched_devices_waste_heat:
                number_cold = math.ceil(exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient / float(device.main_prop_value_1))
                number_heat = math.ceil(exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient / float(device.main_prop_value_2))
                waste_heat = {
                    u'steam': None,
                    u'cool': init_waste_heat_device_dict(1, device.device_type, device.id, device.main_prop_value_1, number=max(number_cold, number_heat), props_str=device.props_json),
                    u'heat': init_waste_heat_device_dict(1, device.device_type, device.id, device.main_prop_value_2, number=max(number_cold, number_heat), props_str=device.props_json),
                    u'heat_plate': None,
                    u'hot_water': None,
                    u'air': None,
                    u'mix': None,
                    u'waste_type': '2'
                }
                waste_heat_device.append(waste_heat)


def waste_heat_gas_turbine_steam_heat_hot_water(steam_h_sat, steam_production, mode=1, disabled_devices=[]):
    '''
    燃气轮机
    蒸汽&热水&供暖 匹配余热设备
    蒸汽型余热锅炉+板换
    input(饱和蒸汽焓值kJ/kg，产汽量t/h, mode=1)
    mode=1 蒸汽+热水
    mode=2 蒸汽+供暖
    '''
    if mode == 1:
        # 1m3/h=700kW, 1kJ/h=1/3600kJ/s=1/3600kW
        gas_heat = steam_h_sat * steam_production * 1000
        hot_water = gas_heat * AlgoConstants.plate_type_heat_exchanger_efficiency / 3600 / 700.0
        waste_heat = {
            u'steam': init_waste_heat_device_dict(8, 5, None, steam_production),
            u'cool': None,
            u'heat': None,
            u'heat_plate': None,
            u'hot_water': init_waste_heat_device_dict(8, 5, None, hot_water),
            u'air': None,
            u'mix': {u'steam': steam_production, u'hot_water': hot_water},
            u'waste_type': '1'
        }
    if mode == 2:
        # kJ/h
        gas_heat = steam_h_sat * steam_production * 1000
        waste_heat = {
            u'steam': init_waste_heat_device_dict(8, 5, None, steam_production),
            u'cool': None,
            u'heat': None,
            u'heat_plate': init_waste_heat_device_dict(8, 5, None, gas_heat * AlgoConstants.plate_type_heat_exchanger_efficiency / 3600),
            u'hot_water': None,
            u'air': None,
            u'mix': {u'steam': steam_production, u'heat_plate': gas_heat * AlgoConstants.plate_type_heat_exchanger_efficiency / 3600},
            u'waste_type': '1'
        }
    if not is_disabled_device(8, 5, disabled_devices):
        waste_heat_device.append(waste_heat)


def waste_heat_gas_turbine_heat_hot_water(hot_water_yield, gas_heat, mode=1, disabled_devices=[]):
    '''
    燃气轮机
    供暖&热水 匹配余热设备
    余热热水锅炉
    input(热水量t/h, 烟气热量kW, mode=1)
    mode=1 供暖+热水
    mode=2 供暖
    mode=3 热水
    '''
    if mode == 1:
        waste_heat = {
            u'steam': None,
            u'cool': None,
            u'heat': None,
            u'heat_plate': init_waste_heat_device_dict(8, 4, None, gas_heat),
            u'hot_water': init_waste_heat_device_dict(8, 4, None, hot_water_yield),
            u'air': None,
            u'mix': {u'heat_plate': gas_heat, u'hot_water': hot_water_yield},
            u'waste_type': '3'
        }
    if mode == 2:
        waste_heat = {
            u'steam': None,
            u'cool': None,
            u'heat': None,
            u'heat_plate': init_waste_heat_device_dict(8, 4, None, gas_heat),
            u'hot_water': None,
            u'air': None,
            u'mix': None,
            u'waste_type': '3'
        }
    if mode == 3:
        waste_heat = {
            u'steam': None,
            u'cool': None,
            u'heat': None,
            u'heat_plate': None,
            u'hot_water': init_waste_heat_device_dict(8, 4, None, hot_water_yield),
            u'air': None,
            u'mix': None,
            u'waste_type': '3'
        }
    if not is_disabled_device(8, 4, disabled_devices):
        waste_heat_device.append(waste_heat)


def waste_heat_gas_turbine_heat_cool_hot_water(matched_devices_waste_heat, hot_water_yield, mode=1, disabled_devices=[]):
    '''
    燃气轮机
    供暖&制冷&热水 匹配余热设备
    余热热水锅炉+温水型溴化锂
    input(温水型溴化锂设备list, 热水量t/h, mode=1)
    mode=1 制冷+供暖+热水
    mode=2 制冷+供暖
    mode=3 制冷+热水
    mode=4 制冷
    '''
    # 1m3/h=700kW
    for device in matched_devices_waste_heat:
        number = math.ceil(hot_water_yield / float(device.main_prop_value_2))
        hot_water_yield_left = hot_water_yield
        hot_water_heat_left = hot_water_yield_left * 700.0
        if mode == 1:
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': init_waste_heat_device_dict(8, 4, None, hot_water_heat_left),
                u'hot_water': init_waste_heat_device_dict(8, 4, None, hot_water_yield_left),
                u'air': None,
                u'mix': {u'heat_plate': hot_water_heat_left, u'hot_water': hot_water_yield_left},
                u'waste_type': '3'
            }
        elif mode == 2:
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': init_waste_heat_device_dict(8, 4, None, hot_water_heat_left),
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '3'
            }
        elif mode == 3:
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': init_waste_heat_device_dict(8, 4, None, hot_water_yield_left),
                u'air': None,
                u'mix': None,
                u'waste_type': '3'
            }
        elif mode == 4:
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '3'
            }
        if mode != 4:
            if not is_disabled_device(8, 4, disabled_devices):
                waste_heat_device.append(waste_heat)
        else:
            waste_heat_device.append(waste_heat)


def waste_heat_gas_turbine_steam_cool_heat_hot_water(steam_p_sat, steam_h_sat, steam_production, need_cool_power, mode=1, disabled_devices=[]):
    '''
    燃气轮机
    蒸汽&供暖&制冷&生活热水 匹配余热设备
    根据mode选择不同的需求组合模式
    余热蒸汽锅炉+蒸汽型溴化锂+板换
    input(饱和蒸汽压力Mpa, 饱和蒸汽焓值kJ/kg, 产汽量t/h, 需求冷功率kW, mode=1)
    mode=1 供暖+制冷
    mode=2 蒸汽+制冷+暖
    mode=3 蒸汽+制冷+生活热水
    mode=4 制冷+生活热水
    '''
    disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
    min_cool_power_device = Device.query.order_by(Device.main_prop_value_1.asc()).filter(
        and_(
            Device.device_class == '1', Device.device_type == '1'
        ) & disabled_devices_conditions
    ).limit(1)
    if (min_cool_power_device is not None) and (min_cool_power_device[0].main_prop_value_1 > need_cool_power):
        matched_devices_waste_heat = min_cool_power_device
    else:
        matched_devices_waste_heat = Device.query.order_by(Device.main_prop_value_2.desc()).filter(
            and_(
                Device.device_class == '1', Device.device_type == '1',
                or_(
                    and_(
                        Device.main_prop_value_1 <= need_cool_power,
                        Device.main_prop_name_2 == '蒸汽消耗量',
                        Device.main_prop_value_2 <= steam_production * 1000,
                        Device.main_prop_value_3 == steam_p_sat
                    ) & disabled_devices_conditions
                )
            )
        ).limit(1)
    for device in matched_devices_waste_heat:
        number = math.ceil(steam_production / float(device.main_prop_value_2) / 1000.)
        # 余热锅炉产汽量减去匹配到的蒸汽溴化锂的蒸汽消耗量后，再计算热水热量进而得到供暖热量和热水热量
        # 1m3/h=700kW
        steam_production_left = steam_production
        # kJ/kg * t/h=kJ/kg * 1000kg/3600s=1000/3600(kJ/s)=1000/3600(kW)
        steam_heat_left = steam_h_sat * steam_production_left * AlgoConstants.plate_type_heat_exchanger_efficiency * 1000. / 3600.
        hot_water_left = steam_heat_left / 700.0
        waste_heat = {}
        if mode == 1:
            # 供暖+制冷
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': init_waste_heat_device_dict(8, 5, None, steam_heat_left),
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '1'
            }
        elif mode == 2:
            # 蒸汽+制冷+暖
            waste_heat = {
                u'steam': init_waste_heat_device_dict(8, 5, None, steam_production_left),
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': init_waste_heat_device_dict(8, 5, None, steam_heat_left),
                u'hot_water': None,
                u'air': None,
                u'mix': {u'steam': steam_production_left, u'heat_plate': steam_heat_left},
                u'waste_type': '1'
            }
        elif mode == 3:
            # 蒸汽+制冷+生活热水
            waste_heat = {
                u'steam': init_waste_heat_device_dict(8, 5, None, steam_production_left),
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': init_waste_heat_device_dict(8, 5, None, steam_heat_left),
                u'hot_water': None,
                u'air': None,
                u'mix': {u'steam': steam_production_left, u'hot_water': hot_water_left},
                u'waste_type': '1'
            }
        elif mode == 4:
            # 制冷+生活热水
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': init_waste_heat_device_dict(8, 5, None, hot_water_left),
                u'air': None,
                u'mix': None,
                u'waste_type': '1'
            }
        elif mode == 5:
            # 蒸汽+供暖
            waste_heat = {
                u'steam': init_waste_heat_device_dict(8, 5, None, steam_production_left),
                u'cool': None,
                u'heat': None,
                u'heat_plate': init_waste_heat_device_dict(8, 5, None, steam_heat_left),
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '1'
            }
        if not is_disabled_device(8, 5, disabled_devices):
            waste_heat_device.append(waste_heat)


def waste_heat_internal_combustion_engine_cool_heat(hot_water_available_power, exhaust_gas_available_power, mode=1, disabled_devices=[]):
    '''
    内燃机
    制冷&供暖 匹配余热设备
    烟气热水型溴化锂
    input(高温水可利用功率kW, 排烟可利用功率kW, mode=1)
    mode=1 制冷+供暖
    mode=2 制冷
    '''
    disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
    matched_devices_waste_heat = Device.query.filter(
        and_(
            or_(
                Device.device_class == '6',
                Device.device_class == '7'
            ),
            or_(
                and_(
                    Device.main_prop_name_1 == '制冷量',
                    Device.main_prop_value_1 <= (hot_water_available_power + exhaust_gas_available_power) * AlgoConstants.gas_LiBr_afterburning_coefficient
                ) & disabled_devices_conditions
            )
        )
    ).all()
    for device in matched_devices_waste_heat:
        number = math.ceil((hot_water_available_power + exhaust_gas_available_power) * AlgoConstants.gas_LiBr_afterburning_coefficient / float(device.main_prop_value_1))
        waste_heat = {}
        if mode == 1:
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_2, number=number, props_str=device.props_json),
                u'heat_plate': None,
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '4'
            }
        elif mode == 2:
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '4'
            }
        waste_heat_device.append(waste_heat)


def waste_heat_internal_combustion_engine_cool_heat_hot_water(gas_consumption, mode=1, disabled_devices=[]):
    '''
    内燃机
    制冷&供暖&热水 匹配余热设备
    溴化锂吸收式直燃型三用机
    input(天然气耗量Nm³/h, mode=1)
    mode=1 制冷+热水
    mode=2 供暖+热水
    '''
    disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
    if mode == 1:
        matched_devices_waste_heat = Device.query.filter(
            and_(
                or_(
                    Device.device_class == '10'
                ),
                or_(
                    and_(Device.main_prop_name_4 == '天然气Nm³/h', Device.main_prop_value_4 <= gas_consumption) & disabled_devices_conditions
                )
            )
        ).all()
        for device in matched_devices_waste_heat:
            number = math.ceil(gas_consumption / float(device.main_prop_value_4))
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_3, number=number, props_str=device.props_json),
                u'air': None,
                u'mix': None,
                u'waste_type': '5'
            }
            waste_heat_device.append(waste_heat)
    elif mode == 2:
        matched_devices_waste_heat = Device.query.filter(
            and_(
                or_(
                    Device.device_class == '10'
                ),
                or_(
                    and_(Device.main_prop_name_5 == '天然气Nm³/h', Device.main_prop_value_5 <= gas_consumption) & disabled_devices_conditions
                )
            )
        ).all()
        for device in matched_devices_waste_heat:
            number = math.ceil(gas_consumption / float(device.main_prop_value_5))
            waste_heat = {
                u'steam': None,
                u'cool': None,
                u'heat': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_2, number=number, props_str=device.props_json),
                u'heat_plate': None,
                u'hot_water': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_3, number=number, props_str=device.props_json),
                u'air': None,
                u'mix': None,
                u'waste_type': '5'
            }
            waste_heat_device.append(waste_heat)


def waste_heat_internal_combustion_engine_cool_heat_hot_water_2(hot_water_available_power, exhaust_gas_available_power, mode=1, disabled_devices=[]):
    '''
    内燃机
    制冷&供暖&热水 匹配余热设备
    烟气型溴化锂+缸套水板换
    input(高温水可利用功率kW, 排烟可利用功率kW, mode=1)
    mode=1 制冷+供暖+热水
    mode=2 制冷+供暖
    mode=3 制冷+热水
    '''
    disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
    # 烟气溴化锂制冷或者供暖，缸套水可以供暖或者生活热水
    # 烟气溴化锂只能单独制冷或者供暖，但可以冬天供暖夏天制冷。缸套水可以同时供暖和生活热水
    # 高温水可回收功率×0.9=供暖或生活热水热量
    matched_devices_waste_heat = Device.query.filter(
        or_(
            and_(
                Device.device_type == '8', Device.main_prop_name_1 == '制冷量',
                Device.main_prop_value_1 <= exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient,
                Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number >= exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient
            ) & disabled_devices_conditions,
            and_(
                Device.device_type == '9', Device.main_prop_name_1 == '烟气直燃同时运转',
                Device.main_prop_value_1 <= exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient,
                Device.main_prop_value_1 * AlgoConstants.max_matched_devices_number >= exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient
            ) & disabled_devices_conditions
        )
    ).all()
    if mode == 1:
        for device in matched_devices_waste_heat:
            number = math.ceil(exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient / float(device.main_prop_value_1))
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_2, number=number, props_str=device.props_json),
                u'heat_plate': init_waste_heat_device_dict(None, None, None, hot_water_available_power * AlgoConstants.hot_water_available_power_coefficient),
                u'hot_water': init_waste_heat_device_dict(None, None, None, hot_water_available_power * AlgoConstants.hot_water_available_power_coefficient / 700.),
                u'air': None,
                u'mix': {u'heat_plate': hot_water_available_power * AlgoConstants.hot_water_available_power_coefficient, u'hot_water': hot_water_available_power * AlgoConstants.hot_water_available_power_coefficient / 700.},
                u'waste_type': '2'
            }
            waste_heat_device.append(waste_heat)
    elif mode == 2:
        for device in matched_devices_waste_heat:
            number = math.ceil(exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient / float(device.main_prop_value_1))
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_2, number=number, props_str=device.props_json),
                u'heat_plate': init_waste_heat_device_dict(None, None, None, hot_water_available_power * AlgoConstants.hot_water_available_power_coefficient),
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '2'
            }
            waste_heat_device.append(waste_heat)
    elif mode == 3:
        for device in matched_devices_waste_heat:
            number = math.ceil(exhaust_gas_available_power * AlgoConstants.exhaust_gas_available_power_coefficient / float(device.main_prop_value_1))
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': init_waste_heat_device_dict(None, None, None, hot_water_available_power * AlgoConstants.hot_water_available_power_coefficient / 700.),
                u'air': None,
                u'mix': None,
                u'waste_type': '2'
            }
            waste_heat_device.append(waste_heat)


def waste_heat_internal_combustion_engine_cool_heat_hot_water_3(hot_water_yield, gas_heat, mode=1, disabled_devices=[]):
    '''
    内燃机
    制冷&供暖&热水 匹配余热设备
    余热热水锅炉+板换
    input(温水型溴化锂设备list, 热水量t/h, mode=1)
    mode=1 供暖+热水
    mode=2 供暖
    mode=3 热水
    '''
    hot_water_yield_left = hot_water_yield
    hot_water_heat_left = hot_water_yield_left * 700.0
    if mode == 1:
        waste_heat = {
            u'steam': None,
            u'cool': None,
            u'heat': None,
            u'heat_plate': init_waste_heat_device_dict(8, 4, None, hot_water_heat_left),
            u'hot_water': init_waste_heat_device_dict(8, 4, None, hot_water_yield_left),
            u'air': None,
            u'mix': {u'heat_plate': hot_water_heat_left, u'hot_water': hot_water_yield_left},
            u'waste_type': '3'
        }
    elif mode == 2:
        waste_heat = {
            u'steam': None,
            u'cool': None,
            u'heat': None,
            u'heat_plate': init_waste_heat_device_dict(8, 4, None, hot_water_heat_left),
            u'hot_water': None,
            u'air': None,
            u'mix': None,
            u'waste_type': '3'
        }
    elif mode == 3:
        waste_heat = {
            u'steam': None,
            u'cool': None,
            u'heat': None,
            u'heat_plate': None,
            u'hot_water': init_waste_heat_device_dict(8, 4, None, hot_water_yield_left),
            u'air': None,
            u'mix': None,
            u'waste_type': '3'
        }
    if not is_disabled_device(8, 4, disabled_devices):
        waste_heat_device.append(waste_heat)


def waste_heat_internal_combustion_engine_steam(steam_production, disabled_devices=[]):
    '''
    内燃机
    蒸汽 匹配余热设备
    余热蒸汽锅炉
    input(产汽量t/h)
    '''
    waste_heat = {
        u'steam': init_waste_heat_device_dict(8, 5, None, steam_production),
        u'cool': None,
        u'heat': None,
        u'heat_plate': None,
        u'hot_water': None,
        u'air': None,
        u'mix': None,
        u'waste_type': '1'
    }
    if not is_disabled_device(8, 5, disabled_devices):
        waste_heat_device.append(waste_heat)


def waste_heat_internal_combustion_engine_steam_heat_hot_water(steam_h_sat, steam_production, mode=1, disabled_devices=[]):
    '''
    内燃机
    蒸汽&供暖&热水 匹配余热设备
    余热蒸汽锅炉+板换
    input(饱和蒸汽焓值kJ/kg, 产汽量t/h, mode=1)
    mode=1 蒸汽+热水
    mode=2 蒸汽+供暖
    mode=3 蒸汽+供暖+热水
    '''
    # kJ/kg * t/h=1000/3600(kW)
    steam_heat_all = steam_h_sat * steam_production * AlgoConstants.plate_type_heat_exchanger_efficiency * 1000 / 3600.
    hot_water = steam_heat_all / 700.
    if mode == 1:
        waste_heat = {
            u'steam': init_waste_heat_device_dict(8, 5, None, steam_production),
            u'cool': None,
            u'heat': None,
            u'heat_plate': None,
            u'hot_water': init_waste_heat_device_dict(8, 5, None, hot_water),
            u'air': None,
            u'mix': {u'steam': steam_production, u'hot_water': hot_water},
            u'waste_type': '1'
        }
    elif mode == 2:
        waste_heat = {
            u'steam': init_waste_heat_device_dict(8, 5, None, steam_production),
            u'cool': None,
            u'heat': None,
            u'heat_plate': init_waste_heat_device_dict(8, 5, None, steam_heat_all),
            u'hot_water': None,
            u'air': None,
            u'mix': {u'steam': steam_production, u'heat_plate': steam_heat_all},
            u'waste_type': '1'
        }
    elif mode == 3:
        waste_heat = {
            u'steam': init_waste_heat_device_dict(8, 5, None, steam_production),
            u'cool': None,
            u'heat': None,
            u'heat_plate': init_waste_heat_device_dict(8, 5, None, steam_heat_all),
            u'hot_water': init_waste_heat_device_dict(8, 5, None, hot_water),
            u'air': None,
            u'mix': {u'steam': steam_production, u'heat_plate': steam_heat_all, u'hot_water': hot_water},
            u'waste_type': '1'
        }
    if not is_disabled_device(8, 5, disabled_devices):
        waste_heat_device.append(waste_heat)


def waste_heat_internal_combustion_engine_steam_cool(steam_h_sat, steam_production, disabled_devices=[]):
    '''
    内燃机
    蒸汽&制冷 匹配余热设备
    余热蒸汽锅炉+蒸汽型溴化锂
    input(饱和蒸汽焓值kJ/kg, 产汽量t/h)
    '''
    disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
    matched_devices_waste_heat = Device.query.filter(
        and_(
            Device.device_class == '1',
            or_(
                and_(Device.main_prop_name_2 == '蒸汽消耗量', Device.main_prop_value_2 <= steam_production * 1000) & disabled_devices_conditions
            )
        )
    ).all()
    for device in matched_devices_waste_heat:
        number = math.ceil(steam_production * 1000 / float(device.main_prop_value_2))
        waste_heat = {
            u'steam': init_waste_heat_device_dict(8, 5, None, steam_production),
            u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
            u'heat': None,
            u'heat_plate': None,
            u'hot_water': None,
            u'air': None,
            u'mix': None,
            u'waste_type': '1'
        }
        if not is_disabled_device(8, 5, disabled_devices):
            waste_heat_device.append(waste_heat)


def waste_heat_internal_combustion_engine_steam_cool_heat_hot_water(steam_h_sat, steam_production, mode=1):
    '''
    内燃机
    蒸汽&制冷&供暖&热水 匹配余热设备
    余热蒸汽锅炉+蒸汽型溴化锂+板换
    input(饱和蒸汽焓值kJ/kg, 产汽量t/h)
    mode=1 蒸汽+制冷+供暖
    mode=2 蒸汽+制冷+热水
    '''
    matched_devices_waste_heat = Device.query.filter(
        and_(
            Device.device_class == '1',
            or_(
                and_(Device.main_prop_name_2 == '蒸汽消耗量', Device.main_prop_value_2 <= steam_production * 1000)
            )
        )
    ).all()
    for device in matched_devices_waste_heat:
        number = math.ceil(steam_production * 1000 / float(device.main_prop_value_2))
        # 1m3/h=700kW
        steam_production_left = steam_production
        # kJ/kg * t/h=1000/3600(kW)
        steam_heat_left = steam_h_sat * steam_production_left * AlgoConstants.plate_type_heat_exchanger_efficiency * 1000. / 3600.
        hot_water_left = steam_heat_left / 700.0
        if mode == 1:
            waste_heat = {
                u'steam': init_waste_heat_device_dict(8, 5, None, steam_production_left),
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': init_waste_heat_device_dict(8, 5, None, steam_heat_left),
                u'hot_water': None,
                u'air': None,
                u'mix': {u'steam': steam_production_left, u'heat_plate': steam_heat_left},
                u'waste_type': '1'
            }
        elif mode == 2:
            waste_heat = {
                u'steam': init_waste_heat_device_dict(8, 5, None, steam_production_left),
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': None,
                u'heat_plate': None,
                u'hot_water': init_waste_heat_device_dict(8, 5, None, hot_water_left),
                u'air': None,
                u'mix': {u'steam': steam_production_left, u'hot_water': hot_water_left},
                u'waste_type': '1'
            }
        waste_heat_device.append(waste_heat)


def search_warm_water_type_lithium(hot_water_temperature, hot_water_yield, disabled_devices=[]):
    '''
    燃气轮机
    余热热水锅炉+温水型溴化锂
    根据温度搜索温水型溴化锂设备
    input(温度℃, 热水量t/h)
    '''
    disabled_devices_conditions = get_disabled_devices_conditions(disabled_devices)
    temp = []
    if hot_water_temperature >= 100:
        # 高温
        temp.append('2')
        temp.append('5')
    else:
        # 低温
        temp.append('3')
        temp.append('4')
    min_cool_power_device = Device.query.order_by(Device.main_prop_value_2.asc()).filter(
        and_(
            Device.device_class == '1',
            or_(
                Device.device_type == temp[0], Device.device_type == temp[1]
            )
        )
    ).limit(1)
    if (min_cool_power_device is not None) and (min_cool_power_device[0].main_prop_value_2 > hot_water_yield):
        matched_devices_waste_heat = min_cool_power_device
    else:
        matched_devices_waste_heat = Device.query.filter(
            and_(
                Device.device_class == '1',
                or_(
                    Device.device_type == temp[0], Device.device_type == temp[1]
                ),
                or_(
                    Device.main_prop_value_2 <= hot_water_yield
                )
            ) & disabled_devices_conditions
        ).all()
    return matched_devices_waste_heat


def waste_heat_device_select(requirement, used_devices_list):
    '''
    添加余热设备方案，按照四个典型日分别添加
    '''
    global device_list, device_list_day_2, device_list_day_3, device_list_day_4
    device_list_day_2 = copy.deepcopy(device_list)
    device_list_day_3 = copy.deepcopy(device_list)
    device_list_day_4 = copy.deepcopy(device_list)
    price, req = get_need_and_price(requirement, 'day_1')
    waste_heat_device_select_sub(req, device_list, used_devices_list)
    air_device_select(req, device_list, used_devices_list)
    price, req = get_need_and_price(requirement, 'day_2')
    waste_heat_device_select_sub(req, device_list_day_2, used_devices_list)
    air_device_select(req, device_list_day_2, used_devices_list)
    price, req = get_need_and_price(requirement, 'day_3')
    waste_heat_device_select_sub(req, device_list_day_3, used_devices_list)
    air_device_select(req, device_list_day_3, used_devices_list)
    price, req = get_need_and_price(requirement, 'day_4')
    waste_heat_device_select_sub(req, device_list_day_4, used_devices_list)
    air_device_select(req, device_list_day_4, used_devices_list)


def waste_heat_device_select_sub(requirement, device_list, disabled_devices):
    '''
    添加余热设备方案
    waste_heat_device的每个元素为一个dict
    key值为heat、cool、hot_water、steam
    分别代表热负荷、冷负荷、热水量、蒸汽量
    每个dict构成一个余热设备方案
    '''
    if requirement is None:
        return
    for case in device_list:
        waste_heat_device[:] = []
        # 根据电负荷设备类型进行余热设备添加
        matched_devices_waste_heat = []
        # 发电设备数量
        number = case['electric'][u'number']
        # 燃气轮机
        if case['electric'][u'class'] == '4':
            # 锅炉烟气流量t/h&燃机排烟温度℃
            (gas_flow, out_temp) = get_gas_turbine_props(case['electric'][u'props'])
            # 蒸汽型余热锅炉(系)
            # 蒸汽型余热锅炉计算，饱和蒸汽温度&饱和蒸汽压力&饱和蒸汽焓值&产汽量
            (steam_t_sat, steam_p_sat, steam_h_sat, steam_production) = steam_waste_heat_boiler(number * gas_flow * 1000, out_temp)
            # 蒸汽
            if requirement[u'蒸汽需求'] and not requirement[u'冷负荷'] and not requirement[u'热水需求'] and not requirement[u'热负荷']:
                waste_heat_gas_turbine_steam(steam_production, disabled_devices=disabled_devices)
            # 蒸汽型余热锅炉+蒸汽型溴化锂(饱和蒸汽，需要满足压力)
            # 蒸汽+冷
            if requirement[u'蒸汽需求'] and requirement[u'冷负荷'] and not requirement[u'热水需求'] and not requirement[u'热负荷']:
                waste_heat_gas_turbine_steam_cool(steam_p_sat, steam_production, requirement[u'冷负荷'], mode=1, disabled_devices=disabled_devices)
            # 冷
            if not requirement[u'蒸汽需求'] and requirement[u'冷负荷'] and not requirement[u'热水需求'] and not requirement[u'热负荷'] and case['electric'][u'load'] > 5700:
                waste_heat_gas_turbine_steam_cool(steam_p_sat, steam_production, requirement[u'冷负荷'], mode=2, disabled_devices=disabled_devices)
            # 蒸汽型余热锅炉+板换
            # 蒸汽+热水
            if requirement[u'蒸汽需求'] and not requirement[u'冷负荷'] and requirement[u'热水需求'] and not requirement[u'热负荷']:
                waste_heat_gas_turbine_steam_heat_hot_water(steam_h_sat, steam_production, mode=1, disabled_devices=disabled_devices)
            # 蒸汽+供暖
            if requirement[u'蒸汽需求'] and not requirement[u'冷负荷'] and not requirement[u'热水需求'] and requirement[u'热负荷']:
                waste_heat_gas_turbine_steam_heat_hot_water(steam_h_sat, steam_production, mode=2, disabled_devices=disabled_devices)
            # 余热蒸汽锅炉+蒸汽型溴化锂+板换
            # 热水流量与热量转换 1m3/h=700kW
            # 冷+暖
            # if not requirement[u'蒸汽需求'] and not requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷']:
            #     waste_heat_gas_turbine_steam_cool_heat_hot_water(steam_p_sat, steam_h_sat, steam_production, mode=1)
            # 蒸汽+冷+暖
            if requirement[u'蒸汽需求'] and not requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷']:
                waste_heat_gas_turbine_steam_cool_heat_hot_water(steam_p_sat, steam_h_sat, steam_production, requirement[u'冷负荷'], mode=2, disabled_devices=disabled_devices)
            # 蒸汽+冷+生活热水
            if requirement[u'蒸汽需求'] and requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷']:
                waste_heat_gas_turbine_steam_cool_heat_hot_water(steam_p_sat, steam_h_sat, steam_production, requirement[u'冷负荷'], mode=3, disabled_devices=disabled_devices)
            # 冷+生活热水
            # if not requirement[u'蒸汽需求'] and requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷']:
            #     waste_heat_gas_turbine_steam_cool_heat_hot_water(steam_p_sat, steam_h_sat, steam_production, mode=4)

            # 烟气溴化锂(系)
            # 冷
            # 烟气双效（补燃）型溴化锂机组；燃气轮机：排烟可利用功率通过余热锅炉计算烟气能量，排烟可回收功率×1.3=制冷量
            if not requirement[u'蒸汽需求'] and not requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷']:
                waste_heat_gas_turbine_cool(number * gas_flow, out_temp, mode=1, disabled_devices=disabled_devices)
            # 冷+暖
            if not requirement[u'蒸汽需求'] and not requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷']:
                waste_heat_gas_turbine_cool(number * gas_flow, out_temp, mode=2, disabled_devices=disabled_devices)

            # 余热热水锅炉(系)
            # 供暖还是看余热热水锅炉的烟气热量，通过锅炉中计算公式计算烟气热量，在余热热水锅炉中制取热水或者采暖
            # 热水出水温度&热水量&烟气热量
            (hot_water_temperature, hot_water_yield, gas_heat) = waste_heat_boiler_calculate(number * gas_flow, out_temp, mode=1)
            # 供暖+热水
            if not requirement[u'蒸汽需求'] and requirement[u'热水需求'] and requirement[u'热负荷'] and not requirement[u'冷负荷']:
                waste_heat_gas_turbine_heat_hot_water(hot_water_yield, gas_heat, mode=1, disabled_devices=disabled_devices)
            # 供暖
            if not requirement[u'蒸汽需求'] and requirement[u'热负荷'] and not requirement[u'热水需求'] and not requirement[u'冷负荷']:
                waste_heat_gas_turbine_heat_hot_water(hot_water_yield, gas_heat, mode=2, disabled_devices=disabled_devices)
            # 热水
            if not requirement[u'蒸汽需求'] and requirement[u'热水需求'] and requirement[u'热负荷'] and not requirement[u'冷负荷'] and case[u'electric'][u'load'] < 5700:
                waste_heat_gas_turbine_heat_hot_water(hot_water_yield, gas_heat, mode=3, disabled_devices=disabled_devices)
            # 余热热水锅炉+温水型溴化锂
            # 燃气轮机后余热热水锅炉+温水型，温水型指低温和高温所有皆可
            # 温水型溴化锂供暖+制冷，部分热水进入溴化锂机组
            # 温水溴化锂只提供冷
            # 余热热水锅炉可同时供暖和生活热水
            # 搜索出温水型溴化锂设备
            matched_devices_waste_heat = search_warm_water_type_lithium(hot_water_temperature, hot_water_yield, disabled_devices=disabled_devices)
            # 供暖+制冷+热水
            if not requirement[u'蒸汽需求'] and requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷']:
                waste_heat_gas_turbine_heat_cool_hot_water(matched_devices_waste_heat, hot_water_yield, mode=1, disabled_devices=disabled_devices)
            # 供暖+制冷
            # if not requirement[u'蒸汽需求'] and not requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷']:
            #     waste_heat_gas_turbine_heat_cool_hot_water(matched_devices_waste_heat, hot_water_yield, mode=2)
            # 制冷+热水
            if not requirement[u'蒸汽需求'] and requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷']:
                waste_heat_gas_turbine_heat_cool_hot_water(matched_devices_waste_heat, hot_water_yield, mode=3, disabled_devices=disabled_devices)
            # 制冷
            if not requirement[u'蒸汽需求'] and not requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷']:
                waste_heat_gas_turbine_heat_cool_hot_water(matched_devices_waste_heat, hot_water_yield, mode=4, disabled_devices=disabled_devices)

            # 蒸汽+供暖+制冷+热水 全部需求
            if requirement[u'蒸汽需求'] and requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷']:
                # TODO 找出四选三的方案后剩余一种用调峰设备补足，使用[温水型溴化锂: 供暖+制冷+热水]
                waste_heat_gas_turbine_heat_cool_hot_water(matched_devices_waste_heat, hot_water_yield, mode=1, disabled_devices=disabled_devices)
            # TODO 没有设备选型的蒸汽+供暖+热水需求，采用[余热蒸汽锅炉+蒸汽型溴化锂+板换]
            if requirement[u'蒸汽需求'] and requirement[u'热水需求'] and requirement[u'热负荷'] and not requirement[u'冷负荷']:
                waste_heat_gas_turbine_steam_cool_heat_hot_water(steam_p_sat, steam_h_sat, steam_production, requirement[u'冷负荷'], mode=5, disabled_devices=disabled_devices)
        if case[u'electric'][u'class'] == '5':
            # 内燃机
            # 排烟温度&烟气流量&排烟可利用功率&高温水可利用功率
            (exhaust_gas_temperature, mass_flow_rate, exhaust_gas_available_power, hot_water_available_power) = get_internal_combustion_engine_props(case['electric'][u'props'], number=number)
            # 烟气热水型溴化锂(系)
            # 烟气热水型（补燃型）溴化锂机组：只有内燃机后跟烟气热水型（补燃型）溴化锂机组，（高温水可利用功率+排烟可利用功率）×1.1=制冷量
            # 冷+暖
            if not requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_cool_heat(hot_water_available_power, exhaust_gas_available_power, mode=1, disabled_devices=disabled_devices)
            # 冷
            if not requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_cool_heat(hot_water_available_power, exhaust_gas_available_power, mode=2, disabled_devices=disabled_devices)

            # 溴化锂吸收式直燃型三用机(系)
            # 冷+热水
            if requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                # 获取天然气耗量
                gas_consumption = requirement[u'天然气耗量(冷)']
                waste_heat_internal_combustion_engine_cool_heat_hot_water(gas_consumption, mode=1, disabled_devices=disabled_devices)
            # 暖+热水
            if requirement[u'热水需求'] and requirement[u'热负荷'] and not requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                # 获取天然气耗量
                gas_consumption = requirement[u'天然气耗量(热)']
                waste_heat_internal_combustion_engine_cool_heat_hot_water(gas_consumption, mode=2, disabled_devices=disabled_devices)

            # 烟气型溴化锂(系)
            # 烟气型溴化锂+缸套水板换
            # 冷+暖+热水
            if requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_cool_heat_hot_water_2(hot_water_available_power, exhaust_gas_available_power, mode=1, disabled_devices=disabled_devices)
            # 冷+暖
            if not requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_cool_heat_hot_water_2(hot_water_available_power, exhaust_gas_available_power, mode=2, disabled_devices=disabled_devices)
            # 冷+热水
            if requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_cool_heat_hot_water_2(hot_water_available_power, exhaust_gas_available_power, mode=3, disabled_devices=disabled_devices)

            # 余热热水锅炉(系)
            # 余热热水锅炉+板换
            # 余热热水锅炉计算，热水温度&热水量&烟气热量
            (hot_water_temperature, hot_water_yield, gas_heat) = waste_heat_boiler_calculate(mass_flow_rate, exhaust_gas_temperature, mode=1)
            # 暖+热水
            if requirement[u'热水需求'] and requirement[u'热负荷'] and not requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_cool_heat_hot_water_3(hot_water_yield, gas_heat, mode=1, disabled_devices=disabled_devices)
            # 暖
            if not requirement[u'热水需求'] and requirement[u'热负荷'] and not requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_cool_heat_hot_water_3(hot_water_yield, gas_heat, mode=2, disabled_devices=disabled_devices)
            # 热水
            if requirement[u'热水需求'] and not requirement[u'热负荷'] and not requirement[u'冷负荷'] and not requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_cool_heat_hot_water_3(hot_water_yield, gas_heat, mode=3, disabled_devices=disabled_devices)

            # 余热蒸汽锅炉(系)
            # 蒸汽型余热锅炉计算，饱和蒸汽温度&饱和蒸汽压力&饱和蒸汽焓值&产汽量
            (steam_t_sat, steam_p_sat, steam_h_sat, steam_production) = steam_waste_heat_boiler(mass_flow_rate, exhaust_gas_temperature)
            # 蒸汽
            if not requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷'] and requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_steam(steam_production, disabled_devices=disabled_devices)
            # 余热蒸汽锅炉+板换
            # 蒸汽+生活热水
            if requirement[u'热水需求'] and not requirement[u'热负荷'] and not requirement[u'冷负荷'] and requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_steam_heat_hot_water(steam_h_sat, steam_production, mode=1, disabled_devices=disabled_devices)
            # 蒸汽+暖
            if not requirement[u'热水需求'] and requirement[u'热负荷'] and not requirement[u'冷负荷'] and requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_steam_heat_hot_water(steam_h_sat, steam_production, mode=2, disabled_devices=disabled_devices)
            # 蒸汽+暖+生活热水
            if requirement[u'热水需求'] and requirement[u'热负荷'] and not requirement[u'冷负荷'] and requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_steam_heat_hot_water(steam_h_sat, steam_production, mode=3, disabled_devices=disabled_devices)
            # 余热蒸汽锅炉+蒸汽型溴化锂
            # 蒸汽+冷
            if not requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷'] and requirement[u'蒸汽需求']:
                waste_heat_internal_combustion_engine_steam_cool(steam_h_sat, steam_production, disabled_devices=disabled_devices)
            # 余热蒸汽锅炉+蒸汽型溴化锂+板换
            # 蒸汽+热水+冷
            # if requirement[u'热水需求'] and not requirement[u'热负荷'] and requirement[u'冷负荷'] and requirement[u'蒸汽需求']:
            #     waste_heat_internal_combustion_engine_steam_cool_heat_hot_water(steam_h_sat, steam_production, mode=1)
            # # 蒸汽+冷+暖
            # if not requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷'] and requirement[u'蒸汽需求']:
            #     waste_heat_internal_combustion_engine_steam_cool_heat_hot_water(steam_h_sat, steam_production, mode=2)

            # 蒸汽+供暖+制冷+热水 全部需求
            if requirement[u'蒸汽需求'] and requirement[u'热水需求'] and requirement[u'热负荷'] and requirement[u'冷负荷']:
                # TODO 找出四选三的方案后剩余一种用调峰设备补足，采用[余热蒸汽锅炉+板换: 蒸汽+暖+生活热水]
                waste_heat_internal_combustion_engine_steam_heat_hot_water(steam_h_sat, steam_production, mode=3, disabled_devices=disabled_devices)
        # 将匹配到的余热设备list加入发电设备的key='waste'中
        case['waste'] = waste_heat_device[:]
    print('waste load matching end')


def waste_heat_device_select_test(number=1):
    for case in device_list:
        waste_heat_device[:] = []
        matched_devices_waste_heat = []
        matched_devices_waste_heat = Device.query.filter(
            and_(
                Device.device_class == '1',
                or_(
                    and_(
                        Device.device_type == '7', Device.main_prop_value_1 >= 2500
                    )
                )
            )
        ).all()
        for device in matched_devices_waste_heat:
            waste_heat = {
                u'steam': None,
                u'cool': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_1, number=number, props_str=device.props_json),
                u'heat': init_waste_heat_device_dict(device.device_class, device.device_type, device.id, device.main_prop_value_2, number=number, props_str=device.props_json),
                u'heat_plate': None,
                u'hot_water': None,
                u'air': None,
                u'mix': None,
                u'waste_type': '4'
            }
            waste_heat_device.append(waste_heat)
        case['waste'] = waste_heat_device[:]


def peak_load_regulation_device_select(requirement):
    '''
    添加调峰设备的方案
    '''
    price, req = get_need_and_price(requirement, 'day_1')
    if req:
        peak_load_regulation_device_select_sub(req, device_list)
    price, req = get_need_and_price(requirement, 'day_2')
    if req:
        peak_load_regulation_device_select_sub(requirement, device_list_day_2)
    price, req = get_need_and_price(requirement, 'day_3')
    if req:
        peak_load_regulation_device_select_sub(requirement, device_list_day_3)
    price, req = get_need_and_price(requirement, 'day_4')
    if req:
        peak_load_regulation_device_select_sub(requirement, device_list_day_4)


def peak_load_regulation_device_select_sub(requirement, device_list):
    '''
    添加调峰设备方案
    '''
    for case in device_list:
        left_load_list_electric = []
        left_load_list_steam = []
        left_load_list_cool = []
        left_load_list_heat = []
        left_load_list_hot_water = []
        # left_load_list_air = []
        for waste in case['waste']:
            for index in range(0, 24):
                if waste[u'need_list'][index][u'electric'] >= 0:
                    left_load_list_electric.append(waste[u'need_list'][index][u'electric'] - waste[u'operating_state'][index]['output_x'][0])
                else:
                    left_load_list_electric.append(0.0)
                if waste[u'need_list'][index][u'steam'] >= 0:
                    left_load_list_steam.append(waste[u'need_list'][index][u'steam'] - waste[u'operating_state'][index]['output_x'][1])
                else:
                    left_load_list_steam.append(0.0)
                if waste[u'need_list'][index][u'cool'] >= 0:
                    left_load_list_cool.append(waste[u'need_list'][index][u'cool'] - waste[u'operating_state'][index]['output_x'][2])
                else:
                    left_load_list_cool.append(0.0)
                if waste[u'need_list'][index][u'heat'] >= 0:
                    left_load_list_heat.append(waste[u'need_list'][index][u'heat'] - waste[u'operating_state'][index]['output_x'][3] - waste[u'operating_state'][index]['output_x'][4])
                else:
                    left_load_list_heat.append(0.0)
                if waste[u'need_list'][index][u'hot_water'] >= 0:
                    left_load_list_hot_water.append(waste[u'need_list'][index][u'hot_water'] - waste[u'operating_state'][index]['output_x'][5])
                    # if len(waste[u'operating_state'][index]['output_x']) == 6:
                    #     left_load_list_hot_water.append(waste[u'need_list'][index][u'hot_water'] - waste[u'operating_state'][index]['output_x'][4])
                    # else:
                    #     left_load_list_hot_water.append(waste[u'need_list'][index][u'hot_water'] - waste[u'operating_state'][index]['output_x'][4] - waste[u'operating_state'][index]['output_x'][5])
                else:
                    left_load_list_hot_water.append(0.0)
        # 缺口最大值计算
        electric_delta_max = max(left_load_list_electric) if len(left_load_list_electric) > 0 else 0
        steam_delta_max = max(left_load_list_steam) if len(left_load_list_steam) > 0 else 0
        cool_delta_max = max(left_load_list_cool) if len(left_load_list_cool) > 0 else 0
        heat_delta_max = max(left_load_list_heat) if len(left_load_list_heat) > 0 else 0
        hot_water_delta_max = max(left_load_list_hot_water) if len(left_load_list_hot_water) > 0 else 0
        # if requirement[u'电力需求']:
        #     peak_load_regulation[u'electric'] = requirement[u'蒸汽需求'] - x_matrix[0]
        # if requirement[u'蒸汽需求']:
        #     peak_load_regulation[u'steam'] = requirement[u'蒸汽需求'] - x_matrix[1]
        # if requirement[u'冷负荷']:
        #     peak_load_regulation[u'cool'] = requirement[u'冷负荷'] - x_matrix[2]
        # if requirement[u'热负荷']:
        #     peak_load_regulation[u'heat'] = requirement[u'热负荷'] - x_matrix[3]
        # if requirement[u'热水需求']:
        #     if x_matrix.shape[0] == 6:
        #         peak_load_regulation[u'hot_water'] = requirement[u'热水需求'] - x_matrix[4]
        #     else:
        #         peak_load_regulation[u'hot_water'] = requirement[u'热水需求'] - x_matrix[4] - x_matrix[5]
        # if requirement[u'蓄能']:
        #     peak_load_regulation[u'storage'] = requirement[u'蓄能']
        peak_load_regulation = {
            u'electric': electric_delta_max, u'steam': steam_delta_max, u'cool': cool_delta_max, u'heat': heat_delta_max, u'hot_water': hot_water_delta_max, u'storage': None
        }
        case[u'peak_load_regulation'] = peak_load_regulation


def auxiliary_device_select():
    '''
    添加辅机设备方案
    auxiliary_device的每个元素为一个dict
    key值未定
    每个dict构成一个调峰设备方案
    '''
    auxiliary_device.append()


def get_running_curve(need_curve, our_resource=0, index=0, photovoltaic=None, wind=None):
    '''
    获取某一时刻的需求数值
    减去外部资源提供的与光伏风电等资源后的等效需求
    '''
    need = 0
    if need_curve and need_curve[index] - our_resource > 0:
        need = need_curve[index] - our_resource
    if photovoltaic and need - photovoltaic[index] > 0:
        need = need - photovoltaic[index]
    if wind and need - wind[index] > 0:
        need = need - wind[index]
    return need


def get_peak_out_running_curve(need_curve, state=0, consumption=0, index=0, out_resource=0, photovoltaic=None, wind=None, mode='peak', peak_devices=None):
    '''
    获取前台的调峰设备/外部资源设备曲线
    需求加上耗散减去运行大于0的时候说明运行不足，需要调峰设备补充
    '''
    global out_resource_detail
    peak = 0
    out_resource_running = 0
    if need_curve:
        if need_curve[index] - state + consumption - out_resource > 0:
            peak = need_curve[index] - state + consumption - out_resource
            out_resource_running = out_resource
        else:
            out_resource_running = need_curve[index] - state + consumption
    if photovoltaic and peak - photovoltaic[index] > 0 and out_resource_detail['electric'][u'光伏']['used'] == 1:
        peak = peak - photovoltaic[index]
    if wind and peak - wind[index] > 0 and out_resource_detail['electric'][u'风电']['used'] == 1:
        peak = peak - wind[index]
    if mode == 'peak':
        if not peak_devices:
            peak = 0
        return peak
    elif mode == 'out_running':
        return out_resource_running


def get_after_burning_curve(need_curve, state=0, waste_type=None, waste=None, index=0):
    '''
    获取前台的余热设备补燃曲线
    '''
    after_burning = 0
    if waste_type == '1' or waste_type == '3':
        if need_curve and need_curve[index] <= state * 1.3:
            after_burning = need_curve[index] - state
    return after_burning


def get_bounds_matrix(
    need, electric, waste, special=False,
    electric_max=1.0, steam_max=1.0, cool_max=1.0, heat_max=1.0, heat_palte_max=1.0, hot_water_max=1.0, air_max=1.0,
    electric_min=0.7, steam_min=0.7, cool_min=0.7, heat_min=0.7, heat_palte_min=0.7, hot_water_min=0.7, air_min=1.0,
):
    '''
    创建边界条件矩阵
    input(当前时段的需求曲线数值, 各种需求的设备输出所设定上下限)
    不设置上下限时则按照需求曲线70%~需求曲线100%作为范围匹配曲线
    '''
    need_electric_max = float(electric['load']) * float(electric['number'])
    if need_electric_max < need['electric']:
        need_electric_max = need_electric_max
        electric_rate = 1
    else:
        electric_rate = abs(round(need['electric'] / need_electric_max - 0.0000000000000005, 15))
        need_electric_max = need['electric']
    need_steam_max = need['steam'] if need['steam'] and need['steam'] > 0 and waste[u'steam'] else 0
    need_cool_max = need['cool'] if need['cool'] and need['cool'] > 0 and waste[u'cool'] else 0
    need_heat_max = need['heat'] if need['heat'] and need['heat'] > 0 and waste[u'heat'] else 0
    need_heat_plate_max = need['heat'] if need['heat'] and need['heat'] and waste[u'heat_plate'] > 0 else 0
    need_hot_water_max = need['hot_water'] if need['hot_water'] and need['hot_water'] and waste[u'hot_water'] > 0 else 0
    need_air_max = need['air'] if need['air'] and need['air'] and waste[u'air'] > 0 else 0
    need_steam_min = need_cool_min = need_heat_min = 0
    # if waste['mix']:
    #     if 'steam' in waste['mix']:
    #         need_steam_max = waste['mix']['steam']
    #     if 'cool' in waste['mix']:
    #         need_cool_max = waste['mix']['cool']
    #     if 'heat' in waste['mix']:
    #         need_heat_max = waste['mix']['heat']
    #     if 'heat_plate' in waste['mix']:
    #         need_heat_plate_max = waste['mix']['heat_plate']
    #     if 'hot_water' in waste['mix']:
    #         need_hot_water_max = waste['mix']['hot_water']
    #     if 'air' in waste['mix']:
    #         need_air_max = waste['mix']['air']
    # if need['steam'] > 0 and waste['steam']:
    #     need_steam_max = float(waste['steam']['load']) * waste['steam']['number']
    # if need['cool'] > 0 and waste['cool']:
    #     need_cool_max = float(waste['cool']['load']) * waste['cool']['number']
    # if need['heat'] > 0 and waste['heat']:
    #     need_heat_max = float(waste['heat']['load']) * waste['heat']['number']
    # if waste['heat_plate'] and waste['heat_plate']:
    #     need_heat_plate_max = float(waste['heat_plate']['load']) * waste['heat_plate']['number']
    # if waste['hot_water'] and waste['hot_water']:
    #     need_hot_water_max = float(waste['hot_water']['load']) * waste['hot_water']['number']
    # if need['air'] > 0 and waste['air']:
    #     need_air_max = float(waste['air']['load']) * waste['air']['number']
    # bounds = (
    #     (electric_min * need_electric_max, electric_max * need_electric_max),
    #     (steam_min * electric_rate * float(need_steam_min), steam_max * electric_rate * float(need_steam_max)),
    #     (cool_min * electric_rate * float(need_cool_min), cool_max * electric_rate * float(need_cool_max)),
    #     (heat_min * electric_rate * float(need_heat_min), heat_max * electric_rate * float(need_heat_max)),
    #     (0, heat_palte_max * electric_rate * float(need_heat_plate_max)),
    #     (0, hot_water_max * electric_rate * float(need_hot_water_max)),
    #     # (hot_water_min * electric_rate * float(need_hot_water_max), hot_water_max * float(need_hot_water_max)),
    #     (air_min * float(need_air_max), air_max * float(need_air_max))
    # )
    bounds = (
        (electric_min * need_electric_max, electric_max * need_electric_max),
        (steam_min * float(need_steam_min), steam_max * float(need_steam_max)),
        (cool_min * float(need_cool_min), cool_max * float(need_cool_max)),
        (heat_min * float(need_heat_min), heat_max * float(need_heat_max)),
        (0, heat_palte_max * float(need_heat_plate_max)),
        (0, hot_water_max * float(need_hot_water_max)),
        (air_min * float(need_air_max), air_max * float(need_air_max))
    )
    return bounds


def get_coefficient_matrix_gas_warm_water_LiBr(
    electric, waste, alpha_dict=None, device_class='5',
    price=None, need=None, heat_and_cool=False, used_devices_list=[]
):
    '''
    创建烟气热水溴化锂的方程参数矩阵
    '''
    alpha_cool_gas_0, alpha_cool_gas_1 = alpha_dict['cool_gas']
    alpha_cool_fuel_0, alpha_cool_fuel_1 = alpha_dict['cool_fuel']
    alpha_heat_gas_0, alpha_heat_gas_1 = alpha_dict['heat_gas']
    alpha_heat_fuel_0, alpha_heat_fuel_1 = alpha_dict['heat_fuel']
    alpha_heat_cool_0, alpha_heat_cool_1 = alpha_dict['heat_cool']
    relation_dict = get_internal_combustion_parameter_engine_relation(electric[u'id'], electric[u'class'], electric[u'load'], electric[u'props'])
    gas_flow_theta_0, gas_flow_theta_1 = relation_dict['gas_flow_theta']
    alpha_ex_0, alpha_ex_1 = relation_dict['alpha_ex']
    alpha_w_0, alpha_w_1 = relation_dict['alpha_w']
    A_ub = b_ub = A_eq = b_eq = A_ub_2 = b_ub_2 = c_2 = bounds_2 = None
    # 不等式矩阵 电，(蒸汽)，冷，热(LiBr)，热(缸套水板换)，(热水)，(空气)
    if device_class == '5':
        if heat_and_cool:
            # 冷热同时提供
            A_ub = numpy.array([[-AlgoConstants.gas_LiBr_afterburning_coefficient * (alpha_w_1 + alpha_ex_1), 0, 1, 1 / alpha_heat_cool_1, 0, 0, 0]])
            b_ub_cool = numpy.array([AlgoConstants.gas_LiBr_afterburning_coefficient * (alpha_w_0 + alpha_ex_0)])
            b_ub_heat = numpy.array([AlgoConstants.gas_LiBr_afterburning_coefficient * (alpha_w_0 + alpha_ex_0) + alpha_heat_cool_0 / alpha_heat_cool_1])
            c = get_peak_ita(need, price, used_devices_list=used_devices_list)
            bounds_cool = get_bounds_matrix(need, electric, waste, steam_min=0, steam_max=0, heat_min=0, heat_max=0, heat_palte_min=0, heat_palte_max=0, hot_water_min=0, hot_water_max=0)
            bounds_heat = get_bounds_matrix(need, electric, waste, steam_min=0, steam_max=0, cool_min=0, cool_max=0, heat_palte_min=0, heat_palte_max=0, hot_water_min=0, hot_water_max=0)
            return A_ub, b_ub_cool, A_eq, b_eq, c, bounds_cool, A_ub, b_ub_heat, c, bounds_heat
        else:
            A_ub = numpy.array([[-AlgoConstants.gas_LiBr_afterburning_coefficient * (alpha_w_1 + alpha_ex_1), 0, 1, 1 / alpha_heat_cool_1, 0, 0, 0]])
            if need['cool'] > 0:
                b_ub = numpy.array([AlgoConstants.gas_LiBr_afterburning_coefficient * (alpha_w_0 + alpha_ex_0)])
                bounds = get_bounds_matrix(need, electric, waste, steam_min=0, steam_max=0, heat_min=0, heat_max=0, heat_palte_min=0, heat_palte_max=0, hot_water_min=0, hot_water_max=0)
            elif need['heat'] > 0:
                b_ub = numpy.array([AlgoConstants.gas_LiBr_afterburning_coefficient * (alpha_w_0 + alpha_ex_0) + alpha_heat_cool_0 / alpha_heat_cool_1])
                bounds = get_bounds_matrix(need, electric, waste, steam_min=0, steam_max=0, cool_min=0, cool_max=0, heat_palte_min=0, heat_palte_max=0, hot_water_min=0, hot_water_max=0)
            else:
                b_ub = numpy.array([AlgoConstants.gas_LiBr_afterburning_coefficient * (alpha_w_0 + alpha_ex_0)])
                bounds = get_bounds_matrix(need, electric, waste, steam_min=0, steam_max=0, heat_min=0, heat_max=0, cool_min=0, cool_max=0, heat_palte_min=0, heat_palte_max=0, hot_water_min=0, hot_water_max=0)
            c = get_peak_ita(need, price, used_devices_list=used_devices_list)
            return A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2


def get_coefficient_matrix_gas_LiBr(
    electric, waste, gas_heat_theta_0, gas_heat_theta_1, alpha_dict=None, device_class='4',
    price=None, need=None, heat_and_cool=0, used_devices_list=[]
):
    '''
    创建烟气溴化锂的方程参数矩阵
    '''
    alpha_cool_gas_0, alpha_cool_gas_1 = alpha_dict['cool_gas']
    alpha_cool_fuel_0, alpha_cool_fuel_1 = alpha_dict['cool_fuel']
    alpha_heat_gas_0, alpha_heat_gas_1 = alpha_dict['heat_gas']
    alpha_heat_fuel_0, alpha_heat_fuel_1 = alpha_dict['heat_fuel']
    alpha_heat_cool_0, alpha_heat_cool_1 = alpha_dict['heat_cool']
    A_ub = b_ub = A_eq = b_eq = A_ub_2 = b_ub_2 = c_2 = bounds_2 = None
    if device_class == '4':
        # 不等式矩阵 电，(蒸汽)，冷，热(LiBr)，热(缸套水板换)，(热水)，(空气)
        if heat_and_cool:
            # 冷热同时提供
            A_ub = numpy.array([[-gas_heat_theta_1, 0, 1, 1 / alpha_heat_cool_1, 0, 0, 0]])
            b_ub_cool = numpy.array([gas_heat_theta_0])
            b_ub_heat = numpy.array([gas_heat_theta_0 + alpha_heat_cool_0 / alpha_heat_cool_1])
            c = get_peak_ita(need, price, used_devices_list=used_devices_list)
            bounds_cool = get_bounds_matrix(need, electric, waste, heat_min=0, heat_max=0)
            bounds_heat = get_bounds_matrix(need, electric, waste, cool_min=0, cool_max=0)
            return A_ub, b_ub_cool, A_eq, b_eq, c, bounds_cool, A_ub, b_ub_heat, c, bounds_heat
        else:
            A_ub = numpy.array([[-gas_heat_theta_1, 0, 1, 1 / alpha_heat_cool_1, 0, 0, 0]])
            if need['cool'] > 0:
                b_ub = numpy.array([gas_heat_theta_0])
            elif need['heat'] > 0:
                b_ub = numpy.array([gas_heat_theta_0 + alpha_heat_cool_0 / alpha_heat_cool_1])
            c = get_peak_ita(need, price, used_devices_list=used_devices_list)
            bounds = get_bounds_matrix(need, electric, waste)
            return A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2
    elif device_class == '5':
        relation_dict = get_internal_combustion_parameter_engine_relation(electric[u'id'], electric[u'class'], electric[u'load'], electric[u'props'])
        gas_flow_theta_0, gas_flow_theta_1 = relation_dict['gas_flow_theta']
        alpha_ex_0, alpha_ex_1 = relation_dict['alpha_ex']
        alpha_w_0, alpha_w_1 = relation_dict['alpha_w']
        if heat_and_cool:
            # 冷热同时提供
            A_ub_cool = numpy.array([
                [-AlgoConstants.hot_water_available_power_coefficient * alpha_w_1, 0, 0, 0, 1, 700, 0], [-AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_1, 0, 1, 0, 0, 0, 0]
            ])
            b_ub_cool = numpy.array([
                AlgoConstants.hot_water_available_power_coefficient * alpha_w_0, AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_0
            ])
            c_cool = get_peak_ita(need, price, special=True, used_devices_list=used_devices_list)
            bounds_cool = get_bounds_matrix(need, electric, waste, heat_min=0, heat_max=0)
            need_heat_max = need['heat'] if need['heat'] else 0
            device_water_heat_max = float(waste['mix']['heat_plate']) if waste['mix'] else 0
            A_ub_heat = numpy.array([
                [-AlgoConstants.hot_water_available_power_coefficient * alpha_w_1, 0, 0, 0, 1, 700, 0],
                [-AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_1, 0, 0, alpha_heat_cool_1, 0, 0, 0],
                [0, 0, 0, 0, 1, 700, 0],
                [0, 0, 0, 1, 1, 0, 0]
            ])
            b_ub_heat = numpy.array([
                AlgoConstants.hot_water_available_power_coefficient * alpha_w_0, AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_0 - alpha_heat_cool_0, device_water_heat_max, need_heat_max
            ])
            c_heat = get_peak_ita(need, price, special=True, used_devices_list=used_devices_list)
            bounds_heat = get_bounds_matrix(need, electric, waste, cool_min=0, cool_max=0, hot_water_min=0, special=True)
            return A_ub_cool, b_ub_cool, A_eq, b_eq, c_cool, bounds_cool, A_ub_heat, b_ub_heat, c_heat, bounds_heat
        else:
            if need['cool'] > 0:
                # 不等式矩阵 电，(蒸汽)，冷，热(LiBr)，热(缸套水板换)，(热水)，(空气)
                A_ub = numpy.array([
                    [-AlgoConstants.hot_water_available_power_coefficient * alpha_w_1, 0, 0, 0, 0, 700, 0], [-AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_1, 0, 1, 0, 0, 0, 0]
                ])
                b_ub = numpy.array([
                    AlgoConstants.hot_water_available_power_coefficient * alpha_w_0, AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_0
                ])
                c = get_peak_ita(need, price, used_devices_list=used_devices_list)
                bounds = get_bounds_matrix(need, electric, waste)
            elif need['heat'] > 0:
                # TODO 特殊情况，热由两部分提供，其中一部分为烟气溴化锂，另一部分为缸套水板换
                # 不等式矩阵 电，(蒸汽)，冷，热(LiBr)，热(缸套水板换)，(热水)，(空气)
                need_heat_max = need['heat'] if need['heat'] else 0
                device_water_heat_max = float(waste['mix']['heat_plate']) if waste['mix'] else 0
                device_water_heat_max = float(waste['heat_plate']['load']) if device_water_heat_max == 0 else device_water_heat_max
                A_ub = numpy.array([
                    [-AlgoConstants.hot_water_available_power_coefficient * alpha_w_1, 0, 0, 0, 1, 700, 0],
                    [-AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_1, 0, 0, alpha_heat_cool_1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 700, 0],
                    [0, 0, 0, 1, 1, 0, 0]
                ])
                b_ub = numpy.array([
                    AlgoConstants.hot_water_available_power_coefficient * alpha_w_0, AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_0 - alpha_heat_cool_0, device_water_heat_max, need_heat_max
                ])
                c = get_peak_ita(need, price, special=True, used_devices_list=used_devices_list)
                bounds = get_bounds_matrix(need, electric, waste, hot_water_min=0, special=True)
            else:
                A_ub = numpy.array([
                    [-AlgoConstants.hot_water_available_power_coefficient * alpha_w_1, 0, 0, 0, 700, 0], [-AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_1, 0, 1, 0, 0, 0]
                ])
                b_ub = numpy.array([
                    AlgoConstants.hot_water_available_power_coefficient * alpha_w_0, AlgoConstants.exhaust_gas_available_power_coefficient * alpha_ex_0
                ])
                c = get_peak_ita(need, price, used_devices_list=used_devices_list)
                bounds = get_bounds_matrix(need, electric, waste, heat_min=0, heat_max=0, cool_min=0, cool_max=0)
            return A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2


def get_coefficient_matrix_steam_boiler(
    electric, waste, gas_heat_theta_0, gas_heat_theta_1, cool_alpha_0, cool_alpha_1, heat_alpha=0, water_alpha=0,
    price=None, need=None, heat_and_cool=False, used_devices_list=[]
):
    '''
    创建余热蒸汽锅炉(系)的方程参数矩阵
    '''
    A_ub = b_ub = A_eq = b_eq = A_ub_2 = b_ub_2 = c_2 = bounds_2 = None
    # 不等式矩阵 电，蒸汽，冷，热(LiBr)，热(缸套水板换)，热水，(空气)
    if heat_and_cool:
        # 冷热同时提供
        A_ub = numpy.array([[-gas_heat_theta_1, 1., cool_alpha_1, 0, heat_alpha, water_alpha, 0]])
        b_ub_cool = gas_heat_theta_0 - cool_alpha_0
        b_ub_heat = gas_heat_theta_0
        c = get_peak_ita(need, price, used_devices_list=used_devices_list)
        bounds_cool = get_bounds_matrix(need, electric, waste, heat_min=0, heat_max=0)
        bounds_heat = get_bounds_matrix(need, electric, waste, cool_min=0, cool_max=0)
        return A_ub, b_ub_cool, A_eq, b_eq, c, bounds_cool, A_ub, b_ub_heat, c, bounds_heat
    else:
        # A_ub = numpy.array([[-gas_heat_theta_1, 1., cool_alpha_1, 0, heat_alpha, water_alpha, 0]])
        if need['cool'] > 0 and waste[u'cool'] is not None:
            b_ub = gas_heat_theta_0 - cool_alpha_0
            A_ub = numpy.array([[-gas_heat_theta_1, 1., cool_alpha_1, 0, heat_alpha, water_alpha, 0]])
        else:
            b_ub = gas_heat_theta_0
            A_ub = numpy.array([[-gas_heat_theta_1, 1., 0, 0, heat_alpha, water_alpha, 0]])
        c = get_peak_ita(need, price, used_devices_list=used_devices_list)
        bounds = get_bounds_matrix(need, electric, waste)
        return A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2


def get_coefficient_matrix_hot_water_boiler(
    electric, waste, gas_heat_theta_0, gas_heat_theta_1, cool_alpha_0, cool_alpha_1,
    price=None, need=None, heat_and_cool=False, used_devices_list=[]
):
    '''
    创建余热热水锅炉(系)的方程参数矩阵
    '''
    A_ub = b_ub = A_eq = b_eq = A_ub_2 = b_ub_2 = c_2 = bounds_2 = None
    # 不等式矩阵 电，(蒸汽)，冷，热(LiBr)，热(缸套水板换)，热水，(空气)
    if heat_and_cool:
        # 冷热同时提供
        A_ub = numpy.array([[-gas_heat_theta_1, 0, 700. * cool_alpha_1, 0, 1., 700., 0]])
        c = get_peak_ita(need, price, used_devices_list=used_devices_list)
        b_ub_cool = numpy.array([gas_heat_theta_0 - 700 * cool_alpha_0])
        b_ub_heat = numpy.array([gas_heat_theta_0])
        bounds_cool = get_bounds_matrix(need, electric, waste, heat_min=0, heat_max=0)
        bounds_heat = get_bounds_matrix(need, electric, waste, cool_min=0, cool_max=0)
        return A_ub, b_ub_cool, A_eq, b_eq, c, bounds_cool, A_ub, b_ub_heat, c, bounds_heat
    else:
        A_ub = numpy.array([[-gas_heat_theta_1, 0, 700. * cool_alpha_1, 0, 1., 700., 0]])
        c = get_peak_ita(need, price, used_devices_list=used_devices_list)
        bounds = get_bounds_matrix(need, electric, waste)
        if need['cool'] > 0:
            b_ub = numpy.array([gas_heat_theta_0 - 700 * cool_alpha_0])
        else:
            b_ub = numpy.array([gas_heat_theta_0])
        return A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2


def get_coefficient_matrix_three_use_LiBr(
    electric, waste, alpha_dict=None,
    price=None, need=None, heat_and_cool=False, used_devices_list=[]
):
    '''
    创建溴化锂吸收式直燃型三用机的方程参数矩阵
    '''
    alpha_cool_fuel_0, alpha_cool_fuel_1 = alpha_dict['cool_fuel']
    alpha_heat_fuel_0, alpha_heat_fuel_1 = alpha_dict['heat_fuel']
    A_ub = b_ub = A_eq = b_eq = A_ub_2 = b_ub_2 = c_2 = bounds_2 = None
    if heat_and_cool:
        # 冷热同时提供
        c = get_peak_ita(need, price, used_devices_list=used_devices_list)
        b_ub_cool = b_ub_heat = None
        bounds_cool = get_bounds_matrix(need, electric, waste, heat_min=0, heat_max=0)
        bounds_heat = get_bounds_matrix(need, electric, waste, cool_min=0, cool_max=0)
        return A_ub, b_ub_cool, A_eq, b_eq, c, bounds_cool, A_ub, b_ub_heat, c, bounds_heat
    else:
        # if need['cool'] > 0:
        #     # 等式矩阵 电，冷，热水
        # else:
        #     # 等式矩阵 电，热
        c = get_peak_ita(need, price, used_devices_list=used_devices_list)
        bounds = get_bounds_matrix(need, electric, waste)
    return A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2


def gas_turbine_parameter_relation(device_id, device_class, device_load, props_str):
    '''
    燃气轮机的参数关系
    燃机出力p与锅炉烟气流量flow(kg/h)、燃气消耗量gas_c(m3/h)的近似线性关系
    flow = gas_flow_theta_0 + gas_flow_theta_1 * p
    gas_c = alpha_gas_c_0 + alpha_gas_c_1 * p
    return(dict)
    '''
    device_prop_json = json.loads(props_str)
    gas_flow_index = device_prop_json[u'prop_name'].index(u'锅炉烟气流量')
    gas_flow = float(device_prop_json[u'prop_value'][gas_flow_index]) * 1000
    gas_c_index = device_prop_json[u'prop_name'].index(u'天然气耗量')
    if device_prop_json[u'prop_value'][gas_c_index]:
        gas_c = float(device_prop_json[u'prop_value'][gas_c_index])
    else:
        gas_c = 0
    gas_flow_theta_0 = 0
    gas_flow_theta_1 = gas_flow / float(device_load)
    alpha_gas_c_0 = 0
    alpha_gas_c_1 = gas_c / float(device_load)
    return {
        'gas_flow_theta': (gas_flow_theta_0, gas_flow_theta_1),
        'gas_c': (alpha_gas_c_0, alpha_gas_c_1)
    }


def get_internal_combustion_parameter_engine_relation(device_id, device_class, device_load, props_str):
    '''
    内燃机的参数关系
    电功率p与锅炉烟气流量flow的近似线性关系
    flow = gas_flow_theta_0 + gas_flow_theta_1 * p
    电功率p与排烟可回收功率ex_p、高温水可回收功率w_p、燃气消耗量gas_c的近似线性关系
    ex_p = alpha_ex_0 + alpha_ex_1 * p
    w_p = alpha_w_0 + alpha_w_1 * p
    gas_c = alpha_gas_c_0 + alpha_gas_c_1 * p
    return(dict)
    '''
    # TODO 假设：电功率和排烟功率、高温水功率完全按照等比例变化
    device_prop_json = json.loads(props_str)
    gas_flow_index = device_prop_json[u'prop_name'].index(u'质量流量，湿')
    gas_flow = float(device_prop_json[u'prop_value'][gas_flow_index])
    ex_index = device_prop_json[u'prop_name'].index(u'排烟可利用功率')
    ex = float(device_prop_json[u'prop_value'][ex_index])
    w_index = device_prop_json[u'prop_name'].index(u'高温水可利用功率')
    w = float(device_prop_json[u'prop_value'][w_index])
    gas_c_index = device_prop_json[u'prop_name'].index(u'燃气消耗量')
    gas_c = float(device_prop_json[u'prop_value'][gas_c_index])
    gas_flow_theta_0 = 0
    gas_flow_theta_1 = gas_flow / float(device_load)
    alpha_ex_0 = 0
    alpha_ex_1 = ex / float(device_load)
    alpha_w_0 = 0
    alpha_w_1 = w / float(device_load)
    alpha_gas_c_0 = 0
    alpha_gas_c_1 = gas_c / float(device_load)
    return {
        'gas_flow_theta': (gas_flow_theta_0, gas_flow_theta_1),
        'alpha_ex': (alpha_ex_0, alpha_ex_1),
        'alpha_w': (alpha_w_0, alpha_w_1),
        'gas_c': (alpha_gas_c_0, alpha_gas_c_1)
    }


def get_boiler_gas_heat(props_str, device_class, device_id, device_load, gas_out_temp=120, gas_specific_heat=1.2, boiler_thermal_efficiency=1):
    '''
    燃机的烟气热量计算
    烟气热量与燃机出力的关系
    gas_heat = gas_heat_theta_0 + gas_heat_theta_1 * p
    return(gas_heat_theta_0, gas_heat_theta_1)
    '''
    if device_class == '4':
        relation_dict = gas_turbine_parameter_relation(device_id, device_class, device_load, props_str)
        gas_flow_theta_0, gas_flow_theta_1 = relation_dict['gas_flow_theta']
        device_prop_json = json.loads(props_str)
        out_temp_index = device_prop_json[u'prop_name'].index(u'燃机排烟温度')
        out_temp = float(device_prop_json[u'prop_value'][out_temp_index])
        gas_heat_theta_0 = gas_specific_heat * (out_temp - gas_out_temp) * gas_flow_theta_0 * 1000 / 3600.
        gas_heat_theta_1 = gas_specific_heat * (out_temp - gas_out_temp) * gas_flow_theta_1 * 1000 / 3600.
    else:
        return 0, 0
    return gas_heat_theta_0, gas_heat_theta_1


def get_theta_steam_boiler(props_str, device_class, device_id, device_load, gas_out_temp=100, gas_specific_heat=1.2, steam_pressure=0.4, steam_temperature=190, water_supply_temperature=20, boiler_thermal_efficiency=0.89):
    '''
    余热蒸汽锅炉对应的系数
    燃机出力转换锅炉热量系数gas_heat_theta_0, gas_heat_theta_1
    热水系数water_alpha
    热量系数heat_alpha
    return(gas_heat_theta_0, gas_heat_theta_1, heat_alpha, water_alpha)
    '''
    steam_h = seuif97.pt2h(steam_pressure, steam_temperature)
    water_supply_h = seuif97.pt2h(steam_pressure, water_supply_temperature)
    if device_class == '4':
        # TODO 需要知道燃机出力p与锅炉烟气流量flow的近似线性关系
        relation_dict = gas_turbine_parameter_relation(device_id, device_class, device_load, props_str)
        gas_flow_theta_0, gas_flow_theta_1 = relation_dict['gas_flow_theta']
        device_prop_json = json.loads(props_str)
        out_temp_index = device_prop_json[u'prop_name'].index(u'燃机排烟温度')
        out_temp = float(device_prop_json[u'prop_value'][out_temp_index])
        c = gas_specific_heat * (out_temp - gas_out_temp) * boiler_thermal_efficiency / (steam_h - water_supply_h) / 1000.
        gas_heat_theta_0 = c * gas_flow_theta_0
        gas_heat_theta_1 = c * gas_flow_theta_1
    if device_class == '5':
        # TODO 需要知道电功率p与锅炉烟气流量flow的近似线性关系
        relation_dict = get_internal_combustion_parameter_engine_relation(device_id, device_class, device_load, props_str)
        gas_flow_theta_0, gas_flow_theta_1 = relation_dict['gas_flow_theta']
        device_prop_json = json.loads(props_str)
        exhaust_gas_temperature_index = device_prop_json[u'prop_name'].index(u'排烟温度')
        exhaust_gas_temperature = float(device_prop_json[u'prop_value'][exhaust_gas_temperature_index])
        c = gas_specific_heat * (exhaust_gas_temperature - gas_out_temp) * boiler_thermal_efficiency / (steam_h - water_supply_h) / 1000.
        gas_heat_theta_0 = c * gas_flow_theta_0
        gas_heat_theta_1 = c * gas_flow_theta_1
    water_alpha = 3600 * 700 / (1000. * steam_h * AlgoConstants.plate_type_heat_exchanger_efficiency)
    heat_alpha = 3600 / (1000 * steam_h * AlgoConstants.plate_type_heat_exchanger_efficiency)
    return gas_heat_theta_0, gas_heat_theta_1, heat_alpha, water_alpha


def get_theta_hot_water_boiler(props_str, device_class, device_id, device_load, gas_out_temp=100, gas_specific_heat=1.2, boiler_thermal_efficiency=0.91):
    '''
    余热热水锅炉对应的系数
    燃机出力转换锅炉热量系数gas_heat_theta_0, gas_heat_theta_1
    return(gas_heat_theta_0, gas_heat_theta_1)
    '''
    if device_class == '4':
        # TODO 需要知道燃机出力p与锅炉烟气流量flow的近似线性关系
        relation_dict = gas_turbine_parameter_relation(device_id, device_class, device_load, props_str)
        gas_flow_theta_0, gas_flow_theta_1 = relation_dict['gas_flow_theta']
        device_prop_json = json.loads(props_str)
        out_temp_index = device_prop_json[u'prop_name'].index(u'燃机排烟温度')
        out_temp = float(device_prop_json[u'prop_value'][out_temp_index])
        gas_heat_theta_0 = gas_specific_heat * (out_temp - gas_out_temp) * gas_flow_theta_0 / 3600.
        gas_heat_theta_1 = gas_specific_heat * (out_temp - gas_out_temp) * gas_flow_theta_1 / 3600.
    if device_class == '5':
        # TODO 需要知道电功率p与锅炉烟气流量flow的近似线性关系
        relation_dict = get_internal_combustion_parameter_engine_relation(device_id, device_class, device_load, props_str)
        gas_flow_theta_0, gas_flow_theta_1 = relation_dict['gas_flow_theta']
        device_prop_json = json.loads(props_str)
        exhaust_gas_temperature_index = device_prop_json[u'prop_name'].index(u'排烟温度')
        exhaust_gas_temperature = float(device_prop_json[u'prop_value'][exhaust_gas_temperature_index])
        gas_heat_theta_0 = gas_specific_heat * (exhaust_gas_temperature - gas_out_temp) * gas_flow_theta_0 / 3600.
        gas_heat_theta_1 = gas_specific_heat * (exhaust_gas_temperature - gas_out_temp) * gas_flow_theta_1 / 3600.
    return gas_heat_theta_0, gas_heat_theta_1


def get_alpha_warm_water_LiBr(device_type=None):
    '''
    获取温水溴化锂的制冷量(p_cool)与温水量(y_water)的关系
    input(设备小类型)
    y_water = alpha_1 * p_cool + alpha_0
    return(alpha_0, alpha_1)
    '''
    if device_type == '3':
        return 0.0530493231126, 0.033810256525
    elif device_type == '4':
        return 0.242226240225, 0.204577788533
    elif device_type == '2':
        return 0.0188712876527, 0.0816977798704
    elif device_type == '5':
        return 0.061519299221, -0.107202085072
    else:
        return 0, 0


def get_alpha_steam_LiBr(steam_pressure=None):
    '''
    获取蒸汽溴化锂的
    制冷量(p_cool)与蒸汽消耗量(steam_p)的关系
    input(蒸汽压力 MPa)
    steam_p = alpha_1 * p_cool + alpha_0
    return(alpha_0, alpha_1)
    '''
    if steam_pressure == 0.4:
        return -0.0268358429424, 1.14606538233
    elif steam_pressure == 0.6:
        return -0.11969904766, 1.14613538503
    elif steam_pressure == 0.8:
        return 23.7352284749, 1.13162926937
    else:
        # TODO 外部汽源压力不符合的时候如何计算
        return 23.7352284749, 1.13162926937


def get_alpha_gas_LiBr(device_type):
    '''
    获取烟气溴化锂的
    制冷量(p_cool)与烟气耗量(gas_flow)/燃料耗量(fuel_cool)的关系
    供暖量(p_heat)与烟气耗量(gas_flow)/燃料耗量(fuel_heat)
    input(设备小类型)
    gas_flow = alpha_gas_cool_1 * p_cool + alpha_gas_cool_0
    fuel_cool = alpha_fuel_cool_1 * p_cool + alpha_fuel_cool_0
    gas_flow = alpha_gas_heat_1 * p_heat + alpha_gas_heat_0
    fuel_heat = alpha_fuel_heat_1 * p_heat + alpha_fuel_heat_0
    制冷量(p_cool)与供暖量(p_heat)的关系
    p_heat =  alpha_heat_cool_1 * p_cool + alpha_heat_cool_0
    return(dict)
    '''
    if device_type == '8':
        return {
            'cool_gas': (-0.918182670244, 6.82612305936), 'cool_fuel': (0, 0),
            'heat_gas': (-3.58652351331, 8.53475038442), 'heat_fuel': (0, 0),
            'heat_cool': (0.310042197226, 0.799827671724)
        }
    elif device_type == '9':
        return {
            'cool_gas': (-0.944965254179, 6.82649087598), 'cool_fuel': (-0.0233616849136, 0.0592357651983),
            'heat_gas': (-0.974527210362, 8.15958929007), 'heat_fuel': (-0.0238793996047, 0.083448324764),
            'heat_cool': (0.0332654714475, 0.836649206909)
        }
    else:
        return {
            'cool_gas': (0, 0), 'cool_fuel': (0, 0),
            'heat_gas': (0, 0), 'heat_fuel': (0, 0),
            'heat_cool': (0, 0)
        }


def get_alpha_gas_warm_water_LiBr(device_type):
    '''
    获取烟气热水溴化锂的
    制冷量(p_cool)与供暖量(p_heat)的关系
    制冷量(p_cool)与燃料耗量(fuel_cool/fuel_heat)的关系
    input(设备小类型)
    p_heat = alpha_cool_heat_1 * p_cool + alpha_cool_heat_0
    fuel_cool = alpha_fuel_cool_1 * p_cool + alpha_fuel_cool_0
    fuel_heat = alpha_fuel_heat_1 * p_heat + alpha_fuel_heat_0 = alpha_fuel_heat_1 * alpha_cool_heat_1 * p_cool + alpha_fuel_heat_1 * alpha_cool_heat_0 + alpha_fuel_heat_0
    return(dict)
    '''
    if device_type == '6':
        return {
            'cool_gas': (0, 0.20965608465608465608465608465608), 'cool_fuel': (-0.0154912317292, 0.0592175099832),
            'heat_gas': (0, 0.11746031746031746031746031746032), 'heat_fuel': (0.0267172928093, 0.0834264221335),
            'heat_cool': (-0.100552156948, 0.836415088463)
        }
    elif device_type == '7':
        return {
            'cool_gas': (0, 0.20965608465608465608465608465608), 'cool_fuel': (0, 0),
            'heat_gas': (0, 0.11746031746031746031746031746032), 'heat_fuel': (0, 0),
            'heat_cool': (-0.0322605675412, 0.560585974844)
        }
    else:
        return {
            'cool_gas': (0, 0), 'cool_fuel': (0, 0),
            'heat_gas': (0, 0), 'heat_fuel': (0, 0),
            'heat_cool': (0, 0)
        }


def get_alpha_three_use_LiBr(device_type):
    '''
    获取溴化锂吸收式直燃型三用机的
    制冷量(p_cool)与燃料耗量(fuel_cool)的关系
    供暖量(p_heat)与燃料耗量(fuel_heat)的关系
    input(设备小类型)
    fuel_cool = alpha_fuel_cool_1 * p_cool + alpha_fuel_cool_0
    fuel_heat = alpha_fuel_heat_1 * p_heat + alpha_fuel_heat_0
    return(dict)
    '''
    if device_type == '10':
        return {
            'cool_fuel': (-0.0203246837677, 0.0592410631516), 'heat_fuel': (-0.00521820778582, 0.0834323488435)
        }
    else:
        return {
            'cool_fuel': (0, 0), 'heat_fuel': (0, 0)
        }


def get_json_data(json_str, name, number=1):
    '''
    解析json字符串，获取对应key的数值
    input(json字符串，key值，设备数量)
    return(对应数值 * 设备数量)
    '''
    index = json_str[u'prop_name'].index(name)
    if json_str[u'prop_value'][index]:
        data = float(json_str[u'prop_value'][index]) * number
    else:
        data = 0
    return data


def get_consumption_running_ratio_dict(electric=0, gas=0, water=0, power=1):
    '''
    计算设备运行状态中会随自身输出变化而变化的自消耗与设备输出的比值
    '''
    return{'gas': gas / power, 'electric': electric / power, 'water': water / power}


def get_consumption_running_cost(consumption_running_ratio_dict, price, key):
    '''
    计算设备运行状态中会随自身输出变化而变化的自消耗所对应的成本系数
    return(燃气耗量成本系数+水耗量成本系数+电耗量成本系数)
    '''
    gas = consumption_running_ratio_dict[key]['gas'] * price[u'gas']
    water = consumption_running_ratio_dict[key]['water'] * price[u'water']
    electric = consumption_running_ratio_dict[key]['electric'] * price[u'electric']
    return gas + water + electric


def get_peak_ita(need, price, special=False, used_devices_list=[]):
    '''
    创建需求对应的调峰成本系数矩阵
    系数为对应的需求使用调峰设备来补全的时候的成本价
    return(电，蒸汽，冷，热(LiBr)，热(缸套水板换)，热水，空气)
    '''
    global boiler_params
    used_devices_class_list = list(map(lambda x: x['device_class'], used_devices_list))
    steam_production, gas_consumption, gas_steam_ratio = gas_boiler_param_calculate(mode=2)
    hot_water_yield, gas_consumption, gas_hot_water_ratio = gas_boiler_param_calculate(mode=1)
    if u'10' in used_devices_class_list:
        ita_electric_c = -price['electric']
    else:
        ita_electric_c = 0
    # 热水和蒸汽需要考虑锅炉的补水消耗，以及可能的电消耗，不仅仅是燃气消耗产生的成本
    if need['cool'] > 0 and u'2' in used_devices_class_list:
        ita_cool_c = -price['electric'] / AlgoConstants.electric_cool_cop
    else:
        ita_cool_c = 0
    if (need['heat'] > 0 or need['hot_water'] > 0) and boiler_params['1']:
        ita_heat_c = -(price['gas'] * gas_hot_water_ratio + price['water'] * AlgoConstants.supply_water_coefficient + price['electric'] * AlgoConstants.hot_water_boiler_electric_power) / 700.
        ita_hot_water_c = -(price['gas'] * gas_hot_water_ratio + price['water'] * AlgoConstants.supply_water_coefficient + price['electric'] * AlgoConstants.hot_water_boiler_electric_power)
    else:
        ita_heat_c = 0
        ita_hot_water_c = 0
    if need['steam'] > 0 and boiler_params['2']:
        ita_steam_c = -price['gas'] * gas_steam_ratio - (price['water'] * AlgoConstants.supply_water_coefficient + price['electric'] * AlgoConstants.steam_boiler_electric_power)
    else:
        ita_steam_c = 0
    ita_air_c = 0
    if special:
        c = numpy.array([ita_electric_c, ita_steam_c, ita_cool_c, ita_heat_c, ita_heat_c, ita_hot_water_c, ita_air_c])
    else:
        c = numpy.array([ita_electric_c, ita_steam_c, ita_cool_c, ita_heat_c, ita_heat_c, ita_hot_water_c, ita_air_c])
    return c


def get_consumption_peak_ratio(electric, waste):
    '''
    获取调峰设备的资源消耗量与设备输出的比值
    例: 天然气耗量/燃气蒸汽锅炉产汽
    consumption_peak_ratio_dict中的key为7种输出，对应的值为dict，其中分为electric电耗量与输出比值、gas燃气耗量与输出比值、water水耗量与输出比值
    return(consumption_peak_ratio_dict)
    '''
    consumption_peak_ratio_dict = {'electric': None, 'steam': None, 'cool': None, 'heat': None, 'heat_plate': None, 'hot_water': None, 'air': None}
    consumption_peak_ratio_dict['cool'] = get_consumption_running_ratio_dict(electric=1. / AlgoConstants.electric_cool_cop)
    steam_production, gas_consumption, gas_steam_ratio = gas_boiler_param_calculate(mode=2)
    if gas_steam_ratio != 0:
        consumption_peak_ratio_dict['steam'] = get_consumption_running_ratio_dict(gas=gas_consumption, power=steam_production)
    hot_water_yield, gas_consumption, gas_hot_water_ratio = gas_boiler_param_calculate(mode=1)
    if gas_hot_water_ratio != 0:
        consumption_peak_ratio_dict['heat_plate'] = get_consumption_running_ratio_dict(gas=gas_consumption, power=hot_water_yield * 700)
        consumption_peak_ratio_dict['hot_water'] = get_consumption_running_ratio_dict(gas=gas_consumption, power=hot_water_yield)
    return consumption_peak_ratio_dict


def get_devices_consumption_running_ratio(electric, waste):
    '''
    获取设备运行状态中资源消耗量与设备输出的比值
    例: 天然气耗量/燃机出力
    consumption_running_ratio_dict中的key为7种输出，对应的值为dict，其中分为electric电耗量与输出比值、gas燃气耗量与输出比值、water水耗量与输出比值
    return(consumption_running_ratio_dict)
    '''
    electric_device_prop_json = json.loads(electric[u'props'])
    consumption_running_ratio_dict = {'electric': None, 'steam': None, 'cool': None, 'heat': None, 'heat_plate': None, 'hot_water': None, 'air': None}
    if electric[u'class'] == '4':
        # 燃机耗能
        power = get_json_data(electric_device_prop_json, u'燃机出力')
        consumption_running_ratio_dict['electric'] = get_consumption_running_ratio_dict(
            electric=power * AlgoConstants.gas_turbine_electric_coefficient,
            gas=get_json_data(electric_device_prop_json, u'天然气耗量'),
            power=power
        )
    elif electric[u'class'] == '5':
        # 内燃机耗能
        power = get_json_data(electric_device_prop_json, u'电功率')
        consumption_running_ratio_dict['electric'] = get_consumption_running_ratio_dict(
            electric=power * AlgoConstants.internal_combustion_engine_electric_coefficient,
            gas=get_json_data(electric_device_prop_json, u'燃气消耗量'),
            water=get_json_data(electric_device_prop_json, u'中冷器(2级)冷却水流量') + get_json_data(electric_device_prop_json, u'缸套水流量'),
            power=power
        )
    # 蒸汽锅炉耗电
    consumption_running_ratio_dict['steam'] = get_consumption_running_ratio_dict(
        electric=AlgoConstants.steam_boiler_electric_power
    )
    # 溴化锂设备的制冷耗能
    if waste[u'cool'] is not None and waste[u'cool']['device_id'] is not None:
        cool_device_prop_json = json.loads(waste[u'cool'][u'props'])
        cool_power = float(waste[u'cool'][u'load'])
        if waste[u'cool'][u'device_type'] == '6':
            # TODO 耗电，补燃的时候消耗燃气
            consumption_running_ratio_dict['cool'] = get_consumption_running_ratio_dict(
                water=(get_json_data(cool_device_prop_json, u'冷却水流量') + get_json_data(cool_device_prop_json, u'冷水流量')) * AlgoConstants.LiBr_supply_water_coefficient,
                # gas=get_json_data(cool_device_prop_json, u'燃料耗量（制冷时）'),
                power=cool_power
            )
        elif waste[u'cool'][u'device_type'] == '9':
            consumption_running_ratio_dict['cool'] = get_consumption_running_ratio_dict(
                water=(get_json_data(cool_device_prop_json, u'冷却水流量') + get_json_data(cool_device_prop_json, u'冷水流量')) * AlgoConstants.LiBr_supply_water_coefficient,
                # gas=get_json_data(cool_device_prop_json, u'燃料耗量（制冷时）'),
                power=cool_power
            )
        elif waste[u'cool'][u'device_type'] == '10':
            consumption_running_ratio_dict['cool'] = get_consumption_running_ratio_dict(
                water=(get_json_data(cool_device_prop_json, u'冷却水流量') + get_json_data(cool_device_prop_json, u'冷水流量')) * AlgoConstants.LiBr_supply_water_coefficient,
                # gas=get_json_data(cool_device_prop_json, u'燃料耗量（制冷时）天然气'),
                power=cool_power
            )
        else:
            consumption_running_ratio_dict['cool'] = get_consumption_running_ratio_dict(
                water=(get_json_data(cool_device_prop_json, u'冷却水流量') + get_json_data(cool_device_prop_json, u'冷水流量')) * AlgoConstants.LiBr_supply_water_coefficient,
                power=cool_power
            )
    # 溴化锂设备的供暖耗能
    if waste[u'heat'] is not None and waste[u'heat']['device_id'] is not None:
        heat_device_prop_json = json.loads(waste[u'heat'][u'props'])
        heat_power = float(waste[u'heat'][u'load'])
        if waste[u'heat'][u'device_type'] == '6':
            consumption_running_ratio_dict['heat'] = get_consumption_running_ratio_dict(
                water=get_json_data(heat_device_prop_json, u'冷却水流量') + get_json_data(heat_device_prop_json, u'冷水流量'),
                gas=get_json_data(heat_device_prop_json, u'燃料耗量（采暖时）'),
                power=heat_power
            )
        elif waste[u'heat'][u'device_type'] == '9':
            consumption_running_ratio_dict['heat'] = get_consumption_running_ratio_dict(
                water=get_json_data(heat_device_prop_json, u'冷却水流量') + get_json_data(heat_device_prop_json, u'冷水流量'),
                gas=get_json_data(heat_device_prop_json, u'燃料耗量（采暖时）'),
                power=heat_power
            )
        elif waste[u'heat'][u'device_type'] == '10':
            consumption_running_ratio_dict['heat'] = get_consumption_running_ratio_dict(
                water=get_json_data(heat_device_prop_json, u'冷却水流量') + get_json_data(heat_device_prop_json, u'冷水流量'),
                gas=get_json_data(heat_device_prop_json, u'燃料耗量（制热时）天然气'),
                power=heat_power
            )
        else:
            consumption_running_ratio_dict['heat'] = get_consumption_running_ratio_dict(
                water=get_json_data(heat_device_prop_json, u'冷却水流量') + get_json_data(heat_device_prop_json, u'冷水流量'),
                power=heat_power
            )
    # 热水锅炉耗电
    consumption_running_ratio_dict['hot_water'] = get_consumption_running_ratio_dict(
        electric=AlgoConstants.hot_water_boiler_electric_power
    )
    if waste[u'air']:
        air_device_prop_json = json.loads(waste[u'air'][u'props'])
        air_flow = float(waste[u'air'][u'load']) * 60
        if waste[u'air'][u'device_type'] == '2':
            consumption_running_ratio_dict['air'] = get_consumption_running_ratio_dict(
                electric=get_json_data(air_device_prop_json, u'电机 KW') + get_json_data(air_device_prop_json, u'风扇电机KW'),
                power=air_flow
            )
        elif waste[u'air'][u'device_type'] == '1':
            consumption_running_ratio_dict['air'] = get_consumption_running_ratio_dict(
                electric=get_json_data(air_device_prop_json, u'电机 KW'),
                water=get_json_data(air_device_prop_json, u'水耗量 L/s') * 3600 / 1000.,
                power=air_flow
            )
    #  TODO 是否要加入蒸汽锅炉与热水锅炉补燃时的燃气耗量系数，该系数应该添加在哪里？heat_plate还是steam或者hot_water里面
    # 蒸汽锅炉补水
    if waste[u'waste_type'] == '1':
        consumption_running_ratio_dict['steam']['water'] = AlgoConstants.supply_water_coefficient
    # 热水锅炉补水
    if waste[u'waste_type'] == '3':
        consumption_running_ratio_dict['hot_water']['water'] = AlgoConstants.supply_water_coefficient
    return consumption_running_ratio_dict


def get_devices_consumption_running_cost_coefficient(electric, waste, need, price):
    '''
    获取设备自身的耗能所对应的成本系数(电、蒸汽、冷、热、水、空气)，与之后的调峰成本系数矩阵与单价矩阵相加得到最终的系数矩阵
    在某种工作状态下的系数
    比如:燃机发电量p(kW)，消耗燃气c(m³/h)，则有关系f(p) = c
    近似可以认为f(p) = a*p = c，发电量转换成对应的燃气耗量后乘以燃气价格就是对应
    的发电量的消耗所需要的成本价格，设燃气价格为cost_gas，则电功率消耗转换系数
    定义为electric_a = p*cost_gas
    类似的有发电量转换为耗水量后得到的系数electric_a = p_water*cost_water
    两个系数相加得到的就是设备发电同时消耗的燃气&水资源所对应的以发电量为基准的单位成本
    return(电功率消耗kW转换系数, 蒸汽消耗m³/h转换系数, 冷消耗kW转换系数, 热消耗kW转换系数, 水消耗m³/h转换系数, 燃气消耗m³/h转换系数)
    '''
    # consumption_running_ratio_dict = get_devices_consumption_running_ratio(electric, waste)
    consumption_running_ratio_dict = waste[u'consumption_running_ratio_dict']
    electric_a = steam_a = cool_a = heat_a = heat_a_2 = water_a = air_a = steam_a_2 = water_a_2 = 0.
    if electric[u'class'] == '4':
        # 燃机耗能
        electric_a = electric_a + get_consumption_running_cost(consumption_running_ratio_dict, price, 'electric')
    elif electric[u'class'] == '5':
        # 内燃机耗能
        electric_a = electric_a + get_consumption_running_cost(consumption_running_ratio_dict, price, 'electric')
    # 蒸汽锅炉耗电
    if need['steam'] > 0 and waste[u'steam'] is not None:
        steam_a = steam_a + get_consumption_running_cost(consumption_running_ratio_dict, price, 'steam')
    if need['cool'] > 0 and waste[u'cool']['device_id'] is not None:
        # 溴化锂设备的制冷耗能
        cool_a = cool_a + get_consumption_running_cost(consumption_running_ratio_dict, price, 'cool')
    if need['heat'] > 0 and waste[u'heat'] is not None:
        # 溴化锂设备的供暖耗能
        heat_a = heat_a + get_consumption_running_cost(consumption_running_ratio_dict, price, 'heat')
    # 热水锅炉耗电
    if need['hot_water'] and waste[u'heat'] is not None:
        water_a = water_a + get_consumption_running_cost(consumption_running_ratio_dict, price, 'hot_water')
    # 空压站耗电/耗水
    if need['air'] and waste[u'air'] is not None:
        air_a = air_a + get_consumption_running_cost(consumption_running_ratio_dict, price, 'air')
    steam_a_2 = steam_a
    water_a_2 = water_a
    # 蒸汽锅炉补水
    if waste[u'waste_type'] == '1':
        steam_a = steam_a + AlgoConstants.supply_water_coefficient * price[u'water']
        # 补燃
        steam_a_2 = steam_a + 3600. / (AlgoConstants.gas_caloricity * AlgoConstants.steam_boiler_efficiency) * price[u'gas']
    # 热水锅炉补水
    if waste[u'waste_type'] == '3':
        water_a = water_a + AlgoConstants.supply_water_coefficient * price[u'water']
        # 补燃
        water_a_2 = water_a + 3600. / (AlgoConstants.gas_caloricity * AlgoConstants.hot_water_boiler_efficiency) * price[u'gas']
    c_running_1 = numpy.array([electric_a, steam_a, cool_a, heat_a, heat_a_2, water_a, air_a])
    c_running_2 = numpy.array([electric_a, steam_a_2, cool_a, heat_a, heat_a_2, water_a_2, air_a])
    return c_running_1, c_running_2


def get_income_price_ita(need, price):
    '''
    计算资源对应的收入单价矩阵，用来和之前的调峰成本、自耗能系数相加得到最终的系数矩阵
    '''
    ita_electric_c = price['electric']
    if need['cool'] > 0:
        ita_cool_c = price['cool']
    else:
        ita_cool_c = 0
    if need['heat'] > 0 or need['hot_water'] > 0:
        ita_heat_c = price['heat']
        ita_hot_water_c = price['hot_water']
    else:
        ita_heat_c = 0
        ita_hot_water_c = 0
    if need['steam'] > 0:
        ita_steam_c = price['steam']
    else:
        ita_steam_c = 0
    ita_air_c = 0
    c_income = numpy.array([ita_electric_c, ita_steam_c, ita_cool_c, ita_heat_c, ita_heat_c, ita_hot_water_c, ita_air_c])
    return c_income


def get_consumption_running_load(output_x_key, consumption_running_ratio_dict_key, key='electric'):
    '''
    根据负荷数值output_x_key与对应的负荷转换系数字典consumption_running_ratio_dict_key
    以及对应的转换属性key，来计算某种资源的消耗量
    '''
    if consumption_running_ratio_dict_key:
        return output_x_key * consumption_running_ratio_dict_key[key]
    else:
        return 0


def get_devices_consumption_regular(electric, waste, x_matrix):
    '''
    获取设备自身的耗能常量(电、水、燃气)
    return(电功率消耗kW, 水消耗m³/h, 燃气消耗m³/h)
    '''
    electric_device_prop_json = json.loads(electric[u'props'])
    electric_consumption = water_consumption = gas_consumption = 0
    cool_device_id = 0
    if waste[u'cool'] and (float(x_matrix[2]) != 0):
        # 溴化锂设备的耗能
        cool_device_prop_json = json.loads(waste[u'cool'][u'props'])
        cool_device_id = waste[u'cool'][u'device_id']
        if waste[u'cool'][u'device_type'] != '10':
            electric_consumption = electric_consumption + get_json_data(cool_device_prop_json, u'合计', waste[u'cool']['number'])
        if waste[u'cool'][u'device_type'] == '10':
            electric_consumption = electric_consumption + get_json_data(cool_device_prop_json, u'鼓风机燃油', waste[u'cool']['number'])
    if waste[u'heat'] and (float(x_matrix[3]) != 0):
        heat_device_prop_json = json.loads(waste[u'heat'][u'props'])
        # 同时制冷制热的时候防止电耗能重复计算
        if cool_device_id != waste[u'heat'][u'device_id']:
            if waste[u'heat'][u'device_type'] != '10':
                # electric_index_1 = heat_device_prop_json[u'prop_name'].index(u'合计')
                # electric_consumption = electric_consumption + waste[u'heat']['number'] * float(heat_device_prop_json[u'prop_value'][electric_index_1])
                electric_consumption = electric_consumption + get_json_data(heat_device_prop_json, u'合计', waste[u'heat']['number'])
            else:
                # electric_index_1 = heat_device_prop_json[u'prop_name'].index(u'鼓风机燃油')
                # waste[u'heat']['number'] * float(heat_device_prop_json[u'prop_value'][electric_index_1])
                electric_consumption = electric_consumption + get_json_data(heat_device_prop_json, u'鼓风机燃油', waste[u'heat']['number'])
    if waste[u'air'] and (float(x_matrix[6]) != 0):
        air_device_prop_json = json.loads(waste[u'air'][u'props'])
        if waste[u'air'][u'device_type'] == '2':
            electric_consumption = electric_consumption + get_json_data(air_device_prop_json, u'风扇电机KW', waste[u'air']['number'])
        if waste[u'air'][u'device_type'] == '1':
            water_consumption = water_consumption + get_json_data(air_device_prop_json, u'水耗量 L/s', waste[u'air']['number']) * 3600 / 1000.
    if u'热泵' in out_resource_detail['cool'].keys() and out_resource_detail['cool'][u'热泵']['used'] == 1:
        electric_consumption = electric_consumption + out_resource_detail['cool'][u'热泵']['self_consumption']['electric']
    if u'热泵' in out_resource_detail['heat'].keys() and out_resource_detail['heat'][u'热泵']['used'] == 1:
        electric_consumption = electric_consumption + out_resource_detail['heat'][u'热泵']['self_consumption']['electric']
    return electric_consumption, water_consumption, gas_consumption


def get_constant(electric, waste, x_matrix, price, need, used_devices_list=[]):
    '''
    计算成本中的常数部分(设备运行中的固定消耗部分与调峰设备补足需求的部分)
    '''
    electric_consumption, water_consumption, gas_consumption = get_devices_consumption_regular(electric, waste, x_matrix)
    constant = 0
    c = get_peak_ita(need, price, used_devices_list=used_devices_list)
    if need['electric'] > 0:
        constant = constant + need['electric'] * float(-c[0])
    if need['steam'] > 0:
        constant = constant + need['steam'] * float(-c[1])
    if need['cool'] > 0:
        constant = constant + need['cool'] * float(-c[2])
    if need['heat'] > 0:
        constant = constant + need['heat'] * float(-c[3])
    if need['hot_water'] > 0:
        constant = constant + need['hot_water'] * float(-c[5])
    if need['air'] > 0:
        constant = constant + need['air'] * float(-c[6])
    constant = constant + electric_consumption * float(-c[0]) + water_consumption * price['water'] + gas_consumption * price['gas']
    # constant = constant + electric_consumption * float(-c[0]) + water_consumption * float(-c[4]) + gas_consumption * float(-c[3])
    return constant


def get_cost_applied_afterburning(result_1, c_matrix_2, waste, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    '''
    计算补燃段的运行情况
    '''
    # TODO 需要验证所有类型的情况
    # 蒸汽锅炉补燃
    if waste[u'waste_type'] == '1':
        if abs(bounds[1][1] - result_1.x[1]) < 1:
            new_bounds = (
                abs(bounds[0] - result_1.x[0]), (bounds[1][0], bounds[1][1] * AlgoConstants.afterburning_percentage),
                (bounds[2][0], bounds[2] - result_1.x[2]), (bounds[3][0], bounds[3] - result_1.x[3]), (bounds[4][0], bounds[4] - result_1.x[4]),
                (bounds[5][0], bounds[5] - result_1.x[5]), abs(bounds[6] - result_1.x[6])
            )
            result_2 = linprog(c_matrix_2, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=new_bounds, method='interior-point')
            if result_1.fun > result_2.fun:
                return result_2
    # 热水锅炉补燃
    elif waste[u'waste_type'] == '3':
        new_bounds = (bounds[0], bounds[1], bounds[2], bounds[3], bounds[4], (bounds[5][0], bounds[5][1] * (1 + AlgoConstants.afterburning_percentage)), bounds[6])
        result_2 = linprog(c_matrix_2, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=new_bounds, method='interior-point')
        if result_1.fun > result_2.fun:
            return result_2
    return result_1


def create_charge_device(heat_pump, charge_dict_array, electric_need, cool_need, heat_need):
    '''
    根据需求调研表创建储能设备实例
    '''
    use_electric_charge = use_cool_charge = use_heat_charge = False
    electric_quantity = cool_quantity = heat_quantity = 0
    if charge_dict_array is not None:
        for charge_dict in charge_dict_array:
            if charge_dict == u'水蓄能':
                use_cool_charge = use_heat_charge = True
                cool_quantity = cool_need
                heat_quantity = heat_need
            elif charge_dict == u'冰蓄能':
                use_cool_charge = True
                cool_quantity = cool_need
            elif charge_dict == u'电蓄能':
                use_electric_charge = True
                electric_quantity = electric_need
    if heat_pump:
        # 有热泵
        charge_device = ChargeDevice(use_electric_charge, use_cool_charge, use_heat_charge, True, electric_quantity * 0.3, cool_quantity * 0.3, heat_quantity * 0.3)
    else:
        # 无热泵
        charge_device = ChargeDevice(use_electric_charge, use_cool_charge, use_heat_charge, False, electric_quantity, cool_quantity, heat_quantity)
    return charge_device


def get_charge_coefficient(index, c_matrix, electric_charge, cool_charge):
    '''
    获取储能系数
    input(当前时间段index, 设备运行状态对应的成本矩阵)
    return(electric_charge, cool_charge)
    '''
    if index == 0:
        electric_charge['coefficient'] = c_matrix[0]
        electric_charge['index'] = index
        cool_charge['coefficient'] = c_matrix[2]
        cool_charge['index'] = index
    else:
        if c_matrix[0] < electric_charge['coefficient']:
            electric_charge['coefficient'] = c_matrix[0]
            electric_charge['index'] = index
        if c_matrix[2] < cool_charge['coefficient']:
            cool_charge['coefficient'] = c_matrix[2]
            cool_charge['index'] = index
        # print(index, electric_charge['coefficient'], cool_charge['coefficient'])
    return electric_charge, cool_charge


def get_charge_use(bounds, x_matrix, need):
    '''
    判断是否使用储能设备
    input(边界条件，运行状态，当前时刻需求)
    return(bool)
    '''
    use_electric_charge = use_cool_charge = use_heat_charge = False
    if abs(bounds[0][0] - x_matrix[0]) < 1:
        use_electric_charge = True
    if abs(bounds[0][1] - x_matrix[0]) < 1:
        use_electric_charge = False
    if need['cool'] > x_matrix[2]:
        use_cool_charge = True
    if need['heat'] > (x_matrix[3] + x_matrix[4]):
        use_heat_charge = True
    # if abs(bounds[2][0] - x_matrix[2]) < 1:
    #     use_cool_charge = True
    # if abs(bounds[2][1] - x_matrix[2]) < 1:
    #     use_cool_charge = False
    # if abs(bounds[3][0] - x_matrix[3]) < 1 or abs(bounds[4][0] - x_matrix[4]) < 1:
    #     use_heat_charge = True
    # if abs(bounds[3][1] - x_matrix[3]) < 1 and abs(bounds[4][1] - x_matrix[4]) < 1:
    #     use_heat_charge = False
    # print('success' if min(abs(bounds[0][0] - x_matrix[0]), abs(bounds[0][1] - x_matrix[0])) < 1 else 'failed')
    return {'electric': use_electric_charge, 'cool': use_cool_charge, 'heat': use_heat_charge}


def apply_charge(use_charge, charge_device, result, need):
    '''
    尝试储能设备的应用
    根据条件进行储能/放能
    '''
    error_electric = (need['electric'] - float(result.x[0])) if need['electric'] > 0 else (-float(result.x[0]))
    error_cool = (need['cool'] - float(result.x[2])) if need['cool'] > 0 else (-float(result.x[2]))
    error_heat = (need['heat'] - (float(result.x[3]) + float(result.x[4]))) if need['heat'] > 0 else (-(float(result.x[3]) + float(result.x[4])))
    release_electric = release_cool = release_heat = 0
    if charge_device.electric_charge > 0:
        if use_charge['electric']:
            release_electric = charge_device.release_electric()
            result.x[0] -= release_electric if result.x[0] > release_electric else 0
        else:
            charge_device.charge(-error_electric, 0, 0)
    else:
        charge_device.charge(-error_electric, 0, 0)
    if charge_device.cool_charge > 0:
        if use_charge['cool']:
            release_cool = charge_device.release_cool()
            result.x[2] -= release_cool if result.x[2] > release_cool else 0
        else:
            charge_device.charge(0, -error_cool, 0)
    else:
        charge_device.charge(0, -error_cool, 0)
    if charge_device.heat_charge > 0:
        if use_charge['heat']:
            release_heat = charge_device.release_heat()
            # TODO  储存的热能释放在溴化锂设备还是锅炉上
            result.x[4] -= release_heat if result.x[4] > release_heat else 0
        else:
            charge_device.charge(0, 0, -error_heat)
    else:
        charge_device.charge(0, 0, -error_heat)
    if release_electric != 0 or release_cool != 0 or release_heat != 0:
        return True
    # return release_electric, release_cool, release_heat
    return False


def get_cost_applied_charge(result, need, bounds, charge_device, c_matrix):
    '''
    计算应用储能之后得到的运行情况
    '''
    result_before = copy.deepcopy(result)
    use_charge = get_charge_use(bounds, result.x, need)
    # 应用储能
    released = apply_charge(use_charge, charge_device, result, need)
    result.fun = numpy.sum((result.x * c_matrix), axis=0)
    if released:
        # print(result_before.fun, result.fun)
        if result_before.fun > result.fun:
            return result
    return result_before


def get_price_dict_array(price_dict_list=None):
    '''
    弃用
    '''
    price_dict_array_summer = []
    price_dict_array_winter = []
    if price_dict_list is None:
        # 供电价格	元/kwh	峰平谷
        # 光伏发电价格	元/kwh	0.85
        # 风电价格	元/kwh	0.85
        # 天然气价格	元/Nm³	冬夏过度
        # 供汽价格	元/zt	120
        # 供暖价格	元/GJ	20
        # 供热水价格	元/t	10
        # 供冷价格	元/GJ	5
        # 水价	元/t	5.5
        price = {
            'electric': 0.8208, 'photovoltaic': 0.85, 'wind_electric': 0.85,
            'gas_summer': 2.46, 'gas_winter': 3.23, 'steam': 120,
            'heat': 20 * 3600. / 10**6, 'hot_water': 10, 'cool': 5 * 3600. / 10**6,
            'water': 5.5
        }
        price_summer = copy.deepcopy(price)
        price_winter = copy.deepcopy(price)
        price_summer['gas'] = price['gas_summer']
        price_winter['gas'] = price['gas_winter']
        for i in range(0, 24):
            new_price_summer = copy.deepcopy(price_summer)
            new_price_winter = copy.deepcopy(price_winter)
            if 8 <= i and i < 11 or 18 <= i and i < 23:
                new_price_summer['electric'] = 0.8208
                new_price_winter['electric'] = 0.8208
            if 7 <= i and i < 8 or 11 <= i and i < 18:
                new_price_summer['electric'] = 0.5193
                new_price_winter['electric'] = 0.5193
            if 0 <= i and i < 7 or 23 <= i and i < 24:
                new_price_summer['electric'] = 0.2178
                new_price_winter['electric'] = 0.2178
            price_dict_array_summer.append(new_price_summer)
            price_dict_array_winter.append(price_winter)
    else:
        for i in range(0, 24):
            price = {
                'electric': price_dict_list['price']['electric'], 'photovoltaic': price_dict_list['price']['photovoltaic'], 'wind_electric': price_dict_list['price']['wind_electric'],
                'gas_summer': price_dict_list['price']['gas_summer'], 'gas_winter': price_dict_list['price']['gas_winter'], 'steam': price_dict_list['price']['steam'],
                'heat': price_dict_list['price']['heat'] * 3600. / 10**6, 'hot_water': price_dict_list['price']['hot_water'], 'cool': price_dict_list['price']['cool'] * 3600. / 10**6,
                'water': price_dict_list['price']['water']
            }
            price_summer = copy.deepcopy(price)
            price_winter = copy.deepcopy(price)
            price_summer['gas'] = price['gas_summer']
            price_winter['gas'] = price['gas_winter']
            price_dict_array_summer.append(price_summer)
            price_dict_array_winter.append(price_winter)
    return price_dict_array_summer, price_dict_array_winter


def cost_optimization(electric, waste, need, price, electric_load_max, charge_device, used_devices_list):
    '''
    成本优化方法
    input(发电设备dict, 余热设备dict, 该时段负荷需求, 该时段资源价格, 提供的电需求最大值kW, 储能设备)
    '''
    if need[u'heat'] > 0 and need[u'cool'] > 0 and waste[u'heat'] and waste[u'cool']:
        heat_and_cool = True
    else:
        heat_and_cool = False
    result = None
    constant = None
    steam = waste[u'steam']
    cool = waste[u'cool']
    heat = waste[u'heat']
    hot_water = waste[u'hot_water']
    air = waste[u'air']
    mix = waste[u'mix']
    if waste[u'waste_type'] == '1':
        # 蒸汽型余热锅炉(系)
        gas_heat_theta_0, gas_heat_theta_1, heat_alpha, water_alpha = get_theta_steam_boiler(electric[u'props'], electric[u'class'], electric[u'id'], float(electric[u'load']) * electric[u'number'])
        cool_alpha_0, cool_alpha_1 = get_alpha_steam_LiBr(steam_pressure=0.4)
        A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2 = get_coefficient_matrix_steam_boiler(
            electric, waste, gas_heat_theta_0, gas_heat_theta_1, cool_alpha_0, cool_alpha_1, heat_alpha=heat_alpha, water_alpha=water_alpha,
            price=price, need=need, heat_and_cool=heat_and_cool, used_devices_list=used_devices_list
        )
    if waste[u'waste_type'] == '2':
        # 烟气溴化锂(系)
        # TODO 包含了特殊情况
        gas_heat_theta_0, gas_heat_theta_1 = get_boiler_gas_heat(electric[u'props'], electric[u'class'], electric[u'id'], float(electric[u'load']) * electric[u'number'])
        alpha_dict = get_alpha_gas_LiBr(device_type=cool['device_type'] if cool else None)
        A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2 = get_coefficient_matrix_gas_LiBr(
            electric, waste, gas_heat_theta_0, gas_heat_theta_1, alpha_dict=alpha_dict, device_class=electric[u'class'],
            price=price, need=need, heat_and_cool=heat_and_cool, used_devices_list=used_devices_list
        )
    if waste[u'waste_type'] == '3':
        # 余热热水锅炉(系)
        gas_heat_theta_0, gas_heat_theta_1 = get_theta_hot_water_boiler(electric[u'props'], electric[u'class'], electric[u'id'], float(electric[u'load']) * electric[u'number'])
        cool_alpha_0, cool_alpha_1 = get_alpha_warm_water_LiBr(device_type=cool['device_type'] if cool else None)
        A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2 = get_coefficient_matrix_hot_water_boiler(
            electric, waste, gas_heat_theta_0, gas_heat_theta_1, cool_alpha_0, cool_alpha_1,
            price=price, need=need, heat_and_cool=heat_and_cool, used_devices_list=used_devices_list
        )
    if waste[u'waste_type'] == '4':
        # 烟气热水型溴化锂(系)
        alpha_dict = get_alpha_gas_warm_water_LiBr(device_type=cool['device_type'] if cool else None)
        A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2 = get_coefficient_matrix_gas_warm_water_LiBr(
            electric, waste, alpha_dict=alpha_dict,
            price=price, need=need, heat_and_cool=heat_and_cool, used_devices_list=used_devices_list
        )
    if waste[u'waste_type'] == '5':
        # 溴化锂吸收式直燃型三用机(系)
        alpha_dict = get_alpha_three_use_LiBr()
        A_ub, b_ub, A_eq, b_eq, c, bounds, A_ub_2, b_ub_2, c_2, bounds_2 = get_coefficient_matrix_three_use_LiBr(
            electric, waste, alpha_dict=alpha_dict,
            price=price, need=need, heat_and_cool=heat_and_cool, used_devices_list=used_devices_list
        )
    charge_device_2 = copy.deepcopy(charge_device)
    c_running_1, c_running_2 = get_devices_consumption_running_cost_coefficient(electric, waste, need, price)
    # c_income = get_income_price_ita(need, price)
    c_income = [0, 0, 0, 0, 0, 0, 0]
    # 开始优化
    result = linprog(c_running_1 + c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='interior-point')
    # 常数部分
    constant = get_constant(electric, waste, result.x, price, need, used_devices_list=used_devices_list)
    # 补燃
    # result = get_cost_applied_afterburning(result, c_running_2 + c - c_income, waste, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    # 储能
    result = get_cost_applied_charge(result, need, bounds, charge_device, c_running_1 + c - c_income)
    if heat_and_cool:
        result2 = linprog(c_running_1 + c_2 - c_income, A_ub=A_ub_2, b_ub=b_ub_2, A_eq=A_eq, b_eq=b_eq, bounds=bounds_2, method='interior-point')
        constant2 = get_constant(electric, waste, result2.x, price, need, used_devices_list=used_devices_list)
        # result2 = get_cost_applied_afterburning(result2, c_running_2 + c_2 - c_income, waste, A_ub=A_ub_2, b_ub=b_ub_2, A_eq=A_eq, b_eq=b_eq, bounds=bounds_2)
        result2 = get_cost_applied_charge(result2, need, bounds_2, charge_device_2, c_running_1 + c_2 - c_income)
        if result2.fun + constant2 >= result.fun + constant:
            return result, constant, {'running': c_running_1, 'peak': c, 'income': c_income}, charge_device
        else:
            return result2, constant2, {'running': c_running_1, 'peak': c_2, 'income': c_income}, charge_device_2
    else:
        return result, constant, {'running': c_running_1, 'peak': c, 'income': c_income}, charge_device


def step_electric_device(
    curve_dict_array, price_dict_array, heat_pump, charge_dict_array, electric_need,
    cool_need, heat_need, photovoltaic_curve, wind_curve, device_list, used_devices_list
):
    '''
    遍历设备方案，构建成本方程并进行优化，输出最优解
    工作状况，计算成本
    '''
    phv = PhotovoltaicCurve()
    for case in device_list:
        electric_load_max = case[u'electric'][u'load'] * Decimal(case[u'electric'][u'number'])
        cost_total_min = 0
        for waste in case['waste']:
            success = True
            need_list = []
            cost_total = 0
            operating_state_list = []
            electric_charge = {}
            cool_charge = {}
            consumption_running_ratio_dict = get_devices_consumption_running_ratio(case[u'electric'], waste)
            consumption_peak_ratio_dict = get_consumption_peak_ratio(case[u'electric'], waste)
            waste[u'consumption_running_ratio_dict'] = copy.deepcopy(consumption_running_ratio_dict)
            waste[u'consumption_peak_ratio_dict'] = copy.deepcopy(consumption_peak_ratio_dict)
            waste[u'photovoltaic'] = photovoltaic_curve
            charge_device = create_charge_device(heat_pump, charge_dict_array, electric_need, cool_need, heat_need)
            for index in range(0, 24):
                need = {
                    'heat': get_running_curve(curve_dict_array[u'heat_curve'], out_resource['heat'], index),
                    'cool': get_running_curve(curve_dict_array[u'cool_curve'], out_resource['cool'], index),
                    'steam': get_running_curve(curve_dict_array[u'steam_curve'], out_resource['steam'], index=index),
                    'electric': get_running_curve(curve_dict_array[u'electric_curve'], index=index, photovoltaic=photovoltaic_curve, wind=wind_curve),
                    'hot_water': get_running_curve(curve_dict_array[u'hot_water_curve'], out_resource['hot_water'], index),
                    'air': get_running_curve(curve_dict_array[u'air_curve'], out_resource['air'], index=index)
                }
                if index == 13:
                    print('here')
                # if index != 0:
                #     charge_device.charge(not use_charge['electric'], not use_charge['cool'], use_charge['heat'])
                price = price_dict_array[index]
                optimization_result, constant, c_matrix, charge_device = cost_optimization(case[u'electric'], waste, need, price, electric_load_max, charge_device, used_devices_list)
                electric_consumption, water_consumption, gas_consumption = get_devices_consumption_regular(case[u'electric'], waste, optimization_result.x)
                # electric_charge, cool_charge = get_charge_coefficient(index, c_matrix['running'] + c_matrix['peak'], electric_charge, cool_charge)
                if not optimization_result.success:
                    # 方案无效
                    success = False
                    print('need: %s, heat: %s' % (need, need[u'heat']))
                    break
                cost = optimization_result['fun'] + constant
                cost_total = cost_total + cost
                operating_state_list.append({
                    'cost': cost, 'income': float(numpy.sum(c_matrix['income'] * optimization_result.x, axis=0)), 'output_x': optimization_result.x.tolist(),
                    'charge': charge_device.to_dict(), 'constant_electric_consumption': electric_consumption, 'constant_water_consumption': water_consumption,
                    'constant_gas_consumption': gas_consumption
                })
                need_list.append(need)
            if success:
                waste[u'operating_state'] = operating_state_list
                waste[u'operating_cost_total'] = cost_total
                waste[u'need_list'] = need_list
                waste[u'out_resource'] = out_resource_detail
                if cost_total_min == 0:
                    cost_total_min = cost_total
                elif cost_total_min >= cost_total:
                    cost_total_min = cost_total
                waste[u'is_success'] = True
            else:
                waste[u'is_success'] = False
                break
        case[u'operating_cost_total_min'] = cost_total_min
    for case in device_list:
        case['waste'] = filter(lambda waste: waste[u'is_success'], case['waste'])
        # 升序排列每种方案的运行成本
        case['waste'].sort(key=lambda waste: waste[u'operating_cost_total'], reverse=False)


def match_curve(requirement, used_devices_list):
    '''
    匹配曲线
    '''
    need_curve, photovoltaic_vurve = get_curve(requirement)
    price, req = get_need_and_price(requirement, 'day_1')
    if req:
        step_electric_device(
            need_curve[u'day_1'], price, req[u'热泵'], req[u'蓄能'], req[u'电力需求'],
            req[u'冷负荷'], req[u'热负荷'], photovoltaic_vurve, req[u'风电曲线'], device_list, used_devices_list
        )
    price, req = get_need_and_price(requirement, 'day_2')
    if req:
        step_electric_device(
            need_curve[u'day_2'], price, req[u'热泵'], req[u'蓄能'], req[u'电力需求'],
            req[u'冷负荷'], req[u'热负荷'], photovoltaic_vurve, req[u'风电曲线'], device_list_day_2, used_devices_list
        )
    price, req = get_need_and_price(requirement, 'day_3')
    if req:
        step_electric_device(
            need_curve[u'day_3'], price, req[u'热泵'], req[u'蓄能'], req[u'电力需求'],
            req[u'冷负荷'], req[u'热负荷'], photovoltaic_vurve, req[u'风电曲线'], device_list_day_3, used_devices_list
        )
    price, req = get_need_and_price(requirement, 'day_4')
    if req:
        step_electric_device(
            need_curve[u'day_4'], price, req[u'热泵'], req[u'蓄能'], req[u'电力需求'],
            req[u'冷负荷'], req[u'热负荷'], photovoltaic_vurve, req[u'风电曲线'], device_list_day_4, used_devices_list
        )
    return 0


def get_running_consumption(requirement, used_devices_list):
    '''
    获取设备运行时的消耗量
    '''
    peak_devices = get_peak_devices(used_devices_list)
    price, req = get_need_and_price(requirement, 'day_1')
    if req:
        get_running_consumption_sub(req, device_list, typical_day='1', peak_devices=peak_devices)
    price, req = get_need_and_price(requirement, 'day_2')
    if req:
        get_running_consumption_sub(req, device_list_day_2, typical_day='2', peak_devices=peak_devices)
    price, req = get_need_and_price(requirement, 'day_3')
    if req:
        get_running_consumption_sub(req, device_list_day_3, typical_day='3', peak_devices=peak_devices)
    price, req = get_need_and_price(requirement, 'day_4')
    if req:
        get_running_consumption_sub(req, device_list_day_4, typical_day='4', peak_devices=peak_devices)


def get_running_consumption_sub(requirement, device_list, typical_day='1', peak_devices={}):
    '''
    获取设备运行时的消耗量
    '''
    for case in device_list:
        need_curve, photovoltaic_vurve = get_curve(requirement)
        if typical_day == '1':
            case[u'need'] = copy.deepcopy(need_curve[u'day_1'])
        elif typical_day == '2':
            case[u'need'] = copy.deepcopy(need_curve[u'day_2'])
        elif typical_day == '3':
            case[u'need'] = copy.deepcopy(need_curve[u'day_3'])
        elif typical_day == '4':
            case[u'need'] = copy.deepcopy(need_curve[u'day_4'])
        self_electirc_list = []
        self_water_list = []
        self_gas_list = []
        for waste in case['waste']:
            waste[u'consumption_running'] = {}
            for state in waste[u'operating_state']:
                index = waste[u'operating_state'].index(state)
                electric_consumption = state['constant_electric_consumption']
                water_consumption = state['constant_water_consumption']
                gas_consumption = state['constant_gas_consumption']
                state['peak_x'] = [
                    0,
                    get_peak_out_running_curve(case[u'need'][u'steam_curve'], state['output_x'][1], index=index, out_resource=out_resource['steam'], peak_devices=peak_devices['steam']),
                    get_peak_out_running_curve(case[u'need'][u'cool_curve'], state['output_x'][2], index=index, out_resource=out_resource['cool'], peak_devices=peak_devices['cool']),
                    get_peak_out_running_curve(case[u'need'][u'heat_curve'], (state['output_x'][3] + state['output_x'][4]), index=index, out_resource=out_resource['heat'], peak_devices=peak_devices['heat']),
                    0,
                    get_peak_out_running_curve(case[u'need'][u'hot_water_curve'], state['output_x'][5], index=index, out_resource=out_resource['hot_water'], peak_devices=peak_devices['hot_water']),
                    get_peak_out_running_curve(case[u'need'][u'air_curve'], state['output_x'][6], index=index, out_resource=out_resource['air']),
                ]
                for key, v in AlgoConstants.device_running_dict.items():
                    electric_consumption = electric_consumption + get_consumption_running_load(state['output_x'][v], waste[u'consumption_running_ratio_dict'][key], key='electric') + get_consumption_running_load(state['peak_x'][v], waste[u'consumption_peak_ratio_dict'][key], key='electric')
                    gas_consumption = gas_consumption + get_consumption_running_load(state['output_x'][v], waste[u'consumption_running_ratio_dict'][key], key='gas') + get_consumption_running_load(state['peak_x'][v], waste[u'consumption_peak_ratio_dict'][key], key='gas')
                    water_consumption = water_consumption + get_consumption_running_load(state['output_x'][v], waste[u'consumption_running_ratio_dict'][key], key='water') + get_consumption_running_load(state['peak_x'][v], waste[u'consumption_peak_ratio_dict'][key], key='water')
                self_electirc_list.append(electric_consumption)
                self_water_list.append(water_consumption)
                self_gas_list.append(gas_consumption)
                state['peak_x'][0] = get_peak_out_running_curve(case[u'need'][u'electric_curve'], state['output_x'][0], electric_consumption, index, out_resource=0, photovoltaic=waste[u'photovoltaic'], wind=requirement[u'风电曲线'], peak_devices=peak_devices['electric'])
                state['after_burning_x'] = [
                    0,
                    get_after_burning_curve(case[u'need'][u'steam_curve'], state['output_x'][1], waste[u'waste_type'], waste[u'steam'], index=index),
                    0,
                    0,
                    get_after_burning_curve(case[u'need'][u'heat_curve'], state['output_x'][4], waste[u'waste_type'], waste[u'heat_plate'], index=index),
                    get_after_burning_curve(case[u'need'][u'hot_water_curve'], state['output_x'][5], waste[u'waste_type'], waste[u'hot_water'], index=index),
                    0
                ]
                state['out_resource_running'] = [
                    get_peak_out_running_curve(case[u'need'][u'electric_curve'], state['output_x'][0], electric_consumption, index, out_resource=0, photovoltaic=waste[u'photovoltaic'], wind=requirement[u'风电曲线'], mode='out_running'),
                    get_peak_out_running_curve(case[u'need'][u'steam_curve'], state['output_x'][1], index=index, out_resource=out_resource['steam'], mode='out_running'),
                    get_peak_out_running_curve(case[u'need'][u'cool_curve'], state['output_x'][2], index=index, out_resource=out_resource['cool'], mode='out_running'),
                    get_peak_out_running_curve(case[u'need'][u'heat_curve'], (state['output_x'][3] + state['output_x'][4]), index=index, out_resource=out_resource['heat'], mode='out_running'),
                    0,
                    get_peak_out_running_curve(case[u'need'][u'hot_water_curve'], state['output_x'][5], index=index, out_resource=out_resource['hot_water'], mode='out_running'),
                    get_peak_out_running_curve(case[u'need'][u'air_curve'], state['output_x'][6], index=index, out_resource=out_resource['air'], mode='out_running'),
                ]
            waste[u'wind'] = requirement[u'风电曲线']
            waste[u'consumption_running'][u'electric_consumption'] = self_electirc_list[:]
            waste[u'consumption_running'][u'water_consumption'] = self_water_list[:]
            waste[u'consumption_running'][u'gas_consumption'] = self_gas_list[:]
    # print(self_gas_list, self_electirc_list, self_water_list)


def create_data(requirement):
    price, req = get_need_and_price(requirement, 'day_1')
    if req:
        front_data_day_1 = create_data_sub(price, device_list)
    else:
        front_data_day_1 = None
    price, req = get_need_and_price(requirement, 'day_2')
    if req:
        front_data_day_2 = create_data_sub(price, device_list_day_2)
    else:
        front_data_day_2 = None
    price, req = get_need_and_price(requirement, 'day_3')
    if req:
        front_data_day_3 = create_data_sub(price, device_list_day_3)
    else:
        front_data_day_3 = None
    price, req = get_need_and_price(requirement, 'day_4')
    if req:
        front_data_day_4 = create_data_sub(price, device_list_day_4)
    else:
        front_data_day_4 = None
    return {u'front_data_day_1': front_data_day_1, u'front_data_day_2': front_data_day_2, u'front_data_day_3': front_data_day_3, u'front_data_day_4': front_data_day_4}


def create_data_sub(price, device_list):
    '''
    创建返回至页面的数据
    '''
    front_data = []
    global out_resource_detail
    for case in device_list:
        electric = {
            u'load': float(case[u'electric'][u'load']),
            u'unit': case[u'electric'][u'unit'],
            u'number': case[u'electric'][u'number'],
            u'id': case[u'electric'][u'id'],
            u'class': case[u'electric'][u'class'],
            u'props': json.loads(case[u'electric'][u'props'])
        }
        for waste in case['waste']:
            data_dict = {
                u'electric': electric, u'photovoltaic': case[u'photovoltaic'], u'wind': case[u'wind'],
                u'operating_cost_total_min': case['operating_cost_total_min'],
                u'need': case[u'need']
            }
            waste_transform = {
                u'steam': create_front_waste_heat_device_dict(waste[u'steam']),
                u'cool': create_front_waste_heat_device_dict(waste[u'cool']),
                u'heat': create_front_waste_heat_device_dict(waste[u'heat']),
                u'heat_plate': create_front_waste_heat_device_dict(waste[u'heat_plate']),
                u'hot_water': create_front_waste_heat_device_dict(waste[u'hot_water']),
                u'air': create_front_waste_heat_device_dict(waste[u'air']),
                u'mix': {
                    u'steam': waste[u'mix'][u'steam'] if waste[u'mix'] and u'steam' in waste[u'mix'] else None,
                    u'cool': waste[u'mix'][u'cool'] if waste[u'mix'] and u'cool' in waste[u'mix'] else None,
                    u'heat': waste[u'mix'][u'heat'] if waste[u'mix'] and u'heat' in waste[u'mix'] else None,
                    u'heat_plate': waste[u'mix'][u'heat_plate'] if waste[u'mix'] and u'heat_plate' in waste[u'mix'] else None,
                    u'hot_water': waste[u'mix'][u'hot_water'] if waste[u'mix'] and u'hot_water' in waste[u'mix'] else None
                },
                u'waste_type': waste[u'waste_type'],
                u'operating_state': waste[u'operating_state'],
                u'operating_cost_total': waste[u'operating_cost_total'],
                u'consumption_running_ratio_dict': waste[u'consumption_running_ratio_dict'],
                u'consumption_peak_ratio_dict': waste[u'consumption_peak_ratio_dict'],
                u'consumption_running': waste[u'consumption_running'],
                u'photovoltaic': waste[u'photovoltaic'] if out_resource_detail['electric'][u'光伏']['used'] == 1 else [0 for i in range(24)],
                u'wind': waste[u'wind'] if out_resource_detail['electric'][u'风电']['used'] == 1 else [0 for i in range(24)],
                u'out_resource': waste[u'out_resource']
            }
            data_dict[u'waste'] = waste_transform
            # data_dict[u'out_resource'] = out_resource
            data_dict[u'price'] = price
            front_data.append(data_dict)
    return front_data


def run_search_get_device(requirement, used_devices_list=None):
    '''
    设备匹配
    '''
    global device_list, device_list_day_2, device_list_day_3, device_list_day_4
    # set_waste_device_used(used_devices_list, requirement)
    power_generating_device_select(requirement, used_devices_list)
    waste_heat_device_select(requirement, used_devices_list)
    return {'day_1': device_list, 'day_2': device_list_day_2, 'day_3': device_list_day_3, 'day_4': device_list_day_4}


def get_graph_device_dict(plan):
    '''
    生成设备的连接图的每个方案
    '''
    device_dict_list = []
    device_dict = {}
    idx = 1
    device_dict['id'] = idx
    device_dict['parentId'] = u"开始"
    device_dict['name'] = plan[u'electric']['props']['prop_value'][0]
    device_dict_list.append(device_dict)
    for key, v in AlgoConstants.device_running_dict.items():
        waste = plan['waste']
        if key != 'electric' and waste[key]:
            device_dict_waste = {}
            idx = idx + 1
            device_dict_waste['id'] = idx
            device_dict_waste['parentId'] = 1
            if waste[key]['props']:
                device_dict_waste['name'] = waste[key]['props']['prop_value'][0] + waste[key]['props']['prop_value'][1]
            else:
                device_dict_waste['name'] = u'板换'
            device_dict_list.append(device_dict_waste)
    return device_dict_list


def device_graph(front_data):
    '''
    生成设备的连接图
    TODO
    '''
    for typical_day in front_data.values():
        if typical_day:
            for plan in typical_day:
                get_graph_device_dict(plan)
        print(typical_day)
#     [{"id": "1", "parentId": "开始", "name": u"设备1"}
# , {"id": "2", "parentId": "1", "name": u"设备2"}
# , {"id": "3", "parentId": "1", "name": u"设备3"}
# , {"id": "4", "parentId": "3", "name": u"设备4"}
# , {"id": "5", "parentId": "2", "name": u"设备5"}
# , {"id": "6", "parentId": "5", "name": u"设备6"}
# , {"id": "7", "parentId": "4", "name": u"设备7"}
# , {"id": "8", "parentId": "4,7", "name": u"设备8"}
# , {"id": "9", "parentId": "8", "name": u"设备9"}
# , {"id": "10", "parentId": "7", "name": u"设备10"}
# , {"id": "11", "parentId": "8", "name": u"设备11"}
# ]
    return


def run_search(requirement, disabled_devices):
    start_time = time.clock()
    # # power_generating_device_select_test(requirement, disabled_devices_conditions)
    # # waste_heat_device_select_test(number=2)
    used_devices_list = get_used_devices()
    run_search_get_device(requirement, used_devices_list)
    match_curve(requirement, used_devices_list)
    peak_load_regulation_device_select(requirement)
    get_running_consumption(requirement, used_devices_list)
    front_data = create_data(requirement)
    # device_graph(front_data)
    end_time = time.clock()
    duration = round(end_time - start_time, 2)
    print 'time: %s' % duration
    # pool = ThreadPool(processes=4)
    # async_result = pool.apply_async(match_curve, [requirement])
    # return_val = async_result.get()
    # print 'time: %s' % duration
    # if return_val == 0:
    #     front_data = create_data()
    #     end_time = time.clock()
    #     duration = round(end_time - start_time, 2)
    #     print 'time: %s' % duration
    return front_data


def reset_data():
    global device_list, device_list_day_2, device_list_day_3, device_list_day_4, waste_heat_device,\
    air_device, peak_load_regulation_device, out_resource, out_resource_detail
    device_list = []
    device_list_day_2 = []
    device_list_day_3 = []
    device_list_day_4 = []
    waste_heat_device = []
    air_device = []
    # out_resource = {'electric': 0, 'steam': 0, 'cool': 0, 'heat': 0, 'hot_water': 0, 'air': 0}
    # out_resource_detail = {'steam': {}, 'cool': {}, 'heat': {}, 'hot_water': {}, 'air': {}}
    peak_load_regulation_device = []


class TestData():
    # curve = {
    #     u'heat_curve': [20000, 18000, 999, 999, 18000, 999, 999, 999, 999, 17000, 17000, 17000, 18000, 17000, 15000, 15000, 15000, 15000, 999, 999, 999, 999, 999, 999],
    #     # u'cool_curve': [2000, 1800, 1800, 1700, 1800, 999, 999, 999, 999, 1800, 1500, 1800, 1800, 1600, 1700, 1800, 1900, 999, 999, 999, 999, 999, 999, 999],
    #     u'cool_curve': None,
    #     # u'steam_curve': [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
    #     u'steam_curve': None,
    #     u'electric_curve': [10000, 12300, 8000, 14000, 13000, 12000, 999, 999, 999, 999, 999, 10000, 11000, 9000, 9900, 14000, 14500, 14600, 13800, 999, 999, 999, 999, 999],
    #     u'hot_water_curve': [1000, 1200, 1300, 1400, 999, 999, 999, 999, 600, 700, 800, 900, 1000, 1100, 1000, 1000, 1200, 999, 999, 999, 999, 999, 999, 999],
    #     u'air_curve': [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]
    # }
    # curve = {
    #     u'heat_curve': [20000, 18000, 999, 999, 18000, 19000, 0, 0, 0, 0, 0, 0, 18000, 17000, 15000, 15000, 15000, 15000, 0, 0, 0, 0, 0, 0],
    #     u'cool_curve': [0, 0, 0, 0, 0, 0, 1800, 1700, 1600, 1800, 1500, 1800, 0, 0, 0, 0, 0, 0, 999, 999, 999, 999, 999, 999],
    #     # u'cool_curve': None,
    #     # u'steam_curve': [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
    #     u'steam_curve': None,
    #     u'electric_curve': [10000, 12300, 8000, 14000, 13000, 12000, 999, 999, 999, 999, 999, 10000, 11000, 9000, 9900, 14000, 14500, 14600, 13800, 999, 999, 999, 999, 999],
    #     u'hot_water_curve': [10.00, 12.00, 13.00, 14.00, 9.99, 9.99, 9.99, 9.99, 6.00, 7.00, 8.00, 9.00, 1.000, 11.00, 10.00, 10.00, 12.00, 9.99, 9.99, 9.99, 9.99, 9.99, 9.99, 9.99],
    #     u'air_curve': [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]
    # }
    # 测试数据1
    # curve = {
    #     u'heat_curve': [11112, 18000, 999, 999, 18000, 19000, 0, 0, 0, 0, 0, 0, 18000, 17000, 15000, 15000, 15000, 15000, 0, 0, 0, 0, 0, 0],
    #     u'cool_curve': [1765, 0, 0, 0, 0, 0, 1800, 1700, 1600, 1800, 1500, 1800, 0, 0, 0, 0, 0, 0, 999, 999, 999, 999, 999, 999],
    #     # u'cool_curve': None,
    #     # u'steam_curve': [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
    #     u'steam_curve': None,
    #     u'electric_curve': [10000, 12300, 8000, 14000, 13000, 12000, 999, 999, 999, 999, 999, 10000, 11000, 9000, 9900, 14000, 14500, 14600, 13800, 999, 999, 999, 999, 999],
    #     u'hot_water_curve': [10.00, 12.00, 13.00, 14.00, 9.99, 9.99, 9.99, 9.99, 6.00, 7.00, 8.00, 9.00, 1.000, 11.00, 10.00, 10.00, 12.00, 9.99, 9.99, 9.99, 9.99, 9.99, 9.99, 9.99],
    #     u'air_curve': [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]
    # }
    # out_resource = {
    #     u'热泵': {u'地源热泵': {'cool': 100, 'heat': 200}, u'水源热泵': None, u'干热岩热泵': None, u'污水源热泵': None},
    #     u'蒸汽': {u'压力': 0.4, u'流量': 0.05},
    #     u'热水': {u'温度': 95, u'流量': 0.05},
    #     u'烟气': {u'压力': 0.4, u'流量': 0.05},
    #     # u'空压站余热利用': {u'进水温度': 10, u'出水温度': 55, u'流量': 10}
    #     u'空压站余热利用': None
    # }
    # photovoltaic_curve = [0, 0, 0, 0, 0, 0, 0, 10, 20, 50, 60, 70, 80, 100, 110, 80, 40, 10, 0, 0, 0, 0, 0, 0]
    # wind_curve = [500, 600, 400, 300, 500, 100, 200, 400, 300, 400, 200, 400, 600, 400, 500, 200, 300, 400, 200, 500, 300, 500, 400, 400]
    # requirement = {
    #     u'电力需求': 15000,
    #     u'热负荷': 20000,
    #     # u'热负荷': None,
    #     u'冷负荷': 2000,
    #     # u'冷负荷': None,
    #     # u'蒸汽需求': {u'压力': 1, u'温度': 200, u'总计': 300},
    #     u'蒸汽需求': None,
    #     # u'热水需求': None,
    #     u'热水需求': {u'压力': 1, u'温度': 200, u'总计': 300},
    #     u'供气需求': {u'压力': 0.8, u'温度': 50, u'流量': 1200, u'冷却类型': 1},
    #     u'热泵': None,
    #     u'蓄能': [u'水蓄能', u'电蓄能'],
    #     u'光伏': {
    #         u'名称': None,
    #         u'有效面积㎡': 1000,
    #         u'倾斜角': None,
    #         u'均布承载力': None
    #     },
    #     u'风电': None,
    #     u'外部资源': out_resource,
    #     u'已有电力需求': 500,
    #     u'已有热负荷': 1000,
    #     u'天然气耗量(冷)': 50,
    #     u'天然气耗量(热)': 60,
    #     u'燃料信息': {u'电价-峰': '8:00-11:30;18:30-23:00', u'电价-平': '7:00-8:00;11:30-18:30', u'电价-谷': '0:00-7:00;23:00-24:00'},
    #     u'光伏曲线': photovoltaic_curve,
    #     u'风电曲线': wind_curve,
    #     u'负荷曲线': curve
    # }
    # disabled_devices = [{u'device_class': '5', u'device_type': '1'}]
    disabled_devices = []
    # 测试数据2
    # curve数据可以获取
    curve = {
        u'heat_curve': [14680, 14680, 14680, 14680, 14680, 14680, 14680, 14680, 29946, 29946, 29946, 29946, 29946, 29946, 29946, 29946, 29946, 29946, 14680, 14680, 14680, 14680, 14680, 14680],
        # u'heat_curve': None,
        u'cool_curve': [2703.2, 0, 0, 0, 0, 0, 3494.5, 3487.5, 3441.0, 3424.6, 3513.6, 3625.3, 3712.8, 3734.6, 3831.6, 3937.9, 3887.4, 3805.5, 3755.1, 3768.7, 3936.5, 3887.4, 3857.4, 3871.0],
        # u'cool_curve': None,
        u'steam_curve': [8, 8.3, 7.9, 8.5, 8.7, 7.8, 7.8, 8.8, 8.9, 9.5, 9.8, 10, 9.5, 10.2, 10.5, 10.4, 10.7, 10, 9.5, 8.9, 8.5, 8, 8.2, 7.9],
        u'electric_curve': [15000, 16000, 4000, 4000, 3000, 4000, 4200, 3000, 6000, 9000, 9000, 8000, 5000, 5000, 5000, 7800, 9000, 12000, 9000, 13000, 11000, 11000, 16000, 15000],
        u'hot_water_curve': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 0, 0, 0, 15, 15, 15, 0, 0, 0, 0],
        u'air_curve': [100, 100, 100, 100, 100, 100, 100, 100, 120, 140, 140, 120, 120, 120, 120, 120, 120, 120, 100, 100, 100, 100, 100, 100]
    }
    # 热泵计算
    heat_pump = {u'可利用的绿化面积': 10000, u'生活污水': 100, u'工业污水': 100, u'类型': 1}
    heat_pump_data = get_heat_pump_data(heat_pump[u'可利用的绿化面积'], heat_pump[u'生活污水'] + heat_pump[u'工业污水'], heat_pump[u'类型'])
    out_resource = {
        u'热泵': None,
        # u'热泵': {u'地源热泵': {'cool': 100, 'heat': 200}, u'水源热泵': None, u'干热岩热泵': None, u'污水源热泵': None},
        u'蒸汽': None,
        # u'蒸汽': {u'压力': 0.4, u'流量': 0.05},
        u'热水': None,
        # u'热水': {u'温度': 55, u'流量': 9},
        u'烟气': None,
        # u'烟气': {u'压力': 0.4, u'流量': 0.05},
        u'空压站余热利用': {u'进水温度': 10, u'出水温度': 55, u'流量': 9}
    }
    # 每个时段光伏数据用拟合出来的数据
    photovoltaic_curve = [0, 0, 0, 0, 0, 0, 10, 30, 100, 200, 300, 450, 490, 550, 580, 470, 200, 80, 0, 0, 0, 0, 0, 0]
    wind_curve = [500, 600, 400, 300, 500, 100, 200, 400, 300, 400, 200, 400, 600, 400, 500, 200, 300, 400, 200, 500, 300, 500, 400, 400]
    price_dict_array_summer, price_dict_array_winter = get_price_dict_array()
    requirement = {
        u'电力需求': 16000,
        u'热负荷': 29946,
        u'冷负荷': 3990,
        u'蒸汽需求': {u'压力': 3.5, u'温度': 400, u'总计': 10.7},
        u'热水需求': {u'供水温度': 10, u'回水温度': 60, u'流量': 15},
        u'供气需求': {u'压力': 0.8, u'温度': 50, u'流量': 1200, u'冷却类型': 1},
        # True/False
        u'热泵': False,
        # list [u'水蓄能', u'电蓄能']
        u'蓄能': None,
        u'光伏': {
            u'名称': None,
            u'有效面积㎡': 14000,
            u'倾斜角': None,
            u'均布承载力': None,
            u'峰值功率': 1300,
            u'日出时间': '7:12',
            u'日落时间': '18:38'
        },
        u'风电': None,
        u'外部资源': out_resource,
        u'已有电力需求': 0,
        u'已有热负荷': 0,
        u'天然气耗量(冷)': 50,
        u'天然气耗量(热)': 60,
        u'价格-夏': price_dict_array_summer,
        u'价格-冬': price_dict_array_winter,
        u'光伏曲线': photovoltaic_curve,
        u'风电曲线': wind_curve,
        u'负荷曲线': {u'day_1': curve, u'day_2': curve, u'day_3': curve, u'day_4': curve}
    }
    # TODO LiBr 1%补水
