# -*- coding:UTF-8 -*-
from util.imgdealwith.imgInfoModel import ImageInfo
from util.imgdealwith.imagedealwith import imageProcesse
from util.get_all_path import GetPath
from app.ccpp import gl


def imgdealwithExecute(ccppobj, turbineobj, plan_id, user_id):

    if ccppobj.boiler_single_or_dula_pressure_design == "singlepot" and turbineobj.s_steam_type_test == 2:
        dbimgInfoDir = {'sourceimgPathName': GetPath.getImgCcppSource("db.png"),
                        'trgimgPathName': GetPath.getImgCcppResult("db", plan_id, user_id),
                        'imgInfoList': get_db_imgInfoList(ccppobj, turbineobj)}
        imageProcesse(dbimgInfoDir)
    if ccppobj.boiler_single_or_dula_pressure_design == "singlepot" and turbineobj.s_steam_type_test == 1:
        dcimgInfoDir = {'sourceimgPathName': GetPath.getImgCcppSource("dc.png"),
                        'trgimgPathName': GetPath.getImgCcppResult("dc", plan_id, user_id),
                        'imgInfoList': get_dc_imgInfoList(ccppobj, turbineobj)}
        imageProcesse(dcimgInfoDir)
    if ccppobj.boiler_single_or_dula_pressure_design == "singlepot" and turbineobj.s_steam_type_test is None:
        dnimgInfoDir = {'sourceimgPathName': GetPath.getImgCcppSource("dn.png"),
                        'trgimgPathName': GetPath.getImgCcppResult("dn", plan_id, user_id),
                        'imgInfoList': get_dn_imgInfoList(ccppobj)}
        imageProcesse(dnimgInfoDir)
    if ccppobj.boiler_single_or_dula_pressure_design == "doublepot" and turbineobj.s_steam_type_test == 1:
        scimgInfoDir = {'sourceimgPathName': GetPath.getImgCcppSource("sc.png"),
                        'trgimgPathName': GetPath.getImgCcppResult("sc", plan_id, user_id),
                        'imgInfoList': get_sc_imgInfoList(ccppobj, turbineobj)}
        imageProcesse(scimgInfoDir)
    if ccppobj.boiler_single_or_dula_pressure_design == "doublepot" and turbineobj.s_steam_type_test == 2:
        sbimgInfoDir = {'sourceimgPathName': GetPath.getImgCcppSource("sb.png"),
                        'trgimgPathName': GetPath.getImgCcppResult("sb", plan_id, user_id),
                        'imgInfoList': get_sb_imgInfoList(ccppobj, turbineobj)}
        imageProcesse(sbimgInfoDir)
    if ccppobj.boiler_single_or_dula_pressure_design == "doublepot" and turbineobj.s_steam_type_test == 3:
        sbimgInfoDir = {'sourceimgPathName': GetPath.getImgCcppSource("sbq.png"),
                        'trgimgPathName': GetPath.getImgCcppResult("sbq", plan_id, user_id),
                        'imgInfoList': get_sbq_imgInfoList(ccppobj, turbineobj)}
        imageProcesse(sbimgInfoDir)
    if ccppobj.boiler_single_or_dula_pressure_design == "doublepot" and turbineobj.s_steam_type_test is None:
        snimgInfoDir = {'sourceimgPathName': GetPath.getImgCcppSource("sn.png"),
                        'trgimgPathName': GetPath.getImgCcppResult("sn", plan_id, user_id),
                        'imgInfoList': get_sn_imgInfoList(ccppobj)}
        imageProcesse(snimgInfoDir)


