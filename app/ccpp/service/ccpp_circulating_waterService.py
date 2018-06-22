# -*- coding: utf-8 -*-
from app.ccpp.models.constantModel import CcppConstant
from app.models import Plan
from app.ccpp.models.ccpp_circulating_waterModel import CcppCirculatingWater
from app.ccpp import gl
from datetime import datetime
from app import db


"""
ccpp_circulating_water：sheet的服务处理程序
"""

list_column_circulatingWater = [
    'v_steam_exhaust_flow_winter', 'v_steam_exhaust_flow_summer',
    'v_steam_exhaust_flow_select', 'v_circulating_ratio_winter',
    'v_circulating_ratio_summer', 'v_circulating_water_winter',
    'v_circulating_water_summer', 'v_auxiliary_engine_cooling_winter',
    'v_auxiliary_engine_cooling_summer', 'v_total_circulating_water_winter',
    'v_total_circulating_water_summer', 'v_total_circulating_water_select',
    'v_enter_the_outlet_temperature_difference', 'v_dry_bulb_temperature',
    'v_up_dry_bulb_temperature', 'v_down_dry_bulb_temperature', 'v_up_k',
    'v_down_k', 'v_k', 'v_evaporation_loss_rate', 'v_evaporation_loss',
    'v_blowing_loss_rate', 'v_partial_blow_loss', 'v_concentrate_ratio',
    'v_discharge_loss', 'v_discharge_capacity', 'v_amount_of_makeup_water',
    'v_circulating_pool_size', 'v_circulating_pool_long',
    'v_circulating_pool_wide', 'v_circulating_pool_hight',
    'v_check_circulating_pool_size', 'p_spray_density', 'p_spray_area',
    'p_select_f', 'p_count', 'p_single_cold_amount', 'p_select_s',
    'c_pressure_condenser', 'c_condenser_tube_friction',
    'c_circulating_water_pressure', 'c_circulating_pool_pressure',
    'c_circulation_height_difference', 'c_height_difference_inlet',
    'c_pipe_losses', 'c_y_losses', 'c_pumping_head', 'c_flow', 'c_pump_power',
    'c_mechine_power', 'c_motor_power', 'c_motor_backup_coefficient',
    'c_supporting_motor_power', 'c_forklift_parameters_power',
    'c_forklift_parameters_flow', 'c_forklift_parameters_lift'
]


class CirculatingWaterService():

    '''
    加载字段常量数据
    '''
    @staticmethod
    def getCirculatingWaterConstant():
        constant = CcppConstant.search_ccppConstant('ccpp_circulatingWater')
        gl.listsort(constant)
        return constant

    # 根据plan_id删除实体
    def deletebyPlanId(self, plan_id):
        circulating_water = \
            CcppCirculatingWater.search_circulating_water(plan_id)
        db.session.delete(circulating_water)

    # 根据plan_id查询实体
    def search_circulating_water(self, plan_id):
        return CcppCirculatingWater.search_circulating_water(plan_id)

    # 根据plan_id更新实体
    def insert_circulating_water(self, circulatingWater):
        CcppCirculatingWater.updata_circulating_water(circulatingWater)

    def to_circulatingWaterJson(self, circulatingWater):
        datas = {}
        for index in range(len(list_column_circulatingWater)):
            datas[list_column_circulatingWater[index]] = gl.format_value(getattr(circulatingWater, list_column_circulatingWater[index]))
        return datas

    def to_circulatingWater(self, form, plan_id):
        circulatingWater = CcppCirculatingWater.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_circulatingWater)):
            val = form.get(list_column_circulatingWater[index])
            if val is not None and val != '':
                setattr(circulatingWater, list_column_circulatingWater[index],
                        form.get(list_column_circulatingWater[index]))
            else:
                setattr(circulatingWater, list_column_circulatingWater[index],
                        None)
        setattr(circulatingWater, 'plan_id', plan_id)
        return circulatingWater

    def update_plan_date(self, plan_id):
        plan = Plan.query.filter_by(id=plan_id).first()
        plan.plan_update_date = datetime.now()
        Plan.insert_plan(plan)
    
    # 根据plan_id更新实体
    def updata_circulating_water(self, CcppCirculatingWater):
        CcppCirculatingWater.updata_circulating_water(CcppCirculatingWater)
  
