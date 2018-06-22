# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from ... import db
from ... import login_manager


# 煤气发电常量表
class GasPowerGenerationConstant(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_constant'
    __table_args__ = {'comment': u'煤气发电常量表'}

    # 常量表id， 自动生成
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 模块(页面)id：
    module_name = db.Column(db.String(200), index=True)
    # 字段英文名
    name_eng = db.Column(db.String(200))
    # 字段中文名
    name = db.Column(db.String(200))
    # 表示符号
    symbol = db.Column(db.String(200))
    # 计量单位
    unit = db.Column(db.String(50))
    # 计算公式
    calculate = db.Column(db.String(200))
    # 备注
    remark = db.Column(db.Text())
    # 默认值
    default_value = db.Column(db.String(200))
    # 是否为disable(t可修改，f不可修改)
    disable = db.Column(db.String(2))

    @staticmethod
    def create_gasPowerGenerationConstant(module_name, name_eng, name, symbol, 
                                        unit, calculate, remark, default_value, disable):
        gasPowerGenerationConstant = GasPowerGenerationConstant()
        gasPowerGenerationConstant.module_name = module_name
        gasPowerGenerationConstant.name_eng = name_eng
        gasPowerGenerationConstant.name = name
        gasPowerGenerationConstant.symbol = symbol
        gasPowerGenerationConstant.unit = unit
        gasPowerGenerationConstant.calculate = calculate
        gasPowerGenerationConstant.remark = remark
        gasPowerGenerationConstant.default_value = default_value
        gasPowerGenerationConstant.disable = disable

        return gasPowerGenerationConstant

    @staticmethod
    def insert_gasPowerGenerationConstant(gasPowerGenerationConstant):
        try:
            db.session.add(gasPowerGenerationConstant)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gasPowerGenerationConstant<id=%s, module_name=%s>" %
                  (gasPowerGenerationConstant.id, gasPowerGenerationConstant.module_name))

    @staticmethod
    def search_gasPowerGenerationConstant(module_name):
        result = GasPowerGenerationConstant.query.filter_by(module_name=module_name).all()
        return result

    def __repr__(self):
        return '<gasPowerGenerationConstant %r>' % self.module_name

