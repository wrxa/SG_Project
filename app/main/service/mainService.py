# -*- coding: utf-8 -*-
from app.models import Plan, Module, Company, User, EquipmentList, \
     EquipmentListTemplate, ReportTemplate
import os
from app.ccpp.service.ccpp_questionService import QuestionService
from app.ccpp.service.ccpp_ccppService import CcppCalculateService
from app.ccpp.service.ccpp_circulating_waterService import CirculatingWaterService
from app.ccpp.service.ccpp_turbineService import CcppTurbineService
from app.ccpp.service.ccpp_chimney_calculateService import \
    ChimneyCalculateService
from app.ccpp.service.ccpp_TurbineAuxiliary import CcppTurbineAuxiliaryService
from app.coal_chp.model.coalchpModels import CoalCHPNeedsQuestionnaire, \
     CoalCHPFurnaceCalculation, CoalCHPCoalHandingSystem,\
     CoalCHPRemovalAshSlag, CoalCHPDesulfurization, CoalCHPCirculatingWater,\
     CoalCHPSmokeAirSystem, CoalCHPBoilerAuxiliaries, \
     CoalCHPTurbineBackpressure, CoalCHPEconomicIndicators, CoalCHPChimney,\
     CoalchpTurbineAuxiliary, CoalCHPOfficialProcess, CoalCHPHeatSupply,\
     CoalCHPChemicalWater
from app.coal_chp.service.coalService import ToCoalCHP
from app.biomass_chp.models.modelsBiomass import BiomassCHPNeedsQuestionnaire,\
     BiomassCHPBoilerCalculation, BiomassCHPFuelStorageTransportation,\
     BiomassCHPDesulfurizationAndDenitrification, BiomassCHPDASRemove,\
     BiomassCHPBoilerAuxiliaries, BiomassCHPTurbineBackpressure, \
     BiomassCHPOfficialProcess, BiomassCHPWaterTreatment, \
     BiomassCHPHeatSupply, BiomassCHPChimney, BiomassCHPCirculatingWater, \
     BiomasschpTurbineAuxiliary, BiomasschpEconomicIndicators
from app.gpg.model.gasPowerGeneration_models import GasPowerGenerationConstant,\
     GasPowerGenerationNeedsQuestionnaire, GPGBoilerOfPTS, GPGFlueGasAirSystem,\
     GPGSmokeResistance, GPGWindResistance, GPGCirculatingWaterSystem, \
     GPGSmokeAirCalculate, GPGTurbineAuxiliarySystem, GPGSteamWaterPipe, \
     GPGBoilerAuxiliaries, GPGTurbineOfPTS, GasPowerGenerationEconomicIndicators
from app.ccpp.service.ccpp_planservice import getCcppPlanData, CcppPlanService
from app.gpg.service.gasPowerGeneration_Service import getGPGPlanData
from app.biomass_chp.service.biomass_planservice import getBiomassPlanData
from app.biomass_chp.service.biomassService import ToBiomassCHP
import sqlalchemy
import json
import urllib
from config import Config, config
from app.ccpp.service.ccpp_economicService import EconomicService
from app.ccpp.service.ccpp_imgService import CcppImgService
from app.ccpp.service.ccpp_biomassService import BiomassService as CcppWaterTreatmentService
from util.get_all_path import GetPath
from util.annotation import db_transaction
from app.energy_island.models import EnergyIslandRequirement


