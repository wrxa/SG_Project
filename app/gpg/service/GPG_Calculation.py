# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97

'''汽轮机部分'''
# 实现字段e_steam_entropy:特殊处理部分--7熵,的计算1
class E_steam_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_steam_entropy = seuif97.pt2s(
                (float(val['e_steam_pressure'])),
                (float(val['e_steam_temperature']))
            )

            if e_steam_entropy >= 0:
                if val['flg'] == 'design':
                    result.e_steam_entropy = e_steam_entropy
                elif val['flg'] == 'check':
                    result.e_steam_entropy_check = e_steam_entropy
        print(result)


# 实现字段e_steam_enthalpy:特殊处理部分--8焓,的计算2
class E_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_steam_enthalpy = seuif97.pt2h(
                (float(val['e_steam_pressure'])),
                (float(val['e_steam_temperature']))
            )
            if e_steam_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.e_steam_enthalpy = e_steam_enthalpy
                elif val['flg'] == 'check':
                    result.e_steam_enthalpy_check = e_steam_enthalpy
        print(result)


# 实现字段e_exhaust_point_temperature:特殊处理部分--10温度,的计算3
class E_exhaust_point_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_exhaust_point_temperature = seuif97.ps2t((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_exhaust_point_temperature >= 0:
                if val['flg'] == 'design':
                    result.e_exhaust_point_temperature = e_exhaust_point_temperature
                elif val['flg'] == 'check':
                    result.e_exhaust_point_temperature_check = e_exhaust_point_temperature
        print(result)


# 实现字段e_exhaust_point_enthalpy:特殊处理部分--12焓,的计算4
class E_exhaust_point_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_exhaust_point_enthalpy = seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_exhaust_point_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.e_exhaust_point_enthalpy = e_exhaust_point_enthalpy
                elif val['flg'] == 'check':
                    result.e_exhaust_point_enthalpy_check = e_exhaust_point_enthalpy
        print(result)


# 实现字段e_steam_exhaust_enthalpy:特殊处理部分--19焓,的计算5
class E_steam_exhaust_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_exhaust_pressure'] != '' and val['e_steam_exhaust_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_steam_exhaust_enthalpy = seuif97.ps2h((float(val['e_steam_exhaust_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_steam_exhaust_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.e_steam_exhaust_enthalpy = e_steam_exhaust_enthalpy
                elif val['flg'] == 'check':
                    result.e_steam_exhaust_enthalpy_check = e_steam_exhaust_enthalpy
        print(result)


# 实现字段e_backpressure_temperature:特殊处理部分--背压温度,的计算6
class E_backpressure_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None :
            e_backpressure_temperature = seuif97.tsat_p((float(val['e_backpressure_pressure']))*10)
            if e_backpressure_temperature >= 0:
                if val['flg'] == 'design':
                    result.e_backpressure_temperature = e_backpressure_temperature
                elif val['flg'] == 'check':
                    result.e_backpressure_temperature_check = e_backpressure_temperature
        print(result)


# 实现字段e_backpressure_enthalpy:特殊处理部分--背压焓,的计算7
class E_backpressure_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_backpressure_enthalpy = seuif97.ps2h((float(val['e_backpressure_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_backpressure_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.e_backpressure_enthalpy = e_backpressure_enthalpy
                elif val['flg'] == 'check':
                    result.e_backpressure_enthalpy_check = e_backpressure_enthalpy
        print(result)


# 实现字段i_steam_entropy:特殊处理部分--106熵,的计算8
class I_steam_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_steam_entropy = seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))
            if i_steam_entropy >= 0:
                if val['flg'] == 'design':
                    result.i_steam_entropy = i_steam_entropy
                elif val['flg'] == 'check':
                    result.i_steam_entropy_check = i_steam_entropy
        print(result)


# 实现字段i_steam_enthalpy:特殊处理部分--107焓,的计算9
class I_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_steam_enthalpy = seuif97.pt2h(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))
            if i_steam_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.i_steam_enthalpy = i_steam_enthalpy
                elif val['flg'] == 'check':
                    result.i_steam_enthalpy_check = i_steam_enthalpy
        print(result)


# 实现字段i_high1_temperature:特殊处理部分--110温度,的计算10
class I_high1_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['i_high1_pressure'] != '' and val['i_high1_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_high1_temperature = seuif97.ps2t((float(val['i_high1_pressure'])),((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))
            if i_high1_temperature >= 0:
                if val['flg'] == 'design':
                    result.i_high1_temperature = i_high1_temperature
                elif val['flg'] == 'check':
                    result.i_high1_temperature_check = i_high1_temperature
        print(result)


# 实现字段i_high1_enthalpy:特殊处理部分--111焓,的计算11
class I_high1_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['i_high1_pressure'] != '' and val['i_high1_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_high1_enthalpy = seuif97.ps2h((float(val['i_high1_pressure'])),((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))
            if i_high1_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.i_high1_enthalpy = i_high1_enthalpy
                elif val['flg'] == 'check':
                    result.i_high1_enthalpy_check = i_high1_enthalpy
        print(result)


# 实现字段i_high2_temperature:特殊处理部分--116温度,的计算12
class I_high2_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None and val['hh2_pressure_loss'] != '' and val['hh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_high2_temperature = seuif97.ps2t((((seuif97.psat_t(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))*0.1)/(1-(float(val['hh2_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))
            if i_high2_temperature >= 0:
                if val['flg'] == 'design':
                    result.i_high2_temperature = i_high2_temperature
                elif val['flg'] == 'check':
                    result.i_high2_temperature_check = i_high2_temperature
        print(result)


# 实现字段i_high2_enthalpy:特殊处理部分--117焓,的计算13
class I_high2_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None and val['hh2_pressure_loss'] != '' and val['hh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_high2_enthalpy = seuif97.ps2h((((seuif97.psat_t(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))*0.1)/(1-(float(val['hh2_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))
            if i_high2_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.i_high2_enthalpy = i_high2_enthalpy
                elif val['flg'] == 'check':
                    result.i_high2_enthalpy_check = i_high2_enthalpy
        print(result)


# 实现字段i_deoxidize_temperature:特殊处理部分--122温度,的计算14
class I_deoxidize_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_deoxidize_temperature = seuif97.ps2t((((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss']))))),((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))
            if i_deoxidize_temperature >= 0:
                if val['flg'] == 'design':
                    result.i_deoxidize_temperature = i_deoxidize_temperature
                elif val['flg'] == 'check':
                    result.i_deoxidize_temperature_check = i_deoxidize_temperature
        print(result)


# 实现字段i_deoxidize_enthalpy:特殊处理部分--123焓,的计算15
class I_deoxidize_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_deoxidize_enthalpy = seuif97.ps2h((((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss']))))),((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))
            if i_deoxidize_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.i_deoxidize_enthalpy = i_deoxidize_enthalpy
                elif val['flg'] == 'check':
                    result.i_deoxidize_enthalpy_check = i_deoxidize_enthalpy
        print(result)


# 实现字段i_low1_temperature:特殊处理部分--134温度,的计算16
class I_low1_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_low1_temperature = seuif97.ps2t((((seuif97.psat_t(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))))
            if i_low1_temperature >= 0:
                if val['flg'] == 'design':
                    result.i_low1_temperature = i_low1_temperature
                elif val['flg'] == 'check':
                    result.i_low1_temperature_check = i_low1_temperature
        print(result)


# 实现字段i_low1_enthalpy:特殊处理部分--135焓,的计算17
class I_low1_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_low1_enthalpy = seuif97.ps2h((((seuif97.psat_t(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))))
            if i_low1_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.i_low1_enthalpy = i_low1_enthalpy
                elif val['flg'] == 'check':
                    result.i_low1_enthalpy_check = i_low1_enthalpy
        print(result)


# 实现字段i_low2_temperature:特殊处理部分--140温度,的计算18
class I_low2_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None and val['lh2_pressure_loss'] != '' and val['lh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_low2_temperature = seuif97.ps2t((((seuif97.psat_t(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))*0.1)/(1-(float(val['lh2_pressure_loss']))))),(((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))))
            if i_low2_temperature >= 0:
                if val['flg'] == 'design':
                    result.i_low2_temperature = i_low2_temperature
                elif val['flg'] == 'check':
                    result.i_low2_temperature_check = i_low2_temperature
        print(result)


# 实现字段i_low2_enthalpy:特殊处理部分--141焓,的计算19
class I_low2_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None and val['lh2_pressure_loss'] != '' and val['lh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_low2_enthalpy = seuif97.ps2h((((seuif97.psat_t(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))*0.1)/(1-(float(val['lh2_pressure_loss']))))),(((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))))
            if i_low2_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.i_low2_enthalpy = i_low2_enthalpy
                elif val['flg'] == 'check':
                    result.i_low2_enthalpy_check = i_low2_enthalpy
        print(result)


# 实现字段i_steam_exhaust_enthalpy:特殊处理部分--146焓,的计算20
class I_steam_exhaust_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None and val['i_steam_exhaust_pressure'] != '' and val['i_steam_exhaust_pressure'] is not None :
            i_steam_exhaust_enthalpy = seuif97.ps2h((float(val['i_steam_exhaust_pressure'])),((((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))))
            if i_steam_exhaust_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy = i_steam_exhaust_enthalpy
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_check = i_steam_exhaust_enthalpy
        print(result)


# 实现字段i_steam_exhaust_enthalpy_steam:特殊处理部分--148饱和蒸汽焓,的计算21
class I_steam_exhaust_enthalpy_steam(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['i_steam_exhaust_pressure'] != '' and val['i_steam_exhaust_pressure'] is not None :
            i_steam_exhaust_enthalpy_steam = seuif97.HG_P((float(val['i_steam_exhaust_pressure'])))
            if i_steam_exhaust_enthalpy_steam >= 0:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy_steam = i_steam_exhaust_enthalpy_steam
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_steam_check = i_steam_exhaust_enthalpy_steam
        print(result)


# 实现字段i_steam_exhaust_enthalpy_water:特殊处理部分--149饱和水焓,的计算22
class I_steam_exhaust_enthalpy_water(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['i_steam_exhaust_pressure'] != '' and val['i_steam_exhaust_pressure'] is not None :
            i_steam_exhaust_enthalpy_water = seuif97.HL_P((float(val['i_steam_exhaust_pressure'])))
            if i_steam_exhaust_enthalpy_water >= 0:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy_water = i_steam_exhaust_enthalpy_water
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_water_check = i_steam_exhaust_enthalpy_water
        print(result)


# 实现字段h_enthalpy:特殊处理部分--28焓值,的计算23
class H_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['h_temperature'] != '' and val['h_temperature'] is not None and val['d_work_pressure'] != '' and val['d_work_pressure'] is not None :
            h_enthalpy = seuif97.pt2h((float(val['h_temperature'])),(2*(float(val['d_work_pressure']))))
            if h_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.h_enthalpy = h_enthalpy
                elif val['flg'] == 'check':
                    result.h_enthalpy_check = h_enthalpy
        print(result)


# 实现字段hh1_saturated_water_enthalpy:特殊处理部分--34饱和水焓,的计算24
class Hh1_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh1_water_temperature'] != '' and val['hh1_water_temperature'] is not None and val['hh1_top_difference'] != '' and val['hh1_top_difference'] is not None :
            hh1_saturated_water_enthalpy = seuif97.HL_T(((float(val['hh1_water_temperature']))+(float(val['hh1_top_difference']))))
            if hh1_saturated_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.hh1_saturated_water_enthalpy = hh1_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_saturated_water_enthalpy_check = hh1_saturated_water_enthalpy
        print(result)


# 实现字段hh1_work_pressure:特殊处理部分--35工作压力,的计算25
class Hh1_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh1_water_temperature'] != '' and val['hh1_water_temperature'] is not None and val['hh1_top_difference'] != '' and val['hh1_top_difference'] is not None :
            hh1_work_pressure = seuif97.psat_t(((float(val['hh1_water_temperature']))+(float(val['hh1_top_difference']))))*0.1
            if hh1_work_pressure >= 0:
                if val['flg'] == 'design':
                    result.hh1_work_pressure = hh1_work_pressure
                elif val['flg'] == 'check':
                    result.hh1_work_pressure_check = hh1_work_pressure
        print(result)


# 实现字段hh1_extraction_enthalpy:特殊处理部分--38抽汽焓,的计算26
class Hh1_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh1_water_temperature'] != '' and val['hh1_water_temperature'] is not None and val['hh1_top_difference'] != '' and val['hh1_top_difference'] is not None and val['hh1_pressure_loss'] != '' and val['hh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            hh1_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['hh1_water_temperature']))+(float(val['hh1_top_difference']))))*0.1)/(1-(float(val['hh1_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if hh1_extraction_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.hh1_extraction_enthalpy = hh1_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_extraction_enthalpy_check = hh1_extraction_enthalpy
        print(result)


# 实现字段hh2_saturated_water_enthalpy:特殊处理部分--44饱和水焓,的计算27
class Hh2_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None :
            hh2_saturated_water_enthalpy = seuif97.HL_T(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))
            if hh2_saturated_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.hh2_saturated_water_enthalpy = hh2_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh2_saturated_water_enthalpy_check = hh2_saturated_water_enthalpy
        print(result)


# 实现字段hh2_work_pressure:特殊处理部分--45工作压力,的计算28
class Hh2_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None :
            hh2_work_pressure = seuif97.psat_t(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))*0.1
            if hh2_work_pressure >= 0:
                if val['flg'] == 'design':
                    result.hh2_work_pressure = hh2_work_pressure
                elif val['flg'] == 'check':
                    result.hh2_work_pressure_check = hh2_work_pressure
        print(result)


# 实现字段hh2_extraction_enthalpy:特殊处理部分--48抽汽焓,的计算29
class Hh2_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None and val['hh2_pressure_loss'] != '' and val['hh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            hh2_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))*0.1)/(1-(float(val['hh2_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if hh2_extraction_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.hh2_extraction_enthalpy = hh2_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.hh2_extraction_enthalpy_check = hh2_extraction_enthalpy
        print(result)


# 实现字段d_water_enthalpy:特殊处理部分--51给水出口焓,的计算30
class D_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None :
            d_water_enthalpy = seuif97.HL_T((float(val['d_water_temperature'])))
            if d_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.d_water_enthalpy = d_water_enthalpy
                elif val['flg'] == 'check':
                    result.d_water_enthalpy_check = d_water_enthalpy
        print(result)


# 实现字段d_extraction_enthalpy:特殊处理部分--55抽汽焓,的计算31
class D_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            d_extraction_enthalpy = seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if d_extraction_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.d_extraction_enthalpy = d_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.d_extraction_enthalpy_check = d_extraction_enthalpy
        print(result)


# 实现字段lh1_saturated_water_enthalpy:特殊处理部分--61饱和水焓,的计算32
class Lh1_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None :
            lh1_saturated_water_enthalpy = seuif97.HL_T(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))
            if lh1_saturated_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.lh1_saturated_water_enthalpy = lh1_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.lh1_saturated_water_enthalpy_check = lh1_saturated_water_enthalpy

        print(result)


# 实现字段lh1_work_pressure:特殊处理部分--62工作压力,的计算33
class Lh1_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None :
            lh1_work_pressure = seuif97.psat_t(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))*0.1
            if lh1_work_pressure >= 0:
                if val['flg'] == 'design':
                    result.lh1_work_pressure = lh1_work_pressure
                elif val['flg'] == 'check':
                    result.lh1_work_pressure_check = lh1_work_pressure
        print(result)


# 实现字段lh1_extraction_enthalpy:特殊处理部分--65抽汽焓,的计算34
class Lh1_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            lh1_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss'])))),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if lh1_extraction_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.lh1_extraction_enthalpy = lh1_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.lh1_extraction_enthalpy_check = lh1_extraction_enthalpy
        print(result)


# 实现字段lh2_saturated_water_enthalpy:特殊处理部分--71饱和水焓,的计算35
class Lh2_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None :
            lh2_saturated_water_enthalpy = seuif97.HL_T(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))
            if lh2_saturated_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.lh2_saturated_water_enthalpy = lh2_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.lh2_saturated_water_enthalpy_check = lh2_saturated_water_enthalpy
        print(result)


# 实现字段lh2_work_pressure:特殊处理部分--72工作压力,的计算36
class Lh2_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None :
            lh2_work_pressure = seuif97.psat_t(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))*0.1
            if lh2_work_pressure >= 0:
                if val['flg'] == 'design':
                    result.lh2_work_pressure = lh2_work_pressure
                elif val['flg'] == 'check':
                    result.lh2_work_pressure_check = lh2_work_pressure
        print(result)


# 实现字段lh2_extraction_enthalpy:特殊处理部分--75抽汽焓,的计算37
class Lh2_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None and val['lh2_pressure_loss'] != '' and val['lh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            lh2_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))*0.1)/(1-(float(val['lh2_pressure_loss'])))),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if lh2_extraction_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.lh2_extraction_enthalpy = lh2_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.lh2_extraction_enthalpy_check = lh2_extraction_enthalpy
        print(result)


# 实现字段c_water_temperature:特殊处理部分--77给水出水温度,的计算39
class C_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_steam_exhaust_pressure'] != '' and val['e_steam_exhaust_pressure'] is not None :
            c_water_temperature = seuif97.tsat_p(((float(val['e_steam_exhaust_pressure']))*10))
            if c_water_temperature >= 0:
                if val['flg'] == 'design':
                    result.c_water_temperature = c_water_temperature
                elif val['flg'] == 'check':
                    result.c_water_temperature_check = c_water_temperature

        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None :
            c_water_temperature = seuif97.tsat_p(((float(val['e_backpressure_pressure']))*10))
            if c_water_temperature >= 0:
                if val['flg'] == 'design':
                    result.c_water_temperature = c_water_temperature
                elif val['flg'] == 'check':
                    result.c_water_temperature_check = c_water_temperature
        print(result)


# 实现字段c_water_enthalpy:特殊处理部分--78给水出口焓,的计算39
class C_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None :

            water_temperature = float(seuif97.tsat_p(((float(val['e_backpressure_pressure']))*10)))
            exhaust_pressure = float(val['e_backpressure_pressure'])
            c_water_enthalpy = seuif97.pt2h(exhaust_pressure,water_temperature)

            if c_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.c_water_enthalpy = c_water_enthalpy
                elif val['flg'] == 'check':
                    result.c_water_enthalpy_check = c_water_enthalpy

        if val['e_steam_exhaust_pressure'] != '' and val['e_steam_exhaust_pressure'] is not None :
            water_temperature = float(seuif97.tsat_p(((float(val['e_steam_exhaust_pressure']))*10)))
            exhaust_pressure = float(val['e_steam_exhaust_pressure'])
            c_water_enthalpy = seuif97.pt2h(exhaust_pressure,water_temperature)
            if c_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.c_water_enthalpy = c_water_enthalpy
                elif val['flg'] == 'check':
                    result.c_water_enthalpy_check = c_water_enthalpy


        print(result)


# 实现字段hh3_saturated_water_enthalpy:特殊处理部分--84饱和水焓,的计算40
class Hh3_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh3_water_temperature'] != '' and val['hh3_water_temperature'] is not None and val['hh3_top_difference'] != '' and val['hh3_top_difference'] is not None :
            hh3_saturated_water_enthalpy = seuif97.HL_T(((float(val['hh3_water_temperature']))+(float(val['hh3_top_difference']))))
            if hh3_saturated_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.hh3_saturated_water_enthalpy = hh3_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh3_saturated_water_enthalpy_check = hh3_saturated_water_enthalpy
        print(result)


# 实现字段hh3_work_pressure:特殊处理部分--85工作压力,的计算41
class Hh3_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh3_water_temperature'] != '' and val['hh3_water_temperature'] is not None and val['hh3_top_difference'] != '' and val['hh3_top_difference'] is not None :
            hh3_work_pressure = seuif97.psat_t(((float(val['hh3_water_temperature']))+(float(val['hh3_top_difference']))))*0.1
            if hh3_work_pressure >= 0:
                if val['flg'] == 'design':
                    result.hh3_work_pressure = hh3_work_pressure
                elif val['flg'] == 'check':
                    result.hh3_work_pressure_check = hh3_work_pressure
        print(result)


# 实现字段hh3_extraction_enthalpy:特殊处理部分--88抽汽焓,的计算42
class Hh3_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh3_water_temperature'] != '' and val['hh3_water_temperature'] is not None and val['hh3_top_difference'] != '' and val['hh3_top_difference'] is not None and val['hh3_pressure_loss'] != '' and val['hh3_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            hh3_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['hh3_water_temperature']))+(float(val['hh3_top_difference']))))*0.1)/(1-(float(val['hh3_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if hh3_extraction_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.hh3_extraction_enthalpy = hh3_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.hh3_extraction_enthalpy_check = hh3_extraction_enthalpy
        print(result)


# 实现字段lh3_saturated_water_enthalpy:特殊处理部分--94饱和水焓,的计算43
class Lh3_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh3_water_temperature'] != '' and val['lh3_water_temperature'] is not None and val['lh3_top_difference'] != '' and val['lh3_top_difference'] is not None :
            lh3_saturated_water_enthalpy = seuif97.HL_T(((float(val['lh3_water_temperature']))+(float(val['lh3_top_difference']))))
            if lh3_saturated_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.lh3_saturated_water_enthalpy = lh3_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.lh3_saturated_water_enthalpy_check = lh3_saturated_water_enthalpy
        print(result)


# 实现字段lh3_work_pressure:特殊处理部分--95工作压力,的计算44
class Lh3_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh3_water_temperature'] != '' and val['lh3_water_temperature'] is not None and val['lh3_top_difference'] != '' and val['lh3_top_difference'] is not None :
            lh3_work_pressure = seuif97.psat_t(((float(val['lh3_water_temperature']))+(float(val['lh3_top_difference']))))*0.1
            if lh3_work_pressure >= 0:
                if val['flg'] == 'design':
                    result.lh3_work_pressure = lh3_work_pressure
                elif val['flg'] == 'check':
                    result.lh3_work_pressure_check = lh3_work_pressure
        print(result)


# 实现字段lh3_extraction_enthalpy:特殊处理部分--98抽汽焓,的计算45
class Lh3_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['lh3_water_temperature'] != '' and val['lh3_water_temperature'] is not None and val['lh3_top_difference'] != '' and val['lh3_top_difference'] is not None and val['lh3_pressure_loss'] != '' and val['lh3_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            lh3_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['lh3_water_temperature']))+(float(val['lh3_top_difference']))))*0.1)/(1-(float(val['lh3_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if lh3_extraction_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.lh3_extraction_enthalpy = lh3_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.lh3_extraction_enthalpy_check = lh3_extraction_enthalpy
        print(result)

# 实现字段hh1_water_enthalpy:特殊处理部分--31给水出口焓,的计算25
class Hh1_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['hh1_water_temperature'] != '' and val['hh1_water_temperature'] is not None :
            hh1_water_enthalpy = seuif97.HL_T((float(val['hh1_water_temperature'])))
            if hh1_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.hh1_water_enthalpy = hh1_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_water_enthalpy_check = hh1_water_enthalpy
        print(result)


'''锅炉辅机部分'''
# 锅炉辅机部分 定期排污水量
class GPG_BoilerAuxiliaries_r_sewage_quantity(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['r_boiler_evaporation'] != '' and \
            val['r_emission_rate'] != '' and \
            val['r_boiler_evaporation'] is not None and \
            val['r_emission_rate'] is not None:

            r_sewage_quantity = float(val['r_boiler_evaporation']) * float(val['r_emission_rate']) *1000 *60 / 100
            if r_sewage_quantity >= 0:
                result.r_sewage_quantity = r_sewage_quantity

# 锅炉辅机部分 汽包压力下的饱和水焓
# L18 = HL_P(L17)
# L17: r_drum_pressure
# L18: r_drum_aturatedwater_enthalpy
class GPG_BoilerAuxiliaries_r_drum_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['r_drum_pressure'] != '' and \
            val['r_drum_pressure'] is not None:

            r_drum_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_drum_pressure']))*10)

            if r_drum_aturatedwater_enthalpy >= 0:
                result.r_drum_aturatedwater_enthalpy = r_drum_aturatedwater_enthalpy
        # 没有则不做任何操作！

# 锅炉辅机部分 扩容器压力下饱和水焓
# L20 = HL_P(L19)
# L19: r_work_pressure
# L20: r_work_aturatedwater_enthalpy
class GPG_BoilerAuxiliaries_r_work_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['r_work_pressure'] != '' and \
            val['r_work_pressure'] is not None:

            r_work_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_work_pressure']))*10)

            if r_work_aturatedwater_enthalpy >= 0:
                result.r_work_aturatedwater_enthalpy = r_work_aturatedwater_enthalpy
        # 没有则不做任何操作！

# 锅炉辅机部分 扩容器压力下蒸汽比容
# L22 = VG_P(F20)
class GPG_BoilerAuxiliaries_r_work_steam_special_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['r_work_pressure'] != '' and \
            val['r_work_pressure'] is not None:

            r_work_steam_special_volume = seuif97.VG_P(
                (float(val['r_work_pressure']))*10)

            if r_work_steam_special_volume >= 0:
                result.r_work_steam_special_volume = r_work_steam_special_volume

# 锅炉辅机部分 扩容器压力下汽化潜热
# L21 = HG_P(L19)-L20 = HG_P(L19)- HL_P(L19)
# L19: r_work_pressure
# L20: r_work_aturatedwater_enthalpy
# L21: r_work_latentheat_vaporization
class GPG_BoilerAuxiliaries_r_work_latentheat_vaporization(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['r_work_pressure'] != '' and \
            val['r_work_pressure'] is not None:

            r_work_latentheat_vaporization = seuif97.HG_P(
                (float(val['r_work_pressure']))*10) - seuif97.HL_P(
                (float(val['r_work_pressure']))*10)

            if r_work_latentheat_vaporization >= 0:
                result.r_work_latentheat_vaporization = r_work_latentheat_vaporization
        # 没有则不做任何操作！

# 锅炉辅机部分 排污水汽化量
class GPG_BoilerAuxiliaries_r_vaporization_capacity(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['r_drum_pressure'] != '' and \
            val['r_drum_pressure'] is not None and \
            val['r_work_pressure'] != '' and \
            val['r_work_pressure'] is not None:

            r_drum_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_drum_pressure']))*10)

            r_work_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_work_pressure']))*10)

            r_work_latentheat_vaporization = seuif97.HG_P(
                (float(val['r_work_pressure']))*10) - seuif97.HL_P(
                (float(val['r_work_pressure']))*10)
            
            if r_work_latentheat_vaporization > 0:
                r_vaporization_capacity = (r_drum_aturatedwater_enthalpy * 0.98 - r_work_aturatedwater_enthalpy)/(0.97 * r_work_latentheat_vaporization)
                if r_vaporization_capacity >= 0:
                    result.r_vaporization_capacity = r_vaporization_capacity

# 锅炉辅机部分 排污扩容汽容积
class GPG_BoilerAuxiliaries_r_steam_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['r_drum_pressure'] != '' and \
            val['r_drum_pressure'] is not None and \
            val['r_work_pressure'] != '' and \
            val['r_work_pressure'] is not None and\
            val['r_boiler_evaporation'] != '' and \
            val['r_emission_rate'] != '' and \
            val['r_boiler_evaporation'] is not None and \
            val['r_emission_rate'] is not None and \
            val['r_ultimate_strength'] != '' and \
            val['r_ultimate_strength'] is not None and \
            val['r_affluence_coefficient'] != '' and \
            val['r_affluence_coefficient'] is not None:

            r_sewage_quantity = float(val['r_boiler_evaporation']) * float(val['r_emission_rate']) *1000 *60 / 100

            r_work_steam_special_volume = seuif97.VG_P(
                (float(val['r_work_pressure']))*10)

            r_drum_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_drum_pressure']))*10)

            r_work_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_work_pressure']))*10)

            r_work_latentheat_vaporization = seuif97.HG_P(
                (float(val['r_work_pressure']))*10) - seuif97.HL_P(
                (float(val['r_work_pressure']))*10)

            r_ultimate_strength = float(val['r_ultimate_strength'])

            r_affluence_coefficient = float(val['r_affluence_coefficient'])

            if r_work_latentheat_vaporization > 0 and r_ultimate_strength > 0:
                r_steam_volume = (r_sewage_quantity * r_work_steam_special_volume * ((r_drum_aturatedwater_enthalpy * 0.98 - r_work_aturatedwater_enthalpy)/(0.97 * r_work_latentheat_vaporization))) / r_ultimate_strength * r_affluence_coefficient

                if r_steam_volume >= 0:
                    result.r_steam_volume = r_steam_volume

# 锅炉辅机部分 排污扩容容积
class GPG_BoilerAuxiliaries_r_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['r_drum_pressure'] != '' and \
            val['r_drum_pressure'] is not None and \
            val['r_work_pressure'] != '' and \
            val['r_work_pressure'] is not None and\
            val['r_boiler_evaporation'] != '' and \
            val['r_emission_rate'] != '' and \
            val['r_boiler_evaporation'] is not None and \
            val['r_emission_rate'] is not None and \
            val['r_ultimate_strength'] != '' and \
            val['r_ultimate_strength'] is not None and \
            val['r_affluence_coefficient'] != '' and \
            val['r_affluence_coefficient'] is not None:

            r_sewage_quantity = float(val['r_boiler_evaporation']) * float(val['r_emission_rate']) *1000 *60 / 100

            r_work_steam_special_volume = seuif97.VG_P(
                (float(val['r_work_pressure']))*10)

            r_drum_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_drum_pressure']))*10)

            r_work_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_work_pressure']))*10)

            r_work_latentheat_vaporization = seuif97.HG_P(
                (float(val['r_work_pressure']))*10) - seuif97.HL_P(
                (float(val['r_work_pressure']))*10)

            r_ultimate_strength = float(val['r_ultimate_strength'])

            r_affluence_coefficient = float(val['r_affluence_coefficient'])

            if r_work_latentheat_vaporization > 0 and r_ultimate_strength > 0:
                r_volume = 1.25 * ((r_sewage_quantity * r_work_steam_special_volume * ((r_drum_aturatedwater_enthalpy * 0.98 - r_work_aturatedwater_enthalpy)/(0.97 * r_work_latentheat_vaporization))) / r_ultimate_strength * r_affluence_coefficient)

                if r_volume >= 0:
                    result.r_volume = r_volume




# 锅炉辅机部分 汽包压力下的饱和水焓
# L29 = HL_P(L28)
# L28: c_drum_pressure
# L29: c_drum_aturatedwater_enthalpy
class GPG_BoilerAuxiliaries_c_drum_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['c_drum_pressure'] != '' and \
            val['c_drum_pressure'] is not None:

            c_drum_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['c_drum_pressure']))*10)

            if c_drum_aturatedwater_enthalpy >= 0:
                result.c_drum_aturatedwater_enthalpy = c_drum_aturatedwater_enthalpy
        # 没有则不做任何操作！

        # 锅炉辅机部分 扩容器压力下饱和水焓
        # L31 = HL_P(L30)
        # L30: c_work_pressure
        # L31: c_work_aturatedwater_enthalpy
class GPG_BoilerAuxiliaries_c_work_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['c_work_pressure'] != '' and \
            val['c_work_pressure'] is not None:

            c_work_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['c_work_pressure']))*10)

            if c_work_aturatedwater_enthalpy >= 0:
                result.c_work_aturatedwater_enthalpy = c_work_aturatedwater_enthalpy
        # 没有则不做任何操作！

        # 锅炉辅机部分 扩容器压力下蒸汽比容
        # L32 = VG_P(L30)
        # L30: c_work_pressure
        # L32: c_work_steam_pecificvolume
class GPG_BoilerAuxiliaries_c_work_steam_pecificvolume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['c_work_pressure'] != '' and \
            val['c_work_pressure'] is not None:

            c_work_steam_pecificvolume = seuif97.VG_P(
                (float(val['c_work_pressure'])))

            if c_work_steam_pecificvolume >= 0:
                result.c_work_steam_pecificvolume = c_work_steam_pecificvolume
        # 没有则不做任何操作！

        # 锅炉辅机部分 扩容器压力下汽化潜热
        # L33 = HG_P(L30)-L31 = HG_P(L30)- HL_P(L30)
        # L30: c_work_pressure
        # L33: c_work_latentheat_vaporization
class GPG_BoilerAuxiliaries_c_work_latentheat_vaporization(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['c_work_pressure'] != '' and \
            val['c_work_pressure'] is not None:

            c_work_latentheat_vaporization = seuif97.HG_P(
                (float(val['c_work_pressure']))*10) - seuif97.HL_P(
                (float(val['c_work_pressure']))*10)

            if c_work_latentheat_vaporization >= 0:
                result.c_work_latentheat_vaporization = c_work_latentheat_vaporization
        # 没有则不做任何操作！

        # 锅炉辅机部分 当地大气压对应下的密度
        # L81 = 1/VL_P(L80/1000000)
        # L80: s_local_atmosphere
        # L81: s_local_atmosphere_density
class GPG_BoilerAuxiliaries_s_local_atmosphere_density(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['s_local_atmosphere'] != '' and \
            val['s_local_atmosphere'] is not None:

            s_local_atmosphere_density = 1/seuif97.VL_P(
                #(float(val['s_local_atmosphere'])/1000000 * 10))
                (float(val['s_local_atmosphere'])/100000))

            if s_local_atmosphere_density >= 0:
                result.s_local_atmosphere_density = s_local_atmosphere_density
        # 没有则不做任何操作！


# 锅炉辅机部分 新蒸汽焓值
class GPG_BoilerAuxiliaries_new_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['new_steam_temperature'] != '' and \
            val['new_steam_pressure'] != '' and \
            val['new_steam_temperature'] is not None and \
            val['new_steam_pressure'] is not None:

            new_steam_enthalpy = seuif97.pt2hz(
                float(val['new_steam_pressure']), float(val['new_steam_temperature']))

            if new_steam_enthalpy >= 0:
                result.new_steam_enthalpy = new_steam_enthalpy

# 锅炉辅机部分 减温水压力
class GPG_BoilerAuxiliaries_desuperheater_water_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['desuperheater_steam_pressure'] != '' and \
            val['desuperheater_steam_pressure'] is not None:

            desuperheater_water_pressure = float(val['desuperheater_steam_pressure']) + 1.47

            if desuperheater_water_pressure >= 0:
                result.desuperheater_water_pressure = desuperheater_water_pressure

# 锅炉辅机部分 减温水焓
class GPG_BoilerAuxiliaries_desuperheater_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['desuperheater_steam_pressure'] != '' and \
            val['desuperheater_water_temperature'] != '' and \
            val['desuperheater_steam_pressure'] is not None and \
            val['desuperheater_water_temperature'] is not None:

            desuperheater_water_enthalpy = seuif97.pt2hw(
                (float(val['desuperheater_steam_pressure'])+1.47), float(val['desuperheater_water_temperature']))

            if desuperheater_water_enthalpy >= 0:
                result.desuperheater_water_enthalpy = desuperheater_water_enthalpy

# 锅炉辅机部分 减温水流量
class GPG_BoilerAuxiliaries_desuperheater_water_flux(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['new_steam_temperature'] != '' and \
            val['new_steam_pressure'] != '' and \
            val['new_steam_flux'] != '' and \
            val['desuperheater_water_temperature'] != '' and \
            val['desuperheater_steam_pressure'] != '' and \
            val['desuperheater_steam_temperature'] != '' and \
            val['no_vaporized_percent'] != '' and \
            val['new_steam_temperature'] is not None and \
            val['new_steam_pressure'] is not None and \
            val['new_steam_flux'] is not None and \
            val['desuperheater_water_temperature'] is not None and \
            val['desuperheater_steam_pressure'] is not None and \
            val['desuperheater_steam_temperature'] is not None and \
            val['no_vaporized_percent'] is not None:

            new_steam_enthalpy = seuif97.pt2hz(
                float(val['new_steam_pressure']), float(val['new_steam_temperature']))

            desuperheater_steam_enthalpy = seuif97.pt2hz(
                float(val['desuperheater_steam_pressure']), float(val['desuperheater_steam_temperature']))

            desuperheater_water_enthalpy = seuif97.pt2hw(
                (float(val['desuperheater_steam_pressure'])+1.47), float(val['desuperheater_water_temperature']))

            saturation_water_enthalpy = seuif97.HL_P(
                (float(val['desuperheater_steam_pressure'])*10))

            desuperheater_water_flux = (
                new_steam_enthalpy - desuperheater_steam_enthalpy
            ) * float(val['new_steam_flux']) / (
                desuperheater_steam_enthalpy - desuperheater_water_enthalpy +
                float(val['no_vaporized_percent']) *
                (saturation_water_enthalpy - desuperheater_steam_enthalpy))

            if desuperheater_water_flux >= 0:
                result.desuperheater_water_flux = desuperheater_water_flux

# 锅炉辅机部分 减温后蒸汽焓
class GPG_BoilerAuxiliaries_desuperheater_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['desuperheater_steam_pressure'] != '' and \
            val['desuperheater_steam_temperature'] != '' and \
            val['desuperheater_steam_pressure'] is not None and \
            val['desuperheater_steam_temperature'] is not None:

            desuperheater_steam_enthalpy = seuif97.pt2hz(
                float(val['desuperheater_steam_pressure']), float(val['desuperheater_steam_temperature']))

            if desuperheater_steam_enthalpy >= 0:
                result.desuperheater_steam_enthalpy = desuperheater_steam_enthalpy

# 锅炉辅机部分 饱和水焓值
class GPG_BoilerAuxiliaries_saturation_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['desuperheater_steam_pressure'] != '' and \
            val['desuperheater_steam_pressure'] is not None:

            saturation_water_enthalpy = seuif97.HL_P(
                (float(val['desuperheater_steam_pressure'])*10))

            if saturation_water_enthalpy >= 0:
                result.saturation_water_enthalpy = saturation_water_enthalpy

# 锅炉辅机部分 减温减压流量
class GPG_BoilerAuxiliaries_de_press_temp_device_flux(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['new_steam_temperature'] != '' and \
            val['new_steam_pressure'] != '' and \
            val['new_steam_flux'] != '' and \
            val['desuperheater_water_temperature'] != '' and \
            val['desuperheater_steam_pressure'] != '' and \
            val['desuperheater_steam_temperature'] != '' and \
            val['no_vaporized_percent'] != '' and \
            val['new_steam_temperature'] is not None and \
            val['new_steam_pressure'] is not None and \
            val['new_steam_flux'] is not None and \
            val['desuperheater_water_temperature'] is not None and \
            val['desuperheater_steam_pressure'] is not None and \
            val['desuperheater_steam_temperature'] is not None and \
            val['no_vaporized_percent'] is not None:

            new_steam_enthalpy = seuif97.pt2hz(
                float(val['new_steam_pressure']), float(val['new_steam_temperature']))

            desuperheater_steam_enthalpy = seuif97.pt2hz(
                float(val['desuperheater_steam_pressure']), float(val['desuperheater_steam_temperature']))

            desuperheater_water_enthalpy = seuif97.pt2hw(
                (float(val['desuperheater_steam_pressure'])+1.47), float(val['desuperheater_water_temperature']))

            saturation_water_enthalpy = seuif97.HL_P(
                (float(val['desuperheater_steam_pressure'])*10))

            desuperheater_water_flux = (
                new_steam_enthalpy - desuperheater_steam_enthalpy
                ) * float(val['new_steam_flux']) / (
                desuperheater_steam_enthalpy - desuperheater_water_enthalpy +
                float(val['no_vaporized_percent']) *
                (saturation_water_enthalpy - desuperheater_steam_enthalpy))

            de_press_temp_device_flux = float(val['new_steam_flux']) + desuperheater_water_flux*(1 - float(val['no_vaporized_percent']))

            if de_press_temp_device_flux >= 0:
                result.de_press_temp_device_flux = de_press_temp_device_flux

# 锅炉辅机部分 充热压力下的饱和水焓
class GPG_BoilerAuxiliaries_charging_saturation_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['charging_pressure'] != '' and \
            val['charging_pressure'] is not None:

            charging_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['charging_pressure'])*10))

            if charging_saturation_water_enthalpy >= 0:
                result.charging_saturation_water_enthalpy = charging_saturation_water_enthalpy

# 锅炉辅机部分 放热压力下的饱和水焓
class GPG_BoilerAuxiliaries_exothermic_saturation_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['exothermic_pressure'] is not None:

            exothermic_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['exothermic_pressure'])*10))

            if exothermic_saturation_water_enthalpy >= 0:
                result.exothermic_saturation_water_enthalpy = exothermic_saturation_water_enthalpy

# 锅炉辅机部分 充热压力下的饱和汽焓
class GPG_BoilerAuxiliaries_charging_saturation_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['charging_pressure'] != '' and \
            val['charging_pressure'] is not None:

            charging_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['charging_pressure'])*10))

            if charging_saturation_steam_enthalpy >= 0:
                result.charging_saturation_steam_enthalpy = charging_saturation_steam_enthalpy

# 锅炉辅机部分 放热压力下的饱和汽焓
class GPG_BoilerAuxiliaries_exothermic_saturation_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['exothermic_pressure'] is not None:

            exothermic_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['exothermic_pressure'])*10))

            if exothermic_saturation_steam_enthalpy >= 0:
                result.exothermic_saturation_steam_enthalpy = exothermic_saturation_steam_enthalpy

# 锅炉辅机部分 P2压力下产生蒸汽量
class GPG_BoilerAuxiliaries_p2_steam_amount(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['charging_pressure'] != '' and \
            val['exothermic_pressure'] is not None and \
            val['charging_pressure'] is not None:

            charging_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['charging_pressure'])*10))

            charging_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['charging_pressure'])*10))

            exothermic_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['exothermic_pressure'])*10))

            exothermic_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['exothermic_pressure'])*10))

            p2_steam_amount = (charging_saturation_water_enthalpy -
                               exothermic_saturation_water_enthalpy) / (
                                   (charging_saturation_steam_enthalpy   +
                                    exothermic_saturation_steam_enthalpy) / 2 -
                                   exothermic_saturation_water_enthalpy)

            if p2_steam_amount >= 0:
                result.p2_steam_amount = p2_steam_amount

