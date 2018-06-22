# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, redirect, url_for, flash,\
    abort, jsonify, request, session, send_from_directory
from flask_login import login_required, current_user
import copy
import os
import json
import urllib
from config import config

'''
from ... import main
from app.main.forms import EditProfileForm, EditProfileAdminForm, \
    ChangePasswordForm, ChangeEmailForm, UpdateUserForm, RegistrationForm
from ... import db

from ..models import User, CoalCHPComponent, CoalCHPConstant,\
    CoalCHPNeedsQuestionnaire, Plan, Company, CoalCHPFurnaceCalculation,\
    BiomassCHPconstant, BiomassCHPBeltWidth,\
    BiomassCHPNeedsQuestionnaire, BiomassCHPBoilerCalculation
from coalService import ToCoalCHP
from biomassService import ToBiomassCHP
'''

from app.decorators import admin_required

from . import gpg_view
from app.models import User, Plan, Company, EquipmentList, EquipmentListTemplate, Module
from ... import db
from util.iapws_if97 import seuif97

from app.gpg.model.gasPowerGeneration_models import GasPowerGenerationConstant, \
    GasPowerGenerationNeedsQuestionnaire, GPGBoilerOfPTS, GPGFlueGasAirSystem, \
    GPGSmokeResistance, GPGWindResistance, GPGCirculatingWaterSystem, \
    GPGSmokeAirCalculate, GPGTurbineAuxiliarySystem, GPGSteamWaterPipe,\
    GPGBoilerAuxiliaries, GPGTurbineOfPTS, GasPowerGenerationEconomicIndicators

from app.gpg.service.gasPowerGeneration_Service import ToGPG
from app.gpg.service.gasPowerGeneration_Service import GPGImgService

from app.gpg.service.execution_strategy import GPG_Boiler_superheated_steam_enthalpy_EXEC, \
    GPG_Boiler_feedwater_enthalpy_EXEC, GPG_Boiler_air_enthalpy_EXEC, \
    GPG_Boiler_saturation_water_temperature_EXEC, \
    GPG_Boiler_saturation_water_enthalpy_EXEC, \
    GPG_TurbineAuxiliary_saturation_temperature_EXEC, \
    GPG_TurbineAuxiliary_condensate_water_enthalpy_EXEC,\
    GPG_SteamWaterPipe_main_steam_meida_specific_volume_c_EXEC,\
    GPG_BoilerAuxiliaries_r_drum_aturatedwater_enthalpy_EXEC,\
    GPG_BoilerAuxiliaries_r_work_aturatedwater_enthalpy_EXEC,\
    GPG_BoilerAuxiliaries_r_work_latentheat_vaporization_EXEC,\
    GPG_BoilerAuxiliaries_c_drum_aturatedwater_enthalpy_EXEC,\
    GPG_BoilerAuxiliaries_c_work_aturatedwater_enthalpy_EXEC,\
    GPG_BoilerAuxiliaries_c_work_steam_pecificvolume_EXEC,\
    GPG_BoilerAuxiliaries_c_work_latentheat_vaporization_EXEC,\
    GPG_BoilerAuxiliaries_s_local_atmosphere_density_EXEC, \
    GPG_BoilerAuxiliaries_new_steam_enthalpy_EXEC, \
    GPG_BoilerAuxiliaries_desuperheater_water_pressure_EXEC, \
    GPG_BoilerAuxiliaries_desuperheater_water_enthalpy_EXEC, \
    GPG_BoilerAuxiliaries_desuperheater_water_flux_EXEC, \
    GPG_BoilerAuxiliaries_desuperheater_steam_enthalpy_EXEC, \
    GPG_BoilerAuxiliaries_saturation_water_enthalpy_EXEC, \
    GPG_BoilerAuxiliaries_de_press_temp_device_flux_EXEC, \
    GPG_BoilerAuxiliaries_charging_saturation_water_enthalpy_EXEC, \
    GPG_BoilerAuxiliaries_exothermic_saturation_water_enthalpy_EXEC, \
    GPG_BoilerAuxiliaries_charging_saturation_steam_enthalpy_EXEC, \
    GPG_BoilerAuxiliaries_exothermic_saturation_steam_enthalpy_EXEC, \
    GPG_BoilerAuxiliaries_p2_steam_amount_EXEC, \
    GPG_BoilerAuxiliaries_charging_water_specific_volume_EXEC, \
    GPG_BoilerAuxiliaries_unit_water_heat_amount_EXEC, \
    GPG_BoilerAuxiliaries_regenerarot_volume_EXEC, \
    GPG_BoilerAuxiliaries_regenerarot_top_steam_volume_EXEC, \
    GPG_BoilerAuxiliaries_regenerarot_max_bleed_EXEC, \
    GPG_BoilerAuxiliaries_evaporation_capacity_EXEC, \
    GPG_BoilerAuxiliaries_charging_volume_EXEC, \
    GPG_BoilerAuxiliaries_exothermic_water_specific_volume_EXEC, \
    GPG_BoilerAuxiliaries_exothermic_water_volume_EXEC, \
    GPG_BoilerAuxiliaries_r_sewage_quantity_EXEC, \
    GPG_BoilerAuxiliaries_r_work_steam_special_volume_EXEC, \
    GPG_BoilerAuxiliaries_r_vaporization_capacity_EXEC, \
    GPG_BoilerAuxiliaries_r_steam_volume_EXEC, \
    GPG_BoilerAuxiliaries_r_volume_EXEC, \
    GPG_TurbineOfPts_EXEC

from app.main.service.mainService import MainService

# ###################### 煤气发电 start ####################
@gpg_view.route('/GPG_SaveQuestionnaire', methods=['POST'])
@login_required
def GPG_SaveQuestionnaire():
    plan_name = request.form.get('plan_name')
    companyName = request.form.get('company_name')
    companyLocation = request.form.get('company_location')
    projectApprovalEia = request.form.get('project_approval_eia')

    # plan_id = session.get('planId')
    # if plan_id is None:
    plan_id = ToGPG.create_plan(companyName, plan_name, companyLocation, None)

    questionnaire = ToGPG.to_questionnaire(request.form, plan_id)

    if projectApprovalEia == "true":
        setattr(questionnaire, 'project_approval_eia', True)
    else:
        setattr(questionnaire, 'project_approval_eia', False)

    GasPowerGenerationNeedsQuestionnaire.insert_questionnaire(questionnaire)
    ToGPG.update_plan_date(plan_id)
    session['planId'] = plan_id
    return jsonify({'planId': plan_id})

