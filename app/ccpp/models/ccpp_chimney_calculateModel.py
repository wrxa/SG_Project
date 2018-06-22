# -*- coding: utf-8 -*-
from app import db


# 烟囱计算
class CcppChimneyCalculate(db.Model):
    # 表名
    __tablename__ = 'ccpp_chimney_calculate'
    __table_args__ = {'comment': u'燃气蒸汽联合循环-烟囱计算数据'}
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))
    # 烟气量
    flue_gas_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气量")
    # 排烟压力
    pressure_exhaust_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排烟压力")
    # 排烟温度
    temperature_exhaust_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排烟温度")
    # 烟气流速
    flue_gas_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气流速")
    # 烟囱内径
    inner_diameter_chimney = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱内径")
    # 燃机数量
    engine_num_design = db.Column(db.Integer, comment=u"燃机数量")

    def __init__(self, **kwargs):
        super(CcppChimneyCalculate, self).__init__(**kwargs)

    @staticmethod
    def updata_chimney_calculate(ccppChimneyCalculate):
        try:
            db.session.add(ccppChimneyCalculate)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update CcppChimneyCalculate"
                  "<id=%s> in database" % (ccppChimneyCalculate.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_chimney_calculate(plan_id):
        result = CcppChimneyCalculate.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_chimney_calculate(plan_id):
        chimney_calculate = \
            CcppChimneyCalculate.search_chimney_calculate(plan_id)
        try:
            db.session.delete(chimney_calculate)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete CcppChimneyCalculate<id=%s, plan_id=%s> in database" %
                  (chimney_calculate.id, chimney_calculate.plan_id))
