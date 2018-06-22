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
            if f_steam_enthalpy != -1:
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
                seuif97.HL_P(float(val['f_steam_pressure'])*1.1*10)
            if f_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.f_saturated_water_enthalpy_design = \
                      f_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.f_saturated_water_enthalpy_check = \
                      f_saturated_water_enthalpy
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
            if f_water_enthalpy != -1:
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
                seuif97.psat_t(float(val['a_temperature']))
            if a_saturation_pressure != -1:
                if val['flg'] == 'design':
                    result.a_saturation_pressure_design = \
                      a_saturation_pressure*100
                elif val['flg'] == 'check':
                    result.a_saturation_pressure_check = \
                      a_saturation_pressure*100
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
                seuif97.psat_t(float(result.a_temperature_design))
            if a_saturation_pressure != -1:
                result.a_saturation_pressure_design = \
                    a_saturation_pressure*100

        if result.a_temperature_check is not None:
            # G45=1000*P_T(G44)
            a_saturation_pressure = \
                seuif97.psat_t(float(result.a_temperature_check))
            if a_saturation_pressure != -1:
                result.a_saturation_pressure_check = \
                    a_saturation_pressure*100

        # 没有则不做任何操作!
        print(result)


# 实现字段e_steam_entropy:特殊处理部分--7熵,的计算1
class E_steam_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_steam_entropy = seuif97.pt2s(
                (float(val['e_steam_pressure'])),
                (float(val['e_steam_temperature']))
            )

            if e_steam_entropy != -1:
                if val['flg'] == 'design':
                    result.e_steam_entropy = e_steam_entropy
                elif val['flg'] == 'check':
                    result.e_steam_entropy_check = e_steam_entropy
        print(result)


# 实现字段e_steam_enthalpy:特殊处理部分--8焓,的计算2
class E_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_steam_enthalpy = seuif97.pt2h(
                (float(val['e_steam_pressure'])),
                (float(val['e_steam_temperature']))
            )
            if e_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_steam_enthalpy = e_steam_enthalpy
                elif val['flg'] == 'check':
                    result.e_steam_enthalpy_check = e_steam_enthalpy
        print(result)


