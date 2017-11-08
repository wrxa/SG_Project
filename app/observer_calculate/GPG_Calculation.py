# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97

# 原则性热力系统锅炉部分--过热蒸汽焓值
# F8=H_PT(F6,F7)
# F6: superheated_steam_outlet_pressure
# F7: superheated_steam_temperature
# F8: superheated_steam_enthalpy
class GPG_Boiler_superheated_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['superheated_steam_outlet_pressure'] != '' and \
            val['superheated_steam_temperature'] != '' and \
            val['superheated_steam_outlet_pressure'] is not None and \
            val['superheated_steam_temperature'] is not None:

            superheated_steam_enthalpy = seuif97.pt2h(
                float(val['superheated_steam_outlet_pressure']),
                float(val['superheated_steam_temperature'])
            )
            if superheated_steam_enthalpy >= 0:
                result.superheated_steam_enthalpy = superheated_steam_enthalpy
                
        # 没有则不做任何操作！


# 原则性热力系统锅炉部分--给水焓值
# F14=H_PT(F6,F13)
# F6: superheated_steam_outlet_pressure
# F13: boiler_feed_water_temperature
# F14: feedwater_enthalpy
class GPG_Boiler_feedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['superheated_steam_outlet_pressure'] != '' and \
            val['boiler_feed_water_temperature'] != '' and \
            val['superheated_steam_outlet_pressure'] is not None and \
            val['boiler_feed_water_temperature'] is not None:

            feedwater_enthalpy = seuif97.pt2h(
                float(val['superheated_steam_outlet_pressure']),
                float(val['boiler_feed_water_temperature'])
            )
            if feedwater_enthalpy >= 0:
                result.feedwater_enthalpy = feedwater_enthalpy
                
        # 没有则不做任何操作！


'''空气焓值部分公式未给'''
# 原则性热力系统锅炉部分--空气焓值
# F11=H_PT(F6,F10)
# F6: superheated_steam_outlet_pressure
# F10: air_temperature
# F11: air_enthalpy
class GPG_Boiler_air_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['superheated_steam_outlet_pressure'] != '' and \
            val['air_temperature'] != '' and \
            val['superheated_steam_outlet_pressure'] is not None and \
            val['air_temperature'] is not None:

            air_enthalpy = seuif97.pt2h(
                float(val['superheated_steam_outlet_pressure']),
                float(val['air_temperature'])
            )
            if air_enthalpy >= 0:
                result.air_enthalpy = air_enthalpy
                
        # 没有则不做任何操作！

# 原则性热力系统锅炉部分--饱和水温度
# F16=T_P(F6)
# F6: superheated_steam_outlet_pressure
# F16: saturation_water_temperature
class GPG_Boiler_saturation_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['superheated_steam_outlet_pressure'] != '' and \
            val['superheated_steam_outlet_pressure'] is not None:

            saturation_water_temperature = seuif97.tsat_p(
                float(val['superheated_steam_outlet_pressure']))

            if saturation_water_temperature >= 0:
                result.saturation_water_temperature = saturation_water_temperature
                
        # 没有则不做任何操作！


# 原则性热力系统锅炉部分--饱和水焓值
# F17=HL_P(F6)
# F6: superheated_steam_outlet_pressure
# F17: saturation_water_enthalpy
class GPG_Boiler_saturation_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['superheated_steam_outlet_pressure'] != '' and \
            val['superheated_steam_outlet_pressure'] is not None:

            saturation_water_enthalpy = seuif97.h_p(
                float(val['superheated_steam_outlet_pressure']))

            if saturation_water_enthalpy >= 0:
                result.saturation_water_enthalpy = saturation_water_enthalpy
                
        # 没有则不做任何操作！

if __name__ == "__main__":
    print("GPG_Calculation.py")