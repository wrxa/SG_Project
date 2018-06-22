# -*- coding: utf-8 -*-
from base import CalculationObserver, ExecuteStrategy
from coalchp_furnace_calculation import FSteamEnthalpy, \
        FWaterEnthalpy, ASaturationPressure, FSaturatedWaterEnthalpy, \
        ASaturationPressureAfter, RAturatedwaterEnthalpy, \
        RLatentheatVaporization, CAturatedwaterEnthalpy, \
        CSteamPecificvolume, CLatentheatVaporization, \
        E_steam_entropy, \
        E_steam_enthalpy, \
        E_exhaust_point_temperature, \
        E_exhaust_point_enthalpy, \
        E_steam_exhaust_enthalpy, \
        E_backpressure_temperature, \
        E_backpressure_enthalpy, \
        I_steam_entropy, \
        I_steam_enthalpy, \
        I_high1_temperature, \
        I_high1_enthalpy, \
        I_high2_temperature, \
        I_high2_enthalpy, \
        I_deoxidize_temperature, \
        I_deoxidize_enthalpy, \
        I_low1_temperature, \
        I_low1_enthalpy, \
        I_low2_temperature, \
        I_low2_enthalpy, \
        I_steam_exhaust_enthalpy, \
        I_steam_exhaust_enthalpy_steam, \
        I_steam_exhaust_enthalpy_water, \
        H_enthalpy, \
        Hh1_saturated_water_enthalpy, \
        Hh1_work_pressure, \
        Hh1_extraction_enthalpy, \
        Hh2_saturated_water_enthalpy, \
        Hh2_work_pressure, \
        Hh2_extraction_enthalpy, \
        D_water_enthalpy, \
        D_extraction_enthalpy, \
        Lh1_saturated_water_enthalpy, \
        Lh1_work_pressure, \
        Lh1_extraction_enthalpy, \
        Lh2_saturated_water_enthalpy, \
        Lh2_work_pressure, \
        Lh2_extraction_enthalpy, \
        C_water_temperature, \
        C_water_enthalpy, \
        Hh3_saturated_water_enthalpy, \
        Hh3_work_pressure, \
        Hh3_extraction_enthalpy, \
        Lh3_saturated_water_enthalpy, \
        Lh3_work_pressure, \
        Lh3_extraction_enthalpy, \
        Hh1_water_enthalpy, \
        M_saturation_temperature, \
        M_condensate_enthalpy, \
        T_new_enthalpy, T_reduce_water_pressure, T_reduce_water_enthalpy,\
        T_reduce_water_flow_rate, T_rudece_flow_rate,\
        T_reduce_steam_enthalpy, T_reduce_enough_enthalpy,\
        S_local_atmosphere_value, S_local_atmosphere_density,\
        S_design_flux, S_pump_install_height, \
        Charging_saturation_water_enthalpy, Exothermic_saturation_water_enthalpy, \
        Charging_saturation_steam_enthalpy, Exothermic_saturation_steam_enthalpy, \
        P2_steam_amount, Charging_water_specific_volume, \
        Unit_water_heat_amount, Regenerarot_max_bleed, \
        Evaporation_capacity, Charging_volume, \
        Exothermic_water_specific_volume, Exothermic_water_volume, \
        Regenerarot_volume, Regenerarot_top_steam_volume


from app.biomass_chp.models.modelsBiomass import BiomassCHPBoilerCalculation


