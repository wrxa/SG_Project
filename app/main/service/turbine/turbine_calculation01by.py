
# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97
from base import CalculationObserver, ExecuteStrategy


# 实现字段e_steam_entropy:特殊处理部分--7熵,的计算1
class E_steam_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            e_steam_entropy = seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))
            if e_steam_entropy != -1:
                if val['flg'] == 'design':
                    result.e_steam_entropy = e_steam_entropy
                elif val['flg'] == 'check':
                    result.e_steam_entropy = e_steam_entropy
        print(result)


# 实现字段e_steam_enthalpy:特殊处理部分--8焓,的计算2
class E_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            e_steam_enthalpy = seuif97.pt2hz((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))
            if e_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_steam_enthalpy = e_steam_enthalpy
                elif val['flg'] == 'check':
                    result.e_steam_enthalpy = e_steam_enthalpy
        print(result)


# 实现字段e_exhaust_point_entropy:11熵,的计算3
class E_exhaust_point_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            e_exhaust_point_entropy = (seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))
            if e_exhaust_point_entropy != -1:
                if val['flg'] == 'design':
                    result.e_exhaust_point_entropy = e_exhaust_point_entropy
                elif val['flg'] == 'check':
                    result.e_exhaust_point_entropy = e_exhaust_point_entropy
        print(result)


# 实现字段e_exhaust_point_enthalpy:特殊处理部分--12焓,的计算4
class E_exhaust_point_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            e_exhaust_point_enthalpy = seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_exhaust_point_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_exhaust_point_enthalpy = e_exhaust_point_enthalpy
                elif val['flg'] == 'check':
                    result.e_exhaust_point_enthalpy = e_exhaust_point_enthalpy
        print(result)


# 实现字段e_exhaust_after_steam:14抽汽后蒸汽量,的计算5
class E_exhaust_after_steam(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_flow'] != '' and val['e_exhaust_point_flow'] is not None and val['e_steam_flow'] != '' and val['e_steam_flow'] is not None:
            e_exhaust_after_steam = (float(val['e_steam_flow']))-(float(val['e_exhaust_point_flow']))
            if e_exhaust_after_steam != -1:
                if val['flg'] == 'design':
                    result.e_exhaust_after_steam = e_exhaust_after_steam
                elif val['flg'] == 'check':
                    result.e_exhaust_after_steam = e_exhaust_after_steam
        print(result)


# 实现字段e_exhaust_after_pressure:15压力,的计算6
class E_exhaust_after_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None:
            e_exhaust_after_pressure = (float(val['e_exhaust_point_pressure']))
            if e_exhaust_after_pressure != -1:
                if val['flg'] == 'design':
                    result.e_exhaust_after_pressure = e_exhaust_after_pressure
                elif val['flg'] == 'check':
                    result.e_exhaust_after_pressure = e_exhaust_after_pressure
        print(result)


# 实现字段e_exhaust_after_enthalpy:16焓,的计算7
class E_exhaust_after_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            e_exhaust_after_enthalpy = (seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))))
            if e_exhaust_after_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_exhaust_after_enthalpy = e_exhaust_after_enthalpy
                elif val['flg'] == 'check':
                    result.e_exhaust_after_enthalpy = e_exhaust_after_enthalpy
        print(result)


# 实现字段e_exhaust_after_entropy:17熵,的计算8
class E_exhaust_after_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            e_exhaust_after_entropy = (seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))
            if e_exhaust_after_entropy != -1:
                if val['flg'] == 'design':
                    result.e_exhaust_after_entropy = e_exhaust_after_entropy
                elif val['flg'] == 'check':
                    result.e_exhaust_after_entropy = e_exhaust_after_entropy
        print(result)


