# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97


# 实现字段m_saturation_temperature:特殊处理部分--饱和温度,的计算1
class M_saturation_temperature(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_condenser_pressure'] != '' and val['m_condenser_pressure'] is not None:
            m_saturation_temperature = seuif97.tsat_p(
                10 * (float(val['m_condenser_pressure'])))
            if m_saturation_temperature != -1:
                if val['flg'] == 'design':
                    result.m_saturation_temperature = m_saturation_temperature
                elif val['flg'] == 'check':
                    result.m_saturation_temperature_check = m_saturation_temperature
        print(result)


# 实现字段m_condensate_enthalpy:特殊处理部分--凝结水焓,的计算2
class M_condensate_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_condenser_pressure'] != '' and val['m_condenser_pressure'] is not None and val['m_supercooling'] != '' and val['m_supercooling'] is not None:
            m_condensate_enthalpy = seuif97.pt2h(
                (float(val['m_condenser_pressure'])),
                ((seuif97.tsat_p(10 *
                                 (float(val['m_condenser_pressure'])))) -
                 (float(val['m_supercooling']))))
            if m_condensate_enthalpy != -1:
                if val['flg'] == 'design':
                    result.m_condensate_enthalpy = m_condensate_enthalpy
                elif val['flg'] == 'check':
                    result.m_condensate_enthalpy_check = m_condensate_enthalpy
        print(result)
