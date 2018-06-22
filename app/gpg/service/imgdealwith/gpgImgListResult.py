# -*- coding:UTF-8 -*-
from util.imgdealwith.imgInfoModel import ImageInfo
from util.imgdealwith.imagedealwith import imageProcesse
import os
from config import config
from app.gpg.model.gasPowerGeneration_models import GPGFlueGasAirSystem, \
                                                    GPGCirculatingWaterSystem, \
                                                    GPGBoilerOfPTS, \
                                                    GPGBoilerAuxiliaries,\
                                                    GPGTurbineOfPTS

pathGpgSourceImg = config['imgConfig'].GPG_IMG_PATH_SOURCE
pathGpgTargetImg = config['imgConfig'].GPG_IMG_PATH_RESULT


def getGpgImgPath(pathGpgSourceImg, fileName):
    if not os.path.exists(pathGpgSourceImg):
        os.makedirs(pathGpgSourceImg)
    return os.path.join(os.getcwd(), pathGpgSourceImg, fileName)


def imgdealwithExecute(plan_id):
    GpgPcsImgInfoDir = {
        'sourceimgPathName': getGpgImgPath(pathGpgSourceImg, "gpg_pcs.png"),
        'trgimgPathName': getGpgImgPath(pathGpgTargetImg + '/' + str(plan_id), "gpg_pcs_" + str(plan_id) + ".png"),
        'imgInfoList': getGpgPcsImgInfoList(plan_id)
    }

    GpgPtsAImgInfoDir = {
        'sourceimgPathName': getGpgImgPath(pathGpgSourceImg, "gpg_ptsA.png"),
        'trgimgPathName': getGpgImgPath(pathGpgTargetImg + '/' + str(plan_id), "gpg_ptsA_" + str(plan_id) + ".png"),
        'imgInfoList': getGpgPtsAImgInfoList(plan_id)
    }

    GpgPtsBImgInfoDir = {
        'sourceimgPathName': getGpgImgPath(pathGpgSourceImg, "gpg_ptsB.png"),
        'trgimgPathName': getGpgImgPath(pathGpgTargetImg + '/' + str(plan_id), "gpg_ptsB_" + str(plan_id) + ".png"),
        'imgInfoList': getGpgPtsBImgInfoList(plan_id)
    }

    GpgPcwtAImgInfoDir = {
        'sourceimgPathName': getGpgImgPath(pathGpgSourceImg, "gpg_pcwtA.jpg"),
        'trgimgPathName': getGpgImgPath(pathGpgTargetImg + '/' + str(plan_id), "gpg_pcwtA_" + str(plan_id) + ".png"),
        'imgInfoList': getGpgPcwtAImgInfoList(plan_id)
    }

    GpgPcwtBImgInfoDir = {
        'sourceimgPathName': getGpgImgPath(pathGpgSourceImg, "gpg_pcwtB.jpg"),
        'trgimgPathName': getGpgImgPath(pathGpgTargetImg + '/' + str(plan_id), "gpg_pcwtB_" + str(plan_id) + ".png"),
        'imgInfoList': getGpgPcwtBImgInfoList(plan_id)
    }

    imageProcesse(GpgPcsImgInfoDir)

    gpg_CirculatingWaterData = GPGCirculatingWaterSystem.search_CirculatingWater(plan_id)
    cooling_tower_selected_type = getattr(gpg_CirculatingWaterData, 'cooling_tower_selected_type')

    gpg_BoilerAuxiliariesData = GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
    desalted_water_tech_type = getattr(gpg_BoilerAuxiliariesData, 'desalted_water_tech_type')

    if cooling_tower_selected_type != '' and cooling_tower_selected_type is not None:
        if float(cooling_tower_selected_type) == 1.0:
            imageProcesse(GpgPtsAImgInfoDir)
        elif float(cooling_tower_selected_type) == 2.0:
            imageProcesse(GpgPtsBImgInfoDir)

    if desalted_water_tech_type != '' and desalted_water_tech_type is not None:
        if float(desalted_water_tech_type) == 1.0:
            imageProcesse(GpgPcwtAImgInfoDir)
        elif float(desalted_water_tech_type) == 2.0:
            imageProcesse(GpgPcwtBImgInfoDir)


if __name__ == '__main__':
    pass