@gpg_view.route('/GPG_SaveBoilerOfPTS', methods=['POST'])
@login_required
def GPG_SaveBoilerOfPTS():
    plan_id = session.get('planId')

    try:
        boiler = ToGPG.to_BoilerOfPTS(request.form, plan_id)
        boiler_efficiency = getattr(boiler, 'boiler_efficiency')
        rate_of_blowdown = getattr(boiler, 'rate_of_blowdown')

        if boiler_efficiency != '' and boiler_efficiency is not None:
            setattr(boiler, 'boiler_efficiency', float(boiler_efficiency)/100)
            # print(getattr(boiler, 'boiler_efficiency'))

        if rate_of_blowdown != '' and rate_of_blowdown is not None:
            setattr(boiler, 'rate_of_blowdown', float(rate_of_blowdown)/100)
            # print(getattr(boiler, 'rate_of_blowdown'))

        GPG_Boiler_superheated_steam_enthalpy_EXEC().specialCalculation(boiler, request.form)
        GPG_Boiler_feedwater_enthalpy_EXEC().specialCalculation(boiler, request.form)
        GPG_Boiler_saturation_water_temperature_EXEC().specialCalculation(boiler, request.form)
        GPG_Boiler_saturation_water_enthalpy_EXEC().specialCalculation(boiler, request.form)

        '''以下公式有问题'''
        #GPG_Boiler_air_enthalpy_EXEC().specialCalculation(boiler, request.form)

        ToGPG.update_plan_date(plan_id)
        GPGBoilerOfPTS.insert_BoilerOfPTS(boiler)
        session['planId'] = plan_id
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': None})
    except ZeroDivisionError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "-1"})
    else:
        newData = GPGBoilerOfPTS.search_BoilerOfPTS(plan_id)
        cloneData = copy.deepcopy(newData)

        #更新设备清单
        equipmentList = EquipmentList.search_equipmentList(plan_id)
        equipmentList_json = json.loads(equipmentList.equipment_content)
        equipmentCount = len(equipmentList_json['equipment_name'])

        j = 0
        for j in range(0, equipmentCount):
            if equipmentList_json['equipment_uid'][j] == "uid1":
                string = u"*G-" + ToGPG.convertNumber(newData.steam_output) + "/" + ToGPG.convertNumber(newData.saturation_water_temperature) + u"-Q型"
                equipmentList_json['equipment_content'][j] = string
                break

        equipmentList.equipment_content = json.dumps(equipmentList_json)
        EquipmentList.insert_equipmentList(equipmentList)

        new_boiler_efficiency = getattr(cloneData, 'boiler_efficiency')
        new_rate_of_blowdown = getattr(cloneData, 'rate_of_blowdown')

        if new_boiler_efficiency != '' and new_boiler_efficiency is not None:
            setattr(cloneData, 'boiler_efficiency', float(new_boiler_efficiency)*100)

        if new_rate_of_blowdown != '' and new_rate_of_blowdown is not None:
            setattr(cloneData, 'rate_of_blowdown', float(new_rate_of_blowdown)*100)

        datas = ToGPG.to_BoilerJson(cloneData)
        return jsonify({'newDatas': datas})


@gpg_view.route('/GPG_SaveGasAirData', methods=['POST'])
@login_required
def GPG_SaveGasAirData():
    plan_id = session.get('planId')

    request_blower_specification_power = request.form.get('blower_specification_power')
    request_blower_specification_flux = request.form.get('blower_specification_flux')
    request_induced_specification_power = request.form.get('induced_specification_power')
    request_induced_specification_flux = request.form.get('induced_specification_flux')

    # try:
    GasAirData = ToGPG.to_GasAirData(request.form, plan_id)
    ToGPG.update_plan_date(plan_id)
    GPGFlueGasAirSystem.insert_FlueGasAirSystem(GasAirData)
    session['planId'] = plan_id
    # except ValueError as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': None})
    # except ZeroDivisionError as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': "-1"})
    # except Exception as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': "0"})
    # else:

    GasAirData1 = GPGFlueGasAirSystem.search_FlueGasAirSystem(plan_id)

    if request_blower_specification_power is None or request_blower_specification_power == '':
        if GasAirData1.blower_motor_power is not None:
            GasAirData1.blower_specification_power = str(round(float(str(float(GasAirData1.blower_motor_power)/2).rstrip('0')), 2))

    if request_blower_specification_flux is None or request_blower_specification_flux == '':
        if GasAirData1.blower_fan_selected_flux is not None:
            GasAirData1.blower_specification_flux = str(round(float(str(float(GasAirData1.blower_fan_selected_flux)/2).rstrip('0')), 2))

    if request_induced_specification_power is None or request_induced_specification_power == '':
        if GasAirData1.induced_motor_power is not None:
            GasAirData1.induced_specification_power = str(round(float(str(float(GasAirData1.induced_motor_power)/2).rstrip('0')), 2))

    if request_induced_specification_flux is None or request_induced_specification_flux == '':
        if GasAirData1.induced_fan_selected_flux is not None:
            GasAirData1.induced_specification_flux = str(round(float(str(float(GasAirData1.induced_fan_selected_flux)/2).rstrip('0')), 2))

    newData = GPGFlueGasAirSystem.search_FlueGasAirSystem(plan_id)

    # 更新设备清单
    equipmentList = EquipmentList.search_equipmentList(plan_id)
    equipmentList_json = json.loads(equipmentList.equipment_content)
    equipmentCount = len(equipmentList_json['equipment_name'])

    j = 0
    flag1 = flag2 = flag3 = flag4 = flag5 = 0
    for j in range(0, equipmentCount):
        if flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1 and flag5 == 1:
            break

        if equipmentList_json['equipment_uid'][j] == "uid28":
            if newData.blower_specification_flux is not None:
                string = "p=" + ToGPG.convertNumber(newData.blower_fan_selected_total_pressure) + "Pa; Q=" + str(newData.blower_specification_flux.encode('utf-8')) + "m³/h;"
                equipmentList_json['equipment_content'][j] = string
            flag1 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid29":
            # if newData.blower_motor_power is not None:
                # string = "P=" + str(newData.blower_motor_power.encode('utf-8')) + "kW"
            string = "P=" + ToGPG.convertNumber(newData.blower_motor_power) + "kW"
            equipmentList_json['equipment_content'][j] = string
            flag2 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid30":
            if newData.induced_specification_flux is not None:
                string = "p=" + ToGPG.convertNumber(newData.induced_fan_selected_total_pressure) + "Pa; Q=" + str(newData.induced_specification_flux.encode('utf-8')) + "m³/h;"
                equipmentList_json['equipment_content'][j] = string
            flag3 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid31":
            # if newData.induced_motor_power is not None:
            #     string = "P=" + str(newData.induced_motor_power.encode('utf-8')) + "kW"
            string = "P=" + ToGPG.convertNumber(newData.induced_motor_power) + "kW"
            equipmentList_json['equipment_content'][j] = string
            flag4 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid35":
            string = u"高度H=" + ToGPG.convertNumber(newData.chimney_height) + u"m; 出口直径=" + ToGPG.convertNumber(newData.chimney_outlet_selected_inner_diameter) + "m"
            equipmentList_json['equipment_content'][j] = string
            flag5 = 1

    equipmentList.equipment_content = json.dumps(equipmentList_json)
    EquipmentList.insert_equipmentList(equipmentList)

    datas = ToGPG.to_GasAirJson(newData)
    return jsonify({'newDatas': datas})

@gpg_view.route('/GPG_SaveSmokeResistanceData', methods=['POST'])
@login_required
def GPG_SaveSmokeResistanceData():
    plan_id = session.get('planId')
    SmokeResistanceData = ToGPG.to_SmokeResistanceData(request.form, plan_id)

    GPGSmokeResistance.insert_SmokeResistance(SmokeResistanceData)
    session['planId'] = plan_id
    datas = {}
    datas['flag'] = "success"
    return jsonify({'result': datas})

@gpg_view.route('/GPG_SaveWindResistanceData', methods=['POST'])
@login_required
def GPG_SaveWindResistanceData():
    plan_id = session.get('planId')
    WindResistanceData = ToGPG.to_WindResistanceData(request.form, plan_id)
    GPGWindResistance.insert_WindResistance(WindResistanceData)
    session['planId'] = plan_id
    datas = {}
    datas['flag'] = "success"
    return jsonify({'result': datas})

