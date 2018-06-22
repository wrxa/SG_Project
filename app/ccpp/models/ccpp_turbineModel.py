# -*- coding: utf-8 -*-
from app import db


class CcppTurbine(db.Model):
    # 表名
    __tablename__ = 'ccpp_turbine'
    __table_args__ = {'comment': u'燃气蒸汽联合循环-汽轮机计算数据'}
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 参数
    # 是否已经输入参数
    s_parameter_flg = db.Column(db.String(50))
    # 汽轮机类型
    s_steam_type_test = db.Column(db.Integer)
    # 除氧器温度和压力
    s_temperature_pressure = db.Column(db.String(50), comment=u"除氧器温度和压力")
    # 高加级数
    s_hh_grade = db.Column(db.Integer, comment=u"高加级数")
    # 低加级数
    s_lh_grade = db.Column(db.Integer, comment=u"低加级数")

    # 发电功率估算
    # 汽轮机内效率
    e_turbine_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：汽轮机内效率")
    # 机械效率
    e_mechanical_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：机械效率")
    # 发电机效率
    e_generator_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：发电机效率")
    # 汽轮机机组型式
    e_steam_type = db.Column(db.String(50), comment=u"发电功率估算：汽轮机机组型式")
    # 主蒸汽  压力
    e_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-压力")
    # 温度
    e_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-温度")
    # 流量
    e_steam_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-流量")
    # 熵
    e_steam_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-熵")
    # 焓
    e_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-焓")
    # 抽汽点  压力
    e_exhaust_point_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-压力")
    # 温度
    e_exhaust_point_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-温度")
    # 熵
    e_exhaust_point_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-熵")
    # 焓
    e_exhaust_point_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-焓")
    # 流量
    e_exhaust_point_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-流量")
    # 抽汽后蒸汽量
    e_exhaust_after_steam = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后蒸汽量")
    # 压力
    e_exhaust_after_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后压力")
    # 焓
    e_exhaust_after_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后焓")
    # 熵
    e_exhaust_after_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后熵")
    # 乏汽  压力
    e_steam_exhaust_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：乏汽-压力")
    # 焓
    e_steam_exhaust_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：乏汽-焓")

    # 背压  压力
    e_backpressure_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-压力")
    # 背压  温度
    e_backpressure_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-温度")
    # 焓
    e_backpressure_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-焓")
    # 流量
    e_backpressure_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-流量")

    # 总发电量
    e_gross_generation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：总发电量")
    # 回热抽汽经验数据
    e_hot_data = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：回热抽汽经验数据")
    # 去除抽汽后
    e_steam_extraction = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：去除抽汽后")
    # 选定
    e_steam_extraction_select = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：选定")
    # 全厂汽水损失
    e_steam_water_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：全厂汽水损失")
    # 进汽量
    e_throttle_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：进汽量")


    # 汽轮机回热系统计算
    # 假设
    h_assume = db.Column(db.String(100), comment=u"汽轮机回热系统-假设")
    # 温度
    h_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-温度")
    # 压力
    h_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-压力")
    # 焓值
    h_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-焓值")
    # 量
    h_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-量")

    # HH1
    # 给水出水温度
    hh1_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-给水出水温度")
    # 给水出口焓
    hh1_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-给水出口焓")
    # 上端差
    hh1_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-上端差")
    # 饱和水温度
    hh1_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-饱和水温度")
    # 饱和水焓
    hh1_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-饱和水焓")
    # 工作压力
    hh1_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-工作压力")
    # 抽汽管压损
    hh1_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽管压损")
    # 抽汽压力
    hh1_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽压力")
    # 抽汽焓
    hh1_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽焓")
    # 抽汽量
    hh1_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽量")
    
    # HH2
    # 给水出水温度
    hh2_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-给水出水温度")
    # 给水出口焓
    hh2_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-给水出口焓")
    # 上端差
    hh2_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-上端差")
    # 饱和水温度
    hh2_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-饱和水温度")
    # 饱和水焓
    hh2_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-饱和水焓")
    # 工作压力
    hh2_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-工作压力")
    # 抽汽管压损
    hh2_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽管压损")
    # 抽汽压力
    hh2_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽压力")
    # 抽汽焓
    hh2_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽焓")
    # 抽汽量
    hh2_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽量")

    # HH3
    # 给水出水温度
    hh3_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-给水出水温度")
    # 给水出口焓
    hh3_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-给水出口焓")
    # 上端差
    hh3_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-上端差")
    # 饱和水温度
    hh3_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-饱和水温度")
    # 饱和水焓
    hh3_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-饱和水焓")
    # 工作压力
    hh3_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-工作压力")
    # 抽汽管压损
    hh3_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽管压损")
    # 抽汽压力
    hh3_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽压力")
    # 抽汽焓
    hh3_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽焓")
    # 抽汽量
    hh3_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽量")

    # D
    # 给水出水温度
    d_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-给水出水温度")
    # 给水出口焓
    d_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-给水出口焓")
    # 工作压力
    d_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-工作压力")
    # 抽汽管压损
    d_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽管压损")
    # 抽汽压力
    d_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽压力")
    # 抽汽焓
    d_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽焓")
    # 抽汽量
    d_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽量")

    # LH1
    # 给水出水温度
    lh1_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-给水出水温度")
    # 给水出口焓
    lh1_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-给水出口焓")
    # 上端差
    lh1_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-上端差")
    # 饱和水温度
    lh1_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-饱和水温度")
    # 饱和水焓
    lh1_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-饱和水焓")
    # 工作压力
    lh1_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-工作压力")
    # 抽汽管压损
    lh1_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽管压损")
    # 抽汽压力
    lh1_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽压力")
    # 抽汽焓
    lh1_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽焓")
    # 抽汽量
    lh1_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽量")

    # LH2
    # 给水出水温度
    lh2_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-给水出水温度")
    # 给水出口焓
    lh2_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-给水出口焓")
    # 上端差
    lh2_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-上端差")
    # 饱和水温度
    lh2_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-饱和水温度")
    # 饱和水焓
    lh2_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-饱和水焓")
    # 工作压力
    lh2_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-工作压力")
    # 抽汽管压损
    lh2_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽管压损")
    # 抽汽压力
    lh2_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽压力")
    # 抽汽焓
    lh2_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽焓")
    # 抽汽量
    lh2_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽量")

    # LH3
    # 给水出水温度
    lh3_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-给水出水温度")
    # 给水出口焓
    lh3_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-给水出口焓")
    # 上端差
    lh3_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-上端差")
    # 饱和水温度
    lh3_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-饱和水温度")
    # 饱和水焓
    lh3_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-饱和水焓")
    # 工作压力
    lh3_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-工作压力")
    # 抽汽管压损
    lh3_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽管压损")
    # 抽汽压力
    lh3_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽压力")
    # 抽汽焓
    lh3_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽焓")
    # 抽汽量
    lh3_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽量")

    # C
    # 给水出水温度
    c_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-给水出水温度")
    # 给水出口焓
    c_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-给水出口焓")
    # 工作压力
    c_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-工作压力")
    # 抽汽管压损
    c_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽管压损")
    # 抽汽压力
    c_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽压力")
    # 抽汽焓
    c_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽焓")
    # 抽汽量
    c_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽量")

    # 组内功率计算及校核
    # 汽轮机内效率
    i_turbine_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：汽轮机内效率")
    # 机械效率
    i_mechanical_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：机械效率")
    # 发电机效率
    i_generator_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：发电机效率")
    # 主蒸汽  压力
    i_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-压力")
    # 温度
    i_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-温度")
    # 流量
    i_steam_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-流量")
    # 熵
    i_steam_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-熵")
    # 焓
    i_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-焓")
    # 1#高压  压力
    i_high1_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-压力")
    # 熵
    i_high1_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-熵")
    # 温度
    i_high1_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-温度")
    # 焓
    i_high1_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-焓")
    # 流量
    i_high1_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-流量")
    # 主汽至HH1功率
    i_steam_hh1_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主汽至HH1功率")
    # 2#高压  压力
    i_high2_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-压力")
    # 熵
    i_high2_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-熵")
    # 温度
    i_high2_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-温度")
    # 焓
    i_high2_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-焓")
    # 流量
    i_high2_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-流量")
    # HH1至HH2功率
    i_hh1_hh2_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：HH1至HH2功率")
    # D除氧  压力
    i_deoxidize_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-压力")
    # 熵
    i_deoxidize_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-熵")
    # 温度
    i_deoxidize_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-温度")
    # 焓
    i_deoxidize_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-焓")
    # 流量
    i_deoxidize_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-流量")
    # HH2至D功率
    i_hh2_deoxidize_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：HH2至D功率")
    # 抽汽点  压力
    i_exhaust_point_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-压力")
    # 温度
    i_exhaust_point_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-温度")
    # 熵
    i_exhaust_point_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-熵")
    # 焓
    i_exhaust_point_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-焓")
    # 流量
    i_exhaust_point_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-流量")
    # D至抽汽功率
    i_deoxidize_exhaust_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D至抽汽功率")
    # 1#低加  压力
    i_low1_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-压力")
    # 熵
    i_low1_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-熵")
    # 温度
    i_low1_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-温度")
    # 焓
    i_low1_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-焓")
    # 流量
    i_low1_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-流量")
    # 抽汽至LH1功率
    i_exhaust_lh1_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽至LH1功率")
    # 2#低加  压力
    i_low2_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-压力")
    # 熵
    i_low2_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-熵")
    # 温度
    i_low2_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-温度")
    # 焓
    i_low2_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-焓")
    # 流量
    i_low2_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-流量")
    # LH1至LH2功率
    i_lh1_lh2_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH1至LH2功率")
    # 3#低加  压力
    i_low3_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-压力")
    # 熵
    i_low3_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-熵")
    # 温度
    i_low3_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-温度")
    # 焓
    i_low3_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-焓")
    # 流量
    i_low3_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-流量")
    # LH2至LH3功率
    i_lh2_lh3_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH2至LH3功率")

    # 乏汽/背压   压力
    i_steam_exhaust_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-压力")
    # 熵
    i_steam_exhaust_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-熵")
    # 焓
    i_steam_exhaust_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-焓")
    # 实际焓
    i_steam_exhaust_enthalpy_actual = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-实际焓")
    # 饱和蒸汽焓
    i_steam_exhaust_enthalpy_steam = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-饱和蒸汽焓")
    # 饱和水焓
    i_steam_exhaust_enthalpy_water = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-饱和水焓")
    # 干度
    i_steam_exhaust_dry = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-干度")
    # 流量
    i_steam_exhaust_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-流量")
    # LH2至乏汽功率
    i_lh2_steam_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH2至乏汽功率")
    # 总功率
    i_total_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：总功率")
    # 计算误差
    i_calculation_error = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：计算误差")
    # 锅炉排污率
    h_blowdown_rate = db.Column(db.NUMERIC(precision=15, scale=5))
    # 追加补汽焓（补凝场合）
    e_steam_plus_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"补汽焓")

    def __init__(self, **kwargs):
        super(CcppTurbine, self).__init__(**kwargs)

    @staticmethod
    def insert_CcppTurbine(turbine):
        try:
            if turbine.id is not None:
                db.session.add(turbine)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassCHPDesDen"
                  "<id=%s> in database" % (turbine.id))

    # 根据plan id查找实体
    @staticmethod
    def search_CcppTurbine(planId):
        result = CcppTurbine.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_CcppTurbine(plan_id):
        Turbine = CcppTurbine.search_CcppTurbine(plan_id)
        try:
            db.session.delete(Turbine)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete Turbine<id=%s, plan_id=%s> in database" %
                  (Turbine.id, Turbine.plan_id))