# 锅炉辅机部分 充热压力下的饱和水比容
class GPG_BoilerAuxiliaries_charging_water_specific_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['charging_pressure'] != '' and \
            val['charging_pressure'] is not None:

            charging_water_specific_volume = seuif97.VL_P(
                (float(val['charging_pressure'])*10))

            if charging_water_specific_volume >= 0:
                result.charging_water_specific_volume = charging_water_specific_volume

# 锅炉辅机部分 单位水容积蓄热量
class GPG_BoilerAuxiliaries_unit_water_heat_amount(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['charging_pressure'] != '' and \
            val['exothermic_pressure'] is not None and \
            val['charging_pressure'] is not None:

            charging_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['charging_pressure'])*10))

            charging_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['charging_pressure'])*10))

            exothermic_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['exothermic_pressure'])*10))

            exothermic_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['exothermic_pressure'])*10))

            charging_water_specific_volume = seuif97.VL_P(
                (float(val['charging_pressure'])*10))

            p2_steam_amount = (
                charging_saturation_water_enthalpy - exothermic_saturation_water_enthalpy) / (
                (charging_saturation_steam_enthalpy + exothermic_saturation_steam_enthalpy) / 2
                - exothermic_saturation_water_enthalpy)

            unit_water_heat_amount = p2_steam_amount/charging_water_specific_volume

            if unit_water_heat_amount >= 0:
                result.unit_water_heat_amount = unit_water_heat_amount