@gpg_view.route('/GPG_SaveCirculatingWaterData', methods=['POST'])
@login_required
def GPG_SaveCirculatingWaterData():
    plan_id = session.get('planId')
    # try:
    CirculatingWaterData = ToGPG.to_CirculatingWaterData(request.form, plan_id)
    cooling_tower_selected_type = getattr(CirculatingWaterData, 'cooling_tower_selected_type')
    if cooling_tower_selected_type == '1':
        setattr(CirculatingWaterData, 'cooling_tower_selected_name', u'双曲线自然通风冷却塔')
    elif cooling_tower_selected_type == '2':
        setattr(CirculatingWaterData, 'cooling_tower_selected_name', u'逆流式机械通风冷却塔')

    request_selected_pump_model_power = request.form.get('selected_pump_model_power')
    request_selected_pump_model_flow = request.form.get('selected_pump_model_flow')
    request_selected_pump_model_lift = request.form.get('selected_pump_model_lift')

    ToGPG.update_plan_date(plan_id)
    GPGCirculatingWaterSystem.insert_CirculatingWater(CirculatingWaterData)
    session['planId'] = plan_id
    CirculatingWaterData1 = GPGCirculatingWaterSystem.search_CirculatingWater(plan_id)

    if request_selected_pump_model_power is None or request_selected_pump_model_power == '':
        if CirculatingWaterData1.pump_matching_motor_power is not None:
            CirculatingWaterData1.selected_pump_model_power = str(round(float(str(float(CirculatingWaterData1.pump_matching_motor_power)/2).rstrip('0')), 2))

    if request_selected_pump_model_flow is None or request_selected_pump_model_flow == '':
        if CirculatingWaterData1.pump_flow is not None:
            CirculatingWaterData1.selected_pump_model_flow = str(round(float(str(float(CirculatingWaterData1.pump_flow)/2).rstrip('0')), 2))

    if request_selected_pump_model_lift is None or request_selected_pump_model_lift == '':
        if CirculatingWaterData1.total_pumping_lift is not None:
            CirculatingWaterData1.selected_pump_model_lift = str(round(float(str(float(CirculatingWaterData1.total_pumping_lift)).rstrip('0')), 2))

    GPGCirculatingWaterSystem.insert_CirculatingWater(CirculatingWaterData1)
    newData = GPGCirculatingWaterSystem.search_CirculatingWater(plan_id)

    # 更新设备清单
    equipmentList = EquipmentList.search_equipmentList(plan_id)
    equipmentList_json = json.loads(equipmentList.equipment_content)
    equipmentCount = len(equipmentList_json['equipment_name'])

    coolingTowerType = str(round(float(str(float(newData.cooling_tower_selected_type)).rstrip('0')), 0))
    j = 0
    flag1 = flag2 = flag3 = flag4 = 0
    for j in range(0, equipmentCount):
        if flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1:
            break
        if coolingTowerType == '1.0':
            if equipmentList_json['equipment_uid'][j] == "uid98":
                string = u"喷淋面积=" + ToGPG.convertNumber(newData.spray_area) + u"㎡"
                equipmentList_json['equipment_name'][j] = u"自然通风双曲线冷却塔"
                equipmentList_json['equipment_content'][j] = string
                flag1 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid99":
                string = u"250m³"
                equipmentList_json['equipment_name'][j] = u"过滤器"
                equipmentList_json['equipment_content'][j] = string
                flag2 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid100":
                if newData.selected_pump_model_flow is not None \
                    and newData.selected_pump_model_lift is not None:
                    string = "Q=" + str(newData.selected_pump_model_flow.encode('utf-8')) + "m³/h; H=" + str(newData.selected_pump_model_lift.encode('utf-8')) + "m;"
                    equipmentList_json['equipment_content'][j] = string
                flag3 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid101":
                if newData.selected_pump_model_power is not None:
                    string = "P=" + str(newData.selected_pump_model_power.encode('utf-8')) + "kW"
                    equipmentList_json['equipment_content'][j] = string
                flag4 = 1
        elif coolingTowerType == '2.0':
            if equipmentList_json['equipment_uid'][j] == "uid98":
                string = u"冷却流量=" + ToGPG.convertNumber(newData.spray_area) + u"m³/h, 风机功率160kW"
                equipmentList_json['equipment_name'][j] = u"机力通风冷却塔"
                equipmentList_json['equipment_content'][j] = string
                flag1 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid99":
                string = u"300m³/h"
                equipmentList_json['equipment_name'][j] = u"全自动过滤器"
                equipmentList_json['equipment_content'][j] = string
                flag2 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid100":
                if newData.selected_pump_model_flow is not None \
                    and newData.selected_pump_model_lift is not None:
                    string = "Q=" + str(newData.selected_pump_model_flow.encode('utf-8')) + "m³/h; H=" + str(newData.selected_pump_model_lift.encode('utf-8')) + "m H2O;"
                    equipmentList_json['equipment_content'][j] = string
                flag3 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid101":
                if newData.selected_pump_model_power is not None:
                    string = "N=" + str(newData.selected_pump_model_power.encode('utf-8')) + "kW; U=10KV"
                    equipmentList_json['equipment_content'][j] = string
                flag4 = 1
        else:
            break

    equipmentList.equipment_content = json.dumps(equipmentList_json)
    EquipmentList.insert_equipmentList(equipmentList)

    # except ValueError as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': None})
    # except ZeroDivisionError as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': "-1"})
    # except Exception as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': "0"})
    # else:

    datas = ToGPG.to_CirculatingWaterJson(newData)
    return jsonify({'newDatas': datas})


@gpg_view.route('/GPG_SaveSmokeAirCalculateData', methods=['POST'])
@login_required
def GPG_SaveSmokeAirCalculateData():
    plan_id = session.get('planId')
    try:
        SmokeAirCalculateData = ToGPG.to_SmokeAirCalculateData(request.form, plan_id)
        ToGPG.update_plan_date(plan_id)
        GPGSmokeAirCalculate.insert_SmokeAirCalculate(SmokeAirCalculateData)
        session['planId'] = plan_id
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': None})
    except ZeroDivisionError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "-1"})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "0"})
    else:
        newData = GPGSmokeAirCalculate.search_SmokeAirCalculate(plan_id)
        datas = ToGPG.to_SmokeAirCalculateJson(newData)
        return jsonify({'newDatas': datas})

