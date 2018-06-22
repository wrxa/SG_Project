# -*- coding:UTF-8 -*-
from util.imgdealwith.imgInfoModel import ImageInfo
from util.imgdealwith.imagedealwith import imageProcesse
import os
import threading
from config import config
from app.biomass_chp.models.modelsBiomass import BiomassCHPWaterTreatment, \
                            BiomassCHPDASRemove, BiomassCHPBoilerCalculation, \
                            BiomassCHPFuelStorageTransportation, BiomassCHPBoilerAuxiliaries, \
                            BiomassCHPCirculatingWater, BiomassCHPTurbineBackpressure



pathBiomassSourceImg = config['imgConfig'].BIOMASS_IMG_PATH_SOURCE
pathBiomassTargetImg = config['imgConfig'].BIOMASS_IMG_PATH_RESULT

def getBiomassImgPath(pathBiomassSourceImg, fileName):
    if not os.path.exists(pathBiomassSourceImg):
        os.makedirs(pathBiomassSourceImg)

    return os.path.join(os.getcwd(), pathBiomassSourceImg, fileName)

class GetimgInfoList():
    def searchImgData(self, plan_id):
        furnaceCalculation = BiomassCHPBoilerCalculation.search_furnace_calculation(
            plan_id)
        boilerAuxiliaries = BiomassCHPBoilerAuxiliaries.search_auxiliaries(
            plan_id)
        turbineBackpressure = BiomassCHPTurbineBackpressure.search_turbineBackpressure(
            plan_id)
        circulatingWater = BiomassCHPCirculatingWater.search_circulating_water(
            plan_id)

        return furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater

def imgdealwithExecute(plan_id):
    thread_list = []
    # 原则性化学水处理系统图P1
    BiomassWater1ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_water1.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_water1_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssWater1ImgInfoList(plan_id)
    }
    # 原则性化学水处理系统图P2
    BiomassWater2ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_water2.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_water2_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssWater1ImgInfoList(plan_id)
    }

    biomassCHPWaterTreatmentData = BiomassCHPWaterTreatment.search_water(plan_id)
    o_process_route = getattr(biomassCHPWaterTreatmentData, 'o_process_route')
    #根据不同的工艺路线，出力不同的原则性化学水处理系统图
    if o_process_route == "1":
        thr = threading.Thread(target=imageProcesse, args=[BiomassWater1ImgInfoDir, ])
        thread_list.append(thr)

        # imageProcesse(BiomassWater1ImgInfoDir)
    else:
        if o_process_route == "2":
            thr = threading.Thread(target=imageProcesse, args=[BiomassWater2ImgInfoDir, ])
            thread_list.append(thr)
        #   imageProcesse(BiomassWater2ImgInfoDir)  



    # 原则性除灰系统图
    BiomassDustImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_dust.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_dust_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssDustImgInfoList(plan_id)
    } 
    thr = threading.Thread(target=imageProcesse, args=[BiomassDustImgInfoDir, ])
    thread_list.append(thr)
    # imageProcesse(BiomassDustImgInfoDir)


    # 原则性除渣系统图P1
    BiomassAsh1ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_ash1.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_ash1_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssAshImgInfoListP1(plan_id)
    }

    # 原则性除渣系统图P2
    BiomassAsh2ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_ash2.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_ash2_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssAshImgInfoListP2(plan_id)
    }

    biomassCHPBoilerCalculationData = BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
    boiler_type = getattr(biomassCHPBoilerCalculationData, 'boiler_type')
    #根据不同的锅炉种类，出力不同的原则性除渣系统图 
    if boiler_type == "1" or boiler_type == "2":
        thr = threading.Thread(target=imageProcesse, args=[BiomassAsh1ImgInfoDir, ])
        thread_list.append(thr)
        # imageProcesse(BiomassAsh1ImgInfoDir)
    else:
        if boiler_type == "3" or boiler_type == "4":
            thr = threading.Thread(target=imageProcesse, args=[BiomassAsh2ImgInfoDir, ])
            thread_list.append(thr)
            # imageProcesse(BiomassAsh2ImgInfoDir)


    # 原则性燃料输送系统图P1
    BiomassTrans1ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_trans1.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_trans1_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssTransImgInfoListP1(plan_id)
    }

    # 原则性燃料输送系统图P2
    BiomassTrans2ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_trans2.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_trans2_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssTransImgInfoListP2(plan_id)
    }

    biomassCHPFuelStorageTransportationData = BiomassCHPFuelStorageTransportation.search_storage_transportation(plan_id)
    f_belt_number = getattr(biomassCHPFuelStorageTransportationData, 'f_belt_number')

    if f_belt_number == 1.0:
        thr = threading.Thread(target=imageProcesse, args=[BiomassTrans1ImgInfoDir, ])
        thread_list.append(thr)
        # imageProcesse(BiomassTrans1ImgInfoDir)
    else:
        if f_belt_number == 2.0:
            thr = threading.Thread(target=imageProcesse, args=[BiomassTrans2ImgInfoDir, ])
            thread_list.append(thr)
            # imageProcesse(BiomassTrans2ImgInfoDir)

    # 原则性燃烧系统图P1
    BiomassFire1ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_fire1.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_fire1_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssFireImgInfoListP1(plan_id)
    }

    # 原则性燃烧系统图P2
    BiomassFire2ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_fire2.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_fire2_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssFireImgInfoListP2(plan_id)
    }

    # 原则性燃烧系统图P3
    BiomassFire3ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_fire3.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_fire3_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssFireImgInfoListP3(plan_id)
    }

    # 原则性燃烧系统图P4
    BiomassFire4ImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_fire4.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_fire4_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssFireImgInfoListP4(plan_id)
    }

    biomassCHPBoilerCalculationData = BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
    boiler_type = getattr(biomassCHPBoilerCalculationData, 'boiler_type')
    #根据不同的锅炉种类，燃烧系统图 
    if boiler_type == "1":
        thr = threading.Thread(target=imageProcesse, args=[BiomassFire1ImgInfoDir, ])
        thread_list.append(thr)
        # imageProcesse(BiomassFire1ImgInfoDir)

    if boiler_type == "3":
        thr = threading.Thread(target=imageProcesse, args=[BiomassFire2ImgInfoDir, ])
        thread_list.append(thr)
        # imageProcesse(BiomassFire2ImgInfoDir)

    if boiler_type == "2":
        thr = threading.Thread(target=imageProcesse, args=[BiomassFire3ImgInfoDir, ])
        thread_list.append(thr)
        # imageProcesse(BiomassFire3ImgInfoDir)

    if boiler_type == "4":
        thr = threading.Thread(target=imageProcesse, args=[BiomassFire4ImgInfoDir, ])
        thread_list.append(thr)
        # imageProcesse(BiomassFire4ImgInfoDir)


    # 原则性热力系统图P1a
    BiomassHot1aImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_hot1a.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_hot1a_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssHotImgInfoListP1a(plan_id)
    }

    # imageProcesse(BiomassHot1aImgInfoDir)

    # 原则性热力系统图P1b
    BiomassHot1bImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_hot1b.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_hot1b_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssHotImgInfoListP1b(plan_id)
    }

    # imageProcesse(BiomassHot1bImgInfoDir)

    # 原则性热力系统图P2a
    BiomassHot2aImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_hot2a.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_hot2a_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssHotImgInfoListP2a(plan_id)
    }

    # imageProcesse(BiomassHot2aImgInfoDir)

    # 原则性热力系统图P2b
    BiomassHot2bImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_hot2b.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_hot2b_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssHotImgInfoListP2b(plan_id)
    }

    # imageProcesse(BiomassHot2bImgInfoDir)

    # 原则性热力系统图P3a
    BiomassHot3aImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_hot3a.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_hot3a_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssHotImgInfoListP3a(plan_id)
    }

    # imageProcesse(BiomassHot3aImgInfoDir)

    # 原则性热力系统图P3b
    BiomassHot3bImgInfoDir = {
        'sourceimgPathName': getBiomassImgPath(pathBiomassSourceImg, "biomass_hot3b.png"),
        'trgimgPathName': getBiomassImgPath(pathBiomassTargetImg, "biomass_hot3b_" + str(plan_id) + ".png"),
        'imgInfoList': getBiomasssHotImgInfoListP3b(plan_id)
    }

    # imageProcesse(BiomassHot3bImgInfoDir)

    # 根据不同的给水温度，回热级数，冷却塔类型，出力不同的热力系统图
    biomassCHPTurbineBackpressureData = BiomassCHPTurbineBackpressure.search_turbineBackpressure(plan_id)
    biomassCHPCirculatingWaterData = BiomassCHPCirculatingWater.search_circulating_water(plan_id)

    # 给水温度
    hh1_water_temperature = getattr(biomassCHPTurbineBackpressureData, 'hh1_water_temperature')
    # 高加级数
    s_hh_grade = getattr(biomassCHPTurbineBackpressureData, 's_hh_grade')
    # 低加级数
    s_lh_grade = getattr(biomassCHPTurbineBackpressureData, 's_lh_grade')   
    # 冷却塔类型
    p_select = getattr(biomassCHPCirculatingWaterData, 'p_select')

    if hh1_water_temperature == 215 and s_hh_grade == 2 and s_lh_grade == 3:
        if p_select == "1":
            thr = threading.Thread(target=imageProcesse, args=[BiomassHot1aImgInfoDir, ])
            thread_list.append(thr)
            # imageProcesse(BiomassHot1aImgInfoDir)
        else:
            if p_select == "2":
                thr = threading.Thread(target=imageProcesse, args=[BiomassHot1bImgInfoDir, ])
                thread_list.append(thr)
                # imageProcesse(BiomassHot1bImgInfoDir)

    if hh1_water_temperature == 158 and s_hh_grade == 0 and s_lh_grade == 2:
        if p_select == "1":
            thr = threading.Thread(target=imageProcesse, args=[BiomassHot2aImgInfoDir, ])
            thread_list.append(thr)
            # imageProcesse(BiomassHot2aImgInfoDir)
        else:
            if p_select == "2":
                thr = threading.Thread(target=imageProcesse, args=[BiomassHot2bImgInfoDir, ])
                thread_list.append(thr)
                # imageProcesse(BiomassHot2bImgInfoDir)

    if hh1_water_temperature == 150 and s_hh_grade == 1 and s_lh_grade == 1:
        if p_select == "1":
            thr = threading.Thread(target=imageProcesse, args=[BiomassHot3aImgInfoDir, ])
            thread_list.append(thr)
            # imageProcesse(BiomassHot3aImgInfoDir)
        else:
            if p_select == "2":
                thr = threading.Thread(target=imageProcesse, args=[BiomassHot3bImgInfoDir, ])
                thread_list.append(thr)
                # imageProcesse(BiomassHot3bImgInfoDir)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


if __name__ == '__main__':
    pass



# 原则性化学水处理系统图作成
def getBiomasssWater1ImgInfoList(plan_id):
    biomassCHPWaterTreatmentData = BiomassCHPWaterTreatment.search_water(plan_id)
    o_boiler_water_normal = getattr(biomassCHPWaterTreatmentData, 'o_boiler_water_normal')
    o_salt_water_tank = getattr(biomassCHPWaterTreatmentData, 'o_salt_water_tank')

    return [
        ImageInfo('0', (861, 2471), getstrcolm(o_boiler_water_normal), 100),
        ImageInfo('0', (2277, 3447), getstrcolm(o_salt_water_tank), 100)
    ]

# 原则性除灰系统图作成
def getBiomasssDustImgInfoList(plan_id):
    biomassCHPDASRemoveData = BiomassCHPDASRemove.search_dasRemove(plan_id)
    a_gas_consumption = getattr(biomassCHPDASRemoveData, 'a_gas_consumption')
    s_height = getattr(biomassCHPDASRemoveData, 's_height')
    s_diameter = getattr(biomassCHPDASRemoveData, 's_diameter')
    a_volumn = getattr(biomassCHPDASRemoveData, 'a_volumn')
    a_storage_time = getattr(biomassCHPDASRemoveData, 'a_storage_time')

    return [
        ImageInfo('0', (2839, 3879), getstrcolm(a_gas_consumption), 80),
        ImageInfo('0', (4939, 1807), getstrcolm(s_height), 80),
        ImageInfo('0', (4933, 1673), getstrcolm(s_diameter), 80),
        ImageInfo('0', (4945, 1543), getstrcolm(a_volumn), 80),
        ImageInfo('0', (4989, 1415), getstrcolm(a_storage_time), 80)
    ]

# 原则性除渣系统图P1作成
def getBiomasssAshImgInfoListP1(plan_id):
    biomassCHPDASRemoveData = BiomassCHPDASRemove.search_dasRemove(plan_id)
    s_coolwater = getattr(biomassCHPDASRemoveData, 's_coolwater')
    s_yns_output = getattr(biomassCHPDASRemoveData, 's_yns_output')
    s_conveyor_output = getattr(biomassCHPDASRemoveData, 's_conveyor_output')
    s_storage_time = getattr(biomassCHPDASRemoveData, 's_storage_time')
    s_volumn = getattr(biomassCHPDASRemoveData, 's_volumn')
    s_diameter = getattr(biomassCHPDASRemoveData, 's_diameter')
    s_height = getattr(biomassCHPDASRemoveData, 's_height')

    return [
        ImageInfo('0', (1473, 1445), getstrcolm(s_coolwater), 70),#G31
        ImageInfo('0', (2533, 2181), getstrcolm(s_yns_output), 70),#G30
        ImageInfo('0', (2829, 1677), getstrcolm(s_coolwater), 70),#G31
        ImageInfo('0', (3177, 2957), getstrcolm(s_conveyor_output), 70),#G34
        ImageInfo('0', (3529, 1669), getstrcolm(s_coolwater), 70),#G31
        ImageInfo('0', (4415, 2189), getstrcolm(s_yns_output), 70),#G30
        ImageInfo('0', (4921, 1445), getstrcolm(s_coolwater), 70),#G31
        ImageInfo('0', (6823, 2219), getstrcolm(s_height), 50),#G40
        ImageInfo('0', (6829, 2133), getstrcolm(s_diameter), 50),#G39
        ImageInfo('0', (6877, 2041), getstrcolm(s_volumn), 50),#G38
        ImageInfo('0', (6881, 1943), getstrcolm(s_storage_time), 50),#G37
    ]

# 原则性除渣系统图P2作成
def getBiomasssAshImgInfoListP2(plan_id):
    biomassCHPDASRemoveData = BiomassCHPDASRemove.search_dasRemove(plan_id)
    s_conveyor_output = getattr(biomassCHPDASRemoveData, 's_conveyor_output')
    s_storage_time = getattr(biomassCHPDASRemoveData, 's_storage_time')
    s_volumn = getattr(biomassCHPDASRemoveData, 's_volumn')
    s_diameter = getattr(biomassCHPDASRemoveData, 's_diameter')
    s_height = getattr(biomassCHPDASRemoveData, 's_height')

    return [
        ImageInfo('0', (4030, 1797), getstrcolm(s_conveyor_output), 70),#G34
        ImageInfo('0', (7171, 2359), getstrcolm(s_height), 50),#G40
        ImageInfo('0', (7177, 2263), getstrcolm(s_diameter), 50),#G39
        ImageInfo('0', (7220, 2176), getstrcolm(s_volumn), 50),#G38
        ImageInfo('0', (7231, 2081), getstrcolm(s_storage_time), 50),#G37
    ]