# 锅炉辅机部分 蓄热器容积
class GPG_BoilerAuxiliaries_regenerarot_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['charging_pressure'] != '' and \
            val['regenerarot_efficiency'] != '' and \
            val['water_fill_coefficient'] != '' and \
            val['regenerarot_heat_amount'] != '' and \
            val['exothermic_pressure'] is not None and \
            val['charging_pressure'] is not None and \
            val['regenerarot_efficiency'] is not None and \
            val['water_fill_coefficient'] is not None and \
            val['regenerarot_heat_amount'] is not None:

            charging_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['charging_pressure'])*10))

            charging_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['charging_pressure'])*10))

            exothermic_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['exothermic_pressure'])*10))

            exothermic_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['exothermic_pressure'])*10))

            charging_water_specific_volume = seuif97.VL_P(
                (float(val['charging_pressure'])*10))

            p2_steam_amount = (
                charging_saturation_water_enthalpy - exothermic_saturation_water_enthalpy) / (
                (charging_saturation_steam_enthalpy + exothermic_saturation_steam_enthalpy) / 2
                - exothermic_saturation_water_enthalpy)

            unit_water_heat_amount = p2_steam_amount/charging_water_specific_volume

            regenerarot_volume = (float(val['regenerarot_heat_amount']) * 1000) / (unit_water_heat_amount * float(val['regenerarot_efficiency']) * float(val['water_fill_coefficient']))

            if regenerarot_volume >= 0:
                result.regenerarot_volume = regenerarot_volume

