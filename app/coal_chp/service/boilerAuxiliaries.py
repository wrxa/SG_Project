# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97


# 实现字段r_drum_aturatedwater_enthalpy:特殊处理部分--汽包压力下的饱和水焓,的计算1
class R_drum_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['r_drum_pressure'] != '' and val['r_drum_pressure'] is not None:
            r_drum_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_drum_pressure']) * 10))
            if r_drum_aturatedwater_enthalpy != -1:
                if val['flg'] == 'design':
                    result.r_drum_aturatedwater_enthalpy = \
                     r_drum_aturatedwater_enthalpy
                elif val['flg'] == 'check':
                    result.r_drum_aturatedwater_enthalpy_check = \
                     r_drum_aturatedwater_enthalpy
        print(result)


# 实现字段r_work_aturatedwater_enthalpy:特殊处理部分--扩容器压力下饱和水焓,的计算2
class R_work_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['r_work_pressure'] != '' and val['r_work_pressure'] is not None:
            r_work_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['r_work_pressure']))*10)
            if r_work_aturatedwater_enthalpy != -1:
                if val['flg'] == 'design':
                    result.r_work_aturatedwater_enthalpy = \
                     r_work_aturatedwater_enthalpy
                elif val['flg'] == 'check':
                    result.r_work_aturatedwater_enthalpy_check = \
                     r_work_aturatedwater_enthalpy
        print(result)


