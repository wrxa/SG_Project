# -*- coding: utf-8 -*-
from models import BiomassCHPconstant, Role, User, Company, BiomassCHPBeltWidth

# 生物质热电联产需求调查表
questionnaire_data=[
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_carbon",
        "name": u"收到基碳含量",
        "symbol": u"Car",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_hydrogen",
        "name": u"收到基氢含量",
        "symbol": u"Har",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_oxygen",
        "name": u"收到基氧含量",
        "symbol": u"Oar",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_nitrogen",
        "name": u"收到基氮含量",
        "symbol": u"Nar",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_sulfur",
        "name": u"收到基硫含量",
        "symbol": u"Sar",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_total_moisture",
        "name": u"收到基全水份",
        "symbol": u"Mar",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_grey",
        "name": u"收到基灰份",
        "symbol": u"Var",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_daf",
        "name": u"干燥无灰基挥发分",
        "symbol": u"Aar",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_grindability",
        "name": u"固定碳",
        "symbol": u"FCar",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_quantity",
        "name": u"收到基低位发热量",
        "symbol": u"Qnet，ar，q",
        "unit": u"MJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_deformation",
        "name": u"变形温度",
        "symbol": u"DT",
        "unit": u"℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_softening",
        "name": u"软化温度",
        "symbol": u"ST",
        "unit": u"℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_hemispherical",
        "name": u"半球温度",
        "symbol": u"HT",
        "unit": u"℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_flow",
        "name": u"流动温度",
        "symbol": u"FT",
        "unit": u"℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_fuel_density",
        "name": u"燃料堆积密度",
        "symbol": u"ρrl",
        "unit": u"t/m3",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "s_ash_density",
        "name": u"飞灰堆积密度",
        "symbol": u"ρfh",
        "unit": u"t/m3",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "l_altitude",
        "name": u"当地平均海拔",
        "symbol": u"A",
        "unit": u"m",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "l_pressure",
        "name": u"历年平均气压",
        "symbol": u"Pb",
        "unit": u"kPa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "l_temperature",
        "name": u"历年平均气温",
        "symbol": u"T",
        "unit": u"℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "l_max_temperature",
        "name": u"历年极端最高气温",
        "symbol": u"Tmax",
        "unit": u"℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "l_min_temperature",
        "name": u"历年极端最低气温",
        "symbol": u"Tmin",
        "unit": u"℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "l_humidity",
        "name": u"历年平均相对湿度",
        "symbol": u"φ",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_pressure_grade",
        "name": u"蒸汽压力等级",
        "symbol": u"P",
        "unit": u"MPa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_temperature_grade",
        "name": u"蒸汽温度等级",
        "symbol": u"T",
        "unit": u"℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_steam_time",
        "name": u"用汽时段",
        "symbol": u"--",
        "unit": u"--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_recent_steam_flow_range",
        "name": u"近期蒸汽流量范围",
        "symbol": u"Qjq",
        "unit": u"t/h",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_forward_steam_flow_range",
        "name": u"远期蒸汽流量范围",
        "symbol": u"Qyq",
        "unit": u"t/h",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_condensate_water_iron",
        "name": u"凝结水含铁量",
        "symbol": u"CFe",
        "unit": u"mg/m3",
        "calculate": "",
        "remark": "考虑回水是否受主工艺污染",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_condensate_water_recovery_rate",
        "name": u"凝结水回收率",
        "symbol": u"Φ",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_hhl_heating_occasions_type",
        "name": u"采暖场合类型",
        "symbol": u"--",
        "unit": u"--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_year_heating_days",
        "name": u"全年采暖天数",
        "symbol": u"--",
        "unit": u"d/a",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_recent_heating_area",
        "name": u"近期采暖面积",
        "symbol": u"--",
        "unit": u"万m3",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "t_forward_heating_area",
        "name": u"远期采暖面积",
        "symbol": u"--",
        "unit": u"万m3",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "o_planning_area",
        "name": u"规划占地面积",
        "symbol": u"--",
        "unit": u"亩",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "o_planned_expansion_capacity",
        "name": u"规划扩建容量",
        "symbol": u"--",
        "unit": u"MW",
        "calculate": "",
        "remark": "是否扩建",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "o_local_water_condition",
        "name": u"当地水源条件",
        "symbol": u"--",
        "unit": u"--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "o_higher_voltage_level",
        "name": u"上级变电压等级",
        "symbol": u"--",
        "unit": u"kV",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "o_plant_distance",
        "name": u"厂区距上级变距离",
        "symbol": u"--",
        "unit": u"km",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "o_flue_gas_sox_limits",
        "name": u"烟气SOX排放限值",
        "symbol": u"--",
        "unit": u"mg/Nm3",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "o_flue_gas_nox_limits",
        "name": u"烟气NOX排放限值",
        "symbol": u"--",
        "unit": u"mg/Nm3",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "biomassCHP_questionnaire",
        "name_eng": "o_flue_gas_dust_limits",
        "name": u"烟气烟尘排放限值",
        "symbol": u"--",
        "unit": u"mg/Nm3",
        "calculate": "",
        "remark": "",
        "default_value": ""
    }
]

