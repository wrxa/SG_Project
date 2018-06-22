# -*- coding: utf-8 -*-
from base import CalculationObserver, ExecuteStrategy

'''
from coalchp_furnace_calculation import FSteamEnthalpy, \
        FWaterEnthalpy, ASaturationPressure, FSaturatedWaterEnthalpy, \
        ASaturationPressureAfter
from ...models import CoalCHPFurnaceCalculation
'''

from GPG_Calculation import GPG_Boiler_superheated_steam_enthalpy, \
    GPG_Boiler_feedwater_enthalpy, GPG_Boiler_air_enthalpy, \
    GPG_Boiler_saturation_water_temperature, \
    GPG_Boiler_saturation_water_enthalpy, \
    GPG_TurbineAuxiliary_saturation_temperature,\
    GPG_TurbineAuxiliary_condensate_water_enthalpy,\
    GPG_SteamWaterPipe_main_steam_meida_specific_volume_c,\
    GPG_BoilerAuxiliaries_r_drum_aturatedwater_enthalpy,\
    GPG_BoilerAuxiliaries_r_work_aturatedwater_enthalpy,\
    GPG_BoilerAuxiliaries_r_work_latentheat_vaporization,\
    GPG_BoilerAuxiliaries_c_drum_aturatedwater_enthalpy,\
    GPG_BoilerAuxiliaries_c_work_aturatedwater_enthalpy,\
    GPG_BoilerAuxiliaries_c_work_steam_pecificvolume,\
    GPG_BoilerAuxiliaries_c_work_latentheat_vaporization,\
    GPG_BoilerAuxiliaries_s_local_atmosphere_density, \
    GPG_BoilerAuxiliaries_new_steam_enthalpy, \
    GPG_BoilerAuxiliaries_desuperheater_water_pressure, \
    GPG_BoilerAuxiliaries_desuperheater_water_enthalpy, \
    GPG_BoilerAuxiliaries_desuperheater_water_flux, \
    GPG_BoilerAuxiliaries_desuperheater_steam_enthalpy, \
    GPG_BoilerAuxiliaries_saturation_water_enthalpy, \
    GPG_BoilerAuxiliaries_de_press_temp_device_flux, \
    GPG_BoilerAuxiliaries_charging_saturation_water_enthalpy, \
    GPG_BoilerAuxiliaries_exothermic_saturation_water_enthalpy, \
    GPG_BoilerAuxiliaries_charging_saturation_steam_enthalpy, \
    GPG_BoilerAuxiliaries_exothermic_saturation_steam_enthalpy, \
    GPG_BoilerAuxiliaries_p2_steam_amount, \
    GPG_BoilerAuxiliaries_charging_water_specific_volume, \
    GPG_BoilerAuxiliaries_unit_water_heat_amount, \
    GPG_BoilerAuxiliaries_regenerarot_volume, \
    GPG_BoilerAuxiliaries_regenerarot_top_steam_volume, \
    GPG_BoilerAuxiliaries_regenerarot_max_bleed, \
    GPG_BoilerAuxiliaries_evaporation_capacity, \
    GPG_BoilerAuxiliaries_charging_volume, \
    GPG_BoilerAuxiliaries_exothermic_water_specific_volume, \
    GPG_BoilerAuxiliaries_exothermic_water_volume, \
    GPG_BoilerAuxiliaries_r_sewage_quantity, \
    GPG_BoilerAuxiliaries_r_work_steam_special_volume, \
    GPG_BoilerAuxiliaries_r_vaporization_capacity, \
    GPG_BoilerAuxiliaries_r_steam_volume, \
    GPG_BoilerAuxiliaries_r_volume, \
    E_steam_entropy, E_steam_enthalpy, E_exhaust_point_temperature, \
    E_exhaust_point_enthalpy, E_steam_exhaust_enthalpy, \
    E_backpressure_temperature, E_backpressure_enthalpy, \
    I_steam_entropy, I_steam_enthalpy, I_high1_temperature, \
    I_high1_enthalpy, I_high2_temperature, I_high2_enthalpy, \
    I_deoxidize_temperature, I_deoxidize_enthalpy, \
    I_low1_temperature, I_low1_enthalpy, \
    I_low2_temperature, I_low2_enthalpy, \
    I_steam_exhaust_enthalpy, I_steam_exhaust_enthalpy_steam, \
    I_steam_exhaust_enthalpy_water, H_enthalpy, \
    Hh1_saturated_water_enthalpy,  Hh1_work_pressure, \
    Hh1_extraction_enthalpy, Hh2_saturated_water_enthalpy, \
    Hh2_work_pressure, Hh2_extraction_enthalpy, \
    D_water_enthalpy, D_extraction_enthalpy, \
    Lh1_saturated_water_enthalpy, Lh1_work_pressure, \
    Lh1_extraction_enthalpy, Lh2_saturated_water_enthalpy, \
    Lh2_work_pressure, Lh2_extraction_enthalpy, \
    C_water_temperature, C_water_enthalpy, \
    Hh3_saturated_water_enthalpy, Hh3_work_pressure, \
    Hh3_extraction_enthalpy, Lh3_saturated_water_enthalpy, \
    Lh3_work_pressure, Lh3_extraction_enthalpy, \
    Hh1_water_enthalpy

