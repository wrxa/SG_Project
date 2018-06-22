# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97
from base import CalculationObserver, ExecuteStrategy


# 实现字段smoke_heat_consumption_rate:抽凝工况热耗率,的计算1
class Smoke_heat_consumption_rate(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_steam_enthalpy'] != '' and val['t_steam_enthalpy'] is not None and val['t_throttle_flow'] != '' and val['t_throttle_flow'] is not None and val['t_total_power'] != '' and val['t_total_power'] is not None and val['t_water_enthalpy'] != '' and val['t_water_enthalpy'] is not None:
            smoke_heat_consumption_rate = (float(val['t_throttle_flow']))*((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))/(float(val['t_total_power']))*1000
            if smoke_heat_consumption_rate != -1:
                if val['flg'] == 'design':
                    result.smoke_heat_consumption_rate = smoke_heat_consumption_rate
                elif val['flg'] == 'check':
                    result.smoke_heat_consumption_rate = smoke_heat_consumption_rate
        print(result)


# 实现字段heat_consumption_rate:纯凝工况热耗率,的计算2
class Heat_consumption_rate(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_steam_enthalpy'] != '' and val['t_steam_enthalpy'] is not None and val['t_throttle_flow'] != '' and val['t_throttle_flow'] is not None and val['t_total_power0'] != '' and val['t_total_power0'] is not None and val['t_water_enthalpy'] != '' and val['t_water_enthalpy'] is not None:
            heat_consumption_rate = (float(val['t_throttle_flow']))*((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))/(float(val['t_total_power0']))*1000
            if heat_consumption_rate != -1:
                if val['flg'] == 'design':
                    result.heat_consumption_rate = heat_consumption_rate
                elif val['flg'] == 'check':
                    result.heat_consumption_rate = heat_consumption_rate
        print(result)


# 实现字段smoke_steam_consumption_rate:抽凝工况汽耗率,的计算3
class Smoke_steam_consumption_rate(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_steam_enthalpy'] != '' and val['t_steam_enthalpy'] is not None and val['t_throttle_flow'] != '' and val['t_throttle_flow'] is not None and val['t_total_power'] != '' and val['t_total_power'] is not None and val['t_water_enthalpy'] != '' and val['t_water_enthalpy'] is not None:
            smoke_steam_consumption_rate = ((float(val['t_throttle_flow']))*((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))/(float(val['t_total_power']))*1000)/((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))
            if smoke_steam_consumption_rate != -1:
                if val['flg'] == 'design':
                    result.smoke_steam_consumption_rate = smoke_steam_consumption_rate
                elif val['flg'] == 'check':
                    result.smoke_steam_consumption_rate = smoke_steam_consumption_rate
        print(result)


# 实现字段steam_consumption_rate:纯凝工况汽耗率,的计算4
class Steam_consumption_rate(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_steam_enthalpy'] != '' and val['t_steam_enthalpy'] is not None and val['t_throttle_flow'] != '' and val['t_throttle_flow'] is not None and val['t_total_power0'] != '' and val['t_total_power0'] is not None and val['t_water_enthalpy'] != '' and val['t_water_enthalpy'] is not None:
            steam_consumption_rate = ((float(val['t_throttle_flow']))*((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))/(float(val['t_total_power0']))*1000)/((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))
            if steam_consumption_rate != -1:
                if val['flg'] == 'design':
                    result.steam_consumption_rate = steam_consumption_rate
                elif val['flg'] == 'check':
                    result.steam_consumption_rate = steam_consumption_rate
        print(result)


# 实现字段annual_heat_supply:年供热量,的计算5
class Annual_heat_supply(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['condensate_backwater_pressure'] != '' and val['condensate_backwater_pressure'] is not None and val['t_point_enthalpy'] != '' and val['t_point_enthalpy'] is not None and val['t_point_flow'] != '' and val['t_point_flow'] is not None and val['annual_heat_hours'] != '' and val['annual_heat_hours'] is not None:
            annual_heat_supply = (float(val['t_point_flow']))*((float(val['t_point_enthalpy']))-(seuif97.HL_P(10.00*(float(val['condensate_backwater_pressure'])))))*(float(val['annual_heat_hours']))/1000
            if annual_heat_supply != -1:
                if val['flg'] == 'design':
                    result.annual_heat_supply = annual_heat_supply
                elif val['flg'] == 'check':
                    result.annual_heat_supply = annual_heat_supply
        print(result)


# 实现字段annual_power_generation:年发电量,的计算6
class Annual_power_generation(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_total_power'] != '' and val['t_total_power'] is not None and val['t_total_power0'] != '' and val['t_total_power0'] is not None and val['annual_useage_hours'] != '' and val['annual_useage_hours'] is not None and val['annual_heat_hours'] != '' and val['annual_heat_hours'] is not None:
            annual_power_generation = (float(val['t_total_power']))*(float(val['annual_heat_hours']))/10000+(float(val['t_total_power0']))*((float(val['annual_useage_hours']))-(float(val['annual_heat_hours'])))/10000
            if annual_power_generation != -1:
                if val['flg'] == 'design':
                    result.annual_power_generation = annual_power_generation
                elif val['flg'] == 'check':
                    result.annual_power_generation = annual_power_generation
        print(result)


# 实现字段annual_power_supply:年供电量,的计算7
class Annual_power_supply(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['plant_electricity_consumption'] != '' and val['plant_electricity_consumption'] is not None and val['t_total_power'] != '' and val['t_total_power'] is not None and val['t_total_power0'] != '' and val['t_total_power0'] is not None and val['annual_useage_hours'] != '' and val['annual_useage_hours'] is not None and val['annual_heat_hours'] != '' and val['annual_heat_hours'] is not None:
            annual_power_supply = ((float(val['t_total_power']))*(float(val['annual_heat_hours']))/10000+(float(val['t_total_power0']))*((float(val['annual_useage_hours']))-(float(val['annual_heat_hours'])))/10000)*(1-(float(val['plant_electricity_consumption']))/100)
            if annual_power_supply != -1:
                if val['flg'] == 'design':
                    result.annual_power_supply = annual_power_supply
                elif val['flg'] == 'check':
                    result.annual_power_supply = annual_power_supply
        print(result)


# 实现字段smoke_power_coal_consumption:抽凝工况发电标煤耗率,的计算8
class Smoke_power_coal_consumption(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['boiler_efficiency'] != '' and val['boiler_efficiency'] is not None and val['pipeline_efficiency'] != '' and val['pipeline_efficiency'] is not None and val['t_steam_enthalpy'] != '' and val['t_steam_enthalpy'] is not None and val['t_throttle_flow'] != '' and val['t_throttle_flow'] is not None and val['t_total_power'] != '' and val['t_total_power'] is not None and val['t_water_enthalpy'] != '' and val['t_water_enthalpy'] is not None:
            smoke_power_coal_consumption = ((float(val['t_throttle_flow']))*((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))/(float(val['t_total_power']))*1000)/((float(val['boiler_efficiency']))*0.01)/((float(val['pipeline_efficiency']))*0.01)/(7000*4.1868)*1000
            if smoke_power_coal_consumption != -1:
                if val['flg'] == 'design':
                    result.smoke_power_coal_consumption = smoke_power_coal_consumption
                elif val['flg'] == 'check':
                    result.smoke_power_coal_consumption = smoke_power_coal_consumption
        print(result)


# 实现字段power_coal_consumption:纯凝工况发电标煤耗率,的计算9
class Power_coal_consumption(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['boiler_efficiency'] != '' and val['boiler_efficiency'] is not None and val['pipeline_efficiency'] != '' and val['pipeline_efficiency'] is not None and val['t_steam_enthalpy'] != '' and val['t_steam_enthalpy'] is not None and val['t_throttle_flow'] != '' and val['t_throttle_flow'] is not None and val['t_total_power0'] != '' and val['t_total_power0'] is not None and val['t_water_enthalpy'] != '' and val['t_water_enthalpy'] is not None:
            power_coal_consumption = ((float(val['t_throttle_flow']))*((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))/(float(val['t_total_power0']))*1000)/((float(val['boiler_efficiency']))*0.01)/((float(val['pipeline_efficiency']))*0.01)/(7000*4.1868)*1000
            if power_coal_consumption != -1:
                if val['flg'] == 'design':
                    result.power_coal_consumption = power_coal_consumption
                elif val['flg'] == 'check':
                    result.power_coal_consumption = power_coal_consumption
        print(result)


# 实现字段smoke_supply_coal_consumption:抽凝工况供电标煤耗率,的计算10
class Smoke_supply_coal_consumption(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['plant_electricity_consumption'] != '' and val['plant_electricity_consumption'] is not None and val['boiler_efficiency'] != '' and val['boiler_efficiency'] is not None and val['pipeline_efficiency'] != '' and val['pipeline_efficiency'] is not None and val['t_steam_enthalpy'] != '' and val['t_steam_enthalpy'] is not None and val['t_throttle_flow'] != '' and val['t_throttle_flow'] is not None and val['t_total_power'] != '' and val['t_total_power'] is not None and val['t_water_enthalpy'] != '' and val['t_water_enthalpy'] is not None:
            smoke_supply_coal_consumption = (((float(val['t_throttle_flow']))*((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))/(float(val['t_total_power']))*1000)/((float(val['boiler_efficiency']))*0.01)/((float(val['pipeline_efficiency']))*0.01)/(7000*4.1868)*1000)/(1-(float(val['plant_electricity_consumption']))/100)
            if smoke_supply_coal_consumption != -1:
                if val['flg'] == 'design':
                    result.smoke_supply_coal_consumption = smoke_supply_coal_consumption
                elif val['flg'] == 'check':
                    result.smoke_supply_coal_consumption = smoke_supply_coal_consumption
        print(result)


# 实现字段supply_coal_consumption:纯凝工况供电标煤耗率,的计算11
class Supply_coal_consumption(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['plant_electricity_consumption'] != '' and val['plant_electricity_consumption'] is not None and val['boiler_efficiency'] != '' and val['boiler_efficiency'] is not None and val['pipeline_efficiency'] != '' and val['pipeline_efficiency'] is not None and val['t_steam_enthalpy'] != '' and val['t_steam_enthalpy'] is not None and val['t_throttle_flow'] != '' and val['t_throttle_flow'] is not None and val['t_total_power0'] != '' and val['t_total_power0'] is not None and val['t_water_enthalpy'] != '' and val['t_water_enthalpy'] is not None:
            supply_coal_consumption = (((float(val['t_throttle_flow']))*((float(val['t_steam_enthalpy']))-(float(val['t_water_enthalpy'])))/(float(val['t_total_power0']))*1000)/((float(val['boiler_efficiency']))*0.01)/((float(val['pipeline_efficiency']))*0.01)/(7000*4.1868)*1000)/(1-(float(val['plant_electricity_consumption']))/100)
            if supply_coal_consumption != -1:
                if val['flg'] == 'design':
                    result.supply_coal_consumption = supply_coal_consumption
                elif val['flg'] == 'check':
                    result.supply_coal_consumption = supply_coal_consumption
        print(result)


# 实现字段annual_average_thermoelectric_ratio:全年平均热电比,的计算12
class Annual_average_thermoelectric_ratio(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['condensate_backwater_pressure'] != '' and val['condensate_backwater_pressure'] is not None and val['t_point_enthalpy'] != '' and val['t_point_enthalpy'] is not None and val['t_point_flow'] != '' and val['t_point_flow'] is not None and val['t_total_power'] != '' and val['t_total_power'] is not None and val['t_total_power0'] != '' and val['t_total_power0'] is not None and val['annual_useage_hours'] != '' and val['annual_useage_hours'] is not None and val['annual_heat_hours'] != '' and val['annual_heat_hours'] is not None:
            annual_average_thermoelectric_ratio = ((float(val['t_point_flow']))*((float(val['t_point_enthalpy']))-(seuif97.HL_P(10.00*(float(val['condensate_backwater_pressure'])))))*(float(val['annual_heat_hours']))/1000)/(((float(val['t_total_power']))*(float(val['annual_heat_hours']))/10000+(float(val['t_total_power0']))*((float(val['annual_useage_hours']))-(float(val['annual_heat_hours'])))/10000)*3.6*10)*100
            if annual_average_thermoelectric_ratio != -1:
                if val['flg'] == 'design':
                    result.annual_average_thermoelectric_ratio = annual_average_thermoelectric_ratio
                elif val['flg'] == 'check':
                    result.annual_average_thermoelectric_ratio = annual_average_thermoelectric_ratio
        print(result)


# 实现字段smoke_heat_efficiency:抽凝工况全厂热效率,的计算13
class Smoke_heat_efficiency(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        # val['surplus_gas_bfg'] = Boiler.surplus_gas_bfg
        # val['surplus_gas_ldg'] = Boiler.surplus_gas_ldg
        # val['surplus_gas_cog'] = Boiler.surplus_gas_cog
        # val['bfg_gas_calorific_value'] = Boiler.bfg_gas_calorific_value
        # val['ldg_gas_calorific_value'] = Boiler.ldg_gas_calorific_value
        # val['cog_gas_calorific_value'] = Boiler.cog_gas_calorific_value

        if val['condensate_backwater_pressure'] != '' and val['condensate_backwater_pressure'] is not None and \
            val['t_point_enthalpy'] != '' and val['t_point_enthalpy'] is not None and \
            val['t_point_flow'] != '' and val['t_point_flow'] is not None and \
            val['t_total_power'] != '' and val['t_total_power'] is not None and \
            val['surplus_gas_bfg'] != '' and val['surplus_gas_bfg'] is not None and \
            val['surplus_gas_ldg'] != '' and val['surplus_gas_ldg'] is not None and \
            val['surplus_gas_cog'] != '' and val['surplus_gas_cog'] is not None and \
            val['bfg_gas_calorific_value'] != '' and val['bfg_gas_calorific_value'] is not None and \
            val['ldg_gas_calorific_value'] != '' and val['ldg_gas_calorific_value'] is not None and \
            val['cog_gas_calorific_value'] != '' and val['cog_gas_calorific_value'] is not None:

            smoke_heat_efficiency = (float(val['t_total_power'])*3.6+float(val['t_point_flow'])*(float(val['t_point_enthalpy'])-(seuif97.HL_P(10.00*float(val['condensate_backwater_pressure'])))))/(float(val['surplus_gas_bfg'])*float(val['bfg_gas_calorific_value'])+float(val['surplus_gas_ldg'])*float(val['ldg_gas_calorific_value'])+float(val['surplus_gas_cog'])*float(val['cog_gas_calorific_value']))*100
            if smoke_heat_efficiency != -1:
                if val['flg'] == 'design':
                    result.smoke_heat_efficiency = smoke_heat_efficiency
                elif val['flg'] == 'check':
                    result.smoke_heat_efficiency = smoke_heat_efficiency
        print(result)


# 实现字段heat_efficiency:纯凝工况全厂热效率,的计算14
class Heat_efficiency(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_total_power'] != '' and val['t_total_power'] is not None and \
            val['surplus_gas_bfg'] != '' and val['surplus_gas_bfg'] is not None and \
            val['surplus_gas_ldg'] != '' and val['surplus_gas_ldg'] is not None and \
            val['surplus_gas_cog'] != '' and val['surplus_gas_cog'] is not None and \
            val['bfg_gas_calorific_value'] != '' and val['bfg_gas_calorific_value'] is not None and \
            val['ldg_gas_calorific_value'] != '' and val['ldg_gas_calorific_value'] is not None and \
            val['cog_gas_calorific_value'] != '' and val['cog_gas_calorific_value'] is not None:

            heat_efficiency = (float(val['t_total_power'])*3.6)/(float(val['surplus_gas_bfg'])*float(val['bfg_gas_calorific_value'])+float(val['surplus_gas_ldg'])*float(val['ldg_gas_calorific_value'])+float(val['surplus_gas_cog'])*float(val['cog_gas_calorific_value']))*100
            if heat_efficiency != -1:
                if val['flg'] == 'design':
                    result.heat_efficiency = heat_efficiency
                elif val['flg'] == 'check':
                    result.heat_efficiency = heat_efficiency
        print(result)


# 实现字段condensate_backwater_temperature:特殊处理部分--凝结水回水温度,的计算15
class Condensate_backwater_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['condensate_backwater_pressure'] != '' and val['condensate_backwater_pressure'] is not None:
            condensate_backwater_temperature = seuif97.tsat_p(10.00*(float(val['condensate_backwater_pressure'])))
            if condensate_backwater_temperature != -1:
                if val['flg'] == 'design':
                    result.condensate_backwater_temperature = condensate_backwater_temperature
                elif val['flg'] == 'check':
                    result.condensate_backwater_temperature = condensate_backwater_temperature
        print(result)


# 实现字段condensate_backwater_enthalpy:特殊处理部分--凝结水回水焓值,的计算16
class Condensate_backwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['condensate_backwater_pressure'] != '' and val['condensate_backwater_pressure'] is not None:
            condensate_backwater_enthalpy = seuif97.HL_P(10.00*(float(val['condensate_backwater_pressure'])))
            if condensate_backwater_enthalpy != -1:
                if val['flg'] == 'design':
                    result.condensate_backwater_enthalpy = condensate_backwater_enthalpy
                elif val['flg'] == 'check':
                    result.condensate_backwater_enthalpy = condensate_backwater_enthalpy
        print(result)



class Economic_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        # 添加注册类
        calculationObserver.register(Smoke_heat_consumption_rate())
        calculationObserver.register(Heat_consumption_rate())
        calculationObserver.register(Smoke_steam_consumption_rate())
        calculationObserver.register(Steam_consumption_rate())
        calculationObserver.register(Annual_heat_supply())
        calculationObserver.register(Annual_power_generation())
        calculationObserver.register(Annual_power_supply())
        calculationObserver.register(Smoke_power_coal_consumption())
        calculationObserver.register(Power_coal_consumption())
        calculationObserver.register(Smoke_supply_coal_consumption())
        calculationObserver.register(Supply_coal_consumption())
        calculationObserver.register(Annual_average_thermoelectric_ratio())
        calculationObserver.register(Smoke_heat_efficiency())
        calculationObserver.register(Heat_efficiency())
        calculationObserver.register(Condensate_backwater_temperature())
        calculationObserver.register(Condensate_backwater_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, dbmodel, Boiler, form):
        val = {
            'flg': 'design',
            # 't_steam_enthalpy': form.get('t_steam_enthalpy'),
            # 't_point_enthalpy': form.get('t_point_enthalpy'),
            # 't_rated_fuel_consumption': form.get('t_rated_fuel_consumption'),
            'boiler_efficiency': form.get('boiler_efficiency'),
            'annual_heat_hours': form.get('annual_heat_hours'),
            # 't_total_power': form.get('t_total_power'),
            'condensate_backwater_pressure': form.get('condensate_backwater_pressure'),
            'annual_useage_hours': form.get('annual_useage_hours'),
            # 't_total_power0': form.get('t_total_power0'),
            # 't_base_heat_received_user': form.get('t_base_heat_received_user'),
            'plant_electricity_consumption': form.get('plant_electricity_consumption'),
            'pipeline_efficiency': form.get('pipeline_efficiency'),
            # 't_water_enthalpy': form.get('t_water_enthalpy'),
            # 't_point_flow': form.get('t_point_flow'),
            # 't_throttle_flow': form.get('t_throttle_flow'),
            'dbresult': dbmodel}

        val['t_steam_enthalpy'] = dbmodel.t_steam_enthalpy
        val['t_point_enthalpy'] = dbmodel.t_point_enthalpy
        val['t_point_flow'] = dbmodel.t_point_flow
        val['t_throttle_flow'] = dbmodel.t_throttle_flow
        val['t_total_power'] = dbmodel.t_total_power
        val['t_total_power0'] = dbmodel.t_total_power0
        val['t_base_heat_received_user'] = dbmodel.t_base_heat_received_user
        val['t_water_enthalpy'] = dbmodel.t_water_enthalpy
        val['t_rated_fuel_consumption'] = dbmodel.t_rated_fuel_consumption

        val['surplus_gas_bfg'] = Boiler.surplus_gas_bfg
        val['surplus_gas_ldg'] = Boiler.surplus_gas_ldg
        val['surplus_gas_cog'] = Boiler.surplus_gas_cog
        val['bfg_gas_calorific_value'] = Boiler.bfg_gas_calorific_value
        val['ldg_gas_calorific_value'] = Boiler.ldg_gas_calorific_value
        val['cog_gas_calorific_value'] = Boiler.cog_gas_calorific_value

        self.creatSubscriber(val)
        return val['dbresult']


