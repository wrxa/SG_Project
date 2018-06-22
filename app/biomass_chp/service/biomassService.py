# -*- coding: utf-8 -*-
from datetime import datetime
from app.biomass_chp.models.modelsBiomass import BiomassCHPNeedsQuestionnaire, \
                     BiomassCHPBoilerCalculation,\
                     BiomassCHPFuelStorageTransportation, \
                     BiomassCHPDesulfurizationAndDenitrification,\
                     BiomassCHPDASRemove, BiomassCHPBoilerAuxiliaries, \
                     BiomassCHPOfficialProcess, BiomassCHPTurbineBackpressure, \
                     BiomassCHPWaterTreatment, BiomassCHPHeatSupply, \
                     BiomassCHPChimney, BiomassCHPCirculatingWater, \
                     BiomasschpTurbineAuxiliary, BiomasschpEconomicIndicators, \
                     BiomassCHPFuelComponent
from flask_login import current_user
from app.models import Company, Plan, Module, EquipmentList, EquipmentListTemplate
from app.biomass_chp.service.execution_strategy import \
                     Furnace_calculationBefore, \
                     Auxiliaries_calculationBefore, \
                     Steam_calculationBefore, \
                     BiomassTurbineAuxiliaryBefore
from app.main.service.turbine import turbine_foctory
from app.main.service.economic import economic_foctory
from app.biomass_chp.service.imgdealwith import biomassImgListResult
from app.ccpp import gl
from util.get_all_path import GetPath
import os
import json
import urllib

lists = [
    's_carbon_design',
    's_carbon_check',
    's_hydrogen_design',
    's_hydrogen_check',
    's_oxygen_design',
    's_oxygen_check',
    's_nitrogen_design',
    's_nitrogen_check',
    's_sulfur_design',
    's_sulfur_check',
    's_total_moisture_design',
    's_total_moisture_check',
    's_grey_design',
    's_grey_check',
    's_daf_design',
    's_daf_check',
    's_grindability_design',
    's_grindability_check',
    's_quantity_design',
    's_quantity_check',
    's_deformation_design',
    's_deformation_check',
    's_softening_design',
    's_softening_check',
    's_hemispherical_design',
    's_hemispherical_check',
    's_flow_design',
    's_flow_check',
    's_fuel_density_design',
    's_fuel_density_check',
    's_ash_density_design',
    's_ash_density_check',
    'l_altitude',
    'l_pressure',
    'l_temperature',
    'l_max_temperature',
    'l_min_temperature',
    'l_humidity',
    't_pressure_grade',
    't_temperature_grade',
    # 't_steam_time',
    't_recent_steam_flow_range',
    't_forward_steam_flow_range',
    't_condensate_water_iron',
    't_condensate_water_recovery_rate',
    # 't_hhl_heating_occasions_type',
    't_year_heating_days',
    't_recent_heating_area',
    't_forward_heating_area',
    'o_planning_area',
    'o_planned_expansion_capacity',
    'o_local_water_condition',
    'o_higher_voltage_level',
    'o_plant_distance',
    'o_flue_gas_sox_limits',
    'o_flue_gas_nox_limits',
    'o_flue_gas_dust_limits'
]

list_column_furnace = [
    'c_carbon_content_received_design',
    'c_carbon_content_received_check',
    'c_hydrogen_content_received_design',
    'c_hydrogen_content_received_check',
    'c_oxygen_content_received_design',
    'c_oxygen_content_received_check',
    'c_nitrogen_content_design',
    'c_nitrogen_content_check',
    'c_sulfur_content_received_design',
    'c_sulfur_content_received_check',
    'c_ash_content_received_design',
    'c_ash_content_received_check',
    'c_water_content_received_design',
    'c_water_content_received_check',
    'c_sum_design',
    'c_sum_check',
    'c_base_volatile_obtained_design',
    'c_base_volatile_obtained_check',
    'c_daf_design',
    'c_daf_check',
    'c_base_heat_received_user_design',
    'c_base_heat_received_user_check',
    'c_base_heat_received_calculation_design',
    'c_base_heat_received_calculation_check',
    'c_low_calorific_value_estimation_design',
    'c_low_calorific_value_estimation_check',
    'c_high_calorific_value_estimation_design',
    'c_high_calorific_value_estimation_check',
    'f_steam_flow_design',
    'f_steam_flow_check',
    'f_steam_pressure_design',
    'f_steam_pressure_check',
    'f_steam_temperature_design',
    'f_steam_temperature_check',
    'f_steam_enthalpy_design',
    'f_steam_enthalpy_check',
    'f_boiler_pressure_design',
    'f_boiler_pressure_check',
    'f_saturated_water_enthalpy_design',
    'f_saturated_water_enthalpy_check',
    'f_water_temperature_design',
    'f_water_temperature_check',
    'f_water_enthalpy_design',
    'f_water_enthalpy_check',
    'f_boiler_efficiency_design',
    'f_boiler_efficiency_check',
    'f_unburned_loss_design',
    'f_unburned_loss_check',
    'f_blowdown_rate_design',
    'f_blowdown_rate_check',
    'f_boiler_consumption_design',
    'f_boiler_consumption_check',
    'f_calculation_consumption_design',
    'f_calculation_consumption_check',
    'd_total_design',
    'd_total_check',
    'd_boiler_total_design',
    'd_boiler_total_check',
    'd_ash_share_design',
    'd_ash_share_check',
    'd_dust_share_design',
    'd_dust_share_check',
    'd_ash_total_design',
    'd_ash_total_check',
    'd_dust_total_design',
    'd_dust_total_check',
    'a_air_volumn_design',
    'a_air_volumn_check',
    'a_hot_temperature_design',
    'a_hot_temperature_check',
    'a_humidity_design',
    'a_humidity_check',
    'a_pressure_design',
    'a_pressure_check',
    'a_temperature_design',
    'a_temperature_check',
    'a_saturation_pressure_design',
    'a_saturation_pressure_check',
    'a_steam_perssure_design',
    'a_steam_perssure_check',
    'a_air_humidity_design',
    'a_air_humidity_check',
    'a_standard_air_humidity_design',
    'a_standard_air_humidity_check',
    'a_wet_air_volumn_design',
    'a_wet_air_volumn_check',
    's_nitrogen_volume_design',
    's_nitrogen_volume_check',
    's_dioxide_volume_design',
    's_dioxide_volume_check',
    's_steam_volume_design',
    's_steam_volume_check',
    's_smoke_volume_design',
    's_smoke_volume_check',
    's_1kg_weight_design',
    's_1kg_weight_check',
    's_wet_smoke_density_design',
    's_wet_smoke_density_check',
    'p_boiler_air_design',
    'p_boiler_air_check',
    'p_wind_design',
    'p_wind_check',
    'p_wind_air_design',
    'p_wind_air_check',
    'p_high_design',
    'p_high_check',
    'p_hign_air_design',
    'p_hign_air_check',
    'p_low_design',
    'p_low_check',
    'p_low_air_design',
    'p_low_air_check',
    'p_fule_design',
    'p_fule_check',
    'p_fule_air_design',
    'p_fule_air_check',
    'p_heater_design',
    'p_heater_check',
    'p_heater_air_design',
    'p_heater_air_check',
    'p_plus_air_design',
    'p_plus_air_check',
    'p_dust_exit_design',
    'p_dust_exit_check',
    'p_dust_design',
    'p_dust_check',
    'p_dust_entry_design',
    'p_dust_entry_check',
    'p_plus_dust_design',
    'p_plus_dust_check',
    'p_fans_air_design',
    'p_fans_air_check',
    'p_1kg_volume_design',
    'p_1kg_volume_check',
    'p_1kg_quality_design',
    'p_1kg_quality_check',
    # 'p_heater_type_design',
    # 'p_heater_type_check',
    'p_heater_first_entry_design',
    'p_heater_first_entry_check',
    'p_heater_second_entry_design',
    'p_heater_second_entry_check',
    'p_heater_first_exit_design',
    'p_heater_first_exit_check',
    'p_heater_second_exit_design',
    'p_heater_second_exit_check',
    'p_smoke_temperature_design',
    'p_smoke_temperature_check',
    'a_theory_air_quality_design',
    'a_theory_air_quality_check',
    'a_boiler_air_design',
    'a_boiler_air_check',
    'a_actual_air_design',
    'a_actual_air_check',
    'a_calculation_consumption_design',
    'a_calculation_consumption_check',
    'a_actual_air_total_design',
    'a_actual_air_total_check',
    'a_first_wind_volume_design',
    'a_first_wind_volume_check',
    'a_cwind_temperature_calculation_design',
    'a_cwind_temperature_calculation_check',
    'a_local_pressure_design',
    'a_local_pressure_check',
    'a_first_cwind_standard_design',
    'a_first_cwind_standard_check',
    'a_first_cwind_actual_design',
    'a_first_cwind_actual_check',
    'a_first_standard_air_density_design',
    'a_first_standard_air_density_check',
    'a_first_cwind_flow_design',
    'a_first_cwind_flow_check',
    'a_first_cwind_density_design',
    'a_first_cwind_density_check',
    'a_check_design',
    'a_check_check',
    'a_first_hwind_temperatue_design',
    'a_first_hwind_temperatue_check',
    'a_first_hwind_flow_design',
    'a_first_hwind_flow_check',
    'a_first_wet_air_density_design',
    'a_first_wet_air_density_check',
    'a_second_wind_volume_design',
    'a_second_wind_volume_check',
    'a_cwind_temperature_design',
    'a_cwind_temperature_check',
    'a_second_cwind_standard_design',
    'a_second_cwind_standard_check',
    'a_second_cwind_actual_design',
    'a_second_cwind_actual_check',
    'a_second_standard_air_density_design',
    'a_second_standard_air_density_check',
    'a_second_cwind_flow_design',
    'a_second_cwind_flow_check',
    'a_second_cwind_density_design',
    'a_second_cwind_density_check',
    'a_second_hwind_temperatue_design',
    'a_second_hwind_temperatue_check',
    'a_second_hwind_flow_design',
    'a_second_hwind_flow_check',
    'a_second_wet_air_density_design',
    'a_second_wet_air_density_check',
    'h_1kg_volume_design',
    'h_1kg_volume_check',
    'h_1kg_quality_design',
    'h_1kg_quality_check',
    'h_calculation_consumption_design',
    'h_calculation_consumption_check',
    'h_standard_smoke_flow_design',
    'h_standard_smoke_flow_check',
    'h_smoke_flow_design',
    'h_smoke_flow_check',
    'h_smoke_temperature_design',
    'h_smoke_temperature_check',
    'h_smoke_volume_design',
    'h_smoke_volume_check',
    'h_smoke_density_design',
    'h_smoke_density_check',
    'd_exit_air_design',
    'd_exit_air_check',
    'd_wind_parameter_design',
    'd_wind_parameter_check',
    'd_entry_air_design',
    'd_entry_air_check',
    'd_cold_air_temperature_design',
    'd_cold_air_temperature_check',
    'd_entry_somke_temperature_design',
    'd_entry_somke_temperature_check',
    'd_standard_1kg_volume_design',
    'd_standard_1kg_volume_check',
    'd_entry_1kg_quality_design',
    'd_entry_1kg_quality_check',
    'd_standard_smoke_flow_design',
    'd_standard_smoke_flow_check',
    'd_entry_somke_flow_design',
    'd_entry_somke_flow_check',
    'd_entry_smoke_actual_flow_design',
    'd_entry_smoke_actual_flow_check',
    'e_wind_parameter_design',
    'e_wind_parameter_check',
    'e_air_parameter_design',
    'e_air_parameter_check',
    'e_smoke_temperature_design',
    'e_smoke_temperature_check',
    'e_standard_1kg_volume_design',
    'e_standard_1kg_volume_check',
    'e_1kg_quality_design',
    'e_1kg_quality_check',
    'e_standard_smoke_flow_design',
    'e_standard_smoke_flow_check',
    'e_smoke_flow_design',
    'e_smoke_flow_check',
    'e_smoke_actual_flow_design',
    'e_smoke_actual_flow_check',
    'e_smoke_actual_density_design',
    'e_smoke_actual_density_check',
    'i_wind_parameter_design',
    'i_wind_parameter_check',
    'i_air_parameter_design',
    'i_air_parameter_check',
    'i_smoke_temperature_design',
    'i_smoke_temperature_check',
    'i_standard_1kg_volume_design',
    'i_standard_1kg_volume_check',
    'i_1kg_quality_design',
    'i_1kg_quality_check',
    'i_standard_smoke_flow1_design',
    'i_standard_smoke_flow1_check',
    'i_standard_smoke_flow2_design',
    'i_standard_smoke_flow2_check',
    'i_smoke_flow_design',
    'i_smoke_flow_check',
    'i_smoke_actual_flow1_design',
    'i_smoke_actual_flow1_check',
    'i_smoke_actual_flow2_design',
    'i_smoke_actual_flow2_check',
    'i_smoke_actual_density_design',
    'i_smoke_actual_density_check',
    'i_wet_smoke_actual_density_design',
    'i_wet_smoke_actual_density_check',
    'go_oxygen_vol_design',
    'go_oxygen_vol_check',
    'go_theoretica_vol_design',
    'go_theoretica_vol_check',
    'go_theoretica_flow_design',
    'go_theoretica_flow_check',
    'go_calculation_consumption_design',
    'go_calculation_consumption_check',
    'go_air_parameter_design',
    'go_air_parameter_check',
    'go_standard_1kg_volume_design',
    'go_standard_1kg_volume_check',
    'go_smoke_flow_design',
    'go_smoke_flow_check',
    'go_drygas_oxygen_vol_design',
    'go_drygas_oxygen_vol_check',
    'go_total_combustion_product_vol_design',
    'go_total_combustion_product_vol_check',
    'boiler_type',
    'pressure_temperature'
]