# 锅炉计算sheet
boilerCalculation_data=[
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_carbon_content_received",
        "name": u"收到基碳含量",
        "symbol": u"Car",
        "unit": u"%",
        "calculate": "见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_hydrogen_content_received",
        "name": u"收到基氢含量",
        "symbol": u"Har",
        "unit": u"%",
        "calculate": "见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_oxygen_content_received",
        "name": u"收到基氧含量",
        "symbol": u"Oar",
        "unit": u"%",
        "calculate": "见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_nitrogen_content_received",
        "name": u"收到基氮含量",
        "symbol": u"Nar",
        "unit": u"%",
        "calculate": "见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_sulfur_content_received",
        "name": u"收到基硫含量",
        "symbol": u"Sar",
        "unit": u"%",
        "calculate": "见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_ash_content_received",
        "name": u"收到基灰分",
        "symbol": u"Aar",
        "unit": u"%",
        "calculate": "见需求调研表；一般＜10",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_water_content_received",
        "name": u"收到基水分",
        "symbol": u"Mar",
        "unit": u"%",
        "calculate": "见需求调研表；设计燃料入炉条件≤30；校核燃料入炉条件≤40",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_sum",
        "name": u"总和",
        "symbol": u"100",
        "unit": u"%",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_base_volatile_obtained",
        "name": u"收到基挥发分",
        "symbol": u"Var",
        "unit": u"%",
        "calculate": "见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_daf",
        "name": u"干燥无灰基挥发分",
        "symbol": u"Vdaf",
        "unit": u"%",
        "calculate": "一般＞60",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_base_heat_received_user",
        "name": u"收到基低位发热量（用户提供）",
        "symbol": u"Qnet.Ar",
        "unit": u"Kj/kg",
        "calculate": "见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_base_heat_received_calculation",
        "name": u"收到基低位发热量（计算得到）",
        "symbol": u"Qnet.Ar",
        "unit": u"Kcal/kg",
        "calculate": "KJ=4.1868*Kcal",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_low_calorific_value_estimation",
        "name": u"低位发热量估算",
        "symbol": u"Qnet.Ar",
        "unit": u"Kj/kg",
        "calculate": "Qnet.ar=339xCar+1030*Har-25xMar-109(Oar-Sar)",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "c_high_calorific_value_estimation",
        "name": u"高位发热量估算",
        "symbol": u"Qar.gt",
        "unit": u"Kj/kg",
        "calculate": "Qnet.gt=339xCar+1256*Har-109(Oar-Sar)",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_steam_flow",
        "name": u"过热蒸汽额定流量",
        "symbol": u"Dgr",
        "unit": u"t/h",
        "calculate": u"推荐值为35t/h、48t/h、60t/h、75t/h、130t/h、220t/h",
        "remark": "",
        "default_value": "130",
        
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_steam_pressure",
        "name": u"过热蒸汽出口压力",
        "symbol": u"Pgr",
        "unit": u"Mpa(g)",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_steam_temperature",
        "name": u"过热蒸汽温度",
        "symbol": u"Tgr",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_steam_enthalpy",
        "name": u"过热蒸汽焓值",
        "symbol": u"Igr",
        "unit": u"Kj/kg",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_boiler_pressure",
        "name": u"锅筒压力",
        "symbol": u"Dgr",
        "unit": u"Mpa(g)",
        "calculate": u"过热蒸汽压力*1.1",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_saturated_water_enthalpy",
        "name": u"汽包内饱和水焓值",
        "symbol": u"Ibs",
        "unit": u"Kj/kg",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_water_temperature",
        "name": u"给水温度",
        "symbol": u"Tgs",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_water_enthalpy",
        "name": u"给水焓值",
        "symbol": u"Igs",
        "unit": u"Kj/kg",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_boiler_efficiency",
        "name": u"锅炉效率",
        "symbol": u"ηg",
        "unit": u"%",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_unburned_loss",
        "name": u"机械未燃烧损失",
        "symbol": u"q4",
        "unit": u"%",
        "calculate": u"一般为0.5~2%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_blowdown_rate",
        "name": u"锅炉排污率",
        "symbol": u"ηpw",
        "unit": u"%",
        "calculate": u"",
        "remark": "",
        "default_value": "0.02"
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_boiler_consumption",
        "name": u"锅炉燃料消耗量",
        "symbol": u"Bg",
        "unit": u"kg/h",
        "calculate": u"Dgr*1000*/ηg（(Igr-Igs)+ηpw(ibs-igs)）/Qnet.ar",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "f_calculation _consumption",
        "name": u"计算燃料消耗量",
        "symbol": u"Bj",
        "unit": u"kg/h",
        "calculate": u"Bg*（1-q4）",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_total",
        "name": u"灰渣总量",
        "symbol": u"Gzhb",
        "unit": u"kg/h",
        "calculate": u"Bg(Aar/100+Qnet,ar*q4/3387000)   P209",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_boiler_total",
        "name": u"炉内喷钙灰渣总量",
        "symbol": u"G'zhb",
        "unit": u"kg/h",
        "calculate": u"生物质热电项目脱硫系统一般采用炉内喷钙工艺",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_ash_share",
        "name": u"飞灰份额",
        "symbol": u"k1",
        "unit": u"--",
        "calculate": u"CFB锅炉和ICFB锅炉取0.9；联合炉排炉和水冷振动炉排炉取0.6",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_dust_share",
        "name": u"底渣份额",
        "symbol": u"k2",
        "unit": u"--",
        "calculate": u"1-k1",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_ash_total",
        "name": u"灰量",
        "symbol": u"Gh",
        "unit": u"t/h",
        "calculate": u"Gznb*k1",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_dust_total",
        "name": u"渣量",
        "symbol": u"Gz",
        "unit": u"t/h",
        "calculate": u"Gznb*k2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_air_volumn",
        "name": u"理论干空气量",
        "symbol": u"Vo",
        "unit": u"Nm3/kg",
        "calculate": u"0.0889（Car+0.375St,ar)+0.265Har-0.0333Oar",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_hot_temperature",
        "name": u"最热月平均气温",
        "symbol": u"Trp",
        "unit": u"℃",
        "calculate": u"见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_humidity",
        "name": u"多年平均相对湿度",
        "symbol": u"φ",
        "unit": u"%",
        "calculate": u"见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_pressure",
        "name": u"多年平均气压",
        "symbol": u"Pb",
        "unit": u"kPa",
        "calculate": u"见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_temperature",
        "name": u"多年平均气温",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_saturation_pressure ",
        "name": u"多年平均气温下的饱和压力",
        "symbol": u"Ps",
        "unit": u"kPa",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_steam_perssure",
        "name": u"水蒸气分压力",
        "symbol": u"Pv",
        "unit": u"kPa",
        "calculate": u"φ*Ps/100",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_air_humidity",
        "name": u"空气的绝对湿度（含湿量）",
        "symbol": u"d",
        "unit": u"g水/kg空气",
        "calculate": u"d=622*Pv/(Pb-Pv)，如无气象资料，可取d=10（经验值）",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_standard_air_humidity",
        "name": u"标况下湿空气密度",
        "symbol": u"ρao",
        "unit": u"kg/Nm3空气",
        "calculate": u"(1+0.001d)/(1/1.293+0.001d/0.804)",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_wet_air_volumn",
        "name": u"理论湿空气量",
        "symbol": u"Vo'",
        "unit": u"Nm3/kg燃料",
        "calculate": u"(1+0.0016d)Vo",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "s_nitrogen_volume ",
        "name": u"理论氮气容积",
        "symbol": u"V1N2",
        "unit": u"Nm3/kg",
        "calculate": u"0.79Vo+0.008*Nar",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "s_dioxide_volume",
        "name": u"理论二氧化物容积",
        "symbol": u"VoRO2",
        "unit": u"Nm3/kg",
        "calculate": u"1.866(Car+0.375Sar)/100",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "s_steam_volume",
        "name": u"理论水蒸汽容积",
        "symbol": u"VoH2O",
        "unit": u"Nm3/kg",
        "calculate": u"0.111Har+0.0124Mar+1.293*d*Vo/0.804/1000",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "s_smoke_volume",
        "name": u"理论烟气容积",
        "symbol": u"Vyo",
        "unit": u"Nm3/kg",
        "calculate": u"V1N2+VoRO2+VoH2O",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "s_1kg_weight",
        "name": u"1kg燃料生成理论湿烟气的重量",
        "symbol": u"Gyo",
        "unit": u"kg/kg燃料",
        "calculate": u"1-Aar/100+(1+d/1000)*1.293*α*Vo",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "s_wet_smoke_density",
        "name": u"标况下理论湿烟气密度",
        "symbol": u"ρyo",
        "unit": u"kg/Nm3",
        "calculate": u"Gyo/Vyo",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_boiler_air",
        "name": u"炉膛出口过剩空气系数",
        "symbol": u"αl",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_wind",
        "name": u"旋风分离器漏风系数",
        "symbol": u"ΔαfL",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_wind_air",
        "name": u"旋风分离器出口过剩空气系数",
        "symbol": u"αfL",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_high",
        "name": u"高过漏风系数",
        "symbol": u"Δαgr",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_hign_air",
        "name": u"高过出口过剩空气系数",
        "symbol": u"αgr",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_low",
        "name": u"低过漏风系数",
        "symbol": u"Δαdr",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_low_air",
        "name": u"低过出口过剩空气系数",
        "symbol": u"αdr",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_fule",
        "name": u"省燃料器漏风系数",
        "symbol": u"Δαsm",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_fule_air",
        "name": u"省燃料器出口过剩空气系数",
        "symbol": u"αsm",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_heater",
        "name": u"空预器漏风系数",
        "symbol": u"Δαky",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_heater_air",
        "name": u"空预器出口过剩空气系数",
        "symbol": u"αky",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_plus_air",
        "name": u"空予器至除尘器烟道漏风系数",
        "symbol": u"Δαcj",
        "unit": u"--",
        "calculate": u"L(烟道长度)*0.001",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_dust_exit",
        "name": u"除尘器进口过剩空气系数",
        "symbol": u"αcj",
        "unit": u"--",
        "calculate": u"αky+Δαcj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_dust",
        "name": u"除尘器漏风系数",
        "symbol": u"Δαcc",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_dust_entry",
        "name": u"除尘器出口过剩空气系数",
        "symbol": u"αcc",
        "unit": u"--",
        "calculate": u"αcj+Δαcc",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_plus_dust",
        "name": u"除尘器出口至引风机烟道漏风系数",
        "symbol": u"Δαyd2",
        "unit": u"--",
        "calculate": u"L(烟道长度)*0.001",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_fans_air",
        "name": u"引风机入口过剩空气系数",
        "symbol": u"αxf",
        "unit": u"--",
        "calculate": u"αcc+Δαyd2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_1kg_volume",
        "name": u"1Kg燃料产生的空预器出口湿烟气容积",
        "symbol": u"Vy",
        "unit": u"Nm3/kg",
        "calculate": u"Vyo+(αky-1)Vo+0.0161(αky-1)Vo",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_1kg_quality",
        "name": u"1Kg燃料产生的空预器出口湿烟气质量",
        "symbol": u"Gy",
        "unit": u"kg/kg",
        "calculate": u"1-Aar/100+(1+d/1000)*1.293*αky*Vo",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_heater_type",
        "name": u"空预器",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_heater_first_entry",
        "name": u"空预器一次风进口温度",
        "symbol": u"T'ky.p",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_heater_second_entry",
        "name": u"空预器二次风进口温度",
        "symbol": u"T'ky.s",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_heater_first_exit",
        "name": u"空预器一次风出口温度",
        "symbol": u"T'ky.p",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_heater_second_exit",
        "name": u"空预器二次风出口温度",
        "symbol": u"T'ky.s",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "p_smoke_temperature",
        "name": u"锅炉排烟温度",
        "symbol": u"T'y",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_theory_air_quality",
        "name": u"理论空气量（体积,湿）",
        "symbol": u"Vo'",
        "unit": u"Nm3/kg燃料",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_boiler_air",
        "name": u"炉膛出口过剩空气系数",
        "symbol": u"αl",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_actual_air",
        "name": u"实际空气量（体积,湿）",
        "symbol": u"Voks",
        "unit": u"Nm3/kg",
        "calculate": u"αl*Vo'",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_calculation_consumption",
        "name": u"计算燃料消耗量",
        "symbol": u"Bj",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_actual_air_total",
        "name": u"实际空气总量（体积，湿）",
        "symbol": u"Vok",
        "unit": u"Nm3/h",
        "calculate": u"Bj*Voks",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_wind_volume",
        "name": u"一次风份额",
        "symbol": u"β1",
        "unit": u"%",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_cwind_temperature_calculation",
        "name": u"冷风温度（计算温度）",
        "symbol": u"T'ky.p",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_local_pressure",
        "name": u"当地年平均气压",
        "symbol": u"Pb",
        "unit": u"kPa",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_cwind_standard",
        "name": u"冷一次风量（湿-标准态）",
        "symbol": u"VNLf 1",
        "unit": u"Nm3/h",
        "calculate": u"β1*Vok",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_cwind_actual",
        "name": u"冷一次风量（湿-实态）",
        "symbol": u"VLf 1",
        "unit": u"m3/h",
        "calculate": u"VNLf 1*(273+T ' ky.p)/273*101.325/Pb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_standard_air_density",
        "name": u"标况下湿空气密度",
        "symbol": u"ρao",
        "unit": u"kg/Nm3",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_cwind_flow",
        "name": u"冷一次风量（质量流量）",
        "symbol": u"GLf 1",
        "unit": u"kg/h",
        "calculate": u"ρao*VNLf 1",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_cwind_density",
        "name": u"冷一次风湿空气密度（湿-实态）",
        "symbol": u"ρa1",
        "unit": u"kg/m3",
        "calculate": u"GLf 1/VLf 1",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_check",
        "name": u"校核",
        "symbol": u"ρa1",
        "unit": u"kg/m3",
        "calculate": u"ρao*273/（273+T'ky.p）*Pb/101.325（校核）",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_hwind_temperatue",
        "name": u"热一次风温度",
        "symbol": u"T'ky.p",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_hwind_flow",
        "name": u"热一次风量（湿-实态）",
        "symbol": u"VRf 1",
        "unit": u"m3/h",
        "calculate": u"VNLf 1*(273+T'ky.s)/273*101.325/Pb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_first_wet_air_density",
        "name": u"湿空气密度（湿-实态）",
        "symbol": u"ρ'a1",
        "unit": u"kg/m3",
        "calculate": u"GLf 1/VRf 1",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_wind_volume",
        "name": u"二次风份额",
        "symbol": u"β2",
        "unit": u"%",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_cwind_temperature",
        "name": u"冷风温度",
        "symbol": u"T'ky.s",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_cwind_standard",
        "name": u"冷二次风量（湿-标准态）",
        "symbol": u"VNLf 2",
        "unit": u"Nm3/h",
        "calculate": u"β2*Vok",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_cwind_actual",
        "name": u"冷二次风量（湿-实态）",
        "symbol": u"VLf 2",
        "unit": u"m3/h",
        "calculate": u"VNLf 2*(273+T'ky.s)/273*101.325/Pb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_standard_air_density",
        "name": u"标况下湿空气密度",
        "symbol": u"ρao",
        "unit": u"kg/Nm3",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_cwind_flow",
        "name": u"冷二次风量（质量流量）",
        "symbol": u"GLf 2",
        "unit": u"kg/h",
        "calculate": u"ρao*VNLf2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_cwind_density",
        "name": u"冷二次风湿空气密度（湿-实态）",
        "symbol": u"ρa2",
        "unit": u"kg/m3",
        "calculate": u"GLf2/VLf2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_hwind_temperatue",
        "name": u"热二次风温度",
        "symbol": u"T'ky.s",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_hwind_flow",
        "name": u"热二次风量（湿-实态）",
        "symbol": u"VRf 2",
        "unit": u"m3/h",
        "calculate": u"VNLf 2*(273+T'ky.s)/273*101.325/Pb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "a_second_wet_air_density",
        "name": u"湿空气密度（湿-实态）",
        "symbol": u"ρ'a2",
        "unit": u"kg/m3",
        "calculate": u"GLf 2/VRf 2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "h_1kg_volume",
        "name": u"标况下空预器出口1Kg燃料湿烟气容积",
        "symbol": u"Vy",
        "unit": u"Nm3/kg",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "h_1kg_quality",
        "name": u"空预器出口1Kg燃料产生的湿烟气质量",
        "symbol": u"Gy",
        "unit": u"kg/kg",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "h_calculation_consumption",
        "name": u"计算燃料消耗量",
        "symbol": u"Bj",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "h_standard_smoke_flow",
        "name": u"标况下空预器出口烟气容积流量",
        "symbol": u"VNyk",
        "unit": u"Nm3/h",
        "calculate": u"Vy*Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "h_smoke_flow",
        "name": u"空预器出口烟气质量流量",
        "symbol": u"Gyk",
        "unit": u"kg/h",
        "calculate": u"Gy*Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "h_smoke_temperature",
        "name": u"锅炉空预器出口排烟温度",
        "symbol": u"T'y",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "h_smoke_volume",
        "name": u"空预器出口烟气容积量(实态）",
        "symbol": u"Vyk",
        "unit": u"m3/h",
        "calculate": u"VNyk*(273+T'y)/273*101.325/Pb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "h_smoke_density",
        "name": u"烟气密度（实态）",
        "symbol": u"ρyk",
        "unit": u"kg/m3",
        "calculate": u"Gyk/Vyk",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_exit_air",
        "name": u"空预器出口过剩空气系数",
        "symbol": u"αky",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_wind_parameter",
        "name": u"空预器至除尘器烟道漏风系数",
        "symbol": u"Δαcj",
        "unit": u"--",
        "calculate": u"L(烟道长度)*0.001",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_entry_air",
        "name": u"除尘器进口过剩空气系数",
        "symbol": u"αcj",
        "unit": u"--",
        "calculate": u"αky+Δαcj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_cold_air_temperature",
        "name": u"冷空气温度",
        "symbol": u"Tlk",
        "unit": u"℃",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_entry_somke_temperature",
        "name": u"除尘器进口处烟气温度",
        "symbol": u"Tcj",
        "unit": u"℃",
        "calculate": u"(αkyT'y+△αcj*Tlk)/(αky+△αcj)",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_standard_1kg_volume",
        "name": u"标况下除尘器进口处1kg燃料湿烟气容积",
        "symbol": u"V'ycj",
        "unit": u"Nm3/kg",
        "calculate": u"Vy+△αcj*VO'+0.0161*VO'",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_entry_1kg_quality",
        "name": u"除尘器进口处1kg燃料湿烟气质量",
        "symbol": u"G'ycj",
        "unit": u"kg/kg",
        "calculate": u"1-Aar/100+1.293*(1+d/1000)*αcj*Vo",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_standard_smoke_flow",
        "name": u"标况下除尘器进口烟气容积流量",
        "symbol": u"VNycj",
        "unit": u"Nm3/h",
        "calculate": u"V'ycj*Bj ",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_entry_somke_flow",
        "name": u"除尘器进口处烟气质量流量",
        "symbol": u"Gycj",
        "unit": u"kg/h",
        "calculate": u"G'ycj*Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "d_entry_smoke_actual_flow",
        "name": u"除尘器进口处烟气容积流量(实态）",
        "symbol": u"Vycj",
        "unit": u"m3/h",
        "calculate": u"VNycj*(273+Tcj)/273*101.325/Pb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_wind_parameter",
        "name": u"除尘器漏风系数",
        "symbol": u"Δαcc",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_air_parameter",
        "name": u"除尘器出口过剩空气系数",
        "symbol": u"αcc",
        "unit": u"--",
        "calculate": u"αcj+△αcc",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_smoke_temperature",
        "name": u"除尘器出口烟气温度",
        "symbol": u"Tcc",
        "unit": u"℃",
        "calculate": u"湿法脱硫，给定",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_standard_1kg_volume",
        "name": u"标况下除尘器出口处1kg燃料湿烟气容积",
        "symbol": u"V'ycc",
        "unit": u"Nm3/kg",
        "calculate": u"V'ycj+△αcc*VO'+0.0161*△αcc*VO'",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_1kg_quality",
        "name": u"除尘器出口处1kg燃料湿烟气质量",
        "symbol": u"G'ycc",
        "unit": u"kg/kg",
        "calculate": u"1-Aar/100+1.293*(1+d/1000)*αcc*Vo",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_standard_smoke_flow",
        "name": u"标况下除尘器出口湿烟气容积流量",
        "symbol": u"VNycc",
        "unit": u"Nm3/h",
        "calculate": u"V'ycc*Bj ",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_smoke_flow",
        "name": u"除尘器出口处湿烟气质量流量",
        "symbol": u"Gycc",
        "unit": u"kg/h",
        "calculate": u"G'ycc*Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_smoke_actual_flow",
        "name": u"除尘器出口处湿烟气容积流量(实态）",
        "symbol": u"Vycc",
        "unit": u"m3/h",
        "calculate": u"VNycc*(273+Tcc)/273*101.325/Pb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "e_smoke_actual_density",
        "name": u"烟气密度（实态）",
        "symbol": u"ρycc",
        "unit": u"kg/m3",
        "calculate": u"Gycc/Vycc",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_wind_parameter",
        "name": u"除尘器出口至引风机烟道漏风系数",
        "symbol": u"Δαxj",
        "unit": u"--",
        "calculate": u"L(烟道长度)*0.001",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_air_parameter",
        "name": u"引风机入口过剩空气系数",
        "symbol": u"αxf",
        "unit": u"--",
        "calculate": u"αcc+Δαxj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_smoke_temperature",
        "name": u"引风机入口烟气温度",
        "symbol": u"Txf",
        "unit": u"℃",
        "calculate": u"(αcc*Tcc+△αxj*Tlk)/(αcc+△αxj)",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_standard_1kg_volume",
        "name": u"标况下引风机进口处1kg燃料湿烟气容积",
        "symbol": u"V'xf",
        "unit": u"Nm3/kg",
        "calculate": u"V'ycc+△αxj*Vo'+0.0161*△αxj*Vo'",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_1kg_quality",
        "name": u"引风机进口处1kg燃料湿烟气质量",
        "symbol": u"G'xf",
        "unit": u"kg/kg",
        "calculate": u"1-Aar/100+1.293*(1+d/1000)*αxf*Vo",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_standard_smoke_flow1",
        "name": u"标况下引风机进口湿烟气容积流量",
        "symbol": u"VNxf",
        "unit": u"Nm3/h",
        "calculate": u"V'xf*Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_standard_smoke_flow2",
        "name": u"标况下引风机进口湿烟气容积流量",
        "symbol": u"",
        "unit": u"Nm3/s",
        "calculate": u"V'xf*Bj/3600",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_smoke_flow",
        "name": u"引风机进口处湿烟气质量流量",
        "symbol": u"Gxf",
        "unit": u"kg/h",
        "calculate": u"G'xf*Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_smoke_actual_flow1",
        "name": u"引风机进口处湿烟气容积流量(实态）",
        "symbol": u"Vxf",
        "unit": u"m3/h",
        "calculate": u"VNxf*(273+Txf)/273*101.325/Pb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_smoke_actual_flow2",
        "name": u"引风机进口处湿烟气容积流量(实态）",
        "symbol": u"Vxfc",
        "unit": u"m3/s",
        "calculate": u"Vxf/3600",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_smoke_actual_density",
        "name": u"烟气密度（实态）",
        "symbol": u"ρyxf",
        "unit": u"kg/m3",
        "calculate": u"Gyxf/Vyxf",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "i_wet_smoke_actual_density",
        "name": u"引风机处计算湿烟气密度（标况）",
        "symbol": u"ρyo",
        "unit": u"kg/Nm3",
        "calculate": u"Gxf/VNxf",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_oxygen_vol",
        "name": u"烟气中的氧量",
        "symbol": u"VO2'",
        "unit": u"Nm3/kg燃料",
        "calculate": u"0.21(axf-1)V0",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_theoretica_vol",
        "name": u"理论干烟气容积",
        "symbol": u"Vgyo",
        "unit": u"Nm3/kg燃料",
        "calculate": u"VoN2+VoRO2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_theoretica_flow",
        "name": u"理论干空气量",
        "symbol": u"Vo",
        "unit": u"Nm3/kg燃料",
        "calculate": u"0.0889（Car+0.375St,ar)+0.265Har-0.0333Oar",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_calculation_consumption",
        "name": u"计算燃料消耗量",
        "symbol": u"Bj",
        "unit": u"kg/h",
        "calculate": u"燃料灰渣量计算表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_air_parameter",
        "name": u"引风机入口过剩空气系数",
        "symbol": u"αxf",
        "unit": u"--",
        "calculate": u"αcc+Δαxj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_standard_1kg_volume",
        "name": u"1Kg燃料产生的引风机进口干烟气容积",
        "symbol": u"V'gy",
        "unit": u"Nm3/kg燃料",
        "calculate": u"Vgyo+(axf-1)V0",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_smoke_flow",
        "name": u"引风机进口干烟气容积流量",
        "symbol": u"Vgy",
        "unit": u"Nm3/h",
        "calculate": u"V'gy*Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_dryGas_oxygen_vol",
        "name": u"干烟气中含氧量",
        "symbol": u"ngo2",
        "unit": u"%",
        "calculate": u"VO2'/Vgy'",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_calculation",
        "name_eng": "go_total_combustion_product_vol",
        "name": u"总燃烧产物6%O2干体积",
        "symbol": u"Vgy-O2",
        "unit": u"Nm3/h",
        "calculate": u"Vgy*(21-ngo2')/(21-6)",
        "remark": "",
        "default_value": ""
    }
]