# 单压锅炉+抽凝汽轮机对应的映射关系
def get_dc_imgInfoList(ccppobj, turbineobj):
    return [
        ImageInfo('0', (128, 869), u'给水流量:' + gl.getstrcolm(ccppobj.sp_low_feedwater_flux_design) + u't/h'),
        ImageInfo('0', (129, 777), u'给水压力:' + gl.getstrcolm(ccppobj.sp_low_economizer_pressure_design) + u'Mpa'),
        ImageInfo('0', (129, 823), u'给水温度:' + gl.getstrcolm(ccppobj.sp_low_feedwater_temperature_design) + u'℃'),
        ImageInfo('0', (309, 538), u'排烟温度:' + gl.getstrcolm(ccppobj.sp_low_economizer_effluent_smoke_temperature_design) + u'℃'),
        ImageInfo('0', (637, 482), u'主蒸汽温度:' + gl.getstrcolm(ccppobj.sp_steam_temperature_design) + u'℃'),
        ImageInfo('0', (637, 526), u'主蒸汽流量:' + gl.getstrcolm(ccppobj.sp_low_gas_production_design) + u't/h'),
        ImageInfo('0', (638, 435), u'主蒸汽压力:' + gl.getstrcolm(ccppobj.sp_steam_pressure_design) + u'Mpa'),
        ImageInfo('0', (758, 942), u'补燃量:' + gl.getstrcolm(ccppobj.boiler_afterburning_amount_design) + u'Nm3/h'),
        ImageInfo('0', (872, 786), u'排烟温度:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_temperature_design) + u'℃'),
        ImageInfo('0', (872, 833), u'排烟流量:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_flux_design) + u't/h'),
        ImageInfo('0', (1038, 698), u'单机天然气耗量:' + gl.getstrcolm(ccppobj.individual_gas_consumption_design) + u''),
        ImageInfo('0', (1152, 886), u'功率:' + gl.getstrcolm(ccppobj.engine_power_design) + u'MW'),
        # 汽轮机
        ImageInfo('0', (782, 44), u'入口焓:' + gl.getstrcolm(turbineobj.e_steam_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (782, 90), u'入口压力:' + gl.getstrcolm(turbineobj.e_steam_pressure) + u'Mpa'),
        ImageInfo('0', (782, 136), u'入口温度:' + gl.getstrcolm(turbineobj.e_steam_temperature) + u'℃'),
        ImageInfo('0', (782, 182), u'入口流量:' + gl.getstrcolm(turbineobj.e_steam_flow) + u't/h'),
        # 汽轮机:抽气点
        ImageInfo('0', (1064, 380), u'抽气压力:' + gl.getstrcolm(turbineobj.i_exhaust_point_pressure) + u'Mpa'),
        ImageInfo('0', (1064, 427), u'抽气温度:' + gl.getstrcolm(turbineobj.i_exhaust_point_temperature) + u'℃'),
        ImageInfo('0', (1064, 472), u'抽气流量:' + gl.getstrcolm(turbineobj.i_exhaust_point_flow) + u't/h'),
        ImageInfo('0', (1064, 519), u'抽气焓:' + gl.getstrcolm(turbineobj.i_exhaust_point_enthalpy) + u'kJ/kg'),
        # 汽轮机
        ImageInfo('0', (1154, 252), u'功率:' + gl.getstrcolm(turbineobj.i_total_power) + u'MW'),
        # 汽轮机：乏汽
        ImageInfo('0', (1320, 93), u'出口压力:' + gl.getstrcolm(turbineobj.e_exhaust_after_pressure) + u'Mpa'),
        ImageInfo('0', (1320, 140), u'出口焓:' + gl.getstrcolm(turbineobj.i_steam_exhaust_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (1320, 186), u'出口流量:' + gl.getstrcolm(turbineobj.e_exhaust_after_steam) + u't/h'),
    ]


# 单压锅炉+背压汽轮机对应的映射关系
def get_db_imgInfoList(ccppobj, turbineobj):

    return [
        ImageInfo('0', (128, 869), u'给水流量:' + gl.getstrcolm(ccppobj.sp_low_feedwater_flux_design) + u't/h'),
        ImageInfo('0', (129, 777), u'给水压力:' + gl.getstrcolm(ccppobj.sp_low_economizer_pressure_design) + u'Mpa'),
        ImageInfo('0', (129, 823), u'给水温度:' + gl.getstrcolm(ccppobj.sp_low_feedwater_temperature_design) + u'℃'),
        ImageInfo('0', (309, 538), u'排烟温度:' + gl.getstrcolm(ccppobj.sp_low_economizer_effluent_smoke_temperature_design) + u'℃'),
        ImageInfo('0', (637, 482), u'主蒸汽温度:' + gl.getstrcolm(ccppobj.sp_steam_temperature_design) + u'℃'),
        ImageInfo('0', (637, 526), u'主蒸汽流量:' + gl.getstrcolm(ccppobj.sp_low_gas_production_design) + u't/h'),
        ImageInfo('0', (638, 435), u'主蒸汽压力:' + gl.getstrcolm(ccppobj.sp_steam_pressure_design) + u'Mpa'),
        ImageInfo('0', (758, 942), u'补燃量:' + gl.getstrcolm(ccppobj.boiler_afterburning_amount_design) + u'Nm3/h'),
        ImageInfo('0', (872, 786), u'排烟温度:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_temperature_design) + u'℃'),
        ImageInfo('0', (872, 833), u'排烟流量:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_flux_design) + u't/h'),
        ImageInfo('0', (1038, 698), u'单机天然气耗量:' + gl.getstrcolm(ccppobj.individual_gas_consumption_design) + u''),
        ImageInfo('0', (1152, 886), u'功率:' + gl.getstrcolm(ccppobj.engine_power_design) + u'MW'),
        # 汽轮机
        ImageInfo('0', (782, 44), u'入口焓:' + gl.getstrcolm(turbineobj.e_steam_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (782, 90), u'入口压力:' + gl.getstrcolm(turbineobj.e_steam_pressure) + u'Mpa'),
        ImageInfo('0', (782, 136), u'入口温度:' + gl.getstrcolm(turbineobj.e_steam_temperature) + u'℃'),
        ImageInfo('0', (782, 182), u'入口流量:' + gl.getstrcolm(turbineobj.e_steam_flow) + u't/h'),
        # 汽轮机
        ImageInfo('0', (1154, 252), u'功率:' + gl.getstrcolm(turbineobj.i_total_power) + u'MW'),

        ImageInfo('0', (1320, 93), u'出口压力:' + gl.getstrcolm(turbineobj.e_exhaust_after_pressure) + u'Mpa'),
        ImageInfo('0', (1320, 140), u'出口焓:' + gl.getstrcolm(turbineobj.i_steam_exhaust_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (1320, 186), u'出口流量:' + gl.getstrcolm(turbineobj.e_exhaust_after_steam) + u't/h'),
    ]


# 单压锅炉+不带汽轮机对应的映射关系
def get_dn_imgInfoList(ccppobj):

    return [
        ImageInfo('0', (128, 869), u'给水流量:' + gl.getstrcolm(ccppobj.sp_low_feedwater_flux_design) + u't/h'),
        ImageInfo('0', (129, 777), u'给水压力:' + gl.getstrcolm(ccppobj.sp_low_economizer_pressure_design) + u'Mpa'),
        ImageInfo('0', (129, 823), u'给水温度:' + gl.getstrcolm(ccppobj.sp_low_feedwater_temperature_design) + u'℃'),
        ImageInfo('0', (309, 538), u'排烟温度:' + gl.getstrcolm(ccppobj.sp_low_economizer_effluent_smoke_temperature_design) + u'℃'),
        ImageInfo('0', (637, 482), u'主蒸汽温度:' + gl.getstrcolm(ccppobj.sp_steam_temperature_design) + u'℃'),
        ImageInfo('0', (637, 526), u'主蒸汽流量:' + gl.getstrcolm(ccppobj.sp_low_gas_production_design) + u't/h'),
        ImageInfo('0', (638, 435), u'主蒸汽压力:' + gl.getstrcolm(ccppobj.sp_steam_pressure_design) + u'Mpa'),
        ImageInfo('0', (758, 942), u'补燃量:' + gl.getstrcolm(ccppobj.boiler_afterburning_amount_design) + u'Nm3/h'),
        ImageInfo('0', (872, 786), u'排烟温度:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_temperature_design) + u'℃'),
        ImageInfo('0', (872, 833), u'排烟流量:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_flux_design) + u't/h'),
        ImageInfo('0', (1038, 698), u'单机天然气耗量:' + gl.getstrcolm(ccppobj.individual_gas_consumption_design) + u''),
        ImageInfo('0', (1152, 886), u'功率:' + gl.getstrcolm(ccppobj.engine_power_design) + u'MW'),
    ]


# 双压锅炉+抽凝汽轮机对应的映射关系
def get_sc_imgInfoList(ccppobj, turbineobj):

    return [
        ImageInfo('0', (129, 907), u'给水温度:' + gl.getstrcolm(ccppobj.low_feedwater_temperature_design) + u'℃'),
        ImageInfo('0', (129, 953), u'给水流量:' + gl.getstrcolm(ccppobj.low_feedwater_flux_design) + u't/h'),
        ImageInfo('0', (184, 572), u'排烟温度:' + gl.getstrcolm(ccppobj.low_economizer_effluent_smoke_temperature_design) + u'℃'),
        
        ImageInfo('0', (645, 446), u'低压蒸汽压力:' + gl.getstrcolm(ccppobj.low_drum_pressure_design) + u'Mpa'),
        ImageInfo('0', (645, 492), u'低压蒸汽温度:' + gl.getstrcolm(ccppobj.low_superheat_steam_temperature_design) + u'℃'),
        ImageInfo('0', (645, 538), u'低压蒸汽流量:' + gl.getstrcolm(ccppobj.low_gas_production_design) + u't/h'),
        
        ImageInfo('0', (739, 942), u'补燃量:' + gl.getstrcolm(ccppobj.boiler_afterburning_amount_design) + u'Nm3/h'),
        ImageInfo('0', (813, 759), u'排烟温度:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_temperature_design) + u'℃'),
        ImageInfo('0', (813, 805), u'排烟流量:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_flux_design) + u't/h'),

        ImageInfo('0', (898, 552), u'主蒸汽压力:' + gl.getstrcolm(ccppobj.high_steam_pressure_design) + u'Mpa'),
        ImageInfo('0', (898, 599), u'主蒸汽温度:' + gl.getstrcolm(ccppobj.high_steam_temperature_design) + u'℃'),
        ImageInfo('0', (898, 645), u'主蒸汽流量:' + gl.getstrcolm(ccppobj.high_gas_production_design) + u't/h'),

        ImageInfo('0', (1024, 695), u'单机天然气耗量:' + gl.getstrcolm(ccppobj.individual_gas_consumption_design) + u''),
        ImageInfo('0', (1134, 872), u'功率:' + gl.getstrcolm(ccppobj.engine_power_design) + u'MW'),

        ImageInfo('0', (750, 27), u'入口焓:' + gl.getstrcolm(turbineobj.e_steam_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (750, 73), u'入口压力:' + gl.getstrcolm(turbineobj.e_steam_pressure) + u'Mpa'),
        ImageInfo('0', (750, 119), u'入口温度:' + gl.getstrcolm(turbineobj.e_steam_temperature) + u'℃'),
        ImageInfo('0', (750, 165), u'入口流量:' + gl.getstrcolm(turbineobj.e_steam_flow) + u't/h'),
        

        ImageInfo('0', (1045, 346), u'抽气压力:' + gl.getstrcolm(turbineobj.i_exhaust_point_pressure) + u'Mpa'),
        ImageInfo('0', (1045, 392), u'抽气温度:' + gl.getstrcolm(turbineobj.i_exhaust_point_temperature) + u'℃'),
        ImageInfo('0', (1045, 438), u'抽气流量:' + gl.getstrcolm(turbineobj.i_exhaust_point_flow) + u't/h'),
        ImageInfo('0', (1045, 484), u'抽气焓:' + gl.getstrcolm(turbineobj.i_exhaust_point_enthalpy) + u'kJ/kg'),


        ImageInfo('0', (1142, 243), u'功率:' + gl.getstrcolm(turbineobj.i_total_power) + u'MW'),

        ImageInfo('0', (1327, 104), u'出口压力:' + gl.getstrcolm(turbineobj.e_exhaust_after_pressure) + u'Mpa'),
        ImageInfo('0', (1327, 150), u'出口焓:' + gl.getstrcolm(turbineobj.i_steam_exhaust_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (1327, 196), u'出口流量:' + gl.getstrcolm(turbineobj.e_exhaust_after_steam) + u't/h'),
    ]


# 双压锅炉+背压汽轮机对应的映射关系
def get_sb_imgInfoList(ccppobj, turbineobj):

    return [
        ImageInfo('0', (129, 907), u'给水温度:' + gl.getstrcolm(ccppobj.low_feedwater_temperature_design) + u'℃'),
        ImageInfo('0', (129, 953), u'给水流量:' + gl.getstrcolm(ccppobj.low_feedwater_flux_design) + u't/h'),
        ImageInfo('0', (184, 572), u'排烟温度:' + gl.getstrcolm(ccppobj.low_economizer_effluent_smoke_temperature_design) + u'℃'),
        
        ImageInfo('0', (645, 446), u'低压蒸汽压力:' + gl.getstrcolm(ccppobj.low_drum_pressure_design) + u'Mpa'),
        ImageInfo('0', (645, 492), u'低压蒸汽温度:' + gl.getstrcolm(ccppobj.low_superheat_steam_temperature_design) + u'℃'),
        ImageInfo('0', (645, 538), u'低压蒸汽流量:' + gl.getstrcolm(ccppobj.low_gas_production_design) + u't/h'),
        
        ImageInfo('0', (739, 942), u'补燃量:' + gl.getstrcolm(ccppobj.boiler_afterburning_amount_design) + u'Nm3/h'),
        ImageInfo('0', (813, 759), u'排烟温度:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_temperature_design) + u'℃'),
        ImageInfo('0', (813, 805), u'排烟流量:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_flux_design) + u't/h'),

        ImageInfo('0', (898, 552), u'主蒸汽压力:' + gl.getstrcolm(ccppobj.high_steam_pressure_design) + u'Mpa'),
        ImageInfo('0', (898, 599), u'主蒸汽温度:' + gl.getstrcolm(ccppobj.high_steam_temperature_design) + u'℃'),
        ImageInfo('0', (898, 645), u'主蒸汽流量:' + gl.getstrcolm(ccppobj.high_gas_production_design) + u't/h'),

        ImageInfo('0', (1024, 695), u'单机天然气耗量:' + gl.getstrcolm(ccppobj.individual_gas_consumption_design) + u''),
        ImageInfo('0', (1134, 872), u'功率:' + gl.getstrcolm(ccppobj.engine_power_design) + u'MW'),

        ImageInfo('0', (750, 27), u'入口焓:' + gl.getstrcolm(turbineobj.e_steam_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (750, 73), u'入口压力:' + gl.getstrcolm(turbineobj.e_steam_pressure) + u'Mpa'),
        ImageInfo('0', (750, 119), u'入口温度:' + gl.getstrcolm(turbineobj.e_steam_temperature) + u'℃'),
        ImageInfo('0', (750, 165), u'入口流量:' + gl.getstrcolm(turbineobj.e_steam_flow) + u't/h'),

        ImageInfo('0', (1142, 243), u'功率:' + gl.getstrcolm(turbineobj.i_total_power) + u'MW'),

        ImageInfo('0', (1327, 104), u'出口压力:' + gl.getstrcolm(turbineobj.e_exhaust_after_pressure) + u'Mpa'),
        ImageInfo('0', (1327, 150), u'出口焓:' + gl.getstrcolm(turbineobj.i_steam_exhaust_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (1327, 196), u'出口流量:' + gl.getstrcolm(turbineobj.e_exhaust_after_steam) + u't/h'),
    ]


# 双压锅炉+补气汽轮机对应的映射关系
def get_sbq_imgInfoList(ccppobj, turbineobj):

    return [
        ImageInfo('0', (113, 926), u'给水温度:' + gl.getstrcolm(ccppobj.low_feedwater_temperature_design) + u'℃'),
        ImageInfo('0', (113, 964), u'给水流量:' + gl.getstrcolm(ccppobj.low_feedwater_flux_design) + u't/h'),
        ImageInfo('0', (151, 570), u'排烟温度:' + gl.getstrcolm(ccppobj.low_economizer_effluent_smoke_temperature_design) + u'℃'),
        ImageInfo('0', (234, 376), u'蒸汽流量:' + gl.getstrcolm(ccppobj.high_gas_production_design) + u't/h'),
        ImageInfo('0', (250, 492), u'蒸汽流量:' + gl.getstrcolm(ccppobj.high_gas_production_design) + u't/h'),
        ImageInfo('0', (657, 456), u'低压蒸汽压力:' + gl.getstrcolm(ccppobj.low_drum_pressure_design) + u'Mpa'),
        ImageInfo('0', (657, 529), u'低压蒸汽流量:' + gl.getstrcolm(ccppobj.low_gas_production_design) + u't/h'),
        ImageInfo('0', (658, 493), u'低压蒸汽温度:' + gl.getstrcolm(ccppobj.low_superheat_steam_temperature_design) + u'℃'),
        ImageInfo('0', (703, 930), u'补燃量:' + gl.getstrcolm(ccppobj.boiler_afterburning_amount_design) + u'Nm3/h'),
        
        ImageInfo('0', (724, 54), u'入口焓:' + gl.getstrcolm(turbineobj.e_steam_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (724, 91), u'入口压力:' + gl.getstrcolm(turbineobj.e_steam_pressure) + u'Mpa'),
        ImageInfo('0', (724, 128), u'入口温度:' + gl.getstrcolm(turbineobj.e_steam_temperature) + u'℃'),
        ImageInfo('0', (724, 163), u'入口流量:' + gl.getstrcolm(turbineobj.e_steam_flow) + u't/h'),

        ImageInfo('0', (842, 765), u'排烟温度:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_temperature_design) + u'℃'),
        ImageInfo('0', (845, 812), u'排烟流量:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_flux_design) + u't/h'),
        ImageInfo('0', (900, 527), u'主蒸汽压力:' + gl.getstrcolm(ccppobj.high_steam_pressure_design) + u'Mpa'),
        ImageInfo('0', (901, 572), u'主蒸汽温度:' + gl.getstrcolm(ccppobj.high_steam_temperature_design) + u'℃'),
        ImageInfo('0', (901, 619), u'主蒸汽流量:' + gl.getstrcolm(ccppobj.high_gas_production_design) + u't/h'),
        ImageInfo('0', (979, 658), u'单机天然气耗量:' + gl.getstrcolm(ccppobj.individual_gas_consumption_design) + u''),

        ImageInfo('0', (1038, 385), u'补气压力:' + gl.getstrcolm(turbineobj.i_exhaust_point_pressure) + u'Mpa'),
        ImageInfo('0', (1038, 424), u'补气温度:' + gl.getstrcolm(turbineobj.i_exhaust_point_temperature) + u'℃'),
        ImageInfo('0', (1038, 468), u'补气流量:' + gl.getstrcolm(turbineobj.i_exhaust_point_flow) + u't/h'),
        ImageInfo('0', (1038, 512), u'补气混合焓:' + gl.getstrcolm(turbineobj.i_exhaust_point_enthalpy) + u'kJ/kg'),

        ImageInfo('0', (1114, 892), u'功率:' + gl.getstrcolm(ccppobj.engine_power_design) + u'MW'),
        ImageInfo('0', (1160, 251), u'功率:' + gl.getstrcolm(turbineobj.i_total_power) + u'MW'),

        ImageInfo('0', (1311, 100), u'出口压力:' + gl.getstrcolm(turbineobj.e_exhaust_after_pressure) + u'Mpa'),
        ImageInfo('0', (1311, 136), u'出口焓:' + gl.getstrcolm(turbineobj.i_steam_exhaust_enthalpy) + u'kJ/kg'),
        ImageInfo('0', (1311, 172), u'出口流量:' + gl.getstrcolm(turbineobj.e_exhaust_after_steam) + u't/h'),
    ]


# 双压锅炉+背压汽轮机对应的映射关系
def get_sn_imgInfoList(ccppobj):

    return [
        ImageInfo('0', (129, 907), u'给水温度:' + gl.getstrcolm(ccppobj.low_feedwater_temperature_design) + u'℃'),
        ImageInfo('0', (129, 953), u'给水流量:' + gl.getstrcolm(ccppobj.low_feedwater_flux_design) + u't/h'),
        ImageInfo('0', (184, 572), u'排烟温度:' + gl.getstrcolm(ccppobj.low_economizer_effluent_smoke_temperature_design) + u'℃'),
        
        ImageInfo('0', (645, 446), u'低压蒸汽压力:' + gl.getstrcolm(ccppobj.low_drum_pressure_design) + u'Mpa'),
        ImageInfo('0', (645, 492), u'低压蒸汽温度:' + gl.getstrcolm(ccppobj.low_superheat_steam_temperature_design) + u'℃'),
        ImageInfo('0', (645, 538), u'低压蒸汽流量:' + gl.getstrcolm(ccppobj.low_gas_production_design) + u't/h'),
        
        ImageInfo('0', (739, 942), u'补燃量:' + gl.getstrcolm(ccppobj.boiler_afterburning_amount_design) + u'Nm3/h'),
        ImageInfo('0', (813, 759), u'排烟温度:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_temperature_design) + u'℃'),
        ImageInfo('0', (813, 805), u'排烟流量:' + gl.getstrcolm(ccppobj.engine_exhuast_gas_flux_design) + u't/h'),

        ImageInfo('0', (898, 552), u'主蒸汽压力:' + gl.getstrcolm(ccppobj.high_steam_pressure_design) + u'Mpa'),
        ImageInfo('0', (898, 599), u'主蒸汽温度:' + gl.getstrcolm(ccppobj.high_steam_temperature_design) + u'℃'),
        ImageInfo('0', (898, 645), u'主蒸汽流量:' + gl.getstrcolm(ccppobj.high_gas_production_design) + u't/h'),

        ImageInfo('0', (1024, 695), u'单机天然气耗量:' + gl.getstrcolm(ccppobj.individual_gas_consumption_design) + u''),
        ImageInfo('0', (1134, 872), u'功率:' + gl.getstrcolm(ccppobj.engine_power_design) + u'MW'),
    ]

# def imageProcesse1(dbimgInfoDir):
#     import threading
#     thread_list = []
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     for t in thread_list:
#         t.start()
#     for t in thread_list:
#         t.join()


# def imageProcesse2(dbimgInfoDir):
#     import threading
#     thread_list = []
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     for t in thread_list:
#         t.start()
#     for t in thread_list:
#         t.join()


# def imageProcesse3(dbimgInfoDir):
#     import threading
#     thread_list = []
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     for t in thread_list:
#         t.start()
#     for t in thread_list:
#         t.join()


# def imageProcesse4(dbimgInfoDir):
#     import threading
#     thread_list = []
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     thr = threading.Thread(target=imageProcesse, args=[dbimgInfoDir, ])
#     thread_list.append(thr)
#     for t in thread_list:
#         t.start()
#     for t in thread_list:
#         t.join()
# 调用
# from multiprocessing import Process
# import threading
# process_list = []
# thread_list = []
# pro = Process(target=imageProcesse1, args=(dbimgInfoDir,))
# process_list.append(pro)

# pro = Process(target=imageProcesse2, args=(dbimgInfoDir,))
# process_list.append(pro)

# pro = Process(target=imageProcesse3, args=(dbimgInfoDir,))
# process_list.append(pro)

# pro = Process(target=imageProcesse4, args=(dbimgInfoDir,))
# process_list.append(pro)

# for p in process_list:
#     p.start()
# for p in process_list:
#     p.join()