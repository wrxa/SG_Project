
# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97
from base import CalculationObserver, ExecuteStrategy
# from __future__ import division


# 实现字段engine_exhuast_gas_energy:特殊处理部分--排烟能量,的计算1
class Engine_exhuast_gas_energy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None:
            engine_exhuast_gas_energy = seuif97.h_kqccpp((float(val['engine_exhuast_gas_temperature'])))/1.34*(float(val['engine_exhuast_gas_flux']))/3.6
            if engine_exhuast_gas_energy != -1:
                if val['flg'] == 'design':
                    result.engine_exhuast_gas_energy_design = engine_exhuast_gas_energy
                elif val['flg'] == 'check':
                    result.engine_exhuast_gas_energy_check = engine_exhuast_gas_energy
        print(result)


# 实现字段boiler_afterburning_exhuast_energy:补燃后排烟能量,的计算2
class Boiler_afterburning_exhuast_energy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None:
            boiler_afterburning_exhuast_energy = (seuif97.h_kqccpp((float(val['engine_exhuast_gas_temperature'])))/1.34*(float(val['engine_exhuast_gas_flux']))/3.6)+(float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/3600
            if boiler_afterburning_exhuast_energy != -1:
                if val['flg'] == 'design':
                    result.boiler_afterburning_exhuast_energy_design = boiler_afterburning_exhuast_energy
                elif val['flg'] == 'check':
                    result.boiler_afterburning_exhuast_energy_check = boiler_afterburning_exhuast_energy
        print(result)


# 实现字段boiler_afterburning_exhuast_temperature:补燃后排烟温度,的计算3
class Boiler_afterburning_exhuast_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None:
            boiler_afterburning_exhuast_temperature = round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)
            if boiler_afterburning_exhuast_temperature != -1:
                if val['flg'] == 'design':
                    result.boiler_afterburning_exhuast_temperature_design = boiler_afterburning_exhuast_temperature
                elif val['flg'] == 'check':
                    result.boiler_afterburning_exhuast_temperature_check = boiler_afterburning_exhuast_temperature
        print(result)


# 实现字段high_engine_exhuast_gas_flux:燃机排烟流量,的计算4
class High_engine_exhuast_gas_flux(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None:
            high_engine_exhuast_gas_flux = (float(val['engine_exhuast_gas_flux']))*1000/1.34
            if high_engine_exhuast_gas_flux != -1:
                if val['flg'] == 'design':
                    result.high_engine_exhuast_gas_flux_design = high_engine_exhuast_gas_flux
                elif val['flg'] == 'check':
                    result.high_engine_exhuast_gas_flux_check = high_engine_exhuast_gas_flux
        print(result)


# 实现字段high_engine_exhuast_gas_temperature:燃机排烟温度,的计算5
class High_engine_exhuast_gas_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None:
            high_engine_exhuast_gas_temperature = (round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2))
            if high_engine_exhuast_gas_temperature != -1:
                if val['flg'] == 'design':
                    result.high_engine_exhuast_gas_temperature_design = high_engine_exhuast_gas_temperature
                elif val['flg'] == 'check':
                    result.high_engine_exhuast_gas_temperature_check = high_engine_exhuast_gas_temperature
        print(result)


# 实现字段high_engine_exhuast_gas_energy:特殊处理部分--燃机排烟能量,的计算6
class High_engine_exhuast_gas_energy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None:
            high_engine_exhuast_gas_energy = seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2))))
            if high_engine_exhuast_gas_energy != -1:
                if val['flg'] == 'design':
                    result.high_engine_exhuast_gas_energy_design = high_engine_exhuast_gas_energy
                elif val['flg'] == 'check':
                    result.high_engine_exhuast_gas_energy_check = high_engine_exhuast_gas_energy
        print(result)


# 实现字段high_steam_temperature:主蒸汽温度,的计算7
class High_steam_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['high_terminal_temperature_difference'] != '' and val['high_terminal_temperature_difference'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None:
            high_steam_temperature = ((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference']))
            if high_steam_temperature != -1:
                if val['flg'] == 'design':
                    result.high_steam_temperature_design = high_steam_temperature
                elif val['flg'] == 'check':
                    result.high_steam_temperature_check = high_steam_temperature
        print(result)


# 实现字段high_steam_enthalpy:特殊处理部分--主蒸汽焓值,的计算8
class High_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_terminal_temperature_difference'] != '' and val['high_terminal_temperature_difference'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None:
            high_steam_enthalpy = seuif97.pt2h((float(val['high_steam_pressure'])),(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference']))))
            if high_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.high_steam_enthalpy_design = high_steam_enthalpy
                elif val['flg'] == 'check':
                    result.high_steam_enthalpy_check = high_steam_enthalpy
        print(result)


# 实现字段high_drum_pressure:高压汽包压力,的计算9
class High_drum_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None:
            high_drum_pressure = (float(val['high_steam_pressure']))*1.05
            if high_drum_pressure != -1:
                if val['flg'] == 'design':
                    result.high_drum_pressure_design = high_drum_pressure
                elif val['flg'] == 'check':
                    result.high_drum_pressure_check = high_drum_pressure
        print(result)


# 实现字段high_evaporating_temperature:特殊处理部分--高压蒸发温度,的计算10
class High_evaporating_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None:
            high_evaporating_temperature = seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05))
            if high_evaporating_temperature != -1:
                if val['flg'] == 'design':
                    result.high_evaporating_temperature_design = high_evaporating_temperature
                elif val['flg'] == 'check':
                    result.high_evaporating_temperature_check = high_evaporating_temperature
        print(result)


# 实现字段high_evaporator_effluent_water_temperature:高压进蒸发器热水温度,的计算11
class High_evaporator_effluent_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None:
            high_evaporator_effluent_water_temperature = (seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))
            if high_evaporator_effluent_water_temperature != -1:
                if val['flg'] == 'design':
                    result.high_evaporator_effluent_water_temperature_design = high_evaporator_effluent_water_temperature
                elif val['flg'] == 'check':
                    result.high_evaporator_effluent_water_temperature_check = high_evaporator_effluent_water_temperature
        print(result)


# 实现字段high_evaporator_effluent_water_enthalpy:特殊处理部分--高压进蒸发器热水焓值,的计算12
class High_evaporator_effluent_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None:
            high_evaporator_effluent_water_enthalpy = seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))))
            if high_evaporator_effluent_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.high_evaporator_effluent_water_enthalpy_design = high_evaporator_effluent_water_enthalpy
                elif val['flg'] == 'check':
                    result.high_evaporator_effluent_water_enthalpy_check = high_evaporator_effluent_water_enthalpy
        print(result)


# 实现字段high_evaporator_effluent_smoke_temperature:高压出蒸发器烟气温度,的计算13
class High_evaporator_effluent_smoke_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None and val['high_proximity_temperature_difference'] != '' and val['high_proximity_temperature_difference'] is not None:
            high_evaporator_effluent_smoke_temperature = ((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference']))
            if high_evaporator_effluent_smoke_temperature != -1:
                if val['flg'] == 'design':
                    result.high_evaporator_effluent_smoke_temperature_design = high_evaporator_effluent_smoke_temperature
                elif val['flg'] == 'check':
                    result.high_evaporator_effluent_smoke_temperature_check = high_evaporator_effluent_smoke_temperature
        print(result)


# 实现字段high_evaporator_effluent_smoke_enthalpy:特殊处理部分--高压出蒸发器烟气焓值,的计算14
class High_evaporator_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None and val['high_proximity_temperature_difference'] != '' and val['high_proximity_temperature_difference'] is not None:
            high_evaporator_effluent_smoke_enthalpy = seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference']))))
            if high_evaporator_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.high_evaporator_effluent_smoke_enthalpy_design = high_evaporator_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.high_evaporator_effluent_smoke_enthalpy_check = high_evaporator_effluent_smoke_enthalpy
        print(result)


# 实现字段high_economizer_effluent_smoke_enthalpy:高压出省煤器烟气焓值,的计算15
class High_economizer_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['high_boiler_efficiency'] != '' and val['high_boiler_efficiency'] is not None and val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_terminal_temperature_difference'] != '' and val['high_terminal_temperature_difference'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None and val['high_proximity_temperature_difference'] != '' and val['high_proximity_temperature_difference'] is not None and val['high_blowdown_rate'] != '' and val['high_blowdown_rate'] is not None and val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None:
            high_economizer_effluent_smoke_enthalpy = (seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference'])))))-((((float(val['engine_exhuast_gas_flux']))*1000/1.34)*((seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['high_steam_pressure'])),(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference'])))))-(seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))))))/1000)*(1+(float(val['high_blowdown_rate']))))*((seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))))-((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))))*1000/(float(val['high_boiler_efficiency']))/((float(val['engine_exhuast_gas_flux']))*1000/1.34)
            if high_economizer_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.high_economizer_effluent_smoke_enthalpy_design = high_economizer_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.high_economizer_effluent_smoke_enthalpy_check = high_economizer_effluent_smoke_enthalpy
        print(result)