# 原则性化学水处理系统图A
def getGpgPcwtAImgInfoList(plan_id):
    gpg_BoilerAuxiliariesData = GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
    m_boiler_watersupply_all = getattr(gpg_BoilerAuxiliariesData, 'm_boiler_watersupply_all')
    s_volume = getattr(gpg_BoilerAuxiliariesData, 's_volume')

    return [
        ImageInfo('0', (564, 1647), str(m_boiler_watersupply_all), 30),
        ImageInfo('0', (1375, 2264), str(s_volume), 30)
    ]

# 原则性化学水处理系统图B
def getGpgPcwtBImgInfoList(plan_id):
    gpg_BoilerAuxiliariesData = GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
    m_boiler_watersupply_all = getattr(gpg_BoilerAuxiliariesData, 'm_boiler_watersupply_all')
    s_volume = getattr(gpg_BoilerAuxiliariesData, 's_volume')

    return [
        ImageInfo('0', (560, 1706), str(m_boiler_watersupply_all), 30),
        ImageInfo('0', (1368, 2262), str(s_volume), 30)
    ]

# 原则性热力系统图A
def getGpgPtsAImgInfoList(plan_id):
    gpg_BoilerData = GPGBoilerOfPTS.search_BoilerOfPTS(plan_id)
    superheated_steam_outlet_pressure = getattr(gpg_BoilerData, 'superheated_steam_outlet_pressure')
    superheated_steam_temperature = getattr(gpg_BoilerData, 'superheated_steam_temperature')
    superheated_steam_enthalpy = getattr(gpg_BoilerData, 'superheated_steam_enthalpy')
    steam_output = getattr(gpg_BoilerData, 'steam_output')
    if steam_output == '' or steam_output is None:
        steam_output = '0.0'

    gpg_BoilerAuxiliariesData = GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
    c_sewage_quantity = getattr(gpg_BoilerAuxiliariesData, 'c_sewage_quantity')
    if c_sewage_quantity == '' or c_sewage_quantity is None:
        c_sewage_quantity = '0.0'

    c_work_pressure = getattr(gpg_BoilerAuxiliariesData, 'c_work_pressure')
    c_work_aturatedwater_enthalpy = getattr(gpg_BoilerAuxiliariesData, 'c_work_aturatedwater_enthalpy')
    p_feedpump_total_head = getattr(gpg_BoilerAuxiliariesData, 'p_feedpump_total_head')
    if p_feedpump_total_head == '' or p_feedpump_total_head is None:
        p_feedpump_total_head = '0.0'

    p_flow = getattr(gpg_BoilerAuxiliariesData, 'p_flow')

    gpg_CirculatingWaterData = GPGCirculatingWaterSystem.search_CirculatingWater(plan_id)
    circulation_water_flow_summer = getattr(gpg_CirculatingWaterData, 'circulation_water_flow_summer')
    evaporation_loss = getattr(gpg_CirculatingWaterData, 'evaporation_loss')
    wind_blow_loss = getattr(gpg_CirculatingWaterData, 'wind_blow_loss')
    discharge_capacity = getattr(gpg_CirculatingWaterData, 'discharge_capacity')
    supply_water_amount = getattr(gpg_CirculatingWaterData, 'supply_water_amount')
    spray_area = getattr(gpg_CirculatingWaterData, 'spray_area')

    gpg_TurbineData = GPGTurbineOfPTS.search_TurbineOfPTS(plan_id)
    hh1_water_temperature = getattr(gpg_TurbineData, 'hh1_water_temperature')
    d_water_temperature = getattr(gpg_TurbineData, 'd_water_temperature')
    lh1_water_temperature = getattr(gpg_TurbineData, 'lh1_water_temperature')
    lh2_water_temperature = getattr(gpg_TurbineData, 'lh2_water_temperature')
    c_water_temperature = getattr(gpg_TurbineData, 'c_water_temperature')

    hh1_water_enthalpy = getattr(gpg_TurbineData, 'hh1_water_enthalpy')
    d_water_enthalpy = getattr(gpg_TurbineData, 'd_water_enthalpy')
    lh1_water_enthalpy = getattr(gpg_TurbineData, 'lh1_water_enthalpy')
    lh2_water_enthalpy = getattr(gpg_TurbineData, 'lh2_water_enthalpy')
    c_water_enthalpy = getattr(gpg_TurbineData, 'c_water_enthalpy')

    h_temperature = getattr(gpg_TurbineData, 'h_temperature')
    lh1_saturated_water_temperature = getattr(gpg_TurbineData, 'lh1_saturated_water_temperature')
    lh2_saturated_water_temperature = getattr(gpg_TurbineData, 'lh2_saturated_water_temperature')
    e_steam_flow = getattr(gpg_TurbineData, 'e_steam_flow')
    e_steam_extraction_select = getattr(gpg_TurbineData, 'e_steam_extraction_select')
    h_pressure = getattr(gpg_TurbineData, 'h_pressure')

    lh1_saturated_water_enthalpy = getattr(gpg_TurbineData, 'lh1_saturated_water_enthalpy')
    lh2_saturated_water_enthalpy = getattr(gpg_TurbineData, 'lh2_saturated_water_enthalpy')
    i_exhaust_point_pressure = getattr(gpg_TurbineData, 'i_exhaust_point_pressure')
    i_exhaust_point_temperature = getattr(gpg_TurbineData, 'i_exhaust_point_temperature')
    i_exhaust_point_enthalpy = getattr(gpg_TurbineData, 'i_exhaust_point_enthalpy')
    i_exhaust_point_flow = getattr(gpg_TurbineData, 'i_exhaust_point_flow')
    i_steam_exhaust_pressure = getattr(gpg_TurbineData, 'i_steam_exhaust_pressure')
    i_steam_exhaust_enthalpy_actual = getattr(gpg_TurbineData, 'i_steam_exhaust_enthalpy_actual')
    i_steam_exhaust_flow = getattr(gpg_TurbineData, 'i_steam_exhaust_flow')
    if i_steam_exhaust_flow == '' or i_steam_exhaust_flow is None:
        i_steam_exhaust_flow = '0.0'

    d_work_pressure = getattr(gpg_TurbineData, 'd_work_pressure')  
    d_extraction_pressure = getattr(gpg_TurbineData, 'd_extraction_pressure')
    lh1_extraction_pressure = getattr(gpg_TurbineData, 'lh1_extraction_pressure')
    lh2_extraction_pressure = getattr(gpg_TurbineData, 'lh2_extraction_pressure')

    h_enthalpy = getattr(gpg_TurbineData, 'h_enthalpy')
    d_extraction_enthalpy = getattr(gpg_TurbineData, 'd_extraction_enthalpy')
    lh1_extraction_enthalpy = getattr(gpg_TurbineData, 'lh1_extraction_enthalpy')
    lh2_extraction_enthalpy = getattr(gpg_TurbineData, 'lh2_extraction_enthalpy')

    h_amount = getattr(gpg_TurbineData, 'h_amount')
    if h_amount == '' or h_amount is None:
        h_amount = '0.0'

    d_extraction_amount = getattr(gpg_TurbineData, 'd_extraction_amount')
    lh1_extraction_amount = getattr(gpg_TurbineData, 'lh1_extraction_amount')
    lh2_extraction_amount = getattr(gpg_TurbineData, 'lh2_extraction_amount')

    if lh1_extraction_amount == '' or lh1_extraction_amount is None:
        lh1_extraction_amount = '0.0'
    
    if lh2_extraction_amount == '' or lh2_extraction_amount is None:
        lh2_extraction_amount = '0.0'

    return [
        ImageInfo('0', (161, 621), u'P:压力Mpa', 20),
        ImageInfo('0', (161, 677), u'I:焓值kj/kg', 20),
        ImageInfo('0', (226, 2011), str(c_work_aturatedwater_enthalpy), 20),
        ImageInfo('0', (229, 1955), str(c_work_pressure), 20),
        ImageInfo('0', (232, 1283), str(hh1_water_enthalpy), 20),
        ImageInfo('0', (233, 1230), str(float(p_feedpump_total_head)/100), 20),
        ImageInfo('0', (285, 629), u'T:温度℃', 20),
        ImageInfo('0', (285, 673), u'G:流量t/h', 20),
        ImageInfo('0', (349, 2014), str(float(c_sewage_quantity)/1000), 20),
        ImageInfo('0', (350, 1960), u'—— ——', 20),
        ImageInfo('0', (393, 1236), str(hh1_water_temperature), 20),
        ImageInfo('0', (394, 1283), str(p_flow), 20),
        ImageInfo('0', (516, 816), str(steam_output), 20),
        ImageInfo('0', (744, 2517), str(d_work_pressure), 20),
        ImageInfo('0', (745, 2568), str(d_water_enthalpy), 20),
        ImageInfo('0', (894, 1665), str(d_extraction_enthalpy), 20),
        ImageInfo('0', (896, 1614), str(d_extraction_pressure), 20),
        ImageInfo('0', (912, 2516), str(d_water_temperature), 20),
        ImageInfo('0', (913, 2570), str(steam_output), 20),
        ImageInfo('0', (1053, 1614), u'—— ——', 20),
        ImageInfo('0', (1054, 1665), str(d_extraction_amount), 20),
        ImageInfo('0', (1224, 511), str(superheated_steam_outlet_pressure), 20),
        ImageInfo('0', (1224, 564), str(superheated_steam_enthalpy), 20),
        ImageInfo('0', (1239, 2594), str(h_pressure), 20),
        ImageInfo('0', (1243, 2646), str(h_enthalpy), 20),
        ImageInfo('0', (1251, 2049), u'—— ——', 20),
        ImageInfo('0', (1251, 2106), str(lh1_water_enthalpy), 20),
        ImageInfo('0', (1345, 510), str(superheated_steam_temperature), 20),
        ImageInfo('0', (1345, 567), str(e_steam_flow), 20),
        ImageInfo('0', (1389, 2052), str(lh1_water_temperature), 20),
        ImageInfo('0', (1391, 2107), str(float(lh1_extraction_amount)+float(lh2_extraction_amount)+float(i_steam_exhaust_flow)), 20),
        ImageInfo('0', (1444, 2645), str(float(steam_output)*float(h_amount)), 20),
        ImageInfo('0', (1445, 2594), str(h_temperature), 20),
        ImageInfo('0', (1607, 1670), str(lh1_extraction_enthalpy), 20),
        ImageInfo('0', (1608, 1617), str(lh1_extraction_pressure), 20),
        ImageInfo('0', (1632, 2213), u'—— ——', 20),
        ImageInfo('0', (1633, 2269), str(lh1_saturated_water_enthalpy), 20),
        ImageInfo('0', (1676, 2051), u'—— ——', 20),
        ImageInfo('0', (1678, 2105), str(lh2_water_enthalpy), 20),
        ImageInfo('0', (1737, 1619), u'—— ——', 20),
        ImageInfo('0', (1739, 1671), str(lh1_extraction_amount), 20),
        ImageInfo('0', (1767, 2213), str(lh1_saturated_water_temperature), 20),
        ImageInfo('0', (1769, 2267), str(lh1_extraction_amount), 20),
        ImageInfo('0', (1816, 2051), str(lh2_water_temperature), 20),
        ImageInfo('0', (1817, 2106), str(float(lh1_extraction_amount)+float(lh2_extraction_amount)+float(i_steam_exhaust_flow)), 20),
        ImageInfo('0', (1834, 1103), e_steam_extraction_select, 20),
        ImageInfo('0', (1951, 1673), str(lh2_extraction_enthalpy), 20),
        ImageInfo('0', (1956, 1618), str(lh2_extraction_pressure), 20),
        ImageInfo('0', (2003, 2267), str(lh2_saturated_water_enthalpy), 20),
        ImageInfo('0', (2005, 916), str(i_exhaust_point_pressure), 20),
        ImageInfo('0', (2005, 971), str(i_exhaust_point_enthalpy), 20),
        ImageInfo('0', (2005, 2216), u'—— ——', 20),
        ImageInfo('0', (2083, 2050), u'—— ——', 20),
        ImageInfo('0', (2084, 2107), str(c_water_enthalpy), 20),
        ImageInfo('0', (2086, 1674), str(lh2_extraction_amount), 20),
        ImageInfo('0', (2090, 1619), u'—— ——', 20),
        ImageInfo('0', (2140, 2216), str(lh2_saturated_water_temperature), 20),
        ImageInfo('0', (2141, 973), str(i_exhaust_point_flow), 20),
        ImageInfo('0', (2142, 2267), str(float(lh1_extraction_amount)+float(lh2_extraction_amount)), 20),
        ImageInfo('0', (2143, 918), str(i_exhaust_point_temperature), 20),
        ImageInfo('0', (2220, 2053), str(c_water_temperature), 20),
        ImageInfo('0', (2220, 2108), str(float(lh1_extraction_amount)+float(lh2_extraction_amount)+float(i_steam_exhaust_flow)), 20),
        ImageInfo('0', (2551, 1390), str(i_steam_exhaust_enthalpy_actual), 20),
        ImageInfo('0', (2553, 1336), str(i_steam_exhaust_pressure), 20),
        ImageInfo('0', (2696, 1337), u'—— ——', 20),
        ImageInfo('0', (2698, 1391), str(i_steam_exhaust_flow), 20),
        ImageInfo('0', (2735, 1731), u'—— ——', 20),
        ImageInfo('0', (2737, 1785), u'—— ——', 20),
        ImageInfo('0', (2783, 1133), e_steam_extraction_select, 20),
        ImageInfo('0', (2858, 1731), u'20/33', 20),
        ImageInfo('0', (2859, 1784), str(circulation_water_flow_summer), 20),
        ImageInfo('0', (2878, 1337), u'—— ——', 20),
        ImageInfo('0', (2880, 1390), u'—— ——', 20),
        ImageInfo('0', (2998, 1338), u'30/43', 20),
        ImageInfo('0', (2998, 1391), str(circulation_water_flow_summer), 20),
        ImageInfo('0', (3263, 988), str(evaporation_loss), 20),
        ImageInfo('0', (3313, 1839), str(spray_area), 20),
        ImageInfo('0', (3478, 2214), str(discharge_capacity), 20),
        ImageInfo('0', (3790, 990), str(wind_blow_loss), 20),
        ImageInfo('0', (4350, 2130), str(supply_water_amount), 20)
    ]

