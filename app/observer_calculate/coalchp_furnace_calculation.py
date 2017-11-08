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


# 表内计算G22=H_PT(G20,G21)
class FSteamEnthalpy(FieldCalculation):
    def notify(self, val):
        # 判断f_steam_pressure是否有变化
        result = val['dbresult']
        # 得到字段：G20:f_steam_pressure、G21:f_steam_temperature
        if val['f_steam_pressure'] != '' and \
            val['f_steam_temperature'] != '' and \
            val['f_steam_pressure'] is not None and \
                val['f_steam_temperature'] is not None:
            # G22=H_PT(G20,G21) 并更新
            f_steam_enthalpy = seuif97.pt2h(
                float(val['f_steam_pressure']),
                float(val['f_steam_temperature'])
            )
            if f_steam_enthalpy > 0:
                if val['flg'] == 'design':
                    result.f_steam_enthalpy_design = \
                      f_steam_enthalpy
                elif val['flg'] == 'check':
                    result.f_steam_enthalpy_check = \
                      f_steam_enthalpy
        # 没有则不做任何操作！
        print(result)


#  表内计算G24=HL_P(G20*1.1)
class FSaturatedWaterEnthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        # 得到字段：f_steam_pressure
        if val['f_steam_pressure'] != '' and \
                val['f_steam_pressure'] is not None:
            # G24=HL_P(G20*1.1)G24:f_saturated_water_enthalpy
            f_saturated_water_enthalpy = \
                seuif97.h_p(float(val['f_steam_pressure']))
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


# 表内计算G26=H_PT(G20*1.1,G25)G26:f_water_enthalpy
class FWaterEnthalpy(FieldCalculation):
    def notify(self, val):
        # 判断f_steam_pressure是否有变化
        result = val['dbresult']
        # 得到字段：G20:f_steam_pressure、G25:f_water_temperature
        if val['f_steam_pressure'] != '' and \
            val['f_water_temperature'] != '' and \
            val['f_steam_pressure'] is not None and \
                val['f_water_temperature'] is not None:
            # G26=H_PT(G20*1.1,G25)G26:f_water_enthalpy
            f_water_enthalpy = seuif97.pt2h(
                float(val['f_steam_pressure'])*1.1,
                float(val['f_water_temperature'])
            )
            if f_water_enthalpy > 0:
                if val['flg'] == 'design':
                    result.f_water_enthalpy_design = \
                      f_water_enthalpy
                elif val['flg'] == 'check':
                    result.f_water_enthalpy_check = \
                      f_water_enthalpy
        # 没有则不做任何操作！
        print(result)


# G45=1000*P_T(G44)
# G44:a_temperature
# G45:a_saturation_pressure
# 表内
class ASaturationPressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        # 得到字段：a_temperature
        if val['a_temperature'] != '' and val['a_temperature'] is not None:
            # G45=1000*P_T(G44)
            a_saturation_pressure = \
                seuif97.psat_t(float(val['a_temperature']))*100
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
# 表间
# 因为字段：a_temperature是从需求调查表中同步过来，
# 当需求调查表该字段修改后，触发器不会因为该字段的修改而改变a_saturation_pressure的值，故需要自行添加该流程：
# 每当需求表提交更新成功后，接着执行该程序段更新字段a_saturation_pressure
# 故：第一步，分析被计算字段的值是因为哪些根本字段而影响的是，第二步，分析：根本字段是自定义输入，还是读取需求调查表得到而来，
# 第三步：如果是自定义仅仅需要表内计算即可，如果是同步则，如果需求要求可改变则需要写两段代码（表间，表内），否则仅仅需要如上代码
class ASaturationPressureAfter(FieldCalculation):
    def notify(self, val):
        result = val
        # 得到字段：a_temperature
        if result.a_temperature_design is not None:
            # G45=1000*P_T(G44)
            a_saturation_pressure = \
                seuif97.psat_t(float(result.a_temperature_design))*100
            if a_saturation_pressure >= 0:
                result.a_saturation_pressure_design = \
                    a_saturation_pressure

        if result.a_temperature_check is not None:
            # G45=1000*P_T(G44)
            a_saturation_pressure = \
                seuif97.psat_t(float(result.a_temperature_check))*100
            if a_saturation_pressure >= 0:
                result.a_saturation_pressure_check = \
                    a_saturation_pressure

        # 没有则不做任何操作!
        print(result)

if __name__ == "__main__":
    print("coalchp_furnace_calculation.py")
