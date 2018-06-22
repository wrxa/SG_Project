# -*- coding: utf-8 -*-

from app.gpg.model.gasPowerGeneration_models import GasPowerGenerationConstant, \
                                    GasPowerGenerationNeedsQuestionnaire, \
                                    GPGBoilerOfPTS, GPGFlueGasAirSystem, \
                                    GPGSmokeResistance, GPGWindResistance, \
                                    GPGCirculatingWaterSystem, GPGSmokeAirCalculate, \
                                    GPGTurbineAuxiliarySystem, GPGSteamWaterPipe, \
                                    GPGBoilerAuxiliaries, GPGTurbineOfPTS

# 煤气发电 锅炉辅机系统

GPGBoilerAuxiliaries_data = [{
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_boiler_evaporation",
    "name": u"锅炉蒸发量",
    "symbol": u"D0",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u"", 
    "default_value": "",
    "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_emission_time",
    "name": u"排放时间",
    "symbol": u"t",
    "unit": u"min",
    "calculate": u"一班一次，2-3次，一次0.5-1min",
    "remark": u"", 
	"default_value": "1", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_emission_rate",
    "name": u"定期排污率",
    "symbol": u"η",
    "unit": u"%",
    "calculate": u"0.1%-0.5%",
    "remark": u"",
	"default_value": "0.2", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_sewage_quantity",
    "name": u"定期排污水量",
    "symbol": u"Dpb",
    "unit": u"kg/h",
    "calculate": u"D0*1000*t*60*η",
    "remark": u"",
	"default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_drum_pressure",
    "name": u"汽包压力",
    "symbol": u"P",
    "unit": u"Mpa",
    "calculate": u"",
    "remark": u"",
	"default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_drum_aturatedwater_enthalpy",
    "name": u"汽包压力下的饱和水焓",
    "symbol": u"hd",
    "unit": u"kj/kg",
    "calculate": u"汽包压力",
    "remark": u"",   
	"default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_work_pressure",
    "name": u"排污扩容器工作压力",
    "symbol": u"",
    "unit": u"Mpa",
    "calculate": u"扩容器压力选0.15MPa(a)/0.45",
    "remark": u"",   
	"default_value": "0.15", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_work_aturatedwater_enthalpy",
    "name": u"扩容器压力下饱和水焓",
    "symbol": u"hs",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"",    
	"default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_work_steam_special_volume",
    "name": u"扩容器压力下蒸汽比容",
    "symbol": u"υ",
    "unit": u"m3/kg",
    "calculate": u"查表",
    "remark": u"",
    "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_work_latentheat_vaporization",
    "name": u"扩容器压力下汽化潜热",
    "symbol": u"r",
    "unit": u"kj/kg",
    "calculate": u"查表（饱和汽焓-饱和水焓）",
    "remark": u"",    
	"default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_work_steam_dryness",
    "name": u"扩容器蒸汽干度",
    "symbol": u"X",
    "unit": u"",
    "calculate": u"0.97~0.98",
    "remark": u"",
	"default_value": "0.97", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_ultimate_strength",
    "name": u"扩容器单位容积润许极限强度",
    "symbol": u"R",
    "unit": u"m3/（m3/kg）",
    "calculate": u"2000",
    "remark": u"" 
	, "default_value": "2000", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_vaporization_capacity",
    "name": u"排污水汽化量",
    "symbol": u"Df",
    "unit": u"kg/h",
    "calculate": u"(hd*η-hs)/xr",
    "remark": u"",
	"default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_affluence_coefficient",
    "name": u"富裕系数",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"1.3~1.5的富裕系数",
    "remark": u""
	, "default_value": "1.4", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_steam_volume",
    "name": u"排污扩容汽容积",
    "symbol": u"Vv",
    "unit": u"m³",
    "calculate": u"",
    "remark": u"",
	"default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_volume",
    "name": u"排污扩容容积",
    "symbol": u"V",
    "unit": u"m³",
    "calculate": u"V=Vv+Vw，Vw=20%～30%Vv",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "r_specifications",
    "name": u"选取",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_boiler_evaporation",
    "name": u"锅炉蒸发量",
    "symbol": u"D0",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_emission_rate",
    "name": u"连续排污率",
    "symbol": u"η",
    "unit": u"%",
    "calculate": u"1%-2%",
    "remark": u""
	, "default_value": "2", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_sewage_quantity",
    "name": u"连续排污水量",
    "symbol": u"Dpb",
    "unit": u"kg/h",
    "calculate": u"D0*1000*η",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_drum_pressure",
    "name": u"汽包压力",
    "symbol": u"P",
    "unit": u"Mpa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_drum_aturatedwater_enthalpy",
    "name": u"汽包压力下的饱和水焓",
    "symbol": u"hd",
    "unit": u"kj/kg",
    "calculate": u"汽包压力",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_work_pressure",
    "name": u"排污扩容器工作压力",
    "symbol": u"",
    "unit": u"Mpa",
    "calculate": u"扩容器压力选0.15MPa(a)/0.45/1.0",
    "remark": u""
	, "default_value": "0.45", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_work_aturatedwater_enthalpy",
    "name": u"扩容器压力下饱和水焓",
    "symbol": u"hs",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_work_steam_pecificvolume",
    "name": u"扩容器压力下蒸汽比容",
    "symbol": u"υ",
    "unit": u"m3/kg",
    "calculate": u"查表",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_work_latentheat_vaporization",
    "name": u"扩容器压力下汽化潜热",
    "symbol": u"r",
    "unit": u"kj/kg",
    "calculate": u"查表（饱和汽焓-饱和水焓）",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_steam_dryness",
    "name": u"扩容器蒸汽干度",
    "symbol": u"X",
    "unit": u"--",
    "calculate": u"0.97~0.98",
    "remark": u""
	, "default_value": "0.97", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_ultimate_strength",
    "name": u"扩容器单位容积润许极限强度",
    "symbol": u"R",
    "unit": u"m3/（m3/kg）",
    "calculate": u"2000",
    "remark": u""
	, "default_value": "2000", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_vaporization_capacity",
    "name": u"排污水汽化量",
    "symbol": u"Df",
    "unit": u"kg/h",
    "calculate": u"(hd*η-hs)/xr",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_affluence_coefficient",
    "name": u"富裕系数",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"1.2的富裕系数",
    "remark": u""
	, "default_value": "1.2", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_steam_volume",
    "name": u"排污扩容汽容积",
    "symbol": u"Vv",
    "unit": u"m³",
    "calculate": u"Vv=Dpb*Df*υ/R",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_volume",
    "name": u"排污扩容容积",
    "symbol": u"V",
    "unit": u"m³",
    "calculate": u"V=Vv+Vw，Vw=20%～30%Vv",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "c_specifications",
    "name": u"选取",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_boiler_watersystem_volume",
    "name": u"锅炉水系统容积",
    "symbol": u"V",
    "unit": u"m³",
    "calculate": u"输入",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_phosphate_content",
    "name": u"应维持的磷酸根含量",
    "symbol": u"PO43-",
    "unit": u"mg/L",
    "calculate": u"10~30",
    "remark": u""
	, "default_value": "20", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_water_hardness",
    "name": u"给水硬度（原水）",
    "symbol": u"H",
    "unit": u"mmol/L",
    "calculate": u"7.0~9.5",
    "remark": u""
	, "default_value": "8.5", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_purity",
    "name": u"纯度",
    "symbol": u"ε",
    "unit": u"m",
    "calculate": u"0.92~0.98",
    "remark": u""
	, "default_value": "0.95", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_boiler_dosage_startup",
    "name": u"锅炉启动时加药量",
    "symbol": u"qm",
    "unit": u"g",
    "calculate": u"V(PO4+28.5*H)/250ε",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_boiler_water_supply",
    "name": u"锅炉给水量",
    "symbol": u"qfm",
    "unit": u"t/h",
    "calculate": u"输入",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_boiler_sewage_quantity",
    "name": u"锅炉排污量",
    "symbol": u"qbl",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_boiler_dosage_run",
    "name": u"运行时加药量",
    "symbol": u"qm",
    "unit": u"g/h",
    "calculate": u"计算",
    "remark": u"" 
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_na3po4_concentration",
    "name": u"磷酸钠浓度",
    "symbol": u"C",
    "unit": u"%",
    "calculate": u"1%~5%",
    "remark": u""
	, "default_value": "4", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_na3po4_density",
    "name": u"在C浓度下的磷酸三钠密度",
    "symbol": u"ρ",
    "unit": u"g/cm3",
    "calculate": u"见表",
    "remark": u""
	, "default_value": "1.0405", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "d_solution_quantity_run",
    "name": u"运行时汽包内加入的溶液量",
    "symbol": u"qv",
    "unit": u"m3/h",
    "calculate": u"qm/10Cρ",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_boiler_design_pressure",
    "name": u"锅炉设计使用压力",
    "symbol": u"P",
    "unit": u"Mpa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_BoilerAuxiliaries",
    "name_eng":
    "p_inlet_pressure",
    "name":
    u"省煤器入口进水压力",
    "symbol":
    u"P1",
    "unit":
    u"Mpa",
    "calculate":
    u"当工作压力P≤0.8MPa时，取P+0.05；当0.8<P≤5.9MPa时，取1.06P",
    "remark":
    ""
	, "default_value": "10.63", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_deaerator_pressure",
    "name": u"除氧器工作压力",
    "symbol": u"Pd",
    "unit": u"Mpa",
    "calculate": u"",
    "remark": u""
	, "default_value": "0.59", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_water_supply_resistance",
    "name": u"给水管阻力（以压头计）",
    "symbol": u"ΔPfw",
    "unit": u"m",
    "calculate": u"计算--许可流速2~3m/s",
    "remark": u""
	, "default_value": "5", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_water_inlet_resistance",
    "name": u"进水管阻力（以压头计）",
    "symbol": u"ΔPin",
    "unit": u"m",
    "calculate": u"计算--许可流速0.5~1m/s",
    "remark": u""
	, "default_value": "5", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_center_altitude_difference",
    "name": u"水泵中心至汽包正常水位的几何高度差",
    "symbol": u"Hy",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
	, "default_value": "20", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_deaerator_altitude_difference",
    "name": u"除氧器最低水位至水泵中心几何高度差（给水泵进口静水头）",
    "symbol": u"Hst",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
	, "default_value": "25", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_feedpump_total_head",
    "name": u"给水泵总扬程",
    "symbol": u"Hsw",
    "unit": u"m",
    "calculate": u"（P1-Pd）*102+1.2*(ΔPfw+ΔPin)+Hy-Hst",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_flow",
    "name": u"流量",
    "symbol": u"Q",
    "unit": u"t/h",
    "calculate": u"已知",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_pump_efficiency",
    "name": u"泵效率",
    "symbol": u"η",
    "unit": u"/",
    "calculate": u"0.6~0.8",
    "remark": u""
	, "default_value": "0.7", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_transmission_efficiency",
    "name": u"机械传动效率",
    "symbol": u"η2",
    "unit": u"/",
    "calculate": u"直连1.0，联轴器0.98，皮带0.95",
    "remark": u""
	, "default_value": "0.98", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_motor_efficiency",
    "name": u"电动机效率",
    "symbol": u"η3",
    "unit": u"/",
    "calculate": u"通常取0.9",
    "remark": u""
	, "default_value": "0.9", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_motor_reserve_factor",
    "name": u"电动机备用系数",
    "symbol": u"β",
    "unit": u"/",
    "calculate": u"查表选取",
    "remark": u""
	, "default_value": "1.15", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_auxiliary_motor_power",
    "name": u"配套电机功率",
    "symbol": u"P",
    "unit": u"kw",
    "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p_specifications",
    "name": u"给水泵选用规格",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_boiler_evaporation",
    "name": u"锅炉蒸发量",
    "symbol": u"D0",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_makeup_steam",
    "name": u"补汽量",
    "symbol": u"D0''",
    "unit": u"t/h",
    "calculate": u"若无取0",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_steamwater_cycle_loss",
    "name": u"厂内汽水循环损失",
    "symbol": u"D1",
    "unit": u"t/h",
    "calculate": u"0.03",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_pollution_loss",
    "name": u"排污损失",
    "symbol": u"D2",
    "unit": u"t/h",
    "calculate": u"0.02",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_condensing_capacity",
    "name": u"凝结水量",
    "symbol": u"D0'",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_condensate_loss",
    "name": u"换热凝结水损失",
    "symbol": u"D1'",
    "unit": u"t/h",
    "calculate": u"0.02",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_boiler_normal_watersupply",
    "name": u"锅炉正常补水量",
    "symbol": u"D1s",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_boiler_desalted_water_rate",
    "name": u"除盐设备自用水率",
    "symbol": u"r",
    "unit": u"/",
    "calculate": u"",
    "remark": u""
	, "default_value": "0.1", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_boiler_desalted_work_cycle",
    "name": u"一级除盐设备工作周期",
    "symbol": u"T",
    "unit": u"h",
    "calculate": u"",
    "remark": u""
	, "default_value": "20", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_boiler_desalted_rebirth_time",
    "name": u"设备再生时间",
    "symbol": u"t",
    "unit": u"h",
    "calculate": u"",
    "remark": u""
	, "default_value": "4", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_increase_loss",
    "name": u"启动或事故增加损失",
    "symbol": u"Dx",
    "unit": u"t/h",
    "calculate": u"10%",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_boiler_max_watersupply",
    "name": u"锅炉最大补水量",
    "symbol": u"Dbu",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_boiler_watersupply_all",
    "name": u"水处理设备全部出力",
    "symbol": u"Q1",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "m_boiler_watersupply_specifications",
    "name": u"选取水处理设备出力",
    "symbol": u"Q1’",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "desalted_water_tech_type",
    "name": u"化学除盐水工艺类型选择",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_boiler_evaporation",
    "name": u"锅炉蒸发量",
    "symbol": u"D0",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_storage_time",
    "name": u"储水时间",
    "symbol": u"t",
    "unit": u"min",
    "calculate": u"130t/h以下20min；130t/h以上10~15min",
    "remark": u""
	, "default_value": "15", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_volume",
    "name": u"容积",
    "symbol": u"V",
    "unit": u"m3",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_size_length",
    "name": u"尺寸(长)",
    "symbol": u"L",
    "unit": u"m",
    "calculate": u"长",
    "remark": u""
	, "default_value": "4", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_size_diameter",
    "name": u"尺寸(直径)",
    "symbol": u"D",
    "unit": u"m",
    "calculate": u"直径",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_max_feedwater_amount",
    "name": u"最大给水量",
    "symbol": u"D0",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_de_ox_pressure",
    "name": u"热力除氧压力",
    "symbol": u"P1",
    "unit": u"Mpa",
    "calculate": u"即液面压力",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_local_atmosphere",
    "name": u"当地大气压",
    "symbol": u"P0",
    "unit": u"pa",
    "calculate": u"与海拔有关",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_local_atmosphere_density",
    "name": u"当地大气压对应下的密度",
    "symbol": u"ρ",
    "unit": u"kg/m3",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_design_flux",
    "name": u"设计流量",
    "symbol": u"Dmax",
    "unit": u"t/h",
    "calculate": u"D0*ρ/ρ'",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_net_positive_suction_head",
    "name": u"泵必需汽蚀余量",
    "symbol": u"NPSHr",
    "unit": u"m",
    "calculate": u"估算或样本查询",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_total_resistance",
    "name": u"吸入管路的总阻力",
    "symbol": u"H’",
    "unit": u"m",
    "calculate": u"估算",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_inlet_speed",
    "name": u"泵入口流速",
    "symbol": u"V",
    "unit": u"m/s",
    "calculate": u"一般0.5~2",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_added_height",
    "name": u"附加高度",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"一般0.3~0.5",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "s_pump_install_height",
    "name": u"泵安装高度",
    "symbol": u"H",
    "unit": u"m",
    "calculate": u"除氧器最低压面距离泵入口中心线距离",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "new_steam_temperature",
    "name": u"新蒸汽温度",
    "symbol": u"t0",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "new_steam_pressure",
    "name": u"新蒸汽压力",
    "symbol": u"P0",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "new_steam_enthalpy",
    "name": u"新蒸汽焓",
    "symbol": u"h0",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "new_steam_flux",
    "name": u"新蒸汽流量",
    "symbol": u"q0",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "desuperheater_water_temperature",
    "name": u"减温水温度",
    "symbol": u"t1",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "desuperheater_water_pressure",
    "name": u"减温水压力",
    "symbol": u"P1",
    "unit": u"MPa",
    "calculate": u"减温减压器出口压力+1.47MPA",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "desuperheater_water_enthalpy",
    "name": u"减温水焓",
    "symbol": u"h1",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "desuperheater_water_flux",
    "name": u"减温水流量",
    "symbol": u"q1",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "desuperheater_steam_temperature",
    "name": u"减温后蒸汽温度",
    "symbol": u"t2",
    "unit": u"℃",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "desuperheater_steam_pressure",
    "name": u"减温后蒸汽压力",
    "symbol": u"P2",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "desuperheater_steam_enthalpy",
    "name": u"减温后蒸汽焓",
    "symbol": u"h2",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "saturation_water_enthalpy",
    "name": u"饱和水焓值",
    "symbol": u"h2’",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "no_vaporized_percent",
    "name": u"减温水中未蒸发部分所占份额",
    "symbol": u"t",
    "unit": u"",
    "calculate": u"0.3-0.35",
    "remark": u"", 
    "default_value": "0.35", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "de_press_temp_device_flux",
    "name": u"减温减压器流量",
    "symbol": u"q2",
    "unit": u"t/h",
    "calculate": u"q0+q1*（1-t）",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "charging_pressure",
    "name": u"充热压力",
    "symbol": u"P1",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "exothermic_pressure",
    "name": u"放热压力",
    "symbol": u"P2",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "charging_saturation_water_enthalpy",
    "name": u"充热压力下的饱和水焓",
    "symbol": u"h1‘",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "exothermic_saturation_water_enthalpy",
    "name": u"放热压力下的饱和水焓",
    "symbol": u"h2‘",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "charging_saturation_steam_enthalpy",
    "name": u"充热压力下的饱和汽焓",
    "symbol": u"h1”",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "exothermic_saturation_steam_enthalpy",
    "name": u"放热压力下的饱和汽焓",
    "symbol": u"h2”",
    "unit": u"kj/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "p2_steam_amount",
    "name": u"P2压力下产生蒸汽量",
    "symbol": u"g",
    "unit": u"kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "charging_water_specific_volume",
    "name": u"充热压力下的饱和水比容",
    "symbol": u"r1'",
    "unit": u"m3/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "unit_water_heat_amount",
    "name": u"单位水容积蓄热量",
    "symbol": u"gs",
    "unit": u"kg/m3",
    "calculate": u"g/r1'",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "regenerarot_efficiency",
    "name": u"蓄热器热效率",
    "symbol": u"η",
    "unit": u"",
    "calculate": u"0.95~0.99",
    "remark": u"", 
    "default_value": "0.95", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "water_fill_coefficient",
    "name": u"充水系数",
    "symbol": u"η2",
    "unit": u"",
    "calculate": u"0.65~0.85",
    "remark": u"", 
    "default_value": "0.85", 
 	"disable": ""},
  {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "regenerarot_heat_amount",
    "name": u"蓄热器的蓄热量",
    "symbol": u"G",
    "unit": u"t",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "regenerarot_volume",
    "name": u"蓄热器容积",
    "symbol": u"V",
    "unit": u"m3",
    "calculate": u"G/gs*η*η2",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "regenerarot_top_steam_volume",
    "name": u"蓄热器上部蒸汽容积",
    "symbol": u"V''",
    "unit": u"m3",
    "calculate": u"（1-η2）*V",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "boiler_max_load",
    "name": u"锅炉最大负荷",
    "symbol": u"Dmax",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "boiler_average_load",
    "name": u"锅炉平均负荷",
    "symbol": u"Di",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "regenerarot_max_bleed",
    "name": u"蓄热器最大放汽量",
    "symbol": u"D",
    "unit": u"t/h",
    "calculate": u"Dmax-Di",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "evaporation_capacity",
    "name": u"质量蒸发强度",
    "symbol": u"R2",
    "unit": u"R2<R2'",
    "calculate": u"D/V''",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "exothermic_evaporation_capacity",
    "name": u"放热压力下的质量蒸发强度",
    "symbol": u"R2'",
    "unit": u"R2<R2'",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": ""},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "charging_volume",
    "name": u"充热状态下的体积",
    "symbol": u"V1",
    "unit": u"m3",
    "calculate": u"G/gs",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "exothermic_water_specific_volume",
    "name": u"放热压力下的饱和水比容",
    "symbol": u"r2’",
    "unit": u"m3/kg",
    "calculate": u"",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"},
 {
    "module_name": "GPG_BoilerAuxiliaries",
    "name_eng": "exothermic_water_volume",
    "name": u"放热完了水的体积",
    "symbol": u"V2",
    "unit": u"m3",
    "calculate": u"（V1*r1'-G)/r2'",
    "remark": u"", 
    "default_value": "", 
 	"disable": "T"}
]

# 煤气发电 汽水管道
GPGSteamWaterPipe_data = [{
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "design_pressure",
        "name": u"设计压力",
        "symbol": u"P",
        "unit": u"Mpa",
        "calculate": u"最大工作压力",
        "remark": u"锅炉BMCR下工作压力，若有超压，计算超压"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "design_temperature",
        "name": u"设计温度",
        "symbol": u"T",
        "unit": u"℃",
        "calculate": u"最大工作温度",
        "remark": u"锅炉过热器出口额定温度+5℃"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "steel",
        "name": u"钢材",
        "symbol": u"",
        "unit": u"",
        "calculate": u"参见常用国产钢材许用应力",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "temperature_stress",
        "name": u"设计温度下许用应力",
        "symbol": u"[µ]t",
        "unit": u"Mpa",
        "calculate": u"参见常用国产钢材许用应力",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "20c_stress",
        "name": u"20℃下许用应力",
        "symbol": u"[µ]20",
        "unit": u"Mpa",
        "calculate": u"参见常用国产钢材许用应力",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "nominal_pressure",
        "name": u"公称压力",
        "symbol": u"PN",
        "unit": u"Mpa",
        "calculate": u"P*[µ]200/[µ]t",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "pipe_mass_flow",
        "name": u"管子质量流量",
        "symbol": u"Q",
        "unit": u"t/h",
        "calculate": u"设计参数",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "selected_velocity",
        "name": u"选取流速",
        "symbol": u"ε",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "meida_specific_volume",
        "name": u"介质比容",
        "symbol": u"v",
        "unit": u"m3/kg",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "inner_diamete",
        "name": u"管子内径",
        "symbol": u"Di",
        "unit": u"mm",
        "calculate": u"594.7*（Qv/w）²",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SteamWaterPipe",
        "name_eng":
        "temperature_correct_coefficient",
        "name":
        u"温度修正系数",
        "symbol":
        u"Y",
        "unit":
        u"",
        "calculate":
        u"（1）铁素体钢≤482-0.4；510-0.5；≥538-0.7（2）奥氏体钢≤566-0.4；593-0.5；≥621-0.7",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "stress_correct_coefficient",
        "name": u"许用应力修正系数",
        "symbol": u"η",
        "unit": u"",
        "calculate": u"无缝钢管1.0；螺旋焊管0.9",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "additional_thickness",
        "name": u"附加厚度",
        "symbol": u"α",
        "unit": u"mm",
        "calculate": u"一般不考虑，排污、再循环工业水、高加疏水取2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "pipe_min_thickness",
        "name": u"直管最小壁厚",
        "symbol": u"Sm",
        "unit": u"mm",
        "calculate": u"见常用数据选取",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "negative_deviation_coefficient",
        "name": u"壁厚负偏差系数",
        "symbol": u"A",
        "unit": u"",
        "calculate": u"取负偏差-5%下的A",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "negative_deviation_added_value",
        "name": u"壁厚负偏差附加值",
        "symbol": u"C",
        "unit": u"mm",
        "calculate": u"A*sm",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "calculate_thickness",
        "name": u"计算壁厚",
        "symbol": u"Sc",
        "unit": u"mm",
        "calculate": u"Sm+c",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "calculate_outer_diameter",
        "name": u"计算外径",
        "symbol": u"Do",
        "unit": u"mm",
        "calculate": u"2*Sc+Di",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "selected_nominal_diameter",
        "name": u"取值--公称通径",
        "symbol": u"Dn",
        "unit": u"mm",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "selected_outer_diameter",
        "name": u"取值--外径",
        "symbol": u"OD",
        "unit": u"mm",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "selected_thickness",
        "name": u"取值--壁厚",
        "symbol": u"S",
        "unit": u"mm",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "selected_inner_diameter",
        "name": u"取值--内径",
        "symbol": u"Di’",
        "unit": u"mm",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "backstepping_velocity",
        "name": u"反推流速",
        "symbol": u"ε’",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "selected_pipe_spec",
        "name": u"最终选取管道规格",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "work_press",
        "name": u"运行压力（表压)",
        "symbol": u"P",
        "unit": u"Mpa",
        "calculate": u"锅炉厂资料",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "work_temperature",
        "name": u"运行温度",
        "symbol": u"T",
        "unit": u"℃",
        "calculate": u"锅炉厂资料",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "rated_flow",
        "name": u"额定流量",
        "symbol": u"G",
        "unit": u"t/h",
        "calculate": u"锅炉厂资料",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "msv",
        "name": u"介质比容",
        "symbol": u"γ",
        "unit": u"m³/kg",
        "calculate": u"水蒸汽计算表",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "media_viscosity",
        "name": u"介质运动粘度",
        "symbol": u"υ",
        "unit": u"m²/s",
        "calculate": u"水蒸汽计算表",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "velocity",
        "name": u"流速",
        "symbol": u"W",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "calculate_velocity",
        "name": u"计算流速",
        "symbol": u"W",
        "unit": u"m/s",
        "calculate": u"0.3537Gγ/Di2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "dynamic_head",
        "name": u"动压头",
        "symbol": u"Hd",
        "unit": u"Pa",
        "calculate": u"W2/（2γ）",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "pipe_outer_diameter",
        "name": u"管道外径",
        "symbol": u"D",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "pipe_thickness",
        "name": u"管道壁厚",
        "symbol": u"S",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "pipe_inner_diameter",
        "name": u"管道内径",
        "symbol": u"Di",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "friction_resistance",
        "name": u"摩擦阻力",
        "symbol": u"△Pm",
        "unit": u"Pa",
        "calculate": u"△Pd*L",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "reynolds",
        "name": u"雷诺数",
        "symbol": u"Re",
        "unit": u"",
        "calculate": u"W*Di/υ",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "equivalent_roughness",
        "name": u"等值粗糙度",
        "symbol": u"ε",
        "unit": u"mm",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "relative_roughness",
        "name": u"相对粗糙度",
        "symbol": u"ε/Di",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "resistance_coefficient",
        "name": u"摩擦阻力系数",
        "symbol": u"λ",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "unit_length_resistance",
        "name": u"单位长度摩擦阻力",
        "symbol": u"△Pd",
        "unit": u"Pa/m",
        "calculate": u"λ*Hd/Di",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "pipe_length",
        "name": u"管道长度",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "local_resistance",
        "name": u"局部阻力",
        "symbol": u"△Pj",
        "unit": u"Pa",
        "calculate": u"ζ*Hd",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "total_local_resistance_coefficient",
        "name": u"局部阻力系数合计",
        "symbol": u"ζ",
        "unit": u"",
        "calculate": u"ξ1+ξ2+ξ3+ξ4+ξ5+ξ6",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "elbow_resistance_coefficient",
        "name": u"弯头阻力系数",
        "symbol": u"ξ1",
        "unit": u"",
        "calculate": u"n1*ξ1'",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "elbow_spec",
        "name": u"弯头规格",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "elbow_radius",
        "name": u"弯头半径",
        "symbol": u"R",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "elbow_radius_to_inner_diameter",
        "name": u"弯头半径 / 管道内径",
        "symbol": u"R/Di",
        "unit": u"",
        "calculate": u"R/Di",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "90elbow_resistance_coefficient",
        "name": u"单个90º弯头阻力系数",
        "symbol": u"ξ1'",
        "unit": u"",
        "calculate": u"14λ",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "90elbow_count",
        "name": u"90º弯头数量",
        "symbol": u"n1",
        "unit": u"个",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "triplet_resistance_coefficient",
        "name": u"三通阻力系数",
        "symbol": u"ξ2",
        "unit": u"",
        "calculate": u"n2*ξ2'",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "single_triplet_resistance_coefficient",
        "name": u"单个三通阻力系数",
        "symbol": u"ξ2'",
        "unit": u"",
        "calculate": u"60λ",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "triplet_count",
        "name": u"三通数量",
        "symbol": u"n2",
        "unit": u"个",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "reducer_resistance_coefficient",
        "name": u"异径管的阻力系数",
        "symbol": u"ξ3",
        "unit": u"",
        "calculate": u"ξ31+ξ32",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "converging_resistance_coefficient",
        "name": u"渐缩管（相应于小管径的阻力系数）",
        "symbol": u"ξ31",
        "unit": u"",
        "calculate": u"0.8sinθ*(1-β2)/β4",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "converging_spec",
        "name": u"异径管规格（渐缩管）",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "converging_angle",
        "name": u"角度（渐缩管）",
        "symbol": u"θ",
        "unit": u"度",
        "calculate": u"tan-1[(d2-d1)/2/L]",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "converging_diameter_radio",
        "name": u"较小直径与较大直径之比（渐缩管）",
        "symbol": u"β",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "increasing_resistance_coefficient",
        "name": u"渐扩管（相应于大管径的阻力系数）",
        "symbol": u"ξ32",
        "unit": u"",
        "calculate": u"2.6sinθ*(1-β2)2/β4",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "increasing_spec",
        "name": u"异径管规格（渐扩管）",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "increasing_angle",
        "name": u"角度（渐扩管）",
        "symbol": u"θ",
        "unit": u"",
        "calculate": u"tan-1[(d2-d1)/2/L]",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "increasing_diameter_radio",
        "name": u"较小直径与较大直径之比（渐扩管）",
        "symbol": u"β",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "in_out_resistance_coefficient",
        "name": u"管道入口与出口阻力系数",
        "symbol": u"ξ4",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "valve_resistance_coefficient",
        "name": u"阀门的局部阻力系数",
        "symbol": u"ξ5",
        "unit": u"",
        "calculate": u"ξ51+ξ52+ξ53+ξ54",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "filter",
        "name": u"滤网",
        "symbol": u"ξ51",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "sluice_resistance_coefficient",
        "name": u"闸阀阻力系数",
        "symbol": u"ξ52",
        "unit": u"",
        "calculate": u"ξ'52*n52",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "single_sluice_resistance_coefficient",
        "name": u"单个闸阀阻力系数",
        "symbol": u"ξ'52",
        "unit": u"",
        "calculate": u"8λ",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "sluice_count",
        "name": u"闸阀数量",
        "symbol": u"n52",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "check_resistance_coefficient",
        "name": u"止回阀阻力系数",
        "symbol": u"ξ53",
        "unit": u"",
        "calculate": u"ξ'53*n53",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "single_check_resistance_coefficient",
        "name": u"单个止回阀阻力系数",
        "symbol": u"ξ'53",
        "unit": u"",
        "calculate": u"600λ",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "check_count",
        "name": u"止回阀数量",
        "symbol": u"n53",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "regulating_resistance_coefficient",
        "name": u"调节阀阻力系数",
        "symbol": u"ξ54",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "plate_resistance_coefficient",
        "name": u"流量测量孔板阻力系数",
        "symbol": u"ξ6",
        "unit": u"",
        "calculate": u"△P2/Hd",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SteamWaterPipe",
        "name_eng": "measuring_pressure_loss",
        "name": u"测量装置压损",
        "symbol": u"△P2",
        "unit": u"Pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""}
]

# 煤气发电 汽机辅机系统
GPGTurbineAuxiliarySystem_data = [
    {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "deaerator_work_pressure",
        "name": u"除氧器工作压力",
        "symbol": u"P",
        "unit": u"Mpa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "deaerator_condensation_well_pressure_difference",
        "name":
        u"除氧器凝结水入口与凝汽器热井最低水位间的水柱静压差",
        "symbol":
        u"H1",
        "unit":
        u"m",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "deaerator_condensation_spray_pressure",
        "name":
        u"除氧器入口凝结水管喷雾头所需喷雾压力",
        "symbol":
        u"H2",
        "unit":
        u"m",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condenser_maximum_vacuum",
        "name": u"凝汽器的最高真空",
        "symbol": u"P",
        "unit": u"Mpa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "deaerator_condensation_well_pipe_resistance",
        "name":
        u"从热井到除氧器凝结水入口的凝结水管道流动阻力",
        "symbol":
        u"H3",
        "unit":
        u"m",
        "calculate":
        u"另加20%裕量",
        "remark":
        u"一般采用5m H2O"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condensate_pump_design_lift",
        "name": u"凝结水泵的设计扬程",
        "symbol": u"H",
        "unit": u"m",
        "calculate": u"101.97P+H1+H2+H3",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condensate_pump_flow",
        "name": u"流量",
        "symbol": u"Q",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condensate_pump_efficiency",
        "name": u"泵效率",
        "symbol": u"η",
        "unit": u"",
        "calculate": u"0.6~0.8",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "condensate_pump_transmission_efficiency",
        "name":
        u"机械传动效率",
        "symbol":
        u"η2",
        "unit":
        u"",
        "calculate":
        u"直连1.0，联轴器0.98，皮带0.95",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "condensate_pump_motor_efficiency",
        "name":
        u"电动机效率",
        "symbol":
        u"η3",
        "unit":
        u"",
        "calculate":
        u"通常取0.9",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "condensate_pump_motor_spare_coefficient",
        "name":
        u"电动机备用系数",
        "symbol":
        u"β",
        "unit":
        u"",
        "calculate":
        u"查表选取",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condensate_pump_motor_power",
        "name": u"配套电机功率",
        "symbol": u"P",
        "unit": u"kw",
        "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condensate_pump_selected",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"",
        "calculate": u"一用一备",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "extractor_work_pressure",
        "name": u"射水抽气器工作压力",
        "symbol": u"P1",
        "unit": u"Mpa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "ejection_tank_work_pressure",
        "name": u"射水箱工作压力",
        "symbol": u"P2",
        "unit": u"Mpa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "extractor_ejection_waterline_height_difference",
        "name":
        u"射水抽气器安装高度与射水箱最高水位之差",
        "symbol":
        u"H1",
        "unit":
        u"M",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "jet_pump_pipe_loss",
        "name": u"射水泵进出口管路损失",
        "symbol": u"H2",
        "unit": u"M",
        "calculate": u"一般采用5m H2O",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "jet_pump_total_lift",
        "name": u"总扬程",
        "symbol": u"H",
        "unit": u"M",
        "calculate": u"101.97(P1-P2)+H1+H2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "jet_pump_flow",
        "name": u"流量",
        "symbol": u"Q",
        "unit": u"t/h",
        "calculate": u"汽轮机资料",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "jet_pump_efficiency",
        "name": u"泵效率",
        "symbol": u"η",
        "unit": u"",
        "calculate": u"0.6~0.8",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "jet_pump_transmission_efficiency",
        "name":
        u"机械传动效率",
        "symbol":
        u"η2",
        "unit":
        u"",
        "calculate":
        u"直连1.0，联轴器0.98，皮带0.95",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "jet_pump_motor_efficiency",
        "name": u"电动机效率",
        "symbol": u"η3",
        "unit": u"",
        "calculate": u"通常取0.9",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "jet_pump_motor_spare_coefficient",
        "name":
        u"电动机备用系数",
        "symbol":
        u"β",
        "unit":
        u"",
        "calculate":
        u"查表选取",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "jet_pump_motor_power",
        "name": u"配套电机功率",
        "symbol": u"β",
        "unit": u"",
        "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "jet_pump_selected",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_ejection_tank_work_pressure",
        "name":
        u"射水箱工作压力",
        "symbol":
        u"P1",
        "unit":
        u"Mpa",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_circulating_water_to_header_pressure",
        "name":
        u"循环水回水母管压力",
        "symbol":
        u"P2",
        "unit":
        u"Mpa",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_extractor_ejection_waterline_height_difference",
        "name":
        u"射水抽气器安装高度与射水箱最高水位之差",
        "symbol":
        u"H1",
        "unit":
        u"M",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_jet_pump_pipe_loss",
        "name": u"射水泵进出口管路损失",
        "symbol": u"H2",
        "unit": u"M",
        "calculate": u"一般采用5m H2O",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_jet_pump_total_lift",
        "name": u"总扬程",
        "symbol": u"H",
        "unit": u"M",
        "calculate": u"101.97(P2-P1)+H1+H2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_jet_pump_flow",
        "name": u"流量",
        "symbol": u"Q",
        "unit": u"t/h",
        "calculate": u"已知（半小时抽完射水箱水）",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_jet_pump_efficiency",
        "name": u"泵效率",
        "symbol": u"η",
        "unit": u"",
        "calculate": u"0.6~0.8",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_jet_pump_transmission_efficiency",
        "name":
        u"机械传动效率",
        "symbol":
        u"η2",
        "unit":
        u"",
        "calculate":
        u"直连1.0，联轴器0.98，皮带0.95",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_jet_pump_motor_efficiency",
        "name":
        u"电动机效率",
        "symbol":
        u"η3",
        "unit":
        u"",
        "calculate":
        u"通常取0.9",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_jet_pump_motor_spare_coefficient",
        "name":
        u"电动机备用系数",
        "symbol":
        u"β",
        "unit":
        u"",
        "calculate":
        u"查表选取",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_jet_pump_motor_power",
        "name": u"配套电机功率",
        "symbol": u"β",
        "unit": u"",
        "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_jet_pump_selected",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condenser_flow_amount",
        "name": u"凝汽量",
        "symbol": u"Dn",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condenser_pressure",
        "name": u"凝汽器压力",
        "symbol": u"Pk",
        "unit": u"kpa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "turbine_exhaust_enthalpy",
        "name": u"汽轮机排汽焓",
        "symbol": u"Hs",
        "unit": u"kj/kg",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_water_inlet_temperature",
        "name":
        u"冷却水进口温度",
        "symbol":
        u"t1",
        "unit":
        u"℃",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "saturation_temperature",
        "name": u"饱和温度",
        "symbol": u"tbh",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "supercooling_degree",
        "name": u"过冷度",
        "symbol": u"t'",
        "unit": u"℃",
        "calculate": u"0~2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condensate_water_temperature",
        "name": u"凝结水温度",
        "symbol": u"tc",
        "unit": u"℃",
        "calculate": u"tbh-t'",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condensate_water_enthalpy",
        "name": u"凝结水焓",
        "symbol": u"hc",
        "unit": u"kj/kg",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_pipe_clean_coefficient",
        "name":
        u"冷却管的洁净系数",
        "symbol":
        u"ξc",
        "unit":
        u"",
        "calculate":
        u"直流0.8~0.85，循环0.7~0.8",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_pipe_correct_coefficient",
        "name":
        u"冷却管材料和壁厚的修正系数",
        "symbol":
        u"ξm",
        "unit":
        u"",
        "calculate":
        u"黄铜管为 ，铝黄铜管为 ，B5铜镍合金管为 ，B30铜镍合金管为 ，不锈钢管为 ",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "calculate_exponent",
        "name":
        u"计算指数",
        "symbol":
        u"χ",
        "unit":
        u"",
        "calculate":
        u"计算指数 t1≤26.7时，χ=0.122*ξc*ξm*(1+0.15*t1)",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_pipe_flow_velocity",
        "name": u"冷却管内流速",
        "symbol": u"Vw",
        "unit": u"m/s",
        "calculate": u"1.5~2.5",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_pipe_diameter",
        "name": u"冷却管内径",
        "symbol": u"d2",
        "unit": u"m",
        "calculate": u"冷却管规格25*1",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "condenser_steam_load_correct_coefficient",
        "name":
        u"凝汽器比蒸汽负荷修正系数",
        "symbol":
        u"b",
        "unit":
        u"",
        "calculate":
        u"取0.42",
        "remark":
        u""
    	, "default_value": "0.42", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_pipe_flow_velocity_correct_coefficient",
        "name":
        u"冷却管内流速的修正系数",
        "symbol":
        u"Φw",
        "unit":
        u"",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_water_inlet_temperature_correct_coefficient",
        "name":
        u"冷却水进口温度修正系数",
        "symbol":
        u"Φt",
        "unit":
        u"",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_water_pass_correct_coefficient",
        "name":
        u"冷却水流程数的修正系数",
        "symbol":
        u"Φz",
        "unit":
        u"",
        "calculate":
        u"冷却水流程数Z=2时，取1",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "condenser_steam_load_change_correct_coefficient",
        "name":
        u"考虑凝汽器蒸汽负荷变化的修正系数",
        "symbol":
        u"Φδ",
        "unit":
        u"",
        "calculate":
        u"额定工况",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "total_heat_transfer_coefficient",
        "name":
        u"总传热系数",
        "symbol":
        u"K",
        "unit":
        u"",
        "calculate":
        u"K=4.07*ξc*ξm*Φw*Φt*Φz*Φδ",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "condenser_heat_load",
        "name": u"凝汽器热负荷",
        "symbol": u"Q",
        "unit": u"kw",
        "calculate": u"Dn*(hs-hc)",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "circulation_ratio",
        "name": u"循环倍率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"55~70，按地区选择",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "circulating_water_amount",
        "name": u"循环水量",
        "symbol": u"Dw",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_water_temperature_rise",
        "name":
        u"冷却水温升",
        "symbol":
        u"△t",
        "unit":
        u"℃",
        "calculate":
        u"Q/Dw*Cp",
        "remark":
        u"冷却水Cp 取4.1868"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "cooling_water_outlet_temperature",
        "name":
        u"冷却水出口温度",
        "symbol":
        u"t2",
        "unit":
        u"℃",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "logarithmic_average_temperature_difference",
        "name":
        u"对数平均温差",
        "symbol":
        u"△tm",
        "unit":
        u"℃",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_TurbineAuxiliarySystem",
        "name_eng": "cooling_area",
        "name": u"冷却面积",
        "symbol": u"A",
        "unit": u"m2",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_TurbineAuxiliarySystem",
        "name_eng":
        "vacuum_pump_condensate_flow_amount",
        "name":
        u"凝汽量",
        "symbol":
        u"Dn",
        "unit":
        u"t/h",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""}
]

# 煤气发电 烟风量计算
GPGSmokeAirCalculate_data = [{
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "h2",
        "name": u"H2",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "co",
        "name": u"CO",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "ch4",
        "name": u"CH4",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "c2h4",
        "name": u"C2H4",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "c3h8",
        "name": u"C3H8",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "c4h10",
        "name": u"C4H10",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "n2",
        "name": u"N2",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "o2",
        "name": u"O2",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "co2",
        "name": u"CO2",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "h2s",
        "name": u"H2S",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "cmhn",
        "name": u"CmHn",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_need_air_amonut_per_m3",
        "name": u"标态下每m³干燃气燃烧所需理论空气量",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_air_density",
        "name": u"标态下空气密度",
        "symbol": u"ρ0",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "1.293", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_need_air_mass_per_m3",
        "name": u"标态下每m³干燃气燃烧所需理论空气质量",
        "symbol": u"L0",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "excessive_air_coefficient",
        "name": u"过量空气系数",
        "symbol": u"α",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"1.05-1.1"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "actual_need_air_amonut",
        "name": u"实际所需空气量",
        "symbol": u"V",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_gas_humidity_per_m3",
        "name": u"标态下每m³燃气的含湿量",
        "symbol": u"dR",
        "unit": u"g/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_air_humidity_per_m3",
        "name": u"标态下每m³空气的含湿量",
        "symbol": u"dK",
        "unit": u"g/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "actual_air_amount_in_wet",
        "name": u"空气中有水时，实际空气量",
        "symbol": u"V",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_ro2_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中RO2",
        "symbol": u"VRO2",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_n2_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中N2",
        "symbol": u"VN2",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_actual_n2_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中N2实际",
        "symbol": u"VN2",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_h2o_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中H2O",
        "symbol": u"VH2O",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_actual_h2o_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中H2O实际",
        "symbol": u"VH2O",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_o2_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中O2",
        "symbol": u"VO2",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "actual_burning_gas_amonut",
        "name": u"实际燃烧烟气量",
        "symbol": u"Vy",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "theory_burning_gas_amonut",
        "name": u"理论燃烧烟气量",
        "symbol": u"Vy",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "net_calorific_value",
        "name": u"低位发热量",
        "symbol": u"Hl",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "gross_heating_value",
        "name": u"高位发热量",
        "symbol": u"Hh",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "gas_init_temperature",
        "name": u"燃气初始温度",
        "symbol": u"tg",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "air_init_temperature",
        "name": u"空气初始温度",
        "symbol": u"tg",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "gas_average_cpvh",
        "name": u"燃气平均定压体积热容",
        "symbol": u"Cg",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "gas_h2o_average_cpvh",
        "name": u"燃气中H2O平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "air_average_cpvh",
        "name": u"空气平均定压体积热容",
        "symbol": u"Ca",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "air_h2o_average_cpvh",
        "name": u"空气中H2O平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "hy_adiabatic_calorimeter_temperature",
        "name": u"假设---绝热状态的热量计温度",
        "symbol": u"tc",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"1300℃~1500℃"
    	, "default_value": "1400", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_ro2_average_cpvh",
        "name": u"烟气中RO2平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_h2o_average_cpvh",
        "name": u"烟气中H2O平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_n2_average_cpvh",
        "name": u"烟气中N2平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_o2_average_cpvh",
        "name": u"烟气中O2平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "calc_adiabatic_calorimeter_temperature",
        "name":
        u"计算---绝热状态的热量计温度",
        "symbol":
        u"tc",
        "unit":
        u"℃",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "deviation_check",
        "name": u"误差核对---2%以内合理",
        "symbol": u"",
        "unit": u"%",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "incomplete_combustion_loss_coefficient",
        "name":
        u"化学不完全燃烧热损失系数",
        "symbol":
        u"q3",
        "unit":
        u"%",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "incomplete_combustion_loss",
        "name": u"化学不完全燃烧热损失",
        "symbol": u"Q3",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "heat_loss_coefficient",
        "name": u"散热损失系数",
        "symbol": u"q5",
        "unit": u"%",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "heat_loss",
        "name": u"散热损失",
        "symbol": u"Q5",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "calc_theory_burning_temperature",
        "name": u"计算---理论燃烧温度",
        "symbol": u"tc",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "high_temperature_coefficient",
        "name": u"高温系数",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "coefficient_actual_temperature",
        "name": u"实际燃烧温度--系数法",
        "symbol": u"tc",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "calc_actual_temperature",
        "name": u"实际燃烧温度--计算法",
        "symbol": u"tc",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "ro2_volume_enthalpy",
        "name": u"烟气中R02体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "n2_volume_enthalpy",
        "name": u"烟气中N2体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "h2o_volume_enthalpy",
        "name": u"烟气中H2O体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "air_volume_enthalpy",
        "name": u"烟气中空气体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "dust_volume_enthalpy",
        "name": u"烟气中飞灰体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "theory_smoke_volume_enthalpy",
        "name": u"理论烟气体积焓",
        "symbol": u"hy0",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "theory_air_volume_enthalpy",
        "name": u"理论空气体积焓",
        "symbol": u"hk0",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "theory_dust_volume_enthalpy",
        "name": u"理论飞灰体积焓",
        "symbol": u"hfh",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "0", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_enthalpy",
        "name": u"烟气焓",
        "symbol": u"hy",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "qd_net",
        "name": u"燃气干燥基低位发热量",
        "symbol": u"Qd.net",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "qar_net",
        "name": u"燃气收到基地位发热量",
        "symbol": u"Qar.net",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_need_air_amonut_b_10500",
        "name": u"标态下每m³干燃气燃烧所需理论空气量(Qd.net<10500时)",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_need_air_amonut_a_10500",
        "name": u"标态下每m³干燃气燃烧所需理论空气量(Qd.net>10500时)",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_need_air_amonut_gas",
        "name": u"标态下每m³干燃气燃烧所需理论空气量(天然气)",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_need_air_amonut_lng",
        "name": u"标态下每m³干燃气燃烧所需理论空气量(液化石油气)",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_excessive_air_coefficient",
        "name": u"过量空气系数",
        "symbol": u"α",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_actual_need_air_amonut",
        "name": u"标态下每m³干燃气燃烧所需实际空气量",
        "symbol": u"V",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_theory_burning_amonut_gas",
        "name": u"理论燃烧烟气量(天然气)",
        "symbol": u"Vy'",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_theory_burning_amonut_oag",
        "name": u"理论燃烧烟气量(石油伴生气)",
        "symbol": u"Vy'",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_theory_burning_amonut_lng",
        "name": u"理论燃烧烟气量(液化天然气)",
        "symbol": u"Vy'",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_theory_burning_amonut_cog",
        "name": u"理论燃烧烟气量(焦炉煤气)",
        "symbol": u"Vy'",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "unknown_theory_burning_amonut_b_12600",
        "name":
        u"理论燃烧烟气量(Qar.net<12600)",
        "symbol":
        u"Vy'",
        "unit":
        u"m³/m³",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_actual_burning_gas_amonut",
        "name": u"实际燃烧烟气量",
        "symbol": u"Vy",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "unknown_boiler_actual_burning_gas_amonut",
        "name":
        u"高炉煤气实际燃烧烟气量",
        "symbol":
        u"Vy",
        "unit":
        u"m³/m³",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "unknown_gas_actual_burning_gas_amonut",
        "name":
        u"天然气实际燃烧烟气量",
        "symbol":
        u"Vy",
        "unit":
        u"m³/m³",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_theory_air_amount_a_35799",
        "name": u"理论空气量(QL＞35799)",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_theory_air_amount_b_35799",
        "name": u"理论空气量(QL＜35799)",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_excessive_air_coefficient",
        "name": u"过量空气系数",
        "symbol": u"α",
        "unit": u"",
        "calculate": u"1.05~1.1",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_actual_amonut_a_35799",
        "name": u"实际烟气量(QL＞35799)",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_actual_amonut_b_35799",
        "name": u"实际烟气量(QL＜35799)",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_boiler_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "exp_boiler_theory_air_amount_a_12561",
        "name":
        u"理论空气量(QL＞12561)",
        "symbol":
        u"L0",
        "unit":
        u"m³/m³",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "exp_boiler_theory_air_amount_b_12561",
        "name":
        u"理论空气量(QL＜12561)",
        "symbol":
        u"L0",
        "unit":
        u"m³/m³",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "exp_boiler_excessive_air_coefficient",
        "name":
        u"过量空气系数",
        "symbol":
        u"α",
        "unit":
        u"",
        "calculate":
        u"1.05~1.1",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_boiler_actual_amonut_a_12561",
        "name": u"实际烟气量(QL＞12561)",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_boiler_actual_amonut_b_12561",
        "name": u"实际烟气量(QL＜12561)",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_liquid_fuel_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_liquid_fuel_theory_air_amount",
        "name": u"理论空气量",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "exp_liquid_fuel_excessive_air_coefficient",
        "name":
        u"过量空气系数",
        "symbol":
        u"α",
        "unit":
        u"m³/m³",
        "calculate":
        u"1.1~1.2",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_liquid_fuel_actual_amonut",
        "name": u"实际烟气量",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_coal_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_coal_theory_air_amount",
        "name": u"理论空气量",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_coal_excessive_air_coefficient",
        "name": u"过量空气系数",
        "symbol": u"α",
        "unit": u"m³/m³",
        "calculate": u"1.15~1.25",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_coal_actual_amonut",
        "name": u"实际烟气量",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_water_content",
        "name": u"含水量",
        "symbol": u"W",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_theory_air_amount",
        "name": u"理论空气量",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "exp_wood_peat_excessive_air_coefficient",
        "name":
        u"过量空气系数",
        "symbol":
        u"α",
        "unit":
        u"m³/m³",
        "calculate":
        u"1.15~1.25",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_best_water_content",
        "name": u"最佳含水量",
        "symbol": u"Wop",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_actual_amonut",
        "name": u"实际烟气量",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"}
]

# 煤气发电 循环水系统
GPGCirculatingWaterSystem_data = [{
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "steam_exhaust_flux_winter",
        "name": u"冬季乏汽流量",
        "symbol": u"",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "steam_exhaust_flux_summer",
        "name": u"夏季乏汽流量",
        "symbol": u"",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "steam_exhaust_flux_selected",
        "name": u"乏汽流量-选定",
        "symbol": u"",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u"选定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulation_ratio_winter",
        "name": u"冬季循环倍率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"北方60~70；中部65~75；南方70~80"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulation_ratio_summer",
        "name": u"夏季循环倍率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"北方60~70；中部65~75；南方70~80"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulation_water_flow_winter",
        "name": u"冬季循环水量",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulation_water_flow_summer",
        "name": u"夏季循环水量",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "auxiliary_cooling_water_flow_winter",
        "name":
        u"冬季辅机冷却水量",
        "symbol":
        u"",
        "unit":
        u"m3/h",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "auxiliary_cooling_water_flow_summer",
        "name":
        u"夏季辅机冷却水量",
        "symbol":
        u"",
        "unit":
        u"m3/h",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "total_circulation_water_flow_winter",
        "name":
        u"冬季总循环水量",
        "symbol":
        u"",
        "unit":
        u"m3/h",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "total_circulation_water_flow_summer",
        "name":
        u"夏季总循环水量",
        "symbol":
        u"",
        "unit":
        u"m3/h",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "selected_total_circulation_water_flow",
        "name": u"总循环水量-选定",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u"Q选定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "spray_density",
        "name": u"喷淋密度",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "spray_area",
        "name": u"喷淋面积",
        "symbol": u"",
        "unit": u"m2",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "in_out_water_temperature_difference",
        "name":
        u"进、出水口温差",
        "symbol":
        u"",
        "unit":
        u"℃",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "dry_bulb_temperature",
        "name": u"干球温度",
        "symbol": u"",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "dry_bulb_k_coefficient",
        "name": u"K",
        "symbol": u"",
        "unit": u"",
        "calculate": u"插值法",
        "remark": u"参考表5.6.1"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "evaporation_loss_rate",
        "name": u"蒸发损失率",
        "symbol": u"",
        "unit": u"%",
        "calculate": u"Pe=K*温差",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "evaporation_loss",
        "name": u"蒸发损失",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"Qe=Pe*Q/100",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "wind_blow_loss_rate",
        "name":
        u"风吹损失率",
        "symbol":
        u"",
        "unit":
        u"",
        "calculate":
        u"Pw：有除水器时为0.2%-0.3%；无除水器时≥0.5%",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "wind_blow_loss",
        "name": u"风吹损失",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "concentration_rate",
        "name": u"浓缩倍率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"C：一般取3",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "discharge_rate",
        "name": u"排污损失率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"Pb=（Pe-Pw（c-1））/（c-1）",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "discharge_capacity",
        "name": u"排污量",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "supply_water_amount",
        "name": u"补充水量",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_water_amount",
        "name": u"循环水池15-25分钟循环水量",
        "symbol": u"",
        "unit": u"m3",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_size_deep",
        "name": u"循环水池尺寸-深",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_size_length",
        "name": u"循环水池尺寸-长",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_size_width",
        "name": u"循环水池尺寸-宽",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_size_checked",
        "name": u"校核循环水池尺寸",
        "symbol": u"",
        "unit": u"m3",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "condenser_friction",
        "name": u"凝汽器阻力",
        "symbol": u"",
        "unit": u"Mpa",
        "calculate": u"",
        "remark": u"厂家提供"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "circulating_backwater_pressure",
        "name":
        u"循环水回水压力",
        "symbol":
        u"",
        "unit":
        u"Mpa",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "circulating_water_reservoir_pressure",
        "name":
        u"循环水吸水池压力",
        "symbol":
        u"",
        "unit":
        u"Mpa",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
{
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "condenser_circulating_water_inlet_pressure",
        "name":
        u"凝汽器循环水进水工作压力",
        "symbol":
        u"",
        "unit":
        u"Mpa",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "circulation_pump_outlet_to_condenser_inlet_height_difference",
        "name":
        u"循环水泵出口与凝汽器循环水进水口高度差",
        "symbol":
        u"",
        "unit":
        u"m",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "reservoir_to_pump_inlet_height_difference",
        "name":
        u"吸水池与水泵入口高度差",
        "symbol":
        u"",
        "unit":
        u"m",
        "calculate":
        u"",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pipe_loss",
        "name": u"管道损失",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"暂定采用5mH2O",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "y_filter_loss",
        "name": u"Y型过滤器损失",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u"厂家提供"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_CirculatingWaterSystem",
        "name_eng":
        "total_pumping_lift",
        "name":
        u"总扬程",
        "symbol":
        u"",
        "unit":
        u"m",
        "calculate":
        u"102*（P1-P2）+(H1-H2)+1.2*(H3+H4)",
        "remark":
        u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_flow",
        "name": u"流量",
        "symbol": u"",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_efficiency",
        "name": u"泵效率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"0.6~0.85"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_transmission_efficiency",
        "name": u"机械传动效率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"直连1.0，联轴器0.98，皮带0.95"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_motor_efficiency",
        "name": u"电动机效率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"通常取0.98"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_motor_spare_coefficient",
        "name": u"电动机备用系数",
        "symbol": u"",
        "unit": u"",
        "calculate": u"查表选取",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_matching_motor_power",
        "name": u"配套电机功率",
        "symbol": u"",
        "unit": u"kW",
        "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "selected_pump_model_power",
        "name": u"选用型号-功率",
        "symbol": u"",
        "unit": u"kW",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "selected_pump_model_flow",
        "name": u"选用型号-流量",
        "symbol": u"",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "selected_pump_model_lift",
        "name": u"选用型号-扬程",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
{
    "module_name": "GPG_CirculatingWaterSystem",
    "name_eng": "p_spray_density",
    "name": u"喷淋密度",
    "symbol": u"",
    "unit": u"--",
    "calculate": u"一般为6~7，取7",
    "remark": "",
    "default_value": "7",
    "disable": ""}, 
{
    "module_name": "GPG_CirculatingWaterSystem",
    "name_eng": "p_spray_area",
    "name": u"喉部喷淋面积",
    "symbol": u"",
    "unit": u"m2",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"}, 
{
    "module_name": "GPG_CirculatingWaterSystem",
    "name_eng": "p_select_f",
    "name": u"选型",
    "symbol": u"",
    "unit": u"m2",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""}, 
{
    "module_name": "GPG_CirculatingWaterSystem",
    "name_eng": "p_count",
    "name": u"数量",
    "symbol": u"",
    "unit": u"台",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""}, 
{
    "module_name": "GPG_CirculatingWaterSystem",
    "name_eng": "p_single_cold_amount",
    "name": u"单台冷却水量",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": "T"}, 
{
    "module_name": "GPG_CirculatingWaterSystem",
    "name_eng": "p_select_s",
    "name": u"选型",
    "symbol": u"",
    "unit": u"m3/h",
    "calculate": u"",
    "remark": "",
    "default_value": "",
    "disable": ""}
]

# 煤气发电 风阻力
GPGWindResistance_data = [
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "recommend_velocity_coldwind",
        "name": u"推荐流速",
        "symbol": u"",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"（8)P6"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "recommend_velocity_hotwind",
        "name": u"推荐流速",
        "symbol": u"",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"（8)P6"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_temperature",
        "name": u"计算温度",
        "symbol": u"T",
        "unit": u"℃",
        "calculate": u"给定",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_amount",
        "name": u"风量",
        "symbol": u"V",
        "unit": u"m³/h",
        "calculate": u"燃烧计算",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_density",
        "name": u"密度",
        "symbol": u"ρ",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_flow_velocity",
        "name": u"流速",
        "symbol": u"W",
        "unit": u"m/s",
        "calculate": u"取定",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_dynamic_pressure_head",
        "name": u"动压头",
        "symbol": u"Hd",
        "unit": u"Pa",
        "calculate": u"W2*ρ/2",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_section_area",
        "name": u"风管截面积",
        "symbol": u"F",
        "unit": u"m2",
        "calculate": u"V/W/3600",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_length",
        "name": u"长",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"取定",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"F/A",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_perimeter",
        "name": u"风管周长",
        "symbol": u"Lc",
        "unit": u"m",
        "calculate": u"2*(A+B)",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_equivalent_diameter",
        "name": u"管道当量直径",
        "symbol": u"De",
        "unit": u"m",
        "calculate": u"4*F/Lc",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_gas_kinetic_viscosity",
        "name": u"气体运动粘度",
        "symbol": u"υ",
        "unit": u"m2/s",
        "calculate": u"",
        "remark": u"（2）P288"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_reynolds_number",
        "name": u"雷诺数",
        "symbol": u"Re",
        "unit": u"",
        "calculate": u"W*De/υ",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_absolute_tube_roughness",
        "name": u"管道内壁绝对粗糙度",
        "symbol": u"△",
        "unit": u"m",
        "calculate": u"",
        "remark": u"（2）P109"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_relative_tube_roughness",
        "name": u"管道内壁相对粗糙度",
        "symbol": u"△1",
        "unit": u"m",
        "calculate": u"△/De",
        "remark": u"（2）P107"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_560_relative_tube_roughness",
        "name": u"560/△1",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_discriminant",
        "name": u"判别式",
        "symbol": u"",
        "unit": u"",
        "calculate": u"4000 <Re< 560/△1",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_frictional_resistance",
        "name": u"摩擦阻力",
        "symbol": u"△Pm1",
        "unit": u"Pa",
        "calculate": u"△Pd*L1",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_frictional_resistance_coefficient",
        "name": u"摩擦阻力系数",
        "symbol": u"λ",
        "unit": u"",
        "calculate": u"图7.2.2",
        "remark": u"（2）P108"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_unit_length_frictional_resistance",
        "name": u"单位长度摩擦阻力",
        "symbol": u"△Pd",
        "unit": u"Pa/m",
        "calculate": u"λ*Hd/De",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_ducting_length",
        "name": u"风管长度",
        "symbol": u"L1",
        "unit": u"m",
        "calculate": u"布置图",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_local_resistance",
        "name": u"局部阻力",
        "symbol": u"△Pj1",
        "unit": u"",
        "calculate": u"ζ*Hd",
        "remark": u"（2）P109"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_local_resistance_coefficient",
        "name": u"局部阻力系数",
        "symbol": u"ζ",
        "unit": u"",
        "calculate": u"ζ1+ζ2+ζ3",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_single_local_resistance_coefficient",
        "name": u"1个吸风口局部阻力系数",
        "symbol": u"ζ1",
        "unit": u"",
        "calculate": u"有档板门",
        "remark": u"（2）P140"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_single_bellows",
        "name": u"1个风机进口风箱",
        "symbol": u"ζ2",
        "unit": u"",
        "calculate": u"改进式进风箱",
        "remark": u"（2）P144"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_single_damper",
        "name": u"1个进口挡板门",
        "symbol": u"ζ3",
        "unit": u"",
        "calculate": u"假定θ=15°",
        "remark": u"（2）P130"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_total_pressure",
        "name": u"风机进口段总阻力",
        "symbol": u"△Pz1",
        "unit": u"",
        "calculate": u"△Pm1+△Pj1",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_frictional_resistance",
        "name": u"摩擦阻力",
        "symbol": u"△Pm2",
        "unit": u"Pa",
        "calculate": u"△Pd*L2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_unit_length_frictional_resistance",
        "name": u"单位长度摩擦阻力",
        "symbol": u"△Pd",
        "unit": u"Pa/m",
        "calculate": u"约同进口",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_ducting_length",
        "name": u"风管长度",
        "symbol": u"L2",
        "unit": u"m",
        "calculate": u"布置图估计",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_local_resistance",
        "name": u"局部阻力",
        "symbol": u"△Pj2",
        "unit": u"",
        "calculate": u"ζ*Hd",
        "remark": u"（2）P109"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_local_resistance_coefficient",
        "name": u"局部阻力系数",
        "symbol": u"ζ",
        "unit": u"",
        "calculate": u"ζ1+ζ2+ζ3",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_single_increase_pipe",
        "name": u"1只出口渐扩管",
        "symbol": u"ζ1",
        "unit": u"",
        "calculate": u"假定",
        "remark": u"（2）P136"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_90_section_slow_turn_elbow",
        "name": u"1只90度等截面急转弯头/（二次风2只）",
        "symbol": u"ζ2",
        "unit": u"",
        "calculate": u"ζ2",
        "remark": u"（2）P136"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_preheater_diffuser_pipe",
        "name": u"空预器接头扩散管",
        "symbol": u"ζ3",
        "unit": u"",
        "calculate": u"假定",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_to_preheater_total_pressure",
        "name": u"风机出口至空预器总阻力",
        "symbol": u"△Pz2",
        "unit": u"",
        "calculate": u"△Pm2+△Pj2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_temperature",
        "name": u"计算温度",
        "symbol": u"T",
        "unit": u"℃",
        "calculate": u"烟风量计算表",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_amount",
        "name": u"风量",
        "symbol": u"V",
        "unit": u"m³/h",
        "calculate": u"烟风量计算表",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_density",
        "name": u"密度",
        "symbol": u"ρ",
        "unit": u"kg/m³",
        "calculate": u"烟风量计算表",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_flow_velocity",
        "name": u"流速",
        "symbol": u"W",
        "unit": u"m/s",
        "calculate": u"取定",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_dynamic_pressure_head",
        "name": u"动压头",
        "symbol": u"Hd",
        "unit": u"Pa",
        "calculate": u"W2*ρ/2",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_section_area",
        "name": u"风管截面积（热风管分两路进入风室）",
        "symbol": u"F",
        "unit": u"m2",
        "calculate": u"V/W/3600/2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_diameter",
        "name": u"圆管直径(一、二次热风为圆管）",
        "symbol": u"D(De)",
        "unit": u"m",
        "calculate": u"F=0.785*D2",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_length",
        "name": u"长",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"取定",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"F/A",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_perimeter",
        "name": u"风管周长",
        "symbol": u"Lc",
        "unit": u"m",
        "calculate": u"2*(A+B)",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_equivalent_diameter",
        "name": u"管道当量直径",
        "symbol": u"De",
        "unit": u"m",
        "calculate": u"4*F/Lc",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_gas_kinetic_viscosity",
        "name": u"气体运动粘度",
        "symbol": u"υ",
        "unit": u"m2/s",
        "calculate": u"",
        "remark": u"（2）P288"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_reynolds_number",
        "name": u"雷诺数",
        "symbol": u"Re",
        "unit": u"",
        "calculate": u"W*De/υ",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_absolute_tube_roughness",
        "name": u"管道内壁绝对粗糙度",
        "symbol": u"△",
        "unit": u"m",
        "calculate": u"",
        "remark": u"（2）P109"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_relative_tube_roughness",
        "name": u"管道内壁相对粗糙度",
        "symbol": u"△1",
        "unit": u"m",
        "calculate": u"△/De",
        "remark": u"（2）P107"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_560_relative_tube_roughness",
        "name": u"560/△1",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_discriminant",
        "name": u"判别式",
        "symbol": u"",
        "unit": u"",
        "calculate": u"4000 <Re< 560/△1",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_frictional_resistance",
        "name": u"摩擦阻力",
        "symbol": u"△Pm3",
        "unit": u"Pa",
        "calculate": u"△Pd*L3",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_frictional_resistance_coefficient",
        "name": u"摩擦阻力系数",
        "symbol": u"λ",
        "unit": u"",
        "calculate": u"图7.2.2",
        "remark": u"（2）P108"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_unit_length_frictional_resistance",
        "name": u"单位长度摩擦阻力",
        "symbol": u"△Pd",
        "unit": u"Pa/m",
        "calculate": u"λ*Hd/De",
        "remark": u"（2）P106"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_ducting_length",
        "name": u"风管长度",
        "symbol": u"L3",
        "unit": u"m",
        "calculate": u"布置图",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_local_resistance",
        "name": u"局部阻力",
        "symbol": u"△Pj3",
        "unit": u"",
        "calculate": u"ζ*Hd",
        "remark": u"（2）P109"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_local_resistance_coefficient",
        "name": u"局部阻力系数",
        "symbol": u"ζ",
        "unit": u"",
        "calculate": u"ζ1+ζ2+ζ3+ζ4",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_shrink_pipe",
        "name": u"1个空预器出口收缩管",
        "symbol": u"ζ1",
        "unit": u"",
        "calculate": u"假定",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_90_sharp_turn_elbow",
        "name": u"6只90度等截面急转弯头",
        "symbol": u"ζ2",
        "unit": u"",
        "calculate": u"ζ2=n*ζo",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_90_sharp_turn_elbow_count",
        "name": u"弯头数量",
        "symbol": u"n",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_90_sharp_turn_elbow_resistance",
        "name": u"弯头局部阻力系统(焊接圆管）",
        "symbol": u"ζo",
        "unit": u"",
        "calculate": u"",
        "remark": u"（12）P？"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_air_intake_gate",
        "name": u"1个热一次风进风室风门",
        "symbol": u"ζ3",
        "unit": u"",
        "calculate": u"假定θ=10°",
        "remark": u"（2）P130"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_combustor_gate",
        "name": u"1个热一次风进燃烧室风门",
        "symbol": u"ζ4",
        "unit": u"",
        "calculate": u"假定θ=10°",
        "remark": u"（2）P130"
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_to_boiler_total_pressure",
        "name": u"空预器出口至锅炉风室总阻力",
        "symbol": u"△Pz3",
        "unit": u"",
        "calculate": u"△Pm3+△Pj3",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},

    {
        "module_name": "GPG_WindResistance",
        "name_eng": "windhole_total_pressure",
        "name": u"风道总阻力",
        "symbol": u"△Pz",
        "unit": u"",
        "calculate": u"△Pz1+△Pz2+△Pz3",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""}
]

# 煤气发电 烟阻力
GPGSmokeResistance_data = [{
    "module_name": "GPG_SmokeResistance",
    "name_eng": "recommend_velocity",
    "name": u"推荐流速",
    "symbol": u"",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u"（8)P6"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_outlet_calculated_temperature",
    "name":
    u"计算温度(空预器出口)",
    "symbol":
    u"T'y",
    "unit":
    u"℃",
    "calculate":
    u"锅炉计算",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_outlet_smoke_amount",
    "name": u"烟量(空预器出口)",
    "symbol": u"Vyk",
    "unit": u"m³/h",
    "calculate": u"燃烧计算",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_density",
    "name": u"密度",
    "symbol": u"ρyk",
    "unit": u"kg/m³",
    "calculate": u"平均值",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_flow_velocity",
    "name": u"流速",
    "symbol": u"W",
    "unit": u"m/s",
    "calculate": u"取定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_dynamic_pressure_head",
    "name": u"动压头",
    "symbol": u"Hd",
    "unit": u"Pa",
    "calculate": u"W2*ρ/2",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_smoke_tube_area",
    "name": u"烟管截面积",
    "symbol": u"F",
    "unit": u"m2",
    "calculate": u"V/W/3600",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_length",
    "name": u"长",
    "symbol": u"A",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_width",
    "name": u"宽",
    "symbol": u"B",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_duct_perimeter",
    "name": u"风管周长",
    "symbol": u"Lc",
    "unit": u"m",
    "calculate": u"2*(A+B)",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_tube_equivalent_diameter",
    "name":
    u"管道当量直径",
    "symbol":
    u"De",
    "unit":
    u"m",
    "calculate":
    u"4*F/Lc",
    "remark":
    u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_gas_kinetic_viscosity",
    "name": u"气体运动粘度",
    "symbol": u"υ",
    "unit": u"m2/s",
    "calculate": u"",
    "remark": u"（2）P288"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_reynolds_number",
    "name": u"雷诺数",
    "symbol": u"Re",
    "unit": u"",
    "calculate": u"",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_absolute_tube_roughness",
    "name":
    u"管道内壁绝对粗糙度",
    "symbol":
    u"△",
    "unit":
    u"m",
    "calculate":
    u"",
    "remark":
    u"（2）P109"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_relative_tube_roughness",
    "name":
    u"管道内壁相对粗糙度",
    "symbol":
    u"△1",
    "unit":
    u"m",
    "calculate":
    u"△/De",
    "remark":
    u"（2）P107"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_560_relative_tube_roughness",
    "name":
    u"560/△1",
    "symbol":
    u"",
    "unit":
    u"",
    "calculate":
    u"",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_discriminant",
    "name": u"判别式",
    "symbol": u"",
    "unit": u"",
    "calculate": u"4000 <Re< 560/△1",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_frictional_resistance",
    "name": u"摩擦阻力",
    "symbol": u"△Pm1",
    "unit": u"Pa",
    "calculate": u"△Pd*L1",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_frictional_resistance_coefficient",
    "name":
    u"摩擦阻力系数",
    "symbol":
    u"λ",
    "unit":
    u"",
    "calculate":
    u"图7.2.2",
    "remark":
    u"（2）P108"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_unit_length_frictional_resistance",
    "name":
    u"单位长度摩擦阻力",
    "symbol":
    u"△Pd",
    "unit":
    u"Pa/m",
    "calculate":
    u"λ*Hd/De",
    "remark":
    u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_ducting_length",
    "name": u"风管长度",
    "symbol": u"L1",
    "unit": u"m",
    "calculate": u"布置图",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_local_resistance",
    "name": u"局部阻力",
    "symbol": u"△Pj1",
    "unit": u"",
    "calculate": u"ζ*Hd",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng":"air_preheater_local_resistance_coefficient",
    "name": u"局部阻力系数",
    "symbol": u"ζ",
    "unit": u"",
    "calculate": u"ζ1+ζ2+ζ3",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_90_outlet_sharp_turn_elbow",
    "name": u"1个90度空预器出口变径急转弯头",
    "symbol": u"ζ1",
    "unit": u"",
    "calculate": u"ζ1=ζu1",
    "remark": u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_powder_local_resistance_coefficient",
    "name": u"含粉气体局部阻力系数",
    "symbol": u"ζu1",
    "unit": u"",
    "calculate": u"ζo（1+Ku）",
    "remark": u"（2）P110"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_air_elbow_local_resistance_coefficient",
    "name": u"纯空气弯头局部阻力系数",
    "symbol": u"ζo",
    "unit": u"",
    "calculate": u"假定",
    "remark":  u"（12）P？"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_powder_concentration_corrected_coefficient",
    "name":
    u"含粉浓度修正系数",
    "symbol":
    u"Ku",
    "unit":
    u"",
    "calculate":
    u"表7.3.2-2",
    "remark":
    u"（2）P113"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_90_section_slow_turn_elbow",
    "name":
    u"1个90度等截面缓转弯头",
    "symbol":
    u"ζ2",
    "unit":
    u"",
    "calculate":
    u"",
    "remark":
    u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_slow_powder_local_resistance_coefficient",
    "name":
    u"含粉气体局部阻力系数",
    "symbol":
    u"ζu2",
    "unit":
    u"",
    "calculate":
    u"ζo（1+Ku）",
    "remark":
    u"（2）P110"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_slow_air_local_resistance_coefficient",
    "name":
    u"纯空气弯头局部阻力系数",
    "symbol":
    u"ζo",
    "unit":
    u"",
    "calculate":
    u"假定",
    "remark":
    u"（12）P？"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_slow_powder_concentration_corrected_coefficient",
    "name":
    u"含粉浓度修正系数",
    "symbol":
    u"Ku",
    "unit":
    u"",
    "calculate":
    u"表7.3.2-2",
    "remark":
    u"（2）P113"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_reducer_tube",
    "name": u"1个渐缩管",
    "symbol": u"ζ3",
    "unit": u"",
    "calculate": u"",
    "remark": u"（2）P137"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "air_preheater_to_deduster_total_resistance",
    "name":
    u"空预器出口至除尘器入口总阻力",
    "symbol":
    u"△Pz1",
    "unit":
    u"",
    "calculate":
    u"△Pm1+△Pj1",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_outlet_calculated_temperature",
    "name":
    u"计算温度",
    "symbol":
    u"Tcc",
    "unit":
    u"℃",
    "calculate":
    u"烟风量计算表",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_outlet_smoke_amount",
    "name": u"烟量(除尘器出口)",
    "symbol": u"Vycc",
    "unit": u"m³/h",
    "calculate": u"烟风量计算表",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_density",
    "name": u"密度",
    "symbol": u"ρycc",
    "unit": u"kg/m³",
    "calculate": u"烟风量计算表",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_flow_velocity",
    "name": u"流速",
    "symbol": u"W",
    "unit": u"m/s",
    "calculate": u"取定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_dynamic_pressure_head",
    "name": u"动压头",
    "symbol": u"Hd",
    "unit": u"Pa",
    "calculate": u"W2*ρ/2",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_smoke_tube_area",
    "name": u"烟管截面积",
    "symbol": u"F",
    "unit": u"m2",
    "calculate": u"V/W/3600",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_length",
    "name": u"长",
    "symbol": u"A",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_width",
    "name": u"宽",
    "symbol": u"B",
    "unit": u"m",
    "calculate": u"F/A",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_duct_perimeter",
    "name": u"风管周长",
    "symbol": u"Lc",
    "unit": u"m",
    "calculate": u"2*(A+B)",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_tube_equivalent_diameter",
    "name": u"管道当量直径",
    "symbol": u"De",
    "unit": u"m",
    "calculate": u"4*F/Lc",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_gas_kinetic_viscosity",
    "name": u"气体运动粘度",
    "symbol": u"υ",
    "unit": u"m2/s",
    "calculate": u"",
    "remark": u"（2）P288"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_reynolds_number",
    "name": u"雷诺数",
    "symbol": u"Re",
    "unit": u"",
    "calculate": u"W*De/υ",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_absolute_tube_roughness",
    "name": u"管道内壁绝对粗糙度",
    "symbol": u"△",
    "unit": u"m",
    "calculate": u"",
    "remark": u"（2）P109"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_relative_tube_roughness",
    "name": u"管道内壁相对粗糙度",
    "symbol": u"△1",
    "unit": u"m",
    "calculate": u"△/De",
    "remark": u"（2）P107"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_560_relative_tube_roughness",
    "name": u"560/△1",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_discriminant",
    "name": u"判别式",
    "symbol": u"",
    "unit": u"",
    "calculate": u"4000 <Re< 560/△1",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_frictional_resistance",
    "name": u"摩擦阻力",
    "symbol": u"△Pm2",
    "unit": u"Pa",
    "calculate": u"△Pd*L3",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_frictional_resistance_coefficient",
    "name":
    u"摩擦阻力系数",
    "symbol":
    u"λ",
    "unit":
    u"",
    "calculate":
    u"图7.2.2",
    "remark":
    u"（2）P108"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_unit_length_frictional_resistance",
    "name":
    u"单位长度摩擦阻力",
    "symbol":
    u"△Pd",
    "unit":
    u"Pa/m",
    "calculate":
    u"λ*Hd/De",
    "remark":
    u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_ducting_length",
    "name": u"风管长度",
    "symbol": u"L2",
    "unit": u"m",
    "calculate": u"布置图",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_local_resistance",
    "name": u"局部阻力",
    "symbol": u"△Pj2",
    "unit": u"",
    "calculate": u"ζ*Hd",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_local_resistance_coefficient",
    "name":
    u"局部阻力系数",
    "symbol":
    u"ζ",
    "unit":
    u"",
    "calculate":
    u"ζ1+ζ2+ζ3",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_90_outlet_slow_turn_elbow",
    "name": u"1个90度除尘器出口缓转弯头",
    "symbol": u"ζ1",
    "unit": u"",
    "calculate": u"ζ1=ζu1",
    "remark": u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_slow_powder_local_resistance_coefficient",
    "name":
    u"含粉气体局部阻力系数",
    "symbol":
    u"ζu1",
    "unit":
    u"",
    "calculate":
    u"ζo（1+Ku）",
    "remark":
    u"（2）P110"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_slow_air_local_resistance_coefficient",
    "name":
    u"纯空气弯头局部阻力系数",
    "symbol":
    u"ζo",
    "unit":
    u"",
    "calculate":
    u"假定",
    "remark":
    u"（12）？"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_slow_powder_concentration_corrected_coefficient",
    "name":
    u"含粉浓度修正系数",
    "symbol":
    u"Ku",
    "unit":
    u"",
    "calculate":
    u"表7.3.2-2",
    "remark":
    u"（2）P113"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_90_section_slow_turn_elbow",
    "name": u"1个90度等截面缓转弯头",
    "symbol": u"ζ2",
    "unit": u"",
    "calculate": u"ζ2=ζu2",
    "remark": u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_section_slow_powder_local_resistance_coefficient",
    "name":
    u"含粉气体局部阻力系数",
    "symbol":
    u"ζu2",
    "unit":
    u"",
    "calculate":
    u"ζo（1+Ku）",
    "remark":
    u"（2）P110"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_section_slow_air_local_resistance_coefficient",
    "name":
    u"纯空气局部阻力系数",
    "symbol":
    u"ζo",
    "unit":
    u"",
    "calculate":
    u"Kθ*Kc*ζ△0",
    "remark":
    u"（2）P110"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_corrected_turning_angle_coefficient",
    "name":
    u"转弯角度修正系数",
    "symbol":
    u"Kθ",
    "unit":
    u"",
    "calculate":
    u"图7.3.2-1",
    "remark":
    u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_section_corrected_height_width_ratio_coefficient",
    "name":
    u"截面高宽比修正系数",
    "symbol":
    u"Kc",
    "unit":
    u"",
    "calculate":
    u"图7.3.2-2",
    "remark":
    u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_section_original_resistance_coefficient_with_roughness",
    "name":
    u"包含管壁粗糙度影响的纯空气下的转弯原始阻力系数",
    "symbol":
    u"ζ△0",
    "unit":
    u"",
    "calculate":
    u"图7.3.2-5",
    "remark":
    u"（2）P113"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_section_slow_powder_corrected_coefficient",
    "name":
    u"含粉浓度修正系数",
    "symbol":
    u"Ku",
    "unit":
    u"",
    "calculate":
    u"图7.3.2-2",
    "remark":
    u"（2）P113"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_inlet_bellows",
    "name": u"1个进口风箱",
    "symbol": u"ζ3",
    "unit": u"",
    "calculate": u"",
    "remark": u"（2）P144"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "deduster_to_induced_draft_total_resistance",
    "name":
    u"除尘器出口至引风机入口总阻力",
    "symbol":
    u"△Pz2",
    "unit":
    u"",
    "calculate":
    u"△Pm2+△Pj2",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_inlet_calculated_temperature",
    "name":
    u"计算温度",
    "symbol":
    u"Txf",
    "unit":
    u"℃",
    "calculate":
    u"烟风量计算表",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_inlet_smoke_amount",
    "name": u"烟量(引风机进口)",
    "symbol": u"Vyxf",
    "unit": u"m3/h",
    "calculate": u"烟风量计算表",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_density",
    "name": u"密度",
    "symbol": u"ρyxf",
    "unit": u"kg/m3",
    "calculate": u"烟风量计算表",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_flow_velocity",
    "name": u"流速",
    "symbol": u"W",
    "unit": u"m/s",
    "calculate": u"取定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_dynamic_pressure_head",
    "name": u"动压头",
    "symbol": u"Hd",
    "unit": u"Pa",
    "calculate": u"W2*ρ/2",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_smoke_tube_area",
    "name": u"烟管截面积",
    "symbol": u"F",
    "unit": u"m2",
    "calculate": u"V/W/3600",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_width",
    "name": u"宽",
    "symbol": u"A",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_height",
    "name": u"高",
    "symbol": u"B",
    "unit": u"m",
    "calculate": u"F/A",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_duct_perimeter",
    "name": u"风管周长",
    "symbol": u"Lc",
    "unit": u"m",
    "calculate": u"2*(A+B)",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_tube_equivalent_diameter",
    "name":
    u"管道当量直径",
    "symbol":
    u"De",
    "unit":
    u"m",
    "calculate":
    u"4*F/Lc",
    "remark":
    u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_gas_kinetic_viscosity",
    "name": u"气体运动粘度",
    "symbol": u"υ",
    "unit": u"m2/s",
    "calculate": u"",
    "remark": u"（2）P288"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_reynolds_number",
    "name": u"雷诺数",
    "symbol": u"Re",
    "unit": u"",
    "calculate": u"W*De/υ",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_absolute_tube_roughness",
    "name":
    u"管道内壁绝对粗糙度",
    "symbol":
    u"△",
    "unit":
    u"m",
    "calculate":
    u"",
    "remark":
    u"（2）P109"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_relative_tube_roughness",
    "name":
    u"管道内壁相对粗糙度",
    "symbol":
    u"△1",
    "unit":
    u"m",
    "calculate":
    u"△/De",
    "remark":
    u"（2）P107"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_560_relative_tube_roughness",
    "name":
    u"560/△1",
    "symbol":
    u"",
    "unit":
    u"",
    "calculate":
    u"",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_discriminant",
    "name": u"判别式",
    "symbol": u"",
    "unit": u"",
    "calculate": u"4000 <Re< 560/△1",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_frictional_resistance",
    "name": u"摩擦阻力",
    "symbol": u"△Pm3",
    "unit": u"Pa",
    "calculate": u"△Pd*L3",
    "remark": u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_frictional_resistance_coefficient",
    "name":
    u"摩擦阻力系数",
    "symbol":
    u"λ",
    "unit":
    u"",
    "calculate":
    u"图7.2.2",
    "remark":
    u"（2）P108"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_unit_length_frictional_resistance",
    "name":
    u"单位长度摩擦阻力",
    "symbol":
    u"△Pd",
    "unit":
    u"Pa/m",
    "calculate":
    u"λ*Hd/De",
    "remark":
    u"（2）P106"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_ducting_length",
    "name": u"风管长度",
    "symbol": u"L3",
    "unit": u"m",
    "calculate": u"布置图",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_local_resistance",
    "name": u"局部阻力",
    "symbol": u"△Pj3",
    "unit": u"Pa",
    "calculate": u"ζ*Hd",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_local_resistance_coefficient",
    "name":
    u"局部阻力系数",
    "symbol":
    u"ζ",
    "unit":
    u"",
    "calculate":
    u"ζ1+ζ2+ζ3+ζ4",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_outlet_plate_gate",
    "name": u"1个出口插板门",
    "symbol": u"ζ1",
    "unit": u"",
    "calculate": u"图7.3.10-1",
    "remark": u"（2）P130"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_outlet_diffuser_tube",
    "name": u"1个出口扩散管",
    "symbol": u"ζ2",
    "unit": u"",
    "calculate": u"",
    "remark": u"（2）P136"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_45_90_slow_turn_elbow",
    "name": u"1个45度缓转弯头（钢烟道）/1个90度缓转弯头（砖烟道）",
    "symbol": u"ζ3",
    "unit": u"",
    "calculate": u"ζ3=ζu",
    "remark": u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_powder_local_resistance_coefficient",
    "name":
    u"含粉气体局部阻力系数",
    "symbol":
    u"ζu",
    "unit":
    u"",
    "calculate":
    u"ζo（1+Ku）",
    "remark":
    u"（2）P110"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_air_local_resistance_coefficient",
    "name":
    u"纯空气局部阻力系数",
    "symbol":
    u"ζo",
    "unit":
    u"",
    "calculate":
    u"Kθ*Kc*ζ△0",
    "remark":
    u"（2）P110"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_corrected_turning_angle_coefficient",
    "name":
    u"转弯角度修正系数",
    "symbol":
    u"Kθ",
    "unit":
    u"",
    "calculate":
    u"图7.3.2-1",
    "remark":
    u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_corrected_height_width_ratio_coefficient",
    "name":
    u"截面高宽比修正系数",
    "symbol":
    u"Kc",
    "unit":
    u"",
    "calculate":
    u"图7.3.2-2",
    "remark":
    u"（2）P111"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_original_resistance_coefficient_with_roughness",
    "name":
    u"包含管壁粗糙度影响的纯空气下的转弯原始阻力系数",
    "symbol":
    u"ζ△0",
    "unit":
    u"",
    "calculate":
    u"图7.3.2-5",
    "remark":
    u"（2）P113"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_powder_concentration_corrected_coefficient",
    "name":
    u"含粉浓度修正系数",
    "symbol":
    u"Ku",
    "unit":
    u"",
    "calculate":
    u"表7.3.2-2",
    "remark":
    u"（2）P113"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "brick_chimney_inlet",
    "name": u"砖烟道烟囱入口",
    "symbol": u"ζ4",
    "unit": u"",
    "calculate": u"表7.4.1",
    "remark": u"（2）P147"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name":
    "GPG_SmokeResistance",
    "name_eng":
    "induced_draft_to_chimney_total_resistance",
    "name":
    u"引风机出口至烟囱入口总阻力",
    "symbol":
    u"△Pz3",
    "unit":
    u"Pa",
    "calculate":
    u"△Pm3+△Pj3",
    "remark":
    u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "smoke_chimney_total_resistance",
    "name": u"烟道总阻力",
    "symbol": u"△Pz",
    "unit": u"Pa",
    "calculate": u"△Pz1+△Pz2+△Pz3",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""}
]

# 煤气发电 烟风系统
GPGGasAirSys_data = [{
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_condition_temperature",
        "name": u"工况温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_condition_flux",
        "name": u"工况流量",
        "symbol": u"qv",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_standard_temperature",
        "name": u"标况温度",
        "symbol": u"t0",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_standard_pressure",
        "name": u"标况压力",
        "symbol": u"p0",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_standard_flux",
        "name": u"标况流量",
        "symbol": u"qv0",
        "unit": u"Nm³/h",
        "calculate": u"qv0=qv*(p/p0)*((t0+273)/(t+273))",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_standard_temperature",
        "name": u"标况温度",
        "symbol": u"t0",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_standard_pressure",
        "name": u"标况压力",
        "symbol": u"p0",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_standard_flux",
        "name": u"标况流量",
        "symbol": u"qv0",
        "unit": u"Nm³/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_condition_temperature",
        "name": u"工况温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_condition_flux",
        "name": u"工况流量",
        "symbol": u"qv",
        "unit": u"m³/h",
        "calculate": u"qv=qv0*(p0/p)*((t+273)/(t0+273))",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_air_temperature",
        "name": u"空气温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"设计值"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_wind_resistance",
        "name": u"风阻力",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u"设计值"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p0",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_condition_smoke_flux",
        "name": u"烟风流量（工况）",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"注意锅炉厂是否含有储备系数"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_temperature",
        "name": u"风机温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "20", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_total_pressure",
        "name": u"风机全压",
        "symbol": u"p1",
        "unit": u"pa",
        "calculate": u"p1=p*(101325/p0)*((t+273)/(t1+273))",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_selected_total_pressure",
        "name": u"风机选用全压",
        "symbol": u"p2",
        "unit": u"",
        "calculate": u"",
        "remark": u"1.10~1.15"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_selected_flux",
        "name": u"风机选用流量",
        "symbol": u"q2",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"1.05~1.2"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_pressure_efficiency",
        "name": u"风机全压头效率",
        "symbol": u"η",
        "unit": u"",
        "calculate": u"",
        "remark": u"0.9"
    	, "default_value": "0.9", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_transmission_efficiency",
        "name": u"机械传动效率",
        "symbol": u"η1",
        "unit": u"",
        "calculate": u"",
        "remark": u"直联时1.0，联轴器连接时0.95~0.98，三角皮带传动0.9~0.95，平皮带传动时0.8"
    	, "default_value": "0.98", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_motor_efficiency",
        "name": u"电动机效率",
        "symbol": u"ηd",
        "unit": u"",
        "calculate": u"",
        "remark": u"0.9"
    	, "default_value": "0.9", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_shaft_power",
        "name": u"风机轴功率",
        "symbol": u"P'",
        "unit": u"kw",
        "calculate": u"P'=p2*q2/η",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_motor_safe_margin",
        "name": u"电机安全裕量",
        "symbol": u"K",
        "unit": u"",
        "calculate": u"",
        "remark": u"1.1"
    	, "default_value": "1.1", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_motor_power",
        "name": u"电机功率",
        "symbol": u"P",
        "unit": u"kw",
        "calculate": u"P=K*P'/ηd",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_specification_power",
        "name": u"选用规格-功率",
        "symbol": u"50%定频",
        "unit": u"kw",
        "calculate": u"一个",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_specification_flux",
        "name": u"选用规格-流量",
        "symbol": u"50%定频",
        "unit": u"m³/h",
        "calculate": u"一个",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_smoke_temperature",
        "name": u"烟风温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"设计值"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_total_pressure",
        "name": u"全压",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u"烟道总阻力"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p0",
        "unit": u"pa",
        "calculate": u"",
        "remark": u"根据当地海拔按表选取"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_condition_smoke_flux",
        "name": u"烟风流量（工况）",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"标---工况之间转换"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_temperature",
        "name": u"风机温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"风机铭牌标定温度，一般为165/200℃"
    	, "default_value": "200", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_smoke_density",
        "name": u"烟气密度",
        "symbol": u"ρ0",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"取一般烟气平均密度"
    	, "default_value": "1.34", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_total_pressure",
        "name": u"风机全压",
        "symbol": u"p1",
        "unit": u"pa’",
        "calculate": u"p1=p*(101325/p0)*((t+273)/(t1+273))",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_selected_total_pressure",
        "name": u"风机选用全压",
        "symbol": u"p2",
        "unit": u"",
        "calculate": u"",
        "remark": u"选用系数：1.10~1.15"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_selected_flux",
        "name": u"风机选用流量",
        "symbol": u"q2",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"选用系数：1.05~1.2"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_efficiency",
        "name": u"风机效率",
        "symbol": u"η",
        "unit": u"",
        "calculate": u"",
        "remark": u"全压头时效率，一般风机0.6，高效风机为0.9"
    	, "default_value": "0.9", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_transmission_efficiency",
        "name":  u"机械传动效率",
        "symbol": u"η1",
        "unit": u"",
        "calculate": u"",
        "remark": u"直联时1.0，联轴器连接时0.95~0.98，三角皮带传动0.9~0.95，平皮带传动时0.8"
    	, "default_value": "0.98", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_motor_efficiency",
        "name": u"电机效率",
        "symbol": u"ηd",
        "unit": u"",
        "calculate": u"",
        "remark": u"电动机效率0.9"
    	, "default_value": "0.9", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_shaft_power",
        "name": u"风机轴功率",
        "symbol": u"P'",
        "unit": u"kw",
        "calculate": u"P'=p2*q2/η",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_motor_safe_margin",
        "name": u"电机安全裕量",
        "symbol": u"K",
        "unit": u"",
        "calculate": u"",
        "remark": u"1.1"
    	, "default_value": "1.1", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_motor_power",
        "name": u"电机功率",
        "symbol": u"P",
        "unit": u"kw",
        "calculate": u"P=K*P'/ηd",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_specification_power",
        "name": u"选用规格-功率",
        "symbol": u"50%定频",
        "unit": u"kw",
        "calculate": u"一个",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_specification_flux",
        "name": u"选用规格-流量",
        "symbol": u"50%定频",
        "unit": u"m³/h",
        "calculate": u"一个",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"煤气管道15-20"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_calculated_diameter",
        "name": u"计算管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_selected_diameter",
        "name": u"选取直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_selected_thickness",
        "name": u"选取壁厚",
        "symbol": u"t",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"冷风道流速10-12"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_calculated_diameter",
        "name": u"计算当量管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_length",
        "name": u"长",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_specification",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"热风道流速15-25"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_calculated_diameter",
        "name": u"计算当量管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_length",
        "name": u"长",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_specification",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"烟道流速10-15"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_calculated_diameter",
        "name": u"计算当量管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_length",
        "name": u"长",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_specification",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"烟道流速10-15"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name":
        "GPG_GasAirSystem",
        "name_eng":
        "branch_smoke_tube_calculated_cross_sectional_area",
        "name":
        u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_calculated_diameter",
        "name": u"计算当量管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_length",
        "name": u"长",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_specification",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"热风道流速15-25"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_calculated_diameter",
        "name": u"计算管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_selected_diameter",
        "name": u"选取直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_selected_thickness",
        "name": u"选取壁厚",
        "symbol": u"t",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"热风道流速15-25"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_calculated_diameter",
        "name": u"计算管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_selected_diameter",
        "name": u"选取直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_selected_thickness",
        "name": u"选取壁厚",
        "symbol": u"t",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_height",
        "name": u"烟囱高度",
        "symbol": u"H",
        "unit": u"m",
        "calculate": u"假定30、45、60、80、100、120、150、180",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "standard_air_density",
        "name": u"标态下空气密度",
        "symbol": u"ρ0",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"平均值"
    	, "default_value": "1.293", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "standard_average_smoke_density",
        "name": u"标态下平均烟气密度",
        "symbol": u"ρ1",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"平均值"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "standard_calculated_smoke_density",
        "name": u"标态下计算烟气密度",
        "symbol": u"ρ2",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"计算值"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "outdoor_air_temperature",
        "name": u"室外空气温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_inlet_temperature",
        "name": u"烟囱进口处烟温",
        "symbol": u"t0",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"锅炉排烟温度"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_temperature_drop_per_meter",
        "name": u"烟囱每米高度的温度降",
        "symbol": u"t'",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"砖砌温降0.1℃/m；钢板0.5℃/m"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_average_temperature",
        "name": u"烟囱内平均温度",
        "symbol": u"t2",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_draft",
        "name": u"烟囱抽力",
        "symbol": u"S",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "smoke_amount",
        "name": u"烟气量",
        "symbol": u"q",
        "unit": u"Nm³/h",
        "calculate": u"",
        "remark": u"燃烧计算"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_temperature",
        "name": u"烟囱出口温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"抽力计算"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_flow",
        "name": u"烟囱出口流速",
        "symbol": u"Wo",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"根据温度和烟囱高度选取12-20，低负荷时2.5-3"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_inner_diameter",
        "name": u"烟囱出口内径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_selected_inner_diameter",
        "name": u"选取烟囱出口内径",
        "symbol": u"d'",
        "unit": u"mm",
        "calculate": u"",
        "remark": u"选取"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_experience_base_diameter",
        "name": u"经验烟囱基础内径",
        "symbol": u"d'’",
        "unit": u"mm",
        "calculate": u"",
        "remark": u"坡度小于2%"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "low_load_smoke_amount",
        "name": u"低负荷下烟气量",
        "symbol": u"q1",
        "unit": u"Nm³/h",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "low_load_smoke_temperature",
        "name": u"低负荷下排烟温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "low_load_flow_30_percent",
        "name": u"30%低负荷校核流速",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"不低于2.5"
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_resistance_coefficient",
        "name": u"烟囱阻力系数",
        "symbol": u"r",
        "unit": u"",
        "calculate": u"",
        "remark": u"一般0.04"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_average_velocity",
        "name": u"烟囱内平均流速",
        "symbol": u"Wo",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_average_diameter",
        "name": u"烟囱平均直径",
        "symbol": u"d'’",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_friction_resistance",
        "name": u"烟囱摩擦阻力",
        "symbol": u"△p1",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_resistance_coefficient",
        "name": u"烟囱出口阻力系数",
        "symbol": u"§",
        "unit": u"pa",
        "calculate": u"",
        "remark": u"一般取1"
    	, "default_value": "", 
 	 "disable": ""},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_resistance",
        "name": u"烟囱出口阻力",
        "symbol": u"△p2",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"},
 {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_total_resistance",
        "name": u"烟囱总阻力",
        "symbol": u"△p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    	, "default_value": "", 
 	 "disable": "T"}
]

# 煤气发电 原则性热力系统锅炉部分
GPGBoilerOfPTS_data = [{
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "surplus_gas_bfg",
    "name": u"煤气流量_BFG",
    "symbol": u"Vg",
    "unit": u"Nm³/h",
    "calculate": u"由余热资源确定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "surplus_gas_ldg",
    "name": u"煤气流量_LDG",
    "symbol": u"Vg",
    "unit": u"Nm³/h",
    "calculate": u"由余热资源确定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "surplus_gas_cog",
    "name": u"煤气流量_COG",
    "symbol": u"Vg",
    "unit": u"Nm³/h",
    "calculate": u"由余热资源确定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "bfg_gas_calorific_value",
    "name": u"BFG 煤气热值",
    "symbol": u"Qar.net.p",
    "unit": u"kJ/Nm³",
    "calculate": u"给定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "ldg_gas_calorific_value",
    "name": u"LDG 煤气热值",
    "symbol": u"Qar.net.p",
    "unit": u"kJ/Nm³",
    "calculate": u"给定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "cog_gas_calorific_value",
    "name": u"COG 煤气热值",
    "symbol": u"Qar.net.p",
    "unit": u"kJ/Nm³",
    "calculate": u"给定",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "boiler_efficiency",
    "name": u"锅炉热效率",
    "symbol": u"η",
    "unit": u"%",
    "calculate": u"设计参数",
    "remark": u""
	, "default_value": "87", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "superheated_steam_outlet_pressure",
    "name": u"过热蒸汽出口压力",
    "symbol": u"P1",
    "unit": u"Mpa",
    "calculate": u"设计参数，绝压",
    "remark": u""
	, "default_value": "9.8", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "superheated_steam_temperature",
    "name": u"过热蒸汽温度",
    "symbol": u"two",
    "unit": u"℃",
    "calculate": u"设计参数",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "superheated_steam_enthalpy",
    "name": u"过热蒸汽焓值",
    "symbol": u"Izo",
    "unit": u"kJ/kg",
    "calculate": u"查表",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "excess_air_coefficient",
    "name": u"过量空气系数",
    "symbol": u"α",
    "unit": u"",
    "calculate": u"",
    "remark": u"1.1~1.2"
	, "default_value": "1.15", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "air_temperature",
    "name": u"空气温度",
    "symbol": u"t",
    "unit": u"℃",
    "calculate": u"设计参数",
    "remark": u"20"
	, "default_value": "20", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "air_enthalpy",
    "name": u"空气焓值",
    "symbol": u"hkq",
    "unit": u"kj/Nm³",
    "calculate": u"查表",
    "remark": u""
	, "default_value": "25.97", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "air_need_for_combustion",
    "name": u"燃烧所需空气量",
    "symbol": u"Vn",
    "unit": u"Nm³/h",
    "calculate": u"0.209*Qar.net.p*Vg*α",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "boiler_feed_water_temperature",
    "name": u"锅炉给水温度",
    "symbol": u"tgs",
    "unit": u"℃",
    "calculate": u"设计参数",
    "remark": u"有高加为150℃或215℃，没高加为104℃"
	, "default_value": "104", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "feedwater_enthalpy",
    "name": u"给水焓值",
    "symbol": u"hgs",
    "unit": u"kJ/kg",
    "calculate": u"查表",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "rate_of_blowdown",
    "name": u"排污率",
    "symbol": u"φ",
    "unit": u"%",
    "calculate": u"设定",
    "remark": u"2%"
	, "default_value": "2", 
 	 "disable": ""},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "saturation_water_temperature",
    "name": u"饱和水温度",
    "symbol": u"tbh",
    "unit": u"℃",
    "calculate": u"查水蒸汽表",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "saturation_water_enthalpy",
    "name": u"饱和水焓值",
    "symbol": u"hbh",
    "unit": u"kj/Nm³",
    "calculate": u"查水蒸汽表",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"},
 {
    "module_name": "GPG_BoilerOfPTS",
    "name_eng": "steam_output",
    "name": u"产汽量",
    "symbol": u"G1",
    "unit": u"t/h",
    "calculate": u"(Vn*hkq+Vg*Qar.net.p）*η/1000/((Izo-hgs)+φ(hbh-hgs))",
    "remark": u""
	, "default_value": "", 
 	 "disable": "T"}
]

# 煤气发电 原则性热力系统汽轮机部分
GPGTurbineOfPTS_data=[
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_turbine_efficiency",
        "name": "汽轮机内效率",
        "symbol": "ηTi",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.78",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_mechanical_efficiency",
        "name": "机械效率",
        "symbol": "ηm",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.95",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_generator_efficiency",
        "name": "发电机效率",
        "symbol": "ηg",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.973",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "Mpa",
        "calculate": "设计参数",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "设计参数",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_flow",
        "name": "进汽量",
        "symbol": "G1",
        "unit": "t/h",
        "calculate": "热源产生主蒸汽总流量",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_entropy",
        "name": "熵",
        "symbol": "",
        "unit": "kJ/(kg·℃)",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_enthalpy",
        "name": "焓",
        "symbol": "Izo",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_point_pressure",
        "name": "压力",
        "symbol": "P2'",
        "unit": "Mpa",
        "calculate": "设计参数",
        "remark": "",
        "default_value": "0.2",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_point_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "120.21",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_point_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_point_enthalpy",
        "name": "焓",
        "symbol": "Izob",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
    "module_name": "GPG_TurbineOfPTS",
    "name_eng": "e_steam_plus_enthalpy",
    "name": "补汽焓",
    "symbol": "Izob",
    "unit": "kJ/kg",
    "calculate": "",
    "remark": "",
    "default_value": "",
    "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_point_flow",
        "name": "抽汽量",
        "symbol": "G2",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "0",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_after_steam",
        "name": "蒸汽量",
        "symbol": "G",
        "unit": "t/h",
        "calculate": "G1+G2",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_after_pressure",
        "name": "压力",
        "symbol": "P2'",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_after_enthalpy",
        "name": "焓",
        "symbol": "Ih",
        "unit": "kJ/kg",
        "calculate": "（（G1-G3）*Izob+G2*Izo'）/G",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_exhaust_after_entropy",
        "name": "熵",
        "symbol": "Sh",
        "unit": "kJ/(kg·℃)",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_exhaust_pressure",
        "name": "压力",
        "symbol": "P3",
        "unit": "Mpa",
        "calculate": "湿冷：0.005～0.007；空冷0.015",
        "remark": "",
        "default_value": "0.009",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_exhaust_enthalpy",
        "name": "焓",
        "symbol": "Ipo",
        "unit": "kJ/kg",
        "calculate": "汽轮机绝热等熵做功排汽焓值，查表",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },

    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_backpressure_pressure",
        "name": "压力",
        "symbol": "P3",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_backpressure_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_backpressure_enthalpy",
        "name": "焓",
        "symbol": "Ipo",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_backpressure_flow",
        "name": "流量",
        "symbol": "G3",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_gross_generation",
        "name": "总发电量",
        "symbol": "P",
        "unit": "kw",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_hot_data",
        "name": "回热抽汽经验数据",
        "symbol": "",
        "unit": "--",
        "calculate": "经验值：有高加0.85；无高加0.9；无低价0.95",
        "remark": "",
        "default_value": "0.85",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_extraction",
        "name": "去除抽汽后",
        "symbol": "P",
        "unit": "MW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_extraction_select",
        "name": "选定",
        "symbol": "P",
        "unit": "MW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_steam_water_loss",
        "name": "全厂汽水损失",
        "symbol": "",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.03",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "e_throttle_flow",
        "name": "进汽量",
        "symbol": "",
        "unit": "t/h",
        "calculate": "选定",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "h_assume",
        "name": "假设",
        "symbol": "",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "h_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "--",
        "calculate": "",
        "remark": "高压设5-6回热，给水温度210-230；中温中压4-5及回热，给水温度150-170；1.3MPa低压2级回热，给水温度104；2.4MPa低压3-4级回热，给水温度150；根据情况选择加热器形式：汇集式或者疏水放流式加热器，汇集式带疏水泵将疏水打至给水；假定换热效率0.98。",
        "default_value": "50",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "h_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "h_enthalpy",
        "name": "焓值",
        "symbol": "",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "h_amount",
        "name": "量",
        "symbol": "",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },


    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_water_temperature",
        "name": "给水出水温度",
        "symbol": "tw2",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_water_enthalpy",
        "name": "给水出口焓",
        "symbol": "hw2",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_top_difference",
        "name": "上端差",
        "symbol": "φ",
        "unit": "℃",
        "calculate": "又称给水端差，是指加热器进口蒸汽压力下的饱和水温度与出口给水温度之差",
        "remark": "",
        "default_value": "2.8",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_saturated_water_temperature",
        "name": "饱和水温度--加热器疏水温度",
        "symbol": "te‘",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_saturated_water_enthalpy",
        "name": "饱和水焓",
        "symbol": "he’",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_work_pressure",
        "name": "工作压力",
        "symbol": "pe‘",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_pressure_loss",
        "name": "抽汽管压损",
        "symbol": "ΔPe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "0.08",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_extraction_pressure",
        "name": "抽汽压力",
        "symbol": "Pe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_extraction_enthalpy",
        "name": "抽汽焓",
        "symbol": "he",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh1_extraction_amount",
        "name": "抽汽量",
        "symbol": "Δde‘",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_water_temperature",
        "name": "给水出水温度",
        "symbol": "tw2",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_water_enthalpy",
        "name": "给水出口焓",
        "symbol": "hw2",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_top_difference",
        "name": "上端差",
        "symbol": "φ",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "2.8",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_saturated_water_temperature",
        "name": "饱和水温度--加热器疏水温度",
        "symbol": "te‘",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_saturated_water_enthalpy",
        "name": "饱和水焓",
        "symbol": "he’",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_work_pressure",
        "name": "工作压力",
        "symbol": "pe‘",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_pressure_loss",
        "name": "抽汽管压损",
        "symbol": "ΔPe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "0.08",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_extraction_pressure",
        "name": "抽汽压力",
        "symbol": "Pe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_extraction_enthalpy",
        "name": "抽汽焓",
        "symbol": "he",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh2_extraction_amount",
        "name": "抽汽量",
        "symbol": "Δde‘",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_water_temperature",
        "name": "给水出水温度",
        "symbol": "tw2",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_water_enthalpy",
        "name": "给水出口焓",
        "symbol": "hw2",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_top_difference",
        "name": "上端差",
        "symbol": "φ",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "2.8",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_saturated_water_temperature",
        "name": "饱和水温度--加热器疏水温度",
        "symbol": "te‘",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_saturated_water_enthalpy",
        "name": "饱和水焓",
        "symbol": "he’",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_work_pressure",
        "name": "工作压力",
        "symbol": "pe‘",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_pressure_loss",
        "name": "抽汽管压损",
        "symbol": "ΔPe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "0.08",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_extraction_pressure",
        "name": "抽汽压力",
        "symbol": "Pe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_extraction_enthalpy",
        "name": "抽汽焓",
        "symbol": "he",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "hh3_extraction_amount",
        "name": "抽汽量",
        "symbol": "Δde‘",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_water_temperature",
        "name": "给水出水温度",
        "symbol": "tw2",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_water_enthalpy",
        "name": "给水出口焓",
        "symbol": "hw2",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_top_difference",
        "name": "上端差",
        "symbol": "φ",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "2.8",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_saturated_water_temperature",
        "name": "饱和水温度--加热器疏水温度",
        "symbol": "te‘",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_saturated_water_enthalpy",
        "name": "饱和水焓",
        "symbol": "he’",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_work_pressure",
        "name": "工作压力",
        "symbol": "pe‘",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_pressure_loss",
        "name": "抽汽管压损",
        "symbol": "ΔPe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "0.08",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_extraction_pressure",
        "name": "抽汽压力",
        "symbol": "Pe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_extraction_enthalpy",
        "name": "抽汽焓",
        "symbol": "he",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh1_extraction_amount",
        "name": "抽汽量",
        "symbol": "Δde‘",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_water_temperature",
        "name": "给水出水温度",
        "symbol": "tw2",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_water_enthalpy",
        "name": "给水出口焓",
        "symbol": "hw2",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_top_difference",
        "name": "上端差",
        "symbol": "φ",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "2.8",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_saturated_water_temperature",
        "name": "饱和水温度--加热器疏水温度",
        "symbol": "te‘",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_saturated_water_enthalpy",
        "name": "饱和水焓",
        "symbol": "he’",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_work_pressure",
        "name": "工作压力",
        "symbol": "pe‘",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_pressure_loss",
        "name": "抽汽管压损",
        "symbol": "ΔPe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "0.08",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_extraction_pressure",
        "name": "抽汽压力",
        "symbol": "Pe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_extraction_enthalpy",
        "name": "抽汽焓",
        "symbol": "he",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh3_extraction_amount",
        "name": "抽汽量",
        "symbol": "Δde‘",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_water_temperature",
        "name": "给水出水温度",
        "symbol": "tw2",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_water_enthalpy",
        "name": "给水出口焓",
        "symbol": "hw2",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_top_difference",
        "name": "上端差",
        "symbol": "φ",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "2.8",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_saturated_water_temperature",
        "name": "饱和水温度--加热器疏水温度",
        "symbol": "te‘",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_saturated_water_enthalpy",
        "name": "饱和水焓",
        "symbol": "he’",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_work_pressure",
        "name": "工作压力",
        "symbol": "pe‘",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_pressure_loss",
        "name": "抽汽管压损",
        "symbol": "ΔPe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "0.08",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_extraction_pressure",
        "name": "抽汽压力",
        "symbol": "Pe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_extraction_enthalpy",
        "name": "抽汽焓",
        "symbol": "he",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "lh2_extraction_amount",
        "name": "抽汽量",
        "symbol": "Δde‘",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "d_water_temperature",
        "name": "给水出水温度",
        "symbol": "tw2",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "d_water_enthalpy",
        "name": "给水出口焓",
        "symbol": "hw2",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "d_work_pressure",
        "name": "工作压力",
        "symbol": "pe‘",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "d_pressure_loss",
        "name": "抽汽管压损",
        "symbol": "ΔPe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "0.08",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "d_extraction_pressure",
        "name": "抽汽压力",
        "symbol": "Pe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "d_extraction_enthalpy",
        "name": "抽汽焓",
        "symbol": "he",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "d_extraction_amount",
        "name": "抽汽量",
        "symbol": "Δde‘",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "c_water_temperature",
        "name": "给水出水温度",
        "symbol": "tw2",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "c_water_enthalpy",
        "name": "给水出口焓",
        "symbol": "hw2",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "c_work_pressure",
        "name": "工作压力",
        "symbol": "pe‘",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "c_pressure_loss",
        "name": "抽汽管压损",
        "symbol": "ΔPe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "0.08",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "c_extraction_pressure",
        "name": "抽汽压力",
        "symbol": "Pe",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "c_extraction_enthalpy",
        "name": "抽汽焓",
        "symbol": "he",
        "unit": "kj/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "c_extraction_amount",
        "name": "抽汽量",
        "symbol": "Δde‘",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_turbine_efficiency",
        "name": "汽轮机内效率",
        "symbol": "ηTi",
        "unit": "--",
        "calculate": "",
        "remark": "（1）注意补汽压力所对应的的补汽点位置；（2）注意无高加时，高加抽气压力需手动修改",
        "default_value": "0.82",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_mechanical_efficiency",
        "name": "机械效率",
        "symbol": "ηm",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.95",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_generator_efficiency",
        "name": "发电机效率",
        "symbol": "ηg",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "0.97",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "Mpa",
        "calculate": "设计参数",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "设计参数",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_flow",
        "name": "流量",
        "symbol": "G1",
        "unit": "t/h",
        "calculate": "热源产生主蒸汽总流量",
        "remark": "",
        "default_value": "",
        "disable": ""
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_entropy",
        "name": "熵",
        "symbol": "",
        "unit": "kJ/(kg·℃)",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_enthalpy",
        "name": "焓",
        "symbol": "Izo",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high1_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high1_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high1_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high1_enthalpy",
        "name": "焓",
        "symbol": "Izob",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high1_flow",
        "name": "流量",
        "symbol": "GH1",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_hh1_power",
        "name": "",
        "symbol": "P2",
        "unit": "KW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high2_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high2_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high2_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high2_enthalpy",
        "name": "焓",
        "symbol": "Izob",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_high2_flow",
        "name": "流量",
        "symbol": "GH2",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_hh1_hh2_power",
        "name": "",
        "symbol": "P3",
        "unit": "KW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_deoxidize_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_deoxidize_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_deoxidize_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_deoxidize_enthalpy",
        "name": "焓",
        "symbol": "Izob",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_deoxidize_flow",
        "name": "流量",
        "symbol": "GD",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_hh2_deoxidize_power",
        "name": "",
        "symbol": "P4",
        "unit": "KW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_exhaust_point_pressure",
        "name": "压力",
        "symbol": "P2'",
        "unit": "Mpa",
        "calculate": "设计参数",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_exhaust_point_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "设计参数",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_exhaust_point_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_exhaust_point_enthalpy",
        "name": "焓",
        "symbol": "Izob",
        "unit": "kJ/kg",
        "calculate": "实际焓值",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_exhaust_point_flow",
        "name": "流量",
        "symbol": "G2",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_deoxidize_exhaust_power",
        "name": "",
        "symbol": "P1",
        "unit": "KW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low1_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low1_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low1_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low1_enthalpy",
        "name": "焓",
        "symbol": "Izob",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low1_flow",
        "name": "流量",
        "symbol": "GL2",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_exhaust_lh1_power",
        "name": "",
        "symbol": "P5",
        "unit": "KW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low2_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low2_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low2_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low2_enthalpy",
        "name": "焓",
        "symbol": "Izob",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low2_flow",
        "name": "流量",
        "symbol": "GL2",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_lh1_lh2_power",
        "name": "",
        "symbol": "P6",
        "unit": "KW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low3_pressure",
        "name": "压力",
        "symbol": "",
        "unit": "Mpa",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low3_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low3_temperature",
        "name": "温度",
        "symbol": "",
        "unit": "℃",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low3_enthalpy",
        "name": "焓",
        "symbol": "Izob",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_low3_flow",
        "name": "流量",
        "symbol": "GL2",
        "unit": "t/h",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_lh2_lh3_power",
        "name": "",
        "symbol": "P6",
        "unit": "KW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_exhaust_pressure",
        "name": "压力",
        "symbol": "P3",
        "unit": "Mpa",
        "calculate": "湿冷：0.005～0.007空冷0.015",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_exhaust_entropy",
        "name": "熵",
        "symbol": "S'",
        "unit": "kJ/(kg·℃)",
        "calculate": "主蒸汽绝热等熵",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_exhaust_enthalpy",
        "name": "焓",
        "symbol": "Ipo",
        "unit": "kJ/kg",
        "calculate": "汽轮机绝热等熵做功排汽焓值，查表",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_exhaust_enthalpy_actual",
        "name": "实际焓",
        "symbol": "Ipo‘",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_exhaust_enthalpy_steam",
        "name": "饱和蒸汽焓",
        "symbol": "Ipog",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_exhaust_enthalpy_water",
        "name": "饱和水焓",
        "symbol": "Ipos",
        "unit": "kJ/kg",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_exhaust_dry",
        "name": "干度",
        "symbol": "x",
        "unit": "--",
        "calculate": "(Ipo'-Ipos）/（Ipog-Ipos）小型汽轮机排汽湿度控制在10~12%以内",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_steam_exhaust_flow",
        "name": "流量",
        "symbol": "GL2",
        "unit": "t/h",
        "calculate": "压力提高，排汽干度降低；",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_lh2_steam_power",
        "name": "LH2至乏汽功率",
        "symbol": "P7",
        "unit": "KW",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_total_power",
        "name": "总功率",
        "symbol": "",
        "unit": "--",
        "calculate": "",
        "remark": "",
        "default_value": "",
        "disable": "T"
    },
    {
        "module_name": "GPG_TurbineOfPTS",
        "name_eng": "i_calculation_error",
        "name": "计算误差",
        "symbol": "",
        "unit": "%",
        "calculate": "±3%以内",
        "remark": "",
        "default_value": "",
        "disable": "T"
    }
]

# 煤气发电需求调查表
questionnaire_data = [{
    "module_name": "GPG_questionnaire",
    "name_eng": "surplus_gas_bfg",
    "name": u"BFG 富余的煤气流量",
    "symbol": u"",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "surplus_gas_ldg",
    "name": u"LDG 富余的煤气流量",
    "symbol": u"",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "surplus_gas_cog",
    "name": u"COG 富余的煤气流量",
    "symbol": u"",
    "unit": u"Nm³/h",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "bfg_gas_temperature",
    "name": u"BFG 煤气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "ldg_gas_temperature",
    "name": u"LDG 煤气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "cog_gas_temperature",
    "name": u"COG 煤气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "bfg_gas_pressure",
    "name": u"BFG 煤气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "ldg_gas_pressure",
    "name": u"LDG 煤气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "cog_gas_pressure",
    "name": u"COG 煤气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "bfg_gas_calorific_value",
    "name": u"BFG 煤气热值",
    "symbol": u"",
    "unit": u"kJ/Nm³",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "ldg_gas_calorific_value",
    "name": u"LDG 煤气热值",
    "symbol": u"",
    "unit": u"kJ/Nm³",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "cog_gas_calorific_value",
    "name": u"COG 煤气热值",
    "symbol": u"",
    "unit": u"kJ/Nm³",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "provide_steam_amount",
    "name": u"对外供蒸汽量",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"",
    "remark": u"无则不需要填写"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "provide_steam_pressure",
    "name": u"对外供蒸汽压",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u"无则不需要填写"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "h2_content",
    "name": u"H2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "co_content",
    "name": u"CO",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "ch4_content",
    "name": u"CH4",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "c2h4_content",
    "name": u"C2H4",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "c3h8_content",
    "name": u"C3H8",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "c4h10_content",
    "name": u"C4H10",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "n2_content",
    "name": u"N2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "o2_content",
    "name": u"O2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "co2_content",
    "name": u"CO2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "h2s_content",
    "name": u"H2S",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "cmhn_content",
    "name": u"CmHn",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "h2o_content",
    "name": u"H2O",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "so2_content",
    "name": u"SO2",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "low_heating",
    "name": u"低位发热量",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "high_heating",
    "name": u"高位发热量",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_temperature_h",
    "name": u"最高大气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_temperature_a",
    "name": u"平均大气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_temperature_l",
    "name": u"最低大气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_pressure_h",
    "name": u"最高大气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_pressure_a",
    "name": u"平均大气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "atmosphere_pressure_l",
    "name": u"最低大气压力",
    "symbol": u"",
    "unit": u"kPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "relative_humidity_h",
    "name": u"最高相对湿度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "relative_humidity_a",
    "name": u"平均相对湿度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "relative_humidity_l",
    "name": u"最低相对湿度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "outside_wind_speed_h",
    "name": u"最高室外风速",
    "symbol": u"",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "outside_wind_speed_a",
    "name": u"平均室外风速",
    "symbol": u"",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "outside_wind_speed_l",
    "name": u"最低室外风速",
    "symbol": u"",
    "unit": u"m/s",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "seismic_fortification_intensity_h",
    "name": u"最高抗震设防烈度",
    "symbol": u"",
    "unit": u"度",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "seismic_fortification_intensity_a",
    "name": u"平均抗震设防烈度",
    "symbol": u"",
    "unit": u"度",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "seismic_fortification_intensity_l",
    "name": u"最低抗震设防烈度",
    "symbol": u"",
    "unit": u"度",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
{
    "module_name": "GPG_questionnaire",
    "name_eng": "above_sea_level",
    "name": u"海拔高度",
    "symbol": u"",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
{
    "module_name": "GPG_questionnaire",
    "name_eng": "design_earthquake_acceleration",
    "name": u"设计基本地震加速度",
    "symbol": u"",
    "unit": u"g",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_pressure",
    "name": u"水压力",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_temperature",
    "name": u"水温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_ph",
    "name": u"PH值",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_suspended_matter",
    "name": u"悬浮物",
    "symbol": u"",
    "unit": u"mg/L",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_cl",
    "name": u"氯离子",
    "symbol": u"",
    "unit": u"mg/L",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "nitrogen_purity",
    "name": u"氮气纯度",
    "symbol": u"",
    "unit": u"%",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "nitrogen_pressure",
    "name": u"氮气压力范围",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "nitrogen_temperature",
    "name": u"氮气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "compressed_air_pressure",
    "name": u"压缩空气压力范围",
    "symbol": u"",
    "unit": u"MPa",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "compressed_air_temperature",
    "name": u"压缩空气温度",
    "symbol": u"",
    "unit": u"℃",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "grid_voltage",
    "name": u"并网电压",
    "symbol": u"",
    "unit": u"kV",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "max_short_circuit_capacity",
    "name": u"最大短路容量",
    "symbol": u"",
    "unit": u"kVA",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "voltage_other",
    "name": u"电压其他",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "factory_location_elevation",
    "name": u"拟建厂区坐标点和高程的地形图",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u"CAD版，含风玫瑰"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "dielectric_position_height_caliber_route",
    "name": u"能源介质接点位置、标高、管径、路由",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "water_quality_analysis_report",
    "name": u"全水质分析报告",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u"尽可能提供"
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "cooling_tower",
    "name": u"冷却方式及冷却塔形式",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "project_approval_eia",
    "name": u"项目立项及环评手续",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "converter",
    "name": u"转炉",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "heat_recovery",
    "name": u"烧结余热回收",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "furnace",
    "name": u"加热炉",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "steam_other",
    "name": u"其他",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "a_summer",
    "name": u"夏季平均",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "a_year",
    "name": u"年平均",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "a_winter",
    "name": u"冬季平均",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "a_cold",
    "name": u"最冷月平均",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "a_hot",
    "name": u"最热月平均",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "extreme_h",
    "name": u"年极端最高",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""},
 {
    "module_name": "GPG_questionnaire",
    "name_eng": "extreme_l",
    "name": u"年极端最低",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
	, "default_value": "", 
 	 "disable": ""}
]

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
    "module_name": "economic_indicators",
    "name_eng": "smoke_heat_consumption_rate",
    "name": u"抽凝工况热耗率",
    "symbol": u"qc",
    "unit": u"kJ/(kW.h)",
    "calculate": u"抽凝工况下，机组每产生1kW.h电所需要的热量；Do*(Izo-Igs)/Pc",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "heat_consumption_rate",
    "name": u"纯凝工况热耗率",
    "symbol": u"qn",
    "unit": u"kJ/(kW.h)",
    "calculate": u"纯凝工况下，机组每产生1kW.h电所需要的热量；Do*(Izo-Igs)/Pn",
    "remark": "",
    "default_value": "",
    "disable": "T"
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
    "default_value": "8000",
    "disable": ""
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
    "calculate": u"G2*（Izob-iw）/1000*T",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "annual_power_generation",
    "name": u"年发电量",
    "symbol": u"Pa",
    "unit": u"万kW.h",
    "calculate": u"Pc*T/10000+Pn*（Ha-T）/10000",
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
    "default_value": "6",
    "disable": ""
}, {
    "module_name": "economic_indicators",
    "name_eng": "annual_power_supply",
    "name": u"年供电量",
    "symbol": u"Pag",
    "unit": u"万kW.h",
    "calculate": u"Pa*（1-ζ/100）",
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
    "module_name": "economic_indicators",
    "name_eng": "smoke_power_coal_consumption",
    "name": u"抽凝工况发电标煤耗率",
    "symbol": u"bcf",
    "unit": u"kg/h",
    "calculate": u"标准煤收到基低位发热量按7000kcal/kg计；qc/ηg/ηp/（7000*4.1868）*1000",
    "remark": "",
    "default_value": "",
    "disable": "T"
}, {
    "module_name": "economic_indicators",
    "name_eng": "power_coal_consumption",
    "name": u"纯凝工况发电标煤耗率",
    "symbol": u"bcf",
    "unit": u"kg/h",
    "calculate": u"标准煤收到基低位发热量按7000kcal/kg计；qn/ηg/ηp/（7000*4.1868）*1000",
    "remark": "",
    "default_value": "",
    "disable": "T"
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
    "module_name": "economic_indicators",
    "name_eng": "smoke_heat_efficiency",
    "name": u"抽凝工况全厂热效率",
    "symbol": u"ηcr",
    "unit": u"%",
    "calculate": u"（Pc*3.6+G2*(Izob-iw)）/Bj/Qnet.Ar*100",
    "remark": "",
    "default_value": "",
    "disable": "T"
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


class AddGPG():
    # 初始化数据
    @staticmethod
    def init_data():
        data = [questionnaire_data, GPGBoilerOfPTS_data, GPGTurbineOfPTS_data, 
                GPGGasAirSys_data, GPGSmokeResistance_data, GPGWindResistance_data,
                GPGCirculatingWaterSystem_data, GPGSmokeAirCalculate_data,
                GPGTurbineAuxiliarySystem_data, GPGSteamWaterPipe_data,
                GPGBoilerAuxiliaries_data, economic_indicators_data]

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
            default_value = data[index]["default_value"]
            disable = data[index]["disable"]
            
            gasPowerGenerationConstant = GasPowerGenerationConstant.create_gasPowerGenerationConstant(
                module_name, name_eng, name, symbol, unit, calculate, remark, default_value, disable)
            GasPowerGenerationConstant.insert_gasPowerGenerationConstant(gasPowerGenerationConstant)
