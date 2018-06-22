# -*- coding: utf-8 -*-
from __future__ import division


class Observer:
    def __init__(self):
        pass

    def register(self):
        pass

    def unregister(self):
        pass

    def notifyAll(self):
        pass


class CalculationObserver(Observer):
    def __init__(self):
        self._listOfObj = []
        self.val = None

    def register(self, obj):
        if obj not in self._listOfObj:
            self._listOfObj.append(obj)

    def notifyAll(self):
        for objects in self._listOfObj:
            print(objects)
            objects.notify(self.val)

    def writeNewPost(self, val):
        val['interest_rate_bank_interest'] = float(val['interest_rate_bank_interest']) / 100
        val['percentage_capital_total_investment'] = float(val['percentage_capital_total_investment']) / 100
        val['post_tax_profit_vat'] = float(val['post_tax_profit_vat']) / 100
        self.val = val
        self.notifyAll()


class FieldCalculation:
    def __init__(self):
        pass

    def notify(self):
        pass


class ExecuteStrategy:
    def __init__(self):
        pass

    def creatSubscriber(self):
        pass

    def specialCalculation(self, val):
        pass