# 实现字段e_steam_exhaust_enthalpy:特殊处理部分--19抽凝焓,的计算9
class E_steam_exhaust_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_exhaust_pressure'] != '' and val['e_steam_exhaust_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            e_steam_exhaust_enthalpy = seuif97.ps2h((float(val['e_steam_exhaust_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_steam_exhaust_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_steam_exhaust_enthalpy = e_steam_exhaust_enthalpy
                elif val['flg'] == 'check':
                    result.e_steam_exhaust_enthalpy = e_steam_exhaust_enthalpy
        print(result)


# 实现字段e_backpressure_enthalpy:特殊处理部分--背压焓,的计算10
class E_backpressure_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            e_backpressure_enthalpy = seuif97.ps2h((float(val['e_backpressure_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_backpressure_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_backpressure_enthalpy = e_backpressure_enthalpy
                elif val['flg'] == 'check':
                    result.e_backpressure_enthalpy = e_backpressure_enthalpy
        print(result)


# 实现字段e_backpressure_flow:背压流量,的计算11
class E_backpressure_flow(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_flow'] != '' and val['e_exhaust_point_flow'] is not None and val['e_steam_flow'] != '' and val['e_steam_flow'] is not None:
            e_backpressure_flow = (float(val['e_steam_flow']))-(float(val['e_exhaust_point_flow']))
            if e_backpressure_flow != -1:
                if val['flg'] == 'design':
                    result.e_backpressure_flow = e_backpressure_flow
                elif val['flg'] == 'check':
                    result.e_backpressure_flow = e_backpressure_flow
        print(result)


# 实现字段e_gross_generation:20背压总发电量,的计算12
class E_gross_generation(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_exhaust_point_flow'] != '' and val['e_exhaust_point_flow'] is not None and val['e_turbine_efficiency'] != '' and val['e_turbine_efficiency'] is not None and val['e_mechanical_efficiency'] != '' and val['e_mechanical_efficiency'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_generator_efficiency'] != '' and val['e_generator_efficiency'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None and val['e_steam_flow'] != '' and val['e_steam_flow'] is not None:
            e_gross_generation = (float(val['e_turbine_efficiency']))*(float(val['e_mechanical_efficiency']))*(float(val['e_generator_efficiency']))/3.6*((float(val['e_steam_flow']))*((seuif97.pt2hz((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))-(seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))+((float(val['e_steam_flow']))-(float(val['e_exhaust_point_flow'])))*(((seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))-(seuif97.ps2h((float(val['e_backpressure_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))))))
            if e_gross_generation != -1:
                if val['flg'] == 'design':
                    result.e_gross_generation = e_gross_generation
                elif val['flg'] == 'check':
                    result.e_gross_generation = e_gross_generation
        print(result)


# 实现字段e_steam_extraction:21背压去除抽汽后,的计算13
class E_steam_extraction(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_exhaust_point_flow'] != '' and val['e_exhaust_point_flow'] is not None and val['e_turbine_efficiency'] != '' and val['e_turbine_efficiency'] is not None and val['e_mechanical_efficiency'] != '' and val['e_mechanical_efficiency'] is not None and val['e_hot_data'] != '' and val['e_hot_data'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_generator_efficiency'] != '' and val['e_generator_efficiency'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None and val['e_steam_flow'] != '' and val['e_steam_flow'] is not None:
            e_steam_extraction = (float(val['e_hot_data']))*((float(val['e_turbine_efficiency']))*(float(val['e_mechanical_efficiency']))*(float(val['e_generator_efficiency']))/3.6*((float(val['e_steam_flow']))*((seuif97.pt2hz((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))-(seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))+((float(val['e_steam_flow']))-(float(val['e_exhaust_point_flow'])))*(((seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))-(seuif97.ps2h((float(val['e_backpressure_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))))/1000
            if e_steam_extraction != -1:
                if val['flg'] == 'design':
                    result.e_steam_extraction = e_steam_extraction
                elif val['flg'] == 'check':
                    result.e_steam_extraction = e_steam_extraction
        print(result)


# 实现字段e_steam_extraction_select:22选定,的计算14
class E_steam_extraction_select(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_exhaust_point_flow'] != '' and val['e_exhaust_point_flow'] is not None and val['e_turbine_efficiency'] != '' and val['e_turbine_efficiency'] is not None and val['e_mechanical_efficiency'] != '' and val['e_mechanical_efficiency'] is not None and val['e_hot_data'] != '' and val['e_hot_data'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_generator_efficiency'] != '' and val['e_generator_efficiency'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None and val['e_steam_flow'] != '' and val['e_steam_flow'] is not None:
            e_steam_extraction_select = round(((float(val['e_hot_data']))*((float(val['e_turbine_efficiency']))*(float(val['e_mechanical_efficiency']))*(float(val['e_generator_efficiency']))/3.6*((float(val['e_steam_flow']))*((seuif97.pt2hz((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))-(seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))+((float(val['e_steam_flow']))-(float(val['e_exhaust_point_flow'])))*(((seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))-(seuif97.ps2h((float(val['e_backpressure_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))))/1000))
            if e_steam_extraction_select != -1:
                if val['flg'] == 'design':
                    result.e_steam_extraction_select = e_steam_extraction_select
                elif val['flg'] == 'check':
                    result.e_steam_extraction_select = e_steam_extraction_select
        print(result)


# 实现字段i_mechanical_efficiency:101机械效率,的计算15
class I_mechanical_efficiency(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_mechanical_efficiency'] != '' and val['e_mechanical_efficiency'] is not None:
            i_mechanical_efficiency = (float(val['e_mechanical_efficiency']))
            if i_mechanical_efficiency != -1:
                if val['flg'] == 'design':
                    result.i_mechanical_efficiency = i_mechanical_efficiency
                elif val['flg'] == 'check':
                    result.i_mechanical_efficiency = i_mechanical_efficiency
        print(result)


# 实现字段i_generator_efficiency:102发电机效率,的计算16
class I_generator_efficiency(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_generator_efficiency'] != '' and val['e_generator_efficiency'] is not None:
            i_generator_efficiency = (float(val['e_generator_efficiency']))
            if i_generator_efficiency != -1:
                if val['flg'] == 'design':
                    result.i_generator_efficiency = i_generator_efficiency
                elif val['flg'] == 'check':
                    result.i_generator_efficiency = i_generator_efficiency
        print(result)


# 实现字段i_steam_pressure:103主蒸汽压力,的计算17
class I_steam_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None:
            i_steam_pressure = (float(val['e_steam_pressure']))
            if i_steam_pressure != -1:
                if val['flg'] == 'design':
                    result.i_steam_pressure = i_steam_pressure
                elif val['flg'] == 'check':
                    result.i_steam_pressure = i_steam_pressure
        print(result)


# 实现字段i_steam_temperature:104温度,的计算18
class I_steam_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_steam_temperature = (float(val['e_steam_temperature']))
            if i_steam_temperature != -1:
                if val['flg'] == 'design':
                    result.i_steam_temperature = i_steam_temperature
                elif val['flg'] == 'check':
                    result.i_steam_temperature = i_steam_temperature
        print(result)


# 实现字段i_steam_entropy:特殊处理部分--106熵,的计算19
class I_steam_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_steam_entropy = seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))
            if i_steam_entropy != -1:
                if val['flg'] == 'design':
                    result.i_steam_entropy = i_steam_entropy
                elif val['flg'] == 'check':
                    result.i_steam_entropy = i_steam_entropy
        print(result)


# 实现字段i_steam_enthalpy:特殊处理部分--107焓,的计算20
class I_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_steam_enthalpy = seuif97.pt2hz(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))
            if i_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_steam_enthalpy = i_steam_enthalpy
                elif val['flg'] == 'check':
                    result.i_steam_enthalpy = i_steam_enthalpy
        print(result)


# 实现字段i_deoxidize_pressure:120D除氧压力,的计算21
class I_deoxidize_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None:
            i_deoxidize_pressure = ((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss']))))
            if i_deoxidize_pressure != -1:
                if val['flg'] == 'design':
                    result.i_deoxidize_pressure = i_deoxidize_pressure
                elif val['flg'] == 'check':
                    result.i_deoxidize_pressure = i_deoxidize_pressure
        print(result)


# 实现字段i_deoxidize_entropy:121熵,的计算22
class I_deoxidize_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_deoxidize_entropy = (seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))
            if i_deoxidize_entropy != -1:
                if val['flg'] == 'design':
                    result.i_deoxidize_entropy = i_deoxidize_entropy
                elif val['flg'] == 'check':
                    result.i_deoxidize_entropy = i_deoxidize_entropy
        print(result)


# 实现字段i_deoxidize_temperature:特殊处理部分--122温度,的计算23
class I_deoxidize_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_deoxidize_temperature = seuif97.ps2t((((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss']))))),((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))
            if i_deoxidize_temperature != -1:
                if val['flg'] == 'design':
                    result.i_deoxidize_temperature = i_deoxidize_temperature
                elif val['flg'] == 'check':
                    result.i_deoxidize_temperature = i_deoxidize_temperature
        print(result)


# 实现字段i_deoxidize_enthalpy:特殊处理部分--123焓,的计算24
class I_deoxidize_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_deoxidize_enthalpy = seuif97.ps2h((((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss']))))),((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))
            if i_deoxidize_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_deoxidize_enthalpy = i_deoxidize_enthalpy
                elif val['flg'] == 'check':
                    result.i_deoxidize_enthalpy = i_deoxidize_enthalpy
        print(result)


# 实现字段i_deoxidize_flow:124流量,的计算25
class I_deoxidize_flow(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['h_temperature'] != '' and val['h_temperature'] is not None and val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['h_blowdown_rate'] != '' and val['h_blowdown_rate'] is not None and val['e_steam_water_loss'] != '' and val['e_steam_water_loss'] is not None and val['e_throttle_flow'] != '' and val['e_throttle_flow'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_deoxidize_flow = (((float(val['e_throttle_flow']))*((float(val['e_steam_water_loss'])))*((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hz((2*(float(val['d_work_pressure']))),(float(val['h_temperature'])))))+((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-(float(val['e_throttle_flow']))*((float(val['e_steam_water_loss']))))*((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))-((((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98))*((seuif97.HL_T((float(val['d_water_temperature'])))))*0.98)/(((seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((float(val['d_water_temperature'])))))*0.98+((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))))
            if i_deoxidize_flow != -1:
                if val['flg'] == 'design':
                    result.i_deoxidize_flow = i_deoxidize_flow
                elif val['flg'] == 'check':
                    result.i_deoxidize_flow = i_deoxidize_flow
        print(result)


# 实现字段i_exhaust_point_pressure:126抽汽点压力,的计算26
class I_exhaust_point_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None:
            i_exhaust_point_pressure = (float(val['e_exhaust_point_pressure']))
            if i_exhaust_point_pressure != -1:
                if val['flg'] == 'design':
                    result.i_exhaust_point_pressure = i_exhaust_point_pressure
                elif val['flg'] == 'check':
                    result.i_exhaust_point_pressure = i_exhaust_point_pressure
        print(result)


# 实现字段i_exhaust_point_temperature:127温度,的计算27
class I_exhaust_point_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_temperature'] != '' and val['e_exhaust_point_temperature'] is not None:
            i_exhaust_point_temperature = (float(val['e_exhaust_point_temperature']))
            if i_exhaust_point_temperature != -1:
                if val['flg'] == 'design':
                    result.i_exhaust_point_temperature = i_exhaust_point_temperature
                elif val['flg'] == 'check':
                    result.i_exhaust_point_temperature = i_exhaust_point_temperature
        print(result)


# 实现字段i_exhaust_point_entropy:128熵,的计算28
class I_exhaust_point_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_exhaust_point_entropy = (seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))
            if i_exhaust_point_entropy != -1:
                if val['flg'] == 'design':
                    result.i_exhaust_point_entropy = i_exhaust_point_entropy
                elif val['flg'] == 'check':
                    result.i_exhaust_point_entropy = i_exhaust_point_entropy
        print(result)


# 实现字段i_exhaust_point_enthalpy:129焓,的计算29
class I_exhaust_point_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_exhaust_point_enthalpy = ((seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))
            if i_exhaust_point_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_exhaust_point_enthalpy = i_exhaust_point_enthalpy
                elif val['flg'] == 'check':
                    result.i_exhaust_point_enthalpy = i_exhaust_point_enthalpy
        print(result)


# 实现字段i_exhaust_point_flow:130流量,的计算30
class I_exhaust_point_flow(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_flow'] != '' and val['e_exhaust_point_flow'] is not None:
            i_exhaust_point_flow = (float(val['e_exhaust_point_flow']))
            if i_exhaust_point_flow != -1:
                if val['flg'] == 'design':
                    result.i_exhaust_point_flow = i_exhaust_point_flow
                elif val['flg'] == 'check':
                    result.i_exhaust_point_flow = i_exhaust_point_flow
        print(result)


# 实现字段i_low1_pressure:1321号低加压力,的计算31
class I_low1_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            i_low1_pressure = ((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))
            if i_low1_pressure != -1:
                if val['flg'] == 'design':
                    result.i_low1_pressure = i_low1_pressure
                elif val['flg'] == 'check':
                    result.i_low1_pressure = i_low1_pressure
        print(result)


# 实现字段i_low1_entropy:133熵,的计算32
class I_low1_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_low1_entropy = ((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))
            if i_low1_entropy != -1:
                if val['flg'] == 'design':
                    result.i_low1_entropy = i_low1_entropy
                elif val['flg'] == 'check':
                    result.i_low1_entropy = i_low1_entropy
        print(result)


# 实现字段i_low1_temperature:特殊处理部分--134温度,的计算33
class I_low1_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_low1_temperature = seuif97.ps2t((((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))
            if i_low1_temperature != -1:
                if val['flg'] == 'design':
                    result.i_low1_temperature = i_low1_temperature
                elif val['flg'] == 'check':
                    result.i_low1_temperature = i_low1_temperature
        print(result)


# 实现字段i_low1_enthalpy:特殊处理部分--135焓,的计算34
class I_low1_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_low1_enthalpy = seuif97.ps2h((((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))
            if i_low1_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_low1_enthalpy = i_low1_enthalpy
                elif val['flg'] == 'check':
                    result.i_low1_enthalpy = i_low1_enthalpy
        print(result)


# 实现字段i_low1_flow:136流量,的计算35
class I_low1_flow(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['h_temperature'] != '' and val['h_temperature'] is not None and val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['h_blowdown_rate'] != '' and val['h_blowdown_rate'] is not None and val['e_steam_water_loss'] != '' and val['e_steam_water_loss'] is not None and val['e_throttle_flow'] != '' and val['e_throttle_flow'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_low1_flow = (((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow']))*((float(val['e_steam_water_loss'])))*((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hz((2*(float(val['d_work_pressure']))),(float(val['h_temperature'])))))+((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-(float(val['e_throttle_flow']))*((float(val['e_steam_water_loss']))))*((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))-((((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98))*((seuif97.HL_T((float(val['d_water_temperature'])))))*0.98)/(((seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((float(val['d_water_temperature'])))))*0.98+((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-((float(val['e_steam_water_loss'])))*((float(val['e_throttle_flow']))))*(((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((seuif97.ps2h(((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss'])))),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))))-(seuif97.HL_T(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))))/0.98)
            if i_low1_flow != -1:
                if val['flg'] == 'design':
                    result.i_low1_flow = i_low1_flow
                elif val['flg'] == 'check':
                    result.i_low1_flow = i_low1_flow
        print(result)


# 实现字段i_steam_exhaust_pressure:144背压压力,的计算36
class I_steam_exhaust_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            i_steam_exhaust_pressure = (float(val['e_backpressure_pressure']))
            if i_steam_exhaust_pressure != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_pressure = i_steam_exhaust_pressure
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_pressure = i_steam_exhaust_pressure
        print(result)


# 实现字段i_steam_exhaust_entropy:145熵,的计算37
class I_steam_exhaust_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_steam_exhaust_entropy = (((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))
            if i_steam_exhaust_entropy != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_entropy = i_steam_exhaust_entropy
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_entropy = i_steam_exhaust_entropy
        print(result)


# 实现字段i_steam_exhaust_enthalpy:特殊处理部分--146焓,的计算38
class I_steam_exhaust_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_steam_exhaust_enthalpy = seuif97.ps2h(((float(val['e_backpressure_pressure']))),((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))
            if i_steam_exhaust_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy = i_steam_exhaust_enthalpy
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy = i_steam_exhaust_enthalpy
        print(result)


# 实现字段i_steam_exhaust_enthalpy_actual:147实际焓,的计算39
class I_steam_exhaust_enthalpy_actual(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['i_turbine_efficiency'] != '' and val['i_turbine_efficiency'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_steam_exhaust_enthalpy_actual = (seuif97.ps2h((((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))-((seuif97.ps2h((((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))-(seuif97.ps2h(((float(val['e_backpressure_pressure']))),((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))))*(float(val['i_turbine_efficiency']))
            if i_steam_exhaust_enthalpy_actual != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy_actual = i_steam_exhaust_enthalpy_actual
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_actual = i_steam_exhaust_enthalpy_actual
        print(result)


# 实现字段i_steam_exhaust_enthalpy_steam:特殊处理部分--148饱和蒸汽焓,的计算40
class I_steam_exhaust_enthalpy_steam(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            i_steam_exhaust_enthalpy_steam = seuif97.HG_P(((float(val['e_backpressure_pressure'])))*10)
            if i_steam_exhaust_enthalpy_steam != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy_steam = i_steam_exhaust_enthalpy_steam
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_steam = i_steam_exhaust_enthalpy_steam
        print(result)


# 实现字段i_steam_exhaust_enthalpy_water:特殊处理部分--149饱和水焓,的计算41
class I_steam_exhaust_enthalpy_water(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            i_steam_exhaust_enthalpy_water = seuif97.HL_P(((float(val['e_backpressure_pressure'])))*10)
            if i_steam_exhaust_enthalpy_water != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy_water = i_steam_exhaust_enthalpy_water
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_water = i_steam_exhaust_enthalpy_water
        print(result)


# 实现字段i_steam_exhaust_dry:150干度,的计算42
class I_steam_exhaust_dry(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['i_turbine_efficiency'] != '' and val['i_turbine_efficiency'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            i_steam_exhaust_dry = 1-(((seuif97.ps2h((((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))-((seuif97.ps2h((((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))-(seuif97.ps2h(((float(val['e_backpressure_pressure']))),((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))))*(float(val['i_turbine_efficiency'])))-(seuif97.HL_P(((float(val['e_backpressure_pressure'])))*10)))/((seuif97.HG_P(((float(val['e_backpressure_pressure'])))*10))-(seuif97.HL_P(((float(val['e_backpressure_pressure'])))*10)))
            if i_steam_exhaust_dry != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_dry = i_steam_exhaust_dry
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_dry = i_steam_exhaust_dry
        print(result)


# 实现字段i_steam_exhaust_flow:151流量,的计算43
class I_steam_exhaust_flow(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['h_temperature'] != '' and val['h_temperature'] is not None and val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_exhaust_point_flow'] != '' and val['e_exhaust_point_flow'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['h_blowdown_rate'] != '' and val['h_blowdown_rate'] is not None and val['e_steam_water_loss'] != '' and val['e_steam_water_loss'] is not None and val['e_throttle_flow'] != '' and val['e_throttle_flow'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['i_steam_flow'] != '' and val['i_steam_flow'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['i_high1_flow'] != '' and val['i_high1_flow'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None and val['i_high2_flow'] != '' and val['i_high2_flow'] is not None and val['i_low2_flow'] != '' and val['i_low2_flow'] is not None:
            i_steam_exhaust_flow = (float(val['i_steam_flow']))-(float(val['i_high1_flow']))-(float(val['i_high2_flow']))-((((float(val['e_throttle_flow']))*((float(val['e_steam_water_loss'])))*((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hz((2*(float(val['d_work_pressure']))),(float(val['h_temperature'])))))+((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-(float(val['e_throttle_flow']))*((float(val['e_steam_water_loss']))))*((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))-((((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98))*((seuif97.HL_T((float(val['d_water_temperature'])))))*0.98)/(((seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((float(val['d_water_temperature'])))))*0.98+((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1))))))-((float(val['e_exhaust_point_flow'])))-((((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow']))*((float(val['e_steam_water_loss'])))*((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hz((2*(float(val['d_work_pressure']))),(float(val['h_temperature'])))))+((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-(float(val['e_throttle_flow']))*((float(val['e_steam_water_loss']))))*((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))-((((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98))*((seuif97.HL_T((float(val['d_water_temperature'])))))*0.98)/(((seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((float(val['d_water_temperature'])))))*0.98+((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-((float(val['e_steam_water_loss'])))*((float(val['e_throttle_flow']))))*(((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((seuif97.ps2h(((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss'])))),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))))-(seuif97.HL_T(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))))/0.98))-(float(val['i_low2_flow']))
            if i_steam_exhaust_flow != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_flow = i_steam_exhaust_flow
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_flow = i_steam_exhaust_flow
        print(result)


# 实现字段i_total_power:153总功率,的计算44
class I_total_power(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['i_hh2_deoxidize_power'] != '' and val['i_hh2_deoxidize_power'] is not None and val['i_deoxidize_exhaust_power'] != '' and val['i_deoxidize_exhaust_power'] is not None and val['i_exhaust_lh1_power'] != '' and val['i_exhaust_lh1_power'] is not None and val['i_lh2_steam_power'] != '' and val['i_lh2_steam_power'] is not None:
            i_total_power = ((float(val['i_lh2_steam_power']))+(float(val['i_exhaust_lh1_power']))+(float(val['i_hh2_deoxidize_power']))+(float(val['i_deoxidize_exhaust_power'])))
            if i_total_power != -1:
                if val['flg'] == 'design':
                    result.i_total_power = i_total_power
                elif val['flg'] == 'check':
                    result.i_total_power = i_total_power
        print(result)


# 实现字段i_calculation_error:154计算误差---抽凝,的计算45
class I_calculation_error(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_exhaust_point_flow'] != '' and val['e_exhaust_point_flow'] is not None and val['e_turbine_efficiency'] != '' and val['e_turbine_efficiency'] is not None and val['e_mechanical_efficiency'] != '' and val['e_mechanical_efficiency'] is not None and val['e_hot_data'] != '' and val['e_hot_data'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_generator_efficiency'] != '' and val['e_generator_efficiency'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None and val['i_hh2_deoxidize_power'] != '' and val['i_hh2_deoxidize_power'] is not None and val['e_steam_flow'] != '' and val['e_steam_flow'] is not None and val['i_deoxidize_exhaust_power'] != '' and val['i_deoxidize_exhaust_power'] is not None and val['i_exhaust_lh1_power'] != '' and val['i_exhaust_lh1_power'] is not None and val['i_lh2_steam_power'] != '' and val['i_lh2_steam_power'] is not None:
            i_calculation_error = ((((float(val['i_lh2_steam_power']))+(float(val['i_exhaust_lh1_power']))+(float(val['i_hh2_deoxidize_power']))+(float(val['i_deoxidize_exhaust_power']))))-(round(((float(val['e_hot_data']))*((float(val['e_turbine_efficiency']))*(float(val['e_mechanical_efficiency']))*(float(val['e_generator_efficiency']))/3.6*((float(val['e_steam_flow']))*((seuif97.pt2hz((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))-(seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))+((float(val['e_steam_flow']))-(float(val['e_exhaust_point_flow'])))*(((seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))-(seuif97.ps2h((float(val['e_backpressure_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))))/1000)))*1000)/(round(((float(val['e_hot_data']))*((float(val['e_turbine_efficiency']))*(float(val['e_mechanical_efficiency']))*(float(val['e_generator_efficiency']))/3.6*((float(val['e_steam_flow']))*((seuif97.pt2hz((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))-(seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))+((float(val['e_steam_flow']))-(float(val['e_exhaust_point_flow'])))*(((seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))-(seuif97.ps2h((float(val['e_backpressure_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))))))/1000)))/1000
            if i_calculation_error != -1:
                if val['flg'] == 'design':
                    result.i_calculation_error = i_calculation_error
                elif val['flg'] == 'check':
                    result.i_calculation_error = i_calculation_error
        print(result)


# 实现字段h_pressure:27压力,的计算46
class H_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None:
            h_pressure = 2*(float(val['d_work_pressure']))
            if h_pressure != -1:
                if val['flg'] == 'design':
                    result.h_pressure = h_pressure
                elif val['flg'] == 'check':
                    result.h_pressure = h_pressure
        print(result)


# 实现字段h_enthalpy:特殊处理部分--28焓值,的计算47
class H_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['h_temperature'] != '' and val['h_temperature'] is not None and val['d_work_pressure'] != '' and val['d_work_pressure'] is not None:
            h_enthalpy = seuif97.pt2hz((2*(float(val['d_work_pressure']))),(float(val['h_temperature'])))
            if h_enthalpy != -1:
                if val['flg'] == 'design':
                    result.h_enthalpy = h_enthalpy
                elif val['flg'] == 'check':
                    result.h_enthalpy = h_enthalpy
        print(result)


# 实现字段h_amount:29量,的计算48
class H_amount(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['h_blowdown_rate'] != '' and val['h_blowdown_rate'] is not None and val['e_steam_water_loss'] != '' and val['e_steam_water_loss'] is not None:
            # h_amount = (float(val['e_steam_water_loss']))
            h_amount = (float(val['e_steam_water_loss']))
            if h_amount != -1:
                if val['flg'] == 'design':
                    result.h_amount = h_amount
                elif val['flg'] == 'check':
                    result.h_amount = h_amount
        print(result)


# 实现字段hh1_water_temperature:30给水出水温度,的计算49
class Hh1_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None:
            hh1_water_temperature = (float(val['d_water_temperature']))
            if hh1_water_temperature != -1:
                if val['flg'] == 'design':
                    result.hh1_water_temperature = hh1_water_temperature
                elif val['flg'] == 'check':
                    result.hh1_water_temperature = hh1_water_temperature
        print(result)


# 实现字段hh1_water_enthalpy:特殊处理部分--31给水出口焓,的计算50
class Hh1_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None:
            hh1_water_enthalpy = seuif97.HL_T(((float(val['d_water_temperature']))))
            if hh1_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh1_water_enthalpy = hh1_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_water_enthalpy = hh1_water_enthalpy
        print(result)


# 实现字段hh1_top_difference:32上端差,的计算51
class Hh1_top_difference(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None:
            hh1_top_difference = (float(val['lh1_top_difference']))
            if hh1_top_difference != -1:
                if val['flg'] == 'design':
                    result.hh1_top_difference = hh1_top_difference
                elif val['flg'] == 'check':
                    result.hh1_top_difference = hh1_top_difference
        print(result)


# 实现字段hh1_saturated_water_temperature:33饱和水温度,的计算52
class Hh1_saturated_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None:
            hh1_saturated_water_temperature = ((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))
            if hh1_saturated_water_temperature != -1:
                if val['flg'] == 'design':
                    result.hh1_saturated_water_temperature = hh1_saturated_water_temperature
                elif val['flg'] == 'check':
                    result.hh1_saturated_water_temperature = hh1_saturated_water_temperature
        print(result)


# 实现字段hh1_saturated_water_enthalpy:特殊处理部分--34饱和水焓,的计算53
class Hh1_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None:
            hh1_saturated_water_enthalpy = seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))
            if hh1_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh1_saturated_water_enthalpy = hh1_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_saturated_water_enthalpy = hh1_saturated_water_enthalpy
        print(result)


# 实现字段hh1_work_pressure:特殊处理部分--35工作压力,的计算54
class Hh1_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None:
            hh1_work_pressure = seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1
            if hh1_work_pressure != -1:
                if val['flg'] == 'design':
                    result.hh1_work_pressure = hh1_work_pressure
                elif val['flg'] == 'check':
                    result.hh1_work_pressure = hh1_work_pressure
        print(result)


# 实现字段hh1_pressure_loss:36抽汽管压损,的计算55
class Hh1_pressure_loss(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None:
            hh1_pressure_loss = (float(val['lh1_pressure_loss']))
            if hh1_pressure_loss != -1:
                if val['flg'] == 'design':
                    result.hh1_pressure_loss = hh1_pressure_loss
                elif val['flg'] == 'check':
                    result.hh1_pressure_loss = hh1_pressure_loss
        print(result)


# 实现字段hh1_extraction_pressure:37抽汽压力,的计算56
class Hh1_extraction_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None:
            hh1_extraction_pressure = (seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))
            if hh1_extraction_pressure != -1:
                if val['flg'] == 'design':
                    result.hh1_extraction_pressure = hh1_extraction_pressure
                elif val['flg'] == 'check':
                    result.hh1_extraction_pressure = hh1_extraction_pressure
        print(result)


# 实现字段hh1_extraction_enthalpy:特殊处理部分--38抽汽焓,的计算57
class Hh1_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            hh1_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if hh1_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh1_extraction_enthalpy = hh1_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_extraction_enthalpy = hh1_extraction_enthalpy
        print(result)


# 实现字段hh1_extraction_amount:39抽汽量,的计算58
class Hh1_extraction_amount(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_throttle_flow'] != '' and val['e_throttle_flow'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            hh1_extraction_amount = ((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98
            if hh1_extraction_amount != -1:
                if val['flg'] == 'design':
                    result.hh1_extraction_amount = hh1_extraction_amount
                elif val['flg'] == 'check':
                    result.hh1_extraction_amount = hh1_extraction_amount
        print(result)


# 实现字段d_water_enthalpy:特殊处理部分--51给水出口焓,的计算59
class D_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None:
            d_water_enthalpy = seuif97.HL_T((float(val['d_water_temperature'])))
            if d_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.d_water_enthalpy = d_water_enthalpy
                elif val['flg'] == 'check':
                    result.d_water_enthalpy = d_water_enthalpy
        print(result)


# 实现字段d_extraction_pressure:54抽汽压力,的计算60
class D_extraction_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None:
            d_extraction_pressure = (float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))
            if d_extraction_pressure != -1:
                if val['flg'] == 'design':
                    result.d_extraction_pressure = d_extraction_pressure
                elif val['flg'] == 'check':
                    result.d_extraction_pressure = d_extraction_pressure
        print(result)


# 实现字段d_extraction_enthalpy:特殊处理部分--55抽汽焓,的计算61
class D_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            d_extraction_enthalpy = seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if d_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.d_extraction_enthalpy = d_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.d_extraction_enthalpy = d_extraction_enthalpy
        print(result)


# 实现字段d_extraction_amount:56抽汽量,的计算62
class D_extraction_amount(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['h_temperature'] != '' and val['h_temperature'] is not None and val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['h_blowdown_rate'] != '' and val['h_blowdown_rate'] is not None and val['e_steam_water_loss'] != '' and val['e_steam_water_loss'] is not None and val['e_throttle_flow'] != '' and val['e_throttle_flow'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            d_extraction_amount = ((float(val['e_throttle_flow']))*((float(val['e_steam_water_loss'])))*((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hz((2*(float(val['d_work_pressure']))),(float(val['h_temperature'])))))+((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-(float(val['e_throttle_flow']))*((float(val['e_steam_water_loss']))))*((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))-((((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98))*((seuif97.HL_T((float(val['d_water_temperature'])))))*0.98)/(((seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((float(val['d_water_temperature'])))))*0.98+((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1))))
            if d_extraction_amount != -1:
                if val['flg'] == 'design':
                    result.d_extraction_amount = d_extraction_amount
                elif val['flg'] == 'check':
                    result.d_extraction_amount = d_extraction_amount
        print(result)


# 实现字段lh1_water_temperature:57给水出水温度,的计算63
class Lh1_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            lh1_water_temperature = round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0)
            if lh1_water_temperature != -1:
                if val['flg'] == 'design':
                    result.lh1_water_temperature = lh1_water_temperature
                elif val['flg'] == 'check':
                    result.lh1_water_temperature = lh1_water_temperature
        print(result)


# 实现字段lh1_water_enthalpy:58给水出口焓,的计算64
class Lh1_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            lh1_water_enthalpy = (seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)
            if lh1_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh1_water_enthalpy = lh1_water_enthalpy
                elif val['flg'] == 'check':
                    result.lh1_water_enthalpy = lh1_water_enthalpy
        print(result)


# 实现字段lh1_saturated_water_temperature:60饱和水温度,的计算65
class Lh1_saturated_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            lh1_saturated_water_temperature = (round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))
            if lh1_saturated_water_temperature != -1:
                if val['flg'] == 'design':
                    result.lh1_saturated_water_temperature = lh1_saturated_water_temperature
                elif val['flg'] == 'check':
                    result.lh1_saturated_water_temperature = lh1_saturated_water_temperature
        print(result)


# 实现字段lh1_saturated_water_enthalpy:特殊处理部分--61饱和水焓,的计算66
class Lh1_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            lh1_saturated_water_enthalpy = seuif97.HL_T(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))
            if lh1_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh1_saturated_water_enthalpy = lh1_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.lh1_saturated_water_enthalpy = lh1_saturated_water_enthalpy
        print(result)


# 实现字段lh1_work_pressure:特殊处理部分--62工作压力,的计算67
class Lh1_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            lh1_work_pressure = seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1
            if lh1_work_pressure != -1:
                if val['flg'] == 'design':
                    result.lh1_work_pressure = lh1_work_pressure
                elif val['flg'] == 'check':
                    result.lh1_work_pressure = lh1_work_pressure
        print(result)


# 实现字段lh1_extraction_pressure:64抽汽压力,的计算68
class Lh1_extraction_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            lh1_extraction_pressure = (seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss'])))
            if lh1_extraction_pressure != -1:
                if val['flg'] == 'design':
                    result.lh1_extraction_pressure = lh1_extraction_pressure
                elif val['flg'] == 'check':
                    result.lh1_extraction_pressure = lh1_extraction_pressure
        print(result)


# 实现字段lh1_extraction_enthalpy:特殊处理部分--65抽汽焓,的计算69
class Lh1_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            lh1_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss'])))),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if lh1_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh1_extraction_enthalpy = lh1_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.lh1_extraction_enthalpy = lh1_extraction_enthalpy
        print(result)


# 实现字段lh1_extraction_amount:66抽汽量,的计算70
class Lh1_extraction_amount(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['h_temperature'] != '' and val['h_temperature'] is not None and val['d_water_temperature'] != '' and val['d_water_temperature'] is not None and val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['s_lh_grade'] != '' and val['s_lh_grade'] is not None and val['h_blowdown_rate'] != '' and val['h_blowdown_rate'] is not None and val['e_steam_water_loss'] != '' and val['e_steam_water_loss'] is not None and val['e_throttle_flow'] != '' and val['e_throttle_flow'] is not None and val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None:
            lh1_extraction_amount = ((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow']))*((float(val['e_steam_water_loss'])))*((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hz((2*(float(val['d_work_pressure']))),(float(val['h_temperature'])))))+((float(val['e_throttle_flow']))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-(float(val['e_throttle_flow']))*((float(val['e_steam_water_loss']))))*((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))-((((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98))*((seuif97.HL_T((float(val['d_water_temperature'])))))*0.98)/(((seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((float(val['d_water_temperature'])))))*0.98+((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1)))))-(((float(val['e_throttle_flow'])))*((seuif97.HL_T(((float(val['d_water_temperature'])))))-(seuif97.HL_T((float(val['d_water_temperature'])))))/((seuif97.ps2h(((seuif97.psat_t((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))*0.1)/(1-((float(val['lh1_pressure_loss']))))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))-(seuif97.HL_T((((float(val['d_water_temperature'])))+((float(val['lh1_top_difference'])))))))/0.98)-((float(val['e_steam_water_loss'])))*((float(val['e_throttle_flow']))))*(((seuif97.HL_T((float(val['d_water_temperature']))))-((seuif97.HL_T((float(val['d_water_temperature']))))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((float(val['s_lh_grade']))+1))-(seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))))/((seuif97.ps2h(((seuif97.psat_t(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss'])))),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))))-(seuif97.HL_T(((round((float(val['d_water_temperature']))-((float(val['d_water_temperature']))-(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))/((float(val['s_lh_grade']))+1),0))+(float(val['lh1_top_difference']))))))/0.98
            if lh1_extraction_amount != -1:
                if val['flg'] == 'design':
                    result.lh1_extraction_amount = lh1_extraction_amount
                elif val['flg'] == 'check':
                    result.lh1_extraction_amount = lh1_extraction_amount
        print(result)


# 实现字段c_water_temperature:特殊处理部分--77给水出水温度,的计算71
class C_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            c_water_temperature = seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)
            if c_water_temperature != -1:
                if val['flg'] == 'design':
                    result.c_water_temperature = c_water_temperature
                elif val['flg'] == 'check':
                    result.c_water_temperature = c_water_temperature
        print(result)


# 实现字段c_water_enthalpy:特殊处理部分--78给水出口焓,的计算72
class C_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            c_water_enthalpy = seuif97.pt2hw(((float(val['e_backpressure_pressure']))),(seuif97.tsat_p(((float(val['e_backpressure_pressure'])))*10)))
            if c_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.c_water_enthalpy = c_water_enthalpy
                elif val['flg'] == 'check':
                    result.c_water_enthalpy = c_water_enthalpy
        print(result)


# 实现字段c_work_pressure:79背压工作压力,的计算73
class C_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None:
            c_work_pressure = (float(val['e_backpressure_pressure']))
            if c_work_pressure != -1:
                if val['flg'] == 'design':
                    result.c_work_pressure = c_work_pressure
                elif val['flg'] == 'check':
                    result.c_work_pressure = c_work_pressure
        print(result)



class Turbine_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        # 添加注册类
        calculationObserver.register(E_steam_entropy())
        calculationObserver.register(E_steam_enthalpy())
        calculationObserver.register(E_exhaust_point_entropy())
        calculationObserver.register(E_exhaust_point_enthalpy())
        calculationObserver.register(E_exhaust_after_steam())
        calculationObserver.register(E_exhaust_after_pressure())
        calculationObserver.register(E_exhaust_after_enthalpy())
        calculationObserver.register(E_exhaust_after_entropy())
        calculationObserver.register(E_steam_exhaust_enthalpy())
        calculationObserver.register(E_backpressure_enthalpy())
        calculationObserver.register(E_backpressure_flow())
        calculationObserver.register(E_gross_generation())
        calculationObserver.register(E_steam_extraction())
        calculationObserver.register(E_steam_extraction_select())
        calculationObserver.register(I_mechanical_efficiency())
        calculationObserver.register(I_generator_efficiency())
        calculationObserver.register(I_steam_pressure())
        calculationObserver.register(I_steam_temperature())
        calculationObserver.register(I_steam_entropy())
        calculationObserver.register(I_steam_enthalpy())
        calculationObserver.register(I_deoxidize_pressure())
        calculationObserver.register(I_deoxidize_entropy())
        calculationObserver.register(I_deoxidize_temperature())
        calculationObserver.register(I_deoxidize_enthalpy())
        calculationObserver.register(I_deoxidize_flow())
        calculationObserver.register(I_exhaust_point_pressure())
        calculationObserver.register(I_exhaust_point_temperature())
        calculationObserver.register(I_exhaust_point_entropy())
        calculationObserver.register(I_exhaust_point_enthalpy())
        calculationObserver.register(I_exhaust_point_flow())
        calculationObserver.register(I_low1_pressure())
        calculationObserver.register(I_low1_entropy())
        calculationObserver.register(I_low1_temperature())
        calculationObserver.register(I_low1_enthalpy())
        calculationObserver.register(I_low1_flow())
        calculationObserver.register(I_steam_exhaust_pressure())
        calculationObserver.register(I_steam_exhaust_entropy())
        calculationObserver.register(I_steam_exhaust_enthalpy())
        calculationObserver.register(I_steam_exhaust_enthalpy_actual())
        calculationObserver.register(I_steam_exhaust_enthalpy_steam())
        calculationObserver.register(I_steam_exhaust_enthalpy_water())
        calculationObserver.register(I_steam_exhaust_dry())
        calculationObserver.register(I_steam_exhaust_flow())
        # calculationObserver.register(I_total_power())
        # calculationObserver.register(I_calculation_error())
        calculationObserver.register(H_pressure())
        calculationObserver.register(H_enthalpy())
        calculationObserver.register(H_amount())
        calculationObserver.register(Hh1_water_temperature())
        calculationObserver.register(Hh1_water_enthalpy())
        calculationObserver.register(Hh1_top_difference())
        calculationObserver.register(Hh1_saturated_water_temperature())
        calculationObserver.register(Hh1_saturated_water_enthalpy())
        calculationObserver.register(Hh1_work_pressure())
        calculationObserver.register(Hh1_pressure_loss())
        calculationObserver.register(Hh1_extraction_pressure())
        calculationObserver.register(Hh1_extraction_enthalpy())
        calculationObserver.register(Hh1_extraction_amount())
        calculationObserver.register(D_water_enthalpy())
        calculationObserver.register(D_extraction_pressure())
        calculationObserver.register(D_extraction_enthalpy())
        calculationObserver.register(D_extraction_amount())
        calculationObserver.register(Lh1_water_temperature())
        calculationObserver.register(Lh1_water_enthalpy())
        calculationObserver.register(Lh1_saturated_water_temperature())
        calculationObserver.register(Lh1_saturated_water_enthalpy())
        calculationObserver.register(Lh1_work_pressure())
        calculationObserver.register(Lh1_extraction_pressure())
        calculationObserver.register(Lh1_extraction_enthalpy())
        calculationObserver.register(Lh1_extraction_amount())
        calculationObserver.register(C_water_temperature())
        calculationObserver.register(C_water_enthalpy())
        calculationObserver.register(C_work_pressure())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, dbmodel, form):
        val = {
            'flg': 'design',
            'e_steam_exhaust_pressure': form.get('e_steam_exhaust_pressure'),
            'e_throttle_flow': form.get('e_throttle_flow'),
            'e_backpressure_pressure': form.get('e_backpressure_pressure'),
            's_lh_grade': form.get('s_lh_grade'),
            'lh1_pressure_loss': form.get('lh1_pressure_loss'),
            'i_low2_flow': form.get('i_low2_flow'),
            'h_temperature': form.get('h_temperature'),
            'i_high2_flow': form.get('i_high2_flow'),
            'e_steam_temperature': form.get('e_steam_temperature'),
            'e_generator_efficiency': form.get('e_generator_efficiency'),
            'e_exhaust_point_temperature': form.get('e_exhaust_point_temperature'),
            'd_work_pressure': form.get('d_work_pressure'),
            'i_deoxidize_exhaust_power': form.get('i_deoxidize_exhaust_power'),
            'd_pressure_loss': form.get('d_pressure_loss'),
            'i_exhaust_lh1_power': form.get('i_exhaust_lh1_power'),
            'i_hh2_deoxidize_power': form.get('i_hh2_deoxidize_power'),
            'i_turbine_efficiency': form.get('i_turbine_efficiency'),
            'e_steam_pressure': form.get('e_steam_pressure'),
            'lh1_top_difference': form.get('lh1_top_difference'),
            'e_steam_water_loss': form.get('e_steam_water_loss'),
            'i_lh2_steam_power': form.get('i_lh2_steam_power'),
            'e_steam_flow': form.get('e_steam_flow'),
            'i_steam_flow': form.get('i_steam_flow'),
            'h_blowdown_rate': dbmodel.h_blowdown_rate,
            'd_water_temperature': form.get('d_water_temperature'),
            'e_turbine_efficiency': form.get('e_turbine_efficiency'),
            'e_exhaust_point_flow': form.get('e_exhaust_point_flow'),
            'e_mechanical_efficiency': form.get('e_mechanical_efficiency'),
            'e_exhaust_point_pressure': form.get('e_exhaust_point_pressure'),
            'e_hot_data': form.get('e_hot_data'),
            'i_high1_flow': form.get('i_high1_flow'),
            'dbresult': dbmodel}
        val['s_hh_grade'] = dbmodel.s_hh_grade
        val['s_lh_grade'] = dbmodel.s_lh_grade
        self.creatSubscriber(val)
        return val['dbresult']


class Turbine_PlanList(ExecuteStrategy):
    def specialCalculation(self, dbmodel):
        val = {
            'flg': 'design',
            'e_steam_exhaust_pressure': dbmodel.e_steam_exhaust_pressure,
            'e_throttle_flow': dbmodel.e_throttle_flow,
            'e_backpressure_pressure': dbmodel.e_backpressure_pressure,
            's_lh_grade': dbmodel.s_lh_grade,
            'lh1_pressure_loss': dbmodel.lh1_pressure_loss,
            'i_low2_flow': dbmodel.i_low2_flow,
            'h_temperature': dbmodel.h_temperature,
            'i_high2_flow': dbmodel.i_high2_flow,
            'e_steam_temperature': dbmodel.e_steam_temperature,
            'e_generator_efficiency': dbmodel.e_generator_efficiency,
            'e_exhaust_point_temperature': dbmodel.e_exhaust_point_temperature,
            'd_work_pressure': dbmodel.d_work_pressure,
            'i_deoxidize_exhaust_power': dbmodel.i_deoxidize_exhaust_power,
            'd_pressure_loss': dbmodel.d_pressure_loss,
            'i_exhaust_lh1_power': dbmodel.i_exhaust_lh1_power,
            'i_hh2_deoxidize_power': dbmodel.i_hh2_deoxidize_power,
            'i_turbine_efficiency': dbmodel.i_turbine_efficiency,
            'e_steam_pressure': dbmodel.e_steam_pressure,
            'lh1_top_difference': dbmodel.lh1_top_difference,
            'e_steam_water_loss': dbmodel.e_steam_water_loss,
            'i_lh2_steam_power': dbmodel.i_lh2_steam_power,
            'e_steam_flow': dbmodel.e_steam_flow,
            'i_steam_flow': dbmodel.i_steam_flow,
            'h_blowdown_rate': dbmodel.h_blowdown_rate,
            'd_water_temperature': dbmodel.d_water_temperature,
            'e_turbine_efficiency': dbmodel.e_turbine_efficiency,
            'e_exhaust_point_flow': dbmodel.e_exhaust_point_flow,
            'e_mechanical_efficiency': dbmodel.e_mechanical_efficiency,
            'e_exhaust_point_pressure': dbmodel.e_exhaust_point_pressure,
            'e_hot_data': dbmodel.e_hot_data,
            'i_high1_flow': dbmodel.i_high1_flow,
            'dbresult': dbmodel}
        Turbine_EXEC().creatSubscriber(val)
        return val['dbresult']
