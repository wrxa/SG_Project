
# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97
from base import CalculationObserver, ExecuteStrategy


# 实现字段power_supply_income_2:供电收入-万元/a,的计算1
class Power_supply_income_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['power_supply_capacity_2'] != '' and val['power_supply_capacity_2'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None:
            power_supply_income_2 = (float(val['power_supply_capacity_2']))*(float(val['energy_supply_price']))/1.17
            result.power_supply_income_2 = power_supply_income_2
        print(result)


# 实现字段heating_water_income_2:供热水收入-万元/a,的计算2
class Heating_water_income_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_for_heating_2'] != '' and val['energy_supply_for_heating_2'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None:
            heating_water_income_2 = (float(val['energy_supply_for_heating_2']))*(float(val['energy_supply_water_price']))/1.11
            result.heating_water_income_2 = heating_water_income_2
        print(result)


# 实现字段heating_income_2:供暖收入-万元/a,的计算3
class Heating_income_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_heating_2'] != '' and val['energy_supply_heating_2'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None:
            heating_income_2 = (float(val['energy_supply_heating_2']))*(float(val['energy_supply_for_heating']))/1.11
            result.heating_income_2 = heating_income_2
        print(result)


# 实现字段cooling_income_2:供冷收入-万元/a,的计算4
class Cooling_income_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_for_cooling_2'] != '' and val['energy_supply_for_cooling_2'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            cooling_income_2 = (float(val['energy_supply_for_cooling_2']))*(float(val['energy_supply_refrigeration_price']))/1.11
            result.cooling_income_2 = cooling_income_2
        print(result)


# 实现字段steam_supply_2:供蒸汽收入-万元/a(增值税11%),的计算5
class Steam_supply_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['vapour_production_2'] != '' and val['vapour_production_2'] is not None:
            steam_supply_2 = (float(val['vapour_production_2']))*(float(val['energy_supply_steam_price']))/1.11
            result.steam_supply_2 = steam_supply_2
        print(result)


# 实现字段gas_cost_2:燃气费用-万元/a,的计算6
class Gas_cost_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['gas_consumption_2'] != '' and val['gas_consumption_2'] is not None:
            gas_cost_2 = (float(val['gas_consumption_2']))*(float(val['natural_gas_price']))/1.13
            result.gas_cost_2 = gas_cost_2
        print(result)


# 实现字段coal_cost_2:燃煤费用-万元/a,的计算7
class Coal_cost_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['coal_price'] != '' and val['coal_price'] is not None and val['coal_consumption_2'] != '' and val['coal_consumption_2'] is not None:
            coal_cost_2 = (float(val['coal_consumption_2']))*(float(val['coal_price']))/1.13
            result.coal_cost_2 = coal_cost_2
        print(result)


# 实现字段power_cost_2:电力成本-万元/a,的计算8
class Power_cost_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['power_consumption_2'] != '' and val['power_consumption_2'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None:
            power_cost_2 = (float(val['power_consumption_2']))*(float(val['electricity_price']))/1.17
            result.power_cost_2 = power_cost_2
        print(result)


# 实现字段cost_of_water_consumption_2:耗水成本-万元/a,的计算9
class Cost_of_water_consumption_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['water_consumption_2'] != '' and val['water_consumption_2'] is not None and val['water_price'] != '' and val['water_price'] is not None:
            cost_of_water_consumption_2 = (float(val['water_consumption_2']))*(float(val['water_price']))/1.13
            result.cost_of_water_consumption_2 = cost_of_water_consumption_2
        print(result)


# 实现字段depreciation_amortization_2:折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）,的计算10
class Depreciation_amortization_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['new_investment'] != '' and val['new_investment'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None:
            depreciation_amortization_2 = (float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))
            result.depreciation_amortization_2 = depreciation_amortization_2
        print(result)


# 实现字段total_sales_2:总销售额-万元,的计算11
class Total_sales_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['power_supply_capacity_2'] != '' and val['power_supply_capacity_2'] is not None and val['energy_supply_for_heating_2'] != '' and val['energy_supply_for_heating_2'] is not None and val['energy_supply_heating_2'] != '' and val['energy_supply_heating_2'] is not None and val['energy_supply_for_cooling_2'] != '' and val['energy_supply_for_cooling_2'] is not None and val['vapour_production_2'] != '' and val['vapour_production_2'] is not None and val['income_otherother_2'] != '' and val['income_otherother_2'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            total_sales_2 = ((float(val['power_supply_capacity_2']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_2']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_2']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_2']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_2']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_2']))
            result.total_sales_2 = total_sales_2
        print(result)


# 实现字段total_cost_2:总成本-万元,的计算12
class Total_cost_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['gas_consumption_2'] != '' and val['gas_consumption_2'] is not None and val['coal_consumption_2'] != '' and val['coal_consumption_2'] is not None and val['power_consumption_2'] != '' and val['power_consumption_2'] is not None and val['water_consumption_2'] != '' and val['water_consumption_2'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_2'] != '' and val['material_cost_2'] is not None and val['maintenance_cost_2'] != '' and val['maintenance_cost_2'] is not None and val['artificial_cost_2'] != '' and val['artificial_cost_2'] is not None and val['otherincluding_rent_capacity_2'] != '' and val['otherincluding_rent_capacity_2'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None:
            total_cost_2 = (((float(val['gas_consumption_2']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_2']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_2']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_2']))*(float(val['water_price']))/1.13)+(float(val['material_cost_2']))+(float(val['maintenance_cost_2']))+(float(val['artificial_cost_2']))+(float(val['otherincluding_rent_capacity_2'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years'])))
            result.total_cost_2 = total_cost_2
        print(result)


# 实现字段pre_tax_profit_2:税前利润-万元,的计算13
class Pre_tax_profit_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['power_supply_capacity_2'] != '' and val['power_supply_capacity_2'] is not None and val['energy_supply_for_heating_2'] != '' and val['energy_supply_for_heating_2'] is not None and val['energy_supply_heating_2'] != '' and val['energy_supply_heating_2'] is not None and val['energy_supply_for_cooling_2'] != '' and val['energy_supply_for_cooling_2'] is not None and val['vapour_production_2'] != '' and val['vapour_production_2'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_2'] != '' and val['income_otherother_2'] is not None and val['gas_consumption_2'] != '' and val['gas_consumption_2'] is not None and val['coal_consumption_2'] != '' and val['coal_consumption_2'] is not None and val['power_consumption_2'] != '' and val['power_consumption_2'] is not None and val['water_consumption_2'] != '' and val['water_consumption_2'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_2'] != '' and val['material_cost_2'] is not None and val['maintenance_cost_2'] != '' and val['maintenance_cost_2'] is not None and val['artificial_cost_2'] != '' and val['artificial_cost_2'] is not None and val['otherincluding_rent_capacity_2'] != '' and val['otherincluding_rent_capacity_2'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            pre_tax_profit_2 = (((float(val['power_supply_capacity_2']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_2']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_2']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_2']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_2']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_2'])))-((((float(val['gas_consumption_2']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_2']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_2']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_2']))*(float(val['water_price']))/1.13)+(float(val['material_cost_2']))+(float(val['maintenance_cost_2']))+(float(val['artificial_cost_2']))+(float(val['otherincluding_rent_capacity_2'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest'])))
            result.pre_tax_profit_2 = pre_tax_profit_2
        print(result)


# 实现字段post_tax_profit_2:税后利润-万元(享受三免三减半）,的计算14
class Post_tax_profit_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        # if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['power_supply_capacity_2'] != '' and val['power_supply_capacity_2'] is not None and val['energy_supply_for_heating_2'] != '' and val['energy_supply_for_heating_2'] is not None and val['energy_supply_heating_2'] != '' and val['energy_supply_heating_2'] is not None and val['energy_supply_for_cooling_2'] != '' and val['energy_supply_for_cooling_2'] is not None and val['vapour_production_2'] != '' and val['vapour_production_2'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_2'] != '' and val['income_otherother_2'] is not None and val['gas_consumption_2'] != '' and val['gas_consumption_2'] is not None and val['coal_consumption_2'] != '' and val['coal_consumption_2'] is not None and val['power_consumption_2'] != '' and val['power_consumption_2'] is not None and val['water_consumption_2'] != '' and val['water_consumption_2'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_2'] != '' and val['material_cost_2'] is not None and val['maintenance_cost_2'] != '' and val['maintenance_cost_2'] is not None and val['artificial_cost_2'] != '' and val['artificial_cost_2'] is not None and val['otherincluding_rent_capacity_2'] != '' and val['otherincluding_rent_capacity_2'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['purchase_cost'] != '' and val['purchase_cost'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['post_tax_profit_vat'] != '' and val['post_tax_profit_vat'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['percentage_capital_total_investment'] != '' and val['percentage_capital_total_investment'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
        #     post_tax_profit_2 = ((((float(val['power_supply_capacity_2']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_2']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_2']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_2']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_2']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_2'])))-((((float(val['gas_consumption_2']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_2']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_2']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_2']))*(float(val['water_price']))/1.13)+(float(val['material_cost_2']))+(float(val['maintenance_cost_2']))+(float(val['artificial_cost_2']))+(float(val['otherincluding_rent_capacity_2'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))+((float(val['purchase_cost']))+(float(val['new_investment']))-((float(val['new_investment']))*(float(val['percentage_capital_total_investment']))))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest']))))*(1-(float(val['post_tax_profit_vat']))/2)
        #     result.post_tax_profit_2 = post_tax_profit_2
        result.post_tax_profit_2 = result.pre_tax_profit_2
        print(result)


# 实现字段cash_flow_2:经营现金流-万元,的计算15
class Cash_flow_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['power_supply_capacity_2'] != '' and val['power_supply_capacity_2'] is not None and val['energy_supply_for_heating_2'] != '' and val['energy_supply_for_heating_2'] is not None and val['energy_supply_heating_2'] != '' and val['energy_supply_heating_2'] is not None and val['energy_supply_for_cooling_2'] != '' and val['energy_supply_for_cooling_2'] is not None and val['vapour_production_2'] != '' and val['vapour_production_2'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_2'] != '' and val['income_otherother_2'] is not None and val['gas_consumption_2'] != '' and val['gas_consumption_2'] is not None and val['coal_consumption_2'] != '' and val['coal_consumption_2'] is not None and val['power_consumption_2'] != '' and val['power_consumption_2'] is not None and val['water_consumption_2'] != '' and val['water_consumption_2'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_2'] != '' and val['material_cost_2'] is not None and val['maintenance_cost_2'] != '' and val['maintenance_cost_2'] is not None and val['artificial_cost_2'] != '' and val['artificial_cost_2'] is not None and val['otherincluding_rent_capacity_2'] != '' and val['otherincluding_rent_capacity_2'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            cash_flow_2 = (((((float(val['power_supply_capacity_2']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_2']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_2']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_2']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_2']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_2'])))-((((float(val['gas_consumption_2']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_2']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_2']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_2']))*(float(val['water_price']))/1.13)+(float(val['material_cost_2']))+(float(val['maintenance_cost_2']))+(float(val['artificial_cost_2']))+(float(val['otherincluding_rent_capacity_2'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest'])))))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years'])))
            result.cash_flow_2 = cash_flow_2
        print(result)


# 实现字段bank_loan_balance_2:银行借款余额-万元,的计算16
class Bank_loan_balance_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None:
            bank_loan_balance_2 = (float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x']))
            result.bank_loan_balance_2 = bank_loan_balance_2
            if bank_loan_balance_2 < 0:
                result.bank_loan_balance_2 = 0
        print(result)


# 实现字段bank_interest_2:银行利息-万元(利率7.5%),的计算17
class Bank_interest_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None:
            bank_interest_2 = ((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest']))
            result.bank_interest_2 = bank_interest_2
        print(result)


# 实现字段net_cash_flow_2:净现金流-万元,的计算18
class Net_cash_flow_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['power_supply_capacity_2'] != '' and val['power_supply_capacity_2'] is not None and val['energy_supply_for_heating_2'] != '' and val['energy_supply_for_heating_2'] is not None and val['energy_supply_heating_2'] != '' and val['energy_supply_heating_2'] is not None and val['energy_supply_for_cooling_2'] != '' and val['energy_supply_for_cooling_2'] is not None and val['vapour_production_2'] != '' and val['vapour_production_2'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_2'] != '' and val['income_otherother_2'] is not None and val['gas_consumption_2'] != '' and val['gas_consumption_2'] is not None and val['coal_consumption_2'] != '' and val['coal_consumption_2'] is not None and val['power_consumption_2'] != '' and val['power_consumption_2'] is not None and val['water_consumption_2'] != '' and val['water_consumption_2'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_2'] != '' and val['material_cost_2'] is not None and val['maintenance_cost_2'] != '' and val['maintenance_cost_2'] is not None and val['artificial_cost_2'] != '' and val['artificial_cost_2'] is not None and val['otherincluding_rent_capacity_2'] != '' and val['otherincluding_rent_capacity_2'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            net_cash_flow_2 = ((((((float(val['power_supply_capacity_2']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_2']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_2']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_2']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_2']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_2'])))-((((float(val['gas_consumption_2']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_2']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_2']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_2']))*(float(val['water_price']))/1.13)+(float(val['material_cost_2']))+(float(val['maintenance_cost_2']))+(float(val['artificial_cost_2']))+(float(val['otherincluding_rent_capacity_2'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest'])))))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))
            result.net_cash_flow_2 = net_cash_flow_2
        print(result)


# 实现字段cumulative_cash_flow_2:累计现金流-万元,的计算19
class Cumulative_cash_flow_2(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['cumulative_cash_flow_x'] != '' and val['cumulative_cash_flow_x'] is not None and val['power_supply_capacity_2'] != '' and val['power_supply_capacity_2'] is not None and val['energy_supply_for_heating_2'] != '' and val['energy_supply_for_heating_2'] is not None and val['energy_supply_heating_2'] != '' and val['energy_supply_heating_2'] is not None and val['energy_supply_for_cooling_2'] != '' and val['energy_supply_for_cooling_2'] is not None and val['vapour_production_2'] != '' and val['vapour_production_2'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_2'] != '' and val['income_otherother_2'] is not None and val['gas_consumption_2'] != '' and val['gas_consumption_2'] is not None and val['coal_consumption_2'] != '' and val['coal_consumption_2'] is not None and val['power_consumption_2'] != '' and val['power_consumption_2'] is not None and val['water_consumption_2'] != '' and val['water_consumption_2'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_2'] != '' and val['material_cost_2'] is not None and val['maintenance_cost_2'] != '' and val['maintenance_cost_2'] is not None and val['artificial_cost_2'] != '' and val['artificial_cost_2'] is not None and val['otherincluding_rent_capacity_2'] != '' and val['otherincluding_rent_capacity_2'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            cumulative_cash_flow_2 = (((((((float(val['power_supply_capacity_2']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_2']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_2']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_2']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_2']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_2'])))-((((float(val['gas_consumption_2']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_2']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_2']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_2']))*(float(val['water_price']))/1.13)+(float(val['material_cost_2']))+(float(val['maintenance_cost_2']))+(float(val['artificial_cost_2']))+(float(val['otherincluding_rent_capacity_2'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest'])))))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years'])))))+(float(val['cumulative_cash_flow_x']))
            result.cumulative_cash_flow_2 = cumulative_cash_flow_2
        print(result)



# 实现字段capital:资本金-万元(占总投资30%）,的计算20
class Capital(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['new_investment'] != '' and val['new_investment'] is not None and val['percentage_capital_total_investment'] != '' and val['percentage_capital_total_investment'] is not None:
            capital = (float(val['new_investment']))*(float(val['percentage_capital_total_investment']))
            result.capital = capital
        print(result)


# 实现字段bank_loan:银行借款-万元,的计算21
class Bank_loan(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['purchase_cost'] != '' and val['purchase_cost'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['percentage_capital_total_investment'] != '' and val['percentage_capital_total_investment'] is not None:
            bank_loan = (float(val['purchase_cost']))+(float(val['new_investment']))-((float(val['new_investment']))*(float(val['percentage_capital_total_investment'])))
            result.bank_loan = bank_loan
        print(result)



class Economic_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        # 添加注册类
        calculationObserver.register(Power_supply_income_2())
        calculationObserver.register(Heating_water_income_2())
        calculationObserver.register(Heating_income_2())
        calculationObserver.register(Cooling_income_2())
        calculationObserver.register(Steam_supply_2())
        calculationObserver.register(Gas_cost_2())
        calculationObserver.register(Coal_cost_2())
        calculationObserver.register(Power_cost_2())
        calculationObserver.register(Cost_of_water_consumption_2())
        calculationObserver.register(Depreciation_amortization_2())
        calculationObserver.register(Total_sales_2())
        calculationObserver.register(Total_cost_2())
        calculationObserver.register(Pre_tax_profit_2())
        calculationObserver.register(Post_tax_profit_2())
        calculationObserver.register(Cash_flow_2())
        calculationObserver.register(Bank_loan_balance_2())
        calculationObserver.register(Bank_interest_2())
        calculationObserver.register(Net_cash_flow_2())
        calculationObserver.register(Cumulative_cash_flow_2())
        # calculationObserver.register(Capital())
        # calculationObserver.register(Bank_loan())
        calculationObserver.writeNewPost(val)


 


    def specialCalculation(self, dbmodel, form):
        val = {
            'flg': 'design',
            'power_consumption_2': form.get('power_consumption_2'),
            'electricity_price': form.get('electricity_price'),
            'power_supply_capacity_2': form.get('power_supply_capacity_2'),
            'cumulative_cash_flow_x': dbmodel.cumulative_cash_flow_1,
            'repayment_plan_x': form.get('repayment_plan_1'),
            'energy_supply_heating_2': form.get('energy_supply_heating_2'),
            'artificial_cost_2': form.get('artificial_cost_2'),
            'gas_consumption_2': form.get('gas_consumption_2'),
            'energy_supply_for_heating_2': form.get('energy_supply_for_heating_2'),
            'material_cost_2': form.get('material_cost_2'),
            'purchase_cost': form.get('purchase_cost'),
            'post_tax_profit_vat': form.get('post_tax_profit_vat'),
            'energy_supply_price': form.get('energy_supply_price'),
            'coal_consumption_2': form.get('coal_consumption_2'),
            'water_price': form.get('water_price'),
            'coal_price': form.get('coal_price'),
            'depreciation_amortization_years': form.get('depreciation_amortization_years'),
            'water_consumption_2': form.get('water_consumption_2'),
            'energy_supply_refrigeration_price': form.get('energy_supply_refrigeration_price'),
            'energy_supply_water_price': form.get('energy_supply_water_price'),
            'otherincluding_rent_capacity_2': form.get('otherincluding_rent_capacity_2'),
            'energy_supply_for_cooling_2': form.get('energy_supply_for_cooling_2'),
            'bank_loan_balance_x': dbmodel.bank_loan_balance_1,
            'vapour_production_2': form.get('vapour_production_2'),
            'energy_supply_for_heating': form.get('energy_supply_for_heating'),
            'income_otherother_2': form.get('income_otherother_2'),
            'new_investment': form.get('new_investment'),
            'natural_gas_price': form.get('natural_gas_price'),
            'energy_supply_steam_price': form.get('energy_supply_steam_price'),
            'interest_rate_bank_interest': form.get('interest_rate_bank_interest'),
            'percentage_capital_total_investment': form.get('percentage_capital_total_investment'),
            'maintenance_cost_2': form.get('maintenance_cost_2'),
            'dbresult': dbmodel}
        self.creatSubscriber(val)
        return val['dbresult']