class MainService():
    @staticmethod
    def findMDTemplate(moduleName, planId):
        if moduleName != Module.biomassCHP:
            filename = os.path.join(os.getcwd(), "mark_to_docx/inputfile/template",
                                    moduleName + ".md")
            file_object = open(filename)
        else:
            BiomassFlg = False
            BiomassFlg = ToBiomassCHP.IsBiomass(planId)
            if BiomassFlg is False:
                filename = os.path.join(os.getcwd(), "mark_to_docx/inputfile/template", moduleName + "0.md")
            else:
                filename = os.path.join(os.getcwd(), "mark_to_docx/inputfile/template", moduleName + "1.md")
            file_object = open(filename)

        try:
            all_the_text = file_object.read()
            if moduleName == Module.CCPP:
                all_the_text = all_the_text.decode('utf8')
                plandocxcolumdir = getCcppPlanData(planId)
                for key in plandocxcolumdir:
                    if str(type(plandocxcolumdir[key])) == "<type 'unicode'>":
                        all_the_text = all_the_text.replace((key), plandocxcolumdir[key], len(all_the_text))
                    else:
                        all_the_text = all_the_text.replace((key), str(plandocxcolumdir[key]), len(all_the_text))

            elif moduleName == Module.gasPowerGeneration:
                all_the_text = all_the_text.decode('utf8')
                gpgMdTemplateData = getGPGPlanData(planId)
                for key in gpgMdTemplateData:
                    if str(type(gpgMdTemplateData[key])) == "<type 'unicode'>":
                        all_the_text = all_the_text.replace((key), gpgMdTemplateData[key], len(all_the_text))
                    else:
                        all_the_text = all_the_text.replace((key), str(gpgMdTemplateData[key]), len(all_the_text))

            elif moduleName == Module.biomassCHP:
                all_the_text = all_the_text.decode('utf8')
                plandocxcolumdir = getBiomassPlanData(planId)
                for key in plandocxcolumdir:
                    if str(type(plandocxcolumdir[key])) == "<type 'unicode'>":
                        all_the_text = all_the_text.replace((key), plandocxcolumdir[key], len(all_the_text))
                    else:
                        all_the_text = all_the_text.replace((key), str(plandocxcolumdir[key]), len(all_the_text))

        finally:
            file_object.close()

        if moduleName == Module.coalCHP:
            all_the_text = ToCoalCHP.coverCoalReport(all_the_text, planId)

        return all_the_text

    @staticmethod
    @db_transaction
    def drop_plan_ccpp(plan_id, userId):
        CcppImgService().deletebyPlanIdandUserId(plan_id, userId)
        CcppCalculateService().deletebyPlanId(plan_id)
        QuestionService().deletebyPlanId(plan_id)
        ChimneyCalculateService().deletebyPlanId(plan_id)
        CcppTurbineService().deletebyPlanId(plan_id)
        CcppTurbineAuxiliaryService().deletebyPlanId(plan_id)
        CirculatingWaterService().deletebyPlanId(plan_id)
        EconomicService().deletebyPlanId(plan_id, userId)
        CcppWaterTreatmentService().deletebyPlanId(plan_id)
        EquipmentList.deletebyPlanId(plan_id)
        CcppPlanService().deletebyPlanId(plan_id)

    @staticmethod
    @db_transaction
    def drop_plan_coalchp(plan_id):
        ToCoalCHP.deleteFile(plan_id)
        CoalCHPNeedsQuestionnaire.deletebyPlanId(plan_id)
        CoalCHPFurnaceCalculation.deletebyPlanId(plan_id)
        CoalCHPCoalHandingSystem.deletebyPlanId(plan_id)
        CoalCHPRemovalAshSlag.deletebyPlanId(plan_id)
        CoalCHPDesulfurization.deletebyPlanId(plan_id)
        CoalCHPCirculatingWater.deletebyPlanId(plan_id)
        CoalCHPSmokeAirSystem.deletebyPlanId(plan_id)
        CoalCHPBoilerAuxiliaries.deletebyPlanId(plan_id)
        CoalCHPTurbineBackpressure.deletebyPlanId(plan_id)
        CoalCHPEconomicIndicators.deletebyPlanId(plan_id)
        CoalCHPChimney.deletebyPlanId(plan_id)
        CoalchpTurbineAuxiliary.deletebyPlanId(plan_id)
        CoalCHPOfficialProcess.deletebyPlanId(plan_id)
        CoalCHPHeatSupply.deletebyPlanId(plan_id)
        CoalCHPChemicalWater.deletebyPlanId(plan_id)
        EquipmentList.deletebyPlanId(plan_id)
        Plan.deletebyPlanId(plan_id)

    @staticmethod
    def drop_plan_biomass(plan_id):
        BiomassCHPNeedsQuestionnaire.delete_questionnaire(plan_id)
        BiomassCHPBoilerCalculation.delete_furnace_calculation(plan_id)
        BiomassCHPFuelStorageTransportation.delete_storage_transportation(plan_id)
        BiomassCHPDesulfurizationAndDenitrification.delete_des_den(plan_id)
        BiomassCHPDASRemove.delete_dasRemove(plan_id)
        BiomassCHPBoilerAuxiliaries.delete_auxiliaries(plan_id)
        BiomassCHPOfficialProcess.delete_official(plan_id)
        BiomassCHPWaterTreatment.delete_water(plan_id)
        BiomassCHPTurbineBackpressure.delete_turbineBackpressure(plan_id)
        BiomassCHPChimney.delete_biomassCHPChimney(plan_id)
        BiomassCHPHeatSupply.delete_heatSupply(plan_id)
        BiomassCHPCirculatingWater.delete_circulating_water(plan_id)
        BiomasschpTurbineAuxiliary.delete_turbine_auxiliary(plan_id)
        BiomasschpEconomicIndicators.delete_economic_indicators(plan_id)
        EquipmentList.delete_equipmentList(plan_id)
        Plan.delete_plan(plan_id)

    @staticmethod
    @db_transaction
    def drop_plan_gpg(plan_id):
        Dir = config['imgConfig'].GPG_IMG_PATH_RESULT + '/' + str(plan_id)
        MainService.del_file(Dir)

        GasPowerGenerationNeedsQuestionnaire.deletebyPlanId(plan_id)
        GPGBoilerOfPTS.deletebyPlanId(plan_id)
        GPGFlueGasAirSystem.deletebyPlanId(plan_id)
        GPGSmokeResistance.deletebyPlanId(plan_id)
        GPGWindResistance.deletebyPlanId(plan_id)
        GPGCirculatingWaterSystem.deletebyPlanId(plan_id)
        GPGSmokeAirCalculate.deletebyPlanId(plan_id)
        GPGTurbineAuxiliarySystem.deletebyPlanId(plan_id)
        GPGSteamWaterPipe.deletebyPlanId(plan_id)
        GPGBoilerAuxiliaries.deletebyPlanId(plan_id)
        GPGTurbineOfPTS.deletebyPlanId(plan_id)
        GasPowerGenerationEconomicIndicators.deletebyPlanId(plan_id)
        EquipmentList.deletebyPlanId(plan_id)
        Plan.deletebyPlanId(plan_id)

    @staticmethod
    @db_transaction
    def drop_plan_energyIsland(plan_id):
        EnergyIslandRequirement.batch_delete_requirement(plan_id)
        Plan.deletebyPlanId(plan_id)

    @staticmethod
    def to_planJson(plans):
        datas = []
        for plan in plans:
            planData = {}
            planData['id'] = getattr(plan, 'id')
            planData['company_id'] = getattr(plan, 'company_id')
            planData['user_id'] = getattr(plan, 'user_id')
            planData['company_location'] = getattr(plan, 'company_location')
            planData['plan_update_date'] = str(
                getattr(plan, 'plan_update_date'))[0:19]
            planData['plan_create_date'] = str(
                getattr(plan, 'plan_create_date'))[0:19]
            planData['plan_report_html'] = getattr(plan, 'plan_report_html')
            planData['moduleName'] = getattr(plan, 'module_id')
            planData['plan_state'] = getattr(plan, 'plan_state')
            planData['template_id'] = getattr(plan, 'template_id')

            planData['plan_name'] = getattr(plan, 'plan_name')

            main_equipment_para = getattr(plan, 'main_equipment_para')
            planData['main_equipment_para'] = main_equipment_para
            main_equipment_para_list = MainService.splitStringToList(main_equipment_para, '\n')
            planData['main_equipment_para_list'] = main_equipment_para_list

            planData['approver_id'] = getattr(plan, 'approver_id')
            planData['approve_time'] = str(
                getattr(plan, 'approve_time'))[0:19]
            datas.append(planData)
        return datas

    @staticmethod
    def to_userJson(users):
        datas = []
        for user in users:
            usersData = {}
            usersData['id'] = getattr(user, 'id')
            usersData['user_name'] = getattr(user, 'user_name')
            datas.append(usersData)
        return datas

    @staticmethod
    def to_companyJson(companys):
        datas = []
        for company in companys:
            companysData = {}
            companysData['id'] = getattr(company, 'id')
            companysData['company_name'] = getattr(company, 'company_name')
            datas.append(companysData)
        return datas

    @staticmethod
    def to_templateJson(templates):
        json = []
        for template in templates:
            templateData = {}
            templateData['id'] = getattr(template, 'id')
            templateData['template_name'] = getattr(template, 'template_name')
            templateData['module_id'] = getattr(template, 'module_id')
            templateData['user_id'] = getattr(template, 'user_id')
            templateData['template_update_date'] = str(
                getattr(template, 'template_update_date'))[0:19]
            templateData['template_create_date'] = str(
                getattr(template, 'template_create_date'))[0:19]
            json.append(templateData)
        return json

    @staticmethod
    def deleteFile(planId, userId):
        docxFilePath = GetPath.getDocxTemplateResult(planId, userId)
        md_path = GetPath.getMdTemplateResult(planId, userId)
        html_path = GetPath.getHtmlTemplateResult(planId, userId)
        if os.path.exists(docxFilePath):
            os.remove(docxFilePath)
        if os.path.exists(md_path):
            os.remove(md_path)
        if os.path.exists(html_path):
            os.remove(html_path)

    @staticmethod
    def toColumnNameJson(tableName):
        engine = sqlalchemy.create_engine(Config.DEV_DATABASE_URL, encoding="utf-8", echo=True)
        conn = engine.connect()
        sqlStatement = sqlalchemy.sql.text("SELECT a.attname AS name, col_description(a.attrelid, a.attnum) AS comment \
        FROM pg_class AS c, pg_attribute AS a \
        WHERE c.relname = '" + tableName + "' AND a.attrelid = c.oid AND a.attnum > 0")
        results = conn.execute(sqlStatement).fetchall()
        conn.close()
        return json.dumps([{'column_name': i[0], 'column_description': i[1]} for i in results])

    @staticmethod
    def toTableNameJson(moduleName):
        json = []
        engine = sqlalchemy.create_engine(Config.DEV_DATABASE_URL, encoding="utf-8", echo=True)
        conn = engine.connect()
        sqlStatement = None
        if moduleName == Module.coalCHP:
            sqlStatement = sqlalchemy.sql.text(
                "SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename LIKE 'company%' OR tablename LIKE 'coalchp%' ORDER BY (case tablename when 'company' then 1 end)"
            )
        elif moduleName == Module.biomassCHP:
            sqlStatement = sqlalchemy.sql.text(
                "SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename LIKE 'company%' OR tablename LIKE 'biomasschp%' ORDER BY (case tablename when 'company' then 1 end)"
            )
        elif moduleName == Module.CCPP:
            sqlStatement = sqlalchemy.sql.text(
                "SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename LIKE 'plan' OR tablename LIKE 'company%' OR tablename LIKE 'ccpp%' ORDER BY (case tablename when 'company' then 1 end)"
            )
        elif moduleName == Module.gasPowerGeneration:
            sqlStatement = sqlalchemy.sql.text(
                "SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename LIKE 'company%' OR tablename LIKE 'gaspowergeneration%' ORDER BY (case tablename when 'company' then 1 end)"
            )

        if sqlStatement is not None:
            results = conn.execute(sqlStatement).fetchall()

            for index in range(len(results)):
                name = str(results[index])
                if "constant" not in name \
                    and "gaspowergeneration_smoke_resistance" not in name \
                    and "gaspowergeneration_wind_resistance" not in name:
                    name = name.replace("(u'", "")
                    name = name.replace("',)", "")

                    sqlStatement = sqlalchemy.sql.text("SELECT obj_description('public." + name + "'::regclass)")
                    description = str(conn.execute(sqlStatement).fetchone())
                    description = eval(description)

                    data_format = {
                        "table_name": name,
                        "table_description": description
                    }
                    json.append(data_format)

        conn.close()
        return json

    @staticmethod
    def getlogicJson(moduleName):
        json = []
        from app.models import Textlogic
        textlogiclist = Textlogic.search_by_module(moduleName)
        for textlogic in textlogiclist:
            data_format = {"textlogickey": textlogic.textlogickey, "textlogicremarks": textlogic.textlogicremarks}
            json.append(data_format)
        return json

    @staticmethod
    def getComplete():
        completes = []
        companyaNames = Company.search_company()
        userNames = User.select_all()
        plans = Plan.search_plan_all()
        for companyaName in companyaNames:
            completes.append(companyaName.company_name)
        for userName in userNames:
            completes.append(userName.user_name)
        for plan in plans:
            completes.append(plan.plan_name)
        newCompletes = {}.fromkeys(completes).keys()
        return newCompletes

    @staticmethod
    def getPlanComplete():
        companysComplete = []
        usersComplete = []
        templateComplete = []
        companyaNames = Company.search_company()
        userNames = User.select_all()
        templateNames = ReportTemplate.search_template_all()
        for companyaName in companyaNames:
            companysComplete.append(companyaName.company_name)
        for userName in userNames:
            usersComplete.append(userName.user_name)
        for templateName in templateNames:
            templateComplete.append(templateName.template_name)
        return companysComplete, usersComplete, templateComplete

    @staticmethod
    def getLngLats(plans):
        lngLats = []
        for plan in plans:
            lngLat = {}
            lngLat["id"] = plan.id
            lngLat["moduleId"] = plan.module_id
            lngLat["infoWinContent"] = plan.company_lnglat
            lngLat["position"] = [plan.company_lnglat]
            lngLat["listDesc"] = plan.company_location
            lngLat["planState"] = plan.plan_state
            lngLat["planUpdateDate"] = str(plan.plan_update_date)[0:19]
            lngLat["planCreateDate"] = str(plan.plan_create_date)[0:19]
            lngLat["planState"] = plan.plan_state
            company = Company.search_companyById(plan.company_id)
            lngLat["companyName"] = company.company_name
            lngLat["planaName"] = plan.plan_name
            lngLat["keyParams"] = plan.main_equipment_para
            lngLats.append(lngLat)
        return lngLats

    @staticmethod
    def getKeywordResults(keywords):
        if keywords == "":
            plans = Plan.search_plan_all()
            return MainService.getLngLats(plans)
        byCompanyName = Plan.search_planByCompanyName(keywords)
        byUserName = Plan.search_planByUserName(keywords)
        byPlanName = Plan.search_by_planName(keywords)
        planLists = [byCompanyName, byUserName, byPlanName]
        plansResult = []
        idList = []
        for planList in planLists:
            for plan in planList:
                if plan.id in idList:
                    pass
                else:
                    plans = {}
                    plans["id"] = plan.id
                    plans["moduleId"] = plan.module_id
                    plans["infoWinContent"] = plan.company_lnglat
                    plans["position"] = [plan.company_lnglat]
                    plans["listDesc"] = plan.company_location
                    plans["planState"] = plan.plan_state
                    plans["planUpdateDate"] = str(plan.plan_update_date)[0:19]
                    plans["planCreateDate"] = str(plan.plan_create_date)[0:19]
                    plans["planState"] = plan.plan_state
                    company = Company.search_companyById(plan.company_id)
                    plans["companyName"] = company.company_name
                    plans["planaName"] = plan.plan_name
                    plans["keyParams"] = plan.main_equipment_para
                    plansResult.append(plans)
                    idList.append(plan.id)
        return plansResult

    @staticmethod
    def splitStringToList(string, flag):
        stringList = []
        if string is not None and string != "":
            # stringList = string.split(flag)
            stringList = string.splitlines(False)
        return stringList

    @staticmethod
    def del_file(path):
        if os.path.exists(path):
            for i in os.listdir(path):
                path_file = os.path.join(path, i)  # 取文件绝对路径
                if os.path.isfile(path_file):
                    os.remove(path_file)
                else:
                    MainService.del_file(path_file)
            os.removedirs(path)

    @staticmethod
    def getEquipmentTemplate(planId, moduleName):
        equipment = EquipmentList.search_equipmentList(planId)
        equipmentListTemplate = EquipmentListTemplate.search_EquipmentListTemplate(moduleName)
        if equipment is not None and equipmentListTemplate is not None:
            equipment.equipment_content = equipmentListTemplate.equipment_template
            EquipmentList.insert_equipmentList(equipment)

    @staticmethod
    def saveEquipmentList(planId, uidData, nameData, typeData, contentData, unitData, countData, remarkData, moduleName):
        Equipment = None
        try:
            # 根据传入的参数moduleName来判断是设备模板的更新还是方案中设备清单的更新
            if moduleName is None:
                Equipment = EquipmentList.search_equipmentList(planId)
            else:
                Equipment = EquipmentListTemplate.search_EquipmentListTemplate(moduleName)

            uidElementArray = uidData.split('&')
            uidElementList = []
            for formElement in uidElementArray:
                uidElementList.append(formElement.split('='))

            nameElementArray = nameData.split('&')
            nameElementList = []
            for formElement in nameElementArray:
                nameElementList.append(formElement.split('='))

            typeElementArray = typeData.split('&')
            typeElementList = []
            for formElement in typeElementArray:
                typeElementList.append(formElement.split('='))

            contenteElementArray = contentData.split('&')
            contentElementList = []
            for formElement in contenteElementArray:
                contentElementList.append(formElement.split('='))

            unitElementArray = unitData.split('&')
            unitElementList = []
            for formElement in unitElementArray:
                unitElementList.append(formElement.split('='))

            countElementArray = countData.split('&')
            countElementList = []
            for formElement in countElementArray:
                countElementList.append(formElement.split('='))

            remarkElementArray = remarkData.split('&')
            remarkElementList = []
            for formElement in remarkElementArray:
                remarkElementList.append(formElement.split('='))

            decode_equipment_uid_list = []
            decode_equipment_name_list = []
            decode_equipment_type_list = []
            decode_equipment_content_list = []
            decode_equipment_unit_list = []
            decode_equipment_count_list = []
            decode_equipment_remark_list = []

            for index in range(len(uidElementList)):
                equipment_uid_value = uidElementList[index][1]
                decode_equipment_uid_value = urllib.unquote(str(equipment_uid_value)).decode('utf-8')
                decode_equipment_uid_list.append(decode_equipment_uid_value)

            for index in range(len(nameElementList)):
                equipment_name_value = nameElementList[index][1]
                decode_equipment_name_value = urllib.unquote(str(equipment_name_value)).decode('utf-8')
                decode_equipment_name_list.append(decode_equipment_name_value)

            for index in range(len(typeElementList)):
                equipment_type_value = typeElementList[index][1]
                decode_equipment_type_value = urllib.unquote(str(equipment_type_value)).decode('utf-8')
                decode_equipment_type_list.append(decode_equipment_type_value)
            
            for index in range(len(contentElementList)):
                equipment_content_value = contentElementList[index][1]
                decode_equipment_content_value = urllib.unquote(str(equipment_content_value)).decode('utf-8')
                decode_equipment_content_list.append(decode_equipment_content_value)

            for index in range(len(unitElementList)):
                equipment_unit_value = unitElementList[index][1]
                decode_equipment_unit_value = urllib.unquote(str(equipment_unit_value)).decode('utf-8')
                decode_equipment_unit_list.append(decode_equipment_unit_value)

            for index in range(len(countElementList)):
                equipment_count_value = countElementList[index][1]
                decode_equipment_count_value = urllib.unquote(str(equipment_count_value)).decode('utf-8')
                decode_equipment_count_list.append(decode_equipment_count_value)
            
            for index in range(len(remarkElementList)):
                equipment_remark_value = remarkElementList[index][1]
                decode_equipment_remark_value = urllib.unquote(str(equipment_remark_value)).decode('utf-8')
                decode_equipment_remark_list.append(decode_equipment_remark_value)

            equipment_json = None
            if moduleName is None:
                equipment_json = json.loads(Equipment.equipment_content)
            else:
                equipment_json = json.loads(Equipment.equipment_template)

            equipment_json[u'equipment_uid'] = decode_equipment_uid_list
            equipment_json[u'equipment_name'] = decode_equipment_name_list
            equipment_json[u'equipment_type'] = decode_equipment_type_list
            equipment_json[u'equipment_content'] = decode_equipment_content_list
            equipment_json[u'equipment_unit'] = decode_equipment_unit_list
            equipment_json[u'equipment_count'] = decode_equipment_count_list
            equipment_json[u'equipment_remark'] = decode_equipment_remark_list

            if moduleName is None:
                Equipment.equipment_content = json.dumps(equipment_json)
                EquipmentList.insert_equipmentList(Equipment)
            else:
                Equipment.equipment_template = json.dumps(equipment_json)
                EquipmentListTemplate.insert_EquipmentListTemplate(Equipment)
        except Exception as e:
            Equipment = None
            return Equipment
        else:
            return Equipment
