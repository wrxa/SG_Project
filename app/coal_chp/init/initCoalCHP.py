# -*- coding: utf-8 -*-
from app.models import Role, User, Company, Permission
from app.coal_chp.model.coalchpModels import CoalCHPConstant, \
     CoalCHPComponent
from app.models import Textlogic, ReportTemplate
# 燃煤热电联产需求调查表
questionnaire_data = [{
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_carbon",
    "name": u"收到基碳含量",
    "symbol": u"Car",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_hydrogen",
    "name": u"收到基氢含量",
    "symbol": u"Har",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_oxygen",
    "name": u"收到基氧含量",
    "symbol": u"Oar",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_nitrogen",
    "name": u"收到基氮含量",
    "symbol": u"Nar",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_sulfur",
    "name": u"收到基硫含量",
    "symbol": u"Sar",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_water",
    "name": u"收到基水份",
    "symbol": u"Mar",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_grey",
    "name": u"收到基灰份",
    "symbol": u"Aar",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_daf",
    "name": u"干燥无灰基挥发分",
    "symbol": u"Vdaf",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_grindability",
    "name": u"可磨系数",
    "symbol": u"KVTI",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "s_low",
    "name": u"收到基低位发热量",
    "symbol": u"Qnet，ar",
    "unit": u"KJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_altitude",
    "name": u"当地平均海拔",
    "symbol": u"A",
    "unit": u"m",
    "calculate": "",
    "remark": "",
    "default_value": "957.6",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_mean_annual_temperature",
    "name": u"多年平均温度",
    "symbol": u"T",
    "unit": u"℃",
    "calculate": "",
    "remark": "",
    "default_value": "9.9",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_mean_summer_temperature",
    "name": u"最热月平均温度",
    "symbol": u"T1",
    "unit": u"℃",
    "calculate": "",
    "remark": "",
    "default_value": "23",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_mean_winter_temperature",
    "name": u"最冷月平均温度",
    "symbol": u"T2",
    "unit": u"℃",
    "calculate": "",
    "remark": "",
    "default_value": "-7",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_extreme_high_temperature",
    "name": u"极端最高温度",
    "symbol": u"T3",
    "unit": u"℃",
    "calculate": "",
    "remark": "",
    "default_value": "38.8",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_extreme_low_temperature",
    "name": u"极端最低温度",
    "symbol": u"T4",
    "unit": u"℃",
    "calculate": "",
    "remark": "",
    "default_value": "-24.1",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_mean_annual_barometric",
    "name": u"多年平均大气压力",
    "symbol": u"Pb",
    "unit": u"Kpa",
    "calculate": "",
    "remark": "",
    "default_value": "89.56",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_mean_summer_barometric",
    "name": u"夏季大气压力",
    "symbol": u"pb1",
    "unit": u"Kpa",
    "calculate": "",
    "remark": "",
    "default_value": "87.49",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_mean_winter_barometric",
    "name": u"冬季大气压力",
    "symbol": u"Pb2",
    "unit": u"Kpa",
    "calculate": "",
    "remark": "",
    "default_value": "92.05",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_annual_average_relative_humidity",
    "name": u"多年平均相对湿度",
    "symbol": u"φ",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "59",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_mean_summer_relative_humidity",
    "name": u"全年最热月份平均相对湿度",
    "symbol": u"φ",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "w_mean_winter_relative_humidity",
    "name": u"全年最冷月份平均相对湿度",
    "symbol": u"φ",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "ihl_steam_pressure_level",
    "name": u"蒸汽压力等级",
    "symbol": u"P",
    "unit": u"MPa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "ihl_steam_temperature_level",
    "name": u"蒸汽温度等级",
    "symbol": u"T",
    "unit": u"℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "ihl_steam_time",
    "name": u"用汽时段",
    "symbol": u"--",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "ihl_recent_steam_flow_range",
    "name": u"近期蒸汽流量范围",
    "symbol": u"Qjq",
    "unit": u"t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "ihl_forward_steam_flow_range",
    "name": u"远期蒸汽流量范围",
    "symbol": u"Qyq",
    "unit": u"t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "ihl_condensate_water_iron",
    "name": u"凝结水含铁量",
    "symbol": u"CFe",
    "unit": u"mg/m3",
    "calculate": "",
    "remark": "考虑回水是否受主工艺污染",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "ihl_condensate_water_recovery_rate",
    "name": u"凝结水回收率",
    "symbol": u"Φ",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "hhl_heating_occasions_type",
    "name": u"采暖场合类型",
    "symbol": u"--",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "hhl_year_heating_days",
    "name": u"全年采暖天数",
    "symbol": u"--",
    "unit": u"d/a",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "hhl_recent_heating_area",
    "name": u"近期采暖面积",
    "symbol": u"--",
    "unit": u"万m3",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "hhl_forward_heating_area",
    "name": u"远期采暖面积",
    "symbol": u"--",
    "unit": u"万m3",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "os_planning_area",
    "name": u"规划占地面积",
    "symbol": u"--",
    "unit": u"亩",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "os_planned_expansion_capacity",
    "name": u"规划扩建容量",
    "symbol": u"--",
    "unit": u"MW",
    "calculate": "",
    "remark": "是否扩建",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "os_local_water_condition",
    "name": u"当地水源条件",
    "symbol": u"--",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "oe_electrical_load_demand",
    "name": u"电负荷需求",
    "symbol": u"--",
    "unit": u"KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "oe_higher_voltage_level",
    "name": u"上级变电压等级",
    "symbol": u"--",
    "unit": u"kV",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "oe_plant_distance_higher_change",
    "name": u"厂区距上级变距离",
    "symbol": u"--",
    "unit": u"km",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "oe_is_internet_access",
    "name": u"是否上网",
    "symbol": u"--",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "oe_is_isolated_network",
    "name": u"是否孤网运行",
    "symbol": u"--",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "op_flue_gas_sox_limits",
    "name": u"烟气SOX排放限值",
    "symbol": u"--",
    "unit": u"mg/Nm3",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "op_flue_gas_nox_limits",
    "name": u"烟气NOX排放限值",
    "symbol": u"--",
    "unit": u"mg/Nm3",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "op_flue_gas_dust_limits",
    "name": u"烟气烟尘排放限值",
    "symbol": u"--",
    "unit": u"mg/Nm3",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "od_use_desulfurization_form",
    "name": u"拟采用脱硫形式",
    "symbol": u"--",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "od_use_denitration_form",
    "name": u"拟采用脱硝形式",
    "symbol": u"--",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "od_limestone_supply",
    "name": u"石灰石供应情况",
    "symbol": u"--",
    "unit": u"mg/Nm3",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_questionnaire",
    "name_eng": "od_urea_or_ammonia_water_supply",
    "name": u"尿素/氨水供应情况",
    "symbol": u"--",
    "unit": u"--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}]

# 燃煤热电联产计算_输煤系统sheet
coalHandingSystem_data = [{
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "b_boiler_rated_coal_capacity",
    "name": u"锅炉额定耗煤量",
    "symbol": u"Bj",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "b_boiler_daily_utilization_hours",
    "name": u"锅炉日利用小时数",
    "symbol": u"Hd",
    "unit": u"h",
    "calculate": u"20~22",
    "remark": u"",
    "default_value": "22",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "b_coal_daily_consumption",
    "name": u"日耗煤量",
    "symbol": u"Qd",
    "unit": u"t/d",
    "calculate": u"Bj*Hd",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "b_boiler_annual_utilization_hours",
    "name": u"锅炉年利用小时数",
    "symbol": u"Ha",
    "unit": u"h",
    "calculate": u"7260",
    "remark": u"",
    "default_value": "7260",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "b_coal_annual_consumption",
    "name": u"年耗煤量",
    "symbol": u"Qa",
    "unit": u"万t/a",
    "calculate": u"Bj*Ha",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "b_daily_coal_unbalanced_coefficient",
    "name": u"日来煤不均衡系数",
    "symbol": u"Kb",
    "unit": "--",
    "calculate": u"1.1~1.3",
    "remark": u"",
    "default_value": "1.3",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "b_daily_rail_coal_amount",
    "name": u"铁路来煤日计算煤量",
    "symbol": u"Md",
    "unit": u"t/d",
    "calculate": u"Kb*Qd",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "b_daily_vehicle_coal_amount",
    "name": u"汽车来煤日计算煤量",
    "symbol": u"Md",
    "unit": u"t/d",
    "calculate": u"Kb*Qa*Hd/Ha",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_boiler_hour_coal_capacity",
    "name": u"锅炉每小时最大耗煤量",
    "symbol": u"Q",
    "unit": u"t",
    "calculate": "",
    "remark": u"",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_boiler_daily_working_hours",
    "name": u"锅炉每日运行时数",
    "symbol": u"T",
    "unit": u"h",
    "calculate": u"22",
    "remark": u"",
    "default_value": "22",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_coal_store_days",
    "name": u"煤的储备日数",
    "symbol": u"n",
    "unit": u"d",
    "calculate": u"汽车5~10，火车10~25",
    "remark": u"",
    "default_value": "10",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_coalyard_store_amount",
    "name": u"煤场存储量",
    "symbol": u"B",
    "unit": u"t",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_coal_channel_occupy_coefficient",
    "name": u"煤堆通道占用系数",
    "symbol": u"N",
    "unit": u"--",
    "calculate": u"汽车1.5，火车1.3",
    "remark": u"",
    "default_value": "1.5",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_coal_shape_coefficient",
    "name": u"煤堆形状系数",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"0.6~0.9",
    "remark": u"",
    "default_value": "0.8",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_coal_height",
    "name": u"煤堆高度",
    "symbol": u"H",
    "unit": u"m",
    "calculate": u"装载机2~3 推煤机≤6",
    "remark": u"",
    "default_value": "6",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_coal_bulk_density",
    "name": u"煤的堆密度",
    "symbol": u"p",
    "unit": u"t/m³",
    "calculate": u"0.8~1",
    "remark": u"",
    "default_value": "0.8",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_coalyard_area",
    "name": u"煤场面积",
    "symbol": u"F",
    "unit": u"m²",
    "calculate": u"QTNn/KHp",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_height",
    "name": u"长",
    "symbol": u"L",
    "unit": u"m",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "c_width",
    "name": u"宽",
    "symbol": u"B",
    "unit": u"m",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "e_coal_bunker_counts",
    "name": u"煤仓个数",
    "symbol": u"n",
    "unit": u"--",
    "calculate": u"2运1备",
    "remark": u"",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "e_effective_cubage_selected",
    "name": u"有效容积-选定",
    "symbol": u"V",
    "unit": u"m³",
    "calculate": u"根据计算容积",
    "remark": u"",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "e_effective_cubage_calculated",
    "name": u"有效容积-计算",
    "symbol": u"V",
    "unit": u"m³",
    "calculate": u"二班 10~12",
    "remark": u"",
    "default_value": "10",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "e_backstep_consumption_hours",
    "name": u"反推消耗小时",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "t_transport_unbalanced_coefficient",
    "name": u"运输不平衡系数",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"1.2~1.5",
    "remark": u"",
    "default_value": "1.3",
    "disable": ""
}, {
    "module_name":
    "coalCHP_CoalHandingSystem",
    "name_eng":
    "t_transportsystem_effective_working_hours",
    "name":
    u"运煤系统有效作业时间",
    "symbol":
    u"t",
    "unit":
    u"h",
    "calculate":
    u"三班≤16h",
    "remark":
    u"",
    "default_value":
    "12",
    "disable":
    ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "t_transportsystem_amount",
    "name": u"运煤系统运输量",
    "symbol": u"Q",
    "unit": u"t/h",
    "calculate": u"22*Bj*K/t",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "t_vehicle_capacity_tonnage",
    "name": u"车辆名义载重量",
    "symbol": u"Qa",
    "unit": u"t",
    "calculate": u"17",
    "remark": u"",
    "default_value": "17",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "t_daily_working_hours",
    "name": u"每昼夜小时",
    "symbol": u"T",
    "unit": u"h",
    "calculate": u"6",
    "remark": u"",
    "default_value": "6",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "t_daily_received_coal_amount",
    "name": u"日计算受煤量",
    "symbol": u"Qd",
    "unit": u"t/d",
    "calculate": u"单台",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "t_vehicle_daily_incoming_times",
    "name": u"每天进厂车次",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "t_vehicle_perhour_incoming_times",
    "name": u"每小时进场车次",
    "symbol": u"Ct",
    "unit": u"次/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_mutil_boiler_rated_coal_capacity",
    "name": u"多锅炉额定耗煤量",
    "symbol": u"Bzj",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_mutil_boiler_rated_coal_amount",
    "name": u"多锅炉日额定耗煤总量",
    "symbol": u"Bzj",
    "unit": u"t/h",
    "calculate": u"多锅炉额定耗煤量×小时",
    "remark": u"",
    "default_value": "22",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_transportsystem_output",
    "name": u"输煤系统选定出力",
    "symbol": u"Qxcl",
    "unit": u"t/h",
    "calculate": u"选取",
    "remark": u"",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_transportsystem_working_hours",
    "name": u"输煤系统运行小时",
    "symbol": u"t",
    "unit": u"h",
    "calculate": u"双路 三班",
    "remark": u"",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_shift_working_hours",
    "name": u"每班运行小时",
    "symbol": u"tn",
    "unit": u"h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_belt_width",
    "name": u"带宽",
    "symbol": u"B",
    "unit": u"--",
    "calculate": u"500/650/800 参考表10-9",
    "remark": u"",
    "default_value": "mm",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_section_coefficient",
    "name": u"断面系数",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"选取 参考表10.2.4",
    "remark": u"",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_belt_speed",
    "name": u"带速",
    "symbol": u"V",
    "unit": u"m/s",
    "calculate": u"1.25/1.6/2(参考表10.2.4)",
    "remark": u"",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_material_bulk_density",
    "name": u"物料松散密度",
    "symbol": u"p",
    "unit": u"t/m³",
    "calculate": u"0.8~1",
    "remark": u"",
    "default_value": "0.9",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "s_belt_max_transport_capacity",
    "name": u"皮带最大输送能力",
    "symbol": u"Q",
    "unit": u"t/h",
    "calculate": u"KBBvp",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "g_equipment_sets",
    "name": u"台数",
    "symbol": u"n",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "g_surplus",
    "name": u"富裕量",
    "symbol": u"k",
    "unit": u"%",
    "calculate": u"200%",
    "remark": u"",
    "default_value": "200",
    "disable": ""
}, {
    "module_name": "coalCHP_CoalHandingSystem",
    "name_eng": "g_single_coal_feeder_output",
    "name": u"单台给煤机出力",
    "symbol": u"Qgm",
    "unit": u"t/h",
    "calculate": u"Bj/n*k",
    "remark": "",
    "default_value": "",
    "disable": ""
}]

# 锅炉本体计算
furnaceCalculation_data = [{
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_carbon",
    "name": u"收到基碳含量",
    "symbol": u"Car",
    "unit": u"%",
    "calculate": "见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_hydrogen",
    "name": u"收到基氢含量",
    "symbol": u"Har",
    "unit": u"%",
    "calculate": "见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_oxygen",
    "name": u"收到基氧含量",
    "symbol": u"Oar",
    "unit": u"%",
    "calculate": "见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_nitrogen",
    "name": u"收到基氮含量",
    "symbol": u"Nar",
    "unit": u"%",
    "calculate": "见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_sulfur",
    "name": u"收到基硫含量",
    "symbol": u"Sar",
    "unit": u"%",
    "calculate": "见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_grey",
    "name": u"收到基灰分",
    "symbol": u"Aar",
    "unit": u"%",
    "calculate": "见需求调研表；一般＜10",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_water",
    "name": u"收到基水含量",
    "symbol": u"Mar",
    "unit": u"%",
    "calculate": "见需求调研表；设计燃料入炉条件≤30；校核燃料入炉条件≤40",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_sum",
    "name": u"总和",
    "symbol": u"100",
    "unit": u"%",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_daf",
    "name": u"干燥无灰基挥发分",
    "symbol": u"Vdaf",
    "unit": u"%",
    "calculate": " 无烟煤≤10；贫煤10~20;烟煤20~37；褐煤＞37",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_grindability",
    "name": u"哈氏可磨系数",
    "symbol": u"HGI",
    "unit": u"--",
    "calculate": "见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_low",
    "name": u"收到基低位发热量",
    "symbol": u"Qnet.Ar",
    "unit": u"Kj/kg",
    "calculate": "见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_low_1",
    "name": u"收到基低位发热量",
    "symbol": u"Qnet.Ar",
    "unit": u"Kcal/kg",
    "calculate": "KJ=4.1868*Kcal",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "s_low_estimation",
    "name":
    u"低位发热量估算",
    "symbol":
    u"Qnet.Ar",
    "unit":
    u"Kj/kg",
    "calculate":
    "Qnet.ar=339xCar+1030*Har-25xMar-109(Oar-Sar)",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    ""
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "s_high_estimation",
    "name":
    u"高位发热量估算",
    "symbol":
    u"Qar.gt",
    "unit":
    u"Kj/kg",
    "calculate":
    "Qnet.gt=339xCar+1256*Har-109(Oar-Sar)",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_steam_flow",
    "name": u"过热蒸汽流量",
    "symbol": u"Dgr",
    "unit": u"t/h",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_steam_pressure",
    "name": u"过热蒸汽出口压力",
    "symbol": u"Pgr",
    "unit": u"Mpa(g)",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_steam_temperature",
    "name": u"过热蒸汽温度",
    "symbol": u"Tgr",
    "unit": u"℃",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_steam_enthalpy",
    "name": u"过热蒸汽焓值",
    "symbol": u"Igr",
    "unit": u"Kj/kg",
    "calculate": u"查表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_boiler_pressure",
    "name": u"锅筒压力",
    "symbol": u"Dgr",
    "unit": u"Mpa(g)",
    "calculate": u"锅炉厂资料-----过热蒸汽压力*1.1",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_saturated_water_enthalpy",
    "name": u"汽包内饱和水焓值",
    "symbol": u"Ibs",
    "unit": u"Kj/kg",
    "calculate": u"查表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_water_temperature",
    "name": u"给水温度",
    "symbol": u"Tgs",
    "unit": u"℃",
    "calculate": u"158、104、215",
    "remark": "",
    "default_value": "158",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_water_enthalpy",
    "name": u"给水焓值",
    "symbol": u"Igs",
    "unit": u"Kj/kg",
    "calculate": u"查表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_boiler_efficiency",
    "name": u"锅炉效率",
    "symbol": u"ηg",
    "unit": u"%",
    "calculate": u" 锅炉厂资料",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_unburned_loss",
    "name": u"机械未燃烧损失",
    "symbol": u"q4",
    "unit": u"%",
    "calculate": u"锅炉厂资料；一般为0.5~2% 取3%",
    "remark": "",
    "default_value": "3",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_blowdown_rate",
    "name": u"锅炉排污率",
    "symbol": u"ηpw",
    "unit": u"%",
    "calculate": u"锅炉厂资料 取2%",
    "remark": "",
    "default_value": "2",
    "disable": ""
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "f_boiler_consumption",
    "name":
    u"锅炉燃料消耗量",
    "symbol":
    u"Bg",
    "unit":
    u"kg/h",
    "calculate":
    u"Dgr*1000*/ηg((Igr-Igs)+ηpw(ibs-igs))/Qnet.ar",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "f_calculation_consumption",
    "name": u"计算燃料消耗量",
    "symbol": u"Bj",
    "unit": u"kg/h",
    "calculate": u"Bg*(1-q4)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "d_total",
    "name":
    u"灰渣总量",
    "symbol":
    u"Gzhb",
    "unit":
    u"kg/h",
    "calculate":
    u"Bg(Aar/100+Qnet,ar*q4/3387000)   P209",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_boiler_total",
    "name": u"炉内喷钙灰渣总量",
    "symbol": u"G'zhb",
    "unit": u"kg/h",
    "calculate": u"生物质热电项目脱硫系统一般采用炉内喷钙工艺",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_ash_share",
    "name": u"飞灰份额",
    "symbol": u"k1",
    "unit": u"--",
    "calculate": u"CFB锅炉和ICFB锅炉取0.9；联合炉排炉和水冷振动炉排炉取0.6",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_dust_share",
    "name": u"底渣份额",
    "symbol": u"k2",
    "unit": u"--",
    "calculate": u"1-k1",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_ash_total",
    "name": u"灰量",
    "symbol": u"Gh",
    "unit": u"t/h",
    "calculate": u"Gznb*k1",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_dust_total",
    "name": u"渣量",
    "symbol": u"Gz",
    "unit": u"t/h",
    "calculate": u"Gznb*k2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "a_air_volumn",
    "name":
    u"理论干空气量",
    "symbol":
    u"Vo",
    "unit":
    u"Nm3/kg",
    "calculate":
    u"0.0889(Car+0.375St,ar)+0.265Har-0.0333Oar",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_hot_temperature",
    "name": u"最热月平均气温",
    "symbol": u"Trp",
    "unit": u"℃",
    "calculate": u"见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_humidity",
    "name": u"多年平均相对湿度",
    "symbol": u"φ",
    "unit": u"%",
    "calculate": u"见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_pressure",
    "name": u"多年平均气压",
    "symbol": u"Pb",
    "unit": u"kPa",
    "calculate": u"见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_temperature",
    "name": u"多年平均气温",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"见需求调研表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_saturation_pressure",
    "name": u"多年平均气温下的饱和压力",
    "symbol": u"Ps",
    "unit": u"kPa",
    "calculate": u"查水蒸汽表",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_steam_perssure",
    "name": u"水蒸气分压力",
    "symbol": u"Pv",
    "unit": u"kPa",
    "calculate": u"φ*Ps/100",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "a_air_humidity",
    "name":
    u"空气的绝对湿度(含湿量)",
    "symbol":
    u"d",
    "unit":
    u"g水/kg空气",
    "calculate":
    u"d=622*Pv/(Pb-Pv)，如无气象资料，可取d=10(经验值)",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_standard_air_humidity",
    "name": u"标况下湿空气密度",
    "symbol": u"ρao",
    "unit": u"kg/Nm3空气",
    "calculate": u"(1+0.001d)/(1/1.293+0.001d/0.804)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_wet_air_volumn",
    "name": u"理论湿空气量",
    "symbol": u"Vo'",
    "unit": u"Nm3/kg燃料",
    "calculate": u"(1+0.0016d)Vo",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_nitrogen_volume",
    "name": u"理论氮气容积",
    "symbol": u"V1N2",
    "unit": u"Nm3/kg",
    "calculate": u"0.79Vo+0.008*Nar",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_dioxide_volume",
    "name": u"理论二氧化物容积",
    "symbol": u"VoRO2",
    "unit": u"Nm3/kg",
    "calculate": u"1.866(Car+0.375Sar)/100",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "s_steam_volume",
    "name":
    u"理论水蒸汽容积",
    "symbol":
    u"VoH2O",
    "unit":
    u"Nm3/kg",
    "calculate":
    u"0.111Har+0.0124Mar+1.293*d*Vo/0.804/1000",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_smoke_volume",
    "name": u"理论烟气容积",
    "symbol": u"Vyo",
    "unit": u"Nm3/kg",
    "calculate": u"V1N2+VoRO2+VoH2O",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_1kg_weight",
    "name": u"1kg燃料生成理论湿烟气的重量",
    "symbol": u"Gyo",
    "unit": u"kg/kg燃料",
    "calculate": u"1-Aar/100+(1+d/1000)*1.293*α*Vo",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "s_wet_smoke_density",
    "name": u"标况下理论湿烟气密度",
    "symbol": u"ρyo",
    "unit": u"kg/Nm3",
    "calculate": u"Gyo/Vyo",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_boiler_air",
    "name": u"炉膛出口过剩空气系数",
    "symbol": u"αl",
    "unit": u"--",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "1.2",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_wind",
    "name": u"旋风分离器漏风系数",
    "symbol": u"ΔαfL",
    "unit": u"--",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "0.05",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_wind_air",
    "name": u"旋风分离器出口过剩空气系数",
    "symbol": u"αfL",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_high",
    "name": u"高过漏风系数",
    "symbol": u"Δαgr",
    "unit": u"--",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "0.05",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_hign_air",
    "name": u"高过出口过剩空气系数",
    "symbol": u"αgr",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_low",
    "name": u"低过漏风系数",
    "symbol": u"Δαdr",
    "unit": u"--",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "0",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_low_air",
    "name": u"低过出口过剩空气系数",
    "symbol": u"αdr",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_fule",
    "name": u"省燃料器漏风系数",
    "symbol": u"Δαsm",
    "unit": u"--",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "0.03",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_fule_air",
    "name": u"省燃料器出口过剩空气系数",
    "symbol": u"αsm",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_heater",
    "name": u"空预器漏风系数",
    "symbol": u"Δαky",
    "unit": u"--",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "0.03",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_heater_air",
    "name": u"空预器出口过剩空气系数",
    "symbol": u"αky",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_plus_air",
    "name": u"空予器至除尘器烟道漏风系数",
    "symbol": u"Δαcj",
    "unit": u"--",
    "calculate": u"L(烟道长度)*0.001",
    "remark": "",
    "default_value": "0.02",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_dust_exit",
    "name": u"除尘器进口过剩空气系数",
    "symbol": u"αcj",
    "unit": u"--",
    "calculate": u"αky+Δαcj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_dust",
    "name": u"除尘器漏风系数",
    "symbol": u"Δαcc",
    "unit": u"--",
    "calculate": u"厂家资料",
    "remark": "",
    "default_value": "0.02",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_dust_entry",
    "name": u"除尘器出口过剩空气系数",
    "symbol": u"αcc",
    "unit": u"--",
    "calculate": u"αcj+Δαcc",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_plus_dust",
    "name": u"除尘器出口至引风机烟道漏风系数",
    "symbol": u"Δαyd2",
    "unit": u"--",
    "calculate": u"L(烟道长度)*0.001",
    "remark": "",
    "default_value": "0.03",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_fans_air",
    "name": u"引风机入口过剩空气系数",
    "symbol": u"αxf",
    "unit": u"--",
    "calculate": u"αcc+Δαyd2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_1kg_volume",
    "name": u"1Kg燃料产生的空预器出口湿烟气容积",
    "symbol": u"Vy",
    "unit": u"Nm3/kg",
    "calculate": u"Vyo+(αky-1)Vo+0.0161(αky-1)Vo",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_1kg_quality",
    "name": u"1Kg燃料产生的空预器出口湿烟气质量",
    "symbol": u"Gy",
    "unit": u"kg/kg",
    "calculate": u"1-Aar/100+(1+d/1000)*1.293*αky*Vo",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_heater_type",
    "name": u"空预器",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "管式",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_heater_first_entry",
    "name": u"空预器一次风进口温度",
    "symbol": u"T'ky.p",
    "unit": u"℃",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_heater_second_entry",
    "name": u"空预器二次风进口温度",
    "symbol": u"T'ky.s",
    "unit": u"℃",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_heater_first_exit",
    "name": u"空预器一次风出口温度",
    "symbol": u"T'ky.p",
    "unit": u"℃",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "110",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_heater_second_exit",
    "name": u"空预器二次风出口温度",
    "symbol": u"T'ky.s",
    "unit": u"℃",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "140",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "p_smoke_temperature",
    "name": u"锅炉排烟温度",
    "symbol": u"T'y",
    "unit": u"℃",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "145",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_theory_air_quality",
    "name": u"理论空气量(体积,湿)",
    "symbol": u"Vo'",
    "unit": u"Nm3/kg燃料",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_boiler_air",
    "name": u"炉膛出口过剩空气系数",
    "symbol": u"αl",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_actual_air",
    "name": u"实际空气量(体积,湿)",
    "symbol": u"Voks",
    "unit": u"Nm3/kg",
    "calculate": u"αl*Vo'",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_calculation_consumption",
    "name": u"计算燃料消耗量",
    "symbol": u"Bj",
    "unit": u"kg/h",
    "calculate": u"燃料灰渣量计算表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_actual_air_total",
    "name": u"实际空气总量(体积，湿)",
    "symbol": u"Vok",
    "unit": u"Nm3/h",
    "calculate": u"Bj*Voks",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_first_wind_volume",
    "name": u"一次风份额",
    "symbol": u"β1",
    "unit": u"%",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_cwind_temperature_calculation",
    "name": u"冷风温度(计算温度)",
    "symbol": u"T'ky.p",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_local_pressure",
    "name": u"当地年平均气压",
    "symbol": u"Pb",
    "unit": u"kPa",
    "calculate": u"已知",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_first_cwind_standard",
    "name": u"冷一次风量(湿-标准态)",
    "symbol": u"VNLf 1",
    "unit": u"Nm3/h",
    "calculate": u"β1*Vok",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "a_first_cwind_actual",
    "name":
    u"冷一次风量(湿-实态)",
    "symbol":
    u"VLf 1",
    "unit":
    u"m3/h",
    "calculate":
    u"VNLf 1*(273+T ' ky.p)/273*101.325/Pb",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_first_standard_air_density",
    "name": u"标况下湿空气密度",
    "symbol": u"ρao",
    "unit": u"kg/Nm3",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_first_cwind_flow",
    "name": u"冷一次风量(质量流量)",
    "symbol": u"GLf 1",
    "unit": u"kg/h",
    "calculate": u"ρao*VNLf 1",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_first_cwind_density",
    "name": u"冷一次风湿空气密度(湿-实态)",
    "symbol": u"ρa1",
    "unit": u"kg/m3",
    "calculate": u"GLf 1/VLf 1",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "a_check",
    "name":
    u"校核",
    "symbol":
    u"ρa1",
    "unit":
    u"kg/m3",
    "calculate":
    u"ρao*273/(273+T'ky.p)*Pb/101.325(校核)",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_first_hwind_temperatue",
    "name": u"热一次风温度",
    "symbol": u"T'ky.p",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_first_hwind_flow",
    "name": u"热一次风量(湿-实态)",
    "symbol": u"VRf 1",
    "unit": u"m3/h",
    "calculate": u"VNLf 1*(273+T'ky.s)/273*101.325/Pb",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_first_wet_air_density",
    "name": u"湿空气密度(湿-实态)",
    "symbol": u"ρ'a1",
    "unit": u"kg/m3",
    "calculate": u"GLf 1/VRf 1",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_wind_volume",
    "name": u"二次风份额",
    "symbol": u"β2",
    "unit": u"%",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_cwind_temperature",
    "name": u"冷风温度",
    "symbol": u"T'ky.s",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_cwind_standard",
    "name": u"冷二次风量(湿-标准态)",
    "symbol": u"VNLf 2",
    "unit": u"Nm3/h",
    "calculate": u"β2*Vok",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_cwind_actual",
    "name": u"冷二次风量(湿-实态)",
    "symbol": u"VLf 2",
    "unit": u"m3/h",
    "calculate": u"VNLf 2*(273+T'ky.s)/273*101.325/Pb",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_standard_air_density",
    "name": u"标况下湿空气密度",
    "symbol": u"ρao",
    "unit": u"kg/Nm3",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_cwind_flow",
    "name": u"冷二次风量(质量流量)",
    "symbol": u"GLf 2",
    "unit": u"kg/h",
    "calculate": u"ρao*VNLf2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_cwind_density",
    "name": u"冷二次风湿空气密度(湿-实态)",
    "symbol": u"ρa2",
    "unit": u"kg/m3",
    "calculate": u"GLf2/VLf2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_hwind_temperatue",
    "name": u"热二次风温度",
    "symbol": u"T'ky.s",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_hwind_flow",
    "name": u"热二次风量(湿-实态)",
    "symbol": u"VRf 2",
    "unit": u"m3/h",
    "calculate": u"VNLf 2*(273+T'ky.s)/273*101.325/Pb",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "a_second_wet_air_density",
    "name": u"湿空气密度(湿-实态)",
    "symbol": u"ρ'a2",
    "unit": u"kg/m3",
    "calculate": u"GLf 2/VRf 2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "h_1kg_volume",
    "name": u"标况下空预器出口1Kg燃料湿烟气容积",
    "symbol": u"Vy",
    "unit": u"Nm3/kg",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "h_1kg_quality",
    "name": u"空预器出口1Kg燃料产生的湿烟气质量",
    "symbol": u"Gy",
    "unit": u"kg/kg",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "h_calculation_consumption",
    "name": u"计算燃料消耗量",
    "symbol": u"Bj",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "h_standard_smoke_flow",
    "name": u"标况下空预器出口烟气容积流量",
    "symbol": u"VNyk",
    "unit": u"Nm3/h",
    "calculate": u"Vy*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "h_smoke_flow",
    "name": u"空预器出口烟气质量流量",
    "symbol": u"Gyk",
    "unit": u"kg/h",
    "calculate": u"Gy*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "h_smoke_temperature",
    "name": u"锅炉空预器出口排烟温度",
    "symbol": u"T'y",
    "unit": u"℃",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "h_smoke_volume",
    "name": u"空预器出口烟气容积量(实态)",
    "symbol": u"Vyk",
    "unit": u"m3/h",
    "calculate": u"VNyk*(273+T'y)/273*101.325/Pb",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "h_smoke_density",
    "name": u"烟气密度(实态)",
    "symbol": u"ρyk",
    "unit": u"kg/m3",
    "calculate": u"Gyk/Vyk",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_exit_air",
    "name": u"空预器出口过剩空气系数",
    "symbol": u"αky",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_wind_parameter",
    "name": u"空预器至除尘器烟道漏风系数",
    "symbol": u"Δαcj",
    "unit": u"--",
    "calculate": u"L(烟道长度)*0.001",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_entry_air",
    "name": u"除尘器进口过剩空气系数",
    "symbol": u"αcj",
    "unit": u"--",
    "calculate": u"αky+Δαcj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_cold_air_temperature",
    "name": u"冷空气温度",
    "symbol": u"Tlk",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_entry_somke_temperature",
    "name": u"除尘器进口处烟气温度",
    "symbol": u"Tcj",
    "unit": u"℃",
    "calculate": u"(αkyT'y+△αcj*Tlk)/(αky+△αcj)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_standard_1kg_volume",
    "name": u"标况下除尘器进口处1kg燃料湿烟气容积",
    "symbol": u"V'ycj",
    "unit": u"Nm3/kg",
    "calculate": u"Vy+△αcj*VO'+0.0161*VO'",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_entry_1kg_quality",
    "name": u"除尘器进口处1kg燃料湿烟气质量",
    "symbol": u"G'ycj",
    "unit": u"kg/kg",
    "calculate": u"1-Aar/100+1.293*(1+d/1000)*αcj*Vo",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_standard_smoke_flow",
    "name": u"标况下除尘器进口烟气容积流量",
    "symbol": u"VNycj",
    "unit": u"Nm3/h",
    "calculate": u"V'ycj*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_entry_somke_flow",
    "name": u"除尘器进口处烟气质量流量",
    "symbol": u"Gycj",
    "unit": u"kg/h",
    "calculate": u"G'ycj*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "d_entry_smoke_actual_flow",
    "name": u"除尘器进口处烟气容积流量(实态)",
    "symbol": u"Vycj",
    "unit": u"m3/h",
    "calculate": u"VNycj*(273+Tcj)/273*101.325/Pb",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_wind_parameter",
    "name": u"除尘器漏风系数",
    "symbol": u"Δαcc",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_air_parameter",
    "name": u"除尘器出口过剩空气系数",
    "symbol": u"αcc",
    "unit": u"--",
    "calculate": u"αcj+△αcc",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_smoke_temperature",
    "name": u"除尘器出口烟气温度",
    "symbol": u"Tcc",
    "unit": u"℃",
    "calculate": u"湿法脱硫，给定",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_standard_1kg_volume",
    "name": u"标况下除尘器出口处1kg燃料湿烟气容积",
    "symbol": u"V'ycc",
    "unit": u"Nm3/kg",
    "calculate": u"V'ycj+△αcc*VO'+0.0161*△αcc*VO'",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_1kg_quality",
    "name": u"除尘器出口处1kg燃料湿烟气质量",
    "symbol": u"G'ycc",
    "unit": u"kg/kg",
    "calculate": u"1-Aar/100+1.293*(1+d/1000)*αcc*Vo",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_standard_smoke_flow",
    "name": u"标况下除尘器出口湿烟气容积流量",
    "symbol": u"VNycc",
    "unit": u"Nm3/h",
    "calculate": u"V'ycc*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_smoke_flow",
    "name": u"除尘器出口处湿烟气质量流量",
    "symbol": u"Gycc",
    "unit": u"kg/h",
    "calculate": u"G'ycc*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_smoke_actual_flow",
    "name": u"除尘器出口处湿烟气容积流量(实态)",
    "symbol": u"Vycc",
    "unit": u"m3/h",
    "calculate": u"VNycc*(273+Tcc)/273*101.325/Pb",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "e_smoke_actual_density",
    "name": u"烟气密度(实态)",
    "symbol": u"ρycc",
    "unit": u"kg/m3",
    "calculate": u"Gycc/Vycc",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_wind_parameter",
    "name": u"除尘器出口至引风机烟道漏风系数",
    "symbol": u"Δαxj",
    "unit": u"--",
    "calculate": u"L(烟道长度)*0.001",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_air_parameter",
    "name": u"引风机入口过剩空气系数",
    "symbol": u"αxf",
    "unit": u"--",
    "calculate": u"αcc+Δαxj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_smoke_temperature",
    "name": u"引风机入口烟气温度",
    "symbol": u"Txf",
    "unit": u"℃",
    "calculate": u"(αcc*Tcc+△αxj*Tlk)/(αcc+△αxj)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_standard_1kg_volume",
    "name": u"标况下引风机进口处1kg燃料湿烟气容积",
    "symbol": u"V'xf",
    "unit": u"Nm3/kg",
    "calculate": u"V'ycc+△αxj*Vo'+0.0161*△αxj*Vo'",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_1kg_quality",
    "name": u"引风机进口处1kg燃料湿烟气质量",
    "symbol": u"G'xf",
    "unit": u"kg/kg",
    "calculate": u"1-Aar/100+1.293*(1+d/1000)*αxf*Vo",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_standard_smoke_flow1",
    "name": u"标况下引风机进口湿烟气容积流量",
    "symbol": u"VNxf",
    "unit": u"Nm3/h",
    "calculate": u"V'xf*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_standard_smoke_flow2",
    "name": u"标况下引风机进口湿烟气容积流量",
    "symbol": u"",
    "unit": u"Nm3/s",
    "calculate": u"V'xf*Bj/3600",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_smoke_flow",
    "name": u"引风机进口处湿烟气质量流量",
    "symbol": u"Gxf",
    "unit": u"kg/h",
    "calculate": u"G'xf*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_smoke_actual_flow1",
    "name": u"引风机进口处湿烟气容积流量(实态)",
    "symbol": u"Vxf",
    "unit": u"m3/h",
    "calculate": u"VNxf*(273+Txf)/273*101.325/Pb",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_smoke_actual_flow2",
    "name": u"引风机进口处湿烟气容积流量(实态)",
    "symbol": u"Vxfc",
    "unit": u"m3/s",
    "calculate": u"Vxf/3600",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_smoke_actual_density",
    "name": u"烟气密度(实态)",
    "symbol": u"ρyxf",
    "unit": u"kg/m3",
    "calculate": u"Gyxf/Vyxf",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "i_wet_smoke_actual_density",
    "name": u"引风机处计算湿烟气密度(标况)",
    "symbol": u"ρyo",
    "unit": u"kg/Nm3",
    "calculate": u"Gxf/VNxf",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "go_oxygen_vol",
    "name": u"烟气中的氧量",
    "symbol": u"VO2'",
    "unit": u"Nm3/kg燃料",
    "calculate": u"0.21(axf-1)V0",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "go_theoretica_vol",
    "name": u"理论干烟气容积",
    "symbol": u"Vgyo",
    "unit": u"Nm3/kg燃料",
    "calculate": u"VoN2+VoRO2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "coalCHP_furnaceCalculation",
    "name_eng":
    "go_theoretica_flow",
    "name":
    u"理论干空气量",
    "symbol":
    u"Vo",
    "unit":
    u"Nm3/kg燃料",
    "calculate":
    u"0.0889(Car+0.375St,ar)+0.265Har-0.0333Oar",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "go_calculation_consumption",
    "name": u"计算燃料消耗量",
    "symbol": u"Bj",
    "unit": u"kg/h",
    "calculate": u"燃料灰渣量计算表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "go_air_parameter",
    "name": u"引风机入口过剩空气系数",
    "symbol": u"αxf",
    "unit": u"--",
    "calculate": u"αcc+Δαxj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "go_standard_1kg_volume",
    "name": u"1Kg燃料产生的引风机进口干烟气容积",
    "symbol": u"V'gy",
    "unit": u"Nm3/kg燃料",
    "calculate": u"Vgyo+(axf-1)V0",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "go_smoke_flow",
    "name": u"引风机进口干烟气容积流量",
    "symbol": u"Vgy",
    "unit": u"Nm3/h",
    "calculate": u"V'gy*Bj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "go_drygas_oxygen_vol",
    "name": u"干烟气中含氧量",
    "symbol": u"ngo2",
    "unit": u"%",
    "calculate": u"VO2'/Vgy'",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_furnaceCalculation",
    "name_eng": "go_total_combustion_product_vol",
    "name": u"总燃烧产物6%O2干体积",
    "symbol": u"Vgy-O2",
    "unit": u"Nm3/h",
    "calculate": u"Vgy*(21-ngo2')/(21-6)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}]

# 脱硫脱硝
coalCHP_desulfurization_data = [{
    "module_name": "coalCHP_desulfurization",
    "name_eng": "s_sulfur_design",
    "name": u"收到基硫份",
    "symbol": u"St,ar",
    "unit": u"%",
    "calculate": u"已知",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "s_calcu_coal_consume",
    "name": u"计算耗煤量",
    "symbol": u"Bj",
    "unit": u"kg/h",
    "calculate": u"煤灰渣量计算表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "s_aflame_generate_so2",
    "name": u"燃煤中的含硫量燃烧后氧化成SO2的份额",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"0.98",
    "remark": "",
    "default_value": "0.98",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "s_desulfrization_before_so2",
    "name": u"脱硫前烟气中的SO2含量",
    "symbol": u"Mso2",
    "unit": u"kg/h",
    "calculate": u"2*K*Bj*St,ar/100",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "s_fan_smoke_flow",
    "name": u"引风机进口烟气容积流量(标况)",
    "symbol": u"VNxf",
    "unit": u"Nm3/h",
    "calculate": u"烟风量计算表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "s_no_desulfurization_so2",
    "name": u"未脱硫前SO2浓度(标态)",
    "symbol": u"C'SO2",
    "unit": u"mg/Nm3",
    "calculate": u"Mso2/VNxf*106",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "s_desulfurization_efficiency",
    "name": u"脱硫效率",
    "symbol": u"η",
    "unit": u"%",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "s_desulfrization_after_so2",
    "name": u"脱硫后SO2浓度(标态)",
    "symbol": u"CSO2",
    "unit": u"mg/Nm3",
    "calculate": u"(1-η)C'SO2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "coalCHP_desulfurization",
    "name_eng":
    "s_desulfrization_after_discharge_so2",
    "name":
    u"脱硫后SO2排放量(标态)",
    "symbol":
    u"",
    "unit":
    u"kg/h",
    "calculate":
    u"(1-η)MSO2 或 CSO2*VNxf",
    "remark":
    "",
    "default_value":
    "96",
    "disable":
    "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_furnace_rate",
    "name": u"炉内脱硫百分比",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"给定",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_furnace_concentration",
    "name": u"炉内脱硫后SO2浓度",
    "symbol": u"CSO2(炉内)",
    "unit": u"mg/Nm3",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_others_mass",
    "name": u"脱除SO2质量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_others_mole",
    "name": u"脱除SO2摩尔量",
    "symbol": u"",
    "unit": u"kmol/h",
    "calculate": u"SO2式量64",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_calcium_sulfur_rate",
    "name": u"钙硫摩尔比",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"钙硫比≥2，一般选2",
    "remark": "",
    "default_value": "2",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_nees_caco3_mole",
    "name": u"反应所需CaCO3摩尔量",
    "symbol": u"",
    "unit": u"kmol/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_nees_caco3_mass",
    "name": u"反应所需CaCO3质量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"CaCO3式量100",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_use_caco3_mass",
    "name": u"参加反应CaCO3质量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_generate_coco3_mass",
    "name": u"反应生成CaSO4质量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"CaCO3-〉CaSO4",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_add_mass",
    "name": u"反应后质量增加",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_caco3_pure",
    "name": u"石灰石纯度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": "",
    "default_value": "85",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_coco3_consume",
    "name": u"石灰石耗量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"公式修改",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_generate_grey",
    "name": u"炉内脱硫产生的灰渣量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_storage_time",
    "name": u"石灰石粉仓储存时间",
    "symbol": u"",
    "unit": u"d",
    "calculate": u"3d",
    "remark": "",
    "default_value": "3",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_storage_output",
    "name": u"石灰石粉仓出力",
    "symbol": u"",
    "unit": u"kg",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_storage_density",
    "name": u"石灰石粉堆积密度",
    "symbol": u"Pa",
    "unit": u"t/m³",
    "calculate": u"0.7~0.8",
    "remark": "",
    "default_value": "0.8",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_storage_fullness",
    "name": u"石灰石粉库充满系数",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"0.7~0.8",
    "remark": "",
    "default_value": "0.8",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_storage_volume",
    "name": u"石灰石粉仓体积",
    "symbol": u"V",
    "unit": u"m³",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_height",
    "name": u"高",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "r_diameter",
    "name": u"直径",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_limestone_pure",
    "name": u"石灰石纯度",
    "symbol": u"β",
    "unit": u"--",
    "calculate": u"可根据石灰石成分计算",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_proportion_ca_s",
    "name": u"Ca/S(钙硫比)",
    "symbol": u"m",
    "unit": u"--",
    "calculate": u"1.05",
    "remark": "",
    "default_value": "1.05",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_desulfurization_efficiency",
    "name": u"脱硫效率",
    "symbol": u"η",
    "unit": u"%",
    "calculate": u"99.5",
    "remark": "",
    "default_value": "99.5",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_limestone_consume",
    "name": u"石灰石消耗量",
    "symbol": u"Gs",
    "unit": u"kg/h",
    "calculate": u"100/32*St,ar*Bj*η*m/β",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_gengrate_coca4",
    "name": u"生成CaSO4量",
    "symbol": u"Gzhs",
    "unit": u"kg/h",
    "calculate": u"136/32*St,ar*Bj*η*m/β",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "n_before_nox_concentration",
    "name": u"脱硝前NOX浓度",
    "symbol": u"C'NOX",
    "unit": u"mg/Nm3",
    "calculate": u"给定(锅炉低氮燃烧规定值)",
    "remark": "",
    "default_value": "280",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "n_input_smoke",
    "name": u"引风机进口烟气容积流量(标况)",
    "symbol": u"VNxf",
    "unit": u"Nm3/h",
    "calculate": u"烟风量计算表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "n_desulfurization_efficiency",
    "name": u"脱硝效率(总效率)",
    "symbol": u"η",
    "unit": u"%",
    "calculate": u"给定",
    "remark": "",
    "default_value": "80",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "n_before_nox_discharge",
    "name": u"脱硝前NOX排放量",
    "symbol": u"MNOX",
    "unit": u"kg/h",
    "calculate": u"C'NOX*VNxf*10-6",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "n_after_nox_concentration",
    "name": u"脱硝后NOX浓度",
    "symbol": u"CNOX",
    "unit": u"mg/Nm3",
    "calculate": u"(1-η)C'NOX",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "n_env_after_nox_concentration",
    "name": u"环保要求NOX的排放浓度",
    "symbol": u"C'NOX",
    "unit": u"mg/Nm3",
    "calculate": u"已知",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "n_after_nox_discharge",
    "name": u"脱硝后NOX排放量",
    "symbol": u"M'NOX",
    "unit": u"kg/h",
    "calculate": u"(1-η)MNOX",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_denitration_percentage",
    "name": u"炉内脱硝百分比",
    "symbol": u"η'",
    "unit": u"%",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_denitration_quality",
    "name": u"炉内脱硝量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"(Mnox-M'nox)*η'",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_after_nox_discharge",
    "name": u"炉内脱硝后NOX排放量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_denitration_molar",
    "name": u"炉内脱硝摩尔量",
    "symbol": u"",
    "unit": u"kmol/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_escape_rate",
    "name": u"氨逃逸率",
    "symbol": u"",
    "unit": u"mg/Nm3",
    "calculate": u"取8",
    "remark": "",
    "default_value": "8",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_escape_quality",
    "name": u"氨逃逸量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_escape_quality_urea",
    "name": u"逃逸氨折算尿素量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"(NH2 )2CO→2NH2 + CO",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_nh3nox_molar",
    "name": u"NH3/NOX摩尔比",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"0.8",
    "remark": "",
    "default_value": "0.8",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_urea_nox_molar",
    "name": u"尿素/NOX摩尔比",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"NH3/NOX摩尔比/2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_urea_nox_quality",
    "name": u"尿素/NOX式量比",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"1",
    "remark": "",
    "default_value": "1",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_theory_urea",
    "name": u"理论尿素消耗量",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_use_urea",
    "name": u"尿素用量(一台炉)",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"理论尿素消耗量+逃逸氨折算尿素量",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_water_urea",
    "name": u"尿素溶液消耗水量(一台炉)",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_days_urea",
    "name": u"尿素仓库天数",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"取5d",
    "remark": "",
    "default_value": "5",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "d_capacity_urea",
    "name": u"尿素仓库容量",
    "symbol": u"",
    "unit": u"t",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_denitration_percentage",
    "name": u"烟气脱硝百分比",
    "symbol": u"η'",
    "unit": u"%",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_after_nox_discharge",
    "name": u"烟气脱硝后NOX排放量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_denitration_quality",
    "name": u"烟气脱硝量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_escape_rate",
    "name": u"氨逃逸率",
    "symbol": u"",
    "unit": u"ppm",
    "calculate": u"取3",
    "remark": "",
    "default_value": "3",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_escape_quality",
    "name": u"氨逃逸量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_escape_quality_urea",
    "name": u"逃逸氨折算尿素量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"(NH2 )2CO→2NH2 + CO",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_nh3nox_molar",
    "name": u"NH3/NOX摩尔比",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"已知，取1",
    "remark": "",
    "default_value": "1",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_urea_nox_molar",
    "name": u"尿素/NOX摩尔比",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"NH3/NOX摩尔比/2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_urea_nox_quality",
    "name": u"尿素/NOX式量比",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"已知，取1",
    "remark": "",
    "default_value": "1",
    "disable": ""
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_theory_urea",
    "name": u"理论尿素消耗量",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_desulfurization",
    "name_eng": "g_use_urea",
    "name": u"尿素用量(一台炉)",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"理论尿素消耗量+逃逸氨折算尿素量",
    "remark": "",
    "default_value": "",
    "disable": "T"
}]

# 烟风系统
smokeAirSystem_data = [{
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "a_altitude",
    "name": u"海拔",
    "symbol": u"A",
    "unit": u"m",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "a_atmospheric_pressure",
    "name": u"大气压",
    "symbol": u"P",
    "unit": u"pa",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "p_the_case_temperature",
    "name": u"标况温度",
    "symbol": u"t0",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "0",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "p_standard_of_pressure",
    "name": u"标况压力",
    "symbol": u"p0",
    "unit": u"pa",
    "calculate": u"",
    "remark": "",
    "default_value": "101325",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "p_standard_of_flow",
    "name": u"标况流量",
    "symbol": u"qv0",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "p_temperature_case",
    "name": u"工况温度",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "p_local_atmosphere",
    "name": u"当地大气压",
    "symbol": u"p",
    "unit": u"pa",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "p_operational_point_flow",
    "name": u"工况流量",
    "symbol": u"qv",
    "unit": u"m³/h",
    "calculate": u"qv=qv0*(p0/p)*((t+273)/(t0+273))",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_air_temperature",
    "name": u"空气温度",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"设计值",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_boiler_body_resistance",
    "name": u"锅炉本体阻力",
    "symbol": u"pg",
    "unit": u"pa",
    "calculate": u"是否海拔修正",
    "remark": "",
    "default_value": "7500",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_duct_resistance",
    "name": u"风道阻力",
    "symbol": u"py",
    "unit": u"pa",
    "calculate": u"大气压未修正",
    "remark": "",
    "default_value": "1500",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_local_atmosphere",
    "name": u"当地大气压",
    "symbol": u"p0",
    "unit": u"pa",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_smoke_flow_rate_condition",
    "name": u"烟风流量",
    "symbol": u"q",
    "unit": u"m³/h",
    "calculate": u"50:50时   1.1倍",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_nameplate_medium_temperature",
    "name": u"铭牌介质温度",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"常规20℃",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_fan_total_pressure",
    "name": u"风机全压",
    "symbol": u"p1",
    "unit": u"pa",
    "calculate": u"p1=p*(101325/p0)*((t+273)/(t1+273))",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_fan_select_total_pressure",
    "name": u"风机选用全压",
    "symbol": u"p2",
    "unit": u"--",
    "calculate": u"1.2",
    "remark": "",
    "default_value": "1.2",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_fan_selection_flow",
    "name": u"风机选用流量",
    "symbol": u"q2",
    "unit": u"m³/h",
    "calculate": u"1.3",
    "remark": "",
    "default_value": "1.3",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_fan_power",
    "name": u"风机效率",
    "symbol": u"η1",
    "unit": u"--",
    "calculate": u"取0.75",
    "remark": "",
    "default_value": "0.75",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_electric_motor_power",
    "name": u"电动机效率",
    "symbol": u"ηd",
    "unit": u"--",
    "calculate": u"取0.95",
    "remark": "",
    "default_value": "0.95",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_fan_shaft_power",
    "name": u"风机轴功率",
    "symbol": u"P'",
    "unit": u"kw",
    "calculate": u"P'=p2*q2/η",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_fan_security_volumn",
    "name": u"电机安全裕量",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"取1.1",
    "remark": "",
    "default_value": "1.1",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_motor_power",
    "name": u"电机功率",
    "symbol": u"P",
    "unit": u"kw",
    "calculate": u"P=K*P'/ηd",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "f_lectotype",
    "name": u"选型",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_air_temperature",
    "name": u"空气温度",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"设计值",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_boiler_body_resistance",
    "name": u"锅炉本体阻力",
    "symbol": u"pg",
    "unit": u"pa",
    "calculate": u"是否海拔修正",
    "remark": "",
    "default_value": "5500",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_duct_resistance",
    "name": u"风道阻力",
    "symbol": u"py",
    "unit": u"pa",
    "calculate": u"大气压未修正",
    "remark": "",
    "default_value": "1500",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_local_atmosphere",
    "name": u"当地大气压",
    "symbol": u"p0",
    "unit": u"pa",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_smoke_flow_rate_condition",
    "name": u"烟风流量",
    "symbol": u"q",
    "unit": u"m³/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_nameplate_medium_temperature",
    "name": u"铭牌介质温度",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"常规20℃",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_fan_total_pressure",
    "name": u"风机全压",
    "symbol": u"p1",
    "unit": u"pa",
    "calculate": u"p1=p*(101325/p0)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_fan_select_total_pressure",
    "name": u"风机选用全压",
    "symbol": u"p2",
    "unit": u"--",
    "calculate": u"1.2",
    "remark": "",
    "default_value": "1.2",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_fan_selection_flow",
    "name": u"风机选用流量",
    "symbol": u"q2",
    "unit": u"m³/h",
    "calculate": u"1.3",
    "remark": "",
    "default_value": "1.3",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_fan_power",
    "name": u"风机效率",
    "symbol": u"η1",
    "unit": u"--",
    "calculate": u"取0.75",
    "remark": "",
    "default_value": "0.75",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_electric_motor_power",
    "name": u"电动机效率",
    "symbol": u"ηd",
    "unit": u"--",
    "calculate": u"取0.95",
    "remark": "",
    "default_value": "0.95",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_fan_shaft_power",
    "name": u"风机轴功率",
    "symbol": u"P'",
    "unit": u"kw",
    "calculate": u"P'=p2*q2/η",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_fan_security_volumn",
    "name": u"电机安全裕量",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"取1.1",
    "remark": "",
    "default_value": "1.1",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_motor_power",
    "name": u"电机功率",
    "symbol": u"P",
    "unit": u"kw",
    "calculate": u"P=K*P'/ηd",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "s_lectotype",
    "name": u"选型",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_air_temperature",
    "name": u"烟气温度",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"设计值",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_boiler_body_resistance",
    "name": u"锅炉本体烟气阻力",
    "symbol": u"pg",
    "unit": u"pa",
    "calculate": u"是否海拔修正",
    "remark": "",
    "default_value": "2480",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_denitration",
    "name": u"脱硝",
    "symbol": u"pn",
    "unit": u"pa",
    "calculate": u"大气压未修正",
    "remark": "",
    "default_value": "600",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_duster",
    "name": u"除尘器",
    "symbol": u"pc",
    "unit": u"Pa",
    "calculate": u"大气压未修正",
    "remark": "",
    "default_value": "1200",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_duct_resistance",
    "name": u"风道阻力",
    "symbol": u"py",
    "unit": u"pa",
    "calculate": u"大气压未修正",
    "remark": "",
    "default_value": "500",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_resistance_desulfurization_fan",
    "name": u"风机后脱硫塔及烟囱烟道阻力",
    "symbol": u"ph",
    "unit": u"pa",
    "calculate": u"大气压未修正",
    "remark": "",
    "default_value": "3000",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_local_atmosphere",
    "name": u"当地大气压",
    "symbol": u"p0",
    "unit": u"pa",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_smoke_flow_rate_condition",
    "name": u"烟风流量",
    "symbol": u"q",
    "unit": u"m³/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_nameplate_medium_temperature",
    "name": u"铭牌介质温度",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"常规250℃",
    "remark": "",
    "default_value": "250",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_fan_total_pressure",
    "name": u"风机全压",
    "symbol": u"p1",
    "unit": u"pa",
    "calculate": u"p1=p*(101325/p0)*((t+273)/(t1+273))",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_fan_select_total_pressure",
    "name": u"风机选用全压",
    "symbol": u"p2",
    "unit": u"--",
    "calculate": u"1.2",
    "remark": "",
    "default_value": "1.2",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_fan_selection_flow",
    "name": u"风机选用流量",
    "symbol": u"q2",
    "unit": u"m³/h",
    "calculate": u"1.1",
    "remark": "",
    "default_value": "1.1",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_fan_power",
    "name": u"风机效率",
    "symbol": u"η1",
    "unit": u"--",
    "calculate": u"取0.75",
    "remark": "",
    "default_value": "0.75",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_electric_motor_power",
    "name": u"电动机效率",
    "symbol": u"ηd",
    "unit": u"--",
    "calculate": u"取0.95",
    "remark": "",
    "default_value": "0.95",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_fan_shaft_power",
    "name": u"风机轴功率",
    "symbol": u"P'",
    "unit": u"kw",
    "calculate": u"P'=p2*q2/η",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_fan_security_volumn",
    "name": u"电机安全裕量",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"取1.1",
    "remark": "",
    "default_value": "1.1",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_motor_power",
    "name": u"电机功率",
    "symbol": u"P",
    "unit": u"kw",
    "calculate": u"P=K*P'/ηd",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "i_lectotype",
    "name": u"选型",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_air_temperature",
    "name": u"空气温度",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"常规20",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_boiler_body_resistance",
    "name": u"风压",
    "symbol": u"pg",
    "unit": u"pa",
    "calculate": u"锅炉厂资料",
    "remark": "",
    "default_value": "25000",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_duct_resistance",
    "name": u"管道阻力",
    "symbol": u"pz",
    "unit": u"pa",
    "calculate": u"",
    "remark": "",
    "default_value": "500",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_local_atmosphere",
    "name": u"当地大气压",
    "symbol": u"p0",
    "unit": u"pa",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_smoke_flow_rate_condition",
    "name": u"烟风流量",
    "symbol": u"q",
    "unit": u"m³/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_nameplate_medium_temperature",
    "name": u"铭牌介质温度",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"常规20℃",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_fan_total_pressure",
    "name": u"风机全压",
    "symbol": u"p1",
    "unit": u"pa",
    "calculate": u"p1=p*(101325/p0)*((t+273)/(t1+273))",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_fan_select_total_pressure",
    "name": u"风机选用全压",
    "symbol": u"p2",
    "unit": u"--",
    "calculate": u"1.1",
    "remark": "",
    "default_value": "1.1",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_fan_selection_flow",
    "name": u"风机选用流量",
    "symbol": u"q2",
    "unit": u"m³/h",
    "calculate": u"1.3",
    "remark": "",
    "default_value": "1.3",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_fan_power",
    "name": u"风机效率",
    "symbol": u"η1",
    "unit": u"--",
    "calculate": u"取0.75",
    "remark": "",
    "default_value": "0.75",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_electric_motor_power",
    "name": u"电动机效率",
    "symbol": u"ηd",
    "unit": u"--",
    "calculate": u"取0.95",
    "remark": "",
    "default_value": "0.95",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_fan_shaft_power",
    "name": u"风机轴功率",
    "symbol": u"P'",
    "unit": u"kw",
    "calculate": u"P'=p2*q2/η",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_fan_security_volumn",
    "name": u"电机安全裕量",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"取1.1",
    "remark": "",
    "default_value": "1.1",
    "disable": ""
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_motor_power",
    "name": u"电机功率",
    "symbol": u"P",
    "unit": u"kw",
    "calculate": u"P=K*P'/ηd",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_smokeAirSystem",
    "name_eng": "r_lectotype",
    "name": u"选型",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}]

# 循环水
circulatingWater_data = [{
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_steam_exhaust_flow",
    "name": u"乏汽流量",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_steam_exhaust_flow_select",
    "name": u"乏汽流量选定",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"选定",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_circulating_ratio",
    "name": u"循环倍率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"北方60~70；中部65~75；南方70~80",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_circulating_water",
    "name": u"循环水量",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_auxiliary_engine_cooling_winter",
    "name": u"辅机冷却水量",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"一般取200、350、550",
    "remark": "",
    "default_value": "550",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_total_circulating_water",
    "name": u"总循环水量",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_total_circulating_water_select",
    "name": u"总循环水量选定",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"选定",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name":
    "coalCHP_circulatingWater",
    "name_eng":
    "v_enter_the_outlet_temperature_difference",
    "name":
    u"进、出水口温差",
    "symbol":
    u"",
    "unit":
    u"℃",
    "calculate":
    u"一般取8~12℃",
    "remark":
    "",
    "default_value":
    "10",
    "disable":
    ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_dry_bulb_temperature",
    "name": u"干球温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_up_dry_bulb_temperature",
    "name": u"上区间干球温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "30",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_down_dry_bulb_temperature",
    "name": u"下区间干球温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_up_k",
    "name": u"上区间K",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "0.15",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_down_k",
    "name": u"下区间K",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "0.14",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_k",
    "name": u"K",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_evaporation_loss_rate",
    "name": u"蒸发损失率",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"Pe=K*温差",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_evaporation_loss",
    "name": u"蒸发损失",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"Qe=Pe*Q/100",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_blowing_loss_rate",
    "name": u"风吹损失率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"Pw：有除水器时为0.2%-0.3%；无除水器时≥0.5%",
    "remark": "",
    "default_value": "0.3",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_partial_blow_loss",
    "name": u"风吹损失",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_concentrate_ratio",
    "name": u"浓缩倍率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"C：一般取3",
    "remark": "",
    "default_value": "3",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_discharge_loss",
    "name": u"排污损失率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"Pb=（Pe-Pw（c-1））/（c-1）",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_discharge_capacity",
    "name": u"排污量",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_amount_of_makeup_water",
    "name": u"补充水量",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_circulating_pool_size",
    "name": u"循环水池尺寸",
    "symbol": u"",
    "unit": u"m3",
    "calculate": u"15-25分钟循环水量",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_circulating_pool_long",
    "name": u"循环水池深",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"深",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_circulating_pool_wide",
    "name": u"循环水池长",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"长",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_circulating_pool_hight",
    "name": u"循环水池宽",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"宽",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "v_check_circulating_pool_size",
    "name": u"校核循环水池尺寸",
    "symbol": u"",
    "unit": u"m3",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "p_spray_density",
    "name": u"喷淋密度",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"一般为6~7，取7",
    "remark": "",
    "default_value": "7",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "p_spray_area",
    "name": u"喉部喷淋面积",
    "symbol": u"",
    "unit": u"m2",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "p_select_f",
    "name": u"选型",
    "symbol": u"",
    "unit": u"m2",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "p_count",
    "name": u"数量",
    "symbol": u"",
    "unit": u"台",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "p_single_cold_amount",
    "name": u"单台冷却水量",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "p_select_s",
    "name": u"选型",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_condenser_tube_friction",
    "name": u"凝汽器阻力",
    "symbol": u"",
    "unit": u"Mpa",
    "calculate": u"厂家提供",
    "remark": "",
    "default_value": "0.034",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_circulating_water_pressure",
    "name": u"循环水回水压力",
    "symbol": u"",
    "unit": u"Mpa",
    "calculate": u"",
    "remark": "",
    "default_value": "0.18",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_pressure_condenser",
    "name": u"凝汽器循环水进水工作压力",
    "symbol": u"",
    "unit": u"Mpa",
    "calculate": u"输入",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_circulating_pool_pressure",
    "name": u"循环水吸水池压力",
    "symbol": u"",
    "unit": u"Mpa",
    "calculate": u"输入",
    "remark": "",
    "default_value": "0.1",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_circulation_height_difference",
    "name": u"循环水泵出口与凝汽器循环水进水口高度差",
    "symbol": u"",
    "unit": u"M",
    "calculate": u"输入",
    "remark": "",
    "default_value": "4",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_height_difference_inlet",
    "name": u"吸水池与水泵入口高度差",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"",
    "remark": "",
    "default_value": "-2.5",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_pipe_losses",
    "name": u"管道损失",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"暂定采用5mH2O",
    "remark": "",
    "default_value": "4",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_y_losses",
    "name": u"Y型过滤器损失",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"厂家提供",
    "remark": "",
    "default_value": "5",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_pumping_head",
    "name": u"总扬程",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"102*（P1-P2）+(H1-H2)+1.2*(H3+H4)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_flow",
    "name": u"流量",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_pump_power",
    "name": u"泵效率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"0.6~0.85",
    "remark": "",
    "default_value": "0.6",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_mechine_power",
    "name": u"机械传动效率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"直连1.0，联轴器0.98，皮带0.95",
    "remark": "",
    "default_value": "0.98",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_motor_power",
    "name": u"电动机效率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"通常取0.98",
    "remark": "",
    "default_value": "0.98",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_motor_backup_coefficient",
    "name": u"电动机备用系数",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"查表选取",
    "remark": "",
    "default_value": "1.1",
    "disable": ""
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_supporting_motor_power",
    "name": u"配套电机功率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_forklift_parameters_power",
    "name": u"功率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"两用一备",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_forklift_parameters_flow",
    "name": u"流量",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_circulatingWater",
    "name_eng": "c_forklift_parameters_lift",
    "name": u"扬程",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}]

removalAshSlag_data = [{
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_total_ash_residue_after",
    "name": u"灰渣总量(炉内脱硫后)",
    "symbol": u"",
    "unit": u"kg/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_fly_ash_content",
    "name": u"飞灰份额",
    "symbol": u"αf",
    "unit": u"%",
    "calculate": u"循化流化床一般飞灰比6：4，7：3",
    "remark": "",
    "default_value": "0.6",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_dust_collector_inlet_",
    "name": u"除尘器入口(锅炉出口)飞灰量",
    "symbol": u"Gaf",
    "unit": u"kg/h",
    "calculate": u"αf*Gzh",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_the_imported_smoke_volume",
    "name": u"标况下除尘器进口烟气容积流量",
    "symbol": u"VNycj",
    "unit": u"Nm3/h",
    "calculate": u"烟风量计算表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_the_smoke_volume_flow",
    "name": u"除尘器进口处烟气容积流量(实态)",
    "symbol": u"Vycj",
    "unit": u"m3/h",
    "calculate": u"烟风量计算表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_the_smoke_concentration",
    "name": u"标况下除尘器进口烟气浓度",
    "symbol": u"Ci",
    "unit": u"mg/Nm3",
    "calculate": u"Gaf*106/VNycj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_the_smoke_concentration_solid",
    "name": u"除尘器进口处烟气浓度(实态)",
    "symbol": u"C'i",
    "unit": u"mg/m3",
    "calculate": u"Gaf*106/Vycj",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_collection_efficiency",
    "name": u"除尘效率",
    "symbol": u"ηc",
    "unit": u"%",
    "calculate": u"电布袋除尘器，取99.8",
    "remark": "",
    "default_value": "99.8",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_the_smoke_concentration_chimney",
    "name": u"除尘器(烟囱)出口烟气浓度(标况)",
    "symbol": u"Co",
    "unit": u"mg/Nm3",
    "calculate": u"Ci*(1-ηc)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_dust_collector_stack",
    "name": u"除尘器(烟囱)出口烟气飞灰量(标况)",
    "symbol": u"G'af",
    "unit": u"kg/h",
    "calculate": u"Gaf*(1-ηc)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_ash_under_dust_collector",
    "name": u"除尘器下灰量",
    "symbol": u"Af",
    "unit": u"kg/h",
    "calculate": u"Gaf*ηc",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_the_imported_smoke_real_state",
    "name": u"引风机进口烟气容积量(实态)",
    "symbol": u"Vxf",
    "unit": u"m3/h",
    "calculate": u"烟风量计算表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "a_flue_gas_concentratio",
    "name": u"烟囱出口烟气浓度(实态)",
    "symbol": u"",
    "unit": u"mg/m3",
    "calculate": u"Gaf*(1-ηc)*106/Vxf",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "r_removal_coefficient",
    "name": u"出力系数",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"间断＞200%，连续＞150%",
    "remark": "",
    "default_value": "2.5",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "r_removal_the_ash_system",
    "name": u"除灰系统出力",
    "symbol": u"Gm",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "r_dry_ash_accumulation_density",
    "name": u"干灰堆积密度",
    "symbol": u"Pa",
    "unit": u"t/m³",
    "calculate": u"0.7~0.8",
    "remark": "",
    "default_value": "0.7",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "r_slag_accumulation_coefficient",
    "name": u"灰库充满系数",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"0.7~0.8",
    "remark": "",
    "default_value": "0.7",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "r_stored_ash",
    "name": u"存灰时间",
    "symbol": u"T",
    "unit": u"h",
    "calculate": u"1~2d，用户要求",
    "remark": "",
    "default_value": "2",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "r_effective_volume_ash_storage",
    "name": u"灰库有效体积",
    "symbol": u"Va",
    "unit": u"m³",
    "calculate": u"T*Gm/Pa/K",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "r_dia",
    "name": u"直径",
    "symbol": u"D",
    "unit": u"m",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "r_height",
    "name": u"高度",
    "symbol": u"H",
    "unit": u"m",
    "calculate": u"未含有5m的操作平台",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "g_grey_gas",
    "name": u"灰气比",
    "symbol": u"n",
    "unit": u"--",
    "calculate": u"7~20",
    "remark": "",
    "default_value": "15",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "g_air_transport_ash_system",
    "name": u"输灰系统耗气量",
    "symbol": u"Q",
    "unit": u"Nm³/min",
    "calculate": u"1.2*16.67*Gm/n/1.293",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_slag_amount",
    "name": u"渣量",
    "symbol": u"Gz",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_output_cold_single_stage",
    "name": u"冷渣机的出力(单台)",
    "symbol": u"Glz",
    "unit": u"t/h",
    "calculate": u"250%",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_cold_single_stage_count",
    "name": u"冷渣机台数",
    "symbol": u"n",
    "unit": u"--",
    "calculate": u"事故/运行",
    "remark": "",
    "default_value": "2",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_slag_removal_system",
    "name": u"除渣系统出力",
    "symbol": u"Gzm",
    "unit": u"t/h",
    "calculate": u"2.5倍的冷渣机总出力",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_high_temperature_belt_conveyor",
    "name": u"耐高温带式输送机出力",
    "symbol": u"Gssm",
    "unit": u"t/h",
    "calculate": u"除渣系统出力",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_cold_slag_accumulation_density",
    "name": u"冷渣堆积密度",
    "symbol": u"Pa",
    "unit": u"t/m³",
    "calculate": u"1.2",
    "remark": "",
    "default_value": "1.2",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_slag_accumulation_coefficient",
    "name": u"渣库充满系数",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"0.7~0.8",
    "remark": "",
    "default_value": "0.8",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_sludge_time",
    "name": u"存渣时间",
    "symbol": u"T",
    "unit": u"h",
    "calculate": u"1~2d，用户要求",
    "remark": "",
    "default_value": "2",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_slag_storage_volume_effective",
    "name": u"渣库有效体积",
    "symbol": u"Va",
    "unit": u"m³",
    "calculate": u"T*Gm/Pa/K",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_dia",
    "name": u"直径",
    "symbol": u"D",
    "unit": u"m",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_removalAshSlag",
    "name_eng": "s_height",
    "name": u"高度",
    "symbol": u"H",
    "unit": u"m",
    "calculate": u"未含有5m的操作平台",
    "remark": "",
    "default_value": "",
    "disable": "T"
}]

# 锅炉辅机系统
boilerAuxiliaries_data = [
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_boiler_evaporation",
        "name": u"锅炉蒸发量",
        "symbol": u"D0",
        "unit": u"t/h",
        "calculate": u"数据输入",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_emission_time",
        "name": u"排放时间",
        "symbol": u"t",
        "unit": u"min",
        "calculate": u"一班一次，2-3次，一次0.5-1min",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_emission_rate",
        "name": u"定期排污率",
        "symbol": u"η",
        "unit": u"%",
        "calculate": u"0.1%-0.5%",
        "remark": "",
        "default_value": "0.1",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_sewage_quantity",
        "name": u"定期排污水量",
        "symbol": u"Dpb",
        "unit": u"kg/h",
        "calculate": u"D0*1000*t*60*η",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_drum_pressure",
        "name": u"汽包压力",
        "symbol": u"P",
        "unit": u"Mpa",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_drum_aturatedwater_enthalpy",
        "name": u"汽包压力下的饱和水焓",
        "symbol": u"hd",
        "unit": u"kj/kg",
        "calculate": u"汽包压力",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_work_pressure",
        "name": u"排污扩容器工作压力",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"扩容器压力选0.15MPa(a)/0.45",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_work_aturatedwater_enthalpy",
        "name": u"扩容器压力下饱和水焓",
        "symbol": u"hs",
        "unit": u"kj/kg",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_work_latentheat_vaporization",
        "name": u"扩容器压力下汽化潜热",
        "symbol": u"r",
        "unit": u"kj/kg",
        "calculate": u"查表(饱和汽焓-饱和水焓)",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_ultimate_strength",
        "name": u"扩容器单位容积润许极限强度",
        "symbol": u"R",
        "unit": u"m3/(m3/kg)",
        "calculate": u"2000",
        "remark": "",
        "default_value": "2000",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_affluence_coefficient",
        "name": u"富裕系数",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"1.3~1.5的富裕系数",
        "remark": "",
        "default_value": "1.2",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_volume",
        "name": u"排污扩容容积",
        "symbol": u"Vv",
        "unit": u"m³",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "r_specifications",
        "name": u"选取",
        "symbol": u"考虑紧急放水后：DP-7.5",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_boiler_evaporation",
        "name": u"锅炉蒸发量",
        "symbol": u"D0",
        "unit": u"t/h",
        "calculate": u"数据输入",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_emission_rate",
        "name": u"连续排污率",
        "symbol": u"η",
        "unit": u"%",
        "calculate": u"1%-2%",
        "remark": "",
        "default_value": "1",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_sewage_quantity",
        "name": u"连续排污水量",
        "symbol": u"Dpb",
        "unit": u"kg/h",
        "calculate": u"D0*1000*η",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_drum_pressure",
        "name": u"汽包压力",
        "symbol": u"P",
        "unit": u"Mpa",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_drum_aturatedwater_enthalpy",
        "name": u"汽包压力下的饱和水焓",
        "symbol": u"hd",
        "unit": u"kj/kg",
        "calculate": u"汽包压力",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_work_pressure",
        "name": u"排污扩容器工作压力",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"扩容器压力选0.15MPa(a)/0.45/1.0",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_work_aturatedwater_enthalpy",
        "name": u"扩容器压力下饱和水焓",
        "symbol": u"hs",
        "unit": u"kj/kg",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_work_steam_pecificvolume",
        "name": u"扩容器压力下蒸汽比容",
        "symbol": u"υ",
        "unit": u"m3/kg",
        "calculate": u"查表",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_work_latentheat_vaporization",
        "name": u"扩容器压力下汽化潜热",
        "symbol": u"r",
        "unit": u"kj/kg",
        "calculate": u"查表(饱和汽焓-饱和水焓)",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_steam_dryness",
        "name": u"扩容器蒸汽干度",
        "symbol": u"X",
        "unit": u"--",
        "calculate": u"0.97~0.98",
        "remark": "",
        "default_value": "0.97",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_ultimate_strength",
        "name": u"扩容器单位容积润许极限强度",
        "symbol": u"R",
        "unit": u"m3/(m3/kg)",
        "calculate": u"2000",
        "remark": "",
        "default_value": "2000",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_vaporization_capacity",
        "name": u"排污水汽化量",
        "symbol": u"Df",
        "unit": u"kg/h",
        "calculate": u"(hd*η-hs)/xr",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_affluence_coefficient",
        "name": u"富裕系数",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"1.2的富裕系数",
        "remark": "",
        "default_value": "1.2",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_volume",
        "name": u"排污扩容汽容积",
        "symbol": u"Vv",
        "unit": u"m³",
        "calculate": u"水容积为汽容积的1/4",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "c_specifications",
        "name": u"选取",
        "symbol": u"DP-3.5/DP-1.5",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_boiler_watersystem_volume",
        "name": u"锅炉水系统容积",
        "symbol": u"V",
        "unit": u"m³",
        "calculate": u"输入",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_phosphate_content",
        "name": u"应维持的磷酸根含量",
        "symbol": u"PO43-",
        "unit": u"mg/L",
        "calculate": u"10~30",
        "remark": "",
        "default_value": "10",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_water_hardness",
        "name": u"给水硬度(原水)",
        "symbol": u"H",
        "unit": u"mmol/L",
        "calculate": u"7.0~9.5",
        "remark": "",
        "default_value": "7.0",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_purity",
        "name": u"纯度",
        "symbol": u"ε",
        "unit": u"m",
        "calculate": u"0.92~0.98",
        "remark": "",
        "default_value": "0.92",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_boiler_dosage_startup",
        "name": u"锅炉启动时加药量",
        "symbol": u"qm",
        "unit": u"g",
        "calculate": u"V(PO4+28.5*H)/250ε",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_boiler_water_supply",
        "name": u"锅炉给水量",
        "symbol": u"qfm",
        "unit": u"t/h",
        "calculate": u"输入",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_boiler_sewage_quantity",
        "name": u"锅炉排污量",
        "symbol": u"qbl",
        "unit": u"t/h",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_boiler_dosage_run",
        "name": u"运行时加药量",
        "symbol": u"qm",
        "unit": u"g/h",
        "calculate": u"计算",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_na3po4_concentration",
        "name": u"磷酸钠浓度",
        "symbol": u"C",
        "unit": u"%",
        "calculate": u"1%~5%",
        "remark": "",
        "default_value": "1",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_na3po4_density",
        "name": u"在C浓度下的磷酸三钠密度",
        "symbol": u"ρ",
        "unit": u"g/cm3",
        "calculate": u"见表",
        "remark": "",
        "default_value": "1.04",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "d_solution_quantity_run",
        "name": u"运行时汽包内加入的溶液量",
        "symbol": u"qv",
        "unit": u"m3/h",
        "calculate": u"qm/10Cρ",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_boiler_design_pressure",
        "name": u"锅炉设计使用压力",
        "symbol": u"P",
        "unit": u"Mpa",
        "calculate": u"数据输入",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_inlet_pressure",
        "name": u"省煤器入口进水压力",
        "symbol": u"P1",
        "unit": u"Mpa",
        "calculate": u"当工作压力P≤0.8MPa时，取P+0.05；当0.8<P≤5.9MPa时，取1.06P",
        "remark": "",
        "default_value": "10.63",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_deaerator_pressure",
        "name": u"除氧器工作压力",
        "symbol": u"Pd",
        "unit": u"Mpa",
        "calculate": u"数据输入",
        "remark": "",
        "default_value": "0.59",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_water_supply_resistance",
        "name": u"给水管阻力(以压头计)",
        "symbol": u"ΔPfw",
        "unit": u"m",
        "calculate": u"计算--许可流速2~3m/s",
        "remark": "",
        "default_value": "5",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_water_inlet_resistance",
        "name": u"进水管阻力(以压头计)",
        "symbol": u"ΔPin",
        "unit": u"m",
        "calculate": u"计算--许可流速0.5~1m/s",
        "remark": "",
        "default_value": "5",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_center_altitude_difference",
        "name": u"水泵中心至汽包正常水位的几何高度差",
        "symbol": u"Hy",
        "unit": u"m",
        "calculate": u"数据输入",
        "remark": "",
        "default_value": "20",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_deaerator_altitude_difference",
        "name": u"除氧器最低水位至水泵中心几何高度差(给水泵进口静水头)",
        "symbol": u"Hst",
        "unit": u"m",
        "calculate": u"数据输入",
        "remark": "",
        "default_value": "25",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_feedpump_total_head",
        "name": u"给水泵总扬程",
        "symbol": u"Hsw",
        "unit": u"m",
        "calculate": u"(P1-Pd)*102+1.2*(ΔPfw+ΔPin)+Hy-Hst",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_flow",
        "name": u"流量",
        "symbol": u"Q",
        "unit": u"t/h",
        "calculate": u"已知",
        "remark": "",
        "default_value": "110",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_pump_efficiency",
        "name": u"泵效率",
        "symbol": u"η",
        "unit": u"/",
        "calculate": u"0.6~0.8",
        "remark": "",
        "default_value": "0.7",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_transmission_efficiency",
        "name": u"机械传动效率",
        "symbol": u"η2",
        "unit": u"/",
        "calculate": u"直连1.0，联轴器0.98，皮带0.95",
        "remark": "",
        "default_value": "0.98",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_motor_efficiency",
        "name": u"电动机效率",
        "symbol": u"η3",
        "unit": u"/",
        "calculate": u"通常取0.9",
        "remark": "",
        "default_value": "0.9",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_motor_reserve_factor",
        "name": u"电动机备用系数",
        "symbol": u"β",
        "unit": u"/",
        "calculate": u"查表选取",
        "remark": "",
        "default_value": "1.15",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_auxiliary_motor_power",
        "name": u"配套电机功率",
        "symbol": u"P",
        "unit": u"kw",
        "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "p_specifications",
        "name": u"给水泵选用规格",
        "symbol": u"",
        "unit": u"--",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    #  {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_boiler_evaporation",
    #     "name": u"锅炉蒸发量",
    #     "symbol": u"D0",
    #     "unit": u"t/h",
    #     "calculate": u"数据输入",
    #     "remark": "",
    #     "default_value": "",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_makeup_steam",
    #     "name": u"补汽量",
    #     "symbol": u"D0''",
    #     "unit": u"t/h",
    #     "calculate": u"若无取0",
    #     "remark": "",
    #     "default_value": "",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_steamwater_cycle_loss",
    #     "name": u"厂内汽水循环损失",
    #     "symbol": u"D1",
    #     "unit": u"t/h",
    #     "calculate": u"0.03",
    #     "remark": "",
    #     "default_value": "0.03",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_pollution_loss",
    #     "name": u"排污损失",
    #     "symbol": u"D2",
    #     "unit": u"t/h",
    #     "calculate": u"0.02",
    #     "remark": "",
    #     "default_value": "0.02",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_condensing_capacity",
    #     "name": u"凝结水量",
    #     "symbol": u"D0'",
    #     "unit": u"t/h",
    #     "calculate": u"数据输入",
    #     "remark": "",
    #     "default_value": "",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_condensate_loss",
    #     "name": u"换热凝结水损失",
    #     "symbol": u"D1'",
    #     "unit": u"t/h",
    #     "calculate": u"0.02",
    #     "remark": "",
    #     "default_value": "0.02",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_boiler_normal_watersupply",
    #     "name": u"锅炉正常补水量",
    #     "symbol": u"D1s",
    #     "unit": u"t/h",
    #     "calculate": u"",
    #     "remark": "",
    #     "default_value": "",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_increase_loss",
    #     "name": u"启动或事故增加损失",
    #     "symbol": u"Dx",
    #     "unit": u"t/h",
    #     "calculate": u"0.1",
    #     "remark": "",
    #     "default_value": "0.1",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_boiler_max_watersupply",
    #     "name": u"锅炉最大补水量",
    #     "symbol": u"Dbu",
    #     "unit": u"t/h",
    #     "calculate": u"",
    #     "remark": "",
    #     "default_value": "",
    #     "disable": ""
    # }, {
    #     "module_name": "coalCHP_boilerAuxiliaries",
    #     "name_eng": "m_specifications",
    #     "name": u"选取水处理设备出力",
    #     "symbol": u"Q1’",
    #     "unit": u"t/h",
    #     "calculate": u"",
    #     "remark": "",
    #     "default_value": "",
    #     "disable": ""
    # }, 
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "s_boiler_evaporation",
        "name": u"锅炉蒸发量",
        "symbol": u"D0",
        "unit": u"t/h",
        "calculate": u"数据输入",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "s_storage_time",
        "name": u"储水时间",
        "symbol": u"t",
        "unit": u"min",
        "calculate": u"130t/h以下20min；130t/h以上10~15min",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "s_volume",
        "name": u"容积",
        "symbol": u"V",
        "unit": u"m3",
        "calculate": u"",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "s_size_length",
        "name": u"尺寸(长)",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"长",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "s_size_diameter",
        "name": u"尺寸(直径)",
        "symbol": u"D",
        "unit": u"m",
        "calculate": u"直径",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_new_steam_temperature",
        "name": u"新蒸汽温度",
        "symbol": u"t0",
        "unit": u"℃",
        "calculate": u"给定",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_new_pressure",
        "name": u"压力",
        "symbol": u"P0",
        "unit": u"MPa",
        "calculate": u"给定",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_new_enthalpy",
        "name": u"焓",
        "symbol": u"h0",
        "unit": u"kj/kg",
        "calculate": u"查询",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_new_flow_rate",
        "name": u"流量",
        "symbol": u"q0",
        "unit": u"t/h",
        "calculate": u"给定",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_water_temperature",
        "name": u"减温水温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"给定",
        "remark": "",
        "default_value": "20",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_water_pressure",
        "name": u"压力",
        "symbol": u"P1",
        "unit": u"MPa",
        "calculate": u"减温减压器出口压力+1.47MPA",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_water_enthalpy",
        "name": u"焓",
        "symbol": u"h1",
        "unit": u"kj/kg",
        "calculate": u"查询",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_water_flow_rate",
        "name": u"流量",
        "symbol": u"q1",
        "unit": u"t/h",
        "calculate": u"计算值",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_steam_temperature",
        "name": u"减温后蒸汽温度",
        "symbol": u"t2",
        "unit": u"℃",
        "calculate": u"给定",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_steam_pressure",
        "name": u"压力",
        "symbol": u"P2",
        "unit": u"MPa",
        "calculate": u"给定",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_steam_enthalpy",
        "name": u"焓",
        "symbol": u"h2",
        "unit": u"kj/kg",
        "calculate": u"查询",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_enough_enthalpy",
        "name": u"焓",
        "symbol": u"h2‘",
        "unit": u"kj/kg",
        "calculate": u"饱和水焓值",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_reduce_persent",
        "name": u"减温水中未蒸发部分所占份额",
        "symbol": u"t",
        "unit": u"%",
        "calculate": u"0.3~0.35",
        "remark": "",
        "default_value": "35",
        "disable": ""
    },
    {
        "module_name": "coalCHP_boilerAuxiliaries",
        "name_eng": "t_rudece_flow_rate",
        "name": u"流量",
        "symbol": u"q2",
        "unit": u"t/h",
        "calculate": u"q0+q1*（1-t）",
        "remark": "",
        "default_value": "",
        "disable": "T"
    }
]

coal_data = [
    # (u'阳泉混煤', '67.1', '3.1', '4.7', '1.0', '0.7', '6.0', '16.8', '8', '1.4',
    #  '26250'), 
    (u'原煤', '59.6', '2.0', '0.8', '0.8', '0.5', '10.0', '26.3', '8.2', '1.2',
     '22154'),
    # (u'西山混煤', '55.3', '3.7', '5.2', '0.4', '0.4', '10.0', '24.6', '14', '1.7',
    # '21903'), 
    # (u'鹤壁原煤', '72.3', '4.0', '2.0', '1.4', '0.3', '5.0', '15.0', '12', '2.0',
    #  '28340'),
    # (u'铜川混煤', '64.7', '3.4', '1.8', '1.0', '5.3', '405', '19.3', '14.2', '1.4',
    # '26083'),
    # (u'淄博混煤', '67.8', '3.0', '2.4', '1.3', '2.4', '3.9', '19.2',
    # '15', '1.6', '25958'),
    # (u'义马混煤', '43.4', '3.4', '11.4', '1.1', '1.5', '17.7', '21.5', '41', '1.5',
    # '16720'),
    # (u'大同混煤', '70.5', '4.2', '8.3', '0.9', '1.1', '6.0', '9.0', '30', '1.1',
    #  '27839'),
    # (u'鹤岗四号原煤', '48.4', '3.6', '10.2', '0.6', '0.3', '10.1', '26.8', '36',
    #  '1.3', '19312'),
    # (u'六道湾原煤', '59.6', '3.5', '9.2', '0.7', '0.7', '9.2', '17.1', '37', '1.6',
    #  '22823'),
    # (u'淮南原煤', '56.8', '4.13', '11.51', '1.09', '1.1', '10.6', '14.87', '32.1',
    #  '1.5', '21983'),
    # (u'萍乡安源低质煤', '39.9', '2.7', '4.6', '0.6', '0.2', '7.0', '45.0', '36',
    #  '1.6', '15884'),
    # (u'平顶山原煤', '47.2', '3.3', '6.5', '0.6', '0.8', '5.6', '36.0', '37', '1.3',
    #  '18308'),
    (u'褐煤', '34.2', '3.4', '5.7', '0.8', '0.5', '8.6', '46.8', '37.1', '',
     '14128'),
    # (u'开滦洗三号', '39.8', '2.6', '3.8', '0.8', '1.0', '7.0', '45.0', '37', '',
    #  '15675'),
    (u'洗中煤', '36.7', '3.0', '9.2', '0.7', '0.4', '12.0', '38.0', '45.5', '1.5',
     '14003'),
    (u'中煤', '36.6', '2.4', '5.5', '0.9', '1.6', '15.0', '38.0', '40', '',
     '16093'),
    (u'烟煤', '62.9', '4.13', '6.7', '1.45', '1.224', '10.0', '13.5', '37',
     '1.6', '24720'),
    (u'无烟煤', '64.8', '2.2', '1.82', '1.56', '0.64', '7.0', '22.3', '8', '1.7',
     '22210')
]

# 汽轮机计算
turbine_backpressure_data = [{
    "module_name": "turbine_backpressure",
    "name_eng": "e_turbine_efficiency",
    "name": "汽轮机内效率",
    "symbol": "ηTi",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "0.78",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_mechanical_efficiency",
    "name": "机械效率",
    "symbol": "ηm",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "0.95",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_generator_efficiency",
    "name": "发电机效率",
    "symbol": "ηg",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "0.973",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "Mpa",
    "calculate": "设计参数",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "设计参数",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_flow",
    "name": "进汽量",
    "symbol": "G1",
    "unit": "t/h",
    "calculate": "热源产生主蒸汽总流量",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_entropy",
    "name": "熵",
    "symbol": "",
    "unit": "kJ/(kg·℃)",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_enthalpy",
    "name": "焓",
    "symbol": "Izo",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_point_pressure",
    "name": "压力",
    "symbol": "P2'",
    "unit": "Mpa",
    "calculate": "设计参数",
    "remark": "",
    "default_value": "0.2",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_point_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "120.21",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_point_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_point_enthalpy",
    "name": "焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_plus_enthalpy",
    "name": "补汽焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_point_flow",
    "name": "抽汽量",
    "symbol": "G2",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_after_steam",
    "name": "蒸汽量",
    "symbol": "G",
    "unit": "t/h",
    "calculate": "G1+G2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_after_pressure",
    "name": "压力",
    "symbol": "P2'",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_after_enthalpy",
    "name": "焓",
    "symbol": "Ih",
    "unit": "kJ/kg",
    "calculate": "（（G1-G3）*Izob+G2*Izo'）/G",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_exhaust_after_entropy",
    "name": "熵",
    "symbol": "Sh",
    "unit": "kJ/(kg·℃)",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_exhaust_pressure",
    "name": "压力",
    "symbol": "P3",
    "unit": "Mpa",
    "calculate": "湿冷：0.005～0.007；空冷0.015",
    "remark": "",
    "default_value": "0.009",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_exhaust_enthalpy",
    "name": "焓",
    "symbol": "Ipo",
    "unit": "kJ/kg",
    "calculate": "汽轮机绝热等熵做功排汽焓值，查表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_backpressure_pressure",
    "name": "压力",
    "symbol": "P3",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_backpressure_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_backpressure_enthalpy",
    "name": "焓",
    "symbol": "Ipo",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_backpressure_flow",
    "name": "流量",
    "symbol": "G3",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_gross_generation",
    "name": "总发电量",
    "symbol": "P",
    "unit": "kw",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_hot_data",
    "name": "回热抽汽经验数据",
    "symbol": "",
    "unit": "--",
    "calculate": "经验值：有高加0.85；无高加0.9；无低价0.95",
    "remark": "",
    "default_value": "0.85",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_extraction",
    "name": "去除抽汽后",
    "symbol": "P",
    "unit": "MW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_extraction_select",
    "name": "选定",
    "symbol": "P",
    "unit": "MW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_steam_water_loss",
    "name": "全厂汽水损失",
    "symbol": "",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "0.03",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "e_throttle_flow",
    "name": "进汽量",
    "symbol": "",
    "unit": "t/h",
    "calculate": "选定",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "h_assume",
    "name": "假设",
    "symbol": "",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name":
    "turbine_backpressure",
    "name_eng":
    "h_temperature",
    "name":
    "温度",
    "symbol":
    "",
    "unit":
    "--",
    "calculate":
    "",
    "remark":
    "高压设5-6回热，给水温度210-230；中温中压4-5及回热，给水温度150-170；1.3MPa低压2级回热，给水温度104；2.4MPa低压3-4级回热，给水温度150；根据情况选择加热器形式：汇集式或者疏水放流式加热器，汇集式带疏水泵将疏水打至给水；假定换热效率0.98。",
    "default_value":
    "50",
    "disable":
    ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "h_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "h_enthalpy",
    "name": "焓值",
    "symbol": "",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "h_amount",
    "name": "量",
    "symbol": "",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_water_temperature",
    "name": "给水出水温度",
    "symbol": "tw2",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_water_enthalpy",
    "name": "给水出口焓",
    "symbol": "hw2",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "turbine_backpressure",
    "name_eng":
    "hh1_top_difference",
    "name":
    "上端差",
    "symbol":
    "φ",
    "unit":
    "℃",
    "calculate":
    "又称给水端差，是指加热器进口蒸汽压力下的饱和水温度与出口给水温度之差",
    "remark":
    "",
    "default_value":
    "2.8",
    "disable":
    ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_saturated_water_temperature",
    "name": "饱和水温度--加热器疏水温度",
    "symbol": "te‘",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_saturated_water_enthalpy",
    "name": "饱和水焓",
    "symbol": "he’",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_work_pressure",
    "name": "工作压力",
    "symbol": "pe‘",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_pressure_loss",
    "name": "抽汽管压损",
    "symbol": "ΔPe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "0.08",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_extraction_pressure",
    "name": "抽汽压力",
    "symbol": "Pe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_extraction_enthalpy",
    "name": "抽汽焓",
    "symbol": "he",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh1_extraction_amount",
    "name": "抽汽量",
    "symbol": "Δde‘",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_water_temperature",
    "name": "给水出水温度",
    "symbol": "tw2",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_water_enthalpy",
    "name": "给水出口焓",
    "symbol": "hw2",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_top_difference",
    "name": "上端差",
    "symbol": "φ",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "2.8",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_saturated_water_temperature",
    "name": "饱和水温度--加热器疏水温度",
    "symbol": "te‘",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_saturated_water_enthalpy",
    "name": "饱和水焓",
    "symbol": "he’",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_work_pressure",
    "name": "工作压力",
    "symbol": "pe‘",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_pressure_loss",
    "name": "抽汽管压损",
    "symbol": "ΔPe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "0.08",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_extraction_pressure",
    "name": "抽汽压力",
    "symbol": "Pe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_extraction_enthalpy",
    "name": "抽汽焓",
    "symbol": "he",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh2_extraction_amount",
    "name": "抽汽量",
    "symbol": "Δde‘",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_water_temperature",
    "name": "给水出水温度",
    "symbol": "tw2",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_water_enthalpy",
    "name": "给水出口焓",
    "symbol": "hw2",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_top_difference",
    "name": "上端差",
    "symbol": "φ",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "2.8",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_saturated_water_temperature",
    "name": "饱和水温度--加热器疏水温度",
    "symbol": "te‘",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_saturated_water_enthalpy",
    "name": "饱和水焓",
    "symbol": "he’",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_work_pressure",
    "name": "工作压力",
    "symbol": "pe‘",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_pressure_loss",
    "name": "抽汽管压损",
    "symbol": "ΔPe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "0.08",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_extraction_pressure",
    "name": "抽汽压力",
    "symbol": "Pe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_extraction_enthalpy",
    "name": "抽汽焓",
    "symbol": "he",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "hh3_extraction_amount",
    "name": "抽汽量",
    "symbol": "Δde‘",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_water_temperature",
    "name": "给水出水温度",
    "symbol": "tw2",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_water_enthalpy",
    "name": "给水出口焓",
    "symbol": "hw2",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_top_difference",
    "name": "上端差",
    "symbol": "φ",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "2.8",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_saturated_water_temperature",
    "name": "饱和水温度--加热器疏水温度",
    "symbol": "te‘",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_saturated_water_enthalpy",
    "name": "饱和水焓",
    "symbol": "he’",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_work_pressure",
    "name": "工作压力",
    "symbol": "pe‘",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_pressure_loss",
    "name": "抽汽管压损",
    "symbol": "ΔPe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "0.08",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_extraction_pressure",
    "name": "抽汽压力",
    "symbol": "Pe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_extraction_enthalpy",
    "name": "抽汽焓",
    "symbol": "he",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh1_extraction_amount",
    "name": "抽汽量",
    "symbol": "Δde‘",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_water_temperature",
    "name": "给水出水温度",
    "symbol": "tw2",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_water_enthalpy",
    "name": "给水出口焓",
    "symbol": "hw2",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_top_difference",
    "name": "上端差",
    "symbol": "φ",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "2.8",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_saturated_water_temperature",
    "name": "饱和水温度--加热器疏水温度",
    "symbol": "te‘",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_saturated_water_enthalpy",
    "name": "饱和水焓",
    "symbol": "he’",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_work_pressure",
    "name": "工作压力",
    "symbol": "pe‘",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_pressure_loss",
    "name": "抽汽管压损",
    "symbol": "ΔPe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "0.08",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_extraction_pressure",
    "name": "抽汽压力",
    "symbol": "Pe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_extraction_enthalpy",
    "name": "抽汽焓",
    "symbol": "he",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh3_extraction_amount",
    "name": "抽汽量",
    "symbol": "Δde‘",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_water_temperature",
    "name": "给水出水温度",
    "symbol": "tw2",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_water_enthalpy",
    "name": "给水出口焓",
    "symbol": "hw2",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_top_difference",
    "name": "上端差",
    "symbol": "φ",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "2.8",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_saturated_water_temperature",
    "name": "饱和水温度--加热器疏水温度",
    "symbol": "te‘",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_saturated_water_enthalpy",
    "name": "饱和水焓",
    "symbol": "he’",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_work_pressure",
    "name": "工作压力",
    "symbol": "pe‘",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_pressure_loss",
    "name": "抽汽管压损",
    "symbol": "ΔPe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "0.08",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_extraction_pressure",
    "name": "抽汽压力",
    "symbol": "Pe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_extraction_enthalpy",
    "name": "抽汽焓",
    "symbol": "he",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "lh2_extraction_amount",
    "name": "抽汽量",
    "symbol": "Δde‘",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "d_water_temperature",
    "name": "给水出水温度",
    "symbol": "tw2",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "d_water_enthalpy",
    "name": "给水出口焓",
    "symbol": "hw2",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "d_work_pressure",
    "name": "工作压力",
    "symbol": "pe‘",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "d_pressure_loss",
    "name": "抽汽管压损",
    "symbol": "ΔPe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "0.08",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "d_extraction_pressure",
    "name": "抽汽压力",
    "symbol": "Pe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "d_extraction_enthalpy",
    "name": "抽汽焓",
    "symbol": "he",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "d_extraction_amount",
    "name": "抽汽量",
    "symbol": "Δde‘",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "c_water_temperature",
    "name": "给水出水温度",
    "symbol": "tw2",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "c_water_enthalpy",
    "name": "给水出口焓",
    "symbol": "hw2",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "c_work_pressure",
    "name": "工作压力",
    "symbol": "pe‘",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "c_pressure_loss",
    "name": "抽汽管压损",
    "symbol": "ΔPe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "0.08",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "c_extraction_pressure",
    "name": "抽汽压力",
    "symbol": "Pe",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "c_extraction_enthalpy",
    "name": "抽汽焓",
    "symbol": "he",
    "unit": "kj/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "c_extraction_amount",
    "name": "抽汽量",
    "symbol": "Δde‘",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "turbine_backpressure",
    "name_eng":
    "i_turbine_efficiency",
    "name":
    "汽轮机内效率",
    "symbol":
    "ηTi",
    "unit":
    "--",
    "calculate":
    "",
    "remark":
    "（1）注意补汽压力所对应的的补汽点位置；（2）注意无高加时，高加抽气压力需手动修改",
    "default_value":
    "0.82",
    "disable":
    ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_mechanical_efficiency",
    "name": "机械效率",
    "symbol": "ηm",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "0.95",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_generator_efficiency",
    "name": "发电机效率",
    "symbol": "ηg",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "0.97",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "Mpa",
    "calculate": "设计参数",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "设计参数",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_flow",
    "name": "流量",
    "symbol": "G1",
    "unit": "t/h",
    "calculate": "热源产生主蒸汽总流量",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_entropy",
    "name": "熵",
    "symbol": "",
    "unit": "kJ/(kg·℃)",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_enthalpy",
    "name": "焓",
    "symbol": "Izo",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high1_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high1_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high1_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high1_enthalpy",
    "name": "焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high1_flow",
    "name": "流量",
    "symbol": "GH1",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_hh1_power",
    "name": "",
    "symbol": "P2",
    "unit": "KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high2_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high2_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high2_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high2_enthalpy",
    "name": "焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_high2_flow",
    "name": "流量",
    "symbol": "GH2",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_hh1_hh2_power",
    "name": "",
    "symbol": "P3",
    "unit": "KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_deoxidize_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_deoxidize_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_deoxidize_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_deoxidize_enthalpy",
    "name": "焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_deoxidize_flow",
    "name": "流量",
    "symbol": "GD",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_hh2_deoxidize_power",
    "name": "",
    "symbol": "P4",
    "unit": "KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_exhaust_point_pressure",
    "name": "压力",
    "symbol": "P2'",
    "unit": "Mpa",
    "calculate": "设计参数",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_exhaust_point_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "设计参数",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_exhaust_point_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_exhaust_point_enthalpy",
    "name": "焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "实际焓值",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_exhaust_point_flow",
    "name": "流量",
    "symbol": "G2",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_deoxidize_exhaust_power",
    "name": "",
    "symbol": "P1",
    "unit": "KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low1_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low1_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low1_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low1_enthalpy",
    "name": "焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low1_flow",
    "name": "流量",
    "symbol": "GL2",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_exhaust_lh1_power",
    "name": "",
    "symbol": "P5",
    "unit": "KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low2_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low2_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low2_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low2_enthalpy",
    "name": "焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low2_flow",
    "name": "流量",
    "symbol": "GL2",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_lh1_lh2_power",
    "name": "",
    "symbol": "P6",
    "unit": "KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low3_pressure",
    "name": "压力",
    "symbol": "",
    "unit": "Mpa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low3_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low3_temperature",
    "name": "温度",
    "symbol": "",
    "unit": "℃",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low3_enthalpy",
    "name": "焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_low3_flow",
    "name": "流量",
    "symbol": "GL2",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_lh2_lh3_power",
    "name": "",
    "symbol": "P6",
    "unit": "KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_exhaust_pressure",
    "name": "压力",
    "symbol": "P3",
    "unit": "Mpa",
    "calculate": "湿冷：0.005～0.007空冷0.015",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_exhaust_entropy",
    "name": "熵",
    "symbol": "S'",
    "unit": "kJ/(kg·℃)",
    "calculate": "主蒸汽绝热等熵",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_exhaust_enthalpy",
    "name": "焓",
    "symbol": "Ipo",
    "unit": "kJ/kg",
    "calculate": "汽轮机绝热等熵做功排汽焓值，查表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_exhaust_enthalpy_actual",
    "name": "实际焓",
    "symbol": "Ipo‘",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_exhaust_enthalpy_steam",
    "name": "饱和蒸汽焓",
    "symbol": "Ipog",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_exhaust_enthalpy_water",
    "name": "饱和水焓",
    "symbol": "Ipos",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "turbine_backpressure",
    "name_eng":
    "i_steam_exhaust_dry",
    "name":
    "干度",
    "symbol":
    "x",
    "unit":
    "--",
    "calculate":
    "(Ipo'-Ipos）/（Ipog-Ipos）小型汽轮机排汽湿度控制在10~12%以内",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_steam_exhaust_flow",
    "name": "流量",
    "symbol": "GL2",
    "unit": "t/h",
    "calculate": "压力提高，排汽干度降低；",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_lh2_steam_power",
    "name": "LH2至乏汽功率",
    "symbol": "P7",
    "unit": "KW",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_total_power",
    "name": "总功率",
    "symbol": "",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_backpressure",
    "name_eng": "i_calculation_error",
    "name": "计算误差",
    "symbol": "",
    "unit": "%",
    "calculate": "±3%以内",
    "remark": "",
    "default_value": "",
    "disable": "T"
}]

# 主要技术经济指标
economic_indicators_data = [{
    "module_name": "economic_indicators",
    "name_eng": "condensate_backwater_pressure",
    "name": u"凝结水回水压力",
    "symbol": u"Pw",
    "unit": u"Mpa",
    "calculate": u"一般取0.6~0.8",
    "remark": "",
    "default_value": "0.6",
    "disable": ""
}, {
    "module_name": "economic_indicators",
    "name_eng": "condensate_backwater_temperature",
    "name": u"凝结水回水温度",
    "symbol": u"Tw",
    "unit": u"℃",
    "calculate": u"查表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "condensate_backwater_enthalpy",
    "name": u"凝结水回水焓值",
    "symbol": u"iw",
    "unit": u"kJ/kg",
    "calculate": u"查表",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "economic_indicators",
    "name_eng":
    "smoke_heat_consumption_rate",
    "name":
    u"抽凝工况热耗率",
    "symbol":
    u"qc",
    "unit":
    u"kJ/(kW.h)",
    "calculate":
    u"抽凝工况下，机组每产生1kW.h电所需要的热量；Do*(Izo-Igs)/Pc",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name":
    "economic_indicators",
    "name_eng":
    "heat_consumption_rate",
    "name":
    u"纯凝工况热耗率",
    "symbol":
    u"qn",
    "unit":
    u"kJ/(kW.h)",
    "calculate":
    u"纯凝工况下，机组每产生1kW.h电所需要的热量；Do*(Izo-Igs)/Pn",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "smoke_steam_consumption_rate",
    "name": u"抽凝工况汽耗率",
    "symbol": u"dc",
    "unit": u"kg/(kW.h)",
    "calculate": u"机组每产生1kW.h电所需要的蒸汽量；qc/(Izo-Igs)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "steam_consumption_rate",
    "name": u"纯凝工况汽耗率",
    "symbol": u"dn",
    "unit": u"kg/(kW.h)",
    "calculate": u"机组每产生1kW.h电所需要的蒸汽量；qn/(Izo-Igs)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "annual_useage_hours",
    "name": u"机组年利用小时数",
    "symbol": u"Ha",
    "unit": u"h",
    "calculate": u"设计参数",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "annual_heat_hours",
    "name": u"机组年供热小时数",
    "symbol": u"T",
    "unit": u"h",
    "calculate": u"设计参数",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "economic_indicators",
    "name_eng": "annual_heat_supply",
    "name": u"年供热量",
    "symbol": u"Qa",
    "unit": u"GJ/a",
    "calculate": u"G2*(Izob-iw)/1000*T",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "annual_power_generation",
    "name": u"年发电量",
    "symbol": u"Pa",
    "unit": u"万kW.h",
    "calculate": u"Pc*T/10000+Pn*(Ha-T)/10000",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "plant_electricity_consumption",
    "name": u"厂用电率",
    "symbol": u"ζ",
    "unit": u"%",
    "calculate": u"",
    "remark": "",
    "default_value": "10",
    "disable": ""
}, {
    "module_name": "economic_indicators",
    "name_eng": "annual_power_supply",
    "name": u"年供电量",
    "symbol": u"Pag",
    "unit": u"万kW.h",
    "calculate": u"Pa*(1-ζ/100)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "boiler_efficiency",
    "name": u"锅炉效率",
    "symbol": u"ηg",
    "unit": u"%",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "pipeline_efficiency",
    "name": u"管道效率",
    "symbol": u"ηg",
    "unit": u"%",
    "calculate": u"一般取0.96~0.98",
    "remark": "",
    "default_value": "98",
    "disable": ""
}, {
    "module_name":
    "economic_indicators",
    "name_eng":
    "smoke_power_coal_consumption",
    "name":
    u"抽凝工况发电标煤耗率",
    "symbol":
    u"bcf",
    "unit":
    u"kg/h",
    "calculate":
    u"标准煤收到基低位发热量按7000kcal/kg计；qc/ηg/ηp/(7000*4.1868)*1000",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name":
    "economic_indicators",
    "name_eng":
    "power_coal_consumption",
    "name":
    u"纯凝工况发电标煤耗率",
    "symbol":
    u"bcf",
    "unit":
    u"kg/h",
    "calculate":
    u"标准煤收到基低位发热量按7000kcal/kg计；qn/ηg/ηp/(7000*4.1868)*1000",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "smoke_supply_coal_consumption",
    "name": u"抽凝工况供电标煤耗率",
    "symbol": u"bcg",
    "unit": u"g/(kW.h)",
    "calculate": u"bcf/(1-ζ/100)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "supply_coal_consumption",
    "name": u"纯凝工况供电标煤耗率",
    "symbol": u"bcg",
    "unit": u"g/(kW.h)",
    "calculate": u"bcf/(1-ζ/100)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "annual_average_thermoelectric_ratio",
    "name": u"全年平均热电比",
    "symbol": u"βp",
    "unit": u"%",
    "calculate": u"Qa/(Pa*3.6*10)*100",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name":
    "economic_indicators",
    "name_eng":
    "smoke_heat_efficiency",
    "name":
    u"抽凝工况全厂热效率",
    "symbol":
    u"ηcr",
    "unit":
    u"%",
    "calculate":
    u"(Pc*3.6+G2*(Izob-iw))/Bj/Qnet.Ar*100",
    "remark":
    "",
    "default_value":
    "",
    "disable":
    "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "heat_efficiency",
    "name": u"纯凝工况全厂热效率",
    "symbol": u"ηcr",
    "unit": u"%",
    "calculate": u"Pn*3.6/Bj/Qnet.Ar*100",
    "remark": "",
    "default_value": "",
    "disable": "T"
}]

# 化学水
chemicalWater_data = [{
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_process_route",
    "name": u"工艺路线",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_boiler_evaporation",
    "name": u"锅炉蒸发量",
    "symbol": u"D0",
    "unit": u"t/h",
    "calculate": u"数据输入",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_makeup_steam",
    "name": u"补汽量",
    "symbol": u"D0''",
    "unit": u"t/h",
    "calculate": u"若无取0",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_steamwater_cycle_loss",
    "name": u"厂内汽水循环损失",
    "symbol": u"D1",
    "unit": u"t/h",
    "calculate": u"0.03",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_pollution_loss",
    "name": u"排污损失",
    "symbol": u"D2",
    "unit": u"t/h",
    "calculate": u"0.02",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_condensing_capacity",
    "name": u"凝结水量",
    "symbol": u"D0'",
    "unit": u"t/h",
    "calculate": u"数据输入",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_condensate_loss",
    "name": u"换热凝结水损失",
    "symbol": u"D1'",
    "unit": u"t/h",
    "calculate": u"0.02",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_boiler_normal_watersupply",
    "name": u"锅炉正常补水量",
    "symbol": u"D1s",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_increase_loss",
    "name": u"启动或事故增加损失",
    "symbol": u"Dx",
    "unit": u"t/h",
    "calculate": u"0.1",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_boiler_max_watersupply",
    "name": u"锅炉最大补水量",
    "symbol": u"Dbu",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_output",
    "name": u"选取水处理设备出力",
    "symbol": u"Q",
    "unit": u"t/h",
    "calculate": u"2×20",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_chemicalWater",
    "name_eng": "m_remove_salt_volume",
    "name": u"除盐水箱有效容积",
    "symbol": u"Q*5",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}]

chimney_data = [{
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_height",
    "name": u"烟囱高度",
    "symbol": u"H",
    "unit": u"m",
    "calculate": u"",
    "remark": u"假定30、45、60、80、100、120、150、180",
    "default_value": "80",
    "disable": ""
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "local_atmosphere",
    "name": u"当地大气压",
    "symbol": u"p",
    "unit": u"pa",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "standard_air_density",
    "name": u"标态下空气密度",
    "symbol": u"ρ0",
    "unit": u"kg/m³",
    "calculate": u"",
    "remark": u"平均值",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "standard_average_smoke_density",
    "name": u"标态下平均烟气密度",
    "symbol": u"ρ1",
    "unit": u"kg/m³",
    "calculate": u"",
    "remark": u"平均值",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "standard_calculated_smoke_density",
    "name": u"标态下计算烟气密度",
    "symbol": u"ρ2",
    "unit": u"kg/m³",
    "calculate": u"",
    "remark": u"计算值",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "outdoor_air_temperature",
    "name": u"室外空气温度",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_inlet_temperature",
    "name": u"烟囱进口处烟温",
    "symbol": u"t0",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"锅炉排烟温度",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_temperature_drop_per_meter",
    "name": u"烟囱每米高度的温度降",
    "symbol": u"t'",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"砖砌温降0.1℃/m；钢板0.5℃/m",
    "default_value": "0.1",
    "disable": ""
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_average_temperature",
    "name": u"烟囱内平均温度",
    "symbol": u"t2",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_draft",
    "name": u"烟囱抽力",
    "symbol": u"S",
    "unit": u"pa",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "smoke_amount",
    "name": u"烟气量",
    "symbol": u"q",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": u"锅炉计算",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_outlet_temperature",
    "name": u"烟囱出口温度",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"抽力计算",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_outlet_flow",
    "name": u"烟囱出口流速",
    "symbol": u"Wo",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u"根据温度和烟囱高度选取12-20，低负荷时2.5-3",
    "default_value": "12",
    "disable": ""
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_outlet_inner_diameter",
    "name": u"烟囱出口内径选取",
    "symbol": u"d",
    "unit": u"m",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_outlet_selected_inner_diameter",
    "name": u"选取烟囱出口内径",
    "symbol": u"d'",
    "unit": u"mm",
    "calculate": u"",
    "remark": u"选取",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_experience_base_diameter",
    "name": u"经验烟囱基础内径",
    "symbol": u"d'’",
    "unit": u"mm",
    "calculate": u"",
    "remark": u"坡度小于2%",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "low_load_smoke_amount",
    "name": u"低负荷下烟气量",
    "symbol": u"q1",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "low_load_smoke_temperature",
    "name": u"低负荷下排烟温度",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"",
    "default_value": "100",
    "disable": ""
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "low_load_flow_30_percent",
    "name": u"30%低负荷校核烟气流速",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"不低于2.5",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_resistance_coefficient",
    "name": u"烟囱阻力系数",
    "symbol": u"r",
    "unit": u"--",
    "calculate": u"",
    "remark": u"一般0.04",
    "default_value": "0.04",
    "disable": ""
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_average_velocity",
    "name": u"烟囱内平均流速",
    "symbol": u"Wo",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_average_diameter",
    "name": u"烟囱平均直径",
    "symbol": u"d'’",
    "unit": u"m",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_friction_resistance",
    "name": u"烟囱摩擦阻力",
    "symbol": u"△p1",
    "unit": u"pa",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_outlet_resistance_coefficient",
    "name": u"烟囱出口阻力系数",
    "symbol": u"§",
    "unit": u"pa",
    "calculate": u"",
    "remark": u"一般取1",
    "default_value": "1",
    "disable": ""
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_outlet_resistance",
    "name": u"烟囱出口阻力",
    "symbol": u"△p2",
    "unit": u"pa",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "coalCHP_chimney",
    "name_eng": "chimney_total_resistance",
    "name": u"烟囱总阻力",
    "symbol": u"△p",
    "unit": u"pa",
    "calculate": u"",
    "remark": u"",
    "default_value": "",
    "disable": "T"
}]

# 采暖供热系统sheet
heat_supply_data = [{
    "module_name": "heat_supply",
    "name_eng": "heat_area",
    "name": "采暖面积",
    "symbol": "Ac",
    "unit": "m2",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name":
    "heat_supply",
    "name_eng":
    "heat_hot_target",
    "name":
    "采暖热指标",
    "symbol":
    "qh",
    "unit":
    "W/m2",
    "calculate":
    "民用住宅：50~55W/m2; 公共建筑：55~60W/m2; 工业建筑：80W/m2;  （热指标中已包括约5%的管网热损失）",
    "remark":
    "",
    "default_value":
    "60",
    "disable":
    ""
}, {
    "module_name": "heat_supply",
    "name_eng": "heat_hot_load",
    "name": "采暖热负荷",
    "symbol": "Qh",
    "unit": "Kw",
    "calculate": "Qh=Ac*qh/1000",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "heat_supply",
    "name_eng": "turbine_pressure",
    "name": "汽轮机抽汽压力",
    "symbol": "P2'",
    "unit": "MPa",
    "calculate": "根据汽机厂资料，一般取0.29、0.49、0.59、0.79、0.98",
    "remark": "",
    "default_value": "0.98",
    "disable": ""
}, {
    "module_name": "heat_supply",
    "name_eng": "heat_turbine_flow",
    "name": "汽轮机抽汽量",
    "symbol": "G2",
    "unit": "t/h",
    "calculate": "Qh*3.6/Izob",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "heat_supply",
    "name_eng": "use_flow",
    "name": "工业用汽量",
    "symbol": "Qjq",
    "unit": "t/h",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "heat_supply",
    "name_eng": "steam_supply_rate",
    "name": "供汽同时率",
    "symbol": "Pt",
    "unit": "%",
    "calculate": "60%~90%，一般取80%",
    "remark": "",
    "default_value": "80",
    "disable": ""
}, {
    "module_name": "heat_supply",
    "name_eng": "hot_loss",
    "name": "热网损失",
    "symbol": "Pr",
    "unit": "%",
    "calculate": "取5%",
    "remark": "",
    "default_value": "5",
    "disable": ""
}, {
    "module_name": "heat_supply",
    "name_eng": "hot_turbine_flow",
    "name": "汽轮机抽汽量",
    "symbol": "G2",
    "unit": "t/h",
    "calculate": "Qjq*Pt/(1-Pr)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}]
# 公用工程sheet
official_process_data = [{
    "module_name": "official_process",
    "name_eng": "o_oil_can",
    "name": "容积V",
    "symbol": "",
    "unit": "m3",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "official_process",
    "name_eng": "o_oil_pump",
    "name": "出力Q（单台）",
    "symbol": "",
    "unit": "t/h",
    "calculate": "Qnet.Ar*Bg*15%/10000/4.1868/1000",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "official_process",
    "name_eng": "o_oil_pump_pressure",
    "name": "压力P",
    "symbol": "",
    "unit": "MPa",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name":
    "official_process",
    "name_eng":
    "o_steam_parameter",
    "name":
    "蒸汽参数",
    "symbol":
    "",
    "unit":
    "--",
    "calculate":
    "根据《秸秆发电厂设计规范》可知，启动锅炉应根据工程具体情况确定是否设置，对于扩建电厂，宜采用原有机组的辅助蒸汽作为启动汽源，不设启动锅炉。",
    "remark":
    "低压参数",
    "default_value":
    "",
    "disable":
    ""
}, {
    "module_name":
    "official_process",
    "name_eng":
    "o_steam_volumn",
    "name":
    "额定蒸发量",
    "symbol":
    "",
    "unit":
    "--",
    "calculate":
    "",
    "remark":
    "",
    "default_value":
    "6",
    "disable":
    ""
}, {
    "module_name": "official_process",
    "name_eng": "o_fuel_type",
    "name": "燃料类型",
    "symbol": "",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "official_process",
    "name_eng": "o_install_way",
    "name": "安装方式",
    "symbol": "",
    "unit": "--",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": ""
}]

# 汽机辅机
turbine_auxiliary_data = [{
    "module_name": "turbine_auxiliary",
    "name_eng": "w_deaerator_working_pressure",
    "name": u"除氧器工作压力",
    "symbol": u"P",
    "unit": u"Mpa",
    "calculate": u"数据输入",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_deaerator_difference",
    "name": u"除氧器凝结水入口与凝汽器热井最低水位间的水柱静压差",
    "symbol": u"H1",
    "unit": u"m",
    "calculate": u"数据输入",
    "remark": "",
    "default_value": "25",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_deaerator_need_pressure",
    "name": u"除氧器入口凝结水管喷雾头所需喷雾压力",
    "symbol": u"H2",
    "unit": u"m",
    "calculate": u"数据输入",
    "remark": "",
    "default_value": "10",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_condenser_higter",
    "name": u"凝汽器的最高真空",
    "symbol": u"P",
    "unit": u"Mpa",
    "calculate": u"数据输入",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_hot_well_resistance",
    "name": u" 从热井到除氧器凝结水入口的凝结水管道流动阻力，另加20%裕量",
    "symbol": u"H3",
    "unit": u"m",
    "calculate": u"一般采用5mH2O",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_condensate_pump_lift",
    "name": u"凝结水泵的设计扬程",
    "symbol": u"H",
    "unit": u"m",
    "calculate": u"101.97P+H1+H2+H3",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_flow_amount",
    "name": u"流量",
    "symbol": u"Q",
    "unit": u"t/h",
    "calculate": u"已知",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_pump_efficiency",
    "name": u"泵效率",
    "symbol": u"η",
    "unit": u"--",
    "calculate": u"0.6~0.8",
    "remark": "",
    "default_value": "0.6",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_mechanical_transmission_efficiency",
    "name": u"机械传动效率",
    "symbol": u"η2",
    "unit": u"--",
    "calculate": u"直连1.0，联轴器0.98，皮带0.95",
    "remark": "",
    "default_value": "0.98",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_motor_efficiency",
    "name": u"电动机效率",
    "symbol": u"η3",
    "unit": u"--",
    "calculate": u"通常取0.9",
    "remark": "",
    "default_value": "0.75",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_motor_reserve_coefficient",
    "name": u"电动机备用系数",
    "symbol": u"β",
    "unit": u"--",
    "calculate": u"查表选取",
    "remark": "",
    "default_value": "1.15",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_auxiliary_motor_power",
    "name": u"配套电机功率",
    "symbol": u"P",
    "unit": u"kw",
    "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "w_select",
    "name": u"凝结水泵选型",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"选型参数：流量；扬程；给水温度；功率（一用一备）",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_condensate_amount",
    "name": u"凝汽量",
    "symbol": u"Dn",
    "unit": u"t/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_condenser_pressure",
    "name": u"凝汽器压力",
    "symbol": u"Pk",
    "unit": u"Mpa",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_steam_enthalpy",
    "name": u"汽轮机排汽焓",
    "symbol": u"Hs",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_cooling_water_inlet_temperature",
    "name": u"冷却水进口温度",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"输入",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_saturation_temperature",
    "name": u"饱和温度",
    "symbol": u"tbh",
    "unit": u"℃",
    "calculate": u"查询",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_supercooling",
    "name": u"过冷度",
    "symbol": u"t'",
    "unit": u"℃",
    "calculate": u"0~2",
    "remark": "",
    "default_value": "1",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_condensate_temperature",
    "name": u"凝结水温度",
    "symbol": u"tc",
    "unit": u"℃",
    "calculate": u"tbh-t'",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_condensate_enthalpy",
    "name": u"凝结水焓",
    "symbol": u"hc",
    "unit": u"kj/kg",
    "calculate": u"查询",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_cooling_pipe_coefficient",
    "name": u"冷却管的洁净系数",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"直流0.8~0.85，循环0.7~0.8",
    "remark": "",
    "default_value": "0.8",
    "disable": ""
}, {
    "module_name":
    "turbine_auxiliary",
    "name_eng":
    "m_correction_coefficient",
    "name":
    u"冷却管材料和壁厚的修正系数",
    "symbol":
    u"",
    "unit":
    u"--",
    "calculate":
    u"黄铜管为 ，铝黄铜管为 ，B5铜镍合金管为，B30铜镍合金管为 ，不锈钢管为 ",
    "remark":
    "",
    "default_value":
    "0.96",
    "disable":
    ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_calculation_index",
    "name": u"计算指数 t1≤26.7时",
    "symbol": u"X",
    "unit": u"--",
    "calculate": u"t1≤26.7时",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_cooling_flow",
    "name": u"冷却管内流速",
    "symbol": u"Vw",
    "unit": u"m/s",
    "calculate": u"1.5~2.5",
    "remark": "",
    "default_value": "2.2",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_cooling_type",
    "name": u"冷却管内径",
    "symbol": u"d2",
    "unit": u"m",
    "calculate": u"冷却管规格25*1",
    "remark": "",
    "default_value": "0.023",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_correction_condensers",
    "name": u"凝汽器比蒸汽负荷修正系数",
    "symbol": u"b",
    "unit": u"--",
    "calculate": u"取0.42",
    "remark": "",
    "default_value": "0.42",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_flow_speed_correction",
    "name": u"冷却管内流速的修正系数",
    "symbol": u"φw",
    "unit": u"--",
    "calculate": u"计算",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_inlet_temperature",
    "name": u"冷却水进口温度修正系数",
    "symbol": u"φt",
    "unit": u"--",
    "calculate": u"计算",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_flow_count",
    "name": u"冷却水流程数的修正系数",
    "symbol": u"φz",
    "unit": u"--",
    "calculate": u"冷却水流程数Z=2时，取1",
    "remark": "",
    "default_value": "1",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_consideration_change",
    "name": u"考虑凝汽器蒸汽负荷变化的修正系数",
    "symbol": u"φ6",
    "unit": u"--",
    "calculate": u"额定工况",
    "remark": "",
    "default_value": "1",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_total_heat_transfer",
    "name": u"总传热系数",
    "symbol": u"K",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_condenser_heat_load",
    "name": u"凝汽器热负荷",
    "symbol": u"Q",
    "unit": u"kw",
    "calculate": u"Dn*（hs-hc）",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_cycle_ratio",
    "name": u"循环倍率",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"北方60~70；中部65~75；南方70~80",
    "remark": "",
    "default_value": "65",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_circulating_water",
    "name": u"循环水量",
    "symbol": u"Dw",
    "unit": u"t/h",
    "calculate": u"计算",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_cooling_water_rise",
    "name": u"冷却水温升 冷却水cp 取4.1868",
    "symbol": u"△t",
    "unit": u"℃",
    "calculate": u"Q/Dw*Cp",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_cooling_outlet_temperature",
    "name": u"冷却水出口温度",
    "symbol": u"t2",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_logarithmic_mean_difference",
    "name": u"对数平均温差",
    "symbol": u"△tm",
    "unit": u"℃",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "m_area_cooling_surface",
    "name": u"冷却面积",
    "symbol": u"A",
    "unit": u"m2",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_air_ejector_pressure",
    "name": u"射水抽气器工作压力",
    "symbol": u"P1",
    "unit": u"Mpa",
    "calculate": u"输入",
    "remark": "",
    "default_value": "0.44",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_water_tank_pressure",
    "name": u"射水箱工作压力",
    "symbol": u"P2",
    "unit": u"Mpa",
    "calculate": u"输入",
    "remark": "",
    "default_value": "0.1",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_water_difference",
    "name": u"射水抽气器安装高度与射水箱最高水位之差",
    "symbol": u"H1",
    "unit": u"M",
    "calculate": u"输入",
    "remark": "",
    "default_value": "6",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_ejection_pump_loss",
    "name": u"射水泵进出口管路损失",
    "symbol": u"H2",
    "unit": u"m",
    "calculate": u"一般采用5mH2O",
    "remark": "",
    "default_value": "5",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_total_lift",
    "name": u"总扬程",
    "symbol": u"H",
    "unit": u"m",
    "calculate": u"101.97(P1-P2)+H1+H2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_flow_amount",
    "name": u"流量",
    "symbol": u"Q",
    "unit": u"t/h",
    "calculate": u"汽轮机资料",
    "remark": "",
    "default_value": "187",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_pump_efficiency",
    "name": u"泵效率",
    "symbol": u"η",
    "unit": u"--",
    "calculate": u"0.6~0.8",
    "remark": "",
    "default_value": "0.6",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_mechanical_transmission_efficiency",
    "name": u"机械传动效率",
    "symbol": u"η2",
    "unit": u"--",
    "calculate": u"直连1.0，联轴器0.98，皮带0.95",
    "remark": "",
    "default_value": "0.98",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_motor_efficiency",
    "name": u"电动机效率",
    "symbol": u"η3",
    "unit": u"--",
    "calculate": u"通常取0.9",
    "remark": "",
    "default_value": "0.75",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_motor_reserve_coefficient",
    "name": u"电动机备用系数",
    "symbol": u"β",
    "unit": u"--",
    "calculate": u"查表选取",
    "remark": "",
    "default_value": "1.15",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_auxiliary_motor_power",
    "name": u"配套电机功率",
    "symbol": u"P",
    "unit": u"kw",
    "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "f_select",
    "name": u"射水泵选型",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_water_tank_pressure",
    "name": u"射水箱工作压力",
    "symbol": u"P1",
    "unit": u"Mpa",
    "calculate": u"输入",
    "remark": "",
    "default_value": "0.1",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_recirculating_tube_pressure",
    "name": u"循环水回水母管压力",
    "symbol": u"P2",
    "unit": u"Mpa",
    "calculate": u"输入",
    "remark": "",
    "default_value": "0.2",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_water_difference",
    "name": u"射水抽气器安装高度与射水箱最高水位之差",
    "symbol": u"H1",
    "unit": u"M",
    "calculate": u"输入",
    "remark": "",
    "default_value": "6",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_ejection_pump_loss",
    "name": u"射水泵进出口管路损失",
    "symbol": u"H2",
    "unit": u"m",
    "calculate": u"一般采用5mH2O",
    "remark": "",
    "default_value": "5",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_total_lift",
    "name": u"总扬程",
    "symbol": u"H",
    "unit": u"m",
    "calculate": u"101.97(-P1+P2)+H1+H2",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_flow_amount",
    "name": u"流量",
    "symbol": u"Q",
    "unit": u"t/h",
    "calculate": u"已知（半小时抽完射水箱水）",
    "remark": "",
    "default_value": "20",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_pump_efficiency",
    "name": u"泵效率",
    "symbol": u"η",
    "unit": u"--",
    "calculate": u"0.6~0.8",
    "remark": "",
    "default_value": "0.6",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_mechanical_transmission_efficiency",
    "name": u"机械传动效率",
    "symbol": u"η2",
    "unit": u"--",
    "calculate": u"直连1.0，联轴器0.98，皮带0.95",
    "remark": "",
    "default_value": "0.98",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_motor_efficiency",
    "name": u"电动机效率",
    "symbol": u"η3",
    "unit": u"--",
    "calculate": u"通常取0.9",
    "remark": "",
    "default_value": "0.75",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_motor_reserve_coefficient",
    "name": u"电动机备用系数",
    "symbol": u"β",
    "unit": u"--",
    "calculate": u"查表选取",
    "remark": "",
    "default_value": "1.15",
    "disable": ""
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_auxiliary_motor_power",
    "name": u"配套电机功率",
    "symbol": u"P",
    "unit": u"kw",
    "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "turbine_auxiliary",
    "name_eng": "c_select",
    "name": u"射水箱冷却水泵选型",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""
}]
# 模板表
reportTemplate_data = [{
    "template_name": u"燃煤热电联产标准方案",
    "module_id": u"coalCHP",
    "user_id": "1",
    "template_create_date": "2018-01-01 00:00:00.000",
    "template_update_date": "2018-01-01 00:00:00.000",
    "template__left_menu":
    u"""
[{"id":"1","text":"文档目录","icon":true,"li_attr":{"id":"1"},"a_attr":{"href":"#","id":"1_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_2","text":"一.概   述","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_2"},"a_attr":{"href":"#","id":"j1_2_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_3","text":"二.总承包内容及交接点","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_3"},"a_attr":{"href":"#","id":"j1_3_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_10","text":"2.1项目总承包内容","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_10"},"a_attr":{"href":"#","id":"j1_10_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_11","text":"2.1.1工程设计范围","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_11"},"a_attr":{"href":"#","id":"j1_11_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_3","j1_10"]},{"id":"j1_12","text":"2.1.2成套设备采购及供货：","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_12"},"a_attr":{"href":"#","id":"j1_12_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_3","j1_10"]},{"id":"j1_13","text":"2.1.3设备安装调试内容","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_13"},"a_attr":{"href":"#","id":"j1_13_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_3","j1_10"]},{"id":"j1_14","text":"2.1.4本工程不包含的施工及安装范围","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_14"},"a_attr":{"href":"#","id":"j1_14_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_3","j1_10"]}],"type":"file","parentNode":["1","j1_3"]},{"id":"j1_15","text":"2.2项目交接点","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_15"},"a_attr":{"href":"#","id":"j1_15_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_3"]}],"type":"file","parentNode":["1"]},{"id":"j1_4","text":"三.设计及施工标准规范","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_4"},"a_attr":{"href":"#","id":"j1_4_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_5","text":"四.工程建设技术条件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_5"},"a_attr":{"href":"#","id":"j1_5_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_16","text":"4.1厂址条件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_16"},"a_attr":{"href":"#","id":"j1_16_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]},{"id":"j1_17","text":"4.2气象条件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_17"},"a_attr":{"href":"#","id":"j1_17_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]},{"id":"j1_18","text":"4.3工程地质","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_18"},"a_attr":{"href":"#","id":"j1_18_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]},{"id":"j1_19","text":"4.4地震烈度","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_19"},"a_attr":{"href":"#","id":"j1_19_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]},{"id":"j1_20","text":"4.5建设场地","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_20"},"a_attr":{"href":"#","id":"j1_20_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]},{"id":"j1_21","text":"4.6电源情况","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_21"},"a_attr":{"href":"#","id":"j1_21_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]},{"id":"j1_22","text":"4.7水源状况","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_22"},"a_attr":{"href":"#","id":"j1_22_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]},{"id":"j1_23","text":"4.8辅料供应","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_23"},"a_attr":{"href":"#","id":"j1_23_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]}],"type":"file","parentNode":["1"]},{"id":"j1_6","text":"五.工程建设技术参数","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_6"},"a_attr":{"href":"#","id":"j1_6_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_24","text":"5.1项目概况","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_24"},"a_attr":{"href":"#","id":"j1_24_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_25","text":"5.2项目性质","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_25"},"a_attr":{"href":"#","id":"j1_25_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_26","text":"5.3总图部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_26"},"a_attr":{"href":"#","id":"j1_26_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_27","text":"5.3.1总图布置依据","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_27"},"a_attr":{"href":"#","id":"j1_27_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_26"]},{"id":"j1_28","text":"5.3.2 厂址概述及设想","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_28"},"a_attr":{"href":"#","id":"j1_28_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_26"]},{"id":"j1_29","text":"5.3.3 总平面布置说明","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_29"},"a_attr":{"href":"#","id":"j1_29_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_26"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_30","text":"5.4热机部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_30"},"a_attr":{"href":"#","id":"j1_30_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_31","text":"5.4.1装机方案","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_31"},"a_attr":{"href":"#","id":"j1_31_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_30"]},{"id":"j1_32","text":"5.4.2机组选型","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_32"},"a_attr":{"href":"#","id":"j1_32_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_30"]},{"id":"j1_33","text":"5.4.3点火系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_33"},"a_attr":{"href":"#","id":"j1_33_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_30"]},{"id":"j1_34","text":"5.4.4燃烧系统及辅助设备","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_34"},"a_attr":{"href":"#","id":"j1_34_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_30"]},{"id":"j1_35","text":"5.4.5热力系统及主辅助设备选择","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_35"},"a_attr":{"href":"#","id":"j1_35_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_30"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_39","text":"5.5 燃料输送部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_39"},"a_attr":{"href":"#","id":"j1_39_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_40","text":"5.5.1. 系统范围","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_40"},"a_attr":{"href":"#","id":"j1_40_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_39"]},{"id":"j1_41","text":"5.5.2 主要配置原则","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_41"},"a_attr":{"href":"#","id":"j1_41_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_39"]},{"id":"j1_42","text":"5.5.3 卸煤装置及贮煤设施","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_42"},"a_attr":{"href":"#","id":"j1_42_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_39"]},{"id":"j1_43","text":"5.5.4 除杂筛碎设备","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_43"},"a_attr":{"href":"#","id":"j1_43_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_39"]},{"id":"j1_44","text":"5.5.5 上煤系统及运行方式","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_44"},"a_attr":{"href":"#","id":"j1_44_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_39"]},{"id":"j1_45","text":"5.5.6 辅助设施及附属建筑","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_45"},"a_attr":{"href":"#","id":"j1_45_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_39"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_36","text":"5.6脱硫脱硝部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_36"},"a_attr":{"href":"#","id":"j1_36_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_97","text":"5.6.1概述","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_97"},"a_attr":{"href":"#","id":"j1_97_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_36"]},{"id":"j1_37","text":"5.6.1脱硝系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_37"},"a_attr":{"href":"#","id":"j1_37_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_36"]},{"id":"j1_38","text":"5.6.2脱硫系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_38"},"a_attr":{"href":"#","id":"j1_38_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_36"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_46","text":"5.7除灰、除渣部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_46"},"a_attr":{"href":"#","id":"j1_46_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_47","text":"5.7.1 概述","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_47"},"a_attr":{"href":"#","id":"j1_47_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_46"]},{"id":"j1_48","text":"5.7.2 除渣系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_48"},"a_attr":{"href":"#","id":"j1_48_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_46"]},{"id":"j1_49","text":"5.7.3 除灰系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_49"},"a_attr":{"href":"#","id":"j1_49_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_46"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_51","text":"5.8化学水处理部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_51"},"a_attr":{"href":"#","id":"j1_51_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_50","text":"5.8.1 水源及水质资料","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_50"},"a_attr":{"href":"#","id":"j1_50_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_51"]},{"id":"j1_52","text":"5.8.2给水、炉水、蒸汽质量标准","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_52"},"a_attr":{"href":"#","id":"j1_52_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_51"]},{"id":"j1_53","text":"5.8.3化学水处理工艺流程","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_53"},"a_attr":{"href":"#","id":"j1_53_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_51"]},{"id":"j1_54","text":"5.8.4锅炉补给水量","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_54"},"a_attr":{"href":"#","id":"j1_54_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_51"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_55","text":"5.9水工部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_55"},"a_attr":{"href":"#","id":"j1_55_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_56","text":"5.9.1供水现状","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_56"},"a_attr":{"href":"#","id":"j1_56_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_55"]},{"id":"j1_57","text":"5.9.2水源接入方式","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_57"},"a_attr":{"href":"#","id":"j1_57_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_55"]},{"id":"j1_58","text":"5.9.3循环冷却水系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_58"},"a_attr":{"href":"#","id":"j1_58_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_55"]},{"id":"j1_59","text":"5.9.4排水系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_59"},"a_attr":{"href":"#","id":"j1_59_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_55"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_60","text":"5.10电气部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_60"},"a_attr":{"href":"#","id":"j1_60_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_98","text":"5.10.1总承包界限划分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_98"},"a_attr":{"href":"#","id":"j1_98_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_99","text":"5.10.2电气系统接线方案（下列三选一）","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_99"},"a_attr":{"href":"#","id":"j1_99_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_100","text":"5.10.3直流系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_100"},"a_attr":{"href":"#","id":"j1_100_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_101","text":"5.10.4二次线、继电保护及自动装置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_101"},"a_attr":{"href":"#","id":"j1_101_anchor"},"state":{"loaded":true,"opened":true,"selected":true,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_102","text":"5.10.5主要电气设备布置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_102"},"a_attr":{"href":"#","id":"j1_102_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_103","text":"5.10.6电缆及电缆设施","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_103"},"a_attr":{"href":"#","id":"j1_103_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_104","text":"5.10.7过电压保护与接地","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_104"},"a_attr":{"href":"#","id":"j1_104_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_105","text":"5.10.8照明及检修网络","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_105"},"a_attr":{"href":"#","id":"j1_105_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_106","text":"5.10.9检修网络","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_106"},"a_attr":{"href":"#","id":"j1_106_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_107","text":"5.10.10消防报警及火灾检测自动报警系统、厂内通信","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_107"},"a_attr":{"href":"#","id":"j1_107_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]},{"id":"j1_108","text":"5.10.11设备选型","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_108"},"a_attr":{"href":"#","id":"j1_108_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_60"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_73","text":"5.11 热工自动化部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_73"},"a_attr":{"href":"#","id":"j1_73_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_74","text":"5.11.1 热工自动化水平及控制室布置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_74"},"a_attr":{"href":"#","id":"j1_74_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_73"]},{"id":"j1_75","text":"5.11.2 热工自动化功能","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_75"},"a_attr":{"href":"#","id":"j1_75_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_73"]},{"id":"j1_76","text":"5.11.3热工保护和报警","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_76"},"a_attr":{"href":"#","id":"j1_76_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_73"]},{"id":"j1_77","text":"5.11.4 热工自动化系统配置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_77"},"a_attr":{"href":"#","id":"j1_77_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_73"]},{"id":"j1_78","text":"5.11.5 热工自动化设备选型","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_78"},"a_attr":{"href":"#","id":"j1_78_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_73"]}],"type":"file","parentNode":["1","j1_6"]},{"id":"j1_79","text":"5.12土建部分（以详细设计为准）","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_79"},"a_attr":{"href":"#","id":"j1_79_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_80","text":"5.12.1 建筑设计","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_80"},"a_attr":{"href":"#","id":"j1_80_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_79"]},{"id":"j1_81","text":"5.12.2 结构设计","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_81"},"a_attr":{"href":"#","id":"j1_81_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_79"]},{"id":"j1_82","text":"5.12.3其他主要生产建（构）筑物","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_82"},"a_attr":{"href":"#","id":"j1_82_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_6","j1_79"]}],"type":"file","parentNode":["1","j1_6"]}],"type":"file","parentNode":["1"]},{"id":"j1_7","text":"六.技术服务","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_7"},"a_attr":{"href":"#","id":"j1_7_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_83","text":"6.1技术服务范围","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_83"},"a_attr":{"href":"#","id":"j1_83_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_7"]},{"id":"j1_84","text":"6.2人员培训","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_84"},"a_attr":{"href":"#","id":"j1_84_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_7"]},{"id":"j1_85","text":"6.3设计联络","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_85"},"a_attr":{"href":"#","id":"j1_85_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_7"]},{"id":"j1_86","text":"6.4技术文件提交","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_86"},"a_attr":{"href":"#","id":"j1_86_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_7"]},{"id":"j1_87","text":"6.5竣工资料提交","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_87"},"a_attr":{"href":"#","id":"j1_87_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_7"]}],"type":"file","parentNode":["1"]},{"id":"j1_88","text":"七.工程质量及考核方式","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_88"},"a_attr":{"href":"#","id":"j1_88_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_89","text":"7.1工程质量","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_89"},"a_attr":{"href":"#","id":"j1_89_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_88"]},{"id":"j1_90","text":"7.2性能试验","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_90"},"a_attr":{"href":"#","id":"j1_90_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_88"]}],"type":"file","parentNode":["1"]},{"id":"j1_9","text":"八.其他","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_9"},"a_attr":{"href":"#","id":"j1_9_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]}],"type":"default"}]
""",
    "template_state": "0",
    "template_left_content": u"""
[{"content":"用法简介：\n1. 鼠标选中“文档目录”，点击“添加子标题”按钮，添加一级子目录。\n2. 鼠标选中生成的子级目录，点击“添加子标题”按钮，添加该目录的子级目录。\n3. 鼠标选中目录，点击“删除”按钮，删除该目录结构。\n4. 鼠标选中目录，点击“重命名”按钮或者点击键盘“F2”按钮，重命名目录。\n5. 鼠标选中目录拖拽可交换目录结构位置。\n6. 插入表格或图片后，点击“切换预览方式”按钮，可预览表格和图片，再次点击此按钮回到结构预览。\n7. 插入图表后需要在图表前后各留一行空行。\n8. 编辑模板时，请不要忘记点击“保存”按钮，将数据保存到数据库方便下次使用。\n","id":"1"},{"class":["1"],"content":"##### 用户企业概况：手动输入\n##### 用户能源需求描述：手动输入\n##### 综上所述，针对目前企业的生产用汽情况，考虑企业主工艺扩容的需求，我公司根据多年的发电工程建设及设计经验，计划建设概况如下：\n##### 项目名称：手动输入；\n##### 建设地址：手动输入；\n##### 建设规模：手动输入；\n##### 建设方式：总承包方以EPC总承包方式承担工程建设及相关的服务；\n##### 承包内容：项目范围内的工程设计、设备成套供货、设备安装调试、工程验收及保质期服务工作；\n##### 设计理念：秉承经济、实用、可靠、合理、低成本建设、低投入运行设计理念。\n##### 工程质量：达到国家施工验收规范合格标准；设备制造质量应保证其达到总承包协议书技术附件要求，保证设计的合理性，设备制造质量应保证其可靠性，购置的标准设备应为国家或行业认可的成熟定型产品;所选用的工程材料、构建必须满足国家质量检验标准和设计规范的要求。安装工程质量应该保证质量合格、安全可靠；设计、施工安装、设备及材料、试车及验收等都应满足和符合现行国家及行业相关规范、规程和标准的要求。","id":"j1_2"},{"class":["1"],"content":"","id":"j1_3"},{"class":["1"],"content":"##### 所有设计文件、供货的材料和设备应符合相关的中国标准、规定、规范及法律，或者符合中国钢铁企业余热利用的相关标准、规定、规范及法律：\n##### 《小型火力发电厂设计规范》GB50049-2011\n##### 《火力发电厂设计技术规程》（DL5000-2000）\n##### 《火力发电厂采暖通风与空气调节设计技术规定》DL/T5035-94\n##### 《火力发电厂汽水管道设计技术规定》DL/T5054-1996\n##### 《火力发电厂保温油漆技术规范》DL/T5072-2007\n##### 《火力发电厂建筑设计规程》DL/T5094-1999\n##### 《火力发电厂和变电所照明设计技术规定》DLGJ56-95\n##### 《火力发电厂烟风煤粉管道设计技术规程》DL/T5121-2000\n##### 《工业企业噪声控制设计规范》（GBJ87-85）\n##### 《建筑设计防火规范》（GB50016-2006）\n##### 《建筑物防雷设计规范》（GB50057-94）\n##### 《爆炸和火灾危险环境电力装置设计规范》（GB50058-92）\n##### 《电力配备典型消防规程》（DL5027-93）\n##### 《火力发电厂总图运输设计技术规定》（DL/T5032-2005）\n##### 《火力发电厂与变电所设计防火规范》（GB50229-96）\n##### 《采暖通风与空气调节设计技术规定》（DJ/T5035-95）\n##### 《动力机器基础设计规范》（GB50040-1996）\n##### 《火灾自动报警系统设计规范》（GB50116-98）；\n##### 《蒸汽锅炉安全技术监察规程》（劳部发[1996]276号）\n##### 《电力建设施工及验收技术规范》（建筑工程篇）（SDJ69-1987）；\n##### 《电力建设施工及验收技术规范》(锅炉机组篇)（DL/T-5047-95）；\n##### 《电力建设施工及验收技术规范》(汽轮机机组篇)（DL5011-92）；\n##### 《电气装置安装工程施工及验收规范》GB50254～GB50259-96\n##### 《火力发电厂建设工程启动试运及验收规程》（2009年版）","id":"j1_4"},{"class":["1"],"content":"","id":"j1_5"},{"class":["1"],"content":"##### 本项目属于自备动力站，高效利用煤炭进行燃烧，产生中压蒸汽供厂区用汽。（手动输入）项目投产后，将创造良好的经济效益、社会效益和环保效益。","id":"j1_6"},{"class":["1"],"content":"","id":"j1_7"},{"class":["1","j1_9"],"content":"","id":"j1_8"},{"class":["1"],"content":"##### 1项目在施工调试过程中，总承包方应至少派一名技术人员常驻发包人现场，进行现场服务，协调处理有关技术问题。在试运调试过程中出现的设备事故、人身事故由总承包方负责。\n##### 2施工过程中出现变更，总承包方需报告监理及发包人，经确认后方可施工，由总承包方出具设计变更单。\n##### 3本协议一式6份，发包方4份（一正三副），总承包2份（一正一副）。\n##### 4本协议未尽事宜，友好协商解决。\n##### 以下无正文。\n##### 发包方：唐山旭阳化工有限责任公司           总承包方： 西安陕鼓动力股份有限公司\n##### 代   表：                     \t\t   代    表：\n##### 联系电话：                            联系电话：\n##### 传    真：                             传    真：\n##### 通信地址：                       \t\t通信地址：陕西省西安市高新区沣惠南路8号\n##### 邮    编：　\t\t\t\t\t\t\t\t邮    编：7100100\n##### 日    期：      年  月  日　　　　\t日    期：     年  月  日","id":"j1_9"},{"class":["1","j1_3"],"content":"##### 总承包方项目总承包内容包括：项目整体的工艺设计、工厂设计、土建设计、钢构设计、主辅设备设计及本工程项目所需的所有附属配套设施、工艺管道及管廊设计、电缆桥架及电缆布局设计，并对设计的完整性、合理性及正确性负责。总承包方负责项目范围内成套设备供货、建安工程、调试、试运行，并对项目范围内供货设备整体技术性能、供货质量全面负责，并提供技术服务和售后服务。","id":"j1_10"},{"class":["1","j1_3","j1_10"],"content":"##### 本工程建设内容与设计范围为与新建动力站内所有相关的建筑与工程设计，具体工程建设范围包括如下内容：\n##### ——热力系统(包括锅炉、汽机、发电机以及配套辅机)；\n##### ——燃料输送系统及储煤系统；\n##### ——灰渣处理工程（包括炉渣及飞灰的收集、冷却、输送、仓储、外运部分）；\n##### ——脱硫系统；\n##### ——脱硝系统；\n##### ——脱硫脱硝工程（主要包括脱硫脱硝部分）\n##### ——除盐水工程（主要包括除盐水站、凝结水回水部分）\n##### ——项目配套的电气系统；\n##### ——项目配套的土建工程；\n##### ——项目红线范围内的相关配套能源介质管网；\n##### 设计范围为与上述工程相关的整体方案规划、主辅设备选型、工艺系统设计、电气控制系统设计、建筑与结构设计、采暖与通风设计、保温油漆设计、检修维护起吊配套设计、环保工程设计、节能优化设计、劳动安全与卫生设计等。","id":"j1_11"},{"class":["1","j1_3","j1_10"],"content":"##### 项目范围内主辅设备、电控、自控成套设备及单体设备采购及供货。","id":"j1_12"},{"class":["1","j1_3","j1_10"],"content":"##### 1） 热力系统及其辅助设备的安装调试；\n##### 2） 除灰、除渣系统调试；\n##### 3） 脱硫、脱硝系统调试；\n##### 4） 燃料输送系统调试；\n##### 5） 除盐水系统调试；\n##### 6） 电气及自控设备安装调试，包含电气施工材料、电缆、电缆桥架、软件编程；\n##### 7） 未提及的项目范围内其他设备安装及调试。","id":"j1_13"},{"class":["1","j1_3","j1_10"],"content":"##### ①.  工程项目相关报批，如项目报批、环评、安评、消防报批、开工备案等；\n##### ②.  项目范围内的三通一平及绿化等；\n##### ③.  桩基工程及桩基检测，土建桩基切桩头和灌注钢筋混凝土撞头；地上、地下障碍物的拆迁清除；\n##### ④.  红线范围外集水井、排水管；\n##### ⑤.  开挖石块、建筑垃圾等由总承包方运至发包人指定的免费地点；\n##### ⑥.   调试期所有的能源介质（水、电、气、汽、煤、点火燃料）、药品、试剂等由发包人无偿提供；\n##### ⑦.  水质化验全部设备、设施；\n##### ⑧.  生产工器具(设备自带专用工具除外）、工具、办公家具，工人安全防护、劳保用品、警示牌标（汽、电、气、水、道路）等；\n##### ⑨.  施工过程中如发现受国家法律保护的历史文物、文化遗迹等，由此发生的费用和对工程进度产生的影响由发包人承担。","id":"j1_14"},{"class":["1","j1_3"],"content":"##### 能源介质及各系统交接点如下表：\n\n| 序号 |名称 |交接点 |备注 |\n|:------|:------|:------|:------|\n| 1 |外供蒸汽 | 甲方供至接至电厂围墙外1m以内（自己取水除外）| |\n| 2 |灰渣 |乙供接至电厂围墙外1米以内，并配阀门 | | \n| 3 |凝结水回水 |甲方接至电厂围墙外1米以内，并配阀门  | | \n| 4 |外供电 |乙方接至上级变电站母线绝缘子串 | | \n| 5 |启动电源 | 甲方提供两路10kv电源| | \n| 6 |燃料 |甲方运输至干煤棚 | | \n| 7 |工业污水| 乙方简单处理后接至厂区污水管 | | \n| 8 |生活污水  | 乙方通过化粪池处理后接至厂区污水管| | \n","id":"j1_15"},{"class":["1","j1_5"],"content":"##### 唐山旭阳化工有限责任公司地处环渤海中心区域的京唐港区腹地黄金地带，坐落于河北乐亭经济开发区内 （省级化工园区），现有项目用地 6040.48 亩 。旭阳发展可以建设自有码头，距公司直线距离仅有约2公里。（手动输入）","id":"j1_16"},{"class":["1","j1_5"],"content":"##### （1）气温\n##### 多年平均温度 @@coalchp_needs_questionnaire.w_mean_annual_temperature_value@@℃ \n##### 年最热月份平均温度 @@coalchp_needs_questionnaire.w_mean_summer_temperature_value@@℃\n##### 年最冷月份平均温度 @@coalchp_needs_questionnaire.w_mean_winter_temperature_value@@℃\n##### 极端最高温度 @@coalchp_needs_questionnaire.w_extreme_high_temperature_value@@℃\n##### 极端最低温度 @@coalchp_needs_questionnaire.w_extreme_low_temperature_value@@℃\n##### （2）气压 \n##### 多年平均大气压 @@coalchp_needs_questionnaire.w_mean_annual_barometric_value@@kpa\n##### 历年夏季平均气压 @@coalchp_needs_questionnaire.w_mean_summer_barometric_value@@kpa\n##### 历年冬季平均气压 @@coalchp_needs_questionnaire.w_mean_winter_barometric_value@@kpa\n##### （3）降雨量 \n##### 年平均降水量 手动输入mm\n##### 年最大降水量 手动输入mm\n##### 一昼夜最大降水量 手动输入mm\n##### 一小时最大降水量 手动输入mm\n##### 年降雨日数（≥0.1mm）手动输入（d）\n##### 年降雪日数 手动输入（d）\n##### 最大积雪厚度 手动输入cm\n##### （4）湿度 \n##### 年平均相对湿度 @@coalchp_needs_questionnaire.w_annual_average_relative_humidity_value@@%\n##### 全年最热月份平均相对湿度 @@coalchp_needs_questionnaire.w_mean_summer_relative_humidity_value@@%\n##### 全年最冷月份平均相对湿度 @@coalchp_needs_questionnaire.w_mean_winter_relative_humidity_value@@%\n##### （5）风速 \n##### 平均风速 手动输入m/s\n##### 最大风速及风向 手动输入m/s WNW\n##### 全年盛行风向 手动输入ENE\n##### 夏季盛行风向 手动输入SW\n##### （6）蒸发 \n##### 年平均蒸发量 手动输入（小时蒸发）\n##### （7）特殊气候 \n##### 沙暴  1994-2003  手动输入十年无沙暴\n##### 雷暴  历年雷暴平均日数 手动输入天\n##### 冰雹  年平均 手动输入天/年\n##### 浓雾  历年平均雾日数手动输入天\n##### （8）云雾及日照 \n##### 平均日照时数 手动输入小时","id":"j1_17"},{"class":["1","j1_5"],"content":"##### 总承包方给发包人提供详堪布点图，发包人组织详堪并在10个工作日间将详堪资料以电子版形式反馈给总承包方，由总承包方根据详堪进行设计。","id":"j1_18"},{"class":["1","j1_5"],"content":"##### 根据《建筑抗震设计规范》附录A的划分要求，本工程抗震设防烈度为7度，（手动输入）设计地震分组为第二组（手动输入），设计地震基本加速度为0.15g。（手动输入）本工程按规范进行设计。","id":"j1_19"},{"class":["1","j1_5"],"content":"##### 本工程建设场地的位于唐山旭阳化工有限责任公司厂区内。手动输入","id":"j1_20"},{"class":["1","j1_5"],"content":"##### 本工程需要发包人提供两路独立的10kV电源，装置能力要满足动力站系统的启动、运行用电。","id":"j1_21"},{"class":["1","j1_5"],"content":"##### 利用原厂管网提供水源,发包方负责施工，接至动力站红线外一米处。本工程按接口处供水水压符合以下要求进行设计：\n##### 生产新水≥0.30MPa\n##### 生活给水≥0.25MPa\n##### 消防水≥0.30MPa","id":"j1_22"},{"class":["1","j1_5"],"content":"##### 项目主要消耗药品如氯化钠、磷酸三钠等，由发包人统一自行采购配给。","id":"j1_23"},{"class":["1","j1_6"],"content":"##### 此项目为唐山旭阳新建25万吨/年苯乙烯配套2×100t/h锅炉岛工程。锅炉产生中温中压蒸汽供苯乙烯项目使用，这些蒸汽使用后凝结成水经除铁后进入除盐水箱，然后通过除盐水泵、冷渣器进入除氧器，再经过给水泵进入锅炉，循环使用。（手动输入）","id":"j1_24"},{"class":["1","j1_6"],"content":"##### 本项目属于自备动力站，高效利用煤炭进行燃烧，产生中压蒸汽供厂区用汽。（手动输入）项目投产后，将创造良好的经济效益、社会效益和环保效益。","id":"j1_25"},{"class":["1","j1_6"],"content":"","id":"j1_26"},{"class":["1","j1_6","j1_26"],"content":"##### （1）本期工程业主提供的资料。\n##### （2）《小型火力发电厂设计规范》GB50049-2011\n##### （3）《火力发电厂总图运输设计技术规程》DL/T5032-2005\n##### （4）《建筑设计防火规范》","id":"j1_27"},{"class":["1","j1_6","j1_26"],"content":"##### 本动力站拟建设2×100t/h中温中压循环流化床锅炉（一用一备），项目用地东南侧布置有25万吨/年苯乙烯，处于20万吨/年苯加氢项目南侧。（手动输入） ","id":"j1_28"},{"class":["1","j1_6","j1_26"],"content":"#####  1）总平面设计原则\n##### （1）充分利用现有场地条件，因地制宜，减少工程费用；\n##### （2）工艺流程合理，功能分区明确；\n##### （3）物流流向合理，交通运输便捷；\n##### （4）满足电厂总图运输的有关设计规范、规定要求；\n##### （5）根据气象、日照合理布置建构筑物，改善厂内工作生活环境；\n##### （6）与现有建筑及设施协调一致，有序融合。\n#####  2） 主要建设项目\n##### 本期工程厂区主要建设项目有司炉室、脱硫脱硝及除尘设施、输煤设施、灰库、除盐水站、空压机室，以及相应的辅助、附属建构筑物。\n##### 针对本项目，绿化以厂前区集中绿化和厂区周边及道路两侧的行道树为主，种植落叶木和常青乔木，减少污染，保护环境。","id":"j1_29"},{"class":["1","j1_6"],"content":"","id":"j1_30"},{"class":["1","j1_6","j1_30"],"content":"##### 本期热电站规划建设规模为2×100t/h中温中压燃煤锅炉配套苯乙烯项目使用，一用一备，不考虑扩建。（手动输入）","id":"j1_31"},{"class":["1","j1_6","j1_30"],"content":"##### 1.锅炉主要参数：\n##### 本工程为2×100t/h中温中压循环流化床（手动输入）燃煤锅炉，产品结构简单、紧凑，锅炉本体由燃烧设备、给煤装置、床下点火装置、分离和返料装置、水冷系统、过热器、省煤器、空气预热器、钢架、平台扶梯、炉墙等组成。本期锅炉运转层以下全封闭，以上紧身封闭。\n##### 锅炉主要参数：\n##### 额定蒸发量         @@coalchp_furnace_calculation.f_steam_flow_design@@t/h\n##### 额定蒸汽压力       @@coalchp_furnace_calculation.f_steam_pressure_design@@MPa\n##### 额定蒸汽温度      @@coalchp_furnace_calculation.f_steam_temperature_design@@℃\n##### 给水温度            @@coalchp_furnace_calculation.f_water_temperature_design@@℃\n##### 排烟温度            @@coalchp_furnace_calculation.h_smoke_temperature_design@@℃\n##### 锅炉设计效率         @@coalchp_furnace_calculation.f_boiler_efficiency_design@@%\n##### 锅炉保证效率         @@coalchp_furnace_calculation.f_boiler_efficiency_design@@%\n##### 排污率               @@coalchp_furnace_calculation.f_blowdown_rate_design@@%\n##### 2.汽轮机主要参数：手动输入\n##### 型号：              C15-8.83/0.5\n##### 形式：     高温高压抽汽空冷式汽轮机\n##### 额定功率：             15MW\n##### 额定进汽量：            86t/h\n##### 额定抽汽量：            35t/h\n##### 最大进汽量：            97t/h\n##### 最大抽汽量：          50t/h\n##### 主蒸汽温度：          535℃\n##### 　　压力：               8.83MPa\n##### 抽汽压力：            0.5MPa\n##### 抽汽温度：            158℃\n##### 数    量：             2台\n##### 3.发电机主要参数 手动输入\n##### 额定功率：            15MW\n##### 额定电压:             10.5kV±5%\n##### 转    速：            3000rpm\n##### 功率因数：            0.8\n##### 冷却方式：            空气冷却\n##### 励磁方式：            无刷励磁\n##### 数    量：            2台","id":"j1_32"},{"class":["1","j1_6","j1_30"],"content":"##### 1.锅炉点火燃料\n##### 锅炉点火燃料采用0#轻柴油，油质分析见下表：\n#####  0#轻柴油主要参数表\n| 项     目 |数    值 |\n|:------|:------|\n| 粘  度 |1.23 |\n| 凝固点 |7 |\n| 燃  点 |102 |\n| 闪电（闭口） |90 |\n| 比  重 |0.83 |\n| 低位发热量KJ/Kg |42900 |\n##### 2.燃料来源\n##### 锅炉点火用0#轻柴油利用汽车油槽车从厂外运来，通过卸油泵把油卸入储油罐中，然后利用点火油泵送入锅炉点火油枪。锅炉点火采用二级点火方式，高能点火器直接点燃轻柴油，再点燃床料。","id":"j1_33"},{"class":["1","j1_6","j1_30"],"content":"##### 1.燃烧装置及配风系统\n#####     流化床布风板采用水冷布风板结构；布风板上布置了放渣管，下方接冷渣机。\n#####     空气分为一次风及二次风，一、二次风之比为@@coalchp_furnace_calculation.a_first_wind_volume_design@@：@@coalchp_furnace_calculation.a_second_wind_volume_design@@，一次风从炉膛水冷风室二侧进入，经布风板风帽小孔进入燃烧室。二次风在布风板上高度方向分二层送入。水冷风室底部还布置了二只放灰管，用于定期清除水冷风室中积灰。一次冷风总管上接出一根风管，分别去送煤风和密封风接口。一次热风总管两侧各接出一根风管，分别去播煤风接口。\n##### 2.给煤装置\n##### 破碎后的煤通过输送皮带送至煤仓间落入煤仓内。本期每台锅炉设置一座煤仓，为锅炉额定蒸汽量下约8-9小时耗煤量。\n##### 每座煤仓下面有三个（手动输入）出煤口，每个出煤口安装有一台给煤机。三台（手动输入）给煤总出力满足锅炉200％（手动输入）额定工况的燃煤量要求，每台给煤机设计出力满足锅炉67.8%（手动输入）额定工况的燃煤量要求，正常情况下每台给煤机各带50%（手动输入）负荷运行。给煤量通过改变给煤机的转速来调整。每台给煤机内通入一次冷风作为密封风，由于给煤管内为正压，给煤机必须具有良好的密封性。\n##### 炉前布置了3套（手动输入）落煤装置，煤通过落煤装置送入燃烧室。落煤装置上布置有送煤风和播煤风，以防给煤堵塞。送煤风接一次冷风，播煤风接一次热风，两股风合计约为总风量的4%，每只送风管、播煤风管布置一只风门，以调节送煤风量。\n##### 3.烟气系统\n##### 引风机是输送含尘且温度较高的烟气，风量大风压高，它运行的可靠性、耐磨性、经济性、价格将直接影响电厂的初投资及今后的运行经济效益。\n##### 本工程推荐引风机与脱硫增压风机合并设置。根据《小型火力发电厂设计规范》（GB50049-2011）及《火力发电厂燃烧系统设计计算技术规程》（DL/T 5240-2010）相关要求本工程引风机选用高效离心式风机，采用变频调节方式。\n##### 炉膛出口烟气依次经过尾部受热面、省煤器、烟气脱硝装置、管式空气预热器，然后通过烟道进入电袋除尘器，再经引风机、脱硫吸收塔、烟囱排入大气。\n##### 为降低NOx的排放，锅炉采用低NOx燃烧器、分级配风等措施可有效降低NOx的排放水平，根据本工程的煤质资料和锅炉技术协议，锅炉本体出口(脱硝前)NOx质量排放浓度不超过200mg/Nm3(以NO2计，标态，干烟气，O2=6%)。\n##### a：1台110%    b：2台60%（手动输入）BMCR容量的离心式引风机，配变频调速装置。根据《小型火力发电厂设计规范》，引风机风量裕量系数选为10%，另加温度裕量；风压裕量系数选为20%。\n##### 4.锅炉主要辅机的数量及参数:\n##### 以下为每台锅炉配置：\n##### ● 一次风机                           1台\n##### ● 二次风机                           1台\n##### ● 返料机                             2台\n##### ● 引风机                             1台/2台（手动输入）\n##### ● 除尘器                             1台\n##### （1） 一次风机\n##### 风量                 @@coalchp_smoke_air_system.f_fan_selection_flow@@ m3/h\n##### 风压                 @@coalchp_smoke_air_system.f_fan_select_total_pressure@@ Pa\n##### 台数                  @@coalchp_smoke_air_system.f_count@@ 台\n##### （2）二次风机\n##### 风量                 @@coalchp_smoke_air_system.s_fan_selection_flow@@ m3/h\n##### 风压                 @@coalchp_smoke_air_system.s_fan_select_total_pressure@@ Pa\n##### 台数                  @@coalchp_smoke_air_system.s_count@@ 台\n##### （3）返料风机\n##### 风量                 @@coalchp_smoke_air_system.r_fan_selection_flow@@ m3/h\n##### 风压                 @@coalchp_smoke_air_system.r_fan_select_total_pressure@@ Pa\n##### 台数                 （手动输入）台\n##### （4）引风机\n##### 风量                 @@coalchp_smoke_air_system.i_fan_selection_flow@@ m3/h\n##### 风压                 @@coalchp_smoke_air_system.i_fan_select_total_pressure@@ Pa\n##### 台数                  @@coalchp_smoke_air_system.i_count@@ 台\n##### （5）布袋除尘器\n##### 型式                 长袋脉冲除尘器（手动输入）\n##### 处理烟气量            @@coalchp_furnace_calculation.d_entry_smoke_actual_flow_design@@ m3/h\n##### 出口含尘浓度          ≤30mg/Nm3  达到国家最新环保标准要求\n##### 本体阻力              ≤1200Pa\n##### 本体漏风率            ＜2%\n##### 台数                 （手动输入）台","id":"j1_34"},{"class":["1","j1_6","j1_30"],"content":"##### 热力系统描述\n##### ⑴ 主蒸汽系统：\n##### 本工程为三炉两机（手动输入），a:切换母管制系统  b:集中母管制  c：单元制，（手动选择），主蒸汽管路选用a、15CrMoG（中温中压、次高温次高压适用）；b、12Cr1MoVG（高温高压适用）。（手动选择）\n##### ⑵ 高压给水系统：\n##### 本工程高压给水系统采用采用母管制；给水泵出口设有给水再循环管和给水再循环母管；本期建设2台手动输入可以满足锅炉额定蒸发量的110%容量的给水泵。\n##### 给水操作台采用两路负荷调节系统，范围分别为：主回路给水管为100%BMCR工况运行；30%、70%两条旁路给水管低负荷工况运行。\n##### ⑶ 低压给水及除氧系统：\n##### 本期工程配备1台手动输入110t/h手动输入大气式除氧器手动输入，除氧器采用定压运行方式手动输入，为了保证除氧器在相同工况下运行和对不同工况的要求，除氧器设有汽平衡母管、低压给水母管、加热蒸汽母管、化学补充水母管、主厂区凝结水回水等母管。\n##### 除氧用的加热蒸汽由锅炉锅筒处引出，经减温减压后进入除氧器。\n##### ⑷ 主凝结水系统\n##### 每台机组设2台凝结水泵，正常运行时，1台运行，1台备用；凝结水从排汽装置热井出口由凝结水泵送出，经凝结水处理装置后送至汽封加热器、第三、二、一级低压加热器后，进入高压除氧器。\n##### ⑸ 工业水及冷却水系统\n##### 本期工程工业水系统设置以满足水泵、风机类设备轴承冷却水及其它冷却设备的冷却用水。\n##### ⑹ 锅炉排污系统\n##### 本工程每台锅炉各配置连续排污扩容器、定期排污扩容器各一台，锅炉连续排污水接入连排，回收二次蒸汽引入除氧器，剩余排污水排入定排，夏季工况下，排入排污降温池，冬季工况下，接入厂内一次换热站热水侧利用。\n##### ⑺ 主厂区生产回水系统\n##### 主厂区用汽后凝结水经除铁后到除盐水箱后依次经过除盐水泵、锅炉冷渣器后进入除氧器。\n##### ⑻ 疏水箱有关管道系统\n##### 锅炉、汽机、汽水管路启动、运行、事故、停机、停炉过程中，有大量疏放水，其汽水品质大多情况符合锅炉炉水要求，必须加以收集利用,因此设置疏水箱和疏水扩容器，收集的合格水经疏水泵打入除氧器。","id":"j1_35"},{"class":["1","j1_6"],"content":"","id":"j1_36"},{"class":["1","j1_6","j1_36"],"content":"##### 1、脱硝工艺简介\n##### 燃煤锅炉生成的NOx主要由NO、NO2及微量的N2O组成，其中NO含量超过90%，NO2约占5%～10%，N2O只有1%左右。NOx理论上有三条生成途径，即热力型、燃烧型与瞬态型。其中，燃料型NOX所占比例最大。\n##### （1）燃料型NOx，燃料中的氮氧化物在煤粉火焰前端被氧化而成，所占NOX比例超过80%~90%；\n##### （2）热力型NOx，助燃空气中的N2在燃烧后期1300℃以上的温度下被氧化而成；\n##### （3）瞬态型NOx，由分子氮在火焰前沿的早期阶段生成，所占NOx比例很小。\n##### 利用燃烧过程产生的氮基中间产物或者往烟气中喷射氨气，在合适的温度、气氛或者催化剂条件下将NOx还原，这是燃煤锅炉控制NOx排放的主要机理。由此衍生出炉膛喷射还原剂的选择性非催化还原烟气脱硝（简称SNCR）和炉内烟道喷射还原剂的选择性催化还原烟气脱硝（简称SCR）、SNCR与烟道型SCR联合等三类技术，这些技术成熟可靠，可单独或联合使用。\n##### 1）SNCR脱硝技术介绍\n##### SNCR技术就是利用机械式喷枪将氨基还原剂（如氨气、氨水、尿素）溶液雾化成液滴喷入炉膛，热解生成气态NH3，在850～1100℃温度区域（通常为锅炉对流换热区）和没有催化剂条件下，NH3与NOX进行选择性非催化还原反应，将NOx还原成N2与H2O。喷入炉膛的气态NH3同时参与还原和氧化两个竞争反应：温度超过1100℃时，NH3被氧化成NOx，氧化反应起主导；低于1100℃时，NH3与NOx的还原反应为主，但反应速率降低。\n##### 4 NO + 4 NH3 + O2 → 4 N2 + 6 H2O            \n##### 4 NH3 + 5 O2 → 4NO + 6 H2O\n##### SNCR整体工艺简洁，具有如下特点：\n##### （1）现代SNCR技术可以控制NOX排放浓度降低50～60%，脱硝效率随机组容量增加，炉膛尺寸大，机组负荷变化范围扩大，增加了SNCR反应温度窗口与还原剂均匀混合的控制难度，致使脱硝效率下降。对于300MW以下小容量机组，效率在40%-60%左右。\n##### （2）SNCR装置不增加烟气系统阻力，也不产生新的SO3，氨逃逸浓度通常控制在5～10μL/L以内（SCR是3μL/L）；\n##### （3）合适的反应温度窗口狭窄，为适应锅炉负荷的波动、提高氨在反应区的混合程度和利用率，通常在炉膛出口过热器下方设置多层喷枪。\n##### （4）雾化液滴蒸发与热解过程中需要吸收热量，这会造成锅炉效率降低约0.1～0.3个百分点。\n##### （5）还原剂雾化液滴在大于1100℃温度下分解时，部分被氧化成NOX，增加了NOX原始控制难度，导致还原剂的有效利用率降低。脱硝效率为30～40%时，还原剂利用率仅为20～30%。\n##### 2）SCR脱硝技术介绍\n##### SCR技术就是把还原剂氨气喷入锅炉省煤器下游300～400℃的烟道内，在催化剂作用下，将烟气中NOX还原为无害的N2和H2O。SCR工艺需在烟道上增设一个反应器。受制于锅炉烟气参数、飞灰特性及空间布置等因素，SCR工艺主要分三种：高灰型（HD型）、低灰型（LD型）和尾部型（TE型）等。高灰型SCR是主流布置，工作环境相对恶劣，催化剂活性惰化较快，但烟气温度合适（300～400℃），经济性最高。低灰型SCR与尾部型SCR的选择，主要是为了净化催化剂运行的烟气条件或者是受到布置空间的限制，由于需将烟气加热到300℃，只适合于特定环境。\n目前国内当前已建成、在建、拟建SCR脱硝装置的新老机组约均采用高灰型工艺。主要反应如下： \n##### 4 NO + 4 NH3 + O2 → 4 N2 + 6 H2O            \n##### NO + NO2 + 2 NH3 → 2 N2 + 3 H2O\n##### 6 NO2 + 8 NH3 → 7 N2 + 12 H2O\n##### 4 NH3 + 3 O2 → 2 N2 + 6 H2O\n##### 4 NH3 + 5 O2 → 4NO + 6 H2O\n##### SCR技术具有如下特点：\n##### （1）脱硝效率可以达到90%。\n##### （2）需要在空预器入口（烟温为320～420℃范围）增设反应器，反应器内安装催化剂，增加锅炉烟道阻力约700～1000Pa，需提高引风机压头。\n##### （3）逃逸氨与SO3反应，有可能在空预器换热面上形成硫酸氢氨，可能导致空预器的堵塞，通过控制化学理论量的加氨，可使氨的泄漏量保持在一个可接受的水平上。\n反应器布置在锅炉尾部省煤器与空气预热器之间，烟气经锅炉上级省煤器或下级省器，进入脱硝入口烟道、喷氨格栅、反应器、脱硝出口烟道，空气预热器。\n##### 3）SNCR+SCR联合法技术介绍\n##### SNCR+SCR 联合法技术是SNCR工艺的还原剂喷入炉膛技术同SCR工艺利用逸出的氨气进行催化反应结合起来，从而进一步脱除NOx，是把SNCR低费用的特点同 SCR工艺的高效脱硝率及低的氨逸出率有效结合。该联合工艺于20世纪70年代首次在日本的一座燃油装置上进行试验，试验结果证明该技术是可行的。理论上，SNCR工艺在脱除了部分NOx的同时为后面的SCR催化法提供了所需的NH3。SNCR布置在锅炉烟气出口和省煤器入口间温度为850-950℃左右的温度区域内；SCR反应器布置在改造锅炉上级或者下级省煤器所获得的2.7m-3.5m的尾部烟道空间。\n##### 2、脱硝工艺选择\n##### 对于高温高压循环流化床（手动输入）锅炉，锅炉采用低氮燃烧技术（手动输入）可保证NOx排放浓度大约在80mg/Nm3（手动输入）左右，为了满足a：超低排放50 mg/Nm3的要求，b：SNCR中国《火电厂大气污染排放标准》要求，即NOx排放浓度＜100mg/Nm3。（手动选择）确保锅炉在各个工况下NOx均能达标排放，因此本工程推荐采用a：SNCR脱硝工艺 b：SCR脱硝工艺c:SNCR+SCR联合脱硝工艺，（手动选择）选用a、尿素b、氨水（手动选择）为还原剂。\n##### A：本工程采用SNCR脱硝工艺，采用尿素作为还原剂，经计算，尿素用量约为@@coalchp_desulfurization_denitrification.d_use_urea@@kg/h，尿素溶液浓度按25%考虑，尿素溶液消耗水量约为@@coalchp_desulfurization_denitrification.d_water_urea@@kg/h，尿素仓库存储时间按@@coalchp_desulfurization_denitrification.d_days_urea@@天考虑，尿素最大储量约为@@coalchp_desulfurization_denitrification.d_capacity_urea@@t。\n##### B: 本工程采用SCR脱硝工艺，采用尿素作为还原剂，经计算，尿素用量约为@@@coalchp_desulfurization_denitrification.g_use_urea@@）kg/h，尿素仓库存储时间按@@coalchp_desulfurization_denitrification.d_days_urea@@天考虑，尿素最大储量约为（@@coalchp_desulfurization_denitrification.g_use_urea@@*@@coalchp_desulfurization_denitrification.d_days_urea@@）t。\n##### C: 本工程采用SNCR+SCR脱硝工艺，采用尿素作为还原剂，经计算，尿素用量约为@@coalchp_desulfurization_denitrification.g_use_urea@@+@@coalchp_desulfurization_denitrification.d_use_urea@@）kg/h，尿素仓库存储时间按@@coalchp_desulfurization_denitrification.d_days_urea@@天考虑，尿素最大储量约为（@@coalchp_desulfurization_denitrification.g_use_urea@@*@@coalchp_desulfurization_denitrification.d_days_urea@@+@@coalchp_desulfurization_denitrification.g_use_urea@@）t。\n##### （A/B/C手动选择）\n","id":"j1_37"},{"class":["1","j1_6","j1_36"],"content":"##### 1、脱硫技术介绍\n##### 目前，全世界脱硫工艺共有 100 多种，按其燃烧的过程可分为：燃烧前脱硫、燃烧中脱硫、燃烧后脱硫(烟气脱硫)。\n##### 石灰石—石膏湿法脱硫工艺、氨法脱硫和循环流化床干法脱硫工艺是目前大型火电机组商业应用上最具有代表性的烟气脱硫工艺，下面对这几种脱硫工艺进行简单介绍。\n##### (1) 石灰石—石膏湿法脱硫工艺 \n##### 石灰石—石膏湿法脱硫工艺是采用价廉易得的石灰石作为脱硫吸收剂，石灰石小颗粒经磨细成粉状与水混合搅拌制成吸收浆液。在吸收塔内，吸收浆液与烟气接 触混合，烟气中的 SO2 与浆液中的碳酸钙及鼓入的空气进行氧化反应被脱除，最终反应产物为脱硫石膏。脱硫后的烟气经除雾器除去携带的细小液滴后排入烟囱。\n##### 脱硫石膏浆液经脱水装置脱水后回收，脱硫废水经处理后供电厂除灰系统使用。 根据市场对脱硫石膏的需求，脱硫石膏的质量等因素，对脱硫副产物石膏可以采用抛弃和回收利用两种方式进行处理。\n##### 该工艺适用于任何煤种含硫率的烟气脱硫，脱硫效率可达到 95%以上。石灰石—石膏湿法脱硫工艺由于具有脱硫效率高(Ca/S 大于 1 时，脱硫效率可达 95～98%)、 吸收剂利用率高、技术成熟、运行稳定等特点，因而是目前世界上应用最多的脱硫工艺。在美国、德国和日本，应用该工艺的机组容量约占电厂脱硫机组总容量的 90%，单机容量已达 1000MW。\n##### 在国内，国电费县一期、潍坊二期、邹县三期、广西防城港一期等 300MW～600 级机组等均采用了石灰石－石膏湿法脱硫工艺。已投运的脱硫装置均达到或超过了设计指标，证明了该种脱硫工艺的可靠性。\n##### (2) 氨法脱硫工艺 \n##### 氨法脱硫工艺于上世纪九十年代开始应用于烟气脱硫。在国外，发展氨法的技术商主要有美国环境系统工程公司(GE 氨法)、德国 Lenjets Bischoff 公司、日本钢管公司(NKK 氨法)。氨法脱硫工艺是采用 NH3 做吸收剂除去烟气中的 SO2 的工艺。氨的碱性强于钙基吸收剂；氨吸收烟气中的 SO2 是气—液或气—气反应，反应速率更快、更完全，吸收 剂利用率高，脱硫效率高达 95%以上。另外，其脱硫副产物硫酸铵经过加工后是具有 商业价值的农业肥料。\n##### 从动力学原理来说，氨法实质上是以循环的(NH4)2SO3、NH4HSO3 水溶液吸收 SO2 的 过程。亚硫酸铵对 SO2 具有更好的吸收能力，是氨法中的主要吸收剂。随着亚硫酸氢 铵比例的增大，吸收能力降低，须补充氨水将亚硫酸氢铵转化成亚硫酸铵。\n##### GE 氨法的工艺流程主要分为预洗涤、SO2 吸收、亚硫酸铵氧化和结晶四个工序。 热烟气经电除尘后进入预洗涤塔，与硫酸铵饱和溶液并流接触，烟气被冷却。同时，由于硫酸铵饱和溶液中的水蒸发而析出硫酸铵结晶。来自预吸收塔的已被冷却饱和的烟气经过除雾器进入 SO2 吸收塔，烟气与喷淋而下的稀硫酸铵溶液逆流接触，烟气中的 SO2 在此被吸收。氨气与压缩空气混合进入吸收塔底部浆池，在添加氨的同时氧 化亚硫酸铵。\n##### 在世界的火电厂烟气脱硫市场上，氨法的比例约 1%。当脱硫剂氨的来源充分， 并且副产物硫酸铵有较好的销售市场时，该工艺在运行上才具有经济可行性。\n##### (3) 循环流化床干法脱硫工艺 \n#####循环流化床烟气脱硫属于干法脱硫工艺。循环流化床干法烟气脱硫技术是由德国 Lurgi 公司在 20 世纪 80 年代初开发的，Wulff 公司在此基础上开发了回流式循环流化床烟气脱硫技术(RCFB-FGD)，德国的 Thysseen 公司、美国的 Airpol 公司、法国的 Stein 公司及丹麦 FLS、Miljo 等公司也都在开发和推广该项技术。\n##### 循环流化床烟气脱硫系统主要由吸收剂制备系统、吸收塔、吸收剂再循环系统、 除尘器和控制系统等组成。根据高速烟气与所携带的稠密悬浮颗粒充分接触原理，在吸收塔内喷入消石灰粉使其与烟气充分接触、反应，然后喷入一定量地水，将烟气温度控制在对反应最有利的温度。塔内出去的烟气进入除尘器，除尘器内收集下 来的脱硫灰，小部分排掉，其余的则经循环系统进入吸收塔继续脱硫。吸收塔的底 部为一文丘里装置，烟气流过时被加速并与细小的吸收剂颗粒混合，烟气和吸收剂 颗粒向上运动时，会有一部分烟气产生回流，形成内部湍流，从而增加烟气与吸收剂颗粒的接触时间，提高吸收剂的利用率和系统的脱硫效率。彭城电厂二期 2×300MW、榆社电厂二期 2×300MW 等机组均采用该工艺。\n##### 通过对以上三种典型的烟气脱硫工艺的分析可以看出：氨法脱硫工艺脱硫效率高，运行可靠，但是氨法脱硫受吸收剂供应的制约。另外，氨液脱硫剂的成本高，是钙基脱硫剂价格的十倍以上；副产物如果要加工成有商品价值的农用肥料，还需增加昂贵的后处理设备；所以氨法脱硫受到脱硫剂供给 源和副产物销售市场的很大限制，本工程采用氨法脱硫不具备条件。\n##### 烟气循环流化床脱硫工艺近几年发展迅速,是一种适用于煤种含硫量<0.6%的低 硫煤脱硫；特别适用于机组容量为300MW及以下的中小容量机组脱硫。在西部缺水地 区及脱硫吸收剂(生石灰)来源可靠的地区更为适用。该工艺流程简单，新建和改造 电厂均适用。烟气循环流化床脱硫技术在钙硫比为1.3～1.8的情况下，脱硫效率可达90%以上，可去除烟气中的硫氧化物、HCL、HF、颗粒物和重金属(如汞)；无脱硫废水产生；是一种性能价格比较高的干法烟气脱硫工艺。干法脱硫工艺的脱硫副产物是粉煤灰、消石灰、亚硫酸钙、硫酸钙等组成的混合物。目前，脱硫灰综合利用途径少，商业价值很低，通常只能灰场堆放处理。\n##### 2、脱硫工艺选择\n##### A:本工程采用炉内喷钙脱硫工艺，经计算，石灰石耗量约为@@coalchp_desulfurization_denitrification.r_coco3_consume@@kg/h，石灰石储罐贮存时间按@@coalchp_desulfurization_denitrification.r_storage_time@@天考虑，石灰石储罐体积约为@@coalchp_desulfurization_denitrification.r_storage_volume@@m3，最大储量约为@@coalchp_desulfurization_denitrification.r_storage_output@@kg。\n##### B：本工程采用石灰石-石膏法脱硫工艺，脱硫装置的烟气处理能力按锅炉50～110%BMCR工况时的烟气量，脱硫系统不设置烟气旁路，脱硫工艺尽可能节约能源和水源，降低脱硫系统的投资与运行费用。\n设计脱硫效率脱硫效率≥92.8%@@coalchp_desulfurization_denitrification.s_desulfurization_efficiency@@，脱硫系统SO2入口浓度原设计值为@@coalchp_desulfurization_denitrification.s_no_desulfurization_so2@@ mg/Nm3。经计算，石灰石耗量约为@@coalchp_desulfurization_denitrification.d_limestone_consume@@kg/h，生成CaSO4量为@@coalchp_desulfurization_denitrification.d_gengrate_coca4@@kg/h。 \n##### （A、B手动选择）\n\n\n","id":"j1_38"},{"class":["1","j1_6"],"content":"##### 本工程运煤系统按3×260t/h锅炉容量设计。\n燃料消耗量表\n\n|运行台数 | 燃料种类|小时消耗量（t/h）|日消耗量（t/d） |年消耗量（万吨/a） |\n|:------|:------|:------|:------|:------\n|1台炉（手动输入） | 设计煤种|@@coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_design@@ | @@coalchp_coal_handingsystem.b_coal_daily_consumption_design@@|@@coalchp_coal_handingsystem.b_coal_annual_consumption_design@@ |\n|X台炉 | 设计煤种| | | |\n\t\t\n##### 注：\n##### 1) 燃煤粒度：a ≤200mm\n##### 2).散状密度： ～0.9t/m3（破碎后、入炉前）\n##### 3) 日利用小时数按22h计；\n##### 4) 年利用小时数按7260h计。\n","id":"j1_39"},{"class":["1","j1_6","j1_39"],"content":"##### 自厂内卸煤装置卸车开始一直到将原煤运入锅炉房原煤仓的整个工艺系统,其中包括煤场煤篦子下的地下煤斗、与破碎和筛分破碎装置、运输设备以及输煤系统中的计量、保护、除铁等其它辅助设备和附属建筑。","id":"j1_40"},{"class":["1","j1_6","j1_39"],"content":"##### （1） 输煤系统设置均按1炉（手动输入）最终容量考虑。\n##### （2）贮煤场和干煤棚总储量满足单台100t/h（手动输入）锅炉10天（按设计煤种）的用量，全部采用自卸汽车（手动输入）进厂。\n##### （3）本期工程筛碎系统按一级筛分一级破碎设计。采用双路布置，满足运行的条件。\n##### （4）输煤栈桥为封闭布置。\n##### （5）输煤系统的控制布置在输煤综合楼内。","id":"j1_41"},{"class":["1","j1_6","j1_39"],"content":"##### 1.卸煤装置\n##### 燃煤的运输方式采用公路载重汽车(尽量采用自卸汽车)运输进厂。若日来煤量按不均衡系数@@coalchp_coal_handingsystem.b_daily_coal_unbalanced_coefficient_design@@考虑，则日最大来煤量@@coalchp_coal_handingsystem.b_daily_rail_coal_amount_design@@ t，自卸汽车平均载重量暂按@@coalchp_coal_handingsystem.t_vehicle_capacity_tonnage_design@@ t计，自卸汽车工作时间按每昼夜@@coalchp_coal_handingsystem.t_daily_working_hours_design@@小时计，一天有@@coalchp_coal_handingsystem.t_vehicle_daily_incoming_times_design@@（次）车次进厂卸煤。每小时有约@@coalchp_coal_handingsystem.t_vehicle_perhour_incoming_times_design@@辆。 \n##### 2.储煤场及煤场设备\n##### 本工程的储煤场设置一座@@coalchp_coal_handingsystem.c_height_design@@m×@@coalchp_coal_handingsystem.c_width_design@@m= @@coalchp_coal_handingsystem.c_coalyard_area_design@@m2干煤棚，在煤场主要用推煤机和装载机向地下进煤斗供煤。储煤场堆煤高度@@coalchp_coal_handingsystem.c_coal_height_design@@m计，总储煤量@@coalchp_coal_handingsystem.t_vehicle_daily_incoming_times_design@@吨。可满足动力站@@coalchp_coal_handingsystem.c_coal_store_days_design@@天的锅炉燃煤量。\n##### 干煤棚采用简易钢结构形式，防止煤尘污染四周设置挡风墙。煤场设备配两台推煤机，作为堆煤、压实、整理、煤场翻烧等作业。","id":"j1_42"},{"class":["1","j1_6","j1_39"],"content":"##### 1.筛碎设备\n##### 本期工程筛碎系统双路布置，一路运行，一路备用。筛碎设备选型为：筛煤机出力为@@coalchp_coal_handingsystem.s_transportsystem_output_check@@t/h，入料粒度≤200mm，筛下物粒度≤10mm；可逆细碎机出力50t/h，入料粒度≤200mm，出料粒度≤10mm；","id":"j1_43"},{"class":["1","j1_6","j1_39"],"content":"##### 1.上煤系统 \n#####     从煤场至主场房的带式输送机系统为一路布置。（手动输入）带式输送机的规格为带宽B＝@@coalchp_coal_handingsystem.s_belt_width_check@@mm，带速V=@@coalchp_coal_handingsystem.s_belt_speed_check@@m/s，出力Q=@@coalchp_coal_handingsystem.s_transportsystem_output_check@@t/h。从副跨上煤，煤仓层采用可变槽角电动犁式卸料器卸料。\n##### 本期工程上煤系统日运行时间约为@@coalchp_coal_handingsystem.s_belt_width_check@@小时，2班（手动输入）制运行。\n##### 2.控制方式\n##### 输煤系统逆煤流起动，顺煤流停机，控制采用可编程序控制和就地操作两种方式，为了保证运煤系统能安全、可靠的运行，运煤系统主要运行设备均互相连锁，带式输送机设有：打滑检测装置；纵向撕裂保护装置；跑偏信号；双向拉绳开关；煤流信号；堵煤信号以及煤仓间料位计等。\n##### 输煤系统设有下列保护信号：\n##### A）煤流信号：监测胶带载煤情况。\n##### B）速度信号：用以监测胶带运行速度以控制带式输送机的启停。\n##### C）防跑偏信号：当带式输送机跑偏时发出警报信号，仍继续跑偏至过限时停机。\n##### D）拉线开关：当带式输送机沿线发生设备或其他事故时，可在胶带沿线任何位置拉线停机。\n##### E）高低料位信号：用以监测原煤仓料位的高低。\n##### F）堵煤信号\n##### G）纵向防撕裂信号","id":"j1_44"},{"class":["1","j1_6","j1_39"],"content":"##### （1）输煤系统设2级除铁器，除铁点的建筑设施内均设有弃铁箱，将清除的铁杂质收集。\n##### （2）煤仓层2号甲乙带式输送机上的卸料装置采用B＝@@coalchp_coal_handingsystem.s_belt_width_check@@mm电动双侧犁式卸料器。\n##### （3）计量装置：入炉煤计量装置采用电子皮带秤，为校核其精度，在1号皮带机上设有全动态链码校验装置。为高效、准确检测供煤质量，维护电厂利益，在煤场设汽车入厂煤计量采用2台电子汽车衡即入场煤采样装置。在1号带式输送机前中部装有2台入炉煤采样装置，以检测入炉煤是否满足锅炉运行要求。\n##### （4）预破碎室、碎煤机室及转运站均设有起吊设备，以满足检修的需要。\n##### （5）输煤系统设置输煤综合楼，除布置输煤配电控制外，还设有输煤办公室、洗浴、卫生间等配套设施。","id":"j1_45"},{"class":["1","j1_6"],"content":"","id":"j1_46"},{"class":["1","j1_6","j1_46"],"content":"##### 除灰渣系统采用“灰渣分除”的设计原则，充分考虑当地自然条件，最大限度实现节水和少占地的设计目标，并为灰渣综合利用创造条件，同时考虑减少灰渣运输过程中产生的污染，降低工程造价、提高自动化水平，达到安全、稳定、可靠运行之目的。\n##### 灰渣量\n\n| 灰渣量 |灰渣量 |小时灰渣量(t/h) |小时灰渣量(t/h) |小时灰渣量(t/h) |日灰渣量(t/d) |日灰渣量(t/d) |日灰渣量(t/d) |年灰渣量(万t/a) |年灰渣量(万t/a) |年灰渣量(万t/a) |\n|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|\n| 灰渣量 |灰渣量 |灰渣 |灰 |渣 |灰渣 |灰 |渣 |灰渣 |灰 |渣 |\n| 设计煤种 |单台 |coalCHP[0] |@@coalchp_furnace_calculation.d_ash_total_design @@ |@@coalchp_furnace_calculation.d_dust_total_design@@ |coalCHP[1]|coalCHP[2] |coalCHP[3] |coalCHP[5] |coalCHP[6] |coalCHP[4] |\n\n##### 注：日运行小时按22小时，年达行小时数按7260小时（手动输入）计算。\n##### 灰渣比按7:3(手动输入)考虑","id":"j1_47"},{"class":["1","j1_6","j1_46"],"content":"##### 锅炉排出的热渣经冷渣器冷却后，排入链斗输渣机，最终由斗式提升机将炉渣送入钢制渣仓临时储存。每个渣仓卸料平台设一台散装机和一台双轴搅拌机装汽车外运到砖厂综合利用或运至灰渣场临时储存。\n##### 每台锅炉设1套链斗输渣机，（手动输入）除渣系统设备出力按不小于锅炉排渣量的250%设计，即单套系统设备出力为@@coalchp_removal_ash_slag_system.s_slag_removal_system@@t/h。\n##### 动力站共设1座直径@@coalchp_removal_ash_slag_system.s_dia@@数据m、有效容积@@coalchp_removal_ash_slag_system.s_slag_removal_system@@m³钢渣仓，可储存2（手动输入）台锅炉@@coalchp_removal_ash_slag_system.s_sludge_time@@天的排渣量。\n##### 除渣系统工艺流程：锅炉→冷渣器→带式输送机（1#）→带式输送机（2#）→斗提机→钢渣仓→干式散装机（或双轴搅拌机）→罐装车（或自卸汽车）→砖厂（或灰渣场）。","id":"j1_48"},{"class":["1","j1_6","j1_46"],"content":"##### 本工程采用正压浓相气力除灰系统，通过管道将锅炉飞灰输送至新建混凝土灰库临时储存，定期由密封罐车（干灰）或自卸汽车（湿灰）外运综合利用。\n##### 除灰系统输送用气及仪用气从化工压缩空气总体管网引接，压力为0.5-0.7MPa。\n##### 本工程气力除灰系统出力按锅炉除尘器最大排灰量的@@coalchp_removal_ash_slag_system.r_removal_coefficient@@%考虑，即单台炉除灰系统出力为@@coalchp_removal_ash_slag_system.r_removal_the_ash_system@@t/h。\n##### 全厂共设2（手动输入）座直径@@coalchp_removal_ash_slag_system.r_dia@@米有效容积为@@coalchp_removal_ash_slag_system.r_effective_volume_ash_storage@@m³的混凝土灰库，可储存2台（手动输入）锅炉同时满负荷运行工况下@@coalchp_removal_ash_slag_system.r_stored_ash@@天的排灰量。灰库卸料平台分别设有干灰散装机和双轴加湿搅拌机。用干灰时可通过干灰散装机将灰装密封罐车运至水泥厂、制砖厂等进行综合利用；不考虑干灰利用时，可由双轴加湿搅拌机加喷淋后再由自卸汽车将湿灰运到灰渣场碾压堆放。\n##### 系统流程：电袋复合式除尘器灰斗→手动插板阀→进料阀→仓泵（压力输送罐）→出料阀→输灰管道→灰库。","id":"j1_49"},{"class":["1","j1_6","j1_51"],"content":"##### 1、本工程的化学水处理系统补充水水源来自安瑞佳现有水网、生产供水管网。（手动输入）\n##### 2、原水水质\n##### 原水水质分析表（手动输入）\n\n| 序号 |分 析 项 目 |符号 |单 位 |数值 |\n|:------|:------|:------|:------|:------|\n| 1 |氨氮 | |毫克/升 |0.03 |\n| 2 |氨 | |毫克/升 |<0.1 |\n| 3 |悬浮物 | |毫克/升 |1.2 |\n| 4 |氟化物 | |毫克/升 |0.3 |\n| 5 |硝酸根 | |毫克/升 |0.28 |\n| 6 |酸度 | |毫摩尔/升 |未检出 |\n| 7 |硬度 | |毫克/升（以CaCO3计) |40.4 |\n| 8 |暂时硬度 | |毫摩尔/升 |0.807 |\n| 9 |永久硬度 | |毫摩尔/升 |0 |\n| 10 |负硬度 | |毫摩尔/升 |4.29 |\n| 11 |总碱度 | |毫克/升（以CaCO3计) |255 |\n| 12 |pH | |/ |8.51 |\n| 13 |化学需氧量(锰） | |毫克/升 |0.65 |\n| 14 |全硅 | |毫克/升 |12.1 |\n| 15 |活性硅 | |毫克/升（以SiO2计） |10.9 |\n| 16 |全固 | |毫克/升 |398 |\n| 17 |溶解性固体 | |毫克/升 |374 |\n| 18 |菌落总数 | |CFU/mL |1 |\n| 19 |总大肠菌群 | |MPN/100mL |未检出 |\n| 20 |钾 | |毫克/升 |0.6 |\n| 21 |钠 |Na+ |毫克/升 |140 |\n| 22 |钙 |Ca2+ |毫克/升（以CaCO3计） |35.4 |\n| 22 |镁 |Mg2+ | |5 |\n| 24 |总铁 | |毫克/升 |0.34 |\n| 25 |全铝 | |毫克/升 |0.224 |\n| 26 |HCO3- | |毫克/升 |262 |\n| 27 |CO32- | |毫克/升 |24 |\n| 28 |OH- | |毫克/升 |0 |\n| 29 |SiO32- | |毫克/升 |13.8 |\n| 30 |硫酸盐 | |毫克/升 |11 |\n| 31 |氯离子 | |毫克/升 |37.6 |\n| 32 |阳离子合计 | |毫摩尔/升 |6.94 |\n| 33 |阴离子合计 | |毫摩尔/升 |6.75 |\n| 34 |离子分析误差 | |　 |1.4% |\n| 35 |溶解固体误差 | |　 |0% |\n","id":"j1_50"},{"class":["1","j1_6"],"content":"","id":"j1_51"},{"class":["1","j1_6","j1_51"],"content":"##### 根据GB/T12145-2008标准要求，本工程选用机、炉的给水、炉水、蒸汽质量标准为：\n##### 给水水质要求：（A、中温中压 B、高温高压 手动选择）\n#####  A：中温中压\n#####   锅炉给水质量标准\n\n| 项    目 |单    位 |数    值 |\n|:------|:------|:------|\n|硬度|μmol/L|≤2.0|\n|溶氧(O2)|μg/L|≤15|\n|铁(Fe)|\tμg/L|≤50|\n|铜(Cu)|μg/L|≤10|\n|PH值(25℃)||8.8-9.3|\n##### 蒸汽质量标准\n\n| 项    目 |单    位 |数    值 |\n|:------|:------|:------|\n| 钠 |μg/kg |≤15 |\n| 二氧化硅(SiO2) |μg/kg |≤20 |\n| 铁 |μg/kg |≤20 |\n| 铜 |μg/kg |≤5 |\n| 氢电导率(25℃) |μs/cm |≤0.3 |\n##### 炉水质量标准\n\n| 项    目 |单    位 |数    值 |\n|:------|:------|:------\n|磷酸根|mg/L|5~15|\n| PH| |9~11 |\n\n##### 凝结水质量标准\n\n| 项    目 |单    位 |数    值 |\n|:------|:------|:------\n|硬度|μmol/L|≤2.0|\n|溶氧(O2)|μg/L|≤50|\n\nB：高温高压\n#####   锅炉给水质量标准\n\n| 项    目 |单    位 |数    值 |\n|:------|:------|:------|\n|溶氧(O2)|μg/L|≤7|\n|铁(Fe)|\tμg/L|≤30|\n|铜(Cu)|μg/L|≤5|\n|氢电导率(25℃)|μs/cm|≤0.30|\n|PH值(25℃)||8.8-9.3|\n\n##### 蒸汽质量标准\n\n| 项    目 |单    位 |数    值 |\n|:------|:------|:------|\n|钠|μg/kg|\t≤5|\n|二氧化硅(SiO2)|μg/kg|≤20|\n|铁|μg/kg|≤15|\n|铜|μg/kg|≤3|\n|氢电导率(25℃)|μs/cm|≤0.15|\n##### 炉水质量标准\n\n| 项    目 |单    位 |数    值 |\n|:------|:------|:------\n|磷酸根|mg/L|2～10|\n|PH||9 ~10.5 |\n|二氧化硅(SiO2)|μg/kg|≤2|\n|电导率(25℃)|μs/cm|≤150|\n\n##### 凝结水质量标准\n\n| 项    目 |单    位 |数    值 |\n|:------|:------|:------\n|硬度|μmol/L|≤1|\n|溶氧(O2)|μg/L|≤50|\n|氢电导率(25℃)|μs/cm|≤0.3|\n","id":"j1_52"},{"class":["1","j1_6","j1_51"],"content":"##### （1）除盐水工艺流程：（a、b手动选择）\n##### a、多介质过滤器+超滤装置+两级反渗透装置+EDI处理\n##### 水源来水→原水箱→原水泵→多介质过滤器→活性炭过滤器→保安过滤器→高压泵→反渗透装置→除二氧化碳器→中间水箱→中间水泵→混合离子交换器→除盐水箱→除盐水泵→各用水点。\n特点：设备先进，自动化程度高，运行可靠，但投资大。\n##### b、多介质过滤器+反渗透装置+混床处理\n##### 清水池→生水泵→换热器→多介质过滤器→精密过滤器→超滤装置→超滤水池→超滤水泵→一级保安过滤器→一级高压泵→一级反渗透装置→中间水池→中间水泵→二级保安过滤器→二级高压泵→二级反渗透装置→RO产水池 →EDI供水泵→EDI装置→除盐水箱→除盐水泵→主厂房\n##### 特点：运行安全可靠，投资省，但有酸碱废水产生。\n#####（2）\t凝结水处理工艺流程\n##### 工艺回水经过除油除铁过滤器后进入除盐水箱\n","id":"j1_53"},{"class":["1","j1_6","j1_51"],"content":"##### 本工程正常水汽损失量：\n\n| 序号 |损失类别 |正常损失 |损失数值t/h |\n|:------|:------|:------|:------|\n| 1 |厂内水、汽系统循环损失 |锅炉额定蒸发量的3% |@@coalchp_boiler_auxiliaries.m_steamwater_cycle_loss@@|\n| 2 |汽包锅炉排污损失 |锅炉额定蒸发9量的2% |@@coalchp_boiler_auxiliaries.m_pollution_loss@@ |\n| 3 |对外供汽损失 | |30（手动输入） |\n| 4 |其他除盐水用量 | |5（手动输入） |\n| 5 |启动/事故用水量 |锅炉额定蒸发量的10% |@@coalchp_boiler_auxiliaries.m_increase_loss@@ |\n| 6 |锅炉正常情况下最大补水量 | |40（设置公式，1-4数值相加） |\n| 7 |锅炉启动/事故情况下最大补水量 | |40（设置公式，1-5数值相加） |\n\n##### 考虑到设备运行效率和低压管网换水情况，本化水站的系统出力按2×15t/h（手动输入）进行设计，机组起动或事故时补给水，可以通过调节流量和室外的除盐水箱的水位来满足要求。","id":"j1_54"},{"class":["1","j1_6"],"content":"","id":"j1_55"},{"class":["1","j1_6","j1_55"],"content":"##### 本项目由甲方供水至电站界区，确保与电站用水要求。","id":"j1_56"},{"class":["1","j1_6","j1_55"],"content":"##### 循环冷却水系统由厂区工业新水进行补水；","id":"j1_57"},{"class":["1","j1_6","j1_55"],"content":"##### 1、循环冷却水系统设施、设备\n##### 汽轮机冷凝器冷却水系统采用开式循环冷却供水方式。凝汽器、发电机空冷器冷却水直接取自循环冷却水进水母管，使用后进入循环冷却水排水母管。油冷却器冷却水直接回至循环水池。\n##### 主厂房内其它需要冷却的设备，如风机轴承冷却等采用工业水冷却。为了充分节约用水，且避免冷却水管道结垢阻塞，取样冷却器考虑采用小型闭式循环冷却水装置进行冷却。\n##### 根据本工程水源条件，循环冷却水系统冷却设备选用a、自然通风双曲线冷却塔；b、逆流式机械通风冷却塔。（a、b手动选择）\n##### 循环冷却水供水系统流程为：a、双曲线冷却塔；b、机械通风冷却塔集水池→循环水回水管→循环水泵房吸水井→循环水泵房→循环水供水压力管→凝汽器、空气冷却器、冷油器→循环水排水压力管→a、双曲线冷却塔；b、机械通风冷却塔→a、双曲线冷却塔；b、机械通风冷却塔集水池。（a、b手动选择）\n##### 本工程为机组配置a、1座XXXm2的自然通风冷却塔；b、nxXXXm³逆流式机械通风冷却塔（a、b手动选择）及3台循环水泵以满足机组夏季最严苛工况下的循环冷却水要求。循环水泵参数：流量Q=XXXXm³/h，（手动输入）扬程H=（常规取值范围：25~28）（手动输入）m，两台运行，一台备用，以适应夏季、冬季循环水量的变化。循环水泵安装在循环水泵房内。  \n##### 2、循环水量\n##### 根据当地气象条件，经循环供水系统初步计算，夏季循环水冷却倍率采用@@coalchp_circulating_water.v_circulating_ratio_summer@@倍，冬季采用@@coalchp_circulating_water.v_circulating_ratio_winter@@倍，循环供水系统水量见下表：\n##### 循环水量统计表\n\n| 机组容量 |凝汽量(t/h) |凝汽器循环冷却水量(t/h) |凝汽器循环冷却水量(t/h) |辅机循环冷却水量(t/h) |总循环水量(m3/h) |总循环水量(m3/h) |\n|:------|:------|:------|:------|:------|:------|:------|\n| 机组容量 |凝汽量(t/h) |夏季 |冬季 | 辅机循环冷却水量(t/h) |夏季 |冬季 |\n| 65MW（手动输入） |@@coalchp_circulating_water.v_steam_exhaust_flow_select@@|@@coalchp_circulating_water.v_circulating_water_summer@@|@@coalchp_circulating_water.v_circulating_water_winter@@ |@@coalchp_circulating_water.v_auxiliary_engine_cooling_summer@@ |@@coalchp_circulating_water.v_total_circulating_water_summer@@|@@coalchp_circulating_water.v_total_circulating_water_winter@@ |\n\n##### 3、工业循环水补水量\n##### 循环冷却水补给水量计算结果表\n\n| 项目 |需水量（m3/h） |回收水量（m3/h） |补给水量（m3/h） |\n|:------|:------|:------|:------|\n| 冷却塔蒸发损失 |@@coalchp_circulating_water.v_evaporation_loss@@|0 |@@coalchp_circulating_water.v_amount_of_makeup_water_summer@@ |\n| 冷却塔风吹及飞溅损失 |@@coalchp_circulating_water.v_partial_blow_loss@@ |0 |@@coalchp_circulating_water.v_amount_of_makeup_water_summer@@|\n| 排污及渗漏损失 |@@coalchp_circulating_water.v_discharge_capacity@@|0 |@@coalchp_circulating_water.v_amount_of_makeup_water_summer@@ |\n| 合计 |@@coalchp_circulating_water.v_total_circulating_water_summer@@ | |@@coalchp_circulating_water.v_amount_of_makeup_water_summer@@ |\n","id":"j1_58"},{"class":["1","j1_6","j1_55"],"content":"##### 电厂排水包括生活污水、厂区雨水、非经常性的生产排水等废水。厂区排水分三个系统：生活污水排水系统、厂区雨水排水系统及生产废水排水系统。\n##### 生活污水排水系统包括：厂区内生产建（构）筑物、附属、辅助建筑物的生活污水排水，冲洗设施排水。生活污水经二级生化处理、冲洗废水经隔油池处理后满足国标《污水综合排放标准》中规定的要求，通过厂区内生活污水排水系统排入地下管网。\n##### 厂区雨水及生产废水排水系统包括：各建筑物屋面及场地雨水排水、厂区各种道路的排水。各建筑物屋面及各种道路均设有雨水口，道路一侧设有雨水管道，地面及道路雨水经雨水口排入雨水管道。非经常性的生产排水包括泵类及水管道阀门等设备的检修临时排水，这部分排水水质较好，直接排到厂区雨水排水管道。","id":"j1_59"},{"class":["1","j1_6"],"content":"","id":"j1_60"},{"class":["1","j1_6","j1_60"],"content":"##### 该电站将在拟建的电站主厂房区域配置两套10/0.4kV低压厂用变压器，以0.4kV配电压向拟建电站低压负荷供电。","id":"j1_61"},{"class":["1","j1_6","j1_60"],"content":"##### 发电机装机容量：手动输入\n\n| 名称 |单位 |数值 |\n|:------|:------|:------|\n| 装机容量 |kW |30000 |\n| 功率因数 | |0.8 |\n","id":"j1_62"},{"class":["1","j1_6","j1_60"],"content":"##### 站用电负荷包括锅炉辅机、汽轮机辅机等高、低压负荷。","id":"j1_63"},{"class":["1","j1_6","j1_60"],"content":"##### 电站系统只在电力供应正常时、利用生产过程中产生的可回收热能进行发电。其性质决定，电站所发电能只占厂区用电量的很小部分。电能不会馈送到外电网，只是减少了工厂的外购电量。\n##### 电站属于小型自备电站。电站10.5kV系统与上级10.5kV 系统联网。\n##### 电站站用电负荷的起动电源由发包人提供(用电负荷由总承包单位提供给发包方）；电站并网后，发电机向上级10.5kV系统馈送电能。","id":"j1_64"},{"class":["1","j1_6","j1_60"],"content":"##### 电站I段作为母线联络电源，II段进线柜通过电缆与发包人上级变电站10.5kV系统联接。\n##### 在发电机小室设置发电机出口PT一台，用于检测发电机出口电压及频率；在10.5kV系统母线设置PT柜一台，用于检测系统电压及频率；在电站10.5kV系统母线设置馈电柜，分别向锅炉辅机供电；电站备用馈电柜二台，用于发包人后续其他馈电要求。\n##### 同期点设置在发电机并网柜。\n##### 计算机系统及其它重要负荷设直流屏逆变电源。\n##### 低压电动机设现场和DCS两地起停（现场操作不通过DCS）。煤气区域采用防爆箱，其他区域采用“三防箱”。","id":"j1_65"},{"class":["1","j1_6","j1_60"],"content":"##### 低压厂用电电压0.4/0.22kV由厂用变供电。380V母线采用单母线分段接线方式。\n##### 电站主厂房内辅机设备用电的工作电源均由厂用变10.5/0.4kV低压侧提供。","id":"j1_66"},{"class":["1","j1_6","j1_60"],"content":"##### 10kV高压配电装置、380V低压配电装置分列布置在主厂房一层。机、炉、电集中控制室布置在主厂房二层。发电机出线小室布置在主厂房汽机间一层，装有发电机端PT及出线隔离开关。","id":"j1_67"},{"class":["1","j1_6","j1_60"],"content":"##### 电机保护：\n##### 电机纵差保护\n##### 电机复合电压过电流保护\n##### 电机定子接地保护 \n##### 发电机失磁保护 \n##### 电机定子绕组过负荷保护等\n##### 10kV联络线保护：\n##### 光纤纵差保护 减免，\n##### 方向过电流保护\n##### 零序过流保护\n##### 单相接地保护 \n##### 复合电压闭锁过流保护\n##### 低频低压解列\n##### 干式低压厂用变压器：\n##### 限时速断保护 \n##### 过流保护（带定时限和反时限）\n##### 温度保护 \n##### 单相接地保护 \n##### 低压侧零序过流保护\n##### 电站内涉及电能馈电、授电的主要口设置带远传功能的电度表。","id":"j1_68"},{"class":["1","j1_6","j1_60"],"content":"##### 电动机、厂用变压器、10kV电源线路等元件及线路的控制设在机炉集控室内；厂用变压器、10kV电源线路、10kV高压电动机等采用综合保护装置，设在就地高压开关柜上，并配有微机“五防”装置1套。煤气区域采用防爆箱，其它区域采用“三防箱”。\n##### 在集控室的微机监控系统操作电脑上通过鼠标和键盘可对上述元件及线路进行控制和操作。锅炉给水泵采用软启动。","id":"j1_69"},{"class":["1","j1_6","j1_60"],"content":"##### 主厂房工作照明电源由380/220V低压工作段引接。辅助厂房的工作照明由与其系统相对应的动力箱引接。正常照明主干线路应采用三相五线制系统。\n##### 事故照明采用自带蓄电池的应急灯。主厂房内、主厂房出入口、通道等需要确保人员安全疏散口处，设有安全标志灯即疏散照明。\n##### 主厂房内采用固定的三相五线制电源树干形低压检修网络，检修箱电源分别由低压段回路供电。各辅助建筑物检修由附近动力箱供电。辅助厂房的正常照明由与其系统相对应的配电箱引接。\n##### 锅炉本体内检修用照明电源电压为36V，设有220/36V行灯变压器，由锅炉本体照明配电箱供电。","id":"j1_70"},{"class":["1","j1_6","j1_60"],"content":"##### 1、防雷\n##### 根据中国国家标准《建筑物防雷设计规范》，电站按三类防雷建筑物进行防雷接地设计。主厂房屋面敷设避雷带作为接闪器，经引下线与接地网相接。对于室外高于15m的钢构架，将钢构物（壁厚合乎规定）作防雷接闪器，各部件之间连成电气通路后，直接将钢构架底部与接地网相接。本项目接地采用复合接地网。水平接地体采用镀锌扁钢，垂直接地极采用镀锌钢管。\n##### 电站10.5kV系统母线、发电机出口及发电机中性点均按要求设置专用避雷器。\n##### 2、接地\n##### 沿主厂房四周设置闭合状接地网。防雷接地、工作接地、保护接地共用一个接地网，接地电阻≤4Ω。\n##### 电气接地系统：10.5kV高压系统采用 IT 接地系统；0.4kV低压系统采用TN-C-S接地系统。\n##### 自动化控制系统设单独接地，不得与其他接地混接。\n##### 3、电缆敷设及防火\n##### 本工程电缆敷设采用电缆夹层、电缆沟、电缆桥架及局部穿管埋设等敷设方式。\n##### 高压室、低压室至主厂房内相关电气设备的电缆，均通过电缆沟或电缆桥架敷设。\n##### 为预防电气火灾蔓延，在高压室、低压室及主控室的电缆进出口处、各配电装置通向屋外的接口处，均采用耐火阻燃材料进行阻燃隔断；高压电缆敷设区域按规范设置阻燃隔断。","id":"j1_71"},{"class":["1","j1_6","j1_60"],"content":"##### 全厂设1套蓄电池组（根据设计选型），采用N+1冗余方式配置高频充电模块，220V母线采用单母线接线，为直流动力负荷，220V逆变电源供控制系统。","id":"j1_72"},{"class":["1","j1_6"],"content":"","id":"j1_73"},{"class":["1","j1_6","j1_73"],"content":"##### 1.自动化水平\n##### 给水调节采用全程调节，其它回路的自动调节范围将按在最低稳燃负荷以上设计，顺序控制系统按子组级设计。\n##### 2.控制方式\n##### ① 控制系统采用以微处理器为基础的分散控制系统DCS（包括DAS、MCS、 SCS 、FSSS）对锅炉、汽机、重要辅机等进行监控,运行人员在控制室以DCS为监控中心实现对机组的启/停、正常运行的监视,调整以及机组异常与事故工况的处理。\n##### ② 控制室不设后备监控设备和常规显示仪表。保留少数独立于DCS的硬接线紧急停炉、停机等硬手操设备，以及几项重要参数显示仪表,以确保在DCS系统故障时的安全停机。设置汽包水位和炉膛火焰电视系统。\n##### ③ 本工程按炉、电合设一个集中控制室设计，机炉电集中控制室内的运行组织应按炉电操作员设岗。\n##### ④ 除灰系统、空压机系统控制采用可编程序控制器（PLC）＋上位机的监控模式，与除尘系统合用控制室，均采用PLC控制，值班员单独进行监控，调试期间或运行初期也可在各车间就地进行监控。其它辅助车间采用就地控制方式或根据具体情况纳入就近的PLC控制。\n##### ⑤ 锅炉吹灰系统、捞渣输渣系统纳入DCS进行监控。\n##### ⑥ 循环水系统纳入DCS进行监控。\n##### ⑦  脱硫、脱硝采用程控系统，由设备厂家统一成套系统集成，集中布置在炉后脱硫脱硝除尘控制室，锅炉烟气在线监测系统(CEMS)信号送集中控制室DCS系统，另外烟气在线监测系统(CEMS)系统预留至环保部门的信号接口。\n##### 3.控制室布置\n##### 集中控制室及电子设备间布置\n##### 本工程采用炉、电集中控制室及除氧给水等共用一个集中控制室。集中控制室及电子设备间位于附属框架内，3~12号柱之间，地坪标高7.0米，与汽机运转层同标高，控制室净空不小于3.2米。控制室布置有分散控制系统操作站和DEH操作站等。在控制室左侧布置有电子设备间，布置有DCS工程师站，DCS、DEH、ETS、TSI、FSSS等程控等机柜及机炉电动门及调节阀配电柜。集中控制室（包括电子设备间）的面积约为480平方米。集中控制室相应位置下标高4.2米层设有梁下净空不小于2.5米的电缆夹层。集控室（包括电子设备间）采用柜式空调设备。\n##### 4.控制系统的总体结构\n##### 分散控制系统(DCS)包括数据采集系统（DAS）、模拟量控制系统（MCS）、顺序控制系统（SCS）、锅炉安全监控系统（FSSS）等。\n##### 5.控制系统的可靠性\n##### 保证控制系统可靠性的措施：\n##### 分散控制系统中通讯、网络接口、控制器的DPU均采用冗余配置。\n##### 用于调节、保护用的重要信号如炉膛负压、汽包水位等采用三取二原则。\n##### 设计有完善的自诊断功能。\n##### 电源系统采用冗余供电方式，其中一路为UPS。\n##### 各控制系统控制总线全部采用冗余配置。\n##### 主要控制设备的可靠性指标：\n##### 分散控制系统（包括软、硬件）\n##### 数据采集（DAS） MTBF>8600h\n##### 可用率>99.9%（考核时间为90天）","id":"j1_74"},{"class":["1","j1_6","j1_73"],"content":"##### 1.分散控制系统（DCS）功能：\n##### 数据采集系统（DAS）：\n##### DAS系统是机组安全运行的主要手段，具有高度的可靠性和实时响应能力，能够连续监视机组的各种运行参数，提供完整的报警信息，对所有输入信号进行处理。其主要功能如下：\n##### 显示功能：包括操作显示、标准画面显示（如成组显示、棒状图显示、趋势显示、报警显示等） 、模拟图显示、系统显示、帮助显示等。\n##### 记录显示：包括定期记录、运行人员操作记录、事故顺序记录（SOE） 、事故追忆记录、设备运行记录等。\n##### 历史数据存储和检索。\n##### 性能计算：提供在线计算能力，计算机, 炉及辅机的各种效率及性能参数，计算值及中间计算值应有打印记录，并能在CRT上显示。\n##### 模拟量控制系统（MCS）：\n##### MCS系统主要满足机组安全启、停运行的要求，保证机在最低稳燃负荷至100%MCR负荷范围内，控制机组运行参数不超过允许值； \n##### 锅炉自动调节系统主要包括: \n##### 锅炉燃料调节系统\n##### 锅炉燃烧调节系统\n##### 锅炉送风调节系统\n##### 锅炉给水调节系统\n##### 锅炉主汽温度调节系统\n##### 锅炉炉膛压力调节系统\n##### 锅炉燃油压力调节系统等。\n##### 顺序控制系统（SCS）：\n##### 顺序控制系统作为DCS的一部分，完成炉、电及其辅机的启停顺序控制。对于运行中经常操作的辅机、阀门及挡板，启动过程和事故处理需要及时操作的辅机、阀门及挡板，通过顺序控制系统SCS实现。本工程仅设子组级控制。SCS系统主要包括以下子组：\n##### 锅炉过热蒸汽压力保护控制功能组\n##### 一次风机控制功能组\n##### 二次风机控制功能组\n##### 返料风机控制功能组\n##### 引风机控制功能组\n##### 给煤机控制功能组\n##### 电动给水泵顺序控制功能组\n#####      每个顺序控制功能组,可根据运行人员指令在顺控进行中修改、跳跃或中断。运行人员可按照功能组启停,也可以单台设备在操作站软手操，且具有不同层次的操作许可条件，以防误操作。\n##### 炉膛安全监控系统（FSSS）：\n#####      炉膛安全监控系统（FSSS）包括燃烧器控制和燃料安全系统，是为保证循环流化床锅炉启动和切除燃烧设备中执行的安全的操作程序，其主要功能有：\n##### ·炉膛吹扫\n##### ·燃油系统吹扫\n##### ·燃油泄漏试验\n##### ·点火器及油枪切投控制\n##### ·火焰监视及炉膛灭火保护\n##### ·火检冷却风机控制\n##### ·主燃料跳闸MFT\n##### 其它联锁及监视项目","id":"j1_75"},{"class":["1","j1_6","j1_73"],"content":"##### 1.热工保护\n##### 保护系统的功能是从机组整体出发，使炉、机各辅机之间相互配合，及时处理异常工况或用闭锁条件限制异常工况发生，避免事故扩大或防止误操作，保证人身和设备的安全。主要设以下保护项目（由DCS实现）：\n##### 锅炉本体保护\n##### 1）当发生下列条件之一时，锅炉MFT\n##### ·送风机全停\n##### ·引风机全停\n##### ·汽包水位高三值\n##### ·汽包水位低三值\n##### ·炉膛压力高\n##### ·炉膛压力低\n##### ·全炉膛火焰消失\n##### ·全燃料消失\n##### ·手动停炉\n##### 2）主汽压力保护\n##### 主汽压力保护通过安装在过热蒸汽集箱的脉冲式安全阀来实现。\n##### 重要回路冗余设计\n##### 重要的一次信号如炉膛负压、汽包水位等均采用三取二逻辑。\n##### 2.热工报警\n##### 每台机组在辅助控制盘上设有热工（含电气）信号报警窗。热工报警主要包括下列内容：\n##### 工艺参数越限。\n##### 热工保护动作及主要辅助设备故障。\n##### 热工监控系统故障。\n##### 热工电源故障。\n##### 主要电气设备故障。\n##### 辅助系统故障。","id":"j1_76"},{"class":["1","j1_6","j1_73"],"content":"##### 1.分散控制系统配置\n##### 显示和操作系统：\n##### DCS操作站：每台锅炉设2套操作员站，\n##### 预留3套电气操作员台；\t\n##### 工程师站：DCS设一台工程师站\n##### 打印机：记录打印机：2台\n#####         彩色图形打印机：1台\n#####         工程师站打印机：1台\n##### 2.DCS的I/O点数\n##### DCS总点数初步按700点设计，不包括备用点； \n##### 3.辅盘及硬手操\n##### 操作站前不设辅助盘。在硬手操台上设计有手动跳闸按钮，以备紧急事故情况下跳锅炉、汽机、发电机。硬手操开关包括：\n##### 锅炉紧急跳闸按钮（MFT）双按钮","id":"j1_77"},{"class":["1","j1_6","j1_73"],"content":"##### （1） 分散控制系统(DCS)应选用在相应型号锅炉机组上有成功经验，系统硬件和软件可靠，性能价格比高的国内知名产品。\n##### （2）除灰、空压机、脱硫脱硝程控系统等选用国内有成熟运行经验的厂家,成套供应。\n##### （3） 远传测温元件采用热电偶,热电阻.\n##### （4） 就地测温采用双金属温度计。\n##### （5） 变送器采用知名品牌系列产品。\n##### （6） 联锁保护用的开关量仪表选用国产或国外知名产品。\n##### （7）调节和控制执行机构选用国产或合资知名智能电动执行器或一体化调节阀。\n##### （8） 流量测量装置采用长颈喷嘴，标准孔板，威力巴、AB对称流量计、横截面等。\n##### （9） 电动门采用智能一体化电动头。\n##### （10） 电缆桥架采用镀锌钢桥架。","id":"j1_78"},{"class":["1","j1_6"],"content":"","id":"j1_79"},{"class":["1","j1_6","j1_79"],"content":"##### 1.煤仓间论述：\n##### 煤仓间采用单框架，跨度9m，纵向长度48.0m。零米主要布置10KV厂用配电装置室。锅炉集中控制室及电子设备间布置于7.00m层，给煤机布置于13.5m层。\n##### 锅炉采用紧身封闭，锅炉平台跨度24.0m，锅炉运转层标高为7.00m，长度44.0m。\n##### 2.通风采光\n##### 司炉控制室和电子设备间等主要采用人工照明。\n##### 3.防水与排水\n##### 凡有防、排水要求的房间，如皮带层、煤仓层、卫生间的楼地面均增加防水卷材上做刚性层面层。锅炉房零米层、煤仓层设置排水沟及地漏，以便冲洗水有组织排放。","id":"j1_80"},{"class":["1","j1_6","j1_79"],"content":"##### 1.主要结构构件选型\n##### 除氧煤仓框架各层楼（屋）面采用钢框架及压型钢板混凝土组合楼板结构。\n##### 锅炉房运转层平台采用钢框架及压型钢板混凝土组合楼板结构。\n##### 2.炉后建（构）筑物\n##### 电除尘支架为钢结构，钢烟道支架为钢支架结构，引风机基础采用大块式钢筋混凝结构。 ","id":"j1_81"},{"class":["1","j1_6","j1_79"],"content":"##### 1.燃料建筑\n##### 地下煤斗及煤廊：采用全现浇钢筋砼式地下沟道结构。\n##### 碎煤机室，采用现浇钢筋砼地下结构和上部现浇钢筋砼框架及楼（屋）面结构，空心砖填充墙。\n##### 输煤栈桥：采用钢桁架，钢楼板，檩条及压型钢板轻型屋面，侧面采用压型钢板封闭，支柱为钢框架-支撑结构，独立基础或条形基础。\n##### 煤棚：3m以下采用钢筋混凝土挡土墙，上部可采用网架，铝镁板封闭。\n##### 2.除灰建筑\n##### 灰库可用圆形钢筒仓结构，外附设钢楼梯。\n##### 空压机室为单层建筑，现浇钢筋砼框架及屋面梁板结构，空心砖填充墙。\n##### 渣库圆形钢结构，圆形筏板基础。\n##### 3.脱硫脱硝建筑\n##### 脱硫塔可用圆形钢结构，圆形筏板基础。脱硫脱硝车间采用现浇钢筋砼框架及屋面梁板结构，空心砖填充墙。","id":"j1_82"},{"class":["1","j1_7"],"content":"##### 总承包方的服务范围是指其在现场进行的工作和对发包人的运行、维护人员进行必要的技术培训。\n##### 总承包方应提供完整的电站发电装置调试方案，包括单体调试、分部调试和整体调试的详细文件，交发包人确认，并组织调试工作，总承包方负责试运行期间的维护和消缺工作，由总承包方负责调试，发包人有义务协助总承包方完成调试任务，包括派运行人员参与运行操作，并负责协调配合，试车调试期间所出现安全事故，责任由总承包方负责。总承包方提供机组操作规程，维护保养规程，安全运行规程，点检润滑标准。","id":"j1_83"},{"class":["1","j1_7"],"content":"##### 1）培训内容\n##### 总承包方负责提出培训内容和培训计划，由发包人确认。\n##### 总承包方要选派有经验和有能力的专业人员对发包人技术人员进行现场培训。\n##### 2）培训方式\n##### 待定","id":"j1_84"},{"class":["1","j1_7"],"content":"##### 有关设计联络的计划、时间、地点和内容由发包人、总承包方共同商定。总承包方考虑的设计联络如下表：\n##### 设计联络计划表\n\n| 序号 |次数 |内容 |地点 |时间 |人数 |\n|:------|:------|:------|:------|:------|:------|\n| 1 |1 |初步设计审查 |待定 |待定 |待定 |\n| 2 |1 |施工图交底 |现场 |待定 |待定 |\n\n##### 初步设计应经发包人审查通过，在施工图设计时若需对初步设计作修改，应书面报请发包人签字认可。施工图应对初步设计不完善的地方加以补充，决不能出现简化系统，降低设备技术性能，省略结构部件的现象。 ","id":"j1_85"},{"class":["1","j1_7"],"content":"##### 发包人提供的技术文件及图纸应能满足发电机组总体设计、设备安装、现场调试运行和维护的需要。总承包方可以依据自己对设计方案的理解和认识程度提出建议，如果合理，发包人应予以采纳。\n##### （1）发包人提供的文件资料，但不限于此。\n##### 发包人在合同生效后10天之内提供给总承包方施工图设计用的图纸技术资料：\n##### 发包人根据本合同的规定向总承包方提供必需的图纸和技术资料，对上述资料的正确性、完整性及交付时间负责。负责完成本项目的初步设计阶段及施工图设计阶段的现场勘探（即详勘）。组织对总承包方的初步设计及施工图进行审查。发包人提供的技术资料深度满足总承包方进行施工图阶段设计的要求。资料应准确，不能任意修改。\n##### 发包人提交文件资料\n\n| 编号 |资料名称 |专业 |\n|:------|:------|:------|\n| 1 |总平面布置图 |总图 |\n| 2 |项目位置的气象资料、水文资料、地质勘探资料；50年一遇洪水水位等。 |总图 |\n| 3 |为本母线供电的系统短路容量，变压器容量。发包人及地区调度对电厂通信要求。 |电气 |\n| 4 |煤质全分析报告 |工艺 |\n| 5 |原水全水质分析报告 |化水 |\n\n##### 总承包方提供的技术文件\n##### 总承包应向发包人提供施工图设计文件，全部采购供货的标准设备随机材料（用户手册、安装维修资料等）；设备验收安装资料，设备单体试车资料，设备空负荷联动试车资料，安装施工竣工图和所有竣工资料，并协助参加无负荷联动试车，热负荷试车方案编制。\n##### 总承包方提供的施工图图纸目录、图纸及设备安装资料进度将在本工程技术协议签订后商定。在发包人提供给总承包方所需的设计用资料后35天内，总承包方向发包人提供初步设计方案及工程范围内的机电仪设备明细表（设备规格型号、参数），若有异议，在设计审查会协商解决。","id":"j1_86"},{"class":["1","j1_7"],"content":"##### 按照发包方项目竣工验收的有关文件执行：\n##### （1）工作配合和资料交换所用的语言为中文，单位为国际单位；\n##### （2）总承包方提供给发包方初步设计图纸2套（同时提供PDF、CAD电子版各1套）；\n##### （3）总承包方提供给发包方施工图图纸4套；\n##### （4）总承包方提供设备资料为2 套（其中原件1套）；\n##### （5）总承包方在竣工验收时，向发包方提供竣工资料2套。","id":"j1_87"},{"class":["1"],"content":"","id":"j1_88"},{"class":["1","j1_88"],"content":"##### 工程质量标准：达到技术协议各项指标技术要求，并且工程整套启动试运（第一次联合启动试运开始到72小时试运合格止）符合设计质量标准：\n##### 总承包方在组织施工中必须根据国家颁发的施工验收规范以及设计要求组织施工。\n##### 本工程整体工程的综合性能和质量满足设计图纸、国家规范及标准的要求。\n##### 工程质量等级：单位工程施工质量等级达到100%合格。\n##### 在合同的质保期内因总承包方施工责任和设备材料质量等原因造成的问题，由总承包方负责修理或更换，在双方协商确定的期限内保证问题的解决，并承担相应费用。\n##### 质保期：质保期为壹年。时间从竣工验收合格之日计起。","id":"j1_89"},{"class":["1","j1_88"],"content":"##### a.\t发包人按照相关标准和技术协议的有关规定对合同列出的性能保证项目进行性能试验。\n##### 性能试验由发包人、总包方共同完成，总承包方应按合同要求提出试验大纲并经发包人认可。总承包方负责机组性能，同时派遣有经验的技术专家到现场进行技术服务。\n##### 性能试验满足技术要求，热态连续稳定运行72小时后，则发包人、总承包人双方在性能验收报告上签字确认；\n##### b.\t若考核试验不满足性能考核要求，由总承包方负责分析原因，发包方配合，总承包方负责整改，期限不超过3个月。\n##### c.\t若发包人提供的煤质参数三个月内未能满足考核的前提条件，不再进行考核，视为验收合格。\n##### d.\t若性能试验验收发包方有异议，则由发包方寻找第三方（双方认可）进行裁决。若裁决结果与性能试验数据相符，则费用由发包方承担，否则费用由总承包方承担。","id":"j1_90"},{"class":["1","j1_6","j1_30"],"content":"","id":"j1_96"},{"class":["1","j1_6","j1_36"],"content":"##### A：根据环境保护部、国家发展和改革委员会和国家能源局联合颁布的“关于印发《全面实施燃煤电厂超低排放和节能改造工作方案》的通知（环发[2015]164号）”，到2020年，全国所有具备改造条件的燃煤电厂力争实现超低排放（即在基准氧含量6%条件下，烟尘、二氧化硫、氮氧化物排放浓度分别不高于10、35、50毫克/立方米）。全国有条件的新建燃煤发电机组达到超低排放水平。本次方案设计按该通知的精神进行脱硫除尘和脱硝工艺系统的选择，确保锅炉烟气实现超低排放的标准。\n##### B：本工程烟气排放中，NOx和SO2的排放浓度均满足中国《火电厂大气污染物排放标准》（GB13223-2011）要求，即SO2的排放浓度＜100mg/Nm3，NOx排放浓度＜100mg/Nm3，颗粒物的排放浓度＜30mg/Nm3。（A、B手动选择）\n","id":"j1_97"},{"class":["1","j1_6","j1_60"],"content":"##### 1、总包方负责范围\n##### a、并网电源：\n##### □10KV 并网电源以发电站联络柜端子为界，界内陕鼓负责，界外用户负责。\n##### □35KV 并网电源以升压变压器高压侧35KV联络柜端子为界，界内陕鼓负责，界外用户负责。\n##### □110KV 并网电源以升压变压器高压侧110KV组合开关端子为界，界内陕鼓负责，界外用户负责。（三选一）\n##### b、启动电源：\n##### 以发电站10KV电源进线柜端子为界，界内陕鼓负责，界外用户负责。\n##### c、微机保护整定计算书。\n##### 2、甲方负责范围\n##### a、电源：\n##### □提供一路10KV高压并网电源和一路10KV启动电源。\n##### □提供一路35KV高压并网电源和一路10KV启动电源。\n##### □提供一路110KV高压并网电源和一路10KV启动电源。（三选一）\n##### b、并网申报审批工作和发电接入系统。\n","id":"j1_98"},{"class":["1","j1_6","j1_60"],"content":"##### 1、□发电机接入系统采用10kV 接线方式，发电机出口采用 10KV 并网，与用户上级变电所10KV出线联络，并网点设置在发电机出线柜和系统联络柜。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。\n##### 各级电压的中性点接地方式：\n##### 10kV 采用中性点不接地方式；\n##### 380V 采用中性点直接接地方式；\n##### 检修和照明共用低压供电络。\n##### 2、□发电机接入系统采用35kV 接线方式，发电机出口电压 10KV，经过10/35KV升压变压器升至35KV，并与用户上级变电所35KV出线联络，并网点设置在升压变压器35KV高压侧。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。\n##### 各级电压的中性点接地方式：\n##### 35KV采用中性点直接接地方式；\n##### 10kV 采用中性点不接地方式；\n##### 380V 采用中性点直接接地方式；\n##### 检修和照明共用低压供电络。\n##### 3、□发电机接入系统采用110kV 接线方式，发电机出口电压 10KV，经过10/110KV升压变压器升至110KV，并与用户上级变电所110KV出线联络，并网点设置在升压变压器110KV高压侧。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。\n##### 各级电压的中性点接地方式：\n##### 110KV采用中性点直接接地方式；\n##### 10kV 采用中性点不接地方式；\n##### 380V 采用中性点直接接地方式；\n##### 检修和照明共用低压供电络。\n","id":"j1_99"},{"class":["1","j1_6","j1_60"],"content":"##### 直流负荷包括高压开关操作电源、直流电源、保护控制电源、直流油泵和事故照明等。直流供电的电压为 220V。直流系统采用一套300Ah免维护铅酸蓄电池组。直流电源装置采用微机型相控成套直流电源装置，蓄电池采用 1X300Ah 阀控密封免维护铅酸蓄电池，配置两台逆变器。该直流装置配有微机型直流绝缘在线监测装置，能对所有的直流负荷进行接地故障监测，并能监测直流母线电压信号，在母线欠压、过压或接地时均能发出报警信号。","id":"j1_100"},{"class":["1","j1_6","j1_60"],"content":"##### 1、 控制、信号及测量\n##### 1）本工程电气控制室与热工控制室合并，并设有电子设备间，布置在运转层。\n##### 2）电气系统控制采用独立控制系统：该方案以后台监控系统为主要监控手段，对电气系统的主要设备进行数据采集、监视及控制，该系统也可通过通讯接口与热控系统连接，在热控系统上对以上系统进行监视。\n##### 3）为保证系统的安全可靠性，操作员站台暂考虑保留下列硬手操：\n##### 发电机断路器紧急跳闸开关\n##### 灭磁开关紧急跳闸开关\n##### 2、控制保护\n##### 发电机、厂用变压器等重要设备的控制设在集控室内，低压厂用变压器低压侧开关能实现远方控制。发电机的励磁屏、发电机保护屏、公共测控装置、通讯屏等置于集控室内。低压厂用变压器、高压电动机等采用微机综合保护，装设在就地高压开关柜上。在厂用低压配电装置工作电源和备用电源之间设有备用电源自投装置，当工作电源故障或消失时，备用电源自动/手动投入。\n##### 微机综合保护装置含：发电机保护装置、联络线保护装置、低压厂用变压器保护装置、高压电动机保护装置及后台监控系统等。继电保护按国标 GB/T 50062-2008 “电力装置的继电保护和自动装置设计规范”要求配置：\n##### a. 发电机保护：\n#####    发电机失步解列保护\n#####    纵差保护\n#####    复合电压过电流保护\n#####    定子接地保护（按规范允许单相接地运行两小时）\n#####    定子绕组过负荷保护\n#####    转子一点、二点接地保护\n#####    逆功率保护\n#####    发电机失磁保护\n#####    机跳电保护/热工保护（原动机停机连锁发电机解列）\n##### 电跳机保护（发电机保护动作连锁原动机停机）\n##### b. 低压厂用变压器\n#####    限时速断保护\n#####    过流保护\n#####    温度保护\n##### c. 联络线\n#####    线路纵联差动保护\n#####    方向过电流保护\n##### 电流速断保护\n#####    过电流保护\n#####    过负荷保护\n#####   零序过电流保护\n##### d. 高压电动机\n#####    电流速断保护\n#####    过电流保护\n#####    单相接地保护\n#####    根据负荷类别设低电压保护\n##### e. 同期系统采用微机自动准同期装置，手动准同期装置\n##### f. 发电机励磁系统装设自动调整励磁装置(AVR，静止可控硅)。\n","id":"j1_101"},{"class":["1","j1_6","j1_60"],"content":"##### 厂用高压配电装置布置于主厂房高压配电室内，380V 低压配电装置布置在主厂房低压配电间内。汽机平台下发电机出线小室内布置有发电机出口及中性点电流互感器、发电机出口PT 柜等。其余低压厂用配电设备就地布置。发电机保护屏和直流电源屏等布置在控制室内。","id":"j1_102"},{"class":["1","j1_6","j1_60"],"content":"##### 1、电缆选型原则\n##### 电缆选择及敷设按照国标 GB 50217-2007 “电力工程电缆设计规范”进行。本工程选用交联聚乙烯绝缘护套阻燃电力电缆，普通控制电缆选用阻燃型控制电缆，其他与计算机有关的控制电缆选用计算机屏蔽电缆，电缆为铜芯电缆。\n##### 2、电缆设施\n##### 主厂房底层和高、低压配电室内设电缆沟，主厂房以电缆沟和电缆桥架敷设为主，局部穿钢管敷设，在集控室至400V 及10kV 配电室设置电缆夹层和桥架竖井。电站厂区内的电缆以电缆沟敷设为主，辅以桥架敷设电缆。厂区内照明线路采用穿管方式敷设。\n##### 3、电缆防火\n##### 为防止电缆着火时火灾蔓延造成严重的后果，本工程采取以下措施：\n##### 1）主厂房内及由主厂房引出的电力电缆、控制电缆、测量信号电缆均采用阻燃措施。上料系统采用阻燃电缆。重要回路如消防、报警、应急照明、操作直流电源、计算机监控、双重化继电保护等重要回路采用耐火电缆。\n##### 2）在电缆沟（隧）道分支处和进入建筑物的入口处应设立防火门或防火隔断。厂区部分的沟道每隔100m 应设防火墙。\n##### 3）在电缆敷设完成后，将所有贯穿楼板的电缆孔洞，所有高低压开关柜、控制\n屏、保护屏、动力箱、端子箱、电缆竖井处采用有效阻燃材料进行防火封堵，对电缆刷防火涂料。\n##### 4）对重要的电缆及高温、易燃场所采用阻燃槽盒。\n##### 5）在灰尘容易集聚的地方，电缆桥架加防护罩。\n","id":"j1_103"},{"class":["1","j1_6","j1_60"],"content":"##### 1、电气设备防止过电压的保护措施\n##### 1）装置接地按GB/T50064-2014《交流电气装置的过电压保护和绝缘配合设计规范》\n##### 2）防雷设计按照GB50057-2010《建筑物防雷设计规范》进行设计。\n##### 3）为防止操作过电压，10kV 高压开关柜内真空断路器回路组合式过电压保护器。发电机出口及10kV 母线装设氧化锌避雷器，配电回路真空断路器后装设过电压保护装置。\n##### 2、接地装置要求\n##### 接地装置的接地要求按规程GB/T50065-2011《交流电气装置的接地设计规范》执行。接地装置的年腐蚀度参照原有工程，使用年限不低于地面工程的设计使用年限。新建厂房的接地装置采用-60x6 镀锌扁钢做为水平接地体，∮50 镀锌钢管做为垂直接地体，但以水平接地体为主，并考虑防腐措施，主厂房的梁、柱、板内主筋要接地并与接地网可靠联接。为保证人体和设备安全，所有电气设备的外壳都应与接地装置可靠连接。\n##### 主厂房及较高建筑物屋面装设避雷带，利用建筑物内钢筋作为引下线，基础内预埋钢筋作为接地体。水平接地体采用扁钢，垂直接地极采用热镀锌钢管。\n##### 本工程接地设计采用人工接地装置。\n","id":"j1_104"},{"class":["1","j1_6","j1_60"],"content":"##### 照明按照《建筑照明设计标准》GB50034-2013 和《发电厂和变电站照明设计技术规定》DL/T5390-2014 规定设计。检修电源箱按照《火力发电厂厂用电设计技术规定》DL/T5153-2014-规定设置。\n##### 1、工作照明\n##### 主厂房工作照明电源由 380/220V 低压工作段引接。辅助厂房的工作照明由与其系统相 对应的动力箱引接。正常照明主干线路应采用 TN-C-S 系统。\n##### 2、事故照明\n##### 主厂房事故照明由直流 220V 供电。 远离主厂房的辅助间事故照明采用应急灯。主厂房出入口、通道等人员疏散口处，设有安全标志灯。\n","id":"j1_105"},{"class":["1","j1_6","j1_60"],"content":"##### 主厂房内采用固定的三相五线制电源放射形低压检修网络，检修箱电源分别由低压段回路供电。\n##### 主厂房配电室、电子设备间、值班室设立应急照明，在电源突然失电状态下，主厂房配 电室、电子设备间、值班室事故照明能够实现自动切换，应急照明自动启动。\n","id":"j1_106"},{"class":["1","j1_6","j1_60"],"content":"##### 各控制室设烟气探测，配电室值班室、电子设备间及电缆夹层（电缆沟/隧道）设感温和感烟探测，全厂消防设计满足国家及当地消防部门的要求。集控室设置消防、火灾报警控 制中心。厂内通讯设施主厂房操作室设置行政电话、调度电话共 3 部。调度电话和行政电话接到相应的电话接线盒。","id":"j1_107"},{"class":["1","j1_6","j1_60"],"content":"##### 10KV开关柜采用KYN28型中置柜；\n##### 微机保护系统采用许继、南瑞继保、南自和四方产品；\n##### 互感器采用大连一户、二户产品；\n##### 低压变频器采用施耐德、ABB或西门子等；\n##### 厂用变压器采用干式节能型变压器；\n##### 直流电源电池采用：□国内知名品牌 □德国阳光、荷贝克、海智等；\n##### 真空开关采用：□VS1断路器 □VBG/VEP固封断路器 □VD4断路器；\n##### 低压元器件采用：□二一三、常熟等国内知名品牌 □施耐德、ABB、西门子等；\n##### 高压变频器采用：□汇川、荣信、上广电、利德华福等国内知名品牌 □施耐德（利德华福）、霍尼韦尔（上广电）、艾默生（大禹电气）等；该电站将在拟建的电站主厂房区域配置两套10/0.4kV低压厂用变压器，以0.4kV配\n","id":"j1_108"}]
""",

    "template_content": u"""
# 一.概   述
##### 用户企业概况：手动输入
##### 用户能源需求描述：手动输入
##### 综上所述，针对目前企业的生产用汽情况，考虑企业主工艺扩容的需求，我公司根据多年的发电工程建设及设计经验，计划建设概况如下：
##### 项目名称：手动输入；
##### 建设地址：手动输入；
##### 建设规模：手动输入；
##### 建设方式：总承包方以EPC总承包方式承担工程建设及相关的服务；
##### 承包内容：项目范围内的工程设计、设备成套供货、设备安装调试、工程验收及保质期服务工作；
##### 设计理念：秉承经济、实用、可靠、合理、低成本建设、低投入运行设计理念。
##### 工程质量：达到国家施工验收规范合格标准；设备制造质量应保证其达到总承包协议书技术附件要求，保证设计的合理性，设备制造质量应保证其可靠性，购置的标准设备应为国家或行业认可的成熟定型产品;所选用的工程材料、构建必须满足国家质量检验标准和设计规范的要求。安装工程质量应该保证质量合格、安全可靠；设计、施工安装、设备及材料、试车及验收等都应满足和符合现行国家及行业相关规范、规程和标准的要求。
# 二.总承包内容及交接点
## 2.1项目总承包内容
##### 总承包方项目总承包内容包括：项目整体的工艺设计、工厂设计、土建设计、钢构设计、主辅设备设计及本工程项目所需的所有附属配套设施、工艺管道及管廊设计、电缆桥架及电缆布局设计，并对设计的完整性、合理性及正确性负责。总承包方负责项目范围内成套设备供货、建安工程、调试、试运行，并对项目范围内供货设备整体技术性能、供货质量全面负责，并提供技术服务和售后服务。
### 2.1.1工程设计范围
##### 本工程建设内容与设计范围为与新建动力站内所有相关的建筑与工程设计，具体工程建设范围包括如下内容：
##### ——热力系统(包括锅炉、汽机、发电机以及配套辅机)；
##### ——燃料输送系统及储煤系统；
##### ——灰渣处理工程（包括炉渣及飞灰的收集、冷却、输送、仓储、外运部分）；
##### ——脱硫系统；
##### ——脱硝系统；
##### ——脱硫脱硝工程（主要包括脱硫脱硝部分）
##### ——除盐水工程（主要包括除盐水站、凝结水回水部分）
##### ——项目配套的电气系统；
##### ——项目配套的土建工程；
##### ——项目红线范围内的相关配套能源介质管网；
##### 设计范围为与上述工程相关的整体方案规划、主辅设备选型、工艺系统设计、电气控制系统设计、建筑与结构设计、采暖与通风设计、保温油漆设计、检修维护起吊配套设计、环保工程设计、节能优化设计、劳动安全与卫生设计等。
### 2.1.2成套设备采购及供货：
##### 项目范围内主辅设备、电控、自控成套设备及单体设备采购及供货。
### 2.1.3设备安装调试内容
##### 1） 热力系统及其辅助设备的安装调试；
##### 2） 除灰、除渣系统调试；
##### 3） 脱硫、脱硝系统调试；
##### 4） 燃料输送系统调试；
##### 5） 除盐水系统调试；
##### 6） 电气及自控设备安装调试，包含电气施工材料、电缆、电缆桥架、软件编程；
##### 7） 未提及的项目范围内其他设备安装及调试。
### 2.1.4本工程不包含的施工及安装范围
##### ①.  工程项目相关报批，如项目报批、环评、安评、消防报批、开工备案等；
##### ②.  项目范围内的三通一平及绿化等；
##### ③.  桩基工程及桩基检测，土建桩基切桩头和灌注钢筋混凝土撞头；地上、地下障碍物的拆迁清除；
##### ④.  红线范围外集水井、排水管；
##### ⑤.  开挖石块、建筑垃圾等由总承包方运至发包人指定的免费地点；
##### ⑥.   调试期所有的能源介质（水、电、气、汽、煤、点火燃料）、药品、试剂等由发包人无偿提供；
##### ⑦.  水质化验全部设备、设施；
##### ⑧.  生产工器具(设备自带专用工具除外）、工具、办公家具，工人安全防护、劳保用品、警示牌标（汽、电、气、水、道路）等；
##### ⑨.  施工过程中如发现受国家法律保护的历史文物、文化遗迹等，由此发生的费用和对工程进度产生的影响由发包人承担。
## 2.2项目交接点
##### 能源介质及各系统交接点如下表：

| 序号 |名称 |交接点 |备注 |
|:------|:------|:------|:------|
| 1 |外供蒸汽 | 甲方供至接至电厂围墙外1m以内（自己取水除外）| |
| 2 |灰渣 |乙供接至电厂围墙外1米以内，并配阀门 | | 
| 3 |凝结水回水 |甲方接至电厂围墙外1米以内，并配阀门  | | 
| 4 |外供电 |乙方接至上级变电站母线绝缘子串 | | 
| 5 |启动电源 | 甲方提供两路10kv电源| | 
| 6 |燃料 |甲方运输至干煤棚 | | 
| 7 |工业污水| 乙方简单处理后接至厂区污水管 | | 
| 8 |生活污水  | 乙方通过化粪池处理后接至厂区污水管| | 

# 三.设计及施工标准规范
##### 所有设计文件、供货的材料和设备应符合相关的中国标准、规定、规范及法律，或者符合中国钢铁企业余热利用的相关标准、规定、规范及法律：
##### 《小型火力发电厂设计规范》GB50049-2011
##### 《火力发电厂设计技术规程》（DL5000-2000）
##### 《火力发电厂采暖通风与空气调节设计技术规定》DL/T5035-94
##### 《火力发电厂汽水管道设计技术规定》DL/T5054-1996
##### 《火力发电厂保温油漆技术规范》DL/T5072-2007
##### 《火力发电厂建筑设计规程》DL/T5094-1999
##### 《火力发电厂和变电所照明设计技术规定》DLGJ56-95
##### 《火力发电厂烟风煤粉管道设计技术规程》DL/T5121-2000
##### 《工业企业噪声控制设计规范》（GBJ87-85）
##### 《建筑设计防火规范》（GB50016-2006）
##### 《建筑物防雷设计规范》（GB50057-94）
##### 《爆炸和火灾危险环境电力装置设计规范》（GB50058-92）
##### 《电力配备典型消防规程》（DL5027-93）
##### 《火力发电厂总图运输设计技术规定》（DL/T5032-2005）
##### 《火力发电厂与变电所设计防火规范》（GB50229-96）
##### 《采暖通风与空气调节设计技术规定》（DJ/T5035-95）
##### 《动力机器基础设计规范》（GB50040-1996）
##### 《火灾自动报警系统设计规范》（GB50116-98）；
##### 《蒸汽锅炉安全技术监察规程》（劳部发[1996]276号）
##### 《电力建设施工及验收技术规范》（建筑工程篇）（SDJ69-1987）；
##### 《电力建设施工及验收技术规范》(锅炉机组篇)（DL/T-5047-95）；
##### 《电力建设施工及验收技术规范》(汽轮机机组篇)（DL5011-92）；
##### 《电气装置安装工程施工及验收规范》GB50254～GB50259-96
##### 《火力发电厂建设工程启动试运及验收规程》（2009年版）
# 四.工程建设技术条件
## 4.1厂址条件
##### 唐山旭阳化工有限责任公司地处环渤海中心区域的京唐港区腹地黄金地带，坐落于河北乐亭经济开发区内 （省级化工园区），现有项目用地 6040.48 亩 。旭阳发展可以建设自有码头，距公司直线距离仅有约2公里。（手动输入）
## 4.2气象条件
##### （1）气温
##### 多年平均温度 @@coalchp_needs_questionnaire.w_mean_annual_temperature_value@@℃ 
##### 年最热月份平均温度 @@coalchp_needs_questionnaire.w_mean_summer_temperature_value@@℃
##### 年最冷月份平均温度 @@coalchp_needs_questionnaire.w_mean_winter_temperature_value@@℃
##### 极端最高温度 @@coalchp_needs_questionnaire.w_extreme_high_temperature_value@@℃
##### 极端最低温度 @@coalchp_needs_questionnaire.w_extreme_low_temperature_value@@℃
##### （2）气压 
##### 多年平均大气压 @@coalchp_needs_questionnaire.w_mean_annual_barometric_value@@kpa
##### 历年夏季平均气压 @@coalchp_needs_questionnaire.w_mean_summer_barometric_value@@kpa
##### 历年冬季平均气压 @@coalchp_needs_questionnaire.w_mean_winter_barometric_value@@kpa
##### （3）降雨量 
##### 年平均降水量 手动输入mm
##### 年最大降水量 手动输入mm
##### 一昼夜最大降水量 手动输入mm
##### 一小时最大降水量 手动输入mm
##### 年降雨日数（≥0.1mm）手动输入（d）
##### 年降雪日数 手动输入（d）
##### 最大积雪厚度 手动输入cm
##### （4）湿度 
##### 年平均相对湿度 @@coalchp_needs_questionnaire.w_annual_average_relative_humidity_value@@%
##### 全年最热月份平均相对湿度 @@coalchp_needs_questionnaire.w_mean_summer_relative_humidity_value@@%
##### 全年最冷月份平均相对湿度 @@coalchp_needs_questionnaire.w_mean_winter_relative_humidity_value@@%
##### （5）风速 
##### 平均风速 手动输入m/s
##### 最大风速及风向 手动输入m/s WNW
##### 全年盛行风向 手动输入ENE
##### 夏季盛行风向 手动输入SW
##### （6）蒸发 
##### 年平均蒸发量 手动输入（小时蒸发）
##### （7）特殊气候 
##### 沙暴  1994-2003  手动输入十年无沙暴
##### 雷暴  历年雷暴平均日数 手动输入天
##### 冰雹  年平均 手动输入天/年
##### 浓雾  历年平均雾日数手动输入天
##### （8）云雾及日照 
##### 平均日照时数 手动输入小时
## 4.3工程地质
##### 总承包方给发包人提供详堪布点图，发包人组织详堪并在10个工作日间将详堪资料以电子版形式反馈给总承包方，由总承包方根据详堪进行设计。
## 4.4地震烈度
##### 根据《建筑抗震设计规范》附录A的划分要求，本工程抗震设防烈度为7度，（手动输入）设计地震分组为第二组（手动输入），设计地震基本加速度为0.15g。（手动输入）本工程按规范进行设计。
## 4.5建设场地
##### 本工程建设场地的位于唐山旭阳化工有限责任公司厂区内。手动输入
## 4.6电源情况
##### 本工程需要发包人提供两路独立的10kV电源，装置能力要满足动力站系统的启动、运行用电。
## 4.7水源状况
##### 利用原厂管网提供水源,发包方负责施工，接至动力站红线外一米处。本工程按接口处供水水压符合以下要求进行设计：
##### 生产新水≥0.30MPa
##### 生活给水≥0.25MPa
##### 消防水≥0.30MPa
## 4.8辅料供应
##### 项目主要消耗药品如氯化钠、磷酸三钠等，由发包人统一自行采购配给。
# 五.工程建设技术参数
##### 本项目属于自备动力站，高效利用煤炭进行燃烧，产生中压蒸汽供厂区用汽。（手动输入）项目投产后，将创造良好的经济效益、社会效益和环保效益。
## 5.1项目概况
##### 此项目为唐山旭阳新建25万吨/年苯乙烯配套2×100t/h锅炉岛工程。锅炉产生中温中压蒸汽供苯乙烯项目使用，这些蒸汽使用后凝结成水经除铁后进入除盐水箱，然后通过除盐水泵、冷渣器进入除氧器，再经过给水泵进入锅炉，循环使用。（手动输入）
## 5.2项目性质
##### 本项目属于自备动力站，高效利用煤炭进行燃烧，产生中压蒸汽供厂区用汽。（手动输入）项目投产后，将创造良好的经济效益、社会效益和环保效益。
## 5.3总图部分
### 5.3.1总图布置依据
##### （1）本期工程业主提供的资料。
##### （2）《小型火力发电厂设计规范》GB50049-2011
##### （3）《火力发电厂总图运输设计技术规程》DL/T5032-2005
##### （4）《建筑设计防火规范》
### 5.3.2 厂址概述及设想
##### 本动力站拟建设2×100t/h中温中压循环流化床锅炉（一用一备），项目用地东南侧布置有25万吨/年苯乙烯，处于20万吨/年苯加氢项目南侧。（手动输入） 
### 5.3.3 总平面布置说明
#####  1）总平面设计原则
##### （1）充分利用现有场地条件，因地制宜，减少工程费用；
##### （2）工艺流程合理，功能分区明确；
##### （3）物流流向合理，交通运输便捷；
##### （4）满足电厂总图运输的有关设计规范、规定要求；
##### （5）根据气象、日照合理布置建构筑物，改善厂内工作生活环境；
##### （6）与现有建筑及设施协调一致，有序融合。
#####  2） 主要建设项目
##### 本期工程厂区主要建设项目有司炉室、脱硫脱硝及除尘设施、输煤设施、灰库、除盐水站、空压机室，以及相应的辅助、附属建构筑物。
##### 针对本项目，绿化以厂前区集中绿化和厂区周边及道路两侧的行道树为主，种植落叶木和常青乔木，减少污染，保护环境。
## 5.4热机部分
### 5.4.1装机方案
##### 本期热电站规划建设规模为2×100t/h中温中压燃煤锅炉配套苯乙烯项目使用，一用一备，不考虑扩建。（手动输入）
### 5.4.2机组选型
##### 1.锅炉主要参数：
##### 本工程为2×100t/h中温中压循环流化床（手动输入）燃煤锅炉，产品结构简单、紧凑，锅炉本体由燃烧设备、给煤装置、床下点火装置、分离和返料装置、水冷系统、过热器、省煤器、空气预热器、钢架、平台扶梯、炉墙等组成。本期锅炉运转层以下全封闭，以上紧身封闭。
##### 锅炉主要参数：
##### 额定蒸发量         @@coalchp_furnace_calculation.f_steam_flow_design@@t/h
##### 额定蒸汽压力       @@coalchp_furnace_calculation.f_steam_pressure_design@@MPa
##### 额定蒸汽温度      @@coalchp_furnace_calculation.f_steam_temperature_design@@℃
##### 给水温度            @@coalchp_furnace_calculation.f_water_temperature_design@@℃
##### 排烟温度            @@coalchp_furnace_calculation.h_smoke_temperature_design@@℃
##### 锅炉设计效率         @@coalchp_furnace_calculation.f_boiler_efficiency_design@@%
##### 锅炉保证效率         @@coalchp_furnace_calculation.f_boiler_efficiency_design@@%
##### 排污率               @@coalchp_furnace_calculation.f_blowdown_rate_design@@%
##### 2.汽轮机主要参数：手动输入
##### 型号：              C15-8.83/0.5
##### 形式：     高温高压抽汽空冷式汽轮机
##### 额定功率：             15MW
##### 额定进汽量：            86t/h
##### 额定抽汽量：            35t/h
##### 最大进汽量：            97t/h
##### 最大抽汽量：          50t/h
##### 主蒸汽温度：          535℃
##### 　　压力：               8.83MPa
##### 抽汽压力：            0.5MPa
##### 抽汽温度：            158℃
##### 数    量：             2台
##### 3.发电机主要参数 手动输入
##### 额定功率：            15MW
##### 额定电压:             10.5kV±5%
##### 转    速：            3000rpm
##### 功率因数：            0.8
##### 冷却方式：            空气冷却
##### 励磁方式：            无刷励磁
##### 数    量：            2台
### 5.4.3点火系统
##### 1.锅炉点火燃料
##### 锅炉点火燃料采用0#轻柴油，油质分析见下表：
#####  0#轻柴油主要参数表
| 项     目 |数    值 |
|:------|:------|
| 粘  度 |1.23 |
| 凝固点 |7 |
| 燃  点 |102 |
| 闪电（闭口） |90 |
| 比  重 |0.83 |
| 低位发热量KJ/Kg |42900 |
##### 2.燃料来源
##### 锅炉点火用0#轻柴油利用汽车油槽车从厂外运来，通过卸油泵把油卸入储油罐中，然后利用点火油泵送入锅炉点火油枪。锅炉点火采用二级点火方式，高能点火器直接点燃轻柴油，再点燃床料。
### 5.4.4燃烧系统及辅助设备
##### 1.燃烧装置及配风系统
#####     流化床布风板采用水冷布风板结构；布风板上布置了放渣管，下方接冷渣机。
#####     空气分为一次风及二次风，一、二次风之比为@@coalchp_furnace_calculation.a_first_wind_volume_design@@：@@coalchp_furnace_calculation.a_second_wind_volume_design@@，一次风从炉膛水冷风室二侧进入，经布风板风帽小孔进入燃烧室。二次风在布风板上高度方向分二层送入。水冷风室底部还布置了二只放灰管，用于定期清除水冷风室中积灰。一次冷风总管上接出一根风管，分别去送煤风和密封风接口。一次热风总管两侧各接出一根风管，分别去播煤风接口。
##### 2.给煤装置
##### 破碎后的煤通过输送皮带送至煤仓间落入煤仓内。本期每台锅炉设置一座煤仓，为锅炉额定蒸汽量下约8-9小时耗煤量。
##### 每座煤仓下面有三个（手动输入）出煤口，每个出煤口安装有一台给煤机。三台（手动输入）给煤总出力满足锅炉200％（手动输入）额定工况的燃煤量要求，每台给煤机设计出力满足锅炉67.8%（手动输入）额定工况的燃煤量要求，正常情况下每台给煤机各带50%（手动输入）负荷运行。给煤量通过改变给煤机的转速来调整。每台给煤机内通入一次冷风作为密封风，由于给煤管内为正压，给煤机必须具有良好的密封性。
##### 炉前布置了3套（手动输入）落煤装置，煤通过落煤装置送入燃烧室。落煤装置上布置有送煤风和播煤风，以防给煤堵塞。送煤风接一次冷风，播煤风接一次热风，两股风合计约为总风量的4%，每只送风管、播煤风管布置一只风门，以调节送煤风量。
##### 3.烟气系统
##### 引风机是输送含尘且温度较高的烟气，风量大风压高，它运行的可靠性、耐磨性、经济性、价格将直接影响电厂的初投资及今后的运行经济效益。
##### 本工程推荐引风机与脱硫增压风机合并设置。根据《小型火力发电厂设计规范》（GB50049-2011）及《火力发电厂燃烧系统设计计算技术规程》（DL/T 5240-2010）相关要求本工程引风机选用高效离心式风机，采用变频调节方式。
##### 炉膛出口烟气依次经过尾部受热面、省煤器、烟气脱硝装置、管式空气预热器，然后通过烟道进入电袋除尘器，再经引风机、脱硫吸收塔、烟囱排入大气。
##### 为降低NOx的排放，锅炉采用低NOx燃烧器、分级配风等措施可有效降低NOx的排放水平，根据本工程的煤质资料和锅炉技术协议，锅炉本体出口(脱硝前)NOx质量排放浓度不超过200mg/Nm3(以NO2计，标态，干烟气，O2=6%)。
##### a：1台110%    b：2台60%（手动输入）BMCR容量的离心式引风机，配变频调速装置。根据《小型火力发电厂设计规范》，引风机风量裕量系数选为10%，另加温度裕量；风压裕量系数选为20%。
##### 4.锅炉主要辅机的数量及参数:
##### 以下为每台锅炉配置：
##### ● 一次风机                           1台
##### ● 二次风机                           1台
##### ● 返料机                             2台
##### ● 引风机                             1台/2台（手动输入）
##### ● 除尘器                             1台
##### （1）一次风机
##### 风量                 @@coalchp_smoke_air_system.f_fan_selection_flow@@ m3/h
##### 风压                 @@coalchp_smoke_air_system.f_fan_select_total_pressure@@ Pa
##### 台数                  @@coalchp_smoke_air_system.f_count@@ 台
##### （2）二次风机
##### 风量                 @@coalchp_smoke_air_system.s_fan_selection_flow@@ m3/h
##### 风压                 @@coalchp_smoke_air_system.s_fan_select_total_pressure@@ Pa
##### 台数                  @@coalchp_smoke_air_system.s_count@@ 台
##### （3）返料风机
##### 风量                 @@coalchp_smoke_air_system.r_fan_selection_flow@@ m3/h
##### 风压                 @@coalchp_smoke_air_system.r_fan_select_total_pressure@@ Pa
##### 台数                 （手动输入）台
##### （4）引风机
##### 风量                 @@coalchp_smoke_air_system.i_fan_selection_flow@@ m3/h
##### 风压                 @@coalchp_smoke_air_system.i_fan_select_total_pressure@@ Pa
##### 台数                  @@coalchp_smoke_air_system.i_count@@ 台
##### （5）布袋除尘器
##### 型式                 长袋脉冲除尘器（手动输入）
##### 处理烟气量            @@coalchp_furnace_calculation.d_entry_smoke_actual_flow_design@@ m3/h
##### 出口含尘浓度          ≤30mg/Nm3  达到国家最新环保标准要求
##### 本体阻力              ≤1200Pa
##### 本体漏风率            ＜2%
##### 台数                 （手动输入）台
### 5.4.5热力系统及主辅助设备选择
##### 热力系统描述
##### ⑴ 主蒸汽系统：
##### 本工程为三炉两机（手动输入），a:切换母管制系统  b:集中母管制  c：单元制，（手动选择），主蒸汽管路选用a、15CrMoG（中温中压、次高温次高压适用）；b、12Cr1MoVG（高温高压适用）。（手动选择）
##### ⑵ 高压给水系统：
##### 本工程高压给水系统采用采用母管制；给水泵出口设有给水再循环管和给水再循环母管；本期建设2台手动输入可以满足锅炉额定蒸发量的110%容量的给水泵。
##### 给水操作台采用两路负荷调节系统，范围分别为：主回路给水管为100%BMCR工况运行；30%、70%两条旁路给水管低负荷工况运行。
##### ⑶ 低压给水及除氧系统：
##### 本期工程配备1台手动输入110t/h手动输入大气式除氧器手动输入，除氧器采用定压运行方式手动输入，为了保证除氧器在相同工况下运行和对不同工况的要求，除氧器设有汽平衡母管、低压给水母管、加热蒸汽母管、化学补充水母管、主厂区凝结水回水等母管。
##### 除氧用的加热蒸汽由锅炉锅筒处引出，经减温减压后进入除氧器。
##### ⑷ 主凝结水系统
##### 每台机组设2台凝结水泵，正常运行时，1台运行，1台备用；凝结水从排汽装置热井出口由凝结水泵送出，经凝结水处理装置后送至汽封加热器、第三、二、一级低压加热器后，进入高压除氧器。
##### ⑸ 工业水及冷却水系统
##### 本期工程工业水系统设置以满足水泵、风机类设备轴承冷却水及其它冷却设备的冷却用水。
##### ⑹ 锅炉排污系统
##### 本工程每台锅炉各配置连续排污扩容器、定期排污扩容器各一台，锅炉连续排污水接入连排，回收二次蒸汽引入除氧器，剩余排污水排入定排，夏季工况下，排入排污降温池，冬季工况下，接入厂内一次换热站热水侧利用。
##### ⑺ 主厂区生产回水系统
##### 主厂区用汽后凝结水经除铁后到除盐水箱后依次经过除盐水泵、锅炉冷渣器后进入除氧器。
##### ⑻ 疏水箱有关管道系统
##### 锅炉、汽机、汽水管路启动、运行、事故、停机、停炉过程中，有大量疏放水，其汽水品质大多情况符合锅炉炉水要求，必须加以收集利用,因此设置疏水箱和疏水扩容器，收集的合格水经疏水泵打入除氧器。
## 5.5 燃料输送部分
##### 本工程运煤系统按3×260t/h锅炉容量设计。
燃料消耗量表

|运行台数 | 燃料种类|小时消耗量（t/h）|日消耗量（t/d） |年消耗量（万吨/a） |
|:------|:------|:------|:------|:------
|1台炉（手动输入） | 设计煤种|@@coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_design@@ | @@coalchp_coal_handingsystem.b_coal_daily_consumption_design@@|@@coalchp_coal_handingsystem.b_coal_annual_consumption_design@@ |
|X台炉 | 设计煤种| | | |
		
##### 注：
##### 1) 燃煤粒度：a ≤200mm
##### 2).散状密度： ～0.9t/m3（破碎后、入炉前）
##### 3) 日利用小时数按22h计；
##### 4) 年利用小时数按7260h计。

### 5.5.1. 系统范围
##### 自厂内卸煤装置卸车开始一直到将原煤运入锅炉房原煤仓的整个工艺系统,其中包括煤场煤篦子下的地下煤斗、与破碎和筛分破碎装置、运输设备以及输煤系统中的计量、保护、除铁等其它辅助设备和附属建筑。
### 5.5.2 主要配置原则
##### （1） 输煤系统设置均按1炉（手动输入）最终容量考虑。
##### （2）贮煤场和干煤棚总储量满足单台100t/h（手动输入）锅炉10天（按设计煤种）的用量，全部采用自卸汽车（手动输入）进厂。
##### （3）本期工程筛碎系统按一级筛分一级破碎设计。采用双路布置，满足运行的条件。
##### （4）输煤栈桥为封闭布置。
##### （5）输煤系统的控制布置在输煤综合楼内。
### 5.5.3 卸煤装置及贮煤设施
##### 1.卸煤装置
##### 燃煤的运输方式采用公路载重汽车(尽量采用自卸汽车)运输进厂。若日来煤量按不均衡系数@@coalchp_coal_handingsystem.b_daily_coal_unbalanced_coefficient_design@@考虑，则日最大来煤量@@coalchp_coal_handingsystem.b_daily_rail_coal_amount_design@@ t，自卸汽车平均载重量暂按@@coalchp_coal_handingsystem.t_vehicle_capacity_tonnage_design@@ t计，自卸汽车工作时间按每昼夜@@coalchp_coal_handingsystem.t_daily_working_hours_design@@小时计，一天有@@coalchp_coal_handingsystem.t_vehicle_daily_incoming_times_design@@（次）车次进厂卸煤。每小时有约@@coalchp_coal_handingsystem.t_vehicle_perhour_incoming_times_design@@辆。 
##### 2.储煤场及煤场设备
##### 本工程的储煤场设置一座@@coalchp_coal_handingsystem.c_height_design@@m×@@coalchp_coal_handingsystem.c_width_design@@m= @@coalchp_coal_handingsystem.c_coalyard_area_design@@m2干煤棚，在煤场主要用推煤机和装载机向地下进煤斗供煤。储煤场堆煤高度@@coalchp_coal_handingsystem.c_coal_height_design@@m计，总储煤量@@coalchp_coal_handingsystem.t_vehicle_daily_incoming_times_design@@吨。可满足动力站@@coalchp_coal_handingsystem.c_coal_store_days_design@@天的锅炉燃煤量。
##### 干煤棚采用简易钢结构形式，防止煤尘污染四周设置挡风墙。煤场设备配两台推煤机，作为堆煤、压实、整理、煤场翻烧等作业。
### 5.5.4 除杂筛碎设备
##### 1.筛碎设备
##### 本期工程筛碎系统双路布置，一路运行，一路备用。筛碎设备选型为：筛煤机出力为@@coalchp_coal_handingsystem.s_transportsystem_output_check@@t/h，入料粒度≤200mm，筛下物粒度≤10mm；可逆细碎机出力50t/h，入料粒度≤200mm，出料粒度≤10mm；
### 5.5.5 上煤系统及运行方式
##### 1.上煤系统 
#####     从煤场至主场房的带式输送机系统为一路布置。（手动输入）带式输送机的规格为带宽B＝@@coalchp_coal_handingsystem.s_belt_width_check@@mm，带速V=@@coalchp_coal_handingsystem.s_belt_speed_check@@m/s，出力Q=@@coalchp_coal_handingsystem.s_transportsystem_output_check@@t/h。从副跨上煤，煤仓层采用可变槽角电动犁式卸料器卸料。
##### 本期工程上煤系统日运行时间约为@@coalchp_coal_handingsystem.s_belt_width_check@@小时，2班（手动输入）制运行。
##### 2.控制方式
##### 输煤系统逆煤流起动，顺煤流停机，控制采用可编程序控制和就地操作两种方式，为了保证运煤系统能安全、可靠的运行，运煤系统主要运行设备均互相连锁，带式输送机设有：打滑检测装置；纵向撕裂保护装置；跑偏信号；双向拉绳开关；煤流信号；堵煤信号以及煤仓间料位计等。
##### 输煤系统设有下列保护信号：
##### A）煤流信号：监测胶带载煤情况。
##### B）速度信号：用以监测胶带运行速度以控制带式输送机的启停。
##### C）防跑偏信号：当带式输送机跑偏时发出警报信号，仍继续跑偏至过限时停机。
##### D）拉线开关：当带式输送机沿线发生设备或其他事故时，可在胶带沿线任何位置拉线停机。
##### E）高低料位信号：用以监测原煤仓料位的高低。
##### F）堵煤信号
##### G）纵向防撕裂信号
### 5.5.6 辅助设施及附属建筑
##### （1）输煤系统设2级除铁器，除铁点的建筑设施内均设有弃铁箱，将清除的铁杂质收集。
##### （2）煤仓层2号甲乙带式输送机上的卸料装置采用B＝@@coalchp_coal_handingsystem.s_belt_width_check@@mm电动双侧犁式卸料器。
##### （3）计量装置：入炉煤计量装置采用电子皮带秤，为校核其精度，在1号皮带机上设有全动态链码校验装置。为高效、准确检测供煤质量，维护电厂利益，在煤场设汽车入厂煤计量采用2台电子汽车衡即入场煤采样装置。在1号带式输送机前中部装有2台入炉煤采样装置，以检测入炉煤是否满足锅炉运行要求。
##### （4）预破碎室、碎煤机室及转运站均设有起吊设备，以满足检修的需要。
##### （5）输煤系统设置输煤综合楼，除布置输煤配电控制外，还设有输煤办公室、洗浴、卫生间等配套设施。
## 5.6脱硫脱硝部分
### 5.6.1概述
##### A：根据环境保护部、国家发展和改革委员会和国家能源局联合颁布的“关于印发《全面实施燃煤电厂超低排放和节能改造工作方案》的通知（环发[2015]164号）”，到2020年，全国所有具备改造条件的燃煤电厂力争实现超低排放（即在基准氧含量6%条件下，烟尘、二氧化硫、氮氧化物排放浓度分别不高于10、35、50毫克/立方米）。全国有条件的新建燃煤发电机组达到超低排放水平。本次方案设计按该通知的精神进行脱硫除尘和脱硝工艺系统的选择，确保锅炉烟气实现超低排放的标准。
##### B：本工程烟气排放中，NOx和SO2的排放浓度均满足中国《火电厂大气污染物排放标准》（GB13223-2011）要求，即SO2的排放浓度＜100mg/Nm3，NOx排放浓度＜100mg/Nm3，颗粒物的排放浓度＜30mg/Nm3。（A、B手动选择）

### 5.6.1脱硝系统
##### 1、脱硝工艺简介
##### 燃煤锅炉生成的NOx主要由NO、NO2及微量的N2O组成，其中NO含量超过90%，NO2约占5%～10%，N2O只有1%左右。NOx理论上有三条生成途径，即热力型、燃烧型与瞬态型。其中，燃料型NOX所占比例最大。
##### （1）燃料型NOx，燃料中的氮氧化物在煤粉火焰前端被氧化而成，所占NOX比例超过80%~90%；
##### （2）热力型NOx，助燃空气中的N2在燃烧后期1300℃以上的温度下被氧化而成；
##### （3）瞬态型NOx，由分子氮在火焰前沿的早期阶段生成，所占NOx比例很小。
##### 利用燃烧过程产生的氮基中间产物或者往烟气中喷射氨气，在合适的温度、气氛或者催化剂条件下将NOx还原，这是燃煤锅炉控制NOx排放的主要机理。由此衍生出炉膛喷射还原剂的选择性非催化还原烟气脱硝（简称SNCR）和炉内烟道喷射还原剂的选择性催化还原烟气脱硝（简称SCR）、SNCR与烟道型SCR联合等三类技术，这些技术成熟可靠，可单独或联合使用。
##### 1）SNCR脱硝技术介绍
##### SNCR技术就是利用机械式喷枪将氨基还原剂（如氨气、氨水、尿素）溶液雾化成液滴喷入炉膛，热解生成气态NH3，在850～1100℃温度区域（通常为锅炉对流换热区）和没有催化剂条件下，NH3与NOX进行选择性非催化还原反应，将NOx还原成N2与H2O。喷入炉膛的气态NH3同时参与还原和氧化两个竞争反应：温度超过1100℃时，NH3被氧化成NOx，氧化反应起主导；低于1100℃时，NH3与NOx的还原反应为主，但反应速率降低。
##### 4 NO + 4 NH3 + O2 → 4 N2 + 6 H2O            
##### 4 NH3 + 5 O2 → 4NO + 6 H2O
##### SNCR整体工艺简洁，具有如下特点：
##### （1）现代SNCR技术可以控制NOX排放浓度降低50～60%，脱硝效率随机组容量增加，炉膛尺寸大，机组负荷变化范围扩大，增加了SNCR反应温度窗口与还原剂均匀混合的控制难度，致使脱硝效率下降。对于300MW以下小容量机组，效率在40%-60%左右。
##### （2）SNCR装置不增加烟气系统阻力，也不产生新的SO3，氨逃逸浓度通常控制在5～10μL/L以内（SCR是3μL/L）；
##### （3）合适的反应温度窗口狭窄，为适应锅炉负荷的波动、提高氨在反应区的混合程度和利用率，通常在炉膛出口过热器下方设置多层喷枪。
##### （4）雾化液滴蒸发与热解过程中需要吸收热量，这会造成锅炉效率降低约0.1～0.3个百分点。
##### （5）还原剂雾化液滴在大于1100℃温度下分解时，部分被氧化成NOX，增加了NOX原始控制难度，导致还原剂的有效利用率降低。脱硝效率为30～40%时，还原剂利用率仅为20～30%。
##### 2）SCR脱硝技术介绍
##### SCR技术就是把还原剂氨气喷入锅炉省煤器下游300～400℃的烟道内，在催化剂作用下，将烟气中NOX还原为无害的N2和H2O。SCR工艺需在烟道上增设一个反应器。受制于锅炉烟气参数、飞灰特性及空间布置等因素，SCR工艺主要分三种：高灰型（HD型）、低灰型（LD型）和尾部型（TE型）等。高灰型SCR是主流布置，工作环境相对恶劣，催化剂活性惰化较快，但烟气温度合适（300～400℃），经济性最高。低灰型SCR与尾部型SCR的选择，主要是为了净化催化剂运行的烟气条件或者是受到布置空间的限制，由于需将烟气加热到300℃，只适合于特定环境。
目前国内当前已建成、在建、拟建SCR脱硝装置的新老机组约均采用高灰型工艺。主要反应如下： 
##### 4 NO + 4 NH3 + O2 → 4 N2 + 6 H2O            
##### NO + NO2 + 2 NH3 → 2 N2 + 3 H2O
##### 6 NO2 + 8 NH3 → 7 N2 + 12 H2O
##### 4 NH3 + 3 O2 → 2 N2 + 6 H2O
##### 4 NH3 + 5 O2 → 4NO + 6 H2O
##### SCR技术具有如下特点：
##### （1）脱硝效率可以达到90%。
##### （2）需要在空预器入口（烟温为320～420℃范围）增设反应器，反应器内安装催化剂，增加锅炉烟道阻力约700～1000Pa，需提高引风机压头。
##### （3）逃逸氨与SO3反应，有可能在空预器换热面上形成硫酸氢氨，可能导致空预器的堵塞，通过控制化学理论量的加氨，可使氨的泄漏量保持在一个可接受的水平上。
反应器布置在锅炉尾部省煤器与空气预热器之间，烟气经锅炉上级省煤器或下级省器，进入脱硝入口烟道、喷氨格栅、反应器、脱硝出口烟道，空气预热器。
##### 3）SNCR+SCR联合法技术介绍
##### SNCR+SCR 联合法技术是SNCR工艺的还原剂喷入炉膛技术同SCR工艺利用逸出的氨气进行催化反应结合起来，从而进一步脱除NOx，是把SNCR低费用的特点同 SCR工艺的高效脱硝率及低的氨逸出率有效结合。该联合工艺于20世纪70年代首次在日本的一座燃油装置上进行试验，试验结果证明该技术是可行的。理论上，SNCR工艺在脱除了部分NOx的同时为后面的SCR催化法提供了所需的NH3。SNCR布置在锅炉烟气出口和省煤器入口间温度为850-950℃左右的温度区域内；SCR反应器布置在改造锅炉上级或者下级省煤器所获得的2.7m-3.5m的尾部烟道空间。
##### 2、脱硝工艺选择
##### 对于高温高压循环流化床（手动输入）锅炉，锅炉采用低氮燃烧技术（手动输入）可保证NOx排放浓度大约在80mg/Nm3（手动输入）左右，为了满足a：超低排放50 mg/Nm3的要求，b：SNCR中国《火电厂大气污染排放标准》要求，即NOx排放浓度＜100mg/Nm3。（手动选择）确保锅炉在各个工况下NOx均能达标排放，因此本工程推荐采用a：SNCR脱硝工艺 b：SCR脱硝工艺c:SNCR+SCR联合脱硝工艺，（手动选择）选用a、尿素b、氨水（手动选择）为还原剂。
##### A：本工程采用SNCR脱硝工艺，采用尿素作为还原剂，经计算，尿素用量约为@@coalchp_desulfurization_denitrification.d_use_urea@@kg/h，尿素溶液浓度按25%考虑，尿素溶液消耗水量约为@@coalchp_desulfurization_denitrification.d_water_urea@@kg/h，尿素仓库存储时间按@@coalchp_desulfurization_denitrification.d_days_urea@@天考虑，尿素最大储量约为@@coalchp_desulfurization_denitrification.d_capacity_urea@@t。
##### B: 本工程采用SCR脱硝工艺，采用尿素作为还原剂，经计算，尿素用量约为@@@coalchp_desulfurization_denitrification.g_use_urea@@）kg/h，尿素仓库存储时间按@@coalchp_desulfurization_denitrification.d_days_urea@@天考虑，尿素最大储量约为（@@coalchp_desulfurization_denitrification.g_use_urea@@*@@coalchp_desulfurization_denitrification.d_days_urea@@）t。
##### C: 本工程采用SNCR+SCR脱硝工艺，采用尿素作为还原剂，经计算，尿素用量约为@@coalchp_desulfurization_denitrification.g_use_urea@@+@@coalchp_desulfurization_denitrification.d_use_urea@@）kg/h，尿素仓库存储时间按@@coalchp_desulfurization_denitrification.d_days_urea@@天考虑，尿素最大储量约为（@@coalchp_desulfurization_denitrification.g_use_urea@@*@@coalchp_desulfurization_denitrification.d_days_urea@@+@@coalchp_desulfurization_denitrification.g_use_urea@@）t。
##### （A/B/C手动选择）

### 5.6.2脱硫系统
##### 1、脱硫技术介绍
##### 目前，全世界脱硫工艺共有 100 多种，按其燃烧的过程可分为：燃烧前脱硫、燃烧中脱硫、燃烧后脱硫(烟气脱硫)。
##### 石灰石—石膏湿法脱硫工艺、氨法脱硫和循环流化床干法脱硫工艺是目前大型火电机组商业应用上最具有代表性的烟气脱硫工艺，下面对这几种脱硫工艺进行简单介绍。
##### (1) 石灰石—石膏湿法脱硫工艺 
##### 石灰石—石膏湿法脱硫工艺是采用价廉易得的石灰石作为脱硫吸收剂，石灰石小颗粒经磨细成粉状与水混合搅拌制成吸收浆液。在吸收塔内，吸收浆液与烟气接 触混合，烟气中的 SO2 与浆液中的碳酸钙及鼓入的空气进行氧化反应被脱除，最终反应产物为脱硫石膏。脱硫后的烟气经除雾器除去携带的细小液滴后排入烟囱。
##### 脱硫石膏浆液经脱水装置脱水后回收，脱硫废水经处理后供电厂除灰系统使用。 根据市场对脱硫石膏的需求，脱硫石膏的质量等因素，对脱硫副产物石膏可以采用抛弃和回收利用两种方式进行处理。
##### 该工艺适用于任何煤种含硫率的烟气脱硫，脱硫效率可达到 95%以上。石灰石—石膏湿法脱硫工艺由于具有脱硫效率高(Ca/S 大于 1 时，脱硫效率可达 95～98%)、 吸收剂利用率高、技术成熟、运行稳定等特点，因而是目前世界上应用最多的脱硫工艺。在美国、德国和日本，应用该工艺的机组容量约占电厂脱硫机组总容量的 90%，单机容量已达 1000MW。
##### 在国内，国电费县一期、潍坊二期、邹县三期、广西防城港一期等 300MW～600 级机组等均采用了石灰石－石膏湿法脱硫工艺。已投运的脱硫装置均达到或超过了设计指标，证明了该种脱硫工艺的可靠性。
##### (2) 氨法脱硫工艺 
##### 氨法脱硫工艺于上世纪九十年代开始应用于烟气脱硫。在国外，发展氨法的技术商主要有美国环境系统工程公司(GE 氨法)、德国 Lenjets Bischoff 公司、日本钢管公司(NKK 氨法)。氨法脱硫工艺是采用 NH3 做吸收剂除去烟气中的 SO2 的工艺。氨的碱性强于钙基吸收剂；氨吸收烟气中的 SO2 是气—液或气—气反应，反应速率更快、更完全，吸收 剂利用率高，脱硫效率高达 95%以上。另外，其脱硫副产物硫酸铵经过加工后是具有 商业价值的农业肥料。
##### 从动力学原理来说，氨法实质上是以循环的(NH4)2SO3、NH4HSO3 水溶液吸收 SO2 的 过程。亚硫酸铵对 SO2 具有更好的吸收能力，是氨法中的主要吸收剂。随着亚硫酸氢 铵比例的增大，吸收能力降低，须补充氨水将亚硫酸氢铵转化成亚硫酸铵。
##### GE 氨法的工艺流程主要分为预洗涤、SO2 吸收、亚硫酸铵氧化和结晶四个工序。 热烟气经电除尘后进入预洗涤塔，与硫酸铵饱和溶液并流接触，烟气被冷却。同时，由于硫酸铵饱和溶液中的水蒸发而析出硫酸铵结晶。来自预吸收塔的已被冷却饱和的烟气经过除雾器进入 SO2 吸收塔，烟气与喷淋而下的稀硫酸铵溶液逆流接触，烟气中的 SO2 在此被吸收。氨气与压缩空气混合进入吸收塔底部浆池，在添加氨的同时氧 化亚硫酸铵。
##### 在世界的火电厂烟气脱硫市场上，氨法的比例约 1%。当脱硫剂氨的来源充分， 并且副产物硫酸铵有较好的销售市场时，该工艺在运行上才具有经济可行性。
##### (3) 循环流化床干法脱硫工艺 
#####循环流化床烟气脱硫属于干法脱硫工艺。循环流化床干法烟气脱硫技术是由德国 Lurgi 公司在 20 世纪 80 年代初开发的，Wulff 公司在此基础上开发了回流式循环流化床烟气脱硫技术(RCFB-FGD)，德国的 Thysseen 公司、美国的 Airpol 公司、法国的 Stein 公司及丹麦 FLS、Miljo 等公司也都在开发和推广该项技术。
##### 循环流化床烟气脱硫系统主要由吸收剂制备系统、吸收塔、吸收剂再循环系统、 除尘器和控制系统等组成。根据高速烟气与所携带的稠密悬浮颗粒充分接触原理，在吸收塔内喷入消石灰粉使其与烟气充分接触、反应，然后喷入一定量地水，将烟气温度控制在对反应最有利的温度。塔内出去的烟气进入除尘器，除尘器内收集下 来的脱硫灰，小部分排掉，其余的则经循环系统进入吸收塔继续脱硫。吸收塔的底 部为一文丘里装置，烟气流过时被加速并与细小的吸收剂颗粒混合，烟气和吸收剂 颗粒向上运动时，会有一部分烟气产生回流，形成内部湍流，从而增加烟气与吸收剂颗粒的接触时间，提高吸收剂的利用率和系统的脱硫效率。彭城电厂二期 2×300MW、榆社电厂二期 2×300MW 等机组均采用该工艺。
##### 通过对以上三种典型的烟气脱硫工艺的分析可以看出：氨法脱硫工艺脱硫效率高，运行可靠，但是氨法脱硫受吸收剂供应的制约。另外，氨液脱硫剂的成本高，是钙基脱硫剂价格的十倍以上；副产物如果要加工成有商品价值的农用肥料，还需增加昂贵的后处理设备；所以氨法脱硫受到脱硫剂供给 源和副产物销售市场的很大限制，本工程采用氨法脱硫不具备条件。
##### 烟气循环流化床脱硫工艺近几年发展迅速,是一种适用于煤种含硫量<0.6%的低 硫煤脱硫；特别适用于机组容量为300MW及以下的中小容量机组脱硫。在西部缺水地 区及脱硫吸收剂(生石灰)来源可靠的地区更为适用。该工艺流程简单，新建和改造 电厂均适用。烟气循环流化床脱硫技术在钙硫比为1.3～1.8的情况下，脱硫效率可达90%以上，可去除烟气中的硫氧化物、HCL、HF、颗粒物和重金属(如汞)；无脱硫废水产生；是一种性能价格比较高的干法烟气脱硫工艺。干法脱硫工艺的脱硫副产物是粉煤灰、消石灰、亚硫酸钙、硫酸钙等组成的混合物。目前，脱硫灰综合利用途径少，商业价值很低，通常只能灰场堆放处理。
##### 2、脱硫工艺选择
##### A:本工程采用炉内喷钙脱硫工艺，经计算，石灰石耗量约为@@coalchp_desulfurization_denitrification.r_coco3_consume@@kg/h，石灰石储罐贮存时间按@@coalchp_desulfurization_denitrification.r_storage_time@@天考虑，石灰石储罐体积约为@@coalchp_desulfurization_denitrification.r_storage_volume@@m3，最大储量约为@@coalchp_desulfurization_denitrification.r_storage_output@@kg。
##### B：本工程采用石灰石-石膏法脱硫工艺，脱硫装置的烟气处理能力按锅炉50～110%BMCR工况时的烟气量，脱硫系统不设置烟气旁路，脱硫工艺尽可能节约能源和水源，降低脱硫系统的投资与运行费用。
设计脱硫效率脱硫效率≥92.8%@@coalchp_desulfurization_denitrification.s_desulfurization_efficiency@@，脱硫系统SO2入口浓度原设计值为@@coalchp_desulfurization_denitrification.s_no_desulfurization_so2@@ mg/Nm3。经计算，石灰石耗量约为@@coalchp_desulfurization_denitrification.d_limestone_consume@@kg/h，生成CaSO4量为@@coalchp_desulfurization_denitrification.d_gengrate_coca4@@kg/h。 
##### （A、B手动选择）



## 5.7除灰、除渣部分
### 5.7.1 概述
##### 除灰渣系统采用“灰渣分除”的设计原则，充分考虑当地自然条件，最大限度实现节水和少占地的设计目标，并为灰渣综合利用创造条件，同时考虑减少灰渣运输过程中产生的污染，降低工程造价、提高自动化水平，达到安全、稳定、可靠运行之目的。
##### 灰渣量

| 灰渣量 |灰渣量 |小时灰渣量(t/h) |小时灰渣量(t/h) |小时灰渣量(t/h) |日灰渣量(t/d) |日灰渣量(t/d) |日灰渣量(t/d) |年灰渣量(万t/a) |年灰渣量(万t/a) |年灰渣量(万t/a) |
|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|
| 灰渣量 |灰渣量 |灰渣 |灰 |渣 |灰渣 |灰 |渣 |灰渣 |灰 |渣 |
| 设计煤种 |单台 |coalCHP[0] |@@coalchp_furnace_calculation.d_ash_total_design @@ |@@coalchp_furnace_calculation.d_dust_total_design@@ |coalCHP[1]|coalCHP[2] |coalCHP[3] |coalCHP[5] |coalCHP[6] |coalCHP[4] |

##### 注：日运行小时按22小时，年达行小时数按7260小时（手动输入）计算。
##### 灰渣比按7:3(手动输入)考虑
### 5.7.2 除渣系统
##### 锅炉排出的热渣经冷渣器冷却后，排入链斗输渣机，最终由斗式提升机将炉渣送入钢制渣仓临时储存。每个渣仓卸料平台设一台散装机和一台双轴搅拌机装汽车外运到砖厂综合利用或运至灰渣场临时储存。
##### 每台锅炉设1套链斗输渣机，（手动输入）除渣系统设备出力按不小于锅炉排渣量的250%设计，即单套系统设备出力为@@coalchp_removal_ash_slag_system.s_slag_removal_system@@t/h。
##### 动力站共设1座直径@@coalchp_removal_ash_slag_system.s_dia@@数据m、有效容积@@coalchp_removal_ash_slag_system.s_slag_removal_system@@m³钢渣仓，可储存2（手动输入）台锅炉@@coalchp_removal_ash_slag_system.s_sludge_time@@天的排渣量。
##### 除渣系统工艺流程：锅炉→冷渣器→带式输送机（1#）→带式输送机（2#）→斗提机→钢渣仓→干式散装机（或双轴搅拌机）→罐装车（或自卸汽车）→砖厂（或灰渣场）。
### 5.7.3 除灰系统
##### 本工程采用正压浓相气力除灰系统，通过管道将锅炉飞灰输送至新建混凝土灰库临时储存，定期由密封罐车（干灰）或自卸汽车（湿灰）外运综合利用。
##### 除灰系统输送用气及仪用气从化工压缩空气总体管网引接，压力为0.5-0.7MPa。
##### 本工程气力除灰系统出力按锅炉除尘器最大排灰量的@@coalchp_removal_ash_slag_system.r_removal_coefficient@@%考虑，即单台炉除灰系统出力为@@coalchp_removal_ash_slag_system.r_removal_the_ash_system@@t/h。
##### 全厂共设2（手动输入）座直径@@coalchp_removal_ash_slag_system.r_dia@@米有效容积为@@coalchp_removal_ash_slag_system.r_effective_volume_ash_storage@@m³的混凝土灰库，可储存2台（手动输入）锅炉同时满负荷运行工况下@@coalchp_removal_ash_slag_system.r_stored_ash@@天的排灰量。灰库卸料平台分别设有干灰散装机和双轴加湿搅拌机。用干灰时可通过干灰散装机将灰装密封罐车运至水泥厂、制砖厂等进行综合利用；不考虑干灰利用时，可由双轴加湿搅拌机加喷淋后再由自卸汽车将湿灰运到灰渣场碾压堆放。
##### 系统流程：电袋复合式除尘器灰斗→手动插板阀→进料阀→仓泵（压力输送罐）→出料阀→输灰管道→灰库。
## 5.8化学水处理部分
### 5.8.1 水源及水质资料
##### 1、本工程的化学水处理系统补充水水源来自安瑞佳现有水网、生产供水管网。（手动输入）
##### 2、原水水质
##### 原水水质分析表（手动输入）

| 序号 |分 析 项 目 |符号 |单 位 |数值 |
|:------|:------|:------|:------|:------|
| 1 |氨氮 | |毫克/升 |0.03 |
| 2 |氨 | |毫克/升 |<0.1 |
| 3 |悬浮物 | |毫克/升 |1.2 |
| 4 |氟化物 | |毫克/升 |0.3 |
| 5 |硝酸根 | |毫克/升 |0.28 |
| 6 |酸度 | |毫摩尔/升 |未检出 |
| 7 |硬度 | |毫克/升（以CaCO3计) |40.4 |
| 8 |暂时硬度 | |毫摩尔/升 |0.807 |
| 9 |永久硬度 | |毫摩尔/升 |0 |
| 10 |负硬度 | |毫摩尔/升 |4.29 |
| 11 |总碱度 | |毫克/升（以CaCO3计) |255 |
| 12 |pH | |/ |8.51 |
| 13 |化学需氧量(锰） | |毫克/升 |0.65 |
| 14 |全硅 | |毫克/升 |12.1 |
| 15 |活性硅 | |毫克/升（以SiO2计） |10.9 |
| 16 |全固 | |毫克/升 |398 |
| 17 |溶解性固体 | |毫克/升 |374 |
| 18 |菌落总数 | |CFU/mL |1 |
| 19 |总大肠菌群 | |MPN/100mL |未检出 |
| 20 |钾 | |毫克/升 |0.6 |
| 21 |钠 |Na+ |毫克/升 |140 |
| 22 |钙 |Ca2+ |毫克/升（以CaCO3计） |35.4 |
| 22 |镁 |Mg2+ | |5 |
| 24 |总铁 | |毫克/升 |0.34 |
| 25 |全铝 | |毫克/升 |0.224 |
| 26 |HCO3- | |毫克/升 |262 |
| 27 |CO32- | |毫克/升 |24 |
| 28 |OH- | |毫克/升 |0 |
| 29 |SiO32- | |毫克/升 |13.8 |
| 30 |硫酸盐 | |毫克/升 |11 |
| 31 |氯离子 | |毫克/升 |37.6 |
| 32 |阳离子合计 | |毫摩尔/升 |6.94 |
| 33 |阴离子合计 | |毫摩尔/升 |6.75 |
| 34 |离子分析误差 | |　 |1.4% |
| 35 |溶解固体误差 | |　 |0% |

### 5.8.2给水、炉水、蒸汽质量标准
##### 根据GB/T12145-2008标准要求，本工程选用机、炉的给水、炉水、蒸汽质量标准为：
##### 给水水质要求：（A、中温中压 B、高温高压 手动选择）
#####  A：中温中压
#####   锅炉给水质量标准

| 项    目 |单    位 |数    值 |
|:------|:------|:------|
|硬度|μmol/L|≤2.0|
|溶氧(O2)|μg/L|≤15|
|铁(Fe)|	μg/L|≤50|
|铜(Cu)|μg/L|≤10|
|PH值(25℃)||8.8-9.3|
##### 蒸汽质量标准

| 项    目 |单    位 |数    值 |
|:------|:------|:------|
| 钠 |μg/kg |≤15 |
| 二氧化硅(SiO2) |μg/kg |≤20 |
| 铁 |μg/kg |≤20 |
| 铜 |μg/kg |≤5 |
| 氢电导率(25℃) |μs/cm |≤0.3 |
##### 炉水质量标准

| 项    目 |单    位 |数    值 |
|:------|:------|:------
|磷酸根|mg/L|5~15|
| PH| |9~11 |

##### 凝结水质量标准

| 项    目 |单    位 |数    值 |
|:------|:------|:------
|硬度|μmol/L|≤2.0|
|溶氧(O2)|μg/L|≤50|

B：高温高压
#####   锅炉给水质量标准

| 项    目 |单    位 |数    值 |
|:------|:------|:------|
|溶氧(O2)|μg/L|≤7|
|铁(Fe)|	μg/L|≤30|
|铜(Cu)|μg/L|≤5|
|氢电导率(25℃)|μs/cm|≤0.30|
|PH值(25℃)||8.8-9.3|

##### 蒸汽质量标准

| 项    目 |单    位 |数    值 |
|:------|:------|:------|
|钠|μg/kg|	≤5|
|二氧化硅(SiO2)|μg/kg|≤20|
|铁|μg/kg|≤15|
|铜|μg/kg|≤3|
|氢电导率(25℃)|μs/cm|≤0.15|
##### 炉水质量标准

| 项    目 |单    位 |数    值 |
|:------|:------|:------
|磷酸根|mg/L|2～10|
|PH||9 ~10.5 |
|二氧化硅(SiO2)|μg/kg|≤2|
|电导率(25℃)|μs/cm|≤150|

##### 凝结水质量标准

| 项    目 |单    位 |数    值 |
|:------|:------|:------
|硬度|μmol/L|≤1|
|溶氧(O2)|μg/L|≤50|
|氢电导率(25℃)|μs/cm|≤0.3|

### 5.8.3化学水处理工艺流程
##### （1）除盐水工艺流程：（a、b手动选择）
##### a、多介质过滤器+超滤装置+两级反渗透装置+EDI处理
##### 水源来水→原水箱→原水泵→多介质过滤器→活性炭过滤器→保安过滤器→高压泵→反渗透装置→除二氧化碳器→中间水箱→中间水泵→混合离子交换器→除盐水箱→除盐水泵→各用水点。
特点：设备先进，自动化程度高，运行可靠，但投资大。
##### b、多介质过滤器+反渗透装置+混床处理
##### 清水池→生水泵→换热器→多介质过滤器→精密过滤器→超滤装置→超滤水池→超滤水泵→一级保安过滤器→一级高压泵→一级反渗透装置→中间水池→中间水泵→二级保安过滤器→二级高压泵→二级反渗透装置→RO产水池 →EDI供水泵→EDI装置→除盐水箱→除盐水泵→主厂房
##### 特点：运行安全可靠，投资省，但有酸碱废水产生。
#####（2）	凝结水处理工艺流程
##### 工艺回水经过除油除铁过滤器后进入除盐水箱

### 5.8.4锅炉补给水量
##### 本工程正常水汽损失量：

| 序号 |损失类别 |正常损失 |损失数值t/h |
|:------|:------|:------|:------|
| 1 |厂内水、汽系统循环损失 |锅炉额定蒸发量的3% |@@coalchp_boiler_auxiliaries.m_steamwater_cycle_loss@@|
| 2 |汽包锅炉排污损失 |锅炉额定蒸发9量的2% |@@coalchp_boiler_auxiliaries.m_pollution_loss@@ |
| 3 |对外供汽损失 | |30（手动输入） |
| 4 |其他除盐水用量 | |5（手动输入） |
| 5 |启动/事故用水量 |锅炉额定蒸发量的10% |@@coalchp_boiler_auxiliaries.m_increase_loss@@ |
| 6 |锅炉正常情况下最大补水量 | |40（设置公式，1-4数值相加） |
| 7 |锅炉启动/事故情况下最大补水量 | |40（设置公式，1-5数值相加） |

##### 考虑到设备运行效率和低压管网换水情况，本化水站的系统出力按2×15t/h（手动输入）进行设计，机组起动或事故时补给水，可以通过调节流量和室外的除盐水箱的水位来满足要求。
## 5.9水工部分
### 5.9.1供水现状
##### 本项目由甲方供水至电站界区，确保与电站用水要求。
### 5.9.2水源接入方式
##### 循环冷却水系统由厂区工业新水进行补水；
### 5.9.3循环冷却水系统
##### 1、循环冷却水系统设施、设备
##### 汽轮机冷凝器冷却水系统采用开式循环冷却供水方式。凝汽器、发电机空冷器冷却水直接取自循环冷却水进水母管，使用后进入循环冷却水排水母管。油冷却器冷却水直接回至循环水池。
##### 主厂房内其它需要冷却的设备，如风机轴承冷却等采用工业水冷却。为了充分节约用水，且避免冷却水管道结垢阻塞，取样冷却器考虑采用小型闭式循环冷却水装置进行冷却。
##### 根据本工程水源条件，循环冷却水系统冷却设备选用a、自然通风双曲线冷却塔；b、逆流式机械通风冷却塔。（a、b手动选择）
##### 循环冷却水供水系统流程为：a、双曲线冷却塔；b、机械通风冷却塔集水池→循环水回水管→循环水泵房吸水井→循环水泵房→循环水供水压力管→凝汽器、空气冷却器、冷油器→循环水排水压力管→a、双曲线冷却塔；b、机械通风冷却塔→a、双曲线冷却塔；b、机械通风冷却塔集水池。（a、b手动选择）
##### 本工程为机组配置a、1座XXXm2的自然通风冷却塔；b、nxXXXm³逆流式机械通风冷却塔（a、b手动选择）及3台循环水泵以满足机组夏季最严苛工况下的循环冷却水要求。循环水泵参数：流量Q=XXXXm³/h，（手动输入）扬程H=（常规取值范围：25~28）（手动输入）m，两台运行，一台备用，以适应夏季、冬季循环水量的变化。循环水泵安装在循环水泵房内。  
##### 2、循环水量
##### 根据当地气象条件，经循环供水系统初步计算，夏季循环水冷却倍率采用@@coalchp_circulating_water.v_circulating_ratio_summer@@倍，冬季采用@@coalchp_circulating_water.v_circulating_ratio_winter@@倍，循环供水系统水量见下表：
##### 循环水量统计表

| 机组容量 |凝汽量(t/h) |凝汽器循环冷却水量(t/h) |凝汽器循环冷却水量(t/h) |辅机循环冷却水量(t/h) |总循环水量(m3/h) |总循环水量(m3/h) |
|:------|:------|:------|:------|:------|:------|:------|
| 机组容量 |凝汽量(t/h) |夏季 |冬季 | 辅机循环冷却水量(t/h) |夏季 |冬季 |
| 65MW（手动输入） |@@coalchp_circulating_water.v_steam_exhaust_flow_select@@|@@coalchp_circulating_water.v_circulating_water_summer@@|@@coalchp_circulating_water.v_circulating_water_winter@@ |@@coalchp_circulating_water.v_auxiliary_engine_cooling_summer@@ |@@coalchp_circulating_water.v_total_circulating_water_summer@@|@@coalchp_circulating_water.v_total_circulating_water_winter@@ |

##### 3、工业循环水补水量
##### 循环冷却水补给水量计算结果表

| 项目 |需水量（m3/h） |回收水量（m3/h） |补给水量（m3/h） |
|:------|:------|:------|:------|
| 冷却塔蒸发损失 |@@coalchp_circulating_water.v_evaporation_loss@@|0 |@@coalchp_circulating_water.v_amount_of_makeup_water_summer@@ |
| 冷却塔风吹及飞溅损失 |@@coalchp_circulating_water.v_partial_blow_loss@@ |0 |@@coalchp_circulating_water.v_amount_of_makeup_water_summer@@|
| 排污及渗漏损失 |@@coalchp_circulating_water.v_discharge_capacity@@|0 |@@coalchp_circulating_water.v_amount_of_makeup_water_summer@@ |
| 合计 |@@coalchp_circulating_water.v_total_circulating_water_summer@@ | |@@coalchp_circulating_water.v_amount_of_makeup_water_summer@@ |

### 5.9.4排水系统
##### 电厂排水包括生活污水、厂区雨水、非经常性的生产排水等废水。厂区排水分三个系统：生活污水排水系统、厂区雨水排水系统及生产废水排水系统。
##### 生活污水排水系统包括：厂区内生产建（构）筑物、附属、辅助建筑物的生活污水排水，冲洗设施排水。生活污水经二级生化处理、冲洗废水经隔油池处理后满足国标《污水综合排放标准》中规定的要求，通过厂区内生活污水排水系统排入地下管网。
##### 厂区雨水及生产废水排水系统包括：各建筑物屋面及场地雨水排水、厂区各种道路的排水。各建筑物屋面及各种道路均设有雨水口，道路一侧设有雨水管道，地面及道路雨水经雨水口排入雨水管道。非经常性的生产排水包括泵类及水管道阀门等设备的检修临时排水，这部分排水水质较好，直接排到厂区雨水排水管道。
## 5.10电气部分
### 5.10.1总承包界限划分
##### 1、总包方负责范围
##### a、并网电源：
##### □10KV 并网电源以发电站联络柜端子为界，界内陕鼓负责，界外用户负责。
##### □35KV 并网电源以升压变压器高压侧35KV联络柜端子为界，界内陕鼓负责，界外用户负责。
##### □110KV 并网电源以升压变压器高压侧110KV组合开关端子为界，界内陕鼓负责，界外用户负责。（三选一）
##### b、启动电源：
##### 以发电站10KV电源进线柜端子为界，界内陕鼓负责，界外用户负责。
##### c、微机保护整定计算书。
##### 2、甲方负责范围
##### a、电源：
##### □提供一路10KV高压并网电源和一路10KV启动电源。
##### □提供一路35KV高压并网电源和一路10KV启动电源。
##### □提供一路110KV高压并网电源和一路10KV启动电源。（三选一）
##### b、并网申报审批工作和发电接入系统。

### 5.10.2电气系统接线方案（下列三选一）
##### 1、□发电机接入系统采用10kV 接线方式，发电机出口采用 10KV 并网，与用户上级变电所10KV出线联络，并网点设置在发电机出线柜和系统联络柜。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。
##### 各级电压的中性点接地方式：
##### 10kV 采用中性点不接地方式；
##### 380V 采用中性点直接接地方式；
##### 检修和照明共用低压供电络。
##### 2、□发电机接入系统采用35kV 接线方式，发电机出口电压 10KV，经过10/35KV升压变压器升至35KV，并与用户上级变电所35KV出线联络，并网点设置在升压变压器35KV高压侧。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。
##### 各级电压的中性点接地方式：
##### 35KV采用中性点直接接地方式；
##### 10kV 采用中性点不接地方式；
##### 380V 采用中性点直接接地方式；
##### 检修和照明共用低压供电络。
##### 3、□发电机接入系统采用110kV 接线方式，发电机出口电压 10KV，经过10/110KV升压变压器升至110KV，并与用户上级变电所110KV出线联络，并网点设置在升压变压器110KV高压侧。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。
##### 各级电压的中性点接地方式：
##### 110KV采用中性点直接接地方式；
##### 10kV 采用中性点不接地方式；
##### 380V 采用中性点直接接地方式；
##### 检修和照明共用低压供电络。

### 5.10.3直流系统
##### 直流负荷包括高压开关操作电源、直流电源、保护控制电源、直流油泵和事故照明等。直流供电的电压为 220V。直流系统采用一套300Ah免维护铅酸蓄电池组。直流电源装置采用微机型相控成套直流电源装置，蓄电池采用 1X300Ah 阀控密封免维护铅酸蓄电池，配置两台逆变器。该直流装置配有微机型直流绝缘在线监测装置，能对所有的直流负荷进行接地故障监测，并能监测直流母线电压信号，在母线欠压、过压或接地时均能发出报警信号。
### 5.10.4二次线、继电保护及自动装置
##### 1、 控制、信号及测量
##### 1）本工程电气控制室与热工控制室合并，并设有电子设备间，布置在运转层。
##### 2）电气系统控制采用独立控制系统：该方案以后台监控系统为主要监控手段，对电气系统的主要设备进行数据采集、监视及控制，该系统也可通过通讯接口与热控系统连接，在热控系统上对以上系统进行监视。
##### 3）为保证系统的安全可靠性，操作员站台暂考虑保留下列硬手操：
##### 发电机断路器紧急跳闸开关
##### 灭磁开关紧急跳闸开关
##### 2、控制保护
##### 发电机、厂用变压器等重要设备的控制设在集控室内，低压厂用变压器低压侧开关能实现远方控制。发电机的励磁屏、发电机保护屏、公共测控装置、通讯屏等置于集控室内。低压厂用变压器、高压电动机等采用微机综合保护，装设在就地高压开关柜上。在厂用低压配电装置工作电源和备用电源之间设有备用电源自投装置，当工作电源故障或消失时，备用电源自动/手动投入。
##### 微机综合保护装置含：发电机保护装置、联络线保护装置、低压厂用变压器保护装置、高压电动机保护装置及后台监控系统等。继电保护按国标 GB/T 50062-2008 “电力装置的继电保护和自动装置设计规范”要求配置：
##### a. 发电机保护：
#####    发电机失步解列保护
#####    纵差保护
#####    复合电压过电流保护
#####    定子接地保护（按规范允许单相接地运行两小时）
#####    定子绕组过负荷保护
#####    转子一点、二点接地保护
#####    逆功率保护
#####    发电机失磁保护
#####    机跳电保护/热工保护（原动机停机连锁发电机解列）
##### 电跳机保护（发电机保护动作连锁原动机停机）
##### b. 低压厂用变压器
#####    限时速断保护
#####    过流保护
#####    温度保护
##### c. 联络线
#####    线路纵联差动保护
#####    方向过电流保护
##### 电流速断保护
#####    过电流保护
#####    过负荷保护
#####   零序过电流保护
##### d. 高压电动机
#####    电流速断保护
#####    过电流保护
#####    单相接地保护
#####    根据负荷类别设低电压保护
##### e. 同期系统采用微机自动准同期装置，手动准同期装置
##### f. 发电机励磁系统装设自动调整励磁装置(AVR，静止可控硅)。

### 5.10.5主要电气设备布置
##### 厂用高压配电装置布置于主厂房高压配电室内，380V 低压配电装置布置在主厂房低压配电间内。汽机平台下发电机出线小室内布置有发电机出口及中性点电流互感器、发电机出口PT 柜等。其余低压厂用配电设备就地布置。发电机保护屏和直流电源屏等布置在控制室内。
### 5.10.6电缆及电缆设施
##### 1、电缆选型原则
##### 电缆选择及敷设按照国标 GB 50217-2007 “电力工程电缆设计规范”进行。本工程选用交联聚乙烯绝缘护套阻燃电力电缆，普通控制电缆选用阻燃型控制电缆，其他与计算机有关的控制电缆选用计算机屏蔽电缆，电缆为铜芯电缆。
##### 2、电缆设施
##### 主厂房底层和高、低压配电室内设电缆沟，主厂房以电缆沟和电缆桥架敷设为主，局部穿钢管敷设，在集控室至400V 及10kV 配电室设置电缆夹层和桥架竖井。电站厂区内的电缆以电缆沟敷设为主，辅以桥架敷设电缆。厂区内照明线路采用穿管方式敷设。
##### 3、电缆防火
##### 为防止电缆着火时火灾蔓延造成严重的后果，本工程采取以下措施：
##### 1）主厂房内及由主厂房引出的电力电缆、控制电缆、测量信号电缆均采用阻燃措施。上料系统采用阻燃电缆。重要回路如消防、报警、应急照明、操作直流电源、计算机监控、双重化继电保护等重要回路采用耐火电缆。
##### 2）在电缆沟（隧）道分支处和进入建筑物的入口处应设立防火门或防火隔断。厂区部分的沟道每隔100m 应设防火墙。
##### 3）在电缆敷设完成后，将所有贯穿楼板的电缆孔洞，所有高低压开关柜、控制
屏、保护屏、动力箱、端子箱、电缆竖井处采用有效阻燃材料进行防火封堵，对电缆刷防火涂料。
##### 4）对重要的电缆及高温、易燃场所采用阻燃槽盒。
##### 5）在灰尘容易集聚的地方，电缆桥架加防护罩。

### 5.10.7过电压保护与接地
##### 1、电气设备防止过电压的保护措施
##### 1）装置接地按GB/T50064-2014《交流电气装置的过电压保护和绝缘配合设计规范》
##### 2）防雷设计按照GB50057-2010《建筑物防雷设计规范》进行设计。
##### 3）为防止操作过电压，10kV 高压开关柜内真空断路器回路组合式过电压保护器。发电机出口及10kV 母线装设氧化锌避雷器，配电回路真空断路器后装设过电压保护装置。
##### 2、接地装置要求
##### 接地装置的接地要求按规程GB/T50065-2011《交流电气装置的接地设计规范》执行。接地装置的年腐蚀度参照原有工程，使用年限不低于地面工程的设计使用年限。新建厂房的接地装置采用-60x6 镀锌扁钢做为水平接地体，∮50 镀锌钢管做为垂直接地体，但以水平接地体为主，并考虑防腐措施，主厂房的梁、柱、板内主筋要接地并与接地网可靠联接。为保证人体和设备安全，所有电气设备的外壳都应与接地装置可靠连接。
##### 主厂房及较高建筑物屋面装设避雷带，利用建筑物内钢筋作为引下线，基础内预埋钢筋作为接地体。水平接地体采用扁钢，垂直接地极采用热镀锌钢管。
##### 本工程接地设计采用人工接地装置。

### 5.10.8照明及检修网络
##### 照明按照《建筑照明设计标准》GB50034-2013 和《发电厂和变电站照明设计技术规定》DL/T5390-2014 规定设计。检修电源箱按照《火力发电厂厂用电设计技术规定》DL/T5153-2014-规定设置。
##### 1、工作照明
##### 主厂房工作照明电源由 380/220V 低压工作段引接。辅助厂房的工作照明由与其系统相 对应的动力箱引接。正常照明主干线路应采用 TN-C-S 系统。
##### 2、事故照明
##### 主厂房事故照明由直流 220V 供电。 远离主厂房的辅助间事故照明采用应急灯。主厂房出入口、通道等人员疏散口处，设有安全标志灯。

### 5.10.9检修网络
##### 主厂房内采用固定的三相五线制电源放射形低压检修网络，检修箱电源分别由低压段回路供电。
##### 主厂房配电室、电子设备间、值班室设立应急照明，在电源突然失电状态下，主厂房配 电室、电子设备间、值班室事故照明能够实现自动切换，应急照明自动启动。

### 5.10.10消防报警及火灾检测自动报警系统、厂内通信
##### 各控制室设烟气探测，配电室值班室、电子设备间及电缆夹层（电缆沟/隧道）设感温和感烟探测，全厂消防设计满足国家及当地消防部门的要求。集控室设置消防、火灾报警控 制中心。厂内通讯设施主厂房操作室设置行政电话、调度电话共 3 部。调度电话和行政电话接到相应的电话接线盒。
### 5.10.11设备选型
##### 10KV开关柜采用KYN28型中置柜；
##### 微机保护系统采用许继、南瑞继保、南自和四方产品；
##### 互感器采用大连一户、二户产品；
##### 低压变频器采用施耐德、ABB或西门子等；
##### 厂用变压器采用干式节能型变压器；
##### 直流电源电池采用：□国内知名品牌 □德国阳光、荷贝克、海智等；
##### 真空开关采用：□VS1断路器 □VBG/VEP固封断路器 □VD4断路器；
##### 低压元器件采用：□二一三、常熟等国内知名品牌 □施耐德、ABB、西门子等；
##### 高压变频器采用：□汇川、荣信、上广电、利德华福等国内知名品牌 □施耐德（利德华福）、霍尼韦尔（上广电）、艾默生（大禹电气）等；该电站将在拟建的电站主厂房区域配置两套10/0.4kV低压厂用变压器，以0.4kV配

## 5.11 热工自动化部分
### 5.11.1 热工自动化水平及控制室布置
##### 1.自动化水平
##### 给水调节采用全程调节，其它回路的自动调节范围将按在最低稳燃负荷以上设计，顺序控制系统按子组级设计。
##### 2.控制方式
##### ① 控制系统采用以微处理器为基础的分散控制系统DCS（包括DAS、MCS、 SCS 、FSSS）对锅炉、汽机、重要辅机等进行监控,运行人员在控制室以DCS为监控中心实现对机组的启/停、正常运行的监视,调整以及机组异常与事故工况的处理。
##### ② 控制室不设后备监控设备和常规显示仪表。保留少数独立于DCS的硬接线紧急停炉、停机等硬手操设备，以及几项重要参数显示仪表,以确保在DCS系统故障时的安全停机。设置汽包水位和炉膛火焰电视系统。
##### ③ 本工程按炉、电合设一个集中控制室设计，机炉电集中控制室内的运行组织应按炉电操作员设岗。
##### ④ 除灰系统、空压机系统控制采用可编程序控制器（PLC）＋上位机的监控模式，与除尘系统合用控制室，均采用PLC控制，值班员单独进行监控，调试期间或运行初期也可在各车间就地进行监控。其它辅助车间采用就地控制方式或根据具体情况纳入就近的PLC控制。
##### ⑤ 锅炉吹灰系统、捞渣输渣系统纳入DCS进行监控。
##### ⑥ 循环水系统纳入DCS进行监控。
##### ⑦  脱硫、脱硝采用程控系统，由设备厂家统一成套系统集成，集中布置在炉后脱硫脱硝除尘控制室，锅炉烟气在线监测系统(CEMS)信号送集中控制室DCS系统，另外烟气在线监测系统(CEMS)系统预留至环保部门的信号接口。
##### 3.控制室布置
##### 集中控制室及电子设备间布置
##### 本工程采用炉、电集中控制室及除氧给水等共用一个集中控制室。集中控制室及电子设备间位于附属框架内，3~12号柱之间，地坪标高7.0米，与汽机运转层同标高，控制室净空不小于3.2米。控制室布置有分散控制系统操作站和DEH操作站等。在控制室左侧布置有电子设备间，布置有DCS工程师站，DCS、DEH、ETS、TSI、FSSS等程控等机柜及机炉电动门及调节阀配电柜。集中控制室（包括电子设备间）的面积约为480平方米。集中控制室相应位置下标高4.2米层设有梁下净空不小于2.5米的电缆夹层。集控室（包括电子设备间）采用柜式空调设备。
##### 4.控制系统的总体结构
##### 分散控制系统(DCS)包括数据采集系统（DAS）、模拟量控制系统（MCS）、顺序控制系统（SCS）、锅炉安全监控系统（FSSS）等。
##### 5.控制系统的可靠性
##### 保证控制系统可靠性的措施：
##### 分散控制系统中通讯、网络接口、控制器的DPU均采用冗余配置。
##### 用于调节、保护用的重要信号如炉膛负压、汽包水位等采用三取二原则。
##### 设计有完善的自诊断功能。
##### 电源系统采用冗余供电方式，其中一路为UPS。
##### 各控制系统控制总线全部采用冗余配置。
##### 主要控制设备的可靠性指标：
##### 分散控制系统（包括软、硬件）
##### 数据采集（DAS） MTBF>8600h
##### 可用率>99.9%（考核时间为90天）
### 5.11.2 热工自动化功能
##### 1.分散控制系统（DCS）功能：
##### 数据采集系统（DAS）：
##### DAS系统是机组安全运行的主要手段，具有高度的可靠性和实时响应能力，能够连续监视机组的各种运行参数，提供完整的报警信息，对所有输入信号进行处理。其主要功能如下：
##### ● 显示功能：包括操作显示、标准画面显示（如成组显示、棒状图显示、趋势显示、报警显示等） 、模拟图显示、系统显示、帮助显示等。
##### ● 记录显示：包括定期记录、运行人员操作记录、事故顺序记录（SOE） 、事故追忆记录、设备运行记录等。
##### ● 历史数据存储和检索。
##### ● 性能计算：提供在线计算能力，计算机, 炉及辅机的各种效率及性能参数，计算值及中间计算值应有打印记录，并能在CRT上显示。
##### 模拟量控制系统（MCS）：
##### MCS系统主要满足机组安全启、停运行的要求，保证机在最低稳燃负荷至100%MCR负荷范围内，控制机组运行参数不超过允许值； 
##### 锅炉自动调节系统主要包括: 
##### 锅炉燃料调节系统
##### 锅炉燃烧调节系统
##### 锅炉送风调节系统
##### 锅炉给水调节系统
##### 锅炉主汽温度调节系统
##### 锅炉炉膛压力调节系统
##### 锅炉燃油压力调节系统等。
##### 顺序控制系统（SCS）：
##### 顺序控制系统作为DCS的一部分，完成炉、电及其辅机的启停顺序控制。对于运行中经常操作的辅机、阀门及挡板，启动过程和事故处理需要及时操作的辅机、阀门及挡板，通过顺序控制系统SCS实现。本工程仅设子组级控制。SCS系统主要包括以下子组：
##### 锅炉过热蒸汽压力保护控制功能组
##### ● 一次风机控制功能组
##### ● 二次风机控制功能组
##### ● 返料风机控制功能组
##### ● 引风机控制功能组
##### ● 给煤机控制功能组
##### ● 电动给水泵顺序控制功能组
#####      每个顺序控制功能组,可根据运行人员指令在顺控进行中修改、跳跃或中断。运行人员可按照功能组启停,也可以单台设备在操作站软手操，且具有不同层次的操作许可条件，以防误操作。
##### 炉膛安全监控系统（FSSS）：
#####      炉膛安全监控系统（FSSS）包括燃烧器控制和燃料安全系统，是为保证循环流化床锅炉启动和切除燃烧设备中执行的安全的操作程序，其主要功能有：
##### ·炉膛吹扫
##### ·燃油系统吹扫
##### ·燃油泄漏试验
##### ·点火器及油枪切投控制
##### ·火焰监视及炉膛灭火保护
##### ·火检冷却风机控制
##### ·主燃料跳闸MFT
##### 其它联锁及监视项目
### 5.11.3热工保护和报警
##### 1.热工保护
##### 保护系统的功能是从机组整体出发，使炉、机各辅机之间相互配合，及时处理异常工况或用闭锁条件限制异常工况发生，避免事故扩大或防止误操作，保证人身和设备的安全。主要设以下保护项目（由DCS实现）：
##### 锅炉本体保护
##### 1）当发生下列条件之一时，锅炉MFT
##### ·送风机全停
##### ·引风机全停
##### ·汽包水位高三值
##### ·汽包水位低三值
##### ·炉膛压力高
##### ·炉膛压力低
##### ·全炉膛火焰消失
##### ·全燃料消失
##### ·手动停炉
##### 2）主汽压力保护
##### 主汽压力保护通过安装在过热蒸汽集箱的脉冲式安全阀来实现。
##### 重要回路冗余设计
##### 重要的一次信号如炉膛负压、汽包水位等均采用三取二逻辑。
##### 2.热工报警
##### 每台机组在辅助控制盘上设有热工（含电气）信号报警窗。热工报警主要包括下列内容：
##### ● 工艺参数越限。
##### ● 热工保护动作及主要辅助设备故障。
##### ● 热工监控系统故障。
##### ● 热工电源故障。
##### ● 主要电气设备故障。
##### ● 辅助系统故障。
### 5.11.4 热工自动化系统配置
##### 1.分散控制系统配置
##### 显示和操作系统：
##### DCS操作站：每台锅炉设2套操作员站，
##### 预留3套电气操作员台；	
##### 工程师站：DCS设一台工程师站
##### 打印机：记录打印机：2台
#####         彩色图形打印机：1台
#####         工程师站打印机：1台
##### 2.DCS的I/O点数
##### DCS总点数初步按700点设计，不包括备用点； 
##### 3.辅盘及硬手操
##### 操作站前不设辅助盘。在硬手操台上设计有手动跳闸按钮，以备紧急事故情况下跳锅炉、汽机、发电机。硬手操开关包括：
##### ● 锅炉紧急跳闸按钮（MFT）双按钮
### 5.11.5 热工自动化设备选型
##### （1） 分散控制系统(DCS)应选用在相应型号锅炉机组上有成功经验，系统硬件和软件可靠，性能价格比高的国内知名产品。
##### （2）除灰、空压机、脱硫脱硝程控系统等选用国内有成熟运行经验的厂家,成套供应。
##### （3） 远传测温元件采用热电偶,热电阻.
##### （4） 就地测温采用双金属温度计。
##### （5） 变送器采用知名品牌系列产品。
##### （6） 联锁保护用的开关量仪表选用国产或国外知名产品。
##### （7）调节和控制执行机构选用国产或合资知名智能电动执行器或一体化调节阀。
##### （8） 流量测量装置采用长颈喷嘴，标准孔板，威力巴、AB对称流量计、横截面等。
##### （9） 电动门采用智能一体化电动头。
##### （10） 电缆桥架采用镀锌钢桥架。
## 5.12土建部分（以详细设计为准）
### 5.12.1 建筑设计
##### 1.煤仓间论述：
##### 煤仓间采用单框架，跨度9m，纵向长度48.0m。零米主要布置10KV厂用配电装置室。锅炉集中控制室及电子设备间布置于7.00m层，给煤机布置于13.5m层。
##### 锅炉采用紧身封闭，锅炉平台跨度24.0m，锅炉运转层标高为7.00m，长度44.0m。
##### 2.通风采光
##### 司炉控制室和电子设备间等主要采用人工照明。
##### 3.防水与排水
##### 凡有防、排水要求的房间，如皮带层、煤仓层、卫生间的楼地面均增加防水卷材上做刚性层面层。锅炉房零米层、煤仓层设置排水沟及地漏，以便冲洗水有组织排放。
### 5.12.2 结构设计
##### 1.主要结构构件选型
##### 除氧煤仓框架各层楼（屋）面采用钢框架及压型钢板混凝土组合楼板结构。
##### 锅炉房运转层平台采用钢框架及压型钢板混凝土组合楼板结构。
##### 2.炉后建（构）筑物
##### 电除尘支架为钢结构，钢烟道支架为钢支架结构，引风机基础采用大块式钢筋混凝结构。 
### 5.12.3其他主要生产建（构）筑物
##### 1.燃料建筑
##### 地下煤斗及煤廊：采用全现浇钢筋砼式地下沟道结构。
##### 碎煤机室，采用现浇钢筋砼地下结构和上部现浇钢筋砼框架及楼（屋）面结构，空心砖填充墙。
##### 输煤栈桥：采用钢桁架，钢楼板，檩条及压型钢板轻型屋面，侧面采用压型钢板封闭，支柱为钢框架-支撑结构，独立基础或条形基础。
##### 煤棚：3m以下采用钢筋混凝土挡土墙，上部可采用网架，铝镁板封闭。
##### 2.除灰建筑
##### 灰库可用圆形钢筒仓结构，外附设钢楼梯。
##### 空压机室为单层建筑，现浇钢筋砼框架及屋面梁板结构，空心砖填充墙。
##### 渣库圆形钢结构，圆形筏板基础。
##### 3.脱硫脱硝建筑
##### 脱硫塔可用圆形钢结构，圆形筏板基础。脱硫脱硝车间采用现浇钢筋砼框架及屋面梁板结构，空心砖填充墙。
# 六.技术服务
## 6.1技术服务范围
##### 总承包方的服务范围是指其在现场进行的工作和对发包人的运行、维护人员进行必要的技术培训。
##### 总承包方应提供完整的电站发电装置调试方案，包括单体调试、分部调试和整体调试的详细文件，交发包人确认，并组织调试工作，总承包方负责试运行期间的维护和消缺工作，由总承包方负责调试，发包人有义务协助总承包方完成调试任务，包括派运行人员参与运行操作，并负责协调配合，试车调试期间所出现安全事故，责任由总承包方负责。总承包方提供机组操作规程，维护保养规程，安全运行规程，点检润滑标准。
## 6.2人员培训
##### 1）培训内容
##### 总承包方负责提出培训内容和培训计划，由发包人确认。
##### 总承包方要选派有经验和有能力的专业人员对发包人技术人员进行现场培训。
##### 2）培训方式
##### 待定
## 6.3设计联络
##### 有关设计联络的计划、时间、地点和内容由发包人、总承包方共同商定。总承包方考虑的设计联络如下表：
##### 设计联络计划表

| 序号 |次数 |内容 |地点 |时间 |人数 |
|:------|:------|:------|:------|:------|:------|
| 1 |1 |初步设计审查 |待定 |待定 |待定 |
| 2 |1 |施工图交底 |现场 |待定 |待定 |

##### 初步设计应经发包人审查通过，在施工图设计时若需对初步设计作修改，应书面报请发包人签字认可。施工图应对初步设计不完善的地方加以补充，决不能出现简化系统，降低设备技术性能，省略结构部件的现象。 
## 6.4技术文件提交
##### 发包人提供的技术文件及图纸应能满足发电机组总体设计、设备安装、现场调试运行和维护的需要。总承包方可以依据自己对设计方案的理解和认识程度提出建议，如果合理，发包人应予以采纳。
##### （1）发包人提供的文件资料，但不限于此。
##### 发包人在合同生效后10天之内提供给总承包方施工图设计用的图纸技术资料：
##### 发包人根据本合同的规定向总承包方提供必需的图纸和技术资料，对上述资料的正确性、完整性及交付时间负责。负责完成本项目的初步设计阶段及施工图设计阶段的现场勘探（即详勘）。组织对总承包方的初步设计及施工图进行审查。发包人提供的技术资料深度满足总承包方进行施工图阶段设计的要求。资料应准确，不能任意修改。
##### 发包人提交文件资料

| 编号 |资料名称 |专业 |
|:------|:------|:------|
| 1 |总平面布置图 |总图 |
| 2 |项目位置的气象资料、水文资料、地质勘探资料；50年一遇洪水水位等。 |总图 |
| 3 |为本母线供电的系统短路容量，变压器容量。发包人及地区调度对电厂通信要求。 |电气 |
| 4 |煤质全分析报告 |工艺 |
| 5 |原水全水质分析报告 |化水 |

##### 总承包方提供的技术文件
##### 总承包应向发包人提供施工图设计文件，全部采购供货的标准设备随机材料（用户手册、安装维修资料等）；设备验收安装资料，设备单体试车资料，设备空负荷联动试车资料，安装施工竣工图和所有竣工资料，并协助参加无负荷联动试车，热负荷试车方案编制。
##### 总承包方提供的施工图图纸目录、图纸及设备安装资料进度将在本工程技术协议签订后商定。在发包人提供给总承包方所需的设计用资料后35天内，总承包方向发包人提供初步设计方案及工程范围内的机电仪设备明细表（设备规格型号、参数），若有异议，在设计审查会协商解决。
## 6.5竣工资料提交
##### 按照发包方项目竣工验收的有关文件执行：
##### （1）工作配合和资料交换所用的语言为中文，单位为国际单位；
##### （2）总承包方提供给发包方初步设计图纸2套（同时提供PDF、CAD电子版各1套）；
##### （3）总承包方提供给发包方施工图图纸4套；
##### （4）总承包方提供设备资料为2 套（其中原件1套）；
##### （5）总承包方在竣工验收时，向发包方提供竣工资料2套。
# 七.工程质量及考核方式
## 7.1工程质量
##### 工程质量标准：达到技术协议各项指标技术要求，并且工程整套启动试运（第一次联合启动试运开始到72小时试运合格止）符合设计质量标准：
##### 总承包方在组织施工中必须根据国家颁发的施工验收规范以及设计要求组织施工。
##### 本工程整体工程的综合性能和质量满足设计图纸、国家规范及标准的要求。
##### 工程质量等级：单位工程施工质量等级达到100%合格。
##### 在合同的质保期内因总承包方施工责任和设备材料质量等原因造成的问题，由总承包方负责修理或更换，在双方协商确定的期限内保证问题的解决，并承担相应费用。
##### 质保期：质保期为壹年。时间从竣工验收合格之日计起。
## 7.2性能试验
##### a.	发包人按照相关标准和技术协议的有关规定对合同列出的性能保证项目进行性能试验。
##### 性能试验由发包人、总包方共同完成，总承包方应按合同要求提出试验大纲并经发包人认可。总承包方负责机组性能，同时派遣有经验的技术专家到现场进行技术服务。
##### 性能试验满足技术要求，热态连续稳定运行72小时后，则发包人、总承包人双方在性能验收报告上签字确认；
##### b.	若考核试验不满足性能考核要求，由总承包方负责分析原因，发包方配合，总承包方负责整改，期限不超过3个月。
##### c.	若发包人提供的煤质参数三个月内未能满足考核的前提条件，不再进行考核，视为验收合格。
##### d.	若性能试验验收发包方有异议，则由发包方寻找第三方（双方认可）进行裁决。若裁决结果与性能试验数据相符，则费用由发包方承担，否则费用由总承包方承担。
# 八.其他
##### 1项目在施工调试过程中，总承包方应至少派一名技术人员常驻发包人现场，进行现场服务，协调处理有关技术问题。在试运调试过程中出现的设备事故、人身事故由总承包方负责。
##### 2施工过程中出现变更，总承包方需报告监理及发包人，经确认后方可施工，由总承包方出具设计变更单。
##### 3本协议一式6份，发包方4份（一正三副），总承包2份（一正一副）。
##### 4本协议未尽事宜，友好协商解决。
##### 以下无正文。
##### 发包方：唐山旭阳化工有限责任公司           总承包方： 西安陕鼓动力股份有限公司
##### 代   表：                     		   代    表：
##### 联系电话：                            联系电话：
##### 传    真：                             传    真：
##### 通信地址：                       		通信地址：陕西省西安市高新区沣惠南路8号
##### 邮    编：　								邮    编：7100100
##### 日    期：      年  月  日　　　　	日    期：     年  月  日
"""
}]

# 文本逻辑表
textlogic_data = [{
    "textlogickey": u"coalCHP[0]",
    "textlogicvalue": u"@@coalchp_furnace_calculation.d_total_design/1000@@",
    "textlogicremarks": u"小时灰渣总量",
    "module_name": u"coalCHP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"coalCHP[1]",
    "textlogicvalue": u"@@coalchp_furnace_calculation.d_total_design/1000*24@@",
    "textlogicremarks": u"日灰渣总量",
    "module_name": u"coalCHP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"coalCHP[2]",
    "textlogicvalue": u"@@coalchp_furnace_calculation.d_ash_total_design*24@@",
    "textlogicremarks": u"日灰量",
    "module_name": u"coalCHP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"coalCHP[3]",
    "textlogicvalue": u"@@coalchp_furnace_calculation.d_dust_total_design*24@@",
    "textlogicremarks": u"日渣量",
    "module_name": u"coalCHP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"coalCHP[4]",
    "textlogicvalue": u"@@coalchp_furnace_calculation.d_total_design/1000*24*365@@",
    "textlogicremarks": u"年灰渣总量",
    "module_name": u"coalCHP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"coalCHP[5]",
    "textlogicvalue": u"@@coalchp_furnace_calculation.d_ash_total_design*24*365@@",
    "textlogicremarks": u"年灰量",
    "module_name": u"coalCHP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"coalCHP[6]",
    "textlogicvalue": u"@@coalchp_furnace_calculation.d_dust_total_design*24*365@@",
    "textlogicremarks": u"年渣量",
    "module_name": u"coalCHP",
    "template_id": "",
    "plan_id": ""
}]

roles = [{
    "name": u"超级管理员",
    "defaults": False,
    "permission": Permission.ADMINISTER
}, {
    "name": u"全能专家",
    "defaults": False,
    "permission": Permission.QUERY
}, {
    "name": u"用户",
    "defaults": False,
    "permission": Permission.QUERY
}, {
    "name": u"燃煤专家",
    "defaults": False,
    "permission": Permission.QUERY
}, {
    "name": u"生物质专家",
    "defaults": False,
    "permission": Permission.QUERY
}, {
    "name": u"煤气专家",
    "defaults": False,
    "permission": Permission.QUERY
}, {
    "name": u"燃蒸专家",
    "defaults": False,
    "permission": Permission.QUERY
}, {
    "name": u"能源岛专家",
    "defaults": False,
    "permission": Permission.QUERY
}]

class AddCoalCHP():
    # 初始化数据
    @staticmethod
    def init_data():
        Company.init_company()
        roles_data = [
            roles
        ]
        for index in range(len(roles_data)):
            AddCoalCHP.insert_roles(roles_data[index])
        User.insert_admin()
        data = [
            questionnaire_data, coalHandingSystem_data,
            furnaceCalculation_data, coalCHP_desulfurization_data,
            smokeAirSystem_data, circulatingWater_data, removalAshSlag_data,
            boilerAuxiliaries_data, turbine_backpressure_data,
            economic_indicators_data, chemicalWater_data, chimney_data,
            turbine_auxiliary_data, official_process_data, heat_supply_data
        ]
        for index in range(len(data)):
            AddCoalCHP.insert_constant(data[index])
        AddCoalCHP.insert_component(coal_data)
        # 插入燃煤模块报告标准模板
        template_data = [
            reportTemplate_data
        ]
        for index in range(len(template_data)):
            AddCoalCHP.insert_template(template_data[index])
        # 插入模板逻辑表数据
        logic_data = [
            textlogic_data
        ]
        for index in range(len(logic_data)):
            AddCoalCHP.insert_logic(logic_data[index])

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
            default_value = data[index]["default_value"]
            disable = data[index]["disable"]
            coalCHPConstant = CoalCHPConstant.create_coalCHPConstant(
                module_name, name_eng, name, symbol, unit, calculate, remark,
                default_value, disable)
            CoalCHPConstant.insert_coalCHPConstant(coalCHPConstant)

    # 表中插入煤炭分析数据
    @staticmethod
    def insert_component(coal_data):
        for index in range(len(coal_data)):
            name = coal_data[index][0]
            carbon = coal_data[index][1]
            hydrogen = coal_data[index][2]
            oxygen = coal_data[index][3]
            nitrogen = coal_data[index][4]
            sulfur = coal_data[index][5]
            water = coal_data[index][6]
            grey = coal_data[index][7]
            daf = coal_data[index][8]
            grindability = coal_data[index][9]
            low = coal_data[index][10]
            coalCHPComponent = CoalCHPComponent.create_coalCHPComponent(
                name, carbon, hydrogen, oxygen, nitrogen, sulfur, water, grey,
                daf, grindability, low)
            coalCHPComponent.insert_coalCHPComponent(coalCHPComponent)

    # 表中插入常量数据
    @staticmethod
    def insert_template(data):
        for index in range(len(data)):
            template_name = data[index]["template_name"]
            module_id = data[index]["module_id"]
            user_id = data[index]["user_id"]
            template_create_date = data[index]["template_create_date"]
            template_update_date = data[index]["template_update_date"]
            template__left_menu = data[index]["template__left_menu"]
            template_state = data[index]["template_state"]
            template_left_content = data[index]["template_left_content"]
            template_content = data[index]["template_content"]
            constantdata = ReportTemplate.create_constant(
                template_name, module_id, user_id, template_create_date, template_update_date,
                template__left_menu, template_state, template_left_content,
                template_content)
            ReportTemplate.insert_constant(constantdata)


    # 表中插入常量数据
    @staticmethod
    def insert_logic(data):
        for index in range(len(data)):
            textlogickey = data[index]["textlogickey"]
            textlogicvalue = data[index]["textlogicvalue"]
            textlogicremarks = data[index]["textlogicremarks"]
            module_name = data[index]["module_name"]
            constantdata = Textlogic.create_constant(
                textlogickey, textlogicvalue, textlogicremarks, module_name)
            Textlogic.insert_constant(constantdata)

    # 初始化角色表
    @staticmethod
    def insert_roles(data):
        for index in range(len(data)):
            name = data[index]["name"]
            defaults = data[index]["defaults"]
            permission = data[index]["permission"]
            role = Role.create_roles(
                name, defaults, permission)
            Role.insert_roles(role)