# 锅炉辅机部分 蓄热器上部蒸汽容积
class GPG_BoilerAuxiliaries_regenerarot_top_steam_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['charging_pressure'] != '' and \
            val['regenerarot_efficiency'] != '' and \
            val['water_fill_coefficient'] != '' and \
            val['regenerarot_heat_amount'] != '' and \
            val['exothermic_pressure'] is not None and \
            val['charging_pressure'] is not None and \
            val['regenerarot_efficiency'] is not None and \
            val['water_fill_coefficient'] is not None and \
            val['regenerarot_heat_amount'] is not None:

            charging_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['charging_pressure'])*10))

            charging_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['charging_pressure'])*10))

            exothermic_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['exothermic_pressure'])*10))

            exothermic_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['exothermic_pressure'])*10))

            charging_water_specific_volume = seuif97.VL_P(
                (float(val['charging_pressure'])*10))

            p2_steam_amount = (
                charging_saturation_water_enthalpy - exothermic_saturation_water_enthalpy) / (
                (charging_saturation_steam_enthalpy + exothermic_saturation_steam_enthalpy) / 2
                - exothermic_saturation_water_enthalpy)

            unit_water_heat_amount = p2_steam_amount/charging_water_specific_volume

            regenerarot_top_steam_volume = (1 - float(val['water_fill_coefficient'])) * (
                (float(val['regenerarot_heat_amount']) * 1000) / (unit_water_heat_amount * float(val['regenerarot_efficiency']) * float(val['water_fill_coefficient'])))

            if regenerarot_top_steam_volume >= 0:
                result.regenerarot_top_steam_volume = regenerarot_top_steam_volume

