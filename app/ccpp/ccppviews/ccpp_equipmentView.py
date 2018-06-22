# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
from flask_login import login_required, current_user
from . import ccppviews
import json
from app.models import EquipmentList, EquipmentListTemplate, Module
from app.main.service.mainService import MainService
from app.ccpp.service.ccpp_equipmentService import CcppEquipments
from flask import current_app

prohibitionlist = ['0', '1', '15', '34', '17', '18', '28', '29', '30', '31']


# ************** 设备清单模板 ********************
@ccppviews.route('/toCcppEquipmenttemplate')
@login_required
def toCcppEquipmenttemplate():
    session['menuSelect'] = "ccppequipmenttemplateList"
    return render_template(
        'page/ccpp/ccpp_equipmenttemplate.html'
    )


@ccppviews.route('/getEquipmentTemplate', methods=['POST'])
@login_required
def getEquipmentTemplate():
    current_app.logger.warning(u'操作者：%d,模板设备清单模板初始化', current_user.id)
    equipmentList = EquipmentListTemplate.search_EquipmentListTemplate(Module.CCPP)
    equipmentList_json = json.loads(equipmentList.equipment_template)
    equipment_json = json.dumps(equipmentList_json)
    titlelist = CcppEquipments.gethtmltitledict()
    return jsonify({'titlelist': titlelist, 'equipment_json': equipment_json, 'prohibitionlist': prohibitionlist})


@ccppviews.route('/saveEquipmentTemplate', methods=['POST'])
@login_required
def saveEquipmentTemplate():
    current_app.logger.warning(u'操作者：%d,模板设备清单保存!', current_user.id)
    nameData = request.values.get('nameData')
    uidData = request.values.get('uidData')
    typeData = request.values.get('typeData')
    contentData = request.values.get('contentData')
    unitData = request.values.get('unitData')
    countData = request.values.get('countData')
    remarkData = request.values.get('remarkData')
    Equipment = MainService.saveEquipmentList(None, uidData, nameData, typeData, contentData, unitData, countData, remarkData, Module.CCPP)
    if Equipment is not None:
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'error'})


# ************** 设备清单 ********************
@ccppviews.route('/toCcppEquipment')
@login_required
def toCcppEquipment():
    return render_template(
        'page/ccpp/ccpp_equipment.html'
    )


@ccppviews.route('/getEquipmentList', methods=['POST'])
@login_required
def getEquipmentList():
    planId = session.get('planId')
    current_app.logger.warning(u'操作者：%d,设备清单初始化!', current_user.id)
    equipmentList = EquipmentList.search_equipmentList(planId)
    equipmentList_json = json.loads(equipmentList.equipment_content)
    equipment_json = json.dumps(equipmentList_json)
    titlelist = CcppEquipments.gethtmltitledict()
    return jsonify({'titlelist':titlelist, 'equipment_json': equipment_json, 'prohibitionlist': prohibitionlist})


@ccppviews.route('/saveEquipmentList', methods=['POST'])
@login_required
def saveEquipmentList():
    planId = session.get('planId')
    current_app.logger.warning(u'操作者：%d,设备清单保存!', current_user.id)
    nameData = request.values.get('nameData')
    uidData = request.values.get('uidData')
    typeData = request.values.get('typeData')
    contentData = request.values.get('contentData')
    unitData = request.values.get('unitData')
    countData = request.values.get('countData')
    remarkData = request.values.get('remarkData')
    Equipment = MainService.saveEquipmentList(planId, uidData, nameData, typeData, contentData, unitData, countData, remarkData, None)
    if Equipment is not None:
        return jsonify({'state': 'success'})
    else:
        return jsonify({'state': 'error'})

