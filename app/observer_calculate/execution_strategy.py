# -*- coding: utf-8 -*-
from base import CalculationObserver, ExecuteStrategy
from coalchp_furnace_calculation import FSteamEnthalpy, \
        FWaterEnthalpy, ASaturationPressure, FSaturatedWaterEnthalpy, \
        ASaturationPressureAfter
from ..models import CoalCHPFurnaceCalculation
from GPG_Calculation import GPG_Boiler_superheated_steam_enthalpy, \
    GPG_Boiler_feedwater_enthalpy, GPG_Boiler_air_enthalpy, \
    GPG_Boiler_saturation_water_temperature, \
    GPG_Boiler_saturation_water_enthalpy



class Furnace_calculationBefore(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(FSteamEnthalpy())
        calculationObserver.register(FWaterEnthalpy())
        calculationObserver.register(ASaturationPressure())
        calculationObserver.register(FSaturatedWaterEnthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldobj, form):
        val = {'flg': 'design', 'f_steam_pressure': form.get('f_steam_pressure_design'), 'f_steam_temperature': form.get('f_steam_temperature_design'), 'f_water_temperature': form.get('f_water_temperature_design'), 'a_temperature': form.get('a_temperature_design'), 'dbresult': oldobj}
        self.creatSubscriber(val)

        val = {'flg': 'check', 'f_steam_pressure': form.get('f_steam_pressure_check'), 'f_steam_temperature': form.get('f_steam_temperature_check'), 'f_water_temperature': form.get('f_water_temperature_check'), 'a_temperature': form.get('a_temperature_check'), 'dbresult': oldobj}
        self.creatSubscriber(val)
        return val['dbresult']


class NeedsAfter(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(ASaturationPressureAfter())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, plan_id):
        furnace = CoalCHPFurnaceCalculation.query.filter_by(
            plan_id=plan_id).first()
        self.creatSubscriber(furnace)
        CoalCHPFurnaceCalculation.insert_furnace_calculation(furnace)



class GPG_Boiler_superheated_steam_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_superheated_steam_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'superheated_steam_temperature': form.get('superheated_steam_temperature'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_Boiler_feedwater_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_feedwater_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'boiler_feed_water_temperature': form.get('boiler_feed_water_temperature'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']
    
class GPG_Boiler_air_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_air_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'air_temperature': form.get('air_temperature'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']


class GPG_Boiler_saturation_water_temperature_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_saturation_water_temperature())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_Boiler_saturation_water_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_saturation_water_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']