# -*- coding: utf-8 -*-
from app.models import ReportTemplate, Plan, Company, MyException, EquipmentList, Module
from app.ccpp.models import ccpp_ccpp_calculateModel, ccpp_chimney_calculateModel, ccpp_circulating_waterModel, \
     ccpp_questionnaireModel, ccpp_turbineModel
from app.coal_chp.service.coalService import ToCoalCHP
from app.coal_chp.model.coalchpModels import CoalCHPNeedsQuestionnaire, \
     CoalCHPFurnaceCalculation, CoalCHPCoalHandingSystem,\
     CoalCHPRemovalAshSlag, CoalCHPDesulfurization, CoalCHPCirculatingWater,\
     CoalCHPSmokeAirSystem, CoalCHPBoilerAuxiliaries, \
     CoalCHPTurbineBackpressure, CoalCHPEconomicIndicators,\
     CoalCHPChimney, CoalchpTurbineAuxiliary, CoalCHPOfficialProcess,\
     CoalCHPHeatSupply, CoalCHPChemicalWater
from app.biomass_chp.models.modelsBiomass import BiomassCHPNeedsQuestionnaire,\
     BiomassCHPBoilerCalculation, BiomassCHPFuelStorageTransportation,\
     BiomassCHPDesulfurizationAndDenitrification, BiomassCHPDASRemove,\
     BiomassCHPBoilerAuxiliaries, BiomassCHPTurbineBackpressure, \
     BiomassCHPOfficialProcess, BiomassCHPWaterTreatment, \
     BiomassCHPHeatSupply, BiomassCHPChimney, BiomassCHPCirculatingWater, \
     BiomasschpTurbineAuxiliary, BiomassCHPBoilerAuxiliaries, BiomasschpEconomicIndicators
from app.gpg.model.gasPowerGeneration_models import GasPowerGenerationConstant,\
     GasPowerGenerationNeedsQuestionnaire, GPGBoilerOfPTS, GPGFlueGasAirSystem,\
     GPGSmokeResistance, GPGWindResistance, GPGCirculatingWaterSystem, \
     GPGSmokeAirCalculate, GPGTurbineAuxiliarySystem, GPGSteamWaterPipe, \
     GPGBoilerAuxiliaries, GPGTurbineOfPTS, GasPowerGenerationEconomicIndicators
from app.models import Textlogic
from app.ccpp.service.ccpp_imgService import CcppImgService
from app.gpg.service.gasPowerGeneration_Service import GPGImgService
from app.gpg.service.gasPowerGeneration_Service import ToGPG
from app.biomass_chp.service.biomassService import BiomassImgService, ToBiomassCHP
import re
from config import config
import json
from app.ccpp.service.ccpp_equipmentService import CcppEquipments
from flask import current_app
from app.ccpp import gl