# 实现字段r_work_latentheat_vaporization:特殊处理部分--扩容器压力下汽化潜热,的计算3
class R_work_latentheat_vaporization(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['r_work_pressure'] != '' and val['r_work_pressure'] is not None:
            r_work_latentheat_vaporization = seuif97.HG_P(
                (float(val['r_work_pressure']))*10) - (seuif97.HL_P(
                    (float(val['r_work_pressure']))*10))
            if r_work_latentheat_vaporization != -1:
                if val['flg'] == 'design':
                    result.r_work_latentheat_vaporization = \
                     r_work_latentheat_vaporization
                elif val['flg'] == 'check':
                    result.r_work_latentheat_vaporization_check = \
                     r_work_latentheat_vaporization
        print(result)


# 实现字段c_drum_aturatedwater_enthalpy:特殊处理部分--汽包压力下的饱和水焓,的计算4
class C_drum_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['r_drum_pressure'] != '' and val['r_drum_pressure'] is not None:
            c_drum_aturatedwater_enthalpy = seuif97.HL_P(
                ((float(val['r_drum_pressure'])))*10)
            if c_drum_aturatedwater_enthalpy != -1:
                if val['flg'] == 'design':
                    result.c_drum_aturatedwater_enthalpy = \
                     c_drum_aturatedwater_enthalpy
                elif val['flg'] == 'check':
                    result.c_drum_aturatedwater_enthalpy_check = \
                     c_drum_aturatedwater_enthalpy
        print(result)


# 实现字段c_work_aturatedwater_enthalpy:特殊处理部分--扩容器压力下饱和水焓,的计算5
class C_work_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['c_work_pressure'] != '' and val['c_work_pressure'] is not None:
            c_work_aturatedwater_enthalpy = seuif97.HL_P(
                (float(val['c_work_pressure']))*10)
            if c_work_aturatedwater_enthalpy != -1:
                if val['flg'] == 'design':
                    result.c_work_aturatedwater_enthalpy = \
                     c_work_aturatedwater_enthalpy
                elif val['flg'] == 'check':
                    result.c_work_aturatedwater_enthalpy_check = \
                     c_work_aturatedwater_enthalpy
        print(result)


# 实现字段c_work_steam_pecificvolume:特殊处理部分--扩容器压力下蒸汽比容,的计算6
class C_work_steam_pecificvolume(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['c_work_pressure'] != '' and val['c_work_pressure'] is not None:
            c_work_steam_pecificvolume = seuif97.VG_P(
                (float(val['c_work_pressure']))*10)
            if c_work_steam_pecificvolume != -1:
                if val['flg'] == 'design':
                    result.c_work_steam_pecificvolume = \
                     c_work_steam_pecificvolume
                elif val['flg'] == 'check':
                    result.c_work_steam_pecificvolume_check = \
                     c_work_steam_pecificvolume
        print(result)


# 实现字段c_work_latentheat_vaporization:特殊处理部分--扩容器压力下汽化潜热,的计算7
class C_work_latentheat_vaporization(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['c_work_pressure'] != '' and val['c_work_pressure'] is not None:
            c_work_latentheat_vaporization = seuif97.HG_P(
                (float(val['c_work_pressure']))*10) - (seuif97.HL_P(
                    (float(val['c_work_pressure']))*10))
            if c_work_latentheat_vaporization != -1:
                if val['flg'] == 'design':
                    result.c_work_latentheat_vaporization = \
                     c_work_latentheat_vaporization
                elif val['flg'] == 'check':
                    result.c_work_latentheat_vaporization_check = \
                     c_work_latentheat_vaporization
        print(result)


# 新加模块（减温减压器---已知减温前、后参数求减温水量及减温后量）熵函和普通计算
# 实现字段t_new_enthalpy:特殊处理部分--焓,的计算1
class T_new_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_new_steam_temperature'] != '' and val['t_new_steam_temperature'] is not None and val['t_new_pressure'] != '' and val['t_new_pressure'] is not None:
            t_new_enthalpy = seuif97.pt2h((float(val['t_new_pressure'])),
                                  (float(val['t_new_steam_temperature'])))
            result.t_new_enthalpy = t_new_enthalpy
        print(result)


# 实现字段t_reduce_water_pressure:压力,的计算2
class T_reduce_water_pressure(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_reduce_steam_pressure'] != '' and val['t_reduce_steam_pressure'] is not None:
            t_reduce_water_pressure = (
                float(val['t_reduce_steam_pressure'])) + 1.47
            result.t_reduce_water_pressure = t_reduce_water_pressure
        print(result)


# 实现字段t_reduce_water_enthalpy:特殊处理部分--焓,的计算3
class T_reduce_water_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_reduce_water_temperature'] != '' and val['t_reduce_water_temperature'] is not None and val['t_reduce_steam_pressure'] != '' and val['t_reduce_steam_pressure'] is not None:
            t_reduce_water_enthalpy = seuif97.pt2h(
                ((float(val['t_reduce_steam_pressure'])) + 1.47), (
                    float(val['t_reduce_water_temperature'])))
            result.t_reduce_water_enthalpy = t_reduce_water_enthalpy
        print(result)


# 实现字段t_reduce_water_flow_rate:流量,的计算4
class T_reduce_water_flow_rate(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_new_steam_temperature'] != '' and val['t_new_steam_temperature'] is not None and val['t_new_pressure'] != '' and val['t_new_pressure'] is not None and val['t_new_flow_rate'] != '' and val['t_new_flow_rate'] is not None and val['t_reduce_water_temperature'] != '' and val['t_reduce_water_temperature'] is not None and val['t_reduce_steam_temperature'] != '' and val['t_reduce_steam_temperature'] is not None and val['t_reduce_steam_pressure'] != '' and val['t_reduce_steam_pressure'] is not None and val['t_reduce_persent'] != '' and val['t_reduce_persent'] is not None:
            t_reduce_water_flow_rate = (
                (seuif97.pt2h((float(val['t_new_pressure'])),
                      (float(val['t_new_steam_temperature'])))) - (seuif97.pt2h(
                          (float(val['t_reduce_steam_pressure'])),
                          (float(val['t_reduce_steam_temperature']))))
            ) * (float(val['t_new_flow_rate'])) / (
                (seuif97.pt2h((float(val['t_reduce_steam_pressure'])),
                      (float(val['t_reduce_steam_temperature'])))) - (seuif97.pt2h(
                          ((float(val['t_reduce_steam_pressure'])) + 1.47),
                          (float(val['t_reduce_water_temperature'])))) +
                (float(val['t_reduce_persent'])) / 100 * ((seuif97.HL_P(
                    (float(val['t_reduce_steam_pressure']))*10)) - (seuif97.pt2h(
                        (float(val['t_reduce_steam_pressure'])),
                        (float(val['t_reduce_steam_temperature']))))))
            result.t_reduce_water_flow_rate = t_reduce_water_flow_rate
        print(result)


# 实现字段t_reduce_steam_enthalpy:特殊处理部分--焓,的计算5
class T_reduce_steam_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_reduce_steam_temperature'] != '' and val['t_reduce_steam_temperature'] is not None and val['t_reduce_steam_pressure'] != '' and val['t_reduce_steam_pressure'] is not None:
            t_reduce_steam_enthalpy = seuif97.pt2h(
                (float(val['t_reduce_steam_pressure'])), (
                    float(val['t_reduce_steam_temperature'])))
            result.t_reduce_steam_enthalpy = t_reduce_steam_enthalpy
        print(result)


# 实现字段t_reduce_enough_enthalpy:特殊处理部分--焓,的计算6
class T_reduce_enough_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_reduce_steam_pressure'] != '' and val['t_reduce_steam_pressure'] is not None:
            t_reduce_enough_enthalpy = seuif97.HL_P(
                (float(val['t_reduce_steam_pressure']))*10)
            result.t_reduce_enough_enthalpy = t_reduce_enough_enthalpy
        print(result)


# 实现字段t_rudece_flow_rate:流量,的计算7
class T_rudece_flow_rate(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['t_new_steam_temperature'] != '' and val['t_new_steam_temperature'] is not None and val['t_new_pressure'] != '' and val['t_new_pressure'] is not None and val['t_new_flow_rate'] != '' and val['t_new_flow_rate'] is not None and val['t_reduce_water_temperature'] != '' and val['t_reduce_water_temperature'] is not None and val['t_reduce_steam_temperature'] != '' and val['t_reduce_steam_temperature'] is not None and val['t_reduce_steam_pressure'] != '' and val['t_reduce_steam_pressure'] is not None and val['t_reduce_persent'] != '' and val['t_reduce_persent'] is not None:
            t_rudece_flow_rate = (float(val['t_new_flow_rate'])) + (
                ((seuif97.pt2h((float(val['t_new_pressure'])),
                       (float(val['t_new_steam_temperature'])))) -
                 (seuif97.pt2h((float(val['t_reduce_steam_pressure'])),
                       (float(val['t_reduce_steam_temperature']))))) *
                (float(val['t_new_flow_rate'])) / (
                    (seuif97.pt2h((float(val['t_reduce_steam_pressure'])),
                          (float(val['t_reduce_steam_temperature'])))) - (seuif97.pt2h(
                              ((float(val['t_reduce_steam_pressure'])) + 1.47),
                              (float(val['t_reduce_water_temperature'])))) +
                    (float(val['t_reduce_persent'])) / 100 * ((seuif97.HL_P(
                        (float(val['t_reduce_steam_pressure']))*10)) - (seuif97.pt2h(
                            (float(val['t_reduce_steam_pressure'])),
                            (float(val['t_reduce_steam_temperature']))))))) * (
                                1 - (float(val['t_reduce_persent'])) / 100)
            result.t_rudece_flow_rate = t_rudece_flow_rate
        print(result)
