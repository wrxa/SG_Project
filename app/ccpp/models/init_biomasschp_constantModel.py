# -*- coding: utf-8 -*-
from .constantModel import CcppConstant


# 化学水处理sheet

water_treatment_data = [{
    "module_name": "water_treatment",
    "name_eng": "o_steam_flow",
    "name": u"过热蒸汽额定流量",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"Dgr",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_loss_factory",
    "name": u"厂内汽水损失",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"Dgr*3%",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_boiler_blowdown_loss",
    "name": u"锅炉排污损失",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"Dgr*2%",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_start_accident_increase_loss",
    "name": u"机组启动或事故增加损失",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"Dgr*10%",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_external_supply_loss",
    "name": u"外供汽损失",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"G2*（1-Φ）  （1）生物质发电项目：不对外供汽，所以外供汽损失取0；（2）生物质热电联产项目：对外供汽，外供汽损失主要取决于凝结水回水率Φ的大小，若外供汽由于直接参与换热，凝结水水质较差，不考虑回收，则外供汽损失即为外供汽量。",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_water_consumption",
    "name": u"自用水量",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"(〔1〕+〔2〕+〔4〕）*10%",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_boiler_water_normal",
    "name": u"锅炉补给水系统正常出力",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"〔1〕＋〔2〕＋〔4〕＋〔5〕",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_boiler_water_max",
    "name": u"锅炉补给水系统最大出力",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"〔1〕＋〔2〕＋〔3〕＋〔4〕＋〔5〕",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_boiler_water_system",
    "name": u"锅炉补给水系统出力",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"Q",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
},
{
    "module_name": "water_treatment",
    "name_eng": "o_salt_water_tank",
    "name": u"除盐水箱有效容积",
    "symbol": u"",
    "unit": u"t/h",
    "calculate": u"Q*5",
    "remark": u"",
    "defaultvalue": u"",
    "minmodelid": u"1",
    "controltype": u"input",
    "permission": u"false"
}
]


class InitCcppWaterTreatment():
    # 初始化数据
    @staticmethod
    def init_data():
        data = [
            water_treatment_data
        ]
        for index in range(len(data)):
            InitCcppWaterTreatment.insert_constant(data[index])

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