@gpg_view.route('/GPG_SaveTurbineAuxiliaryData', methods=['POST'])
@login_required
def GPG_SaveTurbineAuxiliaryData():
    plan_id = session.get('planId')
    try:
        TurbineAuxiliaryData = ToGPG.to_TurbineAuxiliaryData(request.form, plan_id)

        GPG_TurbineAuxiliary_saturation_temperature_EXEC().specialCalculation(TurbineAuxiliaryData, request.form)
        GPG_TurbineAuxiliary_condensate_water_enthalpy_EXEC().specialCalculation(TurbineAuxiliaryData, request.form)

        ToGPG.update_plan_date(plan_id)
        GPGTurbineAuxiliarySystem.insert_TurbineAuxiliary(TurbineAuxiliaryData)

        #更新设备清单
        equipmentList = EquipmentList.search_equipmentList(plan_id)
        equipmentList_json = json.loads(equipmentList.equipment_content)
        equipmentCount = len(equipmentList_json['equipment_name'])

        j = 0
        flag1 = flag2 = flag3 = flag4 = flag5 = flag6 = 0
        for j in range(0, equipmentCount):
            if flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1 and flag5 == 1 and flag6 == 1:
                break

            if equipmentList_json['equipment_uid'][j] == "uid4":
                string = u"N-" + ToGPG.convertNumber(TurbineAuxiliaryData.cooling_area)
                equipmentList_json['equipment_content'][j] = string
                flag1 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid11":
                string = u"H=" + ToGPG.convertNumber(TurbineAuxiliaryData.condensate_pump_design_lift) + u"m; Q=" + ToGPG.convertNumber(TurbineAuxiliaryData.condensate_pump_flow) + u"m³/h;"
                equipmentList_json['equipment_content'][j] = string
                flag2 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid12":
                string = u"P=" + ToGPG.convertNumber(TurbineAuxiliaryData.condensate_pump_motor_power) + u"kW"
                equipmentList_json['equipment_content'][j] = string
                flag3 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid13":
                string = u"H=" + ToGPG.convertNumber(TurbineAuxiliaryData.jet_pump_total_lift) + u"m; Q=" + ToGPG.convertNumber(TurbineAuxiliaryData.jet_pump_flow) + u"m³/h;"
                equipmentList_json['equipment_content'][j] = string
                flag4 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid14":
                string = u"P=" + ToGPG.convertNumber(TurbineAuxiliaryData.jet_pump_motor_power) + u"kW"
                equipmentList_json['equipment_content'][j] = string
                flag5 = 5
            elif equipmentList_json['equipment_uid'][j] == "uid16":
                if TurbineAuxiliaryData.cooling_jet_pump_flow is not None:
                    string = u"V=" + str(
                        round(float(str(float(TurbineAuxiliaryData.cooling_jet_pump_flow)*2).rstrip('0')), 2)) + u"m³"
                    equipmentList_json['equipment_content'][j] = string
                flag6 = 1

        equipmentList.equipment_content = json.dumps(equipmentList_json)
        EquipmentList.insert_equipmentList(equipmentList)

        session['planId'] = plan_id
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': None})
    except ZeroDivisionError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "-1"})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "0"})
    else:
        newData = GPGTurbineAuxiliarySystem.search_TurbineAuxiliary(plan_id)
        datas = ToGPG.to_TurbineAuxiliaryJson(newData)
        return jsonify({'newDatas': datas})

@gpg_view.route('/GPG_SaveSteamWaterPipeData', methods=['POST'])
@login_required
def GPG_SaveSteamWaterPipeData():
    plan_id = session.get('planId')
    try:
        SteamWaterPipeData = ToGPG.to_SteamWaterPipeData(request.form, plan_id)

        GPG_SteamWaterPipe_main_steam_meida_specific_volume_c_EXEC().specialCalculation(SteamWaterPipeData, request.form)
        ToGPG.update_plan_date(plan_id)
        GPGSteamWaterPipe.insert_SteamWaterPipe(SteamWaterPipeData)
        session['planId'] = plan_id
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': None})
    except ZeroDivisionError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "-1"})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "0"})
    else:
        newData = GPGSteamWaterPipe.search_SteamWaterPipe(plan_id)
        datas = ToGPG.to_SteamWaterPipeJson(newData)
        return jsonify({'newDatas': datas})

