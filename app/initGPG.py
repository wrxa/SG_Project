# -*- coding: utf-8 -*-
# from models import CoalCHPConstant, CoalCHPComponent,\
#                    CoalCHPNeedsQuestionnaire, Role, User, Company

from gasPowerGeneration_models import GasPowerGenerationConstant, \
                                    GasPowerGenerationNeedsQuestionnaire, \
                                    GPGBoilerOfPTS, GPGFlueGasAirSystem, \
                                    GPGSmokeResistance, GPGWindResistance, \
                                    GPGCirculatingWaterSystem, GPGSmokeAirCalculate
# 煤气发电 烟风量计算
GPGSmokeAirCalculate_data = [{
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "h2",
        "name": u"H2",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "co",
        "name": u"CO",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "ch4",
        "name": u"CH4",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "c2h4",
        "name": u"C2H4",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "c3h8",
        "name": u"C3H8",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "c4h10",
        "name": u"C4H10",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "n2",
        "name": u"N2",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "o2",
        "name": u"O2",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "co2",
        "name": u"CO2",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "h2s",
        "name": u"H2S",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "cmhn",
        "name": u"CmHn",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_need_air_amonut_per_m3",
        "name": u"标态下每m³干燃气燃烧所需理论空气量",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_air_density",
        "name": u"标态下空气密度",
        "symbol": u"ρ0",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_need_air_mass_per_m3",
        "name": u"标态下每m³干燃气燃烧所需理论空气质量",
        "symbol": u"L0",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "excessive_air_coefficient",
        "name": u"过量空气系数",
        "symbol": u"α",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"1.05-1.1"
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "actual_need_air_amonut",
        "name": u"实际所需空气量",
        "symbol": u"V",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_gas_humidity_per_m3",
        "name": u"标态下每m³燃气的含湿量",
        "symbol": u"dR",
        "unit": u"g/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_air_humidity_per_m3",
        "name": u"标态下每m³空气的含湿量",
        "symbol": u"dK",
        "unit": u"g/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "actual_air_amount_in_wet",
        "name": u"空气中有水时，实际空气量",
        "symbol": u"V",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_ro2_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中RO2",
        "symbol": u"VRO2",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_n2_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中N2",
        "symbol": u"VN2",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_actual_n2_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中N2实际",
        "symbol": u"VN2",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_h2o_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中H2O",
        "symbol": u"VH2O",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_actual_h2o_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中H2O实际",
        "symbol": u"VH2O",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "constant_o2_amonut_per_m3",
        "name": u"标态下每m³燃气燃烧理论烟气量中O2",
        "symbol": u"VO2",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "actual_burning_gas_amonut",
        "name": u"实际燃烧烟气量",
        "symbol": u"Vy",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "theory_burning_gas_amonut",
        "name": u"理论燃烧烟气量",
        "symbol": u"Vy",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "net_calorific_value",
        "name": u"低位发热量",
        "symbol": u"Hl",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "gross_heating_value",
        "name": u"高位发热量",
        "symbol": u"Hh",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "gas_init_temperature",
        "name": u"燃气初始温度",
        "symbol": u"tg",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "air_init_temperature",
        "name": u"空气初始温度",
        "symbol": u"tg",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "gas_average_cpvh",
        "name": u"燃气平均定压体积热容",
        "symbol": u"Cg",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "gas_h2o_average_cpvh",
        "name": u"燃气中H2O平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "air_average_cpvh",
        "name": u"空气平均定压体积热容",
        "symbol": u"Ca",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "air_h2o_average_cpvh",
        "name": u"空气中H2O平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name":
        "GPG_SmokeAirCalculate",
        "name_eng":
        "hy_adiabatic_calorimeter_temperature",
        "name":
        u"假设---绝热状态的热量计温度",
        "symbol":
        u"tc",
        "unit":
        u"℃",
        "calculate":
        u"",
        "remark":
        u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_ro2_average_cpvh",
        "name": u"烟气中RO2平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_h2o_average_cpvh",
        "name": u"烟气中H2O平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_n2_average_cpvh",
        "name": u"烟气中N2平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_o2_average_cpvh",
        "name": u"烟气中O2平均定压体积热容",
        "symbol": u"C",
        "unit": u"KJ/m³.K",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "deviation_check",
        "name": u"误差核对---2%以内合理",
        "symbol": u"",
        "unit": u"%",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "incomplete_combustion_loss",
        "name": u"化学不完全燃烧热损失",
        "symbol": u"Q3",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "heat_loss_coefficient",
        "name": u"散热损失系数",
        "symbol": u"q5",
        "unit": u"%",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "heat_loss",
        "name": u"散热损失",
        "symbol": u"Q5",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "calc_theory_burning_temperature",
        "name": u"计算---理论燃烧温度",
        "symbol": u"tc",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "high_temperature_coefficient",
        "name": u"高温系数",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "coefficient_actual_temperature",
        "name": u"实际燃烧温度--系数法",
        "symbol": u"tc",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "calc_actual_temperature",
        "name": u"实际燃烧温度--计算法",
        "symbol": u"tc",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "ro2_volume_enthalpy",
        "name": u"烟气中R02体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "n2_volume_enthalpy",
        "name": u"烟气中N2体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "h2o_volume_enthalpy",
        "name": u"烟气中H2O体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "air_volume_enthalpy",
        "name": u"烟气中空气体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "dust_volume_enthalpy",
        "name": u"烟气中飞灰体积焓",
        "symbol": u"ct",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "theory_smoke_volume_enthalpy",
        "name": u"理论烟气体积焓",
        "symbol": u"hy0",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "theory_air_volume_enthalpy",
        "name": u"理论空气体积焓",
        "symbol": u"hk0",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "theory_dust_volume_enthalpy",
        "name": u"理论飞灰体积焓",
        "symbol": u"hfh",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "smoke_enthalpy",
        "name": u"烟气焓",
        "symbol": u"hy",
        "unit": u"KJ/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "qd_net",
        "name": u"燃气干燥基低位发热量",
        "symbol": u"Qd.net",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "qar_net",
        "name": u"燃气收到基地位发热量",
        "symbol": u"Qar.net",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_need_air_amonut_b_10500",
        "name": u"标态下每m³干燃气燃烧所需理论空气量(Qd.net<10500时)",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_need_air_amonut_a_10500",
        "name": u"标态下每m³干燃气燃烧所需理论空气量(Qd.net>10500时)",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_need_air_amonut_gas",
        "name": u"标态下每m³干燃气燃烧所需理论空气量(天然气)",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_need_air_amonut_lng",
        "name": u"标态下每m³干燃气燃烧所需理论空气量(液化石油气)",
        "symbol": u"V0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_excessive_air_coefficient",
        "name": u"过量空气系数",
        "symbol": u"α",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_actual_need_air_amonut",
        "name": u"标态下每m³干燃气燃烧所需实际空气量",
        "symbol": u"V",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_theory_burning_amonut_gas",
        "name": u"理论燃烧烟气量(天然气)",
        "symbol": u"Vy'",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_theory_burning_amonut_oag",
        "name": u"理论燃烧烟气量(石油伴生气)",
        "symbol": u"Vy'",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_theory_burning_amonut_lng",
        "name": u"理论燃烧烟气量(液化天然气)",
        "symbol": u"Vy'",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_theory_burning_amonut_cog",
        "name": u"理论燃烧烟气量(焦炉煤气)",
        "symbol": u"Vy'",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "unknown_actual_burning_gas_amonut",
        "name": u"实际燃烧烟气量",
        "symbol": u"Vy",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
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
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_theory_air_amount_a_35799",
        "name": u"理论空气量(QL＞35799)",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_theory_air_amount_b_35799",
        "name": u"理论空气量(QL＜35799)",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_excessive_air_coefficient",
        "name": u"过量空气系数",
        "symbol": u"α",
        "unit": u"",
        "calculate": u"1.05~1.1",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_actual_amonut_a_35799",
        "name": u"实际烟气量(QL＞35799)",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_gas_actual_amonut_b_35799",
        "name": u"实际烟气量(QL＜35799)",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_boiler_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
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
    }, {
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
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_boiler_actual_amonut_a_12561",
        "name": u"实际烟气量(QL＞12561)",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_boiler_actual_amonut_b_12561",
        "name": u"实际烟气量(QL＜12561)",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_liquid_fuel_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_liquid_fuel_theory_air_amount",
        "name": u"理论空气量",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_liquid_fuel_actual_amonut",
        "name": u"实际烟气量",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_coal_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_coal_theory_air_amount",
        "name": u"理论空气量",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_coal_excessive_air_coefficient",
        "name": u"过量空气系数",
        "symbol": u"α",
        "unit": u"m³/m³",
        "calculate": u"1.15~1.25",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_coal_actual_amonut",
        "name": u"实际烟气量",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_qnet",
        "name": u"低位发热量",
        "symbol": u"QL",
        "unit": u"KJ/Nm³",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_water_content",
        "name": u"含水量",
        "symbol": u"W",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_theory_air_amount",
        "name": u"理论空气量",
        "symbol": u"L0",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_best_water_content",
        "name": u"最佳含水量",
        "symbol": u"Wop",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_SmokeAirCalculate",
        "name_eng": "exp_wood_peat_actual_amonut",
        "name": u"实际烟气量",
        "symbol": u"Vm",
        "unit": u"m³/m³",
        "calculate": u"",
        "remark": u""
    }
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
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "steam_exhaust_flux_summer",
        "name": u"夏季乏汽流量",
        "symbol": u"",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "steam_exhaust_flux_selected",
        "name": u"乏汽流量-选定",
        "symbol": u"",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u"选定"
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulation_ratio_winter",
        "name": u"冬季循环倍率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"北方60~70；中部65~75；南方70~80"
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulation_ratio_summer",
        "name": u"夏季循环倍率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"北方60~70；中部65~75；南方70~80"
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulation_water_flow_winter",
        "name": u"冬季循环水量",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulation_water_flow_summer",
        "name": u"夏季循环水量",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
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
    }, {
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
    }, {
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
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "selected_total_circulation_water_flow",
        "name": u"总循环水量-选定",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u"Q选定"
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "spray_density",
        "name": u"喷淋密度",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "spray_area",
        "name": u"喷淋面积",
        "symbol": u"",
        "unit": u"m2",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "dry_bulb_temperature",
        "name": u"干球温度",
        "symbol": u"",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "dry_bulb_k_coefficient",
        "name": u"K",
        "symbol": u"",
        "unit": u"",
        "calculate": u"插值法",
        "remark": u"参考表5.6.1"
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "evaporation_loss_rate",
        "name": u"蒸发损失率",
        "symbol": u"",
        "unit": u"%",
        "calculate": u"Pe=K*温差",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "evaporation_loss",
        "name": u"蒸发损失",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"Qe=Pe*Q/100",
        "remark": u""
    }, {
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
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "wind_blow_loss",
        "name": u"风吹损失",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "concentration_rate",
        "name": u"浓缩倍率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"C：一般取3",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "discharge_rate",
        "name": u"排污损失率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"Pb=（Pe-Pw（c-1））/（c-1）",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "discharge_capacity",
        "name": u"排污量",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "supply_water_amount",
        "name": u"补充水量",
        "symbol": u"",
        "unit": u"m3/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_water_amount",
        "name": u"循环水池15-25分钟循环水量",
        "symbol": u"",
        "unit": u"m3",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_size_deep",
        "name": u"循环水池尺寸-深",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_size_length",
        "name": u"循环水池尺寸-长",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_size_width",
        "name": u"循环水池尺寸-宽",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "circulating_pool_size_checked",
        "name": u"校核循环水池尺寸",
        "symbol": u"",
        "unit": u"m3",
        "calculate": u"",
        "remark": u""
    }, {
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
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "condenser_friction",
        "name": u"凝汽器阻力",
        "symbol": u"",
        "unit": u"Mpa",
        "calculate": u"",
        "remark": u"厂家提供"
    }, {
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
    }, {
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
    }, {
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
    }, {
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
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pipe_loss",
        "name": u"管道损失",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"暂定采用5mH2O",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "y_filter_loss",
        "name": u"Y型过滤器损失",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u"厂家提供"
    }, {
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
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_flow",
        "name": u"流量",
        "symbol": u"",
        "unit": u"t/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_efficiency",
        "name": u"泵效率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"0.6~0.85"
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_transmission_efficiency",
        "name": u"机械传动效率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"直连1.0，联轴器0.98，皮带0.95"
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_motor_efficiency",
        "name": u"电动机效率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u"通常取0.98"
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_motor_spare_coefficient",
        "name": u"电动机备用系数",
        "symbol": u"",
        "unit": u"",
        "calculate": u"查表选取",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "pump_matching_motor_power",
        "name": u"配套电机功率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"ρβgHqv/(3600*1000*η*η2*η3)",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "selected_pump_model_power",
        "name": u"选用型号-功率",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "selected_pump_model_flow",
        "name": u"选用型号-流量",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_CirculatingWaterSystem",
        "name_eng": "selected_pump_model_lift",
        "name": u"选用型号-扬程",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    }
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
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "recommend_velocity_hotwind",
        "name": u"推荐流速",
        "symbol": u"",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"（8)P6"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_temperature",
        "name": u"计算温度",
        "symbol": u"T",
        "unit": u"℃",
        "calculate": u"给定",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_amount",
        "name": u"风量",
        "symbol": u"V",
        "unit": u"m³/h",
        "calculate": u"燃烧计算",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_density",
        "name": u"密度",
        "symbol": u"ρ",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_flow_velocity",
        "name": u"流速",
        "symbol": u"W",
        "unit": u"m/s",
        "calculate": u"取定",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "intake_to_preheater_dynamic_pressure_head",
        "name": u"动压头",
        "symbol": u"Hd",
        "unit": u"Pa",
        "calculate": u"W2*ρ/2",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_section_area",
        "name": u"风管截面积",
        "symbol": u"F",
        "unit": u"m2",
        "calculate": u"V/W/3600",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_length",
        "name": u"长",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"取定",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"F/A",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_perimeter",
        "name": u"风管周长",
        "symbol": u"Lc",
        "unit": u"m",
        "calculate": u"2*(A+B)",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_duct_equivalent_diameter",
        "name": u"管道当量直径",
        "symbol": u"De",
        "unit": u"m",
        "calculate": u"4*F/Lc",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_gas_kinetic_viscosity",
        "name": u"气体运动粘度",
        "symbol": u"υ",
        "unit": u"m2/s",
        "calculate": u"",
        "remark": u"（2）P288"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_reynolds_number",
        "name": u"雷诺数",
        "symbol": u"Re",
        "unit": u"",
        "calculate": u"W*De/υ",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_absolute_tube_roughness",
        "name": u"管道内壁绝对粗糙度",
        "symbol": u"△",
        "unit": u"m",
        "calculate": u"",
        "remark": u"（2）P109"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_relative_tube_roughness",
        "name": u"管道内壁相对粗糙度",
        "symbol": u"△1",
        "unit": u"m",
        "calculate": u"△/De",
        "remark": u"（2）P107"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_560_relative_tube_roughness",
        "name": u"560/△1",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_discriminant",
        "name": u"判别式",
        "symbol": u"",
        "unit": u"",
        "calculate": u"4000 <Re< 560/△1",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_frictional_resistance",
        "name": u"摩擦阻力",
        "symbol": u"△Pm1",
        "unit": u"Pa",
        "calculate": u"△Pd*L1",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_frictional_resistance_coefficient",
        "name": u"摩擦阻力系数",
        "symbol": u"λ",
        "unit": u"",
        "calculate": u"图7.2.2",
        "remark": u"（2）P108"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_unit_length_frictional_resistance",
        "name": u"单位长度摩擦阻力",
        "symbol": u"△Pd",
        "unit": u"Pa/m",
        "calculate": u"λ*Hd/De",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_ducting_length",
        "name": u"风管长度",
        "symbol": u"L1",
        "unit": u"m",
        "calculate": u"布置图",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_local_resistance",
        "name": u"局部阻力",
        "symbol": u"△Pj1",
        "unit": u"",
        "calculate": u"ζ*Hd",
        "remark": u"（2）P109"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_local_resistance_coefficient",
        "name": u"局部阻力系数",
        "symbol": u"ζ",
        "unit": u"",
        "calculate": u"ζ1+ζ2+ζ3",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_single_local_resistance_coefficient",
        "name": u"1个吸风口局部阻力系数",
        "symbol": u"ζ1",
        "unit": u"",
        "calculate": u"有档板门",
        "remark": u"（2）P140"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_single_bellows",
        "name": u"1个风机进口风箱",
        "symbol": u"ζ2",
        "unit": u"",
        "calculate": u"改进式进风箱",
        "remark": u"（2）P144"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_single_damper",
        "name": u"1个进口挡板门",
        "symbol": u"ζ3",
        "unit": u"",
        "calculate": u"假定θ=15°",
        "remark": u"（2）P130"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_inlet_total_pressure",
        "name": u"风机进口段总阻力",
        "symbol": u"△Pz1",
        "unit": u"",
        "calculate": u"△Pm1+△Pj1",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_frictional_resistance",
        "name": u"摩擦阻力",
        "symbol": u"△Pm2",
        "unit": u"Pa",
        "calculate": u"△Pd*L2",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_unit_length_frictional_resistance",
        "name": u"单位长度摩擦阻力",
        "symbol": u"△Pd",
        "unit": u"Pa/m",
        "calculate": u"约同进口",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_ducting_length",
        "name": u"风管长度",
        "symbol": u"L2",
        "unit": u"m",
        "calculate": u"布置图估计",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_local_resistance",
        "name": u"局部阻力",
        "symbol": u"△Pj2",
        "unit": u"",
        "calculate": u"ζ*Hd",
        "remark": u"（2）P109"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_local_resistance_coefficient",
        "name": u"局部阻力系数",
        "symbol": u"ζ",
        "unit": u"",
        "calculate": u"ζ1+ζ2+ζ3",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_single_increase_pipe",
        "name": u"1只出口渐扩管",
        "symbol": u"ζ1",
        "unit": u"",
        "calculate": u"假定",
        "remark": u"（2）P136"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_90_section_slow_turn_elbow",
        "name": u"1只90度等截面急转弯头/（二次风2只）",
        "symbol": u"ζ2",
        "unit": u"",
        "calculate": u"ζ2",
        "remark": u"（2）P136"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_preheater_diffuser_pipe",
        "name": u"空预器接头扩散管",
        "symbol": u"ζ3",
        "unit": u"",
        "calculate": u"假定",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "fan_outlet_to_preheater_total_pressure",
        "name": u"风机出口至空预器总阻力",
        "symbol": u"△Pz2",
        "unit": u"",
        "calculate": u"△Pm2+△Pj2",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_temperature",
        "name": u"计算温度",
        "symbol": u"T",
        "unit": u"℃",
        "calculate": u"烟风量计算表",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_amount",
        "name": u"风量",
        "symbol": u"V",
        "unit": u"m³/h",
        "calculate": u"烟风量计算表",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_density",
        "name": u"密度",
        "symbol": u"ρ",
        "unit": u"kg/m³",
        "calculate": u"烟风量计算表",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_flow_velocity",
        "name": u"流速",
        "symbol": u"W",
        "unit": u"m/s",
        "calculate": u"取定",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_to_boiler_dynamic_pressure_head",
        "name": u"动压头",
        "symbol": u"Hd",
        "unit": u"Pa",
        "calculate": u"W2*ρ/2",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_section_area",
        "name": u"风管截面积（热风管分两路进入风室）",
        "symbol": u"F",
        "unit": u"m2",
        "calculate": u"V/W/3600/2",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_diameter",
        "name": u"圆管直径(一、二次热风为圆管）",
        "symbol": u"D(De)",
        "unit": u"m",
        "calculate": u"F=0.785*D2",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_length",
        "name": u"长",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"取定",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"F/A",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_perimeter",
        "name": u"风管周长",
        "symbol": u"Lc",
        "unit": u"m",
        "calculate": u"2*(A+B)",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_duct_equivalent_diameter",
        "name": u"管道当量直径",
        "symbol": u"De",
        "unit": u"m",
        "calculate": u"4*F/Lc",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_gas_kinetic_viscosity",
        "name": u"气体运动粘度",
        "symbol": u"υ",
        "unit": u"m2/s",
        "calculate": u"",
        "remark": u"（2）P288"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_reynolds_number",
        "name": u"雷诺数",
        "symbol": u"Re",
        "unit": u"",
        "calculate": u"W*De/υ",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_absolute_tube_roughness",
        "name": u"管道内壁绝对粗糙度",
        "symbol": u"△",
        "unit": u"m",
        "calculate": u"",
        "remark": u"（2）P109"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_relative_tube_roughness",
        "name": u"管道内壁相对粗糙度",
        "symbol": u"△1",
        "unit": u"m",
        "calculate": u"△/De",
        "remark": u"（2）P107"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_560_relative_tube_roughness",
        "name": u"560/△1",
        "symbol": u"",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_discriminant",
        "name": u"判别式",
        "symbol": u"",
        "unit": u"",
        "calculate": u"4000 <Re< 560/△1",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_frictional_resistance",
        "name": u"摩擦阻力",
        "symbol": u"△Pm3",
        "unit": u"Pa",
        "calculate": u"△Pd*L3",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_frictional_resistance_coefficient",
        "name": u"摩擦阻力系数",
        "symbol": u"λ",
        "unit": u"",
        "calculate": u"图7.2.2",
        "remark": u"（2）P108"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_unit_length_frictional_resistance",
        "name": u"单位长度摩擦阻力",
        "symbol": u"△Pd",
        "unit": u"Pa/m",
        "calculate": u"λ*Hd/De",
        "remark": u"（2）P106"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_ducting_length",
        "name": u"风管长度",
        "symbol": u"L3",
        "unit": u"m",
        "calculate": u"布置图",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_local_resistance",
        "name": u"局部阻力",
        "symbol": u"△Pj3",
        "unit": u"",
        "calculate": u"ζ*Hd",
        "remark": u"（2）P109"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_local_resistance_coefficient",
        "name": u"局部阻力系数",
        "symbol": u"ζ",
        "unit": u"",
        "calculate": u"ζ1+ζ2+ζ3+ζ4",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_shrink_pipe",
        "name": u"1个空预器出口收缩管",
        "symbol": u"ζ1",
        "unit": u"",
        "calculate": u"假定",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_90_sharp_turn_elbow",
        "name": u"6只90度等截面急转弯头",
        "symbol": u"ζ2",
        "unit": u"",
        "calculate": u"ζ2=n*ζo",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_90_sharp_turn_elbow_count",
        "name": u"弯头数量",
        "symbol": u"n",
        "unit": u"",
        "calculate": u"",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_90_sharp_turn_elbow_resistance",
        "name": u"弯头局部阻力系统(焊接圆管）",
        "symbol": u"ζo",
        "unit": u"",
        "calculate": u"",
        "remark": u"（12）P？"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_air_intake_gate",
        "name": u"1个热一次风进风室风门",
        "symbol": u"ζ3",
        "unit": u"",
        "calculate": u"假定θ=10°",
        "remark": u"（2）P130"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_combustor_gate",
        "name": u"1个热一次风进燃烧室风门",
        "symbol": u"ζ4",
        "unit": u"",
        "calculate": u"假定θ=10°",
        "remark": u"（2）P130"
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "preheater_outlet_to_boiler_total_pressure",
        "name": u"空预器出口至锅炉风室总阻力",
        "symbol": u"△Pz3",
        "unit": u"",
        "calculate": u"△Pm3+△Pj3",
        "remark": u""
    },
    {
        "module_name": "GPG_WindResistance",
        "name_eng": "windhole_total_pressure",
        "name": u"风道总阻力",
        "symbol": u"△Pz",
        "unit": u"",
        "calculate": u"△Pz1+△Pz2+△Pz3",
        "remark": u""
    },
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_outlet_smoke_amount",
    "name": u"烟量(空预器出口)",
    "symbol": u"Vyk",
    "unit": u"m³/h",
    "calculate": u"燃烧计算",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_density",
    "name": u"密度",
    "symbol": u"ρyk",
    "unit": u"kg/m³",
    "calculate": u"平均值",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_flow_velocity",
    "name": u"流速",
    "symbol": u"W",
    "unit": u"m/s",
    "calculate": u"取定",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_dynamic_pressure_head",
    "name": u"动压头",
    "symbol": u"Hd",
    "unit": u"Pa",
    "calculate": u"W2*ρ/2",
    "remark": u"（2）P106"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_smoke_tube_area",
    "name": u"烟管截面积",
    "symbol": u"F",
    "unit": u"m2",
    "calculate": u"V/W/3600",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_length",
    "name": u"长",
    "symbol": u"A",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_width",
    "name": u"宽",
    "symbol": u"B",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_duct_perimeter",
    "name": u"风管周长",
    "symbol": u"Lc",
    "unit": u"m",
    "calculate": u"2*(A+B)",
    "remark": u""
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_gas_kinetic_viscosity",
    "name": u"气体运动粘度",
    "symbol": u"υ",
    "unit": u"m2/s",
    "calculate": u"",
    "remark": u"（2）P288"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_reynolds_number",
    "name": u"雷诺数",
    "symbol": u"Re",
    "unit": u"",
    "calculate": u"",
    "remark": u"（2）P106"
}, {
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
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_discriminant",
    "name": u"判别式",
    "symbol": u"",
    "unit": u"",
    "calculate": u"4000 <Re< 560/△1",
    "remark": u"（2）P106"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_frictional_resistance",
    "name": u"摩擦阻力",
    "symbol": u"△Pm1",
    "unit": u"Pa",
    "calculate": u"△Pd*L1",
    "remark": u"（2）P106"
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_ducting_length",
    "name": u"风管长度",
    "symbol": u"L1",
    "unit": u"m",
    "calculate": u"布置图",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_local_resistance",
    "name": u"局部阻力",
    "symbol": u"△Pj1",
    "unit": u"",
    "calculate": u"ζ*Hd",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng":"air_preheater_local_resistance_coefficient",
    "name": u"局部阻力系数",
    "symbol": u"ζ",
    "unit": u"",
    "calculate": u"ζ1+ζ2+ζ3",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_90_outlet_sharp_turn_elbow",
    "name": u"1个90度空预器出口变径急转弯头",
    "symbol": u"ζ1",
    "unit": u"",
    "calculate": u"ζ1=ζu1",
    "remark": u"（2）P111"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_powder_local_resistance_coefficient",
    "name": u"含粉气体局部阻力系数",
    "symbol": u"ζu1",
    "unit": u"",
    "calculate": u"ζo（1+Ku）",
    "remark": u"（2）P110"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_air_elbow_local_resistance_coefficient",
    "name": u"纯空气弯头局部阻力系数",
    "symbol": u"ζo",
    "unit": u"",
    "calculate": u"假定",
    "remark":  u"（12）P？"
}, {
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
}, {
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
}, {
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
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "air_preheater_reducer_tube",
    "name": u"1个渐缩管",
    "symbol": u"ζ3",
    "unit": u"",
    "calculate": u"",
    "remark": u"（2）P137"
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_outlet_smoke_amount",
    "name": u"烟量(除尘器出口)",
    "symbol": u"Vycc",
    "unit": u"m³/h",
    "calculate": u"烟风量计算表",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_density",
    "name": u"密度",
    "symbol": u"ρycc",
    "unit": u"kg/m³",
    "calculate": u"烟风量计算表",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_flow_velocity",
    "name": u"流速",
    "symbol": u"W",
    "unit": u"m/s",
    "calculate": u"取定",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_dynamic_pressure_head",
    "name": u"动压头",
    "symbol": u"Hd",
    "unit": u"Pa",
    "calculate": u"W2*ρ/2",
    "remark": u"（2）P106"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_smoke_tube_area",
    "name": u"烟管截面积",
    "symbol": u"F",
    "unit": u"m2",
    "calculate": u"V/W/3600",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_length",
    "name": u"长",
    "symbol": u"A",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_width",
    "name": u"宽",
    "symbol": u"B",
    "unit": u"m",
    "calculate": u"F/A",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_duct_perimeter",
    "name": u"风管周长",
    "symbol": u"Lc",
    "unit": u"m",
    "calculate": u"2*(A+B)",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_tube_equivalent_diameter",
    "name": u"管道当量直径",
    "symbol": u"De",
    "unit": u"m",
    "calculate": u"4*F/Lc",
    "remark": u"（2）P106"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_gas_kinetic_viscosity",
    "name": u"气体运动粘度",
    "symbol": u"υ",
    "unit": u"m2/s",
    "calculate": u"",
    "remark": u"（2）P288"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_reynolds_number",
    "name": u"雷诺数",
    "symbol": u"Re",
    "unit": u"",
    "calculate": u"W*De/υ",
    "remark": u"（2）P106"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_absolute_tube_roughness",
    "name": u"管道内壁绝对粗糙度",
    "symbol": u"△",
    "unit": u"m",
    "calculate": u"",
    "remark": u"（2）P109"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_relative_tube_roughness",
    "name": u"管道内壁相对粗糙度",
    "symbol": u"△1",
    "unit": u"m",
    "calculate": u"△/De",
    "remark": u"（2）P107"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_560_relative_tube_roughness",
    "name": u"560/△1",
    "symbol": u"",
    "unit": u"",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_discriminant",
    "name": u"判别式",
    "symbol": u"",
    "unit": u"",
    "calculate": u"4000 <Re< 560/△1",
    "remark": u"（2）P106"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_frictional_resistance",
    "name": u"摩擦阻力",
    "symbol": u"△Pm2",
    "unit": u"Pa",
    "calculate": u"△Pd*L3",
    "remark": u"（2）P106"
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_ducting_length",
    "name": u"风管长度",
    "symbol": u"L2",
    "unit": u"m",
    "calculate": u"布置图",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_local_resistance",
    "name": u"局部阻力",
    "symbol": u"△Pj2",
    "unit": u"",
    "calculate": u"ζ*Hd",
    "remark": u""
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_90_outlet_slow_turn_elbow",
    "name": u"1个90度除尘器出口缓转弯头",
    "symbol": u"ζ1",
    "unit": u"",
    "calculate": u"ζ1=ζu1",
    "remark": u"（2）P111"
}, {
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
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_90_section_slow_turn_elbow",
    "name": u"1个90度等截面缓转弯头",
    "symbol": u"ζ2",
    "unit": u"",
    "calculate": u"ζ2=ζu2",
    "remark": u"（2）P111"
}, {
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
}, {
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
}, {
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
}, {
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
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "deduster_inlet_bellows",
    "name": u"1个进口风箱",
    "symbol": u"ζ3",
    "unit": u"",
    "calculate": u"",
    "remark": u"（2）P144"
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_inlet_smoke_amount",
    "name": u"烟量(引风机进口)",
    "symbol": u"Vyxf",
    "unit": u"m3/h",
    "calculate": u"烟风量计算表",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_density",
    "name": u"密度",
    "symbol": u"ρyxf",
    "unit": u"kg/m3",
    "calculate": u"烟风量计算表",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_flow_velocity",
    "name": u"流速",
    "symbol": u"W",
    "unit": u"m/s",
    "calculate": u"取定",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_dynamic_pressure_head",
    "name": u"动压头",
    "symbol": u"Hd",
    "unit": u"Pa",
    "calculate": u"W2*ρ/2",
    "remark": u"（2）P106"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_smoke_tube_area",
    "name": u"烟管截面积",
    "symbol": u"F",
    "unit": u"m2",
    "calculate": u"V/W/3600",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_width",
    "name": u"宽",
    "symbol": u"A",
    "unit": u"m",
    "calculate": u"",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_height",
    "name": u"高",
    "symbol": u"B",
    "unit": u"m",
    "calculate": u"F/A",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_duct_perimeter",
    "name": u"风管周长",
    "symbol": u"Lc",
    "unit": u"m",
    "calculate": u"2*(A+B)",
    "remark": u""
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_gas_kinetic_viscosity",
    "name": u"气体运动粘度",
    "symbol": u"υ",
    "unit": u"m2/s",
    "calculate": u"",
    "remark": u"（2）P288"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_reynolds_number",
    "name": u"雷诺数",
    "symbol": u"Re",
    "unit": u"",
    "calculate": u"W*De/υ",
    "remark": u"（2）P106"
}, {
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
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_discriminant",
    "name": u"判别式",
    "symbol": u"",
    "unit": u"",
    "calculate": u"4000 <Re< 560/△1",
    "remark": u"（2）P106"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_frictional_resistance",
    "name": u"摩擦阻力",
    "symbol": u"△Pm3",
    "unit": u"Pa",
    "calculate": u"△Pd*L3",
    "remark": u"（2）P106"
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_ducting_length",
    "name": u"风管长度",
    "symbol": u"L3",
    "unit": u"m",
    "calculate": u"布置图",
    "remark": u""
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_local_resistance",
    "name": u"局部阻力",
    "symbol": u"△Pj3",
    "unit": u"Pa",
    "calculate": u"ζ*Hd",
    "remark": u""
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_outlet_plate_gate",
    "name": u"1个出口插板门",
    "symbol": u"ζ1",
    "unit": u"",
    "calculate": u"图7.3.10-1",
    "remark": u"（2）P130"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_outlet_diffuser_tube",
    "name": u"1个出口扩散管",
    "symbol": u"ζ2",
    "unit": u"",
    "calculate": u"",
    "remark": u"（2）P136"
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "induced_draft_45_90_slow_turn_elbow",
    "name": u"1个45度缓转弯头（钢烟道）/1个90度缓转弯头（砖烟道）",
    "symbol": u"ζ3",
    "unit": u"",
    "calculate": u"ζ3=ζu",
    "remark": u"（2）P111"
}, {
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
}, {
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
}, {
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
}, {
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
}, {
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
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "brick_chimney_inlet",
    "name": u"砖烟道烟囱入口",
    "symbol": u"ζ4",
    "unit": u"",
    "calculate": u"表7.4.1",
    "remark": u"（2）P147"
}, {
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
}, {
    "module_name": "GPG_SmokeResistance",
    "name_eng": "smoke_chimney_total_resistance",
    "name": u"烟道总阻力",
    "symbol": u"△Pz",
    "unit": u"Pa",
    "calculate": u"△Pz1+△Pz2+△Pz3",
    "remark": u""
}]