# 生物质热电皮带宽度表
beltwidth_data = [(
    '500', '340'
), (
    '650', '365'
), (
    '800', '380'
), (
    '1000', '400'
), (
    '1200', '410'
), (
    '1400', '415'
), (
    '1600', '420'
), (
    '1800', '425'
), (
    '2000', '430'
)]



# 燃料存储及输送系统sheet
fuelST_data=[
    {
        "module_name": "fuel_ST",
        "name_eng": "b_rated_fuel_consumption",
        "name": u"锅炉额定燃料耗量",
        "symbol": u"Bj",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_saily_use_hours",
        "name": u"锅炉日利用小时数",
        "symbol": u"Hd",
        "unit": u"h",
        "calculate": u"推荐值为22h或24h",
        "remark": "",
        "default_value": "22"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_daily_consumption",
        "name": u"日耗量",
        "symbol": u"Qd",
        "unit": u"t/d",
        "calculate": u"Bj*Hd",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_annual_use_hours",
        "name": u"锅炉年利用小时数",
        "symbol": u"Ha",
        "unit": u"h",
        "calculate": u"6000~8000",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_year_consumption",
        "name": u"年耗量",
        "symbol": u"Qa",
        "unit": u"万t/a",
        "calculate": u"Bj*Ha",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_unbalance_coefficient",
        "name": u"不均衡系数",
        "symbol": u"Kb",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": "1.2"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_daily_fuel_consumption",
        "name": u"日进厂燃料量",
        "symbol": u"Md",
        "unit": u"t/d",
        "calculate": u"Kb*Qa*Hd/Ha",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_carrying_vehicle_load",
        "name": u"运载车辆载重",
        "symbol": u"mc",
        "unit": u"t/车",
        "calculate": u"运输车辆利用社会运力",
        "remark": "",
        "default_value": "10"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_daily_vehicle",
        "name": u"日进厂车辆",
        "symbol": u"nc",
        "unit": u"辆",
        "calculate": u"Md/mc",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_fuel_reserve_days",
        "name": u"燃料的储备日数",
        "symbol": u"Tdc",
        "unit": u"d",
        "calculate": u"推荐值为7~8",
        "remark": "目前，国内生物质电厂的燃料一般以各收购点厂外破碎为主，厂内一般不设破碎设备。电子汽车衡配备的数量一般为2台，1台计量进厂重车，1台计量出厂空车，吨位多在50~100t。厂内原料堆场的主要作用是对入厂燃料进行暂存及翻晒，按布置形式可分为露天堆场和半露天堆场，北方地区由于少雨，一般多采用露天堆场，南方地区由于多雨，一般多采用半露天堆场，需设置遮雨棚；按功能作用又可分为常用堆场和备用堆场。（1）配置1台装载机及2台液压叠臂式抓斗起重机，用于燃料的堆卸料及转运工作；（2）原料堆场内的转运及堆高设备由用户根据电厂实际运行情况采购。",
    	"default_value": "8"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_fuel_available_reserves",
        "name": u"燃料可存储量",
        "symbol": u"Bdc",
        "unit": u"t",
        "calculate": u"Qd*T",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_aggregate_coefficient",
        "name": u"计算堆料系数",
        "symbol": u"Ndc",
        "unit": u"--",
        "calculate": u"考虑到消防及汽车通道",
        "remark": "",
        "default_value": "0.65"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_average_stack_height",
        "name": u"平均堆高",
        "symbol": u"Hdc",
        "unit": u"m",
        "calculate": u"推荐值为4~6",
        "remark": "",
        "default_value": "5"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_fuel_bulk_density",
        "name": u"燃料堆积密度",
        "symbol": u"p",
        "unit": u"t/m³",
        "calculate": u"推荐值取0.04~0.1，在无资料情况下 原始设定值取0.04",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_yard_area",
        "name": u"原料堆场面积",
        "symbol": u"Fdc",
        "unit": u"㎡",
        "calculate": u"Bdc/(p*Hdc*Ndc)",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "d_fuel_reserve_days",
        "name": u"燃料的储备日数",
        "symbol": u"Tlp",
        "unit": u"d",
        "calculate": u"推荐值为4~8",
        "remark": "干料棚的主要作用是储存符合入炉要求的燃料，兼具卸载、转运、拌料、上料、整备等功能，一般采用半封闭式结构，设消防措施，不设采暖措施。（1）对于一炉一机配置的生物质电厂，干料棚内一般设置2台液压叠臂式抓斗起重机，每台起重量10t，斗容3m³，也可配置2台内燃叉车或2台轮式装载机，另设1台备用；（2）对于两炉两机配置的生物质电厂，干料棚内一般设置4台液压叠臂式抓斗起重机，每台起重量5t，斗容1.5m³，并辅以装载机及内燃叉车。",
        "default_value": "7"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "d_fuel_available_reserves",
        "name": u"燃料可存储量",
        "symbol": u"Blp",
        "unit": u"t",
        "calculate": u"Qd*T",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "d_aggregate_coefficient",
        "name": u"计算堆料系数",
        "symbol": u"Nlp",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": "0.95"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "d_average_stack_height",
        "name": u"平均堆高",
        "symbol": u"Hlp",
        "unit": u"m",
        "calculate": u"推荐值为5~7",
        "remark": "",
        "default_value": "6"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "d_fuel_bulk_density",
        "name": u"燃料堆积密度",
        "symbol": u"p",
        "unit": u"t/m³",
        "calculate": u"推荐值取0.04~0.1 在无资料情况下，原始设定值取0.04",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "d_yard_area",
        "name": u"原料堆场面积",
        "symbol": u"Flp",
        "unit": u"㎡",
        "calculate": u"Blp/(p*Hlp*Nlp)",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "t_rated_fuel_consumption",
        "name": u"锅炉额定燃料耗量",
        "symbol": u"Bj",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "t_hourage",
        "name": u"消耗小时数",
        "symbol": u"Twb",
        "unit": u"h",
        "calculate": u"",
        "remark": "",
        "default_value": "0.06"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "t_bin_quantity",
        "name": u"料仓数量",
        "symbol": u"Nwb",
        "unit": u"--",
        "calculate": u"每条皮带输送机设置2个尾部料仓",
        "remark": "",
        "default_value": "2"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "t_total_effective_volume",
        "name": u"总有效容积",
        "symbol": u"Vwb",
        "unit": u"m³",
        "calculate": u"Bj*Twb/p",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "t_single_effective_volume_calculation",
        "name": u"单个料仓有效容积-计算",
        "symbol": u"Vdwb",
        "unit": u"m³",
        "calculate": u"Vwb/Nwb",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "t_single_effective_volume_selected",
        "name": u"单个料仓有效容积-选定",
        "symbol": u"V",
        "unit": u"m³",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "t_consumption_hours",
        "name": u"反推消耗小时数",
        "symbol": u"T",
        "unit": u"h",
        "calculate": u"V*p*Nwb/Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_rated_fuel_consumption",
        "name": u"锅炉额定燃料耗量",
        "symbol": u"Bj",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_duplex_number",
        "name": u"双螺旋给料机组数",
        "symbol": u"Nsl",
        "unit": u"--",
        "calculate": u"每个尾部料仓受料斗下设置2组双螺旋给料机",
        "remark": "",
        "default_value": "4"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_flushness",
        "name": u"富裕量",
        "symbol": u"k",
        "unit": u"%",
        "calculate": u"",
        "remark": "",
        "default_value": "150"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_duplex_output",
        "name": u"双螺旋给料机总出力",
        "symbol": u"Qsl",
        "unit": u"t/h",
        "calculate": u"Bj*k/100",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_single_duplex_output",
        "name": u"单组双螺旋给料机出力",
        "symbol": u"Qdsl",
        "unit": u"t/h",
        "calculate": u"Qsl/Nsl",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_single_rated_fuel_consumption",
        "name": u"单台锅炉额定耗煤量",
        "symbol": u"Bj",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "锅炉额定容量≤65t/h，皮带输送机采用单路布置，每路出力≥150%锅炉满负荷燃料耗量;锅炉额定容量＞65t/h，皮带输送机采用双路布置，一用一备，每路出力≥150%锅炉满负荷燃料耗量。上料系统按三班制运行，每班运行约为8h。根据《秸秆发电设计规范》：（1）皮带输送机上应安装电子皮带秤用于入炉燃料的计量；（2）在输料栈桥采光间应设置一级圆盘电磁除铁器，在除铁器落铁处，还应设置集铁桶。",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_daily_consumption",
        "name": u"日耗量",
        "symbol": u"Qd",
        "unit": u"t/d",
        "calculate": u"Bj*Hd",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_feeding_output_calculation",
        "name": u"上料系统出力—计算",
        "symbol": u"Qsl",
        "unit": u"t/h",
        "calculate": u"Bj*150/100",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_feeding_output_selected",
        "name": u"上料系统出力—选定",
        "symbol": u"Q",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_belt_width",
        "name": u"皮带宽度",
        "symbol": u"B",
        "unit": u"mm",
        "calculate": u"推荐值为800、1000、1200、1400",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_section_coefficient",
        "name": u"断面系数",
        "symbol": u"K",
        "unit": u"--",
        "calculate": u"此项与皮带宽度关联，皮带宽度一旦确定，断面系数根据表10.2.4进行自动匹配。",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_belt_speed",
        "name": u"皮带速度",
        "symbol": u"V",
        "unit": u"m/s",
        "calculate": u"推荐值为1.0、1.25、1.6",
        "remark": "",
        "default_value": "1.25"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_loose_density",
        "name": u"物料松散密度",
        "symbol": u"p",
        "unit": u"t/m³",
        "calculate": u"推荐值取0.04~0.1，在无资料情况下，原始设定值取0.04",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "f_belt_max_delivery",
        "name": u"皮带最大输送能力",
        "symbol": u"Qmax",
        "unit": u"t/h",
        "calculate": u"K*B*B*v*p/1000/1000",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "bs_rated_fuel_consumption",
        "name": u"锅炉额定燃料耗量",
        "symbol": u"Bj",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_hourage",
        "name": u"消耗小时数",
        "symbol": u"Tlq",
        "unit": u"h",
        "calculate": u"",
        "remark": "",
        "default_value": "0.5"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_bin_quantity",
        "name": u"料仓数量",
        "symbol": u"Nlq",
        "unit": u"--",
        "calculate": u"每台锅炉设置2个炉前料仓",
        "remark": "",
        "default_value": "2"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_total_effective_volume",
        "name": u"总有效容积",
        "symbol": u"Vlq",
        "unit": u"m³",
        "calculate": u"Bj*Tlq/p",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_single_effective_volume_calculation",
        "name": u"单个料仓有效容积-计算",
        "symbol": u"Vdlq",
        "unit": u"m³",
        "calculate": u"Vlq/Nlq",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_single_effective_volume_selected",
        "name": u"单个料仓有效容积-选定",
        "symbol": u"V",
        "unit": u"m³",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "b_consumption_hours",
        "name": u"反推消耗小时数",
        "symbol": u"T",
        "unit": u"h",
        "calculate": u"V*p*Nlq/Bj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_rated_fuel_consumption",
        "name": u"锅炉额定燃料耗量",
        "symbol": u"Bj",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_duplex_number",
        "name": u"双螺旋给料机组数",
        "symbol": u"Ngl",
        "unit": u"--",
        "calculate": u"65t/h及以下：宜取2；65t/h以上：宜取4",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_flushness",
        "name": u"富裕量",
        "symbol": u"k",
        "unit": u"%",
        "calculate": u"",
        "remark": "",
        "default_value": "150"
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_duplex_output",
        "name": u"双螺旋给料机总出力",
        "symbol": u"Qgl",
        "unit": u"t/h",
        "calculate": u"Bj*k/100",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "fuel_ST",
        "name_eng": "s_single_duplex_output",
        "name": u"单组双螺旋给料机出力",
        "symbol": u"Qdgl",
        "unit": u"t/h",
        "calculate": u"Qgl/Ngl",
        "remark": "",
        "default_value": ""
    }
]

