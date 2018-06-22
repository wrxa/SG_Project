# -*- coding: utf-8 -*-
from app.main.service.economic import economic_indicators_calculation

class Factory():
    def execute(self, dbobj, form):

        result = economic_indicators_calculation.Economic_EXEC().specialCalculation(dbobj, form)
        return result
