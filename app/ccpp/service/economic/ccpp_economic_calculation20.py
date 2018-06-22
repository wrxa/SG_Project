
# -*- coding: utf-8 -*-
from base import FieldCalculation
from util.iapws_if97 import seuif97
from base import CalculationObserver, ExecuteStrategy


# 实现字段power_supply_income_20:供电收入-万元/a,的计算1
class Power_supply_income_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['power_supply_capacity_20'] != '' and val['power_supply_capacity_20'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None:
            power_supply_income_20 = (float(val['power_supply_capacity_20']))*(float(val['energy_supply_price']))/1.17
            result.power_supply_income_20 = power_supply_income_20
        print(result)


# 实现字段heating_water_income_20:供热水收入-万元/a,的计算2
class Heating_water_income_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_for_heating_20'] != '' and val['energy_supply_for_heating_20'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None:
            heating_water_income_20 = (float(val['energy_supply_for_heating_20']))*(float(val['energy_supply_water_price']))/1.11
            result.heating_water_income_20 = heating_water_income_20
        print(result)


# 实现字段heating_income_20:供暖收入-万元/a,的计算3
class Heating_income_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_heating_20'] != '' and val['energy_supply_heating_20'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None:
            heating_income_20 = (float(val['energy_supply_heating_20']))*(float(val['energy_supply_for_heating']))/1.11
            result.heating_income_20 = heating_income_20
        print(result)


# 实现字段cooling_income_20:供冷收入-万元/a,的计算4
class Cooling_income_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_for_cooling_20'] != '' and val['energy_supply_for_cooling_20'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            cooling_income_20 = (float(val['energy_supply_for_cooling_20']))*(float(val['energy_supply_refrigeration_price']))/1.11
            result.cooling_income_20 = cooling_income_20
        print(result)


# 实现字段steam_supply_20:供蒸汽收入-万元/a(增值税11%),的计算5
class Steam_supply_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['vapour_production_20'] != '' and val['vapour_production_20'] is not None:
            steam_supply_20 = (float(val['vapour_production_20']))*(float(val['energy_supply_steam_price']))/1.11
            result.steam_supply_20 = steam_supply_20
        print(result)


# 实现字段gas_cost_20:燃气费用-万元/a,的计算6
class Gas_cost_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['gas_consumption_20'] != '' and val['gas_consumption_20'] is not None:
            gas_cost_20 = (float(val['gas_consumption_20']))*(float(val['natural_gas_price']))/1.13
            result.gas_cost_20 = gas_cost_20
        print(result)


# 实现字段coal_cost_20:燃煤费用-万元/a,的计算7
class Coal_cost_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['coal_price'] != '' and val['coal_price'] is not None and val['coal_consumption_20'] != '' and val['coal_consumption_20'] is not None:
            coal_cost_20 = (float(val['coal_consumption_20']))*(float(val['coal_price']))/1.13
            result.coal_cost_20 = coal_cost_20
        print(result)


# 实现字段power_cost_20:电力成本-万元/a,的计算8
class Power_cost_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['power_consumption_20'] != '' and val['power_consumption_20'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None:
            power_cost_20 = (float(val['power_consumption_20']))*(float(val['electricity_price']))/1.17
            result.power_cost_20 = power_cost_20
        print(result)


# 实现字段cost_of_water_consumption_20:耗水成本-万元/a,的计算9
class Cost_of_water_consumption_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['water_consumption_20'] != '' and val['water_consumption_20'] is not None and val['water_price'] != '' and val['water_price'] is not None:
            cost_of_water_consumption_20 = (float(val['water_consumption_20']))*(float(val['water_price']))/1.13
            result.cost_of_water_consumption_20 = cost_of_water_consumption_20
        print(result)


# 实现字段depreciation_amortization_20:折旧摊销-万元(15年,5%残值)（建筑最少20年，设备最少8年）,的计算10
class Depreciation_amortization_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['depreciation_amortization_years'] == '8' or val['depreciation_amortization_years'] == '15':
            result.depreciation_amortization_20 = 0.0
        elif val['new_investment'] != '' and val['new_investment'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None:
            depreciation_amortization_20 = (float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))
            result.depreciation_amortization_20 = depreciation_amortization_20
        print(result)


# 实现字段total_sales_20:总销售额-万元,的计算11
class Total_sales_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['power_supply_capacity_20'] != '' and val['power_supply_capacity_20'] is not None and val['energy_supply_for_heating_20'] != '' and val['energy_supply_for_heating_20'] is not None and val['energy_supply_heating_20'] != '' and val['energy_supply_heating_20'] is not None and val['energy_supply_for_cooling_20'] != '' and val['energy_supply_for_cooling_20'] is not None and val['vapour_production_20'] != '' and val['vapour_production_20'] is not None and val['income_otherother_20'] != '' and val['income_otherother_20'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            total_sales_20 = ((float(val['power_supply_capacity_20']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_20']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_20']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_20']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_20']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_20']))
            result.total_sales_20 = total_sales_20
        print(result)


# 实现字段total_cost_20:总成本-万元,的计算12
class Total_cost_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        oldnew_investment = val['new_investment']
        if val['depreciation_amortization_years'] == '8':
            val['new_investment'] = '0'
        elif val['depreciation_amortization_years'] == '15':
            val['new_investment'] = '0'
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['gas_consumption_20'] != '' and val['gas_consumption_20'] is not None and val['coal_consumption_20'] != '' and val['coal_consumption_20'] is not None and val['power_consumption_20'] != '' and val['power_consumption_20'] is not None and val['water_consumption_20'] != '' and val['water_consumption_20'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_20'] != '' and val['material_cost_20'] is not None and val['maintenance_cost_20'] != '' and val['maintenance_cost_20'] is not None and val['artificial_cost_20'] != '' and val['artificial_cost_20'] is not None and val['otherincluding_rent_capacity_20'] != '' and val['otherincluding_rent_capacity_20'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None:
            total_cost_20 = (((float(val['gas_consumption_20']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_20']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_20']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_20']))*(float(val['water_price']))/1.13)+(float(val['material_cost_20']))+(float(val['maintenance_cost_20']))+(float(val['artificial_cost_20']))+(float(val['otherincluding_rent_capacity_20'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years'])))
            result.total_cost_20 = total_cost_20
        val['new_investment'] = oldnew_investment
        print(result)


# 实现字段pre_tax_profit_20:税前利润-万元,的计算13
class Pre_tax_profit_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['power_supply_capacity_20'] != '' and val['power_supply_capacity_20'] is not None and val['energy_supply_for_heating_20'] != '' and val['energy_supply_for_heating_20'] is not None and val['energy_supply_heating_20'] != '' and val['energy_supply_heating_20'] is not None and val['energy_supply_for_cooling_20'] != '' and val['energy_supply_for_cooling_20'] is not None and val['vapour_production_20'] != '' and val['vapour_production_20'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_20'] != '' and val['income_otherother_20'] is not None and val['gas_consumption_20'] != '' and val['gas_consumption_20'] is not None and val['coal_consumption_20'] != '' and val['coal_consumption_20'] is not None and val['power_consumption_20'] != '' and val['power_consumption_20'] is not None and val['water_consumption_20'] != '' and val['water_consumption_20'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_20'] != '' and val['material_cost_20'] is not None and val['maintenance_cost_20'] != '' and val['maintenance_cost_20'] is not None and val['artificial_cost_20'] != '' and val['artificial_cost_20'] is not None and val['otherincluding_rent_capacity_20'] != '' and val['otherincluding_rent_capacity_20'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            pre_tax_profit_20 = (((float(val['power_supply_capacity_20']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_20']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_20']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_20']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_20']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_20'])))-((((float(val['gas_consumption_20']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_20']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_20']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_20']))*(float(val['water_price']))/1.13)+(float(val['material_cost_20']))+(float(val['maintenance_cost_20']))+(float(val['artificial_cost_20']))+(float(val['otherincluding_rent_capacity_20'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest'])))
            result.pre_tax_profit_20 = pre_tax_profit_20
        print(result)


# 实现字段post_tax_profit_20:税后利润-万元(享受三免三减半）,的计算14
class Post_tax_profit_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['power_supply_capacity_20'] != '' and val['power_supply_capacity_20'] is not None and val['energy_supply_for_heating_20'] != '' and val['energy_supply_for_heating_20'] is not None and val['energy_supply_heating_20'] != '' and val['energy_supply_heating_20'] is not None and val['energy_supply_for_cooling_20'] != '' and val['energy_supply_for_cooling_20'] is not None and val['vapour_production_20'] != '' and val['vapour_production_20'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_20'] != '' and val['income_otherother_20'] is not None and val['gas_consumption_20'] != '' and val['gas_consumption_20'] is not None and val['coal_consumption_20'] != '' and val['coal_consumption_20'] is not None and val['power_consumption_20'] != '' and val['power_consumption_20'] is not None and val['water_consumption_20'] != '' and val['water_consumption_20'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_20'] != '' and val['material_cost_20'] is not None and val['maintenance_cost_20'] != '' and val['maintenance_cost_20'] is not None and val['artificial_cost_20'] != '' and val['artificial_cost_20'] is not None and val['otherincluding_rent_capacity_20'] != '' and val['otherincluding_rent_capacity_20'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['post_tax_profit_vat'] != '' and val['post_tax_profit_vat'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            post_tax_profit_20 = ((((float(val['power_supply_capacity_20']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_20']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_20']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_20']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_20']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_20'])))-((((float(val['gas_consumption_20']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_20']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_20']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_20']))*(float(val['water_price']))/1.13)+(float(val['material_cost_20']))+(float(val['maintenance_cost_20']))+(float(val['artificial_cost_20']))+(float(val['otherincluding_rent_capacity_20'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest']))))*(1-(float(val['post_tax_profit_vat'])))
            result.post_tax_profit_20 = post_tax_profit_20
        print(result)


# 实现字段cash_flow_20:经营现金流-万元,的计算15
class Cash_flow_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        oldnew_investment = val['new_investment']
        if val['depreciation_amortization_years'] == '8':
            val['new_investment'] = '0'
        elif val['depreciation_amortization_years'] == '15':
            val['new_investment'] = '0'
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['power_supply_capacity_20'] != '' and val['power_supply_capacity_20'] is not None and val['energy_supply_for_heating_20'] != '' and val['energy_supply_for_heating_20'] is not None and val['energy_supply_heating_20'] != '' and val['energy_supply_heating_20'] is not None and val['energy_supply_for_cooling_20'] != '' and val['energy_supply_for_cooling_20'] is not None and val['vapour_production_20'] != '' and val['vapour_production_20'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_20'] != '' and val['income_otherother_20'] is not None and val['gas_consumption_20'] != '' and val['gas_consumption_20'] is not None and val['coal_consumption_20'] != '' and val['coal_consumption_20'] is not None and val['power_consumption_20'] != '' and val['power_consumption_20'] is not None and val['water_consumption_20'] != '' and val['water_consumption_20'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_20'] != '' and val['material_cost_20'] is not None and val['maintenance_cost_20'] != '' and val['maintenance_cost_20'] is not None and val['artificial_cost_20'] != '' and val['artificial_cost_20'] is not None and val['otherincluding_rent_capacity_20'] != '' and val['otherincluding_rent_capacity_20'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['post_tax_profit_vat'] != '' and val['post_tax_profit_vat'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            cash_flow_20 = (((((float(val['power_supply_capacity_20']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_20']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_20']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_20']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_20']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_20'])))-((((float(val['gas_consumption_20']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_20']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_20']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_20']))*(float(val['water_price']))/1.13)+(float(val['material_cost_20']))+(float(val['maintenance_cost_20']))+(float(val['artificial_cost_20']))+(float(val['otherincluding_rent_capacity_20'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest']))))*(1-(float(val['post_tax_profit_vat']))))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years'])))
            result.cash_flow_20 = cash_flow_20
        val['new_investment'] = oldnew_investment
        print(result)


# 实现字段bank_loan_balance_20:银行借款余额-万元,的计算16
class Bank_loan_balance_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None:
            bank_loan_balance_20 = (float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x']))
            result.bank_loan_balance_20 = bank_loan_balance_20
            if bank_loan_balance_20 < 0:
                result.bank_loan_balance_20 = 0
        print(result)


# 实现字段bank_interest_20:银行利息-万元(利率7.5%),的计算17
class Bank_interest_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None:
            bank_interest_20 = ((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest']))
            result.bank_interest_20 = bank_interest_20
        print(result)


# 实现字段net_cash_flow_20:净现金流-万元,的计算18
class Net_cash_flow_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['power_supply_capacity_20'] != '' and val['power_supply_capacity_20'] is not None and val['energy_supply_for_heating_20'] != '' and val['energy_supply_for_heating_20'] is not None and val['energy_supply_heating_20'] != '' and val['energy_supply_heating_20'] is not None and val['energy_supply_for_cooling_20'] != '' and val['energy_supply_for_cooling_20'] is not None and val['vapour_production_20'] != '' and val['vapour_production_20'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_20'] != '' and val['income_otherother_20'] is not None and val['gas_consumption_20'] != '' and val['gas_consumption_20'] is not None and val['coal_consumption_20'] != '' and val['coal_consumption_20'] is not None and val['power_consumption_20'] != '' and val['power_consumption_20'] is not None and val['water_consumption_20'] != '' and val['water_consumption_20'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_20'] != '' and val['material_cost_20'] is not None and val['maintenance_cost_20'] != '' and val['maintenance_cost_20'] is not None and val['artificial_cost_20'] != '' and val['artificial_cost_20'] is not None and val['otherincluding_rent_capacity_20'] != '' and val['otherincluding_rent_capacity_20'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['post_tax_profit_vat'] != '' and val['post_tax_profit_vat'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            net_cash_flow_20 = ((((((float(val['power_supply_capacity_20']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_20']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_20']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_20']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_20']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_20'])))-((((float(val['gas_consumption_20']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_20']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_20']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_20']))*(float(val['water_price']))/1.13)+(float(val['material_cost_20']))+(float(val['maintenance_cost_20']))+(float(val['artificial_cost_20']))+(float(val['otherincluding_rent_capacity_20'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest']))))*(1-(float(val['post_tax_profit_vat']))))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))
            result.net_cash_flow_20 = net_cash_flow_20
        print(result)


# 实现字段cumulative_cash_flow_20:累计现金流-万元,的计算19
class Cumulative_cash_flow_20(FieldCalculation):
    def notify(self, val):
        result = val['dbresult']
        if val['natural_gas_price'] != '' and val['natural_gas_price'] is not None and val['energy_supply_steam_price'] != '' and val['energy_supply_steam_price'] is not None and val['bank_loan_balance_x'] != '' and val['bank_loan_balance_x'] is not None and val['repayment_plan_x'] != '' and val['repayment_plan_x'] is not None and val['cumulative_cash_flow_x'] != '' and val['cumulative_cash_flow_x'] is not None and val['power_supply_capacity_20'] != '' and val['power_supply_capacity_20'] is not None and val['energy_supply_for_heating_20'] != '' and val['energy_supply_for_heating_20'] is not None and val['energy_supply_heating_20'] != '' and val['energy_supply_heating_20'] is not None and val['energy_supply_for_cooling_20'] != '' and val['energy_supply_for_cooling_20'] is not None and val['vapour_production_20'] != '' and val['vapour_production_20'] is not None and val['coal_price'] != '' and val['coal_price'] is not None and val['income_otherother_20'] != '' and val['income_otherother_20'] is not None and val['gas_consumption_20'] != '' and val['gas_consumption_20'] is not None and val['coal_consumption_20'] != '' and val['coal_consumption_20'] is not None and val['power_consumption_20'] != '' and val['power_consumption_20'] is not None and val['water_consumption_20'] != '' and val['water_consumption_20'] is not None and val['water_price'] != '' and val['water_price'] is not None and val['material_cost_20'] != '' and val['material_cost_20'] is not None and val['maintenance_cost_20'] != '' and val['maintenance_cost_20'] is not None and val['artificial_cost_20'] != '' and val['artificial_cost_20'] is not None and val['otherincluding_rent_capacity_20'] != '' and val['otherincluding_rent_capacity_20'] is not None and val['electricity_price'] != '' and val['electricity_price'] is not None and val['new_investment'] != '' and val['new_investment'] is not None and val['energy_supply_price'] != '' and val['energy_supply_price'] is not None and val['depreciation_amortization_years'] != '' and val['depreciation_amortization_years'] is not None and val['post_tax_profit_vat'] != '' and val['post_tax_profit_vat'] is not None and val['energy_supply_water_price'] != '' and val['energy_supply_water_price'] is not None and val['interest_rate_bank_interest'] != '' and val['interest_rate_bank_interest'] is not None and val['energy_supply_for_heating'] != '' and val['energy_supply_for_heating'] is not None and val['energy_supply_refrigeration_price'] != '' and val['energy_supply_refrigeration_price'] is not None:
            cumulative_cash_flow_20 = (((((((float(val['power_supply_capacity_20']))*(float(val['energy_supply_price']))/1.17)+((float(val['energy_supply_for_heating_20']))*(float(val['energy_supply_water_price']))/1.11)+((float(val['energy_supply_heating_20']))*(float(val['energy_supply_for_heating']))/1.11)+((float(val['energy_supply_for_cooling_20']))*(float(val['energy_supply_refrigeration_price']))/1.11)+((float(val['vapour_production_20']))*(float(val['energy_supply_steam_price']))/1.11)+(float(val['income_otherother_20'])))-((((float(val['gas_consumption_20']))*(float(val['natural_gas_price']))/1.13)+((float(val['coal_consumption_20']))*(float(val['coal_price']))/1.13)+((float(val['power_consumption_20']))*(float(val['electricity_price']))/1.17)+((float(val['water_consumption_20']))*(float(val['water_price']))/1.13)+(float(val['material_cost_20']))+(float(val['maintenance_cost_20']))+(float(val['artificial_cost_20']))+(float(val['otherincluding_rent_capacity_20'])))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years']))))-(((float(val['bank_loan_balance_x']))-(float(val['repayment_plan_x'])))*(float(val['interest_rate_bank_interest']))))*(1-(float(val['post_tax_profit_vat']))))+((float(val['new_investment']))*0.95/(float(val['depreciation_amortization_years'])))))+(float(val['cumulative_cash_flow_x']))
            result.cumulative_cash_flow_20 = cumulative_cash_flow_20
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
        calculationObserver.register(Power_supply_income_20())
        calculationObserver.register(Heating_water_income_20())
        calculationObserver.register(Heating_income_20())
        calculationObserver.register(Cooling_income_20())
        calculationObserver.register(Steam_supply_20())
        calculationObserver.register(Gas_cost_20())
        calculationObserver.register(Coal_cost_20())
        calculationObserver.register(Power_cost_20())
        calculationObserver.register(Cost_of_water_consumption_20())
        calculationObserver.register(Depreciation_amortization_20())
        calculationObserver.register(Total_sales_20())
        calculationObserver.register(Total_cost_20())
        calculationObserver.register(Pre_tax_profit_20())
        calculationObserver.register(Post_tax_profit_20())
        calculationObserver.register(Cash_flow_20())
        calculationObserver.register(Bank_loan_balance_20())
        calculationObserver.register(Bank_interest_20())
        calculationObserver.register(Net_cash_flow_20())
        calculationObserver.register(Cumulative_cash_flow_20())
        # calculationObserver.register(Capital())
        # calculationObserver.register(Bank_loan())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, dbmodel, form):
        val = {
            'flg': 'design',
            'material_cost_20': form.get('material_cost_20'),
            'electricity_price': form.get('electricity_price'),
            'otherincluding_rent_capacity_20': form.get('otherincluding_rent_capacity_20'),
            'cumulative_cash_flow_x': dbmodel.cumulative_cash_flow_19,
            'repayment_plan_x': form.get('repayment_plan_19'),
            'power_consumption_20': form.get('power_consumption_20'),
            'vapour_production_20': form.get('vapour_production_20'),
            'energy_supply_heating_20': form.get('energy_supply_heating_20'),
            'energy_supply_for_heating_20': form.get('energy_supply_for_heating_20'),
            'purchase_cost': form.get('purchase_cost'),
            'post_tax_profit_vat': form.get('post_tax_profit_vat'),
            'energy_supply_price': form.get('energy_supply_price'),
            'water_price': form.get('water_price'),
            'coal_price': form.get('coal_price'),
            'depreciation_amortization_years': form.get('depreciation_amortization_years'),
            'energy_supply_refrigeration_price': form.get('energy_supply_refrigeration_price'),
            'gas_consumption_20': form.get('gas_consumption_20'),
            'energy_supply_water_price': form.get('energy_supply_water_price'),
            'energy_supply_for_cooling_20': form.get('energy_supply_for_cooling_20'),
            'maintenance_cost_20': form.get('maintenance_cost_20'),
            'bank_loan_balance_x': dbmodel.bank_loan_balance_19,
            'coal_consumption_20': form.get('coal_consumption_20'),
            'power_supply_capacity_20': form.get('power_supply_capacity_20'),
            'energy_supply_for_heating': form.get('energy_supply_for_heating'),
            'artificial_cost_20': form.get('artificial_cost_20'),
            'new_investment': form.get('new_investment'),
            'income_otherother_20': form.get('income_otherother_20'),
            'natural_gas_price': form.get('natural_gas_price'),
            'energy_supply_steam_price': form.get('energy_supply_steam_price'),
            'interest_rate_bank_interest': form.get('interest_rate_bank_interest'),
            'percentage_capital_total_investment': form.get('percentage_capital_total_investment'),
            'water_consumption_20': form.get('water_consumption_20'),
            'dbresult': dbmodel}
        if val['depreciation_amortization_years'] == '8':
            val['new_investment'] = '0'
        elif val['depreciation_amortization_years'] == '15':
            val['new_investment'] = '0'
        self.creatSubscriber(val)
        return val['dbresult']
