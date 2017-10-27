# -*- coding: utf-8 -*-
from base import TechForum, Subscriber
from ..models import CoalCHPFurnaceCalculation
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
class FSteamEnthalpyDesign(Subscriber):
    def notify(self, val):
        # 得到字段：G20:f_steam_pressure、G21:f_steam_temperature
        f_steam_pressure = val['f_steam_pressure_design']
        f_steam_temperature = val['f_steam_temperature_design']

        # 判断f_steam_pressure是否有变化
        result = val['dbresult']
        if not result.f_steam_pressure_design and \
           not f_steam_pressure and \
           abs(result.f_steam_pressure_design - f_steam_pressure) \
           > 0.00001 or \
           result.f_steam_pressure_design is None and \
           not f_steam_pressure \
           or \
           not result.f_steam_temperature_design and \
           not f_steam_temperature and \
           abs(result.f_steam_temperature_design - f_steam_temperature) \
           > 0.00001 or \
           result.f_steam_temperature_design is None and \
           not f_steam_temperature:

            # G22=H_PT(G20,G21) 并更新
            f_steam_enthalpy = \
                seuif97.pt2h(f_steam_pressure, f_steam_temperature)
            if f_steam_enthalpy > 0:
                result.f_steam_enthalpy_design = \
                    seuif97.pt2h(f_steam_pressure, f_steam_temperature)         
        # 没有则不做任何操作！
        print(result)


# G22=H_PT(G20,G21)
class FSteamEnthalpyCheck(Subscriber):
    def notify(self, val):
        # 得到字段：G20:f_steam_pressure、G21:f_steam_temperature
        # f_steam_pressure = val['f_steam_pressure_check']
        # f_steam_temperature = val['f_steam_temperature_check']
        # 判断f_steam_pressure是否有变化
        # G22=H_PT(G20,G21) 并更新 
        # 没有则不做任何操作！
        print(val['f_steam_pressure_check'])


# G24=HL_P(G20*1.1)
class FSaturatedWaterEnthalpy(Subscriber):
    def notify(self, val):
        # 得到字段：f_steam_pressure
        f_steam_pressure = val['f_steam_pressure']
        # 判断f_steam_temperature是否有变化
        # 有则计算：G22=H_PT(G20,G21) 并更新
        # 没有则不做任何操作！
        print("f_steam_pressure = %f " % (f_steam_pressure))


# G26=H_PT(G20*1.1,G25)
class FWaterEnthalpy(Subscriber):
    def notify(self, val):
        # 得到字段：f_water_temperature
        f_water_temperature = val['f_water_temperature_design']
        # 判断f_water_temperature是否有变化
        # 有则计算：G26=H_PT(G20*1.1,G25) 并更新
        # 没有则不做任何操作！
        print("f_water_temperature_design = %f \
        " % (f_water_temperature))


# G45=1000*P_T(G44)
class ASaturationPressure(Subscriber):
    def notify(self, val):
        # 得到字段：a_temperature
        a_temperature = val['a_temperature_design']
        # 判断a_temperature是否有变化
        # 有则计算：G45=1000*P_T(G44) 并更新
        # 没有则不做任何操作！
        print("a_temperature_design = %f " % (a_temperature))


def specialCalculation(val):
    val['dbresult'] = CoalCHPFurnaceCalculation.searchById(val['id'])
    techForum = TechForum()
    techForum.register(FSteamEnthalpyDesign())
    techForum.register(FWaterEnthalpy())
    techForum.register(ASaturationPressure())
    techForum.writeNewPost(val)
    CoalCHPFurnaceCalculation.updataById(val['dbresult'])


if __name__ == "__main__":
    specialCalculation({'id': 1, 'f_steam_pressure': 9.80, 'f_steam_temperature\
    ': 540.00, 'f_water_temperature': 25, 'a_temperature': 44})