list_column_sorttran = [
    'b_rated_fuel_consumption_design',
    'b_rated_fuel_consumption_check',
    'b_saily_use_hours_design',
    'b_saily_use_hours_check',
    'b_daily_consumption_design',
    'b_daily_consumption_check',
    'b_annual_use_hours_design',
    'b_annual_use_hours_check',
    'b_year_consumption_design',
    'b_year_consumption_check',
    'b_unbalance_coefficient_design',
    'b_unbalance_coefficient_check',
    'b_daily_fuel_consumption_design',
    'b_daily_fuel_consumption_check',
    'b_carrying_vehicle_load_design',
    'b_carrying_vehicle_load_check',
    'b_daily_vehicle_design',
    'b_daily_vehicle_check',
    's_fuel_reserve_days_design',
    's_fuel_reserve_days_check',
    's_fuel_available_reserves_design',
    's_fuel_available_reserves_check',
    's_aggregate_coefficient_design',
    's_aggregate_coefficient_check',
    's_average_stack_height_design',
    's_average_stack_height_check',
    's_fuel_bulk_density_design',
    's_fuel_bulk_density_check',
    's_yardarea_design',
    's_yardarea_check',
    'd_fuel_reserve_days_design',
    'd_fuel_reserve_days_check',
    'd_fuel_available_reserves_design',
    'd_fuel_available_reserves_check',
    'd_aggregate_coefficient_design',
    'd_aggregate_coefficient_check',
    'd_average_stack_height_design',
    'd_average_stack_height_check',
    'd_fuel_bulk_density_design',
    'd_fuel_bulk_density_check',
    'd_yardarea_design',
    'd_yardarea_check',
    't_rated_fuel_consumption_design',
    't_rated_fuel_consumption_check',
    't_hourage_design',
    't_hourage_check',
    't_bin_quantity_design',
    't_bin_quantity_check',
    't_total_effective_volume_design',
    't_total_effective_volume_check',
    't_single_effective_volume_calculation_design',
    't_single_effective_volume_calculation_check',
    't_single_effective_volume_selected_design',
    't_single_effective_volume_selected_check',
    't_consumption_hours_design',
    't_consumption_hours_check',
    'f_rated_fuel_consumption_design',
    'f_rated_fuel_consumption_check',
    'f_duplex_number_design',
    'f_duplex_number_check',
    'f_flushness_design',
    'f_flushness_check',
    'f_duplex_output_design',
    'f_duplex_output_check',
    'f_single_duplex_output_design',
    'f_single_duplex_output_check',
    'f_single_rated_fuel_consumption_design',
    'f_single_rated_fuel_consumption_check',
    'f_daily_consumption_design',
    'f_daily_consumption_check',
    'f_feeding_output_calculation_design',
    'f_feeding_output_calculation_check',
    'f_feeding_output_selected_design',
    'f_feeding_output_selected_check',
    'f_belt_width',
    'f_section_coefficient',
    'f_belt_speed',
    'f_loose_density',
    'f_belt_max_delivery',
    'bs_rated_fuel_consumption_design',
    'bs_rated_fuel_consumption_check',
    'b_hourage_design',
    'b_hourage_check',
    'b_bin_quantity_design',
    'b_bin_quantity_check',
    'b_total_effective_volume_design',
    'b_total_effective_volume_check',
    'b_single_effective_volume_calculation_design',
    'b_single_effective_volume_calculation_check',
    'b_single_effective_volume_selected_design',
    'b_single_effective_volume_selected_check',
    'b_consumption_hours_design',
    'b_consumption_hours_check',
    's_rated_fuel_consumption_design',
    's_rated_fuel_consumption_check',
    's_duplex_number_design',
    's_duplex_number_check',
    's_flushness_design',
    's_flushness_check',
    's_duplex_output_design',
    's_duplex_output_check',
    's_single_duplex_output_design',
    's_single_duplex_output_check'
]

list_column_desuldenit = [
    's_sulfur_content_received',
    's_feed_consumption',
    's_fuel_so2',
    's_before_so2',
    's_input_smoke',
    's_no_before_so2',
    's_desulfurization_efficiency',
    's_after_so2',
    's_env_after_so2',
    's_after_so2_discharge',
    'c_desulfurization_percentage',
    'c_after_so2',
    'c_so2_quality',
    'c_so2_molar',
    'c_sulfur_molar',
    'c_caco3_molar',
    'c_caco3_quality_require',
    'c_caco3_quality_reaction',
    'c_caso4_quality_generation',
    'c_after_quality_add',
    'c_limestone_purity',
    'c_limestone_consumption',
    'c_ash',
    'c_limestone_storage_time',
    'c_limestone_output',
    'c_limestone_density',
    'c_limestone_fullness',
    'c_limestone_volumn',
    'c_limestone_height',
    'c_limestone_diameter',
    'n_before_nox_concentration',
    'n_input_smoke',
    'n_desulfurization_efficiency',
    'n_before_nox_discharge',
    'n_after_nox_concentration',
    'n_env_after_nox_concentration',
    'n_after_nox_discharge',
    'd_denitration_percentage',
    'd_denitration_quality',
    'd_after_nox_discharge',
    'd_denitration_molar',
    'd_escape_rate',
    'd_escape_quality',
    'd_escape_quality_urea',
    'd_nh3nox_molar',
    'd_urea_nox_molar',
    'd_urea_nox_quality',
    'd_theory_urea',
    'd_use_urea',
    'd_water_urea',
    'd_days_urea',
    'd_capacity_urea'
]

list_column_dasremove = [
    'd_total_ash',
    'd_flyash_fraction',
    'd_entry_flyash',
    'd_standard_smoke_flow',
    'd_actual_smoke_flow',
    'd_standard_smoke_concentration',
    'd_actual_smoke_concentration',
    'd_dust_remove_efficiency',
    'd_exit_smoke_concentration',
    'd_exit_smoke_flow',
    'd_dust_wiper_flow',
    'd_entry_smoke_volume',
    'd_tun_exit_smoke_concentration',
    'd_env_particulate',
    'a_remove_output',
    'a_bulk_density',
    'a_fullness',
    'a_storage_time',
    'a_volumn',
    'a_diameter',
    'a_height',
    'a_ratio',
    'a_gas_consumption',
    's_slag_quantity',
    's_yns_output',
    's_coolwater',
    's_yns_number',
    's_slag_output',
    's_conveyor_output',
    's_bulk_density',
    's_fullness',
    's_storage_time',
    's_volumn',
    's_diameter',
    's_height'
]

list_column_auxiliaries = [
    'r_boiler_evaporation',
    'r_emission_time',
    'r_emission_rate',
    'r_sewage_quantity',
    'r_drum_pressure',
    'r_drum_aturatedwater_enthalpy',
    'r_work_pressure',
    'r_work_aturatedwater_enthalpy',
    'r_work_latentheat_vaporization',
    'r_ultimate_strength',
    'r_volume',
    'r_specifications',
    'c_boiler_evaporation',
    'c_emission_rate',
    'c_sewage_quantity',
    'c_drum_pressure',
    'c_drum_aturatedwater_enthalpy',
    'c_work_pressure',
    'c_work_aturatedwater_enthalpy',
    'c_work_steam_pecificvolume',
    'c_work_latentheat_vaporization',
    'c_steam_dryness',
    'c_ultimate_strength',
    'c_vaporization_capacity',
    'c_volume',
    'c_specifications',
    'a_altitude',
    'a_atmosphere',
    'f_working_condition_temperature',
    'f_working_flow',
    'f_local_atmosphere',
    'f_standard_temperature',
    'f_standard_pressure',
    'f_standard_flow',
    's_working_condition_temperature',
    's_working_flow',
    's_local_atmosphere',
    's_standard_temperature',
    's_standard_pressure',
    's_standard_flow',
    'a_working_condition_temperature',
    'a_working_flow',
    'a_local_atmosphere',
    'a_standard_temperature',
    'a_standard_pressure',
    'a_standard_flow',
    'bf_standard_temperature',
    'bf_standard_pressure',
    'bf_standard_flow',
    'bf_working_condition_temperature',
    'bf_local_atmosphere',
    'bf_working_flow',
    'bs_standard_temperature',
    'bs_standard_pressure',
    'bs_standard_flow',
    'bs_working_condition_temperature',
    'bs_local_atmosphere',
    'bs_working_flow',
    'ba_standard_temperature',
    'ba_standard_pressure',
    'ba_standard_flow',
    'ba_working_condition_temperature',
    'ba_local_atmosphere',
    'ba_working_flow',
    'sf_temperature',
    'sf_boiler_resistance',
    'sf_duct_resistance',
    'sf_local_atmosphere',
    'sf_smoke_flow',
    'sf_medium_temperature',
    'sf_fan_pressure',
    'sf_fan_select_pressure',
    'sf_fan_select_flow',
    'sf_fan_efficiency',
    'sf_motor_efficiency',
    'sf_fan_power',
    'sf_motor_safe',
    'sf_motor_power',
    'ss_temperature',
    'ss_boiler_resistance',
    'ss_duct_resistance',
    'ss_local_atmosphere',
    'ss_smoke_flow',
    'ss_medium_temperature',
    'ss_fan_pressure',
    'ss_fan_select_pressure',
    'ss_fan_select_flow',
    'ss_fan_efficiency',
    'ss_motor_efficiency',
    'ss_fan_power',
    'ss_motor_safe',
    'ss_motor_power',
    'i_temperature',
    'i_boiler_resistance',
    'i_denitration',
    'i_duster',
    'i_duct_resistance',
    'i_cduct_resistance',
    'i_local_atmosphere',
    'i_smoke_flow',
    'i_medium_temperature',
    'i_fan_pressure',
    'i_fan_select_pressure',
    'i_fan_select_flow',
    'i_fan_efficiency',
    'i_motor_efficiency',
    'i_fan_power',
    'i_motor_safe',
    'i_motor_power',
    'r_temperature',
    'r_pressure',
    'r_duct_resistance',
    'r_local_atmosphere',
    'r_smoke_flow',
    'r_medium_temperature',
    'r_fan_pressure',
    'r_fan_select_pressure',
    'r_fan_select_flow',
    'r_fan_efficiency',
    'r_motor_efficiency',
    'r_fan_power',
    'r_motor_safe',
    'r_motor_power',
    'f_boiler_use_pressure',
    'f_economizer_entry_pressure',
    'f_deaerator_work_pressure',
    'f_pipe_resistance',
    'f_inlet_pipe_resistance',
    'f_center_water',
    'f_deaerator_center',
    'f_pump_total_head',
    'f_flow',
    'f_pump_efficiency',
    'f_mechanical_transmission_efficiency',
    'f_motor_efficiency',
    'f_motor_reserve_coefficient',
    'f_auxiliary_motor_power',
    # 'f_pump_selection',
    'f_deaerator_quantity',
    'f_deaerator_pressure',
    'f_deaerator_temperature',
    'f_boiler_evaporation',
    'f_water_storage_time',
    'f_effective_volume',
    'f_length',
    'f_diameter',
    's_max_feedwater_amount',
    's_de_ox_pressure', 's_local_atmosphere_value', 's_local_atmosphere_density',
    's_design_flux', 's_net_positive_suction_head', 's_total_resistance',
    's_inlet_speed', 's_added_height', 's_pump_install_height',
    't_new_steam_temperature', 't_new_pressure',
    't_new_enthalpy', 't_new_flow_rate', 't_reduce_water_temperature',
    't_reduce_water_pressure', 't_reduce_water_enthalpy',
    't_reduce_water_flow_rate', 't_reduce_steam_temperature',
    't_reduce_steam_pressure', 't_reduce_steam_enthalpy',
    't_reduce_enough_enthalpy', 't_reduce_persent', 't_rudece_flow_rate',
    'charging_pressure', 'exothermic_pressure', 'charging_saturation_water_enthalpy', 
    'exothermic_saturation_water_enthalpy', 'charging_saturation_steam_enthalpy', 
    'exothermic_saturation_steam_enthalpy', 'p2_steam_amount', 
    'charging_water_specific_volume', 'unit_water_heat_amount', 
    'regenerarot_efficiency', 'water_fill_coefficient', 'regenerarot_heat_amount',
    'regenerarot_volume', 'regenerarot_top_steam_volume', 'boiler_max_load',
    'boiler_average_load', 'regenerarot_max_bleed', 'evaporation_capacity',
    'exothermic_evaporation_capacity', 'charging_volume', 
    'exothermic_water_specific_volume', 'exothermic_water_volume'
]

list_column_official = [
    'o_oil_can',
    'o_oil_pump',
    'o_oil_pump_pressure',
    'o_boiler_type',
    # 'o_fire_way',
    'o_steam_parameter',
    'o_steam_volumn',
    'o_fuel_type'
    #'o_install_way'  
]

list_column_water = [
    'o_steam_flow',
    'o_loss_factory',
    'o_boiler_blowdown_loss',
    'o_start_accident_increase_loss',
    'o_external_supply_loss',
    'o_water_consumption',
    'o_boiler_water_normal',
    'o_boiler_water_max',
    'o_boiler_water_system',
    'o_salt_water_tank',
    'o_process_route'
]

list_column_chimney = [
    "chimney_height", "local_atmosphere", "standard_air_density",
    "standard_average_smoke_density", "standard_calculated_smoke_density",
    "outdoor_air_temperature", "chimney_inlet_temperature",
    "chimney_temperature_drop_per_meter", "chimney_average_temperature",
    "chimney_draft", "smoke_amount", "chimney_outlet_temperature",
    "chimney_outlet_flow", "chimney_outlet_inner_diameter",
    "chimney_outlet_selected_inner_diameter",
    "chimney_experience_base_diameter", "low_load_smoke_amount",
    "low_load_smoke_temperature", "low_load_flow_30_percent",
    "chimney_resistance_coefficient", "chimney_average_velocity",
    "chimney_average_diameter", "chimney_friction_resistance",
    "chimney_outlet_resistance_coefficient", "chimney_outlet_resistance",
    "chimney_total_resistance"
]

list_column_heat = [
    'heat_area',
    'heat_hot_target',
    'heat_hot_load',
    'turbine_pressure',
    'heat_turbine_flow',
    'use_flow',
    'steam_supply_rate',
    'hot_loss',
    'hot_turbine_flow'
]

