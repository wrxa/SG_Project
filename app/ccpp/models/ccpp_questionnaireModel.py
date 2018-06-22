# -*- coding: utf-8 -*-
from app import db


class Questionnaire(db.Model):
    # 表名
    __tablename__ = 'ccpp_questionnaire'
    __table_args__ = {'comment': u'燃气蒸汽联合循环-需求调查数据'}
    # 表ID,自动生成（主键）
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, index=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 燃料:设计值
    s_fuel_design = db.Column(db.NUMERIC(precision=15, scale=5))
    # 燃料:校核值
    s_fuel_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 甲烷:设计值
    methane_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"甲烷含量含量")
    # 甲烷:校核值
    methane_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 乙烷:设计值
    ethane_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"乙烷含量")
    # 乙烷:校核值
    ethane_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 乙烯:设计值
    ethylene_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"乙烯含量")
    # 乙烯:校核值
    ethylene_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 丙烯:设计值
    propylene_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"丙烯含量")
    # 丙烯:校核值
    propylene_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 丙烷:设计值
    propane_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"丙烷含量")
    # 丙烷:校核值
    propane_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 丁烯:设计值
    butene_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"丁烯含量")
    # 丁烯:校核值
    butene_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # i-异丁烷:设计值
    i_isobutane_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"i-异丁烷含量")
    # i-异丁烷:校核值
    i_isobutane_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # n-异丁烷:设计值
    n_isobutane_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"n-异丁烷含量")
    # n-异丁烷:校核值
    n_isobutane_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 戊烷:设计值
    pentane_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"戊烷含量")
    # 戊烷:校核值
    pentane_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 碳6:设计值
    carbon6_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"碳6含量")
    # 碳6:校核值
    carbon6_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 氢气:设计值
    hydrogen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氢气含量")
    # 氢气:校核值
    hydrogen_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 氦气:设计值
    helium_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氦气含量")
    # 氦气:校核值
    helium_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 氮气:设计值
    nitrogen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氮气含量")
    # 氮气:校核值
    nitrogen_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 一氧化碳:设计值
    carbon_monoxide_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"一氧化碳含量")
    # 一氧化碳:校核值
    carbon_monoxide_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 二氧化碳:设计值
    carbon_dioxide_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"二氧化碳含量")
    # 二氧化碳:校核值
    carbon_dioxide_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 硫化氢:设计值
    hydrogen_sulfide_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"硫化氢含量")
    # 硫化氢:校核值
    hydrogen_sulfide_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 氧气:设计值
    oxygen_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氧气含量")
    # 氧气:校核值
    oxygen_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 水:设计值
    water_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"水含量")
    # 水:校核值
    water_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 总计:设计值
    total_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总计")
    # 总计:校核值
    total_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃气低位发热量:设计值
    low_calorific_gas_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气低位发热量")
    # 燃气低位发热量:检查值
    low_calorific_gas_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 高位发热量:设计值
    high_calorific_value_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气高位发热量")
    # 高位发热量:设计值
    high_calorific_value_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 燃气价格:设计值
    price_design = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气价格")
    # 燃气价格:设计值
    price_check = db.Column(db.NUMERIC(precision=15, scale=5))

    # 当地平均海拔:设计值
    local_avg_hight = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"当地平均海拔")

    # 年平均温度:设计值
    year_avg_temperate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年平均温度")

    # 夏季平均温度:设计值
    summer_avg_temperate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"夏季平均温度")

    # 冬季平均温度:设计值
    winter_avg_temperate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冬季平均温度")

    # 年平均大气压力:设计值
    year_avg_press = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年平均大气压力")

    # 夏季大气压力:设计值
    summer_avg_press = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"夏季大气压力")

    # 冬季大气压力:设计值
    winter_avg_press = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冬季大气压力")

    # 年平均相对湿度:设计值
    year_avg_humidity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年平均相对湿度")

    # 蒸汽压力等级1:设计值
    steam_pressure_level_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽压力等级:高")

    # 蒸汽温度等级1:设计值
    steam_temperature_level_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽温度等级")

    # 用汽时段start1:设计值
    use_steam_time_1 = db.Column(db.String(50), comment=u"用汽时段")

    # 蒸汽价格
    steam_price_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽价格")

    # 近期蒸汽流量范围1
    recent_steam_flow_range_1 = db.Column(db.String(50), comment=u"近期蒸汽流量范围")

    # 远期蒸汽流量范围1:设计值
    forward_steam_flow_range_1 = db.Column(db.String(50), comment=u"远期蒸汽流量范围")

    # 凝结水含铁量1:设计值
    icicw_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水含铁量")

    # 凝结水回收率1:设计值
    rrcw_1 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回收率")

    # 蒸汽压力等级2:设计值
    steam_pressure_level_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽压力等级")

    # 蒸汽温度等级2:设计值
    steam_temperature_level_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽温度等级")

    # 用汽时段start2:设计值
    use_steam_time_2 = db.Column(db.String(50), comment=u"用汽时段")

    # 蒸汽价格
    steam_price_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽价格")

    # 近期蒸汽流量范围2
    recent_steam_flow_range_2 = db.Column(db.String(50), comment=u"近期蒸汽流量范围")

    # 远期蒸汽流量范围2:设计值
    forward_steam_flow_range_2 = db.Column(db.String(50), comment=u"远期蒸汽流量范围")

    # 凝结水含铁量2:设计值
    icicw_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水含铁量")

    # 凝结水回收率2:设计值
    rrcw_2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回收率")

    # 蒸汽压力等级3:设计值
    steam_pressure_level_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽压力等级")

    # 蒸汽温度等级3:设计值
    steam_temperature_level_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽温度等级")

    # 用汽时段start3:设计值
    use_steam_time_3 = db.Column(db.String(50), comment=u"用汽时段")

    # 蒸汽价格
    steam_price_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸汽价格")

    # 近期蒸汽流量范围3
    recent_steam_flow_range_3 = db.Column(db.String(50), comment=u"近期蒸汽流量范围")

    # 远期蒸汽流量范围3:设计值
    forward_steam_flow_range_3 = db.Column(db.String(50), comment=u"远期蒸汽流量范围")

    # 凝结水含铁量3:设计值
    icicw_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水含铁量")

    # 凝结水回收率3:设计值
    rrcw_3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回收率")

    # 采暖场合类型:设计值
    heating_occasion_type = db.Column(db.String(50), comment=u"采暖场合类型")

    # 全年采暖天数:设计值
    year_heat_days = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"全年采暖天数")

    # 近期采暖面积:设计值
    recent_heating_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"近期采暖面积")

    # 近期采暖负荷(采暖热负荷):设计值
    recent_heating_load = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"近期采暖负荷(采暖热负荷)")

    # 远期采暖面积:设计值
    forward_heating_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"远期采暖面积")

    # 远期采暖负荷(采暖热负荷):设计值
    forward_heating_load = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"远期采暖负荷(采暖热负荷)")

    # 采暖价格
    heating_load_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"采暖价格")

    # 制冷场合类型(工艺冷负荷)1:设计值
    types_refrigeration_occasion_technology_1 = db.Column(db.String(50))

    # 全年制冷天数(工艺冷负荷)1:设计值
    annual_cooling_days_technology_1 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 近期制冷负荷(工艺冷负荷)1:设计值
    recent_cooling_load_technology_1 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 远期制冷负荷(工艺冷负荷)1:设计值
    forward_cooling_load_technology_1 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 制冷场合类型(工艺冷负荷)2:设计值
    types_refrigeration_occasion_technology_2 = db.Column(db.String(50))

    # 全年制冷天数(工艺冷负荷)2:设计值
    annual_cooling_days_technology_2 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 近期制冷负荷(工艺冷负荷)2:设计值
    recent_cooling_load_technology_2 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 远期制冷负荷(工艺冷负荷)2:设计值
    forward_cooling_load_technology_2 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 制冷场合类型(工艺冷负荷)3:设计值
    types_refrigeration_occasion_technology_3 = db.Column(db.String(50))

    # 全年制冷天数(工艺冷负荷)3:设计值
    annual_cooling_days_technology_3 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 近期制冷负荷(工艺冷负荷)3:设计值
    recent_cooling_load_technology_3 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 远期制冷负荷(工艺冷负荷)3:设计值
    forward_cooling_load_technology_3 = db.Column(
        db.NUMERIC(precision=15, scale=5))

    # 制冷场合类型（民用负荷）:设计值
    type_refrigeration_occasion_civil = db.Column(db.String(50), comment=u"制冷场合类型（民用负荷）")

    # 全年制冷天数（民用负荷）:设计值
    annual_cooling_days_civil = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"全年制冷天数（民用负荷）")

    # 近期制冷面积（民用负荷）:设计值
    recent_cooling_area_civil = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"近期制冷面积（民用负荷）")

    # 近期制冷负荷（民用负荷）:设计值
    recent_cooling_load_civil = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"近期制冷负荷（民用负荷）")

    # 远期制冷面积（民用负荷）:设计值
    forward_cooling_area_civil = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"远期制冷面积（民用负荷）")

    # 远期制冷负荷（民用负荷）:设计值
    forward_cooling_load_civil = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"远期制冷负荷（民用负荷）")

    # 规划占地面积:设计值
    plan_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"规划占地面积")

    # 规划扩建容量:设计值
    planning_expansion_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"规划扩建容量")

    # 当地水源条件:设计值
    local_water_condition = db.Column(db.Text(), nullable=True, comment=u"当地水源条件")

    # 电负荷需求:设计值
    electric_load_demand = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电负荷需求")

    # 上网电价:设计值
    net_electricity_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上网电价")

    # 自用电价:设计值
    personal_electricity_price = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"自用电价")

    # 上级变电压等级:设计值
    higher_voltage_level = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"上级变电压等级")

    # 厂区距上级变距离:设计值
    fachl = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"厂区距上级变距离")

    # 是否上网:设计值
    surf_internet_flage = db.Column(db.String(10), comment=u"是否上网")

    # 是否孤网运行:设计值
    isolated_network_operation_flage = db.Column(db.String(10), comment=u"是否孤网运行")

    # 烟气SOX排放限值:设计值
    sox_discharge_limit = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气SOX排放限值")

    # 烟气NOX排放限值:设计值
    sox_discharge_limit = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气NOX排放限值")

    # 烟气烟尘排放限值:设计值
    smoke_discharge_limit = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气烟尘排放限值")

    # 拟采用脱硝形式:设计值
    denitration_form = db.Column(db.Text(), nullable=True, comment=u"拟采用脱硝形式")

    # 尿素/氨水供应情况:设计值
    urea_ammonia_water_supply = db.Column(db.Text(), nullable=True, comment=u"尿素/氨水供应情况")

    # 更新需求
    @staticmethod
    def updata_questionnaire(questionnaire):
        if questionnaire.id is not None:
            try:
                db.session.add(questionnaire)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("Error %s" % e)
                raise e
            finally:
                print("updata questionnaire<id=%s, > in database" % (questionnaire.id))

    # 根据id查找实体
    @staticmethod
    def search_questionnaire(plan_id):
        result = Questionnaire.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def deleteByPlan_id(plan_id):
        questionnaire = Questionnaire.search_questionnaire(plan_id)
        try:
            db.session.delete(questionnaire)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete questionnaire<id=%s, > in database" % (questionnaire.id))
