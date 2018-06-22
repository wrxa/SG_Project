# -*- coding: utf-8 -*-
from app import db


class Ccpp_ccpp(db.Model):
    # 表名
    __tablename__ = 'ccpp_ccpp'
    __table_args__ = {'comment': u'燃气蒸汽联合循环-余热锅炉计算数据'}
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    # 燃气低位发热量:隐藏值
    low_calorific_gas_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气低位发热量")
    # 燃气低位发热量:隐藏值
    low_calorific_gas_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 燃机id:隐藏值
    engine_id_design = db.Column(db.Integer)
    # 燃机id:隐藏值
    engine_id_check = db.Column(db.Integer)
    # 燃机个数:隐藏值
    engine_num_design = db.Column(db.Integer, comment=u"燃机数量")
    # 燃机个数:隐藏值
    engine_num_check = db.Column(db.Integer)

    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
  
    # 需求功率设计值
    engine_demand_power_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"需求功率")
    # 需求功率:校核值
    engine_demand_power_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机型号设计值
    engine_model_design = db.Column(db.String(50), comment=u"燃机型号")
    # 燃机型号:校核值
    engine_model_check = db.Column(db.String(50))

    # 燃机功率设计值
    engine_power_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃机功率")
    # 燃机功率:校核值
    engine_power_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机热耗率设计值
    engine_heat_consmption_rate_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃机热耗率")
    # 燃机热耗率:校核值
    engine_heat_consmption_rate_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机效率设计值
    engine_efficiency_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃机效率")
    # 燃机效率:校核值
    engine_efficiency_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机压比设计值
    engine_pressure_ratio_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃机压比")
    # 燃机压比:校核值
    engine_pressure_ratio_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 单机天燃气耗量设计值
    individual_gas_consumption_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单机天燃气耗量")
    # 单机天燃气耗量:校核值high_gas_prodction_design
    individual_gas_consumption_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 排烟温度设计值
    engine_exhuast_gas_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排烟温度")
    # 排烟温度:校核值
    engine_exhuast_gas_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 排烟流量设计值
    engine_exhuast_gas_flux_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排烟流量")
    # 排烟流量:校核值
    engine_exhuast_gas_flux_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 排烟能量设计值
    engine_exhuast_gas_energy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排烟能量")
    # 排烟能量:校核值
    engine_exhuast_gas_energy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 锅炉补然否设计值
    boiler_is_afterburning_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 锅炉补然否:校核值
    boiler_is_afterburning_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 锅炉补燃量设计值boiler_afterburning_amont
    boiler_afterburning_amount_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"补燃量")
    # 锅炉补燃量:校核值
    boiler_afterburning_amount_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 补燃后排烟能量设计值boiler_afterburning_exhuast_energy
    boiler_afterburning_exhuast_energy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"补燃后排烟能量")
    # 补燃后排烟能量:校核值
    boiler_afterburning_exhuast_energy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 补燃后排烟温度设计值
    boiler_afterburning_exhuast_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"补燃后排烟温度")
    # 补燃后排烟温度:校核值
    boiler_afterburning_exhuast_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 锅炉采用单压/双压设计值
    boiler_single_or_dula_pressure_design = db.Column(db.String(20), comment=u"锅炉形式")
    # 锅炉采用单压/双压:校核值
    boiler_single_or_dula_pressure_check = db.Column(db.String(20))

    # 燃机排烟流量设计值
    high_engine_exhuast_gas_flux_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压燃机排烟流量")
    # 燃机排烟流量:校核值
    high_engine_exhuast_gas_flux_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机排烟温度设计值
    high_engine_exhuast_gas_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压燃机排烟温度")
    # 燃机排烟温度:校核值
    high_engine_exhuast_gas_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机排烟能量设计值
    high_engine_exhuast_gas_energy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压燃机排烟能量")
    # 燃机排烟能量:校核值
    high_engine_exhuast_gas_energy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 锅炉效率设计值
    high_boiler_efficiency_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压锅炉效率")
    # 锅炉效率:校核值
    high_boiler_efficiency_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 主蒸汽压力设计值
    high_steam_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压主蒸汽压力")
    # 主蒸汽压力:校核值
    high_steam_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 热端温差设计值
    high_terminal_temperature_difference_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压热端温差")
    # 热端温差:校核值
    high_terminal_temperature_difference_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 主蒸汽温度设计值
    high_steam_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压主蒸汽温度")
    # 主蒸汽温度:校核值high_evaporator_effluent_water_temperature
    high_steam_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 主蒸汽焓值设计值
    high_steam_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压主蒸汽焓值")
    # 主蒸汽焓值:校核值
    high_steam_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压汽包压力设计值
    high_drum_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压汽包压力")
    # 高压汽包压力:校核值
    high_drum_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压蒸发温度设计值
    high_evaporating_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压蒸发温度")
    # 高压蒸发温度:校核值
    high_evaporating_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压节点温度设计值
    high_node_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压节点温度")
    # 高压节点温度:校核值
    high_node_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压进蒸发器热水温度设计值
    high_evaporator_effluent_water_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压进蒸发器热水温度")
    # 高压进蒸发器热水温度:校核值
    high_evaporator_effluent_water_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压进蒸发器热水焓值设计值
    high_evaporator_effluent_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压进蒸发器热水焓值")
    # 高压进蒸发器热水焓值:校核值
    high_evaporator_effluent_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 接近点温差设计值
    high_proximity_temperature_difference_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压接近点温差")
    # 接近点温差:校核值
    high_proximity_temperature_difference_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压出蒸发器烟气温度设计值
    high_evaporator_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压出蒸发器烟气温度")
    # 高压出蒸发器烟气温度:校核值
    high_evaporator_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压出蒸发器烟气焓值设计值
    high_evaporator_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压出蒸发器烟气焓值")
    # 高压出蒸发器烟气焓值:校核值
    high_evaporator_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压出省煤器烟气温度设计值
    high_economizer_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压出省煤器烟气温度")
    # 高压出省煤器烟气温度:校核值
    high_economizer_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压出省煤器烟气焓值设计值
    high_economizer_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压出省煤器烟气焓值")
    # 高压出省煤器烟气焓值:校核值
    high_economizer_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压进省煤器热水温度设计值
    high_economizer_effluent_water_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压进省煤器热水温度")
    # 高压进省煤器热水温度:校核值
    high_economizer_effluent_water_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压进省煤器热水焓值设计值
    high_economizer_effluent_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压进省煤器热水焓值")
    # 高压进省煤器热水焓值:校核值
    high_economizer_effluent_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压产汽量设计值
    high_gas_production_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压产汽量")
    # 高压产汽量:校核值
    high_gas_production_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 排污率设计值
    high_blowdown_rate_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压排污率")
    # 排污率:校核值
    high_blowdown_rate_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水量设计值
    high_feedwater_amount_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压给水量")
    # 给水量:校核值
    high_feedwater_amount_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压出省煤器烟焓校核设计值
    high_economizer_effluent_smoke_enthalpy_verify_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压出省煤器烟焓校核")
    # 高压出省煤器烟焓校核:校核值
    high_economizer_effluent_smoke_enthalpy_verify_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压蒸发器出口蒸汽焓设计值
    high_evaporator_effluent_steam_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压蒸发器出口蒸汽焓")
    # 高压蒸发器出口蒸汽焓:校核值
    high_evaporator_effluent_steam_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压过热器出口烟焓设计值
    high_superheater_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压过热器出口烟焓")
    # 高压过热器出口烟焓:校核值
    high_superheater_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压过热器出口烟温设计值
    high_superheater_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压过热器出口烟温")
    # 高压过热器出口烟温:校核值
    high_superheater_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高压过热器出口烟焓校核设计值
    high_superheater_effluent_smoke_enthalpy_verify_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅高压过热器出口烟焓校核")
    # 高压过热器出口烟焓校核:校核值
    high_superheater_effluent_smoke_enthalpy_verify_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压汽包压力设计值
    low_drum_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压汽包压力")
    # 低压汽包压力:校核值
    low_drum_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 进烟温度设计值
    low_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压进烟温度")
    # 进烟温度:校核值
    low_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 进烟焓设计值
    low_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压进烟焓")
    # 进烟焓:校核值
    low_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热蒸汽温度设计值
    low_superheat_steam_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压过热蒸汽温度")
    # 低压过热蒸汽温度:校核值
    low_superheat_steam_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热蒸汽温度修正:设计值
    low_superheat_steam_temperature_correct_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 低压过热蒸汽温度修正:校核值
    low_superheat_steam_temperature_correct_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 蒸汽焓值设计值
    low_steam_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅压出蒸发器蒸汽焓值")
    # 蒸汽焓值:校核值
    low_steam_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压蒸发温度设计值
    low_evaporat_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅压出蒸发器蒸发温度")
    # 低压蒸发温度:校核值
    low_evaporat_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压蒸发器出口蒸汽焓设计值
    low_evaporator_effluent_steam_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压蒸发器出口蒸汽焓")
    # 低压蒸发器出口蒸汽焓:校核值
    low_evaporator_effluent_steam_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 接近点温度设计值
    low_proximity_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅压出蒸发器接近点温度")
    # 接近点温度:校核值
    low_proximity_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进蒸发器热水温度设计值high_evaporator_efflent_smoke_temperature
    low_evaporator_effluent_water_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压进蒸发器热水温度")
    # 低压进蒸发器热水温度:校核值
    low_evaporator_effluent_water_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进蒸发器热水焓值设计值
    low_evaporator_effluent_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压进蒸发器热水焓值")
    # 低压进蒸发器热水焓值:校核值
    low_evaporator_effluent_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压节点温度设计值
    low_node_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅压出蒸发器节点温度")
    # 低压节点温度:校核值
    low_node_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压出蒸发器排烟温度设计值
    low_evaporator_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压出蒸发器排烟温度")
    # 低压出蒸发器排烟温度:校核值
    low_evaporator_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压出蒸发器排烟焓值设计值
    low_evaporator_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压出蒸发器排烟焓值")
    # 低压出蒸发器排烟焓值:校核值
    low_evaporator_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压产汽量设计值
    low_gas_production_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅压出蒸发器产汽量")
    # 低压产汽量:校核值
    low_gas_production_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热器出口烟焓设计值
    low_superheater_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压过热器出口烟焓")
    # 低压过热器出口烟焓:校核值
    low_superheater_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热器出口烟温设计值
    low_superheater_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压过热器出口烟温")
    # 低压过热器出口烟温:校核值
    low_superheater_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热器出口烟焓校核设计值
    low_superheater_effluent_smoke_enthalpy_verify_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压过热器出口烟焓校核")
    # 低压过热器出口烟焓校核:校核值
    low_superheater_effluent_smoke_enthalpy_verify_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压省煤器压力设计值
    low_economizer_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压省煤器压力")
    # 低压省煤器压力:校核值
    low_economizer_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进省煤器热水温度设计值
    low_economizer_effluent_water_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压进省煤器热水温度")
    # 低压进省煤器热水温度:校核值
    low_economizer_effluent_water_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进省煤器热水焓值设计值
    low_economizer_effluent_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压进省煤器热水焓值")
    # 低压进省煤器热水焓值:校核值
    low_economizer_effluent_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水温度设计值
    low_feedwater_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压省煤器给水温度")
    # 给水温度:校核值
    low_feedwater_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水焓值设计值
    low_feedwater_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压省煤器给水焓值")
    # 给水焓值:校核值
    low_feedwater_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压省煤器排烟焓值设计值
    low_economizer_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压省煤器排烟焓值")
    # 低压省煤器排烟焓值:校核值
    low_economizer_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压省煤器排烟温度设计值
    low_economizer_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压省煤器排烟温度")
    # 低压省煤器排烟温度:校核值
    low_economizer_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压省煤器烟焓校核设计值
    low_economizer_effluent_smoke_enthalpy_verify_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压省煤器烟焓校核")
    # 低压省煤器烟焓校核:校核值
    low_economizer_effluent_smoke_enthalpy_verify_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水流量设计值
    low_feedwater_flux_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"双锅低压省煤器给水流量")
    # 给水流量:校核值
    low_feedwater_flux_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机排烟流量设计值
    sp_engine_exhuast_gas_flux_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅燃机排烟流量")
    # 燃机排烟流量:校核值
    sp_engine_exhuast_gas_flux_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机排烟温度设计值sp_low_economizer_efflent_smoke_temperature
    sp_engine_exhuast_gas_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅燃机排烟温度")
    # 燃机排烟温度:校核值
    sp_engine_exhuast_gas_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃机排烟能量设计值
    sp_exhuast_gas_energy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅燃机排烟能量")
    # 燃机排烟能量:校核值
    sp_exhuast_gas_energy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 锅炉效率设计值
    sp_boiler_efficiency_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅锅炉效率")
    # 锅炉效率:校核值
    sp_boiler_efficiency_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 主蒸汽压力设计值
    sp_steam_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅主蒸汽压力")
    # 主蒸汽压力:校核值
    sp_steam_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 主蒸汽温度设计值
    sp_steam_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅主蒸汽温度")
    # 主蒸汽温度:校核值
    sp_steam_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 热端温差设计值
    sp_terminal_temperature_difference_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅热端温差")
    # 热端温差:校核值
    sp_terminal_temperature_difference_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压汽包压力设计值
    sp_low_drum_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器汽包压力")
    # 低压汽包压力:校核值
    sp_low_drum_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进烟温度设计值
    sp_low_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器进烟温度")
    # 低压进烟温度:校核值
    sp_low_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进烟焓设计值
    sp_low_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器进烟焓")
    # 低压进烟焓:校核值
    sp_low_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热蒸汽温度设计值
    sp_low_superheat_steam_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器过热蒸汽温度")
    # 低压过热蒸汽温度:校核值
    sp_low_superheat_steam_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 蒸汽焓值设计值
    sp_low_steam_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器蒸汽焓值")
    # 蒸汽焓值:校核值
    sp_low_steam_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 蒸发温度设计值
    sp_low_evaporating_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器蒸发温度")
    # 蒸发温度:校核值
    sp_low_evaporating_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压蒸发器出口蒸汽焓设计值
    sp_low_evaporator_effluent_steam_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器出口蒸汽焓")
    # 低压蒸发器出口蒸汽焓:校核值
    sp_low_evaporator_effluent_steam_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 接近点温度设计值
    sp_low_proximity_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器接近点温度")
    # 接近点温度:校核值
    sp_low_proximity_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进蒸发器热水温度设计值
    sp_low_evaporator_effluent_water_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压进蒸发器热水温度")
    # 低压进蒸发器热水温度:校核值
    sp_low_evaporator_effluent_water_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进蒸发器热水焓值设计值sp_low_sperheater_effluent_smoke_enthalpy_verify
    sp_low_evaporator_effluent_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压进蒸发器热水焓值")
    # 低压进蒸发器热水焓值:校核值
    sp_low_evaporator_effluent_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压节点温度设计值
    sp_low_node_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器节点温度")
    # 低压节点温度:校核值
    sp_low_node_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压出蒸发器排烟温度设计值sp_low_economizer_efflent_smoke_temperature
    sp_low_evaporator_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压出蒸发器排烟温度")
    # 低压出蒸发器排烟温度:校核值
    sp_low_evaporator_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压出蒸发器排烟焓值设计值
    sp_low_evaporator_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压出蒸发器排烟焓值")
    # 低压出蒸发器排烟焓值:校核值sp_low_evaporator_effluent_smoke_enthalpy
    sp_low_evaporator_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压产汽量设计值
    sp_low_gas_production_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压蒸发器产汽量")
    # 低压产汽量:校核值sp_low_gas_prodction
    sp_low_gas_production_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热器出口烟焓设计值sp_low_sperheater_effluent_smoke_enthalpy_verify
    sp_low_superheater_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压过热器出口烟焓")
    # 低压过热器出口烟焓:校核值
    sp_low_superheater_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热器出口烟温设计值
    sp_low_superheater_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压过热器出口烟温")
    # 低压过热器出口烟温:校核值
    sp_low_superheater_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压过热器出口烟焓校核设计值
    sp_low_superheater_effluent_smoke_enthalpy_verify_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压过热器出口烟焓校核")
    # 低压过热器出口烟焓校核:校核值
    sp_low_superheater_effluent_smoke_enthalpy_verify_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压省煤器压力设计值
    sp_low_economizer_pressure_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压省煤器压力")
    # 低压省煤器压力:校核值
    sp_low_economizer_pressure_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进省煤器热水温度设计值
    sp_low_economizer_effluent_water_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压进省煤器热水温度")
    # 低压进省煤器热水温度:校核值
    sp_low_economizer_effluent_water_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压进省煤器热水焓值设计值
    sp_low_economizer_effluent_water_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压进省煤器热水焓值")
    # 低压进省煤器热水焓值:校核值
    sp_low_economizer_effluent_water_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水温度设计值
    sp_low_feedwater_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压省煤器给水温度")
    # 给水温度:校核值
    sp_low_feedwater_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水焓值设计值
    sp_low_feedwater_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压省煤器给水焓值")
    # 给水焓值:校核值
    sp_low_feedwater_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压省煤器排烟焓值设计值
    sp_low_economizer_effluent_smoke_enthalpy_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压省煤器排烟焓值")
    # 低压省煤器排烟焓值:校核值
    sp_low_economizer_effluent_smoke_enthalpy_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压省煤器排烟温度设计值sp_low_economizer_efflent_smoke_temperature
    sp_low_economizer_effluent_smoke_temperature_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压省煤器排烟温度")
    # 低压省煤器排烟温度:校核值
    sp_low_economizer_effluent_smoke_temperature_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 低压省煤器烟焓校核设计值sp_low_sperheater_inflent_smoke_enthalpy_verify
    sp_low_economizer_effluent_smoke_enthalpy_verify_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压省煤器烟焓校核")
    # 低压省煤器烟焓校核:校核值
    sp_low_economizer_effluent_smoke_enthalpy_verify_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 给水流量设计值
    sp_low_feedwater_flux_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"单锅低压省煤器给水流量")
    # 给水流量:校核值
    sp_low_feedwater_flux_check = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉排污率
    sp_h_blowdown_rate_design = db.Column(db.NUMERIC(precision=15, scale=5))

    # 根据id查找实体
    @staticmethod
    def search_ccpp_ccpp(plan_id):
        result = Ccpp_ccpp.query.filter_by(
            plan_id=plan_id).one_or_none()
        # 所有查询都应该返回深拷贝
        return result

    # 更新ccpp
    @staticmethod
    def updata_ccpp(ccpp):
        if ccpp.id is not None:
            try:
                db.session.add(ccpp)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("Error %s" % e)
                raise e
            finally:
                print("updata ccpp_ccpp<id=%s, > in updata" % (ccpp.id))
    
    # 根据plan_id删除实体
    @staticmethod
    def deleteByPlan_id(plan_id):
        ccpp_ccpp = Ccpp_ccpp.search_ccpp_ccpp(plan_id)
        try:
            db.session.delete(ccpp_ccpp)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete ccpp_ccpp<id=%s, > in database" % (ccpp_ccpp.id))
