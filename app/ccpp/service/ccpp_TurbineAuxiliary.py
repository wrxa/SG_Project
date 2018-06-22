# -*- coding: utf-8 -*-
from app import db
from app.biomass_chp.models.modelsBiomass import BiomasschpTurbineAuxiliary as ccppTurbineAuxiliary

'''
删除唐姐的删除还未完善，在不影响唐姐的代码情况下自己写删除汽机辅机方案，
其他业务代码，表、model均使用生物质模块的代码。因为客户的需求是此模块从生物质拿来。
'''


class CcppTurbineAuxiliaryService():

    # 根据plan_id删除实体
    def deletebyPlanId(self, plan_id):
        turbineAuxiliary = ccppTurbineAuxiliary.search_turbine_auxiliary(plan_id)
        db.session.delete(turbineAuxiliary)