# 锅炉辅机部分 蓄热器最大放汽量
class GPG_BoilerAuxiliaries_regenerarot_max_bleed(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['boiler_max_load'] != '' and \
            val['boiler_average_load'] != '' and \
            val['boiler_max_load'] is not None and \
            val['boiler_average_load'] is not None:

            regenerarot_max_bleed = float(val['boiler_max_load']) - float(val['boiler_average_load'])

            if regenerarot_max_bleed >= 0:
                result.regenerarot_max_bleed = regenerarot_max_bleed

# 锅炉辅机部分 质量蒸发强度
class GPG_BoilerAuxiliaries_evaporation_capacity(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['charging_pressure'] != '' and \
            val['regenerarot_efficiency'] != '' and \
            val['water_fill_coefficient'] != '' and \
            val['regenerarot_heat_amount'] != '' and \
            val['boiler_max_load'] != '' and \
            val['boiler_average_load'] != '' and \
            val['exothermic_pressure'] is not None and \
            val['charging_pressure'] is not None and \
            val['regenerarot_efficiency'] is not None and \
            val['water_fill_coefficient'] is not None and \
            val['regenerarot_heat_amount'] is not None and \
            val['boiler_max_load'] is not None and \
            val['boiler_average_load'] is not None:

            charging_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['charging_pressure'])*10))

            charging_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['charging_pressure'])*10))

            exothermic_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['exothermic_pressure'])*10))

            exothermic_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['exothermic_pressure'])*10))

            charging_water_specific_volume = seuif97.VL_P(
                (float(val['charging_pressure'])*10))

            p2_steam_amount = (
                charging_saturation_water_enthalpy - exothermic_saturation_water_enthalpy) / (
                (charging_saturation_steam_enthalpy + exothermic_saturation_steam_enthalpy) / 2
                - exothermic_saturation_water_enthalpy)

            unit_water_heat_amount = p2_steam_amount/charging_water_specific_volume

            regenerarot_top_steam_volume = (1 - float(val['water_fill_coefficient'])) * (
                (float(val['regenerarot_heat_amount']) * 1000) / (unit_water_heat_amount * float(val['regenerarot_efficiency']) * float(val['water_fill_coefficient'])))

            regenerarot_max_bleed = float(val['boiler_max_load']) - float(val['boiler_average_load'])

            evaporation_capacity = regenerarot_max_bleed / regenerarot_top_steam_volume
            if evaporation_capacity >= 0:
                result.evaporation_capacity = evaporation_capacity

