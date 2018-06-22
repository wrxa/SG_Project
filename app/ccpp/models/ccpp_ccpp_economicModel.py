# -*- coding: utf-8 -*-
from app import db


class Ccpp_ccpp_economic(db.Model):
    # 表名
    __tablename__ = 'ccpp_ccpp_economic'
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 能源天然气价格
    natural_gas_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"能源天然气价格")

    # 能源燃煤价格
    coal_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"能源燃煤价格")

    # 能源水价格
    water_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"能源水价格")

    # 能源电价格
    electricity_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"能源电价格")

    # 能源其他
    energy_priceother = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"能源其他")

    # 供能电价格
    energy_supply_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供能电价格")

    # 供能热水价格
    energy_supply_water_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供能热水价格")

    # 供能采暖价格
    energy_supply_for_heating = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供能采暖价格")

    # 供能制冷价格
    energy_supply_refrigeration_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供能制冷价格")

    # 供能其他
    other_energy_supply = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供能其他")

    # 供能蒸汽价格
    energy_supply_steam_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供能蒸汽价格")

    # 供电收入增值税率17%
    value_added_tax_rate_power_supply = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供电收入增值税率17%")

    # 供热水收入增值税率11%
    value_added_tax_rate_heating_water = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供热水收入增值税率11%")

    # 供暖收入增值税率11%
    heating_income_vat = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供暖收入增值税率11%")

    # 供冷收入增值税率11%
    vat_for_cooling_income = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"供冷收入增值税率11%")

    # 63供蒸汽收入增值税11%
    vat_for_steam_income = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃气费用增值税率13%
    gas_cost_value_added_tax_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气费用增值税率13%")

    # 燃煤费用增值税率13%
    coal_cost_value_added_tax_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃煤费用增值税率13%")

    # 电力成本增值税率17%
    power_cost_value_added_tax_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电力成本增值税率17%")

    # 耗水成本增值税率13%
    water_consumption_cost_value_added_tax_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"耗水成本增值税率13%")

    # 折旧摊销年限
    depreciation_amortization_years = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"折旧摊销年限")

    # 税后利润增值税率
    post_tax_profit_vat = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"税后利润增值税率")

    # 资本金占总投资百分比
    percentage_capital_total_investment = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"资本金占总投资百分比")

    # 银行利息利率
    interest_rate_bank_interest = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"银行利息利率")

    # 收购成本-万元
    purchase_cost = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"收购成本-万元")

    # 新增投资-万元
    new_investment = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"新增投资-万元")

    # 资本金-万元(占总投资30%）
    capital = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"资本金-万元(占总投资30%）")

    # 银行借款-万元
    bank_loan = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"银行借款-万元")

    # 动态投资回收期-年(不含建设期)
    dynamic_recovery_period = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"动态投资回收期-年(不含建设期)")

    # 总投资收益率
    total_return_investment = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总投资收益率")

    # NpV-万元
    npv = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"NpV-万元")

    # iRR(全投资内部收益率)
    irr = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"iRR(全投资内部收益率)")

    # 全投资收益率（集团规定）计算年数
    full_investment_yield_year = db.Column(db.String(50))

    # 全投资收益率（集团规定）
    full_investment_yield = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"全投资收益率（集团规定）")

    # 第1年供电量-万kWh/a
    power_supply_capacity_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供电量-万kWh/a")

    # 第1年供热水-万t/a
    energy_supply_for_heating_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供热水-万t/a")

    # 第1年供暖-万GJ
    energy_supply_heating_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供暖-万GJ")

    # 第1年供冷-万GJ
    energy_supply_for_cooling_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供冷-万GJ")

    # 第1年产汽量-万吨
    vapour_production_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年产汽量-万吨")

    # 第1年其他
    income_other_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年其他")

    # 第1年供电收入-万元/a
    power_supply_income_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供电收入-万元/a")

    # 第1年供热水收入-万元/a
    heating_water_income_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供热水收入-万元/a")

    # 第1年供暖收入-万元/a
    heating_income_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供暖收入-万元/a")

    # 第1年供冷收入-万元/a
    cooling_income_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供冷收入-万元/a")

    # 第1年供蒸汽收入-万元/a(增值税11%)
    steam_supply_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年供蒸汽收入-万元/a(增值税11%)")

    # 第1年其他-万元/a(不含税)(政府补贴)
    income_otherother_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年其他-万元/a(不含税)(政府补贴)")

    # 第1年燃气耗量-万m³/a
    gas_consumption_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年燃气耗量-万m³/a")

    # 第1年燃煤耗量-万t/a
    coal_consumption_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年燃煤耗量-万t/a")

    # 第1年耗电量-万kWh/a
    power_consumption_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年耗电量-万kWh/a")

    # 第1年耗水量-万t/a
    water_consumption_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年耗水量-万t/a")

    # 第1年燃气费用-万元/a
    gas_cost_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年燃气费用-万元/a")

    # 第1年燃煤费用-万元/a
    coal_cost_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年燃煤费用-万元/a")

    # 第1年电力成本-万元/a
    power_cost_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年电力成本-万元/a")

    # 第1年耗水成本-万元/a
    cost_of_water_consumption_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年耗水成本-万元/a")

    # 第1年材料费用-万元/a
    material_cost_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年材料费用-万元/a")

    # 第1年维护费用-万元/a
    maintenance_cost_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年维护费用-万元/a")

    # 第1年人工费用-万元/a
    artificial_cost_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年人工费用-万元/a")

    # 第1年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年其他-万元/a(包括土地租金及容量费)")

    # 第1年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第1年总销售额-万元
    total_sales_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年总销售额-万元")

    # 第1年总成本-万元
    total_cost_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年总成本-万元")

    # 第1年税前利润-万元
    pre_tax_profit_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年税前利润-万元")

    # 第1年税后利润-万元(享受三免三减半）
    post_tax_profit_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年税后利润-万元(享受三免三减半）")

    # 第1年经营现金流-万元
    cash_flow_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年经营现金流-万元")

    # 第1年银行借款余额-万元
    bank_loan_balance_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年银行借款余额-万元")

    # 第1年银行利息-万元(利率7.5%)
    bank_interest_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年银行利息-万元(利率7.5%)")

    # 第1年还款计划-万元
    repayment_plan_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年还款计划-万元")

    # 第1年净现金流-万元
    net_cash_flow_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年净现金流-万元")

    # 第1年累计现金流-万元
    cumulative_cash_flow_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第1年累计现金流-万元")

    # 第2年供电量-万kWh/a
    power_supply_capacity_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供电量-万kWh/a")

    # 第2年供热水-万t/a
    energy_supply_for_heating_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供热水-万t/a")

    # 第2年供暖-万GJ
    energy_supply_heating_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供暖-万GJ")

    # 第2年供冷-万GJ
    energy_supply_for_cooling_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供冷-万GJ")

    # 第2年产汽量-万吨
    vapour_production_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年产汽量-万吨")

    # 第2年其他
    income_other_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年其他")

    # 第2年供电收入-万元/a
    power_supply_income_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供电收入-万元/a")

    # 第2年供热水收入-万元/a
    heating_water_income_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供热水收入-万元/a")

    # 第2年供暖收入-万元/a
    heating_income_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供暖收入-万元/a")

    # 第2年供冷收入-万元/a
    cooling_income_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供冷收入-万元/a")

    # 第2年供蒸汽收入-万元/a(增值税11%)
    steam_supply_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年供蒸汽收入-万元/a(增值税11%)")

    # 第2年其他-万元/a(不含税)(政府补贴)
    income_otherother_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年其他-万元/a(不含税)(政府补贴)")

    # 第2年燃气耗量-万m³/a
    gas_consumption_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年燃气耗量-万m³/a")

    # 第2年燃煤耗量-万t/a
    coal_consumption_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年燃煤耗量-万t/a")

    # 第2年耗电量-万kWh/a
    power_consumption_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年耗电量-万kWh/a")

    # 第2年耗水量-万t/a
    water_consumption_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年耗水量-万t/a")

    # 第2年燃气费用-万元/a
    gas_cost_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年燃气费用-万元/a")

    # 第2年燃煤费用-万元/a
    coal_cost_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年燃煤费用-万元/a")

    # 第2年电力成本-万元/a
    power_cost_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年电力成本-万元/a")

    # 第2年耗水成本-万元/a
    cost_of_water_consumption_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年耗水成本-万元/a")

    # 第2年材料费用-万元/a
    material_cost_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年材料费用-万元/a")

    # 第2年维护费用-万元/a
    maintenance_cost_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年维护费用-万元/a")

    # 第2年人工费用-万元/a
    artificial_cost_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年人工费用-万元/a")

    # 第2年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年其他-万元/a(包括土地租金及容量费)")

    # 第2年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第2年总销售额-万元
    total_sales_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年总销售额-万元")

    # 第2年总成本-万元
    total_cost_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年总成本-万元")

    # 第2年税前利润-万元
    pre_tax_profit_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年税前利润-万元")

    # 第2年税后利润-万元(享受三免三减半）
    post_tax_profit_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年税后利润-万元(享受三免三减半）")

    # 第2年经营现金流-万元
    cash_flow_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年经营现金流-万元")

    # 第2年银行借款余额-万元
    bank_loan_balance_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年银行借款余额-万元")

    # 第2年银行利息-万元(利率7.5%)
    bank_interest_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年银行利息-万元(利率7.5%)")

    # 第2年还款计划-万元
    repayment_plan_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年还款计划-万元")

    # 第2年净现金流-万元
    net_cash_flow_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年净现金流-万元")

    # 第2年累计现金流-万元
    cumulative_cash_flow_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第2年累计现金流-万元")

    # 第3年供电量-万kWh/a
    power_supply_capacity_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供电量-万kWh/a")

    # 第3年供热水-万t/a
    energy_supply_for_heating_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供热水-万t/a")

    # 第3年供暖-万GJ
    energy_supply_heating_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供暖-万GJ")

    # 第3年供冷-万GJ
    energy_supply_for_cooling_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供冷-万GJ")

    # 第3年产汽量-万吨
    vapour_production_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年产汽量-万吨")

    # 第3年其他
    income_other_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年其他")

    # 第3年供电收入-万元/a
    power_supply_income_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供电收入-万元/a")

    # 第3年供热水收入-万元/a
    heating_water_income_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供热水收入-万元/a")

    # 第3年供暖收入-万元/a
    heating_income_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供暖收入-万元/a")

    # 第3年供冷收入-万元/a
    cooling_income_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供冷收入-万元/a")

    # 第3年供蒸汽收入-万元/a(增值税11%)
    steam_supply_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年供蒸汽收入-万元/a(增值税11%)")

    # 第3年其他-万元/a(不含税)(政府补贴)
    income_otherother_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年其他-万元/a(不含税)(政府补贴)")

    # 第3年燃气耗量-万m³/a
    gas_consumption_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年燃气耗量-万m³/a")

    # 第3年燃煤耗量-万t/a
    coal_consumption_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年燃煤耗量-万t/a")

    # 第3年耗电量-万kWh/a
    power_consumption_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年耗电量-万kWh/a")

    # 第3年耗水量-万t/a
    water_consumption_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年耗水量-万t/a")

    # 第3年燃气费用-万元/a
    gas_cost_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年燃气费用-万元/a")

    # 第3年燃煤费用-万元/a
    coal_cost_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年燃煤费用-万元/a")

    # 第3年电力成本-万元/a
    power_cost_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年电力成本-万元/a")

    # 第3年耗水成本-万元/a
    cost_of_water_consumption_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年耗水成本-万元/a")

    # 第3年材料费用-万元/a
    material_cost_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年材料费用-万元/a")

    # 第3年维护费用-万元/a
    maintenance_cost_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年维护费用-万元/a")

    # 第3年人工费用-万元/a
    artificial_cost_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年人工费用-万元/a")

    # 第3年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年其他-万元/a(包括土地租金及容量费)")

    # 第3年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第3年总销售额-万元
    total_sales_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年总销售额-万元")

    # 第3年总成本-万元
    total_cost_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年总成本-万元")

    # 第3年税前利润-万元
    pre_tax_profit_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年税前利润-万元")

    # 第3年税后利润-万元(享受三免三减半）
    post_tax_profit_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年税后利润-万元(享受三免三减半）")

    # 第3年经营现金流-万元
    cash_flow_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年经营现金流-万元")

    # 第3年银行借款余额-万元
    bank_loan_balance_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年银行借款余额-万元")

    # 第3年银行利息-万元(利率7.5%)
    bank_interest_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年银行利息-万元(利率7.5%)")

    # 第3年还款计划-万元
    repayment_plan_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年还款计划-万元")

    # 第3年净现金流-万元
    net_cash_flow_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年净现金流-万元")

    # 第3年累计现金流-万元
    cumulative_cash_flow_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第3年累计现金流-万元")

    # 第4年供电量-万kWh/a
    power_supply_capacity_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供电量-万kWh/a")

    # 第4年供热水-万t/a
    energy_supply_for_heating_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供热水-万t/a")

    # 第4年供暖-万GJ
    energy_supply_heating_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供暖-万GJ")

    # 第4年供冷-万GJ
    energy_supply_for_cooling_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供冷-万GJ")

    # 第4年产汽量-万吨
    vapour_production_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年产汽量-万吨")

    # 第4年其他
    income_other_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年其他")

    # 第4年供电收入-万元/a
    power_supply_income_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供电收入-万元/a")

    # 第4年供热水收入-万元/a
    heating_water_income_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供热水收入-万元/a")

    # 第4年供暖收入-万元/a
    heating_income_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供暖收入-万元/a")

    # 第4年供冷收入-万元/a
    cooling_income_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供冷收入-万元/a")

    # 第4年供蒸汽收入-万元/a(增值税11%)
    steam_supply_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年供蒸汽收入-万元/a(增值税11%)")

    # 第4年其他-万元/a(不含税)(政府补贴)
    income_otherother_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年其他-万元/a(不含税)(政府补贴)")

    # 第4年燃气耗量-万m³/a
    gas_consumption_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年燃气耗量-万m³/a")

    # 第4年燃煤耗量-万t/a
    coal_consumption_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年燃煤耗量-万t/a")

    # 第4年耗电量-万kWh/a
    power_consumption_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年耗电量-万kWh/a")

    # 第4年耗水量-万t/a
    water_consumption_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年耗水量-万t/a")

    # 第4年燃气费用-万元/a
    gas_cost_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年燃气费用-万元/a")

    # 第4年燃煤费用-万元/a
    coal_cost_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年燃煤费用-万元/a")

    # 第4年电力成本-万元/a
    power_cost_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年电力成本-万元/a")

    # 第4年耗水成本-万元/a
    cost_of_water_consumption_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年耗水成本-万元/a")

    # 第4年材料费用-万元/a
    material_cost_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年材料费用-万元/a")

    # 第4年维护费用-万元/a
    maintenance_cost_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年维护费用-万元/a")

    # 第4年人工费用-万元/a
    artificial_cost_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年人工费用-万元/a")

    # 第4年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年其他-万元/a(包括土地租金及容量费)")

    # 第4年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第4年总销售额-万元
    total_sales_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年总销售额-万元")

    # 第4年总成本-万元
    total_cost_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年总成本-万元")

    # 第4年税前利润-万元
    pre_tax_profit_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年税前利润-万元")

    # 第4年税后利润-万元(享受三免三减半）
    post_tax_profit_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年税后利润-万元(享受三免三减半）")

    # 第4年经营现金流-万元
    cash_flow_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年经营现金流-万元")

    # 第4年银行借款余额-万元
    bank_loan_balance_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年银行借款余额-万元")

    # 第4年银行利息-万元(利率7.5%)
    bank_interest_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年银行利息-万元(利率7.5%)")

    # 第4年还款计划-万元
    repayment_plan_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年还款计划-万元")

    # 第4年净现金流-万元
    net_cash_flow_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年净现金流-万元")

    # 第4年累计现金流-万元
    cumulative_cash_flow_4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第4年累计现金流-万元")

    # 第5年供电量-万kWh/a
    power_supply_capacity_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供电量-万kWh/a")

    # 第5年供热水-万t/a
    energy_supply_for_heating_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供热水-万t/a")

    # 第5年供暖-万GJ
    energy_supply_heating_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供暖-万GJ")

    # 第5年供冷-万GJ
    energy_supply_for_cooling_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供冷-万GJ")

    # 第5年产汽量-万吨
    vapour_production_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年产汽量-万吨")

    # 第5年其他
    income_other_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年其他")

    # 第5年供电收入-万元/a
    power_supply_income_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供电收入-万元/a")

    # 第5年供热水收入-万元/a
    heating_water_income_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供热水收入-万元/a")

    # 第5年供暖收入-万元/a
    heating_income_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供暖收入-万元/a")

    # 第5年供冷收入-万元/a
    cooling_income_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供冷收入-万元/a")

    # 第5年供蒸汽收入-万元/a(增值税11%)
    steam_supply_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年供蒸汽收入-万元/a(增值税11%)")

    # 第5年其他-万元/a(不含税)(政府补贴)
    income_otherother_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年其他-万元/a(不含税)(政府补贴)")

    # 第5年燃气耗量-万m³/a
    gas_consumption_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年燃气耗量-万m³/a")

    # 第5年燃煤耗量-万t/a
    coal_consumption_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年燃煤耗量-万t/a")

    # 第5年耗电量-万kWh/a
    power_consumption_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年耗电量-万kWh/a")

    # 第5年耗水量-万t/a
    water_consumption_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年耗水量-万t/a")

    # 第5年燃气费用-万元/a
    gas_cost_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年燃气费用-万元/a")

    # 第5年燃煤费用-万元/a
    coal_cost_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年燃煤费用-万元/a")

    # 第5年电力成本-万元/a
    power_cost_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年电力成本-万元/a")

    # 第5年耗水成本-万元/a
    cost_of_water_consumption_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年耗水成本-万元/a")

    # 第5年材料费用-万元/a
    material_cost_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年材料费用-万元/a")

    # 第5年维护费用-万元/a
    maintenance_cost_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年维护费用-万元/a")

    # 第5年人工费用-万元/a
    artificial_cost_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年人工费用-万元/a")

    # 第5年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年其他-万元/a(包括土地租金及容量费)")

    # 第5年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第5年总销售额-万元
    total_sales_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年总销售额-万元")

    # 第5年总成本-万元
    total_cost_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年总成本-万元")

    # 第5年税前利润-万元
    pre_tax_profit_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年税前利润-万元")

    # 第5年税后利润-万元(享受三免三减半）
    post_tax_profit_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年税后利润-万元(享受三免三减半）")

    # 第5年经营现金流-万元
    cash_flow_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年经营现金流-万元")

    # 第5年银行借款余额-万元
    bank_loan_balance_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年银行借款余额-万元")

    # 第5年银行利息-万元(利率7.5%)
    bank_interest_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年银行利息-万元(利率7.5%)")

    # 第5年还款计划-万元
    repayment_plan_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年还款计划-万元")

    # 第5年净现金流-万元
    net_cash_flow_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年净现金流-万元")

    # 第5年累计现金流-万元
    cumulative_cash_flow_5 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第5年累计现金流-万元")

    # 第6年供电量-万kWh/a
    power_supply_capacity_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供电量-万kWh/a")

    # 第6年供热水-万t/a
    energy_supply_for_heating_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供热水-万t/a")

    # 第6年供暖-万GJ
    energy_supply_heating_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供暖-万GJ")

    # 第6年供冷-万GJ
    energy_supply_for_cooling_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供冷-万GJ")

    # 第6年产汽量-万吨
    vapour_production_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年产汽量-万吨")

    # 第6年其他
    income_other_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年其他")

    # 第6年供电收入-万元/a
    power_supply_income_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供电收入-万元/a")

    # 第6年供热水收入-万元/a
    heating_water_income_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供热水收入-万元/a")

    # 第6年供暖收入-万元/a
    heating_income_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供暖收入-万元/a")

    # 第6年供冷收入-万元/a
    cooling_income_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供冷收入-万元/a")

    # 第6年供蒸汽收入-万元/a(增值税11%)
    steam_supply_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年供蒸汽收入-万元/a(增值税11%)")

    # 第6年其他-万元/a(不含税)(政府补贴)
    income_otherother_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年其他-万元/a(不含税)(政府补贴)")

    # 第6年燃气耗量-万m³/a
    gas_consumption_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年燃气耗量-万m³/a")

    # 第6年燃煤耗量-万t/a
    coal_consumption_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年燃煤耗量-万t/a")

    # 第6年耗电量-万kWh/a
    power_consumption_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年耗电量-万kWh/a")

    # 第6年耗水量-万t/a
    water_consumption_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年耗水量-万t/a")

    # 第6年燃气费用-万元/a
    gas_cost_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年燃气费用-万元/a")

    # 第6年燃煤费用-万元/a
    coal_cost_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年燃煤费用-万元/a")

    # 第6年电力成本-万元/a
    power_cost_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年电力成本-万元/a")

    # 第6年耗水成本-万元/a
    cost_of_water_consumption_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年耗水成本-万元/a")

    # 第6年材料费用-万元/a
    material_cost_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年材料费用-万元/a")

    # 第6年维护费用-万元/a
    maintenance_cost_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年维护费用-万元/a")

    # 第6年人工费用-万元/a
    artificial_cost_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年人工费用-万元/a")

    # 第6年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年其他-万元/a(包括土地租金及容量费)")

    # 第6年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第6年总销售额-万元
    total_sales_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年总销售额-万元")

    # 第6年总成本-万元
    total_cost_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年总成本-万元")

    # 第6年税前利润-万元
    pre_tax_profit_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年税前利润-万元")

    # 第6年税后利润-万元(享受三免三减半）
    post_tax_profit_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年税后利润-万元(享受三免三减半）")

    # 第6年经营现金流-万元
    cash_flow_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年经营现金流-万元")

    # 第6年银行借款余额-万元
    bank_loan_balance_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年银行借款余额-万元")

    # 第6年银行利息-万元(利率7.5%)
    bank_interest_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年银行利息-万元(利率7.5%)")

    # 第6年还款计划-万元
    repayment_plan_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年还款计划-万元")

    # 第6年净现金流-万元
    net_cash_flow_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年净现金流-万元")

    # 第6年累计现金流-万元
    cumulative_cash_flow_6 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第6年累计现金流-万元")

    # 第7年供电量-万kWh/a
    power_supply_capacity_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供电量-万kWh/a")

    # 第7年供热水-万t/a
    energy_supply_for_heating_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供热水-万t/a")

    # 第7年供暖-万GJ
    energy_supply_heating_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供暖-万GJ")

    # 第7年供冷-万GJ
    energy_supply_for_cooling_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供冷-万GJ")

    # 第7年产汽量-万吨
    vapour_production_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年产汽量-万吨")

    # 第7年其他
    income_other_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年其他")

    # 第7年供电收入-万元/a
    power_supply_income_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供电收入-万元/a")

    # 第7年供热水收入-万元/a
    heating_water_income_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供热水收入-万元/a")

    # 第7年供暖收入-万元/a
    heating_income_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供暖收入-万元/a")

    # 第7年供冷收入-万元/a
    cooling_income_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供冷收入-万元/a")

    # 第7年供蒸汽收入-万元/a(增值税11%)
    steam_supply_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年供蒸汽收入-万元/a(增值税11%)")

    # 第7年其他-万元/a(不含税)(政府补贴)
    income_otherother_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年其他-万元/a(不含税)(政府补贴)")

    # 第7年燃气耗量-万m³/a
    gas_consumption_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年燃气耗量-万m³/a")

    # 第7年燃煤耗量-万t/a
    coal_consumption_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年燃煤耗量-万t/a")

    # 第7年耗电量-万kWh/a
    power_consumption_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年耗电量-万kWh/a")

    # 第7年耗水量-万t/a
    water_consumption_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年耗水量-万t/a")

    # 第7年燃气费用-万元/a
    gas_cost_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年燃气费用-万元/a")

    # 第7年燃煤费用-万元/a
    coal_cost_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年燃煤费用-万元/a")

    # 第7年电力成本-万元/a
    power_cost_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年电力成本-万元/a")

    # 第7年耗水成本-万元/a
    cost_of_water_consumption_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年耗水成本-万元/a")

    # 第7年材料费用-万元/a
    material_cost_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年材料费用-万元/a")

    # 第7年维护费用-万元/a
    maintenance_cost_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年维护费用-万元/a")

    # 第7年人工费用-万元/a
    artificial_cost_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年人工费用-万元/a")

    # 第7年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年其他-万元/a(包括土地租金及容量费)")

    # 第7年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第7年总销售额-万元
    total_sales_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年总销售额-万元")

    # 第7年总成本-万元
    total_cost_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年总成本-万元")

    # 第7年税前利润-万元
    pre_tax_profit_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年税前利润-万元")

    # 第7年税后利润-万元(享受三免三减半）
    post_tax_profit_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年税后利润-万元(享受三免三减半）")

    # 第7年经营现金流-万元
    cash_flow_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年经营现金流-万元")

    # 第7年银行借款余额-万元
    bank_loan_balance_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年银行借款余额-万元")

    # 第7年银行利息-万元(利率7.5%)
    bank_interest_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年银行利息-万元(利率7.5%)")

    # 第7年还款计划-万元
    repayment_plan_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年还款计划-万元")

    # 第7年净现金流-万元
    net_cash_flow_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年净现金流-万元")

    # 第7年累计现金流-万元
    cumulative_cash_flow_7 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第7年累计现金流-万元")

    # 第8年供电量-万kWh/a
    power_supply_capacity_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供电量-万kWh/a")

    # 第8年供热水-万t/a
    energy_supply_for_heating_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供热水-万t/a")

    # 第8年供暖-万GJ
    energy_supply_heating_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供暖-万GJ")

    # 第8年供冷-万GJ
    energy_supply_for_cooling_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供冷-万GJ")

    # 第8年产汽量-万吨
    vapour_production_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年产汽量-万吨")

    # 第8年其他
    income_other_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年其他")

    # 第8年供电收入-万元/a
    power_supply_income_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供电收入-万元/a")

    # 第8年供热水收入-万元/a
    heating_water_income_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供热水收入-万元/a")

    # 第8年供暖收入-万元/a
    heating_income_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供暖收入-万元/a")

    # 第8年供冷收入-万元/a
    cooling_income_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供冷收入-万元/a")

    # 第8年供蒸汽收入-万元/a(增值税11%)
    steam_supply_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年供蒸汽收入-万元/a(增值税11%)")

    # 第8年其他-万元/a(不含税)(政府补贴)
    income_otherother_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年其他-万元/a(不含税)(政府补贴)")

    # 第8年燃气耗量-万m³/a
    gas_consumption_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年燃气耗量-万m³/a")

    # 第8年燃煤耗量-万t/a
    coal_consumption_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年燃煤耗量-万t/a")

    # 第8年耗电量-万kWh/a
    power_consumption_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年耗电量-万kWh/a")

    # 第8年耗水量-万t/a
    water_consumption_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年耗水量-万t/a")

    # 第8年燃气费用-万元/a
    gas_cost_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年燃气费用-万元/a")

    # 第8年燃煤费用-万元/a
    coal_cost_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年燃煤费用-万元/a")

    # 第8年电力成本-万元/a
    power_cost_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年电力成本-万元/a")

    # 第8年耗水成本-万元/a
    cost_of_water_consumption_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年耗水成本-万元/a")

    # 第8年材料费用-万元/a
    material_cost_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年材料费用-万元/a")

    # 第8年维护费用-万元/a
    maintenance_cost_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年维护费用-万元/a")

    # 第8年人工费用-万元/a
    artificial_cost_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年人工费用-万元/a")

    # 第8年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年其他-万元/a(包括土地租金及容量费)")

    # 第8年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第8年总销售额-万元
    total_sales_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年总销售额-万元")

    # 第8年总成本-万元
    total_cost_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年总成本-万元")

    # 第8年税前利润-万元
    pre_tax_profit_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年税前利润-万元")

    # 第8年税后利润-万元(享受三免三减半）
    post_tax_profit_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年税后利润-万元(享受三免三减半）")

    # 第8年经营现金流-万元
    cash_flow_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年经营现金流-万元")

    # 第8年银行借款余额-万元
    bank_loan_balance_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年银行借款余额-万元")

    # 第8年银行利息-万元(利率7.5%)
    bank_interest_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年银行利息-万元(利率7.5%)")

    # 第8年还款计划-万元
    repayment_plan_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年还款计划-万元")

    # 第8年净现金流-万元
    net_cash_flow_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年净现金流-万元")

    # 第8年累计现金流-万元
    cumulative_cash_flow_8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第8年累计现金流-万元")

    # 第9年供电量-万kWh/a
    power_supply_capacity_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供电量-万kWh/a")

    # 第9年供热水-万t/a
    energy_supply_for_heating_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供热水-万t/a")

    # 第9年供暖-万GJ
    energy_supply_heating_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供暖-万GJ")

    # 第9年供冷-万GJ
    energy_supply_for_cooling_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供冷-万GJ")

    # 第9年产汽量-万吨
    vapour_production_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年产汽量-万吨")

    # 第9年其他
    income_other_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年其他")

    # 第9年供电收入-万元/a
    power_supply_income_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供电收入-万元/a")

    # 第9年供热水收入-万元/a
    heating_water_income_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供热水收入-万元/a")

    # 第9年供暖收入-万元/a
    heating_income_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供暖收入-万元/a")

    # 第9年供冷收入-万元/a
    cooling_income_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供冷收入-万元/a")

    # 第9年供蒸汽收入-万元/a(增值税11%)
    steam_supply_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年供蒸汽收入-万元/a(增值税11%)")

    # 第9年其他-万元/a(不含税)(政府补贴)
    income_otherother_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年其他-万元/a(不含税)(政府补贴)")

    # 第9年燃气耗量-万m³/a
    gas_consumption_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年燃气耗量-万m³/a")

    # 第9年燃煤耗量-万t/a
    coal_consumption_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年燃煤耗量-万t/a")

    # 第9年耗电量-万kWh/a
    power_consumption_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年耗电量-万kWh/a")

    # 第9年耗水量-万t/a
    water_consumption_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年耗水量-万t/a")

    # 第9年燃气费用-万元/a
    gas_cost_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年燃气费用-万元/a")

    # 第9年燃煤费用-万元/a
    coal_cost_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年燃煤费用-万元/a")

    # 第9年电力成本-万元/a
    power_cost_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年电力成本-万元/a")

    # 第9年耗水成本-万元/a
    cost_of_water_consumption_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年耗水成本-万元/a")

    # 第9年材料费用-万元/a
    material_cost_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年材料费用-万元/a")

    # 第9年维护费用-万元/a
    maintenance_cost_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年维护费用-万元/a")

    # 第9年人工费用-万元/a
    artificial_cost_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年人工费用-万元/a")

    # 第9年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年其他-万元/a(包括土地租金及容量费)")

    # 第9年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第9年总销售额-万元
    total_sales_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年总销售额-万元")

    # 第9年总成本-万元
    total_cost_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年总成本-万元")

    # 第9年税前利润-万元
    pre_tax_profit_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年税前利润-万元")

    # 第9年税后利润-万元(享受三免三减半）
    post_tax_profit_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年税后利润-万元(享受三免三减半）")

    # 第9年经营现金流-万元
    cash_flow_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年经营现金流-万元")

    # 第9年银行借款余额-万元
    bank_loan_balance_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年银行借款余额-万元")

    # 第9年银行利息-万元(利率7.5%)
    bank_interest_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年银行利息-万元(利率7.5%)")

    # 第9年还款计划-万元
    repayment_plan_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年还款计划-万元")

    # 第9年净现金流-万元
    net_cash_flow_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年净现金流-万元")

    # 第9年累计现金流-万元
    cumulative_cash_flow_9 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第9年累计现金流-万元")

    # 第10年供电量-万kWh/a
    power_supply_capacity_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供电量-万kWh/a")

    # 第10年供热水-万t/a
    energy_supply_for_heating_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供热水-万t/a")

    # 第10年供暖-万GJ
    energy_supply_heating_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供暖-万GJ")

    # 第10年供冷-万GJ
    energy_supply_for_cooling_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供冷-万GJ")

    # 第10年产汽量-万吨
    vapour_production_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年产汽量-万吨")

    # 第10年其他
    income_other_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年其他")

    # 第10年供电收入-万元/a
    power_supply_income_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供电收入-万元/a")

    # 第10年供热水收入-万元/a
    heating_water_income_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供热水收入-万元/a")

    # 第10年供暖收入-万元/a
    heating_income_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供暖收入-万元/a")

    # 第10年供冷收入-万元/a
    cooling_income_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供冷收入-万元/a")

    # 第10年供蒸汽收入-万元/a(增值税11%)
    steam_supply_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年供蒸汽收入-万元/a(增值税11%)")

    # 第10年其他-万元/a(不含税)(政府补贴)
    income_otherother_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年其他-万元/a(不含税)(政府补贴)")

    # 第10年燃气耗量-万m³/a
    gas_consumption_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年燃气耗量-万m³/a")

    # 第10年燃煤耗量-万t/a
    coal_consumption_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年燃煤耗量-万t/a")

    # 第10年耗电量-万kWh/a
    power_consumption_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年耗电量-万kWh/a")

    # 第10年耗水量-万t/a
    water_consumption_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年耗水量-万t/a")

    # 第10年燃气费用-万元/a
    gas_cost_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年燃气费用-万元/a")

    # 第10年燃煤费用-万元/a
    coal_cost_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年燃煤费用-万元/a")

    # 第10年电力成本-万元/a
    power_cost_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年电力成本-万元/a")

    # 第10年耗水成本-万元/a
    cost_of_water_consumption_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年耗水成本-万元/a")

    # 第10年材料费用-万元/a
    material_cost_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年材料费用-万元/a")

    # 第10年维护费用-万元/a
    maintenance_cost_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年维护费用-万元/a")

    # 第10年人工费用-万元/a
    artificial_cost_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年人工费用-万元/a")

    # 第10年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年其他-万元/a(包括土地租金及容量费)")

    # 第10年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第10年总销售额-万元
    total_sales_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年总销售额-万元")

    # 第10年总成本-万元
    total_cost_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年总成本-万元")

    # 第10年税前利润-万元
    pre_tax_profit_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年税前利润-万元")

    # 第10年税后利润-万元(享受三免三减半）
    post_tax_profit_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年税后利润-万元(享受三免三减半）")

    # 第10年经营现金流-万元
    cash_flow_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年经营现金流-万元")

    # 第10年银行借款余额-万元
    bank_loan_balance_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年银行借款余额-万元")

    # 第10年银行利息-万元(利率7.5%)
    bank_interest_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年银行利息-万元(利率7.5%)")

    # 第10年还款计划-万元
    repayment_plan_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年还款计划-万元")

    # 第10年净现金流-万元
    net_cash_flow_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年净现金流-万元")

    # 第10年累计现金流-万元
    cumulative_cash_flow_10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第10年累计现金流-万元")

    # 第11年供电量-万kWh/a
    power_supply_capacity_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供电量-万kWh/a")

    # 第11年供热水-万t/a
    energy_supply_for_heating_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供热水-万t/a")

    # 第11年供暖-万GJ
    energy_supply_heating_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供暖-万GJ")

    # 第11年供冷-万GJ
    energy_supply_for_cooling_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供冷-万GJ")

    # 第11年产汽量-万吨
    vapour_production_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年产汽量-万吨")

    # 第11年其他
    income_other_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年其他")

    # 第11年供电收入-万元/a
    power_supply_income_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供电收入-万元/a")

    # 第11年供热水收入-万元/a
    heating_water_income_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供热水收入-万元/a")

    # 第11年供暖收入-万元/a
    heating_income_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供暖收入-万元/a")

    # 第11年供冷收入-万元/a
    cooling_income_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供冷收入-万元/a")

    # 第11年供蒸汽收入-万元/a(增值税11%)
    steam_supply_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年供蒸汽收入-万元/a(增值税11%)")

    # 第11年其他-万元/a(不含税)(政府补贴)
    income_otherother_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年其他-万元/a(不含税)(政府补贴)")

    # 第11年燃气耗量-万m³/a
    gas_consumption_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年燃气耗量-万m³/a")

    # 第11年燃煤耗量-万t/a
    coal_consumption_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年燃煤耗量-万t/a")

    # 第11年耗电量-万kWh/a
    power_consumption_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年耗电量-万kWh/a")

    # 第11年耗水量-万t/a
    water_consumption_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年耗水量-万t/a")

    # 第11年燃气费用-万元/a
    gas_cost_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年燃气费用-万元/a")

    # 第11年燃煤费用-万元/a
    coal_cost_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年燃煤费用-万元/a")

    # 第11年电力成本-万元/a
    power_cost_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年电力成本-万元/a")

    # 第11年耗水成本-万元/a
    cost_of_water_consumption_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年耗水成本-万元/a")

    # 第11年材料费用-万元/a
    material_cost_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年材料费用-万元/a")

    # 第11年维护费用-万元/a
    maintenance_cost_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年维护费用-万元/a")

    # 第11年人工费用-万元/a
    artificial_cost_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年人工费用-万元/a")

    # 第11年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年其他-万元/a(包括土地租金及容量费)")

    # 第11年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第11年总销售额-万元
    total_sales_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年总销售额-万元")

    # 第11年总成本-万元
    total_cost_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年总成本-万元")

    # 第11年税前利润-万元
    pre_tax_profit_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年税前利润-万元")

    # 第11年税后利润-万元(享受三免三减半）
    post_tax_profit_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年税后利润-万元(享受三免三减半）")

    # 第11年经营现金流-万元
    cash_flow_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年经营现金流-万元")

    # 第11年银行借款余额-万元
    bank_loan_balance_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年银行借款余额-万元")

    # 第11年银行利息-万元(利率7.5%)
    bank_interest_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年银行利息-万元(利率7.5%)")

    # 第11年还款计划-万元
    repayment_plan_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年还款计划-万元")

    # 第11年净现金流-万元
    net_cash_flow_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年净现金流-万元")

    # 第11年累计现金流-万元
    cumulative_cash_flow_11 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第11年累计现金流-万元")

    # 第12年供电量-万kWh/a
    power_supply_capacity_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供电量-万kWh/a")

    # 第12年供热水-万t/a
    energy_supply_for_heating_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供热水-万t/a")

    # 第12年供暖-万GJ
    energy_supply_heating_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供暖-万GJ")

    # 第12年供冷-万GJ
    energy_supply_for_cooling_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供冷-万GJ")

    # 第12年产汽量-万吨
    vapour_production_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年产汽量-万吨")

    # 第12年其他
    income_other_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年其他")

    # 第12年供电收入-万元/a
    power_supply_income_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供电收入-万元/a")

    # 第12年供热水收入-万元/a
    heating_water_income_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供热水收入-万元/a")

    # 第12年供暖收入-万元/a
    heating_income_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供暖收入-万元/a")

    # 第12年供冷收入-万元/a
    cooling_income_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供冷收入-万元/a")

    # 第12年供蒸汽收入-万元/a(增值税11%)
    steam_supply_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年供蒸汽收入-万元/a(增值税11%)")

    # 第12年其他-万元/a(不含税)(政府补贴)
    income_otherother_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年其他-万元/a(不含税)(政府补贴)")

    # 第12年燃气耗量-万m³/a
    gas_consumption_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年燃气耗量-万m³/a")

    # 第12年燃煤耗量-万t/a
    coal_consumption_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年燃煤耗量-万t/a")

    # 第12年耗电量-万kWh/a
    power_consumption_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年耗电量-万kWh/a")

    # 第12年耗水量-万t/a
    water_consumption_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年耗水量-万t/a")

    # 第12年燃气费用-万元/a
    gas_cost_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年燃气费用-万元/a")

    # 第12年燃煤费用-万元/a
    coal_cost_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年燃煤费用-万元/a")

    # 第12年电力成本-万元/a
    power_cost_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年电力成本-万元/a")

    # 第12年耗水成本-万元/a
    cost_of_water_consumption_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年耗水成本-万元/a")

    # 第12年材料费用-万元/a
    material_cost_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年材料费用-万元/a")

    # 第12年维护费用-万元/a
    maintenance_cost_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年维护费用-万元/a")

    # 第12年人工费用-万元/a
    artificial_cost_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年人工费用-万元/a")

    # 第12年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年其他-万元/a(包括土地租金及容量费)")

    # 第12年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第12年总销售额-万元
    total_sales_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年总销售额-万元")

    # 第12年总成本-万元
    total_cost_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年总成本-万元")

    # 第12年税前利润-万元
    pre_tax_profit_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年税前利润-万元")

    # 第12年税后利润-万元(享受三免三减半）
    post_tax_profit_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年税后利润-万元(享受三免三减半）")

    # 第12年经营现金流-万元
    cash_flow_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年经营现金流-万元")

    # 第12年银行借款余额-万元
    bank_loan_balance_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年银行借款余额-万元")

    # 第12年银行利息-万元(利率7.5%)
    bank_interest_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年银行利息-万元(利率7.5%)")

    # 第12年还款计划-万元
    repayment_plan_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年还款计划-万元")

    # 第12年净现金流-万元
    net_cash_flow_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年净现金流-万元")

    # 第12年累计现金流-万元
    cumulative_cash_flow_12 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第12年累计现金流-万元")

    # 第13年供电量-万kWh/a
    power_supply_capacity_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供电量-万kWh/a")

    # 第13年供热水-万t/a
    energy_supply_for_heating_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供热水-万t/a")

    # 第13年供暖-万GJ
    energy_supply_heating_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供暖-万GJ")

    # 第13年供冷-万GJ
    energy_supply_for_cooling_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供冷-万GJ")

    # 第13年产汽量-万吨
    vapour_production_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年产汽量-万吨")

    # 第13年其他
    income_other_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年其他")

    # 第13年供电收入-万元/a
    power_supply_income_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供电收入-万元/a")

    # 第13年供热水收入-万元/a
    heating_water_income_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供热水收入-万元/a")

    # 第13年供暖收入-万元/a
    heating_income_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供暖收入-万元/a")

    # 第13年供冷收入-万元/a
    cooling_income_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供冷收入-万元/a")

    # 第13年供蒸汽收入-万元/a(增值税11%)
    steam_supply_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年供蒸汽收入-万元/a(增值税11%)")

    # 第13年其他-万元/a(不含税)(政府补贴)
    income_otherother_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年其他-万元/a(不含税)(政府补贴)")

    # 第13年燃气耗量-万m³/a
    gas_consumption_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年燃气耗量-万m³/a")

    # 第13年燃煤耗量-万t/a
    coal_consumption_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年燃煤耗量-万t/a")

    # 第13年耗电量-万kWh/a
    power_consumption_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年耗电量-万kWh/a")

    # 第13年耗水量-万t/a
    water_consumption_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年耗水量-万t/a")

    # 第13年燃气费用-万元/a
    gas_cost_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年燃气费用-万元/a")

    # 第13年燃煤费用-万元/a
    coal_cost_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年燃煤费用-万元/a")

    # 第13年电力成本-万元/a
    power_cost_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年电力成本-万元/a")

    # 第13年耗水成本-万元/a
    cost_of_water_consumption_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年耗水成本-万元/a")

    # 第13年材料费用-万元/a
    material_cost_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年材料费用-万元/a")

    # 第13年维护费用-万元/a
    maintenance_cost_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年维护费用-万元/a")

    # 第13年人工费用-万元/a
    artificial_cost_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年人工费用-万元/a")

    # 第13年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年其他-万元/a(包括土地租金及容量费)")

    # 第13年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第13年总销售额-万元
    total_sales_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年总销售额-万元")

    # 第13年总成本-万元
    total_cost_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年总成本-万元")

    # 第13年税前利润-万元
    pre_tax_profit_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年税前利润-万元")

    # 第13年税后利润-万元(享受三免三减半）
    post_tax_profit_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年税后利润-万元(享受三免三减半）")

    # 第13年经营现金流-万元
    cash_flow_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年经营现金流-万元")

    # 第13年银行借款余额-万元
    bank_loan_balance_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年银行借款余额-万元")

    # 第13年银行利息-万元(利率7.5%)
    bank_interest_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年银行利息-万元(利率7.5%)")

    # 第13年还款计划-万元
    repayment_plan_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年还款计划-万元")

    # 第13年净现金流-万元
    net_cash_flow_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年净现金流-万元")

    # 第13年累计现金流-万元
    cumulative_cash_flow_13 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第13年累计现金流-万元")

    # 第14年供电量-万kWh/a
    power_supply_capacity_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供电量-万kWh/a")

    # 第14年供热水-万t/a
    energy_supply_for_heating_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供热水-万t/a")

    # 第14年供暖-万GJ
    energy_supply_heating_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供暖-万GJ")

    # 第14年供冷-万GJ
    energy_supply_for_cooling_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供冷-万GJ")

    # 第14年产汽量-万吨
    vapour_production_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年产汽量-万吨")

    # 第14年其他
    income_other_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年其他")

    # 第14年供电收入-万元/a
    power_supply_income_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供电收入-万元/a")

    # 第14年供热水收入-万元/a
    heating_water_income_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供热水收入-万元/a")

    # 第14年供暖收入-万元/a
    heating_income_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供暖收入-万元/a")

    # 第14年供冷收入-万元/a
    cooling_income_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供冷收入-万元/a")

    # 第14年供蒸汽收入-万元/a(增值税11%)
    steam_supply_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年供蒸汽收入-万元/a(增值税11%)")

    # 第14年其他-万元/a(不含税)(政府补贴)
    income_otherother_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年其他-万元/a(不含税)(政府补贴)")

    # 第14年燃气耗量-万m³/a
    gas_consumption_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年燃气耗量-万m³/a")

    # 第14年燃煤耗量-万t/a
    coal_consumption_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年燃煤耗量-万t/a")

    # 第14年耗电量-万kWh/a
    power_consumption_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年耗电量-万kWh/a")

    # 第14年耗水量-万t/a
    water_consumption_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年耗水量-万t/a")

    # 第14年燃气费用-万元/a
    gas_cost_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年燃气费用-万元/a")

    # 第14年燃煤费用-万元/a
    coal_cost_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年燃煤费用-万元/a")

    # 第14年电力成本-万元/a
    power_cost_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年电力成本-万元/a")

    # 第14年耗水成本-万元/a
    cost_of_water_consumption_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年耗水成本-万元/a")

    # 第14年材料费用-万元/a
    material_cost_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年材料费用-万元/a")

    # 第14年维护费用-万元/a
    maintenance_cost_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年维护费用-万元/a")

    # 第14年人工费用-万元/a
    artificial_cost_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年人工费用-万元/a")

    # 第14年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年其他-万元/a(包括土地租金及容量费)")

    # 第14年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第14年总销售额-万元
    total_sales_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年总销售额-万元")

    # 第14年总成本-万元
    total_cost_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年总成本-万元")

    # 第14年税前利润-万元
    pre_tax_profit_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年税前利润-万元")

    # 第14年税后利润-万元(享受三免三减半）
    post_tax_profit_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年税后利润-万元(享受三免三减半）")

    # 第14年经营现金流-万元
    cash_flow_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年经营现金流-万元")

    # 第14年银行借款余额-万元
    bank_loan_balance_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年银行借款余额-万元")

    # 第14年银行利息-万元(利率7.5%)
    bank_interest_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年银行利息-万元(利率7.5%)")

    # 第14年还款计划-万元
    repayment_plan_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年还款计划-万元")

    # 第14年净现金流-万元
    net_cash_flow_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年净现金流-万元")

    # 第14年累计现金流-万元
    cumulative_cash_flow_14 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第14年累计现金流-万元")

    # 第15年供电量-万kWh/a
    power_supply_capacity_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供电量-万kWh/a")

    # 第15年供热水-万t/a
    energy_supply_for_heating_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供热水-万t/a")

    # 第15年供暖-万GJ
    energy_supply_heating_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供暖-万GJ")

    # 第15年供冷-万GJ
    energy_supply_for_cooling_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供冷-万GJ")

    # 第15年产汽量-万吨
    vapour_production_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年产汽量-万吨")

    # 第15年其他
    income_other_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年其他")

    # 第15年供电收入-万元/a
    power_supply_income_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供电收入-万元/a")

    # 第15年供热水收入-万元/a
    heating_water_income_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供热水收入-万元/a")

    # 第15年供暖收入-万元/a
    heating_income_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供暖收入-万元/a")

    # 第15年供冷收入-万元/a
    cooling_income_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供冷收入-万元/a")

    # 第15年供蒸汽收入-万元/a(增值税11%)
    steam_supply_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年供蒸汽收入-万元/a(增值税11%)")

    # 第15年其他-万元/a(不含税)(政府补贴)
    income_otherother_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年其他-万元/a(不含税)(政府补贴)")

    # 第15年燃气耗量-万m³/a
    gas_consumption_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年燃气耗量-万m³/a")

    # 第15年燃煤耗量-万t/a
    coal_consumption_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年燃煤耗量-万t/a")

    # 第15年耗电量-万kWh/a
    power_consumption_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年耗电量-万kWh/a")

    # 第15年耗水量-万t/a
    water_consumption_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年耗水量-万t/a")

    # 第15年燃气费用-万元/a
    gas_cost_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年燃气费用-万元/a")

    # 第15年燃煤费用-万元/a
    coal_cost_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年燃煤费用-万元/a")

    # 第15年电力成本-万元/a
    power_cost_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年电力成本-万元/a")

    # 第15年耗水成本-万元/a
    cost_of_water_consumption_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年耗水成本-万元/a")

    # 第15年材料费用-万元/a
    material_cost_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年材料费用-万元/a")

    # 第15年维护费用-万元/a
    maintenance_cost_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年维护费用-万元/a")

    # 第15年人工费用-万元/a
    artificial_cost_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年人工费用-万元/a")

    # 第15年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年其他-万元/a(包括土地租金及容量费)")

    # 第15年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第15年总销售额-万元
    total_sales_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年总销售额-万元")

    # 第15年总成本-万元
    total_cost_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年总成本-万元")

    # 第15年税前利润-万元
    pre_tax_profit_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年税前利润-万元")

    # 第15年税后利润-万元(享受三免三减半）
    post_tax_profit_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年税后利润-万元(享受三免三减半）")

    # 第15年经营现金流-万元
    cash_flow_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年经营现金流-万元")

    # 第15年银行借款余额-万元
    bank_loan_balance_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年银行借款余额-万元")

    # 第15年银行利息-万元(利率7.5%)
    bank_interest_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年银行利息-万元(利率7.5%)")

    # 第15年还款计划-万元
    repayment_plan_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年还款计划-万元")

    # 第15年净现金流-万元
    net_cash_flow_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年净现金流-万元")

    # 第15年累计现金流-万元
    cumulative_cash_flow_15 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第15年累计现金流-万元")

    # 第16年供电量-万kWh/a
    power_supply_capacity_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供电量-万kWh/a")

    # 第16年供热水-万t/a
    energy_supply_for_heating_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供热水-万t/a")

    # 第16年供暖-万GJ
    energy_supply_heating_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供暖-万GJ")

    # 第16年供冷-万GJ
    energy_supply_for_cooling_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供冷-万GJ")

    # 第16年产汽量-万吨
    vapour_production_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年产汽量-万吨")

    # 第16年其他
    income_other_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年其他")

    # 第16年供电收入-万元/a
    power_supply_income_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供电收入-万元/a")

    # 第16年供热水收入-万元/a
    heating_water_income_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供热水收入-万元/a")

    # 第16年供暖收入-万元/a
    heating_income_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供暖收入-万元/a")

    # 第16年供冷收入-万元/a
    cooling_income_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供冷收入-万元/a")

    # 第16年供蒸汽收入-万元/a(增值税11%)
    steam_supply_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年供蒸汽收入-万元/a(增值税11%)")

    # 第16年其他-万元/a(不含税)(政府补贴)
    income_otherother_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年其他-万元/a(不含税)(政府补贴)")

    # 第16年燃气耗量-万m³/a
    gas_consumption_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年燃气耗量-万m³/a")

    # 第16年燃煤耗量-万t/a
    coal_consumption_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年燃煤耗量-万t/a")

    # 第16年耗电量-万kWh/a
    power_consumption_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年耗电量-万kWh/a")

    # 第16年耗水量-万t/a
    water_consumption_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年耗水量-万t/a")

    # 第16年燃气费用-万元/a
    gas_cost_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年燃气费用-万元/a")

    # 第16年燃煤费用-万元/a
    coal_cost_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年燃煤费用-万元/a")

    # 第16年电力成本-万元/a
    power_cost_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年电力成本-万元/a")

    # 第16年耗水成本-万元/a
    cost_of_water_consumption_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年耗水成本-万元/a")

    # 第16年材料费用-万元/a
    material_cost_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年材料费用-万元/a")

    # 第16年维护费用-万元/a
    maintenance_cost_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年维护费用-万元/a")

    # 第16年人工费用-万元/a
    artificial_cost_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年人工费用-万元/a")

    # 第16年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年其他-万元/a(包括土地租金及容量费)")

    # 第16年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第16年总销售额-万元
    total_sales_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年总销售额-万元")

    # 第16年总成本-万元
    total_cost_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年总成本-万元")

    # 第16年税前利润-万元
    pre_tax_profit_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年税前利润-万元")

    # 第16年税后利润-万元(享受三免三减半）
    post_tax_profit_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年税后利润-万元(享受三免三减半）")

    # 第16年经营现金流-万元
    cash_flow_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年经营现金流-万元")

    # 第16年银行借款余额-万元
    bank_loan_balance_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年银行借款余额-万元")

    # 第16年银行利息-万元(利率7.5%)
    bank_interest_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年银行利息-万元(利率7.5%)")

    # 第16年还款计划-万元
    repayment_plan_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年还款计划-万元")

    # 第16年净现金流-万元
    net_cash_flow_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年净现金流-万元")

    # 第16年累计现金流-万元
    cumulative_cash_flow_16 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第16年累计现金流-万元")

    # 第17年供电量-万kWh/a
    power_supply_capacity_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供电量-万kWh/a")

    # 第17年供热水-万t/a
    energy_supply_for_heating_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供热水-万t/a")

    # 第17年供暖-万GJ
    energy_supply_heating_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供暖-万GJ")

    # 第17年供冷-万GJ
    energy_supply_for_cooling_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供冷-万GJ")

    # 第17年产汽量-万吨
    vapour_production_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年产汽量-万吨")

    # 第17年其他
    income_other_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年其他")

    # 第17年供电收入-万元/a
    power_supply_income_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供电收入-万元/a")

    # 第17年供热水收入-万元/a
    heating_water_income_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供热水收入-万元/a")

    # 第17年供暖收入-万元/a
    heating_income_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供暖收入-万元/a")

    # 第17年供冷收入-万元/a
    cooling_income_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供冷收入-万元/a")

    # 第17年供蒸汽收入-万元/a(增值税11%)
    steam_supply_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年供蒸汽收入-万元/a(增值税11%)")

    # 第17年其他-万元/a(不含税)(政府补贴)
    income_otherother_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年其他-万元/a(不含税)(政府补贴)")

    # 第17年燃气耗量-万m³/a
    gas_consumption_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年燃气耗量-万m³/a")

    # 第17年燃煤耗量-万t/a
    coal_consumption_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年燃煤耗量-万t/a")

    # 第17年耗电量-万kWh/a
    power_consumption_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年耗电量-万kWh/a")

    # 第17年耗水量-万t/a
    water_consumption_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年耗水量-万t/a")

    # 第17年燃气费用-万元/a
    gas_cost_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年燃气费用-万元/a")

    # 第17年燃煤费用-万元/a
    coal_cost_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年燃煤费用-万元/a")

    # 第17年电力成本-万元/a
    power_cost_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年电力成本-万元/a")

    # 第17年耗水成本-万元/a
    cost_of_water_consumption_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年耗水成本-万元/a")

    # 第17年材料费用-万元/a
    material_cost_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年材料费用-万元/a")

    # 第17年维护费用-万元/a
    maintenance_cost_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年维护费用-万元/a")

    # 第17年人工费用-万元/a
    artificial_cost_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年人工费用-万元/a")

    # 第17年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年其他-万元/a(包括土地租金及容量费)")

    # 第17年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第17年总销售额-万元
    total_sales_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年总销售额-万元")

    # 第17年总成本-万元
    total_cost_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年总成本-万元")

    # 第17年税前利润-万元
    pre_tax_profit_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年税前利润-万元")

    # 第17年税后利润-万元(享受三免三减半）
    post_tax_profit_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年税后利润-万元(享受三免三减半）")

    # 第17年经营现金流-万元
    cash_flow_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年经营现金流-万元")

    # 第17年银行借款余额-万元
    bank_loan_balance_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年银行借款余额-万元")

    # 第17年银行利息-万元(利率7.5%)
    bank_interest_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年银行利息-万元(利率7.5%)")

    # 第17年还款计划-万元
    repayment_plan_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年还款计划-万元")

    # 第17年净现金流-万元
    net_cash_flow_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年净现金流-万元")

    # 第17年累计现金流-万元
    cumulative_cash_flow_17 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第17年累计现金流-万元")

    # 第18年供电量-万kWh/a
    power_supply_capacity_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供电量-万kWh/a")

    # 第18年供热水-万t/a
    energy_supply_for_heating_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供热水-万t/a")

    # 第18年供暖-万GJ
    energy_supply_heating_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供暖-万GJ")

    # 第18年供冷-万GJ
    energy_supply_for_cooling_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供冷-万GJ")

    # 第18年产汽量-万吨
    vapour_production_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年产汽量-万吨")

    # 第18年其他
    income_other_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年其他")

    # 第18年供电收入-万元/a
    power_supply_income_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供电收入-万元/a")

    # 第18年供热水收入-万元/a
    heating_water_income_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供热水收入-万元/a")

    # 第18年供暖收入-万元/a
    heating_income_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供暖收入-万元/a")

    # 第18年供冷收入-万元/a
    cooling_income_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供冷收入-万元/a")

    # 第18年供蒸汽收入-万元/a(增值税11%)
    steam_supply_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年供蒸汽收入-万元/a(增值税11%)")

    # 第18年其他-万元/a(不含税)(政府补贴)
    income_otherother_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年其他-万元/a(不含税)(政府补贴)")

    # 第18年燃气耗量-万m³/a
    gas_consumption_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年燃气耗量-万m³/a")

    # 第18年燃煤耗量-万t/a
    coal_consumption_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年燃煤耗量-万t/a")

    # 第18年耗电量-万kWh/a
    power_consumption_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年耗电量-万kWh/a")

    # 第18年耗水量-万t/a
    water_consumption_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年耗水量-万t/a")

    # 第18年燃气费用-万元/a
    gas_cost_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年燃气费用-万元/a")

    # 第18年燃煤费用-万元/a
    coal_cost_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年燃煤费用-万元/a")

    # 第18年电力成本-万元/a
    power_cost_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年电力成本-万元/a")

    # 第18年耗水成本-万元/a
    cost_of_water_consumption_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年耗水成本-万元/a")

    # 第18年材料费用-万元/a
    material_cost_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年材料费用-万元/a")

    # 第18年维护费用-万元/a
    maintenance_cost_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年维护费用-万元/a")

    # 第18年人工费用-万元/a
    artificial_cost_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年人工费用-万元/a")

    # 第18年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年其他-万元/a(包括土地租金及容量费)")

    # 第18年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第18年总销售额-万元
    total_sales_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年总销售额-万元")

    # 第18年总成本-万元
    total_cost_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年总成本-万元")

    # 第18年税前利润-万元
    pre_tax_profit_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年税前利润-万元")

    # 第18年税后利润-万元(享受三免三减半）
    post_tax_profit_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年税后利润-万元(享受三免三减半）")

    # 第18年经营现金流-万元
    cash_flow_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年经营现金流-万元")

    # 第18年银行借款余额-万元
    bank_loan_balance_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年银行借款余额-万元")

    # 第18年银行利息-万元(利率7.5%)
    bank_interest_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年银行利息-万元(利率7.5%)")

    # 第18年还款计划-万元
    repayment_plan_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年还款计划-万元")

    # 第18年净现金流-万元
    net_cash_flow_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年净现金流-万元")

    # 第18年累计现金流-万元
    cumulative_cash_flow_18 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第18年累计现金流-万元")

    # 第19年供电量-万kWh/a
    power_supply_capacity_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供电量-万kWh/a")

    # 第19年供热水-万t/a
    energy_supply_for_heating_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供热水-万t/a")

    # 第19年供暖-万GJ
    energy_supply_heating_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供暖-万GJ")

    # 第19年供冷-万GJ
    energy_supply_for_cooling_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供冷-万GJ")

    # 第19年产汽量-万吨
    vapour_production_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年产汽量-万吨")

    # 第19年其他
    income_other_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年其他")

    # 第19年供电收入-万元/a
    power_supply_income_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供电收入-万元/a")

    # 第19年供热水收入-万元/a
    heating_water_income_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供热水收入-万元/a")

    # 第19年供暖收入-万元/a
    heating_income_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供暖收入-万元/a")

    # 第19年供冷收入-万元/a
    cooling_income_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供冷收入-万元/a")

    # 第19年供蒸汽收入-万元/a(增值税11%)
    steam_supply_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年供蒸汽收入-万元/a(增值税11%)")

    # 第19年其他-万元/a(不含税)(政府补贴)
    income_otherother_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年其他-万元/a(不含税)(政府补贴)")

    # 第19年燃气耗量-万m³/a
    gas_consumption_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年燃气耗量-万m³/a")

    # 第19年燃煤耗量-万t/a
    coal_consumption_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年燃煤耗量-万t/a")

    # 第19年耗电量-万kWh/a
    power_consumption_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年耗电量-万kWh/a")

    # 第19年耗水量-万t/a
    water_consumption_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年耗水量-万t/a")

    # 第19年燃气费用-万元/a
    gas_cost_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年燃气费用-万元/a")

    # 第19年燃煤费用-万元/a
    coal_cost_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年燃煤费用-万元/a")

    # 第19年电力成本-万元/a
    power_cost_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年电力成本-万元/a")

    # 第19年耗水成本-万元/a
    cost_of_water_consumption_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年耗水成本-万元/a")

    # 第19年材料费用-万元/a
    material_cost_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年材料费用-万元/a")

    # 第19年维护费用-万元/a
    maintenance_cost_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年维护费用-万元/a")

    # 第19年人工费用-万元/a
    artificial_cost_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年人工费用-万元/a")

    # 第19年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年其他-万元/a(包括土地租金及容量费)")

    # 第19年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第19年总销售额-万元
    total_sales_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年总销售额-万元")

    # 第19年总成本-万元
    total_cost_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年总成本-万元")

    # 第19年税前利润-万元
    pre_tax_profit_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年税前利润-万元")

    # 第19年税后利润-万元(享受三免三减半）
    post_tax_profit_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年税后利润-万元(享受三免三减半）")

    # 第19年经营现金流-万元
    cash_flow_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年经营现金流-万元")

    # 第19年银行借款余额-万元
    bank_loan_balance_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年银行借款余额-万元")

    # 第19年银行利息-万元(利率7.5%)
    bank_interest_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年银行利息-万元(利率7.5%)")

    # 第19年还款计划-万元
    repayment_plan_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年还款计划-万元")

    # 第19年净现金流-万元
    net_cash_flow_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年净现金流-万元")

    # 第19年累计现金流-万元
    cumulative_cash_flow_19 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第19年累计现金流-万元")

    # 第20年供电量-万kWh/a
    power_supply_capacity_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供电量-万kWh/a")

    # 第20年供热水-万t/a
    energy_supply_for_heating_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供热水-万t/a")

    # 第20年供暖-万GJ
    energy_supply_heating_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供暖-万GJ")

    # 第20年供冷-万GJ
    energy_supply_for_cooling_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供冷-万GJ")

    # 第20年产汽量-万吨
    vapour_production_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年产汽量-万吨")

    # 第20年其他
    income_other_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年其他")

    # 第20年供电收入-万元/a
    power_supply_income_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供电收入-万元/a")

    # 第20年供热水收入-万元/a
    heating_water_income_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供热水收入-万元/a")

    # 第20年供暖收入-万元/a
    heating_income_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供暖收入-万元/a")

    # 第20年供冷收入-万元/a
    cooling_income_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供冷收入-万元/a")

    # 第20年供蒸汽收入-万元/a(增值税11%)
    steam_supply_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年供蒸汽收入-万元/a(增值税11%)")

    # 第20年其他-万元/a(不含税)(政府补贴)
    income_otherother_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年其他-万元/a(不含税)(政府补贴)")

    # 第20年燃气耗量-万m³/a
    gas_consumption_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年燃气耗量-万m³/a")

    # 第20年燃煤耗量-万t/a
    coal_consumption_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年燃煤耗量-万t/a")

    # 第20年耗电量-万kWh/a
    power_consumption_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年耗电量-万kWh/a")

    # 第20年耗水量-万t/a
    water_consumption_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年耗水量-万t/a")

    # 第20年燃气费用-万元/a
    gas_cost_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年燃气费用-万元/a")

    # 第20年燃煤费用-万元/a
    coal_cost_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年燃煤费用-万元/a")

    # 第20年电力成本-万元/a
    power_cost_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年电力成本-万元/a")

    # 第20年耗水成本-万元/a
    cost_of_water_consumption_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年耗水成本-万元/a")

    # 第20年材料费用-万元/a
    material_cost_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年材料费用-万元/a")

    # 第20年维护费用-万元/a
    maintenance_cost_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年维护费用-万元/a")

    # 第20年人工费用-万元/a
    artificial_cost_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年人工费用-万元/a")

    # 第20年其他-万元/a(包括土地租金及容量费)
    otherincluding_rent_capacity_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年其他-万元/a(包括土地租金及容量费)")

    # 第20年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）
    depreciation_amortization_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）")

    # 第20年总销售额-万元
    total_sales_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年总销售额-万元")

    # 第20年总成本-万元
    total_cost_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年总成本-万元")

    # 第20年税前利润-万元
    pre_tax_profit_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年税前利润-万元")

    # 第20年税后利润-万元(享受三免三减半）
    post_tax_profit_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年税后利润-万元(享受三免三减半）")

    # 第20年经营现金流-万元
    cash_flow_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年经营现金流-万元")

    # 第20年银行借款余额-万元
    bank_loan_balance_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年银行借款余额-万元")

    # 第20年银行利息-万元(利率7.5%)
    bank_interest_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年银行利息-万元(利率7.5%)")

    # 第20年还款计划-万元
    repayment_plan_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年还款计划-万元")

    # 第20年净现金流-万元
    net_cash_flow_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年净现金流-万元")

    # 第20年累计现金流-万元
    cumulative_cash_flow_20 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"第20年累计现金流-万元")

    # 根据id查找实体
    @staticmethod
    def search_economic(plan_id):
        result = Ccpp_ccpp_economic.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_Ccppeconomic(plan_id):
        economic = Ccpp_ccpp_economic.search_economic(plan_id)
        try:
            db.session.delete(economic)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete economic<id=%s, plan_id=%s> in database" %
                  (economic.id, economic.plan_id))
    
    # 更新ccpp
    @staticmethod
    def updata_ccppeconomic(economic):
        if economic.id is not None:
            try:
                db.session.add(economic)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("Error %s" % e)
                raise e
            finally:
                print("updata economic<id=%s, > in updata" % (economic.id))
