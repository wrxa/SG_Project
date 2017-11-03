# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97
# G20:f_steam_pressure  # G21:f_steam_temperature
# G22:f_steam_enthalpy  # G24:f_saturated_water_enthalpy
# G25:f_water_temperature  # G26:f_water_enthalpy
# G44:a_temperature  # G45:a_saturation_pressure
# G22=H_PT(G20,G21)
# G24=HL_P(G20*1.1)
# G26=H_PT(G20*1.1,G25)
# G45=1000*P_T(G44)


# G22=H_PT(G20,G21)
class FSteamEnthalpy(FieldCalculation):
    def notify(self, val):
        # 判断f_steam_pressure是否有变化
        result = val['dbresult']
        newf_steam_pressure = ''
        newf_steam_temperature = ''
        oldf_steam_pressure = ''
        oldf_steam_temperature = ''
        # 得到字段：G20:f_steam_pressure、G21:f_steam_temperature
        if val['f_steam_pressure'] != '' and val['f_steam_temperature'] != '':
            newf_steam_pressure = float(val['f_steam_pressure'])
            newf_steam_temperature = float(val['f_steam_temperature'])
        if val['flg'] == 'design' and result.f_steam_pressure_design \
                is not None and result.f_steam_temperature_design is not None:
            oldf_steam_pressure = float(result.f_steam_pressure_design)
            oldf_steam_temperature = float(result.f_steam_temperature_design)
            
        elif val['flg'] == 'check' and result.f_steam_pressure_check \
                is not None and result.f_steam_temperature_check is not None:
            oldf_steam_pressure = float(result.f_steam_pressure_check)
            oldf_steam_temperature = float(result.f_steam_temperature_check)
     
        if oldf_steam_pressure != '' and newf_steam_pressure != '' and \
           abs(oldf_steam_pressure - newf_steam_pressure) > 0.00001 \
           or \
           oldf_steam_temperature != '' and newf_steam_temperature != '' and \
           abs(oldf_steam_temperature - newf_steam_temperature) > 0.00001:
            # G22=H_PT(G20,G21) 并更新
            f_steam_enthalpy = \
                seuif97.pt2h(newf_steam_pressure, newf_steam_temperature)
            if f_steam_enthalpy > 0:
                if val['flg'] == 'design':
                    result.f_steam_enthalpy_design = \
                      f_steam_enthalpy
                elif val['flg'] == 'check':
                    result.f_steam_enthalpy_check = \
                      f_steam_enthalpy
        # 没有则不做任何操作！
        print(result)


# G24=HL_P(G20*1.1)
class FSaturatedWaterEnthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        newf_steam_pressure = ''
        oldf_steam_pressure = ''
        # 得到字段：f_steam_pressure
        if val['f_steam_pressure'] != '':
            newf_steam_pressure = float(val['f_steam_pressure'])
        if val['flg'] == 'design' and \
                result.f_steam_pressure_design is not None:
            oldf_steam_pressure = float(result.f_steam_pressure_design)
        elif val['flg'] == 'check' and \
                result.f_steam_pressure_design is not None:
            oldf_steam_pressure = float(result.f_steam_pressure_check)
        # 判断f_steam_pressure是否有变化
        if oldf_steam_pressure != '' and \
           newf_steam_pressure != '' and \
           abs(oldf_steam_pressure - newf_steam_pressure) \
           > 0.00001:
            # G24=HL_P(G20*1.1)G24:f_saturated_water_enthalpy
            f_saturated_water_enthalpy = \
                seuif97.h_p(newf_steam_pressure)
            if f_saturated_water_enthalpy >= 0:
                if val['flg'] == 'design':
                    result.f_saturated_water_enthalpy_design = \
                      f_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.f_saturated_water_enthalpy_check = \
                      f_saturated_water_enthalpy
            print("计算失败!")
        # 没有则不做任何操作!
        print(result)