# 煤气发电 烟风系统
GPGGasAirSys_data = [{
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_condition_temperature",
        "name": u"工况温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_condition_flux",
        "name": u"工况流量",
        "symbol": u"qv",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_standard_temperature",
        "name": u"标况温度",
        "symbol": u"t0",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_standard_pressure",
        "name": u"标况压力",
        "symbol": u"p0",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "c2s_standard_flux",
        "name": u"标况流量",
        "symbol": u"qv0",
        "unit": u"Nm³/h",
        "calculate": u"qv0=qv*(p/p0)*((t0+273)/(t+273))",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_standard_temperature",
        "name": u"标况温度",
        "symbol": u"t0",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_standard_pressure",
        "name": u"标况压力",
        "symbol": u"p0",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_standard_flux",
        "name": u"标况流量",
        "symbol": u"qv0",
        "unit": u"Nm³/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_condition_temperature",
        "name": u"工况温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "s2c_condition_flux",
        "name": u"工况流量",
        "symbol": u"qv",
        "unit": u"m³/h",
        "calculate": u"qv=qv0*(p0/p)*((t+273)/(t0+273))",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_air_temperature",
        "name": u"空气温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"设计值"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_wind_resistance",
        "name": u"风阻力",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u"设计值"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p0",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_condition_smoke_flux",
        "name": u"烟风流量（工况）",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"注意锅炉厂是否含有储备系数"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_temperature",
        "name": u"风机温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_total_pressure",
        "name": u"风机全压",
        "symbol": u"p1",
        "unit": u"pa",
        "calculate": u"p1=p*(101325/p0)*((t+273)/(t1+273))",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_selected_total_pressure",
        "name": u"风机选用全压",
        "symbol": u"p2",
        "unit": u"",
        "calculate": u"",
        "remark": u"1.10~1.15"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_selected_flux",
        "name": u"风机选用流量",
        "symbol": u"q2",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"1.05~1.2"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_pressure_efficiency",
        "name": u"风机全压头效率",
        "symbol": u"η",
        "unit": u"",
        "calculate": u"",
        "remark": u"0.9"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_transmission_efficiency",
        "name": u"机械传动效率",
        "symbol": u"η1",
        "unit": u"",
        "calculate": u"",
        "remark": u"直联时1.0，联轴器连接时0.95~0.98，三角皮带传动0.9~0.95，平皮带传动时0.8"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_motor_efficiency",
        "name": u"电动机效率",
        "symbol": u"ηd",
        "unit": u"",
        "calculate": u"",
        "remark": u"0.9"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_fan_shaft_power",
        "name": u"风机轴功率",
        "symbol": u"P'",
        "unit": u"kw",
        "calculate": u"P'=p2*q2/η",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_motor_safe_margin",
        "name": u"电机安全裕量",
        "symbol": u"K",
        "unit": u"",
        "calculate": u"",
        "remark": u"1.1"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_motor_power",
        "name": u"电机功率",
        "symbol": u"P",
        "unit": u"kw",
        "calculate": u"P=K*P'/ηd",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_specification_power",
        "name": u"选用规格-功率",
        "symbol": u"50%定频",
        "unit": u"一个",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "blower_specification_flux",
        "name": u"选用规格-流量",
        "symbol": u"50%定频",
        "unit": u"一个",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_smoke_temperature",
        "name": u"烟风温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"设计值"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_total_pressure",
        "name": u"全压",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u"烟道总阻力"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p0",
        "unit": u"pa",
        "calculate": u"",
        "remark": u"根据当地海拔按表选取"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_condition_smoke_flux",
        "name": u"烟风流量（工况）",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"标---工况之间转换"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_temperature",
        "name": u"风机温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"风机铭牌标定温度，一般为165/200℃"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_smoke_density",
        "name": u"烟气密度",
        "symbol": u"ρ0",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"取一般烟气平均密度"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_total_pressure",
        "name": u"风机全压",
        "symbol": u"p1",
        "unit": u"pa’",
        "calculate": u"p1=p*(101325/p0)*((t+273)/(t1+273))",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_selected_total_pressure",
        "name": u"风机选用全压",
        "symbol": u"p2",
        "unit": u"",
        "calculate": u"",
        "remark": u"选用系数：1.10~1.15"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_selected_flux",
        "name": u"风机选用流量",
        "symbol": u"q2",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"选用系数：1.05~1.2"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_efficiency",
        "name": u"风机效率",
        "symbol": u"η",
        "unit": u"",
        "calculate": u"",
        "remark": u"全压头时效率，一般风机0.6，高效风机为0.9"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_transmission_efficiency",
        "name":  u"机械传动效率",
        "symbol": u"η1",
        "unit": u"",
        "calculate": u"",
        "remark": u"直联时1.0，联轴器连接时0.95~0.98，三角皮带传动0.9~0.95，平皮带传动时0.8"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_motor_efficiency",
        "name": u"电机效率",
        "symbol": u"ηd",
        "unit": u"",
        "calculate": u"",
        "remark": u"电动机效率0.9"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_fan_shaft_power",
        "name": u"风机轴功率",
        "symbol": u"P'",
        "unit": u"kw",
        "calculate": u"P'=p2*q2/η",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_motor_safe_margin",
        "name": u"电机安全裕量",
        "symbol": u"K",
        "unit": u"",
        "calculate": u"",
        "remark": u"1.1"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_motor_power",
        "name": u"电机功率",
        "symbol": u"P",
        "unit": u"kw",
        "calculate": u"P=K*P'/ηd",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_specification_power",
        "name": u"选用规格-功率",
        "symbol": u"50%定频",
        "unit": u"一个",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "induced_specification_flux",
        "name": u"选用规格-流量",
        "symbol": u"50%定频",
        "unit": u"一个",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"煤气管道15-20"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_calculated_diameter",
        "name": u"计算管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_selected_diameter",
        "name": u"选取直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "gas_tube_selected_thickness",
        "name": u"选取壁厚",
        "symbol": u"t",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"冷风道流速10-12"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_calculated_diameter",
        "name": u"计算当量管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_length",
        "name": u"长",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "coldwind_tube_specification",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"热风道流速15-25"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_calculated_diameter",
        "name": u"计算当量管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_length",
        "name": u"长",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "hotwind_tube_specification",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"烟道流速10-15"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_calculated_diameter",
        "name": u"计算当量管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_length",
        "name": u"长",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "total_smoke_tube_specification",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"烟道流速10-15"
    }, {
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
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_calculated_diameter",
        "name": u"计算当量管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_length",
        "name": u"长",
        "symbol": u"L",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_width",
        "name": u"宽",
        "symbol": u"B",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_smoke_tube_specification",
        "name": u"选用规格",
        "symbol": u"",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"热风道流速15-25"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_calculated_diameter",
        "name": u"计算管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_selected_diameter",
        "name": u"选取直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "main_hotwind_tube_selected_thickness",
        "name": u"选取壁厚",
        "symbol": u"t",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_medium_flux",
        "name": u"介质流量",
        "symbol": u"q",
        "unit": u"m³/h",
        "calculate": u"",
        "remark": u"计算书"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_medium_temperature",
        "name": u"介质温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_flow_velocity",
        "name": u"流速",
        "symbol": u"v",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"热风道流速15-25"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_calculated_cross_sectional_area",
        "name": u"计算截面积",
        "symbol": u"A",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_calculated_diameter",
        "name": u"计算管道直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_selected_diameter",
        "name": u"选取直径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "branch_hotwind_tube_selected_thickness",
        "name": u"选取壁厚",
        "symbol": u"t",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_height",
        "name": u"烟囱高度",
        "symbol": u"H",
        "unit": u"m",
        "calculate": u"",
        "remark": u"假定30、45、60、80、100、120、150、180"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "local_atmosphere",
        "name": u"当地大气压",
        "symbol": u"p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "standard_air_density",
        "name": u"标态下空气密度",
        "symbol": u"ρ0",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"平均值"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "standard_average_smoke_density",
        "name": u"标态下平均烟气密度",
        "symbol": u"ρ1",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"平均值"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "standard_calculated_smoke_density",
        "name": u"标态下计算烟气密度",
        "symbol": u"ρ2",
        "unit": u"kg/m³",
        "calculate": u"",
        "remark": u"计算值"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "outdoor_air_temperature",
        "name": u"室外空气温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"给定"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_inlet_temperature",
        "name": u"烟囱进口处烟温",
        "symbol": u"t0",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"锅炉排烟温度"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_temperature_drop_per_meter",
        "name": u"烟囱每米高度的温度降",
        "symbol": u"t'",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"砖砌温降0.1℃/m；钢板0.5℃/m"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_average_temperature",
        "name": u"烟囱内平均温度",
        "symbol": u"t2",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_draft",
        "name": u"烟囱抽力",
        "symbol": u"S",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "smoke_amount",
        "name": u"烟气量",
        "symbol": u"q",
        "unit": u"Nm³/h",
        "calculate": u"",
        "remark": u"燃烧计算"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_temperature",
        "name": u"烟囱出口温度",
        "symbol": u"t",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"抽力计算"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_flow",
        "name": u"烟囱出口流速",
        "symbol": u"Wo",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u"根据温度和烟囱高度选取12-20，低负荷时2.5-3"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_inner_diameter",
        "name": u"烟囱出口内径",
        "symbol": u"d",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_selected_inner_diameter",
        "name": u"选取烟囱出口内径",
        "symbol": u"d'",
        "unit": u"mm",
        "calculate": u"",
        "remark": u"选取"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_experience_base_diameter",
        "name": u"经验烟囱基础内径",
        "symbol": u"d'’",
        "unit": u"mm",
        "calculate": u"",
        "remark": u"坡度小于2%"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "low_load_smoke_amount",
        "name": u"低负荷下烟气量",
        "symbol": u"q1",
        "unit": u"Nm³/h",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "low_load_smoke_temperature",
        "name": u"低负荷下排烟温度",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "low_load_flow_30_percent",
        "name": u"30%低负荷校核流速",
        "symbol": u"t1",
        "unit": u"℃",
        "calculate": u"",
        "remark": u"不低于2.5"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_resistance_coefficient",
        "name": u"烟囱阻力系数",
        "symbol": u"r",
        "unit": u"",
        "calculate": u"",
        "remark": u"一般0.04"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_average_velocity",
        "name": u"烟囱内平均流速",
        "symbol": u"Wo",
        "unit": u"m/s",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_average_diameter",
        "name": u"烟囱平均直径",
        "symbol": u"d'’",
        "unit": u"m",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_friction_resistance",
        "name": u"烟囱摩擦阻力",
        "symbol": u"△p1",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_resistance_coefficient",
        "name": u"烟囱出口阻力系数",
        "symbol": u"§",
        "unit": u"pa",
        "calculate": u"",
        "remark": u"一般取1"
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_outlet_resistance",
        "name": u"烟囱出口阻力",
        "symbol": u"△p2",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }, {
        "module_name": "GPG_GasAirSystem",
        "name_eng": "chimney_total_resistance",
        "name": u"烟囱总阻力",
        "symbol": u"△p",
        "unit": u"pa",
        "calculate": u"",
        "remark": u""
    }
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
        data = [questionnaire_data, GPGBoilerOfPTS_data, GPGGasAirSys_data,
                GPGSmokeResistance_data, GPGWindResistance_data,
                GPGCirculatingWaterSystem_data, GPGSmokeAirCalculate_data]

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
