# -*- coding: utf-8 -*-
from app.models import Textlogic, ReportTemplate

# 模板表
reportTemplate_data = [{
    "template_name": u"燃气蒸汽联合循环",
    "module_id": u"CCPP",
    "user_id": "1",
    "template_create_date": "2018-01-10 09:30:40.187",
    "template_update_date": "2018-01-10 13:42:37.821",
    "template__left_menu": u"""
[{"id":"1","text":"文档目录","icon":true,"li_attr":{"id":"1"},"a_attr":{"href":"#","id":"1_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_18","text":"1. 工程概况条件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_18"},"a_attr":{"href":"#","id":"j1_18_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_19","text":"1.1 概述","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_19"},"a_attr":{"href":"#","id":"j1_19_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_21","text":"1.1.1 项目名称","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_21"},"a_attr":{"href":"#","id":"j1_21_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_19"]},{"id":"j1_22","text":"1.1.2  分布式能源项目优势","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_22"},"a_attr":{"href":"#","id":"j1_22_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_19"]},{"id":"j1_23","text":"1.1.3 项目建设单位","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_23"},"a_attr":{"href":"#","id":"j1_23_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_19"]},{"id":"j1_25","text":"1.1.4 项目建设单位简介","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_25"},"a_attr":{"href":"#","id":"j1_25_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_19"]},{"id":"j1_26","text":"1.1.5 建设方案","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_26"},"a_attr":{"href":"#","id":"j1_26_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_19"]},{"id":"j1_27","text":"1.1.6 项目建设的必要性","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_27"},"a_attr":{"href":"#","id":"j1_27_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_19"]}],"type":"file","parentNode":["1","j1_18"]},{"id":"j1_20","text":"1.2 项目现场条件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_20"},"a_attr":{"href":"#","id":"j1_20_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_28","text":"1.2.1 天然气组分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_28"},"a_attr":{"href":"#","id":"j1_28_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_20"]},{"id":"j1_29","text":"1.2.2 天然气主要物理性质","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_29"},"a_attr":{"href":"#","id":"j1_29_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_20"]},{"id":"j1_30","text":"1.2.3 气象条件及海拔地质","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_30"},"a_attr":{"href":"#","id":"j1_30_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_20"]},{"id":"j1_31","text":"1.2.4 (手动输入)工业园区","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_31"},"a_attr":{"href":"#","id":"j1_31_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_20"]},{"id":"j1_32","text":"1.2.5 仪表风及压缩空气","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_32"},"a_attr":{"href":"#","id":"j1_32_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_20"]},{"id":"j1_33","text":"1.2.6 市电供电情况","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_33"},"a_attr":{"href":"#","id":"j1_33_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_18","j1_20"]}],"type":"file","parentNode":["1","j1_18"]}],"type":"file","parentNode":["1"]},{"id":"j1_34","text":"2. 需求分析","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_34"},"a_attr":{"href":"#","id":"j1_34_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_35","text":"3. 主机选型原则及技术规范","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_35"},"a_attr":{"href":"#","id":"j1_35_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_36","text":"3.1 厂址位置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_36"},"a_attr":{"href":"#","id":"j1_36_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_35"]},{"id":"j1_37","text":"3.2 机组选型原则","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_37"},"a_attr":{"href":"#","id":"j1_37_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_38","text":"3.2.1 主设备的型式与容量的确定原则","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_38"},"a_attr":{"href":"#","id":"j1_38_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_35","j1_37"]},{"id":"j1_39","text":"3.2.2 设计依据文件","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_39"},"a_attr":{"href":"#","id":"j1_39_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_35","j1_37"]}],"type":"file","parentNode":["1","j1_35"]}],"type":"file","parentNode":["1"]},{"id":"j1_40","text":"4. 机组选型方案","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_40"},"a_attr":{"href":"#","id":"j1_40_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_41","text":"4.1燃气轮机","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_41"},"a_attr":{"href":"#","id":"j1_41_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_40"]},{"id":"j1_42","text":"4.2余热锅炉","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_42"},"a_attr":{"href":"#","id":"j1_42_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_40"]},{"id":"j1_44","text":"4.3主要设备参数","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_44"},"a_attr":{"href":"#","id":"j1_44_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_40"]}],"type":"file","parentNode":["1"]},{"id":"j1_45","text":"5. 燃气","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_45"},"a_attr":{"href":"#","id":"j1_45_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_46","text":"5.1燃料来源","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_46"},"a_attr":{"href":"#","id":"j1_46_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_45"]},{"id":"j1_47","text":"5.2燃料供应系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_47"},"a_attr":{"href":"#","id":"j1_47_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_45"]},{"id":"j1_48","text":"5.3燃气预处理系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_48"},"a_attr":{"href":"#","id":"j1_48_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_45"]}],"type":"file","parentNode":["1"]},{"id":"j1_49","text":"6. 燃烧系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_49"},"a_attr":{"href":"#","id":"j1_49_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_97","text":"7. 烟气系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_97"},"a_attr":{"href":"#","id":"j1_97_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_98","text":"8. 热力系统及其辅助设备选择","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_98"},"a_attr":{"href":"#","id":"j1_98_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_108","text":"8.1 主蒸汽及旁路系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_108"},"a_attr":{"href":"#","id":"j1_108_anchor"},"state":{"loaded":true,"opened":false,"selected":true,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_98"]},{"id":"j1_109","text":"8.2 给水系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_109"},"a_attr":{"href":"#","id":"j1_109_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_98"]},{"id":"j1_110","text":"8.3 凝结水及补水系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_110"},"a_attr":{"href":"#","id":"j1_110_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_98"]},{"id":"j1_111","text":"8.4 冷却水系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_111"},"a_attr":{"href":"#","id":"j1_111_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_98"]},{"id":"j1_112","text":"8.5 系统补水","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_112"},"a_attr":{"href":"#","id":"j1_112_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_98"]},{"id":"j1_113","text":"8.6 蒸汽输送管网","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_113"},"a_attr":{"href":"#","id":"j1_113_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_98"]}],"type":"file","parentNode":["1"]},{"id":"j1_99","text":"9. 润滑油系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_99"},"a_attr":{"href":"#","id":"j1_99_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]},{"id":"j1_100","text":"10. 电气系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_100"},"a_attr":{"href":"#","id":"j1_100_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_114","text":"10.1 主要电气设备","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_114"},"a_attr":{"href":"#","id":"j1_114_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_100"]},{"id":"j1_115","text":"10.2 电气设备布置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_115"},"a_attr":{"href":"#","id":"j1_115_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_100"]},{"id":"j1_116","text":"10.3 直流电源、二次线、继电保护及自动装置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_116"},"a_attr":{"href":"#","id":"j1_116_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_100"]},{"id":"j1_117","text":"10.4 过电压保护及接地","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_117"},"a_attr":{"href":"#","id":"j1_117_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_100"]},{"id":"j1_118","text":"10.5 照明及检修网络","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_118"},"a_attr":{"href":"#","id":"j1_118_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_100"]},{"id":"j1_119","text":"10.6 通信","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_119"},"a_attr":{"href":"#","id":"j1_119_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_100"]},{"id":"j1_120","text":"10.7 电缆设施","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_120"},"a_attr":{"href":"#","id":"j1_120_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_100"]}],"type":"file","parentNode":["1"]},{"id":"j1_101","text":"11. 电厂化学","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_101"},"a_attr":{"href":"#","id":"j1_101_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_121","text":"11.1 化水系统说明","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_121"},"a_attr":{"href":"#","id":"j1_121_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_101"]},{"id":"j1_122","text":"11.2 化水工艺设备说明","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_122"},"a_attr":{"href":"#","id":"j1_122_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_101"]},{"id":"j1_123","text":"11.3 化学加药系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_123"},"a_attr":{"href":"#","id":"j1_123_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_101"]}],"type":"file","parentNode":["1"]},{"id":"j1_102","text":"12. 热工检测及控制部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_102"},"a_attr":{"href":"#","id":"j1_102_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_124","text":"12.1 控制系统调节回路方案说明","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_124"},"a_attr":{"href":"#","id":"j1_124_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_125","text":"12.1.1 控制的基本策略","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_125"},"a_attr":{"href":"#","id":"j1_125_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102","j1_124"]},{"id":"j1_126","text":"12.1.2 燃气轮机天然气源控制系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_126"},"a_attr":{"href":"#","id":"j1_126_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102","j1_124"]},{"id":"j1_127","text":"12.1.3 蒸汽母管压力恒定控制","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_127"},"a_attr":{"href":"#","id":"j1_127_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102","j1_124"]},{"id":"j1_128","text":"12.1.4 锅炉给水控制系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_128"},"a_attr":{"href":"#","id":"j1_128_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102","j1_124"]},{"id":"j1_129","text":"12.1.5 除氧器压力水位控制系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_129"},"a_attr":{"href":"#","id":"j1_129_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102","j1_124"]}],"type":"file","parentNode":["1","j1_102"]},{"id":"j1_130","text":"12.2 燃气轮机安全保护系统FSSS","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_130"},"a_attr":{"href":"#","id":"j1_130_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102"]},{"id":"j1_131","text":"12.3 燃气轮机的联锁保护系统说明","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_131"},"a_attr":{"href":"#","id":"j1_131_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102"]},{"id":"j1_132","text":"12.4 控制室布置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_132"},"a_attr":{"href":"#","id":"j1_132_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102"]},{"id":"j1_133","text":"12.5 工业电视系统","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_133"},"a_attr":{"href":"#","id":"j1_133_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102"]},{"id":"j1_134","text":"12.6 电源和气源","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_134"},"a_attr":{"href":"#","id":"j1_134_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_102"]}],"type":"file","parentNode":["1"]},{"id":"j1_103","text":"13. 主厂房布置（暂定）","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_103"},"a_attr":{"href":"#","id":"j1_103_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_135","text":"13.1 锅炉布置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_135"},"a_attr":{"href":"#","id":"j1_135_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_103"]},{"id":"j1_136","text":"13.2 燃机布置","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_136"},"a_attr":{"href":"#","id":"j1_136_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_103"]}],"type":"file","parentNode":["1"]},{"id":"j1_104","text":"14. 建筑及结构","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_104"},"a_attr":{"href":"#","id":"j1_104_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_137","text":"14.1 设计原则","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_137"},"a_attr":{"href":"#","id":"j1_137_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_104"]},{"id":"j1_138","text":"14.2 建筑装修标准（分高、中、低档）","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_138"},"a_attr":{"href":"#","id":"j1_138_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_104"]},{"id":"j1_139","text":"14.3 建筑防火","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_139"},"a_attr":{"href":"#","id":"j1_139_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_104"]},{"id":"j1_140","text":"14.4 主要建(构)筑物结构设计","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_140"},"a_attr":{"href":"#","id":"j1_140_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_104"]}],"type":"file","parentNode":["1"]},{"id":"j1_105","text":"15. 通风及空气调节部分","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_105"},"a_attr":{"href":"#","id":"j1_105_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_141","text":"15.1 通风设计","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_141"},"a_attr":{"href":"#","id":"j1_141_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_105"]},{"id":"j1_142","text":"15.2 空调设计","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_142"},"a_attr":{"href":"#","id":"j1_142_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_105"]}],"type":"file","parentNode":["1"]},{"id":"j1_106","text":"16. 经济性分析（估算）","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_106"},"a_attr":{"href":"#","id":"j1_106_anchor"},"state":{"loaded":true,"opened":true,"selected":false,"disabled":false},"data":{},"children":[{"id":"j1_143","text":"16.1 编制依据","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_143"},"a_attr":{"href":"#","id":"j1_143_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_106"]},{"id":"j1_144","text":"16.2 经济效益分析","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_144"},"a_attr":{"href":"#","id":"j1_144_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_106"]},{"id":"j1_145","text":"16.3 敏感性分析","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_145"},"a_attr":{"href":"#","id":"j1_145_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1","j1_106"]}],"type":"file","parentNode":["1"]},{"id":"j1_107","text":"17. 结论和建议","icon":"glyphicon glyphicon-file","li_attr":{"id":"j1_107"},"a_attr":{"href":"#","id":"j1_107_anchor"},"state":{"loaded":true,"opened":false,"selected":false,"disabled":false},"data":{},"children":[],"type":"file","parentNode":["1"]}],"type":"default"}]
""",
    "template_state": "0",
    "template_left_content": 
    u"""
[{"content":"用法简介：\n1. 鼠标选中“文档目录”，点击“添加子标题”按钮，添加一级子目录。\n2. 鼠标选中生成的子级目录，点击“添加子标题”按钮，添加该目录的子级目录。\n3. 鼠标选中目录，点击“删除”按钮，删除该目录结构。\n4. 鼠标选中目录，点击“重命名”按钮或者点击键盘“F2”按钮，重命名目录。\n5. 鼠标选中目录拖拽可交换目录结构位置。\n6. 插入表格或图片后，点击“切换预览方式”按钮，可预览表格和图片，再次点击此按钮回到结构预览。\n7. 插入图表后需要在图表前后各留一行空行。\n8. 编辑模板时，请不要忘记点击“保存”按钮，将数据保存到数据库方便下次使用。\n","id":"1"},{"class":["1"],"content":"","id":"j1_2"},{"class":["1","j1_2"],"content":"@@company.company_name@@项目","id":"j1_3"},{"class":["1","j1_2"],"content":" 1、经济性。一体化方案充分利用发电余热、地热，再生水余热来制热与供冷，因此能源得以合理的梯级利用，从而提高能源利用效率。分布式电源系统减少了大型发电厂和高压输电网的压力，节约投资，并且输配电网的流量减少，相应的降低网损。再生水回用减少了自来水使用量，节约水资源， \n##### 2、环保型。项目采用生物质、垃圾再利用、太阳能、天然气等清洁剂可再生能源为一次能源，减少有害物的排放总量，减轻环保压力。 \n##### 3、能源利用多元性。采用多种形式的一次能源，且同时为用户提供电、热、水、气等多种能源应用方式，是解决能源危机、提高能源利用效率和能源安全问题的一种很好的途径。\n#####  4、调峰填谷。夏季和冬季是负荷高峰时期，此时如果采用工业余热、再生水源热、天然气等，不但解决了夏季的供冷于冬季的供热需要，同时也提供了一部分电力，对电网起到削峰填谷作用。\n##### 5、安全性和可靠性。当电网出现大面积停电事故、热网出现供热故障时，一体化能源系统仍然可以保持正常运行，提高供电、供热的安全性和可靠性。\n##### 6、分布式能源系统的优势。分布式能源系统是相对于传统的集中式能源生产与供应模式（主要代表形式是大电厂加大电网）而言的，是靠近用户端，直接向用户提供各种形式能量的中小型终端供能系统。其便于实现能源综合梯级利用，在具有更高能源利用率的同时还具有更高供能安全性以及更好的环保性能。\n##### 图1.1.2-2天然气分布式能源梯级利用示意图\n##### 天然气分布式能源是分布式能源的主要形式之一，以天然气作为燃料，采用燃气轮机或燃气内燃机为发电设备，在发电的同时，利用发电产生的烟气余热生产冷热产品就近满足用户冷热需求。天然气分布式能源的核心理论就是“温度对口、梯级利用”。与传统的电、热、冷分产系统相比，分布式能源系统的节能率约为20~35%左右，减排率可达到35~45%左右。\n##### 图1.1.2-2分布式能源节能减排原理示意图\n##### 天然气分布式冷热电联供系统以小规模（几百kW 至数十MW）分散布置的方式建在用户附近，配置灵活，便于按冷、热、电负荷的实际需要进行调节，不仅满足了区域内用户的用能需求，还节省了大量的城市供热管网建设和运行的费用，有助于电网和燃气供应的削峰填谷，减少碳化物及有害气体的排放，产生良好的社会效益，符合可持续发展战略，是未来能源技术发展的重要方向之一，在商业、建筑能源系统中将得到广泛的应用。\n##### （1）国内外发展形势\n##### 国外分布式能源发展较早，应用范围广泛。美国上个世纪90年代就已经大面积发展分布式能源，其建设分布式能源站项目超过6000个，其中医院类就有170个以上。欧美和日本的分布式能源发展更为迅猛，项目建设达10000个以上。\n##### 中国发展分布式能源较晚，主要受国内能源结构限制。现国家发改委已明确鼓励大力发展分布式能源项目；同时国家“十三五规划”中明确大力发展分布式能源建设。同时，国家逐步完成对售电侧的放开机制，并加大对分布式能源项目的奖励机制。分布式能源的发展将成为国内电源项目发展的一个新的方向。\n##### （2）与生物质直燃发电相比分布式能源的优势\n##### 分布式能源与生物质项目相比能源的综合利用程度更高，燃料更有保证，不受四季天时的影响，分布式能源项目占地面更小，生物质项目需要更大的燃料储存场站及运输队伍；分布式能源项目排放更达标，利用低氮燃烧技术无需专门的脱硫脱硝除尘设备就可以做到超净排放，生物质项目需要配置专门的脱硫脱硝除尘设备；从盈利方面讲生物质项目的盈利主要靠政府补贴，此外生物质项目的燃料价格，供应蒸汽价格受燃料供应限制价格变化较大，有较大的不可确定性。虽然生物质项目的投资相对较低，但后期运营的限制因素较多，会导致运营成本不可控，盈利难以预测。\n##### 1）分布式能源系统具有更高的能源综合利用效率。\n##### 大型火力发电厂发电效率一般为30%～40%左右，而分布式能源系统得能源利用效率至少在75%以上。\n##### 2）分布式能源系统充分考虑了能量品位的梯级利用。\n##### 分布式能源系统就近消化，克服了冷热负荷无法远距离传输的困难。对于天然气资源来说，燃烧产生的高温烟气首先用来生产高品位的电能，中温余热可以产生蒸汽、低温余热可以生产空调冷热及生活热水，是公认的最为合理的天然气利用方式。\n##### 3）分布式能源系统避免了输配成本。\n##### 传统的集中发电供能方式，必须通过输配电网，才能将生产的电能供给用户。随着电网规模扩大，电能输配成本在总成本中所占的比例越来越大。分布式能源系统由于靠近用户，几乎不需要或只需要很短的输送线路，电能的输配成本几乎为零。分布式的燃料靠管线运输，与燃料运输靠卡车或火车运输的集中发电相比，燃料运输价格更低。\n##### 4）分布式能源系统增加了电网运行的稳定性，提高了电网供电的安全性。\n##### 分布式能源系统，使大电网不再孤立和笨拙。分布式能源系统直接布置在用户侧，相对独立，在电网崩溃和意外灾害（例如地震、暴风雪、人为破坏、战争）情况下，可维持重要用户的供电，保障供电的可靠性。\n##### 5）分布式能源系统具有良好的环保性能。\n##### 分布式能源系统减少了粉尘、SO2、NOx、CO2、废水废渣等废弃物的排放；同时减少了输变电线路和设备，电磁污染和噪声污染极低，因而具有良好的环保性能。\n##### （3）国内分布式能源系统案例\n##### 目前国内分布式能源系统已被广泛应用，江浙地区、两湖两广、四川等地的燃气联合循环电厂已经建设有十几个；小型燃气内燃机分布式能源项目在大中型城市也已快速发展，这些项目主要应用在办公、医院、机场、学校等领域。目前，国内比较典型的燃气内燃机分布式能源项目如下：\n##### 1）北京清河医院供能系统采用的燃气内燃机分布式系统\n##### 2）上海黄浦中心医院采用燃气内燃机分布式能源系统\n##### 3）北京309医院采用燃气内燃机分布式能源系统\n##### 4）北京华电产业园办公大楼燃气内燃机分布式能源项目\n##### 5）上海科技大学燃气内燃机分布式能源项目\n##### 6）长沙黄花机场燃气内燃机分布式能源项目\n##### 7）上海科技大学燃气内燃机分布式能源项目\n##### 8）上海迪士尼燃气内燃机分布式能源项目","id":"j1_4"},{"class":["1","j1_2"],"content":"@@company.company_name@@公司","id":"j1_5"},{"class":["1","j1_2"],"content":"(手动输入)","id":"j1_6"},{"class":["1","j1_2"],"content":"本项目拟建设发电容量为@@ccpp_questionnaire.engine_power@@ kW，蒸汽@@ccpp_questionnaire.recent_steam_flow_range_1@@ t/h，将来有电力和蒸汽增长需求，再按实际增长需求设置燃气调峰锅炉或者再建一套燃气发电装置。","id":"j1_7"},{"class":["1","j1_2"],"content":"本项目是为响应国家关于节能环保的要求，改善利津及周边地区的大气质量，开拓天然气的合理、高效利用而建设的以天然气为燃料的燃气热电联产的天然气分布式能源系统，生物质气化多联产系统，地源热泵系统，以替代目前常规的燃煤或燃气锅炉采暖系统，缓解用电高峰，平衡天然气利用。本工程满足园区蒸汽负荷@@ccpp_questionnaire.recent_steam_flow_range_1@@t/h（@@ccpp_questionnaire.steam_pressure_level_1@@MPa，@@ccpp_questionnaire.steam_temperature_level_1@@℃），并能解决园区供电问题。本项目的建设能够满足园区的能源供给，而且又完全符合国家提出的环保、节能以及低碳的要求。\n##### （1）本项目的建设是落实国家节能政策，建设节约型社会，实现可持续发展战略的需要。\n##### 随着国家经济的快速发展，我国能源需求量也在大幅增加，从1993年开始我国就已成为能源净进口国，而且供求缺口越来越大，2010年我国的能源缺口已达到8%，预计2040年将达到24%左右。近年来国家开始大力发展节能降耗技术，尤其是供热、电厂等耗能工程，国家鼓励采用集中供热取代现有的一批分散供热小锅炉房，以较小的土地、环境、燃料和水等相关资源的代价，获得较大的能源利用效率，使得在能源资源平衡和持续安全供给方面，有效增强能源与环境协调的可持续发展后劲。\n##### （2）本项目为利津循环经济产业园配套能源项目，功能是为河利津循环经济产业园提供冷、热、电综合能源服务，是满足利津循环经济产业园本身整体规划建设和项目实际能源需求的要求。\n##### （3）本项目的建设满足节能减排，提高经济效率的需要。\n##### 本项目采取集中供热、供冷的节约能源、减少污染最有效的途径。将天然气能源最大化梯级综合利用，不仅改善了投资环境，而且可创造较好的经济效益和社会效益。\n##### （4）本项目的建设对区域环境改善作用巨大。\n##### 本项目采用燃机热电联产以清洁能源天然气为燃料，能有效的提高热效率，用能合理，提高了热能的利用率，从而节约了大量燃料；减少了设备的维修、更换设备的劳动力和资金，改善劳动条件；减轻对环境的污染；供热质量得到改善，为企业的健康发展创造了条件。\n##### 综上所述，随着周边用户大量入住用能要求矛盾会更加突出，本项目的建设是非常必要的，建成天然气分布式能源项目也是切实可行的。本项目的建设，对于利津县的经济发展及环境保护，都具有十分很重要的意义。","id":"j1_8"},{"class":["1"],"content":"","id":"j1_9"},{"content":"","id":"j1_10"},{"class":["1","j1_9"],"content":"表1.2.1-1天然气组分表（暂无）按100%CH4计算\n\n| 甲烷 |CH4 |@@ccpp_questionnaire.methane_design@@ |\n|:------|:------|:------|\n| 乙烷 |C2H6 |@@ccpp_questionnaire.ethane_design@@ |\n| 乙烯 |C2H4 |@@ccpp_questionnaire.ethylene_design@@ |\n| 丙烯 |C3H6 |@@ccpp_questionnaire.propylene_design@@ |\n| 丙烷 |C3H8 |@@ccpp_questionnaire.propane_design@@ |\n| 丁烯 |C4H8 |@@ccpp_questionnaire.butene_design@@ |\n| i-异丁烷 |iC4H10 |@@ccpp_questionnaire.i_isobutane_design@@ |\n| n-异丁烷 |nC4H10 |@@ccpp_questionnaire.n_isobutane_design@@ |\n| 戊烷 |C5H12 |@@ccpp_questionnaire.pentane_design@@ |\n| 碳6 |C6+ |@@ccpp_questionnaire.carbon6_design@@ |\n| 氢气 |H2 |@@ccpp_questionnaire.hydrogen_design@@ |\n| 氦气 |He |@@ccpp_questionnaire.helium_design@@ |\n| 氮气 |N2 |@@ccpp_questionnaire.nitrogen_design@@ |\n| 一氧化碳 |CO |@@ccpp_questionnaire.carbon_monoxide_design@@ |\n| 二氧化碳 |CO2 |@@ccpp_questionnaire.carbon_dioxide_design@@ |\n| 硫化氢 |H2S |@@ccpp_questionnaire.hydrogen_sulfide_design@@ |\n| 氧气 |O2 |@@ccpp_questionnaire.oxygen_design@@ |\n| 水 |H2O |@@ccpp_questionnaire.water_design@@ |","id":"j1_11"},{"class":["1","j1_9"],"content":"表1.2.2-1天然气物理性质表（暂无）按100%CH4计算\n\n| 高位发热量 |kJ/Nm3 |@@ccpp_questionnaire.high_calorific_value_design@@ |\n|:------|:------|:------|\n| 燃气价格 |元/Nm3 |@@ccpp_questionnaire.price_design@@ |","id":"j1_12"},{"class":["1","j1_9"],"content":"表1.2.2-2气象条件及海拔地质表按100%CH4计算\n\n| 当地平均海拔 |A |m |@@ccpp_questionnaire.local_avg_hight@@ |\n|:------|:------|:------|:------|\n| 年平均温度 |T0 |℃ |@@ccpp_questionnaire.year_avg_temperate@@ |\n| 夏季平均温度 |Ts |℃ |@@ccpp_questionnaire.summer_avg_temperate@@ |\n| 冬季平均温度 |Tw |℃ |@@ccpp_questionnaire.winter_avg_temperate@@ |\n| 年平均大气压力 |P0 |bar |@@ccpp_questionnaire.year_avg_press@@ |\n| 夏季大气压力 |Ps |bar |@@ccpp_questionnaire.summer_avg_press@@ |\n| 冬季大气压力 |Pw |bar |@@ccpp_questionnaire.winter_avg_press@@ |\n| 年平均相对湿度 |d |% |@@ccpp_questionnaire.year_avg_humidity@@ |","id":"j1_13"},{"class":["1","j1_9"],"content":"(手动输入)","id":"j1_14"},{"class":["1","j1_9"],"content":"主要用于燃气轮机空气过滤器反吹和控制仪表用，仪表风质量要求为：压力0.6~1.0MPag, 储气罐出口压力下水露点≤－40℃, 颗粒≤0.5m ，绝对过滤精度≥99.9％，总颗粒含量≤0.05 mg/m3，油雾＝0.0 mg/m3。","id":"j1_15"},{"class":["1","j1_9"],"content":"市电的供电频率的最大允许偏差不超过±1Hz，供电电压的最大允许偏差不超过额定值的±10%。具体要求见中国《供电营业规则》。其中110kV变压站据项目所在地直线距离km。详细位置见下图。\n##### 图1.2.6-1 110kV位置图\n\n![](http://117.36.73.154:6008/uploaded_file/1.1.2-2.jpg)\n","id":"j1_16"},{"content":"","id":"j1_17"},{"class":["1"],"content":"","id":"j1_18"},{"class":["1","j1_18"],"content":"","id":"j1_19"},{"class":["1","j1_18"],"content":"","id":"j1_20"},{"class":["1","j1_18","j1_19"],"content":"##### @@plan.plan_name@@项目\n","id":"j1_21"},{"class":["1","j1_18","j1_19"],"content":"##### 1、经济性。一体化方案充分利用发电余热、地热，再生水余热来制热与供冷，因此能源得以合理的梯级利用，从而提高能源利用效率。分布式电源系统减少了大型发电厂和高压输电网的压力，节约投资，并且输配电网的流量减少，相应的降低网损。再生水回用减少了自来水使用量，节约水资源， \n##### 2、环保型。项目采用生物质、垃圾再利用、太阳能、天然气等清洁剂可再生能源为一次能源，减少有害物的排放总量，减轻环保压力。 \n##### 3、能源利用多元性。采用多种形式的一次能源，且同时为用户提供电、热、水、气等多种能源应用方式，是解决能源危机、提高能源利用效率和能源安全问题的一种很好的途径。\n##### 4、调峰填谷。夏季和冬季是负荷高峰时期，此时如果采用工业余热、再生水源热、天然气等，不但解决了夏季的供冷于冬季的供热需要，同时也提供了一部分电力，对电网起到削峰填谷作用。\n##### 5、安全性和可靠性。当电网出现大面积停电事故、热网出现供热故障时，一体化能源系统仍然可以保持正常运行，提高供电、供热的安全性和可靠性。\n##### 6、分布式能源系统的优势。分布式能源系统是相对于传统的集中式能源生产与供应模式（主要代表形式是大电厂加大电网）而言的，是靠近用户端，直接向用户提供各种形式能量的中小型终端供能系统。其便于实现能源综合梯级利用，在具有更高能源利用率的同时还具有更高供能安全性以及更好的环保性能。\n##### ![](http://117.36.73.154:6008/uploaded_file/1.1.2-2.jpg)\n##### 图1.1.2-2天然气分布式能源梯级利用示意图\n##### 天然气分布式能源是分布式能源的主要形式之一，以天然气作为燃料，采用燃气轮机或燃气内燃机为发电设备，在发电的同时，利用发电产生的烟气余热生产冷热产品就近满足用户冷热需求。天然气分布式能源的核心理论就是“温度对口、梯级利用”。与传统的电、热、冷分产系统相比，分布式能源系统的节能率约为20~35%左右，减排率可达到35~45%左右。\n##### ![](http://117.36.73.154:6008/uploaded_file/1.1.2-2.jpg)\n##### 图1.1.2-2分布式能源节能减排原理示意图\n##### 天然气分布式冷热电联供系统以小规模（几百kW 至数十MW）分散布置的方式建在用户附近，配置灵活，便于按冷、热、电负荷的实际需要进行调节，不仅满足了区域内用户的用能需求，还节省了大量的城市供热管网建设和运行的费用，有助于电网和燃气供应的削峰填谷，减少碳化物及有害气体的排放，产生良好的社会效益，符合可持续发展战略，是未来能源技术发展的重要方向之一，在商业、建筑能源系统中将得到广泛的应用。\n##### （1）国内外发展形势\n##### 国外分布式能源发展较早，应用范围广泛。美国上个世纪90年代就已经大面积发展分布式能源，其建设分布式能源站项目超过6000个，其中医院类就有170个以上。欧美和日本的分布式能源发展更为迅猛，项目建设达10000个以上。\n##### 中国发展分布式能源较晚，主要受国内能源结构限制。现国家发改委已明确鼓励大力发展分布式能源项目；同时国家“十三五规划”中明确大力发展分布式能源建设。同时，国家逐步完成对售电侧的放开机制，并加大对分布式能源项目的奖励机制。分布式能源的发展将成为国内电源项目发展的一个新的方向。\n##### （2）与生物质直燃发电相比分布式能源的优势\n##### 分布式能源与生物质项目相比能源的综合利用程度更高，燃料更有保证，不受四季天时的影响，分布式能源项目占地面更小，生物质项目需要更大的燃料储存场站及运输队伍；分布式能源项目排放更达标，利用低氮燃烧技术无需专门的脱硫脱硝除尘设备就可以做到超净排放，生物质项目需要配置专门的脱硫脱硝除尘设备；从盈利方面讲生物质项目的盈利主要靠政府补贴，此外生物质项目的燃料价格，供应蒸汽价格受燃料供应限制价格变化较大，有较大的不可确定性。虽然生物质项目的投资相对较低，但后期运营的限制因素较多，会导致运营成本不可控，盈利难以预测。\n##### 1）分布式能源系统具有更高的能源综合利用效率。\n##### 大型火力发电厂发电效率一般为30%～40%左右，而分布式能源系统得能源利用效率至少在75%以上。\n##### 2）分布式能源系统充分考虑了能量品位的梯级利用。\n##### 分布式能源系统就近消化，克服了冷热负荷无法远距离传输的困难。对于天然气资源来说，燃烧产生的高温烟气首先用来生产高品位的电能，中温余热可以产生蒸汽、低温余热可以生产空调冷热及生活热水，是公认的最为合理的天然气利用方式。\n##### 3）分布式能源系统避免了输配成本。\n##### 传统的集中发电供能方式，必须通过输配电网，才能将生产的电能供给用户。随着电网规模扩大，电能输配成本在总成本中所占的比例越来越大。分布式能源系统由于靠近用户，几乎不需要或只需要很短的输送线路，电能的输配成本几乎为零。分布式的燃料靠管线运输，与燃料运输靠卡车或火车运输的集中发电相比，燃料运输价格更低。\n##### 4）分布式能源系统增加了电网运行的稳定性，提高了电网供电的安全性。\n##### 分布式能源系统，使大电网不再孤立和笨拙。分布式能源系统直接布置在用户侧，相对独立，在电网崩溃和意外灾害（例如地震、暴风雪、人为破坏、战争）情况下，可维持重要用户的供电，保障供电的可靠性。\n##### 5）分布式能源系统具有良好的环保性能。\n##### 分布式能源系统减少了粉尘、SO2、NOx、CO2、废水废渣等废弃物的排放；同时减少了输变电线路和设备，电磁污染和噪声污染极低，因而具有良好的环保性能。\n##### （3）国内分布式能源系统案例\n##### 目前国内分布式能源系统已被广泛应用，江浙地区、两湖两广、四川等地的燃气联合循环电厂已经建设有十几个；小型燃气内燃机分布式能源项目在大中型城市也已快速发展，这些项目主要应用在办公、医院、机场、学校等领域。目前，国内比较典型的燃气内燃机分布式能源项目如下：\n##### 1）北京清河医院供能系统采用的燃气内燃机分布式系统\n##### 2）上海黄浦中心医院采用燃气内燃机分布式能源系统\n##### 3）北京309医院采用燃气内燃机分布式能源系统\n##### 4）北京华电产业园办公大楼燃气内燃机分布式能源项目\n##### 5）上海科技大学燃气内燃机分布式能源项目\n##### 6）长沙黄花机场燃气内燃机分布式能源项目\n##### 7）上海科技大学燃气内燃机分布式能源项目\n##### 8）上海迪士尼燃气内燃机分布式能源项目","id":"j1_22"},{"class":["1","j1_18","j1_19"],"content":"##### @@company.company_name@@公司","id":"j1_23"},{"content":"","id":"j1_24"},{"class":["1","j1_18","j1_19"],"content":"##### (手动输入)","id":"j1_25"},{"class":["1","j1_18","j1_19"],"content":"##### 本项目拟建设发电容量为@@ccpp_questionnaire.engine_power_design@@ kW，蒸汽@@ccpp_questionnaire.recent_steam_flow_range_1_design@@ t/h，将来有电力和蒸汽增长需求，再按实际增长需求设置燃气调峰锅炉或者再建一套燃气发电装置。","id":"j1_26"},{"class":["1","j1_18","j1_19"],"content":"##### 本项目是为响应国家关于节能环保的要求，改善利津及周边地区的大气质量，开拓天然气的合理、高效利用而建设的以天然气为燃料的燃气热电联产的天然气分布式能源系统，生物质气化多联产系统，地源热泵系统，以替代目前常规的燃煤或燃气锅炉采暖系统，缓解用电高峰，平衡天然气利用。本工程满足园区蒸汽负荷@@ccpp_questionnaire.recent_steam_flow_range_1_design@@t/h（@@ccpp_questionnaire.steam_pressure_level_1_design@@MPa，@@ccpp_questionnaire.steam_temperature_level_1_design@@℃），并能解决园区供电问题。本项目的建设能够满足园区的能源供给，而且又完全符合国家提出的环保、节能以及低碳的要求。\n##### （1）本项目的建设是落实国家节能政策，建设节约型社会，实现可持续发展战略的需要。\n##### 随着国家经济的快速发展，我国能源需求量也在大幅增加，从1993年开始我国就已成为能源净进口国，而且供求缺口越来越大，2010年我国的能源缺口已达到8%，预计2040年将达到24%左右。近年来国家开始大力发展节能降耗技术，尤其是供热、电厂等耗能工程，国家鼓励采用集中供热取代现有的一批分散供热小锅炉房，以较小的土地、环境、燃料和水等相关资源的代价，获得较大的能源利用效率，使得在能源资源平衡和持续安全供给方面，有效增强能源与环境协调的可持续发展后劲。\n##### （2）本项目为利津循环经济产业园配套能源项目，功能是为河利津循环经济产业园提供冷、热、电综合能源服务，是满足利津循环经济产业园本身整体规划建设和项目实际能源需求的要求。\n##### （3）本项目的建设满足节能减排，提高经济效率的需要。\n##### 本项目采取集中供热、供冷的节约能源、减少污染最有效的途径。将天然气能源最大化梯级综合利用，不仅改善了投资环境，而且可创造较好的经济效益和社会效益。\n##### （4）本项目的建设对区域环境改善作用巨大。\n##### 本项目采用燃机热电联产以清洁能源天然气为燃料，能有效的提高热效率，用能合理，提高了热能的利用率，从而节约了大量燃料；减少了设备的维修、更换设备的劳动力和资金，改善劳动条件；减轻对环境的污染；供热质量得到改善，为企业的健康发展创造了条件。\n##### 综上所述，随着周边用户大量入住用能要求矛盾会更加突出，本项目的建设是非常必要的，建成天然气分布式能源项目也是切实可行的。本项目的建设，对于利津县的经济发展及环境保护，都具有十分很重要的意义。","id":"j1_27"},{"class":["1","j1_18","j1_20"],"content":"##### 表1.2.1-1天然气组分表（暂无）按100%CH4计算\n\n| 甲烷 |CH4 |@@ccpp_questionnaire.methane_design@@ |\n|:------|:------|:------|\n| 乙烷 |C2H6 |@@ccpp_questionnaire.ethane_design@@ |\n| 乙烯 |C2H4 |@@ccpp_questionnaire.ethylene_design@@ |\n| 丙烯 |C3H6 |@@ccpp_questionnaire.propylene_design@@ |\n| 丙烷 |C3H8 |@@ccpp_questionnaire.propane_design@@ |\n| 丁烯 |C4H8 |@@ccpp_questionnaire.butene_design@@ |\n| i-异丁烷 |iC4H10 |@@ccpp_questionnaire.i_isobutane_design@@ |\n| n-异丁烷 |nC4H10 |@@ccpp_questionnaire.n_isobutane_design@@ |\n| 戊烷 |C5H12 |@@ccpp_questionnaire.pentane_design@@ |\n| 碳6 |C6+ |@@ccpp_questionnaire.carbon6_design@@ |\n| 氢气 |H2 |@@ccpp_questionnaire.hydrogen_design@@ |\n| 氦气 |He |@@ccpp_questionnaire.helium_design@@ |\n| 氮气 |N2 |@@ccpp_questionnaire.nitrogen_design@@ |\n| 一氧化碳 |CO |@@ccpp_questionnaire.carbon_monoxide_design@@ |\n| 二氧化碳 |CO2 |@@ccpp_questionnaire.carbon_dioxide_design@@ |\n| 硫化氢 |H2S |@@ccpp_questionnaire.hydrogen_sulfide_design@@ |\n| 氧气 |O2 |@@ccpp_questionnaire.oxygen_design@@ |\n| 水 |H2O |@@ccpp_questionnaire.water_design@@ |","id":"j1_28"},{"class":["1","j1_18","j1_20"],"content":"##### 表1.2.2-1天然气物理性质表（暂无）按100%CH4计算\n\n| 高位发热量 |kJ/Nm3 |@@ccpp_questionnaire.high_calorific_value_design@@ |\n|:------|:------|:------|\n| 燃气价格 |元/Nm3 |@@ccpp_questionnaire.price_design@@ |","id":"j1_29"},{"class":["1","j1_18","j1_20"],"content":"##### 表1.2.2-2气象条件及海拔地质表按100%CH4计算\n\n| 当地平均海拔 |A |m |@@ccpp_questionnaire.local_avg_hight@@ |\n|:------|:------|:------|:------|\n| 年平均温度 |T0 |℃ |@@ccpp_questionnaire.year_avg_temperate@@ |\n| 夏季平均温度 |Ts |℃ |@@ccpp_questionnaire.summer_avg_temperate@@ |\n| 冬季平均温度 |Tw |℃ |@@ccpp_questionnaire.winter_avg_temperate@@ |\n| 年平均大气压力 |P0 |bar |@@ccpp_questionnaire.year_avg_press@@ |\n| 夏季大气压力 |Ps |bar |@@ccpp_questionnaire.summer_avg_press@@ |\n| 冬季大气压力 |Pw |bar |@@ccpp_questionnaire.winter_avg_press@@ |\n| 年平均相对湿度 |d |% |@@ccpp_questionnaire.year_avg_humidity@@ |","id":"j1_30"},{"class":["1","j1_18","j1_20"],"content":"##### (手动输入)","id":"j1_31"},{"class":["1","j1_18","j1_20"],"content":"##### 主要用于燃气轮机空气过滤器反吹和控制仪表用，仪表风质量要求为：压力0.6~1.0MPag, 储气罐出口压力下水露点≤－40℃, 颗粒≤0.5m ，绝对过滤精度≥99.9％，总颗粒含量≤0.05 mg/m3，油雾＝0.0 mg/m3。","id":"j1_32"},{"class":["1","j1_18","j1_20"],"content":"##### 市电的供电频率的最大允许偏差不超过±1Hz，供电电压的最大允许偏差不超过额定值的±10%。具体要求见中国《供电营业规则》。其中110kV变压站据项目所在地直线距离[手动输入]km。详细位置见下图。\n##### ![](http://117.36.73.154:6008/uploaded_file/1.1.2-2.jpg)\n##### 图1.2.6-1 110kV位置图\n","id":"j1_33"},{"class":["1"],"content":"##### 园区蒸汽总需求为@@ccpp_questionnaire.recent_steam_flow_range_1@@ t/h，目前电力需求为@@ccpp_questionnaire.electric_load_demand*0.8@@万kWh/年，且目前园区不断有企业入驻，电力方面有较大增长空间。","id":"j1_34"},{"class":["1"],"content":"","id":"j1_35"},{"class":["1","j1_35"],"content":"##### 本工程拟选厂址位于(手动输入)工业园内，具体选址待定。","id":"j1_36"},{"class":["1","j1_35"],"content":"##### 根据国家发改委、财政部、住建部、能源局联合发布的《关于发展天然气分布式能源的指导意见》（发改能源[2011]2196 号）提出的基本原则，“天然气分布式能源全年综合利用效率应高于70%，在低压配电网就近供应电力。发挥天然气分布式能源的优势，兼顾天然气和电力需求削峰填谷”。","id":"j1_37"},{"class":["1","j1_35","j1_37"],"content":"##### 本项目主设备的型式与容量的确定需要遵循以下原则：\n##### 1）按“以热定电、冷热电三联供”的原则配置能源系统机组容量；\n##### 2）充分考虑技术方案的可行性、运行可靠性和调节的灵活性；\n##### 3）能源的梯级利用和转换效率应达到国内先进水平；\n##### 4）在满足生产和施工安装的前提下，尽量节约用地；\n##### 5）在满足安全可靠的条件下，尽量选用技术先进、效率高的联合循环冷热电三联供发电机组。","id":"j1_38"},{"class":["1","j1_35","j1_37"],"content":"##### 本项目设计需依据以下文件\n##### 国家发改委、财政部、住建部、国家能源局等四部委《关于发展天然气分布式能源的指导意见》（发改能源[2011]2196 号）\n##### 《火力发电厂设计技术规程》(DL5000-2000)。\n##### 《火力发电厂初步设计文件内容深度规定》(DL/T5427-2009)。\n##### 《燃气-蒸汽联合循环电厂设计规定》(DL/T5174-2003)。\n##### 《小型火力发电厂设计规范》（GB50049-2011）   \n##### 国家、地方和行业其他相关的法律、法规、条例以及规程和规范","id":"j1_39"},{"class":["1"],"content":"##### 根据本项目的供能规模及特点，以燃气-蒸汽联合工艺为基础的区域式分布式能源系统非常适合本项目的建设。\n##### 燃气－蒸汽联合循环，热、电联供机组中，燃气轮机、余热锅炉、汽轮机的匹配原则一般是：余热锅炉的蒸发量与燃气轮机排出的烟气余热相匹配，汽轮机的进汽量与余热锅炉的蒸发量相匹配，以使能源的利用效率最大化。汽轮机可以是抽汽凝汽式，也可以是背压式，也可以根据用汽负荷不采用汽轮机。实际运行中，如果有一定的基本热负荷，且变化不大，应采用背压机，若热负荷有变化，则应采用抽凝式汽轮机，本项目根据经济原因不考虑汽轮机。\n##### 本项目蒸汽负荷相对比较稳定，故确定采用1台燃气轮机发电机组、1 台余热锅炉,1台燃气锅炉。不配汽轮机。\n##### 在国际燃气轮机市场中，能够制造燃气轮机的主要厂家有索拉公司、GE公司、德国的Siemens公司、瑞士ABB公司、日本三菱公司和日本的日立公司等。在国内燃气轮机市场中，能够制造燃气轮机的主要厂家有上海汽轮机有限公司、南京汽轮电机（集团）有限责任公司等。\n##### 在中小型民用燃机方面，索拉公司具有非常强的技术及售后服务、检修周期短等优势；在设计经验、价格和性能方面有很强的竞争力。且因为采用低氮燃烧技术，排放负荷国家标准要求。以下是燃机预期的排放值：\n\n| NOx氮氧化物 |38 ppmv (80 mg) |\n|:------|:------|\n| CO一氧化碳 |50ppmv (64 mg) |\n| UHC未燃烧总烃 |25 ppmv (18 mg) |\n\n##### 上述运行点工况排放值限定为：环境温度：(-17 ~48℃) 功率范围：50-100%环境温度：(-17 ~48℃)。SO2排放值取决于燃料中的硫含量。\n##### 目前陆上发电用燃气轮机有轻型和工业型两类可供选择。轻型燃气轮机系由航空燃气轮机派生，体积小，重量轻，设备部件精度高，对机组运行的环境条件要求也较苛刻。轻型燃气轮机起停迅速，单循环热效率较高，非常适宜于作调峰发电机组，如@@ccpp_ccpp.engine_model@@机型等。\n##### 本工程是热电联产的分布式能源电站，根据以热定电的原则，按照本项目平均蒸汽负荷匹配的机组总供热能力考虑运行可靠性和调节的灵活性，根据需求提供蒸汽h，若锅炉补燃可增加蒸汽产生量，但考虑到系统的经济性建议利用燃气锅炉调峰供给。前经过初步的热平衡计算，兼顾高效的特点，本工程建议选用@@ccpp_ccpp.engine_model@@型燃气轮机，余热锅炉选用余热锅炉或配合燃气调峰锅炉联合供汽。\n##### 本工程暂按@@ccpp_ccpp.engine_model@@燃机进行设计，燃机厂商最终将通过招标综合技术评比后确定。\n##### 燃气在燃气轮机燃烧做功发电后，烟气进入余热锅炉，产生蒸汽压力为@@ccpp_questionnaire.steam_pressure_level_1@@ bar，温度@@ccpp_questionnaire.steam_temperature_level_1@@℃；燃气锅炉和余热锅炉供蒸汽母管后，蒸汽直接供生产工艺用，增大能量的利用率。\n","id":"j1_40"},{"class":["1","j1_40"],"content":"##### 燃气轮机主要包含以下几个系统：燃气轮机主机是主要的动力的单元，拖动电机发电；启动系统用于燃气轮机的启动；燃料处理系统主要作用是处理进入燃气轮机的燃气以达到符合燃机的进气条件；润滑油系统为机械转动提供必要润滑油，油箱与底座一体化设计，为机组提供平整的支撑；透平空气进气系统用于处理进入燃气轮机的空气，以满足空气的清洁度要求；透平排气系统包括烟囱和排气消声器的用于处理透平排气；机罩包括通风系统，火焰检测及灭火系统，以及可燃气体检测等，为燃机的安全运行提供必要保护。燃机系统还包括控制系统以及撬上电缆等。\n","id":"j1_41"},{"class":["1","j1_40"],"content":"##### 燃气在燃气轮机内燃烧释放出来的高温烟气经烟道输送至余热锅炉入口，再流经过热器、蒸发器和省煤器，最后经烟囱排入大气，排烟温度一般为 150～180℃，烟气温度从高温降到排烟温度所释放出的热量用来使水变成蒸汽。锅炉给水首先进入省煤器，水在省煤器内吸收热量升温到略低于汽包压力下的饱和温度进入锅筒。进入锅筒的水与锅筒内的饱和水混合后，沿锅筒下方的下降管进入蒸发器吸收热量开始产汽，通常是只有一部分水变成汽，所以在蒸发器内流动的是汽水混合物。汽水混合物离开蒸发器进入上部锅筒通过汽水分离设备分离，水落到锅筒内水空间进入下降管继续吸热产汽，而蒸汽从锅筒上部进入过热器，吸收热量使饱和蒸汽变成过热蒸汽。根据产汽过程的三个阶段对应三个受热面，即省煤器、蒸发器和过热器，如果不需要过热蒸汽，只需要饱和蒸汽，可以不装过热器。当有再热蒸汽时，则可加设再热器。为利用150℃~180℃的烟气可考虑增设热水换热器，降低排烟温度，提高锅炉效率。\n","id":"j1_42"},{"content":"","id":"j1_43"},{"class":["1","j1_40"],"content":"##### 不同方案的对比\n##### 综合考虑园区用汽用电需求本项目的设计规模为：1套@@ccpp_ccpp.engine_model_design@@燃气轮机机组（配发电机）+1台额定蒸发量为@@ccpp_ccpp.low_superheater_effluent_smoke_enthalpy_design@@单压余热锅炉；该套机组在标准工况时的总发电量约为@@ccpp_ccpp.engine_power_design@@MW； @@ccpp_ccpp.high_terminal_temperature_difference_design@@MPa， @@ccpp_ccpp.high_steam_enthalpy_design@@℃的蒸汽供应量约为20t/h， \n##### 1）燃气轮机主要参数\n##### 型号： @@ccpp_ccpp.engine_model_design@@\n##### 台数：@@ccpp_ccpp.engine_num_design@@台\n##### 冷却方式：空气冷却\n##### 表4.3-1Centaur40燃气轮机参数表（标准工况）\n\n| 项目 |单位 |数值 |\n|:------|:------|:------|\n| 单台设计工况出力 |kW |@@ccpp_ccpp.engine_power_design@@ |\n| 热耗率 |kJ/kWh |@@ccpp_ccpp.engine_heat_consmption_rate_design@@ |\n| 发电效率 |% |@@ccpp_ccpp.engine_efficiency_design@@ |\n| 天然气耗量(单台) |Nm3/h |@@ccpp_ccpp.individual_gas_consumption_design@@ |\n| 天然气总耗量 |Nm3/h |@@ccpp_ccpp.individual_gas_consumption_design*ccpp_ccpp.engine_num_design@@ |\n| 排烟流量 |t/h |@@ccpp_ccpp.engine_exhuast_gas_flux_design@@ |\n| 排烟温度 |℃ |@@ccpp_ccpp.engine_exhuast_gas_temperature_design@@ |\nccpplogic[0]\n##### 型号：QC\nccpplogic[1]\nccpplogic[2]\nccpplogic[3]\nccpplogic[4]\nccpplogic[5]\nccpplogic[6]\nccpplogic[7]\nccpplogic[8]\n##### 台数：1台\n##### 4）发电机主要参数\n##### 型 号：@@ccpp_ccpp.engine_model_design@@\n##### 功 率：@@ccpp_ccpp.engine_power_design@@ kW\n##### 电 压：10.5kV\n##### 额定频率：50Hz\n##### 相数：\t3\n##### 功率因数：0.8\n##### 冷却方式：\n##### 转 速：3000r/min\n##### 数 量：1台\n##### 系统参数如下表所示\n##### 表4.3-2 Centaur40燃气轮机发电机组参数表\n\n| 项目 |数值 |\n|:------|:------|\n| 燃机发电量（kW） |@@ccpp_ccpp.engine_power_design@@ |\n| 单套机组气耗量（Nm3/h) |@@ccpp_ccpp.individual_gas_consumption_design@@ |\n| 机组年供蒸汽（t） |@@ccpp_ccpp.high_gas_production_design@@ |\n| 机组年总发电量（万kWh) |@@ccpp_ccpp.engine_power_design*0.8@@ |\n| 联合循环机组总热效率（%） | |\n| 机组年耗气量(万Nm3) |@@ccpp_ccpp.individual_gas_consumption_design*8000@@ |\n| 全厂发电气耗（Nm3/kWh） |@@ccpp_ccpp.individual_gas_consumption_design*8000/ccpp_ccpp.engine_power_design*0.8@@ |\n| 全年平均热电比（%） | |\n","id":"j1_44"},{"class":["1"],"content":"","id":"j1_45"},{"class":["1","j1_45"],"content":"##### 燃气轮机可用的燃料通常为天然气、柴油、重油或原油。天然气作为一种高效清洁能源，是燃气轮机的理想燃料。本能源站所使用的燃料为天然气，因其是洁燃料且采用低氮燃烧技术，燃烧后排放的污染物小，相对于其它燃料，对环境的影响也比较小。且根据已有资料，供用气气源采用管道气，燃料供应是有可靠保障的。请业主及时与天然气公司签订天然气供销合同以保证项目实施、运行。由于暂无天然气压力资料，本项目暂按设置天然气增压系统考虑。本工程不考虑备用燃料。","id":"j1_46"},{"class":["1","j1_45"],"content":"##### 本工程燃气轮机所需天然气压力应不低于3585±138kPa(g），为了保证供气压力，厂内设置天然气增压站，天然气增压站由入口紧急切断单元、粗过滤单元、分离/过滤冷凝存储单元、计量单元、调压单元、出口单元和放散单元组成。由厂外送来的天然气，经过计量、粗分离、精过滤、加热，调压后送至燃机的入口。本工程燃机设置1座调压装置，采用半露天室外布置。当燃气轮机或锅炉区域发生火险时，事故紧急气动（弹簧关闭）阀将自动关闭以阻止天然气进入厂房，为保证天然气管道的安全泄放，天然气管道上设有放散系统。","id":"j1_47"},{"class":["1","j1_45"],"content":"##### 为保证燃机对天然气压力稳定性的要求，红线内设天然气调压站（撬装式）一座。调压站含入口单元、计量单元、过滤单元、换热单元、备用换热单元、燃气调压单元、热水锅炉调压单元、冷凝储罐单元、色谱仪等，配套设天然气放散装置。\n##### 为保证燃机对天然气成分和污物的要求，预留过滤单元作为燃气处理设施。\n##### 为保证燃机对天然气供气温度的要求，设燃气热水锅炉，该锅炉用天然气压力0.11MPa。待系统正常运转后，可用蒸汽换热热水，继而加热天然气，达到调温节能的目的。\n##### 设2套（1用1备）调压系统，同时为燃气热水锅炉设1套调压系统。通过上述方案，保证后续系统的稳定可靠。经调压后的天然气管道一一对应燃机和锅炉，通过架空管道送至各用户点。\n##### 天然气系统检修吹扫、安全阀放散等，统一接到放散管对空放散。\n##### 本系统满足燃气轮机对燃气的温度和压力的需求，亦要满足安全需要。\n","id":"j1_48"},{"class":["1"],"content":"##### 燃烧系统主要由燃气轮机和余热锅炉的烟气系统构成。空气由燃气轮机的进气装置(内部设有过滤器和消声器)引入压气机压缩后，进入环绕在燃机主轴上的分管式燃烧室。天然气经过调压站分离、过滤、调压后进入燃机天然气前置模块的计量、加热、再过滤后，与进入燃烧室的压缩空气进行预混，通过燃料喷嘴喷入燃烧室后燃烧，燃烧后的高温烟气进入燃气轮机膨胀作功，带动燃气轮机转子转动，拖动发电机发电。\n##### 作功后的烟气温度依然很高，高温烟气通过烟道进入余热锅炉。在这里，高温烟气加热锅炉给水产出蒸汽去送往用户，烟气中的热量被充分吸收和利用，最后冷却后的烟气经余热锅炉的主烟囱排入大气。\n##### 为了提高锅炉效率，降低排烟温度，本期工程将扩大余热锅炉低压省煤器的面积来吸收烟气中的余热。\n##### 设有氮气吹扫系统，采用外购氮气瓶做燃机燃料气管线吹扫用气。\n\n","id":"j1_49"},{"class":["1","j1_49"],"content":"","id":"j1_50"},{"class":["1","j1_49"],"content":"##### 本工程给水系统（含给水泵）由余热锅炉厂设计并供货，给水系统采用单元制，每台余热锅炉设置2台100%容量的给水泵，两台给水泵互为备用，设置一台变频器控制。\n##### 在给水泵出口设有最小流量回路，以保证起动和低负荷期间给水泵通过最小流量运行，防止给水泵汽化。","id":"j1_51"},{"class":["1","j1_49"],"content":"##### 凝结水系统是将从用户返回的凝结水和可以回收利用的管路凝结水加热并输送至凝结水母管后分别送入余热锅炉和燃气调峰锅炉的低压省气器再经低压给水操作台进入锅炉蒸汽除氧器，在此过程中，凝结水被加热、除氧。另外本系统还为各种系统提供补给水和其他用水。\n##### 凝结水系统采用母管。余热锅炉设2 台100%容量的凝结水泵，1运1备。每台凝结水泵的容量拟按照满足最大工况下的凝结水流量的110%。当任何1台泵发生故障时，备用泵自动启动投入运行。\n##### 在系统运行的过程中会有汽水损失，需要提供补充软化水，软水制取有专门的制取装置，此补水补充到除氧器，经除氧后送进如锅炉。","id":"j1_52"},{"class":["1","j1_49"],"content":"##### 本项目循环水采用带机力通风冷却塔的二次循环供水系统。开式循环冷却水系统中的冷却水为循环水，采用单元制设置。开式循环冷却水取自主厂房内循环水供水母管，向闭式循环冷却水热交换器、空气压缩机等提供冷却水。排水接至循环水回水母管。定排坑冷却水采用工业水进行冷却。\n##### 闭式循环冷却水系统主要向下列设备提供冷却水：燃机岛设备（燃气轮机润滑油冷却器，发电机的空气冷却器等）。 本系统的水源为化学除盐水，采用单元制设置。系统设1套闭式水集装装置，内含2台100%容量的闭式循环冷却水泵、2台闭式冷却水热交换器和1台膨胀水箱。正常运行时，一台冷却水泵和一台热交换器运行可满足整个系统所需的冷却水量。","id":"j1_53"},{"class":["1","j1_49"],"content":"##### 本工程额定工业热负荷@@ccpp_ccpp.sp_low_gas_production_design*1.1@@t/h，凝结水按70%回收率考虑。根据《小型火力发电厂设计规范》，可计算化学水处理系统出力：\n##### 1）锅炉额定蒸发量：@@ccpp_ccpp.sp_low_gas_production_design*1.1*1@@锅炉额定蒸发量t/h\n##### 2）厂内汽水循环正常损失： @@ccpp_ccpp.sp_low_gas_production_design*1.1*0.03@@厂内汽水循环正常损失t/h\n##### 3）锅炉正常排污损失：@@ccpp_ccpp.sp_low_gas_production_design*1.1*0.02@@水处理系统耗水量t/h\n##### 4）水处理系统耗水量：@@round(ccpp_ccpp.sp_low_gas_production_design*1.1*0.03, 0)@@水处理系统耗水量取整t/h\n##### 5）其它不可预计用水损失：@@round(ccpp_ccpp.sp_low_gas_production_design*1.1*0.03, 0)@@其它不可预计用水损失t/h\n##### 6）启动或事故增加用水量：@@ccpp_ccpp.sp_low_gas_production_design*1.1*0.1@@t/h\n##### 7）外供汽损失：@@ccpp_ccpp.sp_low_gas_production_design*1.1*0.3@@外供汽损失t/h\n##### 8)锅炉补给水处理系统正常出力：厂内汽水循环正常损失：+锅炉正常排污损失+水处理系统耗水量+其它不可预计用水损失：+外供汽损失t/h =12.8t/h\n##### 9）锅炉补给水处理系统最大出力：厂内汽水循环正常损失：+锅炉正常排污损失+水处理系统耗水量+其它不可预计用水损失：+外供汽损失+启动或事故增加用水量t/h =16.4 t/h\n##### 本工程化水系统除盐水站出力按(锅炉补给水处理系统正常出力+锅炉补给水处理系统最大出力)/2t/h计，设置一个有效容积为(锅炉补给水处理系统正常出力+锅炉补给水处理系统最大出力)2.5取整m3的除盐水箱，启动或事故增加的水量由除盐水箱补给。\n##### 化水系统工艺流程：\n##### 水源来水→原水箱→原水泵→多介质过滤器→活性炭过滤器→保安过滤器→高压泵→反渗透装置→除二氧化碳器→中间水箱→中间水泵→混合离子交换器→除盐水箱→除盐水泵→各用水点。\n","id":"j1_54"},{"class":["1","j1_49"],"content":"##### 本项目为园区企业供气，管网建设依据园区具体要求采用地上桥架或地下埋管；管网建设到企业红线外1m预留接口，并配阀门及流量表。","id":"j1_55"},{"content":"","id":"j1_56"},{"class":["1"],"content":"##### 本项目设1套润滑油系统。油箱与底座一体；燃机润滑油系统由主润滑油泵(交流电动机驱动)、满载辅助润滑油泵(交流电动机驱动)、事故油泵(直流电动机驱动)、润滑油板式冷油器(2×100%)、双联滤油器、油箱(包括油烟分离器、排油烟风机、电加热装置)、交流电动机驱动的密封油真空泵等组成。系统向燃气轮机及其发电机轴承供给润滑油，保证机组的正常运转。燃机的主油箱均带有电加热器及温控设备，用于机组冷态启动时保证润滑油正常油温。\n##### 润滑油系统的配置以主机厂家最终资料为准。\n","id":"j1_57"},{"class":["1"],"content":"##### 厂内10kV系统中性点采用消弧线圈接地或不接地方式。低压系统中性点采用直接接地方式。\n##### 10kV直供电电源在燃机发电机出口通过限流电抗器引接，相应地分别设一段10kV直供电线。本10kV直供电系统给经开区内部分就近户供电。 \n##### 机组10kV厂用电均采用单母线接线。燃机发电机组的厂用电在相应的10kV直供电系统引接，其所需厂用电由相应的燃机厂用电系统提供。\n##### 低压厂用电分为PCC和MCC两层。PCC采用暗备用方式，向各MCC供电。各MCC采用放射式方式向用户供电。主工艺系统MCC采用单母 线双电源自动切换接线，个别辅助设施的MCC采用单母线单电源接线。","id":"j1_58"},{"class":["1","j1_58"],"content":"##### 本能源站机组主要电气设备参数分别如下：\n##### 1）燃气轮机发电机 \n##### 额定功率@@ccpp_ccpp.engine_power_design@@kW\n##### 额定电压\t10.5kV\n##### 额定电流@@ccpp_ccpp.engine_power_design/10.5@@ A\n##### 额定功率因素\tcosΦ=0.8；\n##### 2）直供电限流电抗器（核算后确定）\n##### 型号：XKK-10-1500-6\n##### 3）厂用电限流电抗器（核算后确定）\n##### 型号：XKK-10-300-3\n##### 4）10kV高压开关柜：\n##### 户内中置式高压开关柜\n##### 额定电压 12kV\n##### 额定电流\t630~2000A\n##### 开断电流\t31.5kA\n##### 5）低压厂用变压器\n##### 额定容量1250kVA\n##### 额定电压\t10/0.4kV\n##### 短路阻抗Ud=6%\n##### 接线组别D/yn11\n##### 6）0.4kV低压开关柜\n##### 户内固定式\n##### 额定电压\t0.4kV\n##### 额定电流\t100~3000A\n##### 开断电流\t50kA \n","id":"j1_59"},{"class":["1","j1_58"],"content":"##### 燃气轮机升压变压器及10kV直供电系统及厂用电10kV配电装置布置在燃气轮机区域。其余辅助设施的电气设备布置在相应工艺系统的附属小电气室内。","id":"j1_60"},{"class":["1","j1_58"],"content":"##### 直流负荷包括高压开关操作电源、直流电源、保护控制电源、直流油泵和事故照明等。直流供电的电压为220V。直流系统采用一套200Ah免维护铅酸蓄电池组。直流电源装置采用微机型相控成套直流电源装置，蓄电池采用1×200Ah阀控密封免维护铅酸蓄电池，配置两台逆变器。该直流装置配有微机型直流绝缘在线监测装置，能对所有的直流负荷进行接地故障监测，并能监测直流母线电压信号，在母线欠压、过压或接地时均能发出报警信号。\n##### 继电保护及自动装置、测量仪表按照《继电保护和安全自动化装置技术规程》、《电测量仪表装置设计技术规程》、《火力发电厂、变电所二次接线设计规程》、《防止电力生产重大事故的二十五项重点要求》、《火力发电厂厂用电设计技术规程》等有关规定配置。所有保护采用微机保护继电器，发电机的保护及测控装置组屏安装，其它保护均安装在对应的开关柜内。 能源站厂设置有电气监控系统，负责监控能源站发变组、以及厂用电等电气系统设备。本能源站另外设置有DCS控制系统。 \n##### 继电保护按国标GB/T 50062-2008 《电力装置的继电保护和自动装置设计规范》要求配置。\n##### 1）发电机保护：\n##### 发电机失步解列保护\n##### 纵差保护\n##### 复合电压过电流保护\n##### 90%定子接地保护（按规范允许单相接地运行两小时）\n##### 定子绕组过负荷保护\n##### 转子一点、二点接地保护\n##### 逆功率保护\n##### 发电机失磁保护\n##### 2）低压厂用变压器\n##### 限时速断保护\n##### 过流保护\n##### 温度保护\n##### 3）高压电动机\n##### 电流速断保护\n##### 过电流保护\n##### 单相接地保护\n##### 4）同期系统采用微机自动准同期装置，手动准同期装置。\n","id":"j1_61"},{"class":["1","j1_58"],"content":"##### 过电压保护及接地按照《火力发电厂和变电所防雷接地设计技术规定》执行，采用措施防止直击雷、入侵波以及各种原因引起的过电压对电气设备的危害。\n##### 全厂接地采用计算机接地与设备接地共用的联合主接地网方式， 接地电阻按0.5欧姆(<2000/I)设计。独立避雷针设置集中接地装置，其接地电阻不大于10欧。","id":"j1_62"},{"class":["1","j1_58"],"content":"##### 全厂照明采用动力和照明共用的380/220V供电方式，事故照明由直流屏供电。\n##### 全厂设交流低压检修网络，电源由380/220V低压厂用系统供电。\n##### 1）事故照明\n##### 主厂房事故照明由直流220V供电。\n##### 远离主厂房的辅助车间事故照明采用应急灯。\n##### 主厂房出入口、通道等人员疏散口处，设有安全标志灯。\n##### 2）检修网络\n##### 主厂房内采用固定的三相五线制电源放射形低压检修网络，检修箱电源分别由低压段回路供电。\n##### 主厂房配电室、电子设备间、值班室设立应急照明，在电源突然失电状态下，主厂房配电室、电子设备间、值班室事故照明能够实现自动切换，应急照明自动启动。","id":"j1_63"},{"class":["1","j1_58"],"content":"##### 厂内通信包括全厂行政及调度通信，调度交换机和程控交换机预留与上级调度设备（光通讯设备和载波通讯设备）的通信接口。","id":"j1_64"},{"class":["1","j1_58"],"content":"##### 电缆设施按照《电力工程电缆敷设设计规范》执行，地下部分采用电缆隧道、电缆沟、电缆管井等结合的敷设方式，架空部分采用电 缆桥架、支架等敷设方式。\n##### 电缆防火采用设置阻火墙、阻火隔层、涂刷防火涂料等措施。","id":"j1_65"},{"class":["1"],"content":"","id":"j1_66"},{"class":["1","j1_66"],"content":"##### 能源站选用炉的给水、炉水及蒸汽质量标准为：\n##### 表11.1-1 锅炉给水质量表\n\n| 项目 |指标 |单位 |\n|:------|:------|:------|\n| 硬度 |~0 |μ mol/L |\n| 溶解氧 |≤7 |μg/L |\n| 铁 |≤20 |μg/L |\n| 铜 |≤5 |μg/L |\n| 联氨 |≤30 |μg/L |\n| 二氧化硅 |应保证蒸汽中二氧化硅符合标准 |应保证蒸汽中二氧化硅符合标准 |\n| pH（25℃） |8.8~9.3 | |\n| 氢电导率（25℃） |≤0.3 |μS/cm |\n\n##### \n\n##### 表11.1-2蒸汽质量表\n\n| 项目 |指标 |单位 |\n|:------|:------|:------|\n| 钠 |≤15 |μg/kg |\n| 二氧化硅 |≤20 |μg/kg |\n| 铁 |≤15 |μg/kg |\n| 铜 |≤3 |μg/kg |\n| 氢电导率（25℃） |≤0.15 |μS/cm |\n\n##### 表11.1-3 锅炉炉水质量表\n\n| 项目 |指标 |单位 |\n|:------|:------|:------|\n| 磷酸根 |≤3 |mg/L |\n| pH（25℃） |9~9.7 | |\n\n##### 表11.1-4 凝结水质量表\n\n| 项目 |指标 |单位 |\n|:------|:------|:------|\n| 硬度 |≤1.0 |μmol/L |\n| 溶解氧 |≤40 |μg/L |\n| 氢电导率（25℃） |≤0.3 |μS/cm |\n\n##### 为满足机组对给水水质的要求，本化学水处理拟选用两级反渗透+EDI系统。化学水处理系统主要工艺包括预处理系统、预除盐系统、精除盐系统、化学清洗及反渗透冲洗系统等。\n##### 预处理过滤系统主要由原水箱、原水泵、浓水箱、多介质过滤器、活性炭过滤器、过滤器反洗泵及加药系统等组成，在工艺中主要对原水中的浊度、有机物、胶体及硬度进行处理，经此处理后出水水质达到反渗透装置的进水水质要求。\n##### 预除盐系统主要由一级保安过滤器、一级高压泵、一级反渗透装置、一级水箱、中间水泵、PH调整装置、二级保安过滤器、二级高压泵、二级反渗透装置、反渗透清洗装置等组成。反渗透系统主要去除水中大部分溶解盐类。\n##### 精除盐系统由EDI脱盐系统完成，主要由EDI 提升泵、EDI保安过滤器、EDI装置、纯水箱、纯水泵、加氨装置、EDI清洗装置组成，其作用是去除二级反渗透产水中残余的离子。\n##### 除盐水送出及其它配套设备包含除盐水泵、加氨装置、压缩空气储气罐、除盐水系统控制、仪表、阀门管道等。\n","id":"j1_67"},{"class":["1","j1_66"],"content":"##### （1）生水箱\n##### 生水箱起到贮存生水，调节水量的作用，设置生水箱一座，有效容积为35m3，采用钢结构，内防腐，地上布置。\n##### （2）生水泵\n##### 按照一对一，方便操控的原则，本工程设置生水泵1台，1用1备，为后序系统提供稳定的工作压力和水量。\n##### （3）多介质过滤器\n##### 多介质过滤器是反渗透系统的重要预处理装置，它的作用是去除原水中的细小颗粒、悬浮物、胶体等杂质，保证其出水SDI（污染指数）≤4提高反渗透入水品质。设置3台多介质过滤器，两用一备，当过滤器在进出口压差达到一定值或达到累计流量时，则应退出使用进行反洗，保证两台正常运行，以确保稳定的出水水质。多介质过滤器中填充滤料包括石英砂、磁铁矿及无烟煤。\n##### （4）活性炭过滤器\n##### 为了保证RO系统的长期运行和设备的使用寿命进一步降低RO进水的污染指数，预处理系统设置了活性碳过滤器，内装高效净水活性碳，能有效吸附去除原水的有机物和原水中的氯根，并使进RO系统中FI≤3。\n##### 活性炭过滤器为带有椭圆形封头的圆柱形筒体装置。筒体上部设有进水装置，下部设有排水装置，运行时，水经上部进入，流经滤层，从底部流出。过滤器包括进出水阀、排水阀、反冲洗阀、排气阀等；过滤器设有反洗窥视镜，人工取样阀等。运行自动反洗为手动反洗。\n##### （5）阻垢剂加药装置\n##### 为了保证膜元件表面不结垢，保证膜的长期运行效果，延长膜的使用寿命，本工艺在反渗透装置前设置阻垢剂加药装置，通过投加六偏磷酸钠，以防止反渗透膜的结垢，来提高反渗透的产水量和有利于防止反渗透膜上生成沉淀物，加药量一般为3-5mg/L。\n##### （5）保安过滤器\n##### 保安过滤器的作用是保护反渗透膜，每台保安过滤器选用316L材质，滤芯采用进口聚丙烯材质产品。每台保安过滤器的结构可以快速更换芯。\n##### （7）高压泵\n##### 高压泵的作用是为反渗透本体装置提供足够的进水压力，以保证系统达到设计要求的产水量。每套反渗透装置配1台变频高压泵，高压泵出口应装设自动慢开门和压力开关，压力高时报警及停泵。\n##### （8） 反渗透装置\n##### 反渗透装置是本系统中最重要的脱盐装置，经过预处理的水，在系统中被高压泵加压后，在多段膜中可脱除98%以上的盐分，并可去除绝大部分的胶体、有机物、微生物、色素等杂质，系统水回收率可达到75%。\n##### 经过预处理后的合格的生水进入反渗透系统后，水分子和极少量的有机物通过反渗透膜层，经收集管道集中后，经产水管注入中间水箱，反之不能通过的就经由另一组收集管道集中后通往浓水排放管排放。系统的进水、产水和浓水管道上都装有一系列的控制阀门，监控仪表及程控操作系统，这样可以很好的保证设备系统化运行。\n##### （9）反渗透清洗装置\n##### 经过长期运行，反渗透膜面上会积累各种污染物，从而降低反渗透装置的性能（产水量和脱盐率），进水与浓水压差升高。因此除日常的低压冲洗外，还需设置一套清洗装置，定期进行化学清洗，一般半年应进行一次。\n##### 本系统配置一套化学清洗装置，其流程如下：\n##### 清洗水箱 → 清洗泵 →  清洗过滤器  →  反渗透装置\n##### ↑                                    ↓\n##### （10）混合离子化水部分\n##### 采用一套混合离子交换器，对反渗透处理后的水进行软化处理。离子交换工艺具有对一般硬度水质的适应性强，出水水质好且稳定的特点。流量控制再生，双罐系统，保证连续出水。通过对产水量精确计算，准确控制再生时间和程度，即使在出水量变化较大也不影响出水质量，确保用水设备安全运行。\n##### （11）除盐水箱\n##### 除盐水箱起到贮存除盐水，调节水量的作用，设置除盐水箱1台，有效容积为40m3。\n##### （12）除盐水泵\n##### 本工程除盐水泵分为电厂用除盐水泵和外供除盐水泵，电厂用除盐水泵2台（1用1备），保证为除氧器提供稳定的工作压力和水量。\n##### （12） 压缩空气系统\n##### 与系统共用一套压缩空气系统。空气压缩系统由压缩机，干燥机，缓冲罐，过滤器、分气缸等设备构成。\n","id":"j1_68"},{"class":["1","j1_66"],"content":"##### 1.）炉水加磷酸盐系统\n##### 本工程对炉水采用磷酸盐阻垢处理，手动加药。加药泵为电控计量泵，炉水磷酸盐加药量结合给水流量和炉水磷酸根量大小进行调整。本工程设一套组合加药装置，共设2台溶液箱，2台计量泵，加药点给水设在锅炉汽包内。\n##### 2) 化学加药系统设备布置\n##### 加氨装置布置于化学水处理车间；加磷酸盐装置布置于锅炉房，加药间设机械通风，设配制药液的除盐水管，有加药间冲洗设施和药品贮存设施。\n##### 3)汽水取样\n##### 根据化学监督要求，锅炉汽水取样采用分散就地汽水取样装置。汽水监测皆由人工化验，不设监测仪表。汽水取样点设置如下：\n##### \n\n##### 表11.3-1  汽水取样点设置表\n\n| 取样点名称 |取样点位置 |监督项目 |\n|:------|:------|:------|\n| 除氧器后给水 |给水箱出口管 |测溶氧 |\n| 省煤器进口给水 |省煤器进口 |测导电度、PH值 |\n| 炉水 |按锅炉厂要求 |测导电度、PH值 |\n| 饱和蒸汽 |按锅炉厂要求 |测导电度 |\n| 过热蒸汽 |按锅炉厂要求 |测钠离子 |\n| 凝结水 |凝结水箱出口 |测溶氧、导电度 |\n","id":"j1_69"},{"class":["1"],"content":"##### 根据工艺配置，热工自动化主要完成对进行整个装置的过程参数的检测、监视及控制。本能源站采用一套知名品牌的过程控制系统（DCS）作为主控系统，实现对余热锅炉及配套公辅设施自动监视和控制，保证装置的安全和经济运行。主要完成生产过程的数据采集和处理，数据显示和记录，数据设定和生产操作，执行对生产过程的连续调节控制和逻辑顺序控制，运行人员在控制室内通过HMI进行监控，并在现场人员的配合下完成机、炉、电及其辅助系统的启、停、正常运行及异常工况处理。除此之外，在控制室还设有必要的紧急停机按钮，用于机组故障时的安全停机。\n##### 装置DCS控制系统拟采用一套冗余控制器，完成烟气余热锅炉以及循环水站、天然气调压站、供配电等公辅设施1套。通讯网络采用冗余网络，DCS控制系统预留与外部的通讯接口。\n##### 燃气轮机本体仪表及GTC控制系统由燃气轮机厂成套供货，除盐水站本体仪表及PLC控制系统由除盐水制备厂家成套供货，各子系统预留与DCS系统之间的通讯接口，燃机发电系统的过程参数以通讯方式送至DCS进行监视。涉及调节、联锁、控制的信号，采用硬接线方式进行交接，信号遵循输出方隔离原则。","id":"j1_70"},{"class":["1","j1_70"],"content":"","id":"j1_71"},{"class":["1","j1_70","j1_71"],"content":"##### 控制的基本策略是直接快速地响应负荷、测点信息及操作指令，并做适当的抗干扰滤波，提高信息的可靠性。对信号进行动态补偿是信息更为精确度，对一些信号进行必要的前馈处理，并通过闭环反馈控制，使被控物理量达到稳定可靠，更符合实际。\n##### 控制系统设有联锁保护功能，以防止控制系统错误的、危险的动作，如系统某一部分必须具备的条件不能满足时，联锁逻辑应阻止该部分投入“自动”方式；同时，在条件不具备或系统故障时，系统受影响部分不再继续自动运行，将控制方式转换到手动控制方式。\n##### 控制系统任何部分运行方式的切换，不论是人为的还是由联锁系统自动的，均可平滑进行，而不引起过程变量的扰动，且不需运行人员的修正。\n##### DCS控制系统由若干个子系统组成，这些子系统协调运行，并具有前馈调节功能，使机组能安全、快速与稳定的运行，保证在任何工况下，满足机组正常运行。\n","id":"j1_72"},{"class":["1","j1_70","j1_71"],"content":"##### 设燃气调温调压装置，以确保煤气压力的稳定，流量的充分供应，燃烧值等技术指标要靠天然气源确保，并满足调压装置的额定参数，经DCS控制系统进行自动调节，燃机才能正常运行，这是保证机组可靠稳定运行的最重要的条件之一，因而， 压力、流量要进入DCS控制系统，分别进行天然气压力、流量的PID自动调节，实时监控。如供气方气源出现异常及故障，为确保机组安全，要及时通知到电厂有关人员。\n","id":"j1_73"},{"class":["1","j1_70","j1_71"],"content":"##### 蒸汽母管压力恒定是表征燃气轮机废气量，补燃量与锅炉产汽量平衡的的标志。运行中维护蒸汽母管压力恒定，是系统稳定运行的重要环节之一。\n##### 蒸汽母管压力恒定控制，采用母管压力自动调节控制母管压力。在燃气轮机负荷或补燃量变化时，母管压力出现瞬时阶跃，而调节信道的迟延较大，被控对象信道与调节信道的动态特性甚为悬殊，对调节很不利，因此采用经压力、温度补偿后的蒸汽流量信号作为前馈信号，以克服调节信道的迟延。母管压力调节的输出和蒸汽流量前馈信号叠加后作为对并列运行锅炉总的能量需求。\n","id":"j1_74"},{"class":["1","j1_70","j1_71"],"content":"##### 锅炉给水控制系统是通过锅炉汽包水位定值控制，实现锅炉给水量的控制。锅炉汽包水位自动控制回路采用“串级三冲量”控制方式，汽包水位为定值控制，以汽包水位为主冲量，辅助冲量蒸汽流量为前馈量，辅助冲量给水流量为反馈量，调节给水电动阀门，这样，迅速消除由于蒸汽负荷扰动所产生的“虚假液位”现象，提高了控制回路的调节品质。\n##### 三冲量的测量及补偿方式：\n##### (1)汽包水位测量，为是水位测量真实，排除汽包水位膨胀假象，要考虑水位试验取样，汽包水位零刻度修正。还要采用二台差压变送器，取其加权平均值，并进行数字滤波处理，结合汽包水位测量，经补偿修正形成汽包水位信号。\n##### (2)主汽流量经温度和压力补偿处理，结合主汽流量测量，形成主蒸汽流量。\n##### (3)给水流量及减温水流量经温度补偿后形成给水流量。\n","id":"j1_75"},{"class":["1","j1_70","j1_71"],"content":"##### 通过调节除氧器进汽调节阀开度，控制除氧器进汽量，保持除氧器压力为恒定值，以除氧器压力为被调量，采用单回路PID调节回路，给定值由操作员手动设置。\n##### 除氧器水位控制采用连续水位测量，给定值由控制系统自动(或操作员手动)设置，PID单回路调节除氧器进水阀开度，控制除氧器的进水流量，保持除氧器水位为恒定值。\n","id":"j1_76"},{"class":["1","j1_70"],"content":"##### 1、燃气轮机安全保护系统是一个燃烧器管理和燃料安全联锁系统。该系统从功能上分为：燃料安全系统(FSS)、燃烧器控制系统(BCS)两大部分。BCS接受FSS的闭锁，并且将有关信号反馈至FSS，二者相辅相承，构成一个有机整体。它能在燃气轮机启动停止和正常运行等方式下，连续监视燃烧系统的参数与状态，并且进行逻辑运算和判断，通过联锁装置使燃烧设备中的有关执行机构按照既定合理程序完成必要的操作或及时消除事故隐患，保证燃气轮机及燃烧系统的安全，同时防止运行人员操作失误及设备故障引起爆炸，提高燃气轮机运行的可靠性，避免发生事故，减少经济损失。\n##### 2、FSSS系统的作用\n##### 能自动完成各种操作；执行人工操作来不及的安全保护动作；避免运行人员的误操作。主要体现在下列几个方面：\n##### ·吹扫完成及有关条件满足之前，阻止燃料进入燃气轮机。\n##### ·监视燃气轮机的运行工况，在检测到危害人员和设备安全的工况时，发出主燃料跳闸(MFT)信号。\n##### ·当发现危害工况时，停运全部或部分已投运的燃气轮机燃烧设备和有关辅助、快速切断进入燃气轮机的燃料。\n##### ·MFT发生后，维持燃气轮机进风量，以清除燃气轮机和烟道中可能积聚的可燃混合物。\n","id":"j1_77"},{"class":["1","j1_70"],"content":"##### 1、总原则\n##### (1)燃气轮机联锁保护的设计为任意一个原因发生时，则燃气轮机停机的逻辑关系。\n##### (2)除紧急停机按钮外，任意一个原因或停机动作，则均在DCS系统上设置旁路软开关，方便操作人员。\n##### (3)所有原因发生后，均需通过DCS系统软件复位按钮确认后才可重新投入。\n##### 2、锅炉联锁原因及条件\n##### (1)紧急停炉按钮按下。\n##### (2)汽包水位高联锁：当两台汽包水位测量差压变送器的测量信号均高高时。\n##### (3)汽包水位低联锁：当两台汽包水位测量差压变送器的测量信号均低低时。\n##### (4)主蒸汽压力高联锁：当主蒸汽压力测量压力变送器的测量信号高高时。\n##### (5)引风机故障停机时。\n","id":"j1_78"},{"class":["1","j1_70"],"content":"##### 本工程采用机炉电集中控制。操作员站，工程师站，工业电视，打印机等布置在机炉电集中控制室内。过程控制机柜、热控配电柜、电气机柜、安放在机柜室内。\n","id":"j1_79"},{"class":["1","j1_70"],"content":"##### 为了满足生产的要求，监视设备的运行情况，在本项目中设立如下工业电视系统：\n##### 锅炉汽包水位电视监控系统2个摄像头，2个显示器，专业监视器42寸。锅炉汽包及集箱就地压力表引至水位计附近，利用摄像头进行就地监控。\n##### 配置一套工业电视监控系统，2个显示器，专业监视器42寸，摄像头为网络高清摄像头。\n","id":"j1_80"},{"class":["1","j1_70"],"content":"##### 电源是热控设备的动力，是机组安全运行的保证，必须保证供电电源的可靠性。\n##### 分散控制系统(DCS)系统要求提供两路电源：一路来自交流不停电电源(在线式UPS 220V AC)；另一路来自低压厂用母线(220V AC)。在机柜间内配有电源自动切换装置自动完成柜内设备所需电源的配电。控制室内的设备供电由UPS电源提供，断电后持续运行时间不少于30分钟。\n##### 仪表气源\n##### 气动阀门需要的气源采用氮气或压缩空气，全厂共用一套空气压缩系统。\n","id":"j1_81"},{"class":["1"],"content":"","id":"j1_82"},{"class":["1","j1_82"],"content":"##### 本工程规划1台燃机配1台余热锅炉另外布置一台燃气锅炉，燃机为轴向排气，余热锅炉与燃气轮机以组同轴线连续布置，拟依次平行布置，余热锅炉采用露天布置，满足辅助设备布置及通道要求，锅炉设有旁路烟囱，保证变工况时余热锅炉的安全。余热锅炉设有疏水泵房，该泵房中布置有一座20m3疏水箱和一台疏水泵，疏水扩容器布置在疏水箱上，回收余热锅炉疏放水，其炉水加药装置也布置在该泵房内，燃气锅炉与余热锅炉并排布置。","id":"j1_83"},{"class":["1","j1_82"],"content":"##### 燃机室外布置燃机房柱距，宽度，运转层标高，屋底标高。","id":"j1_84"},{"class":["1"],"content":"","id":"j1_85"},{"class":["1","j1_85"],"content":"##### 1、在满足工艺合理的条件下，按照“安全、适用、经济、美观、环保”的设计原则设计，以人为本，采用人机工程学、价值工程学、环境工程学等现代科学设计理念方法设计。\n##### 2、主厂房采用技术先进、工艺成熟的柜排架结构，所有建构筑物造型、色调均力求简洁、明快。\n##### 3、按照国家节约能源法(1997)因地制宜，尽量就地取材，优先采用国家推广的新型、轻质、环保材料；合理选择建筑窗地，以满足热工、采光、审美要求。\n##### 4、主要建筑材料\n##### (1)现浇及预制构件均采用普通硅酸盐水泥，砼强度等级≥C20\n##### (2)墙砌体采用粘土空心砖或轻质砌块。\n##### (3)门窗多采用PVC塑钢门窗或铝合金门窗，少量采用塑钢、木门窗。\n","id":"j1_86"},{"class":["1","j1_85"],"content":"##### （1）地面\n##### 一般地面采用C20细石混凝土，操作室内采用抗静电地板砖，平台采用防滑地砖地面，楼梯栏杆采用不锈钢。\n##### （2）屋面防水\n##### 除有特殊要求的屋面外，均使用4mm厚SBS改性沥青防水卷材。\n##### （3）墙体\n##### 砖混结构为普通粘土砖，内墙厚240，外墙240。燃机间框架结构采用彩钢夹心板维护，除氧间填充墙为砌体墙。\n##### （4）装修\n##### 内外墙面及顶棚均抹灰，刷涂料并作踢脚。\n##### （5）门、窗\n##### 控制室采用防爆隔音门窗，其余采用普通铝合金门窗。屋面采用双坡钢屋架，屋面采用保温彩钢板，天窗架采用钢天窗架上铺彩板。\n","id":"j1_87"},{"class":["1","j1_85"],"content":"##### 各建筑耐火等级均为二级及以上，按火灾危险性分类，除材料库外(丙类)其余均为丁类及以下；各建筑除在选用材料上满足建筑防火规范要求外，主厂房楼梯间通道，高低压配电室，电缆井道检查门，均设防火门，主厂房各层均设消防系统；各建筑主要层及控制室，变配电室等处均设灭火设施。各建构筑物之间距及分区满足规范要求。\n","id":"j1_88"},{"class":["1","j1_85"],"content":"##### 1、基本资料\n##### 抗震设防烈度为8度，设计基本地震动峰值加速度区划为O.10g，设计地震分组为第一组。场地土为Ⅱ类场地。风荷载为0.40kN/m2。\n##### 2、结构形式\n##### 主厂房采用砼框排架结构。\n##### 化水间、循环水泵房采用多层砼框架结构。\n##### 3、基础\n##### 厂房基础采用钢筋砼独立基础，基础埋深，其余建筑物基础埋深1.80m。\n##### 烟囱、锅炉基础采用筏板基础。各主机基础与主厂房基础脱开。\n","id":"j1_89"},{"class":["1"],"content":"","id":"j1_90"},{"class":["1","j1_90"],"content":"##### 需全面通风的房间采用机械通风方式。除需全面通风的房间采用自然通风。配电室设事故排风，平时兼作通风换气，换气次数按每小时12次设计。出线小室设机械排风系统，利用百叶风口（带过滤网）自然进风，换气次数按每小时15次设计。电缆夹层设机械排风系统，换气次数按每小时6次设计。化验室换气次数按每小时10次设计轴流风机。药品室设换气次数15次的机械通风装置，室内吸风口底部距地面0.5m处，且选用电动机、通风机直接连接的防爆通风机。风机选用T35-11系列轴流式通风机，该风机结构合理，具有较高的效率和较低的噪音。","id":"j1_91"},{"class":["1","j1_90"],"content":"##### 为满足工艺及人体卫生对房间的温度、湿度要求，在控制室、机柜室、电气室等房间内设有空调系统。在设有火灾报警系统的房间内，空调设施与火灾报警系统连锁关闭。\n##### 表15.2-1空调场所、设计温度及空调方式表\n\n| 序号 |建筑部位 |室内设计温度（℃） |空调方式 |\n|:------|:------|:------|:------|\n| 1 |控制室 |18～28 |柜式空调 |\n| 2 |高低压配电室 |<35℃ |柜式空调 |\n","id":"j1_92"},{"class":["1"],"content":"##### 本能源站位于工业园区内，拟在工业园区内建设一个能源要素保障企业，为园区内各企业提供价格低廉，质量保证的电力和蒸汽保障。能源站建设供电，供汽主机及其公辅设施，本章对其经济性做出经济效益分析。\n##### 项目建设期为(手动输入)个月，生产运营期取25年，财务评价计算期为26年。经济评价项目工程费用预计(手动输入)万元（不包含征地费,管道建设费，办公楼及其他费用），税费按国家法律规定，按满负荷运转计算。如下表所示为该项目的收益和费用表。其中电价按工业园区统一电价，按需求调研表！元/kWh计算，厂区设备自耗电按5%计算，燃气价格按照需求调研表！元/Nm3，蒸汽价格，按需求调研表！元/t计算(当地园区企业自供汽的成本价)。\n##### 表15.2-1工业园区燃汽轮机热电联产项目收益（单位：万元）\n\n| 序号 |目标客户 |产品名称 |含税价(元) |销量单位 |销量 |含税收入 |销项税 |不含税收入 |备注 |\n|:------|:------|:------|:------|:------|:------|:------|:------|:------|:------|\n| 1 |上网发电 |电 |0.55 |万度 |2671.40 |1469 |213 |1256 | |\n| 2 |园区企业 |蒸汽 |180 |万度 |24 |561.6 |561.6 |3758 |当地园区企业自供汽的成本价 |\n| 合计 | | | | | |5789 |774.1 |5014 | |\n\n##### 本项目的费用主要包括消耗的燃气以及冷却蒸发消耗的工业原水以及锅炉及输送管道的汽水损失，以及工资福利等；工业原水按需求调研表！元/t计算，生活用水按居民生活用水需求调研表！元/t计算，除盐水按需求调研表！元/t计算。具体数据见下表。\n##### 表15.2-2 工业园区燃汽轮机热电联产项目运营费用明细表（单位：万元）\n\n| 序号 |项目 |计量单位 |年消耗量 |单价(含税 元/吨) |金额（含税/年） |进项税 |备注 |\n|:------|:------|:------|:------|:------|:------|:------|:------|\n| 1 |能源介质消耗 | | | | | | |\n| 1.1 |燃气 |万Nm3 | | | | | |\n| 1.2 |工业原水 |万吨 | | | | | |\n| 1.3 |除盐水 |万吨 | | | | | |\n| 1.4 |生活用水 |万吨 | | | | | |\n| 2 |工资及利费 | | | | | | |\n| 3 |日常维护费 | | | | | | |\n| 总计 | | | | | | | |\n\n##### 本项目投资估算包括设备采购费用，设备安装费用，建筑工程费用，，预备费，铺底流动资金，土地购置费用等构成，本方案只考虑工程费用不考虑输汽管网建造费用、办公楼和其他费用，初步估价为万元，预估管网建设费用万元，总计万元。\n##### 表15.2-3 工业园区燃汽轮机热电联产项目投资估算表（单位：万元）（预估）\n\n| 投资构成 |数值（单位：万元） |\n|:------|:------|\n| 能源站工程费用总计 | |\n| 建筑工程费 | |\n| 设备购置费 | |\n| 安装工程费 | |\n| 其他工程建设费用 | |\n| 管网建设费用 | |\n\n","id":"j1_93"},{"class":["1","j1_93"],"content":"##### 根据我国现行法律、法规、财税制度和电价政策，按照国家发展改革委和建设部2006年联合颁发的《建设项目经济评价方法与参数（第三版）》、《火力发电厂工程经济评价导则》《火电厂工程限额设计参考造价指标》等指导文件进行财务评价。\n","id":"j1_94"},{"class":["1","j1_93"],"content":"","id":"j1_95"},{"class":["1","j1_93"],"content":"##### 从以上数据分析，投资的盈利水平与经营成本以及产品的价格较为敏感；从产品价格的角度来看，从长远来讲，受环保煤改气的压力影响，蒸汽是呈上升趋势的。经营成本的最主要构成是燃气价格和电价，燃气价格和电价对投资的盈利水平的影响是显著的。因此为了投资回收期的缩短的最好办法就是降低锁定燃气价格，提高蒸汽及电力售价。\n# 结论和建议\n##### 本项目是燃气轮机热电联产工程，燃机、余热锅炉等都是成熟的产品，安装工期较短，且质量较好保证；项目地区电力和蒸汽需求稳定，且处于不断增长阶段；燃气供应充足，且价格适中；地方政府对项目的支持力度较大。本项目盈利的关键点在于燃气气价、电价以及蒸汽的供应价格以及稳定的蒸汽和电力需求；合理的气价、电价和蒸汽价格能给业主带来明显的投资效益和环保效益。","id":"j1_96"},{"class":["1"],"content":"##### 燃机空气吸入口设置消声器和过滤装置。燃气轮机的排气口排出的高温烟气，首先进入余热锅炉的入口烟道，接着依次流经沿水平方向布置的低压蒸发器、低温省煤器等受热面，然后进入余热锅炉的出口烟道，最后通过烟囱排到大气中，排烟温度约为90-100℃。\n##### 为了吸收热膨胀引起的位移，余热锅炉的入口烟道和出口烟道均安装膨胀节。在余热锅炉的出口烟道和烟囱中还安装了消声器，以减小烟气流动产生的噪声，降低噪声对周围环境的影响。\n##### 能源站的首要任务是向工业园区内的热用户供热，因此，考虑燃气轮机运行的安全性，燃气轮机的排气口和余热锅炉的入口烟道之间设有旁路烟囱。\n##### 在余热锅炉烟气出口处设置烟气热水板式换热器的空间，用于吸收烟气低品位热能生产热水，热水用于在冬季采暖或生活用水。烟气温度从102℃降到75℃，生产90/70℃的热水。","id":"j1_97"},{"class":["1"],"content":"##### 热力系统遵循成熟、可靠合理的原则，充分考虑运行的安全、经济性，优化设备选型和配置，简化工艺系统。\n##### 燃气-蒸汽联合循环机组的热力系统主要由燃气循环系统、余热锅炉汽水系统两部分组成。燃气轮机排气排入余热锅炉，余热锅炉和燃气锅炉产生蒸汽送蒸汽母管后供至工艺处。燃机单独拖动一台发电机。\n##### 从各用户冷却回收的凝结水由凝结水泵升压送入给水母管，后分别送入燃气锅炉和余热锅炉尾部低压省煤器，之后进入低压汽包兼除氧器。除过氧的给水通过低压蒸发器和过热器生成低压过热蒸汽，低压蒸汽直接供工艺使用。\n##### 余热锅炉经补燃后可产生蒸汽供工艺使用，在但是此时的余热锅炉的排烟温度约为143℃，该烟气可用于热水加热，用于供暖使用，最终排烟温度可降至90℃，最大限度的回收余热，燃气锅炉产生蒸汽作为调峰补充。","id":"j1_98"},{"class":["1"],"content":"##### 本项目设1套润滑油系统。油箱与底座一体；燃机润滑油系统由主润滑油泵(交流电动机驱动)、满载辅助润滑油泵(交流电动机驱动)、事故油泵(直流电动机驱动)、润滑油板式冷油器(2×100%)、双联滤油器、油箱(包括油烟分离器、排油烟风机、电加热装置)、交流电动机驱动的密封油真空泵等组成。系统向燃气轮机及其发电机轴承供给润滑油，保证机组的正常运转。燃机的主油箱均带有电加热器及温控设备，用于机组冷态启动时保证润滑油正常油温。\n##### 润滑油系统的配置以主机厂家最终资料为准。\n","id":"j1_99"},{"class":["1"],"content":"##### 厂内10kV系统中性点采用消弧线圈接地或不接地方式。低压系统中性点采用直接接地方式。\n##### 10kV直供电电源在燃机发电机出口通过限流电抗器引接，相应地分别设一段10kV直供电线。本10kV直供电系统给经开区内部分就近户供电。 \n##### 机组10kV厂用电均采用单母线接线。燃机发电机组的厂用电在相应的10kV直供电系统引接，其所需厂用电由相应的燃机厂用电系统提供。\n##### 低压厂用电分为PCC和MCC两层。PCC采用暗备用方式，向各MCC供电。各MCC采用放射式方式向用户供电。主工艺系统MCC采用单母 线双电源自动切换接线，个别辅助设施的MCC采用单母线单电源接线。","id":"j1_100"},{"class":["1"],"content":"","id":"j1_101"},{"class":["1"],"content":"##### 根据工艺配置，热工自动化主要完成对进行整个装置的过程参数的检测、监视及控制。本能源站采用一套知名品牌的过程控制系统（DCS）作为主控系统，实现对余热锅炉及配套公辅设施自动监视和控制，保证装置的安全和经济运行。主要完成生产过程的数据采集和处理，数据显示和记录，数据设定和生产操作，执行对生产过程的连续调节控制和逻辑顺序控制，运行人员在控制室内通过HMI进行监控，并在现场人员的配合下完成机、炉、电及其辅助系统的启、停、正常运行及异常工况处理。除此之外，在控制室还设有必要的紧急停机按钮，用于机组故障时的安全停机。\n##### 装置DCS控制系统拟采用一套冗余控制器，完成烟气余热锅炉以及循环水站、天然气调压站、供配电等公辅设施1套。通讯网络采用冗余网络，DCS控制系统预留与外部的通讯接口。\n##### 燃气轮机本体仪表及GTC控制系统由燃气轮机厂成套供货，除盐水站本体仪表及PLC控制系统由除盐水制备厂家成套供货，各子系统预留与DCS系统之间的通讯接口，燃机发电系统的过程参数以通讯方式送至DCS进行监视。涉及调节、联锁、控制的信号，采用硬接线方式进行交接，信号遵循输出方隔离原则。","id":"j1_102"},{"class":["1"],"content":"","id":"j1_103"},{"class":["1"],"content":"","id":"j1_104"},{"class":["1"],"content":"","id":"j1_105"},{"class":["1"],"content":"##### 本能源站位于工业园内，拟建设一个能源要素保障企业，为园区内各企业提供价格低廉，质量保证的电力和蒸汽保障。能源站建设供电****，供汽*****主机及其公辅设施，本章对其经济性做出经济效益分析。","id":"j1_106"},{"class":["1"],"content":"##### 本项目是燃气轮机热电联产工程，燃机、余热锅炉等都是成熟的产品，安装工期较短，且质量较好保证；项目地区电力和蒸汽需求稳定，且处于不断增长阶段；燃气供应充足，且价格适中；地方政府对项目的支持力度较大。本项目盈利的关键点在于燃气气价、电价以及蒸汽的供应价格以及稳定的蒸汽和电力需求；合理的气价、电价和蒸汽价格能给业主带来明显的投资效益和环保效益。\n","id":"j1_107"},{"class":["1","j1_98"],"content":"ccpplogic[9]\nccpplogic[10]\nccpplogic[11]\nccpplogic[12]\n##### 根据《火力发电厂设备和管道保温油漆设计技术规定》，主要设备和管道保温材料选择如下：\n##### 1) 主蒸汽、主给水管道采用硅酸铝管壳制品。\n##### 2) 其它管道：介质温度>300℃时，采用复合硅酸盐制品；介质温度<300℃时，采用岩棉。\n##### 3) 锅炉烟风道采用岩棉制品。\n##### 4) 外径＜32mm以下的管道采用硅酸铝纤维绳。\n##### 5) 管道、烟风道及设备的保温层外的保护层采用镀锌铁皮或彩钢板。\n##### 6) 管道保温结构的外表，为了便于识别起见，涂刷介质名称，表示介质性质的色环和表示介质流向的箭头。设备保温结构的外表，涂刷设备的名称。\n##### 全厂色彩系统由根据国家标准和业主要求实施。","id":"j1_108"},{"class":["1","j1_98"],"content":"##### 本工程给水系统（含给水泵）由余热锅炉厂设计并供货，给水系统采用单元制，每台余热锅炉设置2台100%容量的给水泵，两台给水泵互为备用，设置一台变频器控制。\n##### 在给水泵出口设有最小流量回路，以保证起动和低负荷期间给水泵通过最小流量运行，防止给水泵汽化。","id":"j1_109"},{"class":["1","j1_98"],"content":"##### 凝结水系统是将从用户返回的凝结水和可以回收利用的管路凝结水加热并输送至凝结水母管后分别送入余热锅炉和燃气调峰锅炉的低压省气器再经低压给水操作台进入锅炉蒸汽除氧器，在此过程中，凝结水被加热、除氧。另外本系统还为各种系统提供补给水和其他用水。\n##### 凝结水系统采用母管。余热锅炉设2 台100%容量的凝结水泵，1运1备。每台凝结水泵的容量拟按照满足最大工况下的凝结水流量的110%。当任何1台泵发生故障时，备用泵自动启动投入运行。\n##### 在系统运行的过程中会有汽水损失，需要提供补充软化水，软水制取有专门的制取装置，此补水补充到除氧器，经除氧后送进如锅炉。","id":"j1_110"},{"class":["1","j1_98"],"content":"##### 本项目循环水采用带机力通风冷却塔的二次循环供水系统。开式循环冷却水系统中的冷却水为循环水，采用单元制设置。开式循环冷却水取自主厂房内循环水供水母管，向闭式循环冷却水热交换器、空气压缩机等提供冷却水。排水接至循环水回水母管。定排坑冷却水采用工业水进行冷却。\n##### 闭式循环冷却水系统主要向下列设备提供冷却水：燃机岛设备（燃气轮机润滑油冷却器，发电机的空气冷却器等）。 本系统的水源为化学除盐水，采用单元制设置。系统设1套闭式水集装装置，内含2台100%容量的闭式循环冷却水泵、2台闭式冷却水热交换器和1台膨胀水箱。正常运行时，一台冷却水泵和一台热交换器运行可满足整个系统所需的冷却水量。","id":"j1_111"},{"class":["1","j1_98"],"content":"##### 本工程额定工业热负荷ccpplogic[13]t/h，凝结水按70%回收率考虑。根据《小型火力发电厂设计规范》，可计算化学水处理系统出力：\n##### 1）锅炉额定蒸发量：ccpplogic[14]×1=36t/h\n##### 2）厂内汽水循环正常损失： ccpplogic[15]×3%=1.08t/h\n##### 3）锅炉正常排污损失：ccpplogic[16]×2%=0.72t/h\n##### 4）水处理系统耗水量：ccpplogic[17]t/h\n##### 5）其它不可预计用水损失：ccpplogic[18]t/h\n##### 6）启动或事故增加用水量：ccpplogic[19]×10%＝3.6t/h\n##### 7）外供汽损失：ccpplogic[20]×30%=9t/h\n##### 8)锅炉补给水处理系统正常出力：厂内汽水循环正常损失：+锅炉正常排污损失+水处理系统耗水量+其它不可预计用水损失：+外供汽损失t/h =12.8t/h\n##### 9）锅炉补给水处理系统最大出力：厂内汽水循环正常损失：+锅炉正常排污损失+水处理系统耗水量+其它不可预计用水损失：+外供汽损失+启动或事故增加用水量t/h =16.4 t/h\n##### 本工程化水系统除盐水站出力按(锅炉补给水处理系统正常出力+锅炉补给水处理系统最大出力)/2t/h计，设置一个有效容积为(锅炉补给水处理系统正常出力+锅炉补给水处理系统最大出力)2.5取整m3的除盐水箱，启动或事故增加的水量由除盐水箱补给。\n##### 化水系统工艺流程：\n##### 水源来水→原水箱→原水泵→多介质过滤器→活性炭过滤器→保安过滤器→高压泵→反渗透装置→除二氧化碳器→中间水箱→中间水泵→混合离子交换器→除盐水箱→除盐水泵→各用水点。\n","id":"j1_112"},{"class":["1","j1_98"],"content":"##### 本项目为园区企业供气，管网建设依据园区具体要求采用地上桥架或地下埋管；管网建设到企业红线外1m预留接口，并配阀门及流量表。","id":"j1_113"},{"class":["1","j1_100"],"content":"##### 本能源站机组主要电气设备参数分别如下：\n##### 1）燃气轮机发电机 \n##### 额定功率@@ccpp_ccpp.engine_power_design@@kW\n##### 额定电压\t10.5kV\n##### 额定电流@@ccpp_ccpp.engine_power_design/10.5@@ A\n##### 额定功率因素\tcosΦ=0.8；\n##### 2）直供电限流电抗器（核算后确定）\n##### 型号：XKK-10-1500-6\n##### 3）厂用电限流电抗器（核算后确定）\n##### 型号：XKK-10-300-3\n##### 4）10kV高压开关柜：\n##### 户内中置式高压开关柜\n##### 额定电压 12kV\n##### 额定电流\t630~2000A\n##### 开断电流\t31.5kA\n##### 5）低压厂用变压器\n##### 额定容量1250kVA\n##### 额定电压\t10/0.4kV\n##### 短路阻抗Ud=6%\n##### 接线组别D/yn11\n##### 6）0.4kV低压开关柜\n##### 户内固定式\n##### 额定电压\t0.4kV\n##### 额定电流\t100~3000A\n##### 开断电流\t50kA \n","id":"j1_114"},{"class":["1","j1_100"],"content":"##### 燃气轮机升压变压器及10kV直供电系统及厂用电10kV配电装置布置在燃气轮机区域。其余辅助设施的电气设备布置在相应工艺系统的附属小电气室内。","id":"j1_115"},{"class":["1","j1_100"],"content":"##### 直流负荷包括高压开关操作电源、直流电源、保护控制电源、直流油泵和事故照明等。直流供电的电压为220V。直流系统采用一套200Ah免维护铅酸蓄电池组。直流电源装置采用微机型相控成套直流电源装置，蓄电池采用1×200Ah阀控密封免维护铅酸蓄电池，配置两台逆变器。该直流装置配有微机型直流绝缘在线监测装置，能对所有的直流负荷进行接地故障监测，并能监测直流母线电压信号，在母线欠压、过压或接地时均能发出报警信号。\n##### 继电保护及自动装置、测量仪表按照《继电保护和安全自动化装置技术规程》、《电测量仪表装置设计技术规程》、《火力发电厂、变电所二次接线设计规程》、《防止电力生产重大事故的二十五项重点要求》、《火力发电厂厂用电设计技术规程》等有关规定配置。所有保护采用微机保护继电器，发电机的保护及测控装置组屏安装，其它保护均安装在对应的开关柜内。 能源站厂设置有电气监控系统，负责监控能源站发变组、以及厂用电等电气系统设备。本能源站另外设置有DCS控制系统。 \n##### 继电保护按国标GB/T 50062-2008 《电力装置的继电保护和自动装置设计规范》要求配置。\n##### 1）发电机保护：\n##### 发电机失步解列保护\n##### 纵差保护\n##### 复合电压过电流保护\n##### 90%定子接地保护（按规范允许单相接地运行两小时）\n##### 定子绕组过负荷保护\n##### 转子一点、二点接地保护\n##### 逆功率保护\n##### 发电机失磁保护\n##### 2）低压厂用变压器\n##### 限时速断保护\n##### 过流保护\n##### 温度保护\n##### 3）高压电动机\n##### 电流速断保护\n##### 过电流保护\n##### 单相接地保护\n##### 4）同期系统采用微机自动准同期装置，手动准同期装置。\n","id":"j1_116"},{"class":["1","j1_100"],"content":"##### 过电压保护及接地按照《火力发电厂和变电所防雷接地设计技术规定》执行，采用措施防止直击雷、入侵波以及各种原因引起的过电压对电气设备的危害。\n##### 全厂接地采用计算机接地与设备接地共用的联合主接地网方式， 接地电阻按0.5欧姆(<2000/I)设计。独立避雷针设置集中接地装置，其接地电阻不大于10欧。","id":"j1_117"},{"class":["1","j1_100"],"content":"##### 全厂照明采用动力和照明共用的380/220V供电方式，事故照明由直流屏供电。\n##### 全厂设交流低压检修网络，电源由380/220V低压厂用系统供电。\n##### 1）事故照明\n##### 主厂房事故照明由直流220V供电。\n##### 远离主厂房的辅助车间事故照明采用应急灯。\n##### 主厂房出入口、通道等人员疏散口处，设有安全标志灯。\n##### 2）检修网络\n##### 主厂房内采用固定的三相五线制电源放射形低压检修网络，检修箱电源分别由低压段回路供电。\n##### 主厂房配电室、电子设备间、值班室设立应急照明，在电源突然失电状态下，主厂房配电室、电子设备间、值班室事故照明能够实现自动切换，应急照明自动启动。","id":"j1_118"},{"class":["1","j1_100"],"content":"##### 厂内通信包括全厂行政及调度通信，调度交换机和程控交换机预留与上级调度设备（光通讯设备和载波通讯设备）的通信接口。","id":"j1_119"},{"class":["1","j1_100"],"content":"##### 电缆设施按照《电力工程电缆敷设设计规范》执行，地下部分采用电缆隧道、电缆沟、电缆管井等结合的敷设方式，架空部分采用电 缆桥架、支架等敷设方式。\n##### 电缆防火采用设置阻火墙、阻火隔层、涂刷防火涂料等措施。","id":"j1_120"},{"class":["1","j1_101"],"content":"##### 能源站选用炉的给水、炉水及蒸汽质量标准为：\n##### 表11.1-1 锅炉给水质量表\n\n| 项目 |指标 |单位 |\n|:------|:------|:------|\n| 硬度 |~0 |μ mol/L |\n| 溶解氧 |≤7 |μg/L |\n| 铁 |≤20 |μg/L |\n| 铜 |≤5 |μg/L |\n| 联氨 |≤30 |μg/L |\n| 二氧化硅 |应保证蒸汽中二氧化硅符合标准 |应保证蒸汽中二氧化硅符合标准 |\n| pH（25℃） |8.8~9.3 | |\n| 氢电导率（25℃） |≤0.3 |μS/cm |\n\n##### \n\n##### 表11.1-2蒸汽质量表\n\n| 项目 |指标 |单位 |\n|:------|:------|:------|\n| 钠 |≤15 |μg/kg |\n| 二氧化硅 |≤20 |μg/kg |\n| 铁 |≤15 |μg/kg |\n| 铜 |≤3 |μg/kg |\n| 氢电导率（25℃） |≤0.15 |μS/cm |\n\n##### 表11.1-3 锅炉炉水质量表\n\n| 项目 |指标 |单位 |\n|:------|:------|:------|\n| 磷酸根 |≤3 |mg/L |\n| pH（25℃） |9~9.7 | |\n\n##### 表11.1-4 凝结水质量表\n\n| 项目 |指标 |单位 |\n|:------|:------|:------|\n| 硬度 |≤1.0 |μmol/L |\n| 溶解氧 |≤40 |μg/L |\n| 氢电导率（25℃） |≤0.3 |μS/cm |\n\n##### 为满足机组对给水水质的要求，本化学水处理拟选用两级反渗透+EDI系统。化学水处理系统主要工艺包括预处理系统、预除盐系统、精除盐系统、化学清洗及反渗透冲洗系统等。\n##### 预处理过滤系统主要由原水箱、原水泵、浓水箱、多介质过滤器、活性炭过滤器、过滤器反洗泵及加药系统等组成，在工艺中主要对原水中的浊度、有机物、胶体及硬度进行处理，经此处理后出水水质达到反渗透装置的进水水质要求。\n##### 预除盐系统主要由一级保安过滤器、一级高压泵、一级反渗透装置、一级水箱、中间水泵、PH调整装置、二级保安过滤器、二级高压泵、二级反渗透装置、反渗透清洗装置等组成。反渗透系统主要去除水中大部分溶解盐类。\n##### 精除盐系统由EDI脱盐系统完成，主要由EDI 提升泵、EDI保安过滤器、EDI装置、纯水箱、纯水泵、加氨装置、EDI清洗装置组成，其作用是去除二级反渗透产水中残余的离子。\n##### 除盐水送出及其它配套设备包含除盐水泵、加氨装置、压缩空气储气罐、除盐水系统控制、仪表、阀门管道等。\n","id":"j1_121"},{"class":["1","j1_101"],"content":"##### （1）生水箱\n##### 生水箱起到贮存生水，调节水量的作用，设置生水箱一座，有效容积为35m3，采用钢结构，内防腐，地上布置。\n##### （2）生水泵\n##### 按照一对一，方便操控的原则，本工程设置生水泵1台，1用1备，为后序系统提供稳定的工作压力和水量。\n##### （3）多介质过滤器\n##### 多介质过滤器是反渗透系统的重要预处理装置，它的作用是去除原水中的细小颗粒、悬浮物、胶体等杂质，保证其出水SDI（污染指数）≤4提高反渗透入水品质。设置3台多介质过滤器，两用一备，当过滤器在进出口压差达到一定值或达到累计流量时，则应退出使用进行反洗，保证两台正常运行，以确保稳定的出水水质。多介质过滤器中填充滤料包括石英砂、磁铁矿及无烟煤。\n##### （4）活性炭过滤器\n##### 为了保证RO系统的长期运行和设备的使用寿命进一步降低RO进水的污染指数，预处理系统设置了活性碳过滤器，内装高效净水活性碳，能有效吸附去除原水的有机物和原水中的氯根，并使进RO系统中FI≤3。\n##### 活性炭过滤器为带有椭圆形封头的圆柱形筒体装置。筒体上部设有进水装置，下部设有排水装置，运行时，水经上部进入，流经滤层，从底部流出。过滤器包括进出水阀、排水阀、反冲洗阀、排气阀等；过滤器设有反洗窥视镜，人工取样阀等。运行自动反洗为手动反洗。\n##### （5）阻垢剂加药装置\n##### 为了保证膜元件表面不结垢，保证膜的长期运行效果，延长膜的使用寿命，本工艺在反渗透装置前设置阻垢剂加药装置，通过投加六偏磷酸钠，以防止反渗透膜的结垢，来提高反渗透的产水量和有利于防止反渗透膜上生成沉淀物，加药量一般为3-5mg/L。\n##### （5）保安过滤器\n##### 保安过滤器的作用是保护反渗透膜，每台保安过滤器选用316L材质，滤芯采用进口聚丙烯材质产品。每台保安过滤器的结构可以快速更换芯。\n##### （7）高压泵\n##### 高压泵的作用是为反渗透本体装置提供足够的进水压力，以保证系统达到设计要求的产水量。每套反渗透装置配1台变频高压泵，高压泵出口应装设自动慢开门和压力开关，压力高时报警及停泵。\n##### （8） 反渗透装置\n##### 反渗透装置是本系统中最重要的脱盐装置，经过预处理的水，在系统中被高压泵加压后，在多段膜中可脱除98%以上的盐分，并可去除绝大部分的胶体、有机物、微生物、色素等杂质，系统水回收率可达到75%。\n##### 经过预处理后的合格的生水进入反渗透系统后，水分子和极少量的有机物通过反渗透膜层，经收集管道集中后，经产水管注入中间水箱，反之不能通过的就经由另一组收集管道集中后通往浓水排放管排放。系统的进水、产水和浓水管道上都装有一系列的控制阀门，监控仪表及程控操作系统，这样可以很好的保证设备系统化运行。\n##### （9）反渗透清洗装置\n##### 经过长期运行，反渗透膜面上会积累各种污染物，从而降低反渗透装置的性能（产水量和脱盐率），进水与浓水压差升高。因此除日常的低压冲洗外，还需设置一套清洗装置，定期进行化学清洗，一般半年应进行一次。\n##### 本系统配置一套化学清洗装置，其流程如下：\n##### 清洗水箱 → 清洗泵 →  清洗过滤器  →  反渗透装置\n##### ↑                                    ↓\n##### （10）混合离子化水部分\n##### 采用一套混合离子交换器，对反渗透处理后的水进行软化处理。离子交换工艺具有对一般硬度水质的适应性强，出水水质好且稳定的特点。流量控制再生，双罐系统，保证连续出水。通过对产水量精确计算，准确控制再生时间和程度，即使在出水量变化较大也不影响出水质量，确保用水设备安全运行。\n##### （11）除盐水箱\n##### 除盐水箱起到贮存除盐水，调节水量的作用，设置除盐水箱1台，有效容积为40m3。\n##### （12）除盐水泵\n##### 本工程除盐水泵分为电厂用除盐水泵和外供除盐水泵，电厂用除盐水泵2台（1用1备），保证为除氧器提供稳定的工作压力和水量。\n##### （12） 压缩空气系统\n##### 与系统共用一套压缩空气系统。空气压缩系统由压缩机，干燥机，缓冲罐，过滤器、分气缸等设备构成。\n","id":"j1_122"},{"class":["1","j1_101"],"content":"##### 1.）炉水加磷酸盐系统\n##### 本工程对炉水采用磷酸盐阻垢处理，手动加药。加药泵为电控计量泵，炉水磷酸盐加药量结合给水流量和炉水磷酸根量大小进行调整。本工程设一套组合加药装置，共设2台溶液箱，2台计量泵，加药点给水设在锅炉汽包内。\n##### 2) 化学加药系统设备布置\n##### 加氨装置布置于化学水处理车间；加磷酸盐装置布置于锅炉房，加药间设机械通风，设配制药液的除盐水管，有加药间冲洗设施和药品贮存设施。\n##### 3)汽水取样\n##### 根据化学监督要求，锅炉汽水取样采用分散就地汽水取样装置。汽水监测皆由人工化验，不设监测仪表。汽水取样点设置如下：\n##### \n\n##### 表11.3-1  汽水取样点设置表\n\n| 取样点名称 |取样点位置 |监督项目 |\n|:------|:------|:------|\n| 除氧器后给水 |给水箱出口管 |测溶氧 |\n| 省煤器进口给水 |省煤器进口 |测导电度、PH值 |\n| 炉水 |按锅炉厂要求 |测导电度、PH值 |\n| 饱和蒸汽 |按锅炉厂要求 |测导电度 |\n| 过热蒸汽 |按锅炉厂要求 |测钠离子 |\n| 凝结水 |凝结水箱出口 |测溶氧、导电度 |\n","id":"j1_123"},{"class":["1","j1_102"],"content":"","id":"j1_124"},{"class":["1","j1_102","j1_124"],"content":"##### 控制的基本策略是直接快速地响应负荷、测点信息及操作指令，并做适当的抗干扰滤波，提高信息的可靠性。对信号进行动态补偿是信息更为精确度，对一些信号进行必要的前馈处理，并通过闭环反馈控制，使被控物理量达到稳定可靠，更符合实际。\n##### 控制系统设有联锁保护功能，以防止控制系统错误的、危险的动作，如系统某一部分必须具备的条件不能满足时，联锁逻辑应阻止该部分投入“自动”方式；同时，在条件不具备或系统故障时，系统受影响部分不再继续自动运行，将控制方式转换到手动控制方式。\n##### 控制系统任何部分运行方式的切换，不论是人为的还是由联锁系统自动的，均可平滑进行，而不引起过程变量的扰动，且不需运行人员的修正。\n##### DCS控制系统由若干个子系统组成，这些子系统协调运行，并具有前馈调节功能，使机组能安全、快速与稳定的运行，保证在任何工况下，满足机组正常运行。\n","id":"j1_125"},{"class":["1","j1_102","j1_124"],"content":"##### 设燃气调温调压装置，以确保煤气压力的稳定，流量的充分供应，燃烧值等技术指标要靠天然气源确保，并满足调压装置的额定参数，经DCS控制系统进行自动调节，燃机才能正常运行，这是保证机组可靠稳定运行的最重要的条件之一，因而， 压力、流量要进入DCS控制系统，分别进行天然气压力、流量的PID自动调节，实时监控。如供气方气源出现异常及故障，为确保机组安全，要及时通知到电厂有关人员。\n","id":"j1_126"},{"class":["1","j1_102","j1_124"],"content":"##### 蒸汽母管压力恒定是表征燃气轮机废气量，补燃量与锅炉产汽量平衡的的标志。运行中维护蒸汽母管压力恒定，是系统稳定运行的重要环节之一。\n##### 蒸汽母管压力恒定控制，采用母管压力自动调节控制母管压力。在燃气轮机负荷或补燃量变化时，母管压力出现瞬时阶跃，而调节信道的迟延较大，被控对象信道与调节信道的动态特性甚为悬殊，对调节很不利，因此采用经压力、温度补偿后的蒸汽流量信号作为前馈信号，以克服调节信道的迟延。母管压力调节的输出和蒸汽流量前馈信号叠加后作为对并列运行锅炉总的能量需求。\n","id":"j1_127"},{"class":["1","j1_102","j1_124"],"content":"##### 锅炉给水控制系统是通过锅炉汽包水位定值控制，实现锅炉给水量的控制。锅炉汽包水位自动控制回路采用“串级三冲量”控制方式，汽包水位为定值控制，以汽包水位为主冲量，辅助冲量蒸汽流量为前馈量，辅助冲量给水流量为反馈量，调节给水电动阀门，这样，迅速消除由于蒸汽负荷扰动所产生的“虚假液位”现象，提高了控制回路的调节品质。\n##### 三冲量的测量及补偿方式：\n##### (1)汽包水位测量，为是水位测量真实，排除汽包水位膨胀假象，要考虑水位试验取样，汽包水位零刻度修正。还要采用二台差压变送器，取其加权平均值，并进行数字滤波处理，结合汽包水位测量，经补偿修正形成汽包水位信号。\n##### (2)主汽流量经温度和压力补偿处理，结合主汽流量测量，形成主蒸汽流量。\n##### (3)给水流量及减温水流量经温度补偿后形成给水流量。\n","id":"j1_128"},{"class":["1","j1_102","j1_124"],"content":"##### 通过调节除氧器进汽调节阀开度，控制除氧器进汽量，保持除氧器压力为恒定值，以除氧器压力为被调量，采用单回路PID调节回路，给定值由操作员手动设置。\n##### 除氧器水位控制采用连续水位测量，给定值由控制系统自动(或操作员手动)设置，PID单回路调节除氧器进水阀开度，控制除氧器的进水流量，保持除氧器水位为恒定值。\n","id":"j1_129"},{"class":["1","j1_102"],"content":"##### 1、燃气轮机安全保护系统是一个燃烧器管理和燃料安全联锁系统。该系统从功能上分为：燃料安全系统(FSS)、燃烧器控制系统(BCS)两大部分。BCS接受FSS的闭锁，并且将有关信号反馈至FSS，二者相辅相承，构成一个有机整体。它能在燃气轮机启动停止和正常运行等方式下，连续监视燃烧系统的参数与状态，并且进行逻辑运算和判断，通过联锁装置使燃烧设备中的有关执行机构按照既定合理程序完成必要的操作或及时消除事故隐患，保证燃气轮机及燃烧系统的安全，同时防止运行人员操作失误及设备故障引起爆炸，提高燃气轮机运行的可靠性，避免发生事故，减少经济损失。\n##### 2、FSSS系统的作用\n##### 能自动完成各种操作；执行人工操作来不及的安全保护动作；避免运行人员的误操作。主要体现在下列几个方面：\n##### ·吹扫完成及有关条件满足之前，阻止燃料进入燃气轮机。\n##### ·监视燃气轮机的运行工况，在检测到危害人员和设备安全的工况时，发出主燃料跳闸(MFT)信号。\n##### ·当发现危害工况时，停运全部或部分已投运的燃气轮机燃烧设备和有关辅助、快速切断进入燃气轮机的燃料。\n##### ·MFT发生后，维持燃气轮机进风量，以清除燃气轮机和烟道中可能积聚的可燃混合物。\n","id":"j1_130"},{"class":["1","j1_102"],"content":"##### 1、总原则\n##### (1)燃气轮机联锁保护的设计为任意一个原因发生时，则燃气轮机停机的逻辑关系。\n##### (2)除紧急停机按钮外，任意一个原因或停机动作，则均在DCS系统上设置旁路软开关，方便操作人员。\n##### (3)所有原因发生后，均需通过DCS系统软件复位按钮确认后才可重新投入。\n##### 2、锅炉联锁原因及条件\n##### (1)紧急停炉按钮按下。\n##### (2)汽包水位高联锁：当两台汽包水位测量差压变送器的测量信号均高高时。\n##### (3)汽包水位低联锁：当两台汽包水位测量差压变送器的测量信号均低低时。\n##### (4)主蒸汽压力高联锁：当主蒸汽压力测量压力变送器的测量信号高高时。\n##### (5)引风机故障停机时。\n","id":"j1_131"},{"class":["1","j1_102"],"content":"##### 本工程采用机炉电集中控制。操作员站，工程师站，工业电视，打印机等布置在机炉电集中控制室内。过程控制机柜、热控配电柜、电气机柜、安放在机柜室内。\n","id":"j1_132"},{"class":["1","j1_102"],"content":"##### 为了满足生产的要求，监视设备的运行情况，在本项目中设立如下工业电视系统：\n##### 锅炉汽包水位电视监控系统2个摄像头，2个显示器，专业监视器42寸。锅炉汽包及集箱就地压力表引至水位计附近，利用摄像头进行就地监控。\n##### 配置一套工业电视监控系统，2个显示器，专业监视器42寸，摄像头为网络高清摄像头。\n","id":"j1_133"},{"class":["1","j1_102"],"content":"##### 电源是热控设备的动力，是机组安全运行的保证，必须保证供电电源的可靠性。\n##### 分散控制系统(DCS)系统要求提供两路电源：一路来自交流不停电电源(在线式UPS 220V AC)；另一路来自低压厂用母线(220V AC)。在机柜间内配有电源自动切换装置自动完成柜内设备所需电源的配电。控制室内的设备供电由UPS电源提供，断电后持续运行时间不少于30分钟。\n##### 仪表气源\n##### 气动阀门需要的气源采用氮气或压缩空气，全厂共用一套空气压缩系统。\n","id":"j1_134"},{"class":["1","j1_103"],"content":"##### 本工程规划1台燃机配1台余热锅炉另外布置一台燃气锅炉，燃机为轴向排气，余热锅炉与燃气轮机以组同轴线连续布置，拟依次平行布置，余热锅炉采用露天布置，满足辅助设备布置及通道要求，锅炉设有旁路烟囱，保证变工况时余热锅炉的安全。余热锅炉设有疏水泵房，该泵房中布置有一座20m3疏水箱和一台疏水泵，疏水扩容器布置在疏水箱上，回收余热锅炉疏放水，其炉水加药装置也布置在该泵房内，燃气锅炉与余热锅炉并排布置。","id":"j1_135"},{"class":["1","j1_103"],"content":"##### 燃机室外布置燃机房柱距，宽度，运转层标高，屋底标高。","id":"j1_136"},{"class":["1","j1_104"],"content":"##### 1、在满足工艺合理的条件下，按照“安全、适用、经济、美观、环保”的设计原则设计，以人为本，采用人机工程学、价值工程学、环境工程学等现代科学设计理念方法设计。\n##### 2、主厂房采用技术先进、工艺成熟的柜排架结构，所有建构筑物造型、色调均力求简洁、明快。\n##### 3、按照国家节约能源法(1997)因地制宜，尽量就地取材，优先采用国家推广的新型、轻质、环保材料；合理选择建筑窗地，以满足热工、采光、审美要求。\n##### 4、主要建筑材料\n##### (1)现浇及预制构件均采用普通硅酸盐水泥，砼强度等级≥C20\n##### (2)墙砌体采用粘土空心砖或轻质砌块。\n##### (3)门窗多采用PVC塑钢门窗或铝合金门窗，少量采用塑钢、木门窗。\n","id":"j1_137"},{"class":["1","j1_104"],"content":"##### （1）地面\n##### 一般地面采用C20细石混凝土，操作室内采用抗静电地板砖，平台采用防滑地砖地面，楼梯栏杆采用不锈钢。\n##### （2）屋面防水\n##### 除有特殊要求的屋面外，均使用4mm厚SBS改性沥青防水卷材。\n##### （3）墙体\n##### 砖混结构为普通粘土砖，内墙厚240，外墙240。燃机间框架结构采用彩钢夹心板维护，除氧间填充墙为砌体墙。\n##### （4）装修\n##### 内外墙面及顶棚均抹灰，刷涂料并作踢脚。\n##### （5）门、窗\n##### 控制室采用防爆隔音门窗，其余采用普通铝合金门窗。屋面采用双坡钢屋架，屋面采用保温彩钢板，天窗架采用钢天窗架上铺彩板。\n","id":"j1_138"},{"class":["1","j1_104"],"content":"##### 各建筑耐火等级均为二级及以上，按火灾危险性分类，除材料库外(丙类)其余均为丁类及以下；各建筑除在选用材料上满足建筑防火规范要求外，主厂房楼梯间通道，高低压配电室，电缆井道检查门，均设防火门，主厂房各层均设消防系统；各建筑主要层及控制室，变配电室等处均设灭火设施。各建构筑物之间距及分区满足规范要求。\n","id":"j1_139"},{"class":["1","j1_104"],"content":"##### 1、基本资料\n##### 抗震设防烈度为8度，设计基本地震动峰值加速度区划为O.10g，设计地震分组为第一组。场地土为Ⅱ类场地。风荷载为0.40kN/m2。\n##### 2、结构形式\n##### 主厂房采用砼框排架结构。\n##### 化水间、循环水泵房采用多层砼框架结构。\n##### 3、基础\n##### 厂房基础采用钢筋砼独立基础，基础埋深，其余建筑物基础埋深1.80m。\n##### 烟囱、锅炉基础采用筏板基础。各主机基础与主厂房基础脱开。\n","id":"j1_140"},{"class":["1","j1_105"],"content":"##### 需全面通风的房间采用机械通风方式。除需全面通风的房间采用自然通风。配电室设事故排风，平时兼作通风换气，换气次数按每小时12次设计。出线小室设机械排风系统，利用百叶风口（带过滤网）自然进风，换气次数按每小时15次设计。电缆夹层设机械排风系统，换气次数按每小时6次设计。化验室换气次数按每小时10次设计轴流风机。药品室设换气次数15次的机械通风装置，室内吸风口底部距地面0.5m处，且选用电动机、通风机直接连接的防爆通风机。风机选用T35-11系列轴流式通风机，该风机结构合理，具有较高的效率和较低的噪音。","id":"j1_141"},{"class":["1","j1_105"],"content":"##### 为满足工艺及人体卫生对房间的温度、湿度要求，在控制室、机柜室、电气室等房间内设有空调系统。在设有火灾报警系统的房间内，空调设施与火灾报警系统连锁关闭。\n##### 表15.2-1空调场所、设计温度及空调方式表\n\n| 序号 |建筑部位 |室内设计温度（℃） |空调方式 |\n|:------|:------|:------|:------|\n| 1 |控制室 |18～28 |柜式空调 |\n| 2 |高低压配电室 |<35℃ |柜式空调 |\n","id":"j1_142"},{"class":["1","j1_106"],"content":"##### 根据我国现行法律、法规、财税制度和电价政策，按照国家发展改革委和建设部2006年联合颁发的《建设项目经济评价方法与参数（第三版）》、《火力发电厂工程经济评价导则》《火电厂工程限额设计参考造价指标》等指导文件进行财务评价。\n","id":"j1_143"},{"class":["1","j1_106"],"content":"##### 项目建设期为(手动输入)个月，生产运营期取25年，财务评价计算期为26年。经济评价项目工程费用预计(手动输入)万元（不包含征地费,管道建设费，办公楼及其他费用），税费按国家法律规定，按满负荷运转计算。如下表所示为该项目的收益和费用表。其中电价按工业园区统一电价即上网电价：@@ccpp_questionnaire.net_electricity_price@@，自用电价：@@ccpp_questionnaire.personal_electricity_price@@，厂区设备自耗电按5%计算，燃气价格:@@ccpp_questionnaire.price_design@@元/Nm3，蒸汽价格:@@ccpp_questionnaire.steam_price_1@@元/t计算(当地园区企业自供汽的成本价)。\n本项目的费用主要包括消耗的燃气以及冷却蒸发消耗的工业原水以及锅炉及输送管道的汽水损失，以及工资福利等；工业原水按需求调研表！元/t计算，生活用水按居民生活用水需求调研表！元/t计算，除盐水按需求调研表！元/t计算。\n本项目投资估算包括设备采购费用，设备安装费用，建筑工程费用，预备费，铺底流动资金，土地购置费用等构成，本方案只考虑工程费用不考虑输汽管网建造费用、办公楼和其他费用，初步估价为(手动输入)万元，预估管网建设费用(手动输入)万元，总计(手动输入)万元。\n","id":"j1_144"},{"class":["1","j1_106"],"content":"##### 从以上数据分析，投资的盈利水平与经营成本以及产品的价格较为敏感；从产品价格的角度来看，从长远来讲，受环保煤改气的压力影响，蒸汽是呈上升趋势的。经营成本的最主要构成是燃气价格和电价，燃气价格和电价对投资的盈利水平的影响是显著的。因此为了投资回收期的缩短的最好办法就是降低锁定燃气价格，提高蒸汽及电力售价。","id":"j1_145"}]
""",
    "template_content": 
    u"""# 1. 工程概况条件
## 1.1 概述
### 1.1.1 项目名称
##### @@plan.plan_name@@项目

### 1.1.2  分布式能源项目优势
##### 1、经济性。一体化方案充分利用发电余热、地热，再生水余热来制热与供冷，因此能源得以合理的梯级利用，从而提高能源利用效率。分布式电源系统减少了大型发电厂和高压输电网的压力，节约投资，并且输配电网的流量减少，相应的降低网损。再生水回用减少了自来水使用量，节约水资源，
##### 2、环保型。项目采用生物质、垃圾再利用、太阳能、天然气等清洁剂可再生能源为一次能源，减少有害物的排放总量，减轻环保压力。
##### 3、能源利用多元性。采用多种形式的一次能源，且同时为用户提供电、热、水、气等多种能源应用方式，是解决能源危机、提高能源利用效率和能源安全问题的一种很好的途径。
##### 4、调峰填谷。夏季和冬季是负荷高峰时期，此时如果采用工业余热、再生水源热、天然气等，不但解决了夏季的供冷于冬季的供热需要，同时也提供了一部分电力，对电网起到削峰填谷作用。
##### 5、安全性和可靠性。当电网出现大面积停电事故、热网出现供热故障时，一体化能源系统仍然可以保持正常运行，提高供电、供热的安全性和可靠性。
##### 6、分布式能源系统的优势。分布式能源系统是相对于传统的集中式能源生产与供应模式（主要代表形式是大电厂加大电网）而言的，是靠近用户端，直接向用户提供各种形式能量的中小型终端供能系统。其便于实现能源综合梯级利用，在具有更高能源利用率的同时还具有更高供能安全性以及更好的环保性能。
##### ![](http://117.36.73.154:6008/uploaded_file/1.1.2-2.jpg)
##### 图1.1.2-2天然气分布式能源梯级利用示意图
##### 天然气分布式能源是分布式能源的主要形式之一，以天然气作为燃料，采用燃气轮机或燃气内燃机为发电设备，在发电的同时，利用发电产生的烟气余热生产冷热产品就近满足用户冷热需求。天然气分布式能源的核心理论就是“温度对口、梯级利用”。与传统的电、热、冷分产系统相比，分布式能源系统的节能率约为20~35%左右，减排率可达到35~45%左右。
##### ![](http://117.36.73.154:6008/uploaded_file/1.1.2-2.jpg)
##### 图1.1.2-2分布式能源节能减排原理示意图
##### 天然气分布式冷热电联供系统以小规模（几百kW 至数十MW）分散布置的方式建在用户附近，配置灵活，便于按冷、热、电负荷的实际需要进行调节，不仅满足了区域内用户的用能需求，还节省了大量的城市供热管网建设和运行的费用，有助于电网和燃气供应的削峰填谷，减少碳化物及有害气体的排放，产生良好的社会效益，符合可持续发展战略，是未来能源技术发展的重要方向之一，在商业、建筑能源系统中将得到广泛的应用。
##### （1）国内外发展形势
##### 国外分布式能源发展较早，应用范围广泛。美国上个世纪90年代就已经大面积发展分布式能源，其建设分布式能源站项目超过6000个，其中医院类就有170个以上。欧美和日本的分布式能源发展更为迅猛，项目建设达10000个以上。
##### 中国发展分布式能源较晚，主要受国内能源结构限制。现国家发改委已明确鼓励大力发展分布式能源项目；同时国家“十三五规划”中明确大力发展分布式能源建设。同时，国家逐步完成对售电侧的放开机制，并加大对分布式能源项目的奖励机制。分布式能源的发展将成为国内电源项目发展的一个新的方向。
##### （2）与生物质直燃发电相比分布式能源的优势
##### 分布式能源与生物质项目相比能源的综合利用程度更高，燃料更有保证，不受四季天时的影响，分布式能源项目占地面更小，生物质项目需要更大的燃料储存场站及运输队伍；分布式能源项目排放更达标，利用低氮燃烧技术无需专门的脱硫脱硝除尘设备就可以做到超净排放，生物质项目需要配置专门的脱硫脱硝除尘设备；从盈利方面讲生物质项目的盈利主要靠政府补贴，此外生物质项目的燃料价格，供应蒸汽价格受燃料供应限制价格变化较大，有较大的不可确定性。虽然生物质项目的投资相对较低，但后期运营的限制因素较多，会导致运营成本不可控，盈利难以预测。
##### 1）分布式能源系统具有更高的能源综合利用效率。
##### 大型火力发电厂发电效率一般为30%～40%左右，而分布式能源系统得能源利用效率至少在75%以上。
##### 2）分布式能源系统充分考虑了能量品位的梯级利用。
##### 分布式能源系统就近消化，克服了冷热负荷无法远距离传输的困难。对于天然气资源来说，燃烧产生的高温烟气首先用来生产高品位的电能，中温余热可以产生蒸汽、低温余热可以生产空调冷热及生活热水，是公认的最为合理的天然气利用方式。
##### 3）分布式能源系统避免了输配成本。
##### 传统的集中发电供能方式，必须通过输配电网，才能将生产的电能供给用户。随着电网规模扩大，电能输配成本在总成本中所占的比例越来越大。分布式能源系统由于靠近用户，几乎不需要或只需要很短的输送线路，电能的输配成本几乎为零。分布式的燃料靠管线运输，与燃料运输靠卡车或火车运输的集中发电相比，燃料运输价格更低。
##### 4）分布式能源系统增加了电网运行的稳定性，提高了电网供电的安全性。
##### 分布式能源系统，使大电网不再孤立和笨拙。分布式能源系统直接布置在用户侧，相对独立，在电网崩溃和意外灾害（例如地震、暴风雪、人为破坏、战争）情况下，可维持重要用户的供电，保障供电的可靠性。
##### 5）分布式能源系统具有良好的环保性能。
##### 分布式能源系统减少了粉尘、SO2、NOx、CO2、废水废渣等废弃物的排放；同时减少了输变电线路和设备，电磁污染和噪声污染极低，因而具有良好的环保性能。
##### （3）国内分布式能源系统案例
##### 目前国内分布式能源系统已被广泛应用，江浙地区、两湖两广、四川等地的燃气联合循环电厂已经建设有十几个；小型燃气内燃机分布式能源项目在大中型城市也已快速发展，这些项目主要应用在办公、医院、机场、学校等领域。目前，国内比较典型的燃气内燃机分布式能源项目如下：
##### 1）北京清河医院供能系统采用的燃气内燃机分布式系统
##### 2）上海黄浦中心医院采用燃气内燃机分布式能源系统
##### 3）北京309医院采用燃气内燃机分布式能源系统
##### 4）北京华电产业园办公大楼燃气内燃机分布式能源项目
##### 5）上海科技大学燃气内燃机分布式能源项目
##### 6）长沙黄花机场燃气内燃机分布式能源项目
##### 7）上海科技大学燃气内燃机分布式能源项目
##### 8）上海迪士尼燃气内燃机分布式能源项目
### 1.1.3 项目建设单位
##### @@company.company_name@@公司
### 1.1.4 项目建设单位简介
##### (手动输入)
### 1.1.5 建设方案
##### 本项目拟建设发电容量为@@ccpp_questionnaire.engine_power_design@@ kW，蒸汽@@ccpp_questionnaire.recent_steam_flow_range_1_design@@ t/h，将来有电力和蒸汽增长需求，再按实际增长需求设置燃气调峰锅炉或者再建一套燃气发电装置。
### 1.1.6 项目建设的必要性
##### 本项目是为响应国家关于节能环保的要求，改善利津及周边地区的大气质量，开拓天然气的合理、高效利用而建设的以天然气为燃料的燃气热电联产的天然气分布式能源系统，生物质气化多联产系统，地源热泵系统，以替代目前常规的燃煤或燃气锅炉采暖系统，缓解用电高峰，平衡天然气利用。本工程满足园区蒸汽负荷@@ccpp_questionnaire.recent_steam_flow_range_1_design@@t/h（@@ccpp_questionnaire.steam_pressure_level_1_design@@MPa，@@ccpp_questionnaire.steam_temperature_level_1_design@@℃），并能解决园区供电问题。本项目的建设能够满足园区的能源供给，而且又完全符合国家提出的环保、节能以及低碳的要求。
##### （1）本项目的建设是落实国家节能政策，建设节约型社会，实现可持续发展战略的需要。
##### 随着国家经济的快速发展，我国能源需求量也在大幅增加，从1993年开始我国就已成为能源净进口国，而且供求缺口越来越大，2010年我国的能源缺口已达到8%，预计2040年将达到24%左右。近年来国家开始大力发展节能降耗技术，尤其是供热、电厂等耗能工程，国家鼓励采用集中供热取代现有的一批分散供热小锅炉房，以较小的土地、环境、燃料和水等相关资源的代价，获得较大的能源利用效率，使得在能源资源平衡和持续安全供给方面，有效增强能源与环境协调的可持续发展后劲。
##### （2）本项目为利津循环经济产业园配套能源项目，功能是为河利津循环经济产业园提供冷、热、电综合能源服务，是满足利津循环经济产业园本身整体规划建设和项目实际能源需求的要求。
##### （3）本项目的建设满足节能减排，提高经济效率的需要。
##### 本项目采取集中供热、供冷的节约能源、减少污染最有效的途径。将天然气能源最大化梯级综合利用，不仅改善了投资环境，而且可创造较好的经济效益和社会效益。
##### （4）本项目的建设对区域环境改善作用巨大。
##### 本项目采用燃机热电联产以清洁能源天然气为燃料，能有效的提高热效率，用能合理，提高了热能的利用率，从而节约了大量燃料；减少了设备的维修、更换设备的劳动力和资金，改善劳动条件；减轻对环境的污染；供热质量得到改善，为企业的健康发展创造了条件。
##### 综上所述，随着周边用户大量入住用能要求矛盾会更加突出，本项目的建设是非常必要的，建成天然气分布式能源项目也是切实可行的。本项目的建设，对于利津县的经济发展及环境保护，都具有十分很重要的意义。
## 1.2 项目现场条件
### 1.2.1 天然气组分
##### 表1.2.1-1天然气组分表（暂无）按100%CH4计算

| 甲烷 |CH4 |@@ccpp_questionnaire.methane_design@@ |
|:------|:------|:------|
| 乙烷 |C2H6 |@@ccpp_questionnaire.ethane_design@@ |
| 乙烯 |C2H4 |@@ccpp_questionnaire.ethylene_design@@ |
| 丙烯 |C3H6 |@@ccpp_questionnaire.propylene_design@@ |
| 丙烷 |C3H8 |@@ccpp_questionnaire.propane_design@@ |
| 丁烯 |C4H8 |@@ccpp_questionnaire.butene_design@@ |
| i-异丁烷 |iC4H10 |@@ccpp_questionnaire.i_isobutane_design@@ |
| n-异丁烷 |nC4H10 |@@ccpp_questionnaire.n_isobutane_design@@ |
| 戊烷 |C5H12 |@@ccpp_questionnaire.pentane_design@@ |
| 碳6 |C6+ |@@ccpp_questionnaire.carbon6_design@@ |
| 氢气 |H2 |@@ccpp_questionnaire.hydrogen_design@@ |
| 氦气 |He |@@ccpp_questionnaire.helium_design@@ |
| 氮气 |N2 |@@ccpp_questionnaire.nitrogen_design@@ |
| 一氧化碳 |CO |@@ccpp_questionnaire.carbon_monoxide_design@@ |
| 二氧化碳 |CO2 |@@ccpp_questionnaire.carbon_dioxide_design@@ |
| 硫化氢 |H2S |@@ccpp_questionnaire.hydrogen_sulfide_design@@ |
| 氧气 |O2 |@@ccpp_questionnaire.oxygen_design@@ |
| 水 |H2O |@@ccpp_questionnaire.water_design@@ |
### 1.2.2 天然气主要物理性质
##### 表1.2.2-1天然气物理性质表（暂无）按100%CH4计算

| 高位发热量 |kJ/Nm3 |@@ccpp_questionnaire.high_calorific_value_design@@ |
|:------|:------|:------|
| 燃气价格 |元/Nm3 |@@ccpp_questionnaire.price_design@@ |
### 1.2.3 气象条件及海拔地质
##### 表1.2.2-2气象条件及海拔地质表按100%CH4计算

| 当地平均海拔 |A |m |@@ccpp_questionnaire.local_avg_hight@@ |
|:------|:------|:------|:------|
| 年平均温度 |T0 |℃ |@@ccpp_questionnaire.year_avg_temperate@@ |
| 夏季平均温度 |Ts |℃ |@@ccpp_questionnaire.summer_avg_temperate@@ |
| 冬季平均温度 |Tw |℃ |@@ccpp_questionnaire.winter_avg_temperate@@ |
| 年平均大气压力 |P0 |bar |@@ccpp_questionnaire.year_avg_press@@ |
| 夏季大气压力 |Ps |bar |@@ccpp_questionnaire.summer_avg_press@@ |
| 冬季大气压力 |Pw |bar |@@ccpp_questionnaire.winter_avg_press@@ |
| 年平均相对湿度 |d |% |@@ccpp_questionnaire.year_avg_humidity@@ |
### 1.2.4 (手动输入)工业园区
##### (手动输入)
### 1.2.5 仪表风及压缩空气
##### 主要用于燃气轮机空气过滤器反吹和控制仪表用，仪表风质量要求为：压力0.6~1.0MPag, 储气罐出口压力下水露点≤－40℃, 颗粒≤0.5m ，绝对过滤精度≥99.9％，总颗粒含量≤0.05 mg/m3，油雾＝0.0 mg/m3。
### 1.2.6 市电供电情况
##### 市电的供电频率的最大允许偏差不超过±1Hz，供电电压的最大允许偏差不超过额定值的±10%。具体要求见中国《供电营业规则》。其中110kV变压站据项目所在地直线距离[手动输入]km。详细位置见下图。
##### ![](http://117.36.73.154:6008/uploaded_file/1.1.2-2.jpg)
##### 图1.2.6-1 110kV位置图

# 2. 需求分析
##### 园区蒸汽总需求为@@ccpp_questionnaire.recent_steam_flow_range_1@@ t/h，目前电力需求为@@ccpp_questionnaire.electric_load_demand*0.8@@万kWh/年，且目前园区不断有企业入驻，电力方面有较大增长空间。
# 3. 主机选型原则及技术规范
## 3.1 厂址位置
##### 本工程拟选厂址位于(手动输入)工业园内，具体选址待定。
## 3.2 机组选型原则
##### 根据国家发改委、财政部、住建部、能源局联合发布的《关于发展天然气分布式能源的指导意见》（发改能源[2011]2196 号）提出的基本原则，“天然气分布式能源全年综合利用效率应高于70%，在低压配电网就近供应电力。发挥天然气分布式能源的优势，兼顾天然气和电力需求削峰填谷”。
### 3.2.1 主设备的型式与容量的确定原则
##### 本项目主设备的型式与容量的确定需要遵循以下原则：
##### 1）按“以热定电、冷热电三联供”的原则配置能源系统机组容量；
##### 2）充分考虑技术方案的可行性、运行可靠性和调节的灵活性；
##### 3）能源的梯级利用和转换效率应达到国内先进水平；
##### 4）在满足生产和施工安装的前提下，尽量节约用地；
##### 5）在满足安全可靠的条件下，尽量选用技术先进、效率高的联合循环冷热电三联供发电机组。
### 3.2.2 设计依据文件
##### 本项目设计需依据以下文件
##### 国家发改委、财政部、住建部、国家能源局等四部委《关于发展天然气分布式能源的指导意见》（发改能源[2011]2196 号）
##### 《火力发电厂设计技术规程》(DL5000-2000)。
##### 《火力发电厂初步设计文件内容深度规定》(DL/T5427-2009)。
##### 《燃气-蒸汽联合循环电厂设计规定》(DL/T5174-2003)。
##### 《小型火力发电厂设计规范》（GB50049-2011）   
##### 国家、地方和行业其他相关的法律、法规、条例以及规程和规范
# 4. 机组选型方案
##### 根据本项目的供能规模及特点，以燃气-蒸汽联合工艺为基础的区域式分布式能源系统非常适合本项目的建设。
##### 燃气－蒸汽联合循环，热、电联供机组中，燃气轮机、余热锅炉、汽轮机的匹配原则一般是：余热锅炉的蒸发量与燃气轮机排出的烟气余热相匹配，汽轮机的进汽量与余热锅炉的蒸发量相匹配，以使能源的利用效率最大化。汽轮机可以是抽汽凝汽式，也可以是背压式，也可以根据用汽负荷不采用汽轮机。实际运行中，如果有一定的基本热负荷，且变化不大，应采用背压机，若热负荷有变化，则应采用抽凝式汽轮机，本项目根据经济原因不考虑汽轮机。
##### 本项目蒸汽负荷相对比较稳定，故确定采用1台燃气轮机发电机组、1 台余热锅炉,1台燃气锅炉。不配汽轮机。
##### 在国际燃气轮机市场中，能够制造燃气轮机的主要厂家有索拉公司、GE公司、德国的Siemens公司、瑞士ABB公司、日本三菱公司和日本的日立公司等。在国内燃气轮机市场中，能够制造燃气轮机的主要厂家有上海汽轮机有限公司、南京汽轮电机（集团）有限责任公司等。
##### 在中小型民用燃机方面，索拉公司具有非常强的技术及售后服务、检修周期短等优势；在设计经验、价格和性能方面有很强的竞争力。且因为采用低氮燃烧技术，排放负荷国家标准要求。以下是燃机预期的排放值：

| NOx氮氧化物 |38 ppmv (80 mg) |
|:------|:------|
| CO一氧化碳 |50ppmv (64 mg) |
| UHC未燃烧总烃 |25 ppmv (18 mg) |

##### 上述运行点工况排放值限定为：环境温度：(-17 ~48℃) 功率范围：50-100%环境温度：(-17 ~48℃)。SO2排放值取决于燃料中的硫含量。
##### 目前陆上发电用燃气轮机有轻型和工业型两类可供选择。轻型燃气轮机系由航空燃气轮机派生，体积小，重量轻，设备部件精度高，对机组运行的环境条件要求也较苛刻。轻型燃气轮机起停迅速，单循环热效率较高，非常适宜于作调峰发电机组，如@@ccpp_ccpp.engine_model@@机型等。
##### 本工程是热电联产的分布式能源电站，根据以热定电的原则，按照本项目平均蒸汽负荷匹配的机组总供热能力考虑运行可靠性和调节的灵活性，根据需求提供蒸汽h，若锅炉补燃可增加蒸汽产生量，但考虑到系统的经济性建议利用燃气锅炉调峰供给。前经过初步的热平衡计算，兼顾高效的特点，本工程建议选用@@ccpp_ccpp.engine_model@@型燃气轮机，余热锅炉选用余热锅炉或配合燃气调峰锅炉联合供汽。
##### 本工程暂按@@ccpp_ccpp.engine_model@@燃机进行设计，燃机厂商最终将通过招标综合技术评比后确定。
##### 燃气在燃气轮机燃烧做功发电后，烟气进入余热锅炉，产生蒸汽压力为@@ccpp_questionnaire.steam_pressure_level_1@@ bar，温度@@ccpp_questionnaire.steam_temperature_level_1@@℃；燃气锅炉和余热锅炉供蒸汽母管后，蒸汽直接供生产工艺用，增大能量的利用率。

## 4.1燃气轮机
##### 燃气轮机主要包含以下几个系统：燃气轮机主机是主要的动力的单元，拖动电机发电；启动系统用于燃气轮机的启动；燃料处理系统主要作用是处理进入燃气轮机的燃气以达到符合燃机的进气条件；润滑油系统为机械转动提供必要润滑油，油箱与底座一体化设计，为机组提供平整的支撑；透平空气进气系统用于处理进入燃气轮机的空气，以满足空气的清洁度要求；透平排气系统包括烟囱和排气消声器的用于处理透平排气；机罩包括通风系统，火焰检测及灭火系统，以及可燃气体检测等，为燃机的安全运行提供必要保护。燃机系统还包括控制系统以及撬上电缆等。

## 4.2余热锅炉
##### 燃气在燃气轮机内燃烧释放出来的高温烟气经烟道输送至余热锅炉入口，再流经过热器、蒸发器和省煤器，最后经烟囱排入大气，排烟温度一般为 150～180℃，烟气温度从高温降到排烟温度所释放出的热量用来使水变成蒸汽。锅炉给水首先进入省煤器，水在省煤器内吸收热量升温到略低于汽包压力下的饱和温度进入锅筒。进入锅筒的水与锅筒内的饱和水混合后，沿锅筒下方的下降管进入蒸发器吸收热量开始产汽，通常是只有一部分水变成汽，所以在蒸发器内流动的是汽水混合物。汽水混合物离开蒸发器进入上部锅筒通过汽水分离设备分离，水落到锅筒内水空间进入下降管继续吸热产汽，而蒸汽从锅筒上部进入过热器，吸收热量使饱和蒸汽变成过热蒸汽。根据产汽过程的三个阶段对应三个受热面，即省煤器、蒸发器和过热器，如果不需要过热蒸汽，只需要饱和蒸汽，可以不装过热器。当有再热蒸汽时，则可加设再热器。为利用150℃~180℃的烟气可考虑增设热水换热器，降低排烟温度，提高锅炉效率。

## 4.3主要设备参数
##### 不同方案的对比
##### 综合考虑园区用汽用电需求本项目的设计规模为：1套@@ccpp_ccpp.engine_model_design@@燃气轮机机组（配发电机）+1台额定蒸发量为@@ccpp_ccpp.low_superheater_effluent_smoke_enthalpy_design@@单压余热锅炉；该套机组在标准工况时的总发电量约为@@ccpp_ccpp.engine_power_design@@MW； @@ccpp_ccpp.high_terminal_temperature_difference_design@@MPa， @@ccpp_ccpp.high_steam_enthalpy_design@@℃的蒸汽供应量约为20t/h， 
##### 1）燃气轮机主要参数
##### 型号： @@ccpp_ccpp.engine_model_design@@
##### 台数：@@ccpp_ccpp.engine_num_design@@台
##### 冷却方式：空气冷却
##### 表4.3-1Centaur40燃气轮机参数表（标准工况）

| 项目 |单位 |数值 |
|:------|:------|:------|
| 单台设计工况出力 |kW |@@ccpp_ccpp.engine_power_design@@ |
| 热耗率 |kJ/kWh |@@ccpp_ccpp.engine_heat_consmption_rate_design@@ |
| 发电效率 |% |@@ccpp_ccpp.engine_efficiency_design@@ |
| 天然气耗量(单台) |Nm3/h |@@ccpp_ccpp.individual_gas_consumption_design@@ |
| 天然气总耗量 |Nm3/h |@@ccpp_ccpp.individual_gas_consumption_design*ccpp_ccpp.engine_num_design@@ |
| 排烟流量 |t/h |@@ccpp_ccpp.engine_exhuast_gas_flux_design@@ |
| 排烟温度 |℃ |@@ccpp_ccpp.engine_exhuast_gas_temperature_design@@ |
ccpplogic[0]
##### 型号：QC
ccpplogic[1]
ccpplogic[2]
ccpplogic[3]
ccpplogic[4]
ccpplogic[5]
ccpplogic[6]
ccpplogic[7]
ccpplogic[8]
##### 台数：1台
##### 4）发电机主要参数
##### 型 号：@@ccpp_ccpp.engine_model_design@@
##### 功 率：@@ccpp_ccpp.engine_power_design@@ kW
##### 电 压：10.5kV
##### 额定频率：50Hz
##### 相数：	3
##### 功率因数：0.8
##### 冷却方式：
##### 转 速：3000r/min
##### 数 量：1台
##### 系统参数如下表所示
##### 表4.3-2 Centaur40燃气轮机发电机组参数表

| 项目 |数值 |
|:------|:------|
| 燃机发电量（kW） |@@ccpp_ccpp.engine_power_design@@ |
| 单套机组气耗量（Nm3/h) |@@ccpp_ccpp.individual_gas_consumption_design@@ |
| 机组年供蒸汽（t） |@@ccpp_ccpp.high_gas_production_design@@ |
| 机组年总发电量（万kWh) |@@ccpp_ccpp.engine_power_design*0.8@@ |
| 联合循环机组总热效率（%） | |
| 机组年耗气量(万Nm3) |@@ccpp_ccpp.individual_gas_consumption_design*8000@@ |
| 全厂发电气耗（Nm3/kWh） |@@ccpp_ccpp.individual_gas_consumption_design*8000/ccpp_ccpp.engine_power_design*0.8@@ |
| 全年平均热电比（%） | |

# 5. 燃气
## 5.1燃料来源
##### 燃气轮机可用的燃料通常为天然气、柴油、重油或原油。天然气作为一种高效清洁能源，是燃气轮机的理想燃料。本能源站所使用的燃料为天然气，因其是洁燃料且采用低氮燃烧技术，燃烧后排放的污染物小，相对于其它燃料，对环境的影响也比较小。且根据已有资料，供用气气源采用管道气，燃料供应是有可靠保障的。请业主及时与天然气公司签订天然气供销合同以保证项目实施、运行。由于暂无天然气压力资料，本项目暂按设置天然气增压系统考虑。本工程不考虑备用燃料。
## 5.2燃料供应系统
##### 本工程燃气轮机所需天然气压力应不低于3585±138kPa(g），为了保证供气压力，厂内设置天然气增压站，天然气增压站由入口紧急切断单元、粗过滤单元、分离/过滤冷凝存储单元、计量单元、调压单元、出口单元和放散单元组成。由厂外送来的天然气，经过计量、粗分离、精过滤、加热，调压后送至燃机的入口。本工程燃机设置1座调压装置，采用半露天室外布置。当燃气轮机或锅炉区域发生火险时，事故紧急气动（弹簧关闭）阀将自动关闭以阻止天然气进入厂房，为保证天然气管道的安全泄放，天然气管道上设有放散系统。
## 5.3燃气预处理系统
##### 为保证燃机对天然气压力稳定性的要求，红线内设天然气调压站（撬装式）一座。调压站含入口单元、计量单元、过滤单元、换热单元、备用换热单元、燃气调压单元、热水锅炉调压单元、冷凝储罐单元、色谱仪等，配套设天然气放散装置。
##### 为保证燃机对天然气成分和污物的要求，预留过滤单元作为燃气处理设施。
##### 为保证燃机对天然气供气温度的要求，设燃气热水锅炉，该锅炉用天然气压力0.11MPa。待系统正常运转后，可用蒸汽换热热水，继而加热天然气，达到调温节能的目的。
##### 设2套（1用1备）调压系统，同时为燃气热水锅炉设1套调压系统。通过上述方案，保证后续系统的稳定可靠。经调压后的天然气管道一一对应燃机和锅炉，通过架空管道送至各用户点。
##### 天然气系统检修吹扫、安全阀放散等，统一接到放散管对空放散。
##### 本系统满足燃气轮机对燃气的温度和压力的需求，亦要满足安全需要。

# 6. 燃烧系统
##### 燃烧系统主要由燃气轮机和余热锅炉的烟气系统构成。空气由燃气轮机的进气装置(内部设有过滤器和消声器)引入压气机压缩后，进入环绕在燃机主轴上的分管式燃烧室。天然气经过调压站分离、过滤、调压后进入燃机天然气前置模块的计量、加热、再过滤后，与进入燃烧室的压缩空气进行预混，通过燃料喷嘴喷入燃烧室后燃烧，燃烧后的高温烟气进入燃气轮机膨胀作功，带动燃气轮机转子转动，拖动发电机发电。
##### 作功后的烟气温度依然很高，高温烟气通过烟道进入余热锅炉。在这里，高温烟气加热锅炉给水产出蒸汽去送往用户，烟气中的热量被充分吸收和利用，最后冷却后的烟气经余热锅炉的主烟囱排入大气。
##### 为了提高锅炉效率，降低排烟温度，本期工程将扩大余热锅炉低压省煤器的面积来吸收烟气中的余热。
##### 设有氮气吹扫系统，采用外购氮气瓶做燃机燃料气管线吹扫用气。


# 7. 烟气系统
##### 燃机空气吸入口设置消声器和过滤装置。燃气轮机的排气口排出的高温烟气，首先进入余热锅炉的入口烟道，接着依次流经沿水平方向布置的低压蒸发器、低温省煤器等受热面，然后进入余热锅炉的出口烟道，最后通过烟囱排到大气中，排烟温度约为90-100℃。
##### 为了吸收热膨胀引起的位移，余热锅炉的入口烟道和出口烟道均安装膨胀节。在余热锅炉的出口烟道和烟囱中还安装了消声器，以减小烟气流动产生的噪声，降低噪声对周围环境的影响。
##### 能源站的首要任务是向工业园区内的热用户供热，因此，考虑燃气轮机运行的安全性，燃气轮机的排气口和余热锅炉的入口烟道之间设有旁路烟囱。
##### 在余热锅炉烟气出口处设置烟气热水板式换热器的空间，用于吸收烟气低品位热能生产热水，热水用于在冬季采暖或生活用水。烟气温度从102℃降到75℃，生产90/70℃的热水。
# 8. 热力系统及其辅助设备选择
##### 热力系统遵循成熟、可靠合理的原则，充分考虑运行的安全、经济性，优化设备选型和配置，简化工艺系统。
##### 燃气-蒸汽联合循环机组的热力系统主要由燃气循环系统、余热锅炉汽水系统两部分组成。燃气轮机排气排入余热锅炉，余热锅炉和燃气锅炉产生蒸汽送蒸汽母管后供至工艺处。燃机单独拖动一台发电机。
##### 从各用户冷却回收的凝结水由凝结水泵升压送入给水母管，后分别送入燃气锅炉和余热锅炉尾部低压省煤器，之后进入低压汽包兼除氧器。除过氧的给水通过低压蒸发器和过热器生成低压过热蒸汽，低压蒸汽直接供工艺使用。
##### 余热锅炉经补燃后可产生蒸汽供工艺使用，在但是此时的余热锅炉的排烟温度约为143℃，该烟气可用于热水加热，用于供暖使用，最终排烟温度可降至90℃，最大限度的回收余热，燃气锅炉产生蒸汽作为调峰补充。
## 8.1 主蒸汽及旁路系统
ccpplogic[9]
ccpplogic[10]
ccpplogic[11]
ccpplogic[12]
##### 根据《火力发电厂设备和管道保温油漆设计技术规定》，主要设备和管道保温材料选择如下：
##### 1) 主蒸汽、主给水管道采用硅酸铝管壳制品。
##### 2) 其它管道：介质温度>300℃时，采用复合硅酸盐制品；介质温度<300℃时，采用岩棉。
##### 3) 锅炉烟风道采用岩棉制品。
##### 4) 外径＜32mm以下的管道采用硅酸铝纤维绳。
##### 5) 管道、烟风道及设备的保温层外的保护层采用镀锌铁皮或彩钢板。
##### 6) 管道保温结构的外表，为了便于识别起见，涂刷介质名称，表示介质性质的色环和表示介质流向的箭头。设备保温结构的外表，涂刷设备的名称。
##### 全厂色彩系统由根据国家标准和业主要求实施。
## 8.2 给水系统
##### 本工程给水系统（含给水泵）由余热锅炉厂设计并供货，给水系统采用单元制，每台余热锅炉设置2台100%容量的给水泵，两台给水泵互为备用，设置一台变频器控制。
##### 在给水泵出口设有最小流量回路，以保证起动和低负荷期间给水泵通过最小流量运行，防止给水泵汽化。
## 8.3 凝结水及补水系统
##### 凝结水系统是将从用户返回的凝结水和可以回收利用的管路凝结水加热并输送至凝结水母管后分别送入余热锅炉和燃气调峰锅炉的低压省气器再经低压给水操作台进入锅炉蒸汽除氧器，在此过程中，凝结水被加热、除氧。另外本系统还为各种系统提供补给水和其他用水。
##### 凝结水系统采用母管。余热锅炉设2 台100%容量的凝结水泵，1运1备。每台凝结水泵的容量拟按照满足最大工况下的凝结水流量的110%。当任何1台泵发生故障时，备用泵自动启动投入运行。
##### 在系统运行的过程中会有汽水损失，需要提供补充软化水，软水制取有专门的制取装置，此补水补充到除氧器，经除氧后送进如锅炉。
## 8.4 冷却水系统
##### 本项目循环水采用带机力通风冷却塔的二次循环供水系统。开式循环冷却水系统中的冷却水为循环水，采用单元制设置。开式循环冷却水取自主厂房内循环水供水母管，向闭式循环冷却水热交换器、空气压缩机等提供冷却水。排水接至循环水回水母管。定排坑冷却水采用工业水进行冷却。
##### 闭式循环冷却水系统主要向下列设备提供冷却水：燃机岛设备（燃气轮机润滑油冷却器，发电机的空气冷却器等）。 本系统的水源为化学除盐水，采用单元制设置。系统设1套闭式水集装装置，内含2台100%容量的闭式循环冷却水泵、2台闭式冷却水热交换器和1台膨胀水箱。正常运行时，一台冷却水泵和一台热交换器运行可满足整个系统所需的冷却水量。
## 8.5 系统补水
##### 本工程额定工业热负荷ccpplogic[13]t/h，凝结水按70%回收率考虑。根据《小型火力发电厂设计规范》，可计算化学水处理系统出力：
##### 1）锅炉额定蒸发量：ccpplogic[14]×1=36t/h
##### 2）厂内汽水循环正常损失： ccpplogic[15]×3%=1.08t/h
##### 3）锅炉正常排污损失：ccpplogic[16]×2%=0.72t/h
##### 4）水处理系统耗水量：ccpplogic[17]t/h
##### 5）其它不可预计用水损失：ccpplogic[18]t/h
##### 6）启动或事故增加用水量：ccpplogic[19]×10%＝3.6t/h
##### 7）外供汽损失：ccpplogic[20]×30%=9t/h
##### 8)锅炉补给水处理系统正常出力：厂内汽水循环正常损失：+锅炉正常排污损失+水处理系统耗水量+其它不可预计用水损失：+外供汽损失t/h =12.8t/h
##### 9）锅炉补给水处理系统最大出力：厂内汽水循环正常损失：+锅炉正常排污损失+水处理系统耗水量+其它不可预计用水损失：+外供汽损失+启动或事故增加用水量t/h =16.4 t/h
##### 本工程化水系统除盐水站出力按(锅炉补给水处理系统正常出力+锅炉补给水处理系统最大出力)/2t/h计，设置一个有效容积为(锅炉补给水处理系统正常出力+锅炉补给水处理系统最大出力)2.5取整m3的除盐水箱，启动或事故增加的水量由除盐水箱补给。
##### 化水系统工艺流程：
##### 水源来水→原水箱→原水泵→多介质过滤器→活性炭过滤器→保安过滤器→高压泵→反渗透装置→除二氧化碳器→中间水箱→中间水泵→混合离子交换器→除盐水箱→除盐水泵→各用水点。

## 8.6 蒸汽输送管网
##### 本项目为园区企业供气，管网建设依据园区具体要求采用地上桥架或地下埋管；管网建设到企业红线外1m预留接口，并配阀门及流量表。
# 9. 润滑油系统
##### 本项目设1套润滑油系统。油箱与底座一体；燃机润滑油系统由主润滑油泵(交流电动机驱动)、满载辅助润滑油泵(交流电动机驱动)、事故油泵(直流电动机驱动)、润滑油板式冷油器(2×100%)、双联滤油器、油箱(包括油烟分离器、排油烟风机、电加热装置)、交流电动机驱动的密封油真空泵等组成。系统向燃气轮机及其发电机轴承供给润滑油，保证机组的正常运转。燃机的主油箱均带有电加热器及温控设备，用于机组冷态启动时保证润滑油正常油温。
##### 润滑油系统的配置以主机厂家最终资料为准。

# 10. 电气系统
##### 厂内10kV系统中性点采用消弧线圈接地或不接地方式。低压系统中性点采用直接接地方式。
##### 10kV直供电电源在燃机发电机出口通过限流电抗器引接，相应地分别设一段10kV直供电线。本10kV直供电系统给经开区内部分就近户供电。 
##### 机组10kV厂用电均采用单母线接线。燃机发电机组的厂用电在相应的10kV直供电系统引接，其所需厂用电由相应的燃机厂用电系统提供。
##### 低压厂用电分为PCC和MCC两层。PCC采用暗备用方式，向各MCC供电。各MCC采用放射式方式向用户供电。主工艺系统MCC采用单母 线双电源自动切换接线，个别辅助设施的MCC采用单母线单电源接线。
## 10.1 主要电气设备
##### 本能源站机组主要电气设备参数分别如下：
##### 1）燃气轮机发电机 
##### 额定功率@@ccpp_ccpp.engine_power_design@@kW
##### 额定电压	10.5kV
##### 额定电流@@ccpp_ccpp.engine_power_design/10.5@@ A
##### 额定功率因素	cosΦ=0.8；
##### 2）直供电限流电抗器（核算后确定）
##### 型号：XKK-10-1500-6
##### 3）厂用电限流电抗器（核算后确定）
##### 型号：XKK-10-300-3
##### 4）10kV高压开关柜：
##### 户内中置式高压开关柜
##### 额定电压 12kV
##### 额定电流	630~2000A
##### 开断电流	31.5kA
##### 5）低压厂用变压器
##### 额定容量1250kVA
##### 额定电压	10/0.4kV
##### 短路阻抗Ud=6%
##### 接线组别D/yn11
##### 6）0.4kV低压开关柜
##### 户内固定式
##### 额定电压	0.4kV
##### 额定电流	100~3000A
##### 开断电流	50kA 

## 10.2 电气设备布置
##### 燃气轮机升压变压器及10kV直供电系统及厂用电10kV配电装置布置在燃气轮机区域。其余辅助设施的电气设备布置在相应工艺系统的附属小电气室内。
## 10.3 直流电源、二次线、继电保护及自动装置
##### 直流负荷包括高压开关操作电源、直流电源、保护控制电源、直流油泵和事故照明等。直流供电的电压为220V。直流系统采用一套200Ah免维护铅酸蓄电池组。直流电源装置采用微机型相控成套直流电源装置，蓄电池采用1×200Ah阀控密封免维护铅酸蓄电池，配置两台逆变器。该直流装置配有微机型直流绝缘在线监测装置，能对所有的直流负荷进行接地故障监测，并能监测直流母线电压信号，在母线欠压、过压或接地时均能发出报警信号。
##### 继电保护及自动装置、测量仪表按照《继电保护和安全自动化装置技术规程》、《电测量仪表装置设计技术规程》、《火力发电厂、变电所二次接线设计规程》、《防止电力生产重大事故的二十五项重点要求》、《火力发电厂厂用电设计技术规程》等有关规定配置。所有保护采用微机保护继电器，发电机的保护及测控装置组屏安装，其它保护均安装在对应的开关柜内。 能源站厂设置有电气监控系统，负责监控能源站发变组、以及厂用电等电气系统设备。本能源站另外设置有DCS控制系统。 
##### 继电保护按国标GB/T 50062-2008 《电力装置的继电保护和自动装置设计规范》要求配置。
##### 1）发电机保护：
##### 发电机失步解列保护
##### 纵差保护
##### 复合电压过电流保护
##### 90%定子接地保护（按规范允许单相接地运行两小时）
##### 定子绕组过负荷保护
##### 转子一点、二点接地保护
##### 逆功率保护
##### 发电机失磁保护
##### 2）低压厂用变压器
##### 限时速断保护
##### 过流保护
##### 温度保护
##### 3）高压电动机
##### 电流速断保护
##### 过电流保护
##### 单相接地保护
##### 4）同期系统采用微机自动准同期装置，手动准同期装置。

## 10.4 过电压保护及接地
##### 过电压保护及接地按照《火力发电厂和变电所防雷接地设计技术规定》执行，采用措施防止直击雷、入侵波以及各种原因引起的过电压对电气设备的危害。
##### 全厂接地采用计算机接地与设备接地共用的联合主接地网方式， 接地电阻按0.5欧姆(<2000/I)设计。独立避雷针设置集中接地装置，其接地电阻不大于10欧。
## 10.5 照明及检修网络
##### 全厂照明采用动力和照明共用的380/220V供电方式，事故照明由直流屏供电。
##### 全厂设交流低压检修网络，电源由380/220V低压厂用系统供电。
##### 1）事故照明
##### 主厂房事故照明由直流220V供电。
##### 远离主厂房的辅助车间事故照明采用应急灯。
##### 主厂房出入口、通道等人员疏散口处，设有安全标志灯。
##### 2）检修网络
##### 主厂房内采用固定的三相五线制电源放射形低压检修网络，检修箱电源分别由低压段回路供电。
##### 主厂房配电室、电子设备间、值班室设立应急照明，在电源突然失电状态下，主厂房配电室、电子设备间、值班室事故照明能够实现自动切换，应急照明自动启动。
## 10.6 通信
##### 厂内通信包括全厂行政及调度通信，调度交换机和程控交换机预留与上级调度设备（光通讯设备和载波通讯设备）的通信接口。
## 10.7 电缆设施
##### 电缆设施按照《电力工程电缆敷设设计规范》执行，地下部分采用电缆隧道、电缆沟、电缆管井等结合的敷设方式，架空部分采用电 缆桥架、支架等敷设方式。
##### 电缆防火采用设置阻火墙、阻火隔层、涂刷防火涂料等措施。
# 11. 电厂化学
## 11.1 化水系统说明
##### 能源站选用炉的给水、炉水及蒸汽质量标准为：
##### 表11.1-1 锅炉给水质量表

| 项目 |指标 |单位 |
|:------|:------|:------|
| 硬度 |~0 |μ mol/L |
| 溶解氧 |≤7 |μg/L |
| 铁 |≤20 |μg/L |
| 铜 |≤5 |μg/L |
| 联氨 |≤30 |μg/L |
| 二氧化硅 |应保证蒸汽中二氧化硅符合标准 |应保证蒸汽中二氧化硅符合标准 |
| pH（25℃） |8.8~9.3 | |
| 氢电导率（25℃） |≤0.3 |μS/cm |

##### 

##### 表11.1-2蒸汽质量表

| 项目 |指标 |单位 |
|:------|:------|:------|
| 钠 |≤15 |μg/kg |
| 二氧化硅 |≤20 |μg/kg |
| 铁 |≤15 |μg/kg |
| 铜 |≤3 |μg/kg |
| 氢电导率（25℃） |≤0.15 |μS/cm |

##### 表11.1-3 锅炉炉水质量表

| 项目 |指标 |单位 |
|:------|:------|:------|
| 磷酸根 |≤3 |mg/L |
| pH（25℃） |9~9.7 | |

##### 表11.1-4 凝结水质量表

| 项目 |指标 |单位 |
|:------|:------|:------|
| 硬度 |≤1.0 |μmol/L |
| 溶解氧 |≤40 |μg/L |
| 氢电导率（25℃） |≤0.3 |μS/cm |

##### 为满足机组对给水水质的要求，本化学水处理拟选用两级反渗透+EDI系统。化学水处理系统主要工艺包括预处理系统、预除盐系统、精除盐系统、化学清洗及反渗透冲洗系统等。
##### 预处理过滤系统主要由原水箱、原水泵、浓水箱、多介质过滤器、活性炭过滤器、过滤器反洗泵及加药系统等组成，在工艺中主要对原水中的浊度、有机物、胶体及硬度进行处理，经此处理后出水水质达到反渗透装置的进水水质要求。
##### 预除盐系统主要由一级保安过滤器、一级高压泵、一级反渗透装置、一级水箱、中间水泵、PH调整装置、二级保安过滤器、二级高压泵、二级反渗透装置、反渗透清洗装置等组成。反渗透系统主要去除水中大部分溶解盐类。
##### 精除盐系统由EDI脱盐系统完成，主要由EDI 提升泵、EDI保安过滤器、EDI装置、纯水箱、纯水泵、加氨装置、EDI清洗装置组成，其作用是去除二级反渗透产水中残余的离子。
##### 除盐水送出及其它配套设备包含除盐水泵、加氨装置、压缩空气储气罐、除盐水系统控制、仪表、阀门管道等。

## 11.2 化水工艺设备说明
##### （1）生水箱
##### 生水箱起到贮存生水，调节水量的作用，设置生水箱一座，有效容积为35m3，采用钢结构，内防腐，地上布置。
##### （2）生水泵
##### 按照一对一，方便操控的原则，本工程设置生水泵1台，1用1备，为后序系统提供稳定的工作压力和水量。
##### （3）多介质过滤器
##### 多介质过滤器是反渗透系统的重要预处理装置，它的作用是去除原水中的细小颗粒、悬浮物、胶体等杂质，保证其出水SDI（污染指数）≤4提高反渗透入水品质。设置3台多介质过滤器，两用一备，当过滤器在进出口压差达到一定值或达到累计流量时，则应退出使用进行反洗，保证两台正常运行，以确保稳定的出水水质。多介质过滤器中填充滤料包括石英砂、磁铁矿及无烟煤。
##### （4）活性炭过滤器
##### 为了保证RO系统的长期运行和设备的使用寿命进一步降低RO进水的污染指数，预处理系统设置了活性碳过滤器，内装高效净水活性碳，能有效吸附去除原水的有机物和原水中的氯根，并使进RO系统中FI≤3。
##### 活性炭过滤器为带有椭圆形封头的圆柱形筒体装置。筒体上部设有进水装置，下部设有排水装置，运行时，水经上部进入，流经滤层，从底部流出。过滤器包括进出水阀、排水阀、反冲洗阀、排气阀等；过滤器设有反洗窥视镜，人工取样阀等。运行自动反洗为手动反洗。
##### （5）阻垢剂加药装置
##### 为了保证膜元件表面不结垢，保证膜的长期运行效果，延长膜的使用寿命，本工艺在反渗透装置前设置阻垢剂加药装置，通过投加六偏磷酸钠，以防止反渗透膜的结垢，来提高反渗透的产水量和有利于防止反渗透膜上生成沉淀物，加药量一般为3-5mg/L。
##### （5）保安过滤器
##### 保安过滤器的作用是保护反渗透膜，每台保安过滤器选用316L材质，滤芯采用进口聚丙烯材质产品。每台保安过滤器的结构可以快速更换芯。
##### （7）高压泵
##### 高压泵的作用是为反渗透本体装置提供足够的进水压力，以保证系统达到设计要求的产水量。每套反渗透装置配1台变频高压泵，高压泵出口应装设自动慢开门和压力开关，压力高时报警及停泵。
##### （8） 反渗透装置
##### 反渗透装置是本系统中最重要的脱盐装置，经过预处理的水，在系统中被高压泵加压后，在多段膜中可脱除98%以上的盐分，并可去除绝大部分的胶体、有机物、微生物、色素等杂质，系统水回收率可达到75%。
##### 经过预处理后的合格的生水进入反渗透系统后，水分子和极少量的有机物通过反渗透膜层，经收集管道集中后，经产水管注入中间水箱，反之不能通过的就经由另一组收集管道集中后通往浓水排放管排放。系统的进水、产水和浓水管道上都装有一系列的控制阀门，监控仪表及程控操作系统，这样可以很好的保证设备系统化运行。
##### （9）反渗透清洗装置
##### 经过长期运行，反渗透膜面上会积累各种污染物，从而降低反渗透装置的性能（产水量和脱盐率），进水与浓水压差升高。因此除日常的低压冲洗外，还需设置一套清洗装置，定期进行化学清洗，一般半年应进行一次。
##### 本系统配置一套化学清洗装置，其流程如下：
##### 清洗水箱 → 清洗泵 →  清洗过滤器  →  反渗透装置
##### ↑                                    ↓
##### （10）混合离子化水部分
##### 采用一套混合离子交换器，对反渗透处理后的水进行软化处理。离子交换工艺具有对一般硬度水质的适应性强，出水水质好且稳定的特点。流量控制再生，双罐系统，保证连续出水。通过对产水量精确计算，准确控制再生时间和程度，即使在出水量变化较大也不影响出水质量，确保用水设备安全运行。
##### （11）除盐水箱
##### 除盐水箱起到贮存除盐水，调节水量的作用，设置除盐水箱1台，有效容积为40m3。
##### （12）除盐水泵
##### 本工程除盐水泵分为电厂用除盐水泵和外供除盐水泵，电厂用除盐水泵2台（1用1备），保证为除氧器提供稳定的工作压力和水量。
##### （12） 压缩空气系统
##### 与系统共用一套压缩空气系统。空气压缩系统由压缩机，干燥机，缓冲罐，过滤器、分气缸等设备构成。

## 11.3 化学加药系统
##### 1.）炉水加磷酸盐系统
##### 本工程对炉水采用磷酸盐阻垢处理，手动加药。加药泵为电控计量泵，炉水磷酸盐加药量结合给水流量和炉水磷酸根量大小进行调整。本工程设一套组合加药装置，共设2台溶液箱，2台计量泵，加药点给水设在锅炉汽包内。
##### 2) 化学加药系统设备布置
##### 加氨装置布置于化学水处理车间；加磷酸盐装置布置于锅炉房，加药间设机械通风，设配制药液的除盐水管，有加药间冲洗设施和药品贮存设施。
##### 3)汽水取样
##### 根据化学监督要求，锅炉汽水取样采用分散就地汽水取样装置。汽水监测皆由人工化验，不设监测仪表。汽水取样点设置如下：
##### 

##### 表11.3-1  汽水取样点设置表

| 取样点名称 |取样点位置 |监督项目 |
|:------|:------|:------|
| 除氧器后给水 |给水箱出口管 |测溶氧 |
| 省煤器进口给水 |省煤器进口 |测导电度、PH值 |
| 炉水 |按锅炉厂要求 |测导电度、PH值 |
| 饱和蒸汽 |按锅炉厂要求 |测导电度 |
| 过热蒸汽 |按锅炉厂要求 |测钠离子 |
| 凝结水 |凝结水箱出口 |测溶氧、导电度 |

# 12. 热工检测及控制部分
##### 根据工艺配置，热工自动化主要完成对进行整个装置的过程参数的检测、监视及控制。本能源站采用一套知名品牌的过程控制系统（DCS）作为主控系统，实现对余热锅炉及配套公辅设施自动监视和控制，保证装置的安全和经济运行。主要完成生产过程的数据采集和处理，数据显示和记录，数据设定和生产操作，执行对生产过程的连续调节控制和逻辑顺序控制，运行人员在控制室内通过HMI进行监控，并在现场人员的配合下完成机、炉、电及其辅助系统的启、停、正常运行及异常工况处理。除此之外，在控制室还设有必要的紧急停机按钮，用于机组故障时的安全停机。
##### 装置DCS控制系统拟采用一套冗余控制器，完成烟气余热锅炉以及循环水站、天然气调压站、供配电等公辅设施1套。通讯网络采用冗余网络，DCS控制系统预留与外部的通讯接口。
##### 燃气轮机本体仪表及GTC控制系统由燃气轮机厂成套供货，除盐水站本体仪表及PLC控制系统由除盐水制备厂家成套供货，各子系统预留与DCS系统之间的通讯接口，燃机发电系统的过程参数以通讯方式送至DCS进行监视。涉及调节、联锁、控制的信号，采用硬接线方式进行交接，信号遵循输出方隔离原则。
## 12.1 控制系统调节回路方案说明
### 12.1.1 控制的基本策略
##### 控制的基本策略是直接快速地响应负荷、测点信息及操作指令，并做适当的抗干扰滤波，提高信息的可靠性。对信号进行动态补偿是信息更为精确度，对一些信号进行必要的前馈处理，并通过闭环反馈控制，使被控物理量达到稳定可靠，更符合实际。
##### 控制系统设有联锁保护功能，以防止控制系统错误的、危险的动作，如系统某一部分必须具备的条件不能满足时，联锁逻辑应阻止该部分投入“自动”方式；同时，在条件不具备或系统故障时，系统受影响部分不再继续自动运行，将控制方式转换到手动控制方式。
##### 控制系统任何部分运行方式的切换，不论是人为的还是由联锁系统自动的，均可平滑进行，而不引起过程变量的扰动，且不需运行人员的修正。
##### DCS控制系统由若干个子系统组成，这些子系统协调运行，并具有前馈调节功能，使机组能安全、快速与稳定的运行，保证在任何工况下，满足机组正常运行。

### 12.1.2 燃气轮机天然气源控制系统
##### 设燃气调温调压装置，以确保煤气压力的稳定，流量的充分供应，燃烧值等技术指标要靠天然气源确保，并满足调压装置的额定参数，经DCS控制系统进行自动调节，燃机才能正常运行，这是保证机组可靠稳定运行的最重要的条件之一，因而， 压力、流量要进入DCS控制系统，分别进行天然气压力、流量的PID自动调节，实时监控。如供气方气源出现异常及故障，为确保机组安全，要及时通知到电厂有关人员。

### 12.1.3 蒸汽母管压力恒定控制
##### 蒸汽母管压力恒定是表征燃气轮机废气量，补燃量与锅炉产汽量平衡的的标志。运行中维护蒸汽母管压力恒定，是系统稳定运行的重要环节之一。
##### 蒸汽母管压力恒定控制，采用母管压力自动调节控制母管压力。在燃气轮机负荷或补燃量变化时，母管压力出现瞬时阶跃，而调节信道的迟延较大，被控对象信道与调节信道的动态特性甚为悬殊，对调节很不利，因此采用经压力、温度补偿后的蒸汽流量信号作为前馈信号，以克服调节信道的迟延。母管压力调节的输出和蒸汽流量前馈信号叠加后作为对并列运行锅炉总的能量需求。

### 12.1.4 锅炉给水控制系统
##### 锅炉给水控制系统是通过锅炉汽包水位定值控制，实现锅炉给水量的控制。锅炉汽包水位自动控制回路采用“串级三冲量”控制方式，汽包水位为定值控制，以汽包水位为主冲量，辅助冲量蒸汽流量为前馈量，辅助冲量给水流量为反馈量，调节给水电动阀门，这样，迅速消除由于蒸汽负荷扰动所产生的“虚假液位”现象，提高了控制回路的调节品质。
##### 三冲量的测量及补偿方式：
##### (1)汽包水位测量，为是水位测量真实，排除汽包水位膨胀假象，要考虑水位试验取样，汽包水位零刻度修正。还要采用二台差压变送器，取其加权平均值，并进行数字滤波处理，结合汽包水位测量，经补偿修正形成汽包水位信号。
##### (2)主汽流量经温度和压力补偿处理，结合主汽流量测量，形成主蒸汽流量。
##### (3)给水流量及减温水流量经温度补偿后形成给水流量。

### 12.1.5 除氧器压力水位控制系统
##### 通过调节除氧器进汽调节阀开度，控制除氧器进汽量，保持除氧器压力为恒定值，以除氧器压力为被调量，采用单回路PID调节回路，给定值由操作员手动设置。
##### 除氧器水位控制采用连续水位测量，给定值由控制系统自动(或操作员手动)设置，PID单回路调节除氧器进水阀开度，控制除氧器的进水流量，保持除氧器水位为恒定值。

## 12.2 燃气轮机安全保护系统FSSS
##### 1、燃气轮机安全保护系统是一个燃烧器管理和燃料安全联锁系统。该系统从功能上分为：燃料安全系统(FSS)、燃烧器控制系统(BCS)两大部分。BCS接受FSS的闭锁，并且将有关信号反馈至FSS，二者相辅相承，构成一个有机整体。它能在燃气轮机启动停止和正常运行等方式下，连续监视燃烧系统的参数与状态，并且进行逻辑运算和判断，通过联锁装置使燃烧设备中的有关执行机构按照既定合理程序完成必要的操作或及时消除事故隐患，保证燃气轮机及燃烧系统的安全，同时防止运行人员操作失误及设备故障引起爆炸，提高燃气轮机运行的可靠性，避免发生事故，减少经济损失。
##### 2、FSSS系统的作用
##### 能自动完成各种操作；执行人工操作来不及的安全保护动作；避免运行人员的误操作。主要体现在下列几个方面：
##### ·吹扫完成及有关条件满足之前，阻止燃料进入燃气轮机。
##### ·监视燃气轮机的运行工况，在检测到危害人员和设备安全的工况时，发出主燃料跳闸(MFT)信号。
##### ·当发现危害工况时，停运全部或部分已投运的燃气轮机燃烧设备和有关辅助、快速切断进入燃气轮机的燃料。
##### ·MFT发生后，维持燃气轮机进风量，以清除燃气轮机和烟道中可能积聚的可燃混合物。

## 12.3 燃气轮机的联锁保护系统说明
##### 1、总原则
##### (1)燃气轮机联锁保护的设计为任意一个原因发生时，则燃气轮机停机的逻辑关系。
##### (2)除紧急停机按钮外，任意一个原因或停机动作，则均在DCS系统上设置旁路软开关，方便操作人员。
##### (3)所有原因发生后，均需通过DCS系统软件复位按钮确认后才可重新投入。
##### 2、锅炉联锁原因及条件
##### (1)紧急停炉按钮按下。
##### (2)汽包水位高联锁：当两台汽包水位测量差压变送器的测量信号均高高时。
##### (3)汽包水位低联锁：当两台汽包水位测量差压变送器的测量信号均低低时。
##### (4)主蒸汽压力高联锁：当主蒸汽压力测量压力变送器的测量信号高高时。
##### (5)引风机故障停机时。

## 12.4 控制室布置
##### 本工程采用机炉电集中控制。操作员站，工程师站，工业电视，打印机等布置在机炉电集中控制室内。过程控制机柜、热控配电柜、电气机柜、安放在机柜室内。

## 12.5 工业电视系统
##### 为了满足生产的要求，监视设备的运行情况，在本项目中设立如下工业电视系统：
##### 锅炉汽包水位电视监控系统2个摄像头，2个显示器，专业监视器42寸。锅炉汽包及集箱就地压力表引至水位计附近，利用摄像头进行就地监控。
##### 配置一套工业电视监控系统，2个显示器，专业监视器42寸，摄像头为网络高清摄像头。

## 12.6 电源和气源
##### 电源是热控设备的动力，是机组安全运行的保证，必须保证供电电源的可靠性。
##### 分散控制系统(DCS)系统要求提供两路电源：一路来自交流不停电电源(在线式UPS 220V AC)；另一路来自低压厂用母线(220V AC)。在机柜间内配有电源自动切换装置自动完成柜内设备所需电源的配电。控制室内的设备供电由UPS电源提供，断电后持续运行时间不少于30分钟。
##### 仪表气源
##### 气动阀门需要的气源采用氮气或压缩空气，全厂共用一套空气压缩系统。

# 13. 主厂房布置（暂定）
## 13.1 锅炉布置
##### 本工程规划1台燃机配1台余热锅炉另外布置一台燃气锅炉，燃机为轴向排气，余热锅炉与燃气轮机以组同轴线连续布置，拟依次平行布置，余热锅炉采用露天布置，满足辅助设备布置及通道要求，锅炉设有旁路烟囱，保证变工况时余热锅炉的安全。余热锅炉设有疏水泵房，该泵房中布置有一座20m3疏水箱和一台疏水泵，疏水扩容器布置在疏水箱上，回收余热锅炉疏放水，其炉水加药装置也布置在该泵房内，燃气锅炉与余热锅炉并排布置。
## 13.2 燃机布置
##### 燃机室外布置燃机房柱距，宽度，运转层标高，屋底标高。
# 14. 建筑及结构
## 14.1 设计原则
##### 1、在满足工艺合理的条件下，按照“安全、适用、经济、美观、环保”的设计原则设计，以人为本，采用人机工程学、价值工程学、环境工程学等现代科学设计理念方法设计。
##### 2、主厂房采用技术先进、工艺成熟的柜排架结构，所有建构筑物造型、色调均力求简洁、明快。
##### 3、按照国家节约能源法(1997)因地制宜，尽量就地取材，优先采用国家推广的新型、轻质、环保材料；合理选择建筑窗地，以满足热工、采光、审美要求。
##### 4、主要建筑材料
##### (1)现浇及预制构件均采用普通硅酸盐水泥，砼强度等级≥C20
##### (2)墙砌体采用粘土空心砖或轻质砌块。
##### (3)门窗多采用PVC塑钢门窗或铝合金门窗，少量采用塑钢、木门窗。

## 14.2 建筑装修标准（分高、中、低档）
##### （1）地面
##### 一般地面采用C20细石混凝土，操作室内采用抗静电地板砖，平台采用防滑地砖地面，楼梯栏杆采用不锈钢。
##### （2）屋面防水
##### 除有特殊要求的屋面外，均使用4mm厚SBS改性沥青防水卷材。
##### （3）墙体
##### 砖混结构为普通粘土砖，内墙厚240，外墙240。燃机间框架结构采用彩钢夹心板维护，除氧间填充墙为砌体墙。
##### （4）装修
##### 内外墙面及顶棚均抹灰，刷涂料并作踢脚。
##### （5）门、窗
##### 控制室采用防爆隔音门窗，其余采用普通铝合金门窗。屋面采用双坡钢屋架，屋面采用保温彩钢板，天窗架采用钢天窗架上铺彩板。

## 14.3 建筑防火
##### 各建筑耐火等级均为二级及以上，按火灾危险性分类，除材料库外(丙类)其余均为丁类及以下；各建筑除在选用材料上满足建筑防火规范要求外，主厂房楼梯间通道，高低压配电室，电缆井道检查门，均设防火门，主厂房各层均设消防系统；各建筑主要层及控制室，变配电室等处均设灭火设施。各建构筑物之间距及分区满足规范要求。

## 14.4 主要建(构)筑物结构设计
##### 1、基本资料
##### 抗震设防烈度为8度，设计基本地震动峰值加速度区划为O.10g，设计地震分组为第一组。场地土为Ⅱ类场地。风荷载为0.40kN/m2。
##### 2、结构形式
##### 主厂房采用砼框排架结构。
##### 化水间、循环水泵房采用多层砼框架结构。
##### 3、基础
##### 厂房基础采用钢筋砼独立基础，基础埋深，其余建筑物基础埋深1.80m。
##### 烟囱、锅炉基础采用筏板基础。各主机基础与主厂房基础脱开。

# 15. 通风及空气调节部分
## 15.1 通风设计
##### 需全面通风的房间采用机械通风方式。除需全面通风的房间采用自然通风。配电室设事故排风，平时兼作通风换气，换气次数按每小时12次设计。出线小室设机械排风系统，利用百叶风口（带过滤网）自然进风，换气次数按每小时15次设计。电缆夹层设机械排风系统，换气次数按每小时6次设计。化验室换气次数按每小时10次设计轴流风机。药品室设换气次数15次的机械通风装置，室内吸风口底部距地面0.5m处，且选用电动机、通风机直接连接的防爆通风机。风机选用T35-11系列轴流式通风机，该风机结构合理，具有较高的效率和较低的噪音。
## 15.2 空调设计
##### 为满足工艺及人体卫生对房间的温度、湿度要求，在控制室、机柜室、电气室等房间内设有空调系统。在设有火灾报警系统的房间内，空调设施与火灾报警系统连锁关闭。
##### 表15.2-1空调场所、设计温度及空调方式表

| 序号 |建筑部位 |室内设计温度（℃） |空调方式 |
|:------|:------|:------|:------|
| 1 |控制室 |18～28 |柜式空调 |
| 2 |高低压配电室 |<35℃ |柜式空调 |

# 16. 经济性分析（估算）
##### 本能源站位于工业园内，拟建设一个能源要素保障企业，为园区内各企业提供价格低廉，质量保证的电力和蒸汽保障。能源站建设供电(手动输入)，供汽(手动输入)主机及其公辅设施，本章对其经济性做出经济效益分析。
## 16.1 编制依据
##### 根据我国现行法律、法规、财税制度和电价政策，按照国家发展改革委和建设部2006年联合颁发的《建设项目经济评价方法与参数（第三版）》、《火力发电厂工程经济评价导则》《火电厂工程限额设计参考造价指标》等指导文件进行财务评价。

## 16.2 经济效益分析
##### 项目建设期为(手动输入)个月，生产运营期取25年，财务评价计算期为26年。经济评价项目工程费用预计(手动输入)万元（不包含征地费,管道建设费，办公楼及其他费用），税费按国家法律规定，按满负荷运转计算。如下表所示为该项目的收益和费用表。其中电价按工业园区统一电价即上网电价：@@ccpp_questionnaire.net_electricity_price@@，自用电价：@@ccpp_questionnaire.personal_electricity_price@@，厂区设备自耗电按5%计算，燃气价格:@@ccpp_questionnaire.price_design@@元/Nm3，蒸汽价格:@@ccpp_questionnaire.steam_price_1@@元/t计算(当地园区企业自供汽的成本价)。
本项目的费用主要包括消耗的燃气以及冷却蒸发消耗的工业原水以及锅炉及输送管道的汽水损失，以及工资福利等；工业原水按需求调研表！元/t计算，生活用水按居民生活用水需求调研表！元/t计算，除盐水按需求调研表！元/t计算。
本项目投资估算包括设备采购费用，设备安装费用，建筑工程费用，，预备费，铺底流动资金，土地购置费用等构成，本方案只考虑工程费用不考虑输汽管网建造费用、办公楼和其他费用，初步估价为(手动输入)万元，预估管网建设费用(手动输入)万元，总计(手动输入)万元。

## 16.3 敏感性分析
##### 从以上数据分析，投资的盈利水平与经营成本以及产品的价格较为敏感；从产品价格的角度来看，从长远来讲，受环保煤改气的压力影响，蒸汽是呈上升趋势的。经营成本的最主要构成是燃气价格和电价，燃气价格和电价对投资的盈利水平的影响是显著的。因此为了投资回收期的缩短的最好办法就是降低锁定燃气价格，提高蒸汽及电力售价。
# 17. 结论和建议
##### 本项目是燃气轮机热电联产工程，燃机、余热锅炉等都是成熟的产品，安装工期较短，且质量较好保证；项目地区电力和蒸汽需求稳定，且处于不断增长阶段；燃气供应充足，且价格适中；地方政府对项目的支持力度较大。本项目盈利的关键点在于燃气气价、电价以及蒸汽的供应价格以及稳定的蒸汽和电力需求；合理的气价、电价和蒸汽价格能给业主带来明显的投资效益和环保效益。

"""
}]


