# -*- coding: utf-8 -*-
from base import CalculationObserver, ExecuteStrategy
from ..service.ccpp_chimney_calculation import Inner_diameter_chimney


class Ccpp_chimney_calculateBefore(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        # 添加注册类
        calculationObserver.register(Inner_diameter_chimney())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, dbmodel, form):
        val = {
            'flg': 'design',
            'flue_gas_flow_velocity': form.get('flue_gas_flow_velocity'),
            'flue_gas_quantity': form.get('flue_gas_quantity'),
            'pressure_exhaust_smoke': form.get('pressure_exhaust_smoke'),
            'temperature_exhaust_smoke': form.get('temperature_exhaust_smoke'),
            'dbresult': dbmodel}
        self.creatSubscriber(val)
        return val['dbresult']
    
    def specialCalculationdb(self, dbmodel):
        val = {
            'flg': 'design',
            'flue_gas_flow_velocity': dbmodel.flue_gas_flow_velocity,
            'flue_gas_quantity': dbmodel.flue_gas_quantity,
            'pressure_exhaust_smoke': dbmodel.pressure_exhaust_smoke,
            'temperature_exhaust_smoke': dbmodel.temperature_exhaust_smoke,
            'dbresult': dbmodel}
        self.creatSubscriber(val)
        return val['dbresult']

