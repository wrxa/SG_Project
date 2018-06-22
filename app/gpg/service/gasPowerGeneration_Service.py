# -*- coding: utf-8 -*-
from app.gpg.model.gasPowerGeneration_models import GasPowerGenerationNeedsQuestionnaire,\
    GPGBoilerOfPTS, GPGTurbineOfPTS, GPGFlueGasAirSystem, GPGSmokeResistance, \
    GPGWindResistance, GPGCirculatingWaterSystem, GPGSmokeAirCalculate, \
    GPGTurbineAuxiliarySystem, GPGSteamWaterPipe, GPGBoilerAuxiliaries, \
    GasPowerGenerationEconomicIndicators
from flask_login import current_user
from app.models import Company, Plan, Module
from datetime import datetime
import time
import sys
from app.gpg.service.execution_strategy import GPG_TurbineOfPts_EXEC
from app.main.service.turbine import turbine_foctory
from app.gpg.service import economic_foctory
from app.gpg.service.imgdealwith import gpgImgListResult
from util.get_all_path import GetPath
from app.gpg.model.imgEntity import ImgDict
import os


list_turbine_of_pts = [
    # 's_parameter_flg',
    # 's_steam_type_test', 
    # 's_temperature_pressure',
    # 's_hh_grade', 
    # 's_lh_grade', 
    'e_turbine_efficiency',
    'e_mechanical_efficiency', 
    'e_generator_efficiency', 
    # 'e_steam_type',
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
    # 'h_assume', 
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
    'hh3_water_enthalpy', 'hh3_top_difference',
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

list_boiler_auxiliaries = [
    'r_boiler_evaporation', 'r_emission_time', 'r_emission_rate',
    'r_sewage_quantity', 'r_drum_pressure', 'r_drum_aturatedwater_enthalpy',
    'r_work_pressure', 'r_work_aturatedwater_enthalpy','r_work_steam_special_volume',
    'r_work_latentheat_vaporization', 'r_work_steam_dryness', 'r_ultimate_strength',
    'r_vaporization_capacity', 'r_affluence_coefficient', 'r_steam_volume', 'r_volume', 'r_specifications',
    'c_boiler_evaporation', 'c_emission_rate', 'c_sewage_quantity',
    'c_drum_pressure', 'c_drum_aturatedwater_enthalpy', 'c_work_pressure',
    'c_work_aturatedwater_enthalpy', 'c_work_steam_pecificvolume',
    'c_work_latentheat_vaporization', 'c_steam_dryness', 'c_ultimate_strength',
    'c_vaporization_capacity', 'c_affluence_coefficient', 'c_steam_volume', 'c_volume',
    'c_specifications', 'd_boiler_watersystem_volume', 'd_phosphate_content',
    'd_water_hardness', 'd_purity', 'd_boiler_dosage_startup',
    'd_boiler_water_supply', 'd_boiler_sewage_quantity', 'd_boiler_dosage_run',
    'd_na3po4_concentration', 'd_na3po4_density', 'd_solution_quantity_run',
    'p_boiler_design_pressure', 'p_inlet_pressure', 'p_deaerator_pressure',
    'p_water_supply_resistance', 'p_water_inlet_resistance',
    'p_center_altitude_difference', 'p_deaerator_altitude_difference',
    'p_feedpump_total_head', 'p_flow', 'p_pump_efficiency',
    'p_transmission_efficiency', 'p_motor_efficiency',
    'p_motor_reserve_factor', 'p_auxiliary_motor_power', 'p_specifications',
    'm_boiler_evaporation', 'm_makeup_steam', 'm_steamwater_cycle_loss',
    'm_pollution_loss', 'm_condensing_capacity', 'm_condensate_loss',
    'm_boiler_normal_watersupply', 'm_boiler_desalted_water_rate',
    'm_boiler_desalted_work_cycle', 'm_boiler_desalted_rebirth_time', 'm_increase_loss',
    'm_boiler_max_watersupply', 'm_boiler_watersupply_all', 'm_boiler_watersupply_specifications',
    's_boiler_evaporation', 's_storage_time',
    's_volume', 's_size_length', 's_size_diameter', 's_max_feedwater_amount',
    's_de_ox_pressure', 's_local_atmosphere', 's_local_atmosphere_density',
    's_design_flux', 's_net_positive_suction_head', 's_total_resistance',
    's_inlet_speed', 's_added_height', 's_pump_install_height',
    'desalted_water_tech_type', 'desalted_water_tech_name',
    'new_steam_temperature', 'new_steam_pressure', 'new_steam_enthalpy', 
    'new_steam_flux', 'desuperheater_water_temperature', 'desuperheater_water_pressure',
    'desuperheater_water_enthalpy', 'desuperheater_water_flux', 'desuperheater_steam_temperature', 
    'desuperheater_steam_pressure', 'desuperheater_steam_enthalpy', 'saturation_water_enthalpy',
    'no_vaporized_percent', 'de_press_temp_device_flux',
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

list_steam_water_pipe = [
    'main_steam_design_pressure_m', 'main_steam_design_pressure_c',
    'main_steam_design_temperature_m', 'main_steam_design_temperature_c',
    'main_steam_steel_m', 'main_steam_steel_c',
    'main_steam_temperature_stress_c', 'main_steam_20c_stress_c',
    'main_steam_nominal_pressure_c', 'main_steam_pipe_mass_flow_c',
    'main_steam_selected_velocity_c', 'main_steam_meida_specific_volume_c',
    'main_steam_inner_diamete_c',
    'main_steam_temperature_correct_coefficient_c',
    'main_steam_stress_correct_coefficient_c',
    'main_steam_additional_thickness_c', 'main_steam_pipe_min_thickness_c',
    'main_steam_negative_deviation_coefficient_c',
    'main_steam_negative_deviation_added_value_c',
    'main_steam_calculate_thickness_c',
    'main_steam_calculate_outer_diameter_c',
    'main_steam_selected_nominal_diameter_c',
    'main_steam_selected_outer_diameter_c', 'main_steam_selected_thickness_c',
    'main_steam_selected_inner_diameter_c',
    'main_steam_backstepping_velocity_c', 'main_steam_selected_pipe_spec_c',
    'main_steam_work_press_m', 'main_steam_work_press_c',
    'main_steam_work_temperature_m', 'main_steam_work_temperature_c',
    'main_steam_rated_flow_m', 'main_steam_rated_flow_c', 'main_steam_msv_m',
    'main_steam_msv_c', 'main_steam_media_viscosity_m',
    'main_steam_media_viscosity_c', 'main_steam_velocity_m',
    'main_steam_velocity_c', 'main_steam_calculate_velocity_m',
    'main_steam_calculate_velocity_c', 'main_steam_dynamic_head_m',
    'main_steam_dynamic_head_c', 'main_steam_pipe_outer_diameter_m',
    'main_steam_pipe_outer_diameter_c', 'main_steam_pipe_thickness_m',
    'main_steam_pipe_thickness_c', 'main_steam_pipe_inner_diameter_m',
    'main_steam_pipe_inner_diameter_c', 'main_steam_friction_resistance_m',
    'main_steam_friction_resistance_c', 'main_steam_reynolds_m',
    'main_steam_reynolds_c', 'main_steam_equivalent_roughness_m',
    'main_steam_equivalent_roughness_c', 'main_steam_relative_roughness_m',
    'main_steam_relative_roughness_c', 'main_steam_resistance_coefficient_m',
    'main_steam_resistance_coefficient_c',
    'main_steam_unit_length_resistance_m',
    'main_steam_unit_length_resistance_c', 'main_steam_pipe_length_m',
    'main_steam_pipe_length_c', 'deoxidized_steam_work_press',
    'deoxidized_steam_work_temperature', 'deoxidized_steam_rated_flow',
    'deoxidized_steam_msv', 'deoxidized_steam_media_viscosity',
    'deoxidized_steam_velocity', 'deoxidized_steam_calculate_velocity',
    'deoxidized_steam_dynamic_head', 'deoxidized_steam_pipe_outer_diameter',
    'deoxidized_steam_pipe_thickness', 'deoxidized_steam_pipe_inner_diameter',
    'deoxidized_steam_friction_resistance', 'deoxidized_steam_reynolds',
    'deoxidized_steam_equivalent_roughness',
    'deoxidized_steam_relative_roughness',
    'deoxidized_steam_resistance_coefficient',
    'deoxidized_steam_unit_length_resistance', 'deoxidized_steam_pipe_length',
    'l_feedwater_work_press_m', 'l_feedwater_work_press_c',
    'l_feedwater_work_temperature_m', 'l_feedwater_work_temperature_c',
    'l_feedwater_rated_flow_m', 'l_feedwater_rated_flow_c',
    'l_feedwater_msv_m', 'l_feedwater_msv_c', 'l_feedwater_media_viscosity_m',
    'l_feedwater_media_viscosity_c', 'l_feedwater_velocity_m',
    'l_feedwater_velocity_c', 'l_feedwater_calculate_velocity_m',
    'l_feedwater_calculate_velocity_c', 'l_feedwater_dynamic_head_m',
    'l_feedwater_dynamic_head_c', 'l_feedwater_pipe_outer_diameter_m',
    'l_feedwater_pipe_outer_diameter_c', 'l_feedwater_pipe_thickness_m',
    'l_feedwater_pipe_thickness_c', 'l_feedwater_pipe_inner_diameter_m',
    'l_feedwater_pipe_inner_diameter_c', 'l_feedwater_friction_resistance_m',
    'l_feedwater_friction_resistance_c', 'l_feedwater_reynolds_m',
    'l_feedwater_reynolds_c', 'l_feedwater_equivalent_roughness_m',
    'l_feedwater_equivalent_roughness_c', 'l_feedwater_relative_roughness_m',
    'l_feedwater_relative_roughness_c', 'l_feedwater_resistance_coefficient_m',
    'l_feedwater_resistance_coefficient_c',
    'l_feedwater_unit_length_resistance_m',
    'l_feedwater_unit_length_resistance_c', 'l_feedwater_pipe_length_m',
    'l_feedwater_pipe_length_c', 'l_feedwater_local_resistance_m',
    'l_feedwater_local_resistance_c',
    'l_feedwater_total_local_resistance_coefficient_m',
    'l_feedwater_total_local_resistance_coefficient_c',
    'l_feedwater_elbow_resistance_coefficient_m',
    'l_feedwater_elbow_resistance_coefficient_c', 'l_feedwater_elbow_spec_m',
    'l_feedwater_elbow_spec_c', 'l_feedwater_elbow_radius_m',
    'l_feedwater_elbow_radius_c',
    'l_feedwater_elbow_radius_to_inner_diameter_m',
    'l_feedwater_elbow_radius_to_inner_diameter_c',
    'l_feedwater_90elbow_resistance_coefficient_m',
    'l_feedwater_90elbow_resistance_coefficient_c',
    'l_feedwater_90elbow_count_m', 'l_feedwater_90elbow_count_c',
    'l_feedwater_triplet_resistance_coefficient_m',
    'l_feedwater_triplet_resistance_coefficient_c',
    'l_feedwater_single_triplet_resistance_coefficient_m',
    'l_feedwater_single_triplet_resistance_coefficient_c',
    'l_feedwater_triplet_count_m', 'l_feedwater_triplet_count_c',
    'l_feedwater_reducer_resistance_coefficient_m',
    'l_feedwater_reducer_resistance_coefficient_c',
    'l_feedwater_converging_resistance_coefficient_m',
    'l_feedwater_converging_resistance_coefficient_c',
    'l_feedwater_converging_spec_m', 'l_feedwater_converging_spec_c',
    'l_feedwater_converging_angle_m', 'l_feedwater_converging_angle_c',
    'l_feedwater_converging_diameter_radio_m',
    'l_feedwater_converging_diameter_radio_c',
    'l_feedwater_increasing_resistance_coefficient_m',
    'l_feedwater_increasing_resistance_coefficient_c',
    'l_feedwater_increasing_spec_m', 'l_feedwater_increasing_spec_c',
    'l_feedwater_increasing_angle_m', 'l_feedwater_increasing_angle_c',
    'l_feedwater_increasing_diameter_radio_m',
    'l_feedwater_increasing_diameter_radio_c',
    'l_feedwater_in_out_resistance_coefficient_m',
    'l_feedwater_in_out_resistance_coefficient_c',
    'l_feedwater_valve_resistance_coefficient_m',
    'l_feedwater_valve_resistance_coefficient_c', 'l_feedwater_filter_m',
    'l_feedwater_filter_c', 'l_feedwater_sluice_resistance_coefficient_m',
    'l_feedwater_sluice_resistance_coefficient_c',
    'l_feedwater_single_sluice_resistance_coefficient_m',
    'l_feedwater_single_sluice_resistance_coefficient_c',
    'l_feedwater_sluice_count_m', 'l_feedwater_sluice_count_c',
    'l_feedwater_check_resistance_coefficient_m',
    'l_feedwater_check_resistance_coefficient_c',
    'l_feedwater_single_check_resistance_coefficient_m',
    'l_feedwater_single_check_resistance_coefficient_c',
    'l_feedwater_check_count_m', 'l_feedwater_check_count_c',
    'l_feedwater_regulating_resistance_coefficient_m',
    'l_feedwater_regulating_resistance_coefficient_c',
    'l_feedwater_plate_resistance_coefficient_m',
    'l_feedwater_plate_resistance_coefficient_c',
    'l_feedwater_measuring_pressure_loss_m',
    'l_feedwater_measuring_pressure_loss_c', 'h_feedwater_work_press_m',
    'h_feedwater_work_press_c', 'h_feedwater_work_temperature_m',
    'h_feedwater_work_temperature_c', 'h_feedwater_rated_flow_m',
    'h_feedwater_rated_flow_c', 'h_feedwater_msv_m', 'h_feedwater_msv_c',
    'h_feedwater_media_viscosity_m', 'h_feedwater_media_viscosity_c',
    'h_feedwater_velocity_m', 'h_feedwater_velocity_c',
    'h_feedwater_calculate_velocity_m', 'h_feedwater_calculate_velocity_c',
    'h_feedwater_dynamic_head_m', 'h_feedwater_dynamic_head_c',
    'h_feedwater_pipe_outer_diameter_m', 'h_feedwater_pipe_outer_diameter_c',
    'h_feedwater_pipe_thickness_m', 'h_feedwater_pipe_thickness_c',
    'h_feedwater_pipe_inner_diameter_m', 'h_feedwater_pipe_inner_diameter_c',
    'h_feedwater_friction_resistance_m', 'h_feedwater_friction_resistance_c',
    'h_feedwater_reynolds_m', 'h_feedwater_reynolds_c',
    'h_feedwater_equivalent_roughness_m', 'h_feedwater_equivalent_roughness_c',
    'h_feedwater_relative_roughness_m', 'h_feedwater_relative_roughness_c',
    'h_feedwater_resistance_coefficient_m',
    'h_feedwater_resistance_coefficient_c',
    'h_feedwater_unit_length_resistance_m',
    'h_feedwater_unit_length_resistance_c', 'h_feedwater_pipe_length_m',
    'h_feedwater_pipe_length_c', 'h_feedwater_local_resistance_m',
    'h_feedwater_local_resistance_c',
    'h_feedwater_total_local_resistance_coefficient_m',
    'h_feedwater_total_local_resistance_coefficient_c',
    'h_feedwater_elbow_resistance_coefficient_m',
    'h_feedwater_elbow_resistance_coefficient_c', 'h_feedwater_elbow_spec_m',
    'h_feedwater_elbow_spec_c', 'h_feedwater_elbow_radius_m',
    'h_feedwater_elbow_radius_c',
    'h_feedwater_elbow_radius_to_inner_diameter_m',
    'h_feedwater_elbow_radius_to_inner_diameter_c',
    'h_feedwater_90elbow_resistance_coefficient_m',
    'h_feedwater_90elbow_resistance_coefficient_c',
    'h_feedwater_90elbow_count_m', 'h_feedwater_90elbow_count_c',
    'h_feedwater_triplet_resistance_coefficient_m',
    'h_feedwater_triplet_resistance_coefficient_c',
    'h_feedwater_single_triplet_resistance_coefficient_m',
    'h_feedwater_single_triplet_resistance_coefficient_c',
    'h_feedwater_triplet_count_m', 'h_feedwater_triplet_count_c',
    'h_feedwater_reducer_resistance_coefficient_m',
    'h_feedwater_reducer_resistance_coefficient_c',
    'h_feedwater_converging_resistance_coefficient_m',
    'h_feedwater_converging_resistance_coefficient_c',
    'h_feedwater_converging_spec_m', 'h_feedwater_converging_spec_c',
    'h_feedwater_converging_angle_m', 'h_feedwater_converging_angle_c',
    'h_feedwater_converging_diameter_radio_m',
    'h_feedwater_converging_diameter_radio_c',
    'h_feedwater_increasing_resistance_coefficient_m',
    'h_feedwater_increasing_resistance_coefficient_c',
    'h_feedwater_increasing_spec_m', 'h_feedwater_increasing_spec_c',
    'h_feedwater_increasing_angle_m', 'h_feedwater_increasing_angle_c',
    'h_feedwater_increasing_diameter_radio_m',
    'h_feedwater_increasing_diameter_radio_c',
    'h_feedwater_in_out_resistance_coefficient_m',
    'h_feedwater_in_out_resistance_coefficient_c',
    'h_feedwater_valve_resistance_coefficient_m',
    'h_feedwater_valve_resistance_coefficient_c', 'h_feedwater_filter_m',
    'h_feedwater_filter_c', 'h_feedwater_sluice_resistance_coefficient_m',
    'h_feedwater_sluice_resistance_coefficient_c',
    'h_feedwater_single_sluice_resistance_coefficient_m',
    'h_feedwater_single_sluice_resistance_coefficient_c',
    'h_feedwater_sluice_count_m', 'h_feedwater_sluice_count_c',
    'h_feedwater_check_resistance_coefficient_m',
    'h_feedwater_check_resistance_coefficient_c',
    'h_feedwater_single_check_resistance_coefficient_m',
    'h_feedwater_single_check_resistance_coefficient_c',
    'h_feedwater_check_count_m', 'h_feedwater_check_count_c',
    'h_feedwater_regulating_resistance_coefficient_m',
    'h_feedwater_regulating_resistance_coefficient_c',
    'h_feedwater_plate_resistance_coefficient_m',
    'h_feedwater_plate_resistance_coefficient_c',
    'h_feedwater_measuring_pressure_loss_m',
    'h_feedwater_measuring_pressure_loss_c', 'pump_in_work_press_m',
    'pump_in_work_press_c', 'pump_in_work_temperature_m',
    'pump_in_work_temperature_c', 'pump_in_rated_flow_m',
    'pump_in_rated_flow_c', 'pump_in_msv_m', 'pump_in_msv_c',
    'pump_in_media_viscosity_m', 'pump_in_media_viscosity_c',
    'pump_in_velocity_m', 'pump_in_velocity_c', 'pump_in_calculate_velocity_m',
    'pump_in_calculate_velocity_c', 'pump_in_dynamic_head_m',
    'pump_in_dynamic_head_c', 'pump_in_pipe_outer_diameter_m',
    'pump_in_pipe_outer_diameter_c', 'pump_in_pipe_thickness_m',
    'pump_in_pipe_thickness_c', 'pump_in_pipe_inner_diameter_m',
    'pump_in_pipe_inner_diameter_c', 'pump_in_friction_resistance_m',
    'pump_in_friction_resistance_c', 'pump_in_reynolds_m', 'pump_in_reynolds_c',
    'pump_in_equivalent_roughness_m', 'pump_in_equivalent_roughness_c',
    'pump_in_relative_roughness_m', 'pump_in_relative_roughness_c',
    'pump_in_resistance_coefficient_m', 'pump_in_resistance_coefficient_c',
    'pump_in_unit_length_resistance_m', 'pump_in_unit_length_resistance_c',
    'pump_in_pipe_length_m', 'pump_in_pipe_length_c',
    'pump_in_local_resistance_m', 'pump_in_local_resistance_c',
    'pump_in_total_local_resistance_coefficient_m',
    'pump_in_total_local_resistance_coefficient_c',
    'pump_in_elbow_resistance_coefficient_m',
    'pump_in_elbow_resistance_coefficient_c', 'pump_in_elbow_spec_m',
    'pump_in_elbow_spec_c', 'pump_in_elbow_radius_m', 'pump_in_elbow_radius_c',
    'pump_in_elbow_radius_to_inner_diameter_m',
    'pump_in_elbow_radius_to_inner_diameter_c',
    'pump_in_90elbow_resistance_coefficient_m',
    'pump_in_90elbow_resistance_coefficient_c', 'pump_in_90elbow_count_m',
    'pump_in_90elbow_count_c', 'pump_in_triplet_resistance_coefficient_m',
    'pump_in_triplet_resistance_coefficient_c',
    'pump_in_single_triplet_resistance_coefficient_m',
    'pump_in_single_triplet_resistance_coefficient_c',
    'pump_in_triplet_count_m', 'pump_in_triplet_count_c',
    'pump_in_reducer_resistance_coefficient_m',
    'pump_in_reducer_resistance_coefficient_c',
    'pump_in_converging_resistance_coefficient_m',
    'pump_in_converging_resistance_coefficient_c', 'pump_in_converging_spec_m',
    'pump_in_converging_spec_c', 'pump_in_converging_angle_m',
    'pump_in_converging_angle_c', 'pump_in_converging_diameter_radio_m',
    'pump_in_converging_diameter_radio_c',
    'pump_in_increasing_resistance_coefficient_m',
    'pump_in_increasing_resistance_coefficient_c', 'pump_in_increasing_spec_m',
    'pump_in_increasing_spec_c', 'pump_in_increasing_angle_m',
    'pump_in_increasing_angle_c', 'pump_in_increasing_diameter_radio_m',
    'pump_in_increasing_diameter_radio_c',
    'pump_in_in_out_resistance_coefficient_m',
    'pump_in_in_out_resistance_coefficient_c',
    'pump_in_valve_resistance_coefficient_m',
    'pump_in_valve_resistance_coefficient_c', 'pump_in_filter_m',
    'pump_in_filter_c', 'pump_in_sluice_resistance_coefficient_m',
    'pump_in_sluice_resistance_coefficient_c',
    'pump_in_single_sluice_resistance_coefficient_m',
    'pump_in_single_sluice_resistance_coefficient_c', 'pump_in_sluice_count_m',
    'pump_in_sluice_count_c', 'pump_in_check_resistance_coefficient_m',
    'pump_in_check_resistance_coefficient_c',
    'pump_in_single_check_resistance_coefficient_m',
    'pump_in_single_check_resistance_coefficient_c', 'pump_in_check_count_m',
    'pump_in_check_count_c', 'pump_in_regulating_resistance_coefficient_m',
    'pump_in_regulating_resistance_coefficient_c',
    'pump_in_plate_resistance_coefficient_m',
    'pump_in_plate_resistance_coefficient_c',
    'pump_in_measuring_pressure_loss_m', 'pump_in_measuring_pressure_loss_c',
    'pump_out_work_press_m', 'pump_out_work_press_c',
    'pump_out_work_temperature_m', 'pump_out_work_temperature_c',
    'pump_out_rated_flow_m', 'pump_out_rated_flow_c', 'pump_out_msv_m',
    'pump_out_msv_c', 'pump_out_media_viscosity_m',
    'pump_out_media_viscosity_c', 'pump_out_velocity_m', 'pump_out_velocity_c',
    'pump_out_calculate_velocity_m', 'pump_out_calculate_velocity_c',
    'pump_out_dynamic_head_m', 'pump_out_dynamic_head_c',
    'pump_out_pipe_outer_diameter_m', 'pump_out_pipe_outer_diameter_c',
    'pump_out_pipe_thickness_m', 'pump_out_pipe_thickness_c',
    'pump_out_pipe_inner_diameter_m', 'pump_out_pipe_inner_diameter_c',
    'pump_out_friction_resistance_m', 'pump_out_friction_resistance_c',
    'pump_out_reynolds_m', 'pump_out_reynolds_c',
    'pump_out_equivalent_roughness_m', 'pump_out_equivalent_roughness_c',
    'pump_out_relative_roughness_m', 'pump_out_relative_roughness_c',
    'pump_out_resistance_coefficient_m', 'pump_out_resistance_coefficient_c',
    'pump_out_unit_length_resistance_m', 'pump_out_unit_length_resistance_c',
    'pump_out_pipe_length_m', 'pump_out_pipe_length_c',
    'pump_out_local_resistance_m', 'pump_out_local_resistance_c',
    'pump_out_total_local_resistance_coefficient_m',
    'pump_out_total_local_resistance_coefficient_c',
    'pump_out_elbow_resistance_coefficient_m',
    'pump_out_elbow_resistance_coefficient_c', 'pump_out_elbow_spec_m',
    'pump_out_elbow_spec_c', 'pump_out_elbow_radius_m',
    'pump_out_elbow_radius_c', 'pump_out_elbow_radius_to_inner_diameter_m',
    'pump_out_elbow_radius_to_inner_diameter_c',
    'pump_out_90elbow_resistance_coefficient_m',
    'pump_out_90elbow_resistance_coefficient_c', 'pump_out_90elbow_count_m',
    'pump_out_90elbow_count_c', 'pump_out_triplet_resistance_coefficient_m',
    'pump_out_triplet_resistance_coefficient_c',
    'pump_out_single_triplet_resistance_coefficient_m',
    'pump_out_single_triplet_resistance_coefficient_c',
    'pump_out_triplet_count_m', 'pump_out_triplet_count_c',
    'pump_out_reducer_resistance_coefficient_m',
    'pump_out_reducer_resistance_coefficient_c',
    'pump_out_converging_resistance_coefficient_m',
    'pump_out_converging_resistance_coefficient_c',
    'pump_out_converging_spec_m', 'pump_out_converging_spec_c',
    'pump_out_converging_angle_m', 'pump_out_converging_angle_c',
    'pump_out_converging_diameter_radio_m',
    'pump_out_converging_diameter_radio_c',
    'pump_out_increasing_resistance_coefficient_m',
    'pump_out_increasing_resistance_coefficient_c',
    'pump_out_increasing_spec_m', 'pump_out_increasing_spec_c',
    'pump_out_increasing_angle_m', 'pump_out_increasing_angle_c',
    'pump_out_increasing_diameter_radio_m',
    'pump_out_increasing_diameter_radio_c',
    'pump_out_in_out_resistance_coefficient_m',
    'pump_out_in_out_resistance_coefficient_c',
    'pump_out_valve_resistance_coefficient_m',
    'pump_out_valve_resistance_coefficient_c', 'pump_out_filter_m',
    'pump_out_filter_c', 'pump_out_sluice_resistance_coefficient_m',
    'pump_out_sluice_resistance_coefficient_c',
    'pump_out_single_sluice_resistance_coefficient_m',
    'pump_out_single_sluice_resistance_coefficient_c',
    'pump_out_sluice_count_m', 'pump_out_sluice_count_c',
    'pump_out_check_resistance_coefficient_m',
    'pump_out_check_resistance_coefficient_c',
    'pump_out_single_check_resistance_coefficient_m',
    'pump_out_single_check_resistance_coefficient_c', 'pump_out_check_count_m',
    'pump_out_check_count_c', 'pump_out_regulating_resistance_coefficient_m',
    'pump_out_regulating_resistance_coefficient_c',
    'pump_out_plate_resistance_coefficient_m',
    'pump_out_plate_resistance_coefficient_c',
    'pump_out_measuring_pressure_loss_m', 'pump_out_measuring_pressure_loss_c'
]

list_turbine_auxiliary = [
    'deaerator_work_pressure',
    'deaerator_condensation_well_pressure_difference',
    'deaerator_condensation_spray_pressure', 'condenser_maximum_vacuum',
    'deaerator_condensation_well_pipe_resistance',
    'condensate_pump_design_lift', 'condensate_pump_flow',
    'condensate_pump_efficiency', 'condensate_pump_transmission_efficiency',
    'condensate_pump_motor_efficiency',
    'condensate_pump_motor_spare_coefficient', 'condensate_pump_motor_power',
    'condensate_pump_selected', 'extractor_work_pressure',
    'ejection_tank_work_pressure',
    'extractor_ejection_waterline_height_difference', 'jet_pump_pipe_loss',
    'jet_pump_total_lift', 'jet_pump_flow', 'jet_pump_efficiency',
    'jet_pump_transmission_efficiency', 'jet_pump_motor_efficiency',
    'jet_pump_motor_spare_coefficient', 'jet_pump_motor_power',
    'jet_pump_selected', 'cooling_ejection_tank_work_pressure',
    'cooling_circulating_water_to_header_pressure',
    'cooling_extractor_ejection_waterline_height_difference',
    'cooling_jet_pump_pipe_loss', 'cooling_jet_pump_total_lift',
    'cooling_jet_pump_flow', 'cooling_jet_pump_efficiency',
    'cooling_jet_pump_transmission_efficiency',
    'cooling_jet_pump_motor_efficiency',
    'cooling_jet_pump_motor_spare_coefficient', 'cooling_jet_pump_motor_power',
    'cooling_jet_pump_selected', 'condenser_flow_amount', 'condenser_pressure',
    'turbine_exhaust_enthalpy', 'cooling_water_inlet_temperature',
    'saturation_temperature', 'supercooling_degree',
    'condensate_water_temperature', 'condensate_water_enthalpy',
    'cooling_pipe_clean_coefficient', 'cooling_pipe_correct_coefficient',
    'calculate_exponent', 'cooling_pipe_flow_velocity',
    'cooling_pipe_diameter', 'condenser_steam_load_correct_coefficient',
    'cooling_pipe_flow_velocity_correct_coefficient',
    'cooling_water_inlet_temperature_correct_coefficient',
    'cooling_water_pass_correct_coefficient',
    'condenser_steam_load_change_correct_coefficient',
    'total_heat_transfer_coefficient', 'condenser_heat_load',
    'circulation_ratio', 'circulating_water_amount',
    'cooling_water_temperature_rise', 'cooling_water_outlet_temperature',
    'logarithmic_average_temperature_difference', 'cooling_area',
    'vacuum_pump_condensate_flow_amount'
]

list_smoke_air_calculate = [
    'component_h2', 'component_co', 'component_ch4', 
    'component_c2h4','component_c3h8', 'component_c4h10', 
    'component_n2', 'component_o2','component_co2', 'component_h2s', 'component_cmhn', 
    'hl_h2', 'hl_co', 'hl_ch4', 
    'hl_c2h4', 'hl_c3h8', 'hl_c4h10', 
    'hl_n2', 'hl_o2', 'hl_co2', 'hl_h2s', 'hl_cmhn', 
    'hh_h2', 'hh_co', 'hh_ch4', 
    'hh_c2h4', 'hh_c3h8', 'hh_c4h10', 
    'hh_n2', 'hh_o2', 'hh_co2', 'hh_h2s', 'hh_cmhn', 
    'cpsh_h2', 'cpsh_co', 'cpsh_ch4', 
    'cpsh_c2h4', 'cpsh_c3h8', 'cpsh_c4h10', 
    'cpsh_n2', 'cpsh_o2', 'cpsh_co2', 'cpsh_h2s', 'cpsh_cmhn',
    'constant_need_air_amonut_per_m3', 'constant_air_density',
    'constant_need_air_mass_per_m3', 'excessive_air_coefficient',
    'actual_need_air_amonut', 'constant_gas_humidity_per_m3',
    'constant_air_humidity_per_m3', 'actual_air_amount_in_wet',
    'constant_ro2_amonut_per_m3', 'constant_n2_amonut_per_m3',
    'constant_actual_n2_amonut_per_m3', 'constant_h2o_amonut_per_m3',
    'constant_actual_h2o_amonut_per_m3', 'constant_o2_amonut_per_m3',
    'actual_burning_gas_amonut', 'theory_burning_gas_amonut',
    'net_calorific_value', 'gross_heating_value', 'gas_init_temperature',
    'air_init_temperature', 'gas_average_cpvh', 'gas_h2o_average_cpvh',
    'air_average_cpvh', 'air_h2o_average_cpvh',
    'hy_adiabatic_calorimeter_temperature', 'smoke_ro2_average_cpvh',
    'smoke_h2o_average_cpvh', 'smoke_n2_average_cpvh', 'smoke_o2_average_cpvh',
    'calc_adiabatic_calorimeter_temperature', 'deviation_check',
    'incomplete_combustion_loss_coefficient', 'incomplete_combustion_loss',
    'heat_loss_coefficient', 'heat_loss', 'calc_theory_burning_temperature',
    'high_temperature_coefficient', 'coefficient_actual_temperature',
    'calc_actual_temperature', 'ro2_volume_enthalpy', 'n2_volume_enthalpy',
    'h2o_volume_enthalpy', 'air_volume_enthalpy', 'dust_volume_enthalpy',
    'theory_smoke_volume_enthalpy', 'theory_air_volume_enthalpy',
    'theory_dust_volume_enthalpy', 'smoke_enthalpy', 'qd_net', 'qar_net',
    'unknown_need_air_amonut_b_10500', 'unknown_need_air_amonut_a_10500',
    'unknown_need_air_amonut_gas', 'unknown_need_air_amonut_lng',
    'unknown_excessive_air_coefficient', 'unknown_actual_need_air_amonut',
    'unknown_theory_burning_amonut_gas', 'unknown_theory_burning_amonut_oag',
    'unknown_theory_burning_amonut_lng', 'unknown_theory_burning_amonut_cog',
    'unknown_theory_burning_amonut_b_12600',
    'unknown_actual_burning_gas_amonut',
    'unknown_boiler_actual_burning_gas_amonut',
    'unknown_gas_actual_burning_gas_amonut', 'exp_gas_qnet',
    'exp_gas_theory_air_amount_a_35799', 'exp_gas_theory_air_amount_b_35799',
    'exp_gas_excessive_air_coefficient', 'exp_gas_actual_amonut_a_35799',
    'exp_gas_actual_amonut_b_35799', 'exp_boiler_qnet',
    'exp_boiler_excessive_air_coefficient', 'exp_liquid_fuel_qnet',
    'exp_liquid_fuel_theory_air_amount',
    'exp_liquid_fuel_excessive_air_coefficient',
    'exp_liquid_fuel_actual_amonut', 'exp_coal_qnet',
    'exp_coal_theory_air_amount', 'exp_coal_excessive_air_coefficient',
    'exp_coal_actual_amonut', 'exp_wood_peat_qnet',
    'exp_wood_peat_water_content', 'exp_wood_peat_theory_air_amount',
    'exp_wood_peat_excessive_air_coefficient',
    'exp_wood_peat_best_water_content', 'exp_wood_peat_actual_amonut',
    'exp_boiler_theory_air_amount_a_12561',
    'exp_boiler_theory_air_amount_b_12561', 'exp_boiler_actual_amonut_a_12561',
    'exp_boiler_actual_amonut_b_12561'
]

list_questionnaire = [
    'surplus_gas_bfg', 'surplus_gas_ldg', 'surplus_gas_cog',
    'bfg_gas_temperature', 'ldg_gas_temperature', 'cog_gas_temperature',
    'bfg_gas_pressure', 'ldg_gas_pressure', 'cog_gas_pressure',
    'bfg_gas_calorific_value', 'ldg_gas_calorific_value',
    'cog_gas_calorific_value', 'provide_steam_amount',
    'provide_steam_pressure',
    'atmosphere_temperature_h', 'atmosphere_temperature_a',
    'atmosphere_temperature_l', 'atmosphere_pressure_h',
    'atmosphere_pressure_l', 'relative_humidity_h',
    'relative_humidity_a', 'relative_humidity_l', 'outside_wind_speed_h',
    'outside_wind_speed_a', 'outside_wind_speed_l',
    'seismic_fortification_intensity_h', 'seismic_fortification_intensity_a',
    'seismic_fortification_intensity_l', 'water_pressure', 'water_temperature',
    'water_ph', 'water_suspended_matter', 'water_cl', 'nitrogen_purity',
    'nitrogen_pressure', 'nitrogen_temperature', 'compressed_air_pressure',
    'compressed_air_temperature', 'grid_voltage', 'max_short_circuit_capacity',
    'factory_location_elevation', 'dielectric_position_height_caliber_route',
    'water_quality_analysis_report', 'cooling_tower', 'project_approval_eia',
    'surplus_gas_bfg_max', 'surplus_gas_bfg_min', 'surplus_gas_ldg_max',
    'surplus_gas_ldg_min', 'surplus_gas_cog_max', 'surplus_gas_cog_min',
    'bfg_gas_temperature_max', 'bfg_gas_temperature_min',
    'ldg_gas_temperature_max', 'ldg_gas_temperature_min',
    'cog_gas_temperature_max', 'cog_gas_temperature_min',
    'bfg_gas_pressure_max', 'bfg_gas_pressure_min', 'ldg_gas_pressure_max',
    'ldg_gas_pressure_min', 'cog_gas_pressure_max', 'cog_gas_pressure_min',
    'bfg_gas_calorific_value_max', 'bfg_gas_calorific_value_min',
    'ldg_gas_calorific_value_max', 'ldg_gas_calorific_value_min',
    'cog_gas_calorific_value_max', 'cog_gas_calorific_value_min',
    'provide_steam_amount_max', 'provide_steam_amount_min',
    'provide_steam_pressure_max', 'provide_steam_pressure_min',
    'atmosphere_temperature_a_winter', 'atmosphere_temperature_a_summer',
    'atmosphere_temperature_a_cold', 'atmosphere_temperature_a_hot',
    'atmosphere_temperature_extreme_h', 'atmosphere_temperature_extreme_l',
    'atmosphere_pressure_a_winter', 'atmosphere_pressure_a_summer',
    'atmosphere_pressure_a_cold', 'atmosphere_pressure_a_hot', 'atmosphere_pressure_a',
    'atmosphere_pressure_extreme_h', 'atmosphere_pressure_extreme_l',
    'relative_humidity_a_winter', 'relative_humidity_a_summer',
    'relative_humidity_a_cold', 'relative_humidity_a_hot',
    'relative_humidity_extreme_h', 'relative_humidity_extreme_l',
    'outside_wind_speed_a_winter', 'outside_wind_speed_a_summer',
    'outside_wind_speed_a_cold', 'outside_wind_speed_a_hot',
    'outside_wind_speed_extreme_h', 'outside_wind_speed_extreme_l',
    'design_earthquake_acceleration', 'voltage_other', 'converter_flow',
    'converter_pressure', 'converter_temperature', 'heat_recovery_flow',
    'heat_recovery_pressure', 'heat_recovery_temperature', 'furnace_flow',
    'furnace_pressure', 'furnace_temperature',
    'furnace_h2_content', 'furnace_co_content',
    'furnace_ch4_content', 'furnace_c2h4_content', 'furnace_c3h8_content',
    'furnace_c4h10_content', 'furnace_n2_content', 'furnace_o2_content',
    'furnace_co2_content', 'furnace_h2s_content', 'furnace_cmhn_content',
    'furnace_h2o_content', 'furnace_so2_content', 'furnace_low_heating',
    'furnace_high_heating', 'converter_h2_content', 'converter_co_content',
    'converter_ch4_content', 'converter_c2h4_content',
    'converter_c3h8_content', 'converter_c4h10_content',
    'converter_n2_content', 'converter_o2_content', 'converter_co2_content',
    'converter_h2s_content', 'converter_cmhn_content', 'converter_h2o_content',
    'converter_so2_content', 'converter_low_heating', 'converter_high_heating',
    'coke_h2_content', 'coke_co_content', 'coke_ch4_content',
    'coke_c2h4_content', 'coke_c3h8_content', 'coke_c4h10_content',
    'coke_n2_content', 'coke_o2_content', 'coke_co2_content',
    'coke_h2s_content', 'coke_cmhn_content', 'coke_h2o_content',
    'coke_so2_content', 'coke_low_heating', 'coke_high_heating',
    'seismic_fortification_intensity_extreme_h', 'steam_other_flow',
    'steam_other_pressure', 'steam_other_temperature',
    'design_earthquake_acceleration', 'above_sea_level'
]

list_boiler_of_pts = [
    'surplus_gas_bfg', 'surplus_gas_ldg', 'surplus_gas_cog',
    'bfg_gas_calorific_value', 'ldg_gas_calorific_value', 'cog_gas_calorific_value',
    'boiler_efficiency', 'superheated_steam_outlet_pressure',
    'superheated_steam_temperature', 'superheated_steam_enthalpy', 'excess_air_coefficient',
    'air_temperature', 'air_enthalpy', 'air_need_for_combustion', 'boiler_feed_water_temperature',
    'feedwater_enthalpy', 'rate_of_blowdown', 'saturation_water_temperature',
    'saturation_water_enthalpy', 'steam_output'
]

list_gas_air_system = [
    "c2s_condition_temperature_air", "c2s_condition_flux_air",
    "c2s_local_atmosphere_air", "c2s_standard_temperature_air",
    "c2s_standard_pressure_air", "c2s_standard_flux_air",
    "c2s_condition_temperature_smoke", "c2s_condition_flux_smoke",
    "c2s_local_atmosphere_smoke", "c2s_standard_temperature_smoke",
    "c2s_standard_pressure_smoke", "c2s_standard_flux_smoke",
    "s2c_standard_temperature_air", "s2c_standard_pressure_air",
    "s2c_standard_flux_air", "s2c_condition_temperature_air",
    "s2c_local_atmosphere_air", "s2c_condition_flux_air",
    "s2c_standard_temperature_smoke", "s2c_standard_pressure_smoke",
    "s2c_standard_flux_smoke", "s2c_condition_temperature_smoke",
    "s2c_local_atmosphere_smoke", "s2c_condition_flux_smoke",
    "s2c_standard_temperature_gas", "s2c_standard_pressure_gas",
    "s2c_standard_flux_gas", "s2c_condition_temperature_gas",
    "s2c_local_atmosphere_gas", "s2c_condition_flux_gas",
    "blower_air_temperature", "blower_wind_resistance",
    "blower_local_atmosphere", "blower_condition_smoke_flux",
    "blower_fan_temperature", "blower_fan_total_pressure",
    "blower_fan_selected_total_pressure", "blower_fan_selected_flux",
    "blower_fan_pressure_efficiency", "blower_transmission_efficiency",
    "blower_motor_efficiency", "blower_fan_shaft_power",
    "blower_motor_safe_margin", "blower_motor_power",
    "blower_specification_power", "blower_specification_flux",
    "induced_smoke_temperature", "induced_local_atmosphere",
    "induced_condition_smoke_flux", "induced_fan_temperature",
    "induced_smoke_density", "induced_fan_total_pressure",
    "induced_fan_selected_total_pressure", "induced_fan_selected_flux",
    "induced_fan_efficiency", "induced_transmission_efficiency",
    "induced_motor_efficiency", "induced_fan_shaft_power",
    "induced_motor_safe_margin", "induced_motor_power",
    "induced_specification_power", "induced_specification_flux",
    "gas_tube_medium_flux", "gas_tube_medium_temperature",
    "gas_tube_flow_velocity", "gas_tube_calculated_cross_sectional_area",
    "gas_tube_calculated_diameter", "gas_tube_selected_diameter",
    "gas_tube_selected_thickness", "coldwind_tube_medium_flux",
    "coldwind_tube_medium_temperature", "coldwind_tube_flow_velocity",
    "coldwind_tube_calculated_cross_sectional_area",
    "coldwind_tube_calculated_diameter", "coldwind_tube_length",
    "coldwind_tube_width", "coldwind_tube_specification",
    "hotwind_tube_medium_flux", "hotwind_tube_medium_temperature",
    "hotwind_tube_flow_velocity",
    "hotwind_tube_calculated_cross_sectional_area",
    "hotwind_tube_calculated_diameter", "hotwind_tube_length",
    "hotwind_tube_width", "hotwind_tube_specification",
    "total_smoke_tube_medium_flux", "total_smoke_tube_medium_temperature",
    "total_smoke_tube_flow_velocity",
    "total_smoke_tube_calculated_cross_sectional_area",
    "total_smoke_tube_calculated_diameter", "total_smoke_tube_length",
    "total_smoke_tube_width", "total_smoke_tube_specification",
    "branch_smoke_tube_medium_flux", "branch_smoke_tube_medium_temperature",
    "branch_smoke_tube_flow_velocity",
    "branch_smoke_tube_calculated_cross_sectional_area",
    "branch_smoke_tube_calculated_diameter", "branch_smoke_tube_length",
    "branch_smoke_tube_width", "branch_smoke_tube_specification",
    "main_hotwind_tube_medium_flux", "main_hotwind_tube_medium_temperature",
    "main_hotwind_tube_flow_velocity",
    "main_hotwind_tube_calculated_cross_sectional_area",
    "main_hotwind_tube_calculated_diameter",
    "main_hotwind_tube_selected_diameter",
    "main_hotwind_tube_selected_thickness", "branch_hotwind_tube_medium_flux",
    "branch_hotwind_tube_medium_temperature",
    "branch_hotwind_tube_flow_velocity",
    "branch_hotwind_tube_calculated_cross_sectional_area",
    "branch_hotwind_tube_calculated_diameter",
    "branch_hotwind_tube_selected_diameter",
    "branch_hotwind_tube_selected_thickness", "chimney_height",
    "local_atmosphere", "standard_air_density",
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
    "chimney_total_resistance", "induced_total_pressure"
]

list_smoke_resistance = [
    "air_preheater_outlet_calculated_temperature",
    "air_preheater_outlet_smoke_amount", "air_preheater_density",
    "air_preheater_flow_velocity", "air_preheater_dynamic_pressure_head",
    "air_preheater_smoke_tube_area", "air_preheater_length",
    "air_preheater_width", "air_preheater_duct_perimeter",
    "air_preheater_tube_equivalent_diameter",
    "air_preheater_gas_kinetic_viscosity", "air_preheater_reynolds_number",
    "air_preheater_absolute_tube_roughness",
    "air_preheater_relative_tube_roughness",
    "air_preheater_560_relative_tube_roughness", "air_preheater_discriminant",
    "air_preheater_frictional_resistance",
    "air_preheater_frictional_resistance_coefficient",
    "air_preheater_unit_length_frictional_resistance",
    "air_preheater_ducting_length", "air_preheater_local_resistance",
    "air_preheater_local_resistance_coefficient",
    "air_preheater_90_outlet_sharp_turn_elbow",
    "air_preheater_powder_local_resistance_coefficient",
    "air_preheater_air_elbow_local_resistance_coefficient",
    "air_preheater_powder_concentration_corrected_coefficient",
    "air_preheater_90_section_slow_turn_elbow",
    "air_preheater_slow_powder_local_resistance_coefficient",
    "air_preheater_slow_air_local_resistance_coefficient",
    "air_preheater_slow_powder_concentration_corrected_coefficient",
    "air_preheater_reducer_tube", "air_preheater_to_deduster_total_resistance",
    "deduster_outlet_calculated_temperature", "deduster_outlet_smoke_amount",
    "deduster_density", "deduster_flow_velocity",
    "deduster_dynamic_pressure_head", "deduster_smoke_tube_area",
    "deduster_length", "deduster_width", "deduster_duct_perimeter",
    "deduster_tube_equivalent_diameter", "deduster_gas_kinetic_viscosity",
    "deduster_reynolds_number", "deduster_absolute_tube_roughness",
    "deduster_relative_tube_roughness", "deduster_560_relative_tube_roughness",
    "deduster_discriminant", "deduster_frictional_resistance",
    "deduster_frictional_resistance_coefficient",
    "deduster_unit_length_frictional_resistance", "deduster_ducting_length",
    "deduster_local_resistance", "deduster_local_resistance_coefficient",
    "deduster_90_outlet_slow_turn_elbow",
    "deduster_slow_powder_local_resistance_coefficient",
    "deduster_slow_air_local_resistance_coefficient",
    "deduster_slow_powder_concentration_corrected_coefficient",
    "deduster_90_section_slow_turn_elbow",
    "deduster_section_slow_powder_local_resistance_coefficient",
    "deduster_section_slow_air_local_resistance_coefficient",
    "deduster_corrected_turning_angle_coefficient",
    "deduster_section_corrected_height_width_ratio_coefficient",
    "deduster_section_original_resistance_coefficient_with_roughness",
    "deduster_section_slow_powder_corrected_coefficient",
    "deduster_inlet_bellows", "deduster_to_induced_draft_total_resistance",
    "induced_draft_inlet_calculated_temperature",
    "induced_draft_inlet_smoke_amount", "induced_draft_density",
    "induced_draft_flow_velocity", "induced_draft_dynamic_pressure_head",
    "induced_draft_smoke_tube_area", "induced_draft_width",
    "induced_draft_height", "induced_draft_duct_perimeter",
    "induced_draft_tube_equivalent_diameter",
    "induced_draft_gas_kinetic_viscosity", "induced_draft_reynolds_number",
    "induced_draft_absolute_tube_roughness",
    "induced_draft_relative_tube_roughness",
    "induced_draft_560_relative_tube_roughness", "induced_draft_discriminant",
    "induced_draft_frictional_resistance",
    "induced_draft_frictional_resistance_coefficient",
    "induced_draft_unit_length_frictional_resistance",
    "induced_draft_ducting_length", "induced_draft_local_resistance",
    "induced_draft_local_resistance_coefficient",
    "induced_draft_outlet_plate_gate", "induced_draft_outlet_diffuser_tube",
    "induced_draft_45_90_slow_turn_elbow",
    "induced_draft_powder_local_resistance_coefficient",
    "induced_draft_air_local_resistance_coefficient",
    "induced_draft_corrected_turning_angle_coefficient",
    "induced_draft_corrected_height_width_ratio_coefficient",
    "induced_draft_original_resistance_coefficient_with_roughness",
    "induced_draft_powder_concentration_corrected_coefficient",
    "brick_chimney_inlet", "induced_draft_to_chimney_total_resistance",
    "smoke_chimney_total_resistance"
]

list_wind_resistance = [
    "recommend_velocity_coldwind", "recommend_velocity_hotwind",
    "intake_to_preheater_temperature", "intake_to_preheater_amount",
    "intake_to_preheater_density", "intake_to_preheater_flow_velocity",
    "intake_to_preheater_dynamic_pressure_head", "fan_inlet_duct_section_area",
    "fan_inlet_duct_length", "fan_inlet_duct_width",
    "fan_inlet_duct_perimeter", "fan_inlet_duct_equivalent_diameter",
    "fan_inlet_gas_kinetic_viscosity", "fan_inlet_reynolds_number",
    "fan_inlet_absolute_tube_roughness", "fan_inlet_relative_tube_roughness",
    "fan_inlet_560_relative_tube_roughness", "fan_inlet_discriminant",
    "fan_inlet_frictional_resistance",
    "fan_inlet_frictional_resistance_coefficient",
    "fan_inlet_unit_length_frictional_resistance", "fan_inlet_ducting_length",
    "fan_inlet_local_resistance", "fan_inlet_local_resistance_coefficient",
    "fan_inlet_single_local_resistance_coefficient",
    "fan_inlet_single_bellows", "fan_inlet_single_damper",
    "fan_inlet_total_pressure", "fan_outlet_frictional_resistance",
    "fan_outlet_unit_length_frictional_resistance",
    "fan_outlet_ducting_length", "fan_outlet_local_resistance",
    "fan_outlet_local_resistance_coefficient",
    "fan_outlet_single_increase_pipe", "fan_outlet_90_section_slow_turn_elbow",
    "fan_outlet_preheater_diffuser_pipe",
    "fan_outlet_to_preheater_total_pressure",
    "preheater_to_boiler_temperature", "preheater_to_boiler_amount",
    "preheater_to_boiler_density", "preheater_to_boiler_flow_velocity",
    "preheater_to_boiler_dynamic_pressure_head",
    "preheater_outlet_duct_section_area", "preheater_outlet_duct_diameter",
    "preheater_outlet_duct_length", "preheater_outlet_duct_width",
    "preheater_outlet_duct_perimeter",
    "preheater_outlet_duct_equivalent_diameter",
    "preheater_outlet_gas_kinetic_viscosity",
    "preheater_outlet_reynolds_number",
    "preheater_outlet_absolute_tube_roughness",
    "preheater_outlet_relative_tube_roughness",
    "preheater_outlet_560_relative_tube_roughness",
    "preheater_outlet_discriminant", "preheater_outlet_frictional_resistance",
    "preheater_outlet_frictional_resistance_coefficient",
    "preheater_outlet_unit_length_frictional_resistance",
    "preheater_outlet_ducting_length", "preheater_outlet_local_resistance",
    "preheater_outlet_local_resistance_coefficient",
    "preheater_outlet_shrink_pipe", "preheater_outlet_90_sharp_turn_elbow",
    "preheater_outlet_90_sharp_turn_elbow_count",
    "preheater_outlet_90_sharp_turn_elbow_resistance",
    "preheater_outlet_air_intake_gate", "preheater_outlet_combustor_gate",
    "preheater_outlet_to_boiler_total_pressure", "windhole_total_pressure"
]

list_circulating_water_system = [
    'steam_exhaust_flux_winter', 'steam_exhaust_flux_summer',
    'steam_exhaust_flux_selected', 'circulation_ratio_winter',
    'circulation_ratio_summer', 'circulation_water_flow_winter',
    'circulation_water_flow_summer', 'auxiliary_cooling_water_flow_winter',
    'auxiliary_cooling_water_flow_summer',
    'total_circulation_water_flow_winter',
    'total_circulation_water_flow_summer',
    'selected_total_circulation_water_flow', 'spray_density', 'spray_area',
    'in_out_water_temperature_difference', 'dry_bulb_temperature',
    'dry_bulb_k_coefficient', 'evaporation_loss_rate', 'evaporation_loss',
    'wind_blow_loss_rate', 'wind_blow_loss', 'concentration_rate',
    'discharge_rate', 'discharge_capacity', 'supply_water_amount',
    'circulating_pool_water_amount', 'circulating_pool_size_deep',
    'circulating_pool_size_length', 'circulating_pool_size_width',
    'circulating_pool_size_checked',
    'condenser_circulating_water_inlet_pressure', 'condenser_friction',
    'circulating_backwater_pressure', 'circulating_water_reservoir_pressure',
    'circulation_pump_outlet_to_condenser_inlet_height_difference',
    'reservoir_to_pump_inlet_height_difference', 'pipe_loss', 'y_filter_loss',
    'total_pumping_lift', 'pump_flow', 'pump_efficiency',
    'pump_transmission_efficiency', 'pump_motor_efficiency',
    'pump_motor_spare_coefficient', 'pump_matching_motor_power',
    'selected_pump_model_power', 'selected_pump_model_flow',
    'selected_pump_model_lift',
    'cooling_tower_selected_type', 'cooling_tower_selected_name',
    'p_spray_density', 'p_spray_area', 'p_select_f', 'p_count', 'p_single_cold_amount', 'p_select_s'
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

list_column_TurbineClear = [
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

# 格式化数据库取出的值
def format_value(flag, values):
    # reload(sys)                         # 2
    # sys.setdefaultencoding('utf-8')
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if not values or values == "null" or values == "None":
        result = ""
    elif values == "True":
        result = True
    elif values == "False":
        result = False
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        # result = float(str(float(values)).rstrip('0'))
        result = round(float(str(float(values)).rstrip('0')), 4)
    else:
        result = values
    return result

# 格式化数据库取出的值
def formatTemplateValue(values):
    # reload(sys)                         # 2
    # sys.setdefaultencoding('utf-8')
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if values == "null" or values == "None" or values is None:
        result = ""
    elif str(type(values)) == "<type 'unicode'>":
        result = values
    elif str(type(values)) == "<type 'int'>":
        result = values
    elif str(type(values)) == "<type 'str'>":
        result = values
    elif abs(values) <= 0.00001:
        result = 0
    else:
        # 只有数字类型的需要取出多余的0
        result = float(str(float(values)).rstrip('0'))
    return result

def getGPGPlanData(planId):
    gpgMdTemplateData = {
        'company.company_name': '',
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_bfg_max': '',
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_bfg_min': '',
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_bfg': '',
        'GasPowerGenerationNeedsQuestionnaire.bfg_gas_pressure': '',
        'GasPowerGenerationNeedsQuestionnaire.bfg_gas_temperature': '',        
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_ldg_max': '',
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_ldg_min': '',
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_ldg': '',
        'GasPowerGenerationNeedsQuestionnaire.ldg_gas_pressure': '',
        'GasPowerGenerationNeedsQuestionnaire.ldg_gas_temperature': '',  
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_cog_max': '',
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_cog_min': '',
        'GasPowerGenerationNeedsQuestionnaire.surplus_gas_cog': '',
        'GasPowerGenerationNeedsQuestionnaire.cog_gas_pressure': '',
        'GasPowerGenerationNeedsQuestionnaire.cog_gas_temperature': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_flow': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_pressure': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_temperature': '',
        'GasPowerGenerationNeedsQuestionnaire.heat_recovery_flow': '',
        'GasPowerGenerationNeedsQuestionnaire.heat_recovery_pressure': '',
        'GasPowerGenerationNeedsQuestionnaire.heat_recovery_temperature': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_flow': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_pressure': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_temperature': '',
        'GasPowerGenerationNeedsQuestionnaire.steam_other_flow': '',
        'GasPowerGenerationNeedsQuestionnaire.steam_other_pressure': '',
        'GasPowerGenerationNeedsQuestionnaire.steam_other_temperature': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_co_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_co2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_ch4_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_n2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_h2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_o2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_h2o_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_cmhn_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_so2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_low_heating': '',
        'GasPowerGenerationNeedsQuestionnaire.furnace_high_heating': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_co_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_co2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_ch4_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_n2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_h2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_o2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_h2o_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_cmhn_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_so2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_low_heating': '',
        'GasPowerGenerationNeedsQuestionnaire.converter_high_heating': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_co_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_co2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_ch4_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_n2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_h2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_o2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_h2o_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_cmhn_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_so2_content': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_low_heating': '',
        'GasPowerGenerationNeedsQuestionnaire.coke_high_heating': '',        
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_temperature_a_summer': '',
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_temperature_a_winter': '',    
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_temperature_a_cold': '',
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_temperature_a_hot': '',
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_temperature_a': '',
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_temperature_extreme_h': '',
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_temperature_extreme_l': '',
        'GasPowerGenerationNeedsQuestionnaire.relative_humidity_a_summer': '',
        'GasPowerGenerationNeedsQuestionnaire.relative_humidity_a_winter': '',
        'GasPowerGenerationNeedsQuestionnaire.relative_humidity_a': '',
        'GasPowerGenerationNeedsQuestionnaire.relative_humidity_extreme_h': '',       
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_pressure_a_summer': '',
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_pressure_a_winter': '',
        'GasPowerGenerationNeedsQuestionnaire.atmosphere_pressure_a': '',
        'GasPowerGenerationNeedsQuestionnaire.above_sea_level': '',
        'GasPowerGenerationNeedsQuestionnaire.outside_wind_speed_a': '',
        'GasPowerGenerationNeedsQuestionnaire.outside_wind_speed_extreme_h': '',
        'GasPowerGenerationNeedsQuestionnaire.seismic_fortification_intensity_a': '',
        'GasPowerGenerationNeedsQuestionnaire.design_earthquake_acceleration': '',
        'GPGBoilerOfPTS.steam_output': '',
        'GPGBoilerOfPTS.superheated_steam_outlet_pressure': '',
        'GPGBoilerOfPTS.superheated_steam_temperature': '',
        'GPGBoilerOfPTS.boiler_feed_water_temperature': '',
        'GPGBoilerOfPTS.boiler_efficiency': '',      
        'GPGBoilerAuxiliaries.s_design_flux': '',
        'GPGBoilerAuxiliaries.s_volume': '',
        'GPGBoilerAuxiliaries.p_deaerator_pressure': '',
        'GPGBoilerAuxiliaries.m_boiler_evaporation': '',
        'GPGBoilerAuxiliaries.m_steamwater_cycle_loss': '',
        'GPGBoilerAuxiliaries.m_pollution_loss': '',
        'GPGBoilerAuxiliaries.m_increase_loss': '',
        'GPGBoilerAuxiliaries.m_boiler_normal_watersupply': '',
        'GPGBoilerAuxiliaries.m_boiler_max_watersupply': '',
        'GPGBoilerAuxiliaries.m_boiler_watersupply_specifications': '',
        'GPGBoilerAuxiliaries.c_specifications': '',
        'GPGBoilerAuxiliaries.r_specifications': '',
        'GPGTurbineOfPTS.i_deoxidize_temperature': '',
        'GPGTurbineOfPTS.e_exhaust_point_flow': '',
        'GPGTurbineOfPTS.e_steam_extraction_select': '',
        'GPGTurbineOfPTS.e_steam_extraction': '',
        'GPGTurbineOfPTS.e_steam_flow': '',
        'GPGTurbineOfPTS.e_steam_pressure': '',
        'GPGTurbineOfPTS.e_steam_temperature': '',
        'GPGCirculatingWaterSystem.supply_water_amount': '',
        'GPGCirculatingWaterSystem.circulation_ratio_summer': '',
        'GPGCirculatingWaterSystem.circulation_ratio_winter': '',
        'GPGCirculatingWaterSystem.steam_exhaust_flux_selected': '',
        'GPGCirculatingWaterSystem.circulation_water_flow_summer': '',
        'GPGCirculatingWaterSystem.circulation_water_flow_winter': '',
        'GPGCirculatingWaterSystem.auxiliary_cooling_water_flow_winter': '',
        'GPGCirculatingWaterSystem.total_circulation_water_flow_summer': '',
        'GPGCirculatingWaterSystem.total_circulation_water_flow_winter': '',
        'GPGCirculatingWaterSystem.evaporation_loss': '',
        'GPGCirculatingWaterSystem.wind_blow_loss': '',
        'GPGCirculatingWaterSystem.discharge_capacity': ''
    }

    questionnaire = GasPowerGenerationNeedsQuestionnaire.search_questionnaire(planId)
    BoilerOfBTS = GPGBoilerOfPTS.search_BoilerOfPTS(planId)
    Turbine = GPGTurbineOfPTS.search_TurbineOfPTS(planId)
    BoilerAuxiliaries = GPGBoilerAuxiliaries.search_boiler_auxiliaries(planId)
    CirculatingWater = GPGCirculatingWaterSystem.search_CirculatingWater(planId)
    plan = Plan.search_planById(planId)
    company = Company.search_companyById(plan.company_id)

    gpgMdTemplateData['company.company_name'] = company.company_name
    for key in gpgMdTemplateData:
        if hasattr(questionnaire, key.split(".")[1]):
            value = getattr(questionnaire, key.split(".")[1])
            if value:
                gpgMdTemplateData[key] = formatTemplateValue(value)
            else:
                gpgMdTemplateData[key] = 0

    for key in gpgMdTemplateData:
        if hasattr(BoilerOfBTS, key.split(".")[1]):
            value = getattr(BoilerOfBTS, key.split(".")[1])
            if value:
                gpgMdTemplateData[key] = formatTemplateValue(value)
            else:
                gpgMdTemplateData[key] = 0

    for key in gpgMdTemplateData:
        if hasattr(Turbine, key.split(".")[1]):
            value = getattr(Turbine, key.split(".")[1])
            if value:
                gpgMdTemplateData[key] = formatTemplateValue(value)
            else:
                gpgMdTemplateData[key] = 0

    for key in gpgMdTemplateData:
        if hasattr(BoilerAuxiliaries, key.split(".")[1]):
            value = getattr(BoilerAuxiliaries, key.split(".")[1])
            if value:
                gpgMdTemplateData[key] = formatTemplateValue(value)
            else:
                gpgMdTemplateData[key] = 0

    for key in gpgMdTemplateData:
        if hasattr(CirculatingWater, key.split(".")[1]):
            value = getattr(CirculatingWater, key.split(".")[1])
            if value:
                gpgMdTemplateData[key] = formatTemplateValue(value)
            else:
                gpgMdTemplateData[key] = 0

    # gpgMdTemplateData['GPGBoilerOfPTS.steamoutput'] = BoilerOfBTS['steam_output']

    gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.surplus_maxldg_gas'] = gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.surplus_gas_ldg_max']
    gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.surplus_minldg_gas'] = gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.surplus_gas_ldg_min']
    gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.surplus_maxcog_gas'] = gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.surplus_gas_cog_max']
    gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.surplus_mincog_gas'] = gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.surplus_gas_cog_min']
    gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.atmosphere_pressureSummer'] = gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.atmosphere_pressure_a_summer']
    gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.atmosphere_pressureWinter'] = gpgMdTemplateData['GasPowerGenerationNeedsQuestionnaire.atmosphere_pressure_a_winter']
    gpgMdTemplateData['supply_water_sum'] = gpgMdTemplateData['GPGCirculatingWaterSystem.supply_water_amount'] + gpgMdTemplateData['GPGBoilerAuxiliaries.m_boiler_max_watersupply']
    return gpgMdTemplateData

