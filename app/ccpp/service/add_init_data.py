# -*- coding: utf-8 -*-
# from app.models import Device_LiBr_steam, Device_LiBr_HDC
# from app.models import Device_LiBr_LCC_DH, Device_LiBr_HCC
# from app.models import Device_LiBr_LCC, Device_LiBr_smoke_water_afterburning
# from app.models import Device_LiBr_smoke_water, Device_LiBr_smoke_double_effect
# from app.models import Device_LiBr_smoke_afterburning
from app.energy_island.models import Device, DeviceProperties, Hikari
from openpyxl import load_workbook
import csv
import os
import json


def initdata():
    xlsx_path = os.path.join(os.getcwd(), "doc", "data_20171009.xlsx")
    addDatas.add_device_from_xlsx(addDatas, xlsx_path)
    addDatas.remove_csv(xlsx_path, "all")
    xlsx_path_hikari = os.path.join(os.getcwd(), "doc", "hikari_time.xlsx")
    addDatas.add_hikari_time_from_xlsx(addDatas, xlsx_path_hikari)
    addDatas.remove_csv(xlsx_path_hikari, "hikari")


class addDatas():
    @staticmethod
    def tran_str_float(string):
        try:
            if string == '' or string is None:
                return 0
            else:
                return float(string)
        except Exception as e:
            print("Error %s" % e)
            raise e

    @staticmethod
    def add_LiBr(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_1.csv'), 'rb')
        reader = csv.reader(csvfile)
        cold_in = 0
        cold_out = 0
        cooling_in = 0
        cooling_out = 0
        high_in = 0
        high_out = 0
        cold_in_out = ""
        cooling_in_out = ""
        high_in_out = ""
        hot_source_in_out = ""
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 77:
                if index == 0:
                    prop_name.append(line[1])
                    prop_name.append(line[2])
                    prop_name.append(line[3])
                    prop_name.append(line[17])
                if index == 1:
                    for i in range(4, 17):
                        prop_name.append(line[i])
                    price = prop_name[3]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 2:
                    for i in range(1, 18):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                # print(line[1], line[2])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 1, props_json))
                if index >= 3:
                    if line[4]:
                        cold_in = line[4].split(r'→')[0]
                        cold_out = line[4].split(r'→')[1]
                        cooling_in = line[6].split(r'→')[0]
                        cooling_out = line[6].split(r'→')[1]
                        cold_in_out = line[4]
                        cooling_in_out = line[6]
                    prop_value = line[1:18:1]
                    if not prop_value[3]:
                        prop_value[3] = cold_in_out
                        prop_value[5] = cooling_in_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        1,
                        prop_value[0],
                        "制冷量",
                        self.tran_str_float(line[3]),
                        "kW",
                        "eng1",
                        "蒸汽消耗量",
                        self.tran_str_float(line[8]),
                        "kg/h",
                        "eng2",
                        "蒸汽压力",
                        self.tran_str_float(line[2]),
                        "MPa",
                        "eng3",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 79 and index <= 92:
                if index == 79:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[2])
                    prop_name.append(line[17])
                if index == 80:
                    for i in range(3, 17):
                        prop_name.append(line[i])
                    price = prop_name[2]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 81:
                    for i in range(1, 18):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 2, props_json))
                if index >= 82:
                    if line[3]:
                        cold_in_out = line[3]
                        cooling_in_out = line[5]
                        high_in_out = line[7]
                        cold_in = line[3].split(r'→')[0]
                        cold_out = line[3].split(r'→')[1]
                        cooling_in = line[5].split(r'→')[0]
                        cooling_out = line[5].split(r'→')[1]
                        high_in = line[7].split(r'→')[0]
                        high_out = line[7].split(r'→')[1]
                    prop_value = line[1:18:1]
                    if not prop_value[3]:
                        prop_value[2] = cold_in_out
                        prop_value[4] = cooling_in_out
                        prop_value[6] = high_in_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        2,
                        "HDC-" + prop_value[0],
                        "制冷能力",
                        self.tran_str_float(line[2]),
                        "10³kcal/h",
                        "eng1",
                        "流量",
                        self.tran_str_float(line[8]),
                        "ton/h",
                        "eng2",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 94 and index <= 124:
                if index == 94:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[2])
                    prop_name.append(line[20])
                if index == 95:
                    for i in range(3, 20):
                        prop_name.append(line[i])
                    price = prop_name[2]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 96:
                    for i in range(1, 21):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 3, props_json))
                if index >= 97:
                    if line[3]:
                        cold_in = line[3]
                        cold_out = line[4]
                        cooling_in = line[6]
                        cooling_out = line[7]
                        high_in = line[9]
                        high_out = line[10]
                    prop_value = line[1:21:1]
                    if not prop_value[3]:
                        prop_value[3] = cold_in
                        prop_value[4] = cold_out
                        prop_value[6] = cooling_in
                        prop_value[7] = cooling_out
                        prop_value[9] = high_in
                        prop_value[10] = high_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        3,
                        "LCC-" + prop_value[0] + "DH",
                        "制冷能力",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "流量",
                        self.tran_str_float(line[11]),
                        "ton/h",
                        "eng2",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 126 and index <= 156:
                if index == 126:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[2])
                    prop_name.append(line[20])
                if index == 127:
                    for i in range(3, 20):
                        prop_name.append(line[i])
                    price = prop_name[2]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 128:
                    for i in range(1, 21):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 4, props_json))
                if index >= 129:
                    if line[3]:
                        cold_in = line[3]
                        cold_out = line[4]
                        cooling_in = line[6]
                        cooling_out = line[7]
                        high_in = line[9]
                        high_out = line[10]
                    prop_value = line[1:21:1]
                    if not prop_value[3]:
                        prop_value[3] = cold_in
                        prop_value[4] = cold_out
                        prop_value[6] = cooling_in
                        prop_value[7] = cooling_out
                        prop_value[9] = high_in
                        prop_value[10] = high_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        4,
                        "LCC-" + prop_value[0],
                        "制冷能力",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "流量",
                        self.tran_str_float(line[11]),
                        "ton/h",
                        "eng2",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 158 and index <= 173:
                if index == 158:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[2])
                    prop_name.append(line[20])
                if index == 159:
                    for i in range(3, 20):
                        prop_name.append(line[i])
                    price = prop_name[2]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 160:
                    for i in range(1, 21):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 5, props_json))
                if index >= 161:
                    if line[3]:
                        cold_in = line[3]
                        cold_out = line[4]
                        cooling_in = line[6]
                        cooling_out = line[7]
                        high_in = line[9]
                        high_out = line[10]
                    prop_value = line[1:21:1]
                    if not prop_value[3]:
                        prop_value[3] = cold_in
                        prop_value[4] = cold_out
                        prop_value[6] = cooling_in
                        prop_value[7] = cooling_out
                        prop_value[9] = high_in
                        prop_value[10] = high_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        5,
                        "HCC-" + prop_value[0],
                        "制冷能力",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "流量",
                        self.tran_str_float(line[11]),
                        "ton/h",
                        "eng2",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 175 and index <= 192:
                if index == 175:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[28])
                if index == 176:
                    for i in range(2, 28):
                        prop_name.append(line[i])
                    price = prop_name[1]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 177:
                    for i in range(1, 29):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 6, props_json))
                if index >= 178:
                    if line[7]:
                        cold_in_out = line[7]
                        cooling_in_out = line[9]
                        high_in_out = line[11]
                    prop_value = line[1:29:1]
                    if not prop_value[7]:
                        prop_value[7] = cold_in_out
                        prop_value[9] = cooling_in_out
                        prop_value[11] = high_in_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        6,
                        "YP-" + prop_value[0] + "LHE",
                        "直燃单独运转或并用",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "直燃单独运转或并用",
                        self.tran_str_float(line[5]),
                        "kW",
                        "eng2",
                        "温水出口温度",
                        self.tran_str_float(line[9].split(r'→')[1]),
                        "℃",
                        "eng3",
                        "温水流量",
                        self.tran_str_float(line[10]),
                        "m³/h",
                        "eng4",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 194 and index <= 214:
                if index == 194:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[24])
                if index == 195:
                    for i in range(2, 24):
                        prop_name.append(line[i])
                    price = prop_name[1]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 196:
                    for i in range(1, 25):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 7, props_json))
                if index >= 197:
                    if line[6]:
                        cold_in_out = line[6]
                        cooling_in_out = line[8]
                        high_in_out = line[10]
                        hot_source_in_out = line[12]
                    prop_value = line[1:25:1]
                    if not prop_value[5]:
                        prop_value[5] = cold_in_out
                        prop_value[7] = cooling_in_out
                        prop_value[9] = high_in_out
                        prop_value[11] = hot_source_in_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        7,
                        "YP-" + prop_value[0] + "LHD",
                        "单效双效同时运转",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "供暖量",
                        self.tran_str_float(line[5]),
                        "kW",
                        "eng2",
                        "温水出口温度",
                        self.tran_str_float(0 if len(line[8]) == 0 else line[8].split(r'→')[1]),
                        "℃",
                        "eng3",
                        "温水流量",
                        self.tran_str_float(line[9]),
                        "m³/h",
                        "eng4",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 216 and index <= 233:
                if index == 216:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[2])
                    prop_name.append(line[3])
                    prop_name.append(line[24])
                if index == 217:
                    for i in range(4, 19):
                        prop_name.append(line[i])
                    price = prop_name[3]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 218:
                    for i in range(1, 20):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 8, props_json))
                if index >= 219:
                    if line[4]:
                        cold_in_out = line[4]
                        cooling_in_out = line[6]
                        high_in_out = line[8]
                    prop_value = line[1:20:1]
                    if not prop_value[3]:
                        prop_value[3] = cold_in_out
                        prop_value[5] = cooling_in_out
                        prop_value[7] = high_in_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        8,
                        "YP-" + prop_value[0] + "LHB",
                        "制冷量",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "供暖量",
                        self.tran_str_float(line[3]),
                        "kW",
                        "eng2",
                        "温水出口温度",
                        self.tran_str_float(line[6].split(r'→')[1]),
                        "℃",
                        "eng3",
                        "最大耗量",
                        self.tran_str_float(line[10]),
                        "kg/h",
                        "eng4",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 235 and index <= 252:
                if index == 235:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[25])
                if index == 236:
                    for i in range(2, 25):
                        prop_name.append(line[i])
                    price = prop_name[1]
                    prop_name.remove(price)
                    prop_name.append(price)
                if index == 237:
                    for i in range(1, 26):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 9, props_json))
                if index >= 238:
                    if line[6]:
                        cold_in_out = line[6]
                        cooling_in_out = line[8]
                        high_in_out = line[10]
                        hot_source_in_out = line[12]
                    prop_value = line[1:26:1]
                    if not prop_value[5]:
                        prop_value[5] = cold_in_out
                        prop_value[7] = cooling_in_out
                        prop_value[9] = high_in_out
                        prop_value[11] = hot_source_in_out
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        9,
                        "YP-" + prop_value[0] + "LHC",
                        "烟气直燃同时运转",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "烟气直燃同时运转/直燃单独运转",
                        self.tran_str_float(line[4]),
                        "kW",
                        "eng2",
                        "温水出口温度",
                        self.tran_str_float(line[8].split(r'→')[1]),
                        "℃",
                        "eng3",
                        "最大耗量",
                        self.tran_str_float(line[13]),
                        "kg/h",
                        "eng4",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 309 and index <= 334:
                if index == 309:
                    del prop_name[:]
                    del prop_unit[:]
                    prop_name.append(line[1])
                    prop_name.append(line[2])
                    prop_name.append(line[3])
                if index == 310:
                    for i in range(4, 29):
                        prop_name.append(line[i])
                    price = prop_name[1]
                if index == 311:
                    for i in range(1, 29):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(1, 10, props_json))
                if index >= 312:
                    prop_value = line[1:29:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        1,
                        10,
                        "DG-" + prop_value[0] + "G(K)HDC",
                        "制冷能力",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "供暖能力",
                        self.tran_str_float(line[3]),
                        "kW",
                        "eng2",
                        "流量",
                        self.tran_str_float(line[11]),
                        "m³/h",
                        "eng3",
                        "天然气Nm³/h",
                        self.tran_str_float(line[14]),
                        "m³/h",
                        "eng4",                        
                        "天然气Nm³/h",
                        self.tran_str_float(line[17]),
                        "m³/h",
                        "eng5",
                        props_json=props_json
                    )
                    Device.insert_device(device)
        csvfile.close()

    @staticmethod
    def add_electric_refrigeration(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_2.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 16:
                if index == 1:
                    for i in range(0, 5):
                        prop_name.append(line[i])
                if index == 2:
                    for i in range(0, 5):
                        prop_unit.append(line[i])
                    prop_unit[0] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(2, 1, props_json))
                if index >= 3:
                    prop_value = line[0:5:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        2,
                        1,
                        prop_value[0],
                        "电机额定功率",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        "油泵电机功率",
                        self.tran_str_float(line[3]),
                        "kW",
                        "eng2",
                        "制冷量左",
                        self.tran_str_float(line[1].split('/')[0]),
                        "kW",
                        "eng3",
                        "制冷量右",
                        self.tran_str_float(line[1].split('/')[1]),
                        "kW",
                        "eng4",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_heat_pump(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_3.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 36:
                if index == 1:
                    for i in range(1, 16):
                        prop_name.append(line[i])
                if index == 2:
                    for i in range(1, 16):
                        prop_unit.append(line[i])
                    prop_unit[14] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(3, 1, props_json))
                if index >= 3:
                    prop_value = line[1:16:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        3,
                        1,
                        "Ground Source Heat Pumps",
                        "制冷量",
                        self.tran_str_float(line[1]),
                        "kW",
                        "eng1",
                        "制热量 ",
                        self.tran_str_float(line[7]),
                        "kW",
                        "eng2",
                        "高温制热量",
                        self.tran_str_float(line[13]),
                        "kW",
                        "eng3",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index >= 57 and index <= 81:
                if index == 57:
                    for i in range(1, 15):
                        prop_name.append(line[i])
                if index == 58:
                    for i in range(1, 15):
                        prop_unit.append(line[i])
                    prop_unit[13] = ""
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(3, 2, props_json))
                if index >= 59:
                    prop_value = line[1:15:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        3,
                        2,
                        "Air Source Heat Pumps",
                        "制冷量",
                        self.tran_str_float(line[1]),
                        "kW",
                        "eng1",
                        "制热量 ",
                        self.tran_str_float(line[4]),
                        "kW",
                        "eng2",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_gas_turbine(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_4.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 52:
                if index == 0:
                    for i in range(0, 30):
                        prop_name.append(line[i])
                if index == 1:
                    for i in range(0, 30):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(4, 1, props_json))
                if index >= 2:
                    prop_value = line[0:30:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        4,
                        1,
                        line[0],
                        "燃机出力",
                        self.tran_str_float(line[1]),
                        "kW",
                        "eng1",
                        "燃机排烟温度",
                        self.tran_str_float(line[14]),
                        "℃",
                        "eng2",
                        "锅炉烟气流量",
                        self.tran_str_float(line[15]),
                        "t/h",
                        "eng3",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_internal_combustion_engine(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_5.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 63:
                if index == 0:
                    for i in range(0, 27):
                        prop_name.append(line[i])
                if index == 1:
                    for i in range(0, 27):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(5, 1, props_json))
                if index >= 2:
                    prop_value = line[0:27:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        5,
                        1,
                        line[1],
                        "电功率",
                        self.tran_str_float(line[0]),
                        "kW",
                        "eng1",
                        "排烟温度",
                        self.tran_str_float(line[14]),
                        "℃",
                        "eng2",
                        "质量流量，湿",
                        self.tran_str_float(line[15]),
                        "kg/h",
                        "eng2",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_photovoltaic(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_6.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 27:
                if index == 0:
                    for i in range(0, 10):
                        prop_name.append(line[i])
                if index == 1:
                    for i in range(0, 10):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(6, 1, props_json))
                if index >= 3:
                    prop_value = line[0:10:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        6,
                        1,
                        line[0],
                        "最大功率",
                        self.tran_str_float(line[4]),
                        "W",
                        "eng1",
                        "组件效率",
                        self.tran_str_float(line[5]),
                        "%",
                        "eng2",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_air_compression_station(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_7.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 93:
                if index == 0:
                    for i in range(0, 13):
                        prop_name.append(line[i])
                if index == 1:
                    for i in range(0, 13):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(7, 1, props_json))
                if index >= 2:
                    prop_value = line[0:13:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        7,
                        1 if line[2] == "水冷" else 2,
                        line[3],
                        "压力",
                        self.tran_str_float(line[4]),
                        "Mpa",
                        "eng1",
                        "气量",
                        self.tran_str_float(line[5]),
                        "m3/min",
                        "eng2",
                        "冷却方式",
                        1 if line[2] == "水冷" else 2,
                        "unit3",
                        "eng3",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_boiler(self, xlsx_path):
        # 未完成，需要进一步讨论
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_8.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 93:
                if index == 0:
                    for i in range(0, 13):
                        prop_name.append(line[i])
                if index == 1:
                    for i in range(0, 13):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(8, 1, props_json))
                if index >= 2:
                    prop_value = line[0:13:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        8,
                        1,
                        line[0],
                        "name1",
                        self.tran_str_float(line[4]),
                        "unit1",
                        "eng1",
                        "name2",
                        self.tran_str_float(line[5]),
                        "unit2",
                        "eng2",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_electricity_storage(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_9.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 7:
                if index == 1:
                    for i in range(0, 24):
                        prop_name.append(line[i])
                if index == 2:
                    for i in range(0, 24):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(9, 1, props_json))
                if index >= 3:
                    prop_value = line[0:24:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        9,
                        1,
                        line[1],
                        "name1",
                        self.tran_str_float(line[0]),
                        "unit1",
                        "eng1",
                        props_json=props_json
                    )
                    Device.insert_device(device)
            elif index <= 16:
                if index == 10:
                    for i in range(0, 24):
                        prop_name.append(line[i])
                if index == 11:
                    for i in range(0, 24):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(9, 2, props_json))
                if index >= 12:
                    prop_value = line[0:24:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        9,
                        2,
                        line[1],
                        "name1",
                        self.tran_str_float(line[0]),
                        "unit1",
                        "eng1",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_wind_power(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_12.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 9:
                if index == 0:
                    for i in range(0, 17):
                        prop_name.append(line[i])
                if index == 1:
                    for i in range(0, 17):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(12, 1, props_json))
                if index >= 2:
                    prop_value = line[0:17:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        12,
                        1,
                        line[1],
                        "额定功率",
                        self.tran_str_float(line[2]),
                        "kW",
                        "eng1",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_sewage(self, xlsx_path):
        csvfile = file(xlsx_path.replace('.xlsx', '_sheet_13.csv'), 'rb')
        reader = csv.reader(csvfile)
        prop_name = []
        prop_unit = []
        for index, line in enumerate(reader):
            if index <= 9:
                if index == 2:
                    for i in range(0, 13):
                        prop_name.append(line[i])
                if index == 3:
                    for i in range(0, 13):
                        prop_unit.append(line[i])
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit})
                    DeviceProperties.insert_device_properties(DeviceProperties.create_device_properties(13, 1, props_json))
                if index >= 4:
                    prop_value = line[0:13:1]
                    props_json = json.dumps({"prop_name": prop_name, "prop_unit": prop_unit, "prop_value": prop_value})
                    device = Device.create_device(
                        13,
                        1,
                        line[0],
                        "name1",
                        self.tran_str_float(line[7]),
                        "unit1",
                        "eng1",
                        props_json=props_json
                    )
                    Device.insert_device(device)

    @staticmethod
    def add_hikari_time(self, xlsx_path):
        province_city_dict = {
            u'山东': u'济南',
            u'河北': u'石家庄',
            u'吉林': u'长春',
            u'黑龙江': u'哈尔滨',
            u'辽宁': u'沈阳',
            u'内蒙古': u'呼和浩特',
            u'我也不知道是哪': u'海拉尔',
            u'新疆': u'乌鲁木齐',
            u'甘肃': u'兰州',
            u'宁夏': u'银川',
            u'山西': u'太原',
            u'陕西': u'西安',
            u'河南': u'郑州',
            u'安徽': u'合肥',
            u'江苏': u'南京',
            u'浙江': u'杭州',
            u'福建': u'福州',
            u'广东': u'广州',
            u'江西': u'南昌',
            u'海南': u'海口',
            u'广西': u'南宁',
            u'贵州': u'贵阳',
            u'湖南': u'长沙',
            u'湖北': u'武汉',
            u'四川': u'成都',
            u'云南': u'昆明',
            u'西藏': u'拉萨',
            u'青海': u'西宁',
            u'天津': u'天津',
            u'上海': u'上海',
            u'重庆': u'重庆',
            u'北京': u'北京',
            u'台湾': u'台北'
        }
        city_province_dict = dict(zip(list(map(lambda x: x.encode('utf-8'), province_city_dict.values())), list(map(lambda x: x.encode('utf-8'), province_city_dict.keys()))))
        csvfile = file(xlsx_path.replace('.xlsx', '_transform.csv'), 'rb')
        reader = csv.reader(csvfile)
        i = 0
        j = 0
        for index, line in enumerate(reader):
            i = i + 1
            if i == 1:
                city_list = line[1:12]
            if i >= 3:
                for city in city_list:
                    index = city_list.index(city)
                    blank = '\xc2\xa0'
                    time_list = line[1:13]
                    province = city_province_dict[city.replace(blank, '')]
                    hikari_time = Hikari(city.replace(blank, ''), province, line[0].split(blank)[0], line[0].split(blank)[1], time_list[index].split(blank)[0], time_list[index].split(blank)[1], time_list[index].split(blank)[2], time_list[index].split(blank)[3])
                    Hikari.insert_hikari_time(hikari_time)
            if i == 38:
                i = 0

    # 读取数据源excel文件，抽出所用的数据做成csv文件
    @staticmethod
    def xlsx2csv(filename):
        try:
            xlsx_file_reader = load_workbook(filename=filename, data_only=True)
            # data_only=True指定后将获得cell的计算值而非表达式
            i = 1
            for sheet in xlsx_file_reader.get_sheet_names():
                # 每个sheet输出到一个csv文件中，文件名用xlsx文件名和sheet名用'_'连接
                csv_filename = '{xlsx}_{sheet}.csv'.format(
                    xlsx=os.path.splitext(filename.replace(' ', '_'))[0],
                    sheet="sheet_" + str(i))

                csv_file = file(csv_filename, 'wb')
                csv_file_writer = csv.writer(csv_file)

                sheet_ranges = xlsx_file_reader[sheet]
                for row in sheet_ranges.rows:
                    row_container = []
                    for cell in row:
                        if cell.value is None:
                            cell.value = u""
                        if type(cell.value) == unicode:
                            row_container.append(
                                cell.value.encode('utf-8'))
                        else:
                            row_container.append(str(cell.value))
                    csv_file_writer.writerow(row_container)
                csv_file.close()
                i = i + 1

        except Exception as e:
            print(e)

    @staticmethod
    def csv_transform(filename):
        csvfile = file(filename.replace('.xlsx', '_sheet_1.csv'), 'rb')
        reader = csv.reader(csvfile)
        line_list = []
        all_list = []
        i = 0
        for index, line in enumerate(reader):
            i = i + 1
            line_list.append(line[0])
            if i == 12:
                all_list.append(line_list[:])
                line_list = []
                i = 0
        print(line_list)
        # f2write = file(filename.replace('.xlsx', '_transform.csv'), 'a')
        # for line in all_list:
        #     f2write.writelines(line)
        # f2write.close()
        with file(filename.replace('.xlsx', '_transform.csv'), 'ab') as csvfile:
            writer = csv.writer(csvfile)
            for line in all_list:
                writer.writerow(line)

    # 删除做成的csv文件
    # param: xlsx_path      excel文件路径
    # param: mode       删除模式: "device"、"carrier_energy"、"setting_config"、"all"
    @staticmethod
    def remove_csv(xlsx_path, mode):
        if mode == "device":
            if os.path.exists(xlsx_path.replace('.xlsx', '_Sheet2.csv')):
                os.remove(xlsx_path.replace('.xlsx', '_Sheet2.csv'))
                print("file: %s removed" % xlsx_path.replace(
                    '.xlsx', '_Sheet2.csv'))
        elif mode == "carrier_energy":
            if os.path.exists(xlsx_path.replace('.xlsx', '_Sheet5.csv')):
                os.remove(xlsx_path.replace('.xlsx', '_Sheet5.csv'))
                print("file: %s removed" % xlsx_path.replace(
                    '.xlsx', '_Sheet5.csv'))
        elif mode == "setting_config":
            if os.path.exists(xlsx_path.replace('.xlsx', '_Sheet7.csv')):
                os.remove(xlsx_path.replace('.xlsx', '_Sheet7.csv'))
                print("file: %s removed" % xlsx_path.replace(
                    '.xlsx', '_Sheet7.csv'))
        elif mode == 'hikari':
            if os.path.exists(xlsx_path.replace('.xlsx', '_sheet_1.csv')):
                    os.remove(xlsx_path.replace('.xlsx', '_sheet_1.csv'))
                    print("file: %s removed" % xlsx_path.replace(
                        '.xlsx', '_sheet_1.csv'))
            if os.path.exists(xlsx_path.replace('.xlsx', '_transform.csv')):
                    os.remove(xlsx_path.replace('.xlsx', '_transform.csv'))
                    print("file: %s removed" % xlsx_path.replace(
                        '.xlsx', '_transform.csv'))
        elif mode == "all":
            for i in range(13):
                if os.path.exists(xlsx_path.replace('.xlsx', '_sheet_' + str(i + 1) + '.csv')):
                    os.remove(xlsx_path.replace('.xlsx', '_sheet_' + str(i + 1) + '.csv'))
                    print("file: %s removed" % xlsx_path.replace(
                        '.xlsx', '_sheet_' + str(i + 1) + '.csv'))
            if os.path.exists(xlsx_path.replace('.xlsx', '_sheet_1.csv')):
                    os.remove(xlsx_path.replace('.xlsx', '_sheet_1.csv'))
                    print("file: %s removed" % xlsx_path.replace(
                        '.xlsx', '_sheet_1.csv'))
            if os.path.exists(xlsx_path.replace('.xlsx', '_transform.csv')):
                    os.remove(xlsx_path.replace('.xlsx', '_transform.csv'))
                    print("file: %s removed" % xlsx_path.replace(
                        '.xlsx', '_transform.csv'))
        else:
            print("mode not correct")

    # 添加device表的数据，数据来源：由excel文件做成的csv文件
    @staticmethod
    def add_device_from_xlsx(self, xlsx_path):
        if not os.path.exists(xlsx_path.replace('.xlsx', '_sheet_1.csv')):
            self.xlsx2csv(xlsx_path)
        self.add_LiBr(self, xlsx_path)
        self.add_electric_refrigeration(self, xlsx_path)
        self.add_heat_pump(self, xlsx_path)
        self.add_gas_turbine(self, xlsx_path)
        self.add_internal_combustion_engine(self, xlsx_path)
        self.add_photovoltaic(self, xlsx_path)
        self.add_air_compression_station(self, xlsx_path)
        self.add_electricity_storage(self, xlsx_path)
        self.add_wind_power(self, xlsx_path)
        self.add_sewage(self, xlsx_path)
        # self.remove_csv(xlsx_path, "device")

    @staticmethod
    def add_hikari_time_from_xlsx(self, xlsx_path):
        if not os.path.exists(xlsx_path.replace('.xlsx', '_sheet_1.csv')):
            self.xlsx2csv(xlsx_path)
        if not os.path.exists(xlsx_path.replace('.xlsx', '_transform.csv')):
            self.csv_transform(xlsx_path)
        self.add_hikari_time(self, xlsx_path)
        # self.remove_csv(xlsx_path, "hikari")
