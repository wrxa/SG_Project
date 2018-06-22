# -*- coding: utf-8 -*-
from base import FieldCalculation


# 实现字段m_steamwater_cycle_loss:厂内汽水循环损失,的计算1
class M_steamwater_cycle_loss(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_boiler_evaporation'] != '' and val['m_boiler_evaporation'] is not None and val['m_makeup_steam'] != '' and val['m_makeup_steam'] is not None:
            m_steamwater_cycle_loss = 0.03 * (
                (float(val['m_boiler_evaporation'])) +
                (float(val['m_makeup_steam'])))
            result.m_steamwater_cycle_loss = m_steamwater_cycle_loss
        print(result)


# 实现字段m_pollution_loss:排污损失,的计算2
class M_pollution_loss(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_boiler_evaporation'] != '' and val['m_boiler_evaporation'] is not None and val['m_makeup_steam'] != '' and val['m_makeup_steam'] is not None:
            m_pollution_loss = 0.02 * ((float(val['m_boiler_evaporation'])) +
                                       (float(val['m_makeup_steam'])))
            result.m_pollution_loss = m_pollution_loss
        print(result)


# 实现字段m_condensate_loss:换热凝结水损失,的计算3
class M_condensate_loss(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_condensing_capacity'] != '' and val['m_condensing_capacity'] is not None:
            m_condensate_loss = 0.02 * (float(val['m_condensing_capacity']))
            result.m_condensate_loss = m_condensate_loss
        print(result)


# 实现字段m_boiler_normal_watersupply:锅炉正常补水量,的计算4
class M_boiler_normal_watersupply(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_boiler_evaporation'] != '' and val['m_boiler_evaporation'] is not None and val['m_makeup_steam'] != '' and val['m_makeup_steam'] is not None and val['m_condensing_capacity'] != '' and val['m_condensing_capacity'] is not None:
            m_boiler_normal_watersupply = (0.03 * (
                (float(val['m_boiler_evaporation'])) +
                (float(val['m_makeup_steam'])))) + (0.02 * (
                    (float(val['m_boiler_evaporation'])) +
                    (float(val['m_makeup_steam'])))) + (
                        0.02 * (float(val['m_condensing_capacity'])))
            result.m_boiler_normal_watersupply = m_boiler_normal_watersupply
        print(result)


# 实现字段m_increase_loss:启动或事故增加损失,的计算5
class M_increase_loss(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_boiler_evaporation'] != '' and val['m_boiler_evaporation'] is not None and val['m_makeup_steam'] != '' and val['m_makeup_steam'] is not None:
            m_increase_loss = 0.1 * ((float(val['m_boiler_evaporation'])) +
                                     (float(val['m_makeup_steam'])))
            result.m_increase_loss = m_increase_loss
        print(result)


# 实现字段m_boiler_max_watersupply:锅炉最大补水量,的计算6
class M_boiler_max_watersupply(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_boiler_evaporation'] != '' and val['m_boiler_evaporation'] is not None and val['m_makeup_steam'] != '' and val['m_makeup_steam'] is not None and val['m_condensing_capacity'] != '' and val['m_condensing_capacity'] is not None:
            m_boiler_max_watersupply = (0.1 * (
                (float(val['m_boiler_evaporation'])) +
                (float(val['m_makeup_steam'])))) + (
                    (0.03 * ((float(val['m_boiler_evaporation'])) +
                             (float(val['m_makeup_steam'])))) + (0.02 * (
                                 (float(val['m_boiler_evaporation'])) +
                                 (float(val['m_makeup_steam'])))) +
                    (0.02 * (float(val['m_condensing_capacity']))))
            result.m_boiler_max_watersupply = m_boiler_max_watersupply
        print(result)


# 实现字段m_remove_salt_volume:除盐水箱有效容积,的计算7
class M_remove_salt_volume(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['m_output'] != '' and val['m_output'] is not None:
            m_remove_salt_volume = (float(val['m_output'])) * 5
            result.m_remove_salt_volume = m_remove_salt_volume
        print(result)