list_column_steam = [
'e_turbine_efficiency',
'e_mechanical_efficiency',
'e_generator_efficiency',
'e_steam_pressure',
'e_steam_temperature',
'e_steam_flow',
'e_steam_entropy',
'e_steam_enthalpy',
'e_exhaust_point_pressure',
'e_exhaust_point_temperature',
'e_exhaust_point_entropy',
'e_exhaust_point_enthalpy',
'e_exhaust_point_flow',
'e_exhaust_after_steam',
'e_exhaust_after_pressure',
'e_exhaust_after_enthalpy',
'e_exhaust_after_entropy',
'e_steam_exhaust_pressure',
'e_steam_exhaust_enthalpy',
'e_backpressure_pressure',
'e_backpressure_temperature',
'e_backpressure_enthalpy',
'e_backpressure_flow',
'e_gross_generation',
'e_hot_data',
'e_steam_extraction',
'e_steam_extraction_select',
'e_steam_water_loss',
'e_throttle_flow',
'h_temperature',
'h_pressure',
'h_enthalpy',
'h_amount',
'hh1_water_temperature',
'hh1_water_enthalpy',
'hh1_top_difference',
'hh1_saturated_water_temperature',
'hh1_saturated_water_enthalpy',
'hh1_work_pressure',
'hh1_pressure_loss',
'hh1_extraction_pressure',
'hh1_extraction_enthalpy',
'hh1_extraction_amount',
'hh2_water_temperature',
'hh2_water_enthalpy',
'hh2_top_difference',
'hh2_saturated_water_temperature',
'hh2_saturated_water_enthalpy',
'hh2_work_pressure',
'hh2_pressure_loss',
'hh2_extraction_pressure',
'hh2_extraction_enthalpy',
'hh2_extraction_amount',
'hh3_water_temperature',
'hh3_water_enthalpy',
'hh3_top_difference',
'hh3_saturated_water_temperature',
'hh3_saturated_water_enthalpy',
'hh3_work_pressure',
'hh3_pressure_loss',
'hh3_extraction_pressure',
'hh3_extraction_enthalpy',
'hh3_extraction_amount',
'd_water_temperature',
'd_water_enthalpy',
'd_work_pressure',
'd_pressure_loss',
'd_extraction_pressure',
'd_extraction_enthalpy',
'd_extraction_amount',
'lh1_water_temperature',
'lh1_water_enthalpy',
'lh1_top_difference',
'lh1_saturated_water_temperature',
'lh1_saturated_water_enthalpy',
'lh1_work_pressure',
'lh1_pressure_loss',
'lh1_extraction_pressure',
'lh1_extraction_enthalpy',
'lh1_extraction_amount',
'lh2_water_temperature',
'lh2_water_enthalpy',
'lh2_top_difference',
'lh2_saturated_water_temperature',
'lh2_saturated_water_enthalpy',
'lh2_work_pressure',
'lh2_pressure_loss',
'lh2_extraction_pressure',
'lh2_extraction_enthalpy',
'lh2_extraction_amount',
'lh3_water_temperature',
'lh3_water_enthalpy',
'lh3_top_difference',
'lh3_saturated_water_temperature',
'lh3_saturated_water_enthalpy',
'lh3_work_pressure',
'lh3_pressure_loss',
'lh3_extraction_pressure',
'lh3_extraction_enthalpy',
'lh3_extraction_amount',
'c_water_temperature',
'c_water_enthalpy',
'c_work_pressure',
'c_pressure_loss',
'c_extraction_pressure',
'c_extraction_enthalpy',
'c_extraction_amount',
'i_turbine_efficiency',
'i_mechanical_efficiency',
'i_generator_efficiency',
'i_steam_pressure',
'i_steam_temperature',
'i_steam_flow',
'i_steam_entropy',
'i_steam_enthalpy',
'i_high1_pressure',
'i_high1_entropy',
'i_high1_temperature',
'i_high1_enthalpy',
'i_high1_flow',
'i_steam_hh1_power',
'i_high2_pressure',
'i_high2_entropy',
'i_high2_temperature',
'i_high2_enthalpy',
'i_high2_flow',
'i_hh1_hh2_power',
'i_deoxidize_pressure',
'i_deoxidize_entropy',
'i_deoxidize_temperature',
'i_deoxidize_enthalpy',
'i_deoxidize_flow',
'i_hh2_deoxidize_power',
'i_exhaust_point_pressure',
'i_exhaust_point_temperature',
'i_exhaust_point_entropy',
'i_exhaust_point_enthalpy',
'i_exhaust_point_flow',
'i_deoxidize_exhaust_power',
'i_low1_pressure',
'i_low1_entropy',
'i_low1_temperature',
'i_low1_enthalpy',
'i_low1_flow',
'i_exhaust_lh1_power',
'i_low2_pressure',
'i_low2_entropy',
'i_low2_temperature',
'i_low2_enthalpy',
'i_low2_flow',
'i_lh1_lh2_power',
'i_low3_pressure',
'i_low3_entropy',
'i_low3_temperature',
'i_low3_enthalpy',
'i_low3_flow',
'i_lh2_lh3_power',
'i_steam_exhaust_pressure',
'i_steam_exhaust_entropy',
'i_steam_exhaust_enthalpy',
'i_steam_exhaust_enthalpy_actual',
'i_steam_exhaust_enthalpy_steam',
'i_steam_exhaust_enthalpy_water',
'i_steam_exhaust_dry',
'i_steam_exhaust_flow',
'i_lh2_steam_power',
'i_total_power',
'i_calculation_error',
'e_steam_plus_enthalpy'
]

list_column_steamClear = [
# 'i_turbine_efficiency',
# 'i_mechanical_efficiency',
# 'i_generator_efficiency',
# 'i_steam_pressure',
# 'i_steam_temperature',
#'i_steam_flow',
'i_steam_entropy',
'i_steam_enthalpy',
'i_high1_pressure',
'i_high1_entropy',
'i_high1_temperature',
'i_high1_enthalpy',
'i_high1_flow',
'i_steam_hh1_power',
'i_high2_pressure',
'i_high2_entropy',
'i_high2_temperature',
'i_high2_enthalpy',
'i_high2_flow',
'i_hh1_hh2_power',
'i_deoxidize_pressure',
'i_deoxidize_entropy',
'i_deoxidize_temperature',
'i_deoxidize_enthalpy',
'i_deoxidize_flow',
'i_hh2_deoxidize_power',
'i_exhaust_point_pressure',
'i_exhaust_point_temperature',
'i_exhaust_point_entropy',
'i_exhaust_point_enthalpy',
'i_exhaust_point_flow',
'i_deoxidize_exhaust_power',
'i_low1_pressure',
'i_low1_entropy',
'i_low1_temperature',
'i_low1_enthalpy',
'i_low1_flow',
'i_exhaust_lh1_power',
'i_low2_pressure',
'i_low2_entropy',
'i_low2_temperature',
'i_low2_enthalpy',
'i_low2_flow',
'i_lh1_lh2_power',
'i_low3_pressure',
'i_low3_entropy',
'i_low3_temperature',
'i_low3_enthalpy',
'i_low3_flow',
'i_lh2_lh3_power',
'i_steam_exhaust_pressure',
'i_steam_exhaust_entropy',
'i_steam_exhaust_enthalpy',
'i_steam_exhaust_enthalpy_actual',
'i_steam_exhaust_enthalpy_steam',
'i_steam_exhaust_enthalpy_water',
'i_steam_exhaust_dry',
'i_steam_exhaust_flow',
'i_lh2_steam_power',
'i_total_power',
'i_calculation_error'
]

list_column_circulatingWater = [
    'v_steam_exhaust_flow_winter', 'v_steam_exhaust_flow_summer',
    'v_steam_exhaust_flow_select', 'v_circulating_ratio_winter',
    'v_circulating_ratio_summer', 'v_circulating_water_winter',
    'v_circulating_water_summer', 'v_auxiliary_engine_cooling_winter',
    'v_auxiliary_engine_cooling_summer', 'v_total_circulating_water_winter',
    'v_total_circulating_water_summer', 'v_total_circulating_water_select',
    'v_enter_the_outlet_temperature_difference', 'v_dry_bulb_temperature',
    'v_up_dry_bulb_temperature', 'v_down_dry_bulb_temperature', 'v_up_k',
    'v_down_k', 'v_k', 'v_evaporation_loss_rate', 'v_evaporation_loss',
    'v_blowing_loss_rate', 'v_partial_blow_loss', 'v_concentrate_ratio',
    'v_discharge_loss', 'v_discharge_capacity', 'v_amount_of_makeup_water',
    'v_circulating_pool_size', 'p_spray_density', 'p_spray_area', 'p_select_f',
    'p_count', 'p_single_cold_amount', 'p_select_s', 'c_pressure_condenser',
    'c_condenser_tube_friction', 'c_circulating_water_pressure',
    'c_circulating_pool_pressure', 'c_circulation_height_difference',
    'c_height_difference_inlet', 'c_pipe_losses', 'c_y_losses',
    'c_pumping_head', 'c_flow', 'c_pump_power', 'c_mechine_power',
    'c_motor_power', 'c_motor_backup_coefficient', 'c_supporting_motor_power',
    'c_forklift_parameters_power', 'c_forklift_parameters_flow',
    'c_forklift_parameters_lift', 'p_select'
]


list_column_turbineAuxiliary = [
    'w_deaerator_working_pressure', 'w_deaerator_difference',
    'w_deaerator_need_pressure', 'w_condenser_higter', 'w_hot_well_resistance',
    'w_condensate_pump_lift', 'w_flow_amount', 'w_pump_efficiency',
    'w_mechanical_transmission_efficiency', 'w_motor_efficiency',
    'w_motor_reserve_coefficient', 'w_auxiliary_motor_power',
    'm_condensate_amount', 'm_condenser_pressure', 'm_steam_enthalpy',
    'm_cooling_water_inlet_temperature', 'm_saturation_temperature',
    'm_supercooling', 'm_condensate_temperature', 'm_condensate_enthalpy',
    'm_cooling_pipe_coefficient', 'm_correction_coefficient',
    'm_calculation_index', 'm_cooling_flow', 'm_cooling_type',
    'm_correction_condensers', 'm_flow_speed_correction',
    'm_inlet_temperature', 'm_flow_count', 'm_consideration_change',
    'm_total_heat_transfer', 'm_condenser_heat_load', 'm_cycle_ratio',
    'm_circulating_water', 'm_cooling_water_rise',
    'm_cooling_outlet_temperature', 'm_logarithmic_mean_difference',
    'm_area_cooling_surface', 'f_air_ejector_pressure',
    'f_water_tank_pressure', 'f_water_difference', 'f_ejection_pump_loss',
    'f_total_lift', 'f_flow_amount', 'f_pump_efficiency',
    'f_mechanical_transmission_efficiency', 'f_motor_efficiency',
    'f_motor_reserve_coefficient', 'f_auxiliary_motor_power',
    'c_water_tank_pressure', 'c_recirculating_tube_pressure',
    'c_water_difference', 'c_ejection_pump_loss', 'c_total_lift',
    'c_flow_amount', 'c_pump_efficiency',
    'c_mechanical_transmission_efficiency', 'c_motor_efficiency',
    'c_motor_reserve_coefficient', 'c_auxiliary_motor_power'
]

list_column_economic = [
    'condensate_backwater_pressure',
    'condensate_backwater_temperature',
    'condensate_backwater_enthalpy',
    'smoke_heat_consumption_rate',
    'heat_consumption_rate',
    'smoke_steam_consumption_rate',
    'steam_consumption_rate',
    'annual_useage_hours',
    'annual_heat_hours',
    'annual_heat_supply',
    'annual_power_generation',
    'plant_electricity_consumption',
    'annual_power_supply',
    'boiler_efficiency',
    'pipeline_efficiency',
    'smoke_power_coal_consumption',
    'power_coal_consumption',
    'smoke_supply_coal_consumption',
    'supply_coal_consumption',
    'annual_average_thermoelectric_ratio',
    'smoke_heat_efficiency',
    'heat_efficiency'
]

list_column_fuel = [
    'carbon',
    'hydrogen',
    'oxygen',
    'nitrogen',
    'sulfur',
    'water',
    'daf',
    'grey',
    'grindability',
    'low'
]


