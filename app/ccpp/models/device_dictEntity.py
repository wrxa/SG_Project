# -*- coding: utf-8 -*-
import json
'''
将查找到的设备以及参数存放在此处
'''


class DeviceDict:

    def __init__(self, device, need_engine_demand_power, number):
        self.device = device
        self.number = number
        self.need_engine_demand_power = need_engine_demand_power
        self.props_json = json.loads(device.props_json)
