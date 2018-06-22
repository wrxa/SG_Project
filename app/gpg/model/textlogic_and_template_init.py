# -*- coding: utf-8 -*-
from app.models import Textlogic, ReportTemplate

# 模板表
reportTemplate_data = [{
    "template_name": u"煤气发电基准模板",
    "module_id": u"gasPowerGeneration",
    "user_id": "1",
    "template_create_date": "2018-01-10 09:30:40.187",
    "template_update_date": "2018-01-10 13:42:37.821",
    "template__left_menu":
    u"""
[{"id":"1","text":"文档目录","icon":true,"li_attr":{"id":"1"},"a_attr":{"href":"#","id":"1_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_2","text":"第一章 概述","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_2"},"a_attr":{"href":"#","id":"j1_2_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_5","text":"第二章\t总承包内容及交接点","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_5"},"a_attr":{"href":"#","id":"j1_5_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_8","text":"2.1\t项目总承包内容","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_8"},"a_attr":{"href":"#","id":"j1_8_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_9","text":"2.1.1\t工程设计范围","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_9"},"a_attr":{"href":"#","id":"j1_9_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5","j1_8"]},{"id":"j1_10","text":"2.1.2\t成套设备采购及供货","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_10"},"a_attr":{"href":"#","id":"j1_10_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5","j1_8"]},{"id":"j1_11","text":"2.1.3\t设备安装调试内容","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_11"},"a_attr":{"href":"#","id":"j1_11_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5","j1_8"]},{"id":"j1_12","text":"2.1.4\t本工程不包含的施工及安装范围","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_12"},"a_attr":{"href":"#","id":"j1_12_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5","j1_8"]},{"id":"j1_13","text":"2.1.5\t土建工程施工主要内容（总承包方范围）：","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_13"},"a_attr":{"href":"#","id":"j1_13_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5","j1_8"]}],"type":"file","parentNode":["1","j1_5"]},{"id":"j1_14","text":"2.2\t项目交接点","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_14"},"a_attr":{"href":"#","id":"j1_14_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_5"]}],"type":"file","parentNode":["1"]},{"id":"j1_15","text":"第三章\t设计及施工标准规范","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_15"},"a_attr":{"href":"#","id":"j1_15_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_16","text":"第四章\t工程建设技术条件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_16"},"a_attr":{"href":"#","id":"j1_16_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_17","text":"4.1\t厂址条件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_17"},"a_attr":{"href":"#","id":"j1_17_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_18","text":"4.2\t气象条件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_18"},"a_attr":{"href":"#","id":"j1_18_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_19","text":"4.3\t工程地质","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_19"},"a_attr":{"href":"#","id":"j1_19_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_20","text":"4.4\t地震烈度","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_20"},"a_attr":{"href":"#","id":"j1_20_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_21","text":"4.5\t建设场地","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_21"},"a_attr":{"href":"#","id":"j1_21_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_22","text":"4.6\t燃料与余热资源（见1.1）","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_22"},"a_attr":{"href":"#","id":"j1_22_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_23","text":"4.7\t电源情况","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_23"},"a_attr":{"href":"#","id":"j1_23_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_24","text":"4.8\t水源状况","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_24"},"a_attr":{"href":"#","id":"j1_24_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_25","text":"4.9\t气源情况","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_25"},"a_attr":{"href":"#","id":"j1_25_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]},{"id":"j1_26","text":"4.10\t辅料供应","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_26"},"a_attr":{"href":"#","id":"j1_26_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_16"]}],"type":"file","parentNode":["1"]},{"id":"j1_29","text":"第五章\t工程建设技术参数","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_29"},"a_attr":{"href":"#","id":"j1_29_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_30","text":"5.1\t项目概况","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_30"},"a_attr":{"href":"#","id":"j1_30_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29"]},{"id":"j1_31","text":"5.2\t项目性质","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_31"},"a_attr":{"href":"#","id":"j1_31_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29"]},{"id":"j1_32","text":"5.3\t主要工艺方案","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_32"},"a_attr":{"href":"#","id":"j1_32_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29"]},{"id":"j1_33","text":"5.4\t系统描述","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_33"},"a_attr":{"href":"#","id":"j1_33_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_34","text":"5.4.1\t机务","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_34"},"a_attr":{"href":"#","id":"j1_34_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29","j1_33"]},{"id":"j1_35","text":"5.4.2\t汽机房","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_35"},"a_attr":{"href":"#","id":"j1_35_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29","j1_33"]},{"id":"j1_36","text":"5.4.3\t锅炉补给水系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_36"},"a_attr":{"href":"#","id":"j1_36_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29","j1_33"]},{"id":"j1_37","text":"5.4.4\t供排水系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_37"},"a_attr":{"href":"#","id":"j1_37_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29","j1_33"]},{"id":"j1_38","text":"5.4.5\t通风和空调设施","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_38"},"a_attr":{"href":"#","id":"j1_38_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29","j1_33"]},{"id":"j1_39","text":"5.4.6\t电气系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_39"},"a_attr":{"href":"#","id":"j1_39_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29","j1_33"]},{"id":"j1_40","text":"5.4.7\t热控部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_40"},"a_attr":{"href":"#","id":"j1_40_anchor"},"state":{"loaded":true,"opened":false,"selected":true,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29","j1_33"]}],"type":"file","parentNode":["1","j1_29"]},{"id":"j1_41","text":"5.5\t土建部分（以详细设计为准）","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_41"},"a_attr":{"href":"#","id":"j1_41_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_29"]}],"type":"file","parentNode":["1"]},{"id":"j1_42","text":"第六章\t设备监造（检验）和性能验收试验","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_42"},"a_attr":{"href":"#","id":"j1_42_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_43","text":"6.1\t设计、制造标准","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_43"},"a_attr":{"href":"#","id":"j1_43_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_42"]},{"id":"j1_44","text":"6.2\t质量保证","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_44"},"a_attr":{"href":"#","id":"j1_44_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_42"]},{"id":"j1_45","text":"6.3\t监造和检查试验","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_45"},"a_attr":{"href":"#","id":"j1_45_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_42"]}],"type":"file","parentNode":["1"]},{"id":"j1_46","text":"第七章\t技术服务","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_46"},"a_attr":{"href":"#","id":"j1_46_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_47","text":"7.1\t技术服务范围","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_47"},"a_attr":{"href":"#","id":"j1_47_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_46"]},{"id":"j1_48","text":"7.2\t人员培训","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_48"},"a_attr":{"href":"#","id":"j1_48_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_46"]},{"id":"j1_49","text":"7.3\t设计联络","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_49"},"a_attr":{"href":"#","id":"j1_49_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_46"]},{"id":"j1_50","text":"7.4\t技术文件提交","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_50"},"a_attr":{"href":"#","id":"j1_50_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_46"]},{"id":"j1_51","text":"7.5\t竣工资料提交按照发包方项目竣工验收的有关文件执行：","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_51"},"a_attr":{"href":"#","id":"j1_51_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_46"]}],"type":"file","parentNode":["1"]},{"id":"j1_52","text":"第八章\t工程质量及考核方式","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_52"},"a_attr":{"href":"#","id":"j1_52_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_53","text":"8.1\t工程质量","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_53"},"a_attr":{"href":"#","id":"j1_53_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_52"]},{"id":"j1_54","text":"8.2\t考核方式","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_54"},"a_attr":{"href":"#","id":"j1_54_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_52"]}],"type":"file","parentNode":["1"]},{"id":"j1_55","text":"第九章\t其他","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_55"},"a_attr":{"href":"#","id":"j1_55_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_56","text":"第十章\t附件目录","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_56"},"a_attr":{"href":"#","id":"j1_56_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]}],"type":"default"}]
""",
    "template_state": "0",
    "template_left_content": u"""
[{"content":"用法简介：\n1. 鼠标选中“文档目录”，点击“添加子标题”按钮，添加一级子目录。\n2. 鼠标选中生成的子级目录，点击“添加子标题”按钮，添加该目录的子级目录。\n3. 鼠标选中目录，点击“删除”按钮，删除该目录结构。\n4. 鼠标选中目录，点击“重命名”按钮或者点击键盘“F2”按钮，重命名目录。\n5. 鼠标选中目录拖拽可交换目录结构位置。\n6. 插入表格或图片后，点击“切换预览方式”按钮，可预览表格和图片，再次点击此按钮回到结构预览。\n7. 插入图表后需要在图表前后各留一行空行。\n8. 编辑模板时，请不要忘记点击“保存”按钮，将数据保存到数据库方便下次使用。\n","id":"1"},{"class":["1"],"content":"##### @@company.company_name@@（以下简称发包人），西安陕鼓动力股份有限公司（以下简称总承包方），根据《中华人民共和国合同法》、《中华人民共和国建筑法》等有关法律规定，遵循公平、平等、诚实信用的原则，为明确双方权利和义务，就总承包 (手动输入) 项目事宜，经双方协商一致，同意并按以下条款签署本协议。总承包方应严格按国家、行业及地方现行标准、规范、规程和有关条例进行设计（双方另有约定的除外），采用成熟、实用、可靠的工艺技术及装备，工程质量合格、生产和设备运行安全可靠。\n##### 目前厂区大量高炉煤气和转炉煤气富余，煤气管网中除了企业自身消耗为，大多处于放散状态，不但造成了环境的污染，而且造成大量能源的浪费，发包人依据厂区富余煤气及蒸汽情况，其参数如下表：\n##### 表1、富余高炉煤气参数表\n\n| 参数名称 |额定流量（Nm³/h） |最大富余量（Nm³/h） |最小富余量（Nm³/h） |供气压力（kPa） |供气温度（℃） |\n|:------|:------|:------|:------|:------|:------|\n| 高炉煤气量 | @@gaspowergeneration_needsquestionnaire.surplus_gas_bfg@@ | @@gaspowergeneration_needsquestionnaire.surplus_gas_bfg_max@@ | @@gaspowergeneration_needsquestionnaire.surplus_gas_bfg_min@@ | @@gaspowergeneration_needsquestionnaire.bfg_gas_pressure@@ | @@gaspowergeneration_needsquestionnaire.bfg_gas_temperature@@ |\n\n##### 表2、富余转炉煤气参数表\n\n| 参数名称 |额定流量（Nm³/h） |最大富余量（Nm³/h） |最小富余量（Nm³/h） |供气压力（kPa） |供气温度（℃） |\n|:------|:------|:------|:------|:------|:------|\n| 转炉煤气量 | @@gaspowergeneration_needsquestionnaire.surplus_gas_ldg@@ | @@gaspowergeneration_needsquestionnaire.surplus_maxldg_gas@@ | @@gaspowergeneration_needsquestionnaire.surplus_minldg_gas@@ | @@gaspowergeneration_needsquestionnaire.ldg_gas_pressure@@ | @@gaspowergeneration_needsquestionnaire.ldg_gas_temperature@@ |\n\n##### 表3、富余焦炉煤气参数表\n\n| 参数名称 |额定流量（Nm³/h） |最大富余量（Nm³/h） |最小富余量（Nm³/h） |供气压力（kPa） |供气温度（℃） |\n|:------|:------|:------|:------|:------|:------|\n| 焦炉煤气量 | @@gaspowergeneration_needsquestionnaire.surplus_gas_cog@@ | @@gaspowergeneration_needsquestionnaire.surplus_maxcog_gas@@ | @@gaspowergeneration_needsquestionnaire.surplus_mincog_gas@@ | @@gaspowergeneration_needsquestionnaire.cog_gas_pressure@@ | @@gaspowergeneration_needsquestionnaire.cog_gas_temperature@@ |\n\n##### 表4、富余蒸汽量参数表(汽源发生处)\n\n| 序号 |蒸汽来源 |流量（t/h） |压力（MPa） |温度（℃） |\n|:------|:------|:------|:------|:------|\n| 1 |转炉 |@@gaspowergeneration_needsquestionnaire.converter_flow@@ |@@gaspowergeneration_needsquestionnaire.converter_pressure@@  |@@gaspowergeneration_needsquestionnaire.converter_temperature@@ |\n| 2 |烧结余热回收 |@@gaspowergeneration_needsquestionnaire.heat_recovery_flow@@ |@@gaspowergeneration_needsquestionnaire.heat_recovery_pressure@@ |@@gaspowergeneration_needsquestionnaire.heat_recovery_temperature@@ |\n| 3 |加热炉 |@@gaspowergeneration_needsquestionnaire.furnace_flow@@ |@@gaspowergeneration_needsquestionnaire.furnace_pressure@@ |@@gaspowergeneration_needsquestionnaire.furnace_temperature@@ |\n| 4 |其他 |@@gaspowergeneration_needsquestionnaire.steam_other_flow@@ |@@gaspowergeneration_needsquestionnaire.steam_other_pressure@@ |@@gaspowergeneration_needsquestionnaire.steam_other_temperature@@ |\n| 注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |\n\n##### 表5、高炉煤气成分含量表（成分有波动，下述成分取值为平均值）\n\n| 高炉煤气成分 |含量 |含量 |\n|:------|:------|:------|\n| CO |% |@@gaspowergeneration_needsquestionnaire.furnace_co_content@@ |\n| CO2 |% |@@gaspowergeneration_needsquestionnaire.furnace_co2_content@@ |\n| CH4 |% |@@gaspowergeneration_needsquestionnaire.furnace_ch4_content@@ |\n| N2 |% |@@gaspowergeneration_needsquestionnaire.furnace_n2_content@@ |\n| H2 |% |@@gaspowergeneration_needsquestionnaire.furnace_h2_content@@ |\n| O2 |% |@@gaspowergeneration_needsquestionnaire.furnace_o2_content@@ |\n| H2O |% |@@gaspowergeneration_needsquestionnaire.furnace_h2o_content@@ |\n| CmHm |% |@@gaspowergeneration_needsquestionnaire.furnace_cmhn_content@@ |\n| H2S |% |@@gaspowergeneration_needsquestionnaire.furnace_h2s_content@@ |\n| 低位发热量 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.furnace_low_heating@@ |\n| 高位发热值 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.furnace_high_heating@@ |\n\n##### 表6、转炉煤气成分含量表（成分有波动，下述成分取值为平均值）\n\n| 转炉煤气成分 |含量 |含量 |\n|:------|:------|:------|\n| CO |% |@@gaspowergeneration_needsquestionnaire.converter_co_content@@ |\n| CO2 |% |@@gaspowergeneration_needsquestionnaire.converter_co2_content@@ |\n| CH4 |% |@@gaspowergeneration_needsquestionnaire.converter_ch4_content@@ |\n| N2 |% |@@gaspowergeneration_needsquestionnaire.converter_n2_content@@ |\n| H2 |% |@@gaspowergeneration_needsquestionnaire.converter_h2_content@@ |\n| O2 |% |@@gaspowergeneration_needsquestionnaire.converter_o2_content@@ |\n| H2O |% |@@gaspowergeneration_needsquestionnaire.converter_h2o_content@@ |\n| CmHm |% |@@gaspowergeneration_needsquestionnaire.converter_cmhn_content@@ |\n| H2S |% |@@gaspowergeneration_needsquestionnaire.converter_h2s_content@@ |\n| 低位发热量 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.converter_low_heating@@ |\n| 高位发热值 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.converter_high_heating@@ |\n\n##### 表7、焦炉煤气成分含量表（成分有波动，下述成分取值为平均值）\n\n| 焦炉煤气成分 |含量 |含量 |\n|:------|:------|:------|\n| CO | |@@gaspowergeneration_needsquestionnaire.coke_co_content@@ |\n| CO2 | |@@gaspowergeneration_needsquestionnaire.coke_co2_content@@ |\n| CH4 | |@@gaspowergeneration_needsquestionnaire.coke_ch4_content@@ |\n| N2 | |@@gaspowergeneration_needsquestionnaire.coke_n2_content@@ |\n| H2 | |@@gaspowergeneration_needsquestionnaire.coke_h2_content@@ |\n| O2 | |@@gaspowergeneration_needsquestionnaire.coke_o2_content@@ |\n| H2O | |@@gaspowergeneration_needsquestionnaire.coke_h2o_content@@ |\n| CmHm | |@@gaspowergeneration_needsquestionnaire.coke_cmhn_content@@ |\n| H2S | |@@gaspowergeneration_needsquestionnaire.coke_h2s_content@@ |\n| 低位发热量 | |@@gaspowergeneration_needsquestionnaire.coke_low_heating@@ |\n| 高位发热值 | |@@gaspowergeneration_needsquestionnaire.coke_high_heating@@ |\n\n#####  综上所述，针对目前厂区富余的余热、余汽资源，我公司根据多年的煤气发电工程建设及设计经验，计划建设概况如下：\n##### 项目名称：(手动输入)\n##### 建设地址：(手动输入)\n##### 建设规模：(手动输入)\n##### 建设方式：(手动输入)\n##### 承包内容：项目范围内的工程设计、设备成套供货、设备安装调试、工程验收及保质期服务工作；\n##### 设计理念：秉承经济、实用、可靠、合理、低成本建设、低投入运行设计理念。\n##### 工程质量：达到国家施工验收规范合格标准；设备制造质量应保证其达到总承包协议书技术附件即 (手动输入) 的要求，保证设计的合理性，设备制造质量应保证其可靠性，购置的标准设备应为国家或行业认可的成熟定型产品;所选用的工程材料、构建必须满足国家质量检验标准和设计规范的要求。安装工程质量应该保证质量合格、安全可靠；设计、施工安装、设备及材料、试车及验收等都应满足和符合现行国家及行业相关规范、规程和标准的要求（双方另有约定的除外）。\n##### 主要经济技术指标如下：\n\n|  |  |  |  |  |\n|:------|:------|:------|:------|:------|\n| 〔1〕 | 抽凝工况热耗率 | qc | kJ/(kW.h) | @@gaspowergeneration_economic_indicators.smoke_heat_consumption_rate@@ |\n| 〔2〕 | 纯凝工况热耗率 | qn | kJ/(kW.h) | @@gaspowergeneration_economic_indicators.heat_consumption_rate@@ |\n| 〔3〕 | 抽凝工况汽耗率 | dc | kg/(kW.h) | @@gaspowergeneration_economic_indicators.smoke_steam_consumption_rate@@ |\n| 〔4〕 | 纯凝工况汽耗率 | dn | kg/(kW.h) | @@gaspowergeneration_economic_indicators.steam_consumption_rate@@ |\n| 〔5〕 | 机组年利用小时数 | Ha | h | @@gaspowergeneration_economic_indicators.annual_useage_hours@@ |\n| 〔6〕 | 机组年供热小时数 | T | h | @@gaspowergeneration_economic_indicators.annual_heat_hours@@ |\n| 〔7〕 | 年供热量 | Qa | GJ/a | @@gaspowergeneration_economic_indicators.annual_heat_supply@@ |\n| 〔8〕 | 年发电量 | Pa | 万kW.h | @@gaspowergeneration_economic_indicators.annual_power_generation@@ |\n| 〔9〕 | 厂用电率 | ζ | % | @@gaspowergeneration_economic_indicators.plant_electricity_consumption@@ |\n| 〔10〕 | 年供电量 | Pag | 万kW.h | @@gaspowergeneration_economic_indicators.annual_power_supply@@ |\n| 〔11〕 | 锅炉效率 | ηg | % | @@gaspowergeneration_economic_indicators.boiler_efficiency@@ |\n| 〔12〕 | 管道效率 | ηp | % | @@gaspowergeneration_economic_indicators.pipeline_efficiency@@ |\n| 〔13〕 | 抽凝工况发电标煤耗率 | bcf | kg/h | @@gaspowergeneration_economic_indicators.smoke_power_coal_consumption@@ |\n| 〔14〕 | 纯凝工况发电标煤耗率 | bnf | kg/h | @@gaspowergeneration_economic_indicators.power_coal_consumption@@ |\n| 〔15〕 | 抽凝工况供电标煤耗率 | bcg | g/(kW.h) | @@gaspowergeneration_economic_indicators.smoke_supply_coal_consumption@@ |\n| 〔16〕 | 纯凝工况供电标煤耗率 | bng | g/(kW.h) | @@gaspowergeneration_economic_indicators.supply_coal_consumption@@ |\n| 〔17〕 | 全年平均热电比 | βp | % | @@gaspowergeneration_economic_indicators.annual_average_thermoelectric_ratio@@ |\n| 〔18〕 | 抽凝工况全厂热效率 | ηcr | % | @@gaspowergeneration_economic_indicators.smoke_heat_efficiency@@ |\n| 〔19〕 | 纯凝工况全厂热效率 | ηnr | % | @@gaspowergeneration_economic_indicators.heat_efficiency@@ |","id":"j1_2"},{"content":"","id":"j1_3"},{"content":"","id":"j1_4"},{"class":["1"],"content":"","id":"j1_5"},{"content":"","id":"j1_6"},{"content":"","id":"j1_7"},{"class":["1","j1_5"],"content":"##### （请手动输入该部分内容）#####","id":"j1_8"},{"class":["1","j1_5","j1_8"],"content":"##### 总承包方承担本工程设计、采购及施工的工作范围包括：(请手动输入) 的初步设计、施工图设计、成套设备采购供货；总承包方负责项目范围内的所有设计内容，主要包含以下方面：\n##### ①发电项目的总图设计；\n##### ②项目范围内的系统工艺、工艺流程及工艺管道设计；\n##### ③锅炉及其辅机设计；\n##### ④热力系统设备管道设计；\n##### ⑤煤气、蒸汽、风、水、电、气的系统设计；\n##### ⑥汽轮发电机组及辅机设计；\n##### ⑦主厂房、设备基础、配电及控制室设计；\n##### ⑧化学水系统及厂房的设计；\n##### ⑨循环水系统的设计（含自然通风冷却塔）；\n##### ⑩项目范围内的控制系统的设计；\n##### ⑪项目范围内的发配电系统的设计；\n##### ⑫项目范围内的检修平台和操作平台、起重设备选用设计；\n##### ⑬项目范围内建筑通风、保温、防腐、消防、给排水、暖通、通讯、照明及防雷接地等设计；\n##### ⑭项目范围内各类设备基础设计；\n##### ⑮未提及的项目范围内其他设计。","id":"j1_9"},{"class":["1","j1_5","j1_8"],"content":"##### 项目范围内主辅设备、电控、自控成套设备及单体设备采购及供货。","id":"j1_10"},{"class":["1","j1_5","j1_8"],"content":"##### ①锅炉及其辅助设备的安装调试；\n##### ②汽轮发电机组及辅助设备的安装调试；\n##### ③化学水设备、管道安装与调试；\n##### ④循环水系统安装调试；\n##### ⑤接点内煤气、蒸汽、风、水、电、气系统调试；\n##### ⑥电气及自控设备安装调试，包含电气施工材料、电缆、电缆桥架、软件编程；\n##### ⑦工程接点范围内保温工程、设备及管道防腐、耐磨处理和外部油漆、保温；\n##### ⑧未提及的项目范围内其他设备安装及调试。","id":"j1_11"},{"class":["1","j1_5","j1_8"],"content":"##### ①工程项目相关报批，如项目报批、环评、开工备案、电力并网等，项目工程监理；\n##### ②(请手动输入) 范围内的三通一平及绿化等；\n##### ③负3米以下（包括负3米）桩基工程及桩基检测，土建桩基切桩头和灌注钢筋混凝土撞头；地上、地下障碍物的拆迁清除。；\n##### ④总图范围外集水井、排水管；\n##### ⑤开挖石块、建筑垃圾等由总承包方运至发包人指定的免费地点(距离项目建设地点不超过5KM)；\n##### ⑥调试期所有的能源介质（水、电、气、汽、煤气、点火燃料）药品、试剂等由发包人无偿提供；\n##### ⑦水质化验全部设备、设施；\n##### ⑧并网相关手续办理和费用由发包人全权负责（总承包方配合提供相关资料）；\n##### ⑨生产工器具(设备自带专用工具除外）、工具、办公家具，工人安全防护、劳保用品、警示牌标（煤气、电、气、水、道路）等；\n##### ⑩施工过程中如发现受国家法律保护的历史文物、文化遗迹等，由此发生的费用和对工程进度产生的影响由发包人承担。","id":"j1_12"},{"class":["1","j1_5","j1_8"],"content":"##### 电站建筑工程的施工：包括全站的建筑、结构、室内外生产、生活给排水、阀门检查井、化粪池、火灾报警、室内外消防、采暖、通风、照明、空调、通讯、建筑物防雷接地、设备二次灌浆、管道支架、钢平台等；\n##### ①厂房土建工程施工，包含建（构）筑、通风、消防、火灾报警、给排水、暖通、照明（含应急照明）、接地网（接地极）及防雷接地（含设备采购、安装）；\n##### ②主辅系统设备基础及二次灌浆；\n##### ③钢筋混凝土结构锅炉烟囱高度暂定60m（具体高度根据详设确定）及烟风道的施工；\n##### ④(请手动输入该部分内容) ；\n##### ⑤主厂房行车的供货和安装（含吊车梁、滑线、钢轨）；\n##### ⑥项目范围内汽、水、烟风管道支吊架的基础施工，支吊架的供货、安装。\n##### ⑦所有预埋件及钢结构护栏的供货和安装，平台、扶手、走道及爬梯、辅助通道；\n##### ⑧厂区埋地管道基础、管沟开挖和回填；\n##### ⑨电缆沟(电缆通廊)及沟盖板；\n##### ⑩电站范围内的道路施工及围墙；","id":"j1_13"},{"class":["1","j1_5"],"content":"##### 各种能源介质的交接点位置如下：总承包方提供所有公辅介质进发电厂区控制阀门和介质计量表；\n##### ①煤气管道由总承包方接至发包人指定接点；\n##### ②低压蒸汽管道总承包方接至发包人指定接点；\n##### ③冷凝水送至加热炉、转炉、烧结处；\n##### ④氮气、天然气由总承包方接至发包人指定接点；\n##### ⑤电站所用动力电源为双回路供电，其中动力电源由发包人送至本项目总承包方高压受电柜上端子；并网电源由总承包方送至上级110KV变电所10KV一段（电缆、桥架、电缆沟等由总承包方负责）；受电柜至电站的电缆、光纤、保护模块的采购等工作由总承包方负责，受电柜由总承包方负责；\n##### ⑥除盐水系统由总承包方统一负责，原水由发包人供接至电站围墙外1m（总承包方配阀），其余由总承包方负责；\n##### ⑦电站生活用水、工业水由发包人供接电站围墙外1m并（总承包方配阀），其余由总承包方负责；\n##### ⑧电站DCS系统与生产线控制系统之间通讯的网络分界点设在煤气电站DCS系统的网络连接口，总承包方负责预留以太网接口。","id":"j1_14"},{"class":["1"],"content":"##### 所有设计文件、供货的材料和设备应符合相关的中国标准、规定、规范及法律，或者符合中国钢铁企业余热利用的相关标准、规定、规范及法律：\n##### 《小型火力发电厂设计规范》GB50049-2011\n##### 《火力发电厂设计技术规程》（DL5000-2000）\n##### 《火力发电厂采暖通风与空气调节设计技术规定》DL/T5035-94\n##### 《火力发电厂汽水管道设计技术规定》DL/T5054-1996\n##### 《火力发电厂保温油漆技术规范》DL/T5072-2007\n##### 《火力发电厂建筑设计规程》DL/T5094-1999\n##### 《火力发电厂和变电所照明设计技术规定》DLGJ56-95\n##### 《火力发电厂烟风煤粉管道设计技术规程》DL/T5121-2000\n##### 《工业企业煤气安全规程》 （GB6222-2005）\n##### 《工业企业噪声控制设计规范》（GBJ87-85）\n##### 《建筑设计防火规范》（GB50016-2006）\n##### 《建筑物防雷设计规范》（GB50057-94）\n##### 《爆炸和火灾危险环境电力装置设计规范》（GB50058-92）\n##### 《电力配备典型消防规程》（DL5027-93）\n##### 《火力发电厂总图运输设计技术规定》（DL/T5032-2005）\n##### 《火力发电厂与变电所设计防火规范》（GB50229-96）\n##### 《采暖通风与空气调节设计技术规定》（DJ/T5035-95）\n##### 《动力机器基础设计规范》（GB50040-1996）\n##### 《火灾自动报警系统设计规范》（GB50116-98）；\n##### 《蒸汽锅炉安全技术监察规程》（劳部发[1996]276号）\n##### 《电力建设施工及验收技术规范》（建筑工程篇）（SDJ69-1987）；\n##### 《电力建设施工及验收技术规范》(锅炉机组篇)（DL/T-5047-95）；\n##### 《电力建设施工及验收技术规范》(汽轮机机组篇)（DL5011-92）；\n##### 《电气装置安装工程施工及验收规范》GB50254～GB50259-96\n##### 《火力发电厂建设工程启动试运及验收规程》（2009年版）","id":"j1_15"},{"class":["1"],"content":"","id":"j1_16"},{"class":["1","j1_16"],"content":"##### (请手动输入该部分内容)","id":"j1_17"},{"class":["1","j1_16"],"content":"##### 1. 工况条件\n##### 1.1自然条件\n##### 1.1.1 温度：\n##### 1.1.1.1年平均气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a@@ ℃\n##### 1.1.1.2夏季平均温度：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a_summer@@ ℃\n##### 1.1.1.3冬季平均温度：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a_winter@@ ℃\n##### 1.1.1.4最冷月一月平均气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a_cold@@ ℃\n##### 1.1.1.5最热月七月平均气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a_hot@@ ℃\n##### 1.1.1.6年极端最高气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_extreme_h@@ ℃\n##### 1.1.1.7年极端最低气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_extreme_l@@ ℃\n##### 1.1.2  湿度：\n##### 1.1.2.1夏季平均相对湿度：@@gaspowergeneration_needsquestionnaire.relative_humidity_a_summer@@ %\n##### 1.1.2.2冬季平均相对湿度：@@gaspowergeneration_needsquestionnaire.relative_humidity_a_winter@@ %\n##### 1.1.2.3年平均相对湿度：@@gaspowergeneration_needsquestionnaire.relative_humidity_a@@ %\n##### 1.1.2.4最高相对湿度：@@gaspowergeneration_needsquestionnaire.relative_humidity_extreme_h@@ %\n##### 1.1.3 大气压力\n##### 1.1.3.1年平均：@@gaspowergeneration_needsquestionnaire.atmosphere_pressure_a@@ kPa\n##### 1.1.3.2夏季平均气压：@@gaspowergeneration_needsquestionnaire.atmosphere_pressureSummer@@ kPa\n##### 1.1.3.3冬季平均气压：@@gaspowergeneration_needsquestionnaire.atmosphere_pressureWinter@@ kPa\n##### 1.1.3.4海拔高度： @@gaspowergeneration_needsquestionnaire.above_sea_level@@ m\n##### 1.1.4 风速及风压：\n##### 1.1.4.1年平均风速：@@gaspowergeneration_needsquestionnaire.outside_wind_speed_a@@ m/s\n##### 1.1.4.2全年最大风速：@@gaspowergeneration_needsquestionnaire.outside_wind_speed_extreme_h@@ m/s\n##### 1.1.5抗震能力：根椐《建筑抗震设计规范》GB50011-2010.该地区的地震设防烈度为@@gaspowergeneration_needsquestionnaire.seismic_fortification_intensity_a@@ 度，设计基本地震加速度值为@@gaspowergeneration_needsquestionnaire.design_earthquake_acceleration@@ g","id":"j1_18"},{"class":["1","j1_16"],"content":"##### 总承包方根据建构筑物、设备基础设计前荷载，给发包人提供详勘测布点图，发包人组织详勘并在10个工作日间将详勘资料以电子版形式反馈给总承包方，由总承包方根据详勘进行设计。","id":"j1_19"},{"class":["1","j1_16"],"content":"##### 根据《建筑抗震设计规范》附录A的划分要求，本工程抗震设防烈度为@@gaspowergeneration_needsquestionnaire.seismic_fortification_intensity_a@@ 度，设计地震分组为第二组，设计地震基本加速度为@@gaspowergeneration_needsquestionnaire.design_earthquake_acceleration@@ g。本工程按规范进行设计。","id":"j1_20"},{"class":["1","j1_16"],"content":"##### 本工程建设场地位于(请手动输入)。","id":"j1_21"},{"class":["1","j1_16"],"content":"","id":"j1_22"},{"class":["1","j1_16"],"content":"##### (请手动输入)需要发包人提供高压保安/启动电源，装置能力要满足电站系统的启动、运行及保安用电。","id":"j1_23"},{"class":["1","j1_16"],"content":"##### 利用原厂管网提供水源,发包方负责施工，接至电站围墙外一米处。电站的正常工业新水补水量约为@@gaspowergeneration_circulating_water_system.supply_water_amount+ gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h (包括除盐水站的原水供水)。\n##### 本工程按接口处供水水压符合以下要求进行设计：\n##### 生产新水≥0.30MPa\n##### 生活给水≥0.25MPa\n##### 消防水≥0.30MPa","id":"j1_24"},{"class":["1","j1_16"],"content":"##### 电站的氮气主要供煤气快切阀、电视摄像机镜头、仪表气动阀、煤气管吹扫之用，为此，在主厂房设氮气储气罐一个，气源点由发包人提供,压力需≥0.60MPa，正常耗氮量小于10m³/h。","id":"j1_25"},{"class":["1","j1_16"],"content":"##### 项目主要消耗药品如氯化钠、磷酸三钠等，由发包人统一自行采购配给（总承包方提名称、相关参数、第一次使用数量及使用周期）。","id":"j1_26"},{"content":"","id":"j1_27"},{"content":"","id":"j1_28"},{"class":["1"],"content":"","id":"j1_29"},{"class":["1","j1_29"],"content":"##### (请手动输入该部分内容)","id":"j1_30"},{"class":["1","j1_29"],"content":"##### 本项目属于回收利用低热值高炉煤气，高效进行清洁能源生产的工程项目。项目投产后，将创造良好的经济效益、社会效益和环保效益。","id":"j1_31"},{"class":["1","j1_29"],"content":"##### 1)热力循环系统\n##### 煤气锅炉所产生的过热蒸汽作为主蒸汽进入汽轮机，蒸汽管网富裕的饱和蒸汽作为补汽进入汽轮机发电做功，做功后的蒸汽进入凝汽器凝结成水，凝结水经凝结水泵加压后分别送入煤气锅炉和低压产汽点。\n##### 2)建设规模\n##### 根据发包人富余的煤气资源，锅炉理论计算额定情况可产@@gaspowergeneration_boiler_of_pts.steam_output@@ t/h高温高压蒸汽，综合考虑煤气波动，机组选型为(手动输入)t/h高温高压煤气锅炉配(手动输入)MW高温高压补汽凝汽式汽轮机组+(手动输入)MW发电机组。\n##### 3)机组主要技术指标\n| 序号 |项目 |单位 |数值 |备注 |\n|:------|:------|:------|:------|:------|\n| 1 |锅炉额定蒸发量 |t/h |(请手动输入) | |\n| 2 |锅炉额定计算产汽量 |t/h |@@gaspowergeneration_boiler_of_pts.steam_output@@ | |\n| 3 |锅炉最大产汽量 |t/h |(请手动输入) | |\n| 3 |汽轮机补汽流量 |t/h |@@gaspowergeneration_turbine_of_pts.e_exhaust_point_flow@@ | |\n| 4 |装机功率 |kW |@@gaspowergeneration_turbine_of_pts.e_steam_extraction_select@@ | |\n| 5 |理论计算发电量 |kW |@@gaspowergeneration_turbine_of_pts.e_steam_extraction@@ | |\n| 6 |厂用电率 |% |暂无 | |\n| 7 |年利用小时 |h |暂无 | |\n| 8 |年发电量 |kW.h/a |暂无 | |\n| 9 |年供电量 |kW.h/a |暂无 | |\n| 10 |年节约标准煤量 |t/a |暂无 | |\n##### 4)主要设备参数\n##### 锅炉\n\n| 序号 |内容 |单位 |数值 |\n|:------|:------|:------|:------|\n| 1 |型号 | |(请手动输入)|\n| 2 |额定蒸发量 | |(请手动输入) |\n| 3 |额定蒸汽压力 |MPa（G） |@@gaspowergeneration_boiler_of_pts.superheated_steam_outlet_pressure@@ |\n| 4 |额定蒸汽温度 |℃ |@@gaspowergeneration_boiler_of_pts.superheated_steam_temperature@@ |\n| 5 |给水温度 |℃ |@@gaspowergeneration_boiler_of_pts.boiler_feed_water_temperature@@ |\n| 6 |排烟温度 |℃ |(请手动输入) |\n| 7 |锅炉效率 | |@@gaspowergeneration_boiler_of_pts.boiler_efficiency@@ |\n| 8 |燃料 | |(请手动输入) |\n##### 汽轮机\n\n| 序号 |内容 |单位 |数值 |\n|:------|:------|:------|:------|\n| 1 |型号 | |(请手动输入) |\n| 2 |形式 | |(请手动输入) |\n| 3 |额定功率 |MW |@@gaspowergeneration_turbine_of_pts.e_steam_extraction_select@@ |\n| 4 |额定转速 |r/min |3000 |\n| 5 |转向 | |顺时针 |\n| 6 |主蒸汽流量 |t/h |@@gaspowergeneration_turbine_of_pts.e_steam_flow@@ |\n| 7 |主蒸汽压力 |MPa（A） |@@gaspowergeneration_turbine_of_pts.e_steam_pressure@@ |\n| 8 |主蒸汽温度 |℃ |@@gaspowergeneration_turbine_of_pts.e_steam_temperature@@ |\n| 9 |补汽流量 |t/h |-- |\n| 10 |补汽压力 |MPa（A） |-- |\n| 11 |补汽温度 |℃ |-- |\n| 12 |凝气压力 |kPa (A) |-- |\n\n##### 发电机\n\n| 序号 |内容 |单位 |数值 |\n|:------|:------|:------|:------|\n| 1 |型号 | |(手动输入) |\n| 2 |额定功率 |kW |@@gaspowergeneration_turbine_of_pts.e_steam_extraction_select@@ |\n| 3 |额定功率因数 | |0.8 |\n| 4 |额定频率 |Hz |50 |\n| 5 |额定转速 |r/min |3000 |\n| 6 |额定电压 |kV |(请手动输入) |\n| 7 |冷却方式 | |(请手动输入) |\n| 8 |励磁系统 | |(请手动输入) |","id":"j1_32"},{"class":["1","j1_29"],"content":"","id":"j1_33"},{"class":["1","j1_29","j1_33"],"content":"##### ⑴燃料来源\n##### 锅炉所需高炉、转炉煤气来自发包人煤气管网。\n##### ⑵燃料特性（由发包人提供）\n##### 1.高炉煤气成份（成分有波动，下述成分取值为平均值）\n\n| 高炉煤气成分 |含量 |含量 |\n|:------|:------|:------|\n| CO |% |@@gaspowergeneration_needsquestionnaire.furnace_co_content@@ |\n| CO2 |% |@@gaspowergeneration_needsquestionnaire.furnace_co2_content@@ |\n| CH4 |% |@@gaspowergeneration_needsquestionnaire.furnace_ch4_content@@ |\n| N2 |% |@@gaspowergeneration_needsquestionnaire.furnace_n2_content@@ |\n| H2 |% |@@gaspowergeneration_needsquestionnaire.furnace_h2_content@@ |\n| O2 |% |@@gaspowergeneration_needsquestionnaire.furnace_o2_content@@ |\n| H2O |% |@@gaspowergeneration_needsquestionnaire.furnace_h2o_content@@ |\n| CmHm |% |@@gaspowergeneration_needsquestionnaire.furnace_cmhn_content@@ |\n| H2S |% |@@gaspowergeneration_needsquestionnaire.furnace_h2s_content@@ |\n| 低位发热量 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.furnace_low_heating@@ |\n| 高位发热值 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.furnace_high_heating@@ |\n\n##### 2.转炉煤气成份（成分有波动，下述成分取值为平均值）\n\n| 转炉煤气成分 |含量 |含量 |\n|:------|:------|:------|\n| CO |% |@@gaspowergeneration_needsquestionnaire.converter_co_content@@ |\n| CO2 |% |@@gaspowergeneration_needsquestionnaire.converter_co2_content@@ |\n| CH4 |% |@@gaspowergeneration_needsquestionnaire.converter_ch4_content@@ |\n| N2 |% |@@gaspowergeneration_needsquestionnaire.converter_n2_content@@ |\n| H2 |% |@@gaspowergeneration_needsquestionnaire.converter_h2_content@@ |\n| O2 |% |@@gaspowergeneration_needsquestionnaire.converter_o2_content@@ |\n| H2O |% |@@gaspowergeneration_needsquestionnaire.converter_h2o_content@@ |\n| CmHm |% |@@gaspowergeneration_needsquestionnaire.converter_cmhn_content@@ |\n| H2S |% |@@gaspowergeneration_needsquestionnaire.converter_h2s_content@@ |\n| 低位发热量 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.converter_low_heating@@ |\n| 高位发热值 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.converter_high_heating@@ |\n\n##### ⑶燃烧系统设施\n##### 锅炉燃烧用的高炉煤气由外部煤气管网接入锅炉房，经锅炉煤气燃烧器送入炉膛燃烧。\n##### 主厂房进口煤气总管上设有电动硬密封蝶阀、电动硬密封盲板阀、气动快速切断阀、电动调节阀、压力检测装置、温度检测装置、流量检测装置，在锅炉燃烧器入口管上设有快速切断阀门、点火探测装置、失压保护装置，煤气管道的末端设有放散装置，按煤气管道规范设排水装置、补偿装置，管道上设有吹扫装置。\n##### 锅炉设有锅炉炉膛安全监控和熄火保护系统，保障锅炉安全、稳定运行。\n##### 锅炉采用平衡通风方式，空气由送风机经空气预热器预热后送至锅炉两侧热风总管，再经燃烧器进入炉膛。\n##### 锅炉烟气由炉后烟道，经一台吸风机送入烟囱，再由烟囱排入大气，锅炉采用一个钢筋混凝土烟囱，再由烟囱排入大气。\n##### ⑷燃烧系统\n##### 锅炉采用平衡通风，(手动输入) 以满足锅炉各种工况下的需要。\n##### 锅炉点火：\n##### (手动输入)，点火系统设施设二级点火系统。即现场手动点火及PLC自动点火。二级点火均采用高压电点火。\n##### ⑸锅炉排污系统\n##### 锅炉设一套连续排污系统，连续排污水通过连续排污扩容器扩容后，再排入定期排污扩容器。\n##### 连续排污扩容器选用@@gaspowergeneration_boiler_auxiliaries.c_specifications@@ ，连续排污扩容的蒸汽分别接入除氧器，排污水排入定期排污扩容器。\n##### 设定期排污扩容器@@gaspowergeneration_boiler_auxiliaries.r_specifications@@ ，能满足锅筒紧急放水量（最大）及连续排污的要求。\n##### ⑹疏放水系统\n##### 主厂房疏放水系统设疏水扩容器，疏水箱容积@@gaspowergeneration_boiler_auxiliaries.s_volume@@ m3和2台疏水泵。主蒸汽管道的启动疏水和经常疏水、低压蒸汽管道的经常疏水，锅炉的疏水均分别接入疏水扩容器。除氧器的溢放水直接排入疏水箱。疏水箱的出水经疏水泵输送至除氧器。\n##### 汽轮发电机组的疏放水系统均设疏水膨胀箱，其疏水接入凝汽器。低压加热器疏水采用自流的方式，送入凝汽器。\n##### ⑺加药取样系统\n##### 为防止锅炉内钙镁盐类的沉积结垢，维持炉水中的磷酸盐浓度，系统设自动磷酸盐加药装置。\n##### 锅炉的过热蒸汽、饱和蒸汽、炉水、给水均设有取样装置，进行定期检验分析，以监察汽水质量。","id":"j1_34"},{"class":["1","j1_29","j1_33"],"content":"##### ⑴主蒸汽系统\n##### 补汽凝汽式汽轮发电机组所需蒸汽由(手动输入)t/h煤气锅炉和低压蒸汽管网供应，主补蒸汽系统采用(手动输入)系统。管道采用高压锅炉用无缝钢管（GB5310），所有蒸汽管道阀门均采用焊接阀门。\n##### ⑵主给水系统\n##### 主给水系统采用(手动输入)系统。锅炉给水温度为(手动输入)℃。煤气锅炉主给水系统设两台电动给水泵，一用一备运行；管道采用锅炉用无缝钢管（GB3087），给水操作台设有调节阀，作为启动、低负荷、额定负荷调节用。\n##### 汽轮机设3段非调整抽汽。一段抽汽接至除氧器，二段接至1#低压加热器, 三段接至2#低压加热器。为防止加热器水位过高而倒流入汽轮机，在各段抽汽管道分别设有止回阀。\n##### 锅炉给水经凝结水泵后由低压给水泵外供15-25t/h水至低压管网。\n##### ⑶凝结水系统\n##### 汽轮机配凝汽器1台，(手动输入)，汽机的凝结水由凝结水泵打出，经汽封加热器和低压加热器送入除氧器。低压加热器的疏水，通过低加疏水器打入主凝结水系统。\n##### 汽轮机选用凝结水泵两台，一用一备。\n##### ⑷抽气系统\n##### 汽轮发电机组的抽气系统设射水抽气器。\n##### ⑸循环水系统\n##### 汽轮机的凝汽器冷却水采用循环冷却系统（@@gaspowergeneration_circulating_water_system.cooling_tower_selected_name@@），凝汽器进、出水管各两根，进、出水管之间设有联络管。\n##### 机组的冷油器、空气冷却器等的冷却水接自凝汽器的循环冷却系统。电动给水泵以及油泵等冷却采用工业净循环水。\n#####  ⑹除氧系统\n##### 工程设除氧器及其给水箱一台。除氧器出力为@@gaspowergeneration_boiler_auxiliaries.s_design_flux@@ t/h，给水箱为@@gaspowergeneration_boiler_auxiliaries.s_volume@@ m3，@@gaspowergeneration_boiler_auxiliaries.p_deaerator_pressure@@ Mpa，出水温度为@@gaspowergeneration_turbine_of_pts.i_deoxidize_temperature@@ ℃，能满足最大给水量除氧及存水时间要求。\n##### 除氧器进水大部分来自凝汽器凝结水，少部分补水来自除盐水站。\n##### ⑺油系统\n##### 汽轮发电机组油系统设施有设在汽机机头的主油泵、主油箱、事故油池、高压交流油泵、低压交流油泵、低压直流油泵、冷油器及油管道组成。","id":"j1_35"},{"class":["1","j1_29","j1_33"],"content":"##### 本工程锅炉补给水采用高温高压锅炉补给水质标准及蒸汽管网富裕的饱和蒸汽执行给水质标准（GB/T12145-2008）\n\n| 项目 | 单位 | 数值 |\n|:------|:------|:------|\n| 硬度 | µmol/l | ≈0 |\n| 电导率 | µs/cm | ≤0.2 |\n| 二氧化硅 | µg/l | ≤20 |\n##### \n##### (1)锅炉补给水系统出力的确定\n##### 1)锅炉总蒸发量：@@gaspowergeneration_boiler_auxiliaries.m_boiler_evaporation@@ t/h\n##### 2)厂内正常水汽损失（考虑锅炉蒸汽和低压饱和蒸汽（25.5t/h)）@@gaspowergeneration_boiler_auxiliaries.m_steamwater_cycle_loss@@ t/h\n##### 3)锅炉排污损失（考虑锅炉蒸汽和低压饱和蒸汽（25.5t/h)）：@@gaspowergeneration_boiler_auxiliaries.m_pollution_loss@@ t/h\n##### 4)机组启动或事故时增加的损失（按最大一台锅炉蒸发量的10%计）：@@gaspowergeneration_boiler_auxiliaries.m_increase_loss@@ t/h\n##### 5)正常补给水量：@@gaspowergeneration_boiler_auxiliaries.m_boiler_normal_watersupply@@ t/h\n##### 6)机组启动或事故时补给水量：@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h\n##### \n##### (2)补给水处理系统出力\n##### 由上述计算可以看出，正常情况下所需除盐水约@@gaspowergeneration_boiler_auxiliaries.m_boiler_normal_watersupply@@ t/h，机组启动或事故时所需除盐水约@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h。\n##### 考虑到设备运行效率和低压管网换水情况，本化水站的系统出力按@@gaspowergeneration_boiler_auxiliaries.m_boiler_watersupply_specifications@@进行设计，机组起动或事故时补给水，可以通过调节流量和室外的除盐水箱的水位来满足要求。\n##### 本电站系统设置1座@@gaspowergeneration_boiler_auxiliaries.s_volume@@ m3的除盐水箱，再通过补水泵供至除氧头、凝汽器等用水点。\n##### \n##### (3)化学除盐水系统的确定\n##### 除盐水原水是工业用水，浊度比较大，详见水质报告。\n##### 除盐水处理系统运行方案初定为：@@gaspowergeneration_boiler_auxiliaries.desalted_water_tech_name@@。最终工艺方案在发包人提供全水质分析报告后确定。\n##### 根据水质情况，以下系统处理方案能满足电厂要求。\n##### 锅炉补给水系统工艺流程：\n##### gpglogic[1]\n##### gpglogic[2]\n##### \n##### (4)自动控制水平\n##### 除盐水采用PLC自动控制,水泵、阀门为远程/机旁控制启停；过滤器为自动反洗。\n##### 除盐水站控制系统在中控室设监视画面。","id":"j1_36"},{"class":["1","j1_29","j1_33"],"content":"##### 1.水量及水质要求\n##### （1）用水量\n##### 电站生产总补充用水量：@@gaspowergeneration_circulating_water_system.supply_water_amount@@ t/h\n##### 生活水：(手动输入)m3/h\n##### 根据当地气象条件，经循环供水系统初步计算，夏季循环水冷却倍率采用@@gaspowergeneration_circulating_water_system.circulation_ratio_summer@@ 倍，冬季采用@@gaspowergeneration_circulating_water_system.circulation_ratio_winter@@ 倍，\n##### 循环供水系统水量见下表：\n\n| 机组容量 |凝汽量(t/h) |循环冷却水量(m3 /h) |循环冷却水量(m3 /h) |辅机冷却水量(m3/h) |总循环水量(m3/h) |总循环水量(m3/h) |\n|:------|:------|:------|:------|:------|:------|:------|\n| 机组容量 |凝汽量(t/h) |夏季 |冬季 |辅机冷却水量(m3/h) |夏季 |冬季 |\n| (手动输入) | @@gaspowergeneration_circulating_water_system.steam_exhaust_flux_selected@@ | @@gaspowergeneration_circulating_water_system.circulation_water_flow_summer@@ | @@gaspowergeneration_circulating_water_system.circulation_water_flow_winter@@ | @@gaspowergeneration_circulating_water_system.auxiliary_cooling_water_flow_winter@@ | @@gaspowergeneration_circulating_water_system.total_circulation_water_flow_summer@@ | @@gaspowergeneration_circulating_water_system.total_circulation_water_flow_winter@@ |\n\n##### （2）循环水系统设施、设备\n##### 依据本工程冷却需循环水量要求，本工程建设gpglogic[0]，塔下新建循环水池(手动输入)座，水池旁设置泵房，安装(手动输入)台循环水泵，以保证本工程机组正常运行对循环冷却水的要求。\n##### \t水质稳定：为保证循环水系统的水质稳定，延长设备使用寿命，需由发包人提供水质化验单（水质符合工业用水水质要求GB50050-95），总承包方确定需投加的水质稳定剂的种类及投加量，水质稳定加药设施可根据要求设置。\n##### 循环冷却水补给水量计算结果如下表：\n\n| 项目 |设计水量（m3/h） |实耗水量（m3/h） |\n|:------|:------|:------|\n| 冷却塔蒸发损失 |@@gaspowergeneration_circulating_water_system.evaporation_loss@@ |122 |\n| 冷却塔风吹及飞溅损失 |@@gaspowergeneration_circulating_water_system.wind_blow_loss@@ |25 |\n| 排污及渗漏损失 |@@gaspowergeneration_circulating_water_system.discharge_capacity@@ |35 |\n| 补给水量 |@@gaspowergeneration_circulating_water_system.supply_water_amount@@ |182 |\n\n##### （3）生活饮用水补给水水质应满足《生活饮用水卫生标准》GB5749-2006 的水质指标。其它补给水水质应满足前述相应水质指标表相关要求。\n##### 2.水源\n##### 本项目由发包人供水至电站界区，确保电站用水要求。循环水站需补充新水@@gaspowergeneration_circulating_water_system.supply_water_amount@@ t/h，化学水站考虑排污及处理效率后需补充新水@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h(最大)。所以本工程需补充新水@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply+gaspowergeneration_circulating_water_system.supply_water_amount@@ t/h。\n##### 3.设计的给排水系统\n##### （1）生产给水系统\n##### 汽轮机凝汽器机组等设备为间接冷却回水，其回水仅温度升高,未受其它污染，故采用净循环给水系统。汽轮机机组净循环水由设计的循环水泵房内的循环给水泵组加压供给，凝汽器排出的热水利用余压直接送至冷却塔冷却，经冷却塔冷却后的水，经过回水管，自流入循环水泵房的冷吸水井，整个循环系统的循环水量最大（夏季）为：@@gaspowergeneration_circulating_water_system.total_circulation_water_flow_summer@@ t/h。除盐水系统所需要的原水量为@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h，生产共所需的补充水量为@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply+gaspowergeneration_circulating_water_system.supply_water_amount@@ t/h。\n##### （2）消防给水系统\n##### 电厂需有完善的消防设施，根据消防规范的相关规定，电厂室内消火栓用水量 15L/s，室外消防用水量为 25L/s，消防总用水量为 40L/s。本期工程单独设置消防水系统，由发包方提供水源，本期电站工程负责消防管路以及设施的敷设和安装。\n##### （3）排水系统\n##### 本工程中，水冷系统外排废水不含有毒和有害物质，可就近排入原工厂排水系统。蒸汽管道疏水可就近排放，汽轮机疏水回收利用。分散零星的不能回收的轴承冷却水、设备检修放空水或其它冲洗水，直接就近排入下水道。\n##### 排水系统的设计须结合(手动输入)现有实际排水系统情况进行设计，以保证统一性。","id":"j1_37"},{"class":["1","j1_29","j1_33"],"content":"##### 电缆夹层，发电机小室、加药、取样间、水处理间、化水站等为消除室内余热，夏季设置轴流通风机进行通风换气。主控室和电气间安装空调，通风和空调设施满足工况需求。","id":"j1_38"},{"class":["1","j1_29","j1_33"],"content":"##### 1、总承包界限划分\n##### 1.1、陕鼓负责范围\n##### a、并网电源：\n##### □10KV 并网电源以发电站联络柜端子为界，界内陕鼓负责，界外用户负责。\n##### □35KV 并网电源以升压变压器高压侧35KV联络柜端子为界，界内陕鼓负责，界外用户负责。\n##### □110KV 并网电源以升压变压器高压侧110KV组合开关端子为界，界内陕鼓负责，界外用户负责。\n##### b、启动电源：\n##### 以发电站10KV电源进线柜端子为界，界内陕鼓负责，界外用户负责。\n##### c、微机保护整定计算书。\n##### 1.2、用户负责范围\n#####  a、电源：\n#####  □提供一路10KV高压并网电源和一路10KV启动电源。\n#####  □提供一路35KV高压并网电源和一路10KV启动电源。\n#####  □提供一路110KV高压并网电源和一路10KV启动电源。\n#####  b、并网申报审批工作和发电接入系统。\n##### 2、 电气系统接线方案\n##### □发电机接入系统采用10kV 接线方式，发电机出口采用 10KV 并网，与用户上级变电所10KV出线联络，并网点设置在发电机出线柜和系统联络柜。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。\n##### 各级电压的中性点接地方式：\n##### 10kV 采用中性点不接地方式；\n##### 380V 采用中性点直接接地方式；\n##### 检修和照明共用低压供电络。\n##### □发电机接入系统采用35kV 接线方式，发电机出口电压 10KV，经过10/35KV升压变压器升至35KV，并与用户上级变电所35KV出线联络，并网点设置在升压变压器35KV高压侧。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。\n##### 各级电压的中性点接地方式：\n##### 35KV采用中性点直接接地方式；\n##### 10kV 采用中性点不接地方式；\n##### 380V 采用中性点直接接地方式；\n##### 检修和照明共用低压供电络。\n##### □发电机接入系统采用110kV 接线方式，发电机出口电压 10KV，经过10/110KV升压变压器升至110KV，并与用户上级变电所110KV出线联络，并网点设置在升压变压器110KV高压侧。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。\n##### 各级电压的中性点接地方式：\n##### 110KV采用中性点直接接地方式；\n##### 10kV 采用中性点不接地方式；\n##### 380V 采用中性点直接接地方式；\n##### 检修和照明共用低压供电络。\n\n##### 3、直流系统\n##### 直流负荷包括高压开关操作电源、直流电源、保护控制电源、直流油泵和事故照明等。直流供电的电压为 220V。直流系统采用一套300Ah免维护铅酸蓄电池组。直流电源装置采用微机型相控成套直流电源装置，蓄电池采用 1X300Ah 阀控密封免维护铅酸蓄电池，配置两台逆变器。该直流装置配有微机型直流绝缘在线监测装置，能对所有的直流负荷进行接地故障监测，并能监测直流母线电压信号，在母线欠压、过压或接地时均能发出报警信号。\n\n##### 4、 二次线、继电保护及自动装置\n##### 4.1、 控制、信号及测量\n##### 1）本工程电气控制室与热工控制室合并，并设有电子设备间，布置在运转层。\n##### 2）电气系统控制采用独立控制系统：该方案以后台监控系统为主要监控手段，对电气系统的主要设备进行数据采集、监视及控制，该系统也可通过通讯接口与热控系统连接，在热控系统上对以上系统进行监视。\n##### 3）为保证系统的安全可靠性，操作员站台暂考虑保留下列硬手操：\n##### 发电机断路器紧急跳闸开关\n##### 灭磁开关紧急跳闸开关\n\n##### 4.2、控制保护\n##### 发电机、厂用变压器等重要设备的控制设在集控室内，低压厂用变压器低压侧开关能实现远方控制。发电机的励磁屏、发电机保护屏、公共测控装置、通讯屏等置于集控室内。低压厂用变压器、高压电动机等采用微机综合保护，装设在就地高压开关柜上。在厂用低压配电装置工作电源和备用电源之间设有备用电源自投装置，当工作电源故障或消失时，备用电源自动/手动投入。\n##### 微机综合保护装置含：发电机保护装置、联络线保护装置、低压厂用变压器保护装置、高压电动机保护装置及后台监控系统等。继电保护按国标 GB/T 50062-2008 “电力装置的继电保护和自动装置设计规范”要求配置：\n##### a. 发电机保护：\n##### ● 发电机失步解列保护\n##### ● 纵差保护\n##### ● 复合电压过电流保护\n##### ● 定子接地保护（按规范允许单相接地运行两小时）\n##### ● 定子绕组过负荷保护\n##### ● 转子一点、二点接地保护\n##### ● 逆功率保护\n##### ● 发电机失磁保护\n##### ● 机跳电保护/热工保护（原动机停机连锁发电机解列）\n##### ● 电跳机保护（发电机保护动作连锁原动机停机）\n##### b. 低压厂用变压器\n##### ● 限时速断保护\n##### ● 过流保护\n##### ● 温度保护\n##### c. 联络线\n##### ● 线路纵联差动保护\n##### ● 方向过电流保护\n##### ● 电流速断保护\n##### ● 过电流保护\n##### ● 过负荷保护\n##### ● 零序过电流保护\n##### d. 高压电动机\n##### ● 电流速断保护\n##### ● 过电流保护\n##### ● 单相接地保护\n##### ● 根据负荷类别设低电压保护\n##### e. 同期系统采用微机自动准同期装置，手动准同期装置\n##### f. 发电机励磁系统装设自动调整励磁装置(AVR，静止可控硅)。\n\n##### 5、 主要电气设备布置\n厂用高压配电装置布置于主厂房高压配电室内，380V 低压配电装置布置在主厂房低压配电间内。汽机平台下发电机出线小室内布置有发电机出口及中性点电流互感器、发电机出口PT 柜等。其余低压厂用配电设备就地布置。发电机保护屏和直流电源屏等布置在控制室内。\n\n##### 6、电缆及电缆设施\n##### 6.1、电缆选型原则\n##### 电缆选择及敷设按照国标 GB 50217-2007 “电力工程电缆设计规范”进行。本工程选用交联聚乙烯绝缘护套阻燃电力电缆，普通控制电缆选用阻燃型控制电缆，其他与计算机有关的控制电缆选用计算机屏蔽电缆，电缆为铜芯电缆。\n##### 6.2、电缆设施\n##### 主厂房底层和高、低压配电室内设电缆沟，主厂房以电缆沟和电缆桥架敷设为主，局部穿钢管敷设，在集控室至400V 及10kV 配电室设置电缆夹层和桥架竖井。电站厂区内的电缆以电缆沟敷设为主，辅以桥架敷设电缆。厂区内照明线路采用穿管方式敷设。\n##### 6.3、电缆防火\n##### 为防止电缆着火时火灾蔓延造成严重的后果，本工程采取以下措施：\n##### 1）主厂房内及由主厂房引出的电力电缆、控制电缆、测量信号电缆均采用阻燃措施。上料系统采用阻燃电缆。重要回路如消防、报警、应急照明、操作直流电源、计算机监控、双重化继电保护等重要回路采用耐火电缆。\n##### 2）在电缆沟（隧）道分支处和进入建筑物的入口处应设立防火门或防火隔断。厂区部分的沟道每隔100m 应设防火墙。\n##### 3）在电缆敷设完成后，将所有贯穿楼板的电缆孔洞，所有高低压开关柜、控制屏、保护屏、动力箱、端子箱、电缆竖井处采用有效阻燃材料进行防火封堵，对电缆刷防火涂料。\n##### 4）对重要的电缆及高温、易燃场所采用阻燃槽盒。\n##### 5）在灰尘容易集聚的地方，电缆桥架加防护罩。\n\n##### 7、过电压保护与接地\n##### 7.1、电气设备防止过电压的保护措施\n##### 1）装置接地按GB/T50064-2014《交流电气装置的过电压保护和绝缘配合设计规范》\n##### 2）防雷设计按照GB50057-2010《建筑物防雷设计规范》进行设计。\n##### 3）为防止操作过电压，10kV 高压开关柜内真空断路器回路组合式过电压保护器。发电机出口及10kV 母线装设氧化锌避雷器，配电回路真空断路器后装设过电压保护装置。\n##### 7.2、接地装置要求\n##### 接地装置的接地要求按规程GB/T50065-2011《交流电气装置的接地设计规范》执行。接地装置的年腐蚀度参照原有工程，使用年限不低于地面工程的设计使用年限。新建厂房的接地装置采用-60x6 镀锌扁钢做为水平接地体，∮50 镀锌钢管做为垂直接地体，但以水平接地体为主，并考虑防腐措施，主厂房的梁、柱、板内主筋要接地并与接地网可靠联接。为保证人体和设备安全，所有电气设备的外壳都应与接地装置可靠连接。\n##### 主厂房及较高建筑物屋面装设避雷带，利用建筑物内钢筋作为引下线，基础内预埋钢筋作为接地体。水平接地体采用扁钢，垂直接地极采用热镀锌钢管。\n##### 本工程接地设计采用人工接地装置。\n\n##### 8、照明及检修网络\n##### 照明按照《建筑照明设计标准》GB50034-2013 和《发电厂和变电站照明设计技术规定》DL/T5390-2014 规定设计。检修电源箱按照《火力发电厂厂用电设计技术规定》DL/T5153-2014-规定设置。\n##### 8.1、工作照明\n##### 主厂房工作照明电源由 380/220V 低压工作段引接。辅助厂房的工作照明由与其系统相 对应的动力箱引接。正常照明主干线路应采用 TN-C-S 系统。\n##### 8.2、事故照明\n##### 主厂房事故照明由直流 220V 供电。 远离主厂房的辅助间事故照明采用应急灯。主厂房出入口、通道等人员疏散口处，设有安全标志灯。\n\n##### 9、检修网络\n##### 主厂房内采用固定的三相五线制电源放射形低压检修网络，检修箱电源分别由低压段回路供电。\n##### 主厂房配电室、电子设备间、值班室设立应急照明，在电源突然失电状态下，主厂房配 电室、电子设备间、值班室事故照明能够实现自动切换，应急照明自动启动。\n\n##### 10、消防报警及火灾检测自动报警系统、厂内通信\n##### 各控制室设烟气探测，配电室值班室、电子设备间及电缆夹层（电缆沟/隧道）设感温和感烟探测，全厂消防设计满足国家及当地消防部门的要求。集控室设置消防、火灾报警控 制中心。厂内通讯设施主厂房操作室设置行政电话、调度电话共 3 部。调度电话和行政电话接到相应的电话接线盒。\n##### 11、设备选型\n##### 10KV开关柜采用KYN28型中置柜；\n##### 微机保护系统采用许继、南瑞继保、南自和四方产品；\n##### 互感器采用大连一户、二户产品；\n##### 低压变频器采用施耐德、ABB或西门子等；\n##### 厂用变压器采用干式节能型变压器；\n##### 直流电源电池采用：□国内知名品牌 □德国阳光、荷贝克、海智等；\n##### 真空开关采用：□VS1断路器 □VBG/VEP固封断路器 □VD4断路器；\n##### 低压元器件采用：□二一三、常熟等国内知名品牌 □施耐德、ABB、西门子等；\n##### 高压变频器采用：□汇川、荣信、上广电、利德华福等国内知名品牌 □施耐德（利德华福）、霍尼韦尔（上广电）、艾默生（大禹电气）等；","id":"j1_39"},{"class":["1","j1_29","j1_33"],"content":"##### （1）热工自动化水平\n##### 1)\t本工程采用分散控制系统(DCS)作为机组的监控，实现集中控制。在少量就地人员配合下，在控制室内实现机组的启/停操作，并能在集控室内实现机组正常运行工况的监视、调整、控制以及异常工况的停炉、停机、报警和紧急事故处理。\n##### 2)\t在控制室内，分散控制系统(DCS)操作员站的LCD、键盘/鼠标是运行人员对机组监视、调整与控制的中心。当分散控制系统(DCS)发生全局性或重大事故时，可通过后备手操设备实现机组的紧急停炉、停机操作。\n##### 3)\t机组的监视与控制主要由DCS来实现。分散控制系统DCS包括：数据采集系统(DAS)，模拟量控制系统(MCS)，顺序控制系统(SCS)，事件顺序记录（SOE）等。\n##### 4)\t顺序控制系统(SCS)设计以子功能组级自动化水平为主。\n##### 5)\t循环冷却水等辅助系统不设值班人员，其控制及监视纳入分散控制系统(DCS)。\n##### （2）控制方式和控制室布置\n##### 1)\t控制方式\n##### 根据本工程热力系统及工艺设备布置的特点，集控室实现机、电集中控制，远程站的所有信号采用电缆通过通讯送至集中控制室。\n##### 化学水处理站反渗透采用PLC控制。\n##### 除设备自带的二次仪表外，基本不再设置盘装仪表，均采用PLC无盘化操作。\n##### 压力差压变送器采用就地分散集中的布置方式。\n##### DCS作为机组的主要控制系统，实现炉机集中控制。在少量就地人员操作配合下，在控制室内实现机和炉的启/停操作，并能在控制室内实现机组正常运行工况监视、调整及异常工况的停机、停炉、报警和紧急事故处理。锅炉汽包水位设摄像头，炉膛火焰设摄像头，采用工业电视监视汽包水位、炉膛火焰。\n##### DCS的功能包括：\n##### 数据采集处理和生产过程的监视（DAS）；\n##### 生产过程调节控制（MCS）；\n##### 生产过程开关量控制和逻辑顺序控制（SCS）；\n##### 锅炉炉膛安全监控系统（FSSS）；\n##### 汽机调节及保护功能：\n##### 汽机数字式电液控制系统（DEH）；\n##### 汽机紧急跳闸系统(ETS)；\n##### 在汽机机头侧设监视保护盘，供机组启动、停止、运行时就地监视。机、炉不设置常规仪表盘，采用DCS对机组热工参数进行监视和控制。以LCD、键盘、鼠标作为机组的主要监控手段。\n##### 2)\t控制室布置\n##### 本工程热控操作在主厂房集中控制室内完成。\n##### 控制室内布置机、炉I/O机柜、继电器柜、DCS服务器柜、DCS电源柜、热控配电柜、热控辅助柜、汽机操作员站、锅炉操作员站、电气操作员站、汽机调速操作员站、工程师站、打印机和生产电话。\n##### 化学水处理站的控制室布置在化学水处理站。\n##### （3）热工自动化功能\n##### 1)\t分散控制系统（DCS）功能\n##### a)\t数据采集和处理系统(DAS)\n##### 数据采集系统是机组在启动、停止、正常运行、事故工况下的主要监视手段。通过LCD显示和打印机等人机接口装置向运行人员提供各种实时参数或经过处理的信息以指导运行操作。其主要功能有:\n##### ● 过程变量的扫描和处理；\n##### ● 过程变量的越线报警及停机；\n##### ● LCD显示；\n##### ● 制表打印；\n##### ● 历史数据存储和检索；\n##### ● 机组性能计算。\n##### b)\t模拟量控制系统(MCS)\n##### 模拟量控制系统或称闭环控制系统，是机组最重要的控制。其主要功能如下： \n##### ● 锅筒水位调节；\n##### ● 过热蒸汽温度调节；\n##### ● 凝汽器液位调节；\n##### ● 锅炉的压力调节；\n##### ● 除氧器水位调节；\n##### ● 除氧器压力调节。\n##### c)\t自动调节系统\n##### 顺序控制主要任务是按照各设备的启停运行要求及运行状态经逻辑判断发出操作指令，对机组主要设备进行顺序启停，同时该系统根据工艺要求实施联锁与保护。\n##### SCS系统主要用于辅机的程序控制及联锁保护，在可能的条件下实现各单元功能。SCS接受运行人员的指令，自动完成功能组与子组内的辅机和相关阀门的顺序启停；\n##### 开关控制自动实现所有辅机和相关阀门的联锁保护。\n##### 顺序控制系统子组级划分以各辅机为单位主要有：\n##### ● 循环冷却水泵单元；\n##### ● 给水泵单元；\n##### ● 凝结水泵单元；\n##### ● 润滑油泵单元；\n##### 顺序控制的主要辅机可在集控室内，通过LCD/键盘进行操作控制。根据运行人员指令可实现程序暂停或中断和程序跳步功能。\n##### LCD上能显示操作指导设备和顺序执行状态及各种信息。\n##### 2)\t汽机监测、控制及保护系统的功能 \n##### a)\t汽机负荷控制系统DEH\n##### 汽机DEH基本功能是：在并网前对汽机转速进行控制；在并网后对汽机进行负荷控制；汽机的自动升速同步和带负荷，并能在补汽凝汽式工况下安全经济运行。DEH包括控制处理过程输入、输出通道，操作站I/O卡件等硬件组成。DEH与DCS之间采用硬接线连接，同时具备与DCS的通讯功能。\n##### b)\t汽轮机紧急跳闸系统ETS\n##### 汽机紧急跳闸系统（ETS）的主要功能是接受来自汽机本体安全监视仪表（TSI）、汽机油系统、凝汽器真空、手动跳闸等停机信号，经逻辑处理后驱动相应的遮断继电器完成汽轮机危急跳闸功能。\n##### 汽机主要保护有：\n##### ● 汽机超速保护；\n##### ● 轴向位移过大；\n##### ● 润滑油压过低）；\n##### ● 汽机振动大；\n##### ● 凝汽器真空低；\n##### ● DEH停机信号；\n##### ● 手动跳闸；\n##### c)\t汽轮机安全监测 系统(TSI)\n##### ● 汽机转速监测报警；\n##### ● 轴承振动监测报警；\n##### ● 轴向位移监测报警；\n##### ● 汽缸胀差监测报警；\n##### ● 油箱油位监测报警；\n##### ● 油动机行程监测；\n##### 3)\t机组保护系统\n##### 保护系统的功能，是从机组整体出发，使炉机电及各辅机之间相互配合，及时处理异常工况或用闭锁条件限制异常工况发生，避免不正常状态的发生和预防误操作，保证人身与设备的安全。\n##### 本工程设置下列保护项目：\n##### 汽机紧急跳闸系统(ETS)；\n##### 重要辅机保护(由SCS)实现；\n##### 为确保保护装置正确、可靠地动作，对影响机组安全运行的重要讯号采用三取二或二取一控制，其接点信号取自专用的就地仪表。\n##### 4)\t热工信号报警系统 \n##### 分散控制系统的LCD报警，适用于全部报警信号，并可通过打印机打印出报警时间、性质和报警恢复时间。重要信号报警主要包括：\n##### 重要热工参数偏离正常范围；\n##### ● 热工保护与重要联锁项目动作；\n##### ● 自动调节系统故障；\n##### ● 程序控制系统故障；\n##### ● 计算机系统故障；\n##### ● 重要电源系统故障；\n##### ● 重要对象的状态异常\n##### 5)\t煤气锅炉\n##### a)\t锅炉露天布置，自带顶棚，锅炉顶部设检修用电动葫芦；锅炉钢架须考虑煤气管道荷载。\n##### b)\t锅炉燃烧器要求\n##### 本锅炉采用专用的煤气燃烧器，煤气和空气在各自的通道经喷嘴旋流混合后再燃烧，保证充分混合，避免在燃烧器内发生爆炸。\n##### c)\t锅炉的密封结构要求\n##### 本锅炉采取多重密封措施，在锅炉内部设置绝热炉墙，各结合部均采取可靠密封，另外各人孔门、看火门等孔也采用特殊的结构保证密封（按LB2190-77标准执行）。过热锅炉炉墙密封应作4000Pa风压试验检查无泄漏。\n##### d)\t锅炉炉膛安全监控FSSS系统功能\n##### FSSS包括燃烧器控制系统（BCS）和燃料安全系统（FSS），应对锅炉运行的主要参数和锅炉辅机运行状态进行连续监测并对锅炉燃烧器进行管理，在操作人员来不及处理的危机情况下将燃料系统置安全状态，保证锅炉及所附设备的安全。\n##### FSSS主要功能\n##### ● 炉膛点火前后的吹扫；\n##### ● 暖炉点火；\n##### ● 主燃料（混合煤气）的引入；\n##### ● 连续运行的监视；\n##### ● 燃烧后的吹扫；\n##### ● 自动完成各种保护与操作动作，避免运行人员的误操作；\n##### ● 紧急停炉，执行人工来不及操作的动作。\n##### FSSS功能体现\n##### a)\tMFT紧急停炉功能：下列任一条件出现时该功能将立即切除进入炉膛的全部燃料，\n##### ● 全炉膛灭火\n##### ● 所有送风机跳闸\n##### ● 所有引风机跳闸\n##### ● 汽包水位高\n##### ● 汽包水位低\n##### ● 燃料丧失\n##### ● 总风量<25%持续3秒\n##### ● 炉膛压力高\n##### ● 炉膛压力低\n##### 当发生MFT时，系统立即切断进入炉膛的一切燃料，自动完成下列操作。\n##### ● 发出声光报警，并产生首出原因\n##### ● 快速关闭所有(手动输入)煤气支路阀\n##### ● 快速关闭(手动输入)煤气总进气阀\n##### ● (手动输入)煤气进入置换放空方式\n##### ● 向其它系统提供MFT跳闸接点\n##### b)\t炉膛吹扫功能（具体周期次数，根据实际情况确定）\n##### 每次锅炉启动点火前必须进行周期为5分钟的炉膛吹扫，以便将炉膛内空气更换5次，以保证炉膛内没有任何未燃尽燃料存在，以防出现爆燃。\n##### 根据NFPA的规定，需用相当于炉膛体积3~5倍的新鲜空气予以更换，一般在风量大于25%前提下吹扫5分钟。\n##### 在MFT状态下，当下列一次吹扫条件满足时，系统将给出“允许进行炉膛吹扫”信息：\n##### ● 高炉煤气总阀已关\n##### ● 高炉煤气支阀全关\n##### ● 引风机运行\n##### ● 任一送风机运行\n##### ● 无MFT条件出现\n##### ● 炉膛无火\t\t\n##### 1)在吹扫完成及有关条件满足之前，阻止煤气进入炉膛；\n##### 2)连续监测锅炉的运行工况，在检测到危害人员和设备安全的工况时，发出MFT(主燃料跳闸)；\n##### 3)当发现危害工况时，停运全部或部分已投运的锅炉燃烧设备和有关辅机，快速切除进入炉膛的燃料；\n##### 4) MFT发生后，维持锅炉进风量，以清除炉膛和烟道中可能积聚的可燃混合物。\n##### （4）热工自动化设备选型\n##### 1)\t分散控制系统(DCS)选型\n##### 分散控制系统(DCS)采用知名控制系统。\n##### 2)\t其它控制子系统选型\n##### 汽机负荷控制系统由汽机厂配套供货。\n##### 汽机本体监测仪表装置（TSI）由汽机厂配套供货。\n##### 3)\t热控主要设备选型\n##### a)\t压力和差压要求变送器选用性能优良系列的智能型变送器。\n##### b)\t汽水系统上的调节阀采用性能优良的调节阀，电动执行机构采用智能一体化电动执行机构，动作频次1200次/小时，控制信号4～20mA，反馈信号4～20mA。\n##### c)\t闭路电视选用国产等数字型成熟产品。\n##### d)\t仪表各取样管以及取样管路上的阀门选用不锈钢材质。仪表汽水管路的各取样阀门选用不锈钢。\n##### e)\t各控制电缆、信号电缆采用计算机屏蔽电缆，高温区域的电缆采用高温阻燃屏蔽电缆。\n##### f)\t仪表电缆桥架采用热镀锌桥架。\n##### g)\t就地水位计采用新光源无盲区双色云母液位计，配备电接点远传液位计，配备平衡容器远传液位计，其它就地液位计采用磁浮式翻板液位计。\n##### h)\t露天安装的变送器、压力开关全部配置防护箱。","id":"j1_40"},{"class":["1","j1_29"],"content":"##### （1）汽轮发电机房\n##### (手动输入)\n##### （2）化水车间\n##### 化水车间分室内与室外布置，室内布置反渗透、加药装置、电控室、化验室等；室外布置有原水箱、除盐水箱、中间水箱。\n##### 化水车间长(手动输入)m，宽(手动输入)m，布置、反渗透、加药装置及其管道。化水车间一端布置有电控室及化验分析间等。\n##### 化水车间为钢筋混凝土框架结构，现浇钢筋混凝土基础、钢筋混凝土梁、柱，捣制钢筋混凝土屋面，围护结构为混凝土砌块，排水方式为有组织排水，卷材防水加刚性防水，防水等级为II级，屋面做挤塑泡沫保温板隔热。\n##### 建筑装修：塑钢门窗，细石混凝土及防滑地砖地面。\n##### （3）循环水泵房\n##### 循环水泵房长(手动输入)米，宽(手动输入)米，高约(手动输入)米。\n##### 建筑装修：塑钢门窗，细石混凝土及防滑地砖地面。\n##### （4）构筑物\n##### 构筑物、设备基础及地沟等为现浇钢筋混凝土结构，地下为防水钢筋混凝土结构，锅炉平台采用钢结构。\n##### （5）厂房安全和工业卫生措施\n##### 厂房内设备与建筑物间要留有满足生产、检修所需的安全距离。主要梯子角度不大于45°，各层平台均设有二个疏散安全出口。\n##### 上人屋面及检修平台（高于1.5米平台，深于1.0米的敞口坑及池沟等周边设安全防护栏杆,高度不低于1.05米，按消防及屋面检修要求设置上屋面钢梯。\n##### 各车间根据使用要求，合理布置门窗，以满足车间自然采光、通风要求,车间采光等级按IV级考虑，汽机间设置自然采光用的阻燃玻璃钢采光带；并合理布置卫生清洁设施。\n##### （6）建筑消防设计\n##### 各建筑物根据生产、使用、储存物品的危险性、可燃物数量、火灾蔓延速度以及扑救难易程度等因素确定不同使用空间的危险等级、火灾种类及手提灭火器数量。 ","id":"j1_41"},{"class":["1"],"content":"","id":"j1_42"},{"class":["1","j1_42"],"content":"##### 煤气锅炉及汽轮发电机等发电设备设计、制造、检验原则上采用中国现行规范、标准，满足本技术协议所列技术规范的规定。","id":"j1_43"},{"class":["1","j1_42"],"content":"##### 1) 发电设备的质量保证，总承包方有完善的质量保证体系。体系符合GB/T19000或ISO9000)系列的要求。总承包方提供产品质保体系的文件及认证证书。\n##### 2)根据本技术协议，总承包方将采取措施确保设备质量，主要产品交货前，保证必要的检查与试验(工厂试验)，以保证整个设计和制造符合规程要求。\n##### 3)进行检查和试验的项目，能证明下列各项：\n##### a. 所有设备符合有关技术条件和安全规范；\n##### b. 安全装置和保护装置动作正确；\n##### 4)总承包方有责任将检查的试验资料按规定完整并及时地提交发包人；对重要的检查与试验项目，发包人派代表参加。并在试验前的20天通知发包人代表。\n##### 总承包方提供有关质量保证的各项文件，包括但不限于：\n##### 产品检验合格证书；\n##### 各种试验（打压试验、动平衡试验、机械运转）报告；\n##### 对于压力容器的焊接、探伤检验资料等档案副本，\n##### 总承包方向发包人提供制造关键设备的各项工艺记录、检验记录等档案副本。\n##### 5)总承包方提供产品(或部件)扩散件及扩散单位的有关情况。并对外购件、外协件质量总负责。\n##### 6)发电设备的质保期中，不发生主要部件损坏事故。如由于产品设计及制造质量原因而发生损坏，总承包方承担返厂修理费及运费或免费现场修复。\n##### 7)总承包方对发电设备质量总负责，加强各种材料的检测，对关键设备或材料、关键部位的阀门、进口部件等加强检验。","id":"j1_44"},{"class":["1","j1_42"],"content":"##### 1) 发电主要设备须进行必要的组装和工厂试验，确定全部制造和材料均无缺陷，所有设备功能都与预期要求相一致，设计和加工都符合技术规范的要求。\n##### 2)对于发电的重要设备在制造厂制造过程中，发包人将派出具有一定技术水平和经验且责任心较强的工程技术人员，在总承包方配合下参加设备制造和出厂前的检验、试验并监造，但这并不代替和减轻总承包方对质量的责任。\n##### 3)制造厂内须进行监造检查或试验的主要项目、主要内容在设备供货合同中列出，供发包人选择监制。","id":"j1_45"},{"class":["1"],"content":"","id":"j1_46"},{"class":["1","j1_46"],"content":"##### 总承包方的服务范围是指其在现场进行的工作和对发包人的运行、维护人员进行必要的技术培训。\n##### 总承包方应提供完整的电站发电装置调试方案，包括单体调试、分部调试和整体调试的详细文件，交发包人确认，并组织调试工作，总承包方负责试运行期间的维护和消缺工作，由总承包方负责调试，发包人有义务协助总承包方完成调试任务，包括派运行人员参与运行操作，并负责协调配合，试车调试期间所出现安全事故，责任由总承包方负责。总承包方提供机组操作规程，维护保养规程，安全运行规程，点检润滑标准。\n##### 主要设备指汽轮机、发电机、锅炉、锅炉引风机、给水泵、循环泵、变压器、电气高压开关柜、电气控制系统、热控DCS等。","id":"j1_47"},{"class":["1","j1_46"],"content":"##### 1）培训内容\n##### 总承包方负责提出培训内容和培训计划，由发包人确认。\n##### 总承包方要选派有经验和有能力的专业人员对发包人技术人员进行现场培训。\n##### 2）培训方式\n##### 步骤一：施工图交底时由总承包方免费进行现场培训，内容见附表一。\n##### 附表一：\n\n| 序号 |内容 |时间 |地点 |备注 |\n|:------|:------|:------|:------|:------|\n| 1 |热力系统：系统配置 设备选型 工艺优化 |一天 |待定 |具体时间待定 |\n| 2 |电气仪表：测点布置 连锁保护原理 系统配置 |一天 |待定 |具体时间待定 |\n| 3 |水工 |一天 |待定 |具体时间待定 |\n\n##### 步骤二：第三方（具有类似煤气发电的企业）现场进行培训；总包方联系安排行程，费用发包方自理。\n##### 步骤三：调试时总承包方现场对发包方进行现场运行培训。\n##### 总承包方提供培训资料。","id":"j1_48"},{"class":["1","j1_46"],"content":"##### 有关设计联络的计划、时间、地点和内容由发包人、总承包方共同商定。总承包方考虑的设计联络如下表：\n##### 设计联络计划表\n\n| 序号 |次数 |内容 |地点 |时间 |人数 |\n|:------|:------|:------|:------|:------|:------|\n| 1 |1 |初步设计审查 |待定 |待定 |待定 |\n| 2 |1 |施工图交底 |现场 |待定 |待定 |\n\n##### 初步设计应经发包人审查通过，在施工图设计时若需对初步设计作修改，应书面报请发包人签字认可。施工图应对初步设计不完善的地方加以补充，决不能出现简化系统，降低设备技术性能，省略结构部件的现象。 ","id":"j1_49"},{"class":["1","j1_46"],"content":"##### 发包人提供的技术文件及图纸应能满足发电机组总体设计、设备安装、现场调试运行和维护的需要。总承包方可以依据自己对设计方案的理解和认识程度提出建议，如果合理，发包人应予以采纳。\n##### （1）发包人提供的文件资料，但不限于此。\n##### 发包人在合同生效后10天之内提供给总承包方施工图设计用的图纸技术资料：\n##### 发包人根据本合同的规定向总承包方提供必需的图纸和技术资料，对上述资料的正确性、完整性及交付时间负责。负责完成本项目的初步设计阶段及施工图设计阶段的现场勘探（即详勘）。组织对总承包方的初步设计及施工图进行审查。发包人提供的技术资料深度满足总承包方进行施工图阶段设计的要求。资料应准确，不能任意修改。\n##### 发包人提交文件资料\n\n| 编号 |资料名称 |专业 |\n|:------|:------|:------|\n| 1 |总平面布置图 |总图 |\n| 2 |电厂位置的气象资料、水文资料、地质勘探资料；50年一遇洪水水位等。 |总图 |\n| 3 |为本母线供电的系统短路容量，变压器容量。发包人及地区调度对电厂通信要求。 |电气 |\n| 4 |煤气资料（包括煤气成份、煤气热值、压力、温度，煤气量等） |工艺 |\n| 5 |原水全水质分析报告 |化水 |\n\n##### 总承包方提供的技术文件\n##### 总承包应向发包人提供施工图设计文件，全部采购供货的标准设备随机材料（用户手册、安装维修资料等）；设备验收安装资料，设备单体试车资料，设备空负荷联动试车资料，安装施工竣工图和所有竣工资料，并协助参加无负荷联动试车，热负荷试车方案编制。\n##### 总承包方提供的施工图图纸目录、图纸及设备安装资料进度将在本工程技术协议签订后商定。在发包人提供给总承包方所需的设计用资料后35天内，总承包方向发包人提供初步设计方案及工程范围内的机电仪设备明细表（设备规格型号、参数），若有异议，在设计审查会协商解决。\n##### 总承包方提供整套系统设备试车大纲、运行维护手册；依据总承包方提供的资料，发包人根据自身实际情况编写运行规程和检修规程。","id":"j1_50"},{"class":["1","j1_46"],"content":"##### （1）工作配合和资料交换所用的语言为中文，单位为国际单位；\n##### （2）总承包方提供给发包方初步设计图纸2套（同时提供PDF、CAD电子版各1套）；\n##### （3）总承包方提供给发包方施工图图纸4套；\n##### （4）总承包方提供设备资料为2 套（其中原件1套）；\n##### （5）总承包方在竣工验收时，向发包方提供竣工资料2套。","id":"j1_51"},{"class":["1"],"content":"","id":"j1_52"},{"class":["1","j1_52"],"content":"##### 工程质量标准：达到技术协议各项指标技术要求，并且工程整套启动试运（第一次联合启动试运开始到72小时试运合格止）符合设计质量标准：\n##### 总承包方在组织施工中必须根据国家颁发的施工验收规范以及设计要求组织施工。\n##### 本工程整体工程的综合性能和质量满足设计图纸、国家规范及标准的要求。\n##### 工程质量等级：单位工程施工质量等级达到100%合格。\n##### 在合同的质保期内因总承包方施工责任和设备材料质量等原因造成的问题，由总承包方负责修理或更换，在双方协商确定的期限内保证问题的解决，并承担相应费用。\n##### 质保期：质保期为壹年。时间从竣工验收合格之日计起。","id":"j1_53"},{"class":["1","j1_52"],"content":"##### 1）煤气、补汽参数及发电量考核值满足下表\n\n| 序号 |高炉煤气量 |煤气热值 |补汽量 |补汽参数 |考核发电量KW |\n|:------|:------|:------|:------|:------|:------|\n| 1 |80000Nm³/H |低位发热量：3583.974KJ/NMm³ 高位发热量：3638.34KJ/NMm³ |30T/H |0.35MPa 饱和蒸汽 |26000×95%（负偏差5%） |\n| 2 |90000 Nm³/H |低位发热量：3583.974KJ/NMm³ 高位发热量：3638.34KJ/NMm³ |30T/H |0.35MPa 饱和蒸汽 |28800×95%（负偏差5%） |\n| 3 |100000 Nm³/H |低位发热量：3583.974KJ/NMm³ 高位发热量：3638.34KJ/NMm³ |30T/H |0.35MPa 饱和蒸汽 |30000×95%（负偏差5%） |\n\n##### 煤气计量装置设在煤气母管上，采用双流量计量，且同型号规格。\n##### 2）性能试验\n##### a.发包人按照相关标准和技术协议的有关规定对合同列出的性能保证项目进行性能试验。性能试验由发包人、总包方共同完成，总承包方应按合同要求提出试验大纲并经发包人认可。总承包方负责机组性能，同时派遣有经验的技术专家到现场进行技术服务。性能试验满足技术要求，热态连续稳定运行72小时后，则发包人、总承包人双方在性能验收报告上签字确认；\n##### b.若考核试验不满足性能考核要求，由总承包方负责分析原因，发包方配合，总承包方负责整改，期限不超过3个月。超过三个月，参照总承包合同10.1.2执行。\n##### c.若发包人提供的煤气参数、蒸汽参数三个月内未能满足考核的前提条件，不再进行考核，视为验收合格。\n##### d.若性能试验验收发包方有异议，则由发包方寻找第三方（双方认可）进行裁决。若裁决结果与性能试验数据相符，则费用由发包方承担，否则费用由总承包方承担。","id":"j1_54"},{"class":["1"],"content":"##### 9.1项目在施工调试过程中，总承包方应至少派一名技术人员常驻发包人现场，进行现场服务，协调处理有关技术问题。在试运调试过程中出现的设备事故、人身事故由总承包方负责（由于非总承包方人员操作导致的事故由相关责任方负责，总承包方积极配合处理）；\n##### 9.2施工过程中出现变更，总承包方需报告监理及发包人，经确认后方可施工，由总承包方出具设计变更单。\n##### 9.3本协议一式6份，发包方4份（一正三副），总承包2份（一正一副）。\n##### 9.4本协议未尽事宜，友好协商解决。","id":"j1_55"},{"class":["1"],"content":"##### 发包方：(手动输入)                          总承包方： 西安陕鼓动力股份有限公司\n##### 代   表：                     \t\t             代    表：\n##### 联系电话：                                           联系电话：\n##### 传    真：                                                  传    真：\n##### 通信地址：                       \t\t       通信地址：陕西省西安市高新区沣惠南路8号\n##### 邮    编：　\t\t\t\t\t\t邮    编：710075\n##### 日    期：      年  月  日　　　　\t         日    期：     年  月日\n##### \n\n# 主要设备备选厂家一览表\n\n| 编号 |设备名称 |推荐厂家 |\n|:------|:------|:------|\n| 1 |汽轮机 |陕鼓汽轮机 南汽 青岛捷能汽轮机股份有限公司 洛发 |\n| 2 |锅炉 |杭州锅炉集团 无锡华光 唐山信德 江西江联 |\n| 3 |水泵 |上海连成 上海凯泉 佛山水泵 |\n| 4 |煤气阀门 |上海中沪 石家庄石脉 石特阀门 |\n| 5 |汽水阀门 |上海良工 河北远大 |\n| 6 |压力容器 |江苏火电 山东宏达 唐山信德 |\n| 7 |化学水系统及过滤器 |江苏金山 宜兴天安 西安皓海嘉 |\n| 9 |DCS |和利时 西门子 ABB AB |\n| 10 |热工仪表 |川仪、吴忠仪表、江苏润仪 |\n| 11 |真空断路器 |施耐德宝光 伊顿 华东森源 |\n| 12 |低压电器元件 |施耐德 ABB 西门子 |\n| 13 |智能变送器（带数字显示，带HART协议） |E+H、EJA、罗斯蒙特 |\n| 14 |电机 |兰电、湘潭、南阳防爆、佳木斯 |\n| 15 |软启动 |长沙奥拓、西安西普、南车 |\n| 16 |综保 |国电南自 许继电气 南瑞 |\n| 17 |电缆 |无锡江南、苏州南洋、安徽华海、安徽中天 |\n| 18 |点火装置 |徐州海德测控、徐州科恩燃控、南京博纳 |\n| 19 |行车 |河南卫华、河南矿山、郑州起重设备 |\n| 20 |互感器 |大连二互、张家港互感器、西安西电高压开关厂 |","id":"j1_56"}]
    """,

    "template_content": u"""# 第一章 概述
##### @@company.company_name@@（以下简称发包人），西安陕鼓动力股份有限公司（以下简称总承包方），根据《中华人民共和国合同法》、《中华人民共和国建筑法》等有关法律规定，遵循公平、平等、诚实信用的原则，为明确双方权利和义务，就总承包 (手动输入) 项目事宜，经双方协商一致，同意并按以下条款签署本协议。总承包方应严格按国家、行业及地方现行标准、规范、规程和有关条例进行设计（双方另有约定的除外），采用成熟、实用、可靠的工艺技术及装备，工程质量合格、生产和设备运行安全可靠。
##### 目前厂区大量高炉煤气和转炉煤气富余，煤气管网中除了企业自身消耗为，大多处于放散状态，不但造成了环境的污染，而且造成大量能源的浪费，发包人依据厂区富余煤气及蒸汽情况，其参数如下表：
##### 表1、富余高炉煤气参数表

| 参数名称 |额定流量（Nm³/h） |最大富余量（Nm³/h） |最小富余量（Nm³/h） |供气压力（kPa） |供气温度（℃） |
|:------|:------|:------|:------|:------|:------|
| 高炉煤气量 | @@gaspowergeneration_needsquestionnaire.surplus_gas_bfg@@ | @@gaspowergeneration_needsquestionnaire.surplus_gas_bfg_max@@ | @@gaspowergeneration_needsquestionnaire.surplus_gas_bfg_min@@ | @@gaspowergeneration_needsquestionnaire.bfg_gas_pressure@@ | @@gaspowergeneration_needsquestionnaire.bfg_gas_temperature@@ |

##### 表2、富余转炉煤气参数表

| 参数名称 |额定流量（Nm³/h） |最大富余量（Nm³/h） |最小富余量（Nm³/h） |供气压力（kPa） |供气温度（℃） |
|:------|:------|:------|:------|:------|:------|
| 转炉煤气量 | @@gaspowergeneration_needsquestionnaire.surplus_gas_ldg@@ | @@gaspowergeneration_needsquestionnaire.surplus_maxldg_gas@@ | @@gaspowergeneration_needsquestionnaire.surplus_minldg_gas@@ | @@gaspowergeneration_needsquestionnaire.ldg_gas_pressure@@ | @@gaspowergeneration_needsquestionnaire.ldg_gas_temperature@@ |

##### 表3、富余焦炉煤气参数表

| 参数名称 |额定流量（Nm³/h） |最大富余量（Nm³/h） |最小富余量（Nm³/h） |供气压力（kPa） |供气温度（℃） |
|:------|:------|:------|:------|:------|:------|
| 焦炉煤气量 | @@gaspowergeneration_needsquestionnaire.surplus_gas_cog@@ | @@gaspowergeneration_needsquestionnaire.surplus_maxcog_gas@@ | @@gaspowergeneration_needsquestionnaire.surplus_mincog_gas@@ | @@gaspowergeneration_needsquestionnaire.cog_gas_pressure@@ | @@gaspowergeneration_needsquestionnaire.cog_gas_temperature@@ |

##### 表4、富余蒸汽量参数表(汽源发生处)

| 序号 |蒸汽来源 |流量（t/h） |压力（MPa） |温度（℃） |
|:------|:------|:------|:------|:------|
| 1 |转炉 |@@gaspowergeneration_needsquestionnaire.converter_flow@@ |@@gaspowergeneration_needsquestionnaire.converter_pressure@@  |@@gaspowergeneration_needsquestionnaire.converter_temperature@@ |
| 2 |烧结余热回收 |@@gaspowergeneration_needsquestionnaire.heat_recovery_flow@@ |@@gaspowergeneration_needsquestionnaire.heat_recovery_pressure@@ |@@gaspowergeneration_needsquestionnaire.heat_recovery_temperature@@ |
| 3 |加热炉 |@@gaspowergeneration_needsquestionnaire.furnace_flow@@ |@@gaspowergeneration_needsquestionnaire.furnace_pressure@@ |@@gaspowergeneration_needsquestionnaire.furnace_temperature@@ |
| 4 |其他 |@@gaspowergeneration_needsquestionnaire.steam_other_flow@@ |@@gaspowergeneration_needsquestionnaire.steam_other_pressure@@ |@@gaspowergeneration_needsquestionnaire.steam_other_temperature@@ |
| 注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |注：冬季采暖用汽约14.05t/h，冬夏季洗浴用蒸汽约4.5t/h。 |

##### 表5、高炉煤气成分含量表（成分有波动，下述成分取值为平均值）

| 高炉煤气成分 |含量 |含量 |
|:------|:------|:------|
| CO |% |@@gaspowergeneration_needsquestionnaire.furnace_co_content@@ |
| CO2 |% |@@gaspowergeneration_needsquestionnaire.furnace_co2_content@@ |
| CH4 |% |@@gaspowergeneration_needsquestionnaire.furnace_ch4_content@@ |
| N2 |% |@@gaspowergeneration_needsquestionnaire.furnace_n2_content@@ |
| H2 |% |@@gaspowergeneration_needsquestionnaire.furnace_h2_content@@ |
| O2 |% |@@gaspowergeneration_needsquestionnaire.furnace_o2_content@@ |
| H2O |% |@@gaspowergeneration_needsquestionnaire.furnace_h2o_content@@ |
| CmHm |% |@@gaspowergeneration_needsquestionnaire.furnace_cmhn_content@@ |
| H2S |% |@@gaspowergeneration_needsquestionnaire.furnace_h2s_content@@ |
| 低位发热量 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.furnace_low_heating@@ |
| 高位发热值 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.furnace_high_heating@@ |

##### 表6、转炉煤气成分含量表（成分有波动，下述成分取值为平均值）

| 转炉煤气成分 |含量 |含量 |
|:------|:------|:------|
| CO |% |@@gaspowergeneration_needsquestionnaire.converter_co_content@@ |
| CO2 |% |@@gaspowergeneration_needsquestionnaire.converter_co2_content@@ |
| CH4 |% |@@gaspowergeneration_needsquestionnaire.converter_ch4_content@@ |
| N2 |% |@@gaspowergeneration_needsquestionnaire.converter_n2_content@@ |
| H2 |% |@@gaspowergeneration_needsquestionnaire.converter_h2_content@@ |
| O2 |% |@@gaspowergeneration_needsquestionnaire.converter_o2_content@@ |
| H2O |% |@@gaspowergeneration_needsquestionnaire.converter_h2o_content@@ |
| CmHm |% |@@gaspowergeneration_needsquestionnaire.converter_cmhn_content@@ |
| H2S |% |@@gaspowergeneration_needsquestionnaire.converter_h2s_content@@ |
| 低位发热量 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.converter_low_heating@@ |
| 高位发热值 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.converter_high_heating@@ |

##### 表7、焦炉煤气成分含量表（成分有波动，下述成分取值为平均值）

| 焦炉煤气成分 |含量 |含量 |
|:------|:------|:------|
| CO | |@@gaspowergeneration_needsquestionnaire.coke_co_content@@ |
| CO2 | |@@gaspowergeneration_needsquestionnaire.coke_co2_content@@ |
| CH4 | |@@gaspowergeneration_needsquestionnaire.coke_ch4_content@@ |
| N2 | |@@gaspowergeneration_needsquestionnaire.coke_n2_content@@ |
| H2 | |@@gaspowergeneration_needsquestionnaire.coke_h2_content@@ |
| O2 | |@@gaspowergeneration_needsquestionnaire.coke_o2_content@@ |
| H2O | |@@gaspowergeneration_needsquestionnaire.coke_h2o_content@@ |
| CmHm | |@@gaspowergeneration_needsquestionnaire.coke_cmhn_content@@ |
| H2S | |@@gaspowergeneration_needsquestionnaire.coke_h2s_content@@ |
| 低位发热量 | |@@gaspowergeneration_needsquestionnaire.coke_low_heating@@ |
| 高位发热值 | |@@gaspowergeneration_needsquestionnaire.coke_high_heating@@ |

#####  综上所述，针对目前厂区富余的余热、余汽资源，我公司根据多年的煤气发电工程建设及设计经验，计划建设概况如下：
##### 项目名称：(手动输入)
##### 建设地址：(手动输入)
##### 建设规模：(手动输入)
##### 建设方式：(手动输入)
##### 承包内容：项目范围内的工程设计、设备成套供货、设备安装调试、工程验收及保质期服务工作；
##### 设计理念：秉承经济、实用、可靠、合理、低成本建设、低投入运行设计理念。
##### 工程质量：达到国家施工验收规范合格标准；设备制造质量应保证其达到总承包协议书技术附件即 (手动输入) 的要求，保证设计的合理性，设备制造质量应保证其可靠性，购置的标准设备应为国家或行业认可的成熟定型产品;所选用的工程材料、构建必须满足国家质量检验标准和设计规范的要求。安装工程质量应该保证质量合格、安全可靠；设计、施工安装、设备及材料、试车及验收等都应满足和符合现行国家及行业相关规范、规程和标准的要求（双方另有约定的除外）。
##### 主要经济技术指标如下：

|  |  |  |  |  |
|:------|:------|:------|:------|:------|
| 〔1〕 | 抽凝工况热耗率 | qc | kJ/(kW.h) | @@gaspowergeneration_economic_indicators.smoke_heat_consumption_rate@@ |
| 〔2〕 | 纯凝工况热耗率 | qn | kJ/(kW.h) | @@gaspowergeneration_economic_indicators.heat_consumption_rate@@ |
| 〔3〕 | 抽凝工况汽耗率 | dc | kg/(kW.h) | @@gaspowergeneration_economic_indicators.smoke_steam_consumption_rate@@ |
| 〔4〕 | 纯凝工况汽耗率 | dn | kg/(kW.h) | @@gaspowergeneration_economic_indicators.steam_consumption_rate@@ |
| 〔5〕 | 机组年利用小时数 | Ha | h | @@gaspowergeneration_economic_indicators.annual_useage_hours@@ |
| 〔6〕 | 机组年供热小时数 | T | h | @@gaspowergeneration_economic_indicators.annual_heat_hours@@ |
| 〔7〕 | 年供热量 | Qa | GJ/a | @@gaspowergeneration_economic_indicators.annual_heat_supply@@ |
| 〔8〕 | 年发电量 | Pa | 万kW.h | @@gaspowergeneration_economic_indicators.annual_power_generation@@ |
| 〔9〕 | 厂用电率 | ζ | % | @@gaspowergeneration_economic_indicators.plant_electricity_consumption@@ |
| 〔10〕 | 年供电量 | Pag | 万kW.h | @@gaspowergeneration_economic_indicators.annual_power_supply@@ |
| 〔11〕 | 锅炉效率 | ηg | % | @@gaspowergeneration_economic_indicators.boiler_efficiency@@ |
| 〔12〕 | 管道效率 | ηp | % | @@gaspowergeneration_economic_indicators.pipeline_efficiency@@ |
| 〔13〕 | 抽凝工况发电标煤耗率 | bcf | kg/h | @@gaspowergeneration_economic_indicators.smoke_power_coal_consumption@@ |
| 〔14〕 | 纯凝工况发电标煤耗率 | bnf | kg/h | @@gaspowergeneration_economic_indicators.power_coal_consumption@@ |
| 〔15〕 | 抽凝工况供电标煤耗率 | bcg | g/(kW.h) | @@gaspowergeneration_economic_indicators.smoke_supply_coal_consumption@@ |
| 〔16〕 | 纯凝工况供电标煤耗率 | bng | g/(kW.h) | @@gaspowergeneration_economic_indicators.supply_coal_consumption@@ |
| 〔17〕 | 全年平均热电比 | βp | % | @@gaspowergeneration_economic_indicators.annual_average_thermoelectric_ratio@@ |
| 〔18〕 | 抽凝工况全厂热效率 | ηcr | % | @@gaspowergeneration_economic_indicators.smoke_heat_efficiency@@ |
| 〔19〕 | 纯凝工况全厂热效率 | ηnr | % | @@gaspowergeneration_economic_indicators.heat_efficiency@@ |
# 第二章	总承包内容及交接点
## 2.1	项目总承包内容
##### （请手动输入该部分内容）#####
### 2.1.1	工程设计范围
##### 总承包方承担本工程设计、采购及施工的工作范围包括：(请手动输入) 的初步设计、施工图设计、成套设备采购供货；总承包方负责项目范围内的所有设计内容，主要包含以下方面：
##### ①发电项目的总图设计；
##### ②项目范围内的系统工艺、工艺流程及工艺管道设计；
##### ③锅炉及其辅机设计；
##### ④热力系统设备管道设计；
##### ⑤煤气、蒸汽、风、水、电、气的系统设计；
##### ⑥汽轮发电机组及辅机设计；
##### ⑦主厂房、设备基础、配电及控制室设计；
##### ⑧化学水系统及厂房的设计；
##### ⑨循环水系统的设计（含自然通风冷却塔）；
##### ⑩项目范围内的控制系统的设计；
##### ⑪项目范围内的发配电系统的设计；
##### ⑫项目范围内的检修平台和操作平台、起重设备选用设计；
##### ⑬项目范围内建筑通风、保温、防腐、消防、给排水、暖通、通讯、照明及防雷接地等设计；
##### ⑭项目范围内各类设备基础设计；
##### ⑮未提及的项目范围内其他设计。
### 2.1.2	成套设备采购及供货
##### 项目范围内主辅设备、电控、自控成套设备及单体设备采购及供货。
### 2.1.3	设备安装调试内容
##### ①锅炉及其辅助设备的安装调试；
##### ②汽轮发电机组及辅助设备的安装调试；
##### ③化学水设备、管道安装与调试；
##### ④循环水系统安装调试；
##### ⑤接点内煤气、蒸汽、风、水、电、气系统调试；
##### ⑥电气及自控设备安装调试，包含电气施工材料、电缆、电缆桥架、软件编程；
##### ⑦工程接点范围内保温工程、设备及管道防腐、耐磨处理和外部油漆、保温；
##### ⑧未提及的项目范围内其他设备安装及调试。
### 2.1.4	本工程不包含的施工及安装范围
##### ①工程项目相关报批，如项目报批、环评、开工备案、电力并网等，项目工程监理；
##### ②(请手动输入) 范围内的三通一平及绿化等；
##### ③负3米以下（包括负3米）桩基工程及桩基检测，土建桩基切桩头和灌注钢筋混凝土撞头；地上、地下障碍物的拆迁清除。；
##### ④总图范围外集水井、排水管；
##### ⑤开挖石块、建筑垃圾等由总承包方运至发包人指定的免费地点(距离项目建设地点不超过5KM)；
##### ⑥调试期所有的能源介质（水、电、气、汽、煤气、点火燃料）药品、试剂等由发包人无偿提供；
##### ⑦水质化验全部设备、设施；
##### ⑧并网相关手续办理和费用由发包人全权负责（总承包方配合提供相关资料）；
##### ⑨生产工器具(设备自带专用工具除外）、工具、办公家具，工人安全防护、劳保用品、警示牌标（煤气、电、气、水、道路）等；
##### ⑩施工过程中如发现受国家法律保护的历史文物、文化遗迹等，由此发生的费用和对工程进度产生的影响由发包人承担。
### 2.1.5	土建工程施工主要内容（总承包方范围）：
##### 电站建筑工程的施工：包括全站的建筑、结构、室内外生产、生活给排水、阀门检查井、化粪池、火灾报警、室内外消防、采暖、通风、照明、空调、通讯、建筑物防雷接地、设备二次灌浆、管道支架、钢平台等；
##### ①厂房土建工程施工，包含建（构）筑、通风、消防、火灾报警、给排水、暖通、照明（含应急照明）、接地网（接地极）及防雷接地（含设备采购、安装）；
##### ②主辅系统设备基础及二次灌浆；
##### ③钢筋混凝土结构锅炉烟囱高度暂定60m（具体高度根据详设确定）及烟风道的施工；
##### ④(请手动输入该部分内容) ；
##### ⑤主厂房行车的供货和安装（含吊车梁、滑线、钢轨）；
##### ⑥项目范围内汽、水、烟风管道支吊架的基础施工，支吊架的供货、安装。
##### ⑦所有预埋件及钢结构护栏的供货和安装，平台、扶手、走道及爬梯、辅助通道；
##### ⑧厂区埋地管道基础、管沟开挖和回填；
##### ⑨电缆沟(电缆通廊)及沟盖板；
##### ⑩电站范围内的道路施工及围墙；
## 2.2	项目交接点
##### 各种能源介质的交接点位置如下：总承包方提供所有公辅介质进发电厂区控制阀门和介质计量表；
##### ①煤气管道由总承包方接至发包人指定接点；
##### ②低压蒸汽管道总承包方接至发包人指定接点；
##### ③冷凝水送至加热炉、转炉、烧结处；
##### ④氮气、天然气由总承包方接至发包人指定接点；
##### ⑤电站所用动力电源为双回路供电，其中动力电源由发包人送至本项目总承包方高压受电柜上端子；并网电源由总承包方送至上级110KV变电所10KV一段（电缆、桥架、电缆沟等由总承包方负责）；受电柜至电站的电缆、光纤、保护模块的采购等工作由总承包方负责，受电柜由总承包方负责；
##### ⑥除盐水系统由总承包方统一负责，原水由发包人供接至电站围墙外1m（总承包方配阀），其余由总承包方负责；
##### ⑦电站生活用水、工业水由发包人供接电站围墙外1m并（总承包方配阀），其余由总承包方负责；
##### ⑧电站DCS系统与生产线控制系统之间通讯的网络分界点设在煤气电站DCS系统的网络连接口，总承包方负责预留以太网接口。
# 第三章	设计及施工标准规范
##### 所有设计文件、供货的材料和设备应符合相关的中国标准、规定、规范及法律，或者符合中国钢铁企业余热利用的相关标准、规定、规范及法律：
##### 《小型火力发电厂设计规范》GB50049-2011
##### 《火力发电厂设计技术规程》（DL5000-2000）
##### 《火力发电厂采暖通风与空气调节设计技术规定》DL/T5035-94
##### 《火力发电厂汽水管道设计技术规定》DL/T5054-1996
##### 《火力发电厂保温油漆技术规范》DL/T5072-2007
##### 《火力发电厂建筑设计规程》DL/T5094-1999
##### 《火力发电厂和变电所照明设计技术规定》DLGJ56-95
##### 《火力发电厂烟风煤粉管道设计技术规程》DL/T5121-2000
##### 《工业企业煤气安全规程》 （GB6222-2005）
##### 《工业企业噪声控制设计规范》（GBJ87-85）
##### 《建筑设计防火规范》（GB50016-2006）
##### 《建筑物防雷设计规范》（GB50057-94）
##### 《爆炸和火灾危险环境电力装置设计规范》（GB50058-92）
##### 《电力配备典型消防规程》（DL5027-93）
##### 《火力发电厂总图运输设计技术规定》（DL/T5032-2005）
##### 《火力发电厂与变电所设计防火规范》（GB50229-96）
##### 《采暖通风与空气调节设计技术规定》（DJ/T5035-95）
##### 《动力机器基础设计规范》（GB50040-1996）
##### 《火灾自动报警系统设计规范》（GB50116-98）；
##### 《蒸汽锅炉安全技术监察规程》（劳部发[1996]276号）
##### 《电力建设施工及验收技术规范》（建筑工程篇）（SDJ69-1987）；
##### 《电力建设施工及验收技术规范》(锅炉机组篇)（DL/T-5047-95）；
##### 《电力建设施工及验收技术规范》(汽轮机机组篇)（DL5011-92）；
##### 《电气装置安装工程施工及验收规范》GB50254～GB50259-96
##### 《火力发电厂建设工程启动试运及验收规程》（2009年版）
# 第四章	工程建设技术条件
## 4.1	厂址条件
##### (请手动输入该部分内容)
## 4.2	气象条件
##### 1. 工况条件
##### 1.1自然条件
##### 1.1.1 温度：
##### 1.1.1.1年平均气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a@@ ℃
##### 1.1.1.2夏季平均温度：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a_summer@@ ℃
##### 1.1.1.3冬季平均温度：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a_winter@@ ℃
##### 1.1.1.4最冷月一月平均气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a_cold@@ ℃
##### 1.1.1.5最热月七月平均气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_a_hot@@ ℃
##### 1.1.1.6年极端最高气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_extreme_h@@ ℃
##### 1.1.1.7年极端最低气温：@@gaspowergeneration_needsquestionnaire.atmosphere_temperature_extreme_l@@ ℃
##### 1.1.2  湿度：
##### 1.1.2.1夏季平均相对湿度：@@gaspowergeneration_needsquestionnaire.relative_humidity_a_summer@@ %
##### 1.1.2.2冬季平均相对湿度：@@gaspowergeneration_needsquestionnaire.relative_humidity_a_winter@@ %
##### 1.1.2.3年平均相对湿度：@@gaspowergeneration_needsquestionnaire.relative_humidity_a@@ %
##### 1.1.2.4最高相对湿度：@@gaspowergeneration_needsquestionnaire.relative_humidity_extreme_h@@ %
##### 1.1.3 大气压力
##### 1.1.3.1年平均：@@gaspowergeneration_needsquestionnaire.atmosphere_pressure_a@@ kPa
##### 1.1.3.2夏季平均气压：@@gaspowergeneration_needsquestionnaire.atmosphere_pressureSummer@@ kPa
##### 1.1.3.3冬季平均气压：@@gaspowergeneration_needsquestionnaire.atmosphere_pressureWinter@@ kPa
##### 1.1.3.4海拔高度： @@gaspowergeneration_needsquestionnaire.above_sea_level@@ m
##### 1.1.4 风速及风压：
##### 1.1.4.1年平均风速：@@gaspowergeneration_needsquestionnaire.outside_wind_speed_a@@ m/s
##### 1.1.4.2全年最大风速：@@gaspowergeneration_needsquestionnaire.outside_wind_speed_extreme_h@@ m/s
##### 1.1.5抗震能力：根椐《建筑抗震设计规范》GB50011-2010.该地区的地震设防烈度为@@gaspowergeneration_needsquestionnaire.seismic_fortification_intensity_a@@ 度，设计基本地震加速度值为@@gaspowergeneration_needsquestionnaire.design_earthquake_acceleration@@ g
## 4.3	工程地质
##### 总承包方根据建构筑物、设备基础设计前荷载，给发包人提供详勘测布点图，发包人组织详勘并在10个工作日间将详勘资料以电子版形式反馈给总承包方，由总承包方根据详勘进行设计。
## 4.4	地震烈度
##### 根据《建筑抗震设计规范》附录A的划分要求，本工程抗震设防烈度为@@gaspowergeneration_needsquestionnaire.seismic_fortification_intensity_a@@ 度，设计地震分组为第二组，设计地震基本加速度为@@gaspowergeneration_needsquestionnaire.design_earthquake_acceleration@@ g。本工程按规范进行设计。
## 4.5	建设场地
##### 本工程建设场地位于(请手动输入)。
## 4.6	燃料与余热资源（见1.1）
## 4.7	电源情况
##### (请手动输入)需要发包人提供高压保安/启动电源，装置能力要满足电站系统的启动、运行及保安用电。
## 4.8	水源状况
##### 利用原厂管网提供水源,发包方负责施工，接至电站围墙外一米处。电站的正常工业新水补水量约为@@gaspowergeneration_circulating_water_system.supply_water_amount+ gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h (包括除盐水站的原水供水)。
##### 本工程按接口处供水水压符合以下要求进行设计：
##### 生产新水≥0.30MPa
##### 生活给水≥0.25MPa
##### 消防水≥0.30MPa
## 4.9	气源情况
##### 电站的氮气主要供煤气快切阀、电视摄像机镜头、仪表气动阀、煤气管吹扫之用，为此，在主厂房设氮气储气罐一个，气源点由发包人提供,压力需≥0.60MPa，正常耗氮量小于10m³/h。
## 4.10	辅料供应
##### 项目主要消耗药品如氯化钠、磷酸三钠等，由发包人统一自行采购配给（总承包方提名称、相关参数、第一次使用数量及使用周期）。
# 第五章	工程建设技术参数
## 5.1	项目概况
##### (请手动输入该部分内容)
## 5.2	项目性质
##### 本项目属于回收利用低热值高炉煤气，高效进行清洁能源生产的工程项目。项目投产后，将创造良好的经济效益、社会效益和环保效益。
## 5.3	主要工艺方案
##### 1)热力循环系统
##### 煤气锅炉所产生的过热蒸汽作为主蒸汽进入汽轮机，蒸汽管网富裕的饱和蒸汽作为补汽进入汽轮机发电做功，做功后的蒸汽进入凝汽器凝结成水，凝结水经凝结水泵加压后分别送入煤气锅炉和低压产汽点。
##### 2)建设规模
##### 根据发包人富余的煤气资源，锅炉理论计算额定情况可产@@gaspowergeneration_boiler_of_pts.steam_output@@ t/h高温高压蒸汽，综合考虑煤气波动，机组选型为(手动输入)t/h高温高压煤气锅炉配(手动输入)MW高温高压补汽凝汽式汽轮机组+(手动输入)MW发电机组。
##### 3)机组主要技术指标
| 序号 |项目 |单位 |数值 |备注 |
|:------|:------|:------|:------|:------|
| 1 |锅炉额定蒸发量 |t/h |(请手动输入) | |
| 2 |锅炉额定计算产汽量 |t/h |@@gaspowergeneration_boiler_of_pts.steam_output@@ | |
| 3 |锅炉最大产汽量 |t/h |(请手动输入) | |
| 3 |汽轮机补汽流量 |t/h |@@gaspowergeneration_turbine_of_pts.e_exhaust_point_flow@@ | |
| 4 |装机功率 |kW |@@gaspowergeneration_turbine_of_pts.e_steam_extraction_select@@ | |
| 5 |理论计算发电量 |kW |@@gaspowergeneration_turbine_of_pts.e_steam_extraction@@ | |
| 6 |厂用电率 |% |暂无 | |
| 7 |年利用小时 |h |暂无 | |
| 8 |年发电量 |kW.h/a |暂无 | |
| 9 |年供电量 |kW.h/a |暂无 | |
| 10 |年节约标准煤量 |t/a |暂无 | |
##### 4)主要设备参数
##### 锅炉

| 序号 |内容 |单位 |数值 |
|:------|:------|:------|:------|
| 1 |型号 | |(请手动输入)|
| 2 |额定蒸发量 | |(请手动输入) |
| 3 |额定蒸汽压力 |MPa（G） |@@gaspowergeneration_boiler_of_pts.superheated_steam_outlet_pressure@@ |
| 4 |额定蒸汽温度 |℃ |@@gaspowergeneration_boiler_of_pts.superheated_steam_temperature@@ |
| 5 |给水温度 |℃ |@@gaspowergeneration_boiler_of_pts.boiler_feed_water_temperature@@ |
| 6 |排烟温度 |℃ |(请手动输入) |
| 7 |锅炉效率 | |@@gaspowergeneration_boiler_of_pts.boiler_efficiency@@ |
| 8 |燃料 | |(请手动输入) |
##### 汽轮机

| 序号 |内容 |单位 |数值 |
|:------|:------|:------|:------|
| 1 |型号 | |(请手动输入) |
| 2 |形式 | |(请手动输入) |
| 3 |额定功率 |MW |@@gaspowergeneration_turbine_of_pts.e_steam_extraction_select@@ |
| 4 |额定转速 |r/min |3000 |
| 5 |转向 | |顺时针 |
| 6 |主蒸汽流量 |t/h |@@gaspowergeneration_turbine_of_pts.e_steam_flow@@ |
| 7 |主蒸汽压力 |MPa（A） |@@gaspowergeneration_turbine_of_pts.e_steam_pressure@@ |
| 8 |主蒸汽温度 |℃ |@@gaspowergeneration_turbine_of_pts.e_steam_temperature@@ |
| 9 |补汽流量 |t/h |-- |
| 10 |补汽压力 |MPa（A） |-- |
| 11 |补汽温度 |℃ |-- |
| 12 |凝气压力 |kPa (A) |-- |

##### 发电机

| 序号 |内容 |单位 |数值 |
|:------|:------|:------|:------|
| 1 |型号 | |(手动输入) |
| 2 |额定功率 |kW |@@gaspowergeneration_turbine_of_pts.e_steam_extraction_select@@ |
| 3 |额定功率因数 | |0.8 |
| 4 |额定频率 |Hz |50 |
| 5 |额定转速 |r/min |3000 |
| 6 |额定电压 |kV |(请手动输入) |
| 7 |冷却方式 | |(请手动输入) |
| 8 |励磁系统 | |(请手动输入) |
## 5.4	系统描述
### 5.4.1	机务
##### ⑴燃料来源
##### 锅炉所需高炉、转炉煤气来自发包人煤气管网。
##### ⑵燃料特性（由发包人提供）
##### 1.高炉煤气成份（成分有波动，下述成分取值为平均值）

| 高炉煤气成分 |含量 |含量 |
|:------|:------|:------|
| CO |% |@@gaspowergeneration_needsquestionnaire.furnace_co_content@@ |
| CO2 |% |@@gaspowergeneration_needsquestionnaire.furnace_co2_content@@ |
| CH4 |% |@@gaspowergeneration_needsquestionnaire.furnace_ch4_content@@ |
| N2 |% |@@gaspowergeneration_needsquestionnaire.furnace_n2_content@@ |
| H2 |% |@@gaspowergeneration_needsquestionnaire.furnace_h2_content@@ |
| O2 |% |@@gaspowergeneration_needsquestionnaire.furnace_o2_content@@ |
| H2O |% |@@gaspowergeneration_needsquestionnaire.furnace_h2o_content@@ |
| CmHm |% |@@gaspowergeneration_needsquestionnaire.furnace_cmhn_content@@ |
| H2S |% |@@gaspowergeneration_needsquestionnaire.furnace_h2s_content@@ |
| 低位发热量 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.furnace_low_heating@@ |
| 高位发热值 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.furnace_high_heating@@ |

##### 2.转炉煤气成份（成分有波动，下述成分取值为平均值）

| 转炉煤气成分 |含量 |含量 |
|:------|:------|:------|
| CO |% |@@gaspowergeneration_needsquestionnaire.converter_co_content@@ |
| CO2 |% |@@gaspowergeneration_needsquestionnaire.converter_co2_content@@ |
| CH4 |% |@@gaspowergeneration_needsquestionnaire.converter_ch4_content@@ |
| N2 |% |@@gaspowergeneration_needsquestionnaire.converter_n2_content@@ |
| H2 |% |@@gaspowergeneration_needsquestionnaire.converter_h2_content@@ |
| O2 |% |@@gaspowergeneration_needsquestionnaire.converter_o2_content@@ |
| H2O |% |@@gaspowergeneration_needsquestionnaire.converter_h2o_content@@ |
| CmHm |% |@@gaspowergeneration_needsquestionnaire.converter_cmhn_content@@ |
| H2S |% |@@gaspowergeneration_needsquestionnaire.converter_h2s_content@@ |
| 低位发热量 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.converter_low_heating@@ |
| 高位发热值 |Kj/Nm3 |@@gaspowergeneration_needsquestionnaire.converter_high_heating@@ |

##### ⑶燃烧系统设施
##### 锅炉燃烧用的高炉煤气由外部煤气管网接入锅炉房，经锅炉煤气燃烧器送入炉膛燃烧。
##### 主厂房进口煤气总管上设有电动硬密封蝶阀、电动硬密封盲板阀、气动快速切断阀、电动调节阀、压力检测装置、温度检测装置、流量检测装置，在锅炉燃烧器入口管上设有快速切断阀门、点火探测装置、失压保护装置，煤气管道的末端设有放散装置，按煤气管道规范设排水装置、补偿装置，管道上设有吹扫装置。
##### 锅炉设有锅炉炉膛安全监控和熄火保护系统，保障锅炉安全、稳定运行。
##### 锅炉采用平衡通风方式，空气由送风机经空气预热器预热后送至锅炉两侧热风总管，再经燃烧器进入炉膛。
##### 锅炉烟气由炉后烟道，经一台吸风机送入烟囱，再由烟囱排入大气，锅炉采用一个钢筋混凝土烟囱，再由烟囱排入大气。
##### ⑷燃烧系统
##### 锅炉采用平衡通风，(手动输入) 以满足锅炉各种工况下的需要。
##### 锅炉点火：
##### (手动输入)，点火系统设施设二级点火系统。即现场手动点火及PLC自动点火。二级点火均采用高压电点火。
##### ⑸锅炉排污系统
##### 锅炉设一套连续排污系统，连续排污水通过连续排污扩容器扩容后，再排入定期排污扩容器。
##### 连续排污扩容器选用@@gaspowergeneration_boiler_auxiliaries.c_specifications@@ ，连续排污扩容的蒸汽分别接入除氧器，排污水排入定期排污扩容器。
##### 设定期排污扩容器@@gaspowergeneration_boiler_auxiliaries.r_specifications@@ ，能满足锅筒紧急放水量（最大）及连续排污的要求。
##### ⑹疏放水系统
##### 主厂房疏放水系统设疏水扩容器，疏水箱容积@@gaspowergeneration_boiler_auxiliaries.s_volume@@ m3和2台疏水泵。主蒸汽管道的启动疏水和经常疏水、低压蒸汽管道的经常疏水，锅炉的疏水均分别接入疏水扩容器。除氧器的溢放水直接排入疏水箱。疏水箱的出水经疏水泵输送至除氧器。
##### 汽轮发电机组的疏放水系统均设疏水膨胀箱，其疏水接入凝汽器。低压加热器疏水采用自流的方式，送入凝汽器。
##### ⑺加药取样系统
##### 为防止锅炉内钙镁盐类的沉积结垢，维持炉水中的磷酸盐浓度，系统设自动磷酸盐加药装置。
##### 锅炉的过热蒸汽、饱和蒸汽、炉水、给水均设有取样装置，进行定期检验分析，以监察汽水质量。
### 5.4.2	汽机房
##### ⑴主蒸汽系统
##### 补汽凝汽式汽轮发电机组所需蒸汽由(手动输入)t/h煤气锅炉和低压蒸汽管网供应，主补蒸汽系统采用(手动输入)系统。管道采用高压锅炉用无缝钢管（GB5310），所有蒸汽管道阀门均采用焊接阀门。
##### ⑵主给水系统
##### 主给水系统采用(手动输入)系统。锅炉给水温度为(手动输入)℃。煤气锅炉主给水系统设两台电动给水泵，一用一备运行；管道采用锅炉用无缝钢管（GB3087），给水操作台设有调节阀，作为启动、低负荷、额定负荷调节用。
##### 汽轮机设3段非调整抽汽。一段抽汽接至除氧器，二段接至1#低压加热器, 三段接至2#低压加热器。为防止加热器水位过高而倒流入汽轮机，在各段抽汽管道分别设有止回阀。
##### 锅炉给水经凝结水泵后由低压给水泵外供15-25t/h水至低压管网。
##### ⑶凝结水系统
##### 汽轮机配凝汽器1台，(手动输入)，汽机的凝结水由凝结水泵打出，经汽封加热器和低压加热器送入除氧器。低压加热器的疏水，通过低加疏水器打入主凝结水系统。
##### 汽轮机选用凝结水泵两台，一用一备。
##### ⑷抽气系统
##### 汽轮发电机组的抽气系统设射水抽气器。
##### ⑸循环水系统
##### 汽轮机的凝汽器冷却水采用循环冷却系统（@@gaspowergeneration_circulating_water_system.cooling_tower_selected_name@@），凝汽器进、出水管各两根，进、出水管之间设有联络管。
##### 机组的冷油器、空气冷却器等的冷却水接自凝汽器的循环冷却系统。电动给水泵以及油泵等冷却采用工业净循环水。
#####  ⑹除氧系统
##### 工程设除氧器及其给水箱一台。除氧器出力为@@gaspowergeneration_boiler_auxiliaries.s_design_flux@@ t/h，给水箱为@@gaspowergeneration_boiler_auxiliaries.s_volume@@ m3，@@gaspowergeneration_boiler_auxiliaries.p_deaerator_pressure@@ Mpa，出水温度为@@gaspowergeneration_turbine_of_pts.i_deoxidize_temperature@@ ℃，能满足最大给水量除氧及存水时间要求。
##### 除氧器进水大部分来自凝汽器凝结水，少部分补水来自除盐水站。
##### ⑺油系统
##### 汽轮发电机组油系统设施有设在汽机机头的主油泵、主油箱、事故油池、高压交流油泵、低压交流油泵、低压直流油泵、冷油器及油管道组成。
### 5.4.3	锅炉补给水系统
##### 本工程锅炉补给水采用高温高压锅炉补给水质标准及蒸汽管网富裕的饱和蒸汽执行给水质标准（GB/T12145-2008）

| 项目 | 单位 | 数值 |
|:------|:------|:------|
| 硬度 | µmol/l | ≈0 |
| 电导率 | µs/cm | ≤0.2 |
| 二氧化硅 | µg/l | ≤20 |
##### 
##### (1)锅炉补给水系统出力的确定
##### 1)锅炉总蒸发量：@@gaspowergeneration_boiler_auxiliaries.m_boiler_evaporation@@ t/h
##### 2)厂内正常水汽损失（考虑锅炉蒸汽和低压饱和蒸汽（25.5t/h)）@@gaspowergeneration_boiler_auxiliaries.m_steamwater_cycle_loss@@ t/h
##### 3)锅炉排污损失（考虑锅炉蒸汽和低压饱和蒸汽（25.5t/h)）：@@gaspowergeneration_boiler_auxiliaries.m_pollution_loss@@ t/h
##### 4)机组启动或事故时增加的损失（按最大一台锅炉蒸发量的10%计）：@@gaspowergeneration_boiler_auxiliaries.m_increase_loss@@ t/h
##### 5)正常补给水量：@@gaspowergeneration_boiler_auxiliaries.m_boiler_normal_watersupply@@ t/h
##### 6)机组启动或事故时补给水量：@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h
##### 
##### (2)补给水处理系统出力
##### 由上述计算可以看出，正常情况下所需除盐水约@@gaspowergeneration_boiler_auxiliaries.m_boiler_normal_watersupply@@ t/h，机组启动或事故时所需除盐水约@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h。
##### 考虑到设备运行效率和低压管网换水情况，本化水站的系统出力按@@gaspowergeneration_boiler_auxiliaries.m_boiler_watersupply_specifications@@进行设计，机组起动或事故时补给水，可以通过调节流量和室外的除盐水箱的水位来满足要求。
##### 本电站系统设置1座@@gaspowergeneration_boiler_auxiliaries.s_volume@@ m3的除盐水箱，再通过补水泵供至除氧头、凝汽器等用水点。
##### 
##### (3)化学除盐水系统的确定
##### 除盐水原水是工业用水，浊度比较大，详见水质报告。
##### 除盐水处理系统运行方案初定为：@@gaspowergeneration_boiler_auxiliaries.desalted_water_tech_name@@。最终工艺方案在发包人提供全水质分析报告后确定。
##### 根据水质情况，以下系统处理方案能满足电厂要求。
##### 锅炉补给水系统工艺流程：
##### gpglogic[1]
##### gpglogic[2]
##### 
##### (4)自动控制水平
##### 除盐水采用PLC自动控制,水泵、阀门为远程/机旁控制启停；过滤器为自动反洗。
##### 除盐水站控制系统在中控室设监视画面。
### 5.4.4	供排水系统
##### 1.水量及水质要求
##### （1）用水量
##### 电站生产总补充用水量：@@gaspowergeneration_circulating_water_system.supply_water_amount@@ t/h
##### 生活水：(手动输入)m3/h
##### 根据当地气象条件，经循环供水系统初步计算，夏季循环水冷却倍率采用@@gaspowergeneration_circulating_water_system.circulation_ratio_summer@@ 倍，冬季采用@@gaspowergeneration_circulating_water_system.circulation_ratio_winter@@ 倍，
##### 循环供水系统水量见下表：

| 机组容量 |凝汽量(t/h) |循环冷却水量(m3 /h) |循环冷却水量(m3 /h) |辅机冷却水量(m3/h) |总循环水量(m3/h) |总循环水量(m3/h) |
|:------|:------|:------|:------|:------|:------|:------|
| 机组容量 |凝汽量(t/h) |夏季 |冬季 |辅机冷却水量(m3/h) |夏季 |冬季 |
| (手动输入) | @@gaspowergeneration_circulating_water_system.steam_exhaust_flux_selected@@ | @@gaspowergeneration_circulating_water_system.circulation_water_flow_summer@@ | @@gaspowergeneration_circulating_water_system.circulation_water_flow_winter@@ | @@gaspowergeneration_circulating_water_system.auxiliary_cooling_water_flow_winter@@ | @@gaspowergeneration_circulating_water_system.total_circulation_water_flow_summer@@ | @@gaspowergeneration_circulating_water_system.total_circulation_water_flow_winter@@ |

##### （2）循环水系统设施、设备
##### 依据本工程冷却需循环水量要求，本工程建设gpglogic[0]，塔下新建循环水池(手动输入)座，水池旁设置泵房，安装(手动输入)台循环水泵，以保证本工程机组正常运行对循环冷却水的要求。
##### 	水质稳定：为保证循环水系统的水质稳定，延长设备使用寿命，需由发包人提供水质化验单（水质符合工业用水水质要求GB50050-95），总承包方确定需投加的水质稳定剂的种类及投加量，水质稳定加药设施可根据要求设置。
##### 循环冷却水补给水量计算结果如下表：

| 项目 |设计水量（m3/h） |实耗水量（m3/h） |
|:------|:------|:------|
| 冷却塔蒸发损失 |@@gaspowergeneration_circulating_water_system.evaporation_loss@@ |122 |
| 冷却塔风吹及飞溅损失 |@@gaspowergeneration_circulating_water_system.wind_blow_loss@@ |25 |
| 排污及渗漏损失 |@@gaspowergeneration_circulating_water_system.discharge_capacity@@ |35 |
| 补给水量 |@@gaspowergeneration_circulating_water_system.supply_water_amount@@ |182 |

##### （3）生活饮用水补给水水质应满足《生活饮用水卫生标准》GB5749-2006 的水质指标。其它补给水水质应满足前述相应水质指标表相关要求。
##### 2.水源
##### 本项目由发包人供水至电站界区，确保电站用水要求。循环水站需补充新水@@gaspowergeneration_circulating_water_system.supply_water_amount@@ t/h，化学水站考虑排污及处理效率后需补充新水@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h(最大)。所以本工程需补充新水@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply+gaspowergeneration_circulating_water_system.supply_water_amount@@ t/h。
##### 3.设计的给排水系统
##### （1）生产给水系统
##### 汽轮机凝汽器机组等设备为间接冷却回水，其回水仅温度升高,未受其它污染，故采用净循环给水系统。汽轮机机组净循环水由设计的循环水泵房内的循环给水泵组加压供给，凝汽器排出的热水利用余压直接送至冷却塔冷却，经冷却塔冷却后的水，经过回水管，自流入循环水泵房的冷吸水井，整个循环系统的循环水量最大（夏季）为：@@gaspowergeneration_circulating_water_system.total_circulation_water_flow_summer@@ t/h。除盐水系统所需要的原水量为@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply@@ t/h，生产共所需的补充水量为@@gaspowergeneration_boiler_auxiliaries.m_boiler_max_watersupply+gaspowergeneration_circulating_water_system.supply_water_amount@@ t/h。
##### （2）消防给水系统
##### 电厂需有完善的消防设施，根据消防规范的相关规定，电厂室内消火栓用水量 15L/s，室外消防用水量为 25L/s，消防总用水量为 40L/s。本期工程单独设置消防水系统，由发包方提供水源，本期电站工程负责消防管路以及设施的敷设和安装。
##### （3）排水系统
##### 本工程中，水冷系统外排废水不含有毒和有害物质，可就近排入原工厂排水系统。蒸汽管道疏水可就近排放，汽轮机疏水回收利用。分散零星的不能回收的轴承冷却水、设备检修放空水或其它冲洗水，直接就近排入下水道。
##### 排水系统的设计须结合(手动输入)现有实际排水系统情况进行设计，以保证统一性。
### 5.4.5	通风和空调设施
##### 电缆夹层，发电机小室、加药、取样间、水处理间、化水站等为消除室内余热，夏季设置轴流通风机进行通风换气。主控室和电气间安装空调，通风和空调设施满足工况需求。
### 5.4.6	电气系统
##### 1、总承包界限划分
##### 1.1、陕鼓负责范围
##### a、并网电源：
##### □10KV 并网电源以发电站联络柜端子为界，界内陕鼓负责，界外用户负责。
##### □35KV 并网电源以升压变压器高压侧35KV联络柜端子为界，界内陕鼓负责，界外用户负责。
##### □110KV 并网电源以升压变压器高压侧110KV组合开关端子为界，界内陕鼓负责，界外用户负责。
##### b、启动电源：
##### 以发电站10KV电源进线柜端子为界，界内陕鼓负责，界外用户负责。
##### c、微机保护整定计算书。
##### 1.2、用户负责范围
#####  a、电源：
#####  □提供一路10KV高压并网电源和一路10KV启动电源。
#####  □提供一路35KV高压并网电源和一路10KV启动电源。
#####  □提供一路110KV高压并网电源和一路10KV启动电源。
#####  b、并网申报审批工作和发电接入系统。
##### 2、 电气系统接线方案
##### □发电机接入系统采用10kV 接线方式，发电机出口采用 10KV 并网，与用户上级变电所10KV出线联络，并网点设置在发电机出线柜和系统联络柜。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。
##### 各级电压的中性点接地方式：
##### 10kV 采用中性点不接地方式；
##### 380V 采用中性点直接接地方式；
##### 检修和照明共用低压供电络。
##### □发电机接入系统采用35kV 接线方式，发电机出口电压 10KV，经过10/35KV升压变压器升至35KV，并与用户上级变电所35KV出线联络，并网点设置在升压变压器35KV高压侧。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。
##### 各级电压的中性点接地方式：
##### 35KV采用中性点直接接地方式；
##### 10kV 采用中性点不接地方式；
##### 380V 采用中性点直接接地方式；
##### 检修和照明共用低压供电络。
##### □发电机接入系统采用110kV 接线方式，发电机出口电压 10KV，经过10/110KV升压变压器升至110KV，并与用户上级变电所110KV出线联络，并网点设置在升压变压器110KV高压侧。发电机出口设置大容量快速开关柜，发生短路时保证发电机的安全。电厂设厂用 10kV I、II 段母线，一路取至发电机出口，另一路由用户提供。厂用高压电动机及 2 台 10/0.4kV 低压厂变电源分别从电厂厂用10KV I、II 段母线引接；低压工作变为全厂的低压负荷供电。
##### 各级电压的中性点接地方式：
##### 110KV采用中性点直接接地方式；
##### 10kV 采用中性点不接地方式；
##### 380V 采用中性点直接接地方式；
##### 检修和照明共用低压供电络。

##### 3、直流系统
##### 直流负荷包括高压开关操作电源、直流电源、保护控制电源、直流油泵和事故照明等。直流供电的电压为 220V。直流系统采用一套300Ah免维护铅酸蓄电池组。直流电源装置采用微机型相控成套直流电源装置，蓄电池采用 1X300Ah 阀控密封免维护铅酸蓄电池，配置两台逆变器。该直流装置配有微机型直流绝缘在线监测装置，能对所有的直流负荷进行接地故障监测，并能监测直流母线电压信号，在母线欠压、过压或接地时均能发出报警信号。

##### 4、 二次线、继电保护及自动装置
##### 4.1、 控制、信号及测量
##### 1）本工程电气控制室与热工控制室合并，并设有电子设备间，布置在运转层。
##### 2）电气系统控制采用独立控制系统：该方案以后台监控系统为主要监控手段，对电气系统的主要设备进行数据采集、监视及控制，该系统也可通过通讯接口与热控系统连接，在热控系统上对以上系统进行监视。
##### 3）为保证系统的安全可靠性，操作员站台暂考虑保留下列硬手操：
##### 发电机断路器紧急跳闸开关
##### 灭磁开关紧急跳闸开关

##### 4.2、控制保护
##### 发电机、厂用变压器等重要设备的控制设在集控室内，低压厂用变压器低压侧开关能实现远方控制。发电机的励磁屏、发电机保护屏、公共测控装置、通讯屏等置于集控室内。低压厂用变压器、高压电动机等采用微机综合保护，装设在就地高压开关柜上。在厂用低压配电装置工作电源和备用电源之间设有备用电源自投装置，当工作电源故障或消失时，备用电源自动/手动投入。
##### 微机综合保护装置含：发电机保护装置、联络线保护装置、低压厂用变压器保护装置、高压电动机保护装置及后台监控系统等。继电保护按国标 GB/T 50062-2008 “电力装置的继电保护和自动装置设计规范”要求配置：
##### a. 发电机保护：
##### ● 发电机失步解列保护
##### ● 纵差保护
##### ● 复合电压过电流保护
##### ● 定子接地保护（按规范允许单相接地运行两小时）
##### ● 定子绕组过负荷保护
##### ● 转子一点、二点接地保护
##### ● 逆功率保护
##### ● 发电机失磁保护
##### ● 机跳电保护/热工保护（原动机停机连锁发电机解列）
##### ● 电跳机保护（发电机保护动作连锁原动机停机）
##### b. 低压厂用变压器
##### ● 限时速断保护
##### ● 过流保护
##### ● 温度保护
##### c. 联络线
##### ● 线路纵联差动保护
##### ● 方向过电流保护
##### ● 电流速断保护
##### ● 过电流保护
##### ● 过负荷保护
##### ● 零序过电流保护
##### d. 高压电动机
##### ● 电流速断保护
##### ● 过电流保护
##### ● 单相接地保护
##### ● 根据负荷类别设低电压保护
##### e. 同期系统采用微机自动准同期装置，手动准同期装置
##### f. 发电机励磁系统装设自动调整励磁装置(AVR，静止可控硅)。

##### 5、 主要电气设备布置
厂用高压配电装置布置于主厂房高压配电室内，380V 低压配电装置布置在主厂房低压配电间内。汽机平台下发电机出线小室内布置有发电机出口及中性点电流互感器、发电机出口PT 柜等。其余低压厂用配电设备就地布置。发电机保护屏和直流电源屏等布置在控制室内。

##### 6、电缆及电缆设施
##### 6.1、电缆选型原则
##### 电缆选择及敷设按照国标 GB 50217-2007 “电力工程电缆设计规范”进行。本工程选用交联聚乙烯绝缘护套阻燃电力电缆，普通控制电缆选用阻燃型控制电缆，其他与计算机有关的控制电缆选用计算机屏蔽电缆，电缆为铜芯电缆。
##### 6.2、电缆设施
##### 主厂房底层和高、低压配电室内设电缆沟，主厂房以电缆沟和电缆桥架敷设为主，局部穿钢管敷设，在集控室至400V 及10kV 配电室设置电缆夹层和桥架竖井。电站厂区内的电缆以电缆沟敷设为主，辅以桥架敷设电缆。厂区内照明线路采用穿管方式敷设。
##### 6.3、电缆防火
##### 为防止电缆着火时火灾蔓延造成严重的后果，本工程采取以下措施：
##### 1）主厂房内及由主厂房引出的电力电缆、控制电缆、测量信号电缆均采用阻燃措施。上料系统采用阻燃电缆。重要回路如消防、报警、应急照明、操作直流电源、计算机监控、双重化继电保护等重要回路采用耐火电缆。
##### 2）在电缆沟（隧）道分支处和进入建筑物的入口处应设立防火门或防火隔断。厂区部分的沟道每隔100m 应设防火墙。
##### 3）在电缆敷设完成后，将所有贯穿楼板的电缆孔洞，所有高低压开关柜、控制屏、保护屏、动力箱、端子箱、电缆竖井处采用有效阻燃材料进行防火封堵，对电缆刷防火涂料。
##### 4）对重要的电缆及高温、易燃场所采用阻燃槽盒。
##### 5）在灰尘容易集聚的地方，电缆桥架加防护罩。

##### 7、过电压保护与接地
##### 7.1、电气设备防止过电压的保护措施
##### 1）装置接地按GB/T50064-2014《交流电气装置的过电压保护和绝缘配合设计规范》
##### 2）防雷设计按照GB50057-2010《建筑物防雷设计规范》进行设计。
##### 3）为防止操作过电压，10kV 高压开关柜内真空断路器回路组合式过电压保护器。发电机出口及10kV 母线装设氧化锌避雷器，配电回路真空断路器后装设过电压保护装置。
##### 7.2、接地装置要求
##### 接地装置的接地要求按规程GB/T50065-2011《交流电气装置的接地设计规范》执行。接地装置的年腐蚀度参照原有工程，使用年限不低于地面工程的设计使用年限。新建厂房的接地装置采用-60x6 镀锌扁钢做为水平接地体，∮50 镀锌钢管做为垂直接地体，但以水平接地体为主，并考虑防腐措施，主厂房的梁、柱、板内主筋要接地并与接地网可靠联接。为保证人体和设备安全，所有电气设备的外壳都应与接地装置可靠连接。
##### 主厂房及较高建筑物屋面装设避雷带，利用建筑物内钢筋作为引下线，基础内预埋钢筋作为接地体。水平接地体采用扁钢，垂直接地极采用热镀锌钢管。
##### 本工程接地设计采用人工接地装置。

##### 8、照明及检修网络
##### 照明按照《建筑照明设计标准》GB50034-2013 和《发电厂和变电站照明设计技术规定》DL/T5390-2014 规定设计。检修电源箱按照《火力发电厂厂用电设计技术规定》DL/T5153-2014-规定设置。
##### 8.1、工作照明
##### 主厂房工作照明电源由 380/220V 低压工作段引接。辅助厂房的工作照明由与其系统相 对应的动力箱引接。正常照明主干线路应采用 TN-C-S 系统。
##### 8.2、事故照明
##### 主厂房事故照明由直流 220V 供电。 远离主厂房的辅助间事故照明采用应急灯。主厂房出入口、通道等人员疏散口处，设有安全标志灯。

##### 9、检修网络
##### 主厂房内采用固定的三相五线制电源放射形低压检修网络，检修箱电源分别由低压段回路供电。
##### 主厂房配电室、电子设备间、值班室设立应急照明，在电源突然失电状态下，主厂房配 电室、电子设备间、值班室事故照明能够实现自动切换，应急照明自动启动。

##### 10、消防报警及火灾检测自动报警系统、厂内通信
##### 各控制室设烟气探测，配电室值班室、电子设备间及电缆夹层（电缆沟/隧道）设感温和感烟探测，全厂消防设计满足国家及当地消防部门的要求。集控室设置消防、火灾报警控 制中心。厂内通讯设施主厂房操作室设置行政电话、调度电话共 3 部。调度电话和行政电话接到相应的电话接线盒。
##### 11、设备选型
##### 10KV开关柜采用KYN28型中置柜；
##### 微机保护系统采用许继、南瑞继保、南自和四方产品；
##### 互感器采用大连一户、二户产品；
##### 低压变频器采用施耐德、ABB或西门子等；
##### 厂用变压器采用干式节能型变压器；
##### 直流电源电池采用：□国内知名品牌 □德国阳光、荷贝克、海智等；
##### 真空开关采用：□VS1断路器 □VBG/VEP固封断路器 □VD4断路器；
##### 低压元器件采用：□二一三、常熟等国内知名品牌 □施耐德、ABB、西门子等；
##### 高压变频器采用：□汇川、荣信、上广电、利德华福等国内知名品牌 □施耐德（利德华福）、霍尼韦尔（上广电）、艾默生（大禹电气）等；
### 5.4.7	热控部分
##### （1）热工自动化水平
##### 1)	本工程采用分散控制系统(DCS)作为机组的监控，实现集中控制。在少量就地人员配合下，在控制室内实现机组的启/停操作，并能在集控室内实现机组正常运行工况的监视、调整、控制以及异常工况的停炉、停机、报警和紧急事故处理。
##### 2)	在控制室内，分散控制系统(DCS)操作员站的LCD、键盘/鼠标是运行人员对机组监视、调整与控制的中心。当分散控制系统(DCS)发生全局性或重大事故时，可通过后备手操设备实现机组的紧急停炉、停机操作。
##### 3)	机组的监视与控制主要由DCS来实现。分散控制系统DCS包括：数据采集系统(DAS)，模拟量控制系统(MCS)，顺序控制系统(SCS)，事件顺序记录（SOE）等。
##### 4)	顺序控制系统(SCS)设计以子功能组级自动化水平为主。
##### 5)	循环冷却水等辅助系统不设值班人员，其控制及监视纳入分散控制系统(DCS)。
##### （2）控制方式和控制室布置
##### 1)	控制方式
##### 根据本工程热力系统及工艺设备布置的特点，集控室实现机、电集中控制，远程站的所有信号采用电缆通过通讯送至集中控制室。
##### 化学水处理站反渗透采用PLC控制。
##### 除设备自带的二次仪表外，基本不再设置盘装仪表，均采用PLC无盘化操作。
##### 压力差压变送器采用就地分散集中的布置方式。
##### DCS作为机组的主要控制系统，实现炉机集中控制。在少量就地人员操作配合下，在控制室内实现机和炉的启/停操作，并能在控制室内实现机组正常运行工况监视、调整及异常工况的停机、停炉、报警和紧急事故处理。锅炉汽包水位设摄像头，炉膛火焰设摄像头，采用工业电视监视汽包水位、炉膛火焰。
##### DCS的功能包括：
##### 数据采集处理和生产过程的监视（DAS）；
##### 生产过程调节控制（MCS）；
##### 生产过程开关量控制和逻辑顺序控制（SCS）；
##### 锅炉炉膛安全监控系统（FSSS）；
##### 汽机调节及保护功能：
##### 汽机数字式电液控制系统（DEH）；
##### 汽机紧急跳闸系统(ETS)；
##### 在汽机机头侧设监视保护盘，供机组启动、停止、运行时就地监视。机、炉不设置常规仪表盘，采用DCS对机组热工参数进行监视和控制。以LCD、键盘、鼠标作为机组的主要监控手段。
##### 2)	控制室布置
##### 本工程热控操作在主厂房集中控制室内完成。
##### 控制室内布置机、炉I/O机柜、继电器柜、DCS服务器柜、DCS电源柜、热控配电柜、热控辅助柜、汽机操作员站、锅炉操作员站、电气操作员站、汽机调速操作员站、工程师站、打印机和生产电话。
##### 化学水处理站的控制室布置在化学水处理站。
##### （3）热工自动化功能
##### 1)	分散控制系统（DCS）功能
##### a)	数据采集和处理系统(DAS)
##### 数据采集系统是机组在启动、停止、正常运行、事故工况下的主要监视手段。通过LCD显示和打印机等人机接口装置向运行人员提供各种实时参数或经过处理的信息以指导运行操作。其主要功能有:
##### ● 过程变量的扫描和处理；
##### ● 过程变量的越线报警及停机；
##### ● LCD显示；
##### ● 制表打印；
##### ● 历史数据存储和检索；
##### ● 机组性能计算。
##### b)	模拟量控制系统(MCS)
##### 模拟量控制系统或称闭环控制系统，是机组最重要的控制。其主要功能如下： 
##### ● 锅筒水位调节；
##### ● 过热蒸汽温度调节；
##### ● 凝汽器液位调节；
##### ● 锅炉的压力调节；
##### ● 除氧器水位调节；
##### ● 除氧器压力调节。
##### c)	自动调节系统
##### 顺序控制主要任务是按照各设备的启停运行要求及运行状态经逻辑判断发出操作指令，对机组主要设备进行顺序启停，同时该系统根据工艺要求实施联锁与保护。
##### SCS系统主要用于辅机的程序控制及联锁保护，在可能的条件下实现各单元功能。SCS接受运行人员的指令，自动完成功能组与子组内的辅机和相关阀门的顺序启停；
##### 开关控制自动实现所有辅机和相关阀门的联锁保护。
##### 顺序控制系统子组级划分以各辅机为单位主要有：
##### ● 循环冷却水泵单元；
##### ● 给水泵单元；
##### ● 凝结水泵单元；
##### ● 润滑油泵单元；
##### 顺序控制的主要辅机可在集控室内，通过LCD/键盘进行操作控制。根据运行人员指令可实现程序暂停或中断和程序跳步功能。
##### LCD上能显示操作指导设备和顺序执行状态及各种信息。
##### 2)	汽机监测、控制及保护系统的功能 
##### a)	汽机负荷控制系统DEH
##### 汽机DEH基本功能是：在并网前对汽机转速进行控制；在并网后对汽机进行负荷控制；汽机的自动升速同步和带负荷，并能在补汽凝汽式工况下安全经济运行。DEH包括控制处理过程输入、输出通道，操作站I/O卡件等硬件组成。DEH与DCS之间采用硬接线连接，同时具备与DCS的通讯功能。
##### b)	汽轮机紧急跳闸系统ETS
##### 汽机紧急跳闸系统（ETS）的主要功能是接受来自汽机本体安全监视仪表（TSI）、汽机油系统、凝汽器真空、手动跳闸等停机信号，经逻辑处理后驱动相应的遮断继电器完成汽轮机危急跳闸功能。
##### 汽机主要保护有：
##### ● 汽机超速保护；
##### ● 轴向位移过大；
##### ● 润滑油压过低）；
##### ● 汽机振动大；
##### ● 凝汽器真空低；
##### ● DEH停机信号；
##### ● 手动跳闸；
##### c)	汽轮机安全监测 系统(TSI)
##### ● 汽机转速监测报警；
##### ● 轴承振动监测报警；
##### ● 轴向位移监测报警；
##### ● 汽缸胀差监测报警；
##### ● 油箱油位监测报警；
##### ● 油动机行程监测；
##### 3)	机组保护系统
##### 保护系统的功能，是从机组整体出发，使炉机电及各辅机之间相互配合，及时处理异常工况或用闭锁条件限制异常工况发生，避免不正常状态的发生和预防误操作，保证人身与设备的安全。
##### 本工程设置下列保护项目：
##### 汽机紧急跳闸系统(ETS)；
##### 重要辅机保护(由SCS)实现；
##### 为确保保护装置正确、可靠地动作，对影响机组安全运行的重要讯号采用三取二或二取一控制，其接点信号取自专用的就地仪表。
##### 4)	热工信号报警系统 
##### 分散控制系统的LCD报警，适用于全部报警信号，并可通过打印机打印出报警时间、性质和报警恢复时间。重要信号报警主要包括：
##### 重要热工参数偏离正常范围；
##### ● 热工保护与重要联锁项目动作；
##### ● 自动调节系统故障；
##### ● 程序控制系统故障；
##### ● 计算机系统故障；
##### ● 重要电源系统故障；
##### ● 重要对象的状态异常
##### 5)	煤气锅炉
##### a)	锅炉露天布置，自带顶棚，锅炉顶部设检修用电动葫芦；锅炉钢架须考虑煤气管道荷载。
##### b)	锅炉燃烧器要求
##### 本锅炉采用专用的煤气燃烧器，煤气和空气在各自的通道经喷嘴旋流混合后再燃烧，保证充分混合，避免在燃烧器内发生爆炸。
##### c)	锅炉的密封结构要求
##### 本锅炉采取多重密封措施，在锅炉内部设置绝热炉墙，各结合部均采取可靠密封，另外各人孔门、看火门等孔也采用特殊的结构保证密封（按LB2190-77标准执行）。过热锅炉炉墙密封应作4000Pa风压试验检查无泄漏。
##### d)	锅炉炉膛安全监控FSSS系统功能
##### FSSS包括燃烧器控制系统（BCS）和燃料安全系统（FSS），应对锅炉运行的主要参数和锅炉辅机运行状态进行连续监测并对锅炉燃烧器进行管理，在操作人员来不及处理的危机情况下将燃料系统置安全状态，保证锅炉及所附设备的安全。
##### FSSS主要功能
##### ● 炉膛点火前后的吹扫；
##### ● 暖炉点火；
##### ● 主燃料（混合煤气）的引入；
##### ● 连续运行的监视；
##### ● 燃烧后的吹扫；
##### ● 自动完成各种保护与操作动作，避免运行人员的误操作；
##### ● 紧急停炉，执行人工来不及操作的动作。
##### FSSS功能体现
##### a)	MFT紧急停炉功能：下列任一条件出现时该功能将立即切除进入炉膛的全部燃料，
##### ● 全炉膛灭火
##### ● 所有送风机跳闸
##### ● 所有引风机跳闸
##### ● 汽包水位高
##### ● 汽包水位低
##### ● 燃料丧失
##### ● 总风量<25%持续3秒
##### ● 炉膛压力高
##### ● 炉膛压力低
##### 当发生MFT时，系统立即切断进入炉膛的一切燃料，自动完成下列操作。
##### ● 发出声光报警，并产生首出原因
##### ● 快速关闭所有(手动输入)煤气支路阀
##### ● 快速关闭(手动输入)煤气总进气阀
##### ● (手动输入)煤气进入置换放空方式
##### ● 向其它系统提供MFT跳闸接点
##### b)	炉膛吹扫功能（具体周期次数，根据实际情况确定）
##### 每次锅炉启动点火前必须进行周期为5分钟的炉膛吹扫，以便将炉膛内空气更换5次，以保证炉膛内没有任何未燃尽燃料存在，以防出现爆燃。
##### 根据NFPA的规定，需用相当于炉膛体积3~5倍的新鲜空气予以更换，一般在风量大于25%前提下吹扫5分钟。
##### 在MFT状态下，当下列一次吹扫条件满足时，系统将给出“允许进行炉膛吹扫”信息：
##### ● 高炉煤气总阀已关
##### ● 高炉煤气支阀全关
##### ● 引风机运行
##### ● 任一送风机运行
##### ● 无MFT条件出现
##### ● 炉膛无火		
##### 1)在吹扫完成及有关条件满足之前，阻止煤气进入炉膛；
##### 2)连续监测锅炉的运行工况，在检测到危害人员和设备安全的工况时，发出MFT(主燃料跳闸)；
##### 3)当发现危害工况时，停运全部或部分已投运的锅炉燃烧设备和有关辅机，快速切除进入炉膛的燃料；
##### 4) MFT发生后，维持锅炉进风量，以清除炉膛和烟道中可能积聚的可燃混合物。
##### （4）热工自动化设备选型
##### 1)	分散控制系统(DCS)选型
##### 分散控制系统(DCS)采用知名控制系统。
##### 2)	其它控制子系统选型
##### 汽机负荷控制系统由汽机厂配套供货。
##### 汽机本体监测仪表装置（TSI）由汽机厂配套供货。
##### 3)	热控主要设备选型
##### a)	压力和差压要求变送器选用性能优良系列的智能型变送器。
##### b)	汽水系统上的调节阀采用性能优良的调节阀，电动执行机构采用智能一体化电动执行机构，动作频次1200次/小时，控制信号4～20mA，反馈信号4～20mA。
##### c)	闭路电视选用国产等数字型成熟产品。
##### d)	仪表各取样管以及取样管路上的阀门选用不锈钢材质。仪表汽水管路的各取样阀门选用不锈钢。
##### e)	各控制电缆、信号电缆采用计算机屏蔽电缆，高温区域的电缆采用高温阻燃屏蔽电缆。
##### f)	仪表电缆桥架采用热镀锌桥架。
##### g)	就地水位计采用新光源无盲区双色云母液位计，配备电接点远传液位计，配备平衡容器远传液位计，其它就地液位计采用磁浮式翻板液位计。
##### h)	露天安装的变送器、压力开关全部配置防护箱。
## 5.5	土建部分（以详细设计为准）
##### （1）汽轮发电机房
##### (手动输入)
##### （2）化水车间
##### 化水车间分室内与室外布置，室内布置反渗透、加药装置、电控室、化验室等；室外布置有原水箱、除盐水箱、中间水箱。
##### 化水车间长(手动输入)m，宽(手动输入)m，布置、反渗透、加药装置及其管道。化水车间一端布置有电控室及化验分析间等。
##### 化水车间为钢筋混凝土框架结构，现浇钢筋混凝土基础、钢筋混凝土梁、柱，捣制钢筋混凝土屋面，围护结构为混凝土砌块，排水方式为有组织排水，卷材防水加刚性防水，防水等级为II级，屋面做挤塑泡沫保温板隔热。
##### 建筑装修：塑钢门窗，细石混凝土及防滑地砖地面。
##### （3）循环水泵房
##### 循环水泵房长(手动输入)米，宽(手动输入)米，高约(手动输入)米。
##### 建筑装修：塑钢门窗，细石混凝土及防滑地砖地面。
##### （4）构筑物
##### 构筑物、设备基础及地沟等为现浇钢筋混凝土结构，地下为防水钢筋混凝土结构，锅炉平台采用钢结构。
##### （5）厂房安全和工业卫生措施
##### 厂房内设备与建筑物间要留有满足生产、检修所需的安全距离。主要梯子角度不大于45°，各层平台均设有二个疏散安全出口。
##### 上人屋面及检修平台（高于1.5米平台，深于1.0米的敞口坑及池沟等周边设安全防护栏杆,高度不低于1.05米，按消防及屋面检修要求设置上屋面钢梯。
##### 各车间根据使用要求，合理布置门窗，以满足车间自然采光、通风要求,车间采光等级按IV级考虑，汽机间设置自然采光用的阻燃玻璃钢采光带；并合理布置卫生清洁设施。
##### （6）建筑消防设计
##### 各建筑物根据生产、使用、储存物品的危险性、可燃物数量、火灾蔓延速度以及扑救难易程度等因素确定不同使用空间的危险等级、火灾种类及手提灭火器数量。 
# 第六章	设备监造（检验）和性能验收试验
## 6.1	设计、制造标准
##### 煤气锅炉及汽轮发电机等发电设备设计、制造、检验原则上采用中国现行规范、标准，满足本技术协议所列技术规范的规定。
## 6.2	质量保证
##### 1) 发电设备的质量保证，总承包方有完善的质量保证体系。体系符合GB/T19000或ISO9000)系列的要求。总承包方提供产品质保体系的文件及认证证书。
##### 2)根据本技术协议，总承包方将采取措施确保设备质量，主要产品交货前，保证必要的检查与试验(工厂试验)，以保证整个设计和制造符合规程要求。
##### 3)进行检查和试验的项目，能证明下列各项：
##### a. 所有设备符合有关技术条件和安全规范；
##### b. 安全装置和保护装置动作正确；
##### 4)总承包方有责任将检查的试验资料按规定完整并及时地提交发包人；对重要的检查与试验项目，发包人派代表参加。并在试验前的20天通知发包人代表。
##### 总承包方提供有关质量保证的各项文件，包括但不限于：
##### 产品检验合格证书；
##### 各种试验（打压试验、动平衡试验、机械运转）报告；
##### 对于压力容器的焊接、探伤检验资料等档案副本，
##### 总承包方向发包人提供制造关键设备的各项工艺记录、检验记录等档案副本。
##### 5)总承包方提供产品(或部件)扩散件及扩散单位的有关情况。并对外购件、外协件质量总负责。
##### 6)发电设备的质保期中，不发生主要部件损坏事故。如由于产品设计及制造质量原因而发生损坏，总承包方承担返厂修理费及运费或免费现场修复。
##### 7)总承包方对发电设备质量总负责，加强各种材料的检测，对关键设备或材料、关键部位的阀门、进口部件等加强检验。
## 6.3	监造和检查试验
##### 1) 发电主要设备须进行必要的组装和工厂试验，确定全部制造和材料均无缺陷，所有设备功能都与预期要求相一致，设计和加工都符合技术规范的要求。
##### 2)对于发电的重要设备在制造厂制造过程中，发包人将派出具有一定技术水平和经验且责任心较强的工程技术人员，在总承包方配合下参加设备制造和出厂前的检验、试验并监造，但这并不代替和减轻总承包方对质量的责任。
##### 3)制造厂内须进行监造检查或试验的主要项目、主要内容在设备供货合同中列出，供发包人选择监制。
# 第七章	技术服务
## 7.1	技术服务范围
##### 总承包方的服务范围是指其在现场进行的工作和对发包人的运行、维护人员进行必要的技术培训。
##### 总承包方应提供完整的电站发电装置调试方案，包括单体调试、分部调试和整体调试的详细文件，交发包人确认，并组织调试工作，总承包方负责试运行期间的维护和消缺工作，由总承包方负责调试，发包人有义务协助总承包方完成调试任务，包括派运行人员参与运行操作，并负责协调配合，试车调试期间所出现安全事故，责任由总承包方负责。总承包方提供机组操作规程，维护保养规程，安全运行规程，点检润滑标准。
##### 主要设备指汽轮机、发电机、锅炉、锅炉引风机、给水泵、循环泵、变压器、电气高压开关柜、电气控制系统、热控DCS等。
## 7.2	人员培训
##### 1）培训内容
##### 总承包方负责提出培训内容和培训计划，由发包人确认。
##### 总承包方要选派有经验和有能力的专业人员对发包人技术人员进行现场培训。
##### 2）培训方式
##### 步骤一：施工图交底时由总承包方免费进行现场培训，内容见附表一。
##### 附表一：

| 序号 |内容 |时间 |地点 |备注 |
|:------|:------|:------|:------|:------|
| 1 |热力系统：系统配置 设备选型 工艺优化 |一天 |待定 |具体时间待定 |
| 2 |电气仪表：测点布置 连锁保护原理 系统配置 |一天 |待定 |具体时间待定 |
| 3 |水工 |一天 |待定 |具体时间待定 |

##### 步骤二：第三方（具有类似煤气发电的企业）现场进行培训；总包方联系安排行程，费用发包方自理。
##### 步骤三：调试时总承包方现场对发包方进行现场运行培训。
##### 总承包方提供培训资料。
## 7.3	设计联络
##### 有关设计联络的计划、时间、地点和内容由发包人、总承包方共同商定。总承包方考虑的设计联络如下表：
##### 设计联络计划表

| 序号 |次数 |内容 |地点 |时间 |人数 |
|:------|:------|:------|:------|:------|:------|
| 1 |1 |初步设计审查 |待定 |待定 |待定 |
| 2 |1 |施工图交底 |现场 |待定 |待定 |

##### 初步设计应经发包人审查通过，在施工图设计时若需对初步设计作修改，应书面报请发包人签字认可。施工图应对初步设计不完善的地方加以补充，决不能出现简化系统，降低设备技术性能，省略结构部件的现象。 
## 7.4	技术文件提交
##### 发包人提供的技术文件及图纸应能满足发电机组总体设计、设备安装、现场调试运行和维护的需要。总承包方可以依据自己对设计方案的理解和认识程度提出建议，如果合理，发包人应予以采纳。
##### （1）发包人提供的文件资料，但不限于此。
##### 发包人在合同生效后10天之内提供给总承包方施工图设计用的图纸技术资料：
##### 发包人根据本合同的规定向总承包方提供必需的图纸和技术资料，对上述资料的正确性、完整性及交付时间负责。负责完成本项目的初步设计阶段及施工图设计阶段的现场勘探（即详勘）。组织对总承包方的初步设计及施工图进行审查。发包人提供的技术资料深度满足总承包方进行施工图阶段设计的要求。资料应准确，不能任意修改。
##### 发包人提交文件资料

| 编号 |资料名称 |专业 |
|:------|:------|:------|
| 1 |总平面布置图 |总图 |
| 2 |电厂位置的气象资料、水文资料、地质勘探资料；50年一遇洪水水位等。 |总图 |
| 3 |为本母线供电的系统短路容量，变压器容量。发包人及地区调度对电厂通信要求。 |电气 |
| 4 |煤气资料（包括煤气成份、煤气热值、压力、温度，煤气量等） |工艺 |
| 5 |原水全水质分析报告 |化水 |

##### 总承包方提供的技术文件
##### 总承包应向发包人提供施工图设计文件，全部采购供货的标准设备随机材料（用户手册、安装维修资料等）；设备验收安装资料，设备单体试车资料，设备空负荷联动试车资料，安装施工竣工图和所有竣工资料，并协助参加无负荷联动试车，热负荷试车方案编制。
##### 总承包方提供的施工图图纸目录、图纸及设备安装资料进度将在本工程技术协议签订后商定。在发包人提供给总承包方所需的设计用资料后35天内，总承包方向发包人提供初步设计方案及工程范围内的机电仪设备明细表（设备规格型号、参数），若有异议，在设计审查会协商解决。
##### 总承包方提供整套系统设备试车大纲、运行维护手册；依据总承包方提供的资料，发包人根据自身实际情况编写运行规程和检修规程。
## 7.5	竣工资料提交按照发包方项目竣工验收的有关文件执行：
##### （1）工作配合和资料交换所用的语言为中文，单位为国际单位；
##### （2）总承包方提供给发包方初步设计图纸2套（同时提供PDF、CAD电子版各1套）；
##### （3）总承包方提供给发包方施工图图纸4套；
##### （4）总承包方提供设备资料为2 套（其中原件1套）；
##### （5）总承包方在竣工验收时，向发包方提供竣工资料2套。
# 第八章	工程质量及考核方式
## 8.1	工程质量
##### 工程质量标准：达到技术协议各项指标技术要求，并且工程整套启动试运（第一次联合启动试运开始到72小时试运合格止）符合设计质量标准：
##### 总承包方在组织施工中必须根据国家颁发的施工验收规范以及设计要求组织施工。
##### 本工程整体工程的综合性能和质量满足设计图纸、国家规范及标准的要求。
##### 工程质量等级：单位工程施工质量等级达到100%合格。
##### 在合同的质保期内因总承包方施工责任和设备材料质量等原因造成的问题，由总承包方负责修理或更换，在双方协商确定的期限内保证问题的解决，并承担相应费用。
##### 质保期：质保期为壹年。时间从竣工验收合格之日计起。
## 8.2	考核方式
##### 1）煤气、补汽参数及发电量考核值满足下表

| 序号 |高炉煤气量 |煤气热值 |补汽量 |补汽参数 |考核发电量KW |
|:------|:------|:------|:------|:------|:------|
| 1 |80000Nm³/H |低位发热量：3583.974KJ/NMm³ 高位发热量：3638.34KJ/NMm³ |30T/H |0.35MPa 饱和蒸汽 |26000×95%（负偏差5%） |
| 2 |90000 Nm³/H |低位发热量：3583.974KJ/NMm³ 高位发热量：3638.34KJ/NMm³ |30T/H |0.35MPa 饱和蒸汽 |28800×95%（负偏差5%） |
| 3 |100000 Nm³/H |低位发热量：3583.974KJ/NMm³ 高位发热量：3638.34KJ/NMm³ |30T/H |0.35MPa 饱和蒸汽 |30000×95%（负偏差5%） |

##### 煤气计量装置设在煤气母管上，采用双流量计量，且同型号规格。
##### 2）性能试验
##### a.发包人按照相关标准和技术协议的有关规定对合同列出的性能保证项目进行性能试验。性能试验由发包人、总包方共同完成，总承包方应按合同要求提出试验大纲并经发包人认可。总承包方负责机组性能，同时派遣有经验的技术专家到现场进行技术服务。性能试验满足技术要求，热态连续稳定运行72小时后，则发包人、总承包人双方在性能验收报告上签字确认；
##### b.若考核试验不满足性能考核要求，由总承包方负责分析原因，发包方配合，总承包方负责整改，期限不超过3个月。超过三个月，参照总承包合同10.1.2执行。
##### c.若发包人提供的煤气参数、蒸汽参数三个月内未能满足考核的前提条件，不再进行考核，视为验收合格。
##### d.若性能试验验收发包方有异议，则由发包方寻找第三方（双方认可）进行裁决。若裁决结果与性能试验数据相符，则费用由发包方承担，否则费用由总承包方承担。
# 第九章	其他
##### 9.1项目在施工调试过程中，总承包方应至少派一名技术人员常驻发包人现场，进行现场服务，协调处理有关技术问题。在试运调试过程中出现的设备事故、人身事故由总承包方负责（由于非总承包方人员操作导致的事故由相关责任方负责，总承包方积极配合处理）；
##### 9.2施工过程中出现变更，总承包方需报告监理及发包人，经确认后方可施工，由总承包方出具设计变更单。
##### 9.3本协议一式6份，发包方4份（一正三副），总承包2份（一正一副）。
##### 9.4本协议未尽事宜，友好协商解决。
# 第十章	附件目录
##### 发包方：(手动输入)                          总承包方： 西安陕鼓动力股份有限公司
##### 代   表：                     		             代    表：
##### 联系电话：                                           联系电话：
##### 传    真：                                                  传    真：
##### 通信地址：                       		       通信地址：陕西省西安市高新区沣惠南路8号
##### 邮    编：　						邮    编：710075
##### 日    期：      年  月  日　　　　	         日    期：     年  月日
##### 


# 主要设备备选厂家一览表

| 编号 |设备名称 |推荐厂家 |
|:------|:------|:------|
| 1 |汽轮机 |陕鼓汽轮机 南汽 青岛捷能汽轮机股份有限公司 洛发 |
| 2 |锅炉 |杭州锅炉集团 无锡华光 唐山信德 江西江联 |
| 3 |水泵 |上海连成 上海凯泉 佛山水泵 |
| 4 |煤气阀门 |上海中沪 石家庄石脉 石特阀门 |
| 5 |汽水阀门 |上海良工 河北远大 |
| 6 |压力容器 |江苏火电 山东宏达 唐山信德 |
| 7 |化学水系统及过滤器 |江苏金山 宜兴天安 西安皓海嘉 |
| 9 |DCS |和利时 西门子 ABB AB |
| 10 |热工仪表 |川仪、吴忠仪表、江苏润仪 |
| 11 |真空断路器 |施耐德宝光 伊顿 华东森源 |
| 12 |低压电器元件 |施耐德 ABB 西门子 |
| 13 |智能变送器（带数字显示，带HART协议） |E+H、EJA、罗斯蒙特 |
| 14 |电机 |兰电、湘潭、南阳防爆、佳木斯 |
| 15 |软启动 |长沙奥拓、西安西普、南车 |
| 16 |综保 |国电南自 许继电气 南瑞 |
| 17 |电缆 |无锡江南、苏州南洋、安徽华海、安徽中天 |
| 18 |点火装置 |徐州海德测控、徐州科恩燃控、南京博纳 |
| 19 |行车 |河南卫华、河南矿山、郑州起重设备 |
| 20 |互感器 |大连二互、张家港互感器、西安西电高压开关厂 |

    """
}]


