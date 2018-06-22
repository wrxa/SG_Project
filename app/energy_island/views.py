# -*- coding: utf-8 -*-
import json
from datetime import datetime
from flask import render_template, redirect, url_for, flash,\
    abort, request, jsonify, session
from flask_login import login_required, current_user
from . import energy_island
from .. import db
from ..models import User
from ..decorators import admin_required
from energyisland_service import EnergyIslandService
from app.algo import algorithm
from app.energy_island.models import Device
from decimal import Decimal


'''
  进入需求调研表页面
'''


@energy_island.route('/energyisland_questionnaire')
@login_required
def energyisland_questionnaire():
    eir_work_list = EnergyIslandService().get_list_eir_work()
    eir_cost_list = EnergyIslandService().get_list_eir_cost()
    eir_available_list = EnergyIslandService().get_list_eir_available()
    eir_available_list_2 = EnergyIslandService().get_list_eir_available_2()
    eir_heat_list = EnergyIslandService().get_list_eir_heat()
    eir_cool_list = EnergyIslandService().get_list_eir_cool()
    eir_steam_list = EnergyIslandService().get_list_eir_steam()
    eir_electric_list = EnergyIslandService().get_list_eir_electric()
    eir_hot_water_list = EnergyIslandService().get_list_eir_hot_water()
    eir_air_supply_list = EnergyIslandService().get_list_eir_air_supply()
    eir_season_typical_day = EnergyIslandService().get_list_eir_season_typical_day()
    time_list = EnergyIslandService().get_list_time()
    month_list = EnergyIslandService().get_list_month()
    session['menuSelect'] = "energyIslandplanList"
    return render_template(
        'page/energyisland/energyisland_questionnaire.html',
        eir_work_list=eir_work_list,
        eir_cost_list=eir_cost_list,
        eir_available_list=eir_available_list,
        eir_available_list_2=eir_available_list_2,
        eir_heat_list=eir_heat_list,
        eir_cool_list=eir_cool_list,
        eir_steam_list=eir_steam_list,
        eir_electric_list=eir_electric_list,
        eir_hot_water_list=eir_hot_water_list,
        eir_air_supply_list=eir_air_supply_list,
        eir_season_typical_day=eir_season_typical_day,
        time_list=time_list,
        month_list=month_list
    )

# 进入ccpp经济性分析表页面
@energy_island.route('/toChooseTemplate/<int:planId>')
@login_required
def toChooseTemplate(planId):
    '''
    需求调研表页面
    '''
    session['planId'] = planId
    eir_work_list = EnergyIslandService().get_list_eir_work()
    eir_cost_list = EnergyIslandService().get_list_eir_cost()
    eir_available_list = EnergyIslandService().get_list_eir_available()
    eir_available_list_2 = EnergyIslandService().get_list_eir_available_2()
    eir_heat_list = EnergyIslandService().get_list_eir_heat()
    eir_cool_list = EnergyIslandService().get_list_eir_cool()
    eir_steam_list = EnergyIslandService().get_list_eir_steam()
    eir_electric_list = EnergyIslandService().get_list_eir_electric()
    eir_hot_water_list = EnergyIslandService().get_list_eir_hot_water()
    eir_air_supply_list = EnergyIslandService().get_list_eir_air_supply()
    eir_season_typical_day = EnergyIslandService().get_list_eir_season_typical_day()
    time_list = EnergyIslandService().get_list_time()
    month_list = EnergyIslandService().get_list_month()
    session['menuSelect'] = "energyIslandplanList"
    return render_template(
        'page/energyisland/energyisland_questionnaire.html',
        eir_work_list=eir_work_list,
        eir_cost_list=eir_cost_list,
        eir_available_list=eir_available_list,
        eir_available_list_2=eir_available_list_2,
        eir_heat_list=eir_heat_list,
        eir_cool_list=eir_cool_list,
        eir_steam_list=eir_steam_list,
        eir_electric_list=eir_electric_list,
        eir_hot_water_list=eir_hot_water_list,
        eir_air_supply_list=eir_air_supply_list,
        eir_season_typical_day=eir_season_typical_day,
        time_list=time_list,
        month_list=month_list
    )


@energy_island.route('/energyIsland/initQuestionnaire', methods=['POST'])
@login_required
def initQuestionnaire():
    '''
    页面select选择公司后加载此程序，传入选择的方案ID
    '''
    planId = session.get('planId')
    # 获得页面的json格式数据
    questionnaireData = None
    if planId is not None:
        questionnaireData = EnergyIslandService().get_questionnaire_data_json(planId)
    return jsonify({'planId': planId, 'questionnaire': questionnaireData})


@energy_island.route('/energyisland_addDevice')
@login_required
def energyisland_addDevice():
    session['menuSelect'] = "energyisland_addDevice"
    return render_template(
        'page/energyisland/addDevice.html'
    )


