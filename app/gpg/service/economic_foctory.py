# -*- coding: utf-8 -*-
from app.gpg.service import economic_indicators_calculation

class Factory():
    def execute(self, dbobj, Boiler, form):

        result = economic_indicators_calculation.Economic_EXEC().specialCalculation(dbobj, Boiler, form)
        return result