@gpg_view.route('/GPG_SaveBoilerAuxiliariesData', methods=['POST'])
@login_required
def GPG_SaveBoilerAuxiliariesData():
    plan_id = session.get('planId')
    # try:
    BoilerAuxiliariesData = ToGPG.to_BoilerAuxiliariesData(request.form, plan_id)

    desalted_water_tech_type = getattr(BoilerAuxiliariesData, 'desalted_water_tech_type')
    if desalted_water_tech_type == '1':
        setattr(BoilerAuxiliariesData, 'desalted_water_tech_name', u'多介质过滤器+超滤装置+两级反渗透装置+EDI处理')
    elif desalted_water_tech_type == '2':
        setattr(BoilerAuxiliariesData, 'desalted_water_tech_name', u'多介质过滤器+反渗透装置+混床处理')

    r_emission_rate = getattr(BoilerAuxiliariesData, 'r_emission_rate')
    c_emission_rate = getattr(BoilerAuxiliariesData, 'c_emission_rate')
    d_na3po4_concentration = getattr(BoilerAuxiliariesData, 'd_na3po4_concentration')

    if r_emission_rate != '' and r_emission_rate is not None:
        setattr(BoilerAuxiliariesData, 'r_emission_rate', float(r_emission_rate)/100)

    if c_emission_rate != '' and c_emission_rate is not None:
        setattr(BoilerAuxiliariesData, 'c_emission_rate', float(c_emission_rate)/100)

    if d_na3po4_concentration != '' and d_na3po4_concentration is not None:
        setattr(BoilerAuxiliariesData, 'd_na3po4_concentration', float(d_na3po4_concentration)/100)

    GPG_BoilerAuxiliaries_r_sewage_quantity_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_r_drum_aturatedwater_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_r_work_aturatedwater_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_r_vaporization_capacity_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_r_work_latentheat_vaporization_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_r_work_steam_special_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_r_steam_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_r_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)

    GPG_BoilerAuxiliaries_c_drum_aturatedwater_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_c_work_aturatedwater_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_c_work_steam_pecificvolume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_c_work_latentheat_vaporization_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_s_local_atmosphere_density_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)

    GPG_BoilerAuxiliaries_new_steam_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_desuperheater_water_pressure_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_desuperheater_water_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_desuperheater_water_flux_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_desuperheater_steam_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_saturation_water_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_de_press_temp_device_flux_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_charging_saturation_water_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_exothermic_saturation_water_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_charging_saturation_steam_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_exothermic_saturation_steam_enthalpy_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_p2_steam_amount_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_charging_water_specific_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_unit_water_heat_amount_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_regenerarot_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_regenerarot_top_steam_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_regenerarot_max_bleed_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_evaporation_capacity_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_charging_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_exothermic_water_specific_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPG_BoilerAuxiliaries_exothermic_water_volume_EXEC().specialCalculation(BoilerAuxiliariesData, request.form)
    GPGBoilerAuxiliaries.insert_boiler_auxiliaries(BoilerAuxiliariesData)
    ToGPG.update_plan_date(plan_id)

    session['planId'] = plan_id
    newData = GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
    cloneData = copy.deepcopy(newData)
    new_r_emission_rate = getattr(cloneData, 'r_emission_rate')
    new_c_emission_rate = getattr(cloneData, 'c_emission_rate')
    new_d_na3po4_concentration = getattr(cloneData, 'd_na3po4_concentration')

    if new_r_emission_rate != '' and new_r_emission_rate is not None:
        setattr(cloneData, 'r_emission_rate', float(new_r_emission_rate)*100)

    if new_c_emission_rate != '' and new_c_emission_rate is not None:
        setattr(cloneData, 'c_emission_rate', float(new_c_emission_rate)*100)

    if new_d_na3po4_concentration != '' and new_d_na3po4_concentration is not None:
        setattr(cloneData, 'd_na3po4_concentration', float(new_d_na3po4_concentration)*100)

    datas = ToGPG.to_BoilerAuxiliariesJson(cloneData)

    #更新设备清单
    equipmentList = EquipmentList.search_equipmentList(plan_id)
    equipmentList_json = json.loads(equipmentList.equipment_content)
    equipmentCount = len(equipmentList_json['equipment_name'])

    j = 0
    flag1 = flag2 = flag3 = flag4 = flag5 = flag6 = flag7 = flag8 = flag9 = flag10 = flag11 = flag12 = flag13 = flag14 = flag15 = flag16 = flag17 = 0
    for j in range(0, equipmentCount):
        if flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1 and flag5 == 1 \
        and flag6 == 1 and flag7 == 1 and flag8 == 1 and flag9 == 1 and flag10 == 1 \
        and flag11 == 1 and flag12 == 1 and flag13 == 1 and flag14 == 1 and flag15 == 1 \
        and flag16 == 1 and flag17 == 1:
            break

        if equipmentList_json['equipment_uid'][j] == "uid17":
            string = u"H=" + ToGPG.convertNumber(newData.p_feedpump_total_head) + u"m; Q=" + ToGPG.convertNumber(newData.p_flow) + u"m³/h;"
            equipmentList_json['equipment_content'][j] = string
            flag1 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid18":
            string = u"P=" + ToGPG.convertNumber(newData.p_auxiliary_motor_power) + u"kW"
            equipmentList_json['equipment_content'][j] = string
            flag2 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid20":
            string = u"D0=" + ToGPG.convertNumber(newData.s_max_feedwater_amount) + u"t/h; V=" + ToGPG.convertNumber(newData.s_volume) + u"m³;"
            equipmentList_json['equipment_content'][j] = string
            flag3 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid21":
            if newData.c_specifications is not None:
                string = str(newData.c_specifications.encode('utf-8'))
                equipmentList_json['equipment_content'][j] = string
            flag4 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid22":
            if newData.r_specifications is not None:
                string = str(newData.r_specifications.encode('utf-8'))
                equipmentList_json['equipment_content'][j] = string
            flag5 = 5
        elif equipmentList_json['equipment_uid'][j] == "uid36":
            string = u"减温水温度=" + ToGPG.convertNumber(newData.desuperheater_water_temperature) + u"℃; 减温水流量=" + ToGPG.convertNumber(newData.desuperheater_water_flux)+ u"t/h; 减温后蒸汽温度=" + ToGPG.convertNumber(newData.desuperheater_steam_temperature)+ u"℃; 减温后蒸汽压力=" + ToGPG.convertNumber(newData.desuperheater_steam_pressure)+ u"Mpa; 减温后蒸汽流量=" + ToGPG.convertNumber(newData.de_press_temp_device_flux)+ u"t/h;"
            equipmentList_json['equipment_content'][j] = string
            flag6 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid102":
            if newData.m_boiler_watersupply_specifications is not None:
                string = "设备出力=" + str(newData.m_boiler_watersupply_specifications.encode('utf-8'))
                equipmentList_json['equipment_content'][j] = string
            flag7 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid107":
            if newData.m_boiler_watersupply_all is not None:
                string = u"产水量 " + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/0.95/0.85/2).rstrip('0')), 2)) + u"m³/h"
                equipmentList_json['equipment_content'][j] = string
            flag8 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid108":
            if newData.m_boiler_watersupply_all is not None:
                string = u"Q=" + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/0.95/0.85/0.75/2).rstrip('0')), 2)) + u"m³/h; H=130-140m; U=380V"
                equipmentList_json['equipment_content'][j] = string
            flag9 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid109":
            if newData.m_boiler_watersupply_all is not None:
                string = u"V=" + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/0.95/0.85*1).rstrip('0')), 2)) + u"m³"
                equipmentList_json['equipment_content'][j] = string
            flag10 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid110":
            if newData.m_boiler_watersupply_all is not None:
                string = u"Q=" + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/0.95/0.85/2).rstrip('0')), 2)) + u"m³/h; U=380V"
                equipmentList_json['equipment_content'][j] = string
            flag11 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid111":
            if newData.m_boiler_watersupply_all is not None:
                string = u"产水量 " + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/0.95/2).rstrip('0')), 2)) + u"m³/h"
                equipmentList_json['equipment_content'][j] = string
            flag12 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid112":
            if newData.m_boiler_watersupply_all is not None:
                string = u"Q=" + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/0.95/0.85/0.75/2).rstrip('0')), 2)) + u"m³/h; H=130-140m; U=380V"
                equipmentList_json['equipment_content'][j] = string
            flag13 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid113":
            if newData.m_boiler_watersupply_all is not None:
                string = u"V=" + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/0.95*1).rstrip('0')), 2)) + u"m³"
                equipmentList_json['equipment_content'][j] = string
            flag14 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid114":
            if newData.m_boiler_watersupply_all is not None:
                string = u"Q=" + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/0.95/2).rstrip('0')), 2)) + u"m³/h"
                equipmentList_json['equipment_content'][j] = string
            flag15 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid115":
            if newData.m_boiler_watersupply_all is not None:
                string = u"产水量 " + str(
                    round(float(str(float(newData.m_boiler_watersupply_all)/2).rstrip('0')), 2)) + u"m³/h"
                equipmentList_json['equipment_content'][j] = string
            flag16 = 1
        elif equipmentList_json['equipment_uid'][j] == "uid116":
            if newData.s_volume is not None:
                string = u"V= " + str(
                    round(float(str(float(newData.s_volume)/2).rstrip('0')), 2)) + u"m³"
                equipmentList_json['equipment_content'][j] = string
            flag17 = 1

    equipmentList.equipment_content = json.dumps(equipmentList_json)
    EquipmentList.insert_equipmentList(equipmentList)


    # except ValueError as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': None})
    # except ZeroDivisionError as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': "-1"})
    # except Exception as e:
    #     print("Error %s" % e)
    #     return jsonify({'newDatas': "0"})
    # else:

    return jsonify({'newDatas': datas})