# 原则性燃料输送系统图P1作成
def getBiomasssTransImgInfoListP1(plan_id):
    BiomassCHPFuelStorageTransportationData = BiomassCHPFuelStorageTransportation.search_storage_transportation(plan_id)
    d_yardarea_design = getattr(BiomassCHPFuelStorageTransportationData, 'd_yardarea_design')
    d_fuel_reserve_days_design = getattr(BiomassCHPFuelStorageTransportationData, 'd_fuel_reserve_days_design')
    t_single_effective_volume_selected_design = getattr(BiomassCHPFuelStorageTransportationData, 't_single_effective_volume_selected_design')
    f_belt_width = getattr(BiomassCHPFuelStorageTransportationData, 'f_belt_width')
    f_belt_speed = getattr(BiomassCHPFuelStorageTransportationData, 'f_belt_speed')
    b_bin_quantity_design = getattr(BiomassCHPFuelStorageTransportationData, 'b_bin_quantity_design')
    b_single_effective_volume_selected_design = getattr(BiomassCHPFuelStorageTransportationData, 'b_single_effective_volume_selected_design')

    if b_bin_quantity_design is not None and b_single_effective_volume_selected_design is not None:
        b_volume = b_bin_quantity_design * b_single_effective_volume_selected_design
    else:
        b_volume = 0

    return [
        ImageInfo('0', (1942, 1294), getstrcolm(d_yardarea_design) + u'm2', 40),
        ImageInfo('0', (1957, 1392), getstrcolm(d_fuel_reserve_days_design) + u'd', 40),
        ImageInfo('0', (1934, 2100), getstrcolm(t_single_effective_volume_selected_design) + u'm2', 40),
        ImageInfo('0', (2418, 2821), getstrcolm(f_belt_speed) + u'm/s', 40),
        ImageInfo('0', (2423, 2740), getstrcolm(f_belt_width) + u'mm', 40),
        ImageInfo('0', (6081, 3135), getstrcolm(f_belt_speed) + u'm/s', 40),
        ImageInfo('0', (6090, 3053), getstrcolm(f_belt_width) + u'mm', 40),
        ImageInfo('0', (7234, 3448), getstrcolm(b_volume) + u'm3', 50),
    ]

# 原则性燃料输送系统图P2作成
def getBiomasssTransImgInfoListP2(plan_id):
    BiomassCHPFuelStorageTransportationData = BiomassCHPFuelStorageTransportation.search_storage_transportation(plan_id)
    d_yardarea_design = getattr(BiomassCHPFuelStorageTransportationData, 'd_yardarea_design')
    d_fuel_reserve_days_design = getattr(BiomassCHPFuelStorageTransportationData, 'd_fuel_reserve_days_design')
    t_single_effective_volume_selected_design = getattr(BiomassCHPFuelStorageTransportationData, 't_single_effective_volume_selected_design')
    f_belt_width = getattr(BiomassCHPFuelStorageTransportationData, 'f_belt_width')
    f_belt_speed = getattr(BiomassCHPFuelStorageTransportationData, 'f_belt_speed')
    b_bin_quantity_design = getattr(BiomassCHPFuelStorageTransportationData, 'b_bin_quantity_design')
    b_single_effective_volume_selected_design = getattr(BiomassCHPFuelStorageTransportationData, 'b_single_effective_volume_selected_design')

    if b_bin_quantity_design is not None and b_single_effective_volume_selected_design is not None:
        b_volume = b_bin_quantity_design * b_single_effective_volume_selected_design
    else:
        b_volume = 0

    return [
        ImageInfo('0', (992, 2103), getstrcolm(t_single_effective_volume_selected_design) + u'm2', 40),
        ImageInfo('0', (1606, 2821), getstrcolm(f_belt_speed) + u'm/s', 40),
        ImageInfo('0', (1607, 2739), getstrcolm(f_belt_width) + u'mm', 40),
        ImageInfo('0', (1932, 1295), getstrcolm(d_yardarea_design) + u'm2', 40),
        ImageInfo('0', (1950, 1389), getstrcolm(d_fuel_reserve_days_design) + u'd', 40),
        ImageInfo('0', (2328, 2106), getstrcolm(t_single_effective_volume_selected_design) + u'm2', 40),
        ImageInfo('0', (2787, 2455), getstrcolm(f_belt_speed) + u'm/s', 40),
        ImageInfo('0', (2792, 2373), getstrcolm(f_belt_width) + u'mm', 40),
        ImageInfo('0', (6117, 3131), getstrcolm(f_belt_speed) + u'm/s', 40),
        ImageInfo('0', (6124, 3049), getstrcolm(f_belt_width) + u'mm', 40),
        ImageInfo('0', (7247, 2383), getstrcolm(f_belt_speed) + u'm/s', 40),
        ImageInfo('0', (7249, 2303), getstrcolm(f_belt_width) + u'mm', 40),
        ImageInfo('0', (7452, 3447), getstrcolm(b_volume) + u'm3', 50),
    ]

# 原则性燃烧系统图P1作成
def getBiomasssFireImgInfoListP1(plan_id):
    # 锅炉计算数据取得
    biomassCHPBoilerCalculationData = BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
    # 锅炉辅机数据取得
    biomassCHPBoilerAuxiliariesData = BiomassCHPBoilerAuxiliaries.search_auxiliaries(plan_id)

    #G43
    ss_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'ss_fan_pressure')
    #G38
    ss_boiler_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'ss_boiler_resistance')
    #G78
    r_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'r_fan_pressure')
    #G76
    r_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'r_smoke_flow')
    #G72
    r_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'r_temperature')
    #G112
    t_new_enthalpy = getattr(biomassCHPBoilerAuxiliariesData, 't_new_enthalpy')
    #G113
    t_new_flow_rate = getattr(biomassCHPBoilerAuxiliariesData, 't_new_flow_rate')
    #G27
    sf_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'sf_fan_pressure')
    #G22
    sf_boiler_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'sf_boiler_resistance')
    #G62
    i_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'i_fan_pressure')
    #G56
    i_duster = getattr(biomassCHPBoilerAuxiliariesData, 'i_duster')   
    #G57
    i_duct_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'i_duct_resistance')   
    #G58
    i_cduct_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'i_cduct_resistance')   

    #G41
    ss_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'ss_smoke_flow')   
    #G37
    ss_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'ss_temperature')   
    #G21
    sf_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'sf_temperature')   
    #G25
    sf_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'sf_smoke_flow')   
    #G62
    i_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'i_fan_pressure')   
    #G53
    i_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'i_temperature')  
    #G60
    i_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'i_smoke_flow') 

    #G43-G38
    if ss_fan_pressure is not None and ss_boiler_resistance is not None:
        calculate_value1 = ss_fan_pressure - ss_boiler_resistance
    else:
        calculate_value1 = 0
    #G27-G22
    if sf_fan_pressure is not None and sf_boiler_resistance is not None:
        calculate_value2 = sf_fan_pressure - sf_boiler_resistance
    else:
        calculate_value2 = 0
    #G62-(G56+G57+G58)
    if i_fan_pressure is not None and i_duster is not None and i_duct_resistance is not None and i_cduct_resistance is not None:
        calculate_value3 = i_fan_pressure - (i_duster + i_duct_resistance + i_cduct_resistance)
    else:
        calculate_value3 = 0

    #G100
    a_first_hwind_temperatue_design = getattr(biomassCHPBoilerCalculationData, 'a_first_hwind_temperatue_design') 
    #G101
    a_first_hwind_flow_design = getattr(biomassCHPBoilerCalculationData, 'a_first_hwind_flow_design') 
    #G82
    p_smoke_temperature_design = getattr(biomassCHPBoilerCalculationData, 'p_smoke_temperature_design') 
    #G155
    i_smoke_actual_flow1_design = getattr(biomassCHPBoilerCalculationData, 'i_smoke_actual_flow1_design') 

    return [
    	# ImageInfo('0', (2251, 3549), getstrcolm(calculate_value1), 35),#G43-G38
    	# ImageInfo('0', (2255, 3823), getstrcolm(r_fan_pressure), 35),#G78
    	# ImageInfo('0', (2545, 3907), getstrcolm(r_smoke_flow), 35),#G76
    	# ImageInfo('0', (2547, 3819), getstrcolm(r_temperature), 35),#G72
    	# ImageInfo('0', (2553, 3555), getstrcolm(t_reduce_water_enthalpy), 35),#G112
    	# ImageInfo('0', (2557, 3633), getstrcolm(t_reduce_water_flow_rate), 35),#G113
    	# ImageInfo('0', (2763, 2959), getstrcolm(calculate_value2), 35),#G27-G22
    	# ImageInfo('0', (3067, 2961), getstrcolm(a_first_hwind_temperatue_design), 35),#G100 *********
    	# ImageInfo('0', (3067, 3039), getstrcolm(a_first_hwind_flow_design), 35),#G101 *********
    	# ImageInfo('0', (3886, 3133), getstrcolm(sf_fan_pressure), 35),#G27
    	# ImageInfo('0', (3886, 3965), getstrcolm(ss_fan_pressure), 35),#G43
    	# ImageInfo('0', (3996, 1935), getstrcolm(calculate_value3), 35),#G62-(G56+G57+G58)
    	# ImageInfo('0', (4174, 4053), getstrcolm(ss_smoke_flow), 35),#G41
    	# ImageInfo('0', (4178, 3969), getstrcolm(ss_temperature), 35),#G37
    	# ImageInfo('0', (4184, 3141), getstrcolm(sf_temperature), 35),#G21
    	# ImageInfo('0', (4184, 3221), getstrcolm(sf_smoke_flow), 35),#G25
    	# ImageInfo('0', (4358, 1935), getstrcolm(p_smoke_temperature_design), 35),#G82 *********
    	# ImageInfo('0', (4360, 2017), getstrcolm(i_smoke_actual_flow1_design), 35),#G155 *********
    	# ImageInfo('0', (6453, 2373), getstrcolm(i_fan_pressure), 35),#G62
    	# ImageInfo('0', (6751, 2377), getstrcolm(i_temperature), 35),#G53
    	# ImageInfo('0', (6751, 2455), getstrcolm(i_smoke_flow), 35),#G60

        # 锅炉辅机!G43-G38 ss_fan_pressure-ss_boiler_resistance
    	ImageInfo('0', (2239, 3538), getstrcolm(calculate_value1), 50),
    	# 锅炉辅机!G78 r_fan_pressure
    	ImageInfo('0', (2239, 3818), getstrcolm(r_fan_pressure), 50),
    	# 锅炉辅机!G72 r_temperature
    	ImageInfo('0', (2541, 3820), getstrcolm(r_temperature), 50),
    	# 锅炉辅机!G76 r_smoke_flow
    	ImageInfo('0', (2541, 3900), getstrcolm(r_smoke_flow), 50),
    	# 锅炉辅机!G112 t_new_enthalpy
    	ImageInfo('0', (2543, 3540), getstrcolm(t_new_enthalpy), 50),
    	# 锅炉辅机!G113 t_new_flow_rate
    	ImageInfo('0', (2543, 3620), getstrcolm(t_new_flow_rate), 50),
    	# 锅炉辅机!G27-G22 sf_fan_pressure-sf_boiler_resistance
    	ImageInfo('0', (2753, 2952), getstrcolm(calculate_value2), 50),
    	# 锅炉计算!G100 a_first_hwind_temperatue_design
    	ImageInfo('0', (3049, 2948), getstrcolm(a_first_hwind_temperatue_design), 50),
    	# 锅炉计算!G101 a_first_hwind_flow_design
    	ImageInfo('0', (3055, 3038), getstrcolm(a_first_hwind_flow_design), 50),
    	# 锅炉辅机!G27 sf_fan_pressure
    	ImageInfo('0', (3872, 3131), getstrcolm(sf_fan_pressure), 50),
    	# 锅炉辅机!G43 ss_fan_pressure 
    	ImageInfo('0', (3872, 3960), getstrcolm(ss_fan_pressure), 50),
    	# 锅炉辅机!G62-(G56+G57+G58) i_fan_pressure-i_duster-i_duct_resistance-i_cduct_resistance
    	ImageInfo('0', (3980, 1931), getstrcolm(calculate_value3), 50),
    	# 锅炉辅机!G25 sf_smoke_flow
    	ImageInfo('0', (4170, 3217), getstrcolm(sf_smoke_flow), 50),
    	# 锅炉辅机!G41 ss_smoke_flow
    	ImageInfo('0', (4170, 4044), getstrcolm(ss_smoke_flow), 50),
    	# 锅炉辅机!G21 sf_temperature
    	ImageInfo('0', (4172, 3131), getstrcolm(sf_temperature), 50),
    	# 锅炉辅机!G37 ss_temperature
    	ImageInfo('0', (4172, 3960), getstrcolm(ss_temperature), 50),
    	# 锅炉计算!G82 p_smoke_temperature_design
    	ImageInfo('0', (4344, 1935), getstrcolm(p_smoke_temperature_design), 50),
    	# 锅炉计算!G155 i_smoke_actual_flow1_design
    	ImageInfo('0', (4344, 2019), getstrcolm(i_smoke_actual_flow1_design), 50),
    	# 锅炉辅机!G62 i_fan_pressure
    	ImageInfo('0', (6441, 2368), getstrcolm(i_fan_pressure), 50),
    	# 锅炉辅机!G53 i_temperature
    	ImageInfo('0', (6745, 2372), getstrcolm(i_temperature), 50),
    	# 锅炉辅机!G60 i_smoke_flow
    	ImageInfo('0', (6745, 2454), getstrcolm(i_smoke_flow), 50),
    ]