# 锅炉辅机系统表
class GPGBoilerAuxiliaries(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_boiler_auxiliaries'
    __table_args__ = {'comment': u'煤气发电锅炉辅机系统表'}
    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 定期排污扩容器 
    # 锅炉蒸发量
    r_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-锅炉蒸发量")
    # 排放时间
    r_emission_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排放时间")
    # 定期排污率
    r_emission_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-定期排污率")
    # 定期排污水量
    r_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-定期排污水量")
    # 汽包压力
    r_drum_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-汽包压力")
    # 汽包压力下的饱和水焓
    r_drum_aturatedwater_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-汽包压力下的饱和水焓")
    # 排污扩容器工作压力
    r_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污扩容器工作压力")
    # 扩容器压力下饱和水焓
    r_work_aturatedwater_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器压力下饱和水焓")
    # 扩容器压力下蒸汽比容
    r_work_steam_special_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器压力下蒸汽比容")
    # 扩容器压力下汽化潜热
    r_work_latentheat_vaporization = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器压力下汽化潜热")
    # 扩容器蒸汽干度
    r_work_steam_dryness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器蒸汽干度")
    # 扩容器单位容积润许极限强度
    r_ultimate_strength = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-扩容器单位容积润许极限强度")
    # 排污水汽化量
    r_vaporization_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污水汽化量")
    # 富裕系数
    r_affluence_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-富裕系数")
    # 排污扩容汽容积
    r_steam_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污扩容汽容积")
    # 排污扩容容积
    r_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污扩容容积")
    # 扩容器规格选取
    r_specifications = db.Column(db.Text(), comment=u"定期排污扩容器-扩容器规格选取")

    # 连续排污扩容器
    # 锅炉蒸发量
    c_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-锅炉蒸发量")
    # 连续排污率
    c_emission_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-连续排污率")
    # 连续排污水量
    c_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-连续排污水量")
    # 汽包压力
    c_drum_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-汽包压力")
    # 汽包压力下的饱和水焓
    c_drum_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-汽包压力下的饱和水焓")
    # 排污扩容器工作压力
    c_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污扩容器工作压力")
    # 扩容器压力下饱和水焓
    c_work_aturatedwater_enthalpy = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下饱和水焓")
    # 扩容器压力下蒸汽比容
    c_work_steam_pecificvolume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下蒸汽比容")
    # 扩容器压力下汽化潜热
    c_work_latentheat_vaporization = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器压力下汽化潜热")
    # 扩容器蒸汽干度
    c_steam_dryness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器蒸汽干度")
    # 扩容器单位容积润许极限强度
    c_ultimate_strength = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-扩容器单位容积润许极限强度")
    # 排污水汽化量
    c_vaporization_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污水汽化量")
    # 富裕系数
    c_affluence_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-富裕系数")
    # 排污扩容汽容积
    c_steam_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"连续排污扩容器-排污扩容汽容积")
    # 排污扩容容积
    c_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"定期排污扩容器-排污扩容容积")
    # 扩容器规格选取
    c_specifications = db.Column(db.Text(), comment=u"连续排污扩容器-扩容器规格选取")

    # 磷酸盐加药装置
    # 锅炉水系统容积
    d_boiler_watersystem_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-锅炉水系统容积")
    # 应维持的磷酸根含量
    d_phosphate_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-应维持的磷酸根含量")
    # 给水硬度（原水）
    d_water_hardness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-给水硬度（原水）")
    # 纯度
    d_purity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-纯度")
    # 锅炉启动时加药量
    d_boiler_dosage_startup = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-锅炉启动时加药量")
    # 锅炉给水量
    d_boiler_water_supply = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-锅炉给水量")
    # 锅炉排污量
    d_boiler_sewage_quantity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-锅炉排污量")
    # 运行时加药量
    d_boiler_dosage_run = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-运行时加药量")
    # 磷酸钠浓度
    d_na3po4_concentration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-磷酸钠浓度")
    # 在C浓度下的磷酸三钠密度
    d_na3po4_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-在C浓度下的磷酸三钠密度")
    # 运行时汽包内加入的溶液量
    d_solution_quantity_run = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"磷酸盐加药装置-运行时汽包内加入的溶液量")

    # 给水泵
    # 锅炉设计使用压力
    p_boiler_design_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-锅炉设计使用压力")
    # 省煤器入口进水压力
    p_inlet_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-省煤器入口进水压力")
    # 除氧器工作压力
    p_deaerator_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-除氧器工作压力")
    # 给水管阻力（以压头计）
    p_water_supply_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-给水管阻力（以压头计）")
    # 进水管阻力（以压头计）
    p_water_inlet_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-进水管阻力（以压头计）")
    # 水泵中心至汽包正常水位的几何高度差
    p_center_altitude_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-水泵中心至汽包正常水位的几何高度差")
    # 除氧器最低水位至水泵中心几何高度差（给水泵进口静水头）
    p_deaerator_altitude_difference = db.Column(
        db.NUMERIC(precision=15, scale=5), comment=u"给水泵-除氧器最低水位至水泵中心几何高度差（给水泵进口静水头）")
    # 给水泵总扬程
    p_feedpump_total_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-给水泵总扬程")
    # 流量
    p_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-流量")
    # 泵效率
    p_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-泵效率")
    # 机械传动效率
    p_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-机械传动效率")
    # 电动机效率
    p_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-电动机效率")
    # 电动机备用系数
    p_motor_reserve_factor = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-电动机备用系数")
    # 配套电机功率
    p_auxiliary_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水泵-配套电机功率")
    # 给水泵选用规格
    p_specifications = db.Column(db.Text(), comment=u"给水泵-给水泵选用规格")

    # 锅炉补给水处理能力
    # 锅炉蒸发量
    m_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-锅炉蒸发量")
    # 补汽量
    m_makeup_steam = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-补汽量")
    # 厂内汽水循环损失
    m_steamwater_cycle_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-厂内汽水循环损失")
    # 排污损失
    m_pollution_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-排污损失")
    # 凝结水量
    m_condensing_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-凝结水量")
    # 换热凝结水损失
    m_condensate_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-换热凝结水损失")
    # 锅炉正常补水量
    m_boiler_normal_watersupply = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-锅炉正常补水量")
    # 除盐设备自用水率
    m_boiler_desalted_water_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-除盐设备自用水率")
    # 一级除盐设备工作周期
    m_boiler_desalted_work_cycle = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-一级除盐设备工作周期")
    # 设备再生时间
    m_boiler_desalted_rebirth_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-设备再生时间")
    # 启动或事故增加损失
    m_increase_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-锅炉最大补水量")
    # 锅炉最大补水量
    m_boiler_max_watersupply = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-锅炉最大补水量")
    # 水处理设备全部出力
    m_boiler_watersupply_all = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉补给水处理能力-水处理设备全部出力")
    # 选取水处理设备出力
    m_boiler_watersupply_specifications = db.Column(db.Text(), comment=u"锅炉补给水处理能力-选取水处理设备出力")
    # 化学除盐水工艺类型
    desalted_water_tech_type = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 化学除盐水工艺名称
    desalted_water_tech_name = db.Column(db.Text(), comment=u"锅炉补给水处理能力-化学除盐水工艺类型")

    # 除氧水箱/凝结水箱 共用
    # 锅炉蒸发
    s_boiler_evaporation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-锅炉蒸发")
    # 储水时间
    s_storage_time = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-储水时间")
    # 容积
    s_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-容积")
    # 尺寸 长
    s_size_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-尺寸 长")
    # 尺寸 直径
    s_size_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧水箱/凝结水箱-尺寸 直径")

    # 除氧器安装高度核算
    # 最大给水量
    s_max_feedwater_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-最大给水量")
    # 热力除氧压力
    s_de_ox_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-热力除氧压力")
    # 当地大气压
    s_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-当地大气压")
    # 当地大气压对应下的密度
    s_local_atmosphere_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-当地大气压对应下的密度")
    # 设计流量
    s_design_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-设计流量")
    # 泵必需汽蚀余量
    s_net_positive_suction_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-泵必需汽蚀余量")
    # 吸入管路的总阻力
    s_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-吸入管路的总阻力")
    # 泵入口流速
    s_inlet_speed = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-泵入口流速")
    # 附加高度
    s_added_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-附加高度")
    # 泵安装高度
    s_pump_install_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器安装高度核算-泵安装高度")

    # 减温减压器
    # 新蒸汽温度
    new_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-新蒸汽温度")
    # 新蒸汽压力
    new_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-新蒸汽压力")
    # 新蒸汽焓
    new_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-新蒸汽焓")
    # 新蒸汽流量
    new_steam_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-新蒸汽流量")
    # 减温水温度
    desuperheater_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水温度")
    # 减温水压力
    desuperheater_water_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水压力")
    # 减温水焓
    desuperheater_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水焓")
    # 减温水流量
    desuperheater_water_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水流量")
    # 减温后蒸汽温度
    desuperheater_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温后蒸汽温度")
    # 减温后蒸汽压力
    desuperheater_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温后蒸汽压力")
    # 减温后蒸汽焓
    desuperheater_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温后蒸汽焓")
    # 饱和水焓值
    saturation_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-饱和水焓值")
    # 减温水中未蒸发部分所占份额
    no_vaporized_percent = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温水中未蒸发部分所占份额")
    # 减温减压器流量
    de_press_temp_device_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"减温减压器-减温减压器流量")

    # 蓄热器
    # 充热压力
    charging_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热压力")
    # 放热压力
    exothermic_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力")
    # 充热压力下的饱和水焓
    charging_saturation_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热压力下的饱和水焓")
    # 放热压力下的饱和水焓
    exothermic_saturation_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力下的饱和水焓")
    # 充热压力下的饱和汽焓
    charging_saturation_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热压力下的饱和汽焓")
    # 放热压力下的饱和汽焓
    exothermic_saturation_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力下的饱和汽焓")
    # P2压力下产生蒸汽量
    p2_steam_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-P2压力下产生蒸汽量")
    # 充热压力下的饱和水比容
    charging_water_specific_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热压力下的饱和水比容")
    # 单位水容积蓄热量
    unit_water_heat_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-单位水容积蓄热量")
    # 蓄热器热效率
    regenerarot_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器热效率")
    # 充水系数
    water_fill_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充水系数")
    # 蓄热器的蓄热量
    regenerarot_heat_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器的蓄热量")
    # 蓄热器容积
    regenerarot_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器容积")
    # 蓄热器上部蒸汽容积
    regenerarot_top_steam_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器上部蒸汽容积")
    # 锅炉最大负荷
    boiler_max_load = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-锅炉最大负荷")
    # 锅炉平均负荷
    boiler_average_load = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-锅炉平均负荷")
    # 蓄热器最大放汽量
    regenerarot_max_bleed = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-蓄热器最大放汽量")
    # 质量蒸发强度
    evaporation_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-质量蒸发强度")
    # 放热压力下的质量蒸发强度
    exothermic_evaporation_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力下的质量蒸发强度")
    # 充热状态下的体积
    charging_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-充热状态下的体积")
    # 放热压力下的饱和水比容
    exothermic_water_specific_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热压力下的饱和水比容")
    # 放热完了水的体积
    exothermic_water_volume = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蓄热器-放热完了水的体积")

    def __init__(self, **kwargs):
        super(GPGBoilerAuxiliaries, self).__init__(**kwargs)

    @staticmethod
    def insert_boiler_auxiliaries(gaspowergeneration_boiler_auxiliaries):
        try:
            db.session.add(gaspowergeneration_boiler_auxiliaries)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update GPGBoilerAuxiliaries"
                  "<id=%s> in database" % ( gaspowergeneration_boiler_auxiliaries.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_boiler_auxiliaries(planId):
        result = GPGBoilerAuxiliaries.query.filter_by(
            plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_boiler_auxiliaries(plan_id):
        boiler_auxiliaries = \
            GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
        try:
            db.session.delete(boiler_auxiliaries)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete boiler_auxiliaries<id=%s, plan_id=%s> in database" %
                  (boiler_auxiliaries.id, boiler_auxiliaries.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        boiler_auxiliaries = GPGBoilerAuxiliaries.search_boiler_auxiliaries(plan_id)
        db.session.delete(boiler_auxiliaries)

# 汽水管道
class GPGSteamWaterPipe(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_steam_water_pipe'
    __table_args__ = {'comment': u'煤气发电汽水管道表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    '''主蒸汽'''
    # 主蒸汽设计压力-母管
    main_steam_design_pressure_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽设计压力-母管")
    # 主蒸汽设计压力-分管
    main_steam_design_pressure_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽设计压力-分管")
    # 主蒸汽设计温度-母管
    main_steam_design_temperature_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽设计温度-母管")
    # 主蒸汽设计温度-分管
    main_steam_design_temperature_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽设计温度-分管")
    # 主蒸汽钢材-母管
    main_steam_steel_m = db.Column(db.Text(), comment=u"主蒸汽钢材-母管")
    # 主蒸汽钢材-分管
    main_steam_steel_c = db.Column(db.Text(), comment=u"主蒸汽钢材-分管")
    # 主蒸汽设计温度下许用应力-分管
    main_steam_temperature_stress_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽设计温度下许用应力-分管")
    # 主蒸汽20℃下许用应力-分管
    main_steam_20c_stress_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽20℃下许用应力-分管")
    # 主蒸汽公称压力-分管
    main_steam_nominal_pressure_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽公称压力-分管")
    # 主蒸汽管子质量流量-分管
    main_steam_pipe_mass_flow_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管子质量流量-分管")
    # 主蒸汽选取流速-分管
    main_steam_selected_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽选取流速-分管")
    # 主蒸汽介质比容-分管
    main_steam_meida_specific_volume_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽介质比容-分管")
    # 主蒸汽管子内径-分管
    main_steam_inner_diamete_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管子内径-分管")
    # 主蒸汽温度修正系数-分管
    main_steam_temperature_correct_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽温度修正系数-分管")
    # 主蒸汽许用应力修正系数-分管
    main_steam_stress_correct_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽许用应力修正系数-分管")
    # 主蒸汽附加厚度-分管
    main_steam_additional_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽附加厚度-分管")
    # 主蒸汽直管最小壁厚-分管
    main_steam_pipe_min_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽直管最小壁厚-分管")
    # 主蒸汽壁厚负偏差系数-分管
    main_steam_negative_deviation_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽壁厚负偏差系数-分管")
    # 主蒸汽壁厚负偏差附加值-分管
    main_steam_negative_deviation_added_value_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽壁厚负偏差附加值-分管")
    # 主蒸汽计算壁厚-分管
    main_steam_calculate_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽计算壁厚-分管")
    # 主蒸汽计算外径-分管
    main_steam_calculate_outer_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽计算外径-分管")
    # 主蒸汽公称通径取值-分管
    main_steam_selected_nominal_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽公称通径取值-分管")
    # 主蒸汽外径取值-分管
    main_steam_selected_outer_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽外径取值-分管")
    # 主蒸汽壁厚取值-分管
    main_steam_selected_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽壁厚取值-分管")
    # 主蒸汽内径取值-分管
    main_steam_selected_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽内径取值-分管")
    # 主蒸汽反推流速-分管
    main_steam_backstepping_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽反推流速-分管")
    # 主蒸汽最终选取管道规格-分管
    main_steam_selected_pipe_spec_c = db.Column(db.Text(), comment=u"主蒸汽最终选取管道规格-分管")

    # 主蒸汽运行压力-母管
    main_steam_work_press_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽运行压力-母管")
    # 主蒸汽运行压力-分管
    main_steam_work_press_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽运行压力-分管")
    # 主蒸汽运行温度-母管
    main_steam_work_temperature_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽运行温度-母管")
    # 主蒸汽运行温度-分管
    main_steam_work_temperature_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽运行温度-分管")
    # 主蒸汽额定流量-母管
    main_steam_rated_flow_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽额定流量-母管")
    # 主蒸汽额定流量-分管
    main_steam_rated_flow_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽额定流量-分管")
    # 主蒸汽介质比容-母管
    main_steam_msv_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽介质比容-母管")
    # 主蒸汽介质比容-分管
    main_steam_msv_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽介质比容-分管")
    # 主蒸汽介质运动粘度-母管
    main_steam_media_viscosity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽介质运动粘度-母管")
    # 主蒸汽介质运动粘度-分管
    main_steam_media_viscosity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽介质运动粘度-分管")
    # 主蒸汽流速-母管
    main_steam_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽流速-母管")
    # 主蒸汽流速-分管
    main_steam_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽流速-分管")
    # 主蒸汽计算流速-母管
    main_steam_calculate_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽计算流速-母管")
    # 主蒸汽计算流速-分管
    main_steam_calculate_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽计算流速-分管")
    # 主蒸汽动压头-母管
    main_steam_dynamic_head_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽动压头-母管")
    # 主蒸汽动压头-分管
    main_steam_dynamic_head_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽动压头-分管")
    # 主蒸汽管道外径-母管
    main_steam_pipe_outer_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管道外径-母管")
    # 主蒸汽管道外径-分管
    main_steam_pipe_outer_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管道外径-分管")
    # 主蒸汽管道壁厚-母管
    main_steam_pipe_thickness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管道壁厚-母管")
    # 主蒸汽管道壁厚-分管
    main_steam_pipe_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管道壁厚-分管")
    # 主蒸汽管道内径-母管
    main_steam_pipe_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管道内径-母管")
    # 主蒸汽管道内径-分管
    main_steam_pipe_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管道内径-分管")
    # 主蒸汽摩擦阻力-母管
    main_steam_friction_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽摩擦阻力-母管")
    # 主蒸汽摩擦阻力-分管
    main_steam_friction_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽摩擦阻力-分管")
    # 主蒸汽雷诺数-母管
    main_steam_reynolds_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽雷诺数-母管")
    # 主蒸汽雷诺数-分管
    main_steam_reynolds_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽雷诺数-分管")
    # 主蒸汽等值粗糙度-母管
    main_steam_equivalent_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽等值粗糙度-母管")
    # 主蒸汽等值粗糙度-分管
    main_steam_equivalent_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽等值粗糙度-分管")
    # 主蒸汽相对粗糙度-母管
    main_steam_relative_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽相对粗糙度-母管")
    # 主蒸汽相对粗糙度-分管
    main_steam_relative_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽相对粗糙度-分管")
    # 主蒸汽摩擦阻力系数-母管
    main_steam_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽摩擦阻力系数-母管")
    # 主蒸汽摩擦阻力系数-分管
    main_steam_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽摩擦阻力系数-分管")
    # 主蒸汽单位长度摩擦阻力-母管
    main_steam_unit_length_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽单位长度摩擦阻力-母管")
    # 主蒸汽单位长度摩擦阻力-分管
    main_steam_unit_length_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽单位长度摩擦阻力-分管")
    # 主蒸汽管道长度-母管
    main_steam_pipe_length_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管道长度-母管")
    # 主蒸汽管道长度-分管
    main_steam_pipe_length_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"主蒸汽管道长度-分管")

    ''' 除氧加热蒸汽（外供）'''
    # 除氧加热蒸汽（外供）-运行压力
    deoxidized_steam_work_press = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-运行压力")
    # 除氧加热蒸汽（外供）-运行温度
    deoxidized_steam_work_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-运行温度")
    # 除氧加热蒸汽（外供）-额定流量
    deoxidized_steam_rated_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-额定流量")
    # 除氧加热蒸汽（外供）-介质比容
    deoxidized_steam_msv = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-介质比容")
    # 除氧加热蒸汽（外供）-介质运动粘度
    deoxidized_steam_media_viscosity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-介质运动粘度")
    # 除氧加热蒸汽（外供）-流速
    deoxidized_steam_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-流速")
    # 除氧加热蒸汽（外供）-计算流速
    deoxidized_steam_calculate_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-计算流速")
    # 除氧加热蒸汽（外供）-动压头
    deoxidized_steam_dynamic_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-动压头")
    # 除氧加热蒸汽（外供）-管道外径
    deoxidized_steam_pipe_outer_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-管道外径")
    # 除氧加热蒸汽（外供）-管道壁厚
    deoxidized_steam_pipe_thickness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-管道壁厚")
    # 除氧加热蒸汽（外供）-管道内径
    deoxidized_steam_pipe_inner_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-管道内径")
    # 除氧加热蒸汽（外供）-摩擦阻力
    deoxidized_steam_friction_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-摩擦阻力")
    # 除氧加热蒸汽（外供）-雷诺数
    deoxidized_steam_reynolds = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-雷诺数")
    # 除氧加热蒸汽（外供）-等值粗糙度
    deoxidized_steam_equivalent_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-等值粗糙度")
    # 除氧加热蒸汽（外供）-相对粗糙度
    deoxidized_steam_relative_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-相对粗糙度")
    # 除氧加热蒸汽（外供）-摩擦阻力系数
    deoxidized_steam_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-摩擦阻力系数")
    # 除氧加热蒸汽（外供）-单位长度摩擦阻力
    deoxidized_steam_unit_length_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-单位长度摩擦阻力")
    # 除氧加热蒸汽（外供）-管道长度
    deoxidized_steam_pipe_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧加热蒸汽（外供）-管道长度")

    ''' 低压给水(给水泵入口）'''
    # 低压给水(给水泵入口）-运行压力-母管
    l_feedwater_work_press_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-运行压力-母管")
    # 低压给水(给水泵入口）-运行压力-分管
    l_feedwater_work_press_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-运行压力-分管")
    # 低压给水(给水泵入口）-运行温度-母管
    l_feedwater_work_temperature_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-运行温度-母管")
    # 低压给水(给水泵入口）-运行温度-分管
    l_feedwater_work_temperature_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-运行温度-分管")
    # 低压给水(给水泵入口）-额定流量-母管
    l_feedwater_rated_flow_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-额定流量-母管")
    # 低压给水(给水泵入口）-额定流量-分管
    l_feedwater_rated_flow_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-额定流量-分管")
    # 低压给水(给水泵入口）-介质比容-母管
    l_feedwater_msv_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-介质比容-母管")
    # 低压给水(给水泵入口）-介质比容-分管
    l_feedwater_msv_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-介质比容-分管")
    # 低压给水(给水泵入口）-介质运动粘度-母管
    l_feedwater_media_viscosity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-介质运动粘度-母管")
    # 低压给水(给水泵入口）-介质运动粘度-分管
    l_feedwater_media_viscosity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-介质运动粘度-分管")
    # 低压给水(给水泵入口）-流速-母管
    l_feedwater_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-流速-母管")
    # 低压给水(给水泵入口）-流速-分管
    l_feedwater_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-流速-分管")
    # 低压给水(给水泵入口）-计算流速-母管
    l_feedwater_calculate_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-计算流速-母管")
    # 低压给水(给水泵入口）-计算流速-分管
    l_feedwater_calculate_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-计算流速-分管")
    # 低压给水(给水泵入口）-动压头-母管
    l_feedwater_dynamic_head_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-动压头-母管")
    # 低压给水(给水泵入口）-动压头-分管
    l_feedwater_dynamic_head_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-动压头-分管")
    # 低压给水(给水泵入口）-管道外径-母管
    l_feedwater_pipe_outer_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道外径-母管")
    # 低压给水(给水泵入口）-管道外径-分管
    l_feedwater_pipe_outer_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道外径-分管")
    # 低压给水(给水泵入口）-管道壁厚-母管
    l_feedwater_pipe_thickness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道壁厚-母管")
    # 低压给水(给水泵入口）-管道壁厚-分管
    l_feedwater_pipe_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道壁厚-分管")
    # 低压给水(给水泵入口）-管道内径-母管
    l_feedwater_pipe_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道内径-母管")
    # 低压给水(给水泵入口）-管道内径-分管
    l_feedwater_pipe_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道内径-分管")
    # 低压给水(给水泵入口）-摩擦阻力-母管
    l_feedwater_friction_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-摩擦阻力-母管")
    # 低压给水(给水泵入口）-摩擦阻力-分管
    l_feedwater_friction_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-摩擦阻力-分管")
    # 低压给水(给水泵入口）-雷诺数-母管
    l_feedwater_reynolds_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-雷诺数-母管")
    # 低压给水(给水泵入口）-雷诺数-分管
    l_feedwater_reynolds_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-雷诺数-分管")
    # 低压给水(给水泵入口）-等值粗糙度-母管
    l_feedwater_equivalent_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-等值粗糙度-母管")
    # 低压给水(给水泵入口）-等值粗糙度-分管
    l_feedwater_equivalent_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-等值粗糙度-分管")
    # 低压给水(给水泵入口）-相对粗糙度-母管
    l_feedwater_relative_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-相对粗糙度-母管")
    # 低压给水(给水泵入口）-相对粗糙度-分管
    l_feedwater_relative_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-相对粗糙度-分管")
    # 低压给水(给水泵入口）-摩擦阻力系数-母管
    l_feedwater_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-摩擦阻力系数-母管")
    # 低压给水(给水泵入口）-摩擦阻力系数-分管
    l_feedwater_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-摩擦阻力系数-分管")
    # 低压给水(给水泵入口）-单位长度摩擦阻力-母管
    l_feedwater_unit_length_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单位长度摩擦阻力-母管")
    # 低压给水(给水泵入口）-单位长度摩擦阻力-分管
    l_feedwater_unit_length_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单位长度摩擦阻力-分管")
    # 低压给水(给水泵入口）-管道长度-母管
    l_feedwater_pipe_length_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道长度-母管")
    # 低压给水(给水泵入口）-管道长度-分管
    l_feedwater_pipe_length_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道长度-分管")
    # 低压给水(给水泵入口）-局部阻力-母管
    l_feedwater_local_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-局部阻力-母管")
    # 低压给水(给水泵入口）-局部阻力-分管
    l_feedwater_local_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-局部阻力-分管")
    # 低压给水(给水泵入口）-局部阻力系数合计-母管
    l_feedwater_total_local_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-局部阻力系数合计-母管")
    # 低压给水(给水泵入口）-局部阻力系数合计-分管
    l_feedwater_total_local_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-局部阻力系数合计-分管")
    # 低压给水(给水泵入口）-弯头阻力系数-母管
    l_feedwater_elbow_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-弯头阻力系数-母管")
    # 低压给水(给水泵入口）-弯头阻力系数-分管
    l_feedwater_elbow_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-弯头阻力系数-分管")
    # 低压给水(给水泵入口）-弯头规格-母管
    l_feedwater_elbow_spec_m = db.Column(db.Text(), comment=u"低压给水(给水泵入口）-弯头规格-母管")
    # 低压给水(给水泵入口）-弯头规格-分管
    l_feedwater_elbow_spec_c = db.Column(db.Text(), comment=u"低压给水(给水泵入口）-弯头规格-分管")
    # 低压给水(给水泵入口）-弯头半径-母管
    l_feedwater_elbow_radius_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-弯头半径-母管")
    # 低压给水(给水泵入口）-弯头半径-分管
    l_feedwater_elbow_radius_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-弯头半径-分管")
    # 低压给水(给水泵入口）-弯头半径 / 管道内径-母管
    l_feedwater_elbow_radius_to_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-弯头半径 / 管道内径-母管")
    # 低压给水(给水泵入口）-弯头半径 / 管道内径-分管
    l_feedwater_elbow_radius_to_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-弯头半径 / 管道内径-分管")
    # 低压给水(给水泵入口）-单个90º弯头阻力系数-母管
    l_feedwater_90elbow_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单个90º弯头阻力系数-母管")
    # 低压给水(给水泵入口）-单个90º弯头阻力系数-分管
    l_feedwater_90elbow_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单个90º弯头阻力系数-分管")
    # 低压给水(给水泵入口）-90º弯头数量-母管
    l_feedwater_90elbow_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-90º弯头数量-母管")
    # 低压给水(给水泵入口）-90º弯头数量-分管
    l_feedwater_90elbow_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-90º弯头数量-分管")
    # 低压给水(给水泵入口）-三通阻力系数-母管
    l_feedwater_triplet_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-三通阻力系数-母管")
    # 低压给水(给水泵入口）-三通阻力系数-分管
    l_feedwater_triplet_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-三通阻力系数-分管")
    # 低压给水(给水泵入口）-单个三通阻力系数-母管
    l_feedwater_single_triplet_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单个三通阻力系数-母管")
    # 低压给水(给水泵入口）-单个三通阻力系数-分管
    l_feedwater_single_triplet_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单个三通阻力系数-分管")
    # 低压给水(给水泵入口）-三通数量-母管
    l_feedwater_triplet_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-三通数量-母管")
    # 低压给水(给水泵入口）-三通数量-分管
    l_feedwater_triplet_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-三通数量-分管")
    # 低压给水(给水泵入口）-异径管的阻力系数-母管
    l_feedwater_reducer_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-异径管的阻力系数-母管")
    # 低压给水(给水泵入口）-异径管的阻力系数-分管
    l_feedwater_reducer_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-异径管的阻力系数-分管")
    # 低压给水(给水泵入口）-渐缩管的阻力系数-母管
    l_feedwater_converging_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐缩管的阻力系数-母管")
    # 低压给水(给水泵入口）-渐缩管的阻力系数-分管
    l_feedwater_converging_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐缩管的阻力系数-分管")
    # 低压给水(给水泵入口）-渐缩管规格-母管
    l_feedwater_converging_spec_m = db.Column(db.Text(), comment=u"低压给水(给水泵入口）-渐缩管规格-母管")
    # 低压给水(给水泵入口）-渐缩管规格-分管
    l_feedwater_converging_spec_c = db.Column(db.Text(), comment=u"低压给水(给水泵入口）-渐缩管规格-分管")
    # 低压给水(给水泵入口）-渐缩管角度-母管
    l_feedwater_converging_angle_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐缩管角度-母管")
    # 低压给水(给水泵入口）-渐缩管角度-分管
    l_feedwater_converging_angle_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐缩管角度-分管")
    # 低压给水(给水泵入口）-渐缩管 较小直径与较大直径之比-母管
    l_feedwater_converging_diameter_radio_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐缩管 较小直径与较大直径之比-母管")
    # 低压给水(给水泵入口）-渐缩管 较小直径与较大直径之比-分管
    l_feedwater_converging_diameter_radio_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐缩管 较小直径与较大直径之比-分管")
    # 低压给水(给水泵入口）-渐扩管的阻力系数-母管
    l_feedwater_increasing_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐扩管的阻力系数-母管")
    # 低压给水(给水泵入口）-渐扩管的阻力系数-分管
    l_feedwater_increasing_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐扩管的阻力系数-分管")
    # 低压给水(给水泵入口）-渐扩管规格-母管
    l_feedwater_increasing_spec_m = db.Column(db.Text(), comment=u"低压给水(给水泵入口）-渐扩管规格-母管")
    # 低压给水(给水泵入口）-渐扩管规格-分管
    l_feedwater_increasing_spec_c = db.Column(db.Text(), comment=u"低压给水(给水泵入口）-渐扩管规格-分管")
    # 低压给水(给水泵入口）-渐扩管角度-母管
    l_feedwater_increasing_angle_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐扩管角度-母管")
    # 低压给水(给水泵入口）-渐扩管角度-分管
    l_feedwater_increasing_angle_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐扩管角度-分管")
    # 低压给水(给水泵入口）-渐扩管 较小直径与较大直径之比-母管
    l_feedwater_increasing_diameter_radio_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐扩管 较小直径与较大直径之比-母管")
    # 低压给水(给水泵入口）-渐扩管 较小直径与较大直径之比-分管
    l_feedwater_increasing_diameter_radio_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-渐扩管 较小直径与较大直径之比-分管")
    # 低压给水(给水泵入口）-管道入口与出口阻力系数-母管
    l_feedwater_in_out_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道入口与出口阻力系数-母管")
    # 低压给水(给水泵入口）-管道入口与出口阻力系数-分管
    l_feedwater_in_out_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-管道入口与出口阻力系数-分管")
    # 低压给水(给水泵入口）-阀门的局部阻力系数-母管
    l_feedwater_valve_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-阀门的局部阻力系数-母管")
    # 低压给水(给水泵入口）-阀门的局部阻力系数-分管
    l_feedwater_valve_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-阀门的局部阻力系数-分管")
    # 低压给水(给水泵入口）-滤网-母管
    l_feedwater_filter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-滤网-母管")
    # 低压给水(给水泵入口）-滤网-分管
    l_feedwater_filter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-滤网-分管")
    # 低压给水(给水泵入口）-闸阀阻力系数-母管
    l_feedwater_sluice_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-闸阀阻力系数-母管")
    # 低压给水(给水泵入口）-闸阀阻力系数-分管
    l_feedwater_sluice_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-闸阀阻力系数-分管")
    # 低压给水(给水泵入口）-单个闸阀阻力系数-母管
    l_feedwater_single_sluice_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单个闸阀阻力系数-母管")
    # 低压给水(给水泵入口）-单个闸阀阻力系数-分管
    l_feedwater_single_sluice_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单个闸阀阻力系数-分管")
    # 低压给水(给水泵入口）-闸阀数量-母管
    l_feedwater_sluice_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-闸阀数量-母管")
    # 低压给水(给水泵入口）-闸阀数量-分管
    l_feedwater_sluice_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-闸阀数量-分管")
    # 低压给水(给水泵入口）-止回阀阻力系数-母管
    l_feedwater_check_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-止回阀阻力系数-母管")
    # 低压给水(给水泵入口）-止回阀阻力系数-分管
    l_feedwater_check_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-止回阀阻力系数-分管")
    # 低压给水(给水泵入口）-单个止回阀阻力系数-母管
    l_feedwater_single_check_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单个止回阀阻力系数-母管")
    # 低压给水(给水泵入口）-单个止回阀阻力系数-分管
    l_feedwater_single_check_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-单个止回阀阻力系数-分管")
    # 低压给水(给水泵入口）-止回阀数量-母管
    l_feedwater_check_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-止回阀数量-母管")
    # 低压给水(给水泵入口）-止回阀数量-分管
    l_feedwater_check_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-止回阀数量-分管")
    # 低压给水(给水泵入口）-调节阀阻力系数-母管
    l_feedwater_regulating_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-调节阀阻力系数-母管")
    # 低压给水(给水泵入口）-调节阀阻力系数-分管
    l_feedwater_regulating_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-调节阀阻力系数-分管")
    # 低压给水(给水泵入口）-流量测量孔板阻力系数-母管
    l_feedwater_plate_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-流量测量孔板阻力系数-母管")
    # 低压给水(给水泵入口）-流量测量孔板阻力系数-分管
    l_feedwater_plate_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-流量测量孔板阻力系数-分管")
    # 低压给水(给水泵入口）-测量装置压损-母管
    l_feedwater_measuring_pressure_loss_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-测量装置压损-母管")
    # 低压给水(给水泵入口）-测量装置压损-分管
    l_feedwater_measuring_pressure_loss_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低压给水(给水泵入口）-测量装置压损-分管")

    '''高压给水(给水泵出口）'''
    # 高压给水(给水泵出口）-运行压力-母管
    h_feedwater_work_press_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-运行压力-母管")
    # 高压给水(给水泵出口）-运行压力-分管
    h_feedwater_work_press_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-运行压力-分管")
    # 高压给水(给水泵出口）-运行温度-母管
    h_feedwater_work_temperature_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-运行温度-母管")
    # 高压给水(给水泵出口）-运行温度-分管
    h_feedwater_work_temperature_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-运行温度-分管")
    # 高压给水(给水泵出口）-额定流量-母管
    h_feedwater_rated_flow_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-额定流量-母管")
    # 高压给水(给水泵出口）-额定流量-分管
    h_feedwater_rated_flow_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-额定流量-分管")
    # 高压给水(给水泵出口）-介质比容-母管
    h_feedwater_msv_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-介质比容-母管")
    # 高压给水(给水泵出口）-介质比容-分管
    h_feedwater_msv_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-介质比容-分管")
    # 高压给水(给水泵出口）-介质运动粘度-母管
    h_feedwater_media_viscosity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-介质运动粘度-母管")
    # 高压给水(给水泵出口）-介质运动粘度-分管
    h_feedwater_media_viscosity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-介质运动粘度-分管")
    # 高压给水(给水泵出口）-流速-母管
    h_feedwater_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-流速-母管")
    # 高压给水(给水泵出口）-流速-分管
    h_feedwater_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-流速-分管")
    # 高压给水(给水泵出口）-计算流速-母管
    h_feedwater_calculate_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-计算流速-母管")
    # 高压给水(给水泵出口）-计算流速-分管
    h_feedwater_calculate_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-计算流速-分管")
    # 高压给水(给水泵出口）-动压头-母管
    h_feedwater_dynamic_head_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-动压头-母管")
    # 高压给水(给水泵出口）-动压头-分管
    h_feedwater_dynamic_head_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-动压头-分管")
    # 高压给水(给水泵出口）-管道外径-母管
    h_feedwater_pipe_outer_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道外径-母管")
    # 高压给水(给水泵出口）-管道外径-分管
    h_feedwater_pipe_outer_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道外径-分管")
    # 高压给水(给水泵出口）-管道壁厚-母管
    h_feedwater_pipe_thickness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道壁厚-母管")
    # 高压给水(给水泵出口）-管道壁厚-分管
    h_feedwater_pipe_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道壁厚-分管")
    # 高压给水(给水泵出口）-管道内径-母管
    h_feedwater_pipe_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道内径-母管")
    # 高压给水(给水泵出口）-管道内径-分管
    h_feedwater_pipe_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道内径-分管")
    # 高压给水(给水泵出口）-摩擦阻力-母管
    h_feedwater_friction_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-摩擦阻力-母管")
    # 高压给水(给水泵出口）-摩擦阻力-分管
    h_feedwater_friction_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-摩擦阻力-分管")
    # 高压给水(给水泵出口）-雷诺数-母管
    h_feedwater_reynolds_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-雷诺数-母管")
    # 高压给水(给水泵出口）-雷诺数-分管
    h_feedwater_reynolds_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-雷诺数-分管")
    # 高压给水(给水泵出口）-等值粗糙度-母管
    h_feedwater_equivalent_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-等值粗糙度-母管")
    # 高压给水(给水泵出口）-等值粗糙度-分管
    h_feedwater_equivalent_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-等值粗糙度-分管")
    # 高压给水(给水泵出口）-相对粗糙度-母管
    h_feedwater_relative_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-相对粗糙度-母管")
    # 高压给水(给水泵出口）-相对粗糙度-分管
    h_feedwater_relative_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-相对粗糙度-分管")
    # 高压给水(给水泵出口）-摩擦阻力系数-母管
    h_feedwater_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-摩擦阻力系数-母管")
    # 高压给水(给水泵出口）-摩擦阻力系数-分管
    h_feedwater_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-摩擦阻力系数-分管")
    # 高压给水(给水泵出口）-单位长度摩擦阻力-母管
    h_feedwater_unit_length_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单位长度摩擦阻力-母管")
    # 高压给水(给水泵出口）-单位长度摩擦阻力-分管
    h_feedwater_unit_length_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单位长度摩擦阻力-分管")
    # 高压给水(给水泵出口）-管道长度-母管
    h_feedwater_pipe_length_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道长度-母管")
    # 高压给水(给水泵出口）-管道长度-分管
    h_feedwater_pipe_length_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道长度-分管")
    # 高压给水(给水泵出口）-局部阻力-母管
    h_feedwater_local_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-局部阻力-母管")
    # 高压给水(给水泵出口）-局部阻力-分管
    h_feedwater_local_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-局部阻力-分管")
    # 高压给水(给水泵出口）-局部阻力系数合计-母管
    h_feedwater_total_local_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-局部阻力系数合计-母管")
    # 高压给水(给水泵出口）-局部阻力系数合计-分管
    h_feedwater_total_local_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-局部阻力系数合计-分管")
    # 高压给水(给水泵出口）-弯头阻力系数-母管
    h_feedwater_elbow_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-弯头阻力系数-母管")
    # 高压给水(给水泵出口）-弯头阻力系数-分管
    h_feedwater_elbow_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-弯头阻力系数-分管")
    # 高压给水(给水泵出口）-弯头规格-母管
    h_feedwater_elbow_spec_m = db.Column(db.Text(), comment=u"高压给水(给水泵出口）-弯头规格-母管")
    # 高压给水(给水泵出口）-弯头规格-分管
    h_feedwater_elbow_spec_c = db.Column(db.Text(), comment=u"高压给水(给水泵出口）-弯头规格-分管")
    # 高压给水(给水泵出口）-弯头半径-母管
    h_feedwater_elbow_radius_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-弯头半径-母管")
    # 高压给水(给水泵出口）-弯头半径-分管
    h_feedwater_elbow_radius_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-弯头半径-分管")
    # 高压给水(给水泵出口）-弯头半径 / 管道内径-母管
    h_feedwater_elbow_radius_to_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-弯头半径 / 管道内径-母管")
    # 高压给水(给水泵出口）-弯头半径 / 管道内径-分管
    h_feedwater_elbow_radius_to_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-弯头半径 / 管道内径-分管")
    # 高压给水(给水泵出口）-单个90º弯头阻力系数-母管
    h_feedwater_90elbow_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单个90º弯头阻力系数-母管")
    # 高压给水(给水泵出口）-单个90º弯头阻力系数-分管
    h_feedwater_90elbow_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单个90º弯头阻力系数-分管")
    # 高压给水(给水泵出口）-90º弯头数量-母管
    h_feedwater_90elbow_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-90º弯头数量-母管")
    # 高压给水(给水泵出口）-90º弯头数量-分管
    h_feedwater_90elbow_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-90º弯头数量-分管")
    # 高压给水(给水泵出口）-三通阻力系数-母管
    h_feedwater_triplet_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-三通阻力系数-母管")
    # 高压给水(给水泵出口）-三通阻力系数-分管
    h_feedwater_triplet_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-三通阻力系数-分管")
    # 高压给水(给水泵出口）-单个三通阻力系数-母管
    h_feedwater_single_triplet_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单个三通阻力系数-母管")
    # 高压给水(给水泵出口）-单个三通阻力系数-分管
    h_feedwater_single_triplet_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单个三通阻力系数-分管")
    # 高压给水(给水泵出口）-三通数量-母管
    h_feedwater_triplet_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-三通数量-母管")
    # 高压给水(给水泵出口）-三通数量-分管
    h_feedwater_triplet_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-三通数量-分管")
    # 高压给水(给水泵出口）-异径管的阻力系数-母管
    h_feedwater_reducer_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-异径管的阻力系数-母管")
    # 高压给水(给水泵出口）-异径管的阻力系数-分管
    h_feedwater_reducer_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-异径管的阻力系数-分管")
    # 高压给水(给水泵出口）-渐缩管的阻力系数-母管
    h_feedwater_converging_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐缩管的阻力系数-母管")
    # 高压给水(给水泵出口）-渐缩管的阻力系数-分管
    h_feedwater_converging_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐缩管的阻力系数-分管")
    # 高压给水(给水泵出口）-渐缩管规格-母管
    h_feedwater_converging_spec_m = db.Column(db.Text(), comment=u"高压给水(给水泵出口）-渐缩管规格-母管")
    # 高压给水(给水泵出口）-渐缩管规格-分管
    h_feedwater_converging_spec_c = db.Column(db.Text(), comment=u"高压给水(给水泵出口）-渐缩管规格-分管")
    # 高压给水(给水泵出口）-渐缩管角度-母管
    h_feedwater_converging_angle_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐缩管角度-母管")
    # 高压给水(给水泵出口）-渐缩管角度-分管
    h_feedwater_converging_angle_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐缩管角度-分管")
    # 高压给水(给水泵出口）-渐缩管 较小直径与较大直径之比-母管
    h_feedwater_converging_diameter_radio_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐缩管 较小直径与较大直径之比-母管")
    # 高压给水(给水泵出口）-渐缩管 较小直径与较大直径之比-分管
    h_feedwater_converging_diameter_radio_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐缩管 较小直径与较大直径之比-分管")
    # 高压给水(给水泵出口）-渐扩管的阻力系数-母管
    h_feedwater_increasing_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐扩管的阻力系数-母管")
    # 高压给水(给水泵出口）-渐扩管的阻力系数-分管
    h_feedwater_increasing_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐扩管的阻力系数-分管")
    # 高压给水(给水泵出口）-渐扩管规格-母管
    h_feedwater_increasing_spec_m = db.Column(db.Text(), comment=u"高压给水(给水泵出口）-渐扩管规格-母管")
    # 高压给水(给水泵出口）-渐扩管规格-分管
    h_feedwater_increasing_spec_c = db.Column(db.Text(), comment=u"高压给水(给水泵出口）-渐扩管规格-分管")
    # 高压给水(给水泵出口）-渐扩管角度-母管
    h_feedwater_increasing_angle_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐扩管角度-母管")
    # 高压给水(给水泵出口）-渐扩管角度-分管
    h_feedwater_increasing_angle_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐扩管角度-分管")
    # 高压给水(给水泵出口）-渐扩管 较小直径与较大直径之比-母管
    h_feedwater_increasing_diameter_radio_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐扩管 较小直径与较大直径之比-母管")
    # 高压给水(给水泵出口）-渐扩管 较小直径与较大直径之比-分管
    h_feedwater_increasing_diameter_radio_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-渐扩管 较小直径与较大直径之比-分管")
    # 高压给水(给水泵出口）-管道入口与出口阻力系数-母管
    h_feedwater_in_out_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道入口与出口阻力系数-母管")
    # 高压给水(给水泵出口）-管道入口与出口阻力系数-分管
    h_feedwater_in_out_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-管道入口与出口阻力系数-分管")
    # 高压给水(给水泵出口）-阀门的局部阻力系数-母管
    h_feedwater_valve_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-阀门的局部阻力系数-母管")
    # 高压给水(给水泵出口）-阀门的局部阻力系数-分管
    h_feedwater_valve_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-阀门的局部阻力系数-分管")
    # 高压给水(给水泵出口）-滤网-母管
    h_feedwater_filter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-滤网-母管")
    # 高压给水(给水泵出口）-滤网-分管
    h_feedwater_filter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-滤网-分管")
    # 高压给水(给水泵出口）-闸阀阻力系数-母管
    h_feedwater_sluice_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-闸阀阻力系数-母管")
    # 高压给水(给水泵出口）-闸阀阻力系数-分管
    h_feedwater_sluice_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-闸阀阻力系数-分管")
    # 高压给水(给水泵出口）-单个闸阀阻力系数-母管
    h_feedwater_single_sluice_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单个闸阀阻力系数-母管")
    # 高压给水(给水泵出口）-单个闸阀阻力系数-分管
    h_feedwater_single_sluice_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单个闸阀阻力系数-分管")
    # 高压给水(给水泵出口）-闸阀数量-母管
    h_feedwater_sluice_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-闸阀数量-母管")
    # 高压给水(给水泵出口）-闸阀数量-分管
    h_feedwater_sluice_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-闸阀数量-分管")
    # 高压给水(给水泵出口）-止回阀阻力系数-母管
    h_feedwater_check_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-止回阀阻力系数-母管")
    # 高压给水(给水泵出口）-止回阀阻力系数-分管
    h_feedwater_check_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-止回阀阻力系数-分管")
    # 高压给水(给水泵出口）-单个止回阀阻力系数-母管
    h_feedwater_single_check_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单个止回阀阻力系数-母管")
    # 高压给水(给水泵出口）-单个止回阀阻力系数-分管
    h_feedwater_single_check_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-单个止回阀阻力系数-分管")
    # 高压给水(给水泵出口）-止回阀数量-母管
    h_feedwater_check_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-止回阀数量-母管")
    # 高压给水(给水泵出口）-止回阀数量-分管
    h_feedwater_check_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-止回阀数量-分管")
    # 高压给水(给水泵出口）-调节阀阻力系数-母管
    h_feedwater_regulating_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-调节阀阻力系数-母管")
    # 高压给水(给水泵出口）-调节阀阻力系数-分管
    h_feedwater_regulating_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-调节阀阻力系数-分管")
    # 高压给水(给水泵出口）-流量测量孔板阻力系数-母管
    h_feedwater_plate_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-流量测量孔板阻力系数-母管")
    # 高压给水(给水泵出口）-流量测量孔板阻力系数-分管
    h_feedwater_plate_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-流量测量孔板阻力系数-分管")
    # 高压给水(给水泵出口）-测量装置压损-母管
    h_feedwater_measuring_pressure_loss_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-测量装置压损-母管")
    # 高压给水(给水泵出口）-测量装置压损-分管
    h_feedwater_measuring_pressure_loss_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高压给水(给水泵出口）-测量装置压损-分管")

    '''凝泵入口'''
    # 凝泵入口-运行压力-母管
    pump_in_work_press_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-运行压力-母管")
    # 凝泵入口-运行压力-分管
    pump_in_work_press_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-运行压力-分管")
    # 凝泵入口-运行温度-母管
    pump_in_work_temperature_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-运行温度-母管")
    # 凝泵入口-运行温度-分管
    pump_in_work_temperature_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-运行温度-分管")
    # 凝泵入口-额定流量-母管
    pump_in_rated_flow_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-额定流量-母管")
    # 凝泵入口-额定流量-分管
    pump_in_rated_flow_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-额定流量-分管")
    # 凝泵入口-介质比容-母管
    pump_in_msv_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-介质比容-母管")
    # 凝泵入口-介质比容-分管
    pump_in_msv_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-介质比容-分管")
    # 凝泵入口-介质运动粘度-母管
    pump_in_media_viscosity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-介质运动粘度-母管")
    # 凝泵入口-介质运动粘度-分管
    pump_in_media_viscosity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-介质运动粘度-分管")
    # 凝泵入口-流速-母管
    pump_in_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-流速-母管")
    # 凝泵入口-流速-分管
    pump_in_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-流速-分管")
    # 凝泵入口-计算流速-母管
    pump_in_calculate_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-计算流速-母管")
    # 凝泵入口-计算流速-分管
    pump_in_calculate_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-计算流速-分管")
    # 凝泵入口-动压头-母管
    pump_in_dynamic_head_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-动压头-母管")
    # 凝泵入口-动压头-分管
    pump_in_dynamic_head_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-动压头-分管")
    # 凝泵入口-管道外径-母管
    pump_in_pipe_outer_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道外径-母管")
    # 凝泵入口-管道外径-分管
    pump_in_pipe_outer_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道外径-分管")
    # 凝泵入口-管道壁厚-母管
    pump_in_pipe_thickness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道壁厚-母管")
    # 凝泵入口-管道壁厚-分管
    pump_in_pipe_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道壁厚-分管")
    # 凝泵入口-管道内径-母管
    pump_in_pipe_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道内径-母管")
    # 凝泵入口-管道内径-分管
    pump_in_pipe_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道内径-分管")
    # 凝泵入口-摩擦阻力-母管
    pump_in_friction_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-摩擦阻力-母管")
    # 凝泵入口-摩擦阻力-分管
    pump_in_friction_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-摩擦阻力-分管")
    # 凝泵入口-雷诺数-母管
    pump_in_reynolds_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-雷诺数-母管")
    # 凝泵入口-雷诺数-分管
    pump_in_reynolds_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-雷诺数-分管")
    # 凝泵入口-等值粗糙度-母管
    pump_in_equivalent_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-等值粗糙度-母管")
    # 凝泵入口-等值粗糙度-分管
    pump_in_equivalent_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-等值粗糙度-分管")
    # 凝泵入口-相对粗糙度-母管
    pump_in_relative_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-相对粗糙度-母管")
    # 凝泵入口-相对粗糙度-分管
    pump_in_relative_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-相对粗糙度-分管")
    # 凝泵入口-摩擦阻力系数-母管
    pump_in_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-摩擦阻力系数-母管")
    # 凝泵入口-摩擦阻力系数-分管
    pump_in_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-摩擦阻力系数-分管")
    # 凝泵入口-单位长度摩擦阻力-母管
    pump_in_unit_length_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单位长度摩擦阻力-母管")
    # 凝泵入口-单位长度摩擦阻力-分管
    pump_in_unit_length_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单位长度摩擦阻力-分管")
    # 凝泵入口-管道长度-母管
    pump_in_pipe_length_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道长度-母管")
    # 凝泵入口-管道长度-分管
    pump_in_pipe_length_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道长度-分管")
    # 凝泵入口-局部阻力-母管
    pump_in_local_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-局部阻力-母管")
    # 凝泵入口-局部阻力-分管
    pump_in_local_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-局部阻力-分管")
    # 凝泵入口-局部阻力系数合计-母管
    pump_in_total_local_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-局部阻力系数合计-母管")
    # 凝泵入口-局部阻力系数合计-分管
    pump_in_total_local_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-局部阻力系数合计-分管")
    # 凝泵入口-弯头阻力系数-母管
    pump_in_elbow_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-弯头阻力系数-母管")
    # 凝泵入口-弯头阻力系数-分管
    pump_in_elbow_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-弯头阻力系数-分管")
    # 凝泵入口-弯头规格-母管
    pump_in_elbow_spec_m = db.Column(db.Text(), comment=u"凝泵入口-弯头规格-母管")
    # 凝泵入口-弯头规格-分管
    pump_in_elbow_spec_c = db.Column(db.Text(), comment=u"凝泵入口-弯头规格-分管")
    # 凝泵入口-弯头半径-母管
    pump_in_elbow_radius_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-弯头半径-母管")
    # 凝泵入口-弯头半径-分管
    pump_in_elbow_radius_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-弯头半径-分管")
    # 凝泵入口-弯头半径 / 管道内径-母管
    pump_in_elbow_radius_to_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-弯头半径 / 管道内径-母管")
    # 凝泵入口-弯头半径 / 管道内径-分管
    pump_in_elbow_radius_to_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-弯头半径 / 管道内径-分管")
    # 凝泵入口-单个90º弯头阻力系数-母管
    pump_in_90elbow_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单个90º弯头阻力系数-母管")
    # 凝泵入口-单个90º弯头阻力系数-分管
    pump_in_90elbow_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单个90º弯头阻力系数-分管")
    # 凝泵入口-90º弯头数量-母管
    pump_in_90elbow_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-90º弯头数量-母管")
    # 凝泵入口-90º弯头数量-分管
    pump_in_90elbow_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-90º弯头数量-分管")
    # 凝泵入口-三通阻力系数-母管
    pump_in_triplet_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-三通阻力系数-母管")
    # 凝泵入口-三通阻力系数-分管
    pump_in_triplet_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-三通阻力系数-分管")
    # 凝泵入口-单个三通阻力系数-母管
    pump_in_single_triplet_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单个三通阻力系数-母管")
    # 凝泵入口-单个三通阻力系数-分管
    pump_in_single_triplet_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单个三通阻力系数-分管")
    # 凝泵入口-三通数量-母管
    pump_in_triplet_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-三通数量-母管")
    # 凝泵入口-三通数量-分管
    pump_in_triplet_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-三通数量-分管")
    # 凝泵入口-异径管的阻力系数-母管
    pump_in_reducer_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-异径管的阻力系数-母管")
    # 凝泵入口-异径管的阻力系数-分管
    pump_in_reducer_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-异径管的阻力系数-分管")
    # 凝泵入口-渐缩管的阻力系数-母管
    pump_in_converging_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐缩管的阻力系数-母管")
    # 凝泵入口-渐缩管的阻力系数-分管
    pump_in_converging_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐缩管的阻力系数-分管")
    # 凝泵入口-渐缩管规格-母管
    pump_in_converging_spec_m = db.Column(db.Text(), comment=u"凝泵入口-渐缩管规格-母管")
    # 凝泵入口-渐缩管规格-分管
    pump_in_converging_spec_c = db.Column(db.Text(), comment=u"凝泵入口-渐缩管规格-分管")
    # 凝泵入口-渐缩管角度-母管
    pump_in_converging_angle_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐缩管角度-母管")
    # 凝泵入口-渐缩管角度-分管
    pump_in_converging_angle_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐缩管角度-分管")
    # 凝泵入口-渐缩管 较小直径与较大直径之比-母管
    pump_in_converging_diameter_radio_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐缩管 较小直径与较大直径之比-母管")
    # 凝泵入口-渐缩管 较小直径与较大直径之比-分管
    pump_in_converging_diameter_radio_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐缩管 较小直径与较大直径之比-分管")
    # 凝泵入口-渐扩管的阻力系数-母管
    pump_in_increasing_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐扩管的阻力系数-母管")
    # 凝泵入口-渐扩管的阻力系数-分管
    pump_in_increasing_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐扩管的阻力系数-分管")
    # 凝泵入口-渐扩管规格-母管
    pump_in_increasing_spec_m = db.Column(db.Text(), comment=u"凝泵入口-渐扩管规格-母管")
    # 凝泵入口-渐扩管规格-分管
    pump_in_increasing_spec_c = db.Column(db.Text(), comment=u"凝泵入口-渐扩管规格-分管")
    # 凝泵入口-渐扩管角度-母管
    pump_in_increasing_angle_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐扩管角度-母管")
    # 凝泵入口-渐扩管角度-分管
    pump_in_increasing_angle_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐扩管角度-分管")
    # 凝泵入口-渐扩管 较小直径与较大直径之比-母管
    pump_in_increasing_diameter_radio_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐扩管 较小直径与较大直径之比-母管")
    # 凝泵入口-渐扩管 较小直径与较大直径之比-分管
    pump_in_increasing_diameter_radio_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-渐扩管 较小直径与较大直径之比-分管")
    # 凝泵入口-管道入口与出口阻力系数-母管
    pump_in_in_out_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道入口与出口阻力系数-母管")
    # 凝泵入口-管道入口与出口阻力系数-分管
    pump_in_in_out_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-管道入口与出口阻力系数-分管")
    # 凝泵入口-阀门的局部阻力系数-母管
    pump_in_valve_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-阀门的局部阻力系数-母管")
    # 凝泵入口-阀门的局部阻力系数-分管
    pump_in_valve_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-阀门的局部阻力系数-分管")
    # 凝泵入口-滤网-母管
    pump_in_filter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-滤网-母管")
    # 凝泵入口-滤网-分管
    pump_in_filter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-滤网-分管")
    # 凝泵入口-闸阀阻力系数-母管
    pump_in_sluice_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-闸阀阻力系数-母管")
    # 凝泵入口-闸阀阻力系数-分管
    pump_in_sluice_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-闸阀阻力系数-分管")
    # 凝泵入口-单个闸阀阻力系数-母管
    pump_in_single_sluice_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单个闸阀阻力系数-母管")
    # 凝泵入口-单个闸阀阻力系数-分管
    pump_in_single_sluice_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单个闸阀阻力系数-分管")
    # 凝泵入口-闸阀数量-母管
    pump_in_sluice_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-闸阀数量-母管")
    # 凝泵入口-闸阀数量-分管
    pump_in_sluice_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-闸阀数量-分管")
    # 凝泵入口-止回阀阻力系数-母管
    pump_in_check_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-止回阀阻力系数-母管")
    # 凝泵入口-止回阀阻力系数-分管
    pump_in_check_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-止回阀阻力系数-分管")
    # 凝泵入口-单个止回阀阻力系数-母管
    pump_in_single_check_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单个止回阀阻力系数-母管")
    # 凝泵入口-单个止回阀阻力系数-分管
    pump_in_single_check_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-单个止回阀阻力系数-分管")
    # 凝泵入口-止回阀数量-母管
    pump_in_check_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-止回阀数量-母管")
    # 凝泵入口-止回阀数量-分管
    pump_in_check_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-止回阀数量-分管")
    # 凝泵入口-调节阀阻力系数-母管
    pump_in_regulating_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-调节阀阻力系数-母管")
    # 凝泵入口-调节阀阻力系数-分管
    pump_in_regulating_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-调节阀阻力系数-分管")
    # 凝泵入口-流量测量孔板阻力系数-母管
    pump_in_plate_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-流量测量孔板阻力系数-母管")
    # 凝泵入口-流量测量孔板阻力系数-分管
    pump_in_plate_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-流量测量孔板阻力系数-分管")
    # 凝泵入口-测量装置压损-母管
    pump_in_measuring_pressure_loss_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵入口-测量装置压损-母管")
    # 凝泵入口-测量装置压损-分管
    pump_in_measuring_pressure_loss_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"泵入口-测量装置压损-分管")

    '''凝泵出口'''
    # 凝泵出口-运行压力-母管
    pump_out_work_press_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-运行压力-母管")
    # 凝泵出口-运行压力-分管
    pump_out_work_press_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-运行压力-分管")
    # 凝泵出口-运行温度-母管
    pump_out_work_temperature_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-运行温度-母管")
    # 凝泵出口-运行温度-分管
    pump_out_work_temperature_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-运行温度-分管")
    # 凝泵出口-额定流量-母管
    pump_out_rated_flow_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-额定流量-母管")
    # 凝泵出口-额定流量-分管
    pump_out_rated_flow_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-额定流量-分管")
    # 凝泵出口-介质比容-母管
    pump_out_msv_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-介质比容-母管")
    # 凝泵出口-介质比容-分管
    pump_out_msv_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-介质比容-分管")
    # 凝泵出口-介质运动粘度-母管
    pump_out_media_viscosity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-介质运动粘度-母管")
    # 凝泵出口-介质运动粘度-分管
    pump_out_media_viscosity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-介质运动粘度-分管")
    # 凝泵出口-流速-母管
    pump_out_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-流速-母管")
    # 凝泵出口-流速-分管
    pump_out_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-流速-分管")
    # 凝泵出口-计算流速-母管
    pump_out_calculate_velocity_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-计算流速-母管")
    # 凝泵出口-计算流速-分管
    pump_out_calculate_velocity_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-计算流速-分管")
    # 凝泵出口-动压头-母管
    pump_out_dynamic_head_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-动压头-母管")
    # 凝泵出口-动压头-分管
    pump_out_dynamic_head_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-动压头-分管")
    # 凝泵出口-管道外径-母管
    pump_out_pipe_outer_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道外径-母管")
    # 凝泵出口-管道外径-分管
    pump_out_pipe_outer_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道外径-分管")
    # 凝泵出口-管道壁厚-母管
    pump_out_pipe_thickness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道壁厚-母管")
    # 凝泵出口-管道壁厚-分管
    pump_out_pipe_thickness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道壁厚-分管")
    # 凝泵出口-管道内径-母管
    pump_out_pipe_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道内径-母管")
    # 凝泵出口-管道内径-分管
    pump_out_pipe_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道内径-分管")
    # 凝泵出口-摩擦阻力-母管
    pump_out_friction_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-摩擦阻力-母管")
    # 凝泵出口-摩擦阻力-分管
    pump_out_friction_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-摩擦阻力-分管")
    # 凝泵出口-雷诺数-母管
    pump_out_reynolds_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-雷诺数-母管")
    # 凝泵出口-雷诺数-分管
    pump_out_reynolds_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-雷诺数-分管")
    # 凝泵出口-等值粗糙度-母管
    pump_out_equivalent_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-等值粗糙度-母管")
    # 凝泵出口-等值粗糙度-分管
    pump_out_equivalent_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-等值粗糙度-分管")
    # 凝泵出口-相对粗糙度-母管
    pump_out_relative_roughness_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-相对粗糙度-母管")
    # 凝泵出口-相对粗糙度-分管
    pump_out_relative_roughness_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-相对粗糙度-分管")
    # 凝泵出口-摩擦阻力系数-母管
    pump_out_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-摩擦阻力系数-母管")
    # 凝泵出口-摩擦阻力系数-分管
    pump_out_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-摩擦阻力系数-分管")
    # 凝泵出口-单位长度摩擦阻力-母管
    pump_out_unit_length_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单位长度摩擦阻力-母管")
    # 凝泵出口-单位长度摩擦阻力-分管
    pump_out_unit_length_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单位长度摩擦阻力-分管")
    # 凝泵出口-管道长度-母管
    pump_out_pipe_length_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道长度-母管")
    # 凝泵出口-管道长度-分管
    pump_out_pipe_length_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道长度-分管")
    # 凝泵出口-局部阻力-母管
    pump_out_local_resistance_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-局部阻力-母管")
    # 凝泵出口-局部阻力-分管
    pump_out_local_resistance_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-局部阻力-分管")
    # 凝泵出口-局部阻力系数合计-母管
    pump_out_total_local_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-局部阻力系数合计-母管")
    # 凝泵出口-局部阻力系数合计-分管
    pump_out_total_local_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-局部阻力系数合计-分管")
    # 凝泵出口-弯头阻力系数-母管
    pump_out_elbow_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-弯头阻力系数-母管")
    # 凝泵出口-弯头阻力系数-分管
    pump_out_elbow_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-弯头阻力系数-分管")
    # 凝泵出口-弯头规格-母管
    pump_out_elbow_spec_m = db.Column(db.Text(), comment=u"凝泵出口-弯头规格-母管")
    # 凝泵出口-弯头规格-分管
    pump_out_elbow_spec_c = db.Column(db.Text(), comment=u"凝泵出口-弯头规格-分管")
    # 凝泵出口-弯头半径-母管
    pump_out_elbow_radius_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-弯头半径-母管")
    # 凝泵出口-弯头半径-分管
    pump_out_elbow_radius_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-弯头半径-分管")
    # 凝泵出口-弯头半径 / 管道内径-母管
    pump_out_elbow_radius_to_inner_diameter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-弯头半径 / 管道内径-母管")
    # 凝泵出口-弯头半径 / 管道内径-分管
    pump_out_elbow_radius_to_inner_diameter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-弯头半径 / 管道内径-分管")
    # 凝泵出口-单个90º弯头阻力系数-母管
    pump_out_90elbow_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单个90º弯头阻力系数-母管")
    # 凝泵出口-单个90º弯头阻力系数-分管
    pump_out_90elbow_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单个90º弯头阻力系数-分管")
    # 凝泵出口-90º弯头数量-母管
    pump_out_90elbow_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-90º弯头数量-母管")
    # 凝泵出口-90º弯头数量-分管
    pump_out_90elbow_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-90º弯头数量-分管")
    # 凝泵出口-三通阻力系数-母管
    pump_out_triplet_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-三通阻力系数-母管")
    # 凝泵出口-三通阻力系数-分管
    pump_out_triplet_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-三通阻力系数-分管")
    # 凝泵出口-单个三通阻力系数-母管
    pump_out_single_triplet_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单个三通阻力系数-母管")
    # 凝泵出口-单个三通阻力系数-分管
    pump_out_single_triplet_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单个三通阻力系数-分管")
    # 凝泵出口-三通数量-母管
    pump_out_triplet_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-三通数量-母管")
    # 凝泵出口-三通数量-分管
    pump_out_triplet_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-三通数量-分管")
    # 凝泵出口-异径管的阻力系数-母管
    pump_out_reducer_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-异径管的阻力系数-母管")
    # 凝泵出口-异径管的阻力系数-分管
    pump_out_reducer_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-异径管的阻力系数-分管")
    # 凝泵出口-渐缩管的阻力系数-母管
    pump_out_converging_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐缩管的阻力系数-母管")
    # 凝泵出口-渐缩管的阻力系数-分管
    pump_out_converging_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐缩管的阻力系数-分管")
    # 凝泵出口-渐缩管规格-母管
    pump_out_converging_spec_m = db.Column(db.Text(), comment=u"凝泵出口-渐缩管规格-母管")
    # 凝泵出口-渐缩管规格-分管
    pump_out_converging_spec_c = db.Column(db.Text(), comment=u"凝泵出口-渐缩管规格-分管")
    # 凝泵出口-渐缩管角度-母管
    pump_out_converging_angle_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐缩管角度-母管")
    # 凝泵出口-渐缩管角度-分管
    pump_out_converging_angle_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐缩管角度-分管")
    # 凝泵出口-渐缩管 较小直径与较大直径之比-母管
    pump_out_converging_diameter_radio_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐缩管 较小直径与较大直径之比-母管")
    # 凝泵出口-渐缩管 较小直径与较大直径之比-分管
    pump_out_converging_diameter_radio_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐缩管 较小直径与较大直径之比-分管")
    # 凝泵出口-渐扩管的阻力系数-母管
    pump_out_increasing_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐扩管的阻力系数-母管")
    # 凝泵出口-渐扩管的阻力系数-分管
    pump_out_increasing_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐扩管的阻力系数-分管")
    # 凝泵出口-渐扩管规格-母管
    pump_out_increasing_spec_m = db.Column(db.Text(), comment=u"凝泵出口-渐扩管规格-母管")
    # 凝泵出口-渐扩管规格-分管
    pump_out_increasing_spec_c = db.Column(db.Text(), comment=u"凝泵出口-渐扩管规格-分管")
    # 凝泵出口-渐扩管角度-母管
    pump_out_increasing_angle_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐扩管角度-母管")
    # 凝泵出口-渐扩管角度-分管
    pump_out_increasing_angle_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐扩管角度-分管")
    # 凝泵出口-渐扩管 较小直径与较大直径之比-母管
    pump_out_increasing_diameter_radio_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐扩管 较小直径与较大直径之比-母管")
    # 凝泵出口-渐扩管 较小直径与较大直径之比-分管
    pump_out_increasing_diameter_radio_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-渐扩管 较小直径与较大直径之比-分管")
    # 凝泵出口-管道入口与出口阻力系数-母管
    pump_out_in_out_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道入口与出口阻力系数-母管")
    # 凝泵出口-管道入口与出口阻力系数-分管
    pump_out_in_out_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-管道入口与出口阻力系数-分管")
    # 凝泵出口-阀门的局部阻力系数-母管
    pump_out_valve_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-阀门的局部阻力系数-母管")
    # 凝泵出口-阀门的局部阻力系数-分管
    pump_out_valve_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-阀门的局部阻力系数-分管")
    # 凝泵出口-滤网-母管
    pump_out_filter_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-滤网-母管")
    # 凝泵出口-滤网-分管
    pump_out_filter_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-滤网-分管")
    # 凝泵出口-闸阀阻力系数-母管
    pump_out_sluice_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-闸阀阻力系数-母管")
    # 凝泵出口-闸阀阻力系数-分管
    pump_out_sluice_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-闸阀阻力系数-分管")
    # 凝泵出口-单个闸阀阻力系数-母管
    pump_out_single_sluice_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单个闸阀阻力系数-母管")
    # 凝泵出口-单个闸阀阻力系数-分管
    pump_out_single_sluice_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单个闸阀阻力系数-分管")
    # 凝泵出口-闸阀数量-母管
    pump_out_sluice_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-闸阀数量-母管")
    # 凝泵出口-闸阀数量-分管
    pump_out_sluice_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-闸阀数量-分管")
    # 凝泵出口-止回阀阻力系数-母管
    pump_out_check_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-止回阀阻力系数-母管")
    # 凝泵出口-止回阀阻力系数-分管
    pump_out_check_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-止回阀阻力系数-分管")
    # 凝泵出口-单个止回阀阻力系数-母管
    pump_out_single_check_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单个止回阀阻力系数-母管")
    # 凝泵出口-单个止回阀阻力系数-分管
    pump_out_single_check_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-单个止回阀阻力系数-分管")
    # 凝泵出口-止回阀数量-母管
    pump_out_check_count_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-止回阀数量-母管")
    # 凝泵出口-止回阀数量-分管
    pump_out_check_count_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-止回阀数量-分管")
    # 凝泵出口-调节阀阻力系数-母管
    pump_out_regulating_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-调节阀阻力系数-母管")
    # 凝泵出口-调节阀阻力系数-分管
    pump_out_regulating_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-调节阀阻力系数-分管")
    # 凝泵出口-流量测量孔板阻力系数-母管
    pump_out_plate_resistance_coefficient_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-流量测量孔板阻力系数-母管")
    # 凝泵出口-流量测量孔板阻力系数-分管
    pump_out_plate_resistance_coefficient_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-流量测量孔板阻力系数-分管")
    # 凝泵出口-测量装置压损-母管
    pump_out_measuring_pressure_loss_m = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝泵出口-测量装置压损-母管")
    # 凝泵出口-测量装置压损-分管
    pump_out_measuring_pressure_loss_c = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"泵入口-测量装置压损-分管")

    def __init__(self, **kwargs):
        super(GPGSteamWaterPipe, self).__init__(**kwargs)

    @staticmethod
    def insert_SteamWaterPipe(gaspowergeneration_steam_water_pipe):
        try:
            db.session.add(gaspowergeneration_steam_water_pipe)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_steam_water_pipe"
                  "<id=%s> in database" % (gaspowergeneration_steam_water_pipe.id))

    # 根据plan id查找实体
    @staticmethod
    def search_SteamWaterPipe(planId):
        result = GPGSteamWaterPipe.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_SteamWaterPipe(plan_id):
        SteamWaterPipe = GPGSteamWaterPipe.search_SteamWaterPipe(plan_id)
        try:
            db.session.delete(SteamWaterPipe)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete SteamWaterPipe<id=%s, plan_id=%s> in database" %
                  (SteamWaterPipe.id, SteamWaterPipe.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        steamWaterPipe = GPGSteamWaterPipe.search_SteamWaterPipe(plan_id)
        db.session.delete(steamWaterPipe)

# 煤气发电 汽机辅机系统 turbine auxiliary system
class GPGTurbineAuxiliarySystem(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_turbine_auxiliary_system'
    __table_args__ = {'comment': u'煤气发电汽机辅机系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    '''1、凝结水泵'''
    # 除氧器工作压力
    deaerator_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器工作压力")
    # 除氧器凝结水入口与凝汽器热井最低水位间的水柱静压差
    deaerator_condensation_well_pressure_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器凝结水入口与凝汽器热井最低水位间的水柱静压差")
    # 除氧器入口凝结水管喷雾头所需喷雾压力
    deaerator_condensation_spray_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"除氧器入口凝结水管喷雾头所需喷雾压力")
    # 凝汽器的最高真空
    condenser_maximum_vacuum = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器的最高真空")
    # 从热井到除氧器凝结水入口的凝结水管道流动阻力，另加20%裕量
    deaerator_condensation_well_pipe_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"从热井到除氧器凝结水入口的凝结水管道流动阻力")
    # 凝结水泵的设计扬程
    condensate_pump_design_lift = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵的设计扬程")
    # 流量
    condensate_pump_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-流量")
    # 泵效率
    condensate_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-泵效率")
    # 机械传动效率
    condensate_pump_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-机械传动效率")
    # 电动机效率
    condensate_pump_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-电动机效率")
    # 电动机备用系数
    condensate_pump_motor_spare_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-电动机备用系数")
    # 配套电机功率
    condensate_pump_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水泵-配套电机功率")
    # 选用规格
    condensate_pump_selected = db.Column(db.Text(), comment=u"凝结水泵-选用规格")

    '''2、射水泵'''
    # 射水抽气器工作压力
    extractor_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水抽气器工作压力")
    # 射水箱工作压力
    ejection_tank_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱工作压力")
    # 射水抽气器安装高度与射水箱最高水位之差
    extractor_ejection_waterline_height_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水抽气器安装高度与射水箱最高水位之差")
    # 射水泵进出口管路损失
    jet_pump_pipe_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵进出口管路损失")
    # 总扬程
    jet_pump_total_lift = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-总扬程")
    # 流量
    jet_pump_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-流量")
    # 泵效率
    jet_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-泵效率")
    # 机械传动效率
    jet_pump_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-机械传动效率")
    # 电动机效率
    jet_pump_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-电动机效率")
    # 电动机备用系数
    jet_pump_motor_spare_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-电动机备用系数")
    # 配套电机功率
    jet_pump_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵-配套电机功率")
    # 选用规格
    jet_pump_selected = db.Column(db.Text(), comment=u"射水泵-选用规格")

    '''3、射水箱冷却水泵'''
    # 射水箱工作压力
    cooling_ejection_tank_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱工作压力")
    # 循环水回水母管压力
    cooling_circulating_water_to_header_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水回水母管压力")
    # 射水抽气器安装高度与射水箱最高水位之差
    cooling_extractor_ejection_waterline_height_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水抽气器安装高度与射水箱最高水位之差")
    # 射水泵进出口管路损失
    cooling_jet_pump_pipe_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水泵进出口管路损失")
    # 总扬程
    cooling_jet_pump_total_lift = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-总扬程")
    # 流量
    cooling_jet_pump_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-流量")
    # 泵效率
    cooling_jet_pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-泵效率")
    # 机械传动效率
    cooling_jet_pump_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-机械传动效率")
    # 电动机效率
    cooling_jet_pump_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-电动机效率")
    # 电动机备用系数
    cooling_jet_pump_motor_spare_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-电动机备用系数")
    # 配套电机功率
    cooling_jet_pump_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"射水箱冷却水泵-配套电机功率")
    # 选用规格
    cooling_jet_pump_selected = db.Column(db.Text(), comment=u"射水箱冷却水泵-选用规格")

    '''4、凝汽器计算（22.4*凝汽量'''
    # 凝汽量
    condenser_flow_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽量")
    # 凝汽器压力
    condenser_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器压力")
    # 汽轮机排汽焓
    turbine_exhaust_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机排汽焓")
    # 冷却水进口温度
    cooling_water_inlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水进口温度")
    # 饱和温度
    saturation_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-饱和温度")
    # 过冷度
    supercooling_degree = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-过冷度")
    # 凝结水温度
    condensate_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-凝结水温度")
    # 凝结水焓
    condensate_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-凝结水焓")
    # 冷却管的洁净系数
    cooling_pipe_clean_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-冷却管的洁净系数")
    # 冷却管材料和壁厚的修正系数
    cooling_pipe_correct_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-冷却管材料和壁厚的修正系数")
    # 计算指数
    calculate_exponent = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-计算指数")
    # 冷却管内流速
    cooling_pipe_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-冷却管内流速")
    # 冷却管内径
    cooling_pipe_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-冷却管内径")
    # 凝汽器比蒸汽负荷修正系数
    condenser_steam_load_correct_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器比蒸汽负荷修正系数")
    # 冷却管内流速的修正系数
    cooling_pipe_flow_velocity_correct_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却管内流速的修正系数")
    # 冷却水进口温度修正系数
    cooling_water_inlet_temperature_correct_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水进口温度修正系数")
    # 冷却水流程数的修正系数
    cooling_water_pass_correct_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷却水流程数的修正系数")
    # 考虑凝汽器蒸汽负荷变化的修正系数
    condenser_steam_load_change_correct_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"考虑凝汽器蒸汽负荷变化的修正系数")
    # 总传热系数
    total_heat_transfer_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-总传热系数")
    # 凝汽器热负荷
    condenser_heat_load = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器热负荷")
    # 循环倍率
    circulation_ratio = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-循环倍率")
    # 循环水量
    circulating_water_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-循环水量")
    # 冷却水温升 冷却水cp 取4.1868
    cooling_water_temperature_rise = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-冷却水温升")
    # 冷却水出口温度
    cooling_water_outlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-冷却水出口温度")
    # 对数平均温差
    logarithmic_average_temperature_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-对数平均温差")
    # 冷却面积
    cooling_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器计算-冷却面积")

    '''5、水环真空泵'''
    # 凝汽量
    vacuum_pump_condensate_flow_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"水环真空泵-凝汽量")

    def __init__(self, **kwargs):
        super(GPGTurbineAuxiliarySystem, self).__init__(**kwargs)

    @staticmethod
    def insert_TurbineAuxiliary(gaspowergeneration_turbine_auxiliary_system):
        try:
            db.session.add(gaspowergeneration_turbine_auxiliary_system)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_turbine_auxiliary_system"
                  "<id=%s> in database" % (gaspowergeneration_turbine_auxiliary_system.id))

    # 根据plan id查找实体
    @staticmethod
    def search_TurbineAuxiliary(planId):
        result = GPGTurbineAuxiliarySystem.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_TurbineAuxiliary(plan_id):
        TurbineAuxiliary = GPGTurbineAuxiliarySystem.search_TurbineAuxiliary(plan_id)
        try:
            db.session.delete(TurbineAuxiliary)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete TurbineAuxiliary<id=%s, plan_id=%s> in database" %
                  (TurbineAuxiliary.id, TurbineAuxiliary.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        TurbineAuxiliary = GPGTurbineAuxiliarySystem.search_TurbineAuxiliary(plan_id)
        db.session.delete(TurbineAuxiliary)


# 煤气发电 烟、风量计算 smoke_air_calculate
class GPGSmokeAirCalculate(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_smoke_air_calculate'
    __table_args__ = {'comment': u'煤气发电烟风量计算表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # H2 组分		
    component_h2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"H2 组分")
    # co 组分		
    component_co = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"CO 组分")
    # ch4 组分		
    component_ch4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"ch4 组分")
    # c2h4 组分		
    component_c2h4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c2h4 组分")
    # c3h8 组分		
    component_c3h8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c3h8 组分")
    # c4h10 组分		
    component_c4h10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c4h10 组分")
    # n2 组分		
    component_n2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"n2 组分")
    # o2 组分		
    component_o2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"o2 组分")
    # co2 组分		
    component_co2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"co2 组分")
    # h2s 组分		
    component_h2s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"h2s 组分")
    # cmhn 组分		
    component_cmhn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"cmhn 组分")

    # H2 Hl		
    hl_h2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"H2 Hl")
    # co Hl		
    hl_co = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"co Hl")
    # ch4 Hl		
    hl_ch4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"ch4 Hl")
    # c2h4 Hl		
    hl_c2h4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c2h4 Hl")
    # c3h8 Hl		
    hl_c3h8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c3h8 Hl")
    # c4h10 Hl		
    hl_c4h10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c4h10 Hl")
    # n2 Hl		
    hl_n2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"n2 Hl")
    # o2 Hl		
    hl_o2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"o2 Hl")
    # co2 Hl		
    hl_co2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"co2 Hl")
    # h2s Hl		
    hl_h2s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"h2s Hl")
    # cmhn Hl		
    hl_cmhn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"cmhn Hl")

    # H2 Hh		
    hh_h2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"H2 Hh")
    # co Hh		
    hh_co = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"co Hh")
    # ch4 Hh		
    hh_ch4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"ch4 Hh")
    # c2h4 Hh		
    hh_c2h4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c2h4 Hh")
    # c3h8 Hh		
    hh_c3h8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c3h8 Hh")
    # c4h10 Hh		
    hh_c4h10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c4h10 Hh")
    # n2 Hh		
    hh_n2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"n2 Hh")
    # o2 Hh		
    hh_o2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"o2 Hh")
    # co2 Hh		
    hh_co2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"co2 Hh")
    # h2s Hh		
    hh_h2s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"h2s Hh")
    # cmhn Hh		
    hh_cmhn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"cmhn Hh")

    # H2 定压比热容		
    cpsh_h2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"H2定压比热容")
    # co 定压比热容		
    cpsh_co = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"co定压比热容")
    # ch4 定压比热容		
    cpsh_ch4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"ch4定压比热容")
    # c2h4 定压比热容		
    cpsh_c2h4 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c2h4定压比热容")
    # c3h8 定压比热容		
    cpsh_c3h8 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c3h8定压比热容")
    # c4h10 定压比热容		
    cpsh_c4h10 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"c4h10定压比热容")
    # n2 定压比热容		
    cpsh_n2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"n2定压比热容")
    # o2 定压比热容		
    cpsh_o2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"o2定压比热容")
    # co2 定压比热容		
    cpsh_co2 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"co2定压比热容")
    # h2s 定压比热容		
    cpsh_h2s = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"h2s定压比热容")
    # cmhn 定压比热容		
    cpsh_cmhn = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"cmhn定压比热容")

    # 标态下每m³干燃气燃烧所需理论空气量																							
    constant_need_air_amonut_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³干燃气燃烧所需理论空气量")
    # 标态下空气密度																																												
    constant_air_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下空气密度")
    # 标态下每m³干燃气燃烧所需理论空气质量																																												
    constant_need_air_mass_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³干燃气燃烧所需理论空气质量")
    # 过量空气系数																																												
    excessive_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过量空气系数")
    # 实际所需空气量																																												
    actual_need_air_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际所需空气量")
    # 标态下每m³燃气的含湿量																																												
    constant_gas_humidity_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³燃气的含湿量")
    # 标态下每m³空气的含湿量																																												
    constant_air_humidity_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³空气的含湿量")
    # 空气中有水时，实际空气量																																																				
    actual_air_amount_in_wet = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气中有水时，实际空气量")
    # 标态下每m³燃气燃烧理论烟气量中RO2																																																																									
    constant_ro2_amonut_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³燃气燃烧理论烟气量中RO2")
    # 标态下每m³燃气燃烧理论烟气量中N2																																																																																														
    constant_n2_amonut_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³燃气燃烧理论烟气量中N2")
    # 标态下每m³燃气燃烧理论烟气量中N2实际																																																																									
    constant_actual_n2_amonut_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³燃气燃烧理论烟气量中N2实际")
    # 标态下每m³燃气燃烧理论烟气量中H2O																																																																									
    constant_h2o_amonut_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³燃气燃烧理论烟气量中H2O")
    # 标态下每m³燃气燃烧理论烟气量中H2O实际																																																																																														
    constant_actual_h2o_amonut_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³燃气燃烧理论烟气量中H2O实际")
    # 标态下每m³燃气燃烧理论烟气量中O2																																																																																														
    constant_o2_amonut_per_m3 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³燃气燃烧理论烟气量中O2")
    # 实际燃烧烟气量																																																																																																					
    actual_burning_gas_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际燃烧烟气量")
    # 理论燃烧烟气量																																																																																																					
    theory_burning_gas_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论燃烧烟气量")
    # 低位发热量																																																																																																					
    net_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低位发热量")
    # 高位发热量																																																																																																					
    gross_heating_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高位发热量")
    # 燃气初始温度																																																																																																																										
    gas_init_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气初始温度")
    # 空气初始温度																																																																																																																										
    air_init_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气初始温度")
    # 燃气平均定压体积热容																																																																																																																												
    gas_average_cpvh = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气平均定压体积热容")
    # 燃气中H2O平均定压体积热容	
    gas_h2o_average_cpvh = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气中H2O平均定压体积热容")	
    # 空气平均定压体积热容	
    air_average_cpvh = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气平均定压体积热容")	
    # 空气中H2O平均定压体积热容	
    air_h2o_average_cpvh = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气中H2O平均定压体积热容")		
    # 假设---绝热状态的热量计温度							
    hy_adiabatic_calorimeter_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"假设-绝热状态的热量计温度")	
    # 烟气中RO2平均定压体积热容	
    smoke_ro2_average_cpvh = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中RO2平均定压体积热容")	
    # 烟气中H2O平均定压体积热容	
    smoke_h2o_average_cpvh = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中H2O平均定压体积热容")	
    # 烟气中N2平均定压体积热容	
    smoke_n2_average_cpvh = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中N2平均定压体积热容")
    # 烟气中O2平均定压体积热容	
    smoke_o2_average_cpvh = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中O2平均定压体积热容")
    # 计算---绝热状态的热量计温度							
    calc_adiabatic_calorimeter_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算-绝热状态的热量计温度")
    # 误差核对---2%以内合理							
    deviation_check = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"误差核对")   	
    # 化学不完全燃烧热损失系数	
    incomplete_combustion_loss_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"化学不完全燃烧热损失系数")  	
    # 化学不完全燃烧热损失	
    incomplete_combustion_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"化学不完全燃烧热损失")	
    # 散热损失系数	
    heat_loss_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"散热损失系数")
    # 散热损失	
    heat_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"散热损失")	
    # 计算---理论燃烧温度							
    calc_theory_burning_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"计算-理论燃烧温度")	
    # 高温系数							
    high_temperature_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高温系数")	
    # 实际燃烧温度--系数法							
    coefficient_actual_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际燃烧温度-系数法")	
    # 实际燃烧温度--计算法							
    calc_actual_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际燃烧温度-计算法")	
    # 烟气中R02体积焓							
    ro2_volume_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中R02体积焓")	
    # 烟气中N2体积焓							
    n2_volume_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中N2体积焓")
    # 烟气中H2O体积焓							
    h2o_volume_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中H2O体积焓")
    # 烟气中空气体积焓							
    air_volume_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中空气体积焓")	
    # 烟气中飞灰体积焓							
    dust_volume_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气中飞灰体积焓")	
    # 理论烟气体积焓							
    theory_smoke_volume_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论烟气体积焓")	
    # 理论空气体积焓							
    theory_air_volume_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论空气体积焓")
    # 理论飞灰体积焓							
    theory_dust_volume_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论飞灰体积焓")
    # 烟气焓							
    smoke_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气焓")

    # 燃气干燥基低位发热量							
    qd_net = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气干燥基低位发热量")
    # 燃气收到基地位发热量							
    qar_net = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃气收到基地位发热量")
    # 标态下每m³干燃气燃烧所需理论空气量 Qd.net<10500时																							
    unknown_need_air_amonut_b_10500 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³干燃气燃烧所需理论空气量 Qd.net<10500时")
    # 标态下每m³干燃气燃烧所需理论空气量 Qd.net>10500时																							
    unknown_need_air_amonut_a_10500 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³干燃气燃烧所需理论空气量 Qd.net>10500时")
    # 标态下每m³干燃气燃烧所需理论空气量 天然气																							
    unknown_need_air_amonut_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³干燃气燃烧所需理论空气量 天然气")
    # 标态下每m³干燃气燃烧所需理论空气量 液化石油气																							
    unknown_need_air_amonut_lng = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³干燃气燃烧所需理论空气量 液化石油气")
    # 过量空气系数																																												
    unknown_excessive_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过量空气系数")
    # 标态下每m³干燃气燃烧所需实际空气量																							
    unknown_actual_need_air_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标态下每m³干燃气燃烧所需实际空气量")
    # 理论燃烧烟气量 天然气																																																																																																				
    unknown_theory_burning_amonut_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论燃烧烟气量 天然气")
    # 理论燃烧烟气量 石油伴生气																																																																																																					
    unknown_theory_burning_amonut_oag = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论燃烧烟气量 石油伴生气")
    # 理论燃烧烟气量 液化天然气																																																																																																				
    unknown_theory_burning_amonut_lng = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论燃烧烟气量 液化天然气")
    # 理论燃烧烟气量 焦炉煤气																																																																																																				
    unknown_theory_burning_amonut_cog = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"理论燃烧烟气量 焦炉煤气")
    # 理论燃烧烟气量 Qar.net<12600																																																																																																					
    unknown_theory_burning_amonut_b_12600 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u" 理论燃烧烟气量 Qar.net<12600时")
    # 实际燃烧烟气量																																																																																																					
    unknown_actual_burning_gas_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"实际燃烧烟气量")
    # 高炉煤气实际燃烧烟气量																																																																																																					
    unknown_boiler_actual_burning_gas_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气实际燃烧烟气量")
    # 天然气实际燃烧烟气量																																																																																																					
    unknown_gas_actual_burning_gas_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"天然气实际燃烧烟气量")

    # 经验公式计算方法 天然气煤气 低位发热量																																																																																																					
    exp_gas_qnet = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"天然气煤气 低位发热量")
    # 经验公式计算方法 天然气煤气 理论空气量 QL＞35799																																																																																																					
    exp_gas_theory_air_amount_a_35799 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"然气煤气 理论空气量 QL＞35799")
    # 经验公式计算方法 天然气煤气 理论空气量 QL＜35799																																																																																																										
    exp_gas_theory_air_amount_b_35799 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"天然气煤气 理论空气量 QL＜35799")
    # 经验公式计算方法 天然气煤气 过量空气系数																																																																																																					
    exp_gas_excessive_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"天然气煤气 过量空气系数")
    # 经验公式计算方法 天然气煤气 实际烟气量 QL＞35799																																																																																																				
    exp_gas_actual_amonut_a_35799 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"天然气煤气 实际烟气量 QL＞35799")
    # 经验公式计算方法 天然气煤气 实际烟气量 QL＜35799																																																																																																				
    exp_gas_actual_amonut_b_35799 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"天然气煤气 实际烟气量 QL＜35799")

    # 经验公式计算方法 焦炉、高炉混合煤气 低位发热量																																																																																																					
    exp_boiler_qnet = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉、高炉混合煤气 低位发热量")
    # 经验公式计算方法 焦炉、高炉混合煤气 理论空气量	QL＞12561																																																																																																				
    exp_boiler_theory_air_amount_a_12561 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉、高炉混合煤气 理论空气量	QL＞12561")
    # 经验公式计算方法 焦炉、高炉混合煤气 理论空气量	QL＜12561																																																																																																				
    exp_boiler_theory_air_amount_b_12561 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉、高炉混合煤气 理论空气量	QL＜12561")
    # 经验公式计算方法 焦炉、高炉混合煤气 过量空气系数																																																																																																					
    exp_boiler_excessive_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉、高炉混合煤气 过量空气系数")
    # 经验公式计算方法 焦炉、高炉混合煤气 实际烟气量	QL＞12561																																																																																																				
    exp_boiler_actual_amonut_a_12561 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉、高炉混合煤气 实际烟气量	QL＞12561")
    # 经验公式计算方法 焦炉、高炉混合煤气 实际烟气量	QL＜12561																																																																																																				
    exp_boiler_actual_amonut_b_12561 = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉、高炉混合煤气 实际烟气量	QL＜12561")

    # 经验公式计算方法 各种液体燃料 低位发热量																																																																																																					
    exp_liquid_fuel_qnet = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"各种液体燃料 低位发热量")
    # 经验公式计算方法 各种液体燃料 理论空气量																																																																																																					
    exp_liquid_fuel_theory_air_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"各种液体燃料 理论空气量")
    # 经验公式计算方法 各种液体燃料 过量空气系数																																																																																																					
    exp_liquid_fuel_excessive_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"各种液体燃料 过量空气系数")
    # 经验公式计算方法 各种液体燃料 实际烟气量																																																																																																					
    exp_liquid_fuel_actual_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"各种液体燃料 实际烟气量")

    # 经验公式计算方法 各种煤 低位发热量																																																																																																					
    exp_coal_qnet = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"各种煤 低位发热量")
    # 经验公式计算方法 各种煤 理论空气量																																																																																																					
    exp_coal_theory_air_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"各种煤 理论空气量")
    # 经验公式计算方法 各种煤 过量空气系数																																																																																																					
    exp_coal_excessive_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"各种煤 过量空气系数")
    # 经验公式计算方法 各种煤 实际烟气量																																																																																																					
    exp_coal_actual_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"各种煤 实际烟气量")

    # 经验公式计算方法 木材和泥煤 低位发热量																																																																																																					
    exp_wood_peat_qnet = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"木材和泥煤 低位发热量")
    # 经验公式计算方法 木材和泥煤 含水量																																																																																																					
    exp_wood_peat_water_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"木材和泥煤 含水量")
    # 经验公式计算方法 木材和泥煤 理论空气量																																																																																																					
    exp_wood_peat_theory_air_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"木材和泥煤 理论空气量")
    # 经验公式计算方法 木材和泥煤 过量空气系数																																																																																																					
    exp_wood_peat_excessive_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"木材和泥煤 过量空气系数")
    # 经验公式计算方法 木材和泥煤 最佳含水量																																																																																																					
    exp_wood_peat_best_water_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"木材和泥煤 最佳含水量")
    # 经验公式计算方法 木材和泥煤 实际烟气量																																																																																																					
    exp_wood_peat_actual_amonut = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"木材和泥煤 实际烟气量")

    def __init__(self, **kwargs):
        super(GPGSmokeAirCalculate, self).__init__(**kwargs)

    @staticmethod
    def insert_SmokeAirCalculate(gaspowergeneration_smoke_air_calculate):
        try:
            db.session.add(gaspowergeneration_smoke_air_calculate)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_smoke_air_calculate"
                  "<id=%s> in database" % (gaspowergeneration_smoke_air_calculate.id))

    # 根据plan id查找实体
    @staticmethod
    def search_SmokeAirCalculate(planId):
        result = GPGSmokeAirCalculate.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_SmokeAirCalculate(plan_id):
        SmokeAirCalculate = GPGSmokeAirCalculate.search_SmokeAirCalculate(plan_id)
        try:
            db.session.delete(SmokeAirCalculate)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete SmokeAirCalculate<id=%s, plan_id=%s> in database" %
                  (SmokeAirCalculate.id, SmokeAirCalculate.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        SmokeAirCalculate = GPGSmokeAirCalculate.search_SmokeAirCalculate(plan_id)
        db.session.delete(SmokeAirCalculate)


# 煤气发电 循环水系统 circulating_water_system
class GPGCirculatingWaterSystem(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_circulating_water_system'
    __table_args__ = {'comment': u'煤气发电循环水系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 冬季乏汽流量
    steam_exhaust_flux_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冬季乏汽流量")
    # 夏季乏汽流量
    steam_exhaust_flux_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"夏季乏汽流量")
    # 选定乏汽流量
    steam_exhaust_flux_selected = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"选定乏汽流量")
    # 冬季循环倍率
    circulation_ratio_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冬季循环倍率")
    # 夏季循环倍率
    circulation_ratio_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"夏季循环倍率")
    # 冬季循环水量
    circulation_water_flow_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冬季循环水量")
    # 夏季循环水量
    circulation_water_flow_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"夏季循环水量")
    # 冬季辅机冷却水量
    auxiliary_cooling_water_flow_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冬季辅机冷却水量")
    # 夏季辅机冷却水量
    auxiliary_cooling_water_flow_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"夏季辅机冷却水量")
    # 冬季总循环水量
    total_circulation_water_flow_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冬季总循环水量")
    # 夏季总循环水量
    total_circulation_water_flow_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"夏季总循环水量")

    # 总循环水量-选定
    selected_total_circulation_water_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总循环水量-选定")
    # 喷淋密度
    spray_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"喷淋密度")
    # 喷淋面积
    spray_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"喷淋面积")
    # 进、出水口温差
    in_out_water_temperature_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"进、出水口温差")
    # 干球温度
    dry_bulb_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"干球温度")
    # K
    dry_bulb_k_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"K系数")
    # 蒸发损失率
    evaporation_loss_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸发损失率")
    # 蒸发损失
    evaporation_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"蒸发损失")
    # 风吹损失率
    wind_blow_loss_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风吹损失率")
    # 风吹损失
    wind_blow_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"风吹损失")
    # 浓缩倍率
    concentration_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"浓缩倍率")
    # 排污损失率
    discharge_rate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排污损失率")
    # 排污量
    discharge_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排污量")
    # 补充水量
    supply_water_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"补充水量")
    # 循环水池15-25分钟循环水量
    circulating_pool_water_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池15-25分钟循环水量")
    # 循环水池尺寸-深
    circulating_pool_size_deep = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池尺寸-深")
    # 循环水池尺寸-长
    circulating_pool_size_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池尺寸-长")
    # 循环水池尺寸-宽
    circulating_pool_size_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水池尺寸-宽")
    # 校核循环水池尺寸
    circulating_pool_size_checked = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"校核循环水池尺寸")
    
    # 凝汽器阻力
    condenser_friction = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器阻力")
    # 循环水回水压力
    circulating_backwater_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水回水压力")
    # 循环水吸水池压力
    circulating_water_reservoir_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水吸水池压力")
    # 凝汽器循环水进水工作压力
    condenser_circulating_water_inlet_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝汽器循环水进水工作压力")
    # 循环水泵出口与凝汽器循环水进水口高度差
    circulation_pump_outlet_to_condenser_inlet_height_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"循环水泵出口与凝汽器循环水进水口高度差")
    # 吸水池与水泵入口高度差
    reservoir_to_pump_inlet_height_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"吸水池与水泵入口高度差")
    # 管道损失
    pipe_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"管道损失")
    # Y型过滤器损失
    y_filter_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"Y型过滤器损失")
    # 总扬程
    total_pumping_lift = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"总扬程")
    # 流量
    pump_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"流量")
    # 泵效率
    pump_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"泵效率")
    # 机械传动效率
    pump_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机械传动效率")
    # 电动机效率
    pump_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机效率")
    # 电动机备用系数
    pump_motor_spare_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"电动机备用系数")
    # 配套电机功率
    pump_matching_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"配套电机功率")
    # 选用型号-功率
    selected_pump_model_power = db.Column(db.Text(), comment=u"选用型号-功率")
    # 选用型号-流量
    selected_pump_model_flow = db.Column(db.Text(), comment=u"选用型号-流量")
    # 选用型号-扬程
    selected_pump_model_lift = db.Column(db.Text(), comment=u"选用型号-扬程")

    cooling_tower_selected_type = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    cooling_tower_selected_name = db.Column(db.Text(), comment=u"循环冷却塔类型")
    # 方案一 双曲线自然通风冷却塔选型
    # 喷淋密度
    p_spray_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 喉部喷淋面积
    p_spray_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 选型
    p_select_f = db.Column(db.Text(), comment=u"")

    # 方案二 逆流式机械通风冷却塔
    # 数量
    p_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 单台冷却水量
    p_single_cold_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 选型
    p_select_s = db.Column(db.Text(), comment=u"")

    def __init__(self, **kwargs):
        super(GPGCirculatingWaterSystem, self).__init__(**kwargs)

    @staticmethod
    def insert_CirculatingWater(gaspowergeneration_circulating_water_system):
        try:
            db.session.add(gaspowergeneration_circulating_water_system)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_circulating_water_system"
                  "<id=%s> in database" % (gaspowergeneration_circulating_water_system.id))

    # 根据plan id查找实体
    @staticmethod
    def search_CirculatingWater(planId):
        result = GPGCirculatingWaterSystem.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_CirculatingWater(plan_id):
        CirculatingWater = GPGCirculatingWaterSystem.search_CirculatingWater(plan_id)
        try:
            db.session.delete(CirculatingWater)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete CirculatingWater<id=%s, plan_id=%s> in database" %
                  (CirculatingWater.id, CirculatingWater.plan_id))
    
    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        CirculatingWater = GPGCirculatingWaterSystem.search_CirculatingWater(plan_id)
        db.session.delete(CirculatingWater)


# 煤气发电 风阻力
class GPGWindResistance(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_wind_resistance'
    __table_args__ = {'comment': u'煤气发电风阻力表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 推荐流速(送风机进出口冷风道)
    recommend_velocity_coldwind = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 推荐流速(热风道)
    recommend_velocity_hotwind = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''冷风道(吸风口至空预器）'''
    # 计算温度
    intake_to_preheater_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风量
    intake_to_preheater_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 密度
    intake_to_preheater_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 流速
    intake_to_preheater_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 动压头
    intake_to_preheater_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''风机进口'''
    # 风管截面积
    fan_inlet_duct_section_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 长
    fan_inlet_duct_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 宽
    fan_inlet_duct_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管周长
    fan_inlet_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道当量直径
    fan_inlet_duct_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 气体运动粘度
    fan_inlet_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 雷诺数
    fan_inlet_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁绝对粗糙度
    fan_inlet_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁相对粗糙度
    fan_inlet_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 560/△1
    fan_inlet_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 判别式
    fan_inlet_discriminant = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    # 摩擦阻力
    fan_inlet_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 摩擦阻力系数
    fan_inlet_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 单位长度摩擦阻力
    fan_inlet_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管长度
    fan_inlet_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力
    fan_inlet_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力系数
    fan_inlet_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1个吸风口局部阻力系数
    fan_inlet_single_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1个风机进口风箱
    fan_inlet_single_bellows = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1个进口挡板门
    fan_inlet_single_damper = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风机进口段总阻力
    fan_inlet_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''风机出口至空预器'''
    # 摩擦阻力
    fan_outlet_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 单位长度摩擦阻力
    fan_outlet_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管长度
    fan_outlet_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力
    fan_outlet_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力系数
    fan_outlet_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1只出口渐扩管
    fan_outlet_single_increase_pipe = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1只90度等截面急转弯头/（二次风2只）
    fan_outlet_90_section_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 空预器接头扩散管
    fan_outlet_preheater_diffuser_pipe = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风机出口至空预器总阻力
    fan_outlet_to_preheater_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''热风道（空预器出口至锅炉风室）'''
    # 计算温度
    preheater_to_boiler_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风量
    preheater_to_boiler_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 密度
    preheater_to_boiler_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 流速
    preheater_to_boiler_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 动压头
    preheater_to_boiler_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管截面积（热风管分两路进入风室）
    preheater_outlet_duct_section_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 圆管直径(一、二次热风为圆管）
    preheater_outlet_duct_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 长
    preheater_outlet_duct_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 宽
    preheater_outlet_duct_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管周长
    preheater_outlet_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道当量直径
    preheater_outlet_duct_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 气体运动粘度
    preheater_outlet_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 雷诺数
    preheater_outlet_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁绝对粗糙度
    preheater_outlet_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁相对粗糙度
    preheater_outlet_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 560/△1
    preheater_outlet_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 判别式
    preheater_outlet_discriminant = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    # 摩擦阻力
    preheater_outlet_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 摩擦阻力系数
    preheater_outlet_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 单位长度摩擦阻力
    preheater_outlet_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管长度
    preheater_outlet_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力
    preheater_outlet_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力系数
    preheater_outlet_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    # 1个空预器出口收缩管
    preheater_outlet_shrink_pipe = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 6只90度等截面急转弯头
    preheater_outlet_90_sharp_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 弯头数量
    preheater_outlet_90_sharp_turn_elbow_count = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 弯头局部阻力系统(焊接圆管）
    preheater_outlet_90_sharp_turn_elbow_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    # 1个热一次风进风室风门
    preheater_outlet_air_intake_gate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1个热一次风进燃烧室风门
    preheater_outlet_combustor_gate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 空预器出口至锅炉风室总阻力
    preheater_outlet_to_boiler_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风道总阻力
    windhole_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    def __init__(self, **kwargs):
        super(GPGWindResistance, self).__init__(**kwargs)

    @staticmethod
    def insert_WindResistance(gaspowergeneration_wind_resistance):
        try:
            db.session.add(gaspowergeneration_wind_resistance)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_wind_resistance"
                  "<id=%s> in database" % (gaspowergeneration_wind_resistance.id))

    # 根据plan id查找实体
    @staticmethod
    def search_WindResistance(planId):
        result = GPGWindResistance.query.filter_by(plan_id=planId).one_or_none()
        return result

     # 根据plan_id删除实体
    @staticmethod
    def delete_WindResistance(plan_id):
        WindResistance = \
            GPGWindResistance.search_WindResistance(plan_id)
        try:
            db.session.delete(WindResistance)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete WindResistance<id=%s, plan_id=%s> in database" %
                  (WindResistance.id, WindResistance.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        WindResistance =  GPGWindResistance.search_WindResistance(plan_id)
        db.session.delete(WindResistance)


# 煤气发电 烟阻力
class GPGSmokeResistance(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_smoke_resistance'
    __table_args__ = {'comment': u'煤气发电烟阻力表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 推荐流速
    recommend_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''空预器出口至除尘器入口'''
    # 计算温度(空预器出口)
    air_preheater_outlet_calculated_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 烟量(空预器出口)
    air_preheater_outlet_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 密度
    air_preheater_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 流速
    air_preheater_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 动压头
    air_preheater_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 烟管截面积
    air_preheater_smoke_tube_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 长
    air_preheater_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 宽
    air_preheater_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管周长
    air_preheater_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道当量直径
    air_preheater_tube_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 气体运动粘度
    air_preheater_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 雷诺数
    air_preheater_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁绝对粗糙度
    air_preheater_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁相对粗糙度
    air_preheater_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 560/△1
    air_preheater_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 判别式
    air_preheater_discriminant = db.Column(db.Text())

    # 摩擦阻力
    air_preheater_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 摩擦阻力系数
    air_preheater_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 单位长度摩擦阻力
    air_preheater_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管长度
    air_preheater_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力
    air_preheater_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力系数
    air_preheater_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''90度空预器出口变径急转弯头'''
    # 1个90度空预器出口变径急转弯头
    air_preheater_90_outlet_sharp_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉气体局部阻力系数
    air_preheater_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 纯空气弯头局部阻力系数
    air_preheater_air_elbow_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉浓度修正系数
    air_preheater_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''90度等截面缓转弯头'''
    # 1个90度等截面缓转弯头
    air_preheater_90_section_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉气体局部阻力系数
    air_preheater_slow_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 纯空气弯头局部阻力系数
    air_preheater_slow_air_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉浓度修正系数
    air_preheater_slow_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1个渐缩管
    air_preheater_reducer_tube = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 空预器出口至除尘器入口总阻力
    air_preheater_to_deduster_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''除尘器出口至引风机入口'''
    # 计算温度(除尘器出口)
    deduster_outlet_calculated_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 烟量(除尘器出口)
    deduster_outlet_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 密度
    deduster_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 流速
    deduster_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 动压头
    deduster_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 烟管截面积
    deduster_smoke_tube_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 长
    deduster_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 宽
    deduster_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管周长
    deduster_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道当量直径
    deduster_tube_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 气体运动粘度
    deduster_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 雷诺数
    deduster_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁绝对粗糙度
    deduster_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁相对粗糙度
    deduster_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 560/△1
    deduster_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 判别式
    deduster_discriminant = db.Column(db.Text())

    # 摩擦阻力
    deduster_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 摩擦阻力系数
    deduster_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 单位长度摩擦阻力
    deduster_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管长度
    deduster_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力
    deduster_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力系数
    deduster_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''90度除尘器出口缓转弯头'''
    # 1个90度除尘器出口缓转弯头
    deduster_90_outlet_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉气体局部阻力系数
    deduster_slow_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 纯空气弯头局部阻力系数
    deduster_slow_air_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉浓度修正系数
    deduster_slow_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    ''' 90度等截面缓转弯头 '''
    # 1个90度等截面缓转弯头
    deduster_90_section_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉气体局部阻力系数
    deduster_section_slow_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 纯空气弯头局部阻力系数
    deduster_section_slow_air_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 转弯角度修正系数
    deduster_corrected_turning_angle_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 截面高宽比修正系数
    deduster_section_corrected_height_width_ratio_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 包含管壁粗糙度影响的纯空气下的转弯原始阻力系数
    deduster_section_original_resistance_coefficient_with_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉浓度修正系数
    deduster_section_slow_powder_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1个进口风箱
    deduster_inlet_bellows = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 除尘器出口至引风机入口总阻力
    deduster_to_induced_draft_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''引风机出口至烟囱'''
    # 计算温度(引风机进口)
    induced_draft_inlet_calculated_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 烟量(引风机进口)
    induced_draft_inlet_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 密度
    induced_draft_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 流速
    induced_draft_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 动压头
    induced_draft_dynamic_pressure_head = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 烟管截面积
    induced_draft_smoke_tube_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"") 
    # 宽
    induced_draft_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 高
    induced_draft_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管周长
    induced_draft_duct_perimeter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道当量直径
    induced_draft_tube_equivalent_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 气体运动粘度
    induced_draft_gas_kinetic_viscosity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 雷诺数
    induced_draft_reynolds_number = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁绝对粗糙度
    induced_draft_absolute_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 管道内壁相对粗糙度
    induced_draft_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 560/△1
    induced_draft_560_relative_tube_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 判别式
    induced_draft_discriminant = db.Column(db.Text())

    # 摩擦阻力
    induced_draft_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 摩擦阻力系数
    induced_draft_frictional_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 单位长度摩擦阻力
    induced_draft_unit_length_frictional_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 风管长度
    induced_draft_ducting_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力
    induced_draft_local_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 局部阻力系数
    induced_draft_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    # 1个出口插板门
    induced_draft_outlet_plate_gate = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1个出口扩散管
    induced_draft_outlet_diffuser_tube = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 1个45度缓转弯头（钢烟道）/1个90度缓转弯头（砖烟道）
    induced_draft_45_90_slow_turn_elbow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉气体局部阻力系数
    induced_draft_powder_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 纯空气局部阻力系数
    induced_draft_air_local_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 转弯角度修正系数
    induced_draft_corrected_turning_angle_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 截面高宽比修正系数
    induced_draft_corrected_height_width_ratio_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 包含管壁粗糙度影响的纯空气下的转弯原始阻力系数
    induced_draft_original_resistance_coefficient_with_roughness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 含粉浓度修正系数
    induced_draft_powder_concentration_corrected_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    # 砖烟道烟囱入口
    brick_chimney_inlet = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 引风机出口至烟囱入口总阻力
    induced_draft_to_chimney_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 烟道总阻力
    smoke_chimney_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    def __init__(self, **kwargs):
        super(GPGSmokeResistance, self).__init__(**kwargs)

    @staticmethod
    def insert_SmokeResistance(gaspowergeneration_smoke_resistance):
        try:
            db.session.add(gaspowergeneration_smoke_resistance)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_smoke_resistance"
                  "<id=%s> in database" % (gaspowergeneration_smoke_resistance.id))

    # 根据plan id查找实体
    @staticmethod
    def search_SmokeResistance(planId):
        result = GPGSmokeResistance.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_SmokeResistance(plan_id):
        SmokeResistance =  GPGSmokeResistance.search_SmokeResistance(plan_id)
        try:
            db.session.delete(SmokeResistance)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete SmokeResistance<id=%s, plan_id=%s> in database" %
                  (SmokeResistance.id, SmokeResistance.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        SmokeResistance =  GPGSmokeResistance.search_SmokeResistance(plan_id)
        db.session.delete(SmokeResistance)

# 煤气发电 烟风系统
class GPGFlueGasAirSystem(db.Model):
     # 表名
    __tablename__ = 'gaspowergeneration_gas_air_system'
    __table_args__ = {'comment': u'煤气发电烟风系统表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    '''工况--标况'''
    # 工况温度-风
    c2s_condition_temperature_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 工况流量-风
    c2s_condition_flux_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 当地大气压-风
    c2s_local_atmosphere_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 标况温度-风
    c2s_standard_temperature_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 标况压力-风
    c2s_standard_pressure_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 标况流量-风
    c2s_standard_flux_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    # 工况温度-烟
    c2s_condition_temperature_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 工况流量-烟
    c2s_condition_flux_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 当地大气压-烟
    c2s_local_atmosphere_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 标况温度-烟
    c2s_standard_temperature_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 标况压力-烟
    c2s_standard_pressure_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 标况流量-烟
    c2s_standard_flux_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    '''标况--工况'''
    # 标况温度-风
    s2c_standard_temperature_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况温度-风")
    # 标况压力-风
    s2c_standard_pressure_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况压力-风")
    # 标况流量-风
    s2c_standard_flux_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况流量-风")
    # 工况温度-风
    s2c_condition_temperature_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：工况温度-风")
    # 当地大气压-风
    s2c_local_atmosphere_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：当地大气压-风")
    # 工况流量-风
    s2c_condition_flux_air = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：工况流量-风")

    # 标况温度-烟
    s2c_standard_temperature_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况温度-烟")
    # 标况压力-烟
    s2c_standard_pressure_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况压力-烟")
    # 标况流量-烟
    s2c_standard_flux_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况流量-烟")
    # 工况温度-烟
    s2c_condition_temperature_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：工况温度-烟")
    # 当地大气压-烟
    s2c_local_atmosphere_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：当地大气压-烟")
    # 工况流量-烟
    s2c_condition_flux_smoke = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：工况流量-烟")

    # 标况温度-煤气
    s2c_standard_temperature_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况温度-煤气")
    # 标况压力-煤气
    s2c_standard_pressure_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况压力-煤气")
    # 标况流量-煤气
    s2c_standard_flux_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：标况流量-煤气")
    # 工况温度-煤气
    s2c_condition_temperature_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：工况温度-煤气")
    # 当地大气压-煤气
    s2c_local_atmosphere_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：当地大气压-煤气")
    # 工况流量-煤气
    s2c_condition_flux_gas = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"标况-工况：工况流量-煤气")

    '''送风机'''
    # 空气温度
    blower_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：空气温度")
    # 风阻力
    blower_wind_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：风阻力")
    # 当地大气压
    blower_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：当地大气压")
    # 烟风流量（工况）
    blower_condition_smoke_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：烟风流量（工况）")
    # 风机温度
    blower_fan_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：风机温度")
    # 风机全压
    blower_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：风机全压")
    # 风机选用全压
    blower_fan_selected_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：风机选用全压")
    # 风机选用流量
    blower_fan_selected_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：风机选用流量")
    # 风机全压头效率
    blower_fan_pressure_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：风机全压头效率")
    # 机械传动效率
    blower_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：机械传动效率")
    # 电动机效率
    blower_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：电动机效率")
    # 风机轴功率
    blower_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：风机轴功率")
    # 电机安全裕量
    blower_motor_safe_margin = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：电机安全裕量")
    # 电机功率
    blower_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"送风机：电机功率")
    # 选用规格功率
    blower_specification_power = db.Column(db.Text(), comment=u"送风机：选用规格-功率")
    # 选用规格流量
    blower_specification_flux = db.Column(db.Text(), comment=u"送风机：选用规格-流量")

    '''引风机'''
    # 烟风温度
    induced_smoke_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：烟风温度")
    # 全压
    induced_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：全压")
    # 当地大气压
    induced_local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：当地大气压")
    # 烟风流量（工况）
    induced_condition_smoke_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：烟风流量（工况）")
    # 风机温度
    induced_fan_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：风机温度")
    # 烟气密度
    induced_smoke_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：烟气密度")
    # 风机全压
    induced_fan_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：风机全压")
    # 风机选用全压
    induced_fan_selected_total_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：风机选用全压")
    # 风机选用流量
    induced_fan_selected_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：风机选用流量")
    # 风机效率
    induced_fan_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：风机效率")
    # 机械传动效率
    induced_transmission_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：机械传动效率")
    # 电动机效率
    induced_motor_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：电动机效率")
    # 风机轴功率
    induced_fan_shaft_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：风机轴功率")
    # 电机安全裕量
    induced_motor_safe_margin = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：电机安全裕量")
    # 电机功率
    induced_motor_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"引风机：电机功率")
    # 选用规格功率
    induced_specification_power = db.Column(db.Text(), comment=u"引风机：选用规格功率")
    # 选用规格流量
    induced_specification_flux = db.Column(db.Text(), comment=u"引风机：选用规格流量")

    '''煤气总管道计算'''
    # 介质流量
    gas_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤气总管道：介质流量")
    # 介质温度
    gas_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤气总管道：介质温度")
    # 流速
    gas_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤气总管道：流速")
    # 计算截面积
    gas_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤气总管道：计算截面积")
    # 计算管道直径
    gas_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤气总管道：计算管道直径")
    # 选取直径
    gas_tube_selected_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤气总管道：选取直径")
    # 选取壁厚
    gas_tube_selected_thickness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"煤气总管道：选取壁厚")

    '''冷风管道计算'''
    # 介质流量
    coldwind_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风管道：介质流量")
    # 介质温度
    coldwind_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风管道：介质温度")
    # 流速
    coldwind_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风管道：流速")
    # 计算截面积
    coldwind_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风管道：计算截面积")
    # 计算当量管道直径
    coldwind_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风管道：计算当量管道直径")
    # 长
    coldwind_tube_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风管道：长")
    # 宽
    coldwind_tube_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"冷风管道：宽")
    # 选用规格
    coldwind_tube_specification = db.Column(db.Text(), comment=u"冷风管道：选用规格")

    '''热风管道计算-空预器出口方管'''
    # 介质流量
    hotwind_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-空预器出口方管：介质流量")
    # 介质温度
    hotwind_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-空预器出口方管：介质温度")
    # 流速
    hotwind_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-空预器出口方管：流速")
    # 计算截面积
    hotwind_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-空预器出口方管：计算截面积")
    # 计算当量管道直径
    hotwind_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-空预器出口方管：计算当量管道直径")
    # 长
    hotwind_tube_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-空预器出口方管：长")
    # 宽
    hotwind_tube_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-空预器出口方管：宽")
    # 选用规格
    hotwind_tube_specification = db.Column(db.Text(), comment=u"热风管道-空预器出口方管：选用规格")

    '''烟管道计算-总'''
    # 介质流量
    total_smoke_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-总：介质流量")
    # 介质温度
    total_smoke_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-总：介质温度")
    # 流速
    total_smoke_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-总：流速")
    # 计算截面积
    total_smoke_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-总：计算截面积")
    # 计算当量管道直径
    total_smoke_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-总：计算当量管道直径")
    # 长
    total_smoke_tube_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-总：长")
    # 宽
    total_smoke_tube_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-总：宽")
    # 选用规格
    total_smoke_tube_specification = db.Column(db.Text(), comment=u"烟管道-总：选用规格")

    '''烟管道计算-支'''
    # 介质流量
    branch_smoke_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-支：介质流量")
    # 介质温度
    branch_smoke_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-支：介质温度")
    # 流速
    branch_smoke_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-支：流速")
    # 计算截面积
    branch_smoke_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-支：计算截面积")
    # 计算当量管道直径
    branch_smoke_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-支：计算当量管道直径")
    # 长
    branch_smoke_tube_length = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-支：长")
    # 宽
    branch_smoke_tube_width = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟管道-支：宽")
    # 选用规格
    branch_smoke_tube_specification = db.Column(db.Text(), comment=u"烟管道-支：选用规格")

    '''热风管道计算-母管'''
    # 介质流量
    main_hotwind_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-母管：介质流量")
    # 介质温度
    main_hotwind_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-母管：介质温度")
    # 流速
    main_hotwind_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-母管：流速")
    # 计算截面积
    main_hotwind_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-母管：计算截面积")
    # 计算管道直径
    main_hotwind_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-母管：计算管道直径")
    # 选取直径
    main_hotwind_tube_selected_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-母管：选取直径")
    # 选取壁厚
    main_hotwind_tube_selected_thickness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-母管：选取壁厚")

    '''热风管道计算-入口支管'''
    # 介质流量
    branch_hotwind_tube_medium_flux = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-入口支管：介质流量")
    # 介质温度
    branch_hotwind_tube_medium_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-入口支管：介质温度")
    # 流速
    branch_hotwind_tube_flow_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-入口支管：流速")
    # 计算截面积
    branch_hotwind_tube_calculated_cross_sectional_area = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-入口支管：计算截面积")
    # 计算管道直径
    branch_hotwind_tube_calculated_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-入口支管：计算管道直径")
    # 选取直径
    branch_hotwind_tube_selected_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-入口支管：选取直径")
    # 选取壁厚
    branch_hotwind_tube_selected_thickness = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"热风管道-入口支管：选取壁厚")

    '''烟囱抽力计算'''
    # 烟囱高度
    chimney_height = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：烟囱高度")
    # 当地大气压
    local_atmosphere = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：当地大气压")
    # 标态下空气密度
    standard_air_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：标态下空气密度")
    # 标态下平均烟气密度
    standard_average_smoke_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：标态下平均烟气密度")
    # 标态下计算烟气密度
    standard_calculated_smoke_density = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：标态下计算烟气密度")
    # 室外空气温度
    outdoor_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：室外空气温度")
    # 烟囱进口处烟温
    chimney_inlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：烟囱进口处烟温")
    # 烟囱每米高度的温度降
    chimney_temperature_drop_per_meter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：烟囱每米高度的温度降")
    # 烟囱内平均温度
    chimney_average_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱：烟囱内平均温度")
    # 烟囱抽力
    chimney_draft = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱抽力")

    '''烟囱出口内径计算及低负荷校核'''
    # 烟气量
    smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟气量")
    # 烟囱出口温度
    chimney_outlet_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口温度")
    # 烟囱出口流速
    chimney_outlet_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口流速")
    # 烟囱出口内径
    chimney_outlet_inner_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口内径")
    # 选取烟囱出口内径
    chimney_outlet_selected_inner_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"选取烟囱出口内径")
    # 经验烟囱基础内径
    chimney_experience_base_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"经验烟囱基础内径")
    # 低负荷下烟气量
    low_load_smoke_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低负荷下烟气量")
    # 低负荷下排烟温度
    low_load_smoke_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"低负荷下排烟温度")
    # 30%低负荷校核流速
    low_load_flow_30_percent = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"30%低负荷校核流速")

    '''烟囱阻力计算'''
    # 烟囱阻力系数
    chimney_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱阻力系数")
    # 烟囱内平均流速
    chimney_average_velocity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱内平均流速")
    # 烟囱平均直径
    chimney_average_diameter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱平均直径")
    # 烟囱摩擦阻力
    chimney_friction_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱摩擦阻力")
    # 烟囱出口阻力系数
    chimney_outlet_resistance_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口阻力系数")
    # 烟囱出口阻力
    chimney_outlet_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱出口阻力")
    # 烟囱总阻力
    chimney_total_resistance = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烟囱总阻力")

    def __init__(self, **kwargs):
        super(GPGFlueGasAirSystem, self).__init__(**kwargs)

    @staticmethod
    def insert_FlueGasAirSystem(gaspowergeneration_gas_air_system):
        try:
            db.session.add(gaspowergeneration_gas_air_system)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_gas_air_system"
                  "<id=%s> in database" % (gaspowergeneration_gas_air_system.id))

    # 根据plan id查找实体
    @staticmethod
    def search_FlueGasAirSystem(planId):
        result = GPGFlueGasAirSystem.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_FlueGasAirSystem(plan_id):
        FlueGasAirSystem = GPGFlueGasAirSystem.search_FlueGasAirSystem(plan_id)
        try:
            db.session.delete(FlueGasAirSystem)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete FlueGasAirSystem<id=%s, plan_id=%s> in database" %
                  (FlueGasAirSystem.id, FlueGasAirSystem.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        FlueGasAirSystem = GPGFlueGasAirSystem.search_FlueGasAirSystem(plan_id)
        db.session.delete(FlueGasAirSystem)


# 煤气发电 原则性热力系统锅炉部分 (boiler of Principle Thermodynamic System)
class GPGBoilerOfPTS(db.Model):
     # 表名
    __tablename__ = 'gaspowergeneration_boiler_of_pts'
    __table_args__ = {'comment': u'煤气发电锅炉计算表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 富余的煤气流量_BFG
    surplus_gas_bfg = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_BFG")

    # 富余的煤气流量_LDG
    surplus_gas_ldg = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_LDG")

    # 富余的煤气流量_COG
    surplus_gas_cog = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_COG")

    # BFG煤气热值
    bfg_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气热值")

    # LDG煤气热值
    ldg_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气热值")

    # COG煤气热值
    cog_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气热值")

    # 锅炉热效率
    boiler_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉热效率")

    # 过热蒸汽出口压力
    superheated_steam_outlet_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽出口压力")

    # 过热蒸汽温度
    superheated_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽温度")

    # 过热蒸汽焓值
    superheated_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过热蒸汽焓值")

    # 过量空气系数
    excess_air_coefficient = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"过量空气系数")

    # 空气温度
    air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气温度")

    # 空气焓值
    air_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"空气焓值")

    # 燃烧所需空气量
    air_need_for_combustion = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"燃烧所需空气量")

    # 锅炉给水温度
    boiler_feed_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉给水温度")

    # 给水焓值
    feedwater_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"给水焓值")

    # 排污率
    rate_of_blowdown = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"排污率")

    # 饱和水温度
    saturation_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"饱和水温度")

    # 饱和水焓值
    saturation_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"饱和水焓值")

    # 产汽量
    steam_output = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"产汽量")

    def __init__(self, **kwargs):
        super(GPGBoilerOfPTS, self).__init__(**kwargs)

    @staticmethod
    def insert_BoilerOfPTS(gaspowergeneration_boiler_of_pts):
        try:
            db.session.add(gaspowergeneration_boiler_of_pts)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_boiler_of_pts"
                  "<id=%s> in database" % (gaspowergeneration_boiler_of_pts.id))

    # 根据plan id查找实体
    @staticmethod
    def search_BoilerOfPTS(planId):
        result = GPGBoilerOfPTS.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_BoilerOfPTS(plan_id):
        BoilerOfPTS = GPGBoilerOfPTS.search_BoilerOfPTS(plan_id)
        try:
            db.session.delete(BoilerOfPTS)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete BoilerOfPTS<id=%s, plan_id=%s> in database" %
                  (BoilerOfPTS.id, BoilerOfPTS.plan_id))
    
    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        BoilerOfPTS = GPGBoilerOfPTS.search_BoilerOfPTS(plan_id)
        db.session.delete(BoilerOfPTS)


# 煤气发电 原则性热力系统汽轮机部分
class GPGTurbineOfPTS(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_turbine_of_pts'
    __table_args__ = {'comment': u'煤气发电汽轮机计算表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 参数
    # 是否已经输入参数
    s_parameter_flg = db.Column(db.String(50))
    # 汽轮机类型
    s_steam_type_test = db.Column(db.Integer)
    # 除氧器温度和压力
    s_temperature_pressure = db.Column(db.String(50), comment=u"除氧器温度和压力")
    # 高加级数
    s_hh_grade = db.Column(db.Integer, comment=u"高加级数")
    # 低加级数
    s_lh_grade = db.Column(db.Integer, comment=u"低加级数")

    # 发电功率估算
    # 汽轮机内效率
    e_turbine_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：汽轮机内效率")
    # 机械效率
    e_mechanical_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：机械效率")
    # 发电机效率
    e_generator_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：发电机效率")
    # 汽轮机机组型式
    e_steam_type = db.Column(db.String(50), comment=u"发电功率估算：汽轮机机组型式")
    # 主蒸汽  压力
    e_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-压力")
    # 温度
    e_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-温度")
    # 流量
    e_steam_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-流量")
    # 熵
    e_steam_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-熵")
    # 焓
    e_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：主蒸汽-焓")
    # 抽汽点  压力
    e_exhaust_point_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-压力")
    # 温度
    e_exhaust_point_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-温度")
    # 熵
    e_exhaust_point_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-熵")
    # 焓
    e_exhaust_point_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-焓")
    # 流量
    e_exhaust_point_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽点-流量")
    # 抽汽后蒸汽量
    e_exhaust_after_steam = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后蒸汽量")
    # 压力
    e_exhaust_after_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后压力")
    # 焓
    e_exhaust_after_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后焓")
    # 熵
    e_exhaust_after_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：抽汽后熵")
    # 乏汽  压力
    e_steam_exhaust_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：乏汽-压力")
    # 焓
    e_steam_exhaust_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：乏汽-焓")

    # 背压  压力
    e_backpressure_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-压力")
    # 背压  温度
    e_backpressure_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-温度")
    # 焓
    e_backpressure_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-焓")
    # 流量
    e_backpressure_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：背压-流量")

    # 追加补汽焓（补凝场合）
    e_steam_plus_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"补汽焓")

    # 总发电量
    e_gross_generation = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：总发电量")
    # 回热抽汽经验数据
    e_hot_data = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：回热抽汽经验数据")
    # 去除抽汽后
    e_steam_extraction = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：去除抽汽后")
    # 选定
    e_steam_extraction_select = db.Column(db.Text(), comment=u"发电功率估算：选定")
    # 全厂汽水损失
    e_steam_water_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：全厂汽水损失")
    # 进汽量
    e_throttle_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"发电功率估算：进汽量")


    # 汽轮机回热系统计算
    # 假设
    h_assume = db.Column(db.String(100), comment=u"汽轮机回热系统-假设")
    # 温度
    h_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-温度")
    # 压力
    h_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-压力")
    # 焓值
    h_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-焓值")
    # 量
    h_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"汽轮机回热系统-量")

    # HH1
    # 给水出水温度
    hh1_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-给水出水温度")
    # 给水出口焓
    hh1_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-给水出口焓")
    # 上端差
    hh1_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-上端差")
    # 饱和水温度
    hh1_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-饱和水温度")
    # 饱和水焓
    hh1_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-饱和水焓")
    # 工作压力
    hh1_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-工作压力")
    # 抽汽管压损
    hh1_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽管压损")
    # 抽汽压力
    hh1_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽压力")
    # 抽汽焓
    hh1_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽焓")
    # 抽汽量
    hh1_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH1-抽汽量")
    
    # HH2
    # 给水出水温度
    hh2_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-给水出水温度")
    # 给水出口焓
    hh2_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-给水出口焓")
    # 上端差
    hh2_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-上端差")
    # 饱和水温度
    hh2_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-饱和水温度")
    # 饱和水焓
    hh2_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-饱和水焓")
    # 工作压力
    hh2_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-工作压力")
    # 抽汽管压损
    hh2_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽管压损")
    # 抽汽压力
    hh2_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽压力")
    # 抽汽焓
    hh2_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽焓")
    # 抽汽量
    hh2_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH2-抽汽量")

    # HH3
    # 给水出水温度
    hh3_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-给水出水温度")
    # 给水出口焓
    hh3_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-给水出口焓")
    # 上端差
    hh3_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-上端差")
    # 饱和水温度
    hh3_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-饱和水温度")
    # 饱和水焓
    hh3_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-饱和水焓")
    # 工作压力
    hh3_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-工作压力")
    # 抽汽管压损
    hh3_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽管压损")
    # 抽汽压力
    hh3_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽压力")
    # 抽汽焓
    hh3_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽焓")
    # 抽汽量
    hh3_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"HH3-抽汽量")

    # D
    # 给水出水温度
    d_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-给水出水温度")
    # 给水出口焓
    d_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-给水出口焓")
    # 工作压力
    d_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-工作压力")
    # 抽汽管压损
    d_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽管压损")
    # 抽汽压力
    d_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽压力")
    # 抽汽焓
    d_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽焓")
    # 抽汽量
    d_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"D-抽汽量")

    # LH1
    # 给水出水温度
    lh1_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-给水出水温度")
    # 给水出口焓
    lh1_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-给水出口焓")
    # 上端差
    lh1_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-上端差")
    # 饱和水温度
    lh1_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-饱和水温度")
    # 饱和水焓
    lh1_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-饱和水焓")
    # 工作压力
    lh1_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-工作压力")
    # 抽汽管压损
    lh1_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽管压损")
    # 抽汽压力
    lh1_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽压力")
    # 抽汽焓
    lh1_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽焓")
    # 抽汽量
    lh1_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH1-抽汽量")

    # LH2
    # 给水出水温度
    lh2_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-给水出水温度")
    # 给水出口焓
    lh2_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-给水出口焓")
    # 上端差
    lh2_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-上端差")
    # 饱和水温度
    lh2_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-饱和水温度")
    # 饱和水焓
    lh2_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-饱和水焓")
    # 工作压力
    lh2_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-工作压力")
    # 抽汽管压损
    lh2_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽管压损")
    # 抽汽压力
    lh2_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽压力")
    # 抽汽焓
    lh2_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽焓")
    # 抽汽量
    lh2_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH2-抽汽量")

    # LH3
    # 给水出水温度
    lh3_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-给水出水温度")
    # 给水出口焓
    lh3_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-给水出口焓")
    # 上端差
    lh3_top_difference = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-上端差")
    # 饱和水温度
    lh3_saturated_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-饱和水温度")
    # 饱和水焓
    lh3_saturated_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-饱和水焓")
    # 工作压力
    lh3_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-工作压力")
    # 抽汽管压损
    lh3_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽管压损")
    # 抽汽压力
    lh3_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽压力")
    # 抽汽焓
    lh3_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽焓")
    # 抽汽量
    lh3_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LH3-抽汽量")

    # C
    # 给水出水温度
    c_water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-给水出水温度")
    # 给水出口焓
    c_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-给水出口焓")
    # 工作压力
    c_work_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-工作压力")
    # 抽汽管压损
    c_pressure_loss = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽管压损")
    # 抽汽压力
    c_extraction_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽压力")
    # 抽汽焓
    c_extraction_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽焓")
    # 抽汽量
    c_extraction_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"C-抽汽量")

    # 组内功率计算及校核
    # 汽轮机内效率
    i_turbine_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：汽轮机内效率")
    # 机械效率
    i_mechanical_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：机械效率")
    # 发电机效率
    i_generator_efficiency = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：发电机效率")
    # 主蒸汽  压力
    i_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-压力")
    # 温度
    i_steam_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-温度")
    # 流量
    i_steam_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-流量")
    # 熵
    i_steam_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-熵")
    # 焓
    i_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主蒸汽-焓")
    # 1#高压  压力
    i_high1_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-压力")
    # 熵
    i_high1_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-熵")
    # 温度
    i_high1_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-温度")
    # 焓
    i_high1_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-焓")
    # 流量
    i_high1_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#高压-流量")
    # 主汽至HH1功率
    i_steam_hh1_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：主汽至HH1功率")
    # 2#高压  压力
    i_high2_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-压力")
    # 熵
    i_high2_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-熵")
    # 温度
    i_high2_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-温度")
    # 焓
    i_high2_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-焓")
    # 流量
    i_high2_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#高压-流量")
    # HH1至HH2功率
    i_hh1_hh2_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：HH1至HH2功率")
    # D除氧  压力
    i_deoxidize_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-压力")
    # 熵
    i_deoxidize_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-熵")
    # 温度
    i_deoxidize_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-温度")
    # 焓
    i_deoxidize_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-焓")
    # 流量
    i_deoxidize_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D除氧-流量")
    # HH2至D功率
    i_hh2_deoxidize_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：HH2至D功率")
    # 抽汽点  压力
    i_exhaust_point_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-压力")
    # 温度
    i_exhaust_point_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-温度")
    # 熵
    i_exhaust_point_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-熵")
    # 焓
    i_exhaust_point_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-焓")
    # 流量
    i_exhaust_point_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽点-流量")
    # D至抽汽功率
    i_deoxidize_exhaust_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：D至抽汽功率")
    # 1#低加  压力
    i_low1_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-压力")
    # 熵
    i_low1_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-熵")
    # 温度
    i_low1_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-温度")
    # 焓
    i_low1_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-焓")
    # 流量
    i_low1_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：1#低加-流量")
    # 抽汽至LH1功率
    i_exhaust_lh1_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：抽汽至LH1功率")
    # 2#低加  压力
    i_low2_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-压力")
    # 熵
    i_low2_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-熵")
    # 温度
    i_low2_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-温度")
    # 焓
    i_low2_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-焓")
    # 流量
    i_low2_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：2#低加-流量")
    # LH1至LH2功率
    i_lh1_lh2_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH1至LH2功率")
	# 3#低加  压力
    i_low3_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-压力")
    # 熵
    i_low3_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-熵")
    # 温度
    i_low3_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-温度")
    # 焓
    i_low3_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-焓")
    # 流量
    i_low3_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：3#低加-流量")
    # LH2至LH3功率
    i_lh2_lh3_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH2至LH3功率")

    # 乏汽/背压   压力
    i_steam_exhaust_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-压力")
    # 熵
    i_steam_exhaust_entropy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-熵")
    # 焓
    i_steam_exhaust_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-焓")
    # 实际焓
    i_steam_exhaust_enthalpy_actual = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-实际焓")
    # 饱和蒸汽焓
    i_steam_exhaust_enthalpy_steam = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-饱和蒸汽焓")
    # 饱和水焓
    i_steam_exhaust_enthalpy_water = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-饱和水焓")
    # 干度
    i_steam_exhaust_dry = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-干度")
    # 流量
    i_steam_exhaust_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：乏汽/背压-流量")
    # LH2至乏汽功率
    i_lh2_steam_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：LH2至乏汽功率")
    # 总功率
    i_total_power = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：总功率")
    # 抽汽点为0的总功率
    i_total_power0 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 计算误差
    i_calculation_error = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"组内功率计算及校核：计算误差")
    # 锅炉排污率
    h_blowdown_rate = db.Column(db.NUMERIC(precision=15, scale=5))   

    def __init__(self, **kwargs):
        super(GPGTurbineOfPTS, self).__init__(**kwargs)

    @staticmethod
    def insert_TurbineOfPTS(gaspowergeneration_turbine_of_pts):
        try:
            db.session.add(gaspowergeneration_turbine_of_pts)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gaspowergeneration_turbine_of_pts"
                  "<id=%s> in database" % (gaspowergeneration_turbine_of_pts.id))

    # 根据plan id查找实体
    @staticmethod
    def search_TurbineOfPTS(planId):
        result = GPGTurbineOfPTS.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_TurbineOfPTS(plan_id):
        TurbineOfPTS = GPGTurbineOfPTS.search_TurbineOfPTS(plan_id)
        try:
            db.session.delete(TurbineOfPTS)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete TurbineOfPTS<id=%s, plan_id=%s> in database" %
                  (TurbineOfPTS.id, TurbineOfPTS.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        TurbineOfPTS = GPGTurbineOfPTS.search_TurbineOfPTS(plan_id)
        db.session.delete(TurbineOfPTS)


# 煤气发电需求调查表
class GasPowerGenerationNeedsQuestionnaire(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_needsquestionnaire'
    __table_args__ = {'comment': u'煤气发电需求调查表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 方案表外键
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 富余的煤气流量_BFG 额定
    surplus_gas_bfg = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_BFG 额定")
    # 富余的煤气流量_BFG 最大
    surplus_gas_bfg_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_BFG 最大")
    # 富余的煤气流量_BFG 最小
    surplus_gas_bfg_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_BFG 最小")

    # 富余的煤气流量_LDG 额定
    surplus_gas_ldg = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_LDG 额定")
    # 富余的煤气流量_LDG 最大
    surplus_gas_ldg_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_LDG 最大")
    # 富余的煤气流量_LDG 最小
    surplus_gas_ldg_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_LDG 最小")

    # 富余的煤气流量_COG 额定
    surplus_gas_cog = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_COG 额定")
    # 富余的煤气流量_COG 最大
    surplus_gas_cog_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_COG 最大")
    # 富余的煤气流量_COG 最小
    surplus_gas_cog_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"富余的煤气流量_COG 最小")

    # BFG煤气温度 额定
    bfg_gas_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气温度 额定")
    # BFG煤气温度 最大
    bfg_gas_temperature_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气温度 最大")
    # BFG煤气温度 最小
    bfg_gas_temperature_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气温度 最小")

    # LDG煤气温度 额定
    ldg_gas_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气温度 额定")
    # LDG煤气温度 最大
    ldg_gas_temperature_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气温度 最大")
    # LDG煤气温度 最小
    ldg_gas_temperature_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气温度 最小")

    # COG煤气温度 额定
    cog_gas_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气温度 额定")
    # COG煤气温度 最大
    cog_gas_temperature_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气温度 最大")
    # COG煤气温度 最小
    cog_gas_temperature_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气温度 最小")

    # BFG煤气压力 额定
    bfg_gas_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气压力 额定")
    # BFG煤气压力 最大
    bfg_gas_pressure_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气压力 最大")
    # BFG煤气压力 最小
    bfg_gas_pressure_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气压力 最小")   

    # LDG煤气压力 额定
    ldg_gas_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气压力 额定")
    # LDG煤气压力 最大
    ldg_gas_pressure_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气压力 最大")
    # LDG煤气压力 最小
    ldg_gas_pressure_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气压力 最小")

    # COG煤气压力 额定
    cog_gas_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气压力 额定")
    # COG煤气压力 最大
    cog_gas_pressure_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气压力 最大")
    # COG煤气压力 最小
    cog_gas_pressure_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气压力 最小")

    # BFG煤气热值 额定
    bfg_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气热值 额定")
    # BFG煤气热值 最大
    bfg_gas_calorific_value_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气热值 最大")
    # BFG煤气热值 最小
    bfg_gas_calorific_value_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"BFG煤气热值 最小")

    # LDG煤气热值 额定
    ldg_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气热值 额定")
    # LDG煤气热值 最大
    ldg_gas_calorific_value_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气热值 最大")
    # LDG煤气热值 最小
    ldg_gas_calorific_value_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"LDG煤气热值 最小")

    # COG煤气热值 额定
    cog_gas_calorific_value = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气热值 额定")
    # COG煤气热值 最大
    cog_gas_calorific_value_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气热值 最大")
    # COG煤气热值 最小
    cog_gas_calorific_value_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"COG煤气热值 最小")

    # 对外供蒸汽量 额定
    provide_steam_amount = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"对外供蒸汽量 额定")
    # 对外供蒸汽量 最大
    provide_steam_amount_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"对外供蒸汽量 最大")
    # 对外供蒸汽量 最小
    provide_steam_amount_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"对外供蒸汽量 最小")

    # 对外供蒸汽压 额定
    provide_steam_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"对外供蒸汽压 额定")
    # 对外供蒸汽压 最大
    provide_steam_pressure_max = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"对外供蒸汽压 最大")
    # 对外供蒸汽压 最小
    provide_steam_pressure_min = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"对外供蒸汽压 最小")

    # 高炉煤气·含量 H2
    furnace_h2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 H2")
    # 高炉煤气·含量 CO
    furnace_co_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 CO")
    # 高炉煤气·含量 CH4
    furnace_ch4_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 CH4")
    # 高炉煤气·含量 C2H4
    furnace_c2h4_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 高炉煤气·含量 C3H8
    furnace_c3h8_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 高炉煤气·含量 C4H10
    furnace_c4h10_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 高炉煤气·含量 N2
    furnace_n2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 N2")
    # 高炉煤气·含量 O2
    furnace_o2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 O2")
    # 高炉煤气·含量 CO2
    furnace_co2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 CO2")
    # 高炉煤气·含量 H2S
    furnace_h2s_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 H2S")
    # 高炉煤气·含量 CmHn
    furnace_cmhn_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 CmHn")
    # 高炉煤气·含量 H2O
    furnace_h2o_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·含量 H2O")
    # 高炉煤气·含量 SO2
    furnace_so2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 高炉煤气·含量 低位发热量
    furnace_low_heating = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·低位发热量 ")
    # 高炉煤气·含量 高位发热量
    furnace_high_heating = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"高炉煤气·高位发热量 ")

    # 转炉煤气·含量 H2
    converter_h2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 H2")
    # 转炉煤气·含量 CO
    converter_co_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 CO")
    # 转炉煤气·含量 CH4
    converter_ch4_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 CH4")
    # 转炉煤气·含量 C2H4
    converter_c2h4_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 转炉煤气·含量 C3H8
    converter_c3h8_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 转炉煤气·含量 C4H10
    converter_c4h10_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 转炉煤气·含量 N2
    converter_n2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 N2")
    # 转炉煤气·含量 O2
    converter_o2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 O2")
    # 转炉煤气·含量 CO2
    converter_co2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 CO2")
    # 转炉煤气·含量 H2S
    converter_h2s_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 H2S")
    # 转炉煤气·含量 CmHn
    converter_cmhn_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 CmHn")
    # 转炉煤气·含量 H2O
    converter_h2o_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·含量 H2O")
    # 转炉煤气·含量 SO2
    converter_so2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 转炉煤气·含量 低位发热量
    converter_low_heating = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·低位发热量 ")
    # 转炉煤气·含量 高位发热量
    converter_high_heating = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉煤气·高位发热量 ")

    # 焦炉煤气·含量 H2
    coke_h2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 H2")
    # 焦炉煤气·含量 CO
    coke_co_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 CO")
    # 焦炉煤气·含量 CH4
    coke_ch4_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 CH4")
    # 焦炉煤气·含量 C2H4
    coke_c2h4_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 焦炉煤气·含量 C3H8
    coke_c3h8_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 焦炉煤气·含量 C4H10
    coke_c4h10_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 焦炉煤气·含量 N2
    coke_n2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 N2")
    # 焦炉煤气·含量 O2
    coke_o2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 O2")
    # 焦炉煤气·含量 CO2
    coke_co2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 CO2")
    # 焦炉煤气·含量 H2S
    coke_h2s_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 H2S")
    # 焦炉煤气·含量 CmHn
    coke_cmhn_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 CmHn")
    # 焦炉煤气·含量 H2O
    coke_h2o_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·含量 H2O")
    # 焦炉煤气·含量 SO2
    coke_so2_content = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    # 焦炉煤气·含量 低位发热量
    coke_low_heating = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·低位发热量 ")
    # 焦炉煤气·含量 高位发热量
    coke_high_heating = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"焦炉煤气·高位发热量 ")

    # 大气温度
    atmosphere_temperature_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    atmosphere_temperature_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    atmosphere_temperature_a = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气温度：年平均")
    atmosphere_temperature_a_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气温度：冬季平均")
    atmosphere_temperature_a_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气温度：夏季平均")
    atmosphere_temperature_a_cold = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气温度：最冷月平均")
    atmosphere_temperature_a_hot = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气温度：最热月平均")
    atmosphere_temperature_extreme_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气温度：年极端最高")
    atmosphere_temperature_extreme_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气温度：年极端最低")

    # 大气压力
    atmosphere_pressure_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")    
    atmosphere_pressure_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    atmosphere_pressure_a = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压力：年平均")
    atmosphere_pressure_a_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压力：冬季平均")
    atmosphere_pressure_a_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压力：夏季平均")
    atmosphere_pressure_a_cold = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压力：最冷月平均")
    atmosphere_pressure_a_hot = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压力：最热月平均")
    atmosphere_pressure_extreme_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压力：年极端最高")
    atmosphere_pressure_extreme_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"大气压力：年极端最低")

    # 相对湿度
    relative_humidity_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")    
    relative_humidity_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    relative_humidity_a = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"相对湿度：年平均")
    relative_humidity_a_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"相对湿度：冬季平均")
    relative_humidity_a_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"相对湿度：夏季平均")
    relative_humidity_a_cold = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"相对湿度：最冷月平均")
    relative_humidity_a_hot = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"相对湿度：最热月平均")
    relative_humidity_extreme_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"相对湿度：年极端最高")
    relative_humidity_extreme_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"相对湿度：年极端最低")

    # 室外风速
    outside_wind_speed_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    outside_wind_speed_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    outside_wind_speed_a = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"室外风速：年平均")
    outside_wind_speed_a_winter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"室外风速：冬季平均")
    outside_wind_speed_a_summer = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"室外风速：夏季平均")
    outside_wind_speed_a_cold = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"室外风速：最冷月平均")
    outside_wind_speed_a_hot = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"室外风速：最热月平均")
    outside_wind_speed_extreme_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"室外风速：年极端最高")
    outside_wind_speed_extreme_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"室外风速：年极端最低")

    # 抗震设防烈度
    seismic_fortification_intensity_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    seismic_fortification_intensity_a = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抗震设防烈度")
    seismic_fortification_intensity_l = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")
    seismic_fortification_intensity_extreme_h = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"")

    # 海拔高度
    above_sea_level = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"海拔高度")

    # 设计基本地震加速度
    design_earthquake_acceleration = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"设计基本地震加速度")

    # 水压力
    water_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"水压力")

    # 水温度
    water_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"水温度")

    # PH值
    water_ph = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"PH值")

    # 悬浮物
    water_suspended_matter = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"悬浮物")

    # 氯离子
    water_cl = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氯离子")

    # 氮气纯度
    nitrogen_purity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氮气纯度")

    # 氮气压力范围
    nitrogen_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氮气压力范围")

    # 氮气温度
    nitrogen_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"氮气温度")

    # 压缩空气压力范围
    compressed_air_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"压缩空气压力范围")

    # 压缩空气温度
    compressed_air_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"压缩空气温度")

    # 并网电压
    grid_voltage = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"并网电压")

    # 最大短路容量
    max_short_circuit_capacity = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"最大短路容量")

    # 电压其他
    voltage_other = db.Column(db.Text(), comment=u"电压其他")

    # 拟建厂区坐标点和高程的地形图
    factory_location_elevation = db.Column(db.Text())

    # 能源介质接点位置、标高、管径、路由
    dielectric_position_height_caliber_route = db.Column(db.Text())

    # 全水质分析报告
    water_quality_analysis_report = db.Column(db.Text())

    # 冷却方式及冷却塔形式	
    cooling_tower = db.Column(db.Text())

    # 项目立项及环评手续
    project_approval_eia = db.Column(db.Boolean, default=False)

    #转炉流量
    converter_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉流量")
    #转炉压力
    converter_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉压力")
    #转炉温度
    converter_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"转炉温度")

    #烧结余热回收流量
    heat_recovery_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烧结余热回收流量")
    #烧结余热回收压力
    heat_recovery_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烧结余热回收压力")
    #烧结余热回收温度
    heat_recovery_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"烧结余热回收温度")

    #加热炉流量
    furnace_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"加热炉流量")
    #加热炉压力
    furnace_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"加热炉压力")
    #加热炉温度
    furnace_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"加热炉温度")

    #其他流量
    steam_other_flow = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"其他流量")
    #其他压力
    steam_other_pressure = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"其他压力")
    #其他温度
    steam_other_temperature = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"其他温度")

    def __init__(self, **kwargs):
        super(GasPowerGenerationNeedsQuestionnaire, self).__init__(**kwargs)

    @staticmethod
    def insert_questionnaire(gasPowerGenerationNeedsQuestionnaire):
        try:
            db.session.add(gasPowerGenerationNeedsQuestionnaire)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update gasPowerGenerationNeedsQuestionnaire"
                  "<id=%s> in database" % (gasPowerGenerationNeedsQuestionnaire.id))

    # 根据Plan id查找实体
    @staticmethod
    def search_questionnaire(planId):
        result = GasPowerGenerationNeedsQuestionnaire.query.filter_by(plan_id=planId).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_questionnaire(plan_id):
        questionnaire = GasPowerGenerationNeedsQuestionnaire.search_questionnaire(plan_id)
        try:
            db.session.delete(questionnaire)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete questionnaire<id=%s, plan_id=%s> in database" %
                  (questionnaire.id, questionnaire.plan_id))

    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        questionnaire = GasPowerGenerationNeedsQuestionnaire.search_questionnaire(plan_id)
        db.session.delete(questionnaire)


# 主要技术经济指标
class GasPowerGenerationEconomicIndicators(db.Model):
    # 表名
    __tablename__ = 'gaspowergeneration_economic_indicators'
    __table_args__ = {'comment': u'煤气发电主要技术经济指标表'}

    # 表ID,自动生成（主键）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    # 方案ID(外键)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'))

    # 凝结水回水压力
    condensate_backwater_pressure  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回水压力")
    # 凝结水回水温度
    condensate_backwater_temperature  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回水温度")
    # 凝结水回水焓值
    condensate_backwater_enthalpy  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"凝结水回水焓值")

    # 抽凝工况热耗率
    smoke_heat_consumption_rate  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况热耗率")
    # 纯凝工况热耗率
    heat_consumption_rate  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况热耗率")
    # 抽凝工况汽耗率
    smoke_steam_consumption_rate  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况汽耗率")
    # 纯凝工况汽耗率
    steam_consumption_rate  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况汽耗率")
    # 机组年利用小时数
    annual_useage_hours  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机组年利用小时数")
    # 机组年供热小时数
    annual_heat_hours  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"机组年供热小时数")
    # 年供热量
    annual_heat_supply  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年供热量")
    # 年发电量
    annual_power_generation  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年发电量")
    # 厂用电率
    plant_electricity_consumption   = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"厂用电率")
    # 年供电量
    annual_power_supply  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"年供电量")
    # 锅炉效率
    boiler_efficiency   = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"锅炉效率")
    # 管道效率
    pipeline_efficiency   = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"管道效率")
    # 抽凝工况发电标煤耗率
    smoke_power_coal_consumption  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况发电标煤耗率")
    # 纯凝工况发电标煤耗率
    power_coal_consumption  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况发电标煤耗率")
    # 抽凝工况供电标煤耗率
    smoke_supply_coal_consumption  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况供电标煤耗率")
    # 纯凝工况供电标煤耗率
    supply_coal_consumption  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况供电标煤耗率")
    # 全年平均热电比
    annual_average_thermoelectric_ratio  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"全年平均热电比")
    # 抽凝工况全厂热效率
    smoke_heat_efficiency  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"抽凝工况全厂热效率")
    # 纯凝工况全厂热效率
    heat_efficiency  = db.Column(db.NUMERIC(precision=15, scale=5), comment=u"纯凝工况全厂热效率")

    # hidden项
    # 汽轮机 主蒸汽焓F9
    t_steam_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 抽汽点焓F13
    t_point_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 抽汽点流量F15
    t_point_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 进汽量F26
    t_throttle_flow = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 总功率F95
    t_total_power = db.Column(db.NUMERIC(precision=15, scale=5))
    # 汽轮机 抽汽点为0的总功率F95
    t_total_power0 = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉 收到基低位发热量G14
    t_base_heat_received_user = db.Column(db.NUMERIC(precision=15, scale=5))
    # 锅炉 给水焓值G26
    t_water_enthalpy = db.Column(db.NUMERIC(precision=15, scale=5))
    # 燃料存储及输送 锅炉额定燃料耗量G3
    t_rated_fuel_consumption = db.Column(db.NUMERIC(precision=15, scale=5))


    def __init__(self, **kwargs):
        super(GasPowerGenerationEconomicIndicators, self).__init__(**kwargs)

    @staticmethod
    def insert_economic_indicators(GasPowerGenerationEconomicIndicators):
        try:
            db.session.add(GasPowerGenerationEconomicIndicators)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Insert/Update GasPowerGenerationEconomicIndicators"
                  "<id=%s> in database" % (GasPowerGenerationEconomicIndicators.id))

    # 根据plan_id查找实体
    @staticmethod
    def search_economic_indicators(plan_id):
        result = GasPowerGenerationEconomicIndicators.query.filter_by(
            plan_id=plan_id).one_or_none()
        return result

    # 根据plan_id删除实体
    @staticmethod
    def delete_economic_indicators(plan_id):
        economic_indicators = \
            GasPowerGenerationEconomicIndicators.search_economic_indicators(plan_id)
        try:
            db.session.delete(economic_indicators)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            print("Delete economic_indicators<id=%s, plan_id=%s> in database" %
                  (economic_indicators.id, economic_indicators.plan_id))
    
    # 根据plan_id删除实体
    @staticmethod
    def deletebyPlanId(plan_id):
        economic_indicators = \
            GasPowerGenerationEconomicIndicators.search_economic_indicators(plan_id)
        db.session.delete(economic_indicators)