# 保存汽轮机页面信息
@gpg_view.route('/SaveTurbineOfPtsData', methods=['POST'])
@login_required
def SaveTurbineOfPtsData():
    plan_id = session.get('planId')

    try:
        TurbineOldData = GPGTurbineOfPTS.query.filter_by(plan_id=plan_id).first()

        if getattr(TurbineOldData, 's_parameter_flg') == '1':
            # 已经存在旧记录的场合，先清理旧记录
            TurbineOfPtsData = ToGPG.clearTurbineData(plan_id)
            GPGTurbineOfPTS.insert_TurbineOfPTS(TurbineOfPtsData)

        pointPower0, TurbineOfPtsData = ToGPG.to_TurbineOfPtsData(request.form, plan_id)
        setattr(TurbineOfPtsData, 's_parameter_flg', '1')
        setattr(TurbineOfPtsData, 'i_total_power0', pointPower0)
        # GPG_TurbineOfPts_EXEC().specialCalculation(TurbineOfPtsData, request.form)

        ToGPG.update_plan_date(plan_id)
        GPGTurbineOfPTS.insert_TurbineOfPTS(TurbineOfPtsData)
        # session['planId'] = plan_id
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': None})
    except ZeroDivisionError as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "-1"})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'newDatas': "0"})
    else:
        newData = GPGTurbineOfPTS.search_TurbineOfPTS(plan_id)
        #更新设备清单
        equipmentList = EquipmentList.search_equipmentList(plan_id)
        equipmentList_json = json.loads(equipmentList.equipment_content)
        equipmentCount = len(equipmentList_json['equipment_name'])

        j = 0
        flag1 = flag2 = 0
        for j in range(0, equipmentCount):
            if flag1 == 1 and flag2 == 1:
                break

            if equipmentList_json['equipment_uid'][j] == "uid2":
                if newData.e_steam_extraction_select is not None:
                    string = "BNC-" + str(newData.e_steam_extraction_select.encode('utf-8')) + "-" + ToGPG.convertNumber(newData.e_steam_pressure) + "/" + ToGPG.convertNumber(newData.e_exhaust_point_pressure)
                    equipmentList_json['equipment_content'][j] = string
                flag1 = 1
            elif equipmentList_json['equipment_uid'][j] == "uid3":
                if newData.e_steam_extraction_select is not None:
                    string = "QF2-" + str(newData.e_steam_extraction_select.encode('utf-8')) + "-2"
                    equipmentList_json['equipment_content'][j] = string
                flag2 = 1

        equipmentList.equipment_content = json.dumps(equipmentList_json)
        EquipmentList.insert_equipmentList(equipmentList)

        datas = ToGPG.to_TurbineOfPtsJson(newData)
        return jsonify({'newDatas': datas})


@gpg_view.route('/getBoilerByPlanId', methods=['POST'])
@login_required
def getBoilerByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_BoilerOfPTS = GPGBoilerOfPTS.search_BoilerOfPTS(planId)

    cloneData = copy.deepcopy(gpg_BoilerOfPTS)

    new_boiler_efficiency = getattr(cloneData, 'boiler_efficiency')
    new_rate_of_blowdown = getattr(cloneData, 'rate_of_blowdown')

    if new_boiler_efficiency != '' and new_boiler_efficiency is not None:

        setattr(cloneData, 'boiler_efficiency',
                float(new_boiler_efficiency) * 100)

    if new_rate_of_blowdown != '' and new_rate_of_blowdown is not None:
        setattr(cloneData, 'rate_of_blowdown', float(new_rate_of_blowdown)*100)

    BoilerJson = ToGPG.to_BoilerJson(cloneData)
    return jsonify({'BoilerJson': BoilerJson})

@gpg_view.route('/getGasAirDataByPlanId', methods=['POST'])
@login_required
def getGasAirDataByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_GasAirData = GPGFlueGasAirSystem.search_FlueGasAirSystem(planId)
    GasAirJson = ToGPG.to_GasAirJson(gpg_GasAirData)
    return jsonify({'GasAirJson': GasAirJson})

@gpg_view.route('/getSmokeResistanceByPlanId', methods=['POST'])
@login_required
def getSmokeResistanceByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_SmokeResistanceData = GPGSmokeResistance.search_SmokeResistance(planId)
    SmokeResistanceJson = ToGPG.to_SmokeResistanceJson(gpg_SmokeResistanceData)
    return jsonify({'SmokeResistanceJson': SmokeResistanceJson})

@gpg_view.route('/getWindResistanceByPlanId', methods=['POST'])
@login_required
def getWindResistanceByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_WindResistanceData = GPGWindResistance.search_WindResistance(planId)
    WindResistanceJson = ToGPG.to_WindResistanceJson(gpg_WindResistanceData)
    return jsonify({'WindResistanceJson': WindResistanceJson})

@gpg_view.route('/getCirculatingWaterDataByPlanId', methods=['POST'])
@login_required
def getCirculatingWaterDataByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_CirculatingWaterData = GPGCirculatingWaterSystem.search_CirculatingWater(planId)
    CirculatingWaterJson = ToGPG.to_CirculatingWaterJson(gpg_CirculatingWaterData)
    return jsonify({'CirculatingWaterJson': CirculatingWaterJson})

@gpg_view.route('/getSmokeAirCalculateDataByPlanId', methods=['POST'])
@login_required
def getSmokeAirCalculateDataByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_SmokeAirCalculateData = GPGSmokeAirCalculate.search_SmokeAirCalculate(planId)
    SmokeAirCalculateJson = ToGPG.to_SmokeAirCalculateJson(gpg_SmokeAirCalculateData)
    return jsonify({'SmokeAirCalculateJson': SmokeAirCalculateJson})

@gpg_view.route('/getTurbineAuxiliaryByPlanId', methods=['POST'])
@login_required
def getTurbineAuxiliaryByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_TurbineAuxiliaryData = GPGTurbineAuxiliarySystem.search_TurbineAuxiliary(planId)
    TurbineAuxiliaryJson = ToGPG.to_TurbineAuxiliaryJson(gpg_TurbineAuxiliaryData)
    return jsonify({'TurbineAuxiliaryJson': TurbineAuxiliaryJson})

@gpg_view.route('/getSteamWaterPipeDataByPlanId', methods=['POST'])
@login_required
def getSteamWaterPipeDataByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_SteamWaterPipeData = GPGSteamWaterPipe.search_SteamWaterPipe(planId)
    SteamWaterPipeJson = ToGPG.to_SteamWaterPipeJson(gpg_SteamWaterPipeData)
    return jsonify({'SteamWaterPipeJson': SteamWaterPipeJson})

@gpg_view.route('/getBoilerAuxiliariesDataByPlanId', methods=['POST'])
@login_required
def getBoilerAuxiliariesDataByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_BoilerAuxiliariesData = GPGBoilerAuxiliaries.search_boiler_auxiliaries(planId)
    cloneData = copy.deepcopy(gpg_BoilerAuxiliariesData)

    new_r_emission_rate = getattr(cloneData, 'r_emission_rate')
    new_c_emission_rate = getattr(cloneData, 'c_emission_rate')
    new_d_na3po4_concentration = getattr(cloneData, 'd_na3po4_concentration')

    if new_r_emission_rate != '' and new_r_emission_rate is not None:
        setattr(cloneData, 'r_emission_rate',
                float(new_r_emission_rate) * 100)

    if new_c_emission_rate != '' and new_c_emission_rate is not None:
        setattr(cloneData, 'c_emission_rate',
                float(new_c_emission_rate) * 100)

    if new_d_na3po4_concentration != '' and new_d_na3po4_concentration is not None:
        setattr(cloneData, 'd_na3po4_concentration',
                float(new_d_na3po4_concentration)*100)

    BoilerAuxiliariesJson = ToGPG.to_BoilerAuxiliariesJson(cloneData)
    return jsonify({'BoilerAuxiliariesJson': BoilerAuxiliariesJson})

# 初期化汽轮机计算
@gpg_view.route('/getTurbineOfPtsByPlanId', methods=['POST'])
@login_required
def getTurbineOfPtsByPlanId():
    planId = session.get('planId')
    print("**************************************")
    print(planId)
    gpg_TurbineOfPtsData = GPGTurbineOfPTS.search_TurbineOfPTS(planId)
    TurbineOfPtsJson = ToGPG.to_TurbineOfPtsJson(gpg_TurbineOfPtsData)
    return jsonify({'TurbineOfPtsJson': TurbineOfPtsJson})

