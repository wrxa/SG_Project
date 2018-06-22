# -*- coding: utf-8 -*-
from app.models import Plan, MyException
from util.get_all_path import GetPath
from app import db


class CcppPlanService():
    # 根据plan_id删除实体
    def deletebyPlanId(self, plan_id):
        plan = Plan.search_planById(plan_id)
        db.session.delete(plan)


# 格式化数据库取出的值
def format_value(values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if values == "null" or values == "None" or values is None:
        result = 0
    elif str(type(values)) == "<type 'unicode'>":
        result = values
    elif str(type(values)) == "<type 'int'>":
        result = values
    elif str(type(values)) == "<type 'str'>":
        result = values
    elif abs(values) <= 0.00001:
        result = 0
    else:
        # 只有数字类型的需要取出多余的0
        result = float(str(float(values)).rstrip('0'))
    return result


def getCcppPlanData(planId):
    return None


def getccppimginfo(self, ccpp, ccppTurbine, planId, user_id):
    if ccpp.boiler_single_or_dula_pressure_design == "singlepot" and ccppTurbine.s_steam_type_test == 2:
        path = GetPath.getImgCcppNetPath('db', planId, user_id)
        if path is not None:
            return u'# 附件\n##### ![](' + path + u')\n##### 单压余热锅炉+背压汽轮机图示'
        else:
            raise MyException("dbPathNotFond",
                                u"单压余热锅炉+背压汽轮机图找不到,请检查数据或者网络是否有误。",
                                path + u"单压余热锅炉+背压汽轮机图找不到,请查看生成图片代码，或者目录结构是否完整。",
                                path)
    elif ccpp.boiler_single_or_dula_pressure_design == "singlepot" and ccppTurbine.s_steam_type_test == 1:
        path = GetPath.getImgCcppNetPath('dc', planId, user_id)
        if path is not None:
            return u'# 附件\n##### ![](' + path + u')\n##### 单压余热锅炉+抽凝汽轮机图示'
        else:
            raise MyException("dcPathNotFond",
                                u"单压余热锅炉+抽凝汽轮机图找不到,请检查数据或者网络是否有误。",
                                path + u"单压余热锅炉+抽凝汽轮机图找不到,请查看生成代码，或者目录结构是否完整。",
                                path)
    elif ccpp.boiler_single_or_dula_pressure_design == "singlepot" and ccppTurbine.s_steam_type_test is None:
        path = GetPath.getImgCcppNetPath('dn', planId, user_id)
        if path is not None:
            return u'# 附件\n##### ![](' + path + u')\n##### 单压余热锅炉图示'
        else:
            raise MyException("dnPathNotFond",
                                u"单压余热锅炉图找不到,请检查数据或者网络是否有误。",
                                path + u"单压余热锅炉图找不到,请查看生成代码，或者目录结构是否完整。",
                                path)
        
    elif ccpp.boiler_single_or_dula_pressure_design == "doublepot" and ccppTurbine.s_steam_type_test == 3:
        path = GetPath.getImgCcppNetPath('sbq', planId, user_id)
        if path is not None:
            return u'# 附件\n##### ![](' + path + u')\n##### 双压余热锅炉+补凝汽轮机图示'
        else:
            raise MyException("sbqPathNotFond",
                                u"双压余热锅炉+补凝汽轮机图找不到,请检查数据或者网络是否有误。",
                                path + u"双压余热锅炉+补凝汽轮机图找不到,请查看生成代码，或者目录结构是否完整。",
                                path)
        
    elif ccpp.boiler_single_or_dula_pressure_design == "doublepot" and ccppTurbine.s_steam_type_test == 2:
        path = GetPath.getImgCcppNetPath('sb', planId, user_id)
        if path is not None:
            return u'# 附件\n##### ![](' + path + u')\n##### 双压余热锅炉+背压汽轮机图示'
        else:
            raise MyException("sbPathNotFond",
                                u"双压余热锅炉+背压汽轮机图找不到,请检查数据或者网络是否有误。",
                                path + u"双压余热锅炉+背压汽轮机图找不到,请查看生成代码，或者目录结构是否完整。",
                                path)
        
    elif ccpp.boiler_single_or_dula_pressure_design == "doublepot" and ccppTurbine.s_steam_type_test == 1:
        path = GetPath.getImgCcppNetPath('sc', planId, user_id)
        if path is not None:
            return u'# 附件\n##### ![](' + path + u')\n##### 双压余热锅炉+抽凝汽轮机图示'
        else:
            raise MyException("scPathNotFond",
                                u"双压余热锅炉+抽凝汽轮机生成资源图找不到,请检查数据或者网络是否有误。",
                                path + u"双压余热锅炉+抽凝汽轮机生成资源图找不到,请查看生成代码，或者目录结构是否完整。",
                                path)
        
    elif ccpp.boiler_single_or_dula_pressure_design == "doublepot" and ccppTurbine.s_steam_type_test is None:
        path = GetPath.getImgCcppNetPath('sn', planId, user_id)
        if path is not None:
            return u'# 附件\n##### ![](' + path + u')\n##### 双压余热锅炉图示'
        else:
            raise MyException("snPathNotFond",
                                u"双压余热锅炉生成资源图找不到,请检查数据或者网络是否有误。",
                                path + u"双压余热锅炉生成资源图找不到,请查看生成代码，或者目录结构是否完整。",
                                path)
    return None
