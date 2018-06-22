# -*- coding: utf-8 -*-
from .constantModel import CcppConstant


# ccpp计算表
ccpp_chimney_calculate_data = [{
    "module_name": "ccpp_chimney_calculate",
    "name_eng": "flue_gas_quantity",
    "name": u"烟气量",
    "symbol": u"--",
    "unit": u"NM3/h",
    "calculate": u"--",
    "remark": u"--",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"true"
}, {
    "module_name": "ccpp_chimney_calculate",
    "name_eng": "pressure_exhaust_smoke",
    "name": u"排烟压力",
    "symbol": u"--",
    "unit": u"MPa",
    "calculate": u"厂家样本",
    "remark": u"厂家样本",
    "defaultvalue": u"0.12",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"true"
}, {
    "module_name": "ccpp_chimney_calculate",
    "name_eng": "temperature_exhaust_smoke",
    "name": u"排烟温度",
    "symbol": u"--",
    "unit": u"℃",
    "calculate": u"厂家样本",
    "remark": u"厂家样本",
    "defaultvalue": u"130",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"true"
}, {
    "module_name": "ccpp_chimney_calculate",
    "name_eng": "flue_gas_flow_velocity",
    "name": u"烟气流速",
    "symbol": u"--",
    "unit": u"m/s",
    "calculate": u"--",
    "remark": u"--",
    "defaultvalue": u"70",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"true"
}, {
    "module_name": "ccpp_chimney_calculate",
    "name_eng": "inner_diameter_chimney",
    "name": u"烟囱内径",
    "symbol": u"--",
    "unit": u"m",
    "calculate": u"--",
    "remark": u"--",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
}, {
    "module_name": "ccpp_chimney_calculate",
    "name_eng": "engine_num_design",
    "name": u"烟囱数量",
    "symbol": u"--",
    "unit": u"台",
    "calculate": u"--",
    "remark": u"--",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"true"
}]


class InitCcppChimneyCalculate():
    # 初始化数据
    @staticmethod
    def init_data():
        data = [
            ccpp_chimney_calculate_data
        ]
        for index in range(len(data)):
            InitCcppChimneyCalculate.insert_constant(data[index])

    # 表中插入常量数据
    @staticmethod
    def insert_constant(data):
        module_name = data[0]["module_name"]
        for index in range(len(data)):
            name_eng = data[index]["name_eng"]
            name = data[index]["name"]
            symbol = data[index]["symbol"]
            unit = data[index]["unit"]
            calculate = data[index]["calculate"]
            remark = data[index]["remark"]
            defaultvalue = data[index]["defaultvalue"]
            minmodelid = data[index]["minmodelid"]
            controltype = data[index]["controltype"]
            permission = data[index]["permission"]
            ccppConstant = CcppConstant.create_ccppConstant(
                module_name, name_eng, name, symbol, unit, calculate, remark,
                defaultvalue, minmodelid, controltype, permission)
            CcppConstant.insert_ccppConstant(ccppConstant)
