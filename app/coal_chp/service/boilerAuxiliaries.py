# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97


# 实现字段r_drum_aturatedwater_enthalpy:特殊处理部分--汽包压力下的饱和水焓,的计算1
class R_drum_aturatedwater_enthalpy(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['r_drum_pressure'] != '' and val['r_drum_pressure'] is not None:
            r_drum_aturatedwater_enthalpy = seuif97.h_p(
                (float(val['r_drum_pressure'])))
            if r_drum_aturatedwater_enthalpy >= 0:
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
            r_work_aturatedwater_enthalpy = seuif97.h_p(
                (float(val['r_work_pressure'])))
            if r_work_aturatedwater_enthalpy >= 0:
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
                (float(val['r_work_pressure']))) - (seuif97.h_p(
                    (float(val['r_work_pressure']))))
            if r_work_latentheat_vaporization >= 0:
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
            c_drum_aturatedwater_enthalpy = seuif97.h_p(
                ((float(val['r_drum_pressure']))))
            if c_drum_aturatedwater_enthalpy >= 0:
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
            c_work_aturatedwater_enthalpy = seuif97.h_p(
                (float(val['c_work_pressure'])))
            if c_work_aturatedwater_enthalpy >= 0:
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
                (float(val['c_work_pressure'])))
            if c_work_steam_pecificvolume >= 0:
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
                (float(val['c_work_pressure']))) - (seuif97.h_p(
                    (float(val['c_work_pressure']))))
            if c_work_latentheat_vaporization >= 0:
                if val['flg'] == 'design':
                    result.c_work_latentheat_vaporization = \
                     c_work_latentheat_vaporization
                elif val['flg'] == 'check':
                    result.c_work_latentheat_vaporization_check = \
                     c_work_latentheat_vaporization
        print(result)
