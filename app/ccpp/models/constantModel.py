# -*- coding: utf-8 -*-
from app import db


# ccpp常量表
class CcppConstant(db.Model):
    # 表名
    __tablename__ = 'ccpp_constant'
    # 常量表id， 自动生成
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 模块(页面)id：
    module_name = db.Column(db.String(200), index=True)
    # 字段英文名
    name_eng = db.Column(db.String(200))
    # 字段中文名
    name = db.Column(db.String(200))
    # 表示符号
    symbol = db.Column(db.String(200))
    # 计量单位
    unit = db.Column(db.String(200))
    # 计算公式
    calculate = db.Column(db.String(200))
    # 备注
    remark = db.Column(db.Text())
    # 默认值
    defaultvalue = db.Column(db.String(50))
    # 小模块
    minmodelid = db.Column(db.String(200))
    # 控件类型
    controltype = db.Column(db.String(20))
    # 控件类型
    permission = db.Column(db.String(200))

    @staticmethod
    def create_ccppConstant(module_name, name_eng, name, symbol, unit,
                            calculate, remark, defaultvalue, minmodelid,
                            controltype, permission):
        ccppConstant = CcppConstant()
        ccppConstant.module_name = module_name
        ccppConstant.name_eng = name_eng
        ccppConstant.name = name
        ccppConstant.symbol = symbol
        ccppConstant.unit = unit
        ccppConstant.calculate = calculate
        ccppConstant.remark = remark
        ccppConstant.defaultvalue = defaultvalue
        ccppConstant.minmodelid = minmodelid
        ccppConstant.controltype = controltype
        ccppConstant.permission = permission
        return ccppConstant

    @staticmethod
    def insert_ccppConstant(ccppConstant):
        try:
            db.session.add(ccppConstant)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update ccppConstant<id=%s, module_name=%s>" %
                  (ccppConstant.id, ccppConstant.module_name))

    @staticmethod
    def search_ccppConstant(module_name):
        result = CcppConstant.query.filter_by(module_name=module_name).all()
        return result

    @staticmethod
    def search_ccppOriginalccppConstant(module_name, permission):
        result = CcppConstant.query.filter_by(module_name=module_name, permission=permission).all()
        return result

    @staticmethod
    def search_ccppConstantbyminmodelid(module_name, minmodelid):
        result = CcppConstant.query.filter_by(module_name=module_name, minmodelid=minmodelid).all()
        return result

    def __repr__(self):
        return '<coalCHPConstant %r>' % self.module_name

