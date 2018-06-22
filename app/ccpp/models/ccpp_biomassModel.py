# -*- coding: utf-8 -*-
from app import db


# 化学水处理表
class CcppCHPWaterTreatment(db.Model):
    # 表名
    __tablename__ = 'ccpp_water_treatment'
    __table_args__ = {'comment': u'燃气蒸汽联合循环-化学水处理数据'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 4过热蒸汽额定流量
    o_steam_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽额定流量")
    # 5厂内汽水损失
    o_loss_factory = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"厂内汽水损失")
    # 6锅炉排污损失
    o_boiler_blowdown_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉排污损失")
    # 7机组启动或事故增加损失
    o_start_accident_increase_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机组启动或事故增加损失")
    # 8外供汽损失
    o_external_supply_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"外供汽损失")
    # 9自用水量
    o_water_consumption = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"自用水量")
    # 10锅炉补给水系统正常出力
    o_boiler_water_normal = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水系统正常出力")
    # 11锅炉补给水系统最大出力
    o_boiler_water_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水系统最大出力")  
    # 12锅炉补给水系统出力
    o_boiler_water_system = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水系统出力") 
    # 13除盐水箱有效容积
    o_salt_water_tank = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除盐水箱有效容积")
    # 工艺路线
    o_process_route = db.Column(db.String(50), comment=u"锅炉补水系统工艺路线")

    def __init__(self, **kwargs):
        super(CcppCHPWaterTreatment, self).__init__(**kwargs)

    @staticmethod
    def insert_water(biomassWater):
        try:
            db.session.add(biomassWater)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update biomassWater"
                  "<id=%s> in database" % (biomassWater.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_water(plan_id):
        result = CcppCHPWaterTreatment.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_water(plan_id):
        water = \
            CcppCHPWaterTreatment.search_water(plan_id)
        try:
            db.session.delete(water)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete water<id=%s, plan_id=%s> in database" %
                  (water.id, water.plan_id))
