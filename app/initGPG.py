# -*- coding: utf-8 -*-
# from models import CoalCHPConstant, CoalCHPComponent,\
#                    CoalCHPNeedsQuestionnaire, Role, User, Company

from app.gasPowerGeneration_models import GasPowerGenerationConstant, \
                                    GasPowerGenerationNeedsQuestionnaire
# 煤气发电 原则性热力系统锅炉部分
GPGBoilerOfPTS_data = [{
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "surplus_gas_bfg",
    "name": u"煤气流量_BFG",
    "symbol": u"Vg",
    "unit": u"Nm³/h",
    "calculate": u"由余热资源确定",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "surplus_gas_ldg",
    "name": u"煤气流量_LDG",
    "symbol": u"Vg",
    "unit": u"Nm³/h",
    "calculate": u"由余热资源确定",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "surplus_gas_cog",
    "name": u"煤气流量_COG",
    "symbol": u"Vg",
    "unit": u"Nm³/h",
    "calculate": u"由余热资源确定",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "bfg_gas_calorific_value",
    "name": u"BFG 煤气热值",
    "symbol": u"Qar.net.p",
    "unit": u"kJ/Nm³",
    "calculate": u"给定",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "ldg_gas_calorific_value",
    "name": u"LDG 煤气热值",
    "symbol": u"Qar.net.p",
    "unit": u"kJ/Nm³",
    "calculate": u"给定",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "cog_gas_calorific_value",
    "name": u"COG 煤气热值",
    "symbol": u"Qar.net.p",
    "unit": u"kJ/Nm³",
    "calculate": u"给定",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "boiler_efficiency",
    "name": u"锅炉热效率",
    "symbol": u"η",
    "unit": u"%",
    "calculate": u"设计参数",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "superheated_steam_outlet_pressure",
    "name": u"过热蒸汽出口压力",
    "symbol": u"P1",
    "unit": u"Mpa",
    "calculate": u"设计参数，绝压",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "superheated_steam_temperature",
    "name": u"过热蒸汽温度",
    "symbol": u"two",
    "unit": u"℃",
    "calculate": u"设计参数",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "superheated_steam_enthalpy",
    "name": u"过热蒸汽焓值",
    "symbol": u"Izo",
    "unit": u"kJ/kg",
    "calculate": u"查表",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "excess_air_coefficient",
    "name": u"过量空气系数",
    "symbol": u"α",
    "unit": u"",
    "calculate": u"",
    "remark": u"1.1~1.2"
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "air_temperature",
    "name": u"空气温度",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"设计参数",
    "remark": u"20"
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "air_enthalpy",
    "name": u"空气焓值",
    "symbol": u"hkq",
    "unit": u"kj/Nm³",
    "calculate": u"查表",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "air_need_for_combustion",
    "name": u"燃烧所需空气量",
    "symbol": u"Vn",
    "unit": u"Nm³/h",
    "calculate": u"0.209*Qar.net.p*Vg*α",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "boiler_feed_water_temperature",
    "name": u"锅炉给水温度",
    "symbol": u"tgs",
    "unit": u"℃",
    "calculate": u"设计参数",
    "remark": u"有高加为150℃或215℃，没高加为104℃"
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "feedwater_enthalpy",
    "name": u"给水焓值",
    "symbol": u"hgs",
    "unit": u"kJ/kg",
    "calculate": u"查表",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "rate_of_blowdown",
    "name": u"排污率",
    "symbol": u"φ",
    "unit": u"%",
    "calculate": u"设定",
    "remark": u"2%"
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "saturation_water_temperature",
    "name": u"饱和水温度",
    "symbol": u"tbh",
    "unit": u"℃",
    "calculate": u"查水蒸汽表",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "saturation_water_enthalpy",
    "name": u"饱和水焓值",
    "symbol": u"hbh",
    "unit": u"kj/Nm³",
    "calculate": u"查水蒸汽表",
    "remark": u""
}, {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "steam_output",
    "name": u"产汽量",
    "symbol": u"G1",
    "unit": u"t/h",
    "calculate": u"(Vn*hkq+Vg*Qar.net.p）*η/1000/((Izo-hgs)+φ(hbh-hgs))",
    "remark": u""
}]