# 原则性燃烧系统图P2作成
def getBiomasssFireImgInfoListP2(plan_id):
    # 锅炉计算数据取得
    biomassCHPBoilerCalculationData = BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
    # 锅炉辅机数据取得
    biomassCHPBoilerAuxiliariesData = BiomassCHPBoilerAuxiliaries.search_auxiliaries(plan_id)

    #G43
    ss_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'ss_fan_pressure')
    #G38
    ss_boiler_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'ss_boiler_resistance')
    #G78
    r_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'r_fan_pressure')
    #G76
    r_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'r_smoke_flow')
    #G72
    r_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'r_temperature')
    #G112
    t_new_enthalpy = getattr(biomassCHPBoilerAuxiliariesData, 't_new_enthalpy')
    #G113
    t_new_flow_rate = getattr(biomassCHPBoilerAuxiliariesData, 't_new_flow_rate')
    #G27
    sf_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'sf_fan_pressure')
    #G22
    sf_boiler_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'sf_boiler_resistance')
    #G62
    i_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'i_fan_pressure')
    #G56
    i_duster = getattr(biomassCHPBoilerAuxiliariesData, 'i_duster')   
    #G57
    i_duct_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'i_duct_resistance')   
    #G58
    i_cduct_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'i_cduct_resistance')   

    #G41
    ss_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'ss_smoke_flow')   
    #G37
    ss_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'ss_temperature')   
    #G21
    sf_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'sf_temperature')   
    #G25
    sf_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'sf_smoke_flow')   
    #G62
    i_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'i_fan_pressure')   
    #G53
    i_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'i_temperature')  
    #G60
    i_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'i_smoke_flow') 

    #G43-G38
    if ss_fan_pressure is not None and ss_boiler_resistance is not None:
        calculate_value1 = ss_fan_pressure - ss_boiler_resistance
    else:
        calculate_value1 = 0
    #G27-G22
    if sf_fan_pressure is not None and sf_boiler_resistance is not None:
        calculate_value2 = sf_fan_pressure - sf_boiler_resistance
    else:
        calculate_value2 = 0
    #G62-(G56+G57+G58)
    if i_fan_pressure is not None and i_duster is not None and i_duct_resistance is not None and i_cduct_resistance is not None:
        calculate_value3 = i_fan_pressure - (i_duster + i_duct_resistance + i_cduct_resistance)
    else:
        calculate_value3 = 0

    #G100
    a_first_hwind_temperatue_design = getattr(biomassCHPBoilerCalculationData, 'a_first_hwind_temperatue_design') 
    #G101
    a_first_hwind_flow_design = getattr(biomassCHPBoilerCalculationData, 'a_first_hwind_flow_design') 
    #G82
    p_smoke_temperature_design = getattr(biomassCHPBoilerCalculationData, 'p_smoke_temperature_design') 
    #G155
    i_smoke_actual_flow1_design = getattr(biomassCHPBoilerCalculationData, 'i_smoke_actual_flow1_design') 

    return [

     	# 锅炉辅机!G43-G38 ss_fan_pressure-ss_boiler_resistance
    	ImageInfo('0', (1281, 3691), getstrcolm(calculate_value1), 50),
    	# 锅炉辅机!G112 t_new_enthalpy
    	ImageInfo('0', (1585, 3691), getstrcolm(t_new_enthalpy), 50),
    	# 锅炉辅机!G113 t_new_flow_rate
    	ImageInfo('0', (1585, 3775), getstrcolm(t_new_flow_rate), 50),
    	# 锅炉辅机!G27-G22 sf_fan_pressure-sf_boiler_resistance
    	ImageInfo('0', (2357, 3695), getstrcolm(calculate_value2), 50),
    	# 锅炉计算!G100 a_first_hwind_temperatue_design
    	ImageInfo('0', (2657, 3699), getstrcolm(a_first_hwind_temperatue_design), 50),
    	# 锅炉计算!G101 a_first_hwind_flow_design
    	ImageInfo('0', (2657, 3783), getstrcolm(a_first_hwind_flow_design), 50),
    	# 锅炉辅机!G27 sf_fan_pressure-sf_boiler_resistance
    	ImageInfo('0', (3985, 3448), getstrcolm(sf_fan_pressure), 50),
    	# 锅炉辅机!G43 ss_fan_pressure-ss_boiler_resistance
    	ImageInfo('0', (3985, 4276), getstrcolm(ss_fan_pressure), 50),
    	# 锅炉辅机!G62-(G56+G57+G58) i_fan_pressure-i_duster-i_duct_resistance-i_cduct_resistance
    	ImageInfo('0', (4033, 1888), getstrcolm(calculate_value3), 50),
    	# 锅炉辅机!G21 sf_temperature
    	ImageInfo('0', (4285, 3448), getstrcolm(sf_temperature), 50),
    	# 锅炉辅机!G25 sf_smoke_flow
    	ImageInfo('0', (4285, 3532), getstrcolm(sf_smoke_flow), 50),
    	# 锅炉辅机!G37 ss_temperature
    	ImageInfo('0', (4285, 4280), getstrcolm(ss_temperature), 50),
    	# 锅炉辅机!G41 ss_smoke_flow
    	ImageInfo('0', (4285, 4360), getstrcolm(ss_smoke_flow), 50),
    	# 锅炉计算!G82 p_smoke_temperature_design
    	ImageInfo('0', (4401, 1888), getstrcolm(p_smoke_temperature_design), 50),
    	# 锅炉计算!G155 i_smoke_actual_flow1_design
    	ImageInfo('0', (4401, 1972), getstrcolm(i_smoke_actual_flow1_design), 50),
    	# 锅炉辅机!G62 i_fan_pressure
    	ImageInfo('0', (6442, 2365), getstrcolm(i_fan_pressure), 50),
    	# 锅炉辅机!G53 i_temperature
    	ImageInfo('0', (6740, 2447), getstrcolm(i_temperature), 50),
    	# 锅炉辅机!G60 i_smoke_flow
    	ImageInfo('0', (6742, 2365), getstrcolm(i_smoke_flow), 50),
    ]

# 原则性燃烧系统图P3作成
def getBiomasssFireImgInfoListP3(plan_id):
    # 锅炉计算数据取得
    biomassCHPBoilerCalculationData = BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
    # 锅炉辅机数据取得
    biomassCHPBoilerAuxiliariesData = BiomassCHPBoilerAuxiliaries.search_auxiliaries(plan_id)

    #G43
    ss_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'ss_fan_pressure')
    #G38
    ss_boiler_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'ss_boiler_resistance')
    #G78
    r_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'r_fan_pressure')
    #G76
    r_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'r_smoke_flow')
    #G72
    r_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'r_temperature')
    #G112
    t_new_enthalpy = getattr(biomassCHPBoilerAuxiliariesData, 't_new_enthalpy')
    #G113
    t_new_flow_rate = getattr(biomassCHPBoilerAuxiliariesData, 't_new_flow_rate')
    #G27
    sf_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'sf_fan_pressure')
    #G22
    sf_boiler_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'sf_boiler_resistance')
    #G62
    i_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'i_fan_pressure')
    #G56
    i_duster = getattr(biomassCHPBoilerAuxiliariesData, 'i_duster')   
    #G57
    i_duct_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'i_duct_resistance')   
    #G58
    i_cduct_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'i_cduct_resistance')   

    #G41
    ss_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'ss_smoke_flow')   
    #G37
    ss_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'ss_temperature')   
    #G21
    sf_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'sf_temperature')   
    #G25
    sf_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'sf_smoke_flow')   
    #G62
    i_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'i_fan_pressure')   
    #G53
    i_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'i_temperature')  
    #G60
    i_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'i_smoke_flow') 

    #G43-G38
    if ss_fan_pressure is not None and ss_boiler_resistance is not None:
        calculate_value1 = ss_fan_pressure - ss_boiler_resistance
    else:
        calculate_value1 = 0
    #G27-G22
    if sf_fan_pressure is not None and sf_boiler_resistance is not None:
        calculate_value2 = sf_fan_pressure - sf_boiler_resistance
    else:
        calculate_value2 = 0
    #G62-(G56+G57+G58)
    if i_fan_pressure is not None and i_duster is not None and i_duct_resistance is not None and i_cduct_resistance is not None:
        calculate_value3 = i_fan_pressure - (i_duster + i_duct_resistance + i_cduct_resistance)
    else:
        calculate_value3 = 0

    #G100
    a_first_hwind_temperatue_design = getattr(biomassCHPBoilerCalculationData, 'a_first_hwind_temperatue_design') 
    #G101
    a_first_hwind_flow_design = getattr(biomassCHPBoilerCalculationData, 'a_first_hwind_flow_design') 
    #G82
    p_smoke_temperature_design = getattr(biomassCHPBoilerCalculationData, 'p_smoke_temperature_design') 
    #G155
    i_smoke_actual_flow1_design = getattr(biomassCHPBoilerCalculationData, 'i_smoke_actual_flow1_design') 

    return [

        # 锅炉辅机G43-G38 ss_fan_pressure-ss_boiler_resistance
        ImageInfo('0', (997, 3487), getstrcolm(calculate_value1), 50),
        # 锅炉辅机G112 t_new_enthalpy
        ImageInfo('0', (1301, 3491), getstrcolm(t_new_enthalpy), 50),
        # 锅炉辅机G113 t_new_flow_rate
        ImageInfo('0', (1301, 3571), getstrcolm(t_new_flow_rate), 50),
        # 锅炉辅机G78 r_fan_pressure
        ImageInfo('0', (2217, 3819), getstrcolm(r_fan_pressure), 50),
        # 锅炉辅机G76 r_smoke_flow
        ImageInfo('0', (2509, 3899), getstrcolm(r_smoke_flow), 50),
        # 锅炉辅机G72 r_temperature
        ImageInfo('0', (2517, 3819), getstrcolm(r_temperature), 50),
        # 锅炉辅机G27-G22 sf_fan_pressure-sf_boiler_resistance
        ImageInfo('0', (2749, 3047), getstrcolm(calculate_value2), 50),
        # 锅炉辅机G101
        ImageInfo('0', (3049, 3123), getstrcolm(a_first_hwind_flow_design), 50),
        # 锅炉辅机G100
        ImageInfo('0', (3053, 3043), getstrcolm(a_first_hwind_temperatue_design), 50),
        # 锅炉辅机G27 sf_fan_pressure-sf_boiler_resistance
        ImageInfo('0', (3845, 3127), getstrcolm(sf_fan_pressure), 50),
        # 锅炉辅机G43 ss_fan_pressure-ss_boiler_resistance
        ImageInfo('0', (3849, 3955), getstrcolm(ss_fan_pressure), 50),
        # 锅炉辅机G62-(G56+G57+G58) i_fan_pressure-i_duster-i_duct_resistance-i_cduct_resistance
        ImageInfo('0', (3973, 1843), getstrcolm(calculate_value3), 50),
        # 锅炉辅机G25 sf_smoke_flow
        ImageInfo('0', (4145, 3215), getstrcolm(sf_smoke_flow), 50),
        # 锅炉辅机G37 ss_temperature
        ImageInfo('0', (4145, 3963), getstrcolm(ss_temperature), 50),
        # 锅炉辅机G41 ss_smoke_flow
        ImageInfo('0', (4145, 4039), getstrcolm(ss_smoke_flow), 50),
        # 锅炉辅机G21 sf_temperature
        ImageInfo('0', (4149, 3135), getstrcolm(sf_temperature), 50),
        # 锅炉辅机G155
        ImageInfo('0', (4321, 1919), getstrcolm(i_smoke_actual_flow1_design), 50),
        # 锅炉辅机G82
        ImageInfo('0', (4325, 1847), getstrcolm(p_smoke_temperature_design), 50),
        # 锅炉辅机G62 i_fan_pressure
        ImageInfo('0', (6417, 2363), getstrcolm(i_fan_pressure), 50),
        # 锅炉辅机G53 i_temperature
        ImageInfo('0', (6717, 2367), getstrcolm(i_temperature), 50),
        # 锅炉辅机G60 i_smoke_flow
        ImageInfo('0', (6717, 2455), getstrcolm(i_smoke_flow), 50),
    ]

# 原则性燃烧系统图P4作成
def getBiomasssFireImgInfoListP4(plan_id):
    # 锅炉计算数据取得
    biomassCHPBoilerCalculationData = BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
    # 锅炉辅机数据取得
    biomassCHPBoilerAuxiliariesData = BiomassCHPBoilerAuxiliaries.search_auxiliaries(plan_id)

    #G43
    ss_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'ss_fan_pressure')
    #G38
    ss_boiler_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'ss_boiler_resistance')
    #G78
    r_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'r_fan_pressure')
    #G76
    r_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'r_smoke_flow')
    #G72
    r_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'r_temperature')
    #G112
    t_new_enthalpy = getattr(biomassCHPBoilerAuxiliariesData, 't_new_enthalpy')
    #G113
    t_new_flow_rate = getattr(biomassCHPBoilerAuxiliariesData, 't_new_flow_rate')
    #G27
    sf_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'sf_fan_pressure')
    #G22
    sf_boiler_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'sf_boiler_resistance')
    #G62
    i_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'i_fan_pressure')
    #G56
    i_duster = getattr(biomassCHPBoilerAuxiliariesData, 'i_duster')   
    #G57
    i_duct_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'i_duct_resistance')   
    #G58
    i_cduct_resistance = getattr(biomassCHPBoilerAuxiliariesData, 'i_cduct_resistance')   

    #G41
    ss_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'ss_smoke_flow')   
    #G37
    ss_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'ss_temperature')   
    #G21
    sf_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'sf_temperature')   
    #G25
    sf_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'sf_smoke_flow')   
    #G62
    i_fan_pressure = getattr(biomassCHPBoilerAuxiliariesData, 'i_fan_pressure')   
    #G53
    i_temperature = getattr(biomassCHPBoilerAuxiliariesData, 'i_temperature')  
    #G60
    i_smoke_flow = getattr(biomassCHPBoilerAuxiliariesData, 'i_smoke_flow') 

    #G43-G38
    if ss_fan_pressure is not None and ss_boiler_resistance is not None:
        calculate_value1 = ss_fan_pressure - ss_boiler_resistance
    else:
        calculate_value1 = 0
    #G27-G22
    if sf_fan_pressure is not None and sf_boiler_resistance is not None:
        calculate_value2 = sf_fan_pressure - sf_boiler_resistance
    else:
        calculate_value2 = 0
    #G62-(G56+G57+G58)
    if i_fan_pressure is not None and i_duster is not None and i_duct_resistance is not None and i_cduct_resistance is not None:
        calculate_value3 = i_fan_pressure - (i_duster + i_duct_resistance + i_cduct_resistance)
    else:
        calculate_value3 = 0

    #G100
    a_first_hwind_temperatue_design = getattr(biomassCHPBoilerCalculationData, 'a_first_hwind_temperatue_design') 
    #G101
    a_first_hwind_flow_design = getattr(biomassCHPBoilerCalculationData, 'a_first_hwind_flow_design') 
    #G82
    p_smoke_temperature_design = getattr(biomassCHPBoilerCalculationData, 'p_smoke_temperature_design') 
    #G155
    i_smoke_actual_flow1_design = getattr(biomassCHPBoilerCalculationData, 'i_smoke_actual_flow1_design') 

    return [

        # 锅炉辅机G43-G38 ss_fan_pressure-ss_boiler_resistance
        ImageInfo('0', (1225, 3698), getstrcolm(calculate_value1), 50),
        # 锅炉辅机G113 t_new_flow_rate
        ImageInfo('0', (1529, 3786), getstrcolm(t_new_flow_rate), 50),
        # 锅炉辅机G112 t_new_enthalpy
        ImageInfo('0', (1537, 3698), getstrcolm(t_new_enthalpy), 50),
        # 锅炉辅机G27-G22 sf_fan_pressure-sf_boiler_resistance
        ImageInfo('0', (2245, 3694), getstrcolm(calculate_value2), 50),
        # 锅炉计算G100 a_first_hwind_temperatue_design
        ImageInfo('0', (2545, 3702), getstrcolm(a_first_hwind_temperatue_design), 50),
        # 锅炉计算G101 a_first_hwind_flow_design
        ImageInfo('0', (2545, 3778), getstrcolm(a_first_hwind_flow_design), 50),
        # 锅炉辅机G27 sf_fan_pressure-sf_boiler_resistance
        ImageInfo('0', (3985, 3450), getstrcolm(sf_fan_pressure), 50),
        # 锅炉辅机G62-(G56+G57+G58) i_fan_pressure-i_duster-i_duct_resistance-i_cduct_resistance
        ImageInfo('0', (4029, 1890), getstrcolm(calculate_value3), 50),
        # 锅炉辅机G21 sf_temperature
        ImageInfo('0', (4285, 3450), getstrcolm(sf_temperature), 50),
        # 锅炉辅机G25 sf_smoke_flow
        ImageInfo('0', (4285, 3530), getstrcolm(sf_smoke_flow), 50),
        # 锅炉计算G155 i_smoke_actual_flow1_design
        ImageInfo('0', (4393, 1966), getstrcolm(i_smoke_actual_flow1_design), 50),
        # 锅炉计算G82 p_smoke_temperature_design
        ImageInfo('0', (4397, 1882), getstrcolm(p_smoke_temperature_design), 50),
        # 锅炉辅机G62 i_fan_pressure
        ImageInfo('0', (6437, 2366), getstrcolm(i_fan_pressure), 50),
        # 锅炉辅机G60 i_smoke_flow
        ImageInfo('0', (6741, 2446), getstrcolm(i_smoke_flow), 50),
        # 锅炉辅机G53 i_temperature
        ImageInfo('0', (6749, 2370), getstrcolm(i_temperature), 50),
        # 锅炉辅机G43 ss_fan_pressure-ss_boiler_resistance
        ImageInfo('0', (3985, 4283), getstrcolm(ss_fan_pressure), 50),
        # 锅炉辅机G37 ss_temperature
        ImageInfo('0', (4285, 4275), getstrcolm(ss_temperature), 50),
        # 锅炉辅机G41 ss_smoke_flow
        ImageInfo('0', (4285, 4359), getstrcolm(ss_smoke_flow), 50),

    ]