# 锅炉辅机部分 充热状态下的体积
class GPG_BoilerAuxiliaries_charging_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['charging_pressure'] != '' and \
            val['regenerarot_heat_amount'] != '' and \
            val['exothermic_pressure'] is not None and \
            val['charging_pressure'] is not None and \
            val['regenerarot_heat_amount'] is not None:

            charging_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['charging_pressure'])*10))

            charging_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['charging_pressure'])*10))

            exothermic_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['exothermic_pressure'])*10))

            exothermic_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['exothermic_pressure'])*10))

            charging_water_specific_volume = seuif97.VL_P(
                (float(val['charging_pressure'])*10))

            p2_steam_amount = (
                charging_saturation_water_enthalpy - exothermic_saturation_water_enthalpy) / (
                (charging_saturation_steam_enthalpy + exothermic_saturation_steam_enthalpy) / 2
                - exothermic_saturation_water_enthalpy)

            unit_water_heat_amount = p2_steam_amount/charging_water_specific_volume

            charging_volume = float(val['regenerarot_heat_amount'])*1000 / unit_water_heat_amount
            if charging_volume >= 0:
                result.charging_volume = charging_volume

# 锅炉辅机部分 放热压力下的饱和水比容
class GPG_BoilerAuxiliaries_exothermic_water_specific_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['exothermic_pressure'] is not None:

            exothermic_water_specific_volume = seuif97.VL_P(
                (float(val['exothermic_pressure'])) *10)

            if exothermic_water_specific_volume >= 0:
                result.exothermic_water_specific_volume = exothermic_water_specific_volume