# 格式化数据库取出的值
def format_value(flag, values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if not values or values == "null" or values == "None":
        result = ""
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        #result = float(str(float(values)).rstrip('0'))
        result = round(float(str(float(values)).rstrip('0')), 2)
    else:
        result = values
    return result

def format_value2(flag, values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if not values or values == "null" or values == "None":
        result = ""
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        result = float(str(float(values)).rstrip('0'))
    else:
        result = values
    return result

def format_value3(flag, values):
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if not values or values == "null" or values == "None":
        result = ""
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        result = round(float(str(float(values)).rstrip('0')), 3)
    else:
        result = values
    return result

class BiomassImgService():
    # 出图处理
    def imgCreate(self, plan_id):
        biomassImgListResult.imgdealwithExecute(plan_id)

    # 获取地址列表
    def getImgList(self, planId):
        path = GetPath.getImgBiomassResultDir(planId)
        imglist = []
        for i in os.listdir(path):
            path_file = os.path.join(path, i)  # 取文件绝对路径
            if os.path.isfile(path_file):
                dirname, filename = os.path.split(path_file)
                chineseName, filenameprefix = self.getChineseName(filename)
                if chineseName is not None:
                    netPath = GetPath.getImgBiomassNetPath(filenameprefix, planId)
                    if netPath is not None:
                        dirname, netfilename = os.path.split(netPath)
                        if filename == netfilename:
                            imgDir = {}
                            imgDir['chineseName'] = chineseName
                            imgDir['netPath'] = netPath
                            imgDir['filename'] = filename
                            imglist.append(imgDir)
        return imglist

    def getChineseName(self, filename):
        if filename is not None and filename.find("biomass_water1") != -1:
            return u"原则性化学水处理系统图", "biomass_water1"
        if filename is not None and filename.find("biomass_water2") != -1:
            return u"原则性化学水处理系统图", "biomass_water2"
        if filename is not None and filename.find("biomass_dust") != -1:
            return u"原则性除灰系统图", "biomass_dust"
        if filename is not None and filename.find("biomass_ash1") != -1:
            return u"原则性除渣系统图", "biomass_ash1"
        if filename is not None and filename.find("biomass_ash2") != -1:
            return u"原则性除渣系统图", "biomass_ash2"

        if filename is not None and filename.find("biomass_trans1") != -1:
            return u"原则性燃料输送系统图", "biomass_trans1"
        if filename is not None and filename.find("biomass_trans2") != -1:
            return u"原则性燃料输送系统图", "biomass_trans2"
        if filename is not None and filename.find("biomass_fire1") != -1:
            return u"原则性燃烧系统图", "biomass_fire1"
        if filename is not None and filename.find("biomass_fire2") != -1:
            return u"原则性燃烧系统图", "biomass_fire2"
        if filename is not None and filename.find("biomass_fire3") != -1:
            return u"原则性燃烧系统图", "biomass_fire3"
        if filename is not None and filename.find("biomass_fire4") != -1:
            return u"原则性燃烧系统图", "biomass_fire4"
        
        if filename is not None and filename.find("biomass_hot1a") != -1:
            return u"原则性热力系统图", "biomass_hot1a"
        if filename is not None and filename.find("biomass_hot1b") != -1:
            return u"原则性热力系统图", "biomass_hot1b"
        if filename is not None and filename.find("biomass_hot2a") != -1:
            return u"原则性热力系统图", "biomass_hot2a"
        if filename is not None and filename.find("biomass_hot2b") != -1:
            return u"原则性热力系统图", "biomass_hot2b"
        if filename is not None and filename.find("biomass_hot3a") != -1:
            return u"原则性热力系统图", "biomass_hot3a"
        if filename is not None and filename.find("biomass_hot3b") != -1:
            return u"原则性热力系统图", "biomass_hot3b"

        return None

class BiomassEquipmentService():
    # 同步设备清单数据
    def updateEquipment(self, plan_id):
        # 锅炉
        furnaceCalculation = BiomassCHPBoilerCalculation.search_furnace_calculation(
            plan_id)
        # 锅炉辅机
        boilerAuxiliaries = BiomassCHPBoilerAuxiliaries.search_auxiliaries(
            plan_id)
        # 汽轮机
        turbineBackpressure = BiomassCHPTurbineBackpressure.search_turbineBackpressure(
            plan_id)
        # 循环水
        circulatingWater = BiomassCHPCirculatingWater.search_circulating_water(
            plan_id)
        # 燃料存储
        transportation = BiomassCHPFuelStorageTransportation.search_storage_transportation(
            plan_id)
        # 除尘除灰
        dasRemove = BiomassCHPDASRemove.search_dasRemove(
            plan_id)
        # 烟囱
        chimney = BiomassCHPChimney.search_biomassCHPChimney(
            plan_id)
        # 公用工程
        official = BiomassCHPOfficialProcess.search_official(
            plan_id)
        # 化学水
        waterTreatment = BiomassCHPWaterTreatment.search_water(
            plan_id)
        # 汽机辅机
        turbineAuxiliary = BiomasschpTurbineAuxiliary.search_turbine_auxiliary(
            plan_id)

        # 设备清单
        equipmentList = EquipmentList.search_equipmentList(plan_id)
        data = json.loads(equipmentList.equipment_content)
        equipmentCount = len(data['equipment_name'])

        for j in range(0, equipmentCount):
            if data['equipment_uid'][j] == '1':
                subText1 = gl.item_format(furnaceCalculation.f_steam_flow_design) + u't/h，'
                subText2 = gl.item_format(furnaceCalculation.f_steam_pressure_design) + u'MPa(g)/' + gl.item_format(furnaceCalculation.f_steam_temperature_design) + u'℃，'

                if furnaceCalculation.boiler_type is not None:
                    if furnaceCalculation.boiler_type == "1":
                        subText3 = u'循环流化床锅炉，露天布置/紧身封闭布置，'
                    elif furnaceCalculation.boiler_type == "2":
                        subText3 = u'高低差速循环流化床锅炉，露天布置/紧身封闭布置，'
                    elif furnaceCalculation.boiler_type == "3":
                        subText3 = u'联合炉排锅炉，露天布置/紧身封闭布置，'
                    elif furnaceCalculation.boiler_type == "4":
                        subText3 = u'水冷振动炉排锅炉，露天布置/紧身封闭布置，'
                    else:
                        subText3 = u""
                else:
                    subText3 = u""
                
                # subText4 = u'给水温度' + gl.item_format(furnaceCalculation.f_water_temperature_design) + u'℃，'
                # subText4 = u'给水温度' + str(float(furnaceCalculation.f_water_temperature_design)).rstrip('.0') + u'℃，'
                subText4 = u'给水温度' + gl.item_format(furnaceCalculation.f_water_temperature_design) + u'℃，'

                subText5 = u'锅炉效率' + gl.item_format(furnaceCalculation.f_boiler_efficiency_design) + u'%'
                data['equipment_content'][j] = subText1 + subText2 + subText3 + subText4 + subText5

            elif data['equipment_uid'][j] == '4':
                subText1 = u'V=' + gl.item_format(transportation.b_single_effective_volume_selected_design) + u'm3'
                data['equipment_content'][j] = subText1

                if transportation.b_bin_quantity_design is not None:
                    subText2 = str(int(transportation.b_bin_quantity_design))
                else:
                    subText2 = u'0'
                data['equipment_unit'][j] = subText2

            elif data['equipment_uid'][j] == '5':
                subText1 = gl.item_format(transportation.s_single_duplex_output_design) + u't/h'
                data['equipment_content'][j] = subText1

                if transportation.s_duplex_number_design is not None:
                    subText2 = str(int(transportation.s_duplex_number_design))
                else:
                    subText2 = u'0'
                data['equipment_unit'][j] = subText2

            elif data['equipment_uid'][j] == '6':
                subText1 = u'离心式，Q=' + gl.item_format(boilerAuxiliaries.sf_fan_select_flow) + u'm3/h，P=' + gl.item_format(boilerAuxiliaries.sf_fan_select_pressure) + u'Pa'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '7':
                if boilerAuxiliaries.sf_select_result is not None:
                    subText1 = boilerAuxiliaries.sf_select_result
                else:
                    subText1 = ""
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '8':
                subText1 = u'离心式，Q=' + gl.item_format(boilerAuxiliaries.ss_fan_select_flow) + u'm3/h，P=' + gl.item_format(boilerAuxiliaries.ss_fan_select_pressure) + u'Pa'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '9':
                if boilerAuxiliaries.ss_select_result is not None:
                    subText1 = boilerAuxiliaries.ss_select_result
                else:
                    subText1 = ""
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '10':
                subText1 = u'定速罗茨风机，Q=' + gl.item_format(boilerAuxiliaries.r_fan_select_flow) + u'm3/h，P=' + gl.item_format(boilerAuxiliaries.r_fan_select_pressure) + u'Pa'
                data['equipment_content'][j] = subText1           
            
            elif data['equipment_uid'][j] == '11':
                if boilerAuxiliaries.r_select_result is not None:
                    subText1 = boilerAuxiliaries.r_select_result
                else:
                    subText1 = ""
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '12':
                subText1 = u'离心式，Q=' + gl.item_format(boilerAuxiliaries.i_fan_select_flow) + u'm3/h，P=' + gl.item_format(boilerAuxiliaries.i_fan_select_pressure) + u'Pa'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '13':
                if boilerAuxiliaries.i_select_result is not None:
                    subText1 = boilerAuxiliaries.i_select_result
                else:
                    subText1 = ""
                data['equipment_content'][j] = subText1 
            
            elif data['equipment_uid'][j] == '14':
                subText1 = u'处理烟气量Q=' + gl.item_format(furnaceCalculation.d_entry_smoke_actual_flow_design) + u'm3/h，入口烟温t=' + gl.item_format(furnaceCalculation.d_entry_somke_temperature_design) + u'℃'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '15':
                subText1 = u'处理烟气量Q=' + gl.item_format(furnaceCalculation.d_entry_smoke_actual_flow_design) + u'm3/h，入口烟温t=' + gl.item_format(furnaceCalculation.d_entry_somke_temperature_design) + u'℃'
                subText2 = u'，效率≥' + gl.item_format(dasRemove.d_dust_remove_efficiency) + u'%'
                data['equipment_content'][j] = subText1 + subText2

            elif data['equipment_uid'][j] == '16':
                subText1 = u'DP-3.5/7.5，V=' + gl.item_format(boilerAuxiliaries.c_volume) + u'm3，工作压力' + gl.item_format(boilerAuxiliaries.c_work_pressure) + u'Mpa'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '17':
                subText1 = u'LP-1.5/3.5，V=' + gl.item_format(boilerAuxiliaries.r_volume) + u'm3，工作压力' + gl.item_format(boilerAuxiliaries.r_work_pressure) + u'Mpa'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '28':
                subText1 = u'高' + gl.item_format(chimney.chimney_height) + u'm，出口内径' + gl.item_format(chimney.chimney_outlet_inner_diameter) + u'm'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '29':
                if official.o_fuel_type == '1':
                    subText1 = u'燃生物质压块/颗粒棒启动锅炉，'
                elif official.o_fuel_type == '2':
                    subText1 = u'燃燃气/燃油启动锅炉，'
                else:
                    subText1 = u""

                if official.o_steam_volumn == '1':
                    subText2 = u'额定蒸发量2t/h，'
                elif official.o_steam_volumn == '2':
                    subText2 = u'额定蒸发量4t/h，'
                elif official.o_steam_volumn == '3':
                    subText2 = u'额定蒸发量6t/h，'
                else:
                    subText2 = u""

                if official.o_steam_parameter == '1':
                    subText3 = u'0.7MPa(g)/170℃，含配套风机、水泵等辅机'
                elif official.o_steam_parameter == '2':
                    subText3 = u'1.0MPa(g)/184℃，含配套风机、水泵等辅机'
                elif official.o_steam_parameter == '3':
                    subText3 = u'1.25MPa(g)/194℃，含配套风机、水泵等辅机'
                elif official.o_steam_parameter == '4':
                    subText3 = u'1.6MPa(g)/204℃℃，含配套风机、水泵等辅机'
                else:
                    subText3 = u''
            
                data['equipment_content'][j] = subText1 + subText2 + subText3

            elif data['equipment_uid'][j] == '31':
                if turbineBackpressure.e_exhaust_point_flow == 0:
                    subText1 = u'凝汽式汽轮机'
                    subText2 = u'N' + gl.item_format(turbineBackpressure.e_steam_extraction_select) + u'-' + gl.item_format(turbineBackpressure.e_steam_pressure) + \
                                u'/' + gl.item_format(turbineBackpressure.e_steam_temperature) + u'，'
                elif turbineBackpressure.e_exhaust_point_flow > 0:
                    subText1 = u'抽凝式汽轮机'
                    subText2 = u'C' + gl.item_format(turbineBackpressure.e_steam_extraction_select) + \
                                u'-' + gl.item_format(turbineBackpressure.e_steam_pressure) + u'/' + gl.item_format(turbineBackpressure.e_exhaust_point_pressure) + u'，'
                else:
                    subText1 = u'凝汽式/抽凝式汽轮机'
                    subText2 = u''

                data['equipment_name'][j] = subText1

                # subText2 = u'N' + gl.item_format(turbineBackpressure.e_steam_extraction_select) + u'-' + gl.item_format(turbineBackpressure.e_steam_pressure) + \
                #            u'/' + gl.item_format(turbineBackpressure.e_steam_temperature) + u'/C' + gl.item_format(turbineBackpressure.e_steam_extraction_select) + \
                #            u'-' + gl.item_format(turbineBackpressure.e_steam_pressure) + u'/' + gl.item_format(turbineBackpressure.e_exhaust_point_pressure) + u'，'

                subText3 = u'额定出力：' + gl.item_format(turbineBackpressure.e_steam_extraction_select) + u'MW，'
                subText4 = u'额定进汽压力：' + gl.item_format(turbineBackpressure.e_steam_pressure) + u'MPa(a)，'
                subText5 = u'额定进汽温度：' + gl.item_format(turbineBackpressure.e_steam_temperature) + u'℃，'
                subText6 = u'排汽压力：' + gl.item_format(turbineBackpressure.e_steam_exhaust_pressure) + u'MPa(a)'

                data['equipment_content'][j] = subText2 + subText3 + subText4 + subText5 + subText6

            elif data['equipment_uid'][j] == '32':
                subText1 = u'QFW-' + gl.item_format(turbineBackpressure.e_steam_extraction_select) + u'-2，'
                subText2 = u'额定功率：' + gl.item_format(turbineBackpressure.e_steam_extraction_select) + u'KW，'
                subText3 = u'额定功率：额定电压：10.5KV，额定转速：3000rpm，功率因素：0.8/0.85'

                data['equipment_content'][j] = subText1 + subText2 + subText3

            elif data['equipment_uid'][j] == '34':
                subText1 = u'Q=' + gl.item_format(boilerAuxiliaries.f_flow) + u't/h，H=' + gl.item_format(boilerAuxiliaries.f_pump_total_head)  + u'mH2O'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '35':
                subText1 = u'额定出力：' + gl.item_format(boilerAuxiliaries.f_boiler_evaporation) + u't/h，'
                subText2 = u'工作压力：' + gl.item_format(turbineBackpressure.d_work_pressure) + u'MPa(a)'

                if turbineBackpressure.h_amount is not None:
                    h_amount_display = turbineBackpressure.h_amount * 100
                else:
                    h_amount_display = u'0'
                subText3 = u'补充水率：' + gl.item_format(h_amount_display) + u'%'
                subText4 = u'平均进水温度：' + gl.item_format(turbineBackpressure.h_temperature) + u'℃'

                data['equipment_content'][j] = subText1 + subText2 + subText3 + subText4

            elif data['equipment_uid'][j] == '36':
                subText1 = u'有效容积：' + gl.item_format(boilerAuxiliaries.f_effective_volume) + u'm3，工作压力：' + gl.item_format(turbineBackpressure.d_work_pressure) + u'MPa(a)'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '37':
                subText1 = u'减压减温后蒸汽量：' + gl.item_format(boilerAuxiliaries.t_rudece_flow_rate) + u't/h，'
                subText2 = u'进出汽压力：' + gl.item_format(boilerAuxiliaries.t_new_pressure) + u'/' + gl.item_format(boilerAuxiliaries.t_reduce_steam_pressure) + u'MPa(a)，'
                subText3 = u'进出汽温度：' + gl.item_format(boilerAuxiliaries.t_new_steam_temperature) + u'/' + gl.item_format(boilerAuxiliaries.t_reduce_steam_temperature) + u'℃，'
                subText4 = u'减温水温度：' + gl.item_format(boilerAuxiliaries.t_reduce_water_temperature) + u'℃'

                data['equipment_content'][j] = subText1 + subText2 + subText3 + subText4

            elif data['equipment_uid'][j] == '38':
                subText1 = u'Q=' + gl.item_format(turbineAuxiliary.w_flow_amount) + u't/h，H='
                subText2 = gl.item_format(turbineAuxiliary.w_condensate_pump_lift) + u'mH2O，N='
                subText3 = gl.item_format(turbineAuxiliary.w_auxiliary_motor_power) + u'kW'

                data['equipment_content'][j] = subText1 + subText2 + subText3

            elif data['equipment_uid'][j] == '39':
                subText1 = u'Q=' + gl.item_format(turbineAuxiliary.f_flow_amount) + u't/h，H='
                subText2 = gl.item_format(turbineAuxiliary.f_total_lift) + u'mH2O，N='
                subText3 = gl.item_format(turbineAuxiliary.f_auxiliary_motor_power) + u'kW'

                data['equipment_content'][j] = subText1 + subText2 + subText3

            elif data['equipment_uid'][j] == '40':
                if turbineAuxiliary.c_flow_amount is not None:
                    f_flow_amount_display = turbineAuxiliary.c_flow_amount * 2
                else:
                    f_flow_amount_display = u'0'
                subText1 = u'V=' + gl.item_format(f_flow_amount_display) + u'm3'

                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '41':
                subText1 = u'Q=' + gl.item_format(turbineAuxiliary.f_flow_amount) + u'm3/h，H=XXMPa'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '49':
                if turbineBackpressure.s_lh_grade == 1:
                    data['equipment_unit'][j] = u'级数1'
                elif turbineBackpressure.s_lh_grade == 2:
                    data['equipment_unit'][j] = u'级数2'
                elif turbineBackpressure.s_lh_grade == 3:
                    data['equipment_unit'][j] = u'级数3'
                else:
                    data['equipment_unit'][j] = u'级数(1/2/3)'

            elif data['equipment_uid'][j] == '50':
                if turbineBackpressure.s_hh_grade == 0:
                    data['equipment_unit'][j] = u'级数0'
                elif turbineBackpressure.s_hh_grade == 1:
                    data['equipment_unit'][j] = u'级数1'
                elif turbineBackpressure.s_hh_grade == 2:
                    data['equipment_unit'][j] = u'级数2'
                else:
                    data['equipment_unit'][j] = u'级数(0/1/2)'

            elif data['equipment_uid'][j] == '68':
                subText1 = u'Q=' + gl.item_format(official.o_oil_pump) + u't/h，P=' + gl.item_format(official.o_oil_pump_pressure) + u'MPa'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '73':
                subText1 = u'V=' + gl.item_format(official.o_oil_can) + u'm3'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '75':
                subText1 = u'BCO1皮带输送机，B=' + gl.item_format(transportation.f_belt_width) + u'mm，'
                subText2 = u'提升角度α=XX°（一般为16~22°），带速' + gl.item_format(transportation.f_belt_speed) + u'm/s，'
                subText3 = u'皮带出力Q=' + gl.item_format(transportation.f_feeding_output_selected_design) + u't/h，55kW，水平投影L=180m，胶带总长度380m'

                data['equipment_content'][j] = subText1 + subText2 + subText3

            elif data['equipment_uid'][j] == '76':
                subText1 = u'V=' + gl.item_format(transportation.t_single_effective_volume_selected_design) + u'm3'
                data['equipment_content'][j] = subText1

                if transportation.t_bin_quantity_design is not None:
                    subText2 = str(int(transportation.t_bin_quantity_design))
                else:
                    subText2 = u'0'
                data['equipment_unit'][j] = subText2

            elif data['equipment_uid'][j] == '77':
                subText1 = u'Q=' + gl.item_format(transportation.f_single_duplex_output_design) + u't/h'
                data['equipment_content'][j] = subText1

                if transportation.f_duplex_number_design is not None:
                    subText2 = str(int(transportation.f_duplex_number_design))
                else:
                    subText2 = u'0'
                data['equipment_unit'][j] = subText2

            elif data['equipment_uid'][j] == '78':
                subText1 = u'5kW，适应带宽' + gl.item_format(transportation.f_belt_width) + u'mm'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '79':
                subText1 = u'系统累计误差≤%%p0.25，称量范围5~5000t/h，皮带宽度' + gl.item_format(transportation.f_belt_width) + u'mm，皮带速度' + gl.item_format(transportation.f_belt_speed) + u'm/s，出力Q=' + gl.item_format(transportation.f_feeding_output_selected_design) + u't/h'
                data['equipment_content'][j] = subText1
            
            elif data['equipment_uid'][j] == '81':
                subText1 = u'带宽B=' + gl.item_format(transportation.f_belt_width) + u'mm，带速' + gl.item_format(transportation.f_belt_speed) + u'm/s'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '90':
                subText1 = u'出力:' + gl.item_format(dasRemove.s_yns_output) + u't/h，冷却水量：' + gl.item_format(dasRemove.s_coolwater) + u't/h，驱动装置：7.5kW'
                data['equipment_content'][j] = subText1

                if dasRemove.s_yns_number is not None:
                    subText2 = str(int(dasRemove.s_yns_number))
                else:
                    subText2 = u'0'
                data['equipment_unit'][j] = subText2

            elif data['equipment_uid'][j] == '91':
                subText1 = u'出力:' + gl.item_format(dasRemove.s_conveyor_output) + u't/h，驱动装置：5.5kW'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '92':
                subText1 = u'出力:' + gl.item_format(dasRemove.s_conveyor_output) + u't/h，驱动装置：5.5kW'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '93':
                subText1 = u'V=' + gl.item_format(dasRemove.s_volumn) + u'm3'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '95':
                subText1 = u'正常出力' + gl.item_format(dasRemove.s_yns_output) + u't/h，最大出力15t/h，槽宽≥1200mm，投影长度19m'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '109':
                subText1 = u'有效容积V=' + gl.item_format(dasRemove.a_volumn) + u'm3'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '121':
                subText1 = u'冷却面积：' + gl.item_format(circulatingWater.p_select_f) + u'm2，△t=8～12℃'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '123':
                subText1 = u'逆流式，处理水量' + gl.item_format(circulatingWater.p_select_s) + u'm3/h，N=XXkW，U=380V'
                data['equipment_content'][j] = subText1

                if circulatingWater.p_count is not None:
                    subText2 = str(int(circulatingWater.p_count))
                else:
                    subText2 = u'0'
                data['equipment_unit'][j] = subText2

            elif data['equipment_uid'][j] == '124':
                subText1 = u'Q=' + gl.item_format(circulatingWater.c_flow) + u'm3/h，'
                subText2 = u'H=' + gl.item_format(circulatingWater.c_pumping_head) + u'm，'
                subText3 = u'P=' + gl.item_format(circulatingWater.c_supporting_motor_power) + u'kW，R=990r/min，10kV/380V'
                data['equipment_content'][j] = subText1 + subText2 + subText3

            elif data['equipment_uid'][j] == '160':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 0.95 / 0.85 / 2
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'产水量' + gl.item_format(o_boiler_water_system_display) + u'm3/h'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '161':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 0.95 / 0.85 / 0.75 / 2
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'Q=' + gl.item_format(o_boiler_water_system_display) + u'm3/h，H=130-140 m；U=380V'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '162':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 0.95 / 0.85 * 1
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'V=' + gl.item_format(o_boiler_water_system_display) + u'm3'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '163':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 0.95 / 0.85 / 2
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'Q=' + gl.item_format(o_boiler_water_system_display) + u'm3/h，U=380V'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '164':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 0.95 / 2
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'产水量' + gl.item_format(o_boiler_water_system_display) + u'm3/h'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '165':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 0.95 / 0.85 / 0.75 / 2
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'Q=' + gl.item_format(o_boiler_water_system_display) + u'm3/h，H=130-140 m；U=380V'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '166':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 0.95 * 1
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'V=' + gl.item_format(o_boiler_water_system_display) + u'm3'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '167':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 0.95 / 2
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'Q=' + gl.item_format(o_boiler_water_system_display) + u'm3/h，U=380V'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '168':
                if waterTreatment.o_boiler_water_system is not None:
                    o_boiler_water_system_display = float(waterTreatment.o_boiler_water_system) / 2
                else:
                    o_boiler_water_system_display = u'0'
                subText1 = u'产水量' + gl.item_format(o_boiler_water_system_display) + u'm3/h'
                data['equipment_content'][j] = subText1

            elif data['equipment_uid'][j] == '169':
                if waterTreatment.o_salt_water_tank is not None:
                    o_salt_water_tank_display = float(waterTreatment.o_salt_water_tank) / 2
                else:
                    o_salt_water_tank_display = u'0'
                subText1 = u'V=' + gl.item_format(o_salt_water_tank_display) + u'm3'
                data['equipment_content'][j] = subText1

            else:
                pass

        equipmentList.equipment_content = json.dumps(data)
        EquipmentList.insert_equipmentList(equipmentList)


class ToBiomassCHP():
    '''
    根据planId返回当前方案的主要设备参数字符串
    '''
    def getMainEquipmentPara(self, planId):

        furnace = BiomassCHPBoilerCalculation.search_furnace_calculation(planId)
        turbine = BiomassCHPTurbineBackpressure.search_turbineBackpressure(planId)
        mainEquipmentPara = u''

        if furnace.f_steam_flow_design is not None and furnace.pressure_temperature is not None and furnace.boiler_type is not None:
            mainEquipmentPara += u'1X' + gl.getstrcolm(furnace.f_steam_flow_design) + u't/h'

            if furnace.pressure_temperature == "1":
                mainEquipmentPara += u'高温高压'
            elif furnace.pressure_temperature == "2":
                mainEquipmentPara += u'次高温次高压'
            elif furnace.pressure_temperature == "3":
                mainEquipmentPara += u'中温中压'
            else:
                pass

            if furnace.boiler_type == "1":
                mainEquipmentPara += u'常规循环流化床锅炉（CFB）\n'
            elif furnace.boiler_type == "2":
                mainEquipmentPara += u'高低差速循环流化床锅炉（ICFB）\n'
            elif furnace.boiler_type == "3":
                mainEquipmentPara += u'联合炉排炉\n'
            elif furnace.boiler_type == "4":
                mainEquipmentPara += u'水冷振动炉排炉\n'
            else:
                pass

        if turbine.e_steam_extraction_select is not None and turbine.e_steam_type is not None and turbine.s_steam_type_test is not None:
            mainEquipmentPara += u'1X' + gl.getstrcolm(turbine.e_steam_extraction_select) + u'MW'

            if turbine.e_steam_type == "1":
                mainEquipmentPara += u'低温低压'
            elif turbine.e_steam_type == "2":
                mainEquipmentPara += u'次中温次中压'
            elif turbine.e_steam_type == "3":
                mainEquipmentPara += u'中温中压'
            elif turbine.e_steam_type == "4":
                mainEquipmentPara += u'次高温次高压'
            elif turbine.e_steam_type == "5":
                mainEquipmentPara += u'高温高压'
            else:
                pass

            if turbine.s_steam_type_test == 1:
                mainEquipmentPara += u'抽凝汽轮发电机组'
            elif turbine.s_steam_type_test == 2:
                mainEquipmentPara += u'背压汽轮发电机组'
            elif turbine.s_steam_type_test == 3:
                mainEquipmentPara += u'补凝汽轮发电机组'
            else:
                pass
        if mainEquipmentPara == u'':
            return None
        else:
            return mainEquipmentPara

    
    @staticmethod
    def create_plan(companyName, planName, companyLocation, company_lnglat):
        # 新增公司信息
        company = Company.query.filter_by(company_name=companyName).first()
        if not company:
            company = Company()
            company.company_name = companyName
            Company.insert_company(company)
        newCompany = Company.query.filter_by(company_name=companyName).first()
        companyId = newCompany.id
        # 创建方案
        plan = Plan.query.filter_by(
            company_id=companyId, module_id=Module.biomassCHP, plan_name=planName).first()
        if not plan:
            plan = Plan()
            plan.plan_name = planName
            plan.user_id = current_user.id
            plan.company_id = companyId
            plan.module_id = Module.biomassCHP
            plan.plan_create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            plan.plan_update_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            plan.company_lnglat = company_lnglat
            Plan.insert_plan(plan)
        plan.company_location = companyLocation
        newPlan = Plan.query.filter_by(
            company_id=companyId, module_id=Module.biomassCHP, plan_name=planName).first()
        return newPlan.id

    # 修改方案表的修改时间
    @staticmethod
    def update_plan_date(plan_id):
        plan = Plan.query.filter_by(id=plan_id).first()
        plan.plan_update_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Plan.insert_plan(plan)

    @staticmethod
    def to_questionnaire(form, plan_id):
        questionnaire = BiomassCHPNeedsQuestionnaire.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(lists)):
            if form.get(lists[index]) != '':
                setattr(questionnaire, lists[index], form.get(lists[index]))
            else:
                setattr(questionnaire, lists[index], None)
        setattr(questionnaire, 's_fuel_design', form.get('s_fuel_design'))
        setattr(questionnaire, 's_fuel_check', form.get('s_fuel_check'))
        setattr(questionnaire, 't_steam_time', form.get('t_steam_time'))
        setattr(questionnaire, 't_hhl_heating_occasions_type', form.get('t_hhl_heating_occasions_type'))
        return questionnaire

    @staticmethod
    def to_questionnaireJson(questionnaire):
        datas = {}
        planId = getattr(questionnaire, 'plan_id')
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        for index in range(len(lists)):
            datas[lists[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(questionnaire, lists[index])))
        datas['s_fuel_design'] = getattr(questionnaire, 's_fuel_design')
        datas['s_fuel_check'] = getattr(questionnaire, 's_fuel_check')
        datas['t_steam_time'] = getattr(questionnaire, 't_steam_time')
        datas['t_hhl_heating_occasions_type'] = getattr(questionnaire, 't_hhl_heating_occasions_type')
        datas['company_name'] = companyName
        datas['company_location'] = companyLocation
        datas['planId'] = planId
        datas['plan_name'] = plan.plan_name
        return datas

    #返回锅炉页面初期值
    @staticmethod
    def to_furnaceJson(furnace):
        datas = {}
        for index in range(len(list_column_furnace)):
            datas[list_column_furnace[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(furnace, list_column_furnace[index])))
        datas['p_heater_type_design'] = getattr(furnace, 'p_heater_type_design')
        datas['p_heater_type_check'] = getattr(furnace, 'p_heater_type_check')
        return datas

    #获得锅炉页面表单的信息
    @staticmethod
    def to_furnace(form, plan_id):
        furnace = BiomassCHPBoilerCalculation.query.filter_by(
            plan_id=plan_id).first()

        #熵焓值计算
        furnace = Furnace_calculationBefore().specialCalculation(furnace, form)
        #先从list中移除熵焓项目
        list_column_furnace.remove('f_steam_enthalpy_design')
        list_column_furnace.remove('f_steam_enthalpy_check')

        list_column_furnace.remove('a_saturation_pressure_design')
        list_column_furnace.remove('a_saturation_pressure_check')

        list_column_furnace.remove('f_water_enthalpy_design')
        list_column_furnace.remove('f_water_enthalpy_check')

        list_column_furnace.remove('f_saturated_water_enthalpy_design')
        list_column_furnace.remove('f_saturated_water_enthalpy_check')

        for index in range(len(list_column_furnace)):
            if form.get(list_column_furnace[index]) != '':
                setattr(furnace, list_column_furnace[index],
                        form.get(list_column_furnace[index]))
            else:
                setattr(furnace, list_column_furnace[index],
                        None)

        setattr(furnace, 'plan_id', plan_id)
        setattr(furnace, 'p_heater_type_design', form.get('p_heater_type_design'))
        setattr(furnace, 'p_heater_type_check', form.get('p_heater_type_check'))

        #给list中的熵焓项目赋值
        list_column_furnace.append('f_steam_enthalpy_design')
        list_column_furnace.append('f_steam_enthalpy_check')

        list_column_furnace.append('a_saturation_pressure_design')
        list_column_furnace.append('a_saturation_pressure_check')

        list_column_furnace.append('f_water_enthalpy_design')
        list_column_furnace.append('f_water_enthalpy_check')

        list_column_furnace.append('f_saturated_water_enthalpy_design')
        list_column_furnace.append('f_saturated_water_enthalpy_check')
        return furnace

    #返回存储运输页面初期值
    @staticmethod
    def to_sorttranJson(sorttran):
        datas = {}
        for index in range(len(list_column_sorttran)):
            datas[list_column_sorttran[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(sorttran, list_column_sorttran[index])))

        return datas

    #获得存储运输页面表单的信息
    @staticmethod
    def to_stortran(form, plan_id):
        stortran = BiomassCHPFuelStorageTransportation.query.filter_by(
            plan_id=plan_id).first()

        # 从锅炉计算表中，获得锅炉额定容量，判断皮带输送机采用单路或双路布置
        boilerData = BiomassCHPBoilerCalculation.search_furnace_calculation(plan_id)
        boilerFlow = getattr(boilerData, 'f_steam_flow_design')
        if boilerFlow != "" or boilerFlow != None :
            if boilerFlow <= 65:
                beltNumber = 1
            else:
                beltNumber = 2
        else:
            beltNumber = None

        setattr(stortran, 'f_belt_number', beltNumber)

        for index in range(len(list_column_sorttran)):
            if form.get(list_column_sorttran[index]) != '':
                setattr(stortran, list_column_sorttran[index],
                        form.get(list_column_sorttran[index]))
            else:
                setattr(stortran, list_column_sorttran[index],
                        None)

        return stortran


    #返回脱硫脱销页面初期值
    @staticmethod
    def to_desuldenitJson(desuldenit):
        datas = {}
        for index in range(len(list_column_desuldenit)):
            datas[list_column_desuldenit[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(desuldenit, list_column_desuldenit[index])))
        return datas

    #获得脱硫脱销页面表单的信息
    @staticmethod
    def to_desuldenit(form, plan_id):
        desuldenit = BiomassCHPDesulfurizationAndDenitrification.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_desuldenit)):
            if form.get(list_column_desuldenit[index]) != '':
                setattr(desuldenit, list_column_desuldenit[index],
                        form.get(list_column_desuldenit[index]))
            else:
                setattr(desuldenit, list_column_desuldenit[index],
                        None)
        return desuldenit


    #返回除尘除灰页面初期值
    @staticmethod
    def to_dasRemoveJson(dasremove):
        datas = {}
        for index in range(len(list_column_dasremove)):
            datas[list_column_dasremove[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(dasremove, list_column_dasremove[index])))
        return datas

    #获得除尘除灰页面表单的信息
    @staticmethod
    def to_dasRemove(form, plan_id):
        dasremove = BiomassCHPDASRemove.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_dasremove)):
            if form.get(list_column_dasremove[index]) != '':
                setattr(dasremove, list_column_dasremove[index],
                        form.get(list_column_dasremove[index]))
            else:
                setattr(dasremove, list_column_dasremove[index],
                        None)
        return dasremove


    #返回锅炉辅机页面初期值
    @staticmethod
    def to_auxiliariesJson(auxiliaries):
        datas = {}
        for index in range(len(list_column_auxiliaries)):
            if list_column_auxiliaries[index] == 's_de_ox_pressure':
                datas[list_column_auxiliaries[index]] = format_value3(
                    # TODO还未过滤特殊字符项
                    "number", str(getattr(auxiliaries, list_column_auxiliaries[index])))
            else:
                datas[list_column_auxiliaries[index]] = format_value(
                    # TODO还未过滤特殊字符项
                    "number", str(getattr(auxiliaries, list_column_auxiliaries[index])))

        # 选型结果赋值
        datas['sf_select_result'] = getattr(auxiliaries, 'sf_select_result')
        datas['ss_select_result'] = getattr(auxiliaries, 'ss_select_result')
        datas['i_select_result'] = getattr(auxiliaries, 'i_select_result')
        datas['r_select_result'] = getattr(auxiliaries, 'r_select_result')
        datas['f_pump_selection'] = getattr(auxiliaries, 'f_pump_selection')

        return datas

    #获得锅炉辅机页面表单的信息
    @staticmethod
    def to_auxiliaries(form, plan_id):
        auxiliaries = BiomassCHPBoilerAuxiliaries.query.filter_by(
            plan_id=plan_id).first()

        #熵焓值计算
        auxiliaries = Auxiliaries_calculationBefore().specialCalculation(auxiliaries, form)
        #先从list中移除熵焓项目
        list_column_auxiliaries.remove('r_work_aturatedwater_enthalpy')
        list_column_auxiliaries.remove('r_work_latentheat_vaporization')
        list_column_auxiliaries.remove('c_work_aturatedwater_enthalpy')
        list_column_auxiliaries.remove('c_work_steam_pecificvolume')
        list_column_auxiliaries.remove('c_work_latentheat_vaporization')
        list_column_auxiliaries.remove('t_rudece_flow_rate')
        list_column_auxiliaries.remove('t_reduce_enough_enthalpy')
        list_column_auxiliaries.remove('t_reduce_steam_enthalpy')
        list_column_auxiliaries.remove('t_reduce_water_flow_rate')
        list_column_auxiliaries.remove('t_reduce_water_enthalpy')
        list_column_auxiliaries.remove('t_reduce_water_pressure')
        list_column_auxiliaries.remove('t_new_enthalpy')
        list_column_auxiliaries.remove('s_local_atmosphere_density')
        list_column_auxiliaries.remove('s_design_flux')
        list_column_auxiliaries.remove('s_pump_install_height')

        list_column_auxiliaries.remove('charging_saturation_water_enthalpy')
        list_column_auxiliaries.remove('exothermic_saturation_water_enthalpy')
        list_column_auxiliaries.remove('charging_saturation_steam_enthalpy')
        list_column_auxiliaries.remove('exothermic_saturation_steam_enthalpy')
        list_column_auxiliaries.remove('p2_steam_amount')
        list_column_auxiliaries.remove('charging_water_specific_volume')
        list_column_auxiliaries.remove('unit_water_heat_amount')
        list_column_auxiliaries.remove('regenerarot_volume')
        list_column_auxiliaries.remove('regenerarot_top_steam_volume')
        list_column_auxiliaries.remove('regenerarot_max_bleed')
        list_column_auxiliaries.remove('evaporation_capacity')
        list_column_auxiliaries.remove('charging_volume')
        list_column_auxiliaries.remove('exothermic_water_specific_volume')
        list_column_auxiliaries.remove('exothermic_water_volume')


        for index in range(len(list_column_auxiliaries)):
            if form.get(list_column_auxiliaries[index]) != '':
                setattr(auxiliaries, list_column_auxiliaries[index],
                        form.get(list_column_auxiliaries[index]))
            else:
                setattr(auxiliaries, list_column_auxiliaries[index],
                        None)

        # 给选型结果赋值
        setattr(auxiliaries, 'sf_select_result', form.get('sf_select_result'))
        setattr(auxiliaries, 'ss_select_result', form.get('ss_select_result'))
        setattr(auxiliaries, 'i_select_result', form.get('i_select_result'))
        setattr(auxiliaries, 'r_select_result', form.get('r_select_result'))
        setattr(auxiliaries, 'f_pump_selection', form.get('f_pump_selection'))


        #给list中的熵焓项目赋值
        list_column_auxiliaries.append('r_work_aturatedwater_enthalpy')
        list_column_auxiliaries.append('r_work_latentheat_vaporization')
        list_column_auxiliaries.append('c_work_aturatedwater_enthalpy')
        list_column_auxiliaries.append('c_work_steam_pecificvolume')
        list_column_auxiliaries.append('c_work_latentheat_vaporization')
        list_column_auxiliaries.append('t_rudece_flow_rate')
        list_column_auxiliaries.append('t_reduce_enough_enthalpy')
        list_column_auxiliaries.append('t_reduce_steam_enthalpy')
        list_column_auxiliaries.append('t_reduce_water_flow_rate')
        list_column_auxiliaries.append('t_reduce_water_enthalpy')
        list_column_auxiliaries.append('t_reduce_water_pressure')
        list_column_auxiliaries.append('t_new_enthalpy')
        list_column_auxiliaries.append('s_local_atmosphere_density')
        list_column_auxiliaries.append('s_design_flux')
        list_column_auxiliaries.append('s_pump_install_height')

        list_column_auxiliaries.append('charging_saturation_water_enthalpy')
        list_column_auxiliaries.append('exothermic_saturation_water_enthalpy')
        list_column_auxiliaries.append('charging_saturation_steam_enthalpy')
        list_column_auxiliaries.append('exothermic_saturation_steam_enthalpy')
        list_column_auxiliaries.append('p2_steam_amount')
        list_column_auxiliaries.append('charging_water_specific_volume')
        list_column_auxiliaries.append('unit_water_heat_amount')
        list_column_auxiliaries.append('regenerarot_volume')
        list_column_auxiliaries.append('regenerarot_top_steam_volume')
        list_column_auxiliaries.append('regenerarot_max_bleed')
        list_column_auxiliaries.append('evaporation_capacity')
        list_column_auxiliaries.append('charging_volume')
        list_column_auxiliaries.append('exothermic_water_specific_volume')
        list_column_auxiliaries.append('exothermic_water_volume')

        return auxiliaries


    #返回化学水处理页面初期值
    @staticmethod
    def to_waterJson(water):
        datas = {}
        for index in range(len(list_column_water)):
            datas[list_column_water[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(water, list_column_water[index])))

        return datas

    #获得化学水处理页面表单的信息
    @staticmethod
    def to_water(form, plan_id):
        water = BiomassCHPWaterTreatment.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_water)):
            if form.get(list_column_water[index]) != '':
                setattr(water, list_column_water[index],
                        form.get(list_column_water[index]))
            else:
                setattr(water, list_column_water[index],
                        None)

        # 查询凝结水回收率和抽汽点流量，来计算外供汽损失
        questionnaire = BiomassCHPNeedsQuestionnaire.search_questionnaire(plan_id)
        waterRecoveryRate = getattr(questionnaire, 't_condensate_water_recovery_rate')
        steam = BiomassCHPTurbineBackpressure.search_turbineBackpressure(plan_id)
        pointFlow = getattr(steam, 'e_exhaust_point_flow')

        #if pointFlow != None or pointFlow != '':
        if pointFlow >= 0:
                externalSupplyLoss = pointFlow * (1 - waterRecoveryRate/100)
                setattr(water, 'o_external_supply_loss', externalSupplyLoss)

        return water


    #返回公用工程页面初期值
    @staticmethod
    def to_officialJson(official):
        datas = {}
        for index in range(len(list_column_official)):

            datas[list_column_official[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(official, list_column_official[index])))
        datas['o_fire_way'] = getattr(official, 'o_fire_way')
        datas['o_install_way'] = getattr(official, 'o_install_way')
        datas['o_furnace_type'] = getattr(official, 'o_furnace_type')
        return datas

    #获得公用工程页面表单的信息
    @staticmethod
    def to_official(form, plan_id):
        official = BiomassCHPOfficialProcess.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_official)):
            if form.get(list_column_official[index]) != '':
                setattr(official, list_column_official[index],
                        form.get(list_column_official[index]))
            else:
                setattr(official, list_column_official[index],
                        None)

        setattr(official, 'o_fire_way', form.get('o_fire_way'))
        setattr(official, 'o_install_way', form.get('o_install_way'))
        setattr(official, 'o_furnace_type', form.get('o_furnace_type'))
        return official


    #返回采暖供热页面初期值
    @staticmethod
    def to_heatJson(heat):
        datas = {}
        for index in range(len(list_column_heat)):
            datas[list_column_heat[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(heat, list_column_heat[index])))

        return datas

    #获得采暖供热页面表单的信息
    @staticmethod
    def to_heat(form, plan_id):
        heat = BiomassCHPHeatSupply.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_heat)):
            if form.get(list_column_heat[index]) != '':
                setattr(heat, list_column_heat[index],
                        form.get(list_column_heat[index]))
            else:
                setattr(heat, list_column_heat[index],
                        None)
        return heat


    #返回供油泵所需要的数据
    @staticmethod
    def to_oilPumpJson(datas):
        datasNew = {}
        datasNew['c_low_calorific_value_estimation_design'] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(datas, 'c_low_calorific_value_estimation_design')))

        datasNew['f_boiler_consumption_design'] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(datas, 'f_boiler_consumption_design')))

        return datasNew


    #返回汽轮机页面初期值
    @staticmethod
    def to_steamJson(steamturbine):
        datas = {}
        for index in range(len(list_column_steam)):
            if list_column_steam[index] == 'e_steam_exhaust_pressure' or list_column_steam[index] == 'c_work_pressure':
                datas[list_column_steam[index]] = format_value2(
                # TODO还未过滤特殊字符项
                "number", str(getattr(steamturbine, list_column_steam[index])))
            else: 
                datas[list_column_steam[index]] = format_value3(
                # TODO还未过滤特殊字符项
                "number", str(getattr(steamturbine, list_column_steam[index])))


        datas['e_steam_type'] = getattr(steamturbine, 'e_steam_type')
        datas['h_assume'] = getattr(steamturbine, 'h_assume')
        datas['s_parameter_flg'] = getattr(steamturbine, 's_parameter_flg')
        datas['s_steam_type_test'] = getattr(steamturbine, 's_steam_type_test')
        datas['s_temperature_pressure'] = getattr(steamturbine, 's_temperature_pressure')
        datas['s_hh_grade'] = getattr(steamturbine, 's_hh_grade')
        datas['s_lh_grade'] = getattr(steamturbine, 's_lh_grade')
        return datas

    #清理汽轮机旧记录
    @staticmethod
    def steamClear(plan_id):
        steam = BiomassCHPTurbineBackpressure.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_steamClear)):
            setattr(steam, list_column_steamClear[index],
                            None)
        return steam


    #获得汽轮机页面表单的信息
    @staticmethod
    def to_steam(form, plan_id):
        steam = BiomassCHPTurbineBackpressure.query.filter_by(
            plan_id=plan_id).first()

        # if getattr(steam, 's_parameter_flg') == '1':
        for index in range(len(list_column_steam)):
            if list_column_steam[index] != 'hh1_water_temperature':
                if form.get(list_column_steam[index]) != '':
                    setattr(steam, list_column_steam[index],
                            form.get(list_column_steam[index]))
                else:
                    setattr(steam, list_column_steam[index],
                            None)
        # 清理页面上的旧记录
        for index in range(len(list_column_steamClear)):
            setattr(steam, list_column_steamClear[index],
                            None)
        
        if form.get('s_temperature_pressure') != "" and form.get('s_temperature_pressure') != None:
            setattr(steam, 's_temperature_pressure', form.get('s_temperature_pressure'))
            setattr(steam, 's_hh_grade', form.get('s_hh_grade'))
            setattr(steam, 's_lh_grade', form.get('s_lh_grade'))

            # 汽轮机类型没有变更
            if getattr(steam,'s_steam_type_test') == None:
                setattr(steam, 's_steam_type_test', form.get('s_steam_type_test'))
            else:
                if float(form.get('s_steam_type_test')) == float(getattr(steam,'s_steam_type_test')):
                    setattr(steam, 's_steam_type_test', form.get('s_steam_type_test'))

        setattr(steam, 'e_steam_type', form.get('e_steam_type'))
        setattr(steam, 'h_assume', form.get('h_assume'))

        pointPower, steam = turbine_foctory.Factory().execute(steam, form)

        # 汽轮机类型变更
        if getattr(steam,'s_steam_type_test') != None:
            if float(form.get('s_steam_type_test')) != float(getattr(steam,'s_steam_type_test')):
                setattr(steam, 's_steam_type_test', form.get('s_steam_type_test'))

        return pointPower, steam

    #返回烟囱Json值
    @staticmethod
    def to_ChimneyJson(Chimney):
        json = {}
        for index in range(len(list_column_chimney)):
            json[list_column_chimney[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(Chimney, list_column_chimney[index])))
        return json

    @staticmethod
    def to_ChimneyData(form, plan_id):
        chimneyData = BiomassCHPChimney.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_chimney)):
            if form.get(list_column_chimney[index]) != '':
                setattr(chimneyData, list_column_chimney[index],
                        form.get(list_column_chimney[index]))
            else:
                setattr(chimneyData, list_column_chimney[index],
                        None)
        return chimneyData

    # 循环水
    @staticmethod
    def to_circulatingWaterJson(circulatingWater, plan_id):
        datas = {}
        for index in range(len(list_column_circulatingWater)):
            # if list_column_circulatingWater[index] in ['v_steam_exhaust_flow_winter', 'v_steam_exhaust_flow_summer']:
            #     if list_column_circulatingWater[index] == 'v_steam_exhaust_flow_winter':
            #         furnace = BiomassCHPBoilerCalculation.query.filter_by(
            #             plan_id=plan_id).first()
            #         steam = BiomassCHPTurbineBackpressure.query.filter_by(
            #             plan_id=plan_id).first()
            #         if furnace.f_steam_flow_design and steam.hh1_extraction_amount and steam.hh2_extraction_amount and steam.d_extraction_amount and steam.lh1_extraction_amount and steam.lh2_extraction_amount and steam.e_exhaust_point_flow:
            #             v_steam_exhaust_flow_winter = float(furnace.f_steam_flow_design)*0.97-float(steam.hh1_extraction_amount)-float(steam.hh2_extraction_amount)-float(steam.d_extraction_amount)-float(steam.lh1_extraction_amount)-float(steam.lh2_extraction_amount)-float(steam.e_exhaust_point_flow)
            #             v_steam_exhaust_flow_summer = float(furnace.f_steam_flow_design)*0.97-float(steam.hh1_extraction_amount)-float(steam.hh2_extraction_amount)-float(steam.d_extraction_amount)-float(steam.lh1_extraction_amount)-float(steam.lh2_extraction_amount)-float(steam.e_exhaust_point_flow)+10
            #             circulatingWater.v_steam_exhaust_flow_winter = v_steam_exhaust_flow_winter
            #             circulatingWater.v_steam_exhaust_flow_summer = v_steam_exhaust_flow_summer
            #         else:
            #             v_steam_exhaust_flow_winter = getattr(circulatingWater, list_column_circulatingWater[index])
            #             v_steam_exhaust_flow_summer = getattr(circulatingWater, 'v_steam_exhaust_flow_summer')
            #         datas[list_column_circulatingWater[index]] = format_value(
            #             "number",
            #             str(v_steam_exhaust_flow_winter))
            #         datas['v_steam_exhaust_flow_summer'] = format_value(
            #             "number",
            #             str(v_steam_exhaust_flow_summer))
            # else:
            #     datas[list_column_circulatingWater[index]] = format_value(
            #         "number",
            #         str(
            #             getattr(circulatingWater, list_column_circulatingWater[
            #                 index])))
             datas[list_column_circulatingWater[index]] = format_value(
                    "number",
                    str(
                        getattr(circulatingWater, list_column_circulatingWater[
                            index])))
        return datas

    @staticmethod
    def to_circulatingWater(form, plan_id):
        circulatingWater = BiomassCHPCirculatingWater.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_circulatingWater)):
            if form.get(list_column_circulatingWater[index]) != '':
                setattr(circulatingWater, list_column_circulatingWater[index],
                        form.get(list_column_circulatingWater[index]))
            else:
                setattr(circulatingWater, list_column_circulatingWater[index],
                        None)
        setattr(circulatingWater, 'plan_id', plan_id)
        return circulatingWater


    # 汽机辅机
    @staticmethod
    def to_turbineAuxiliaryJson(turbineAuxiliary, plan_id):
        datas = {}
        for index in range(len(list_column_turbineAuxiliary)):
            if list_column_turbineAuxiliary[index] == 'm_condenser_pressure' or list_column_turbineAuxiliary[index] == 'w_condenser_higter':
                datas[list_column_turbineAuxiliary[index]] = format_value2(
                # TODO还未过滤特殊字符项
                "number", str(getattr(turbineAuxiliary, list_column_turbineAuxiliary[index])))
            else:
                datas[list_column_turbineAuxiliary[index]] = format_value(
                    "number",
                    str(
                        getattr(turbineAuxiliary, list_column_turbineAuxiliary[
                            index])))


        datas['w_select'] = getattr(turbineAuxiliary, 'w_select')
        datas['f_select'] = getattr(turbineAuxiliary, 'f_select')
        datas['c_select'] = getattr(turbineAuxiliary, 'c_select')

        return datas

    @staticmethod
    def to_turbineAuxiliary(form, plan_id):
        turbineAuxiliary = BiomasschpTurbineAuxiliary.query.filter_by(
            plan_id=plan_id).first()
        turbineAuxiliary = BiomassTurbineAuxiliaryBefore().specialCalculation(turbineAuxiliary, form)
        list_column_turbineAuxiliary.remove('m_saturation_temperature')
        list_column_turbineAuxiliary.remove('m_condensate_enthalpy')
        for index in range(len(list_column_turbineAuxiliary)):
            if form.get(list_column_turbineAuxiliary[index]) != '':
                setattr(turbineAuxiliary, list_column_turbineAuxiliary[index],
                        form.get(list_column_turbineAuxiliary[index]))
            else:
                setattr(turbineAuxiliary, list_column_turbineAuxiliary[index],
                        None)
        setattr(turbineAuxiliary, 'plan_id', plan_id)
        setattr(turbineAuxiliary, 'w_select', form.get('w_select'))
        setattr(turbineAuxiliary, 'f_select', form.get('f_select'))
        setattr(turbineAuxiliary, 'c_select', form.get('c_select'))

        list_column_turbineAuxiliary.append('m_saturation_temperature')
        list_column_turbineAuxiliary.append('m_condensate_enthalpy')
        return turbineAuxiliary


    # 判断项目类型 生物质发电或生物质热电联产
    @staticmethod
    def IsBiomass(plan_id):
        steamturbine = BiomassCHPTurbineBackpressure.query.filter_by(
            plan_id=plan_id).first()
        exhaust_point_flow = getattr(steamturbine, 'e_exhaust_point_flow')

        if exhaust_point_flow == 0:
            IsBiomassFlg = False
        else:
            IsBiomassFlg = True
        
        return IsBiomassFlg


    @staticmethod
    def sortPressure(steamturbine):
        dict_group_check = [
            [float(steamturbine.i_high1_pressure) if steamturbine.i_high1_pressure else 0,
            'i_high1_pressure',
            'i_high1_entropy',
            'i_high1_temperature',
            'i_high1_enthalpy',
            'i_high1_flow',
            'i_steam_hh1_power',
            'HH1',
            u'1#高压'
            ],

            [float(steamturbine.i_high2_pressure) if steamturbine.i_high2_pressure else 0,
            'i_high2_pressure',
            'i_high2_entropy',
            'i_high2_temperature',
            'i_high2_enthalpy',
            'i_high2_flow',
            'i_hh1_hh2_power',
            'HH2',
             u'2#高压'
            ],

            [float(steamturbine.i_deoxidize_pressure) if steamturbine.i_deoxidize_pressure else 0,
            'i_deoxidize_pressure',
            'i_deoxidize_entropy',
            'i_deoxidize_temperature',
            'i_deoxidize_enthalpy',
            'i_deoxidize_flow',
            'i_hh2_deoxidize_power',
            'D',
            u'D除氧'
            ],

            [float(steamturbine.i_exhaust_point_pressure) if steamturbine.i_exhaust_point_pressure else 0,
            'i_exhaust_point_pressure',
            'i_exhaust_point_temperature',
            'i_exhaust_point_entropy',
            'i_exhaust_point_enthalpy',
            'i_exhaust_point_flow',
            'i_deoxidize_exhaust_power',
            u'抽汽点',
            u'抽汽点'],

            [float(steamturbine.i_low1_pressure) if steamturbine.i_low1_pressure else 0,
            'i_low1_pressure',
            'i_low1_entropy',
            'i_low1_temperature',
            'i_low1_enthalpy',
            'i_low1_flow',
            'i_exhaust_lh1_power',
            'LH1',
            u'1#低加'
            ],

            [float(steamturbine.i_low2_pressure) if steamturbine.i_low2_pressure else 0,
            'i_low2_pressure',
            'i_low2_entropy',
            'i_low2_temperature',
            'i_low2_enthalpy',
            'i_low2_flow',
            'i_lh1_lh2_power',
            'LH2',
            u'2#低加'
            ],

            [float(steamturbine.i_low3_pressure) if steamturbine.i_low3_pressure else 0,
            'i_low3_pressure',
            'i_low3_entropy',
            'i_low3_temperature',
            'i_low3_enthalpy',
            'i_low3_flow',
            'i_lh2_lh3_power',
            'LH3',
            u'3#低加'
            ]
        ]

        array_group_check = []
        for item in dict_group_check:
            if not (item[0] is None or item[0] == '' or item[0] == 0):
                array_group_check.append(item)

        array_group_check.sort(cmp=lambda x, y: cmp(y[0], x[0]))

        for item in array_group_check:
            if array_group_check.index(item) == 0:
                item.append(u'主蒸汽至' + item[len(item) - 2] + u'功率')
            else:
                titleFrom = array_group_check[array_group_check.index(item) - 1][len(item) - 2]
                titleTo = item[len(item) - 2]

                if steamturbine.s_steam_type_test == 3:
                    if titleFrom.find(u"抽汽点") != -1:
                        titleFrom = titleFrom.replace(u"抽汽点", u"补汽点")
                    if titleTo.find(u"抽汽点") != -1:
                        titleTo = titleTo.replace(u"抽汽点", u"补汽点")
                
                # item.append(u'' + array_group_check[array_group_check.index(item) - 1][len(item) - 2] + u'至' + item[len(item) - 2] + u'功率')
                item.append(u'' + titleFrom + u'至' + titleTo + u'功率')

        front_page_list = []
        for item in array_group_check:
            front_page_list.append(item)

        return array_group_check


    #返回主要技术经济指标处理页面初期值
    @staticmethod
    def to_economicJson(economic):
        datas = {}
        for index in range(len(list_column_economic)):
            datas[list_column_economic[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(economic, list_column_economic[index])))

        return datas

    #获得主要技术经济指标页面表单的信息
    @staticmethod
    def to_economic(form, plan_id):
        economic = BiomasschpEconomicIndicators.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_economic)):
                if form.get(list_column_economic[index]) != '':
                    setattr(economic, list_column_economic[index],
                            form.get(list_column_economic[index]))
                else:
                    setattr(economic, list_column_economic[index],
                            None)
        # 表单项目计算
        economic = economic_foctory.Factory().execute(economic, form)

        return economic

    # 选择燃料种类
    @staticmethod
    def to_fuelCHPComponentJson(id):
        datas = {}
        biomassCHPComponent = BiomassCHPFuelComponent.search_biomassCHPSort(id)
        datas['s_carbon'] = biomassCHPComponent.carbon
        datas['s_hydrogen'] = biomassCHPComponent.hydrogen
        datas['s_oxygen'] = biomassCHPComponent.oxygen
        datas['s_nitrogen'] = biomassCHPComponent.nitrogen
        datas['s_sulfur'] = biomassCHPComponent.sulfur
        datas['s_water'] = biomassCHPComponent.water
        datas['s_daf'] = biomassCHPComponent.daf
        datas['s_grey'] = biomassCHPComponent.grey
        datas['s_grindability'] = biomassCHPComponent.grindability
        datas['s_low'] = biomassCHPComponent.low
        return datas

    # 选择燃料种类
    @staticmethod
    def to_fuelCHPComponentJson2(id):
        datas = {}
        biomassCHPComponent = BiomassCHPFuelComponent.search_biomassCHPSort(id)
        datas['carbon'] = biomassCHPComponent.carbon
        datas['hydrogen'] = biomassCHPComponent.hydrogen
        datas['oxygen'] = biomassCHPComponent.oxygen
        datas['nitrogen'] = biomassCHPComponent.nitrogen
        datas['sulfur'] = biomassCHPComponent.sulfur
        datas['water'] = biomassCHPComponent.water
        datas['daf'] = biomassCHPComponent.daf
        datas['grey'] = biomassCHPComponent.grey
        datas['grindability'] = biomassCHPComponent.grindability
        datas['low'] = biomassCHPComponent.low
        return datas

    #获得燃料数据
    @staticmethod
    def to_fuel(form):
        #新增的场合
        if form.get("s_fuel_new") != "":
            fuelData = BiomassCHPFuelComponent()
            fuelData.name = form.get("s_fuel_new")
            fuelData.carbon = form.get("carbon")
            fuelData.hydrogen = form.get("hydrogen")
            fuelData.oxygen = form.get("oxygen")
            fuelData.nitrogen = form.get("nitrogen")
            fuelData.sulfur = form.get("sulfur")
            fuelData.water = form.get("water")
            fuelData.daf = form.get("daf")
            fuelData.grey = form.get("grey")
            fuelData.grindability = form.get("grindability")
            fuelData.low = form.get("low")
        #修正的场合
        else:
            fuelData = BiomassCHPFuelComponent.search_biomassCHPSort(form.get("s_fuel_design"))

            for index in range(len(list_column_fuel)):
                if form.get(list_column_fuel[index]) != '':
                    setattr(fuelData, list_column_fuel[index],
                            form.get(list_column_fuel[index]))
                else:
                    setattr(fuelData, list_column_fuel[index],
                            "")

        return fuelData
 
    # 报告中设备清单标题出力
    @staticmethod
    def getmdtitledict(planId):
        mdtitledict = {"a": u"一、锅炉及其辅助设备",
                       "b": u"二、汽轮机及其辅助设备",
                       "c": u"三、点火油系统",
                       "d": u"四、燃料供应系统",
                       "e": u"五、除渣系统",
                       "e1": u"方案（一）：机械干法除渣",
                       "e2": u"方案（二）：机械湿法捞渣",
                       "f": u"六、除灰系统",
                       "g": u"七、压缩空气系统",
                       "h": u"八、供排水系统",
                       "h11": u"（一）循环水系统 ：自然通风",
                       "h12": u"（一）循环水系统 ：强制通风",
                       "h2": u"（二）补给水系统",
                       "h3": u"（三）排水系统",
                       "h4": u"（四）消防系统",
                       "h5": u"（五）其它设备",
                       "i": u"九、化学水处理系统",
                       "i1": u"（一）原水预处理部分",
                       "i2": u"（二）锅炉补给水处理系统",
                       "i3": u"（三）化学加药处理系统",
                       "i4": u"（四）水汽取样系统",
                       "i5": u"（五）循环水加药系统",
                       "i6": u"（六）循环水补水软化装置",
                       "i7": u"（七）实验室仪器仪表",
                       "j": u"十、电气系统",
                       "j1": u"（一）电气一次部分",
                       "j2": u"（二）电气110kV户内GIS装备",
                       "j3": u"（三）电气二次部分",
                       "k": u"十一、热工控制系统",
                       "k1": u"（一）DCS部分",
                       "k2": u"（二）锅炉部分",
                       "k3": u"（三）汽机部分",
                       "k4": u"（四）公用部分" 
                       }
        mdtitledict2 = {"a": u"一、锅炉及其辅助设备",
                       "b": u"二、汽轮机及其辅助设备",
                       "d": u"三、燃料供应系统",
                       "e": u"四、除渣系统",
                       "e1": u"方案（一）：机械干法除渣",
                       "e2": u"方案（二）：机械湿法捞渣",
                       "f": u"五、除灰系统",
                       "g": u"六、压缩空气系统",
                       "h": u"七、供排水系统",
                       "h11": u"（一）循环水系统 ：自然通风",
                       "h12": u"（一）循环水系统 ：强制通风",
                       "h2": u"（二）补给水系统",
                       "h3": u"（三）排水系统",
                       "h4": u"（四）消防系统",
                       "h5": u"（五）其它设备",
                       "i": u"八、化学水处理系统",
                       "i1": u"（一）原水预处理部分",
                       "i2": u"（二）锅炉补给水处理系统",
                       "i3": u"（三）化学加药处理系统",
                       "i4": u"（四）水汽取样系统",
                       "i5": u"（五）循环水加药系统",
                       "i6": u"（六）循环水补水软化装置",
                       "i7": u"（七）实验室仪器仪表",
                       "j": u"九、电气系统",
                       "j1": u"（一）电气一次部分",
                       "j2": u"（二）电气110kV户内GIS装备",
                       "j3": u"（三）电气二次部分",
                       "k": u"十、热工控制系统",
                       "k1": u"（一）DCS部分",
                       "k2": u"（二）锅炉部分",
                       "k3": u"（三）汽机部分",
                       "k4": u"（四）公用部分" 
                       }
        # 锅炉
        furnaceCalculation = BiomassCHPBoilerCalculation.search_furnace_calculation(
            planId)

        if furnaceCalculation.boiler_type == "1" or furnaceCalculation.boiler_type == "2":
            return mdtitledict2
        else:
            return mdtitledict

   # 设备清单模板中标题出力
    @staticmethod
    def getTitleTemplate():
        mdtitledict = {"a": u"一、锅炉及其辅助设备",
                       "b": u"二、汽轮机及其辅助设备",
                       "c": u"三、点火油系统",
                       "d": u"四、燃料供应系统",
                       "e": u"五、除渣系统",
                       "e1": u"方案（一）：机械干法除渣",
                       "e2": u"方案（二）：机械湿法捞渣",
                       "f": u"六、除灰系统",
                       "g": u"七、压缩空气系统",
                       "h": u"八、供排水系统",
                       "h11": u"（一）循环水系统 ：自然通风",
                       "h12": u"（一）循环水系统 ：强制通风",
                       "h2": u"（二）补给水系统",
                       "h3": u"（三）排水系统",
                       "h4": u"（四）消防系统",
                       "h5": u"（五）其它设备",
                       "i": u"九、化学水处理系统",
                       "i1": u"（一）原水预处理部分",
                       "i2": u"（二）锅炉补给水处理系统",
                       "i3": u"（三）化学加药处理系统",
                       "i4": u"（四）水汽取样系统",
                       "i5": u"（五）循环水加药系统",
                       "i6": u"（六）循环水补水软化装置",
                       "i7": u"（七）实验室仪器仪表",
                       "j": u"十、电气系统",
                       "j1": u"（一）电气一次部分",
                       "j2": u"（二）电气110kV户内GIS装备",
                       "j3": u"（三）电气二次部分",
                       "k": u"十一、热工控制系统",
                       "k1": u"（一）DCS部分",
                       "k2": u"（二）锅炉部分",
                       "k3": u"（三）汽机部分",
                       "k4": u"（四）公用部分" 
                       }
        return mdtitledict

    @staticmethod
    def saveEquipmentList(uidData, nameData, typeData, contentData, unitData, countData, remarkData):
        Equipment = None
        try:
            Equipment = EquipmentListTemplate.search_EquipmentListTemplate(Module.biomassCHP)

            uidElementArray = uidData.split('&')
            uidElementList = []
            for formElement in uidElementArray:
                uidElementList.append(formElement.split('='))

            nameElementArray = nameData.split('&')
            nameElementList = []
            for formElement in nameElementArray:
                nameElementList.append(formElement.split('='))

            typeElementArray = typeData.split('&')
            typeElementList = []
            for formElement in typeElementArray:
                typeElementList.append(formElement.split('='))

            contenteElementArray = contentData.split('&')
            contentElementList = []
            for formElement in contenteElementArray:
                contentElementList.append(formElement.split('='))

            unitElementArray = unitData.split('&')
            unitElementList = []
            for formElement in unitElementArray:
                unitElementList.append(formElement.split('='))

            countElementArray = countData.split('&')
            countElementList = []
            for formElement in countElementArray:
                countElementList.append(formElement.split('='))

            remarkElementArray = remarkData.split('&')
            remarkElementList = []
            for formElement in remarkElementArray:
                remarkElementList.append(formElement.split('='))

            decode_equipment_uid_list = []
            decode_equipment_name_list = []
            decode_equipment_type_list = []
            decode_equipment_content_list = []
            decode_equipment_unit_list = []
            decode_equipment_count_list = []
            decode_equipment_remark_list = []

            for index in range(len(uidElementList)):
                equipment_uid_value = uidElementList[index][1]
                decode_equipment_uid_value = urllib.unquote(str(equipment_uid_value)).decode('utf-8')
                decode_equipment_uid_list.append(decode_equipment_uid_value)

            for index in range(len(nameElementList)):
                equipment_name_value = nameElementList[index][1]
                decode_equipment_name_value = urllib.unquote(str(equipment_name_value)).decode('utf-8')
                decode_equipment_name_list.append(decode_equipment_name_value)

            for index in range(len(typeElementList)):
                equipment_type_value = typeElementList[index][1]
                decode_equipment_type_value = urllib.unquote(str(equipment_type_value)).decode('utf-8')
                decode_equipment_type_list.append(decode_equipment_type_value)
            
            for index in range(len(contentElementList)):
                equipment_content_value = contentElementList[index][1]
                decode_equipment_content_value = urllib.unquote(str(equipment_content_value)).decode('utf-8')
                decode_equipment_content_list.append(decode_equipment_content_value)

            for index in range(len(unitElementList)):
                equipment_unit_value = unitElementList[index][1]
                decode_equipment_unit_value = urllib.unquote(str(equipment_unit_value)).decode('utf-8')
                decode_equipment_unit_list.append(decode_equipment_unit_value)

            for index in range(len(countElementList)):
                equipment_count_value = countElementList[index][1]
                decode_equipment_count_value = urllib.unquote(str(equipment_count_value)).decode('utf-8')
                decode_equipment_count_list.append(decode_equipment_count_value)
            
            for index in range(len(remarkElementList)):
                equipment_remark_value = remarkElementList[index][1]
                decode_equipment_remark_value = urllib.unquote(str(equipment_remark_value)).decode('utf-8')
                decode_equipment_remark_list.append(decode_equipment_remark_value)

            equipment_json = json.loads(Equipment.equipment_template)
            equipment_json[u'equipment_uid'] = decode_equipment_uid_list
            equipment_json[u'equipment_name'] = decode_equipment_name_list
            equipment_json[u'equipment_type'] = decode_equipment_type_list
            equipment_json[u'equipment_content'] = decode_equipment_content_list
            equipment_json[u'equipment_unit'] = decode_equipment_unit_list
            equipment_json[u'equipment_count'] = decode_equipment_count_list
            equipment_json[u'equipment_remark'] = decode_equipment_remark_list

            Equipment.equipment_template = json.dumps(equipment_json)
            EquipmentListTemplate.insert_EquipmentListTemplate(Equipment)
        except Exception:
            Equipment = None
            return Equipment
        else:
            return Equipment