@gpg_view.route('/selectPlan', methods=['POST'])
@login_required
def selectPlan():
    planId = request.values.get('planId')
    questionnaireData = GasPowerGenerationNeedsQuestionnaire.search_questionnaire(
        planId)
    questionnaireJson = ToGPG.to_questionnaireJson(questionnaireData)
    session['planId'] = planId
    return jsonify({'questionnaireJson': questionnaireJson})

@gpg_view.route('/initGPGQuestionnaire', methods=['POST'])
@login_required
def initGPGQuestionnaire():
    questionnaireJson = "null"
    if session.get('planId'):
        questionnaire = GasPowerGenerationNeedsQuestionnaire.search_questionnaire(
            session.get('planId'))
        questionnaireJson = ToGPG.to_questionnaireJson(questionnaire)
        # print(questionnaireJson)
    return jsonify({'questionnaireJson': questionnaireJson})

@gpg_view.route('/GPG_Questionnaire')
@login_required
def GPG_Questionnaire():
    # session['moduleName'] = "gasPowerGeneration"
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_questionnaire")
    plans = Plan.search_plan(current_user.id)
    companys = Company.search_company()
    return render_template(
        'page/GasPowerGeneration/GPG_Questionnaire.html',
        menuSelect='GPG_Questionnaire',
        constants=GPGConstant,
        plans=plans,
        companys=companys)

@gpg_view.route('/GPG_BoilerOfPTS')
@login_required
def GPG_BoilerOfPTS():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_BoilerOfPTS")

    gpg_BoilerOfPTS = GPGBoilerOfPTS.search_BoilerOfPTS(session.get('planId'))

    return render_template(
        'page/GasPowerGeneration/GPG_Boiler_of_PTS.html',
        menuSelect='GPG_BoilerOfPTS',
        constants=GPGConstant,
        gpg_BoilerOfPTS=gpg_BoilerOfPTS)

@gpg_view.route('/GPG_TurbineOfPTS')
@login_required
def GPG_TurbineOfPTS():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_TurbineOfPTS")

    gpg_TurbineOfPTS = GPGTurbineOfPTS.search_TurbineOfPTS(session.get('planId'))

    # 抽汽部分压力加入回热系统中时，按照压力排序
    sortPressureAfter = ToGPG.sortPressure(gpg_TurbineOfPTS)

    return render_template(
        'page/GasPowerGeneration/GPG_Turbine_of_PTS.html',
        menuSelect='GPG_TurbineOfPTS',
        constants=GPGConstant,
        gpg_TurbineOfPTS=gpg_TurbineOfPTS)

@gpg_view.route('/GPG_SmokeAirCalculate')
@login_required
def GPG_SmokeAirCalculate():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_SmokeAirCalculate")
    return render_template(
        'page/GasPowerGeneration/GPG_SmokeAirCalculate.html',
        menuSelect='GPG_SmokeAirCalculate',
        constants=GPGConstant)

@gpg_view.route('/GPG_GasAirSystem')
@login_required
def GPG_GasAirSystem():
    print("*******************")
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_GasAirSystem")
    print("********GPG_GasAirSystem***********")
    #gpg_FlueGasAirSystem = GPGFlueGasAirSystem.search_FlueGasAirSystem(session.get('planId'))

    return render_template(
        'page/GasPowerGeneration/GPG_GasAirSystem.html',
        menuSelect='GPG_GasAirSystem',
        constants=GPGConstant)


@gpg_view.route('/GPG_SmokeResistance')
@login_required
def GPG_SmokeResistance():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_SmokeResistance")
    return render_template(
        'page/GasPowerGeneration/GPG_SmokeResistance.html',
        menuSelect='GPG_SmokeResistance',
        constants=GPGConstant)


@gpg_view.route('/GPG_WindResistance')
@login_required
def GPG_WindResistance():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_WindResistance")
    return render_template(
        'page/GasPowerGeneration/GPG_WindResistance.html',
        menuSelect='GPG_WindResistance',
        constants=GPGConstant)

@gpg_view.route('/GPG_CirculatingWaterSystem')
@login_required
def GPG_CirculatingWaterSystem():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_CirculatingWaterSystem")

    return render_template(
        'page/GasPowerGeneration/GPG_CirculatingWaterSystem.html',
        menuSelect='GPG_CirculatingWaterSystem',
        constants=GPGConstant)

@gpg_view.route('/GPG_TurbineAuxiliarySystem')
@login_required
def GPG_TurbineAuxiliarySystem():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_TurbineAuxiliarySystem")

    return render_template(
        'page/GasPowerGeneration/GPG_TurbineAuxiliarySystem.html',
        menuSelect='GPG_TurbineAuxiliarySystem',
        constants=GPGConstant)

@gpg_view.route('/GPG_SteamWaterPipe')
@login_required
def GPG_SteamWaterPipe():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_SteamWaterPipe")

    return render_template(
        'page/GasPowerGeneration/GPG_SteamWaterPipe.html',
        menuSelect='GPG_SteamWaterPipe',
        constants=GPGConstant)

@gpg_view.route('/GPG_BoilerAuxiliaries')
@login_required
def GPG_BoilerAuxiliaries():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "GPG_BoilerAuxiliaries")

    return render_template(
        'page/GasPowerGeneration/GPG_BoilerAuxiliaries.html',
        menuSelect='GPG_BoilerAuxiliaries',
        constants=GPGConstant)




# 根据压力查询温度
@gpg_view.route('/TurbineofPtsByPressure', methods=['POST'])
@login_required
def TurbineofPtsByPressure():
    datas = {}
    try:
        pressure_data = request.form.get('e_exhaust_point_pressure')
        temperature_data = seuif97.tsat_p((float(pressure_data)*10))
        datas['temperature'] = temperature_data
        return jsonify({'temperature': datas})
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'temperature': None})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'temperature': "-1"})
    else:
        return jsonify({'temperature': datas})


# 根据压力和熵查询温度
@gpg_view.route('/byPressureEntropy', methods=['POST'])
@login_required
def byPressureEntropy():
    datas = {}
    try:
        pressure_data = request.form.get('e_exhaust_point_pressure')
        entropy_data = request.form.get('e_exhaust_point_entropy')
        temperature_data = seuif97.ps2t((float(pressure_data)),float(entropy_data))
        datas['temperature'] = temperature_data
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'temperature': None})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'temperature': "-1"})
    else:
        return jsonify({'temperature': datas})

# 根据温度查询压力
@gpg_view.route('/byTemperatureBack', methods=['POST'])
@login_required
def byTemperatureBack():
    datas = {}
    try:
        temperature_data = request.form.get('e_backpressure_temperature')
        pressure_data = seuif97.psat_t((float(temperature_data)))*0.1
        datas['pressure'] = pressure_data
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'pressure': None})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'pressure': "-1"})
    else:
        return jsonify({'pressure': datas})

# 根据压力查询温度
@gpg_view.route('/byPressureBack', methods=['POST'])
@login_required
def byPressureBack():
    datas = {}
    try:
        pressure_data = request.form.get('e_backpressure_pressure')
        temperature_data = seuif97.tsat_p((float(pressure_data)*10))
        datas['temperature'] = temperature_data
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'temperature': None})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'temperature': "-1"})
    else:
        return jsonify({'temperature': datas})

