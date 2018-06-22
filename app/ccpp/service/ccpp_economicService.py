# -*- coding: utf-8 -*-
"""
ccpp需求调查表：sheet的服务处理程序
"""
from app.ccpp.models.constantModel import CcppConstant
from app.ccpp import gl
from app.ccpp.models.ccpp_ccpp_economicModel import Ccpp_ccpp_economic
from app.ccpp.service.economic.ccpp_economic_calculation import Factory
import copy
from app.ccpp.service.excledealwith.economicexcle import createEconomicExcle
from util.get_all_path import GetPath
import os
from app import db


class EconomicService():
    # 生成excle
    def getEconomicExcle(self, plan_id, user_id):
        createEconomicExcle(plan_id, user_id)
        # 返回文件流，供下载

    # 根据plan_id删除实体
    def deletebyPlanId(self, plan_id, userId):
        # 删除生成的结果文件：经济性分析的excle文件、生成的word文件(统一删除)
        excleCcppResultFile = GetPath.getExcleCcppResult(plan_id, userId)
        if os.path.exists(excleCcppResultFile):
            os.remove(excleCcppResultFile)
        economic = Ccpp_ccpp_economic.search_economic(plan_id)
        db.session.delete(economic)

    '''
    进入需求调查表页面
    加载字段常量数据、加载已有方案、加载公司信息
    '''
    @staticmethod
    def getEconomicConstant():
        ccppConstant = CcppConstant.search_ccppConstant('ccpp_economic')
        gl.listsort(ccppConstant)
        return ccppConstant

    def getEconomicDataJson(self, planId):
        '''
        将模型Ccpp_ccpp_economic中的数据转换为json格式
        '''
        ccpp_ccpp_economic = Ccpp_ccpp_economic.search_economic(planId)
        copyccpp_ccpp_economic = copy.deepcopy(ccpp_ccpp_economic)
        # 单位换算：此处可修改数据库的值，所以需要深拷贝
        
        datas = {}
        list_column_economic = gl.getCcppEconomicName_engList()
        for index in range(len(list_column_economic)):
            datas[list_column_economic[index]] = gl.format_value(
                getattr(copyccpp_ccpp_economic, list_column_economic[index]))
        return datas

    def submitEconomicForm(self, form, plan_id):
        '''
        将表单中的数据更新到ccpp表中
        '''
        ccpp_ccpp_economic = Ccpp_ccpp_economic.query.filter_by(
            plan_id=plan_id).first()
        # 构造列
        list_column_ccpp = gl.getCcppEconomicName_engList()
        # 为模型赋值
        for index in range(len(list_column_ccpp)):
            formdata = form.get(list_column_ccpp[index])
            if hasattr(ccpp_ccpp_economic, list_column_ccpp[index]):
                if formdata is not None and formdata != '':
                    setattr(ccpp_ccpp_economic, list_column_ccpp[index],
                            formdata)
                else:
                    setattr(ccpp_ccpp_economic, list_column_ccpp[index],
                            None)
        '''
        计算填充
        '''
        ccpp_ccpp_economic = Factory().execute(ccpp_ccpp_economic, form)
        # 更新数据
        Ccpp_ccpp_economic.updata_ccppeconomic(ccpp_ccpp_economic)

    def getInputData(self, planId):
        # 加载页面input数据
        ccpp_ccpp_economic = Ccpp_ccpp_economic.search_economic(planId)
        copyccpp_ccpp_economic = copy.deepcopy(ccpp_ccpp_economic)
        # 单位换算
       
        ccppConstant = CcppConstant.search_ccppConstant('ccpp_economic')
        list_column_furnace = gl.getCcppEconomicName_engList()
        datas = {}
        permissiondata = {}
        defaultvaluedata = {}
        for index in range(len(list_column_furnace)):
            if hasattr(copyccpp_ccpp_economic, list_column_furnace[index]):
                var = getattr(copyccpp_ccpp_economic, list_column_furnace[index])
                datas[list_column_furnace[index]] = gl.format_value(var)

        for constant in ccppConstant:
            permissiondata[constant.name_eng] = constant.permission
            defaultvaluedata[constant.name_eng] = constant.defaultvalue
        return datas, permissiondata, defaultvaluedata