# 锅炉辅机部分 放热完了水的体积
class GPG_BoilerAuxiliaries_exothermic_water_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']
        if val['exothermic_pressure'] != '' and \
            val['charging_pressure'] != '' and \
            val['regenerarot_heat_amount'] != '' and \
            val['exothermic_pressure'] is not None and \
            val['charging_pressure'] is not None and \
            val['regenerarot_heat_amount'] is not None:

            charging_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['charging_pressure'])*10))

            charging_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['charging_pressure'])*10))

            exothermic_saturation_water_enthalpy = seuif97.HL_P(
                (float(val['exothermic_pressure'])*10))

            exothermic_saturation_steam_enthalpy = seuif97.HG_P(
                (float(val['exothermic_pressure'])*10))

            charging_water_specific_volume = seuif97.VL_P(
                (float(val['charging_pressure'])*10))
            
            exothermic_water_specific_volume = seuif97.VL_P(
                (float(val['exothermic_pressure'])*10))

            p2_steam_amount = (
                charging_saturation_water_enthalpy - exothermic_saturation_water_enthalpy) / (
                (charging_saturation_steam_enthalpy + exothermic_saturation_steam_enthalpy) / 2
                - exothermic_saturation_water_enthalpy)

            unit_water_heat_amount = p2_steam_amount/charging_water_specific_volume

            charging_volume = float(val['regenerarot_heat_amount'])*1000 / unit_water_heat_amount

            exothermic_water_volume = (
                charging_volume / charging_water_specific_volume - float(val['regenerarot_heat_amount']) *1000
                ) * exothermic_water_specific_volume

            if exothermic_water_volume >= 0:
                result.exothermic_water_volume = exothermic_water_volume



