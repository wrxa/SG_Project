# -*- coding: utf-8 -*-
from app.ccpp.models.constantModel import CcppConstant
import os


# def getstrcolm(obj):
#     return str(float('%.2f' % obj if obj is not None else 0.0))


# 预加载ccpp表的字段
def getCcppName_engList():
    '''
    获得ccpp表的所有有效字段
    以list的形式返回
    '''
    list_column_ccpp = []
    result = CcppConstant.search_ccppConstant('ccpp_ccpp')
    for ccppConstant in result:
        list_column_ccpp.append(ccppConstant.name_eng + "_design")
    list_column_ccpp.append('engine_num_design')
    list_column_ccpp.append('engine_id_design')
    return list_column_ccpp


# 预加载Economic表的字段
def getCcppEconomicName_engList():
    '''
    获得Economic表的所有有效字段
    以list的形式返回
    '''
    list_column_ccpp = []
    result = CcppConstant.search_ccppConstant('ccpp_economic')
    for ccppConstant in result:
        list_column_ccpp.append(ccppConstant.name_eng)
    return list_column_ccpp


# 预加载ccpp表的原始数据字段
def getCcppOriginalName_engList():
    '''
    获得ccpp表的所有有效字段
    以list的形式返回
    '''
    list_column_ccpp = []
    result = CcppConstant.search_ccppOriginalccppConstant('ccpp_ccpp', 'true')
    for ccppConstant in result:
        list_column_ccpp.append(ccppConstant.name_eng + "_design")
    list_column_ccpp.append('low_calorific_gas_design')
    list_column_ccpp.append('id')
    list_column_ccpp.append('plan_id')
    return list_column_ccpp


# 预加载汽轮机表的字段
def getTurbineName_engList():
    '''
    获得汽轮机表的所有有效字段
    以list的形式返回
    '''
    list_column_turbine = []
    result = CcppConstant.search_ccppConstant('ccpp_Turbine')
    for ccppConstant in result:
        list_column_turbine.append(ccppConstant.name_eng)
    list_column_turbine.append('s_lh_grade')
    list_column_turbine.append('s_hh_grade')
    list_column_turbine.append('s_temperature_pressure')
    list_column_turbine.append('s_steam_type_test')
    return list_column_turbine


# 预加载汽轮机表的原始数据字段字段
def getTurbineOriginalName_engList():
    '''
    获得汽轮机表的所有有效字段
    以list的形式返回
    '''
    list_column_turbine = []
    result = CcppConstant.search_ccppOriginalccppConstant('ccpp_Turbine', 'true')
    for ccppConstant in result:
        list_column_turbine.append(ccppConstant.name_eng)
    list_column_turbine.append('s_lh_grade')
    list_column_turbine.append('s_hh_grade')
    list_column_turbine.append('s_temperature_pressure')
    list_column_turbine.append('s_steam_type_test')
    list_column_turbine.append('id')
    list_column_turbine.append('plan_id')
    list_column_turbine.append('s_parameter_flg')
    return list_column_turbine


# 预加载需求调查表的字段
def getQuestionName_engList():
    '''
    获得需求调查表的所有有效字段
    供：将表单数据更新到数据库，将模型数据转换称json格式在页面显示使用
    以list的形式返回
    '''
    list_column_questionnaire = []
    result = CcppConstant.search_ccppConstant(
        'ccpp_questionnaire')
    for ccppConstant in result:
        if ccppConstant.minmodelid == '1':
            list_column_questionnaire.append(ccppConstant.name_eng + "_design")
            list_column_questionnaire.append(ccppConstant.name_eng + "_check")
        else:
            list_column_questionnaire.append(ccppConstant.name_eng)
    return list_column_questionnaire


# 预加载需求调查表的字段
def getQuestionName_engDict():
    '''
    获得需求调查表的所有有效字段
    供：将表单数据更新到数据库，将模型数据转换称json格式在页面显示使用
    以list的形式返回
    '''
    dict_column_questionnaire = {}
    result = CcppConstant.search_ccppConstant(
        'ccpp_questionnaire')
    for ccppConstant in result:
        if ccppConstant.minmodelid == '1':
            dict_column_questionnaire[ccppConstant.name_eng + "_design"] = ccppConstant.defaultvalue
            dict_column_questionnaire[ccppConstant.name_eng + "_check"] = ccppConstant.defaultvalue
        else:
            dict_column_questionnaire[ccppConstant.name_eng] = ccppConstant.defaultvalue
    return dict_column_questionnaire


def format_value2(flag, values):
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
        result = float(str(float(values)).rstrip('0'))
    else:
        result = values
    return result


# 格式化数据库取出的值
def format_value(values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if values == "null" or values == "None" or values is None:
        result = ""
    elif str(type(values)) == "<type 'unicode'>":
        result = values
    elif str(type(values)) == "<type 'int'>":
        result = values
    elif str(type(values)) == "<type 'numeric'>":
        result = values
    elif str(type(values)) == "<type 'integer'>":
        result = values
    elif str(type(values)) == "<type 'str'>":
        result = values
    elif abs(values) <= 0.00001:
        result = 0.0
    else:
        # 只有数字类型的需要取出多余的0
        result = float(str(float(values)).rstrip('0'))
        result = float('%.3f' % result)
    return result


# 格式化数据库取出的值
def format_value_forexcle(values):
    result = None
    if values is not None:
        result = float(values)
    return result


def tran_str_float(string):
    try:
        if string == '' or string is None:
            return 0
        else:
            return float('%.3f' % float(string))
    except Exception as e:
        print("Error %s" % e)
        raise e


# flag:false顺序 true:逆序
def listsort(obj_list, flag=False):
    return obj_list.sort(cmp=None, key=lambda x: x.id, reverse=flag)


# 如果是字符串数字时需要先转换为float才能格式化
# 如果是数据库的NUMERIC类型时可直接（转换+格式化）
def getstrcolm(obj):
    return str(float('%.2f' % float(obj) if obj is not None else 0.0))


def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)  # 取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)
    if os.path.exists(path):
        os.removedirs(path)

# 转换设备清单中值的显示，去除.0的情况
def item_format(obj):
    item_result = str(float('%.2f' % float(obj) if obj is not None else 0.0))

    if item_result[-2:] == ".0":
        return item_result[:-2]
    else:
        return item_result
