
# -*- coding: utf-8 -*-
from . import ccpp_economic_calculation1, ccpp_economic_calculation2, ccpp_economic_calculation3, ccpp_economic_calculation4, ccpp_economic_calculation5, ccpp_economic_calculation6, ccpp_economic_calculation7, ccpp_economic_calculation8, ccpp_economic_calculation9, ccpp_economic_calculation10, ccpp_economic_calculation11, ccpp_economic_calculation12, ccpp_economic_calculation13, ccpp_economic_calculation14, ccpp_economic_calculation15, ccpp_economic_calculation16, ccpp_economic_calculation17, ccpp_economic_calculation18, ccpp_economic_calculation19, ccpp_economic_calculation20
import numpy


class Factory():
    def execute(self, dbobj, form):
        dbobj = ccpp_economic_calculation1.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation2.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation3.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation4.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation5.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation6.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation7.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation8.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation9.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation10.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation11.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation12.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation13.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation14.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation15.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation16.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation17.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation18.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation19.Economic_EXEC().specialCalculation(dbobj, form)
        dbobj = ccpp_economic_calculation20.Economic_EXEC().specialCalculation(dbobj, form)
        # 补充计算
        '''
        动态投资回收期-年(不含建设期):dynamic_recovery_period=
        计算流程：
        1、将53：累计现金流-万元进行排序，查找出满足条件【x<0, (x+1)>0】的x
        2、公式的第二个参数如何确定？？？？
        3、哪一行当初说过如果计算出来小于0时，则将其赋值为0？？？？？
        '''
        cumulative_cash_flow_list = [dbobj.cumulative_cash_flow_1, dbobj.cumulative_cash_flow_2, dbobj.cumulative_cash_flow_3, dbobj.cumulative_cash_flow_4,
                                     dbobj.cumulative_cash_flow_5, dbobj.cumulative_cash_flow_6, dbobj.cumulative_cash_flow_7, dbobj.cumulative_cash_flow_8,
                                     dbobj.cumulative_cash_flow_9, dbobj.cumulative_cash_flow_10, dbobj.cumulative_cash_flow_11, dbobj.cumulative_cash_flow_12,
                                     dbobj.cumulative_cash_flow_13, dbobj.cumulative_cash_flow_14, dbobj.cumulative_cash_flow_15, dbobj.cumulative_cash_flow_16,
                                     dbobj.cumulative_cash_flow_17, dbobj.cumulative_cash_flow_18, dbobj.cumulative_cash_flow_19, dbobj.cumulative_cash_flow_20]
        net_cash_flow_list = [dbobj.net_cash_flow_1, dbobj.net_cash_flow_2, dbobj.net_cash_flow_3, dbobj.net_cash_flow_4,
                              dbobj.net_cash_flow_5, dbobj.net_cash_flow_6, dbobj.net_cash_flow_7, dbobj.net_cash_flow_8,
                              dbobj.net_cash_flow_9, dbobj.net_cash_flow_10, dbobj.net_cash_flow_11, dbobj.net_cash_flow_12,
                              dbobj.net_cash_flow_13, dbobj.net_cash_flow_14, dbobj.net_cash_flow_15, dbobj.net_cash_flow_16,
                              dbobj.net_cash_flow_17, dbobj.net_cash_flow_18, dbobj.net_cash_flow_19, dbobj.net_cash_flow_20]

        i = 0
        parameter1 = 0
        parameter2 = 0
        for cumulative_cash_flow in cumulative_cash_flow_list:
            if cumulative_cash_flow > 0:
                if i - 1 >= 0:
                    parameter1 = cumulative_cash_flow_list[i - 1]
                parameter2 = net_cash_flow_list[i]
                break
            i += 1
        if parameter2 != 0:
            dbobj.dynamic_recovery_period = (7 - parameter1 / parameter2)
        else:
            dbobj.dynamic_recovery_period = 0

        '''
        总投资收益率:total_return_investment=
        计算流程：(sum(pre_tax_profit_x)+sum(bank_interest_x))/new_investment/20
        '''
        
        pre_tax_profit_sum = (dbobj.pre_tax_profit_1 + dbobj.pre_tax_profit_2 + dbobj.pre_tax_profit_3 +
                              dbobj.pre_tax_profit_4 + dbobj.pre_tax_profit_5 + dbobj.pre_tax_profit_6 + dbobj.pre_tax_profit_7 +
                              dbobj.pre_tax_profit_8 + dbobj.pre_tax_profit_9 + dbobj.pre_tax_profit_10 + dbobj.pre_tax_profit_11 +
                              dbobj.pre_tax_profit_12 + dbobj.pre_tax_profit_13 + dbobj.pre_tax_profit_14 + dbobj.pre_tax_profit_15 +
                              dbobj.pre_tax_profit_16 + dbobj.pre_tax_profit_17 + dbobj.pre_tax_profit_18 + dbobj.pre_tax_profit_19 +
                              dbobj.pre_tax_profit_20)
        bank_interest_sum = (dbobj.bank_interest_1 + dbobj.bank_interest_2 + dbobj.bank_interest_3 +
                             dbobj.bank_interest_4 + dbobj.bank_interest_5 + dbobj.bank_interest_6 + dbobj.bank_interest_7 +
                             dbobj.bank_interest_8 + dbobj.bank_interest_9 + dbobj.bank_interest_10 + dbobj.bank_interest_11 +
                             dbobj.bank_interest_12 + dbobj.bank_interest_13 + dbobj.bank_interest_14 + dbobj.bank_interest_15 +
                             dbobj.bank_interest_16 + dbobj.bank_interest_17 + dbobj.bank_interest_18 + dbobj.bank_interest_19 +
                             dbobj.bank_interest_20)
        if float(dbobj.new_investment) != 0.0:
            dbobj.total_return_investment = ((pre_tax_profit_sum + bank_interest_sum) / float(dbobj.new_investment) / 20) * 100
        else:
            dbobj.total_return_investment = 0

        '''
        NpV-万元:npv=
        计算流程：
        '''
        dbobj.npv = numpy.npv(0.10, [dbobj.net_cash_flow_1, dbobj.net_cash_flow_2, dbobj.net_cash_flow_3, dbobj.net_cash_flow_4,
                                     dbobj.net_cash_flow_5, dbobj.net_cash_flow_6, dbobj.net_cash_flow_7, dbobj.net_cash_flow_8,
                                     dbobj.net_cash_flow_9, dbobj.net_cash_flow_10, dbobj.net_cash_flow_11, dbobj.net_cash_flow_12,
                                     dbobj.net_cash_flow_13, dbobj.net_cash_flow_14, dbobj.net_cash_flow_15, dbobj.net_cash_flow_16,
                                     dbobj.net_cash_flow_17, dbobj.net_cash_flow_18, dbobj.net_cash_flow_19, dbobj.net_cash_flow_20])

        '''
        iRR(全投资内部收益率):irr=
        计算流程：
        '''
        irr = numpy.irr([dbobj.net_cash_flow_1, dbobj.net_cash_flow_2, dbobj.net_cash_flow_3, dbobj.net_cash_flow_4,
                        dbobj.net_cash_flow_5, dbobj.net_cash_flow_6, dbobj.net_cash_flow_7, dbobj.net_cash_flow_8,
                        dbobj.net_cash_flow_9, dbobj.net_cash_flow_10, dbobj.net_cash_flow_11, dbobj.net_cash_flow_12,
                        dbobj.net_cash_flow_13, dbobj.net_cash_flow_14, dbobj.net_cash_flow_15, dbobj.net_cash_flow_16,
                        dbobj.net_cash_flow_17, dbobj.net_cash_flow_18, dbobj.net_cash_flow_19, dbobj.net_cash_flow_20])
        if str(irr) == 'nan':
            dbobj.irr = -123321
        else:
            dbobj.irr = irr * 100
        '''
        全投资收益率（集团规定）:full_investment_yield=
        计算流程：求其平均值，位数的问题？？
        (post_tax_profit_x/n + bank_interest_x/n)/new_investment
        '''
        bank_interestlist = [dbobj.bank_interest_1, dbobj.bank_interest_2, dbobj.bank_interest_3,
                             dbobj.bank_interest_4, dbobj.bank_interest_5, dbobj.bank_interest_6, dbobj.bank_interest_7,
                             dbobj.bank_interest_8, dbobj.bank_interest_9, dbobj.bank_interest_10, dbobj.bank_interest_11,
                             dbobj.bank_interest_12, dbobj.bank_interest_13, dbobj.bank_interest_14, dbobj.bank_interest_15,
                             dbobj.bank_interest_16, dbobj.bank_interest_17, dbobj.bank_interest_18, dbobj.bank_interest_19,
                             dbobj.bank_interest_20]
        
        year = 0
        for i in range(0, 19):
            year = year + 1
            if int(bank_interestlist[i]) == 0 and int(bank_interestlist[i + 1]) == 0:
                break
        
        post_tax_profit_sum20 = (dbobj.post_tax_profit_1 + dbobj.post_tax_profit_2 + dbobj.post_tax_profit_3 +
                                 dbobj.post_tax_profit_4 + dbobj.post_tax_profit_5 + dbobj.post_tax_profit_6 + dbobj.post_tax_profit_7 +
                                 dbobj.post_tax_profit_8 + dbobj.post_tax_profit_9 + dbobj.post_tax_profit_10 + dbobj.post_tax_profit_11 +
                                 dbobj.post_tax_profit_12 + dbobj.post_tax_profit_13 + dbobj.post_tax_profit_14 + dbobj.post_tax_profit_15 +
                                 dbobj.post_tax_profit_16 + dbobj.post_tax_profit_17 + dbobj.post_tax_profit_18 + dbobj.post_tax_profit_19 +
                                 dbobj.post_tax_profit_20)

        bank_interest_sum20 = (dbobj.bank_interest_1 + dbobj.bank_interest_2 + dbobj.bank_interest_3 +
                               dbobj.bank_interest_4 + dbobj.bank_interest_5 + dbobj.bank_interest_6 + dbobj.bank_interest_7 +
                               dbobj.bank_interest_8 + dbobj.bank_interest_9 + dbobj.bank_interest_10 + dbobj.bank_interest_11 +
                               dbobj.bank_interest_12 + dbobj.bank_interest_13 + dbobj.bank_interest_14 + dbobj.bank_interest_15 +
                               dbobj.bank_interest_16 + dbobj.bank_interest_17 + dbobj.bank_interest_18 + dbobj.bank_interest_19 +
                               dbobj.bank_interest_20)
        
        post_tax_profit_sum15 = (dbobj.post_tax_profit_1 + dbobj.post_tax_profit_2 + dbobj.post_tax_profit_3 +
                                 dbobj.post_tax_profit_4 + dbobj.post_tax_profit_5 + dbobj.post_tax_profit_6 + dbobj.post_tax_profit_7 +
                                 dbobj.post_tax_profit_8 + dbobj.post_tax_profit_9 + dbobj.post_tax_profit_10 + dbobj.post_tax_profit_11 +
                                 dbobj.post_tax_profit_12 + dbobj.post_tax_profit_13 + dbobj.post_tax_profit_14 + dbobj.post_tax_profit_15)

        bank_interest_sum15 = (dbobj.bank_interest_1 + dbobj.bank_interest_2 + dbobj.bank_interest_3 +
                               dbobj.bank_interest_4 + dbobj.bank_interest_5 + dbobj.bank_interest_6 + dbobj.bank_interest_7 +
                               dbobj.bank_interest_8 + dbobj.bank_interest_9 + dbobj.bank_interest_10 + dbobj.bank_interest_11 +
                               dbobj.bank_interest_12 + dbobj.bank_interest_13 + dbobj.bank_interest_14 + dbobj.bank_interest_15)

        full_investment_yield_year = form.get('full_investment_yield_year')
        post_tax_profit_sum = 0
        bank_interest_sum = 0
        if full_investment_yield_year == "15":
            post_tax_profit_sum = post_tax_profit_sum15
            bank_interest_sum = bank_interest_sum15
            if dbobj.new_investment == "0":
                dbobj.full_investment_yield = 0
            else:
                dbobj.full_investment_yield = ((post_tax_profit_sum / 15 + bank_interest_sum / year) / float(dbobj.new_investment)) * 100
        elif full_investment_yield_year == "20":
            post_tax_profit_sum = post_tax_profit_sum20
            bank_interest_sum = bank_interest_sum20
            if dbobj.new_investment == "0":
                dbobj.full_investment_yield = 0
            else:
                dbobj.full_investment_yield = ((post_tax_profit_sum / 20 + bank_interest_sum / year) / float(dbobj.new_investment)) * 100
        else:
            dbobj.full_investment_yield = -1

        return dbobj