# 实现字段e_exhaust_point_temperature:特殊处理部分--10温度,的计算3
class E_exhaust_point_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_exhaust_point_temperature = seuif97.ps2t((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_exhaust_point_temperature != -1:
                if val['flg'] == 'design':
                    result.e_exhaust_point_temperature = e_exhaust_point_temperature
                elif val['flg'] == 'check':
                    result.e_exhaust_point_temperature_check = e_exhaust_point_temperature
        print(result)


# 实现字段e_exhaust_point_enthalpy:特殊处理部分--12焓,的计算4
class E_exhaust_point_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_exhaust_point_pressure'] != '' and val['e_exhaust_point_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_exhaust_point_enthalpy = seuif97.ps2h((float(val['e_exhaust_point_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_exhaust_point_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_exhaust_point_enthalpy = e_exhaust_point_enthalpy
                elif val['flg'] == 'check':
                    result.e_exhaust_point_enthalpy_check = e_exhaust_point_enthalpy
        print(result)


# 实现字段e_steam_exhaust_enthalpy:特殊处理部分--19焓,的计算5
class E_steam_exhaust_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_exhaust_pressure'] != '' and val['e_steam_exhaust_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_steam_exhaust_enthalpy = seuif97.ps2h((float(val['e_steam_exhaust_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_steam_exhaust_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_steam_exhaust_enthalpy = e_steam_exhaust_enthalpy
                elif val['flg'] == 'check':
                    result.e_steam_exhaust_enthalpy_check = e_steam_exhaust_enthalpy
        print(result)


# 实现字段e_backpressure_temperature:特殊处理部分--背压温度,的计算6
class E_backpressure_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None :
            e_backpressure_temperature = seuif97.tsat_p((float(val['e_backpressure_pressure']))*10)
            if e_backpressure_temperature != -1:
                if val['flg'] == 'design':
                    result.e_backpressure_temperature = e_backpressure_temperature
                elif val['flg'] == 'check':
                    result.e_backpressure_temperature_check = e_backpressure_temperature
        print(result)


# 实现字段e_backpressure_enthalpy:特殊处理部分--背压焓,的计算7
class E_backpressure_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            e_backpressure_enthalpy = seuif97.ps2h((float(val['e_backpressure_pressure'])),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if e_backpressure_enthalpy != -1:
                if val['flg'] == 'design':
                    result.e_backpressure_enthalpy = e_backpressure_enthalpy
                elif val['flg'] == 'check':
                    result.e_backpressure_enthalpy_check = e_backpressure_enthalpy
        print(result)


# 实现字段i_steam_entropy:特殊处理部分--106熵,的计算8
class I_steam_entropy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_steam_entropy = seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))
            if i_steam_entropy != -1:
                if val['flg'] == 'design':
                    result.i_steam_entropy = i_steam_entropy
                elif val['flg'] == 'check':
                    result.i_steam_entropy_check = i_steam_entropy
        print(result)


# 实现字段i_steam_enthalpy:特殊处理部分--107焓,的计算9
class I_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_steam_enthalpy = seuif97.pt2h(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))
            if i_steam_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_steam_enthalpy = i_steam_enthalpy
                elif val['flg'] == 'check':
                    result.i_steam_enthalpy_check = i_steam_enthalpy
        print(result)


# 实现字段i_high1_temperature:特殊处理部分--110温度,的计算10
class I_high1_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['i_high1_pressure'] != '' and val['i_high1_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_high1_temperature = seuif97.ps2t((float(val['i_high1_pressure'])),((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))
            if i_high1_temperature != -1:
                if val['flg'] == 'design':
                    result.i_high1_temperature = i_high1_temperature
                elif val['flg'] == 'check':
                    result.i_high1_temperature_check = i_high1_temperature
        print(result)


# 实现字段i_high1_enthalpy:特殊处理部分--111焓,的计算11
class I_high1_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['i_high1_pressure'] != '' and val['i_high1_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_high1_enthalpy = seuif97.ps2h((float(val['i_high1_pressure'])),((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))
            if i_high1_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_high1_enthalpy = i_high1_enthalpy
                elif val['flg'] == 'check':
                    result.i_high1_enthalpy_check = i_high1_enthalpy
        print(result)


# 实现字段i_high2_temperature:特殊处理部分--116温度,的计算12
class I_high2_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None and val['hh2_pressure_loss'] != '' and val['hh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_high2_temperature = seuif97.ps2t((((seuif97.psat_t(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))*0.1)/(1-(float(val['hh2_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))
            if i_high2_temperature != -1:
                if val['flg'] == 'design':
                    result.i_high2_temperature = i_high2_temperature
                elif val['flg'] == 'check':
                    result.i_high2_temperature_check = i_high2_temperature
        print(result)


# 实现字段i_high2_enthalpy:特殊处理部分--117焓,的计算13
class I_high2_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None and val['hh2_pressure_loss'] != '' and val['hh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_high2_enthalpy = seuif97.ps2h((((seuif97.psat_t(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))*0.1)/(1-(float(val['hh2_pressure_loss']))))),(((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))
            if i_high2_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_high2_enthalpy = i_high2_enthalpy
                elif val['flg'] == 'check':
                    result.i_high2_enthalpy_check = i_high2_enthalpy
        print(result)


# 实现字段i_deoxidize_temperature:特殊处理部分--122温度,的计算14
class I_deoxidize_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_deoxidize_temperature = seuif97.ps2t((((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss']))))),((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))
            if i_deoxidize_temperature != -1:
                if val['flg'] == 'design':
                    result.i_deoxidize_temperature = i_deoxidize_temperature
                elif val['flg'] == 'check':
                    result.i_deoxidize_temperature_check = i_deoxidize_temperature
        print(result)


# 实现字段i_deoxidize_enthalpy:特殊处理部分--123焓,的计算15
class I_deoxidize_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_deoxidize_enthalpy = seuif97.ps2h((((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss']))))),((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))
            if i_deoxidize_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_deoxidize_enthalpy = i_deoxidize_enthalpy
                elif val['flg'] == 'check':
                    result.i_deoxidize_enthalpy_check = i_deoxidize_enthalpy
        print(result)


# 实现字段i_low1_temperature:特殊处理部分--134温度,的计算16
class I_low1_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_low1_temperature = seuif97.ps2t((((seuif97.psat_t(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))))
            if i_low1_temperature != -1:
                if val['flg'] == 'design':
                    result.i_low1_temperature = i_low1_temperature
                elif val['flg'] == 'check':
                    result.i_low1_temperature_check = i_low1_temperature
        print(result)


# 实现字段i_low1_enthalpy:特殊处理部分--135焓,的计算17
class I_low1_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_low1_enthalpy = seuif97.ps2h((((seuif97.psat_t(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss']))))),(((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))))
            if i_low1_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_low1_enthalpy = i_low1_enthalpy
                elif val['flg'] == 'check':
                    result.i_low1_enthalpy_check = i_low1_enthalpy
        print(result)


# 实现字段i_low2_temperature:特殊处理部分--140温度,的计算18
class I_low2_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None and val['lh2_pressure_loss'] != '' and val['lh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_low2_temperature = seuif97.ps2t((((seuif97.psat_t(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))*0.1)/(1-(float(val['lh2_pressure_loss']))))),(((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))))
            if i_low2_temperature != -1:
                if val['flg'] == 'design':
                    result.i_low2_temperature = i_low2_temperature
                elif val['flg'] == 'check':
                    result.i_low2_temperature_check = i_low2_temperature
        print(result)


# 实现字段i_low2_enthalpy:特殊处理部分--141焓,的计算19
class I_low2_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None and val['lh2_pressure_loss'] != '' and val['lh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            i_low2_enthalpy = seuif97.ps2h((((seuif97.psat_t(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))*0.1)/(1-(float(val['lh2_pressure_loss']))))),(((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature']))))))))))
            if i_low2_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_low2_enthalpy = i_low2_enthalpy
                elif val['flg'] == 'check':
                    result.i_low2_enthalpy_check = i_low2_enthalpy
        print(result)


# 实现字段i_steam_exhaust_enthalpy:特殊处理部分--146焓,的计算20
class I_steam_exhaust_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None and val['i_steam_exhaust_pressure'] != '' and val['i_steam_exhaust_pressure'] is not None :
            i_steam_exhaust_enthalpy = seuif97.ps2h((float(val['i_steam_exhaust_pressure'])),((((((seuif97.pt2s(((float(val['e_steam_pressure']))),((float(val['e_steam_temperature'])))))))))))
            if i_steam_exhaust_enthalpy != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy = i_steam_exhaust_enthalpy
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_check = i_steam_exhaust_enthalpy
        print(result)


# 实现字段i_steam_exhaust_enthalpy_steam:特殊处理部分--148饱和蒸汽焓,的计算21
class I_steam_exhaust_enthalpy_steam(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['i_steam_exhaust_pressure'] != '' and val['i_steam_exhaust_pressure'] is not None :
            i_steam_exhaust_enthalpy_steam = seuif97.HG_P((float(val['i_steam_exhaust_pressure'])*10))
            if i_steam_exhaust_enthalpy_steam != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy_steam = i_steam_exhaust_enthalpy_steam
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_steam_check = i_steam_exhaust_enthalpy_steam
        print(result)


# 实现字段i_steam_exhaust_enthalpy_water:特殊处理部分--149饱和水焓,的计算22
class I_steam_exhaust_enthalpy_water(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['i_steam_exhaust_pressure'] != '' and val['i_steam_exhaust_pressure'] is not None :
            i_steam_exhaust_enthalpy_water = seuif97.HL_P((float(val['i_steam_exhaust_pressure'])*10))
            if i_steam_exhaust_enthalpy_water != -1:
                if val['flg'] == 'design':
                    result.i_steam_exhaust_enthalpy_water = i_steam_exhaust_enthalpy_water
                elif val['flg'] == 'check':
                    result.i_steam_exhaust_enthalpy_water_check = i_steam_exhaust_enthalpy_water
        print(result)


# 实现字段h_enthalpy:特殊处理部分--28焓值,的计算23
class H_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['h_temperature'] != '' and val['h_temperature'] is not None and val['d_work_pressure'] != '' and val['d_work_pressure'] is not None :
            h_enthalpy = seuif97.pt2h((float(val['h_temperature'])),(2*(float(val['d_work_pressure']))))
            if h_enthalpy != -1:
                if val['flg'] == 'design':
                    result.h_enthalpy = h_enthalpy
                elif val['flg'] == 'check':
                    result.h_enthalpy_check = h_enthalpy
        print(result)


# 实现字段hh1_saturated_water_enthalpy:特殊处理部分--34饱和水焓,的计算24
class Hh1_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh1_water_temperature'] != '' and val['hh1_water_temperature'] is not None and val['hh1_top_difference'] != '' and val['hh1_top_difference'] is not None :
            hh1_saturated_water_enthalpy = seuif97.HL_T(((float(val['hh1_water_temperature']))+(float(val['hh1_top_difference']))))
            if hh1_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh1_saturated_water_enthalpy = hh1_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_saturated_water_enthalpy_check = hh1_saturated_water_enthalpy
        print(result)


# 实现字段hh1_work_pressure:特殊处理部分--35工作压力,的计算25
class Hh1_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh1_water_temperature'] != '' and val['hh1_water_temperature'] is not None and val['hh1_top_difference'] != '' and val['hh1_top_difference'] is not None :
            hh1_work_pressure = seuif97.psat_t(((float(val['hh1_water_temperature']))+(float(val['hh1_top_difference']))))
            if hh1_work_pressure != -1:
                if val['flg'] == 'design':
                    result.hh1_work_pressure = hh1_work_pressure*0.1
                elif val['flg'] == 'check':
                    result.hh1_work_pressure_check = hh1_work_pressure*0.1
        print(result)


# 实现字段hh1_extraction_enthalpy:特殊处理部分--38抽汽焓,的计算26
class Hh1_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh1_water_temperature'] != '' and val['hh1_water_temperature'] is not None and val['hh1_top_difference'] != '' and val['hh1_top_difference'] is not None and val['hh1_pressure_loss'] != '' and val['hh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            hh1_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['hh1_water_temperature']))+(float(val['hh1_top_difference']))))*0.1)/(1-(float(val['hh1_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if hh1_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh1_extraction_enthalpy = hh1_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_extraction_enthalpy_check = hh1_extraction_enthalpy
        print(result)


# 实现字段hh2_saturated_water_enthalpy:特殊处理部分--44饱和水焓,的计算27
class Hh2_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None :
            hh2_saturated_water_enthalpy = seuif97.HL_T(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))
            if hh2_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh2_saturated_water_enthalpy = hh2_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh2_saturated_water_enthalpy_check = hh2_saturated_water_enthalpy
        print(result)


# 实现字段hh2_work_pressure:特殊处理部分--45工作压力,的计算28
class Hh2_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None :
            hh2_work_pressure = seuif97.psat_t(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))
            if hh2_work_pressure != -1:
                if val['flg'] == 'design':
                    result.hh2_work_pressure = hh2_work_pressure*0.1
                elif val['flg'] == 'check':
                    result.hh2_work_pressure_check = hh2_work_pressure*0.1
        print(result)


# 实现字段hh2_extraction_enthalpy:特殊处理部分--48抽汽焓,的计算29
class Hh2_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh2_water_temperature'] != '' and val['hh2_water_temperature'] is not None and val['hh2_top_difference'] != '' and val['hh2_top_difference'] is not None and val['hh2_pressure_loss'] != '' and val['hh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            hh2_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['hh2_water_temperature']))+(float(val['hh2_top_difference']))))*0.1)/(1-(float(val['hh2_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if hh2_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh2_extraction_enthalpy = hh2_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.hh2_extraction_enthalpy_check = hh2_extraction_enthalpy
        print(result)


# 实现字段d_water_enthalpy:特殊处理部分--51给水出口焓,的计算30
class D_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_water_temperature'] != '' and val['d_water_temperature'] is not None :
            d_water_enthalpy = seuif97.HL_T((float(val['d_water_temperature'])))
            if d_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.d_water_enthalpy = d_water_enthalpy
                elif val['flg'] == 'check':
                    result.d_water_enthalpy_check = d_water_enthalpy
        print(result)


# 实现字段d_extraction_enthalpy:特殊处理部分--55抽汽焓,的计算31
class D_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['d_work_pressure'] != '' and val['d_work_pressure'] is not None and val['d_pressure_loss'] != '' and val['d_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            d_extraction_enthalpy = seuif97.ps2h(((float(val['d_work_pressure']))/(1-(float(val['d_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if d_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.d_extraction_enthalpy = d_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.d_extraction_enthalpy_check = d_extraction_enthalpy
        print(result)


# 实现字段lh1_saturated_water_enthalpy:特殊处理部分--61饱和水焓,的计算32
class Lh1_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None :
            lh1_saturated_water_enthalpy = seuif97.HL_T(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))
            if lh1_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh1_saturated_water_enthalpy = lh1_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.lh1_saturated_water_enthalpy_check = lh1_saturated_water_enthalpy

        
        print(result)


# 实现字段lh1_work_pressure:特殊处理部分--62工作压力,的计算33
class Lh1_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None :
            lh1_work_pressure = seuif97.psat_t(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))
            if lh1_work_pressure != -1:
                if val['flg'] == 'design':
                    result.lh1_work_pressure = lh1_work_pressure*0.1
                elif val['flg'] == 'check':
                    result.lh1_work_pressure_check = lh1_work_pressure*0.1
        print(result)


# 实现字段lh1_extraction_enthalpy:特殊处理部分--65抽汽焓,的计算34
class Lh1_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh1_water_temperature'] != '' and val['lh1_water_temperature'] is not None and val['lh1_top_difference'] != '' and val['lh1_top_difference'] is not None and val['lh1_pressure_loss'] != '' and val['lh1_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            lh1_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['lh1_water_temperature']))+(float(val['lh1_top_difference']))))*0.1)/(1-(float(val['lh1_pressure_loss'])))),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if lh1_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh1_extraction_enthalpy = lh1_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.lh1_extraction_enthalpy_check = lh1_extraction_enthalpy
        print(result)


# 实现字段lh2_saturated_water_enthalpy:特殊处理部分--71饱和水焓,的计算35
class Lh2_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None :
            lh2_saturated_water_enthalpy = seuif97.HL_T(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))
            if lh2_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh2_saturated_water_enthalpy = lh2_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.lh2_saturated_water_enthalpy_check = lh2_saturated_water_enthalpy
        print(result)


# 实现字段lh2_work_pressure:特殊处理部分--72工作压力,的计算36
class Lh2_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None :
            lh2_work_pressure = seuif97.psat_t(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))
            if lh2_work_pressure != -1:
                if val['flg'] == 'design':
                    result.lh2_work_pressure = lh2_work_pressure*0.1
                elif val['flg'] == 'check':
                    result.lh2_work_pressure_check = lh2_work_pressure*0.1
        print(result)


# 实现字段lh2_extraction_enthalpy:特殊处理部分--75抽汽焓,的计算37
class Lh2_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh2_water_temperature'] != '' and val['lh2_water_temperature'] is not None and val['lh2_top_difference'] != '' and val['lh2_top_difference'] is not None and val['lh2_pressure_loss'] != '' and val['lh2_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            lh2_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['lh2_water_temperature']))+(float(val['lh2_top_difference']))))*0.1)/(1-(float(val['lh2_pressure_loss'])))),((seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature']))))))
            if lh2_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh2_extraction_enthalpy = lh2_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.lh2_extraction_enthalpy_check = lh2_extraction_enthalpy
        print(result)


# 实现字段c_water_temperature:特殊处理部分--77给水出水温度,的计算39
class C_water_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_steam_exhaust_pressure'] != '' and val['e_steam_exhaust_pressure'] is not None :
            c_water_temperature = seuif97.tsat_p(((float(val['e_steam_exhaust_pressure']))*10))
            if c_water_temperature != -1:
                if val['flg'] == 'design':
                    result.c_water_temperature = c_water_temperature
                elif val['flg'] == 'check':
                    result.c_water_temperature_check = c_water_temperature

        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None :
            c_water_temperature = seuif97.tsat_p(((float(val['e_backpressure_pressure']))*10))
            if c_water_temperature != -1:
                if val['flg'] == 'design':
                    result.c_water_temperature = c_water_temperature
                elif val['flg'] == 'check':
                    result.c_water_temperature_check = c_water_temperature
        print(result)


# 实现字段c_water_enthalpy:特殊处理部分--78给水出口焓,的计算39
class C_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['e_backpressure_pressure'] != '' and val['e_backpressure_pressure'] is not None :

            water_temperature = float(seuif97.tsat_p(((float(val['e_backpressure_pressure']))*10)))
            exhaust_pressure = float(val['e_backpressure_pressure'])
            c_water_enthalpy = seuif97.pt2h(exhaust_pressure,water_temperature)

            if c_water_enthalpy != -1:
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
        result = val['dbresult']
        if val['hh3_water_temperature'] != '' and val['hh3_water_temperature'] is not None and val['hh3_top_difference'] != '' and val['hh3_top_difference'] is not None :
            hh3_saturated_water_enthalpy = seuif97.HL_T(((float(val['hh3_water_temperature']))+(float(val['hh3_top_difference']))))
            if hh3_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh3_saturated_water_enthalpy = hh3_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh3_saturated_water_enthalpy_check = hh3_saturated_water_enthalpy
        print(result)


# 实现字段hh3_work_pressure:特殊处理部分--85工作压力,的计算41
class Hh3_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh3_water_temperature'] != '' and val['hh3_water_temperature'] is not None and val['hh3_top_difference'] != '' and val['hh3_top_difference'] is not None :
            hh3_work_pressure = seuif97.psat_t(((float(val['hh3_water_temperature']))+(float(val['hh3_top_difference']))))
            if hh3_work_pressure != -1:
                if val['flg'] == 'design':
                    result.hh3_work_pressure = hh3_work_pressure*0.1
                elif val['flg'] == 'check':
                    result.hh3_work_pressure_check = hh3_work_pressure*0.1
        print(result)


# 实现字段hh3_extraction_enthalpy:特殊处理部分--88抽汽焓,的计算42
class Hh3_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh3_water_temperature'] != '' and val['hh3_water_temperature'] is not None and val['hh3_top_difference'] != '' and val['hh3_top_difference'] is not None and val['hh3_pressure_loss'] != '' and val['hh3_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            hh3_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['hh3_water_temperature']))+(float(val['hh3_top_difference']))))*0.1)/(1-(float(val['hh3_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if hh3_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh3_extraction_enthalpy = hh3_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.hh3_extraction_enthalpy_check = hh3_extraction_enthalpy
        print(result)


# 实现字段lh3_saturated_water_enthalpy:特殊处理部分--94饱和水焓,的计算43
class Lh3_saturated_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh3_water_temperature'] != '' and val['lh3_water_temperature'] is not None and val['lh3_top_difference'] != '' and val['lh3_top_difference'] is not None :
            lh3_saturated_water_enthalpy = seuif97.HL_T(((float(val['lh3_water_temperature']))+(float(val['lh3_top_difference']))))
            if lh3_saturated_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh3_saturated_water_enthalpy = lh3_saturated_water_enthalpy
                elif val['flg'] == 'check':
                    result.lh3_saturated_water_enthalpy_check = lh3_saturated_water_enthalpy
        print(result)


# 实现字段lh3_work_pressure:特殊处理部分--95工作压力,的计算44
class Lh3_work_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh3_water_temperature'] != '' and val['lh3_water_temperature'] is not None and val['lh3_top_difference'] != '' and val['lh3_top_difference'] is not None :
            lh3_work_pressure = seuif97.psat_t(((float(val['lh3_water_temperature']))+(float(val['lh3_top_difference']))))
            if lh3_work_pressure != -1:
                if val['flg'] == 'design':
                    result.lh3_work_pressure = lh3_work_pressure*0.1
                elif val['flg'] == 'check':
                    result.lh3_work_pressure_check = lh3_work_pressure*0.1
        print(result)


# 实现字段lh3_extraction_enthalpy:特殊处理部分--98抽汽焓,的计算45
class Lh3_extraction_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['lh3_water_temperature'] != '' and val['lh3_water_temperature'] is not None and val['lh3_top_difference'] != '' and val['lh3_top_difference'] is not None and val['lh3_pressure_loss'] != '' and val['lh3_pressure_loss'] is not None and val['e_steam_pressure'] != '' and val['e_steam_pressure'] is not None and val['e_steam_temperature'] != '' and val['e_steam_temperature'] is not None :
            lh3_extraction_enthalpy = seuif97.ps2h(((seuif97.psat_t(((float(val['lh3_water_temperature']))+(float(val['lh3_top_difference']))))*0.1)/(1-(float(val['lh3_pressure_loss'])))),(seuif97.pt2s((float(val['e_steam_pressure'])),(float(val['e_steam_temperature'])))))
            if lh3_extraction_enthalpy != -1:
                if val['flg'] == 'design':
                    result.lh3_extraction_enthalpy = lh3_extraction_enthalpy
                elif val['flg'] == 'check':
                    result.lh3_extraction_enthalpy_check = lh3_extraction_enthalpy
        print(result)

# 实现字段hh1_water_enthalpy:特殊处理部分--31给水出口焓,的计算25
class Hh1_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['hh1_water_temperature'] != '' and val['hh1_water_temperature'] is not None :
            hh1_water_enthalpy = seuif97.HL_T((float(val['hh1_water_temperature'])))
            if hh1_water_enthalpy != -1:
                if val['flg'] == 'design':
                    result.hh1_water_enthalpy = hh1_water_enthalpy
                elif val['flg'] == 'check':
                    result.hh1_water_enthalpy_check = hh1_water_enthalpy
        print(result)


if __name__ == "__main__":
    print("coalchp_furnace_calculation.py")
