# -*- coding: utf-8 -*-
from app.ccpp.models.ccpp_biomassModel import CcppCHPWaterTreatment
from app.ccpp.models.ccpp_questionnaireModel import Questionnaire
from app.ccpp.models.ccpp_turbineModel import CcppTurbine
from app import db

list_column_water = [
    'o_steam_flow',
    'o_loss_factory',
    'o_boiler_blowdown_loss',
    'o_start_accident_increase_loss',
    'o_external_supply_loss',
    'o_water_consumption',
    'o_boiler_water_normal',
    'o_boiler_water_max',
    'o_boiler_water_system',
    'o_salt_water_tank',
    'o_process_route'
]


# 格式化数据库取出的值
def format_value(flag, values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if not values or values == "null" or values == "None":
        result = ""
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        # result = float(str(float(values)).rstrip('0'))
        result = round(float(str(float(values)).rstrip('0')), 2)
    else:
        result = values
    return result


class BiomassService():

    # 根据plan_id删除实体
    def deletebyPlanId(self, plan_id):
        water = CcppCHPWaterTreatment.search_water(plan_id)
        db.session.delete(water)

    # 返回化学水处理页面初期值
    @staticmethod
    def to_waterJson(water):
        datas = {}
        for index in range(len(list_column_water)):
            datas[list_column_water[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(water, list_column_water[index])))

        return datas

    # 获得化学水处理页面表单的信息
    @staticmethod
    def to_water(form, plan_id):
        water = CcppCHPWaterTreatment.query.filter_by(
            plan_id=plan_id).first()
        for index in range(len(list_column_water)):
            val = form.get(list_column_water[index])
            if val is not None and val != '':
                setattr(water, list_column_water[index], val)
            else:
                setattr(water, list_column_water[index], None)

        # 查询凝结水回收率和抽汽点流量，来计算外供汽损失
        questionnaire = Questionnaire.search_questionnaire(plan_id)
        waterRecoveryRate = getattr(questionnaire, 'rrcw_1')
        steam = CcppTurbine.search_CcppTurbine(plan_id)
        pointFlow = getattr(steam, 'e_exhaust_point_flow')
        # if pointFlow != None or pointFlow != '':
        if pointFlow >= 0:
                externalSupplyLoss = pointFlow * (1 - waterRecoveryRate / 100)
                setattr(water, 'o_external_supply_loss', externalSupplyLoss)
        return water
