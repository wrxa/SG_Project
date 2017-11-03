# -*- coding: utf-8 -*-
from base import CalculationObserver, ExecuteStrategy
from coalchp_furnace_calculation import FSteamEnthalpy, \
        FWaterEnthalpy, ASaturationPressure, FSaturatedWaterEnthalpy, \
        ASaturationPressureAfter
from ..models import CoalCHPFurnaceCalculation


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