class GPG_BoilerAuxiliaries_r_sewage_quantity_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_r_sewage_quantity())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'r_boiler_evaporation': form.get('r_boiler_evaporation'),
            'r_emission_rate': form.get('r_emission_rate'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_r_drum_aturatedwater_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_r_drum_aturatedwater_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'r_drum_pressure': form.get('r_drum_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_r_work_aturatedwater_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_r_work_aturatedwater_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'r_work_pressure': form.get('r_work_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_r_work_steam_special_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_r_work_steam_special_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'r_work_pressure': form.get('r_work_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_r_work_latentheat_vaporization_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_r_work_latentheat_vaporization())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'r_work_pressure': form.get('r_work_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_r_vaporization_capacity_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_r_vaporization_capacity())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'r_work_pressure': form.get('r_work_pressure'),
            'r_drum_pressure': form.get('r_drum_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_r_steam_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_r_steam_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'r_work_pressure': form.get('r_work_pressure'),
            'r_drum_pressure': form.get('r_drum_pressure'),
            'r_boiler_evaporation': form.get('r_boiler_evaporation'),
            'r_emission_rate': form.get('r_emission_rate'),
            'r_ultimate_strength': form.get('r_ultimate_strength'),
            'r_affluence_coefficient': form.get('r_affluence_coefficient'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_r_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_r_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'r_work_pressure': form.get('r_work_pressure'),
            'r_drum_pressure': form.get('r_drum_pressure'),
            'r_boiler_evaporation': form.get('r_boiler_evaporation'),
            'r_emission_rate': form.get('r_emission_rate'),
            'r_ultimate_strength': form.get('r_ultimate_strength'),
            'r_affluence_coefficient': form.get('r_affluence_coefficient'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_c_drum_aturatedwater_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_c_drum_aturatedwater_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'c_drum_pressure': form.get('c_drum_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_c_work_aturatedwater_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_c_work_aturatedwater_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'c_work_pressure': form.get('c_work_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_c_work_steam_pecificvolume_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_c_work_steam_pecificvolume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'c_work_pressure': form.get('c_work_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_c_work_latentheat_vaporization_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_c_work_latentheat_vaporization())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'c_work_pressure': form.get('c_work_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_s_local_atmosphere_density_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_s_local_atmosphere_density())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            's_local_atmosphere': form.get('s_local_atmosphere'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_new_steam_enthalpy_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_new_steam_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'new_steam_temperature': form.get('new_steam_temperature'),
            'new_steam_pressure': form.get('new_steam_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_desuperheater_water_pressure_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_desuperheater_water_pressure())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'desuperheater_steam_pressure': form.get('desuperheater_steam_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_desuperheater_water_enthalpy_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_desuperheater_water_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'desuperheater_steam_pressure': form.get('desuperheater_steam_pressure'),
            'desuperheater_water_temperature': form.get('desuperheater_water_temperature'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_desuperheater_water_flux_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_desuperheater_water_flux())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'new_steam_temperature': form.get('new_steam_temperature'),
            'new_steam_pressure': form.get('new_steam_pressure'),
            'new_steam_flux': form.get('new_steam_flux'),
            'desuperheater_water_temperature': form.get('desuperheater_water_temperature'),
            'desuperheater_steam_pressure': form.get('desuperheater_steam_pressure'),
            'desuperheater_steam_temperature': form.get('desuperheater_steam_temperature'),
            'no_vaporized_percent': form.get('no_vaporized_percent'),   
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_desuperheater_steam_enthalpy_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_desuperheater_steam_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'desuperheater_steam_pressure': form.get('desuperheater_steam_pressure'),
            'desuperheater_steam_temperature': form.get('desuperheater_steam_temperature'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_saturation_water_enthalpy_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_saturation_water_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'desuperheater_steam_pressure': form.get('desuperheater_steam_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_de_press_temp_device_flux_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_de_press_temp_device_flux())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'new_steam_temperature': form.get('new_steam_temperature'),
            'new_steam_pressure': form.get('new_steam_pressure'),
            'new_steam_flux': form.get('new_steam_flux'),
            'desuperheater_water_temperature': form.get('desuperheater_water_temperature'),
            'desuperheater_steam_pressure': form.get('desuperheater_steam_pressure'),
            'desuperheater_steam_temperature': form.get('desuperheater_steam_temperature'),
            'no_vaporized_percent': form.get('no_vaporized_percent'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_charging_saturation_water_enthalpy_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_charging_saturation_water_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_exothermic_saturation_water_enthalpy_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_exothermic_saturation_water_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'exothermic_pressure': form.get('exothermic_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_charging_saturation_steam_enthalpy_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_charging_saturation_steam_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_exothermic_saturation_steam_enthalpy_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_exothermic_saturation_steam_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'exothermic_pressure': form.get('exothermic_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_p2_steam_amount_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_p2_steam_amount())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'exothermic_pressure': form.get('exothermic_pressure'),
            'charging_pressure': form.get('charging_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_charging_water_specific_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_charging_water_specific_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_unit_water_heat_amount_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_unit_water_heat_amount())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'exothermic_pressure': form.get('exothermic_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_regenerarot_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_regenerarot_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'exothermic_pressure': form.get('exothermic_pressure'),
            'regenerarot_efficiency': form.get('regenerarot_efficiency'),
            'water_fill_coefficient': form.get('water_fill_coefficient'),
            'regenerarot_heat_amount': form.get('regenerarot_heat_amount'),           
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_regenerarot_top_steam_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_regenerarot_top_steam_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'exothermic_pressure': form.get('exothermic_pressure'),
            'regenerarot_efficiency': form.get('regenerarot_efficiency'),
            'water_fill_coefficient': form.get('water_fill_coefficient'),
            'regenerarot_heat_amount': form.get('regenerarot_heat_amount'),           
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_regenerarot_max_bleed_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_regenerarot_max_bleed())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'boiler_max_load': form.get('boiler_max_load'),
            'boiler_average_load': form.get('boiler_average_load'),        
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_evaporation_capacity_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_evaporation_capacity())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'exothermic_pressure': form.get('exothermic_pressure'),
            'regenerarot_efficiency': form.get('regenerarot_efficiency'),
            'water_fill_coefficient': form.get('water_fill_coefficient'),
            'regenerarot_heat_amount': form.get('regenerarot_heat_amount'),   
            'boiler_max_load': form.get('boiler_max_load'),  
            'boiler_average_load': form.get('boiler_average_load'),               
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_charging_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_charging_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'exothermic_pressure': form.get('exothermic_pressure'),
            'regenerarot_heat_amount': form.get('regenerarot_heat_amount'),        
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']
    
class GPG_BoilerAuxiliaries_exothermic_water_specific_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_exothermic_water_specific_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'exothermic_pressure': form.get('exothermic_pressure'),            
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_BoilerAuxiliaries_exothermic_water_volume_EXEC(ExecuteStrategy):
    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_BoilerAuxiliaries_exothermic_water_volume())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'charging_pressure': form.get('charging_pressure'),
            'exothermic_pressure': form.get('exothermic_pressure'),
            'regenerarot_heat_amount': form.get('regenerarot_heat_amount'),            
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']


class GPG_SteamWaterPipe_main_steam_meida_specific_volume_c_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_SteamWaterPipe_main_steam_meida_specific_volume_c())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'main_steam_design_pressure_c': form.get('main_steam_design_pressure_c'),
            'main_steam_design_temperature_c': form.get('main_steam_design_temperature_c'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_TurbineAuxiliary_condensate_water_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_TurbineAuxiliary_condensate_water_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'condenser_pressure': form.get('condenser_pressure'),
            'supercooling_degree': form.get('supercooling_degree'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_TurbineAuxiliary_saturation_temperature_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_TurbineAuxiliary_saturation_temperature())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'condenser_pressure': form.get('condenser_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_Boiler_superheated_steam_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_superheated_steam_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'superheated_steam_temperature': form.get('superheated_steam_temperature'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_Boiler_feedwater_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_feedwater_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'boiler_feed_water_temperature': form.get('boiler_feed_water_temperature'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']
    
class GPG_Boiler_air_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_air_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'air_temperature': form.get('air_temperature'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']


class GPG_Boiler_saturation_water_temperature_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_saturation_water_temperature())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_Boiler_saturation_water_enthalpy_EXEC(ExecuteStrategy):

    def creatSubscriber(self, val):
        calculationObserver = CalculationObserver()
        calculationObserver.register(GPG_Boiler_saturation_water_enthalpy())
        calculationObserver.writeNewPost(val)

    def specialCalculation(self, oldObj, form):
        val = {
            'superheated_steam_outlet_pressure': form.get('superheated_steam_outlet_pressure'),
            'dbResult': oldObj
        }
        self.creatSubscriber(val)
        return val['dbResult']

class GPG_TurbineOfPts_EXEC(ExecuteStrategy):

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

    def specialCalculation(self, oldObj, form):
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
            
            'dbResult': oldObj
            }
        self.creatSubscriber(val)
        return val['dbResult']