'''汽水管道部分'''
# 汽水管道部分--主蒸汽分管介质比容
# N11 = V_PT(N3,N4)
# N3: main_steam_design_pressure_c
# N4: main_steam_design_temperature_c
# N11: main_steam_meida_specific_volume_c
class GPG_SteamWaterPipe_main_steam_meida_specific_volume_c(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['main_steam_design_pressure_c'] != '' and \
            val['main_steam_design_temperature_c'] != '' and \
            val['main_steam_design_pressure_c'] is not None and \
            val['main_steam_design_temperature_c'] is not None:

            main_steam_meida_specific_volume_c = seuif97.pt2v(
                float(val['main_steam_design_pressure_c']),
                float(val['main_steam_design_temperature_c'])
            )

            if main_steam_meida_specific_volume_c >= 0:
                result.main_steam_meida_specific_volume_c = main_steam_meida_specific_volume_c

        # 没有则不做任何操作！

'''汽机辅机系统部分'''
# 汽机辅机系统部分--凝汽器计算 饱和温度
# F47 = T_P(F44/1000)Kpa
# F44: condenser_pressure Kpa
# F47: saturation_temperature
class GPG_TurbineAuxiliary_saturation_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['condenser_pressure'] != '' and \
            val['condenser_pressure'] is not None:

            # 1 bar = 100 Kpa
            saturation_temperature = seuif97.tsat_p(
                float(val['condenser_pressure']) / 100
            )

            if saturation_temperature >= 0:
                result.saturation_temperature = saturation_temperature

        # 没有则不做任何操作！


        # 汽机辅机系统部分--凝结水焓
        # F50=H_PT(F44/1000,F49) Kpa
        # F44: condenser_pressure Kpa
        # F49: condensate_water_temperature=F47-F48
        # F48:supercooling_degree
        # F47:=T_P(F44/1000)
        # F44: condenser_pressure Kpa
        # F50: condensate_water_enthalpy

        # final:F50=H_PT(F44/1000,(T_P(F44/1000)-F48))
class GPG_TurbineAuxiliary_condensate_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbResult']

        if val['condenser_pressure'] != '' and \
            val['supercooling_degree'] != '' and \
            val['condenser_pressure'] is not None and \
            val['supercooling_degree'] is not None:


            condensate_water_enthalpy = seuif97.pt2h(
                float(val['condenser_pressure']) / 1000,
                seuif97.tsat_p(float(val['condenser_pressure'])/100) - float(val['supercooling_degree'])
            )
            if condensate_water_enthalpy >= 0:
                result.condensate_water_enthalpy = condensate_water_enthalpy

        # 没有则不做任何操作！

'''原则性热力系统锅炉部分'''
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
                float(val['superheated_steam_outlet_pressure'])*10
            )

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
                float(val['superheated_steam_outlet_pressure'])*10
            )

            if saturation_water_enthalpy >= 0:
                result.saturation_water_enthalpy = saturation_water_enthalpy

        # 没有则不做任何操作！

if __name__ == "__main__":
    print("GPG_Calculation.py")