# 原则性热力系统图P1a作成
def getBiomasssHotImgInfoListP1a(plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_four = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_four = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount+turbineBackpressure.i_steam_exhaust_flow
        plus_three = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount
        plus_36_37 = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_36_37 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount
        plus_32_33 = 0
        if turbineBackpressure.hh1_extraction_amount and turbineBackpressure.hh2_extraction_amount:
            plus_32_33 = turbineBackpressure.hh1_extraction_amount + turbineBackpressure.hh2_extraction_amount
        sewage_quantity = 0
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000

        multiply_f33_g19 = 0
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design

        return [
            # 汽轮机-三级低加F33 hh2_saturated_water_enthalpy
            ImageInfo('0', (757, 2575), getstrcolm(turbineBackpressure.hh2_saturated_water_enthalpy), 50),
            # 锅炉辅机G88 f_economizer_entry_pressure
            ImageInfo('0', (807, 1664), getstrcolm(boilerAuxiliaries.f_economizer_entry_pressure), 50),
            # 汽轮机-三级低加C32 hh1_water_enthalpy
            ImageInfo('0', (757, 1760), getstrcolm(turbineBackpressure.hh1_water_enthalpy), 50),
            # 汽轮机-三级低加F32 hh1_saturated_water_enthalpy
            ImageInfo('0', (757, 2067), getstrcolm(turbineBackpressure.hh1_saturated_water_enthalpy), 50),
            # 锅炉辅机F33 c_drum_aturatedwater_enthalpy 
            ImageInfo('0', (758, 3077), getstrcolm(boilerAuxiliaries.c_drum_aturatedwater_enthalpy), 50),
            # 锅炉辅机F32 c_drum_pressure
            ImageInfo('0', (759, 2977), getstrcolm(boilerAuxiliaries.c_drum_pressure), 50),
            # 锅炉辅机F31/1000 c_sewage_quantity/1000
            ImageInfo('0', (977, 3072), getstrcolm(sewage_quantity), 50),
            # 汽轮机-三级低加K32 hh1_extraction_amount
            ImageInfo('0', (1048, 2067), getstrcolm(turbineBackpressure.hh1_extraction_amount), 50),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1048, 1760), getstrcolm(furnaceCalculation.f_steam_flow_design), 50),
            # 汽轮机-三级低加K32+K33 hh1_extraction_amount+hh2_extraction_amount
            ImageInfo('0', (1048, 2574), getstrcolm(plus_32_33), 50),
            # 汽轮机-三级低加E32 hh1_saturated_water_temperature
            ImageInfo('0', (1049, 1971), getstrcolm(turbineBackpressure.hh1_saturated_water_temperature), 50),
            # 汽轮机-三级低加E33  hh2_saturated_water_temperature
            ImageInfo('0', (1049, 2480), getstrcolm(turbineBackpressure.hh2_saturated_water_temperature), 50),
            # 汽轮机-三级低加B32 hh1_water_temperature
            ImageInfo('0', (1051, 1665), getstrcolm(turbineBackpressure.hh1_water_temperature), 50),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1279, 920), getstrcolm(furnaceCalculation.f_steam_flow_design), 50),
            # 汽轮机-三级低加G35 d_work_pressure
            ImageInfo('0', (1687, 3984), getstrcolm(turbineBackpressure.d_work_pressure), 50),
            # 汽轮机-三级低加C35 d_water_enthalpy
            ImageInfo('0', (1687, 4081), getstrcolm(turbineBackpressure.d_water_enthalpy), 50),
            # 汽轮机-三级低加i35 d_extraction_pressure
            ImageInfo('0', (1953, 2355), getstrcolm(turbineBackpressure.d_extraction_pressure), 50),
            # 汽轮机-三级低加J35 d_extraction_enthalpy
            ImageInfo('0', (1953, 2447), getstrcolm(turbineBackpressure.d_extraction_enthalpy), 50),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1993, 4085), getstrcolm(furnaceCalculation.f_steam_flow_design), 50),
            # 汽轮机-三级低加 B35 d_water_temperature
            ImageInfo('0', (1995, 3989), getstrcolm(turbineBackpressure.d_water_temperature), 50),
            # 汽轮机-三级低加k35 d_extraction_amount
            ImageInfo('0', (2239, 2447), getstrcolm(turbineBackpressure.d_extraction_amount), 50),
            # 汽轮机-三级低加J32 hh1_extraction_enthalpy
            ImageInfo('0', (2353, 1665), getstrcolm(turbineBackpressure.hh1_extraction_enthalpy), 50),
            # 汽轮机-三级低加i32 hh1_extraction_pressure
            ImageInfo('0', (2355, 1567), getstrcolm(turbineBackpressure.hh1_extraction_pressure), 50),
            # 汽轮机-三级低加J33 hh2_extraction_enthalpy
            ImageInfo('0', (2355, 1988), getstrcolm(turbineBackpressure.hh2_extraction_enthalpy), 50),
            # 汽轮机-三级低加i33 hh2_extraction_pressure
            ImageInfo('0', (2358, 1888), getstrcolm(turbineBackpressure.hh2_extraction_pressure), 50),
            # 锅炉计算G22 f_steam_enthalpy_design
            ImageInfo('0', (2552, 464), getstrcolm(furnaceCalculation.f_steam_enthalpy_design), 50),
            # 锅炉计算G20 f_steam_pressure_design
            ImageInfo('0', (2553, 365), getstrcolm(furnaceCalculation.f_steam_pressure_design), 50),
            # 汽轮机-三级低加F34  h_pressure
            ImageInfo('0', (2591, 4126), getstrcolm(turbineBackpressure.h_pressure), 50),
            # 汽轮机-三级低加H34 h_enthalpy
            ImageInfo('0', (2592, 4223), getstrcolm(turbineBackpressure.h_enthalpy), 50),
            # 汽轮机-三级低加K32 hh1_extraction_amount
            ImageInfo('0', (2641, 1666), getstrcolm(turbineBackpressure.hh1_extraction_amount), 50),
            # 汽轮机-三级低加K33 hh2_extraction_amount
            ImageInfo('0', (2641, 1986), getstrcolm(turbineBackpressure.hh2_extraction_amount), 50),
            # 汽轮机-三级低加C36 lh1_water_enthalpy
            ImageInfo('0', (2671, 3268), getstrcolm(turbineBackpressure.lh1_water_enthalpy), 50),
            # 汽轮机-三级低加F26 e_throttle_flow
            ImageInfo('0', (2770, 464), getstrcolm(turbineBackpressure.e_throttle_flow), 50),
            # 锅炉计算G21 f_steam_temperature_design
            ImageInfo('0', (2772, 365), getstrcolm(furnaceCalculation.f_steam_temperature_design), 50),
            # 汽轮机-三级低加B36 lh1_water_temperature
            ImageInfo('0', (2887, 3168), getstrcolm(turbineBackpressure.lh1_water_temperature), 50),
            # 汽轮机-三级低加K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2889, 3270), getstrcolm(plus_four), 50),
            # 汽轮机-三级低加I36 lh1_extraction_pressure
            ImageInfo('0', (2914, 2361), getstrcolm(turbineBackpressure.lh1_extraction_pressure), 50),
            # 汽轮机-三级低加J36 lh1_extraction_enthalpy
            ImageInfo('0', (2918, 2463), getstrcolm(turbineBackpressure.lh1_extraction_enthalpy), 50),
            # 锅炉计算G19*汽轮机-三级低加J34 h_amount
            ImageInfo('0', (2953, 4221), getstrcolm(multiply_f33_g19), 50),
            # 汽轮机-三级低加D34 h_temperature
            ImageInfo('0', (2958, 4131), getstrcolm(turbineBackpressure.h_temperature), 50),
            # 汽轮机-三级低加F36  lh1_saturated_water_enthalpy
            ImageInfo('0', (3119, 3527), getstrcolm(turbineBackpressure.lh1_saturated_water_enthalpy), 50),
            # 汽轮机-三级低加K36 lh1_extraction_amount
            ImageInfo('0', (3141, 2462), getstrcolm(turbineBackpressure.lh1_extraction_amount), 50),
            # 汽轮机-三级低加C37 lh2_water_enthalpy
            ImageInfo('0', (3208, 3263), getstrcolm(turbineBackpressure.lh2_water_enthalpy), 50),
            # 汽轮机-三级低加K36 lh1_extraction_amount
            ImageInfo('0', (3351, 3525), getstrcolm(turbineBackpressure.lh1_extraction_amount), 50),
            # 汽轮机-三级低加E36 lh1_saturated_water_temperature
            ImageInfo('0', (3352, 3425), getstrcolm(turbineBackpressure.lh1_saturated_water_temperature), 50),
            # 汽轮机-三级低加J37 lh2_extraction_enthalpy
            ImageInfo('0', (3421, 2459), getstrcolm(turbineBackpressure.lh2_extraction_enthalpy), 50),
            # 汽轮机-三级低加K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3421, 3259), getstrcolm(plus_four), 50),
            # 汽轮机-三级低加i37 lh2_extraction_pressure
            ImageInfo('0', (3423, 2365), getstrcolm(turbineBackpressure.lh2_extraction_pressure), 50),
            # 汽轮机-三级低加B37 lh2_water_temperature
            ImageInfo('0', (3423, 3164), getstrcolm(turbineBackpressure.lh2_water_temperature), 50),
            # 汽轮机-三级低加k37 lh2_extraction_amount
            ImageInfo('0', (3651, 2464), getstrcolm(turbineBackpressure.lh2_extraction_amount), 50),
            # 汽轮机-三级低加F37 lh2_saturated_water_enthalpy
            ImageInfo('0', (3651, 3530), getstrcolm(turbineBackpressure.lh2_saturated_water_enthalpy), 50),
            # 汽轮机-三级低加F24 e_steam_extraction_select
            ImageInfo('0', (3652, 1426), getstrcolm(turbineBackpressure.e_steam_extraction_select), 50),
            # 汽轮机-三级低加c38 lh3_water_enthalpy
            ImageInfo('0', (3715, 3262), getstrcolm(turbineBackpressure.lh3_water_enthalpy), 50),
            # 汽轮机-三级低加E37 lh2_saturated_water_temperature
            ImageInfo('0', (3883, 3436), getstrcolm(turbineBackpressure.lh2_saturated_water_temperature), 50),
            # 汽轮机-三级低加k36+K37 lh1_extraction_amount+lh2_extraction_amount
            ImageInfo('0', (3885, 3531), getstrcolm(plus_36_37), 50),
            # 汽轮机-三级低加b38 lh3_water_temperature
            ImageInfo('0', (3929, 3167), getstrcolm(turbineBackpressure.lh3_water_temperature), 50),
            # 汽轮机-三级低加K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3931, 3265), getstrcolm(plus_four), 50),
            # 汽轮机-三级低加j38 lh3_extraction_enthalpy
            ImageInfo('0', (3935, 2460), getstrcolm(turbineBackpressure.lh3_extraction_enthalpy), 50),
            # 汽轮机-三级低加I38 lh3_extraction_pressure
            ImageInfo('0', (3941, 2367), getstrcolm(turbineBackpressure.lh3_extraction_pressure), 50),
            # 汽轮机-三级低加f69 i_exhaust_point_pressure
            ImageInfo('0', (3969, 1098), getstrcolm(turbineBackpressure.i_exhaust_point_pressure), 50),
            # 汽轮机-三级低加f72 i_exhaust_point_enthalpy
            ImageInfo('0', (3970, 1202), getstrcolm(turbineBackpressure.i_exhaust_point_enthalpy), 50),
            # 汽轮机-三级低加k38 lh3_extraction_amount
            ImageInfo('0', (4157, 2463), getstrcolm(turbineBackpressure.lh3_extraction_amount), 50),
            # 汽轮机-三级低加f38 lh3_saturated_water_enthalpy
            ImageInfo('0', (4193, 3527), getstrcolm(turbineBackpressure.lh3_saturated_water_enthalpy), 50),
            # 汽轮机-三级低加f70 i_exhaust_point_temperature
            ImageInfo('0', (4206, 1102), getstrcolm(turbineBackpressure.i_exhaust_point_temperature), 50),
            # 汽轮机-三级低加f73 i_exhaust_point_flow
            ImageInfo('0', (4206, 1199), getstrcolm(turbineBackpressure.i_exhaust_point_flow), 50),
            # 汽轮机-三级低加C39 c_water_enthalpy
            ImageInfo('0', (4224, 3256), getstrcolm(turbineBackpressure.c_water_enthalpy), 50),
            # 汽轮机-三级低加K36+K37+K38+F100  lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (4394, 3261), getstrcolm(plus_four), 50),
            # 汽轮机-三级低加B39 c_water_temperature
            ImageInfo('0', (4396, 3166), getstrcolm(turbineBackpressure.c_water_temperature), 50),
            # 汽轮机-三级低加K36+K37+K38  lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount
            ImageInfo('0', (4420, 3529), getstrcolm(plus_three), 50),
            # 汽轮机-三级低加E38 lh3_saturated_water_temperature
            ImageInfo('0', (4422, 3434), getstrcolm(turbineBackpressure.lh3_saturated_water_temperature), 50),
            # 汽轮机-三级低加f93 i_steam_exhaust_pressure
            ImageInfo('0', (4955, 1860), getstrcolm(turbineBackpressure.i_steam_exhaust_pressure), 50),
            # 汽轮机-三级低加f96 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4957, 1962), getstrcolm(turbineBackpressure.i_steam_exhaust_enthalpy_actual), 50),
            # 汽轮机-三级低加f100 i_steam_exhaust_flow
            ImageInfo('0', (5215, 1954), getstrcolm(turbineBackpressure.i_steam_exhaust_flow), 50),
            # 汽轮机-三级低加f24 e_steam_extraction_select
            ImageInfo('0', (5373, 1478), getstrcolm(turbineBackpressure.e_steam_extraction_select), 50),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5502, 2666), getstrcolm(circulatingWater.v_total_circulating_water_select), 50),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5750, 1960), getstrcolm(circulatingWater.v_total_circulating_water_select), 50),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6228, 1222), getstrcolm(circulatingWater.v_evaporation_loss), 70),
            # 循环水F23 v_discharge_capacity
            ImageInfo('0', (6614, 3427), getstrcolm(circulatingWater.v_discharge_capacity), 70),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (7173, 1230), getstrcolm(circulatingWater.v_partial_blow_loss), 70),
            # 循环水F24    
            ImageInfo('0', (8192, 3274), getstrcolm(circulatingWater.v_amount_of_makeup_water), 70),
            ImageInfo('0', (785, 1985), '--', 50),
            ImageInfo('0', (785, 2493), '--', 50),
            ImageInfo('0', (2677, 1581), '--', 50),
            ImageInfo('0', (2677, 1905), '--', 50),
            ImageInfo('0', (2677, 2373), '--', 50),
            ImageInfo('0', (3173, 2381), '--', 50),
            ImageInfo('0', (3673, 2381), '--', 50),
            ImageInfo('0', (4185, 2381), '--', 50),

            ImageInfo('0', (2693, 3179), '--', 50),
            ImageInfo('0', (3233, 3183), '--', 50),
            ImageInfo('0', (3733, 3183), '--', 50),
            ImageInfo('0', (4237, 3179), '--', 50),
            ImageInfo('0', (3141, 3443), '--', 50),
            ImageInfo('0', (3669, 3443), '--', 50),
            ImageInfo('0', (4209, 3443), '--', 50),
            ImageInfo('0', (5248, 1873), '--', 50),
            ImageInfo('0', (5564, 1873), '--', 50),
            ImageInfo('0', (5564, 1973), '--', 50),
            ImageInfo('0', (5776, 1873), '30/43', 50),
            ImageInfo('0', (5300, 2585), '--', 50),
            ImageInfo('0', (5300, 2681), '--', 50),
            ImageInfo('0', (5520, 2589), '20/33', 50),

            ImageInfo('0', (999, 2995), '--', 50),
            ImageInfo('0', (2271, 2369), '--', 50),

        ]