# 煤气发电需求调查表
questionnaire_data = [{
    "module_name": "GPG_questionnaire",
    "name_eng": "surplus_gas_bfg",
    "name": u"富余的煤气流量_BFG",
    "symbol": u"",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "surplus_gas_ldg",
    "name": u"富余的煤气流量_LDG",
    "symbol": u"",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "surplus_gas_cog",
    "name": u"富余的煤气流量_COG",
    "symbol": u"",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "bfg_gas_temperature",
    "name": u"BFG 煤气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "ldg_gas_temperature",
    "name": u"LDG 煤气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "cog_gas_temperature",
    "name": u"COG 煤气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "bfg_gas_pressure",
    "name": u"BFG 煤气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "ldg_gas_pressure",
    "name": u"LDG 煤气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "cog_gas_pressure",
    "name": u"COG 煤气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "bfg_gas_calorific_value",
    "name": u"BFG 煤气热值",
    "symbol": u"",
    "unit": u"kJ/Nm³",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "ldg_gas_calorific_value",
    "name": u"LDG 煤气热值",
    "symbol": u"",
    "unit": u"kJ/Nm³",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "cog_gas_calorific_value",
    "name": u"COG 煤气热值",
    "symbol": u"",
    "unit": u"kJ/Nm³",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "provide_steam_amount",
    "name": u"对外供蒸汽量",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u"无则不需要填写"
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "provide_steam_pressure",
    "name": u"对外供蒸汽压",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u"无则不需要填写"
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "h2_content",
    "name": u"H2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "co_content",
    "name": u"CO",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "ch4_content",
    "name": u"CH4",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "c2h4_content",
    "name": u"C2H4",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "c3h8_content",
    "name": u"C3H8",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "c4h10_content",
    "name": u"C4H10",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "n2_content",
    "name": u"N2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "o2_content",
    "name": u"O2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "co2_content",
    "name": u"CO2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "h2s_content",
    "name": u"H2S",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "cmhn_content",
    "name": u"CmHn",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_temperature_h",
    "name": u"最高大气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_temperature_a",
    "name": u"平均大气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_temperature_l",
    "name": u"最低大气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_pressure_h",
    "name": u"最高大气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_pressure_a",
    "name": u"平均大气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_pressure_l",
    "name": u"最低大气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "relative_humidity_h",
    "name": u"最高相对湿度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "relative_humidity_a",
    "name": u"平均相对湿度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "relative_humidity_l",
    "name": u"最低相对湿度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "outside_wind_speed_h",
    "name": u"最高室外风速",
    "symbol": u"",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "outside_wind_speed_a",
    "name": u"平均室外风速",
    "symbol": u"",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "outside_wind_speed_l",
    "name": u"最低室外风速",
    "symbol": u"",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "seismic_fortification_intensity_h",
    "name": u"最高抗震设防烈度",
    "symbol": u"",
    "unit": u"度",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "seismic_fortification_intensity_a",
    "name": u"平均抗震设防烈度",
    "symbol": u"",
    "unit": u"度",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "seismic_fortification_intensity_l",
    "name": u"最低抗震设防烈度",
    "symbol": u"",
    "unit": u"度",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_pressure",
    "name": u"水压力",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_temperature",
    "name": u"水温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_ph",
    "name": u"PH值",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_suspended_matter",
    "name": u"悬浮物",
    "symbol": u"",
    "unit": u"mg/L",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_cl",
    "name": u"氯离子",
    "symbol": u"",
    "unit": u"mg/L",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "nitrogen_purity",
    "name": u"氮气纯度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "nitrogen_pressure",
    "name": u"氮气压力范围",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "nitrogen_temperature",
    "name": u"氮气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "compressed_air_pressure",
    "name": u"压缩空气压力范围",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "compressed_air_temperature",
    "name": u"压缩空气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "grid_voltage",
    "name": u"并网电压",
    "symbol": u"",
    "unit": u"kV",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "max_short_circuit_capacity",
    "name": u"最大短路容量",
    "symbol": u"",
    "unit": u"kVA",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "factory_location_elevation",
    "name": u"拟建厂区坐标点和高程的地形图",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u"CAD版，含风玫瑰"
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "dielectric_position_height_caliber_route",
    "name": u"能源介质接点位置、标高、管径、路由",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_quality_analysis_report",
    "name": u"全水质分析报告",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u"尽可能提供"
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "cooling_tower",
    "name": u"冷却方式及冷却塔形式",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_questionnaire",
    "name_eng": "project_approval_eia",
    "name": u"项目立项及环评手续",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
}]


class AddGPG():
    # 初始化数据
    @staticmethod
    def init_data():
        data = [questionnaire_data, GPGBoilerOfPTS_data]
        for index in range(len(data)):
            AddGPG.insert_constant(data[index])

    # 表中插入常量数据
    @staticmethod
    def insert_constant(data):
        module_name = data[0]["module_name"]
        for index in range(len(data)):
            name_eng = data[index]["name_eng"]
            name = data[index]["name"]
            symbol = data[index]["symbol"]
            unit = data[index]["unit"]
            calculate = data[index]["calculate"]
            remark = data[index]["remark"]
            gasPowerGenerationConstant = GasPowerGenerationConstant.create_gasPowerGenerationConstant(
                module_name, name_eng, name, symbol, unit, calculate, remark)
            GasPowerGenerationConstant.insert_gasPowerGenerationConstant(gasPowerGenerationConstant)