# 脱硫脱硝系统sheet
desul_denit_data=[
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_sulfur_content_received",
        "name": u"收到基硫份",
        "symbol": u"St,ar",
        "unit": u"%",
        "calculate": u"见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_feed_consumption",
        "name": u"计算耗料量",
        "symbol": u"Bj",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_fuel_so2",
        "name": u"燃料中的含硫量燃烧后氧化成SO2的份额",
        "symbol": u"K",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_before_so2",
        "name": u"脱硫前烟气中的SO2含量",
        "symbol": u"Mso2",
        "unit": u"kg/h",
        "calculate": u"2*K*Bj*St,ar/100",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_input_smoke",
        "name": u"引风机进口烟气容积流量（标况）",
        "symbol": u"VNxf",
        "unit": u"Nm3/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_no_before_so2",
        "name": u"未脱硫前SO2浓度（标态）",
        "symbol": u"C'SO2",
        "unit": u"mg/Nm3",
        "calculate": u"Mso2/VNxf*106",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_desulfurization_efficiency",
        "name": u"脱硫效率",
        "symbol": u"η",
        "unit": u"%",
        "calculate": u"炉内喷钙取80",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_after_so2",
        "name": u"脱硫后SO2浓度（标态）",
        "symbol": u"CSO2",
        "unit": u"mg/Nm3",
        "calculate": u"(1-η)C'SO2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_env_after_so2",
        "name": u"环保要求SO2的排放浓度",
        "symbol": u"C''SO2",
        "unit": u"mg/Nm3",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "s_after_so2_discharge",
        "name": u"脱硫后SO2排放量（标态）",
        "symbol": u"M'SO2",
        "unit": u"kg/h",
        "calculate": u"(1-η)MSO2或CSO2*VNxf",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_desulfurization_percentage",
        "name": u"炉内脱硫百分比",
        "symbol": u"",
        "unit": u"%",
        "calculate": u"推荐值为≥90",
        "remark": "",
        "default_value": "95"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_after_so2",
        "name": u"炉内脱硫后SO2浓度",
        "symbol": u"CSO2(炉内)",
        "unit": u"mg/Nm3",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_so2_quality",
        "name": u"脱除SO2质量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_so2_molar",
        "name": u"脱除SO2摩尔量",
        "symbol": u"",
        "unit": u"kmol/h",
        "calculate": u"SO2式量64",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_sulfur_molar",
        "name": u"钙硫摩尔比",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"推荐值为≥2",
        "remark": "",
        "default_value": "2"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_caco3_molar",
        "name": u"反应所需CaCO3摩尔量",
        "symbol": u"",
        "unit": u"kmol/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_caco3_quality_require",
        "name": u"反应所需CaCO3质量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"CaCO3式量100",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_caco3_quality_reaction",
        "name": u"参加反应CaCO3质量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_caso4_quality_generation",
        "name": u"反应生成CaSO4质量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"CaCO3-〉CaSO4",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_after_quality_add",
        "name": u"反应后质量增加",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_purity",
        "name": u"石灰石纯度",
        "symbol": u"",
        "unit": u"%",
        "calculate": u"推荐值为≥90",
        "remark": "",
        "default_value": "90"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_consumption",
        "name": u"石灰石耗量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_ash",
        "name": u"炉内脱硫产生的灰渣量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_storage_time",
        "name": u"石灰石粉仓储存时间",
        "symbol": u"",
        "unit": u"d",
        "calculate": u"",
        "remark": "",
        "default_value": "3"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_output",
        "name": u"石灰石粉仓出力",
        "symbol": u"",
        "unit": u"kg",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_density",
        "name": u"石灰石粉堆积密度",
        "symbol": u"Pa",
        "unit": u"t/m³",
        "calculate": u"推荐值为0.7~0.8",
        "remark": "",
        "default_value": "0.8"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_fullness",
        "name": u"石灰石粉仓充满系数",
        "symbol": u"K",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": "0.7"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_volumn",
        "name": u"石灰石粉仓体积",
        "symbol": u"V",
        "unit": u"m³",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_height",
        "name": u"高",
        "symbol": u"H",
        "unit": u"m",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "c_limestone_diameter",
        "name": u"直径",
        "symbol": u"D",
        "unit": u"m",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "n_before_nox_concentration",
        "name": u"脱硝前NOX浓度",
        "symbol": u"C'NOX",
        "unit": u"mg/Nm3",
        "calculate": u"推荐值为150～250",
        "remark": "",
        "default_value": "200"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "n_input_smoke",
        "name": u"引风机进口烟气容积流量（标况）",
        "symbol": u"VNxf",
        "unit": u"Nm3/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "n_desulfurization_efficiency",
        "name": u"脱硝效率(总效率)",
        "symbol": u"η",
        "unit": u"%",
        "calculate": u"",
        "remark": "",
        "default_value": "60"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "n_before_nox_discharge",
        "name": u"脱硝前NOX排放量",
        "symbol": u"MNOX",
        "unit": u"kg/h",
        "calculate": u"C'NOX*VNxf*10-6",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "n_after_nox_concentration",
        "name": u"脱硝后NOX浓度",
        "symbol": u"CNOX",
        "unit": u"mg/Nm3",
        "calculate": u"(1-η)C'NOX",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "n_env_after_nox_concentration",
        "name": u"环保要求NOX的排放浓度",
        "symbol": u"C'NOX",
        "unit": u"mg/Nm3",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "n_after_nox_discharge",
        "name": u"脱硝后NOX排放量",
        "symbol": u"M'NOX",
        "unit": u"kg/h",
        "calculate": u"(1-η)MNOX",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_denitration_percentage",
        "name": u"炉内脱硝百分比",
        "symbol": u"η'",
        "unit": u"%",
        "calculate": u"推荐值为≥90",
        "remark": "",
        "default_value": "95"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_denitration_quality",
        "name": u"炉内脱硝量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"(Mnox-M'nox)*η'",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_after_nox_discharge",
        "name": u"炉内脱硝后NOX排放量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_denitration_molar",
        "name": u"炉内脱硝摩尔量",
        "symbol": u"",
        "unit": u"kmol/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_escape_rate",
        "name": u"氨逃逸率",
        "symbol": u"",
        "unit": u"mg/Nm3",
        "calculate": u"",
        "remark": "",
        "default_value": "8"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_escape_quality",
        "name": u"氨逃逸量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_escape_quality_urea",
        "name": u"逃逸氨折算尿素量",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"(NH2)2CO→2NH3+CO",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_nh3nox_molar",
        "name": u"NH3/NOX摩尔比",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_urea_nox_molar",
        "name": u"尿素/NOX摩尔比",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"NH3/NOX摩尔比/2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_urea_nox_quality",
        "name": u"尿素/NOX式量比",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_theory_urea",
        "name": u"理论尿素消耗量",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_use_urea",
        "name": u"尿素用量(一台炉)",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"理论尿素消耗量+逃逸氨折算尿素量",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_water_urea",
        "name": u"尿素溶液消耗水量(一台炉)",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"尿素溶液浓度取25%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_days_urea",
        "name": u"尿素仓库天数",
        "symbol": u"",
        "unit": u"d",
        "calculate": u"",
        "remark": "",
        "default_value": "5"
    },
    {
        "module_name": "desulfurization_denitrification",
        "name_eng": "d_capacity_urea",
        "name": u"尿素仓库容量",
        "symbol": u"",
        "unit": u"t",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    }
]