# 原则性热力系统图P1b作成
def getBiomasssHotImgInfoListP1b(plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_four = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_four = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount+turbineBackpressure.i_steam_exhaust_flow
        plus_three = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount
        plus_36_37 = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_36_37 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount
        plus_32_33 = 0
        if turbineBackpressure.hh1_extraction_amount and turbineBackpressure.hh2_extraction_amount:
            plus_32_33 = turbineBackpressure.hh1_extraction_amount + turbineBackpressure.hh2_extraction_amount
        sewage_quantity = 0
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000

        multiply_f33_g19 = 0
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design

        return [
            ImageInfo('0', (387, 2964), getstrcolm(boilerAuxiliaries.c_drum_pressure), 35),
            # --
            ImageInfo('0', (389, 2477), '--', 35),
            # 锅炉辅机F33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (389, 3062), getstrcolm(boilerAuxiliaries.c_drum_aturatedwater_enthalpy), 35),
            # 锅炉辅机！G88 f_economizer_entry_pressure
            ImageInfo('0', (390, 1668), getstrcolm(boilerAuxiliaries.f_economizer_entry_pressure), 35),
            # --
            ImageInfo('0', (390, 1974), '--', 35),
            # 汽轮机-三级低加！F33 hh2_saturated_water_enthalpy
            ImageInfo('0', (390, 2572), getstrcolm(turbineBackpressure.hh2_saturated_water_enthalpy), 35),
            # 汽轮机-三级低加！C32 hh1_water_enthalpy
            ImageInfo('0', (392, 1769), getstrcolm(turbineBackpressure.hh1_water_enthalpy), 35),
            # 汽轮机-三级低加！F32 hh1_saturated_water_enthalpy
            ImageInfo('0', (392, 2072), getstrcolm(turbineBackpressure.hh1_saturated_water_enthalpy), 35),
            # --
            ImageInfo('0', (603, 2966), '--', 35),
            # 锅炉辅机F31/1000 c_sewage_quantity/1000
            ImageInfo('0', (604, 3062), getstrcolm(sewage_quantity), 35),
            # 汽轮机-三级低加！E33 hh2_saturated_water_temperature
            ImageInfo('0', (680, 2476), getstrcolm(turbineBackpressure.hh2_saturated_water_temperature), 35),
            # 汽轮机-三级低加！B32 hh1_water_temperature
            ImageInfo('0', (681, 1673), getstrcolm(turbineBackpressure.hh1_water_temperature), 35),
            # 汽轮机-三级低加！E32 hh1_saturated_water_temperature
            ImageInfo('0', (681, 1976), getstrcolm(turbineBackpressure.hh1_saturated_water_temperature), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (683, 1772), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机-三级低加！K32 hh1_extraction_amount
            ImageInfo('0', (684, 2073), getstrcolm(turbineBackpressure.hh1_extraction_amount), 35),
            # 汽轮机-三级低加K32+K33 hh1_extraction_amount+hh2_extraction_amount
            ImageInfo('0', (685, 2571), getstrcolm(plus_32_33), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (907, 951), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机-三级低加！G35 d_work_pressure
            ImageInfo('0', (1311, 3964), getstrcolm(turbineBackpressure.d_work_pressure), 35),
            # 汽轮机-三级低加！C35 d_water_enthalpy
            ImageInfo('0', (1314, 4058), getstrcolm(turbineBackpressure.d_water_enthalpy), 35),
            # 汽轮机-三级低加！I35 d_extraction_pressure
            ImageInfo('0', (1589, 2361), getstrcolm(turbineBackpressure.d_extraction_pressure), 35),
            # 汽轮机-三级低加！J35 d_extraction_enthalpy
            ImageInfo('0', (1591, 2459), getstrcolm(turbineBackpressure.d_extraction_enthalpy), 35),
            # 汽轮机-三级低加！B35 d_water_temperature
            ImageInfo('0', (1615, 3967), getstrcolm(turbineBackpressure.d_water_temperature), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1619, 4063), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # --
            ImageInfo('0', (1863, 2363), '--', 35),
            # 汽轮机-三级低加！K35 d_extraction_amount
            ImageInfo('0', (1865, 2457), getstrcolm(turbineBackpressure.d_extraction_amount), 35),
            # 汽轮机-三级低加！I32 hh1_extraction_pressure
            ImageInfo('0', (1973, 1584), getstrcolm(turbineBackpressure.hh1_extraction_pressure), 35),
            # 汽轮机-三级低加！I33 hh2_extraction_pressure
            ImageInfo('0', (1973, 1900), getstrcolm(turbineBackpressure.hh2_extraction_pressure), 35),
            # 汽轮机-三级低加！J32 hh1_extraction_enthalpy
            ImageInfo('0', (1975, 1680), getstrcolm(turbineBackpressure.hh1_extraction_enthalpy), 35),
            # 汽轮机-三级低加！J33 hh2_extraction_enthalpy
            ImageInfo('0', (1977, 1998), getstrcolm(turbineBackpressure.hh2_extraction_enthalpy), 35),
            # 锅炉计算！G20 f_steam_pressure_design
            ImageInfo('0', (2161, 396), getstrcolm(furnaceCalculation.f_steam_pressure_design), 35),
            # 锅炉计算！G22 f_steam_enthalpy_design
            ImageInfo('0', (2165, 494), getstrcolm(furnaceCalculation.f_steam_enthalpy_design), 35),
            # 汽轮机-三级低加！F34 h_pressure
            ImageInfo('0', (2193, 4100), getstrcolm(turbineBackpressure.h_pressure), 35),
            # 汽轮机-三级低加！H34 h_enthalpy
            ImageInfo('0', (2195, 4198), getstrcolm(turbineBackpressure.h_enthalpy), 35),
            # --
            ImageInfo('0', (2251, 1582), '--', 35),
            # 汽轮机-三级低加！K32 hh1_extraction_amount
            ImageInfo('0', (2257, 1682), getstrcolm(turbineBackpressure.hh1_extraction_amount), 35),
            # --
            ImageInfo('0', (2259, 1900), '--', 35),
            # 汽轮机-三级低加！K33 hh2_extraction_amount
            ImageInfo('0', (2261, 1996), getstrcolm(turbineBackpressure.hh2_extraction_amount), 35),
            # --
            ImageInfo('0', (2277, 3152), '--', 35),
            # 汽轮机-三级低加！C36 lh1_water_enthalpy
            ImageInfo('0', (2279, 3247), getstrcolm(turbineBackpressure.lh1_water_enthalpy), 35),
            # 锅炉计算！G21 f_steam_temperature_design
            ImageInfo('0', (2379, 394), getstrcolm(furnaceCalculation.f_steam_temperature_design), 35),
            #  汽轮机-三级低加F26 e_throttle_flow
            ImageInfo('0', (2381, 492), getstrcolm(turbineBackpressure.e_throttle_flow), 35),
            # 汽轮机-三级低加！B36 lh1_water_temperature
            ImageInfo('0', (2490, 3151), getstrcolm(turbineBackpressure.lh1_water_temperature), 35),
            # 汽轮机-三级低加！K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2493, 3249), getstrcolm(plus_four), 35),
            # 汽轮机-三级低加！I36 lh1_extraction_pressure
            ImageInfo('0', (2524, 2360), getstrcolm(turbineBackpressure.lh1_extraction_pressure), 35),
            # 汽轮机-三级低加！J36 lh1_extraction_enthalpy
            ImageInfo('0', (2527, 2456), getstrcolm(turbineBackpressure.lh1_extraction_enthalpy), 35),
            # 锅炉计算！G19 * 汽轮机-三级低加！J34
            ImageInfo('0', (2556, 4198), getstrcolm(multiply_f33_g19), 35),
            # 汽轮机-三级低加！D34 h_temperature
            ImageInfo('0', (2557, 4099), getstrcolm(turbineBackpressure.h_temperature), 35),
            # --
            ImageInfo('0', (2722, 3413), '--', 35),
            # 汽轮机-三级低加！F36 lh1_saturated_water_enthalpy
            ImageInfo('0', (2726, 3513), getstrcolm(turbineBackpressure.lh1_saturated_water_enthalpy), 35),
            # --
            ImageInfo('0', (2745, 2360), '--', 35),
            # 汽轮机-三级低加！K36 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2746, 2457), getstrcolm(plus_four), 35),
            # --
            ImageInfo('0', (2807, 3152), '--', 35),
            # 汽轮机-三级低加！C37 lh2_water_enthalpy
            ImageInfo('0', (2809, 3248), getstrcolm(turbineBackpressure.lh2_water_enthalpy), 35),
            # 汽轮机-三级低加！E36 lh1_saturated_water_temperature
            ImageInfo('0', (2955, 3416), getstrcolm(turbineBackpressure.lh1_saturated_water_temperature), 35),
            # 汽轮机-三级低加！K36 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2956, 3511), getstrcolm(plus_four), 35),
            # 汽轮机-三级低加！K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3023, 3249), getstrcolm(plus_four), 35),
            # 汽轮机-三级低加！B37 lh2_water_temperature
            ImageInfo('0', (3025, 2361), getstrcolm(turbineBackpressure.lh2_water_temperature), 35),
            # 汽轮机-三级低加！I37 lh2_extraction_pressure
            ImageInfo('0', (3025, 3152), getstrcolm(turbineBackpressure.lh2_extraction_pressure), 35),
            # 汽轮机-三级低加！J37 lh2_extraction_enthalpy
            ImageInfo('0', (3027, 2463), getstrcolm(turbineBackpressure.lh2_extraction_enthalpy), 35),
            # --
            ImageInfo('0', (3242, 2361), '--', 35),
            # --
            ImageInfo('0', (3244, 3415), '--', 35),
            # 汽轮机-三级低加！K37 lh2_extraction_amount
            ImageInfo('0', (3247, 2460), getstrcolm(turbineBackpressure.lh2_extraction_amount), 35),
            # 汽轮机-三级低加！F37 lh2_saturated_water_enthalpy
            ImageInfo('0', (3247, 3510), getstrcolm(turbineBackpressure.lh2_saturated_water_enthalpy), 35),
            # 汽轮机计算！F24' e_steam_extraction_select
            ImageInfo('0', (3259, 1462), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # --
            ImageInfo('0', (3308, 3151), '--', 35),
            # 汽轮机-三级低加！C38 lh3_water_enthalpy
            ImageInfo('0', (3312, 3255), getstrcolm(turbineBackpressure.lh3_water_enthalpy), 35),
            # 汽轮机-三级低加！E37 lh2_saturated_water_temperature
            ImageInfo('0', (3471, 3414), getstrcolm(turbineBackpressure.lh2_saturated_water_temperature), 35),
            # 汽轮机-三级低加！K36+K37 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3474, 3512), getstrcolm(plus_36_37), 35),
            # 汽轮机-三级低加！K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3527, 3253), getstrcolm(plus_four), 35),
            # 汽轮机-三级低加！B38 lh3_water_temperature
            ImageInfo('0', (3528, 3157), getstrcolm(turbineBackpressure.lh3_water_temperature), 35),
            # 汽轮机-三级低加！I38 lh3_extraction_pressure
            ImageInfo('0', (3529, 2361), getstrcolm(turbineBackpressure.lh3_extraction_pressure), 35),
            # 汽轮机-三级低加！J38 lh3_extraction_enthalpy
            ImageInfo('0', (3532, 2463), getstrcolm(turbineBackpressure.lh3_extraction_enthalpy), 35),
            # 汽轮机-三级低加！F69 i_exhaust_point_pressure
            ImageInfo('0', (3562, 1115), getstrcolm(turbineBackpressure.i_exhaust_point_pressure), 35),
            # 汽轮机-三级低加！F72 i_exhaust_point_enthalpy
            ImageInfo('0', (3565, 1208), getstrcolm(turbineBackpressure.i_exhaust_point_enthalpy), 35),
            # --
            ImageInfo('0', (3754, 2362), '--', 35),
            # 汽轮机-三级低加！K38 lh3_extraction_amount
            ImageInfo('0', (3754, 2457), getstrcolm(turbineBackpressure.lh3_extraction_amount), 35),
            # --
            ImageInfo('0', (3781, 3418), '--', 35),
            # 汽轮机-三级低加！F38 lh3_saturated_water_enthalpy
            ImageInfo('0', (3783, 3517), getstrcolm(turbineBackpressure.lh3_saturated_water_enthalpy), 35),
            # 汽轮机-三级低加！F70 i_exhaust_point_temperature
            ImageInfo('0', (3796, 1115), getstrcolm(turbineBackpressure.i_exhaust_point_temperature), 35),
            # 汽轮机-三级低加！F73 i_exhaust_point_flow
            ImageInfo('0', (3800, 1213), getstrcolm(turbineBackpressure.i_exhaust_point_flow), 35),
            # --
            ImageInfo('0', (3815, 3151), '--', 35),
            # 汽轮机-三级低加！C39 c_water_enthalpy
            ImageInfo('0', (3816, 3248), getstrcolm(turbineBackpressure.c_water_enthalpy), 35),
            # 汽轮机-三级低加！B39 c_water_temperature
            ImageInfo('0', (3979, 3151), getstrcolm(turbineBackpressure.c_water_temperature), 35),
            # 汽轮机-三级低加！K36+K37+K38+F100 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3981, 3246), getstrcolm(plus_four), 35),
            # 汽轮机-三级低加！E38 lh3_saturated_water_temperature
            ImageInfo('0', (4009, 3415), getstrcolm(turbineBackpressure.lh3_saturated_water_temperature), 35),
            # 汽轮机-三级低加！K36+K37+K38 lh1_extraction_amount+lh2_extraction_amount+lh3_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (4010, 3511), getstrcolm(plus_three), 35),
            # 汽轮机计算！F93 i_steam_exhaust_pressure
            ImageInfo('0', (4532, 1864), getstrcolm(turbineBackpressure.i_steam_exhaust_pressure), 35),
            # 汽轮机计算！F96 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4534, 1961), getstrcolm(turbineBackpressure.i_steam_exhaust_enthalpy_actual), 35),
            # --
            ImageInfo('0', (4751, 1864), '--', 35),
            # 汽轮机计算！F100 i_steam_exhaust_flow
            ImageInfo('0', (4751, 1958), getstrcolm(turbineBackpressure.i_steam_exhaust_flow), 35),
            # --
            ImageInfo('0', (4857, 2562), '--', 35),
            # --
            ImageInfo('0', (4861, 2658), '--', 35),
            # 汽轮机计算！F24 e_steam_extraction_select
            ImageInfo('0', (4952, 1512), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 20/33
            ImageInfo('0', (5073, 2562), '20/33', 35),
            # 循环水系统计算！E9 v_total_circulating_water_select
            ImageInfo('0', (5074, 2657), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            # --
            ImageInfo('0', (5111, 1867), '--', 35),
            # --
            ImageInfo('0', (5115, 1968), '--', 35),
            # 30/43
            ImageInfo('0', (5322, 1863), '30/43', 35),
            # u'循环水系统！E9' v_total_circulating_water_select
            ImageInfo('0', (5324, 1964), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            # u'循环水系统！E14'  v_evaporation_loss
            ImageInfo('0', (6100, 1440), getstrcolm(circulatingWater.v_evaporation_loss), 70),
            # u'循环水系统！E19' v_discharge_capacity
            ImageInfo('0', (6752, 3558), getstrcolm(circulatingWater.v_discharge_capacity), 70),
            # u'循环水系统！F16' v_partial_blow_loss
            ImageInfo('0', (7006, 1442), getstrcolm(circulatingWater.v_partial_blow_loss), 70),
            # u'循环水系统！F24' v_amount_of_makeup_water
            ImageInfo('0', (8616, 3410), getstrcolm(circulatingWater.v_amount_of_makeup_water), 70)
        ]

# 原则性热力系统图P2a作成
def getBiomasssHotImgInfoListP2a(plan_id):

        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_three = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount

        sewage_quantity = 0
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000

        plus_35_99 = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_35_99 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.i_steam_exhaust_flow
        multiply_f33_g19 = 0
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        plus_35_36 = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_35_36 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount

        return [
            # 锅炉辅机！G88 f_economizer_entry_pressure
            ImageInfo('0', (753, 1673), getstrcolm(boilerAuxiliaries.f_economizer_entry_pressure), 35),
            # 汽轮机计算-0级高加!C32 hh1_water_enthalpy
            ImageInfo('0', (753, 1765), getstrcolm(turbineBackpressure.hh1_water_enthalpy), 35),
            # 锅炉辅机!E32 c_drum_pressure
            ImageInfo('0', (753, 2981), getstrcolm(boilerAuxiliaries.c_drum_pressure), 35),
            # 锅炉辅机!E33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (757, 3081), getstrcolm(boilerAuxiliaries.c_drum_aturatedwater_enthalpy), 35),
            ImageInfo('0', (981, 2981), "--", 35),
            # 锅炉辅机!E31/1000 c_sewage_quantity/1000
            ImageInfo('0', (981, 3077), getstrcolm(sewage_quantity), 35),
            # 汽轮机计算-0级高加！B32 hh1_water_temperature
            ImageInfo('0', (1049, 1665), getstrcolm(turbineBackpressure.hh1_water_temperature), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1053, 1773), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1273, 929), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-0级高加！G34 d_work_pressure
            ImageInfo('0', (1693, 3983), getstrcolm(turbineBackpressure.d_work_pressure), 35),
            # 汽轮机计算-0级高加！C34 d_water_enthalpy
            ImageInfo('0', (1693, 4079), getstrcolm(turbineBackpressure.d_water_enthalpy), 35),
            # 汽轮机计算-0级高加！J34 d_extraction_enthalpy
            ImageInfo('0', (1957, 2441), getstrcolm(turbineBackpressure.d_extraction_enthalpy), 35),
            # 汽轮机计算-0级高加！I34 d_extraction_pressure
            ImageInfo('0', (1961, 2349), getstrcolm(turbineBackpressure.d_extraction_pressure), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1993, 4079), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-0级高加！B34 d_water_temperature
            ImageInfo('0', (2001, 3995), getstrcolm(turbineBackpressure.d_water_temperature), 35),
            ImageInfo('0', (2241, 2361), "--", 35),
            # 汽轮机计算-0级高加！K34 d_extraction_amount
            ImageInfo('0', (2245, 2445), getstrcolm(turbineBackpressure.d_extraction_amount), 35),
            # 锅炉计算!G20 f_steam_pressure_design
            ImageInfo('0', (2549, 369), getstrcolm(furnaceCalculation.f_steam_pressure_design), 35),
            # 锅炉计算!G22 f_steam_enthalpy_design
            ImageInfo('0', (2549, 469), getstrcolm(furnaceCalculation.f_steam_enthalpy_design), 35),
            # 汽轮机计算-0级高加！H33 h_enthalpy
            ImageInfo('0', (2577, 4223), getstrcolm(turbineBackpressure.h_enthalpy), 35),
            # 汽轮机计算-0级高加！F33 h_pressure
            ImageInfo('0', (2593, 4127), getstrcolm(turbineBackpressure.h_pressure), 35),
            # 汽轮机计算-0级高加！C35 lh1_water_enthalpy
            ImageInfo('0', (2601, 3253), getstrcolm(turbineBackpressure.lh1_water_enthalpy), 35),
            ImageInfo('0', (2621, 3149), "--", 35),
            # 锅炉计算!G21 f_steam_temperature_design
            ImageInfo('0', (2765, 369), getstrcolm(furnaceCalculation.f_steam_temperature_design), 35),
            # 汽轮机计算-0级高加！F26 e_throttle_flow
            ImageInfo('0', (2765, 465), getstrcolm(turbineBackpressure.e_throttle_flow), 35),
            # 汽轮机计算-0级高加！B35 lh1_water_temperature
            ImageInfo('0', (2853, 3145), getstrcolm(turbineBackpressure.lh1_water_temperature), 35),
            # lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2857, 3241), getstrcolm(plus_three), 35),
            # 锅炉计算G19 * 汽轮机0级高加J33
            ImageInfo('0', (2949, 4219), getstrcolm(multiply_f33_g19), 35),
            # 汽轮机计算-0级高加！D33 h_temperature
            ImageInfo('0', (2957, 4123), getstrcolm(turbineBackpressure.h_temperature), 35),
            # 汽轮机计算-0级高加！J35 lh1_extraction_enthalpy
            ImageInfo('0', (3241, 2461), getstrcolm(turbineBackpressure.lh1_extraction_enthalpy), 35),
            # 汽轮机计算-0级高加！I35 lh1_extraction_pressure
            ImageInfo('0', (3245, 2361), getstrcolm(turbineBackpressure.lh1_extraction_pressure), 35),
            # 汽轮机计算-0级高加！F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (3293, 3539), getstrcolm(turbineBackpressure.lh1_saturated_water_enthalpy), 35),
            ImageInfo('0', (3296, 3441), "--", 35),

            # 汽轮机计算-0级高加！C36 lh2_water_enthalpy
            ImageInfo('0', (3369, 3245), getstrcolm(turbineBackpressure.lh2_water_enthalpy), 35),
            ImageInfo('0', (3373, 3149), "--", 35),
            # 汽轮机0级高加K35 lh1_extraction_amount
            ImageInfo('0', (3477, 2461), getstrcolm(turbineBackpressure.lh1_extraction_amount), 35),
            ImageInfo('0', (3485, 2365), "--", 35),
            # 汽轮机0级高加K35 lh1_extraction_amount
            ImageInfo('0', (3531, 3537), getstrcolm(turbineBackpressure.lh1_extraction_amount), 35),
            # 汽轮机计算-0级高加！E35 lh1_saturated_water_temperature
            ImageInfo('0', (3532, 3444), getstrcolm(turbineBackpressure.lh1_saturated_water_temperature), 35),
            # 汽轮机计算-0级高加！B36 lh2_water_temperature 
            ImageInfo('0', (3621, 3149), getstrcolm(turbineBackpressure.lh2_water_temperature), 35),
            # 汽轮机计算-0级高加！(K35+K35+F99) lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3621, 3237), getstrcolm(plus_three), 35),
            # 汽轮机计算-0级高加！F24 e_steam_extraction_select
            ImageInfo('0', (3653, 1445), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 汽轮机计算-0级高加！J36 lh2_extraction_enthalpy
            ImageInfo('0', (3865, 2465), getstrcolm(turbineBackpressure.lh2_extraction_enthalpy), 35),
            # 汽轮机计算-0级高加！I36 lh2_extraction_pressure
            ImageInfo('0', (3869, 2357), getstrcolm(turbineBackpressure.lh2_extraction_pressure), 35),
            ImageInfo('0', (3953, 3444), "--", 35),
            # 汽轮机计算-0级高加！F36 lh2_saturated_water_enthalpy
            ImageInfo('0', (3953, 3539), getstrcolm(turbineBackpressure.lh2_saturated_water_enthalpy), 35),
            # 汽轮机计算-0级高加！F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3965, 1197), getstrcolm(turbineBackpressure.i_exhaust_point_enthalpy), 35),
            # 汽轮机计算-0级高加！F68 i_exhaust_point_pressure
            ImageInfo('0', (3969, 1101), getstrcolm(turbineBackpressure.i_exhaust_point_pressure), 35),
            ImageInfo('0', (4101, 2369), "--", 35),
            # 汽轮机0级高加K36 lh2_extraction_amount
            ImageInfo('0', (4101, 2461), getstrcolm(turbineBackpressure.lh2_extraction_amount), 35),
            # 汽轮机计算-0级高加！C38 c_water_enthalpy
            ImageInfo('0', (4101, 3245), getstrcolm(turbineBackpressure.c_water_enthalpy), 35),
            ImageInfo('0', (4113, 3141), "--", 35),
            # 汽轮机计算-0级高加！E36 lh2_saturated_water_temperature
            ImageInfo('0', (4196, 3441), getstrcolm(turbineBackpressure.c_water_enthalpy), 35),
            # 汽轮机计算-0级高加！(K35+K36) lh1_extraction_amount+lh2_extraction_amount
            ImageInfo('0', (4197, 3535), getstrcolm(plus_35_36), 35),
            # 汽轮机计算-0级高加！F72 i_exhaust_point_flow
            ImageInfo('0', (4201, 1197), getstrcolm(turbineBackpressure.i_exhaust_point_flow), 35),
            # 汽轮机计算-0级高加！F69 i_exhaust_point_temperature
            ImageInfo('0', (4213, 1097), getstrcolm(turbineBackpressure.i_exhaust_point_temperature), 35),
            # 汽轮机计算-0级高加！B38 c_water_temperature
            ImageInfo('0', (4345, 3146), getstrcolm(turbineBackpressure.c_water_temperature), 35),
            # 汽轮机计算-0级高加！(K35+K35+F99) lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (4349, 3249), getstrcolm(plus_three), 35),
            # 汽轮机计算-0级高加！F95 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4949, 1965), getstrcolm(turbineBackpressure.i_steam_exhaust_enthalpy_actual), 35),
            # 汽轮机计算-0级高加！F92 i_steam_exhaust_pressure
            ImageInfo('0', (4957, 1861), getstrcolm(turbineBackpressure.i_steam_exhaust_pressure), 35),
            # 汽轮机计算-0级高加！F99 i_steam_exhaust_flow
            ImageInfo('0', (5213, 1957), getstrcolm(turbineBackpressure.i_steam_exhaust_flow), 35),
            ImageInfo('0', (5217, 1857), "--", 35),
            ImageInfo('0', (5289, 2569), "--", 35),
            ImageInfo('0', (5289, 2665), "--", 35),
            # 汽轮机计算0级高加!F24 e_steam_extraction_select
            ImageInfo('0', (5363, 1492), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # ImageInfo('0', (5505, 2577), getstrcolm(turbineBackpressure.), 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5505, 2669), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            ImageInfo('0', (5537, 1865), "--", 35),
            ImageInfo('0', (5541, 1969), "--", 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5753, 1957), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            ImageInfo('0', (5757, 1865), "30/43", 35),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6221, 1245), getstrcolm(circulatingWater.v_evaporation_loss), 70),
            # 循环水K22 p_select_f
            ImageInfo('0', (6361, 2765), getstrcolm(circulatingWater.p_select_f), 70),
            # 循环水E19 v_discharge_capacity
            ImageInfo('0', (6605, 3443), getstrcolm(circulatingWater.v_discharge_capacity), 70),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (7173, 1234), getstrcolm(circulatingWater.v_partial_blow_loss), 70),
            # 循环水E20 v_amount_of_makeup_water
            ImageInfo('0', (8180, 3293), getstrcolm(circulatingWater.v_amount_of_makeup_water), 70),
            ImageInfo('0', (5505, 2575), "20/33", 35),
        ]


# 原则性热力系统图P2b作成
def getBiomasssHotImgInfoListP2b(plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_three = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount and turbineBackpressure.lh3_extraction_amount:
            plus_three = turbineBackpressure.lh1_extraction_amount+turbineBackpressure.lh2_extraction_amount+turbineBackpressure.lh3_extraction_amount
        plus_35_36 = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.lh2_extraction_amount:
            plus_35_36 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.lh2_extraction_amount

        sewage_quantity = 0
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000

        multiply_f33_g19 = 0
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design

        return [
            # 锅炉辅机e33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (389, 3063), getstrcolm(boilerAuxiliaries.c_drum_aturatedwater_enthalpy), 35),
            # 锅炉辅机！E32 c_drum_pressure
            ImageInfo('0', (393, 2973), getstrcolm(boilerAuxiliaries.c_drum_pressure), 35),
            # 锅炉辅机！G88 f_economizer_entry_pressure
            ImageInfo('0', (395, 1687), getstrcolm(boilerAuxiliaries.f_economizer_entry_pressure), 35),
            # 汽轮机计算-0级高加!C32 hh1_water_enthalpy
            ImageInfo('0', (397, 1771), getstrcolm(turbineBackpressure.hh1_water_enthalpy), 35),
            ImageInfo('0', (611, 2977), "--", 35),
            # 锅炉辅机!E31/1000 c_sewage_quantity/1000
            ImageInfo('0', (613, 3065), getstrcolm(sewage_quantity), 35),
            # 汽轮机计算-0级高加！B32 hh1_water_temperature
            ImageInfo('0', (679, 1681), getstrcolm(turbineBackpressure.hh1_water_temperature), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (685, 1777), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (905, 949), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-0级高加！G34 d_work_pressure
            ImageInfo('0', (1317, 3963), getstrcolm(turbineBackpressure.d_work_pressure), 35),
            # 汽轮机计算-0级高加！C34 d_water_enthalpy
            ImageInfo('0', (1319, 4059), getstrcolm(turbineBackpressure.d_water_enthalpy), 35),
            # 汽轮机计算-0级高加！I34 d_extraction_pressure
            ImageInfo('0', (1575, 2355), getstrcolm(turbineBackpressure.d_extraction_pressure), 35),
            # 汽轮机计算-0级高加！J34 d_extraction_enthalpy
            ImageInfo('0', (1577, 2449), getstrcolm(turbineBackpressure.d_extraction_enthalpy), 35),
            # 汽轮机计算-0级高加！B34 d_water_temperature
            ImageInfo('0', (1616, 3966), getstrcolm(turbineBackpressure.d_water_temperature), 35),
            # 锅炉计算！G19 f_steam_flow_design
            ImageInfo('0', (1620, 4059), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-0级高加！K34 d_extraction_amount
            ImageInfo('0', (1861, 2451), getstrcolm(turbineBackpressure.d_extraction_amount), 35),
            ImageInfo('0', (1867, 2355), "--", 35),
            # 锅炉计算!G22 f_steam_enthalpy_design
            ImageInfo('0', (2163, 495), getstrcolm(furnaceCalculation.f_steam_enthalpy_design), 35),
            # 锅炉计算!G20 f_steam_pressure_design
            ImageInfo('0', (2167, 401), getstrcolm(furnaceCalculation.f_steam_pressure_design), 35),
            # 汽轮机计算-0级高加！F33 h_pressure
            ImageInfo('0', (2197, 4106), getstrcolm(turbineBackpressure.h_pressure), 35),
            # 汽轮机计算-0级高加！H33 h_enthalpy
            ImageInfo('0', (2201, 4200), getstrcolm(turbineBackpressure.h_enthalpy), 35),
            # 汽轮机计算-0级高加！C35 lh1_water_enthalpy
            ImageInfo('0', (2213, 3235), getstrcolm(turbineBackpressure.lh1_water_enthalpy), 35),
            ImageInfo('0', (2217, 3147), "--", 35),
            # 汽轮机计算-0级高加！F26 e_throttle_flow
            ImageInfo('0', (2379, 487), getstrcolm(turbineBackpressure.e_throttle_flow), 35),
            ImageInfo('0', (2395, 403), "--", 35),
            # 汽轮机计算-0级高加！B35 lh1_water_temperature
            ImageInfo('0', (2457, 3131), getstrcolm(turbineBackpressure.lh1_water_temperature), 35),
            # lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (2461, 3235), getstrcolm(plus_three), 35),
            # 汽轮机计算-0级高加！D33 h_temperature
            ImageInfo('0', (2568, 4106), getstrcolm(turbineBackpressure.h_temperature), 35),
            # 锅炉计算G19 * 汽轮机0级高加J33
            ImageInfo('0', (2568, 4196), getstrcolm(multiply_f33_g19), 35),
            # 汽轮机计算-0级高加！I35 lh1_extraction_pressure
            ImageInfo('0', (2843, 2365), getstrcolm(turbineBackpressure.lh1_extraction_pressure), 35),
            # 汽轮机计算-0级高加！J35 lh1_extraction_enthalpy
            ImageInfo('0', (2847, 2463), getstrcolm(turbineBackpressure.lh1_extraction_enthalpy), 35),
            ImageInfo('0', (2895, 3433), "--", 35),
            # 汽轮机计算-0级高加！F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (2903, 3527), getstrcolm(turbineBackpressure.lh1_saturated_water_enthalpy), 35),
            # 汽轮机计算-0级高加！C36 lh2_water_enthalpy
            ImageInfo('0', (2972, 3233), getstrcolm(turbineBackpressure.lh2_water_enthalpy), 35),
            ImageInfo('0', (2975, 3137), "--", 35),
            ImageInfo('0', (3079, 2367), "--", 35),
            # 汽轮机0级高加K35 lh1_extraction_amount
            ImageInfo('0', (3083, 2461), getstrcolm(turbineBackpressure.lh1_extraction_amount), 35),
            # 汽轮机0级高加K35 lh1_extraction_amount
            ImageInfo('0', (3135, 3527), getstrcolm(turbineBackpressure.lh1_extraction_amount), 35),
            # 汽轮机计算-0级高加！E35 lh1_saturated_water_temperature
            ImageInfo('0', (3137, 3435), getstrcolm(turbineBackpressure.lh1_saturated_water_temperature), 35),
            # 汽轮机计算-0级高加！(K35+K35+F99) lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3215, 3235), getstrcolm(plus_three), 35),
            # 汽轮机计算-0级高加！B36 lh2_water_temperature 
            ImageInfo('0', (3225, 3141), getstrcolm(turbineBackpressure.lh2_water_temperature), 35),
            # 汽轮机计算-0级高加！F24 e_steam_extraction_select
            ImageInfo('0', (3253, 1457), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 汽轮机计算-0级高加！J36 lh2_extraction_enthalpy
            ImageInfo('0', (3455, 2461), getstrcolm(turbineBackpressure.lh2_extraction_enthalpy), 35),
            # 汽轮机计算-0级高加！I36 lh2_extraction_pressure
            ImageInfo('0', (3463, 2367), getstrcolm(turbineBackpressure.lh2_extraction_pressure), 35),
            ImageInfo('0', (3545, 3425), "--", 35),
            # 汽轮机计算-0级高加！F36 lh2_saturated_water_enthalpy
            ImageInfo('0', (3545, 3527), getstrcolm(turbineBackpressure.lh2_saturated_water_enthalpy), 35),
            # 汽轮机计算-0级高加！F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3557, 1215), getstrcolm(turbineBackpressure.i_exhaust_point_enthalpy), 35),
            # 汽轮机计算-0级高加！F68 i_exhaust_point_pressure
            ImageInfo('0', (3559, 1125), getstrcolm(turbineBackpressure.i_exhaust_point_pressure), 35),
            # 汽轮机0级高加K36 lh2_extraction_amount
            ImageInfo('0', (3693, 2461), getstrcolm(turbineBackpressure.lh2_extraction_amount), 35),
            ImageInfo('0', (3695, 2369), "--", 35),
            # 汽轮机计算-0级高加！C38 c_water_enthalpy
            ImageInfo('0', (3695, 3237), getstrcolm(turbineBackpressure.c_water_enthalpy), 35),
            ImageInfo('0', (3697, 3143), "--", 35),
            # 汽轮机计算-0级高加！E36 lh2_saturated_water_temperature
            ImageInfo('0', (3787, 3431), getstrcolm(turbineBackpressure.lh2_saturated_water_temperature), 35),
            # 汽轮机计算-0级高加！(K35+K36) lh1_extraction_amount+lh2_extraction_amount
            ImageInfo('0', (3793, 3527), getstrcolm(plus_35_36), 35),
            # 汽轮机计算-0级高加！F72 i_exhaust_point_flow
            ImageInfo('0', (3798, 1213), getstrcolm(turbineBackpressure.i_exhaust_point_flow), 35),
            # 汽轮机计算-0级高加！F69 i_exhaust_point_temperature
            ImageInfo('0', (3800, 1121), getstrcolm(turbineBackpressure.i_exhaust_point_temperature), 35),
            # 汽轮机计算-0级高加！B38 c_water_temperature
            ImageInfo('0', (3933, 3141), getstrcolm(turbineBackpressure.c_water_temperature), 35),
            # 汽轮机计算-0级高加！(K35+K35+F99) lh1_extraction_amount+lh2_extraction_amount+i_steam_exhaust_flow
            ImageInfo('0', (3933, 3237), getstrcolm(plus_three), 35),
            # 汽轮机计算-0级高加！F92 i_steam_exhaust_pressure
            ImageInfo('0', (4534, 1873), getstrcolm(turbineBackpressure.i_steam_exhaust_pressure), 35),
            # 汽轮机计算-0级高加！F95 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4534, 1957), getstrcolm(turbineBackpressure.i_steam_exhaust_enthalpy_actual), 35),
            ImageInfo('0', (4800, 1869), "--", 35),
            # 汽轮机计算-0级高加！F99 i_steam_exhaust_flow
            ImageInfo('0', (4802, 1967), getstrcolm(turbineBackpressure.i_steam_exhaust_flow), 35),
            ImageInfo('0', (4860, 2575), "--", 35),
            ImageInfo('0', (4864, 2667), "--", 35),
            # 汽轮机计算0级高加!F24 e_steam_extraction_select
            ImageInfo('0', (4944, 1507), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5074, 2665), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            ImageInfo('0', (5082, 2567), "20/23", 35),
            ImageInfo('0', (5112, 1867), "--", 35),
            ImageInfo('0', (5114, 1965), "--", 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5324, 1967), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            ImageInfo('0', (5326, 1871), "30/43", 35),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6088, 1433), getstrcolm(circulatingWater.v_evaporation_loss), 70),
            # 循环水K24 p_count
            ImageInfo('0', (6182, 1965), getstrcolm(circulatingWater.p_count), 60),
            # 循环水K26 p_select_s
            ImageInfo('0', (6526, 1963), getstrcolm(circulatingWater.p_select_s), 60),
            # 循环水E19 v_discharge_capacity
            ImageInfo('0', (6736, 3543), getstrcolm(circulatingWater.v_discharge_capacity), 70),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (6998, 1431), getstrcolm(circulatingWater.v_partial_blow_loss), 70),
            # 循环水E20 v_amount_of_makeup_water
            ImageInfo('0', (8600, 3403), getstrcolm(circulatingWater.v_amount_of_makeup_water), 70),
        ]


# 原则性热力系统图P3a作成
def getBiomasssHotImgInfoListP3a(plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)

        plus_35_36 = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_35_36 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.i_steam_exhaust_flow

        sewage_quantity = 0
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000

        multiply_f33_g19 = 0
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design

        return [
            # 锅炉辅机E33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (753, 3073), getstrcolm(boilerAuxiliaries.c_drum_aturatedwater_enthalpy), 35),
            # 汽轮机计算-1级高加F32 hh1_saturated_water_enthalpy
            ImageInfo('0', (755, 2575), getstrcolm(turbineBackpressure.hh1_saturated_water_enthalpy), 35),
            # 汽轮机计算-1级高加C32 hh1_water_enthalpy
            ImageInfo('0', (759, 1763), getstrcolm(turbineBackpressure.hh1_water_enthalpy), 35),
            # 锅炉辅机E32 c_drum_pressure
            ImageInfo('0', (759, 2977), getstrcolm(boilerAuxiliaries.c_drum_pressure), 35),
            # 锅炉辅机G88 f_economizer_entry_pressure
            ImageInfo('0', (761, 1669), getstrcolm(boilerAuxiliaries.f_economizer_entry_pressure), 35),
            # --
            ImageInfo('0', (761, 2487), '--', 35),
            # 锅炉辅机E31 c_sewage_quantity/1000
            ImageInfo('0', (975, 3075), getstrcolm(sewage_quantity), 35),
            # --
            ImageInfo('0', (981, 2977), '--', 35),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1047, 1767), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-1级高加B32 hh1_water_temperature
            ImageInfo('0', (1057, 1661), getstrcolm(turbineBackpressure.hh1_water_temperature), 35),
            # 汽轮机计算-1级高加K32 hh1_extraction_amount
            ImageInfo('0', (1057, 2575), getstrcolm(turbineBackpressure.hh1_extraction_amount), 35),
            # 汽轮机计算-1级高加E32 hh1_saturated_water_temperature
            ImageInfo('0', (1059, 2491), getstrcolm(turbineBackpressure.hh1_saturated_water_temperature), 35),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1273, 937), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-1级高加C34 d_water_enthalpy
            ImageInfo('0', (1691, 4081), getstrcolm(turbineBackpressure.d_water_enthalpy), 35),
            # 汽轮机计算-1级高加G34 d_work_pressure
            ImageInfo('0', (1697, 3981), getstrcolm(turbineBackpressure.d_work_pressure), 35),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1993, 4081), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-1级高加B34 d_water_temperature
            ImageInfo('0', (1997, 3979), getstrcolm(turbineBackpressure.d_water_temperature), 35),
            # 汽轮机计算-1级高加J32 hh1_extraction_enthalpy
            ImageInfo('0', (2303, 1821), getstrcolm(turbineBackpressure.hh1_extraction_enthalpy), 35),
            # 汽轮机计算-1级高加I32 hh1_extraction_pressure
            ImageInfo('0', (2305, 1729), getstrcolm(turbineBackpressure.hh1_extraction_pressure), 35),
            # 锅炉计算G20 f_steam_pressure_design
            ImageInfo('0', (2553, 369), getstrcolm(furnaceCalculation.f_steam_pressure_design), 35),
            # 锅炉计算G22 f_steam_enthalpy_design
            ImageInfo('0', (2553, 469), getstrcolm(furnaceCalculation.f_steam_enthalpy_design), 35),
            # 汽轮机计算-1级高加F33 h_pressure
            ImageInfo('0', (2587, 4125), getstrcolm(turbineBackpressure.h_pressure), 35),
            # 汽轮机计算-1级高加H33 h_enthalpy
            ImageInfo('0', (2591, 4221), getstrcolm(turbineBackpressure.h_enthalpy), 35),
            # 汽轮机计算-1级高加K32 hh1_extraction_amount
            ImageInfo('0', (2593, 1823), getstrcolm(turbineBackpressure.hh1_extraction_amount), 35),
            # --
            ImageInfo('0', (2595, 1729), '--', 35),
            # 汽轮机计算-1级高加J34 d_extraction_enthalpy
            ImageInfo('0', (2729, 2447), getstrcolm(turbineBackpressure.d_extraction_enthalpy), 35),
            # 汽轮机计算-1级高加I34 d_extraction_pressure
            ImageInfo('0', (2733, 2353), getstrcolm(turbineBackpressure.d_extraction_pressure), 35),
            # 汽轮机计算-1级高加C35 lh1_water_enthalpy
            ImageInfo('0', (2771, 3241), getstrcolm(turbineBackpressure.lh1_water_enthalpy), 35),
            # 锅炉计算G21 f_steam_temperature_design
            ImageInfo('0', (2773, 365), getstrcolm(furnaceCalculation.f_steam_temperature_design), 35),
            # --
            ImageInfo('0', (2775, 3145), '--', 35),
            # 汽轮机计算-1级高加F26 e_steam_extraction_select
            ImageInfo('0', (2777, 461), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 汽轮机计算-1级高加J33 h_amount * 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (2951, 4215), getstrcolm(multiply_f33_g19), 35),
            # 汽轮机计算-1级高加D33 h_temperature
            ImageInfo('0', (2971, 4125), getstrcolm(turbineBackpressure.h_temperature), 35),
            # --
            ImageInfo('0', (3013, 2349), '--', 35),
            # 汽轮机计算-1级高加K34 d_extraction_amount
            ImageInfo('0', (3019, 2447), getstrcolm(turbineBackpressure.d_extraction_amount), 35),
            # 汽轮机计算-1级高加B35 lh1_water_temperature
            ImageInfo('0', (3053, 3147), getstrcolm(turbineBackpressure.lh1_water_temperature), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount+F93 i_steam_exhaust_flow
            ImageInfo('0', (3057, 3243), getstrcolm(plus_35_36), 35),
            # 汽轮机计算-1级高加J33 h_amount * 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (3653, 1447), getstrcolm(multiply_f33_g19), 35),
            # 汽轮机计算-1级高加F24 e_steam_extraction_select
            ImageInfo('0', (3654, 1447), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 汽轮机计算-1级高加J35 lh1_extraction_enthalpy
            ImageInfo('0', (3654, 2519), getstrcolm(turbineBackpressure.lh1_extraction_enthalpy), 35),
            # 汽轮机计算-1级高加F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (3656, 3235), getstrcolm(turbineBackpressure.lh1_saturated_water_enthalpy), 35),
            # 汽轮机计算-1级高加I35 lh1_extraction_pressure
            ImageInfo('0', (3658, 2425), getstrcolm(turbineBackpressure.lh1_extraction_pressure), 35),
            # --
            ImageInfo('0', (3660, 3141), '--', 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount
            ImageInfo('0', (3934, 2521), getstrcolm(turbineBackpressure.lh1_extraction_amount), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount
            ImageInfo('0', (3936, 3241), getstrcolm(turbineBackpressure.lh1_extraction_amount), 35),
            # 汽轮机计算-1级高加E35 lh1_saturated_water_temperature
            ImageInfo('0', (3942, 3145), getstrcolm(turbineBackpressure.lh1_saturated_water_temperature), 35),
            # --
            ImageInfo('0', (3954, 2425), '--', 35),
            # 汽轮机计算-1级高加F68 i_exhaust_point_pressure
            ImageInfo('0', (3965, 1109), getstrcolm(turbineBackpressure.i_exhaust_point_pressure), 35),
            # 汽轮机计算-1级高加F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3965, 1193), getstrcolm(turbineBackpressure.i_exhaust_point_enthalpy), 35),
            # 汽轮机计算-1级高加F69 i_exhaust_point_temperature
            ImageInfo('0', (4201, 1101), getstrcolm(turbineBackpressure.i_exhaust_point_temperature), 35),
            # 汽轮机计算-1级高加F72 i_exhaust_point_flow
            ImageInfo('0', (4205, 1201), getstrcolm(turbineBackpressure.i_exhaust_point_flow), 35),
            # 汽轮机计算-1级高加C38 c_water_enthalpy
            ImageInfo('0', (4428, 3237), getstrcolm(turbineBackpressure.c_water_enthalpy), 35),
            # --
            ImageInfo('0', (4432, 3141), '--', 35),
            # 汽轮机计算-1级高加B38 c_water_temperature
            ImageInfo('0', (4710, 3143), getstrcolm(turbineBackpressure.c_water_temperature), 35),
            # 汽轮机计算-1级高加K35+F93 lh1_extraction_amount + i_steam_exhaust_flow
            ImageInfo('0', (4716, 3237), getstrcolm(plus_35_36), 35),
            # 汽轮机计算-1级高加F93 i_steam_exhaust_flow  -->F86 i_steam_exhaust_pressure
            ImageInfo('0', (4948, 1859), getstrcolm(turbineBackpressure.i_steam_exhaust_pressure), 35),
            # 汽轮机计算-1级高加F96 i_calculation_error -->F89 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4954, 1959), getstrcolm(turbineBackpressure.i_steam_exhaust_enthalpy_actual), 35),
            # 汽轮机计算-1级高加F93 i_steam_exhaust_flow
            ImageInfo('0', (5190, 1957), getstrcolm(turbineBackpressure.i_steam_exhaust_flow), 35),
            # --
            ImageInfo('0', (5192, 1863), '--', 35),
            # --
            ImageInfo('0', (5278, 2669), '--', 35),
            # --
            ImageInfo('0', (5282, 2569), '--', 35),
            # 汽轮机计算-1级高加F24 e_steam_extraction_select
            ImageInfo('0', (5364, 1495), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 循环水系统计算E9 v_total_circulating_water_select
            ImageInfo('0', (5492, 2667), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            # --
            ImageInfo('0', (5502, 2573), u'20/33', 35),
            # --
            ImageInfo('0', (5528, 1951), '--', 35),
            # --
            ImageInfo('0', (5534, 1857), '--', 35),
            # --
            ImageInfo('0', (5748, 1855), u'30/43', 35),
            # 循环水系统计算E9 v_total_circulating_water_select
            ImageInfo('0', (5748, 1951), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            # 循环水系统计算E14 v_evaporation_loss
            ImageInfo('0', (6222, 1239), getstrcolm(circulatingWater.v_evaporation_loss), 70),
            # 循环水系统计算K22 p_select_f
            ImageInfo('0', (6334, 2827), getstrcolm(circulatingWater.p_select_f), 70),
            # 循环水系统计算E19 v_discharge_capacity
            ImageInfo('0', (6610, 3441), getstrcolm(circulatingWater.v_discharge_capacity), 70),
            # (循环水系统计算E16) v_partial_blow_loss
            ImageInfo('0', (7170, 1241), getstrcolm(circulatingWater.v_partial_blow_loss), 70),
            # 循环水系统计算E20 v_amount_of_makeup_water
            ImageInfo('0', (8186, 3285), getstrcolm(circulatingWater.v_amount_of_makeup_water), 70)
        ]

# 原则性热力系统图P3b作成
def getBiomasssHotImgInfoListP3b(plan_id):
        furnaceCalculation, boilerAuxiliaries, turbineBackpressure, circulatingWater = GetimgInfoList(
        ).searchImgData(plan_id)
        plus_35_93 = 0
        if turbineBackpressure.lh1_extraction_amount and turbineBackpressure.i_steam_exhaust_flow:
            plus_35_93 = turbineBackpressure.lh1_extraction_amount + turbineBackpressure.i_steam_exhaust_flow

        sewage_quantity = 0
        if boilerAuxiliaries.c_sewage_quantity:
            sewage_quantity = boilerAuxiliaries.c_sewage_quantity/1000
        multiply_f33_g19 = 0
        if turbineBackpressure.h_amount and furnaceCalculation.f_steam_flow_design:
            multiply_f33_g19 = turbineBackpressure.h_amount * furnaceCalculation.f_steam_flow_design
        return [
            # 汽轮机计算-1级高加!C32 hh1_water_enthalpy
            ImageInfo('0', (385, 1773), getstrcolm(turbineBackpressure.hh1_water_enthalpy), 35),
            # 汽轮机计算-1级高加F32 hh1_saturated_water_enthalpy
            ImageInfo('0', (391, 2577), getstrcolm(turbineBackpressure.hh1_saturated_water_enthalpy), 35),
            # 锅炉辅机F33 c_drum_aturatedwater_enthalpy
            ImageInfo('0', (393, 3077), getstrcolm(boilerAuxiliaries.c_drum_aturatedwater_enthalpy), 35),
            # --
            ImageInfo('0', (395, 2481), '--', 35),
            # 锅炉辅机F32 c_drum_pressure
            ImageInfo('0', (395, 2977), getstrcolm(boilerAuxiliaries.c_drum_pressure), 35),
            # 锅炉辅机G88 f_economizer_entry_pressure
            ImageInfo('0', (397, 1687), getstrcolm(boilerAuxiliaries.f_economizer_entry_pressure), 35),
            # 锅炉辅机F31/1000 c_sewage_quantity/1000
            ImageInfo('0', (607, 3069), getstrcolm(sewage_quantity), 35),
            # --
            ImageInfo('0', (619, 2981), '--', 35),
            # 汽轮机计算-1级高加B32 hh1_water_temperature
            ImageInfo('0', (679, 1683), getstrcolm(turbineBackpressure.hh1_water_temperature), 35),
            # 锅炉计算G19 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (681, 1779), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-1级高加E32 hh1_saturated_water_temperature
            ImageInfo('0', (685, 2477), getstrcolm(turbineBackpressure.hh1_saturated_water_temperature), 35),
            # 汽轮机计算-1级高加K32 hh1_extraction_amount
            ImageInfo('0', (691, 2579), getstrcolm(turbineBackpressure.hh1_extraction_amount), 35),
            # 锅炉计算G19 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (901, 951), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-1级高加C34 d_water_enthalpy
            ImageInfo('0', (1305, 4061), getstrcolm(turbineBackpressure.d_water_enthalpy), 35),
            # 汽轮机计算-1级高加G34 d_work_pressure
            ImageInfo('0', (1315, 3963), getstrcolm(turbineBackpressure.d_work_pressure), 35),
            # 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (1611, 4057), getstrcolm(furnaceCalculation.f_steam_flow_design), 35),
            # 汽轮机计算-1级高加B34 d_water_temperature
            ImageInfo('0', (1617, 3961), getstrcolm(turbineBackpressure.d_water_temperature), 35),
            # 汽轮机计算-1级高加J32 hh1_extraction_enthalpy
            ImageInfo('0', (1923, 1835), getstrcolm(turbineBackpressure.hh1_extraction_enthalpy), 35),
            # 汽轮机计算-1级高加I32 hh1_extraction_pressure
            ImageInfo('0', (1925, 1743), getstrcolm(turbineBackpressure.hh1_extraction_pressure), 35),
            # 锅炉计算G22 f_steam_enthalpy_design
            ImageInfo('0', (2163, 495), getstrcolm(furnaceCalculation.f_steam_enthalpy_design), 35),
            # 锅炉计算G20 f_steam_pressure_design
            ImageInfo('0', (2169, 401), getstrcolm(furnaceCalculation.f_steam_pressure_design), 35),
            # 汽轮机计算-1级高加F33 h_pressure
            ImageInfo('0', (2197, 4107), getstrcolm(turbineBackpressure.h_pressure), 35),
            # 汽轮机计算-1级高加H33 h_enthalpy
            ImageInfo('0', (2199, 4199), getstrcolm(turbineBackpressure.h_enthalpy), 35),
            # 汽轮机计算-1级高加K32 hh1_extraction_amount
            ImageInfo('0', (2213, 1833), getstrcolm(turbineBackpressure.hh1_extraction_amount), 35),
            ImageInfo('0', (2221, 1745), '--', 35),
            # 汽轮机计算-1级高加I34 d_extraction_pressure
            ImageInfo('0', (2347, 2353), getstrcolm(turbineBackpressure.d_extraction_pressure), 35),
            # 汽轮机计算-1级高加J34 d_extraction_enthalpy
            ImageInfo('0', (2347, 2453), getstrcolm(turbineBackpressure.d_extraction_enthalpy), 35),
            # 汽轮机计算-1级高加C35 lh1_water_enthalpy
            ImageInfo('0', (2377, 3229), getstrcolm(turbineBackpressure.lh1_water_enthalpy), 35),
            # 汽轮机计算-1级高加F26 e_steam_extraction_select
            ImageInfo('0', (2379, 497), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 锅炉计算G21 f_steam_temperature_design
            ImageInfo('0', (2383, 401), getstrcolm(furnaceCalculation.f_steam_temperature_design), 35),
            # --
            ImageInfo('0', (2383, 3139), '--', 35),
            # 汽轮机计算-1级高加J33 h_amount * 锅炉计算G19 f_steam_flow_design
            ImageInfo('0', (2557, 4197), getstrcolm(multiply_f33_g19), 35),
            # 汽轮机计算-1级高加D33 h_temperature
            ImageInfo('0', (2563, 4105), getstrcolm(turbineBackpressure.h_temperature), 35),
            # --
            ImageInfo('0', (2625, 2361), '--', 35),
            # 汽轮机计算-1级高加K34 d_extraction_amount
            ImageInfo('0', (2631, 2451), getstrcolm(turbineBackpressure.d_extraction_amount), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount + 汽轮机计算-1级高加F93 i_steam_exhaust_flow
            ImageInfo('0', (2663, 3229), getstrcolm(plus_35_93), 35),
            # 汽轮机计算-1级高加B35 lh1_water_temperature
            ImageInfo('0', (2671, 3137), getstrcolm(turbineBackpressure.lh1_water_temperature), 35),
            # 汽轮机计算-1级高加F24 e_steam_extraction_select
            ImageInfo('0', (3251, 1457), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 汽轮机计算-1级高加J35 lh1_extraction_enthalpy
            ImageInfo('0', (3251, 2525), getstrcolm(turbineBackpressure.lh1_extraction_enthalpy), 35),
            # 汽轮机计算-1级高加I35 lh1_extraction_pressure
            ImageInfo('0', (3253, 2427), getstrcolm(turbineBackpressure.lh1_extraction_pressure), 35),
            # 汽轮机计算-1级高加F35 lh1_saturated_water_enthalpy
            ImageInfo('0', (3253, 3231), getstrcolm(turbineBackpressure.lh1_saturated_water_enthalpy), 35),
            # --
            ImageInfo('0', (3261, 3141), '--', 35),
            # --
            ImageInfo('0', (3533, 2431), '--', 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount
            ImageInfo('0', (3535, 3233), getstrcolm(turbineBackpressure.lh1_extraction_amount), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount
            ImageInfo('0', (3537, 2525), getstrcolm(turbineBackpressure.lh1_extraction_amount), 35),
            # 汽轮机计算-1级高加E35 lh1_saturated_water_temperature
            ImageInfo('0', (3543, 3137), getstrcolm(turbineBackpressure.lh1_saturated_water_temperature), 35),
            # 汽轮机计算-1级高加F71 i_exhaust_point_enthalpy
            ImageInfo('0', (3559, 1207), getstrcolm(turbineBackpressure.i_exhaust_point_enthalpy), 35),
            # 汽轮机计算-1级高加F68 i_exhaust_point_pressure
            ImageInfo('0', (3561, 1117), getstrcolm(turbineBackpressure.i_exhaust_point_pressure), 35),
            # 汽轮机计算-1级高加F72 i_exhaust_point_flow
            ImageInfo('0', (3795, 1215), getstrcolm(turbineBackpressure.i_exhaust_point_flow), 35),
            # 汽轮机计算-1级高加F69 i_exhaust_point_temperature
            ImageInfo('0', (3799, 1119), getstrcolm(turbineBackpressure.i_exhaust_point_temperature), 35),
            # 汽轮机计算-1级高加C38 c_water_enthalpy
            ImageInfo('0', (4019, 3229), getstrcolm(turbineBackpressure.c_water_enthalpy), 35),
            ImageInfo('0', (4023, 3135), '--', 35),
            # 汽轮机计算-1级高加B38 c_water_temperature
            ImageInfo('0', (4301, 3139), getstrcolm(turbineBackpressure.c_water_temperature), 35),
            # 汽轮机计算-1级高加K35 lh1_extraction_amount + 汽轮机计算-1级高加F93 i_steam_exhaust_flow
            ImageInfo('0', (4305, 3229), getstrcolm(plus_35_93), 35),
            # 汽轮机计算-1级高加F86 i_steam_exhaust_pressure
            ImageInfo('0', (4533, 1867), getstrcolm(turbineBackpressure.i_steam_exhaust_pressure), 35),
            # 汽轮机计算-1级高加F89 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4533, 1961), getstrcolm(turbineBackpressure.i_steam_exhaust_enthalpy_actual), 35),
            # 汽轮机计算-1级高加F89 i_steam_exhaust_enthalpy_actual
            ImageInfo('0', (4773, 1961), getstrcolm(turbineBackpressure.i_steam_exhaust_enthalpy_actual), 35),
            # --
            ImageInfo('0', (4777, 1871), '--', 35),
            # --
            ImageInfo('0', (4859, 2577), '--', 35),
            # --
            ImageInfo('0', (4867, 2673), '--', 35),
            # 汽轮机计算-1级高加F24 e_steam_extraction_select
            ImageInfo('0', (4945, 1509), getstrcolm(turbineBackpressure.e_steam_extraction_select), 35),
            # 常量
            ImageInfo('0', (5077, 2577), '20/33', 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5081, 2661), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            # --
            ImageInfo('0', (5115, 1873), '--', 35),
            # --
            ImageInfo('0', (5115, 1975), '--', 35),
            # 循环水E9 v_total_circulating_water_select
            ImageInfo('0', (5327, 1967), getstrcolm(circulatingWater.v_total_circulating_water_select), 35),
            # --
            ImageInfo('0', (5333, 1871), '30/43', 35),
            # 循环水E14 v_evaporation_loss
            ImageInfo('0', (6089, 1433), getstrcolm(circulatingWater.v_evaporation_loss), 70),
            # 循环水K24 p_count
            ImageInfo('0', (6155, 1987), getstrcolm(circulatingWater.p_count), 60),
            # 循环水K26 p_select_s
            ImageInfo('0', (6497, 1987), getstrcolm(circulatingWater.p_select_s), 60),
            # 循环水E19 v_discharge_capacity
            ImageInfo('0', (6733, 3549), getstrcolm(circulatingWater.v_discharge_capacity), 70),
            # 循环水E16 v_partial_blow_loss
            ImageInfo('0', (6995, 1437), getstrcolm(circulatingWater.v_partial_blow_loss), 70),
            # 循环水E20 v_amount_of_makeup_water
            ImageInfo('0', (8602, 3399), getstrcolm(circulatingWater.v_amount_of_makeup_water), 70)
        ]

def getstrcolm(obj):
    return str(float('%.3f' % obj if obj is not None else 0.0))