# 原则性热力系统图B
def getGpgPtsBImgInfoList(plan_id):
    gpg_BoilerData = GPGBoilerOfPTS.search_BoilerOfPTS(plan_id)
    superheated_steam_outlet_pressure = getattr(gpg_BoilerData, 'superheated_steam_outlet_pressure')
    superheated_steam_temperature = getattr(gpg_BoilerData, 'superheated_steam_temperature')
    superheated_steam_enthalpy = getattr(gpg_BoilerData, 'superheated_steam_enthalpy')
    steam_output = getattr(gpg_BoilerData, 'steam_output')
    if steam_output == '' or steam_output is None:
        steam_output = '0.0'

    gpg_BoilerAuxiliariesData = GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
    c_sewage_quantity = getattr(gpg_BoilerAuxiliariesData, 'c_sewage_quantity')
    if c_sewage_quantity == '' or c_sewage_quantity is None:
        c_sewage_quantity = '0.0'

    c_work_pressure = getattr(gpg_BoilerAuxiliariesData, 'c_work_pressure')
    c_work_aturatedwater_enthalpy = getattr(gpg_BoilerAuxiliariesData, 'c_work_aturatedwater_enthalpy')
    p_feedpump_total_head = getattr(gpg_BoilerAuxiliariesData, 'p_feedpump_total_head')
    if p_feedpump_total_head == '' or p_feedpump_total_head is None:
        p_feedpump_total_head = '0.0'

    p_flow = getattr(gpg_BoilerAuxiliariesData, 'p_flow')

    gpg_CirculatingWaterData = GPGCirculatingWaterSystem.search_CirculatingWater(plan_id)
    circulation_water_flow_summer = getattr(gpg_CirculatingWaterData, 'circulation_water_flow_summer')
    evaporation_loss = getattr(gpg_CirculatingWaterData, 'evaporation_loss')
    wind_blow_loss = getattr(gpg_CirculatingWaterData, 'wind_blow_loss')
    discharge_capacity = getattr(gpg_CirculatingWaterData, 'discharge_capacity')
    supply_water_amount = getattr(gpg_CirculatingWaterData, 'supply_water_amount')
    selected_total_circulation_water_flow = getattr(gpg_CirculatingWaterData, 'selected_total_circulation_water_flow')

    gpg_TurbineData = GPGTurbineOfPTS.search_TurbineOfPTS(plan_id)
    hh1_water_temperature = getattr(gpg_TurbineData, 'hh1_water_temperature')
    d_water_temperature = getattr(gpg_TurbineData, 'd_water_temperature')
    lh1_water_temperature = getattr(gpg_TurbineData, 'lh1_water_temperature')
    lh2_water_temperature = getattr(gpg_TurbineData, 'lh2_water_temperature')
    c_water_temperature = getattr(gpg_TurbineData, 'c_water_temperature')

    hh1_water_enthalpy = getattr(gpg_TurbineData, 'hh1_water_enthalpy')
    d_water_enthalpy = getattr(gpg_TurbineData, 'd_water_enthalpy')
    lh1_water_enthalpy = getattr(gpg_TurbineData, 'lh1_water_enthalpy')
    lh2_water_enthalpy = getattr(gpg_TurbineData, 'lh2_water_enthalpy')
    c_water_enthalpy = getattr(gpg_TurbineData, 'c_water_enthalpy')

    h_temperature = getattr(gpg_TurbineData, 'h_temperature')
    lh1_saturated_water_temperature = getattr(gpg_TurbineData, 'lh1_saturated_water_temperature')
    lh2_saturated_water_temperature = getattr(gpg_TurbineData, 'lh2_saturated_water_temperature')
    e_throttle_flow = getattr(gpg_TurbineData, 'e_throttle_flow')
    e_steam_extraction_select = getattr(gpg_TurbineData, 'e_steam_extraction_select')
    h_pressure = getattr(gpg_TurbineData, 'h_pressure')

    lh1_saturated_water_enthalpy = getattr(gpg_TurbineData, 'lh1_saturated_water_enthalpy')
    lh2_saturated_water_enthalpy = getattr(gpg_TurbineData, 'lh2_saturated_water_enthalpy')
    i_exhaust_point_pressure = getattr(gpg_TurbineData, 'i_exhaust_point_pressure')
    i_exhaust_point_temperature = getattr(gpg_TurbineData, 'i_exhaust_point_temperature')
    i_exhaust_point_enthalpy = getattr(gpg_TurbineData, 'i_exhaust_point_enthalpy')
    i_exhaust_point_flow = getattr(gpg_TurbineData, 'i_exhaust_point_flow')
    i_steam_exhaust_pressure = getattr(gpg_TurbineData, 'i_steam_exhaust_pressure')
    i_steam_exhaust_enthalpy_actual = getattr(gpg_TurbineData, 'i_steam_exhaust_enthalpy_actual')
    i_steam_exhaust_flow = getattr(gpg_TurbineData, 'i_steam_exhaust_flow')
    if i_steam_exhaust_flow == '' or i_steam_exhaust_flow is None:
        i_steam_exhaust_flow = '0.0'

    d_work_pressure = getattr(gpg_TurbineData, 'd_work_pressure')  
    d_extraction_pressure = getattr(gpg_TurbineData, 'd_extraction_pressure')
    lh1_extraction_pressure = getattr(gpg_TurbineData, 'lh1_extraction_pressure')
    lh2_extraction_pressure = getattr(gpg_TurbineData, 'lh2_extraction_pressure')

    h_enthalpy = getattr(gpg_TurbineData, 'h_enthalpy')
    d_extraction_enthalpy = getattr(gpg_TurbineData, 'd_extraction_enthalpy')
    lh1_extraction_enthalpy = getattr(gpg_TurbineData, 'lh1_extraction_enthalpy')
    lh2_extraction_enthalpy = getattr(gpg_TurbineData, 'lh2_extraction_enthalpy')

    h_amount = getattr(gpg_TurbineData, 'h_amount')
    if h_amount == '' or h_amount is None:
        h_amount = '0.0'

    d_extraction_amount = getattr(gpg_TurbineData, 'd_extraction_amount')
    lh1_extraction_amount = getattr(gpg_TurbineData, 'lh1_extraction_amount')
    lh2_extraction_amount = getattr(gpg_TurbineData, 'lh2_extraction_amount')

    if lh1_extraction_amount == '' or lh1_extraction_amount is None:
        lh1_extraction_amount = '0.0'
    
    if lh2_extraction_amount == '' or lh2_extraction_amount is None:
        lh2_extraction_amount = '0.0'

    return [
        ImageInfo('0', (204, 1985), str(c_work_aturatedwater_enthalpy), 20),
        ImageInfo('0', (204, 1933), str(c_work_pressure), 20),
        ImageInfo('0', (204, 1317), str(hh1_water_enthalpy), 20),
        ImageInfo('0', (200, 1264), str(float(p_feedpump_total_head)/100), 20),
        ImageInfo('0', (314, 1984), str(float(c_sewage_quantity)/1000), 20),
        ImageInfo('0', (316, 1934), u'—— ——', 20),
        ImageInfo('0', (354, 1269), str(hh1_water_temperature), 20),
        ImageInfo('0', (353, 1320), str(p_flow), 20),
        ImageInfo('0', (466, 896), str(steam_output), 20),
        ImageInfo('0', (673, 2440), str(d_work_pressure), 20),
        ImageInfo('0', (673, 2491), str(d_water_enthalpy), 20),
        ImageInfo('0', (811, 1662), str(d_extraction_enthalpy), 20),
        ImageInfo('0', (810, 1614), str(d_extraction_pressure), 20),
        ImageInfo('0', (829, 2440), str(d_water_temperature), 20),
        ImageInfo('0', (830, 2490), str(steam_output), 20),
        ImageInfo('0', (953, 1614), u'—— ——', 20),
        ImageInfo('0', (954, 1662), str(d_extraction_amount), 20),
        ImageInfo('0', (1109, 606), str(superheated_steam_outlet_pressure), 20),
        ImageInfo('0', (1109, 658), str(superheated_steam_enthalpy), 20),        
        ImageInfo('0', (1127, 2511), str(h_pressure), 20),
        ImageInfo('0', (1127, 2561), str(h_enthalpy), 20),
        ImageInfo('0', (1137, 2016), u'—— ——', 20),
        ImageInfo('0', (1137, 2065), str(lh1_water_enthalpy), 20),
        ImageInfo('0', (1218, 607), str(superheated_steam_temperature), 20),
        ImageInfo('0', (1220, 658), str(e_throttle_flow), 20),
        ImageInfo('0', (1263, 2015), str(lh1_water_temperature), 20),
        ImageInfo('0', (1266, 2067), str(float(lh1_extraction_amount)+float(lh2_extraction_amount)+float(i_steam_exhaust_flow)), 20),
        ImageInfo('0', (1311, 2560), str(float(steam_output)*float(h_amount)), 20),
        ImageInfo('0', (1310, 2510), str(h_temperature), 20),
        ImageInfo('0', (1460, 1668), str(lh1_extraction_enthalpy), 20),
        ImageInfo('0', (1460, 1620), str(lh1_extraction_pressure), 20),
        ImageInfo('0', (1486, 2166), u'—— ——', 20),
        ImageInfo('0', (1487, 2216), str(lh1_saturated_water_enthalpy), 20),
        ImageInfo('0', (1521, 2016), u'—— ——', 20),
        ImageInfo('0', (1522, 2064), str(lh2_water_enthalpy), 20),
        ImageInfo('0', (1578, 1619), u'—— ——', 20),
        ImageInfo('0', (1580, 1672), str(lh1_extraction_amount), 20),
        ImageInfo('0', (1608, 2167), str(lh1_saturated_water_temperature), 20),
        ImageInfo('0', (1608, 2218), str(lh1_extraction_amount), 20),
        ImageInfo('0', (1646, 2016), str(lh2_water_temperature), 20),
        ImageInfo('0', (1646, 2064), str(float(lh1_extraction_amount)+float(lh2_extraction_amount)+float(i_steam_exhaust_flow)), 20),
        ImageInfo('0', (1675, 1156), e_steam_extraction_select, 20),
        ImageInfo('0', (1775, 1669), str(lh2_extraction_enthalpy), 20),
        ImageInfo('0', (1774, 1618), str(lh2_extraction_pressure), 20),
        ImageInfo('0', (1820, 2217), str(lh2_saturated_water_enthalpy), 20),
        ImageInfo('0', (1826, 981), str(i_exhaust_point_pressure), 20),
        ImageInfo('0', (1828, 1030), str(i_exhaust_point_enthalpy), 20),
        ImageInfo('0', (1819, 2166), u'—— ——', 20),
        ImageInfo('0', (1892, 2017), u'—— ——', 20),
        ImageInfo('0', (1892, 2068), str(c_water_enthalpy), 20),
        ImageInfo('0', (1894, 1672), str(lh2_extraction_amount), 20),
        ImageInfo('0', (1895, 1619), u'—— ——', 20),
        ImageInfo('0', (1942, 2164), str(lh2_saturated_water_temperature), 20),
        ImageInfo('0', (1949, 1029), str(i_exhaust_point_flow), 20),
        ImageInfo('0', (1940, 2216), str(float(lh1_extraction_amount)+float(lh2_extraction_amount)), 20),
        ImageInfo('0', (1947, 981), str(i_exhaust_point_temperature), 20),
        ImageInfo('0', (2015, 2019), str(c_water_temperature), 20),
        ImageInfo('0', (2019, 2068), str(float(lh1_extraction_amount)+float(lh2_extraction_amount)+float(i_steam_exhaust_flow)), 20),
        ImageInfo('0', (2326, 1413), str(i_steam_exhaust_enthalpy_actual), 20),
        ImageInfo('0', (2326, 1364), str(i_steam_exhaust_pressure), 20),
        ImageInfo('0', (2457, 1364), u'—— ——', 20),
        ImageInfo('0', (2457, 1413), str(i_steam_exhaust_flow), 20),
        ImageInfo('0', (2492, 1723), u'—— ——', 20),
        ImageInfo('0', (2494, 1774), u'—— ——', 20),
        ImageInfo('0', (2359, 1181), e_steam_extraction_select, 20),
        ImageInfo('0', (2602, 1724), u'20/33', 20),
        ImageInfo('0', (2603, 1773), str(circulation_water_flow_summer), 20),
        ImageInfo('0', (2621, 1364), u'—— ——', 20),
        ImageInfo('0', (2620, 1413), u'—— ——', 20),
        ImageInfo('0', (2731, 1364), u'30/43', 20),
        ImageInfo('0', (2730, 1413), str(circulation_water_flow_summer), 20),
        ImageInfo('0', (3125, 1144), str(evaporation_loss), 20),
        ImageInfo('0', (3179, 1419), str(selected_total_circulation_water_flow), 20),
        ImageInfo('0', (3456, 2226), str(discharge_capacity), 20),
        ImageInfo('0', (3593, 1143), str(wind_blow_loss), 20),
        ImageInfo('0', (4412, 2151), str(supply_water_amount), 20)
    ]