class InitCcppReportTemplate():
    # 初始化数据
    @staticmethod
    def init_data():
        data = [
            reportTemplate_data
        ]
        for index in range(len(data)):
            InitCcppReportTemplate.insert_constant(data[index])

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
textlogic_data = [{
    "textlogickey": u"ccpplogic[0]",
    "textlogicvalue": u"##### @@\'单压\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \"singlepot\" else \'双压\'@@",
    "textlogicremarks": u"如果是单压输出：单压，如果是双压输出： 双压",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[1]",
    "textlogicvalue": u"##### @@\'2）补燃型单压余热锅炉主要参数（手动选择）\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \"singlepot\" else \'2）补燃型双压余热锅炉主要参数\'@@",
    "textlogicremarks": u"如果是单压输出：2）补燃型单压余热锅炉主要参数（手动选择），如果是双压输出：2）补燃型双压余热锅炉主要参数",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[2]",
    "textlogicvalue": u"##### @@\'额定蒸发量\'ccpp_ccpp.sp_low_gas_production_design\' t/h（最终根据最低蒸汽负荷选取）\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'高压额定蒸发量\'ccpp_ccpp.high_gas_production\' t/h（最终根据最低蒸汽负荷选取）\'@@",
    "textlogicremarks": u"如果是单压输出：额定蒸发量X t/h, 如果是单压输出：高压额定蒸发量X t/h",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[3]",
    "textlogicvalue": u"##### @@\'给水温度\'ccpp_ccpp.sp_low_feedwater_temperature_design\'℃\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'给水温度\'ccpp_ccpp.high_economizer_effluent_water_temperature_design\'℃\'@@",
    "textlogicremarks": u"如果是单压输出：给水温度X℃, 如果是双压输出：给水温度X℃, 高压进省煤器热水温度X℃",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[4]",
    "textlogicvalue": u"@@\'\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 低压段压力\'ccpp_ccpp.low_drum_pressure_design\' MPa\'@@",
    "textlogicremarks": u"如果是双压输出：低压段压力X℃",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[5]",
    "textlogicvalue": u"@@\'\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 低压段压力\'ccpp_ccpp.low_drum_pressure_design\' MPa\'@@",
    "textlogicremarks": u"如果是双压输出：低压段压力X℃",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[6]",
    "textlogicvalue": u"@@\'\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 低压段温度\'ccpp_ccpp.low_effluent_smoke_temperature_design\'℃ MPa\'@@",
    "textlogicremarks": u"如果是双压输出：低压段温度X℃",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[7]",
    "textlogicvalue": u"@@\'\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 额定蒸发量\'ccpp_ccpp.low_gas_production_design\' t/h（最终根据最低蒸汽负荷选取）\'@@",
    "textlogicremarks": u"如果是双压输出：额定蒸发量X℃",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[8]",
    "textlogicvalue": u"@@\'\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 给水温度\'ccpp_ccpp.low_feedwater_temperature_design\'℃\'@@",
    "textlogicremarks": u"如果是双压输出：给水温度X℃",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[9]",
    "textlogicvalue": u"@@\'##### 主蒸汽系统采用母管制：低压主汽从余热锅炉低压过热器出口一部分用于锅炉自除氧，另一部分经电动关断阀，流量计等接至低压蒸汽母管。低压蒸汽管道上应有1分支管直供能源站用作采暖或者供应生活热水。\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 蒸汽系统采用母管制，蒸汽由每台锅炉出口集箱引出接至不同参数的蒸汽母管。\'@@",
    "textlogicremarks": u"8.1 主蒸汽及旁路系统文本逻辑4",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[10]",
    "textlogicvalue": u"@@\'##### 低压蒸汽管道材料选用12Cr1MoV，进水或进汽压力高于容器设计压力的各类压力容器应装设安全阀。安全阀的排放能力应大于容器的安全泄放量。标准按《电力工业锅炉压力容器监察规程》DL612-1996执行。\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 中压主蒸汽(3.88MPa)管道从余热锅炉的高压过热器出口引出，接入主蒸汽母管，从主蒸汽母管分支接至用户或汽轮机主汽阀，蒸汽管道上设置流量测量装置，在锅炉侧设电动隔离阀，供余热锅炉停炉保压用。高压主蒸汽母管道上并联设置2套减温减压装置，通过减温减压后向园区提供1.0MPa的蒸汽，可满足汽轮机停机时正常供热 的需要，提高供热的可靠性。\'@@",
    "textlogicremarks": u"8.1 主蒸汽及旁路系统文本逻辑3",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[11]",
    "textlogicvalue": u"@@\'\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 低压蒸汽（1MPa）管道从余热锅炉的低压过热器出口引出，一部分用于锅炉自除氧，另一部分接入低压蒸汽母管，蒸汽管道上设置流量测量装置，在锅炉侧设电动隔离阀。低压蒸汽管道采用单母管制设置，低压蒸汽母管有园区蒸汽用户。低压蒸汽母管有1分支管直供能源站用作采暖或者供应生活热水。\'@@",
    "textlogicremarks": u"8.1 主蒸汽及旁路系统文本逻辑2",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[12]",
    "textlogicvalue": u"@@\'\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'##### 蒸汽管道材料选用12Cr1MoV，进水或进汽压力高于容器设计压力的各类压力容器应装设安全阀。安全阀的排放能力应大于容器的安全泄放量。标准按《电力工业锅炉压力容器监察规程》DL612-1996执行。\'@@",
    "textlogicremarks": u"8.1 主蒸汽及旁路系统文本逻辑1",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[13]",
    "textlogicvalue": u"@@\'\'ccpp_ccpp.sp_low_gas_production_design\'*1.1\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \'singlepot\' else \'4567893213215641231413228454\'@@@@\'4567893213215641231413228454\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \'singlepot\' else \'(\'ccpp_ccpp.high_gas_production_design\'+\'ccpp_ccpp.low_gas_production_design\')*1.1\'@@",
    "textlogicremarks": u"本工程额定工业热负荷为(（CCPP!G45+CCPPG67）*1.1,双压锅炉)（CCPPG106*1.1，单压锅炉）t/h",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[14]",
    "textlogicvalue": u"@@\'4567893213215641231413228454\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'(\'ccpp_ccpp.high_gas_production_design\'+\'ccpp_ccpp.low_gas_production_design\')*1.1\' @@@@\'\'ccpp_ccpp.sp_low_gas_production_design\'*1.1\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'4567893213215641231413228454\'@@",
    "textlogicremarks": u"1）锅炉额定蒸发量： (（CCPP!G45+CCPPG67）*1.1,双压锅炉)（CCPPG106*1.1，单压锅炉）",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[15]",
    "textlogicvalue": u"@@\'4567893213215641231413228454\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'(\'ccpp_ccpp.high_gas_production_design\'+\'ccpp_ccpp.low_gas_production_design\')*1.1\'@@@@\'\'ccpp_ccpp.sp_low_gas_production_design\'*1.1\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \'singlepot\' else \'4567893213215641231413228454\'@@",
    "textlogicremarks": u"2）厂内汽水循环正常损失：(（CCPP!G45+CCPPG67）*1.1,双压锅炉)（CCPPG106*1.1，单压锅炉）",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[16]",
    "textlogicvalue": u"@@\'4567893213215641231413228454\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'(\'ccpp_ccpp.high_gas_production_design\'+\'ccpp_ccpp.low_gas_production_design\')*1.1\'@@@@\'\'ccpp_ccpp.sp_low_gas_production_design\'*1.1\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \'singlepot\' else \'4567893213215641231413228454\'@@",
    "textlogicremarks": u"3）锅炉正常排污损失： (（CCPP!G45+CCPPG67）*1.1,双压锅炉)（CCPPG106*1.1，单压锅炉）",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[17]",
    "textlogicvalue": u"@@\'4567893213215641231413228454\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'round((\'ccpp_ccpp.high_gas_production_design\'+\'ccpp_ccpp.low_gas_production_design\')*1.1*0.03,5)\'@@@@\'round(\'ccpp_ccpp.sp_low_gas_production_design\'*1.1*0.03,5)\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \'singlepot\' else \'4567893213215641231413228454\'@@",
    "textlogicremarks": u"4）水处理系统耗水量：（CCPP!G45+CCPPG67）*1.1,双压锅炉)（CCPPG106*1.1，单压锅炉）*0.03取整",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[18]",
    "textlogicvalue": u"@@\'4567893213215641231413228454\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'round((\'ccpp_ccpp.high_gas_production_design\'+\'ccpp_ccpp.low_gas_production_design\')*1.1*0.03,5)\'@@@@\'round(\'ccpp_ccpp.sp_low_gas_production_design\'*1.1*0.03, 5)\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \'singlepot\' else \'4567893213215641231413228454\'@@",
    "textlogicremarks": u"5）其它不可预计用水损失：(CCPP!G45+CCPPG67）*1.1,双压锅炉)（CCPPG106*1.1，单压锅炉）*0.03取整",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[19]",
    "textlogicvalue": u"@@\'4567893213215641231413228454\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'(\'ccpp_ccpp.high_gas_production_design\'+\'ccpp_ccpp.low_gas_production_design\')*1.1\'@@@@\'round(\'ccpp_ccpp.sp_low_gas_production_design\'*1.1*0.03, 5)\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \'singlepot\' else \'4567893213215641231413228454\'@@",
    "textlogicremarks": u"6）启动或事故增加用水量： (（CCPP!G45+CCPPG67）*1.1,双压锅炉)（CCPPG106*1.1，单压锅炉）",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}, {
    "textlogickey": u"ccpplogic[20]",
    "textlogicvalue": u"@@\'4567893213215641231413228454\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is  \'singlepot\' else \'(\'ccpp_ccpp.high_gas_production_design\'+\'ccpp_ccpp.low_gas_production_design\')*1.1\'@@@@\'round(\'ccpp_ccpp.sp_low_gas_production_design\'*1.1*0.03, 5)\' if \"ccpp_ccpp.boiler_single_or_dula_pressure_design\" is \'singlepot\' else \'4567893213215641231413228454\'@@",
    "textlogicremarks": u"7）外供汽损失： (（CCPP!G45+CCPPG67）*1.1,双压锅炉)（CCPPG106*1.1，单压锅炉）",
    "module_name": u"CCPP",
    "template_id": "",
    "plan_id": ""
}]


class InitCcppTextlogic():
    # 初始化数据
    @staticmethod
    def init_data():
        data = [
            textlogic_data
        ]
        for index in range(len(data)):
            InitCcppTextlogic.insert_constant(data[index])

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