# 实现字段high_economizer_effluent_water_temperature:高压进省煤器热水温度,的计算16
class High_economizer_effluent_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None:
            high_economizer_effluent_water_temperature = (seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))
            if high_economizer_effluent_water_temperature != -1:
                if val['flg'] == 'design':
                    result.high_economizer_effluent_water_temperature_design = high_economizer_effluent_water_temperature
                elif val['flg'] == 'check':
                    result.high_economizer_effluent_water_temperature_check = high_economizer_effluent_water_temperature
        print(result)


# 实现字段high_economizer_effluent_water_enthalpy:特殊处理部分--高压进省煤器热水焓值,的计算17
class High_economizer_effluent_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None:
            high_economizer_effluent_water_enthalpy = seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))))
            if high_economizer_effluent_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.high_economizer_effluent_water_enthalpy_design = high_economizer_effluent_water_enthalpy
                elif val['flg'] == 'check':
                    result.high_economizer_effluent_water_enthalpy_check = high_economizer_effluent_water_enthalpy
        print(result)


# 实现字段high_gas_production:高压产汽量,的计算18
class High_gas_production(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['high_boiler_efficiency'] != '' and val['high_boiler_efficiency'] is not None and val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_terminal_temperature_difference'] != '' and val['high_terminal_temperature_difference'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None and val['high_proximity_temperature_difference'] != '' and val['high_proximity_temperature_difference'] is not None:
            high_gas_production = ((float(val['engine_exhuast_gas_flux']))*1000/1.34)*((seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['high_steam_pressure'])),(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference'])))))-(seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))))))/1000
            if high_gas_production != -1:
                if val['flg'] == 'design':
                    result.high_gas_production_design = high_gas_production
                elif val['flg'] == 'check':
                    result.high_gas_production_check = high_gas_production
        print(result)


# 实现字段high_feedwater_amount:给水量,的计算19
class High_feedwater_amount(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['high_boiler_efficiency'] != '' and val['high_boiler_efficiency'] is not None and val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_terminal_temperature_difference'] != '' and val['high_terminal_temperature_difference'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None and val['high_proximity_temperature_difference'] != '' and val['high_proximity_temperature_difference'] is not None and val['high_blowdown_rate'] != '' and val['high_blowdown_rate'] is not None:
            high_feedwater_amount = (((float(val['engine_exhuast_gas_flux']))*1000/1.34)*((seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['high_steam_pressure'])),(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference'])))))-(seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))))))/1000)*(1+(float(val['high_blowdown_rate'])))
            if high_feedwater_amount != -1:
                if val['flg'] == 'design':
                    result.high_feedwater_amount_design = high_feedwater_amount
                elif val['flg'] == 'check':
                    result.high_feedwater_amount_check = high_feedwater_amount
        print(result)


# 实现字段high_economizer_effluent_smoke_enthalpy_verify:特殊处理部分--高压出省煤器烟焓校核,的计算20
class High_economizer_effluent_smoke_enthalpy_verify(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None:
            high_economizer_effluent_smoke_enthalpy_verify = seuif97.h_kqccpp((float(val['high_economizer_effluent_smoke_temperature'])))
            if high_economizer_effluent_smoke_enthalpy_verify != -1:
                if val['flg'] == 'design':
                    result.high_economizer_effluent_smoke_enthalpy_verify_design = high_economizer_effluent_smoke_enthalpy_verify
                elif val['flg'] == 'check':
                    result.high_economizer_effluent_smoke_enthalpy_verify_check = high_economizer_effluent_smoke_enthalpy_verify
        print(result)


# 实现字段high_evaporator_effluent_steam_enthalpy:特殊处理部分--高压蒸发器出口蒸汽焓,的计算21
class High_evaporator_effluent_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None:
            high_evaporator_effluent_steam_enthalpy = seuif97.HG_P(10*((float(val['high_steam_pressure']))*1.05))
            if high_evaporator_effluent_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.high_evaporator_effluent_steam_enthalpy_design = high_evaporator_effluent_steam_enthalpy
                elif val['flg'] == 'check':
                    result.high_evaporator_effluent_steam_enthalpy_check = high_evaporator_effluent_steam_enthalpy
        print(result)


# 实现字段high_superheater_effluent_smoke_enthalpy:高压过热器出口烟焓,的计算22
class High_superheater_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['high_boiler_efficiency'] != '' and val['high_boiler_efficiency'] is not None and val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_terminal_temperature_difference'] != '' and val['high_terminal_temperature_difference'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None and val['high_proximity_temperature_difference'] != '' and val['high_proximity_temperature_difference'] is not None:
            high_superheater_effluent_smoke_enthalpy = (seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))))-(((float(val['engine_exhuast_gas_flux']))*1000/1.34)*((seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['high_steam_pressure'])),(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference'])))))-(seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))))))/1000)*1000*((seuif97.pt2h((float(val['high_steam_pressure'])),(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference'])))))-(seuif97.HG_P(10*((float(val['high_steam_pressure']))*1.05))))/(float(val['high_boiler_efficiency']))/((float(val['engine_exhuast_gas_flux']))*1000/1.34)
            if high_superheater_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.high_superheater_effluent_smoke_enthalpy_design = high_superheater_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.high_superheater_effluent_smoke_enthalpy_check = high_superheater_effluent_smoke_enthalpy
        print(result)