# 原则性燃烧系统图
def getGpgPcsImgInfoList(plan_id):
    gpg_GasAirData = GPGFlueGasAirSystem.search_FlueGasAirSystem(plan_id)

    blower_air_temperature = getattr(gpg_GasAirData, 'blower_air_temperature')
    blower_fan_selected_total_pressure = getattr(gpg_GasAirData, 'blower_fan_selected_total_pressure')
    blower_fan_selected_flux = getattr(gpg_GasAirData, 'blower_fan_selected_flux')
    induced_smoke_temperature = getattr(gpg_GasAirData, 'induced_smoke_temperature')
    induced_fan_selected_total_pressure = getattr(gpg_GasAirData, 'induced_fan_selected_total_pressure')
    induced_fan_selected_flux = getattr(gpg_GasAirData, 'induced_fan_selected_flux')
    s2c_standard_temperature_gas = getattr(gpg_GasAirData, 's2c_standard_temperature_gas')
    s2c_standard_pressure_gas = getattr(gpg_GasAirData, 's2c_standard_pressure_gas')
    s2c_standard_flux_gas = getattr(gpg_GasAirData, 's2c_standard_flux_gas')

    return [
        ImageInfo('0', (2307, 2159), str(s2c_standard_pressure_gas), 20),
        ImageInfo('0', (2308, 1450), str(blower_fan_selected_total_pressure), 20),
        ImageInfo('0', (2308, 1503), u'—— ——', 20),
        ImageInfo('0', (2308, 2210), u'—— ——', 20),
        ImageInfo('0', (2486, 2158), str(s2c_standard_temperature_gas), 20),
        ImageInfo('0', (2486, 2208), str(s2c_standard_flux_gas), 20),
        ImageInfo('0', (2487, 1450), str(blower_air_temperature), 20),
        ImageInfo('0', (2488, 1505), str(blower_fan_selected_flux), 20),
        ImageInfo('0', (3325, 1640), str(induced_fan_selected_total_pressure), 20),
        ImageInfo('0', (3326, 1693), u'—— ——', 20),
        ImageInfo('0', (3505, 1640), str(induced_smoke_temperature), 20),
        ImageInfo('0', (3506, 1691), str(induced_fan_selected_flux), 20)
    ]