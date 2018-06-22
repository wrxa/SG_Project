# -*- coding: utf-8 -*-
import unittest
import os
import json
from app import create_app, db
# collection
from app.energy_island.models import Device, DeviceProperties
from add_init_data import addDatas
# from mongoengine.queryset.visitor import Q
from app.algo import algorithm
from util.iapws_if97 import seuif97


class DeviceModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    # 测试设备表添加修改删除查找功能
    def test_device(self):
        print("\nstart...\n")
        # test = collection.find({'test': 'test'})
        # print(test)
        # device = Device.query.filter_by(id=1).all()
        # json_dict = json.loads(device[0].other_props_json)
        # print(json_dict)

        # xlsx_path = os.path.join(os.getcwd(), "doc", "data_20171009.xlsx")
        # addDatas.add_device_from_xlsx(addDatas, xlsx_path)
        # addDatas.remove_csv(xlsx_path, "all")
        # xlsx_path = os.path.join(os.getcwd(), "doc", "data_20171009.xlsx")
        # addDatas.add_device_from_xlsx(addDatas, xlsx_path)
        # addDatas.remove_csv(xlsx_path, "all")
        # a = seuif97.psat_s(8)
        # b = seuif97.psat_t(100)
        # c = seuif97.tsat_p(1)
        # d = seuif97.tsat_s(8)
        # e = seuif97.psat_t(seuif97.tsat_p(a))
        # f = seuif97.psat_t(d)
        # g = seuif97.tsat_p(b)
        # print("a=%s, b=%s, c=%s, d=%s, e=%s, f=%s, g=%s" % (a, b, c, d, e, f, g))
        # a = Device.query.filter(Device.id == 1).all()[0]
        # device_prop_json = json.loads(a.props_json)
        # for name in device_prop_json[u'prop_name']:
        #     index = device_prop_json[u'prop_name'].index(name)
        #     print("name: %s, value: %s" % (name, device_prop_json[u'prop_value'][index]))
        # algorithm.run_search(algorithm.TestData.requirement, algorithm.TestData.disabled_devices)