# 除尘除灰除渣系统sheet
das_remove_data=[
    {
        "module_name": "das_remove",
        "name_eng": "d_total_ash",
        "name": u"灰渣总量(炉内脱硫后)",
        "symbol": u"",
        "unit": u"kg/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_flyash_fraction",
        "name": u"飞灰份额",
        "symbol": u"αf",
        "unit": u"%",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_entry_flyash",
        "name": u"除尘器入口（锅炉出口）飞灰量",
        "symbol": u"Gaf",
        "unit": u"kg/h",
        "calculate": u"αf*Gzh",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_standard_smoke_flow",
        "name": u"标况下除尘器进口烟气容积流量",
        "symbol": u"VNycj",
        "unit": u"Nm3/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_actual_smoke_flow",
        "name": u"除尘器进口处烟气容积流量(实态）",
        "symbol": u"Vycj",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_standard_smoke_concentration",
        "name": u"标况下除尘器进口烟气浓度",
        "symbol": u"Ci",
        "unit": u"mg/Nm3",
        "calculate": u"Gaf*106/VNycj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_actual_smoke_concentration",
        "name": u"除尘器进口处烟气浓度(实态）",
        "symbol": u"C'i",
        "unit": u"mg/m3",
        "calculate": u"Gaf*106/Vycj",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_dust_remove_efficiency",
        "name": u"综合除尘效率",
        "symbol": u"ηc",
        "unit": u"%",
        "calculate": u"根据相关项目经验及设计院资料可知，国内生物质发电项目除尘方式多采用旋风除尘器＋布袋除尘器，即组合式除尘器。前置的双筒旋风除尘器主要作用是预除尘，其除尘效率~70%，后置的布袋除尘器是主要的除尘设备，其除尘效率≥99.80%。",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_exit_smoke_concentration",
        "name": u"除尘器（烟囱）出口烟气浓度（标况）",
        "symbol": u"Co",
        "unit": u"mg/Nm3",
        "calculate": u"Ci*（1-ηc）",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_exit_smoke_flow",
        "name": u"除尘器（烟囱）出口烟气飞灰量（标况）",
        "symbol": u"G'af",
        "unit": u"kg/h",
        "calculate": u"Gaf*（1-ηc）",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_dust_wiper_flow",
        "name": u"除尘器下灰量",
        "symbol": u"Af",
        "unit": u"kg/h",
        "calculate": u"Gaf*ηc",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_entry_smoke_volume",
        "name": u"引风机进口烟气容积量(实态）",
        "symbol": u"Vxf",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_tun_exit_smoke_concentration",
        "name": u"烟囱出口烟气浓度（实态）",
        "symbol": u"",
        "unit": u"mg/m3",
        "calculate": u"Gaf*（1-ηc）*106/Vxf",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "d_env_particulate",
        "name": u"环保要求颗粒物的排放浓度",
        "symbol": u"",
        "unit": u"mg/m3",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_remove_output",
        "name": u"除灰系统出力",
        "symbol": u"Gm",
        "unit": u"t/h",
        "calculate": u"250%*Af",
        "remark": "除灰系统的主要设备除了灰仓外，还包括仓泵、脉冲布袋除尘器、气化槽、气化风机、电加热器、库底卸料器、干灰散装机、双轴加湿搅拌机（湿度15~25%）、储气罐等。",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_bulk_density",
        "name": u"干灰堆积密度",
        "symbol": u"Pa",
        "unit": u"t/m³",
        "calculate": u"推荐值取0.2~0.4，在无资料情况下，原始设定值取0.2",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_fullness",
        "name": u"灰仓充满系数",
        "symbol": u"K",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": "0.7"
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_storage_time",
        "name": u"存灰时间",
        "symbol": u"T",
        "unit": u"h",
        "calculate": u"推荐值为1~2",
        "remark": "",
        "default_value": "2"
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_volumn",
        "name": u"灰仓有效容积",
        "symbol": u"Va",
        "unit": u"m³",
        "calculate": u"T*Gm/Pa/K",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_diameter",
        "name": u"直径",
        "symbol": u"D",
        "unit": u"m",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_height",
        "name": u"高度",
        "symbol": u"H",
        "unit": u"m",
        "calculate": u"未含有5m的操作平台",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_ratio",
        "name": u"灰气比",
        "symbol": u"n",
        "unit": u"--",
        "calculate": u"推荐值为7~20",
        "remark": "",
        "default_value": "15"
    },
    {
        "module_name": "das_remove",
        "name_eng": "a_gas_consumption",
        "name": u"输灰系统耗气量",
        "symbol": u"Q",
        "unit": u"Nm³/min",
        "calculate": u"1.2*16.67*Gm/n/1.293",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_slag_quantity",
        "name": u"渣量",
        "symbol": u"Gz",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "除渣系统的主要设备除了水冷滚筒冷渣器、链斗输送机、斗式提升机、渣仓外，还包括仓顶脉冲收尘器、排渣门等。",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_yns_output",
        "name": u"冷渣机的出力（单台）",
        "symbol": u"Glz",
        "unit": u"t/h",
        "calculate": u"375%*Gz",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_coolwater",
        "name": u"冷却水量（单台）",
        "symbol": u"Qlqs",
        "unit": u"t/h",
        "calculate": u"Glz*6",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_yns_number",
        "name": u"冷渣机台数",
        "symbol": u"n",
        "unit": u"--",
        "calculate": u"事故/运行；单台锅炉配置2台",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_slag_output",
        "name": u"除渣系统出力",
        "symbol": u"Gzm",
        "unit": u"t/h",
        "calculate": u"n*Gz",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_conveyor_output",
        "name": u"链斗输送机出力",
        "symbol": u"Gssm",
        "unit": u"t/h",
        "calculate": u"1.67*Gzm",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_bulk_density",
        "name": u"冷渣堆积密度",
        "symbol": u"Pa",
        "unit": u"t/m³",
        "calculate": u"",
        "remark": "",
        "default_value": "0.45"
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_fullness",
        "name": u"渣库充满系数",
        "symbol": u"K",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": "0.7"
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_storage_time",
        "name": u"存渣时间",
        "symbol": u"T",
        "unit": u"h",
        "calculate": u"推荐值为1~2",
        "remark": "",
        "default_value": "7"
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_volumn",
        "name": u"钢渣仓有效容积",
        "symbol": u"Va",
        "unit": u"m³",
        "calculate": u"T*Gm/Pa/K",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_diameter",
        "name": u"直径",
        "symbol": u"D",
        "unit": u"m",
        "calculate": u"",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "das_remove",
        "name_eng": "s_height",
        "name": u"高度",
        "symbol": u"H",
        "unit": u"m",
        "calculate": u"未含有5m的操作平台",
        "remark": "",
        "default_value": ""
    }
]

