# -*- coding: utf-8 -*-
from base import FieldCalculation


# 实现字段inner_diameter_chimney:特殊处理部分--烟囱内径,的计算1
class Inner_diameter_chimney(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['flue_gas_quantity'] != '' and val['flue_gas_quantity'] is not None and val['pressure_exhaust_smoke'] != '' and val['pressure_exhaust_smoke'] is not None and val['temperature_exhaust_smoke'] != '' and val['temperature_exhaust_smoke'] is not None and val['flue_gas_flow_velocity'] != '' and val['flue_gas_flow_velocity'] is not None :
            inner_diameter_chimney = (float(val['flue_gas_quantity'])) * 0.101325 / 273 * (273 + (float(val['temperature_exhaust_smoke']))) / (float(val['pressure_exhaust_smoke'])) / (float(val['flue_gas_flow_velocity']))
            if inner_diameter_chimney != -1:
                if val['flg'] == 'design':
                    result.inner_diameter_chimney = inner_diameter_chimney / 3600.0
                elif val['flg'] == 'check':
                    result.inner_diameter_chimney_check = inner_diameter_chimney / 3600.0
        print(result)