@energy_island.route('/energyisland_specification')
@login_required
def energyisland_specification():
    session['menuSelect'] = "energyisland_specification"
    return render_template(
        'page/energyisland/specification.html'
    )


@energy_island.route('/getDeviceList', methods=['POST'])
@login_required
def getDeviceList():
    device_class = request.values.get('deviceClass')
    device_type = request.values.get('deviceType')
    result_list = EnergyIslandService().getDeviceList(device_class, device_type)
    return jsonify({'props_json_list': result_list[1], 'id_list': result_list[0]})


@energy_island.route('/getDeviceByID', methods=['POST'])
@login_required
def getDeviceByID():
    device_id = request.values.get('deviceId')
    device = Device.search_deviceById(device_id)
    device.props_json
    device.device_class
    device.device_type
    # return device.props_json
    return jsonify({'props_json': device.props_json, 'device_class': device.device_class, 'device_type': device.device_type})


@energy_island.route('/editDevice', methods=['POST'])
@login_required
def editDevice():
    device_id = request.values.get('deviceId')
    formData = request.values.get('formData')
    oldDevice = Device.search_deviceById(device_id)
    newDevice = EnergyIslandService().updateDevice(oldDevice, formData)
    if newDevice is not None:
        Device.insert_device(newDevice)
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'fail'})


@energy_island.route('/deleteDevice', methods=['POST'])
@login_required
def deleteDevice():
    device_id = request.values.get('deviceId')
    device = Device.search_deviceById(device_id)
    device_class = device.device_class
    device_type = device.device_type
    Device.delete_device(device_id)
    result_list = EnergyIslandService().getDeviceList(device_class, device_type)
    return jsonify({'props_json_list': result_list[1], 'id_list': result_list[0]})


@energy_island.route('/addDevice', methods=['POST'])
@login_required
def addDevice():
    formData = request.values.get('formData')
    device = EnergyIslandService().getDevice(formData)
    if device is not None:
        Device.insert_device(device)
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'fail'})


@energy_island.route('/getPropertyByDeviceType', methods=['POST'])
@login_required
def getDataByDeviceType():
    device_class = request.values.get('deviceClass')
    device_type = request.values.get('deviceType')
    props_json = EnergyIslandService().getDeviceProperty(device_class, device_type)
    return props_json


# 保存调研表数据
@energy_island.route('/formDataEnergyIslandQuestionnaire', methods=['POST'])
@login_required
def energyisland_form_data():
    planId = session.get('planId')
    EnergyIslandService().save_questionnaire(planId, request.form)
    return jsonify({'state': 0})


def formtodirrelist(formestr):
    formestrlist = formestr.split("&")
    resultlist = []
    for yr in formestrlist:
        yrlist = yr.split("=")
        resultlist.append({'conumname':yrlist[0], 'conumval':yrlist[1]})
    return resultlist


def strtolist(result):
    if result is not None and result != '':
        result = result.split("#")
        del result[0]
    return result


@energy_island.route('/energyIsland/get_device_select', methods=['POST'])
@login_required
def get_device_select():
    planId = session.get('planId')
    requirement = EnergyIslandService().model_transform(planId)
    algorithm.out_resource_init()
    device_select_list1, device_select_list2 = EnergyIslandService().createdatatype(request)
    # 更新全局字典
    # algorithm.used_devices = []
    algorithm.out_resource = {'electric': 0, 'steam': 0, 'cool': 0, 'heat': 0, 'hot_water': 0, 'air': 0}
    algorithm.set_out_source_used(device_select_list1, requirement)
    algorithm.used_devices = device_select_list2
    algorithm.set_waste_device_used(device_select_list2, requirement)
    session['out_resource_detail'] = algorithm.out_resource_detail
    session['used_devices'] = algorithm.used_devices
    return jsonify({'state': 0})


@energy_island.route('/energyIsland/device_select')
@login_required
def energyisland_device_select():
    session['menuSelect'] = "energyIslandplanList"
    planId = session.get('planId')
    # 获取需求调研表的数据
    requirement = EnergyIslandService().model_transform(planId)
    out_resource_detail_list = EnergyIslandService().get_select_device_data(requirement)
    # 锅炉数据
    boilerlist11, boilerlist13, boilerlist14, boilerlist15 = EnergyIslandService().getselectdeviceboilerdata()
    return render_template(
        'page/energyisland/device_select.html',
        out_resource_detail_list=out_resource_detail_list,
        boilerlist11=boilerlist11,
        boilerlist13=boilerlist13,
        boilerlist14=boilerlist14,
        boilerlist15=boilerlist15)