# G26=H_PT(G20*1.1,G25)G26:f_water_enthalpy
class FWaterEnthalpy(FieldCalculation):
    def notify(self, val):
        # 判断f_steam_pressure是否有变化
        result = val['dbresult']
        # 得到字段：G20:f_steam_pressure、G25:f_water_temperature
        newf_steam_pressure = ''
        newf_water_temperature = ''
        oldf_steam_pressure = ''
        oldf_water_temperature = ''
        if val['f_steam_pressure'] != '' and val['f_water_temperature'] != '':
            newf_steam_pressure = float(val['f_steam_pressure'])
            newf_water_temperature = float(val['f_water_temperature'])
        if val['flg'] == 'design' and result.f_steam_pressure_design is not None and result.f_water_temperature_design is not None:
            oldf_steam_pressure = float(result.f_steam_pressure_design)
            oldf_water_temperature = float(result.f_water_temperature_design)
        elif val['flg'] == 'check' and result.f_steam_pressure_check is not None and result.f_water_temperature_check is not None:
            oldf_steam_pressure = float(result.f_steam_pressure_check)
            oldf_water_temperature = float(result.f_water_temperature_check)
       
        if oldf_steam_pressure != '' and \
           newf_steam_pressure != '' and \
           abs(oldf_steam_pressure - newf_steam_pressure) \
           > 0.00001 \
           or \
           oldf_water_temperature != '' and \
           newf_water_temperature != '' and \
           abs(oldf_water_temperature - newf_water_temperature) \
           > 0.00001:
            # G26=H_PT(G20*1.1,G25)G26:f_water_enthalpy
            f_water_enthalpy = \
                seuif97.pt2h(newf_steam_pressure*1.1, newf_water_temperature)
            if f_water_enthalpy > 0:
                if val['flg'] == 'design':
                    result.f_water_enthalpy_design = \
                      f_water_enthalpy
                elif val['flg'] == 'check':
                    result.f_water_enthalpy_check = \
                      f_water_enthalpy
        # 没有则不做任何操作！
        print(result)


# G45=1000*P_T(G44)G44:a_temperature
# G45:a_saturation_pressure
class ASaturationPressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        newa_temperature = ''
        olda_temperature = ''
        # 得到字段：a_temperature
        if val['a_temperature'] != '':
            newa_temperature = float(val['a_temperature'])
        if val['flg'] == 'design' and result.a_temperature_design is not None:
            olda_temperature = float(result.a_temperature_design)
        elif val['flg'] == 'check' and result.a_temperature_check is not None:
            olda_temperature = float(result.a_temperature_check)
        
        # 判断a_temperature是否有变化
        if olda_temperature != '' and \
           newa_temperature != '' and \
           abs(olda_temperature - newa_temperature) \
           > 0.00001:
            # G45=1000*P_T(G44)
            a_saturation_pressure = \
                seuif97.psat_t(newa_temperature)*100
            if a_saturation_pressure > 0:
                if val['flg'] == 'design':
                    result.a_saturation_pressure_design = \
                      a_saturation_pressure
                elif val['flg'] == 'check':
                    result.a_saturation_pressure_check = \
                      a_saturation_pressure
        # 没有则不做任何操作!
        print(result)


# G45=1000*P_T(G44)
# G44:a_temperature
# G45:a_saturation_pressure
class ASaturationPressureAfter(FieldCalculation):
    def notify(self, val):
        result = val
        a_temperature_design = ''
        a_temperature_check = ''
        # 得到字段：a_temperature
        if result.a_temperature_design is not None:
            a_temperature_design = float(result.a_temperature_design)
        if result.a_temperature_check is not None:
            a_temperature_check = float(result.a_temperature_check)
        
        if a_temperature_design != '':
            # G45=1000*P_T(G44)
            a_saturation_pressure = \
                seuif97.psat_t(a_temperature_design)*100
            if a_saturation_pressure >= 0:
                result.a_saturation_pressure_design = \
                    a_saturation_pressure

        if a_temperature_check != '':
            # G45=1000*P_T(G44)
            a_saturation_pressure = \
                seuif97.psat_t(a_temperature_check)*100
            if a_saturation_pressure >= 0:
                result.a_saturation_pressure_check = \
                    a_saturation_pressure
        # 没有则不做任何操作!
        print(result)


if __name__ == "__main__":
    print("coalchp_furnace_calculation.py")