class InitGPGReportTemplate():
    # 初始化数据
    @staticmethod
    def init_data():
        data = [
            reportTemplate_data
        ]
        for index in range(len(data)):
            InitGPGReportTemplate.insert_constant(data[index])

    # 表中插入常量数据
    @staticmethod
    def insert_constant(data):
        for index in range(len(data)):
            template_name = data[index]["template_name"]
            module_id = data[index]["module_id"]
            user_id = data[index]["user_id"]
            template_create_date = data[index]["template_create_date"]
            template_update_date = data[index]["template_update_date"]
            template__left_menu = data[index]["template__left_menu"]
            template_state = data[index]["template_state"]
            template_left_content = data[index]["template_left_content"]
            template_content = data[index]["template_content"]
            constantdata = ReportTemplate.create_constant(
                template_name, module_id, user_id, template_create_date, template_update_date,
                template__left_menu, template_state, template_left_content,
                template_content)
            ReportTemplate.insert_constant(constantdata)

# 文本逻辑表
textlogic_data = [
    {
        "textlogickey": u"gpglogic[0]",
        "textlogicvalue": u"@@\'1座\'gaspowergeneration_circulating_water_system.p_spray_area\'m2的自然通风冷却塔\' if \"gaspowergeneration_circulating_water_system.cooling_tower_selected_type\" is \"1.0\" else \'\'gaspowergeneration_circulating_water_system.p_count\' 台\'gaspowergeneration_circulating_water_system.p_single_cold_amount\'m3逆流式机械通风冷却塔\'@@",
        "textlogicremarks": u"",
        "module_name": u"gasPowerGeneration",
        "template_id": "",
        "plan_id": ""
    },

    {
        "textlogickey": u"gpglogic[1]",
        "textlogicvalue": u"@@\'水源来水→原水箱→原水泵→多介质过滤器→活性炭过滤器→保安过滤器→高压泵→反渗透装置→除二氧化碳器→中间水箱→中间水泵→混合离子交换器→除盐水箱→除盐水泵→各用水点\' if \"gaspowergeneration_boiler_auxiliaries.desalted_water_tech_type\" is \"2.0\" else \'清水池→生水泵→换热器→多介质过滤器→精密过滤器→超滤装置→超滤水池→超滤水泵→一级保安过滤器→一级高压泵→一级反渗透装置→中间水池→中间水泵→二级保安过滤器→二级高压泵→二级反渗透装置→RO产水池 →EDI供水泵→EDI装置→除盐水箱→除盐水泵→主厂房\'@@",
        "textlogicremarks": u"",
        "module_name": u"gasPowerGeneration",
        "template_id": "",
        "plan_id": ""
    },

    {
        "textlogickey": u"gpglogic[2]",
        "textlogicvalue": u"@@\'特点：设备先进，自动化程度高，运行可靠，但投资大。\' if \"gaspowergeneration_boiler_auxiliaries.desalted_water_tech_type\" is \"2.0\" else \'特点：运行安全可靠，投资省，但有酸碱废水产生。\'@@",
        "textlogicremarks": u"",
        "module_name": u"gasPowerGeneration",
        "template_id": "",
        "plan_id": ""
    },
]

class InitGPGTextlogic():
    # 初始化数据
    @staticmethod
    def init_data():
        data = [
            textlogic_data
        ]
        for index in range(len(data)):
            InitGPGTextlogic.insert_constant(data[index])

    # 表中插入常量数据
    @staticmethod
    def insert_constant(data):
        for index in range(len(data)):
            textlogickey = data[index]["textlogickey"]
            textlogicvalue = data[index]["textlogicvalue"]
            textlogicremarks = data[index]["textlogicremarks"]
            module_name = data[index]["module_name"]
            constantdata = Textlogic.create_constant(
                textlogickey, textlogicvalue, textlogicremarks, module_name)
            Textlogic.insert_constant(constantdata)