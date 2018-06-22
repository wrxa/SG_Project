# -*- coding: utf-8 -*-
from app.ccpp.models.constantModel import CcppConstant
from datetime import datetime
from app.models import Plan
from app.ccpp import gl
from app.ccpp.models.ccpp_chimney_calculateModel import CcppChimneyCalculate
from app.ccpp.service.ccpp_chimney_strategy import Ccpp_chimney_calculateBefore
from app import db

"""
ccpp_chimney_calculate：sheet的服务处理程序
"""


list_column_chimneycalculate = [
    'inner_diameter_chimney',
    'flue_gas_flow_velocity',
    'temperature_exhaust_smoke',
    'pressure_exhaust_smoke',
    'flue_gas_quantity',
    'engine_num_design'
]


class ChimneyCalculateService():
    '''
    加载字段常量数据
    '''
    @staticmethod
    def getChimneyCalculateConstant():
        ccppConstant = CcppConstant.search_ccppConstant('ccpp_chimney_calculate')
        gl.listsort(ccppConstant)
        return ccppConstant

    # 根据plan_id删除实体
    def deletebyPlanId(self, plan_id):
        chimney_calculate = \
            CcppChimneyCalculate.search_chimney_calculate(plan_id)
        db.session.delete(chimney_calculate)

    # 根据plan_id查询实体
    def search_chimney_calculate(self, plan_id):
        return CcppChimneyCalculate.search_chimney_calculate(plan_id)

    # 根据plan_id更新实体
    def updata_chimney_calculate(self, chimneyCalculate):
        CcppChimneyCalculate.updata_chimney_calculate(chimneyCalculate)

    def to_ChimneyCalculateJson(self, chimneycalculate):
        datas = {}
        for index in range(len(list_column_chimneycalculate)):
            datas[list_column_chimneycalculate[index]] = gl.format_value(getattr(chimneycalculate, list_column_chimneycalculate[index]))
        return datas

    def to_ChimneyCalculate(self, form, plan_id):
        chimneyCalculate = CcppChimneyCalculate.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_chimneycalculate)):
            val = form.get(list_column_chimneycalculate[index])
            if val is not None and val != '':
                setattr(chimneyCalculate, list_column_chimneycalculate[index], val)
            else:
                setattr(chimneyCalculate, list_column_chimneycalculate[index], None)
        setattr(chimneyCalculate, 'plan_id', plan_id)
        Ccpp_chimney_calculateBefore().specialCalculation(chimneyCalculate, form)
        return chimneyCalculate

    def update_plan_date(self, plan_id):
        plan = Plan.query.filter_by(id=plan_id).first()
        plan.plan_update_date = datetime.now()
        Plan.insert_plan(plan)