class TemplateDealwithService():

    '''
    通用模板主函数
    '''

    def templateDealwithMian(self, planId, userId):
        current_app.logger.warning(u'完善模板开始......')
        logicDir = TemplateDealwithService().getLogicDir(planId)
        templateContent = TemplateDealwithService().getTemplateContent(planId)
        # 替换逻辑
        current_app.logger.warning(u'替换逻辑......')
        templateContent = TemplateDealwithService().dbreplaceTemplate(templateContent, logicDir)
        # 追加图纸
        current_app.logger.warning(u'追加图纸......')
        templateContent = TemplateDealwithService().reportTemplateappendimg(templateContent, planId, userId)
        # 追加设备表单
        current_app.logger.warning(u'追加设备表单......')
        templateContent = TemplateDealwithService().analyzeEquipmentType(templateContent, planId, userId)
        # 解析模板
        current_app.logger.warning(u'解析模板......')
        originalDir, replaceDir = TemplateDealwithService().analyzeTemplate(templateContent)
        # 设置数据
        current_app.logger.warning(u'设置数据......')
        replaceDir = TemplateDealwithService().setdbdata(originalDir, replaceDir, planId)
        # 替换数据
        current_app.logger.warning(u'替换数据......')
        templateContentresult = TemplateDealwithService().replaceTemplate(templateContent, replaceDir)
        current_app.logger.warning(u'完善模板结束......')
        return templateContentresult

    '''
    通过方案的id得到当前方案所采用的模板
    返回模板的内容。
    '''

    def getTemplateContent(self, planId):
        plan = Plan.search_planById(planId)
        templateId = plan.template_id
        reportTemplate = ReportTemplate.search_templateById(int(templateId) if templateId != '' and templateId is not None else 0)
        if reportTemplate is not None:
            return reportTemplate.template_content
        else:
            return "方案Id传入有误！！！"

    '''
    1、将传入的字符串进行分割,获取@@??@@部分的数据、并建立字典replaceDir：{键：@@??@@, 值：eval(??)}
    2、将@@??@@部分的数据进行再次通过+、-、*、/、^分割
    3、解析字典replaceDir的值：替换、计算
    4、返回字典replaceDir
    '''

    def analyzeTemplate(self, templateContent):
        prefixlist = ['coalchp_', 'biomasschp_', 'ccpp_', 'gaspowergeneration_', 'company', 'plan', 'round']
        replaceDir = {}
        originalDir = {}
        resultcontent = ''
        pattern = re.compile(r'^' + prefixlist[0] + '|' + prefixlist[1] + '|' + prefixlist[2] + '|' + prefixlist[3] + '|' + prefixlist[4] + '|' + prefixlist[5] + '|' + prefixlist[6])
        templateContentList = templateContent.split('@@')
        # templateContentList中包含：单变量、纯文本、逻辑、复杂变量
        for content in templateContentList:
            # 将正则表达式编译成Pattern对象
            match = pattern.match(content)
            # 将纯文本排除剩余：单变量、逻辑、复杂变量
            if match is not None or content.find("if") != -1:
                # 目的将逻辑、复杂变量中的变量取出
                contentlist = re.split('\\+|\\*|/|\\-|\\(|\\)|^| |>|<|\'|\\"', content)
                resultcontent = content
                for originalContent in contentlist:
                    match = pattern.match(originalContent)
                    if match is not None and originalContent.find('_') != -1 and originalContent.find('.') != -1:
                        originalDir[originalContent] = originalContent
                replaceDir['@@' + content + '@@'] = resultcontent
        return originalDir, replaceDir

    '''
    根据方案模块id查询数据，设置进originalDir字典当中
    替换replaceDir中的value值，返回replaceDir
    '''

    def setdbdata(self, originalDir, replaceDir, planId):
        # 查询原始数据
        for key in originalDir:
            value = originalDir[key]
            if value.find('.') != -1:
                valuelist = value.split('.')
                originalDir[key] = TemplateDealwithService().getdbdata(valuelist[0], valuelist[1], planId)
        # 更新替换数据
        for key in replaceDir:
            resultcontent = replaceDir[key]
            contentlist = re.split('\\+|\\*|/|\\-|\\(|\\)|^| |>|<|\'|\\"|,', resultcontent)
            for cont in contentlist:
                if originalDir.has_key(cont):
                    a = u'[This value is None, fill in manually]'
                    # 替换逻辑数据
                    if resultcontent.find("'" + str(cont) + "'") != -1 or resultcontent.find('"' + str(cont) + '"') != -1:
                        resultcontent = resultcontent.replace(u"'" + str(cont) + "'", str(originalDir[cont] if originalDir[cont] is not None else a), len(resultcontent))
                    
                    if resultcontent.find('"' + str(cont) + '"') != -1:
                        resultcontent = resultcontent.replace(u'"' + str(cont) + '"', u'"' + str(originalDir[cont] if originalDir[cont] is not None else a) + '"', len(resultcontent))
                    
                    # 替换非逻辑数据
                    if resultcontent.find(str(cont)) != -1 and resultcontent.find(str("\' if \"")) == -1:
                        trplaceval = originalDir[cont] if originalDir[cont] is not None else a
                        # 对初始化字典中的值是汉字和数据的情况进行分类处理：解决编码问题
                        if str(type(trplaceval)) == "<type 'unicode'>":
                            resultcontent = resultcontent.replace(str(cont), originalDir[cont] if originalDir[cont] is not None else a, len(resultcontent))
                        else:
                            resultcontent = resultcontent.replace(str(cont), str(originalDir[cont] if originalDir[cont] is not None else a), len(resultcontent))
            if resultcontent.find('\' if \"') == -1 and resultcontent.find(a) != -1:
                replaceDir[key] = a
            else:
                try:
                    if resultcontent.find('4567893213215641231413228454') != -1 and '4567893213215641231413228454' != str(eval(resultcontent)):
                        replacedir_key = eval(str(eval(resultcontent)))
                        if replacedir_key is not None and str(type(replacedir_key)) == "<type 'float'>":
                            replacedir_key = float('%.2f' % replacedir_key)
                        replaceDir[key] = replacedir_key
                    elif '4567893213215641231413228454' == str(eval(resultcontent)):
                        replaceDir[key] = ''
                    else:
                        replacedir_key = eval(resultcontent)
                        if replacedir_key is not None and str(type(replacedir_key)) == "<type 'float'>":
                            replacedir_key = float('%.2f' % replacedir_key)
                        replaceDir[key] = replacedir_key
                except SyntaxError:
                    replaceDir[key] = resultcontent
                except NameError:
                    replaceDir[key] = resultcontent
        # 将解析后的单变量、逻辑、复杂变量的字典返回。即：replaceDir字典不会存在包含关系，因为键值均为：@@***@@模式
        return replaceDir

    '''
    根据plan_id和表名和字段名称返回对应的值
    '''

    def getdbdata(self, tablename, fieldname, plan_id):
        if tablename == 'biomasschp_boiler_auxiliaries':
            modeldata = BiomassCHPBoilerAuxiliaries.search_auxiliaries(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_boiler_calculation':
            modeldata = BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    # return float('%.2f' % float(getattr(modeldata, fieldname)))
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_chimney':
            modeldata = BiomassCHPChimney.search_biomassCHPChimney(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_circulating_water':
            modeldata = BiomassCHPCirculatingWater.search_circulating_water(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_das_remove':
            modeldata = BiomassCHPDASRemove.search_dasRemove(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_des_den':
            modeldata = BiomassCHPDesulfurizationAndDenitrification.search_des_den(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_fuel_st':
            modeldata = BiomassCHPFuelStorageTransportation.search_storage_transportation(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_heat_supply':
            modeldata = BiomassCHPHeatSupply.search_heatSupply(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_needs_questionnaire':
            modeldata = BiomassCHPNeedsQuestionnaire.search_questionnaire(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_official_process':
            modeldata = BiomassCHPOfficialProcess.search_official(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_turbine_auxiliary':
            modeldata = BiomasschpTurbineAuxiliary.search_turbine_auxiliary(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_turbine_backpressure':
            modeldata = BiomassCHPTurbineBackpressure.search_turbineBackpressure(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_water_treatment':
            modeldata = BiomassCHPWaterTreatment.search_water(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'biomasschp_economic_indicators':
            modeldata = BiomasschpEconomicIndicators.search_economic_indicators(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return gl.item_format(getattr(modeldata, fieldname))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'ccpp_ccpp':
            modeldata = ccpp_ccpp_calculateModel.Ccpp_ccpp.search_ccpp_ccpp(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'ccpp_chimney_calculate':
            modeldata = ccpp_chimney_calculateModel.CcppChimneyCalculate.search_chimney_calculate(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'ccpp_circulating_water':
            modeldata = ccpp_circulating_waterModel.CcppCirculatingWater.search_circulating_water(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'ccpp_questionnaire':
            modeldata = ccpp_questionnaireModel.Questionnaire.search_questionnaire(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'ccpp_turbine':
            modeldata = ccpp_turbineModel.CcppTurbine.search_CcppTurbine(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_boiler_auxiliaries':
            modeldata = CoalCHPBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_circulating_water':
            modeldata = CoalCHPCirculatingWater.search_circulating_water(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_coal_handingsystem':
            modeldata = CoalCHPCoalHandingSystem.search_handing_system(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_desulfurization_denitrification':
            modeldata = CoalCHPDesulfurization.search_desulfurization(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_furnace_calculation':
            modeldata = CoalCHPFurnaceCalculation.search_furnace_calculation(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_needs_questionnaire':
            modeldata = CoalCHPNeedsQuestionnaire.search_questionnaire(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_removal_ash_slag_system':
            modeldata = CoalCHPRemovalAshSlag.search_removal_ash_slag(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_smoke_air_system':
            modeldata = CoalCHPSmokeAirSystem.search_smoke_air_system(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_turbine_backpressure':
            modeldata = CoalCHPTurbineBackpressure.search_turbineBackpressure(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_economic_indicators':
            modeldata = CoalCHPEconomicIndicators.search_economic_indicators(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_chemical_water':
            modeldata = CoalCHPChemicalWater.search_chemical_water(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_chimney':
            modeldata = CoalCHPChimney.search_coalCHPChimney(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_turbine_auxiliary':
            modeldata = CoalchpTurbineAuxiliary.search_turbine_auxiliary(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_heat_supply':
            modeldata = CoalCHPHeatSupply.search_heatSupply(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'coalchp_official_process':
            modeldata = CoalCHPOfficialProcess.search_official(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_boiler_auxiliaries':
            modeldata = GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_boiler_of_pts':
            modeldata = GPGBoilerOfPTS.search_BoilerOfPTS(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_circulating_water_system':
            modeldata = GPGCirculatingWaterSystem.search_CirculatingWater(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_gas_air_system':
            modeldata = GPGFlueGasAirSystem.search_FlueGasAirSystem(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_needsquestionnaire':
            modeldata = GasPowerGenerationNeedsQuestionnaire.search_questionnaire(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_smoke_air_calculate':
            modeldata = GPGSmokeAirCalculate.search_SmokeAirCalculate(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_smoke_resistance':
            modeldata = GPGSmokeResistance.search_SmokeResistance(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_steam_water_pipe':
            modeldata = GPGSteamWaterPipe.search_SteamWaterPipe(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_turbine_auxiliary_system':
            modeldata = GPGTurbineAuxiliarySystem.search_TurbineAuxiliary(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_turbine_of_pts':
            modeldata = GPGTurbineOfPTS.search_TurbineOfPTS(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_wind_resistance':
            modeldata = GPGWindResistance.search_WindResistance(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'gaspowergeneration_economic_indicators':
            modeldata = GasPowerGenerationEconomicIndicators.search_economic_indicators(plan_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)                 
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'company':
            plan = Plan.search_planById(plan_id)
            modeldata = Company.search_companyById(plan.company_id)
            if hasattr(modeldata, fieldname.encode('utf-8')):
                data = getattr(modeldata, fieldname)
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(modeldata, fieldname)))
                else:
                    return getattr(modeldata, fieldname)
            else:
                return None
        elif tablename == 'plan':
            plan = Plan.search_planById(plan_id)
            if hasattr(plan, fieldname.encode('utf-8')):
                data = getattr(plan, fieldname)
                if data is not None and str(type(data)) == "<class 'decimal.Decimal'>":
                    return float('%.2f' % float(getattr(plan, fieldname)))
                else:
                    return getattr(plan, fieldname)
            else:
                return None
        else:
            return None

    '''
    替换， 返回结果文本
    '''

    def replaceTemplate(self, templateContent, replaceDir):
        templateContentresult = templateContent
        print("替换， 返回结果文本")
        current_app.logger.warning(u'替换， 返回结果文本')
        for key in replaceDir:
            if str(type(replaceDir[key])) == "<type 'unicode'>":
                templateContentresult = templateContentresult.replace(key, replaceDir[key], len(templateContentresult))
            else:
                templateContentresult = templateContentresult.replace(key, str(replaceDir[key]).decode('utf-8'), len(templateContentresult))
        return templateContentresult

    '''  
    数据库替换， 返回结果文本for logic
    '''

    def dbreplaceTemplate(self, templateContent, replaceDir):
        current_app.logger.warning(u'逻辑替换')
        templateContentresult = templateContent
        print("数据库替换， 返回结果文本for logic")
        current_app.logger.warning(u'数据库替换， 返回结果文本for logic')
        for key in replaceDir:
            templateContentresult = templateContentresult.replace(key, replaceDir[key], len(templateContentresult))
        return templateContentresult

    '''
    获得逻辑字典
    '''
    def getLogicDir(self, planId):
        logicDir = {}
        plan = Plan.search_planById(planId)
        reportTemplate = ReportTemplate.search_templateById(plan.template_id)
        textlogiclist = Textlogic.search_by_module(reportTemplate.module_id)
        for textlogic in textlogiclist:
            logicDir[textlogic.textlogickey] = textlogic.textlogicvalue
        return logicDir

    '''
    生成图纸
    追加图纸信息
    '''
    def reportTemplateappendimg(self, templateContent, planId, user_id):
        plan = Plan.search_planById(planId)
        reportTemplate = ReportTemplate.search_templateById(plan.template_id)
        if reportTemplate.module_id == Module.CCPP:
            # 生成图纸
            ccpp, ccppTurbine = CcppImgService().imgCreate(planId, user_id)
            current_app.logger.warning(u'生成图纸')
            # 追加图纸
            allimgpathmd = CcppImgService().getccppimginfo(ccpp, ccppTurbine, planId, user_id)
            current_app.logger.warning(u'生成图纸地址:\n%s', allimgpathmd)
            if allimgpathmd is not None:
                return templateContent + allimgpathmd
            else:
                return templateContent
        elif reportTemplate.module_id == Module.coalCHP:
            # 生成图片
            templateContent = ToCoalCHP.generate_img(planId, templateContent, -1)
            return templateContent
        elif reportTemplate.module_id == Module.biomassCHP:
            # 生成图片
            BiomassImgService().imgCreate(planId)
            # 水处理图纸
            waterPic = TemplateDealwithService().getBiomassWaterImgInfo(planId)
            if waterPic is None:
                waterPic = ""
            # 除灰图纸
            dustPic = TemplateDealwithService().getBiomassDustImgInfo(planId)
            if dustPic is None:
                dustPic = ""
            # 除渣图纸
            ashPic = TemplateDealwithService().getBiomassAshImgInfo(planId)
            if ashPic is None:
                ashPic = ""
            # 运输图纸
            transPic = TemplateDealwithService().getBiomassTransImgInfo(planId)
            if transPic is None:
                transPic = ""
            # 燃烧图纸
            firePic = TemplateDealwithService().getBiomassFireImgInfo(planId)
            if firePic is None:
                firePic = ""
            # 热力图纸
            hotPic = TemplateDealwithService().getBiomassHotImgInfo(planId)
            if hotPic is None:
                hotPic = ""
            
            wordString = u'# 附件一  图纸\n'
            return templateContent + wordString + waterPic + dustPic + ashPic + transPic + firePic + hotPic

        elif reportTemplate.module_id == Module.gasPowerGeneration:
            GPGImgService().imgCreate(planId)
            return templateContent + TemplateDealwithService().getGPGImgInfo(planId)

    '''获得Biomass水处理图纸的信息 '''
    def getBiomassWaterImgInfo(self, planId):
        biomassCHPWaterTreatmentData = BiomassCHPWaterTreatment.search_water(planId)
        o_process_route = getattr(biomassCHPWaterTreatmentData, 'o_process_route')
        # 根据不同的工艺路线，出力不同的原则性化学水处理系统图
        if o_process_route == "1":
            return u'''
##### 原则性化学水处理系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_water1_''' + str(planId) + u'''.png)
'''
        else:
            if o_process_route == "2":
                return u'''
##### 原则性化学水处理系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_water2_''' + str(planId) + u'''.png)
'''

    '''获得Biomass除灰图纸的信息 '''
    def getBiomassDustImgInfo(self, planId):

        return u'''
##### 原则性除灰系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_dust_''' + str(planId) + u'''.png)
'''


    '''获得Biomass除渣图纸的信息 '''
    def getBiomassAshImgInfo(self, planId):
        biomassCHPBoilerCalculationData = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
        boiler_type = getattr(biomassCHPBoilerCalculationData, 'boiler_type')

        #根据不同的锅炉种类，出力不同的原则性除渣系统图
        if boiler_type == "1" or boiler_type == "2":
            return u'''
##### 原则性除渣系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_ash1_''' + str(planId) + u'''.png)
'''
        else:
            if boiler_type == "3" or boiler_type == "4":
                return u'''
##### 原则性除渣系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_ash2_''' + str(planId) + u'''.png)
'''

    '''获得Biomass燃料运输图纸的信息 '''
    def getBiomassTransImgInfo(self, planId):
        biomassCHPFuelStorageTransportationData = BiomassCHPFuelStorageTransportation.search_storage_transportation(planId)
        f_belt_number = getattr(biomassCHPFuelStorageTransportationData, 'f_belt_number')

        #根据单路，双路布置，出力不同的原则性燃料输送系统图
        if f_belt_number == 1.0:
            return u'''
##### 原则性燃料输送系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_trans1_''' + str(planId) + u'''.png)
'''
        else:
            if f_belt_number == 2.0:
                return u'''
##### 原则性燃料输送系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_trans2_''' + str(planId) + u'''.png)
'''


    '''获得Biomass燃烧图纸的信息 '''
    def getBiomassFireImgInfo(self, planId):
        biomassCHPBoilerCalculationData = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
        boiler_type = getattr(biomassCHPBoilerCalculationData, 'boiler_type')

        #根据不同的锅炉种类，出力不同的原则性除渣系统图
        if boiler_type == "1":
            return u'''
##### 原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_fire1_''' + str(planId) + u'''.png)
'''
        if boiler_type == "3":
            return u'''
##### 原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_fire2_''' + str(planId) + u'''.png)
'''

        if boiler_type == "2":
            return u'''
##### 原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_fire3_''' + str(planId) + u'''.png)
'''

        if boiler_type == "4":
            return u'''
##### 原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_fire4_''' + str(planId) + u'''.png)
'''   

    '''获得Biomass热力图纸的信息 '''
    def getBiomassHotImgInfo(self, planId):

        # 根据不同的给水温度，回热级数，冷却塔类型，出力不同的热力系统图
        biomassCHPTurbineBackpressureData = BiomassCHPTurbineBackpressure.search_turbineBackpressure(planId)
        biomassCHPCirculatingWaterData = BiomassCHPCirculatingWater.search_circulating_water(planId)

        # 给水温度
        hh1_water_temperature = getattr(biomassCHPTurbineBackpressureData, 'hh1_water_temperature')
        # 高加级数
        s_hh_grade = getattr(biomassCHPTurbineBackpressureData, 's_hh_grade')
        # 低加级数
        s_lh_grade = getattr(biomassCHPTurbineBackpressureData, 's_lh_grade')   
        # 冷却塔类型
        p_select = getattr(biomassCHPCirculatingWaterData, 'p_select')

        if hh1_water_temperature == 215 and s_hh_grade == 2 and s_lh_grade == 3:
            if p_select == "1":
                return u'''
##### 原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_hot1a_''' + str(planId) + u'''.png)
'''  
            else:
                if p_select == "2":
                    return u'''
##### 原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_hot1b_''' + str(planId) + u'''.png)
'''                      

        if hh1_water_temperature == 158 and s_hh_grade == 0 and s_lh_grade == 2:
            if p_select == "1":
                return u'''
##### 原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_hot2a_''' + str(planId) + u'''.png)
'''                 
            else:                        
                if p_select == "2":
                    return u'''
##### 原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_hot2b_''' + str(planId) + u'''.png)
'''                      

        if hh1_water_temperature == 150 and s_hh_grade == 1 and s_lh_grade == 1:
            if p_select == "1":
                return u'''
##### 原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_hot3a_''' + str(planId) + u'''.png)
'''                  
            else:
                if p_select == "2":
                    return u'''
##### 原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/biomassimgpreview/biomass_hot3b_''' + str(planId) + u'''.png)
'''                  
                    

    '''获得GPG追加图纸的信息 '''
    def getGPGImgInfo(self, planId):
        gpg_CirculatingWaterData = GPGCirculatingWaterSystem.search_CirculatingWater(planId)
        cooling_tower_selected_type = getattr(gpg_CirculatingWaterData, 'cooling_tower_selected_type')

        gpg_BoilerAuxiliariesData = GPGBoilerAuxiliaries.search_boiler_auxiliaries(planId)
        desalted_water_tech_type = getattr(gpg_BoilerAuxiliariesData, 'desalted_water_tech_type')

        if cooling_tower_selected_type != '' and cooling_tower_selected_type is not None:
            if desalted_water_tech_type != '' and desalted_water_tech_type is not None:
                if float(cooling_tower_selected_type) == 1.0 and float(desalted_water_tech_type) == 1.0:
                    return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
##### (P2)原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_ptsA_''' + str(planId) + u'''.png)
##### (P3)原则性化学水处理系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcwtA_''' + str(planId) + u'''.png)
'''
                elif float(cooling_tower_selected_type) == 1.0 and float(desalted_water_tech_type) == 2.0:
                    return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
##### (P2)原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_ptsA_''' + str(planId) + u'''.png)
##### (P3)原则性化学水处理系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcwtB_''' + str(planId) + u'''.png)
'''
                elif float(cooling_tower_selected_type) == 2.0 and float(desalted_water_tech_type) == 1.0:
                    return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
##### (P2)原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_ptsB_''' + str(planId) + u'''.png)
##### (P3)原则性化学水处理系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcwtA_''' + str(planId) + u'''.png)
'''
                elif float(cooling_tower_selected_type) == 2.0 and float(desalted_water_tech_type) == 2.0:
                    return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
##### (P2)原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_ptsB_''' + str(planId) + u'''.png)
##### (P3)原则性化学水处理系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcwtB_''' + str(planId) + u'''.png)
'''
            elif float(cooling_tower_selected_type) == 1.0:
                return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
##### (P2)原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_ptsA_''' + str(planId) + u'''.png)
'''
            elif float(cooling_tower_selected_type) == 2.0:
                return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
##### (P2)原则性热力系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_ptsB_''' + str(planId) + u'''.png)
'''
        elif desalted_water_tech_type != '' and desalted_water_tech_type is not None:
            if float(desalted_water_tech_type) == 1.0:
                return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
##### (P2)原则性化学水处理系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcwtA_''' + str(planId) + u'''.png)
'''
            elif float(desalted_water_tech_type) == 2.0:
                return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
##### (P2)原则性化学水处理系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcwtB_''' + str(planId) + u'''.png)
'''
        else:
            return u'''
# 附件一 图纸\n##### (P1)原则性燃烧系统图
##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/gpgimgpreview/''' + str(planId) + '''/gpg_pcs_''' + str(planId) + u'''.png)
'''

    def analyzeEquipmentType(self, templateContent, planId, userId):
        current_app.logger.warning(u'生成设备清单')
        mdtitletotitle = None
        tbodyString = None
        plan = Plan.search_planById(planId)
        if plan.module_id == Module.coalCHP:
            # 更新数据库最新json值
            ToCoalCHP.replaceDeviceJson(planId)
            titledict = ToCoalCHP.getmdtitledict()
            tbodyString = u'\n# 附件二  设备清册（最终参数、数量、名称以施工图设计为准）\n'
        elif plan.module_id == Module.biomassCHP:
            titledict = ToBiomassCHP.getmdtitledict(planId)
            tbodyString = u'\n# 附件二 设备清册（最终参数、数量、名称以施工图设计为准）\n'
        elif plan.module_id == Module.CCPP:
            titledict, mdtitletotitle = CcppEquipments.getmdtitledict()
            allimgpathmd = CcppImgService().getccppimginfo(None, None, planId, userId)
            if allimgpathmd is not None:
                tbodyString = u'\n# 附件二  设备清册（最终参数、数量、名称以施工图设计为准）\n'
            else:
                tbodyString = u'\n# 附件一  设备清册（最终参数、数量、名称以施工图设计为准）\n'
        elif plan.module_id == Module.gasPowerGeneration:
            titledict = ToGPG.getmdtitledict()
            tbodyString = u'\n# 附件二: 设备清册（最终参数、数量、名称以施工图设计为准）\n'
        else:
            pass

        equipmentList = EquipmentList.search_equipmentList(planId)
        data = json.loads(equipmentList.equipment_content)
        equipmentCount = len(data['equipment_name'])

        tbodyString += u'| 序号 |名称 |型号及规格 |数量 |单位 |备注|\n|:------|:------|:------|:------|:------|:------|\n'
        keylist = titledict.keys()
        keylist.sort()

        # 生物质模块项目出力判断逻辑
        if plan.module_id == Module.biomassCHP:
            # 锅炉
            furnaceCalculation = BiomassCHPBoilerCalculation.search_furnace_calculation(
                planId)
            # 循环水
            circulatingWater = BiomassCHPCirculatingWater.search_circulating_water(
                planId)
            # 汽轮机
            turbineBackpressure = BiomassCHPTurbineBackpressure.search_turbineBackpressure(
                planId)

            if furnaceCalculation.boiler_type == "1" or furnaceCalculation.boiler_type == "2":
                if circulatingWater.p_select == '1':
                    keylist.remove('e2')
                    keylist.remove('h12')
                else:
                    if circulatingWater.p_select == '2':
                        keylist.remove('e2')
                        keylist.remove('h11')

            elif furnaceCalculation.boiler_type == "3" or furnaceCalculation.boiler_type == "4":
                if circulatingWater.p_select == '1':
                    keylist.remove('e1')
                    keylist.remove('h12')
                else:
                    if circulatingWater.p_select == '2':
                        keylist.remove('e1')
                        keylist.remove('h11')
            else:
                pass

            if turbineBackpressure.e_exhaust_point_flow == 0:
                keylist.remove('h5')

            for key in keylist:
                if mdtitletotitle is not None and mdtitletotitle[key] is not None:
                    tbodyString += u'|' + mdtitletotitle[key] + u'|' + titledict[key] + u'| | | | |\n'
                else:
                    tbodyString += u'| |' + titledict[key] + u'| | | | |\n'

                index = 1
                # 启动锅炉判断flag
                noStart = False
                # 热网补水泵判断flag
                noWater = False
                for j in range(0, equipmentCount):
                    if data['equipment_uid'][j] == '29' and data['equipment_content'][j] == '':
                        noStart = True
                    else:
                        noStart = False

                    if data['equipment_uid'][j] == '196' and turbineBackpressure.e_exhaust_point_flow == 0:
                        noWater = True
                    else:
                        noWater = False

                    if data['equipment_type'][j] == key and noStart == False and noWater == False:
                        tbodyString += u'|' + str(index) +\
                                    u'|' + data['equipment_name'][j] +\
                                    u'|' + data['equipment_content'][j] +\
                                    u'|' + data['equipment_count'][j] +\
                                    u'|' + data['equipment_unit'][j] +\
                                    u'|注:' + data['equipment_remark'][j] +\
                                    u'\n'
                        index += 1
        # 生物质以外模块        
        else:
            for key in keylist:
                if mdtitletotitle is not None and mdtitletotitle[key] is not None:
                    tbodyString += u'|' + mdtitletotitle[key] + u'|' + titledict[key] + u'| | | | |\n'
                else:
                    tbodyString += u'| |' + titledict[key] + u'| | | | |\n'

                index = 1
                for j in range(0, equipmentCount):
                    if data['equipment_type'][j] == key:
                        tbodyString += u'|' + str(index) +\
                                    u'|' + data['equipment_name'][j] +\
                                    u'|' + data['equipment_content'][j] +\
                                    u'|' + data['equipment_count'][j] +\
                                    u'|' + data['equipment_unit'][j] +\
                                    u'|注:' + data['equipment_remark'][j] +\
                                    u'\n'
                        index += 1
        # tbodyString += u'|d2342344   | d234234444444444444444444444442  |d2342344444444444444444444444424444444 |  d23421 | d23423 | d23423444444444444444442  |\n'
        return templateContent + tbodyString


def main():
    pass


if __name__ == '__main__':
    main()