class Furnace_calculationBefore(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(FSteamEnthalpy())
        calculationObserver.register(FWaterEnthalpy())
        calculationObserver.register(ASaturationPressure())
        calculationObserver.register(FSaturatedWaterEnthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldobj, form):
        val = {'flg': 'design', 'f_steam_pressure': form.get('f_steam_pressure_design'), 'f_steam_temperature': form.get('f_steam_temperature_design'), 'f_water_temperature': form.get('f_water_temperature_design'), 'a_temperature': form.get('a_temperature_design'), 'f_boiler_pressure': form.get('f_boiler_pressure_design'), 'dbresult': oldobj}
        self.creatSubscriber(val)

        val = {'flg': 'check', 'f_steam_pressure': form.get('f_steam_pressure_check'), 'f_steam_temperature': form.get('f_steam_temperature_check'), 'f_water_temperature': form.get('f_water_temperature_check'), 'a_temperature': form.get('a_temperature_check'), 'f_boiler_pressure': form.get('f_boiler_pressure_check'), 'dbresult': oldobj}
        self.creatSubscriber(val)
        return val['dbresult']


class NeedsAfter(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(ASaturationPressureAfter())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, plan_id):
        furnace = BiomassCHPBoilerCalculation.query.filter_by(
            plan_id=plan_id).first()
        self.creatSubscriber(furnace)
        BiomassCHPBoilerCalculation.insert_furnace_calculation(furnace)


class Auxiliaries_calculationBefore(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(RAturatedwaterEnthalpy())
        calculationObserver.register(RLatentheatVaporization())

        calculationObserver.register(CAturatedwaterEnthalpy())
        calculationObserver.register(CSteamPecificvolume())
        calculationObserver.register(CLatentheatVaporization())

        # 追加除氧器安装高度核算
        # calculationObserver.register(S_local_atmosphere_value())
        calculationObserver.register(S_local_atmosphere_density())
        calculationObserver.register(S_design_flux())
        calculationObserver.register(S_pump_install_height())
        # 追加减温减压器
        calculationObserver.register(T_new_enthalpy())
        calculationObserver.register(T_reduce_water_pressure())
        calculationObserver.register(T_reduce_water_enthalpy())
        calculationObserver.register(T_reduce_water_flow_rate())
        calculationObserver.register(T_reduce_steam_enthalpy())
        calculationObserver.register(T_reduce_enough_enthalpy())
        calculationObserver.register(T_rudece_flow_rate())
        # 追加蓄热器
        calculationObserver.register(Charging_saturation_water_enthalpy())
        calculationObserver.register(Exothermic_saturation_water_enthalpy())
        calculationObserver.register(Charging_saturation_steam_enthalpy())
        calculationObserver.register(Exothermic_saturation_steam_enthalpy())
        calculationObserver.register(P2_steam_amount())
        calculationObserver.register(Charging_water_specific_volume())
        calculationObserver.register(Unit_water_heat_amount())
        calculationObserver.register(Regenerarot_volume())
        calculationObserver.register(Regenerarot_top_steam_volume())
        calculationObserver.register(Regenerarot_max_bleed())
        calculationObserver.register(Evaporation_capacity())
        calculationObserver.register(Charging_volume())
        calculationObserver.register(Exothermic_water_specific_volume())
        calculationObserver.register(Exothermic_water_volume())


        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldobj, form):
        val = {
                'flg': '', 
                'r_work_pressure': form.get('r_work_pressure'), 
                'c_work_pressure': form.get('c_work_pressure'), 
                't_reduce_steam_temperature': form.get('t_reduce_steam_temperature'),
                't_new_flow_rate': form.get('t_new_flow_rate'),
                't_reduce_water_temperature': form.get('t_reduce_water_temperature'),
                't_reduce_steam_pressure': form.get('t_reduce_steam_pressure'),
                't_new_pressure': form.get('t_new_pressure'),
                't_new_steam_temperature': form.get('t_new_steam_temperature'),
                't_reduce_persent': form.get('t_reduce_persent'),
                's_inlet_speed': form.get('s_inlet_speed'),
                's_added_height': form.get('s_added_height'),
                's_net_positive_suction_head': form.get('s_net_positive_suction_head'),
                's_local_atmosphere_value': form.get('s_local_atmosphere_value'),
                's_total_resistance': form.get('s_total_resistance'),
                's_max_feedwater_amount': form.get('s_max_feedwater_amount'),
                'charging_pressure': form.get('charging_pressure'),
                'regenerarot_heat_amount': form.get('regenerarot_heat_amount'),
                'boiler_average_load': form.get('boiler_average_load'),
                'water_fill_coefficient': form.get('water_fill_coefficient'),
                'exothermic_pressure': form.get('exothermic_pressure'),
                'regenerarot_efficiency': form.get('regenerarot_efficiency'),
                'boiler_max_load': form.get('boiler_max_load'),
                'dbresult': oldobj}
        self.creatSubscriber(val)

        return val['dbresult']


class Steam_calculationBefore(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        # 添加注册类
        calculationObserver.register(E_steam_entropy())
        calculationObserver.register(E_steam_enthalpy())
        calculationObserver.register(E_exhaust_point_temperature())
        calculationObserver.register(E_exhaust_point_enthalpy())
        calculationObserver.register(E_steam_exhaust_enthalpy())
        calculationObserver.register(E_backpressure_temperature())
        calculationObserver.register(E_backpressure_enthalpy())
        calculationObserver.register(I_steam_entropy())
        calculationObserver.register(I_steam_enthalpy())
        calculationObserver.register(I_high1_temperature())
        calculationObserver.register(I_high1_enthalpy())
        calculationObserver.register(I_high2_temperature())
        calculationObserver.register(I_high2_enthalpy())
        calculationObserver.register(I_deoxidize_temperature())
        calculationObserver.register(I_deoxidize_enthalpy())
        calculationObserver.register(I_low1_temperature())
        calculationObserver.register(I_low1_enthalpy())
        calculationObserver.register(I_low2_temperature())
        calculationObserver.register(I_low2_enthalpy())
        calculationObserver.register(I_steam_exhaust_enthalpy())
        calculationObserver.register(I_steam_exhaust_enthalpy_steam())
        calculationObserver.register(I_steam_exhaust_enthalpy_water())
        calculationObserver.register(H_enthalpy())
        calculationObserver.register(Hh1_saturated_water_enthalpy())
        calculationObserver.register(Hh1_work_pressure())
        calculationObserver.register(Hh1_extraction_enthalpy())
        calculationObserver.register(Hh2_saturated_water_enthalpy())
        calculationObserver.register(Hh2_work_pressure())
        calculationObserver.register(Hh2_extraction_enthalpy())
        calculationObserver.register(D_water_enthalpy())
        calculationObserver.register(D_extraction_enthalpy())
        calculationObserver.register(Lh1_saturated_water_enthalpy())
        calculationObserver.register(Lh1_work_pressure())
        calculationObserver.register(Lh1_extraction_enthalpy())
        calculationObserver.register(Lh2_saturated_water_enthalpy())
        calculationObserver.register(Lh2_work_pressure())
        calculationObserver.register(Lh2_extraction_enthalpy())
        calculationObserver.register(C_water_temperature())
        calculationObserver.register(C_water_enthalpy())
        calculationObserver.register(Hh3_saturated_water_enthalpy())
        calculationObserver.register(Hh3_work_pressure())
        calculationObserver.register(Hh3_extraction_enthalpy())
        calculationObserver.register(Lh3_saturated_water_enthalpy())
        calculationObserver.register(Lh3_work_pressure())
        calculationObserver.register(Lh3_extraction_enthalpy())
        calculationObserver.register(Hh1_water_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, dbmodel, form):
        val = {
            'flg': 'design',
            'e_steam_exhaust_pressure': form.get('e_steam_exhaust_pressure'),
            'hh1_water_temperature': form.get('hh1_water_temperature'),
            'e_backpressure_pressure': form.get('e_backpressure_pressure'),
            'lh1_pressure_loss': form.get('lh1_pressure_loss'),
            'lh2_water_temperature': form.get('lh2_water_temperature'),
            'hh2_top_difference': form.get('hh2_top_difference'),
            'h_temperature': form.get('h_temperature'),
            'hh3_water_temperature': form.get('hh3_water_temperature'),
            'e_steam_temperature': form.get('e_steam_temperature'),
            'i_high1_pressure': form.get('i_high1_pressure'),
            'd_work_pressure': form.get('d_work_pressure'),
            'hh2_pressure_loss': form.get('hh2_pressure_loss'),
            'hh2_water_temperature': form.get('hh2_water_temperature'),
            'd_pressure_loss': form.get('d_pressure_loss'),
            'lh3_top_difference': form.get('lh3_top_difference'),
            'lh3_pressure_loss': form.get('lh3_pressure_loss'),
            'hh3_top_difference': form.get('hh3_top_difference'),
            'e_steam_pressure': form.get('e_steam_pressure'),
            'lh1_top_difference': form.get('lh1_top_difference'),
            'lh1_water_temperature': form.get('lh1_water_temperature'),
            'hh1_pressure_loss': form.get('hh1_pressure_loss'),
            'lh2_top_difference': form.get('lh2_top_difference'),
            'lh3_water_temperature': form.get('lh3_water_temperature'),
            'hh3_pressure_loss': form.get('hh3_pressure_loss'),
            'i_steam_exhaust_pressure': form.get('i_steam_exhaust_pressure'),
            'd_water_temperature': form.get('d_water_temperature'),
            'lh2_pressure_loss': form.get('lh2_pressure_loss'),
            'hh1_top_difference': form.get('hh1_top_difference'),
            'e_exhaust_point_pressure': form.get('e_exhaust_point_pressure'),

            'dbresult': dbmodel}
        self.creatSubscriber(val)
        return val['dbresult']


class BiomassTurbineAuxiliaryBefore(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(M_saturation_temperature())
        calculationObserver.register(M_condensate_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldobj, form):
        val = {
            'flg': 'design',
            'm_condenser_pressure': form.get('m_condenser_pressure'),
            'm_supercooling': form.get('m_supercooling'),
            'dbresult': oldobj
        }
        self.creatSubscriber(val)

        return val['dbresult']