@energy_island.route('/energyIsland/get_checked_box', methods=['POST'])
@login_required
def energyisland_get_checked_box():
    session['menuSelect'] = "energyIslandplanList"
    if 'out_resource_detail' in session:
        out_resource_detail = session['out_resource_detail']
    else:
        out_resource_detail = None
    if 'used_devices' in session:
        used_devices = session['used_devices']
    else:
        used_devices = None
    checked_device = EnergyIslandService().get_checked_device(out_resource_detail, used_devices)
    return jsonify(checked_device)


@energy_island.route('/energyIsland/get_useful_device_list', methods=['POST'])
@login_required
def energyisland_get_useful_device_list():
    session['menuSelect'] = "energyIslandplanList"
    planId = session.get('planId')
    requirement = EnergyIslandService().model_transform(planId)
    algorithm.reset_data()
    front_data = algorithm.run_search_get_device(requirement, algorithm.TestData.disabled_devices)
    for typical_day_data in front_data.values():
        for plan_data in typical_day_data:
            if isinstance(plan_data['electric']['load'], Decimal):
                plan_data['electric']['load'] = float(plan_data['electric']['load'])
                plan_data['electric']['props'] = json.loads(plan_data['electric']['props'])
            if 'waste' in plan_data.keys():
                for waste in plan_data['waste'][0].values():
                    if waste and not isinstance(waste, str) and ('load' in waste.keys()):
                        if waste['props']:
                            waste['props'] = json.loads(waste['props'])
                        if isinstance(waste['load'], Decimal):
                            waste['load'] = float(waste['load'])
    return jsonify(front_data)


@energy_island.route('/energyisland_graph')
@login_required
def energyisland_graph():
    session['menuSelect'] = "energyisland_graph"
    list_column_eir_running_param = EnergyIslandService().get_list_eir_running_param()
    list_column_eir_running_cost = EnergyIslandService().get_list_eir_running_cost()
    list_column_eir_running_income = EnergyIslandService().get_list_eir_running_income()
    planId = session.get('planId')
    return render_template(
        'page/energyisland/graph.html',
        plan_id=planId,
        list_column_eir_running_param=list_column_eir_running_param,
        list_column_eir_running_cost=list_column_eir_running_cost,
        list_column_eir_running_income=list_column_eir_running_income
    )


@energy_island.route('/energyIsland/get_graph_data_need', methods=['POST'])
@login_required
def get_graph_data_need():
    planId = session.get('planId')
    front_data_dict = EnergyIslandService().get_need_curve(planId)
    return jsonify(front_data_dict)


@energy_island.route('/energyIsland/get_graph_data', methods=['POST'])
@login_required
def get_graph_data():
    id = request.values.get('id')
    print(id)
    planId = session.get('planId')
    requirement = EnergyIslandService().model_transform(planId)
    algorithm.reset_data()
    # front_data = None
    front_data = algorithm.run_search(requirement, algorithm.TestData.disabled_devices)
    # front_data = algorithm.run_search(algorithm.TestData.requirement, algorithm.TestData.disabled_devices)
    return jsonify(front_data)


@energy_island.route('/energyIsland/save_mark_data', methods=['POST'])
@login_required
def save_mark_data():
    planId = session.get('planId')
    EnergyIslandService().save_mark_data(planId, request)
    # requirement = EnergyIslandService().model_transform(planId)
    # algorithm.reset_data()
    # front_data = algorithm.run_search(requirement, algorithm.TestData.disabled_devices)
    return jsonify({'state': 0})


# @energy_island.route('/energyIsland/get_device_list', methods=['POST'])
# @login_required
# def energyisland_get_device_list():
#     session['menuSelect'] = "energyIslandplanList"
#     planId = session.get('planId')
#     requirement = EnergyIslandService().model_transform(planId)
#     algorithm.reset_data()
#     front_data = algorithm.run_search_get_device(requirement, algorithm.TestData.disabled_devices)
#     for typical_day_data in front_data.values():
#         for plan_data in typical_day_data:
#             if isinstance(plan_data['electric']['load'], Decimal):
#                 plan_data['electric']['load'] = float(plan_data['electric']['load'])
#                 plan_data['electric']['props'] = json.loads(plan_data['electric']['props'])
#             if 'waste' in plan_data.keys():
#                 for waste in plan_data['waste'][0].values():
#                     if waste and not isinstance(waste, str) and ('load' in waste.keys()):
#                         if waste['props']:
#                             waste['props'] = json.loads(waste['props'])
#                         if isinstance(waste['load'], Decimal):
#                             waste['load'] = float(waste['load'])
#                     # if waste and not isinstance(waste, str) and ('load' in waste.keys()) and isinstance(waste['load'], Decimal):
#                     #     waste['load'] = float(waste['load'])
#     return jsonify(front_data)
