#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import create_app, db
from app.ccpp.models.ccpp_ccpp_calculateModel import Ccpp_ccpp
from app.ccpp.models.ccpp_questionnaireModel import Questionnaire
from app.ccpp.models.ccpp_circulating_waterModel import CcppCirculatingWater
from app.ccpp.models.ccpp_chimney_calculateModel import CcppChimneyCalculate
from app.ccpp.models.ccpp_turbineModel import CcppTurbine
from app.ccpp.models.init_ccpp_constantModel import InitCcppCalculate
from app.ccpp.models.init_circulating_waterModel import InitCcppCirculatingWater
from app.ccpp.models.init_questionnaire_constantModel \
    import InitCcppQuestionnaire
from app.ccpp.models.init_ccpp_chimney_calculateModel import InitCcppChimneyCalculate
from app.ccpp.models.init_ccpp_turbineModel import InitCcppTurbine
from app.ccpp.service.add_init_data import initdata
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from app.ccpp.models.constantModel import CcppConstant
from app.models import User, Permission, ReportTemplate
from app.coal_chp.init.initCoalCHP import AddCoalCHP as addCoalCHP
from app.coal_chp.model.coalchpModels import CoalCHPConstant
from app.biomass_chp.models.initBiomassCHP import AddBiomassCHP as addBiomassCHP
from app.biomass_chp.models import modelsBiomass
from app.gpg.model import gasPowerGeneration_models
from app.gpg.init.initGPG import AddGPG as addGPG
from app.energy_island.energyisland_service import EnergyIslandService
from app.ccpp.models.textlogic_and_template_init import InitCcppTextlogic, InitCcppReportTemplate
from app.gpg.model.textlogic_and_template_init import InitGPGReportTemplate, InitGPGTextlogic
from app.biomass_chp.models.textlogic_and_template_init import InitBiomassTextlogic, InitBiomassReportTemplate
from app.ccpp.models.init_ccpp_ccpp_economicModel import InitCcppEconomic
from app.ccpp.models.ccpp_ccpp_economicModel import Ccpp_ccpp_economic
from app.ccpp.models.init_biomasschp_constantModel import InitCcppWaterTreatment
from app.main.initEquipmentListTemplate import initEquipmentListTemplate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


# 自定义过滤器(格式化时间)
# def dateformat(value, format="%Y-%m-%d %H:%M:%S"):
def dateformat(value, format="%Y-%m-%d"):
    return value.strftime(format)


# 注册自定义过滤器
env = app.jinja_env
env.filters['dateformat'] = dateformat


# 为shell命令添加上下文
def make_shell_context():
    return dict(
        app=app,
        db=db,
        Permission=Permission)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
# manager.add_command("runserver", Server(host="0.0.0.0", port=80))


@manager.command
def creatcontentjson():
    f = open('a.txt', 'w')
    import sys
    old = sys.stdout
    # 将当前系统输出储存到一个临时变量中
    sys.stdout = f
    # 输出重定向到文件
    coalCHPConstant = CoalCHPConstant.search_coalCHPConstant('coalCHP_circulatingWater')
    print('# -*- coding: utf-8 -*-')
    print('from .constantModel import CcppConstant')
    print
    print
    print('# ccpp循环水')
    print('circulatingWater_data = [{')
    for constant in coalCHPConstant:
        print('    "module_name": "' + constant.module_name.encode("utf-8") + '",')
        print('    "name_eng": "' + constant.name_eng.encode("utf-8") + '",')
        print('    "name": u"' + constant.name.encode("utf-8") + '",')
        print('    "symbol": u"' + constant.symbol.encode("utf-8") + '",')
        print('    "unit": u"' + constant.unit.encode("utf-8") + '",')
        print('    "calculate": u"' + constant.calculate.encode("utf-8") + '",')
        print('    "remark": u"' + constant.remark.encode("utf-8") + '",')
        print('    "defaultvalue": u"' + constant.default_value.encode("utf-8") + '",')
        print('    "minmodelid": u"1",')
        print('    "controltype": u"input",')
        if constant.disable == "T":
            print('    "permission": u"false",')
        else:
            print('    "permission": u"true",')
        print('}, {')
    # 测试一个打印输出
    sys.stdout = old
    # 还原原系统输出
    f.close()

@manager.command
def initGpgReportTemplate():
    InitGPGReportTemplate.init_data()
    
@manager.command
def initdatas():
    db.drop_all()
    db.create_all()
    addCoalCHP.init_data()
    addBiomassCHP.init_data()
    InitCcppCalculate.init_data()
    InitCcppQuestionnaire.init_data()
    InitCcppCirculatingWater.init_data()
    InitCcppChimneyCalculate.init_data()
    InitCcppTurbine.init_data()
    InitCcppWaterTreatment.init_data()
    initdata()
    addGPG.init_data()
    InitCcppTextlogic.init_data()
    InitCcppReportTemplate.init_data()
    InitGPGTextlogic.init_data()
    InitGPGReportTemplate.init_data()
    InitBiomassTextlogic.init_data()
    InitBiomassReportTemplate.init_data()
    InitCcppEconomic.init_data()
    initEquipmentListTemplate.init_data()


@manager.command
def backup():
    os.system('pg_dump -h 192.168.33.110 -p 5432 -U postgres -d energy_island > energy_island.bak')


@manager.command
def recovery():
    db.drop_all()
    os.system('psql -h 192.168.33.110 -p 5432 -U postgres -d energy_island < energy_island.bak')


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


env = app.jinja_env
env.filters['slice_arr'] = EnergyIslandService.slice_arr

if __name__ == '__main__':
    # manager.run(default_command="runserver")
    manager.run()
    # app.run(host='0.0.0.0', port=5000)