# 实现字段high_superheater_effluent_smoke_enthalpy_verify:特殊处理部分--高压过热器出口烟焓校核,的计算23
class High_superheater_effluent_smoke_enthalpy_verify(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_superheater_effluent_smoke_temperature'] != '' and val['high_superheater_effluent_smoke_temperature'] is not None:
            high_superheater_effluent_smoke_enthalpy_verify = seuif97.h_kqccpp((float(val['high_superheater_effluent_smoke_temperature'])))
            if high_superheater_effluent_smoke_enthalpy_verify != -1:
                if val['flg'] == 'design':
                    result.high_superheater_effluent_smoke_enthalpy_verify_design = high_superheater_effluent_smoke_enthalpy_verify
                elif val['flg'] == 'check':
                    result.high_superheater_effluent_smoke_enthalpy_verify_check = high_superheater_effluent_smoke_enthalpy_verify
        print(result)


# 实现字段low_effluent_smoke_temperature:进烟温度,的计算24
class Low_effluent_smoke_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None:
            low_effluent_smoke_temperature = (float(val['high_economizer_effluent_smoke_temperature']))-15
            if low_effluent_smoke_temperature != -1:
                if val['flg'] == 'design':
                    result.low_effluent_smoke_temperature_design = low_effluent_smoke_temperature
                elif val['flg'] == 'check':
                    result.low_effluent_smoke_temperature_check = low_effluent_smoke_temperature
        print(result)


# 实现字段low_effluent_smoke_enthalpy:特殊处理部分--进烟焓,的计算25
class Low_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None:
            low_effluent_smoke_enthalpy = seuif97.h_kqccpp(((float(val['high_economizer_effluent_smoke_temperature']))-15))
            if low_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_effluent_smoke_enthalpy_design = low_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.low_effluent_smoke_enthalpy_check = low_effluent_smoke_enthalpy
        print(result)


# 实现字段low_superheat_steam_temperature:低压过热蒸汽温度,的计算26
class Low_superheat_steam_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_superheat_steam_temperature_correct'] != '' and val['low_superheat_steam_temperature_correct'] is not None and val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None:
            low_superheat_steam_temperature = (float(val['high_economizer_effluent_smoke_temperature']))-(float(val['low_superheat_steam_temperature_correct']))
            if low_superheat_steam_temperature != -1:
                if val['flg'] == 'design':
                    result.low_superheat_steam_temperature_design = low_superheat_steam_temperature
                elif val['flg'] == 'check':
                    result.low_superheat_steam_temperature_check = low_superheat_steam_temperature
        print(result)


# 实现字段low_steam_enthalpy:特殊处理部分--蒸汽焓值,的计算27
class Low_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_superheat_steam_temperature_correct'] != '' and val['low_superheat_steam_temperature_correct'] is not None and val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None and val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None:
            low_steam_enthalpy = seuif97.pt2h((float(val['low_drum_pressure'])),((float(val['high_economizer_effluent_smoke_temperature']))-(float(val['low_superheat_steam_temperature_correct']))))
            if low_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_steam_enthalpy_design = low_steam_enthalpy
                elif val['flg'] == 'check':
                    result.low_steam_enthalpy_check = low_steam_enthalpy
        print(result)


# 实现字段low_evaporat_temperature:特殊处理部分--低压蒸发温度,的计算28
class Low_evaporat_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None:
            low_evaporat_temperature = seuif97.tsat_p(10.00*(float(val['low_drum_pressure'])))
            if low_evaporat_temperature != -1:
                if val['flg'] == 'design':
                    result.low_evaporat_temperature_design = low_evaporat_temperature
                elif val['flg'] == 'check':
                    result.low_evaporat_temperature_check = low_evaporat_temperature
        print(result)


# 实现字段low_evaporator_effluent_steam_enthalpy:特殊处理部分--低压蒸发器出口蒸汽焓,的计算29
class Low_evaporator_effluent_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None:
            low_evaporator_effluent_steam_enthalpy = seuif97.HG_P(10.00*(float(val['low_drum_pressure'])))
            if low_evaporator_effluent_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_evaporator_effluent_steam_enthalpy_design = low_evaporator_effluent_steam_enthalpy
                elif val['flg'] == 'check':
                    result.low_evaporator_effluent_steam_enthalpy_check = low_evaporator_effluent_steam_enthalpy
        print(result)


# 实现字段low_evaporator_effluent_water_temperature:低压进蒸发器热水温度,的计算30
class Low_evaporator_effluent_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None:
            low_evaporator_effluent_water_temperature = (seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature']))
            if low_evaporator_effluent_water_temperature != -1:
                if val['flg'] == 'design':
                    result.low_evaporator_effluent_water_temperature_design = low_evaporator_effluent_water_temperature
                elif val['flg'] == 'check':
                    result.low_evaporator_effluent_water_temperature_check = low_evaporator_effluent_water_temperature
        print(result)


# 实现字段low_evaporator_effluent_water_enthalpy:特殊处理部分--低压进蒸发器热水焓值,的计算31
class Low_evaporator_effluent_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None:
            low_evaporator_effluent_water_enthalpy = seuif97.pt2h((float(val['low_drum_pressure'])),((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature']))))
            if low_evaporator_effluent_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_evaporator_effluent_water_enthalpy_design = low_evaporator_effluent_water_enthalpy
                elif val['flg'] == 'check':
                    result.low_evaporator_effluent_water_enthalpy_check = low_evaporator_effluent_water_enthalpy
        print(result)


# 实现字段low_evaporator_effluent_smoke_temperature:低压出蒸发器排烟温度,的计算32
class Low_evaporator_effluent_smoke_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None and val['low_node_temperature'] != '' and val['low_node_temperature'] is not None:
            low_evaporator_effluent_smoke_temperature = ((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))+(float(val['low_node_temperature']))
            if low_evaporator_effluent_smoke_temperature != -1:
                if val['flg'] == 'design':
                    result.low_evaporator_effluent_smoke_temperature_design = low_evaporator_effluent_smoke_temperature
                elif val['flg'] == 'check':
                    result.low_evaporator_effluent_smoke_temperature_check = low_evaporator_effluent_smoke_temperature
        print(result)


# 实现字段low_evaporator_effluent_smoke_enthalpy:特殊处理部分--低压出蒸发器排烟焓值,的计算33
class Low_evaporator_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None and val['low_node_temperature'] != '' and val['low_node_temperature'] is not None:
            low_evaporator_effluent_smoke_enthalpy = seuif97.h_kqccpp((((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))+(float(val['low_node_temperature']))))
            if low_evaporator_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_evaporator_effluent_smoke_enthalpy_design = low_evaporator_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.low_evaporator_effluent_smoke_enthalpy_check = low_evaporator_effluent_smoke_enthalpy
        print(result)


# 实现字段low_gas_production:低压产汽量,的计算34
class Low_gas_production(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['low_superheat_steam_temperature_correct'] != '' and val['low_superheat_steam_temperature_correct'] is not None and val['high_boiler_efficiency'] != '' and val['high_boiler_efficiency'] is not None and val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None and val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None and val['low_node_temperature'] != '' and val['low_node_temperature'] is not None:
            low_gas_production = ((((float(val['engine_exhuast_gas_flux']))*1000/1.34))*((seuif97.h_kqccpp(((float(val['high_economizer_effluent_smoke_temperature']))-15)))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))+(float(val['low_node_temperature']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['low_drum_pressure'])),((float(val['high_economizer_effluent_smoke_temperature']))-(float(val['low_superheat_steam_temperature_correct'])))))-(seuif97.pt2h((float(val['low_drum_pressure'])),((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature']))))))/1000)
            if low_gas_production != -1:
                if val['flg'] == 'design':
                    result.low_gas_production_design = low_gas_production
                elif val['flg'] == 'check':
                    result.low_gas_production_check = low_gas_production
        print(result)


# 实现字段low_superheater_effluent_smoke_enthalpy:低压过热器出口烟焓,的计算35
class Low_superheater_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['low_superheat_steam_temperature_correct'] != '' and val['low_superheat_steam_temperature_correct'] is not None and val['high_boiler_efficiency'] != '' and val['high_boiler_efficiency'] is not None and val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None and val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None and val['low_node_temperature'] != '' and val['low_node_temperature'] is not None:
            low_superheater_effluent_smoke_enthalpy = (seuif97.h_kqccpp(((float(val['high_economizer_effluent_smoke_temperature']))-15)))-(((((float(val['engine_exhuast_gas_flux']))*1000/1.34))*((seuif97.h_kqccpp(((float(val['high_economizer_effluent_smoke_temperature']))-15)))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))+(float(val['low_node_temperature']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['low_drum_pressure'])),((float(val['high_economizer_effluent_smoke_temperature']))-(float(val['low_superheat_steam_temperature_correct'])))))-(seuif97.pt2h((float(val['low_drum_pressure'])),((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature']))))))/1000))*1000*((seuif97.pt2h((float(val['low_drum_pressure'])),((float(val['high_economizer_effluent_smoke_temperature']))-(float(val['low_superheat_steam_temperature_correct'])))))-(seuif97.HG_P(10.00*(float(val['low_drum_pressure'])))))/(float(val['high_boiler_efficiency']))/(((float(val['engine_exhuast_gas_flux']))*1000/1.34))
            if low_superheater_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_superheater_effluent_smoke_enthalpy_design = low_superheater_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.low_superheater_effluent_smoke_enthalpy_check = low_superheater_effluent_smoke_enthalpy
        print(result)


# 实现字段low_superheater_effluent_smoke_enthalpy_verify:特殊处理部分--低压过热器出口烟焓校核,的计算36
class Low_superheater_effluent_smoke_enthalpy_verify(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_superheater_effluent_smoke_temperature'] != '' and val['low_superheater_effluent_smoke_temperature'] is not None:
            low_superheater_effluent_smoke_enthalpy_verify = seuif97.h_kqccpp((float(val['low_superheater_effluent_smoke_temperature'])))
            if low_superheater_effluent_smoke_enthalpy_verify != -1:
                if val['flg'] == 'design':
                    result.low_superheater_effluent_smoke_enthalpy_verify_design = low_superheater_effluent_smoke_enthalpy_verify
                elif val['flg'] == 'check':
                    result.low_superheater_effluent_smoke_enthalpy_verify_check = low_superheater_effluent_smoke_enthalpy_verify
        print(result)


# 实现字段low_economizer_pressure:低压省煤器压力,的计算37
class Low_economizer_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None:
            low_economizer_pressure = (float(val['low_drum_pressure']))
            if low_economizer_pressure != -1:
                if val['flg'] == 'design':
                    result.low_economizer_pressure_design = low_economizer_pressure
                elif val['flg'] == 'check':
                    result.low_economizer_pressure_check = low_economizer_pressure
        print(result)


# 实现字段low_economizer_effluent_water_temperature:低压进省煤器热水温度,的计算38
class Low_economizer_effluent_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None:
            low_economizer_effluent_water_temperature = ((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))
            if low_economizer_effluent_water_temperature != -1:
                if val['flg'] == 'design':
                    result.low_economizer_effluent_water_temperature_design = low_economizer_effluent_water_temperature
                elif val['flg'] == 'check':
                    result.low_economizer_effluent_water_temperature_check = low_economizer_effluent_water_temperature
        print(result)


# 实现字段low_economizer_effluent_water_enthalpy:特殊处理部分--低压进省煤器热水焓值,的计算39
class Low_economizer_effluent_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None:
            low_economizer_effluent_water_enthalpy = seuif97.pt2h(((float(val['low_drum_pressure']))),(((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))))
            if low_economizer_effluent_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_economizer_effluent_water_enthalpy_design = low_economizer_effluent_water_enthalpy
                elif val['flg'] == 'check':
                    result.low_economizer_effluent_water_enthalpy_check = low_economizer_effluent_water_enthalpy
        print(result)


# 实现字段low_feedwater_enthalpy:特殊处理部分--给水焓值,的计算40
class Low_feedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_feedwater_temperature'] != '' and val['low_feedwater_temperature'] is not None:
            low_feedwater_enthalpy = seuif97.pt2h(((float(val['low_drum_pressure']))),(float(val['low_feedwater_temperature'])))
            if low_feedwater_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_feedwater_enthalpy_design = low_feedwater_enthalpy
                elif val['flg'] == 'check':
                    result.low_feedwater_enthalpy_check = low_feedwater_enthalpy
        print(result)


# 实现字段low_economizer_effluent_smoke_enthalpy:低压省煤器排烟焓值,的计算41
class Low_economizer_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_blowdown_rate'] != '' and val['high_blowdown_rate'] is not None and val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['low_superheat_steam_temperature_correct'] != '' and val['low_superheat_steam_temperature_correct'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['high_boiler_efficiency'] != '' and val['high_boiler_efficiency'] is not None and val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_terminal_temperature_difference'] != '' and val['high_terminal_temperature_difference'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None and val['high_proximity_temperature_difference'] != '' and val['high_proximity_temperature_difference'] is not None and val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None and val['high_blowdown_rate'] != '' and val['high_blowdown_rate'] is not None and val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None and val['low_node_temperature'] != '' and val['low_node_temperature'] is not None and val['low_feedwater_temperature'] != '' and val['low_feedwater_temperature'] is not None:
            low_economizer_effluent_smoke_enthalpy = (seuif97.h_kqccpp((((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))+(float(val['low_node_temperature'])))))-(((((float(val['engine_exhuast_gas_flux']))*1000/1.34)*((seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['high_steam_pressure'])),(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference'])))))-(seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))))))/1000)*(1+(float(val['high_blowdown_rate']))))+(((((float(val['engine_exhuast_gas_flux']))*1000/1.34))*((seuif97.h_kqccpp(((float(val['high_economizer_effluent_smoke_temperature']))-15)))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))+(float(val['low_node_temperature']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['low_drum_pressure'])),((float(val['high_economizer_effluent_smoke_temperature']))-(float(val['low_superheat_steam_temperature_correct'])))))-(seuif97.pt2h((float(val['low_drum_pressure'])),((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature']))))))/1000))*(1+float(val['high_blowdown_rate'])))*1000*((seuif97.pt2h(((float(val['low_drum_pressure']))),(((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature']))))))-(seuif97.pt2h(((float(val['low_drum_pressure']))),(float(val['low_feedwater_temperature'])))))/(((float(val['engine_exhuast_gas_flux']))*1000/1.34))/(float(val['high_boiler_efficiency']))
            if low_economizer_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.low_economizer_effluent_smoke_enthalpy_design = low_economizer_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.low_economizer_effluent_smoke_enthalpy_check = low_economizer_effluent_smoke_enthalpy
        print(result)


# 实现字段low_economizer_effluent_smoke_enthalpy_verify:特殊处理部分--低压省煤器烟焓校核,的计算42
class Low_economizer_effluent_smoke_enthalpy_verify(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['low_economizer_effluent_smoke_temperature'] != '' and val['low_economizer_effluent_smoke_temperature'] is not None:
            low_economizer_effluent_smoke_enthalpy_verify = seuif97.h_kqccpp((float(val['low_economizer_effluent_smoke_temperature'])))
            if low_economizer_effluent_smoke_enthalpy_verify != -1:
                if val['flg'] == 'design':
                    result.low_economizer_effluent_smoke_enthalpy_verify_design = low_economizer_effluent_smoke_enthalpy_verify
                elif val['flg'] == 'check':
                    result.low_economizer_effluent_smoke_enthalpy_verify_check = low_economizer_effluent_smoke_enthalpy_verify
        print(result)


# 实现字段low_feedwater_flux:给水流量,的计算43
class Low_feedwater_flux(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['high_blowdown_rate'] != '' and val['high_blowdown_rate'] is not None and val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['low_superheat_steam_temperature_correct'] != '' and val['low_superheat_steam_temperature_correct'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['high_boiler_efficiency'] != '' and val['high_boiler_efficiency'] is not None and val['high_steam_pressure'] != '' and val['high_steam_pressure'] is not None and val['high_terminal_temperature_difference'] != '' and val['high_terminal_temperature_difference'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['high_node_temperature'] != '' and val['high_node_temperature'] is not None and val['high_proximity_temperature_difference'] != '' and val['high_proximity_temperature_difference'] is not None and val['high_economizer_effluent_smoke_temperature'] != '' and val['high_economizer_effluent_smoke_temperature'] is not None and val['high_blowdown_rate'] != '' and val['high_blowdown_rate'] is not None and val['low_drum_pressure'] != '' and val['low_drum_pressure'] is not None and val['low_proximity_temperature'] != '' and val['low_proximity_temperature'] is not None and val['low_node_temperature'] != '' and val['low_node_temperature'] is not None:
            low_feedwater_flux = ((((float(val['engine_exhuast_gas_flux']))*1000/1.34)*((seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature'])))+(float(val['high_proximity_temperature_difference']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['high_steam_pressure'])),(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['high_terminal_temperature_difference'])))))-(seuif97.pt2h(((float(val['high_steam_pressure']))*1.05),((seuif97.tsat_p(10.00*((float(val['high_steam_pressure']))*1.05)))-(float(val['high_node_temperature']))))))/1000)*(1+(float(val['high_blowdown_rate']))))+(((((float(val['engine_exhuast_gas_flux']))*1000/1.34))*((seuif97.h_kqccpp(((float(val['high_economizer_effluent_smoke_temperature']))-15)))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature'])))+(float(val['low_node_temperature']))))))*(float(val['high_boiler_efficiency']))/((seuif97.pt2h((float(val['low_drum_pressure'])),((float(val['high_economizer_effluent_smoke_temperature']))-(float(val['low_superheat_steam_temperature_correct'])))))-(seuif97.pt2h((float(val['low_drum_pressure'])),((seuif97.tsat_p(10.00*(float(val['low_drum_pressure']))))-(float(val['low_proximity_temperature']))))))/1000))*(1+float(val['high_blowdown_rate']))
            if low_feedwater_flux != -1:
                if val['flg'] == 'design':
                    result.low_feedwater_flux_design = low_feedwater_flux
                elif val['flg'] == 'check':
                    result.low_feedwater_flux_check = low_feedwater_flux
        print(result)


# 实现字段sp_engine_exhuast_gas_flux:燃机排烟流量,的计算44
class Sp_engine_exhuast_gas_flux(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None:
            sp_engine_exhuast_gas_flux = (float(val['engine_exhuast_gas_flux']))*1000/1.34
            if sp_engine_exhuast_gas_flux != -1:
                if val['flg'] == 'design':
                    result.sp_engine_exhuast_gas_flux_design = sp_engine_exhuast_gas_flux
                elif val['flg'] == 'check':
                    result.sp_engine_exhuast_gas_flux_check = sp_engine_exhuast_gas_flux
        print(result)


# 实现字段sp_engine_exhuast_gas_temperature:燃机排烟温度,的计算45
class Sp_engine_exhuast_gas_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None:
            sp_engine_exhuast_gas_temperature = (round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2))
            if sp_engine_exhuast_gas_temperature != -1:
                if val['flg'] == 'design':
                    result.sp_engine_exhuast_gas_temperature_design = sp_engine_exhuast_gas_temperature
                elif val['flg'] == 'check':
                    result.sp_engine_exhuast_gas_temperature_check = sp_engine_exhuast_gas_temperature
        print(result)


# 实现字段sp_exhuast_gas_energy:特殊处理部分--燃机排烟能量,的计算46
class Sp_exhuast_gas_energy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None:
            sp_exhuast_gas_energy = seuif97.h_kqccpp(((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2))))
            if sp_exhuast_gas_energy != -1:
                if val['flg'] == 'design':
                    result.sp_exhuast_gas_energy_design = sp_exhuast_gas_energy
                elif val['flg'] == 'check':
                    result.sp_exhuast_gas_energy_check = sp_exhuast_gas_energy
        print(result)


# 实现字段sp_low_drum_pressure:低压汽包压力,的计算47
class Sp_low_drum_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_drum_pressure = (float(val['sp_steam_pressure']))
            if sp_low_drum_pressure != -1:
                if val['flg'] == 'design':
                    result.sp_low_drum_pressure_design = sp_low_drum_pressure
                elif val['flg'] == 'check':
                    result.sp_low_drum_pressure_check = sp_low_drum_pressure
        print(result)


# 实现字段sp_low_effluent_smoke_temperature:低压进烟温度,的计算48
class Sp_low_effluent_smoke_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['sp_terminal_temperature_difference'] != '' and val['sp_terminal_temperature_difference'] is not None:
            sp_low_effluent_smoke_temperature = ((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['sp_terminal_temperature_difference']))
            if sp_low_effluent_smoke_temperature != -1:
                if val['flg'] == 'design':
                    result.sp_low_effluent_smoke_temperature_design = sp_low_effluent_smoke_temperature
                elif val['flg'] == 'check':
                    result.sp_low_effluent_smoke_temperature_check = sp_low_effluent_smoke_temperature
        print(result)


# 实现字段sp_low_effluent_smoke_enthalpy:特殊处理部分--低压进烟焓,的计算49
class Sp_low_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['sp_terminal_temperature_difference'] != '' and val['sp_terminal_temperature_difference'] is not None:
            sp_low_effluent_smoke_enthalpy = seuif97.h_kqccpp((((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['sp_terminal_temperature_difference']))))
            if sp_low_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_effluent_smoke_enthalpy_design = sp_low_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_effluent_smoke_enthalpy_check = sp_low_effluent_smoke_enthalpy
        print(result)


# 实现字段sp_low_superheat_steam_temperature:低压过热蒸汽温度,的计算50
class Sp_low_superheat_steam_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_steam_temperature'] != '' and val['sp_steam_temperature'] is not None:
            sp_low_superheat_steam_temperature = (float(val['sp_steam_temperature']))
            if sp_low_superheat_steam_temperature != -1:
                if val['flg'] == 'design':
                    result.sp_low_superheat_steam_temperature_design = sp_low_superheat_steam_temperature
                elif val['flg'] == 'check':
                    result.sp_low_superheat_steam_temperature_check = sp_low_superheat_steam_temperature
        print(result)


# 实现字段sp_low_steam_enthalpy:特殊处理部分--蒸汽焓值,的计算51
class Sp_low_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None and val['sp_steam_temperature'] != '' and val['sp_steam_temperature'] is not None:
            sp_low_steam_enthalpy = seuif97.pt2h(((float(val['sp_steam_pressure']))),((float(val['sp_steam_temperature']))))
            if sp_low_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_steam_enthalpy_design = sp_low_steam_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_steam_enthalpy_check = sp_low_steam_enthalpy
        print(result)


# 实现字段sp_low_evaporating_temperature:特殊处理部分--蒸发温度,的计算52
class Sp_low_evaporating_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_evaporating_temperature = seuif97.tsat_p(10.00*((float(val['sp_steam_pressure']))))
            if sp_low_evaporating_temperature != -1:
                if val['flg'] == 'design':
                    result.sp_low_evaporating_temperature_design = sp_low_evaporating_temperature
                elif val['flg'] == 'check':
                    result.sp_low_evaporating_temperature_check = sp_low_evaporating_temperature
        print(result)


# 实现字段sp_low_evaporator_effluent_steam_enthalpy:特殊处理部分--低压蒸发器出口蒸汽焓,的计算53
class Sp_low_evaporator_effluent_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_evaporator_effluent_steam_enthalpy = seuif97.HG_P(10.00*((float(val['sp_steam_pressure']))))
            if sp_low_evaporator_effluent_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_evaporator_effluent_steam_enthalpy_design = sp_low_evaporator_effluent_steam_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_evaporator_effluent_steam_enthalpy_check = sp_low_evaporator_effluent_steam_enthalpy
        print(result)


# 实现字段sp_low_evaporator_effluent_water_temperature:低压进蒸发器热水温度,的计算54
class Sp_low_evaporator_effluent_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_evaporator_effluent_water_temperature = (seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature']))
            if sp_low_evaporator_effluent_water_temperature != -1:
                if val['flg'] == 'design':
                    result.sp_low_evaporator_effluent_water_temperature_design = sp_low_evaporator_effluent_water_temperature
                elif val['flg'] == 'check':
                    result.sp_low_evaporator_effluent_water_temperature_check = sp_low_evaporator_effluent_water_temperature
        print(result)


# 实现字段sp_low_evaporator_effluent_water_enthalpy:特殊处理部分--低压进蒸发器热水焓值,的计算55
class Sp_low_evaporator_effluent_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_evaporator_effluent_water_enthalpy = seuif97.pt2h((float(val['sp_steam_pressure'])),((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature']))))
            if sp_low_evaporator_effluent_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_evaporator_effluent_water_enthalpy_design = sp_low_evaporator_effluent_water_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_evaporator_effluent_water_enthalpy_check = sp_low_evaporator_effluent_water_enthalpy
        print(result)


# 实现字段sp_low_evaporator_effluent_smoke_temperature:低压出蒸发器排烟温度,的计算56
class Sp_low_evaporator_effluent_smoke_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_low_node_temperature'] != '' and val['sp_low_node_temperature'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_evaporator_effluent_smoke_temperature = ((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))+(float(val['sp_low_node_temperature']))
            if sp_low_evaporator_effluent_smoke_temperature != -1:
                if val['flg'] == 'design':
                    result.sp_low_evaporator_effluent_smoke_temperature_design = sp_low_evaporator_effluent_smoke_temperature
                elif val['flg'] == 'check':
                    result.sp_low_evaporator_effluent_smoke_temperature_check = sp_low_evaporator_effluent_smoke_temperature
        print(result)


# 实现字段sp_low_evaporator_effluent_smoke_enthalpy:特殊处理部分--低压出蒸发器排烟焓值,的计算57
class Sp_low_evaporator_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_low_node_temperature'] != '' and val['sp_low_node_temperature'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_evaporator_effluent_smoke_enthalpy = seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))+(float(val['sp_low_node_temperature']))))
            if sp_low_evaporator_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_evaporator_effluent_smoke_enthalpy_design = sp_low_evaporator_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_evaporator_effluent_smoke_enthalpy_check = sp_low_evaporator_effluent_smoke_enthalpy
            # elif val['flg'] == 'design':
            #     result.sp_low_evaporator_effluent_smoke_enthalpy_design = None
            # elif val['flg'] == 'check':
            #     result.sp_low_evaporator_effluent_smoke_enthalpy_check = None
        print(result)


# 实现字段sp_low_gas_production:低压产汽量,的计算58
class Sp_low_gas_production(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_low_node_temperature'] != '' and val['sp_low_node_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['sp_boiler_efficiency'] != '' and val['sp_boiler_efficiency'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None and val['sp_steam_temperature'] != '' and val['sp_steam_temperature'] is not None and val['sp_terminal_temperature_difference'] != '' and val['sp_terminal_temperature_difference'] is not None:
            sp_low_gas_production = ((((float(val['engine_exhuast_gas_flux']))*1000/1.34))*((seuif97.h_kqccpp((((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['sp_terminal_temperature_difference'])))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))+(float(val['sp_low_node_temperature']))))))*(float(val['sp_boiler_efficiency']))/((seuif97.pt2h(((float(val['sp_steam_pressure']))),((float(val['sp_steam_temperature'])))))-(seuif97.pt2h((float(val['sp_steam_pressure'])),((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature']))))))/1000)
            if sp_low_gas_production != -1:
                if val['flg'] == 'design':
                    result.sp_low_gas_production_design = sp_low_gas_production
                elif val['flg'] == 'check':
                    result.sp_low_gas_production_check = sp_low_gas_production
        print(result)


# 实现字段sp_low_superheater_effluent_smoke_enthalpy:低压过热器出口烟焓,的计算59
class Sp_low_superheater_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_low_node_temperature'] != '' and val['sp_low_node_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['sp_boiler_efficiency'] != '' and val['sp_boiler_efficiency'] != '0'  and val['sp_boiler_efficiency'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None and val['sp_steam_temperature'] != '' and val['sp_steam_temperature'] is not None and val['sp_terminal_temperature_difference'] != '' and val['sp_terminal_temperature_difference'] is not None:
            sp_low_superheater_effluent_smoke_enthalpy = (seuif97.h_kqccpp((((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['sp_terminal_temperature_difference'])))))-(((((float(val['engine_exhuast_gas_flux']))*1000/1.34))*((seuif97.h_kqccpp((((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['sp_terminal_temperature_difference'])))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))+(float(val['sp_low_node_temperature']))))))*(float(val['sp_boiler_efficiency']))/((seuif97.pt2h(((float(val['sp_steam_pressure']))),((float(val['sp_steam_temperature'])))))-(seuif97.pt2h((float(val['sp_steam_pressure'])),((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature']))))))/1000))*1000*((seuif97.pt2h(((float(val['sp_steam_pressure']))),((float(val['sp_steam_temperature'])))))-(seuif97.HG_P(10.00*((float(val['sp_steam_pressure']))))))/(float(val['sp_boiler_efficiency']))/(((float(val['engine_exhuast_gas_flux']))*1000/1.34))
            if sp_low_superheater_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_superheater_effluent_smoke_enthalpy_design = sp_low_superheater_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_superheater_effluent_smoke_enthalpy_check = sp_low_superheater_effluent_smoke_enthalpy
        print(result)


# 实现字段sp_low_superheater_effluent_smoke_enthalpy_verify:特殊处理部分--低压过热器出口烟焓校核,的计算60
class Sp_low_superheater_effluent_smoke_enthalpy_verify(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_superheater_effluent_smoke_temperature'] != '' and val['sp_low_superheater_effluent_smoke_temperature'] is not None:
            sp_low_superheater_effluent_smoke_enthalpy_verify = seuif97.h_kqccpp((float(val['sp_low_superheater_effluent_smoke_temperature'])))
            if sp_low_superheater_effluent_smoke_enthalpy_verify != -1:
                if val['flg'] == 'design':
                    result.sp_low_superheater_effluent_smoke_enthalpy_verify_design = sp_low_superheater_effluent_smoke_enthalpy_verify
                elif val['flg'] == 'check':
                    result.sp_low_superheater_effluent_smoke_enthalpy_verify_check = sp_low_superheater_effluent_smoke_enthalpy_verify
        print(result)


# 实现字段sp_low_economizer_pressure:低压省煤器压力,的计算61
class Sp_low_economizer_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_economizer_pressure = ((float(val['sp_steam_pressure'])))
            if sp_low_economizer_pressure != -1:
                if val['flg'] == 'design':
                    result.sp_low_economizer_pressure_design = sp_low_economizer_pressure
                elif val['flg'] == 'check':
                    result.sp_low_economizer_pressure_check = sp_low_economizer_pressure
        print(result)


# 实现字段sp_low_economizer_effluent_water_temperature:低压进省煤器热水温度,的计算62
class Sp_low_economizer_effluent_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_economizer_effluent_water_temperature = ((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))
            if sp_low_economizer_effluent_water_temperature != -1:
                if val['flg'] == 'design':
                    result.sp_low_economizer_effluent_water_temperature_design = sp_low_economizer_effluent_water_temperature
                elif val['flg'] == 'check':
                    result.sp_low_economizer_effluent_water_temperature_check = sp_low_economizer_effluent_water_temperature
        print(result)


# 实现字段sp_low_economizer_effluent_water_enthalpy:特殊处理部分--低压进省煤器热水焓值,的计算63
class Sp_low_economizer_effluent_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_economizer_effluent_water_enthalpy = seuif97.pt2h((((float(val['sp_steam_pressure'])))),(((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))))
            if sp_low_economizer_effluent_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_economizer_effluent_water_enthalpy_design = sp_low_economizer_effluent_water_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_economizer_effluent_water_enthalpy_check = sp_low_economizer_effluent_water_enthalpy
        print(result)


# 实现字段sp_low_feedwater_enthalpy:特殊处理部分--给水焓值,的计算64
class Sp_low_feedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_feedwater_temperature'] != '' and val['sp_low_feedwater_temperature'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None:
            sp_low_feedwater_enthalpy = seuif97.pt2h((((float(val['sp_steam_pressure'])))),(float(val['sp_low_feedwater_temperature'])))
            if sp_low_feedwater_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_feedwater_enthalpy_design = sp_low_feedwater_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_feedwater_enthalpy_check = sp_low_feedwater_enthalpy
        print(result)


# 实现字段sp_low_economizer_effluent_smoke_enthalpy:低压省煤器排烟焓值,的计算65
class Sp_low_economizer_effluent_smoke_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_h_blowdown_rate'] != '' and val['sp_h_blowdown_rate'] is not None and val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_low_node_temperature'] != '' and val['sp_low_node_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['sp_low_feedwater_temperature'] != '' and val['sp_low_feedwater_temperature'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['sp_boiler_efficiency'] != '' and val['sp_boiler_efficiency'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None and val['sp_steam_temperature'] != '' and val['sp_steam_temperature'] is not None and val['sp_terminal_temperature_difference'] != '' and val['sp_terminal_temperature_difference'] is not None and float(val['sp_boiler_efficiency']) != 0.0:
            sp_low_economizer_effluent_smoke_enthalpy = (seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))+(float(val['sp_low_node_temperature'])))))-((((((float(val['engine_exhuast_gas_flux']))*1000/1.34))*((seuif97.h_kqccpp((((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['sp_terminal_temperature_difference'])))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))+(float(val['sp_low_node_temperature']))))))*(float(val['sp_boiler_efficiency']))/((seuif97.pt2h(((float(val['sp_steam_pressure']))),((float(val['sp_steam_temperature'])))))-(seuif97.pt2h((float(val['sp_steam_pressure'])),((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature']))))))/1000))*(1+float(val['sp_h_blowdown_rate'])))*1000*((seuif97.pt2h((((float(val['sp_steam_pressure'])))),(((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature']))))))-(seuif97.pt2h((((float(val['sp_steam_pressure'])))),(float(val['sp_low_feedwater_temperature'])))))/(((float(val['engine_exhuast_gas_flux']))*1000/1.34))/(float(val['sp_boiler_efficiency']))
            if sp_low_economizer_effluent_smoke_enthalpy != -1:
                if val['flg'] == 'design':
                    result.sp_low_economizer_effluent_smoke_enthalpy_design = sp_low_economizer_effluent_smoke_enthalpy
                elif val['flg'] == 'check':
                    result.sp_low_economizer_effluent_smoke_enthalpy_check = sp_low_economizer_effluent_smoke_enthalpy
        print(result)


# 实现字段sp_low_economizer_effluent_smoke_enthalpy_verify:特殊处理部分--低压省煤器烟焓校核,的计算66
class Sp_low_economizer_effluent_smoke_enthalpy_verify(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_low_economizer_effluent_smoke_temperature'] != '' and val['sp_low_economizer_effluent_smoke_temperature'] is not None:
            sp_low_economizer_effluent_smoke_enthalpy_verify = seuif97.h_kqccpp((float(val['sp_low_economizer_effluent_smoke_temperature'])))
            if sp_low_economizer_effluent_smoke_enthalpy_verify != -1:
                if val['flg'] == 'design':
                    result.sp_low_economizer_effluent_smoke_enthalpy_verify_design = sp_low_economizer_effluent_smoke_enthalpy_verify
                elif val['flg'] == 'check':
                    result.sp_low_economizer_effluent_smoke_enthalpy_verify_check = sp_low_economizer_effluent_smoke_enthalpy_verify
        print(result)


# 实现字段sp_low_feedwater_flux:给水流量,的计算67
class Sp_low_feedwater_flux(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['sp_h_blowdown_rate'] != '' and val['sp_h_blowdown_rate'] is not None and val['engine_exhuast_gas_temperature'] != '' and val['engine_exhuast_gas_temperature'] is not None and val['sp_low_proximity_temperature'] != '' and val['sp_low_proximity_temperature'] is not None and val['sp_low_node_temperature'] != '' and val['sp_low_node_temperature'] is not None and val['engine_exhuast_gas_flux'] != '' and val['engine_exhuast_gas_flux'] is not None and val['boiler_afterburning_amount'] != '' and val['boiler_afterburning_amount'] is not None and val['low_calorific_gas'] != '' and val['low_calorific_gas'] is not None and val['sp_boiler_efficiency'] != '' and val['sp_boiler_efficiency'] is not None and val['sp_steam_pressure'] != '' and val['sp_steam_pressure'] is not None and val['sp_steam_temperature'] != '' and val['sp_steam_temperature'] is not None and val['sp_terminal_temperature_difference'] != '' and val['sp_terminal_temperature_difference'] is not None:
            sp_low_feedwater_flux = (((((float(val['engine_exhuast_gas_flux']))*1000/1.34))*((seuif97.h_kqccpp((((round((float(val['boiler_afterburning_amount']))*(float(val['low_calorific_gas']))/(float(val['engine_exhuast_gas_flux']))/1000/1.141+(float(val['engine_exhuast_gas_temperature'])), 2)))-(float(val['sp_terminal_temperature_difference'])))))-(seuif97.h_kqccpp((((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature'])))+(float(val['sp_low_node_temperature']))))))*(float(val['sp_boiler_efficiency']))/((seuif97.pt2h(((float(val['sp_steam_pressure']))),((float(val['sp_steam_temperature'])))))-(seuif97.pt2h((float(val['sp_steam_pressure'])),((seuif97.tsat_p(10.00*((float(val['sp_steam_pressure'])))))-(float(val['sp_low_proximity_temperature']))))))/1000))*(1+float(val['sp_h_blowdown_rate']))
            if sp_low_feedwater_flux != -1:
                if val['flg'] == 'design':
                    result.sp_low_feedwater_flux_design = sp_low_feedwater_flux
                elif val['flg'] == 'check':
                    result.sp_low_feedwater_flux_check = sp_low_feedwater_flux
        print(result)



class Ccpp_EXEC(ExecuteStrategy):
    def creatSubscriberall(self, val):
        calculationObserver = CalculationObserver()
        # 添加注册类
        calculationObserver.register(Engine_exhuast_gas_energy())
        calculationObserver.register(Boiler_afterburning_exhuast_energy())
        calculationObserver.register(Boiler_afterburning_exhuast_temperature())
        calculationObserver.register(High_engine_exhuast_gas_flux())
        calculationObserver.register(High_engine_exhuast_gas_temperature())
        calculationObserver.register(High_engine_exhuast_gas_energy())
        calculationObserver.register(High_steam_temperature())
        calculationObserver.register(High_steam_enthalpy())
        calculationObserver.register(High_drum_pressure())
        calculationObserver.register(High_evaporating_temperature())
        calculationObserver.register(High_evaporator_effluent_water_temperature())
        calculationObserver.register(High_evaporator_effluent_water_enthalpy())
        calculationObserver.register(High_evaporator_effluent_smoke_temperature())
        calculationObserver.register(High_evaporator_effluent_smoke_enthalpy())
        calculationObserver.register(High_economizer_effluent_smoke_enthalpy())
        calculationObserver.register(High_economizer_effluent_water_temperature())
        calculationObserver.register(High_economizer_effluent_water_enthalpy())
        calculationObserver.register(High_gas_production())
        calculationObserver.register(High_feedwater_amount())
        calculationObserver.register(High_economizer_effluent_smoke_enthalpy_verify())
        calculationObserver.register(High_evaporator_effluent_steam_enthalpy())
        calculationObserver.register(High_superheater_effluent_smoke_enthalpy())
        calculationObserver.register(High_superheater_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Low_effluent_smoke_temperature())
        calculationObserver.register(Low_effluent_smoke_enthalpy())
        calculationObserver.register(Low_superheat_steam_temperature())
        calculationObserver.register(Low_steam_enthalpy())
        calculationObserver.register(Low_evaporat_temperature())
        calculationObserver.register(Low_evaporator_effluent_steam_enthalpy())
        calculationObserver.register(Low_evaporator_effluent_water_temperature())
        calculationObserver.register(Low_evaporator_effluent_water_enthalpy())
        calculationObserver.register(Low_evaporator_effluent_smoke_temperature())
        calculationObserver.register(Low_evaporator_effluent_smoke_enthalpy())
        calculationObserver.register(Low_gas_production())
        calculationObserver.register(Low_superheater_effluent_smoke_enthalpy())
        calculationObserver.register(Low_superheater_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Low_economizer_pressure())
        calculationObserver.register(Low_economizer_effluent_water_temperature())
        calculationObserver.register(Low_economizer_effluent_water_enthalpy())
        calculationObserver.register(Low_feedwater_enthalpy())
        calculationObserver.register(Low_economizer_effluent_smoke_enthalpy())
        calculationObserver.register(Low_economizer_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Low_feedwater_flux())
        calculationObserver.register(Sp_engine_exhuast_gas_flux())
        calculationObserver.register(Sp_engine_exhuast_gas_temperature())
        calculationObserver.register(Sp_exhuast_gas_energy())
        calculationObserver.register(Sp_low_drum_pressure())
        calculationObserver.register(Sp_low_effluent_smoke_temperature())
        calculationObserver.register(Sp_low_effluent_smoke_enthalpy())
        calculationObserver.register(Sp_low_superheat_steam_temperature())
        calculationObserver.register(Sp_low_steam_enthalpy())
        calculationObserver.register(Sp_low_evaporating_temperature())
        calculationObserver.register(Sp_low_evaporator_effluent_steam_enthalpy())
        calculationObserver.register(Sp_low_evaporator_effluent_water_temperature())
        calculationObserver.register(Sp_low_evaporator_effluent_water_enthalpy())
        calculationObserver.register(Sp_low_evaporator_effluent_smoke_temperature())
        calculationObserver.register(Sp_low_evaporator_effluent_smoke_enthalpy())
        calculationObserver.register(Sp_low_gas_production())
        calculationObserver.register(Sp_low_superheater_effluent_smoke_enthalpy())
        calculationObserver.register(Sp_low_superheater_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Sp_low_economizer_pressure())
        calculationObserver.register(Sp_low_economizer_effluent_water_temperature())
        calculationObserver.register(Sp_low_economizer_effluent_water_enthalpy())
        calculationObserver.register(Sp_low_feedwater_enthalpy())
        calculationObserver.register(Sp_low_economizer_effluent_smoke_enthalpy())
        calculationObserver.register(Sp_low_economizer_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Sp_low_feedwater_flux())
        calculationObserver.writeNewPost(val)

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        # 添加注册类
        calculationObserver.register(Engine_exhuast_gas_energy())
        calculationObserver.register(Boiler_afterburning_exhuast_energy())
        calculationObserver.register(Boiler_afterburning_exhuast_temperature())

        calculationObserver.register(Sp_engine_exhuast_gas_flux())
        calculationObserver.register(Sp_engine_exhuast_gas_temperature())
        calculationObserver.register(Sp_exhuast_gas_energy())
        calculationObserver.register(Sp_low_drum_pressure())
        calculationObserver.register(Sp_low_effluent_smoke_temperature())
        calculationObserver.register(Sp_low_effluent_smoke_enthalpy())
        calculationObserver.register(Sp_low_superheat_steam_temperature())
        calculationObserver.register(Sp_low_steam_enthalpy())
        calculationObserver.register(Sp_low_evaporating_temperature())
        calculationObserver.register(Sp_low_evaporator_effluent_steam_enthalpy())
        calculationObserver.register(Sp_low_evaporator_effluent_water_temperature())
        calculationObserver.register(Sp_low_evaporator_effluent_water_enthalpy())
        calculationObserver.register(Sp_low_evaporator_effluent_smoke_temperature())
        calculationObserver.register(Sp_low_evaporator_effluent_smoke_enthalpy())
        calculationObserver.register(Sp_low_gas_production())
        calculationObserver.register(Sp_low_superheater_effluent_smoke_enthalpy())
        calculationObserver.register(Sp_low_superheater_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Sp_low_economizer_pressure())
        calculationObserver.register(Sp_low_economizer_effluent_water_temperature())
        calculationObserver.register(Sp_low_economizer_effluent_water_enthalpy())
        calculationObserver.register(Sp_low_feedwater_enthalpy())
        calculationObserver.register(Sp_low_economizer_effluent_smoke_enthalpy())
        calculationObserver.register(Sp_low_economizer_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Sp_low_feedwater_flux())
        calculationObserver.writeNewPost(val)

    def creatSubscriberdouble(self, val):
        calculationObserver = CalculationObserver()
        # 添加注册类
        calculationObserver.register(Engine_exhuast_gas_energy())
        calculationObserver.register(Boiler_afterburning_exhuast_energy())
        calculationObserver.register(Boiler_afterburning_exhuast_temperature())
        calculationObserver.register(High_engine_exhuast_gas_flux())
        calculationObserver.register(High_engine_exhuast_gas_temperature())
        calculationObserver.register(High_engine_exhuast_gas_energy())
        calculationObserver.register(High_steam_temperature())
        calculationObserver.register(High_steam_enthalpy())
        calculationObserver.register(High_drum_pressure())
        calculationObserver.register(High_evaporating_temperature())
        calculationObserver.register(High_evaporator_effluent_water_temperature())
        calculationObserver.register(High_evaporator_effluent_water_enthalpy())
        calculationObserver.register(High_evaporator_effluent_smoke_temperature())
        calculationObserver.register(High_evaporator_effluent_smoke_enthalpy())
        calculationObserver.register(High_economizer_effluent_smoke_enthalpy())
        calculationObserver.register(High_economizer_effluent_water_temperature())
        calculationObserver.register(High_economizer_effluent_water_enthalpy())
        calculationObserver.register(High_gas_production())
        calculationObserver.register(High_feedwater_amount())
        calculationObserver.register(High_economizer_effluent_smoke_enthalpy_verify())
        calculationObserver.register(High_evaporator_effluent_steam_enthalpy())
        calculationObserver.register(High_superheater_effluent_smoke_enthalpy())
        calculationObserver.register(High_superheater_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Low_effluent_smoke_temperature())
        calculationObserver.register(Low_effluent_smoke_enthalpy())
        calculationObserver.register(Low_superheat_steam_temperature())
        calculationObserver.register(Low_steam_enthalpy())
        calculationObserver.register(Low_evaporat_temperature())
        calculationObserver.register(Low_evaporator_effluent_steam_enthalpy())
        calculationObserver.register(Low_evaporator_effluent_water_temperature())
        calculationObserver.register(Low_evaporator_effluent_water_enthalpy())
        calculationObserver.register(Low_evaporator_effluent_smoke_temperature())
        calculationObserver.register(Low_evaporator_effluent_smoke_enthalpy())
        calculationObserver.register(Low_gas_production())
        calculationObserver.register(Low_superheater_effluent_smoke_enthalpy())
        calculationObserver.register(Low_superheater_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Low_economizer_pressure())
        calculationObserver.register(Low_economizer_effluent_water_temperature())
        calculationObserver.register(Low_economizer_effluent_water_enthalpy())
        calculationObserver.register(Low_feedwater_enthalpy())
        calculationObserver.register(Low_economizer_effluent_smoke_enthalpy())
        calculationObserver.register(Low_economizer_effluent_smoke_enthalpy_verify())
        calculationObserver.register(Low_feedwater_flux())
        calculationObserver.writeNewPost(val)


    def specialCalculation(self, dbmodel, form):
        val = {
            'flg': 'design',
            'sp_boiler_efficiency': form.get('sp_boiler_efficiency_design'),
            'high_superheater_effluent_smoke_temperature': form.get('high_superheater_effluent_smoke_temperature_design'),
            'low_drum_pressure': form.get('low_drum_pressure_design'),
            'high_blowdown_rate': form.get('high_blowdown_rate_design'),
            'low_proximity_temperature': form.get('low_proximity_temperature_design'),
            'engine_exhuast_gas_flux': form.get('engine_exhuast_gas_flux_design'),
            'sp_low_economizer_effluent_smoke_temperature': form.get('sp_low_economizer_effluent_smoke_temperature_design'),
            'low_feedwater_temperature': form.get('low_feedwater_temperature_design'),
            'low_economizer_effluent_smoke_temperature': form.get('low_economizer_effluent_smoke_temperature_design'),
            'sp_steam_pressure': form.get('sp_steam_pressure_design'),
            'sp_terminal_temperature_difference': form.get('sp_terminal_temperature_difference_design'),
            'high_terminal_temperature_difference': form.get('high_terminal_temperature_difference_design'),
            'boiler_afterburning_amount': form.get('boiler_afterburning_amount_design'),
            'sp_low_superheater_effluent_smoke_temperature': form.get('sp_low_superheater_effluent_smoke_temperature_design'),
            'high_proximity_temperature_difference': form.get('high_proximity_temperature_difference_design'),
            'sp_steam_temperature': form.get('sp_steam_temperature_design'),
            'low_superheat_steam_temperature_correct': form.get('low_superheat_steam_temperature_correct_design'),
            'high_node_temperature': form.get('high_node_temperature_design'),
            'high_economizer_effluent_smoke_temperature': form.get('high_economizer_effluent_smoke_temperature_design'),
            'sp_low_proximity_temperature': form.get('sp_low_proximity_temperature_design'),
            'sp_low_node_temperature': form.get('sp_low_node_temperature_design'),
            'engine_exhuast_gas_temperature': form.get('engine_exhuast_gas_temperature_design'),
            'low_calorific_gas': form.get('low_calorific_gas_design'),
            'sp_low_feedwater_temperature': form.get('sp_low_feedwater_temperature_design'),
            'high_steam_pressure': form.get('high_steam_pressure_design'),
            'high_boiler_efficiency': form.get('high_boiler_efficiency_design'),
            'low_node_temperature': form.get('low_node_temperature_design'),
            'low_superheater_effluent_smoke_temperature': form.get('low_superheater_effluent_smoke_temperature_design'),
            'sp_h_blowdown_rate': form.get('sp_h_blowdown_rate_design'),
            'dbresult': dbmodel}
        val['low_calorific_gas'] = dbmodel.low_calorific_gas_design
        boiler_single_or_dula_pressure = form.get('boiler_single_or_dula_pressure_design')
        if boiler_single_or_dula_pressure == 'singlepot':
            val['sp_boiler_efficiency'] = float(val['sp_boiler_efficiency'])/100
            val['sp_h_blowdown_rate'] = float(val['sp_h_blowdown_rate'])/100
            self.creatSubscriber(val)
        elif boiler_single_or_dula_pressure == 'doublepot':
            val['high_blowdown_rate'] = float(val['high_blowdown_rate'])/100
            val['high_boiler_efficiency'] = float(val['high_boiler_efficiency'])/100
            self.creatSubscriberdouble(val)
        else:
            pass
        return val['dbresult']


class Ccpp_PlanList(ExecuteStrategy):
    def specialCalculation(self, dbmodel):
        val = {
            'flg': 'design',
            'sp_boiler_efficiency': dbmodel.sp_boiler_efficiency_design,
            'high_superheater_effluent_smoke_temperature': dbmodel.high_superheater_effluent_smoke_temperature_design,
            'low_drum_pressure': dbmodel.low_drum_pressure_design,
            'high_blowdown_rate': dbmodel.high_blowdown_rate_design,
            'low_proximity_temperature': dbmodel.low_proximity_temperature_design,
            'engine_exhuast_gas_flux': dbmodel.engine_exhuast_gas_flux_design,
            'sp_low_economizer_effluent_smoke_temperature': dbmodel.sp_low_economizer_effluent_smoke_temperature_design,
            'low_feedwater_temperature': dbmodel.low_feedwater_temperature_design,
            'low_economizer_effluent_smoke_temperature': dbmodel.low_economizer_effluent_smoke_temperature_design,
            'sp_steam_pressure': dbmodel.sp_steam_pressure_design,
            'sp_terminal_temperature_difference': dbmodel.sp_terminal_temperature_difference_design,
            'high_terminal_temperature_difference': dbmodel.high_terminal_temperature_difference_design,
            'boiler_afterburning_amount': dbmodel.boiler_afterburning_amount_design,
            'sp_low_superheater_effluent_smoke_temperature': dbmodel.sp_low_superheater_effluent_smoke_temperature_design,
            'high_proximity_temperature_difference': dbmodel.high_proximity_temperature_difference_design,
            'sp_steam_temperature': dbmodel.sp_steam_temperature_design,
            'low_superheat_steam_temperature_correct': dbmodel.low_superheat_steam_temperature_correct_design,
            'high_node_temperature': dbmodel.high_node_temperature_design,
            'high_economizer_effluent_smoke_temperature': dbmodel.high_economizer_effluent_smoke_temperature_design,
            'sp_low_proximity_temperature': dbmodel.sp_low_proximity_temperature_design,
            'sp_low_node_temperature': dbmodel.sp_low_node_temperature_design,
            'engine_exhuast_gas_temperature': dbmodel.engine_exhuast_gas_temperature_design,
            'low_calorific_gas': dbmodel.low_calorific_gas_design,
            'sp_low_feedwater_temperature': dbmodel.sp_low_feedwater_temperature_design,
            'high_steam_pressure': dbmodel.high_steam_pressure_design,
            'high_boiler_efficiency': dbmodel.high_boiler_efficiency_design,
            'low_node_temperature': dbmodel.low_node_temperature_design,
            'low_superheater_effluent_smoke_temperature': dbmodel.low_superheater_effluent_smoke_temperature_design,
            'sp_h_blowdown_rate': dbmodel.sp_h_blowdown_rate_design,
            'dbresult': dbmodel}
        boiler_single_or_dula_pressure = dbmodel.boiler_single_or_dula_pressure_design
        if boiler_single_or_dula_pressure == 'singlepot':
            val['sp_boiler_efficiency'] = float(val['sp_boiler_efficiency'])/100
            val['sp_h_blowdown_rate'] = float(val['sp_h_blowdown_rate'])/100
            Ccpp_EXEC().creatSubscriber(val)
        elif boiler_single_or_dula_pressure == 'doublepot':
            val['high_blowdown_rate'] = float(val['high_blowdown_rate'])/100
            val['high_boiler_efficiency'] = float(val['high_boiler_efficiency'])/100
            Ccpp_EXEC().creatSubscriberdouble(val)
        else:
            pass
        return val['dbresult']