class GPGImgService():

    def imgCreate(self, plan_id):
        gpgImgListResult.imgdealwithExecute(plan_id)
        # 压缩下载

    def getImgList(self, planId):
        path = GetPath.getImgGPGResultDir(planId)
        imglist = []
        for i in os.listdir(path):
            path_file = os.path.join(path, i)  # 取文件绝对路径
            if os.path.isfile(path_file):
                dirname, filename = os.path.split(path_file)
                chineseName, filenameprefix = self.getChineseName(filename)
                if chineseName is not None:
                    netPath = GetPath.getImgGPGNetPath(filenameprefix, planId)
                    dirname, netfilename = os.path.split(netPath)
                    if filename == netfilename:
                        imglist.append(ImgDict(chineseName, netPath, filename))
        return imglist

    def getChineseName(self, filename):
        if filename is not None and filename.find("gpg_pcs") != -1:
            return u"原则性燃烧系统图", "gpg_pcs"
        if filename is not None and filename.find("gpg_ptsA") != -1:
            return u"原则性热力系统图", "gpg_ptsA"
        if filename is not None and filename.find("gpg_ptsB") != -1:
            return u"原则性热力系统图", "gpg_ptsB"
        if filename is not None and filename.find("gpg_pcwtA") != -1:
            return u"原则性化学水处理系统图", "gpg_pcwtA"
        if filename is not None and filename.find("gpg_pcwtB") != -1:
            return u"原则性化学水处理系统图", "gpg_pcwtB"
        return None