# 锅炉辅机sheet
boiler_auxiliaries_data=[
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_boiler_evaporation",
        "name": "锅炉蒸发量",
        "symbol": "Dgr",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_emission_time",
        "name": "排放时间",
        "symbol": "t",
        "unit": "min",
        "calculate": "一班一次，2-3次，一次0.5-1min；推荐值为0.5-1min，原始设定值取1min",
        "remark": "",
        "default_value": "1"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_emission_rate",
        "name": "定期排污率",
        "symbol": "η",
        "unit": "/",
        "calculate": "推荐值为0.1%-0.5%",
        "remark": "",
        "default_value": "0.1"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_sewage_quantity",
        "name": "定期排污水量",
        "symbol": "Dpb",
        "unit": "kg/h",
        "calculate": "Dgr*1000*t*60*η",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_drum_pressure",
        "name": "汽包压力",
        "symbol": "P",
        "unit": "MPa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_drum_aturatedwater_enthalpy",
        "name": "汽包压力下的饱和水焓",
        "symbol": "hd",
        "unit": "kj/kg",
        "calculate": "汽包压力",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_work_pressure",
        "name": "排污扩容器工作压力",
        "symbol": "",
        "unit": "--",
        "calculate": "扩容器压力推荐选0.15MPa(a)/0.45",
        "remark": "",
        "default_value": "0.15"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_work_aturatedwater_enthalpy",
        "name": "扩容器压力下饱和水焓",
        "symbol": "hs",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_work_latentheat_vaporization",
        "name": "扩容器压力下汽化潜热",
        "symbol": "r",
        "unit": "kj/kg",
        "calculate": "查表（饱和汽焓-饱和水焓）",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_ultimate_strength",
        "name": "扩容器单位容积允许极限强度",
        "symbol": "R",
        "unit": "m3/（m3/kg）",
        "calculate": "推荐值为800~1000",
        "remark": "",
        "default_value": "2000"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_volume",
        "name": "排污扩容容积",
        "symbol": "Vv",
        "unit": "m³",
        "calculate": "1.3~1.5的富裕系数",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_specifications",
        "name": "扩容器规格",
        "symbol": "",
        "unit": "--",
        "calculate": "考虑紧急放水后：DP-7.5",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_boiler_evaporation",
        "name": "锅炉蒸发量",
        "symbol": "Dgr",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_emission_rate",
        "name": "连续排污率",
        "symbol": "η",
        "unit": "/",
        "calculate": "推荐值为1%-2%",
        "remark": "",
        "default_value": "2"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_sewage_quantity",
        "name": "连续排污水量",
        "symbol": "Dpb",
        "unit": "kg/h",
        "calculate": "D0*1000*η",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_drum_pressure",
        "name": "汽包压力",
        "symbol": "P",
        "unit": "MPa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_drum_aturatedwater_enthalpy",
        "name": "汽包压力下的饱和水焓",
        "symbol": "hd",
        "unit": "kj/kg",
        "calculate": "汽包压力",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_work_pressure",
        "name": "排污扩容器工作压力",
        "symbol": "",
        "unit": "--",
        "calculate": "扩容器压力推荐选取0.15MPa(a)/0.45/1.0",
        "remark": "",
        "default_value": "1"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_work_aturatedwater_enthalpy",
        "name": "扩容器压力下饱和水焓",
        "symbol": "hs",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_work_steam_pecificvolume",
        "name": "扩容器压力下蒸汽比容",
        "symbol": "υ",
        "unit": "m3/kg",
        "calculate": "查表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_work_latentheat_vaporization",
        "name": "扩容器压力下汽化潜热",
        "symbol": "r",
        "unit": "kj/kg",
        "calculate": "查表（饱和汽焓-饱和水焓）",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_steam_dryness",
        "name": "扩容器蒸汽干度",
        "symbol": "X",
        "unit": "--",
        "calculate": "推荐值为0.97~0.98",
        "remark": "",
        "default_value": "0.97"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_ultimate_strength",
        "name": "扩容器单位容积润许极限强度",
        "symbol": "R",
        "unit": "m3/（m3/kg）",
        "calculate": "推荐值为800~1000",
        "remark": "",
        "default_value": "800"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_vaporization_capacity",
        "name": "排污水汽化量",
        "symbol": "Df",
        "unit": "kg/kg",
        "calculate": "(hd*η-hs)/xr",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_volume",
        "name": "排污扩容汽容积",
        "symbol": "Vv",
        "unit": "m³",
        "calculate": "1.2的富裕系数，水容积为汽容积的1/4",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "c_specifications",
        "name": "扩容器规格",
        "symbol": "",
        "unit": "--",
        "calculate": "LP-3.5/LP-1.5",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "a_altitude",
        "name": "海拔",
        "symbol": "A",
        "unit": "m",
        "calculate": "见需求调研表",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "a_atmosphere",
        "name": "大气压",
        "symbol": "P",
        "unit": "pa",
        "calculate": "若需求调研表中无当地历年平均气压数据，则按该公式计算大气压。",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "g_working_condition_temperature",
        "name": "工况温度",
        "symbol": "t",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "g_working_flow",
        "name": "工况流量",
        "symbol": "qv",
        "unit": "m³/h",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "g_local_atmosphere",
        "name": "当地大气压",
        "symbol": "p",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "g_standard_temperature",
        "name": "标况温度",
        "symbol": "t0",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "g_standard_pressure",
        "name": "标况压力",
        "symbol": "p0",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "g_standard_flow",
        "name": "标况流量",
        "symbol": "qv0",
        "unit": "Nm³/h",
        "calculate": "qv0=qv*(p/p0)*((t0+273)/(t+273))",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "b_standard_temperature",
        "name": "标况温度",
        "symbol": "t0",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "b_standard_pressure",
        "name": "标况压力",
        "symbol": "p0",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "b_standard_flow",
        "name": "标况流量",
        "symbol": "qv0",
        "unit": "Nm³/h",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "b_working_condition_temperature",
        "name": "工况温度",
        "symbol": "t",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "b_local_atmosphere",
        "name": "当地大气压",
        "symbol": "p",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "b_working_flow",
        "name": "工况流量",
        "symbol": "qv",
        "unit": "m³/h",
        "calculate": "qv=qv0*(p0/p)*((t+273)/(t0+273))",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_temperature",
        "name": "空气温度",
        "symbol": "t",
        "unit": "℃",
        "calculate": "设计值",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_boiler_resistance",
        "name": "锅炉本体阻力",
        "symbol": "pg",
        "unit": "pa",
        "calculate": "是否海拔修正,原始设定值为7500",
        "remark": "",
        "default_value": "7500"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_duct_resistance",
        "name": "风道阻力",
        "symbol": "py",
        "unit": "pa",
        "calculate": "大气压未修正,原始设定值为1500",
        "remark": "",
        "default_value": "1500"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_local_atmosphere",
        "name": "当地大气压",
        "symbol": "p0",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_smoke_flow",
        "name": "烟风流量（工况）",
        "symbol": "q",
        "unit": "m³/h",
        "calculate": "50:50时1.1倍",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_medium_temperature",
        "name": "铭牌介质温度",
        "symbol": "t1",
        "unit": "℃",
        "calculate": "常规20℃",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_fan_pressure",
        "name": "风机全压",
        "symbol": "p1",
        "unit": "pa",
        "calculate": "p1=p*(101325/p0)*((t+273)/(t1+273))",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_fan_select_pressure",
        "name": "风机选用全压",
        "symbol": "p2",
        "unit": "--",
        "calculate": "压头裕量≥20%，取20%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_fan_select_flow",
        "name": "风机选用流量",
        "symbol": "q2",
        "unit": "m³/h",
        "calculate": "风量裕量≥20%，取30%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_fan_efficiency",
        "name": "风机效率",
        "symbol": "η1",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.75"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_motor_efficiency",
        "name": "电动机效率",
        "symbol": "ηd",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.95"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_fan_power",
        "name": "风机轴功率",
        "symbol": "P'",
        "unit": "kw",
        "calculate": "P'=p2*q2/η",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_motor_safe",
        "name": "电机安全裕量",
        "symbol": "K",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "sf_motor_power",
        "name": "电机功率",
        "symbol": "P",
        "unit": "kw",
        "calculate": "P=K*P'/ηd",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_temperature",
        "name": "空气温度",
        "symbol": "t",
        "unit": "℃",
        "calculate": "设计值",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_boiler_resistance",
        "name": "锅炉本体阻力",
        "symbol": "pg",
        "unit": "pa",
        "calculate": "是否海拔修正,原始设定值为5500",
        "remark": "",
        "default_value": "7500"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_duct_resistance",
        "name": "风道阻力",
        "symbol": "py",
        "unit": "pa",
        "calculate": "大气压未修正,原始设定值为1500",
        "remark": "",
        "default_value": "1500"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_local_atmosphere",
        "name": "当地大气压",
        "symbol": "p0",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_smoke_flow",
        "name": "烟风流量（工况）",
        "symbol": "q",
        "unit": "m³/h",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_medium_temperature",
        "name": "铭牌介质温度",
        "symbol": "t1",
        "unit": "℃",
        "calculate": "常规20℃",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_fan_pressure",
        "name": "风机全压",
        "symbol": "p1",
        "unit": "pa",
        "calculate": "p1=p*(101325/p0)",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_fan_select_pressure",
        "name": "风机选用全压",
        "symbol": "p2",
        "unit": "--",
        "calculate": "压头裕量≥20%，取20%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_fan_select_flow",
        "name": "风机选用流量",
        "symbol": "q2",
        "unit": "m³/h",
        "calculate": "风量裕量≥10%，取30%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_fan_efficiency",
        "name": "风机效率",
        "symbol": "η1",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.85"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_motor_efficiency",
        "name": "电动机效率",
        "symbol": "ηd",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.95"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_fan_power",
        "name": "风机轴功率",
        "symbol": "P'",
        "unit": "kw",
        "calculate": "P'=p2*q2/η",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_motor_safe",
        "name": "电机安全裕量",
        "symbol": "K",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "ss_motor_power",
        "name": "电机功率",
        "symbol": "P",
        "unit": "kw",
        "calculate": "P=K*P'/ηd",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_temperature",
        "name": "烟气温度",
        "symbol": "t",
        "unit": "℃",
        "calculate": "设计值",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_boiler_resistance",
        "name": "锅炉本体烟气阻力",
        "symbol": "pg",
        "unit": "pa",
        "calculate": "是否海拔修正,原始设定值为2480",
        "remark": "",
        "default_value": "2480"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_denitration",
        "name": "脱硝",
        "symbol": "pn",
        "unit": "pa",
        "calculate": "大气压未修正,原始设定值为600",
        "remark": "",
        "default_value": "600"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_duster",
        "name": "除尘器",
        "symbol": "pc",
        "unit": "Pa",
        "calculate": "大气压未修正,原始设定值为1200",
        "remark": "",
        "default_value": "1200"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_duct_resistance",
        "name": "风道阻力",
        "symbol": "py",
        "unit": "pa",
        "calculate": "大气压未修正,原始设定值为500",
        "remark": "",
        "default_value": "500"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_cduct_resistance",
        "name": "风机后脱硫塔及烟囱烟道阻力",
        "symbol": "ph",
        "unit": "pa",
        "calculate": "大气压未修正,原始设定值为3000",
        "remark": "",
        "default_value": "3000"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_local_atmosphere",
        "name": "当地大气压",
        "symbol": "p0",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_smoke_flow",
        "name": "烟风流量（工况）",
        "symbol": "q",
        "unit": "m³/h",
        "calculate": "引风机配置2台，便于烟风负荷调节。",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_medium_temperature",
        "name": "铭牌介质温度",
        "symbol": "t1",
        "unit": "℃",
        "calculate": "常规250℃",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_fan_pressure",
        "name": "风机全压",
        "symbol": "p1",
        "unit": "pa",
        "calculate": "p1=p*(101325/p0)*((t+273)/(t1+273))",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_fan_select_pressure",
        "name": "风机选用全压",
        "symbol": "p2",
        "unit": "--",
        "calculate": "压头裕量≥20%，取20%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_fan_select_flow",
        "name": "风机选用流量",
        "symbol": "q2",
        "unit": "m³/h",
        "calculate": "风量裕量≥10%，取10%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_fan_efficiency",
        "name": "风机效率",
        "symbol": "η1",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.85"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_motor_efficiency",
        "name": "电动机效率",
        "symbol": "ηd",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.95"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_fan_power",
        "name": "风机轴功率",
        "symbol": "P'",
        "unit": "kw",
        "calculate": "P'=p2*q2/η",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_motor_safe",
        "name": "电机安全裕量",
        "symbol": "K",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "i_motor_power",
        "name": "电机功率",
        "symbol": "P",
        "unit": "kw",
        "calculate": "P=K*P'/ηd",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_temperature",
        "name": "空气温度",
        "symbol": "t",
        "unit": "℃",
        "calculate": "设计值",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_pressure",
        "name": "风压",
        "symbol": "pg",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": "25000"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_duct_resistance",
        "name": "管道阻力",
        "symbol": "pz",
        "unit": "pa",
        "calculate": "原始设定值取500",
        "remark": "",
        "default_value": "500"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_local_atmosphere",
        "name": "当地大气压",
        "symbol": "p0",
        "unit": "pa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_smoke_flow",
        "name": "烟风流量（工况）",
        "symbol": "q",
        "unit": "m³/h",
        "calculate": "原始设定值取950",
        "remark": "",
        "default_value": "950"
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_medium_temperature",
        "name": "铭牌介质温度",
        "symbol": "t1",
        "unit": "℃",
        "calculate": "常规20℃",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_fan_pressure",
        "name": "风机全压",
        "symbol": "p1",
        "unit": "pa",
        "calculate": "p1=p*(101325/p0)*((t+273)/(t1+273))",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_fan_select_pressure",
        "name": "风机选用全压",
        "symbol": "p2",
        "unit": "--",
        "calculate": "压头裕量≥20%，取20%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_fan_select_flow",
        "name": "风机选用流量",
        "symbol": "q2",
        "unit": "m³/h",
        "calculate": "风量裕量≥20%，取30%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_fan_efficiency",
        "name": "风机效率",
        "symbol": "η1",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_motor_efficiency",
        "name": "电动机效率",
        "symbol": "ηd",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_fan_power",
        "name": "风机轴功率",
        "symbol": "P'",
        "unit": "kw",
        "calculate": "P'=p2*q2/η",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_motor_safe",
        "name": "电机安全裕量",
        "symbol": "K",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "boiler_auxiliaries",
        "name_eng": "r_motor_power",
        "name": "电机功率",
        "symbol": "P",
        "unit": "kw",
        "calculate": "P=K*P'/ηd",
        "remark": "",
        "default_value": ""
    }
]