# 根据压力和熵查询焓
@gpg_view.route('/byPressureEntropyBack', methods=['POST'])
@login_required
def byPressureEntropyBack():
    datas = {}
    try:
        pressure_data = request.form.get('e_backpressure_pressure')
        entropy_data = request.form.get('e_exhaust_after_entropy')
        enthalpy_data = seuif97.ps2h((float(pressure_data)),float(entropy_data))
        datas['enthalpy'] = enthalpy_data
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'enthalpy': None})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'enthalpy': "-1"})
    else:
        return jsonify({'enthalpy': datas})

# 根据温度和熵查询焓
@gpg_view.route('/byTemperatureEntropyBack', methods=['POST'])
@login_required
def byTemperatureEntropyBack():
    datas = {}
    try:
        temperature_data = request.form.get('e_backpressure_temperature')
        entropy_data = request.form.get('e_exhaust_after_entropy')
        enthalpy_data = seuif97.ts2h((float(temperature_data)),float(entropy_data))
        datas['enthalpy'] = enthalpy_data
    except ValueError as e:
        print("Error %s" % e)
        return jsonify({'enthalpy': None})
    except Exception as e:
        print("Error %s" % e)
        return jsonify({'enthalpy': "-1"})
    else:
        return jsonify({'enthalpy': datas})

# ###################### 煤气发电 end ####################

# ###################### 生成方案图纸 start ####################
# @gpg_view.route('/GPG_CreateDrawings')
# @login_required
# def CreateDrawings():
#     planId = request.form.get('planId')
#     gpg_GasAirSystemData = GPGFlueGasAirSystem.search_FlueGasAirSystem(planId)

#     return render_template(
#         'page/GasPowerGeneration/GPG_EconomicIndicators.html',
#         menuSelect='GPG_EconomicIndicators',
#         constants=GPGConstant)

# ###################### 生成方案图纸 end ####################

# **************主要技术经济指标处理 start*******************
@gpg_view.route('/GPG_EconomicIndicators')
@login_required
def GPG_EconomicIndicators():
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "economic_indicators")
    return render_template(
        'page/GasPowerGeneration/GPG_EconomicIndicators.html',
        menuSelect='GPG_EconomicIndicators',
        constants=GPGConstant)


@gpg_view.route('/GPG_ChooseTemplate/<int:planId>')
@login_required
def GPG_ChooseTemplate(planId):
    session['planId'] = planId
    GPGConstant = GasPowerGenerationConstant.search_gasPowerGenerationConstant(
        "economic_indicators")
    return render_template(
        'page/GasPowerGeneration/GPG_EconomicIndicators.html',
        menuSelect='GPG_EconomicIndicators',
        constants=GPGConstant)


# 主要技术经济指标初期化处理
@gpg_view.route('/GPG_InitEconomic', methods=['POST'])
@login_required
def GPG_InitEconomic():
    planId = request.values.get('planId')
    economic = GasPowerGenerationEconomicIndicators.search_economic_indicators(planId)
    economicData = ToGPG.to_economicJson(economic)
    return jsonify({'economic': economicData})

#保存主要技术经济指标页面信息
@gpg_view.route('/GPG_FormDataEconomic', methods=['POST'])
@login_required
def GPG_FormDataEconomic():
    economicData = ToGPG.to_economic(request.form,
                                     session.get('planId'))
    GasPowerGenerationEconomicIndicators.insert_economic_indicators(economicData)

    datas = {}
    datas['flag'] = "success"

    return jsonify({'coalSort': datas})

# **************主要技术经济指标处理 end**************


# ************** 文件预览 **************
@gpg_view.route('/gpgimgpreview/<planid>/<filename>', methods=['GET'])
def gpgimgpreview(planid, filename):
    return send_from_directory(
        os.path.join(os.getcwd(), config['imgConfig'].GPG_IMG_PATH_RESULT + "/" + str(planid), ""), filename)

@gpg_view.route('/GPG_Image')
@login_required
def GPG_Image():
    # 生成图纸
    planId = session.get('planId')
    # user_id = current_user.id
    GPGImgService().imgCreate(planId)

    # 获取地址列表
    imglist = GPGImgService().getImgList(planId)
    return render_template(
        'page/GasPowerGeneration/GPG_img.html',
        imglist=imglist,
        imglength=len(imglist))

# **************文件预览 end*******************

# ************** 设备清单模板 ********************
@gpg_view.route('/GPG_EquipmentTemplate')
@login_required
def GPG_EquipmentTemplate():
    return render_template(
        'page/GasPowerGeneration/GPG_EquipmentTemplate.html'
    )

@gpg_view.route('/getGPGEquipmentTemplate', methods=['POST'])
@login_required
def getGPGEquipmentTemplate():
    equipmentTemplate = EquipmentListTemplate.search_EquipmentListTemplate(Module.gasPowerGeneration)
    equipmentTemplate_json = json.loads(equipmentTemplate.equipment_template)  
    equipment_json = json.dumps(equipmentTemplate_json)
    return equipment_json

@gpg_view.route('/saveGPGEquipmentTemplate', methods=['POST'])
@login_required
def saveGPGEquipmentTemplate():
    uidData = request.values.get('uidData')
    nameData = request.values.get('nameData')
    typeData = request.values.get('typeData')
    contentData = request.values.get('contentData')
    unitData = request.values.get('unitData')
    countData = request.values.get('countData')
    remarkData = request.values.get('remarkData')

    Equipment = MainService.saveEquipmentList(None, uidData, nameData, typeData, contentData, unitData, countData, remarkData, Module.gasPowerGeneration)

    if Equipment is not None:
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'error'})

# ************** 设备清单 ********************

@gpg_view.route('/GPG_EquipmentList')
@login_required
def GPG_EquipmentList():
    return render_template(
        'page/GasPowerGeneration/GPG_EquipmentList.html'
    )

@gpg_view.route('/getGPGEquipmentList', methods=['POST'])
@login_required
def getGPGEquipmentList():
    planId = session.get('planId')
    equipmentList = EquipmentList.search_equipmentList(planId)
    equipmentList_json = json.loads(equipmentList.equipment_content)
    equipment_json = json.dumps(equipmentList_json)
    return equipment_json

@gpg_view.route('/saveGPGEquipmentList', methods=['POST'])
@login_required
def saveGPGEquipmentList():
    planId = session.get('planId')
    # deleteId = request.values.get('deleteId')
    uidData = request.values.get('uidData')
    nameData = request.values.get('nameData')
    typeData = request.values.get('typeData')
    contentData = request.values.get('contentData')
    unitData = request.values.get('unitData')
    countData = request.values.get('countData')
    remarkData = request.values.get('remarkData')
    # Equipment = EquipmentList.search_equipmentList(planId)

    Equipment = MainService.saveEquipmentList(planId, uidData, nameData, typeData, contentData, unitData, countData, remarkData, None)

    if Equipment is not None:
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'error'})

# ************** 文件预览 ********************


'''
@main.route('/subPages3')
@login_required
def subPages3():
    return render_template('page/elements.3.html', menuSelect='elements3')


@main.route('/elements')
@login_required
def elements():
    return render_template('page/elements.html', menuSelect='elements')


@main.route('/charts')
@login_required
def charts():
    return render_template('page/charts.html', menuSelect='charts')


@main.route('/tables')
@login_required
def tables():
    return render_template('page/tables.html', menuSelect='tables')


@main.route('/typography')
@login_required
def typography():
    return render_template('page/typography.html', menuSelect='typography')


@main.route('/icons')
@login_required
def icons():
    return render_template('page/icons.html', menuSelect='icons')
'''