class ToGPG():
    '''
    根据planId返回当前方案的主要设备参数字符串
    '''
    def getMainEquipmentPara(self, plan_id):
        gpg_BoilerData = GPGBoilerOfPTS.search_BoilerOfPTS(plan_id)
        steam_output = getattr(gpg_BoilerData, 'steam_output')

        gpg_TurbineData = GPGTurbineOfPTS.search_TurbineOfPTS(plan_id)
        e_steam_extraction_select = getattr(gpg_TurbineData, 'e_steam_extraction_select')
        if e_steam_extraction_select == "" or e_steam_extraction_select is None:
            e_steam_extraction_select = u""
        else:
            e_steam_extraction_select = e_steam_extraction_select

        e_steam_type = getattr(gpg_TurbineData, 'e_steam_type')
        if e_steam_type == "1":
            e_steam_type = u"低温低压"
        elif e_steam_type == "2":
            e_steam_type = u"次中温次中压"
        elif e_steam_type == "3":
            e_steam_type = u"中温中压"
        elif e_steam_type == "4":
            e_steam_type = u"次高温次高压"
        elif e_steam_type == "5":
            e_steam_type = u"高温高压"
        else:
            e_steam_type = u""

        s_steam_type_test = getattr(gpg_TurbineData, 's_steam_type_test')
        if s_steam_type_test == 1:
            s_steam_type_test = u"抽凝"
        elif s_steam_type_test == 2:
            s_steam_type_test = u"背压"
        elif s_steam_type_test == 3:
            s_steam_type_test = u"补凝"
        else:
            pass
        
        deviceParameter = u""

        # 锅炉组
        if steam_output is not None:
            steam_output = round(float(str(float(steam_output)).rstrip('0')), 3)
            deviceParameter += u"1X " + str(steam_output) + u"t/h高温高压煤气锅炉。\n"
        # 汽轮机组
        if s_steam_type_test is not None:
            deviceParameter += "1X " + e_steam_extraction_select + "MW" + e_steam_type + s_steam_type_test + u"汽轮发电机组。"
        if deviceParameter == u'':
            return None
        else:
            return deviceParameter

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
            company_id=companyId, module_id=Module.gasPowerGeneration, plan_name=planName).first()
        if not plan:
            plan = Plan()
            plan.plan_name = planName
            plan.user_id = current_user.id
            plan.company_id = companyId
            plan.module_id = Module.gasPowerGeneration
            plan.plan_create_date = datetime.now()
            plan.plan_update_date = datetime.now()
            plan.company_lnglat = company_lnglat
            Plan.insert_plan(plan)
        plan.company_location = companyLocation
        newPlan = Plan.query.filter_by(
            company_id=companyId, module_id=Module.gasPowerGeneration, plan_name=planName).first()
        return newPlan.id

    # 修改方案表的修改时间
    @staticmethod
    def update_plan_date(plan_id):
        plan = Plan.query.filter_by(id=plan_id).first()
        plan.plan_update_date = datetime.now()
        Plan.insert_plan(plan)

    '''
    #删除方案
    @staticmethod
    def drop_plan(plan_id):
        GasPowerGenerationNeedsQuestionnaire.delete_questionnaire(plan_id)
        GPGBoilerOfPTS.delete_BoilerOfPTS(plan_id)
        GPGFlueGasAirSystem.delete_FlueGasAirSystem(plan_id)
        GPGSmokeResistance.delete_SmokeResistance(plan_id)
        GPGWindResistance.delete_WindResistance(plan_id)
        GPGCirculatingWaterSystem.delete_CirculatingWater(plan_id)
        GPGSmokeAirCalculate.delete_SmokeAirCalculate(plan_id)
        GPGTurbineAuxiliarySystem.delete_TurbineAuxiliary(plan_id)
        GPGSteamWaterPipe.delete_SteamWaterPipe(plan_id)
        GPGBoilerAuxiliaries.delete_boiler_auxiliaries(plan_id)
        GPGTurbineOfPTS.delete_TurbineOfPTS(plan_id)
        Plan.delete_plan(plan_id)
        '''

    '''
    @staticmethod
    def to_planJson(plans):
        datas = []
        for plan in plans:
            planData = {}
            planData['id'] = getattr(plan, 'id')
            planData['company_id'] = getattr(plan, 'company_id')
            planData['user_id'] = getattr(plan, 'user_id')
            planData['company_location'] = getattr(plan, 'company_location')
            planData['plan_update_date'] = str(
                getattr(plan, 'plan_update_date'))
            planData['plan_create_date'] = str(
                getattr(plan, 'plan_create_date'))
            datas.append(planData)
        return datas
    '''
    '''
    @staticmethod
    def to_userJson(users):
        datas = []
        for user in users:
            usersData = {}
            usersData['id'] = getattr(user, 'id')
            usersData['user_name'] = getattr(user, 'user_name')
            datas.append(usersData)
        return datas

    @staticmethod
    def to_companyJson(companys):
        datas = []
        for company in companys:
            companysData = {}
            companysData['id'] = getattr(company, 'id')
            companysData['company_name'] = getattr(company, 'company_name')
            datas.append(companysData)
        return datas
    '''

    @staticmethod
    def to_questionnaire(form, plan_id):
        questionnaire = GasPowerGenerationNeedsQuestionnaire.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_questionnaire)):
            if form.get(list_questionnaire[index]) != '':
                setattr(questionnaire, list_questionnaire[index],
                        form.get(list_questionnaire[index]))
        return questionnaire

    @staticmethod
    def to_questionnaireJson(questionnaire):
        datas = {}
        planId = getattr(questionnaire, 'plan_id')
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        for index in range(len(list_questionnaire)):
            datas[list_questionnaire[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(questionnaire, list_questionnaire[index])))
        datas['company_name'] = companyName
        datas['company_location'] = companyLocation
        datas['planId'] = planId
        datas['plan_name'] = plan.plan_name
        return datas

    #返回汽轮机部分json值
    @staticmethod
    def to_TurbineOfPtsJson(TurbineOfPtsData):
        json = {}
        for index in range(len(list_turbine_of_pts)):
            if list_turbine_of_pts[index] == 'e_steam_extraction_select':
                json[list_turbine_of_pts[index]] = format_value(
                    "", getattr(TurbineOfPtsData, list_turbine_of_pts[index]))
            else:
                json[list_turbine_of_pts[index]] = format_value(
                    "number", str(getattr(TurbineOfPtsData, list_turbine_of_pts[index])))

        json['e_steam_type'] = getattr(TurbineOfPtsData, 'e_steam_type')
        json['h_assume'] = getattr(TurbineOfPtsData, 'h_assume')
        json['s_parameter_flg'] = getattr(TurbineOfPtsData, 's_parameter_flg')
        json['s_steam_type_test'] = getattr(TurbineOfPtsData, 's_steam_type_test')
        json['s_temperature_pressure'] = getattr(TurbineOfPtsData, 's_temperature_pressure')
        json['s_hh_grade'] = getattr(TurbineOfPtsData, 's_hh_grade')
        json['s_lh_grade'] = getattr(TurbineOfPtsData, 's_lh_grade')
        return json

    #清理汽轮机旧记录
    @staticmethod
    def clearTurbineData(plan_id):
        TurbineOfPtsData = GPGTurbineOfPTS.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_TurbineClear)):
            setattr(TurbineOfPtsData, list_column_TurbineClear[index], None)
        return TurbineOfPtsData

    @staticmethod
    def to_TurbineOfPtsData(form, plan_id):
        TurbineOfPtsData = GPGTurbineOfPTS.query.filter_by(
            plan_id=plan_id).first()

        # if getattr(TurbineOfPtsData, 's_parameter_flg') == '1':
        for index in range(len(list_turbine_of_pts)):
            if list_turbine_of_pts[index] != 'hh1_water_temperature':
                if form.get(list_turbine_of_pts[index]) != '':
                    setattr(TurbineOfPtsData, list_turbine_of_pts[index],
                            form.get(list_turbine_of_pts[index]))
                else:
                    setattr(TurbineOfPtsData, list_turbine_of_pts[index], None)

        # 清理页面上的旧记录
        for index in range(len(list_column_TurbineClear)):
            setattr(TurbineOfPtsData, list_column_TurbineClear[index], None)
        
        if form.get('s_temperature_pressure') != "" and form.get('s_temperature_pressure') != None:
            setattr(TurbineOfPtsData, 's_temperature_pressure', form.get('s_temperature_pressure'))
            setattr(TurbineOfPtsData, 's_hh_grade', form.get('s_hh_grade'))
            setattr(TurbineOfPtsData, 's_lh_grade', form.get('s_lh_grade'))

            # 汽轮机类型没有变更
            if getattr(TurbineOfPtsData,'s_steam_type_test') == None:
                setattr(TurbineOfPtsData, 's_steam_type_test', form.get('s_steam_type_test'))
            else:
                if float(form.get('s_steam_type_test')) == float(getattr(TurbineOfPtsData,'s_steam_type_test')):
                    setattr(TurbineOfPtsData, 's_steam_type_test', form.get('s_steam_type_test'))

        setattr(TurbineOfPtsData, 'e_steam_type', form.get('e_steam_type'))
        setattr(TurbineOfPtsData, 'h_assume', form.get('h_assume'))

        pointPower, TurbineOfPtsData = turbine_foctory.Factory().execute(TurbineOfPtsData, form)

        # 汽轮机类型变更
        if getattr(TurbineOfPtsData,'s_steam_type_test') != None:
            if float(form.get('s_steam_type_test')) != float(getattr(TurbineOfPtsData,'s_steam_type_test')):
                setattr(TurbineOfPtsData, 's_steam_type_test', form.get('s_steam_type_test'))


        setattr(TurbineOfPtsData, 'e_steam_extraction_select', form.get('e_steam_extraction_select'))

        return pointPower, TurbineOfPtsData

    #返回锅炉辅机json值
    @staticmethod
    def to_BoilerAuxiliariesJson(BoilerAuxiliariesData):
        json = {}
        for index in range(len(list_boiler_auxiliaries)):
            if list_boiler_auxiliaries[index] == 'r_specifications' \
            or list_boiler_auxiliaries[index] == 'c_specifications' \
            or list_boiler_auxiliaries[index] == 'p_specifications' \
            or list_boiler_auxiliaries[index] == 'desalted_water_tech_name' \
            or list_boiler_auxiliaries[index] == 'm_boiler_watersupply_specifications':
                 json[list_boiler_auxiliaries[index]] = format_value(
                "", getattr(BoilerAuxiliariesData, list_boiler_auxiliaries[index]))
            else:
                json[list_boiler_auxiliaries[index]] = format_value(
                "number", str(getattr(BoilerAuxiliariesData, list_boiler_auxiliaries[index])))
        return json

    @staticmethod
    def to_BoilerAuxiliariesData(form, plan_id):
        BoilerAuxiliariesData = GPGBoilerAuxiliaries.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_boiler_auxiliaries)):
            if form.get(list_boiler_auxiliaries[index]) != '':
                setattr(BoilerAuxiliariesData, list_boiler_auxiliaries[index],
                        form.get(list_boiler_auxiliaries[index]))
        return BoilerAuxiliariesData

    #返回汽水管道json值
    @staticmethod
    def to_SteamWaterPipeJson(SteamWaterPipeData):
        json = {}
        for index in range(len(list_steam_water_pipe)):
            json[list_steam_water_pipe[index]] = format_value(
                "", str(getattr(SteamWaterPipeData, list_steam_water_pipe[index])))
        return json

    @staticmethod
    def to_SteamWaterPipeData(form, plan_id):
        SteamWaterPipeData = GPGSteamWaterPipe.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_steam_water_pipe)):
            if form.get(list_steam_water_pipe[index]) != '':
                setattr(SteamWaterPipeData, list_steam_water_pipe[index],
                        form.get(list_steam_water_pipe[index]))
        return SteamWaterPipeData

    #返回汽机辅机json值
    @staticmethod
    def to_TurbineAuxiliaryJson(TurbineAuxiliaryData):
        json = {}
        for index in range(len(list_turbine_auxiliary)):
            if list_turbine_auxiliary[index] == 'condensate_pump_selected' \
            or list_turbine_auxiliary[index] == 'jet_pump_selected' \
            or list_turbine_auxiliary[index] == 'cooling_jet_pump_selected':
                 json[list_turbine_auxiliary[index]] = format_value(
                "", getattr(TurbineAuxiliaryData, list_turbine_auxiliary[index]))
            else:
                json[list_turbine_auxiliary[index]] = format_value(
                "number", str(getattr(TurbineAuxiliaryData, list_turbine_auxiliary[index])))
        return json

    @staticmethod
    def to_TurbineAuxiliaryData(form, plan_id):
        TurbineAuxiliaryData = GPGTurbineAuxiliarySystem.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_turbine_auxiliary)):
            if form.get(list_turbine_auxiliary[index]) != '':
                setattr(TurbineAuxiliaryData, list_turbine_auxiliary[index],
                        form.get(list_turbine_auxiliary[index]))
        return TurbineAuxiliaryData

    #返回烟风量计算json值
    @staticmethod
    def to_SmokeAirCalculateJson(SmokeAirCalculateData):
        json = {}
        for index in range(len(list_smoke_air_calculate)):
            json[list_smoke_air_calculate[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(SmokeAirCalculateData, list_smoke_air_calculate[index])))
        return json

    @staticmethod
    def to_SmokeAirCalculateData(form, plan_id):
        SmokeAirCalculateData = GPGSmokeAirCalculate.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_smoke_air_calculate)):
            if form.get(list_smoke_air_calculate[index]) != '':
                setattr(SmokeAirCalculateData, list_smoke_air_calculate[index],
                        form.get(list_smoke_air_calculate[index]))
        return SmokeAirCalculateData

    #返回循环水系统json值
    @staticmethod
    def to_CirculatingWaterJson(CirculatingWaterData):
        json = {}
        for index in range(len(list_circulating_water_system)):
            if list_circulating_water_system[index] == 'cooling_tower_selected_name' \
                or list_circulating_water_system[index] == 'p_select_f' \
                or list_circulating_water_system[index] == 'selected_pump_model_power' \
                or list_circulating_water_system[index] == 'selected_pump_model_flow' \
                or list_circulating_water_system[index] == 'selected_pump_model_lift':
                 json[list_circulating_water_system[index]] = format_value(
                "", getattr(CirculatingWaterData, list_circulating_water_system[index]))
            else:
                json[list_circulating_water_system[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(CirculatingWaterData, list_circulating_water_system[index])))
        return json

    @staticmethod
    def to_CirculatingWaterData(form, plan_id):
        CirculatingWaterData = GPGCirculatingWaterSystem.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_circulating_water_system)):
            if form.get(list_circulating_water_system[index]) != '':
                setattr(CirculatingWaterData, list_circulating_water_system[index],
                        form.get(list_circulating_water_system[index]))
        return CirculatingWaterData

    #返回烟风系统json值
    @staticmethod
    def to_GasAirJson(GasAirData):
        json = {}
        for index in range(len(list_gas_air_system)):
            if list_gas_air_system[index] == 'coldwind_tube_specification' \
            or list_gas_air_system[index] == 'hotwind_tube_specification' \
            or list_gas_air_system[index] == 'total_smoke_tube_specification' \
            or list_gas_air_system[index] == 'branch_smoke_tube_specification' \
            or list_gas_air_system[index] == 'induced_specification_flux' \
            or list_gas_air_system[index] == 'induced_specification_power' \
            or list_gas_air_system[index] == 'blower_specification_power' \
            or list_gas_air_system[index] == 'blower_specification_flux':
                 json[list_gas_air_system[index]] = format_value(
                "", getattr(GasAirData, list_gas_air_system[index]))
            else:
                json[list_gas_air_system[index]] = format_value(
                "number", str(getattr(GasAirData, list_gas_air_system[index])))
        return json

    @staticmethod
    def to_GasAirData(form, plan_id):
        GasAirData = GPGFlueGasAirSystem.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_gas_air_system)):
            if form.get(list_gas_air_system[index]) != '':
                setattr(GasAirData, list_gas_air_system[index],
                        form.get(list_gas_air_system[index]))
        return GasAirData

    #返回烟阻力json值
    @staticmethod
    def to_SmokeResistanceJson(SmokeResistanceData):
        json = {}
        for index in range(len(list_smoke_resistance)):
            json[list_smoke_resistance[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(SmokeResistanceData, list_smoke_resistance[index])))
        return json

    @staticmethod
    def to_SmokeResistanceData(form, plan_id):
        SmokeResistanceData = GPGSmokeResistance.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_smoke_resistance)):
            if form.get(list_smoke_resistance[index]) != '':
                setattr(SmokeResistanceData, list_smoke_resistance[index],
                        form.get(list_smoke_resistance[index]))
        return SmokeResistanceData

    #返回风阻力json值
    @staticmethod
    def to_WindResistanceJson(WindResistanceData):
        json = {}
        for index in range(len(list_wind_resistance)):
            json[list_wind_resistance[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(WindResistanceData, list_wind_resistance[index])))
        return json

    @staticmethod
    def to_WindResistanceData(form, plan_id):
        WindResistanceData = GPGWindResistance.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_wind_resistance)):
            if form.get(list_wind_resistance[index]) != '':
                setattr(WindResistanceData, list_wind_resistance[index],
                        form.get(list_wind_resistance[index]))
        return WindResistanceData


    #返回锅炉页面初期值
    @staticmethod
    def to_BoilerJson(BoilerData):
        json = {}
        for index in range(len(list_boiler_of_pts)):
            json[list_boiler_of_pts[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(BoilerData, list_boiler_of_pts[index])))
        return json

    #获得锅炉页面表单的信息
    @staticmethod
    def to_BoilerOfPTS(form, plan_id):
        boiler = GPGBoilerOfPTS.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_boiler_of_pts)):
            if form.get(list_boiler_of_pts[index]) != '' :
                setattr(boiler, list_boiler_of_pts[index], form.get(list_boiler_of_pts[index]))
                # print("sdsd "+str(list_boiler_of_pts[index]))
            else:
                setattr(boiler, list_boiler_of_pts[index], None)
                # print("NONE " + str(list_boiler_of_pts[index]))
        return boiler

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
        economic = GasPowerGenerationEconomicIndicators.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_economic)):
                if form.get(list_column_economic[index]) != '':
                    setattr(economic, list_column_economic[index],
                            form.get(list_column_economic[index]))
                else:
                    setattr(economic, list_column_economic[index],
                            None)

        # 根据planid获得锅炉及汽轮机的数据
        # Turbine = GPGTurbineOfPTS.search_TurbineOfPTS(plan_id)
        Boiler = GPGBoilerOfPTS.search_BoilerOfPTS(plan_id)

        # 表单项目计算
        economic = economic_foctory.Factory().execute(economic, Boiler, form)

        return economic
    
    @staticmethod
    def convertNumber(number):
        if number is not None:
            return str(
                round(float(str(float(number)).rstrip('0')), 2))
        else:
            return str('')
    
    @staticmethod
    def getmdtitledict():
        mdtitledict = {"1heat": u"一、热机部分",
                       "2elec": u"二、电气部分",
                       "3control": u"三、热控部分",
                       "4control-fire": u"点火控制系统",
                       "5monitor": u"工业电视监控系统",
                       "5monitor-fire": u"炉膛火焰监视部分",
                       "6monitor-water": u"汽包水位监视部分",
                       "7water": u"四、水工部分",
                       "8chemistry-water": u"五、化学水系统"
                       }
        return mdtitledict