# 公用工程sheet
official_process_data=[
    {
        "module_name": "official_process",
        "name_eng": "o_oil_can",
        "name": "容积V",
        "symbol": "",
        "unit": "m3",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_oil_pump",
        "name": "出力Q（单台）",
        "symbol": "",
        "unit": "t/h",
        "calculate": "Qnet.Ar*Bg*15%/10000/4.1868/1000",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_oil_pump_pressure",
        "name": "压力P",
        "symbol": "",
        "unit": "MPa",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_steam_flow",
        "name": "过热蒸汽额定流量",
        "symbol": "",
        "unit": "t/h",
        "calculate": "Dgr",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_loss_factory",
        "name": "厂内汽水损失",
        "symbol": "",
        "unit": "t/h",
        "calculate": "Dgr*3%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_boiler_blowdown_loss",
        "name": "锅炉排污损失",
        "symbol": "",
        "unit": "t/h",
        "calculate": "Dgr*2%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_start_accident_increase_loss",
        "name": "机组启动或事故增加损失",
        "symbol": "",
        "unit": "t/h",
        "calculate": "Dgr*10%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_external_supply_loss",
        "name": "外供汽损失",
        "symbol": "",
        "unit": "t/h",
        "calculate": "Qwg*（1-ηhs） （1）生物质发电项目：不对外供汽，所以外供汽损失取0；（2）生物质热电联产项目：对外供汽，外供汽损失主要取决于凝结水回水率ηhs的大小，若外供汽由于直接参与换热，凝结水水质较差，不考虑回收，则外供汽损失即为外供汽量。",
        "remark": "",
        "default_value": "0"
    },
    {
        "module_name": "official_process",
        "name_eng": "o_water_consumption",
        "name": "自用水量",
        "symbol": "",
        "unit": "t/h",
        "calculate": "(〔1〕+〔2〕+〔4〕）*10%",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_boiler_water_normal",
        "name": "锅炉补给水系统正常出力",
        "symbol": "",
        "unit": "t/h",
        "calculate": "〔1〕＋〔2〕＋〔4〕＋〔5〕",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_boiler_water_max",
        "name": "锅炉补给水系统最大出力",
        "symbol": "",
        "unit": "t/h",
        "calculate": "〔1〕＋〔2〕＋〔3〕＋〔4〕＋〔5〕",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_boiler_water_system",
        "name": "锅炉补给水系统出力",
        "symbol": "",
        "unit": "t/h",
        "calculate": "Q",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_salt_water_tank",
        "name": "除盐水箱有效容积",
        "symbol": "",
        "unit": "t/h",
        "calculate": "Q*5",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_steam_parameter",
        "name": "蒸汽参数",
        "symbol": "",
        "unit": "",
        "calculate": "根据《秸秆发电厂设计规范》可知，启动锅炉应根据工程具体情况确定是否设置，对于扩建电厂，宜采用原有机组的辅助蒸汽作为启动汽源，不设启动锅炉。",
        "remark": "低压参数，一般为0.32MPa（g）/204℃",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_steam_volumn",
        "name": "额定蒸发量",
        "symbol": "",
        "unit": "",
        "calculate": "",
        "remark": "推荐值为2~6t/h。根据《秸秆发电厂设计规范》可知，启动锅炉的容量应只考虑启动中必须的蒸汽量，不考虑裕量、汽轮机冲转调试用汽量、可暂时停用的施工用汽量及非启动用的其它用汽量，其容量宜为2~6t/h。在采暖区，同时考虑冬季全厂停电取暖时，启动锅炉容量可根据情况适当放大。",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_fuel_type",
        "name": "燃料类型",
        "symbol": "",
        "unit": "",
        "calculate": "",
        "remark": "",
        "default_value": ""
    },
    {
        "module_name": "official_process",
        "name_eng": "o_install_way",
        "name": "安装方式",
        "symbol": "",
        "unit": "",
        "calculate": "",
        "remark": "",
        "default_value": ""
    }
]


class AddBiomassCHP():
    # 初始化数据
    @staticmethod
    def init_data():
        # Company.insert_company()
        # Role.insert_roles()
        # User.insert_admin()
        data = [questionnaire_data, boilerCalculation_data, fuelST_data, desul_denit_data, das_remove_data, boiler_auxiliaries_data, official_process_data]
        for index in range(len(data)):
            AddBiomassCHP.insert_data(data[index])
        AddBiomassCHP.insert_component(beltwidth_data)

    # 表中插入数据
    @staticmethod
    def insert_data(data):
        module_name = data[0]["module_name"]
        for index in range(len(data)):
            name_eng = data[index]["name_eng"]
            name = data[index]["name"]
            symbol = data[index]["symbol"]
            unit = data[index]["unit"]
            calculate = data[index]["calculate"]
            remark = data[index]["remark"]
            default_value = data[index]["default_value"]
            biomassCHPconstant = BiomassCHPconstant.create_biomassCHPconstant(
                module_name, name_eng, name, symbol, unit, calculate, remark, default_value)
            BiomassCHPconstant.insert_biomassCHPconstant(biomassCHPconstant)

    # 表中插入皮带宽度数据
    @staticmethod
    def insert_component(beltwidth_data):
        for index in range(len(beltwidth_data)):
            width = beltwidth_data[index][0]
            coefficient = beltwidth_data[index][1]
            biomassCHPBeltWidth = BiomassCHPBeltWidth.create_biomassCHPBeltWidth(
                width, coefficient)
            biomassCHPBeltWidth.insert_biomassCHPBeltWidth(biomassCHPBeltWidth)