# -*- coding: utf-8 -*-
import os
from datetime import datetime
import json
import math
from config import config
from ..model.coalchpModels import CoalCHPNeedsQuestionnaire, CoalCHPComponent,\
     CoalCHPFurnaceCalculation, CoalCHPCoalHandingSystem,\
     CoalCHPRemovalAshSlag, CoalCHPDesulfurization, CoalCHPCirculatingWater,\
     CoalCHPSmokeAirSystem, CoalCHPBoilerAuxiliaries, \
     CoalCHPTurbineBackpressure, CoalCHPEconomicIndicators,\
     CoalCHPChemicalWater, CoalCHPChimney, CoalCHPHeatSupply,\
     CoalCHPOfficialProcess, CoalchpTurbineAuxiliary
from flask_login import current_user
from ...models import Company, Plan, Module, MyException, EquipmentList
from execution_strategy import Furnace_calculationBefore,\
     boilerAuxiliariesBefore, chemicalWaterBefore,\
     CoalTurbineAuxiliaryBefore
from app.main.service.turbine import turbine_foctory
from app.main.service.economic import economic_foctory
from imgProcessing.logic.imgInfoList import GetimgInfoList
from util.imgdealwith.imagedealwith import imageProcesse
from util.get_all_path import GetPath
from app.ccpp import gl

list_column_questionnaire = [
    's_fuel_design', 's_fuel_check', 's_carbon_design', 's_carbon_check',
    's_hydrogen_design', 's_hydrogen_check', 's_oxygen_design',
    's_oxygen_check', 's_nitrogen_design', 's_nitrogen_check',
    's_sulfur_design', 's_sulfur_check', 's_water_design', 's_water_check',
    's_grey_design', 's_grey_check', 's_daf_design', 's_daf_check',
    's_grindability_design', 's_grindability_check', 's_low_design',
    's_low_check', 'w_altitude_value', 'w_mean_annual_temperature_value',
    'w_mean_summer_temperature_value', 'w_mean_winter_temperature_value',
    'w_extreme_high_temperature_value', 'w_extreme_low_temperature_value',
    'w_mean_annual_barometric_value', 'w_mean_summer_barometric_value',
    'w_mean_winter_barometric_value',
    'w_annual_average_relative_humidity_value',
    'w_mean_summer_relative_humidity_value',
    'w_mean_winter_relative_humidity_value', 'ihl_steam_pressure_level_value',
    'ihl_steam_temperature_level_value', 'ihl_steam_time_value',
    'ihl_recent_steam_flow_range_value', 'ihl_forward_steam_flow_range_value',
    'ihl_condensate_water_iron_value',
    'ihl_condensate_water_recovery_rate_value',
    'hhl_heating_occasions_type_value', 'hhl_year_heating_days_value',
    'hhl_recent_heating_area_value', 'hhl_forward_heating_area_value',
    'os_planning_area_value', 'os_planned_expansion_capacity_value',
    'os_local_water_condition_value', 'oe_electrical_load_demand_value',
    'oe_higher_voltage_level_value', 'oe_plant_distance_higher_change_value',
    'oe_is_internet_access_value', 'oe_is_isolated_network_value',
    'op_flue_gas_sox_limits_value', 'op_flue_gas_nox_limits_value',
    'op_flue_gas_dust_limits_value', 'od_use_desulfurization_form_value',
    'od_use_denitration_form_value', 'od_limestone_supply_value',
    'od_urea_or_ammonia_water_supply_value'
]

list_column_furnace = [
    'plan_id', 's_carbon_design', 's_carbon_check', 's_hydrogen_design',
    's_hydrogen_check', 's_oxygen_design', 's_oxygen_check',
    's_nitrogen_design', 's_nitrogen_check', 's_sulfur_design',
    's_sulfur_check', 's_grey_design', 's_grey_check', 's_water_design',
    's_water_check', 's_sum_design', 's_sum_check', 's_daf_design',
    's_daf_check', 's_grindability_design', 's_grindability_check',
    's_low_design', 's_low_check', 's_low_1_design', 's_low_1_check',
    's_low_estimation_design', 's_low_estimation_check',
    's_high_estimation_design', 's_high_estimation_check',
    'f_steam_flow_design', 'f_steam_flow_check', 'f_steam_pressure_design',
    'f_steam_pressure_check', 'f_steam_temperature_design',
    'f_steam_temperature_check', 'f_steam_enthalpy_design',
    'f_steam_enthalpy_check', 'f_boiler_pressure_design',
    'f_boiler_pressure_check', 'f_saturated_water_enthalpy_design',
    'f_saturated_water_enthalpy_check', 'f_water_temperature_design',
    'f_water_temperature_check', 'f_water_enthalpy_design',
    'f_water_enthalpy_check', 'f_boiler_efficiency_design',
    'f_boiler_efficiency_check', 'f_unburned_loss_design',
    'f_unburned_loss_check', 'f_blowdown_rate_design', 'f_blowdown_rate_check',
    'f_boiler_consumption_design', 'f_boiler_consumption_check',
    'f_calculation_consumption_design', 'f_calculation_consumption_check',
    'd_total_design', 'd_total_check', 'd_boiler_total_design',
    'd_boiler_total_check', 'd_ash_share_design', 'd_ash_share_check',
    'd_dust_share_design', 'd_dust_share_check', 'd_ash_total_design',
    'd_ash_total_check', 'd_dust_total_design', 'd_dust_total_check',
    'a_air_volumn_design', 'a_air_volumn_check', 'a_hot_temperature_design',
    'a_hot_temperature_check', 'a_humidity_design', 'a_humidity_check',
    'a_pressure_design', 'a_pressure_check', 'a_temperature_design',
    'a_temperature_check', 'a_saturation_pressure_design',
    'a_saturation_pressure_check', 'a_steam_perssure_design',
    'a_steam_perssure_check', 'a_air_humidity_design', 'a_air_humidity_check',
    'a_standard_air_humidity_design', 'a_standard_air_humidity_check',
    'a_wet_air_volumn_design', 'a_wet_air_volumn_check',
    's_nitrogen_volume_design', 's_nitrogen_volume_check',
    's_dioxide_volume_design', 's_dioxide_volume_check',
    's_steam_volume_design', 's_steam_volume_check', 's_smoke_volume_design',
    's_smoke_volume_check', 's_1kg_weight_design', 's_1kg_weight_check',
    's_wet_smoke_density_design', 's_wet_smoke_density_check',
    'p_boiler_air_design', 'p_boiler_air_check', 'p_wind_design',
    'p_wind_check', 'p_wind_air_design', 'p_wind_air_check', 'p_high_design',
    'p_high_check', 'p_hign_air_design', 'p_hign_air_check', 'p_low_design',
    'p_low_check', 'p_low_air_design', 'p_low_air_check', 'p_fule_design',
    'p_fule_check', 'p_fule_air_design', 'p_fule_air_check', 'p_heater_design',
    'p_heater_check', 'p_heater_air_design', 'p_heater_air_check',
    'p_plus_air_design', 'p_plus_air_check', 'p_dust_exit_design',
    'p_dust_exit_check', 'p_dust_design', 'p_dust_check',
    'p_dust_entry_design', 'p_dust_entry_check', 'p_plus_dust_design',
    'p_plus_dust_check', 'p_fans_air_design', 'p_fans_air_check',
    'p_1kg_volume_design', 'p_1kg_volume_check', 'p_1kg_quality_design',
    'p_1kg_quality_check', 'p_heater_type_design', 'p_heater_type_check',
    'p_heater_first_entry_design', 'p_heater_first_entry_check',
    'p_heater_second_entry_design', 'p_heater_second_entry_check',
    'p_heater_first_exit_design', 'p_heater_first_exit_check',
    'p_heater_second_exit_design', 'p_heater_second_exit_check',
    'p_smoke_temperature_design', 'p_smoke_temperature_check',
    'a_theory_air_quality_design', 'a_theory_air_quality_check',
    'a_boiler_air_design', 'a_boiler_air_check', 'a_actual_air_design',
    'a_actual_air_check', 'a_calculation_consumption_design',
    'a_calculation_consumption_check', 'a_actual_air_total_design',
    'a_actual_air_total_check', 'a_first_wind_volume_design',
    'a_first_wind_volume_check', 'a_cwind_temperature_calculation_design',
    'a_cwind_temperature_calculation_check', 'a_local_pressure_design',
    'a_local_pressure_check', 'a_first_cwind_standard_design',
    'a_first_cwind_standard_check', 'a_first_cwind_actual_design',
    'a_first_cwind_actual_check', 'a_first_standard_air_density_design',
    'a_first_standard_air_density_check', 'a_first_cwind_flow_design',
    'a_first_cwind_flow_check', 'a_first_cwind_density_design',
    'a_first_cwind_density_check', 'a_check_design', 'a_check_check',
    'a_first_hwind_temperatue_design', 'a_first_hwind_temperatue_check',
    'a_first_hwind_flow_design', 'a_first_hwind_flow_check',
    'a_first_wet_air_density_design', 'a_first_wet_air_density_check',
    'a_second_wind_volume_design', 'a_second_wind_volume_check',
    'a_cwind_temperature_design', 'a_cwind_temperature_check',
    'a_second_cwind_standard_design', 'a_second_cwind_standard_check',
    'a_second_cwind_actual_design', 'a_second_cwind_actual_check',
    'a_second_standard_air_density_design',
    'a_second_standard_air_density_check', 'a_second_cwind_flow_design',
    'a_second_cwind_flow_check', 'a_second_cwind_density_design',
    'a_second_cwind_density_check', 'a_second_hwind_temperatue_design',
    'a_second_hwind_temperatue_check', 'a_second_hwind_flow_design',
    'a_second_hwind_flow_check', 'a_second_wet_air_density_design',
    'a_second_wet_air_density_check', 'h_1kg_volume_design',
    'h_1kg_volume_check', 'h_1kg_quality_design', 'h_1kg_quality_check',
    'h_calculation_consumption_design', 'h_calculation_consumption_check',
    'h_standard_smoke_flow_design', 'h_standard_smoke_flow_check',
    'h_smoke_flow_design', 'h_smoke_flow_check', 'h_smoke_temperature_design',
    'h_smoke_temperature_check', 'h_smoke_volume_design',
    'h_smoke_volume_check', 'h_smoke_density_design', 'h_smoke_density_check',
    'd_exit_air_design', 'd_exit_air_check', 'd_wind_parameter_design',
    'd_wind_parameter_check', 'd_entry_air_design', 'd_entry_air_check',
    'd_cold_air_temperature_design', 'd_cold_air_temperature_check',
    'd_entry_somke_temperature_design', 'd_entry_somke_temperature_check',
    'd_standard_1kg_volume_design', 'd_standard_1kg_volume_check',
    'd_entry_1kg_quality_design', 'd_entry_1kg_quality_check',
    'd_standard_smoke_flow_design', 'd_standard_smoke_flow_check',
    'd_entry_somke_flow_design', 'd_entry_somke_flow_check',
    'd_entry_smoke_actual_flow_design', 'd_entry_smoke_actual_flow_check',
    'e_wind_parameter_design', 'e_wind_parameter_check',
    'e_air_parameter_design', 'e_air_parameter_check',
    'e_smoke_temperature_design', 'e_smoke_temperature_check',
    'e_standard_1kg_volume_design', 'e_standard_1kg_volume_check',
    'e_1kg_quality_design', 'e_1kg_quality_check',
    'e_standard_smoke_flow_design', 'e_standard_smoke_flow_check',
    'e_smoke_flow_design', 'e_smoke_flow_check', 'e_smoke_actual_flow_design',
    'e_smoke_actual_flow_check', 'e_smoke_actual_density_design',
    'e_smoke_actual_density_check', 'i_wind_parameter_design',
    'i_wind_parameter_check', 'i_air_parameter_design',
    'i_air_parameter_check', 'i_smoke_temperature_design',
    'i_smoke_temperature_check', 'i_standard_1kg_volume_design',
    'i_standard_1kg_volume_check', 'i_1kg_quality_design',
    'i_1kg_quality_check', 'i_standard_smoke_flow1_design',
    'i_standard_smoke_flow1_check', 'i_standard_smoke_flow2_design',
    'i_standard_smoke_flow2_check', 'i_smoke_flow_design',
    'i_smoke_flow_check', 'i_smoke_actual_flow1_design',
    'i_smoke_actual_flow1_check', 'i_smoke_actual_flow2_design',
    'i_smoke_actual_flow2_check', 'i_smoke_actual_density_design',
    'i_smoke_actual_density_check', 'i_wet_smoke_actual_density_design',
    'i_wet_smoke_actual_density_check', 'go_oxygen_vol_design',
    'go_oxygen_vol_check', 'go_theoretica_vol_design',
    'go_theoretica_vol_check', 'go_theoretica_flow_design',
    'go_theoretica_flow_check', 'go_calculation_consumption_design',
    'go_calculation_consumption_check', 'go_air_parameter_design',
    'go_air_parameter_check', 'go_standard_1kg_volume_design',
    'go_standard_1kg_volume_check', 'go_smoke_flow_design',
    'go_smoke_flow_check', 'go_drygas_oxygen_vol_design',
    'go_drygas_oxygen_vol_check', 'go_total_combustion_product_vol_design',
    'go_total_combustion_product_vol_check', 'boiler_params_select'
]

list_column_handingsystem = [
    'plan_id', 'b_boiler_rated_coal_capacity_design',
    'b_boiler_rated_coal_capacity_check',
    'b_boiler_daily_utilization_hours_design',
    'b_boiler_daily_utilization_hours_check',
    'b_coal_daily_consumption_design', 'b_coal_daily_consumption_check',
    'b_boiler_annual_utilization_hours_design',
    'b_boiler_annual_utilization_hours_check',
    'b_coal_annual_consumption_design', 'b_coal_annual_consumption_check',
    'b_daily_coal_unbalanced_coefficient_design',
    'b_daily_coal_unbalanced_coefficient_check',
    'b_daily_rail_coal_amount_design', 'b_daily_rail_coal_amount_check',
    'b_daily_vehicle_coal_amount_design', 'b_daily_vehicle_coal_amount_check',
    'c_boiler_hour_coal_capacity_design', 'c_boiler_hour_coal_capacity_check',
    'c_boiler_daily_working_hours_design',
    'c_boiler_daily_working_hours_check', 'c_coal_store_days_design',
    'c_coal_store_days_check', 'c_coalyard_store_amount_design',
    'c_coalyard_store_amount_check',
    'c_coal_channel_occupy_coefficient_design',
    'c_coal_channel_occupy_coefficient_check',
    'c_coal_shape_coefficient_design', 'c_coal_shape_coefficient_check',
    'c_coal_height_design', 'c_coal_height_check',
    'c_coal_bulk_density_design', 'c_coal_bulk_density_check',
    'c_coalyard_area_design', 'c_coalyard_area_check', 'c_height_design',
    'c_height_check', 'c_width_design', 'c_width_check',
    'e_effective_cubage_calculated_design',
    'e_effective_cubage_calculated_check', 'e_coal_bunker_counts_design',
    'e_coal_bunker_counts_check', 'e_effective_cubage_selected_design',
    'e_effective_cubage_selected_check', 'e_backstep_consumption_hours_design',
    'e_backstep_consumption_hours_check',
    't_transport_unbalanced_coefficient_design',
    't_transport_unbalanced_coefficient_check',
    't_transportsystem_effective_working_hours_design',
    't_transportsystem_effective_working_hours_check',
    't_transportsystem_amount_design', 't_transportsystem_amount_check',
    't_vehicle_capacity_tonnage_design', 't_vehicle_capacity_tonnage_check',
    't_daily_working_hours_design', 't_daily_working_hours_check',
    't_daily_received_coal_amount_design',
    't_daily_received_coal_amount_check',
    't_vehicle_daily_incoming_times_design',
    't_vehicle_daily_incoming_times_check',
    't_vehicle_perhour_incoming_times_design',
    't_vehicle_perhour_incoming_times_check',
    's_mutil_boiler_rated_coal_capacity_design',
    's_mutil_boiler_rated_coal_capacity_check',
    's_mutil_boiler_rated_coal_amount_design',
    's_mutil_boiler_rated_coal_amount_check',
    's_transportsystem_output_design', 's_transportsystem_output_check',
    's_transportsystem_working_hours_design',
    's_transportsystem_working_hours_check', 's_shift_working_hours_design',
    's_shift_working_hours_check', 's_belt_width_design', 's_belt_width_check',
    's_section_coefficient_design', 's_section_coefficient_check',
    's_belt_speed_design', 's_belt_speed_check',
    's_material_bulk_density_design', 's_material_bulk_density_check',
    's_belt_max_transport_capacity_design',
    's_belt_max_transport_capacity_check', 'g_equipment_sets_design',
    'g_equipment_sets_check', 'g_surplus_design', 'g_surplus_check',
    'g_single_coal_feeder_output_design', 'g_single_coal_feeder_output_check'
]

list_column_removalAshSlag = [
    'plan_id', 'a_total_ash_residue_after', 'a_fly_ash_content',
    'a_dust_collector_inlet_', 'a_the_imported_smoke_volume',
    'a_the_smoke_volume_flow', 'a_the_smoke_concentration',
    'a_the_smoke_concentration_solid', 'a_collection_efficiency',
    'a_the_smoke_concentration_chimney', 'a_dust_collector_stack',
    'a_ash_under_dust_collector', 'a_the_imported_smoke_real_state',
    'a_flue_gas_concentratio', 'r_removal_coefficient',
    'r_removal_the_ash_system', 'r_dry_ash_accumulation_density',
    'r_slag_accumulation_coefficient', 'r_stored_ash',
    'r_effective_volume_ash_storage', 'r_dia', 'r_height', 'g_grey_gas',
    'g_air_transport_ash_system', 's_slag_amount',
    's_output_cold_single_stage', 's_cold_single_stage_count',
    's_slag_removal_system', 's_high_temperature_belt_conveyor',
    's_cold_slag_accumulation_density', 's_slag_accumulation_coefficient',
    's_sludge_time', 's_slag_storage_volume_effective', 's_dia', 's_height'
]

list_column_desulfurization = [
    's_sulfur_design', 's_calcu_coal_consume', 's_aflame_generate_so2',
    's_desulfrization_before_so2', 's_fan_smoke_flow',
    's_no_desulfurization_so2', 's_desulfurization_efficiency',
    's_desulfrization_after_so2', 's_desulfrization_after_discharge_so2',
    'r_furnace_rate', 'r_furnace_concentration', 'r_others_mass',
    'r_others_mole', 'r_calcium_sulfur_rate', 'r_nees_caco3_mole',
    'r_nees_caco3_mass', 'r_use_caco3_mass', 'r_generate_coco3_mass',
    'r_add_mass', 'r_caco3_pure', 'r_coco3_consume', 'r_generate_grey',
    'r_storage_time', 'r_storage_output', 'r_storage_density',
    'r_storage_fullness', 'r_storage_volume', 'r_height', 'r_diameter',
    'd_limestone_pure', 'd_proportion_ca_s', 'd_desulfurization_efficiency',
    'd_limestone_consume', 'd_gengrate_coca4', 'n_before_nox_concentration',
    'n_input_smoke', 'n_desulfurization_efficiency', 'n_before_nox_discharge',
    'n_after_nox_concentration', 'n_env_after_nox_concentration',
    'n_after_nox_discharge', 'd_denitration_percentage',
    'd_denitration_quality', 'd_after_nox_discharge', 'd_denitration_molar',
    'd_escape_rate', 'd_escape_quality', 'd_escape_quality_urea',
    'd_nh3nox_molar', 'd_urea_nox_molar', 'd_urea_nox_quality',
    'd_theory_urea', 'd_use_urea', 'd_water_urea', 'd_days_urea',
    'd_capacity_urea', 'g_denitration_percentage', 'g_after_nox_discharge',
    'g_denitration_quality', 'g_escape_rate', 'g_escape_quality',
    'g_escape_quality_urea', 'g_nh3nox_molar', 'g_urea_nox_molar',
    'g_urea_nox_quality', 'g_theory_urea', 'g_use_urea'
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
    'v_circulating_pool_size', 'v_circulating_pool_long',
    'v_circulating_pool_wide', 'v_circulating_pool_hight',
    'v_check_circulating_pool_size', 'p_spray_density', 'p_spray_area',
    'p_select_f', 'p_count', 'p_single_cold_amount', 'p_select_s',
    'c_pressure_condenser', 'c_condenser_tube_friction',
    'c_circulating_water_pressure', 'c_circulating_pool_pressure',
    'c_circulation_height_difference', 'c_height_difference_inlet',
    'c_pipe_losses', 'c_y_losses', 'c_pumping_head', 'c_flow', 'c_pump_power',
    'c_mechine_power', 'c_motor_power', 'c_motor_backup_coefficient',
    'c_supporting_motor_power', 'c_forklift_parameters_power',
    'c_forklift_parameters_flow', 'c_forklift_parameters_lift',
    'circleWaterSelect'
]

list_column_smokeAirSystem = [
    'a_altitude', 'a_atmospheric_pressure', 'p_the_case_temperature_f',
    'p_standard_of_pressure_f', 'p_standard_of_flow_f', 'p_temperature_case_f',
    'p_local_atmosphere_f', 'p_operational_point_flow_f',
    'p_the_case_temperature_s', 'p_standard_of_pressure_s',
    'p_standard_of_flow_s', 'p_temperature_case_s', 'p_local_atmosphere_s',
    'p_operational_point_flow_s', 'p_the_case_temperature_t',
    'p_standard_of_pressure_t', 'p_standard_of_flow_t', 'p_temperature_case_t',
    'p_local_atmosphere_t', 'p_operational_point_flow_t', 'f_name',
    'f_air_temperature', 'f_boiler_body_resistance', 'f_duct_resistance',
    'f_local_atmosphere', 'f_smoke_flow_rate_condition',
    'f_nameplate_medium_temperature', 'f_fan_total_pressure',
    'f_fan_select_total_pressure', 'f_fan_selection_flow', 'f_fan_power',
    'f_electric_motor_power', 'f_fan_shaft_power', 'f_fan_security_volumn',
    'f_motor_power', 's_name', 's_air_temperature', 's_boiler_body_resistance',
    's_duct_resistance', 's_local_atmosphere', 's_smoke_flow_rate_condition',
    's_nameplate_medium_temperature', 's_fan_total_pressure',
    's_fan_select_total_pressure', 's_fan_selection_flow', 's_fan_power',
    's_electric_motor_power', 's_fan_shaft_power', 's_fan_security_volumn',
    's_motor_power', 'i_name', 'i_air_temperature', 'i_boiler_body_resistance',
    'i_denitration', 'i_duster', 'i_resistance_desulfurization_fan',
    'i_duct_resistance', 'i_local_atmosphere', 'i_smoke_flow_rate_condition',
    'i_nameplate_medium_temperature', 'i_fan_total_pressure',
    'i_fan_select_total_pressure', 'i_fan_selection_flow', 'i_fan_power',
    'i_electric_motor_power', 'i_fan_shaft_power', 'i_fan_security_volumn',
    'i_motor_power', 'r_name', 'r_air_temperature', 'r_boiler_body_resistance',
    'r_duct_resistance', 'r_local_atmosphere', 'r_smoke_flow_rate_condition',
    'r_nameplate_medium_temperature', 'r_fan_total_pressure',
    'r_fan_select_total_pressure', 'r_fan_selection_flow', 'r_fan_power',
    'r_electric_motor_power', 'r_fan_shaft_power', 'r_fan_security_volumn',
    'r_motor_power', 'r_lectotype', 'f_lectotype', 'i_lectotype',
    's_lectotype', 'f_count', 'i_count', 'f_wind_Proportion', 's_count'
]
list_column_BoilerAuxiliaries = [
    'r_boiler_evaporation', 'r_emission_time', 'r_emission_rate',
    'r_sewage_quantity', 'r_drum_pressure', 'r_drum_aturatedwater_enthalpy',
    'r_work_pressure', 'r_work_aturatedwater_enthalpy',
    'r_work_latentheat_vaporization', 'r_ultimate_strength',
    'r_affluence_coefficient', 'r_volume', 'r_specifications',
    'c_boiler_evaporation', 'c_emission_rate', 'c_sewage_quantity',
    'c_drum_pressure', 'c_drum_aturatedwater_enthalpy', 'c_work_pressure',
    'c_work_aturatedwater_enthalpy', 'c_work_steam_pecificvolume',
    'c_work_latentheat_vaporization', 'c_steam_dryness', 'c_ultimate_strength',
    'c_vaporization_capacity', 'c_affluence_coefficient', 'c_volume',
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
    's_boiler_evaporation', 's_storage_time', 's_volume', 's_size_length',
    's_size_diameter', 't_new_steam_temperature', 't_new_pressure',
    't_new_enthalpy', 't_new_flow_rate', 't_reduce_water_temperature',
    't_reduce_water_pressure', 't_reduce_water_enthalpy',
    't_reduce_water_flow_rate', 't_reduce_steam_temperature',
    't_reduce_steam_pressure', 't_reduce_steam_enthalpy',
    't_reduce_enough_enthalpy', 't_reduce_persent', 't_rudece_flow_rate'
]

list_column_steam = [
    'e_turbine_efficiency', 'e_mechanical_efficiency',
    'e_generator_efficiency', 'e_steam_pressure', 'e_steam_temperature',
    'e_steam_flow', 'e_steam_entropy', 'e_steam_enthalpy',
    'e_exhaust_point_pressure', 'e_exhaust_point_temperature',
    'e_exhaust_point_entropy', 'e_exhaust_point_enthalpy',
    'e_exhaust_point_flow', 'e_exhaust_after_steam',
    'e_exhaust_after_pressure', 'e_exhaust_after_enthalpy',
    'e_exhaust_after_entropy', 'e_steam_exhaust_pressure',
    'e_steam_exhaust_enthalpy', 'e_backpressure_pressure',
    'e_backpressure_temperature', 'e_backpressure_enthalpy',
    'e_backpressure_flow', 'e_gross_generation', 'e_hot_data',
    'e_steam_extraction', 'e_steam_extraction_select', 'e_steam_water_loss',
    'e_throttle_flow', 'h_temperature', 'h_pressure', 'h_enthalpy', 'h_amount',
    'hh1_water_temperature', 'hh1_water_enthalpy', 'hh1_top_difference',
    'hh1_saturated_water_temperature', 'hh1_saturated_water_enthalpy',
    'hh1_work_pressure', 'hh1_pressure_loss', 'hh1_extraction_pressure',
    'hh1_extraction_enthalpy', 'hh1_extraction_amount',
    'hh2_water_temperature', 'hh2_water_enthalpy', 'hh2_top_difference',
    'hh2_saturated_water_temperature', 'hh2_saturated_water_enthalpy',
    'hh2_work_pressure', 'hh2_pressure_loss', 'hh2_extraction_pressure',
    'hh2_extraction_enthalpy', 'hh2_extraction_amount',
    'hh3_water_temperature', 'hh3_water_enthalpy', 'hh3_top_difference',
    'hh3_saturated_water_temperature', 'hh3_saturated_water_enthalpy',
    'hh3_work_pressure', 'hh3_pressure_loss', 'hh3_extraction_pressure',
    'hh3_extraction_enthalpy', 'hh3_extraction_amount', 'd_water_temperature',
    'd_water_enthalpy', 'd_work_pressure', 'd_pressure_loss',
    'd_extraction_pressure', 'd_extraction_enthalpy', 'd_extraction_amount',
    'lh1_water_temperature', 'lh1_water_enthalpy', 'lh1_top_difference',
    'lh1_saturated_water_temperature', 'lh1_saturated_water_enthalpy',
    'lh1_work_pressure', 'lh1_pressure_loss', 'lh1_extraction_pressure',
    'lh1_extraction_enthalpy', 'lh1_extraction_amount',
    'lh2_water_temperature', 'lh2_water_enthalpy', 'lh2_top_difference',
    'lh2_saturated_water_temperature', 'lh2_saturated_water_enthalpy',
    'lh2_work_pressure', 'lh2_pressure_loss', 'lh2_extraction_pressure',
    'lh2_extraction_enthalpy', 'lh2_extraction_amount',
    'lh3_water_temperature', 'lh3_water_enthalpy', 'lh3_top_difference',
    'lh3_saturated_water_temperature', 'lh3_saturated_water_enthalpy',
    'lh3_work_pressure', 'lh3_pressure_loss', 'lh3_extraction_pressure',
    'lh3_extraction_enthalpy', 'lh3_extraction_amount', 'c_water_temperature',
    'c_water_enthalpy', 'c_work_pressure', 'c_pressure_loss',
    'c_extraction_pressure', 'c_extraction_enthalpy', 'c_extraction_amount',
    'i_turbine_efficiency', 'i_mechanical_efficiency',
    'i_generator_efficiency', 'i_steam_pressure', 'i_steam_temperature',
    'i_steam_flow', 'i_steam_entropy', 'i_steam_enthalpy', 'i_high1_pressure',
    'i_high1_entropy', 'i_high1_temperature', 'i_high1_enthalpy',
    'i_high1_flow', 'i_steam_hh1_power', 'i_high2_pressure', 'i_high2_entropy',
    'i_high2_temperature', 'i_high2_enthalpy', 'i_high2_flow',
    'i_hh1_hh2_power', 'i_deoxidize_pressure', 'i_deoxidize_entropy',
    'i_deoxidize_temperature', 'i_deoxidize_enthalpy', 'i_deoxidize_flow',
    'i_hh2_deoxidize_power', 'i_exhaust_point_pressure',
    'i_exhaust_point_temperature', 'i_exhaust_point_entropy',
    'i_exhaust_point_enthalpy', 'i_exhaust_point_flow',
    'i_deoxidize_exhaust_power', 'i_low1_pressure', 'i_low1_entropy',
    'i_low1_temperature', 'i_low1_enthalpy', 'i_low1_flow',
    'i_exhaust_lh1_power', 'i_low2_pressure', 'i_low2_entropy',
    'i_low2_temperature', 'i_low2_enthalpy', 'i_low2_flow', 'i_lh1_lh2_power',
    'i_low3_pressure', 'i_low3_entropy', 'i_low3_temperature',
    'i_low3_enthalpy', 'i_low3_flow', 'i_lh2_lh3_power',
    'i_steam_exhaust_pressure', 'i_steam_exhaust_entropy',
    'i_steam_exhaust_enthalpy', 'i_steam_exhaust_enthalpy_actual',
    'i_steam_exhaust_enthalpy_steam', 'i_steam_exhaust_enthalpy_water',
    'i_steam_exhaust_dry', 'i_steam_exhaust_flow', 'i_lh2_steam_power',
    'i_total_power', 'i_calculation_error', 'e_steam_plus_enthalpy'
]

list_column_economic = [
    'condensate_backwater_pressure', 'condensate_backwater_temperature',
    'condensate_backwater_enthalpy', 'smoke_heat_consumption_rate',
    'heat_consumption_rate', 'smoke_steam_consumption_rate',
    'steam_consumption_rate', 'annual_useage_hours', 'annual_heat_hours',
    'annual_heat_supply', 'annual_power_generation',
    'plant_electricity_consumption', 'annual_power_supply',
    'boiler_efficiency', 'pipeline_efficiency', 'smoke_power_coal_consumption',
    'power_coal_consumption', 'smoke_supply_coal_consumption',
    'supply_coal_consumption', 'annual_average_thermoelectric_ratio',
    'smoke_heat_efficiency', 'heat_efficiency'
]

list_column_chemical_water = [
    'm_process_route', 'm_boiler_evaporation', 'm_makeup_steam',
    'm_steamwater_cycle_loss', 'm_pollution_loss', 'm_condensing_capacity',
    'm_condensate_loss', 'm_boiler_normal_watersupply', 'm_increase_loss',
    'm_boiler_max_watersupply', 'm_output', 'm_remove_salt_volume'
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

# 公用工程
list_column_official = [
    'o_oil_can',
    'o_oil_pump',
    'o_oil_pump_pressure',
    'o_boiler_type',
    'o_fire_way',
    'o_steam_parameter',
    'o_steam_volumn',
    'o_fuel_type',
    'o_install_way'
]

list_column_heat = [
    'heat_area', 'heat_hot_target', 'heat_hot_load', 'turbine_pressure',
    'heat_turbine_flow', 'use_flow', 'steam_supply_rate', 'hot_loss',
    'hot_turbine_flow'
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

list_column_steamClear = [
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
    '''
    格式化数据库中取出的值
    将decimal格式去掉多余无效的位数
    将null，None等字符过滤
    '''
    result = ""
    if not values or values == "null" or values == "None":
        result = ""
    elif values == "0":
        result = "0"
    # flag=number，只有数字类型的需要取出多余的0
    elif flag == "number":
        result = round(float(str(float(values)).rstrip('0')), 3)
    else:
        result = values
    return result


def toMyInt(value):
    return int(math.floor(float(value)))


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


def getstrcolm(obj):
    return str(float('%.2f' % float(obj) if obj is not None else 0.0))


class ToCoalCHP():
    '''
    根据planId返回当前方案的主要设备参数字符串
    '''
    def getMainEquipmentPara(self, planId):
        furnace = CoalCHPFurnaceCalculation.search_furnace_calculation(planId)
        turbine = CoalCHPTurbineBackpressure.search_turbineBackpressure(planId)
        mainEquipmentPara = u''

        if furnace.f_steam_flow_design is not None and furnace.boiler_params_select is not None:
            mainEquipmentPara += u'1X' + gl.getstrcolm(furnace.f_steam_flow_design) + u't/h'
            if furnace.boiler_params_select == 1:
                mainEquipmentPara += u'高温高压'
            elif furnace.boiler_params_select == 2:
                mainEquipmentPara += u'次高温次高压'
            elif furnace.boiler_params_select == 3:
                mainEquipmentPara += u'中温中压'
            else:
                pass

            # 燃煤只有一种锅炉
            mainEquipmentPara += u'常规循环流化床锅炉（CFB）。\n'

        if turbine.e_steam_extraction_select is not None and turbine.e_steam_type is not None and turbine.s_steam_type_test is not None:
            mainEquipmentPara += u'1X' + gl.getstrcolm(turbine.e_steam_extraction_select) + u'MW'
            if turbine.e_steam_type == '1':
                mainEquipmentPara += u'低温低压'
            elif turbine.e_steam_type == '2':
                mainEquipmentPara += u'次中温次中压'
            elif turbine.e_steam_type == '3':
                mainEquipmentPara += u'中温中压'
            elif turbine.e_steam_type == '4':
                mainEquipmentPara += u'次高温次高压'
            elif turbine.e_steam_type == '5':
                mainEquipmentPara += u'高温高压'
            else:
                pass

            if turbine.s_steam_type_test == 1:
                mainEquipmentPara += u'抽凝汽轮发电机组。'
            elif turbine.s_steam_type_test == 2:
                mainEquipmentPara += u'背压汽轮发电机组。'
            elif turbine.s_steam_type_test == 3:
                mainEquipmentPara += u'补凝汽轮发电机组。'
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
            company_id=companyId, module_id=Module.coalCHP, plan_name=planName).first()
        if not plan:
            plan = Plan()
            plan.user_id = current_user.id
            plan.company_id = companyId
            plan.module_id = Module.coalCHP
            plan.plan_create_date = datetime.now()
            plan.plan_update_date = datetime.now()
            plan.company_lnglat = company_lnglat
            plan.plan_name = planName
            Plan.insert_plan(plan)
        plan.company_location = companyLocation
        newPlan = Plan.query.filter_by(
            company_id=companyId, module_id=Module.coalCHP, plan_name=planName).first()
        return newPlan.id

    # 修改方案表的修改时间
    @staticmethod
    def update_plan_date(plan_id):
        plan = Plan.query.filter_by(id=plan_id).first()
        plan.plan_update_date = datetime.now()
        Plan.insert_plan(plan)

    @staticmethod
    def to_questionnaire(form, plan_id):
        questionnaire = CoalCHPNeedsQuestionnaire.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_questionnaire)):
            if form.get(list_column_questionnaire[index]) != '':
                setattr(questionnaire, list_column_questionnaire[index],
                        form.get(list_column_questionnaire[index]))
            else:
                setattr(questionnaire, list_column_questionnaire[index], None)
        return questionnaire

    @staticmethod
    def to_questionnaireJson(questionnaire):
        datas = {}
        planId = getattr(questionnaire, 'plan_id')
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        for index in range(len(list_column_questionnaire)):
            # 如果是字符串类型的字段则跳过此步奏
            if list_column_questionnaire[index] in [
                    'ihl_steam_time_value', 'hhl_heating_occasions_type_value',
                    'os_local_water_condition_value',
                    'oe_is_internet_access_value',
                    'oe_is_isolated_network_value',
                    'od_use_desulfurization_form_value',
                    'od_use_denitration_form_value',
                    'od_urea_or_ammonia_water_supply_value'
            ]:
                datas[list_column_questionnaire[index]] = getattr(
                    questionnaire, list_column_questionnaire[index])
            else:
                datas[list_column_questionnaire[index]] = format_value(
                    "number",
                    str(
                        getattr(questionnaire, list_column_questionnaire[
                            index])))

        datas['company_name'] = companyName
        datas['company_location'] = companyLocation
        datas['planId'] = planId
        datas['plan_name'] = plan.plan_name
        return datas

    @staticmethod
    def to_coalCHPComponentJson(id):
        datas = {}
        coalCHPComponent = CoalCHPComponent.search_coalCHPSort(id)
        datas['s_carbon'] = coalCHPComponent.carbon
        datas['s_hydrogen'] = coalCHPComponent.hydrogen
        datas['s_oxygen'] = coalCHPComponent.oxygen
        datas['s_nitrogen'] = coalCHPComponent.nitrogen
        datas['s_sulfur'] = coalCHPComponent.sulfur
        datas['s_water'] = coalCHPComponent.water
        datas['s_grey'] = coalCHPComponent.grey
        datas['s_daf'] = coalCHPComponent.daf
        datas['s_grindability'] = coalCHPComponent.grindability
        datas['s_low'] = coalCHPComponent.low
        return datas

    @staticmethod
    def to_furnaceJson(furnace):
        datas = {}
        for index in range(len(list_column_furnace)):
            if list_column_furnace[index] in [
                    'p_heater_type_design', 'p_heater_type_check'
            ]:
                datas[list_column_furnace[index]] = getattr(
                    furnace, list_column_furnace[index])
            else:
                datas[list_column_furnace[index]] = format_value(
                    "number",
                    str(getattr(furnace, list_column_furnace[index])))

        return datas

    @staticmethod
    def to_furnace(form, plan_id):
        furnace = CoalCHPFurnaceCalculation.query.filter_by(
            plan_id=plan_id).first()
        furnace = Furnace_calculationBefore().specialCalculation(furnace, form)
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
                setattr(furnace, list_column_furnace[index], None)
        setattr(furnace, 'plan_id', plan_id)
        list_column_furnace.append('f_steam_enthalpy_design')
        list_column_furnace.append('f_steam_enthalpy_check')

        list_column_furnace.append('a_saturation_pressure_design')
        list_column_furnace.append('a_saturation_pressure_check')

        list_column_furnace.append('f_water_enthalpy_design')
        list_column_furnace.append('f_water_enthalpy_check')

        list_column_furnace.append('f_saturated_water_enthalpy_design')
        list_column_furnace.append('f_saturated_water_enthalpy_check')
        return furnace

    @staticmethod
    def to_handingSystemJson(handingSystem):
        datas = {}
        for index in range(len(list_column_handingsystem)):
            datas[list_column_handingsystem[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(handingSystem, list_column_handingsystem[index])))
        return datas

    @staticmethod
    def to_handingSystem(form, plan_id):
        handingSystem = CoalCHPCoalHandingSystem.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_handingsystem)):
            if form.get(list_column_handingsystem[index]) != '':
                setattr(handingSystem, list_column_handingsystem[index],
                        form.get(list_column_handingsystem[index]))
            else:
                setattr(handingSystem, list_column_handingsystem[index], None)
        setattr(handingSystem, 'plan_id', plan_id)
        return handingSystem

    @staticmethod
    def to_removalAshSlagJson(removalAshSlag):
        datas = {}
        for index in range(len(list_column_removalAshSlag)):
            datas[list_column_removalAshSlag[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(
                    getattr(removalAshSlag, list_column_removalAshSlag[
                        index])))
        return datas

    @staticmethod
    def to_removalAshSlag(form, plan_id):
        removalAshSlag = CoalCHPRemovalAshSlag.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_removalAshSlag)):
            if form.get(list_column_removalAshSlag[index]) != '':
                setattr(removalAshSlag, list_column_removalAshSlag[index],
                        form.get(list_column_removalAshSlag[index]))
            else:
                setattr(removalAshSlag, list_column_removalAshSlag[index],
                        None)
        setattr(removalAshSlag, 'plan_id', plan_id)
        return removalAshSlag

    @staticmethod
    def to_desulfurizationJson(desulfurization):
        datas = {}
        for index in range(len(list_column_desulfurization)):
            datas[list_column_desulfurization[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(
                    getattr(desulfurization, list_column_desulfurization[
                        index])))
        return datas

    @staticmethod
    def to_desulfurization(form, plan_id):
        desulfurization = CoalCHPDesulfurization.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_desulfurization)):
            if form.get(list_column_desulfurization[index]) != '':
                setattr(desulfurization, list_column_desulfurization[index],
                        form.get(list_column_desulfurization[index]))
            else:
                setattr(desulfurization, list_column_desulfurization[index],
                        None)
        setattr(desulfurization, 'plan_id', plan_id)
        return desulfurization

    @staticmethod
    def to_circulatingWaterJson(circulatingWater):
        datas = {}
        for index in range(len(list_column_circulatingWater)):
            datas[list_column_circulatingWater[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(
                    getattr(circulatingWater, list_column_circulatingWater[
                        index])))
        return datas

    @staticmethod
    def to_circulatingWater(form, plan_id):
        circulatingWater = CoalCHPCirculatingWater.query.filter_by(
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

    @staticmethod
    def to_smokeAirSystemJson(smokeAirSystem):
        datas = {}
        for index in range(len(list_column_smokeAirSystem)):
            datas[list_column_smokeAirSystem[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(
                    getattr(smokeAirSystem, list_column_smokeAirSystem[
                        index])))
        return datas

    @staticmethod
    def to_smokeAirSystem(form, plan_id):
        smokeAirSystem = CoalCHPSmokeAirSystem.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_smokeAirSystem)):
            if form.get(list_column_smokeAirSystem[index]) != '':
                setattr(smokeAirSystem, list_column_smokeAirSystem[index],
                        form.get(list_column_smokeAirSystem[index]))
            else:
                setattr(smokeAirSystem, list_column_smokeAirSystem[index],
                        None)
        setattr(smokeAirSystem, 'plan_id', plan_id)
        return smokeAirSystem

    @staticmethod
    def to_boilerAuxiliariesJson(boilerAuxiliaries):
        datas = {}
        for index in range(len(list_column_BoilerAuxiliaries)):
            if list_column_BoilerAuxiliaries[index] in [
                    'r_specifications', 'c_specifications', 'p_specifications'
            ]:
                datas[list_column_BoilerAuxiliaries[index]] = getattr(
                    boilerAuxiliaries, list_column_BoilerAuxiliaries[index])
            else:
                datas[list_column_BoilerAuxiliaries[index]] = format_value(
                    "number",
                    str(
                        getattr(boilerAuxiliaries,
                                list_column_BoilerAuxiliaries[index])))

        return datas

    @staticmethod
    def to_boilerAuxiliaries(form, plan_id):
        boilerAuxiliaries = CoalCHPBoilerAuxiliaries.query.filter_by(
            plan_id=plan_id).first()
        boilerAuxiliaries = boilerAuxiliariesBefore().specialCalculation(
            boilerAuxiliaries, form)

        list_column_BoilerAuxiliaries.remove('r_drum_aturatedwater_enthalpy')
        list_column_BoilerAuxiliaries.remove('r_work_aturatedwater_enthalpy')
        list_column_BoilerAuxiliaries.remove('r_work_latentheat_vaporization')
        list_column_BoilerAuxiliaries.remove('c_drum_aturatedwater_enthalpy')
        list_column_BoilerAuxiliaries.remove('c_work_aturatedwater_enthalpy')
        list_column_BoilerAuxiliaries.remove('c_work_steam_pecificvolume')
        list_column_BoilerAuxiliaries.remove('c_work_latentheat_vaporization')
        list_column_BoilerAuxiliaries.remove('t_rudece_flow_rate')
        list_column_BoilerAuxiliaries.remove('t_reduce_enough_enthalpy')
        list_column_BoilerAuxiliaries.remove('t_reduce_steam_enthalpy')
        list_column_BoilerAuxiliaries.remove('t_reduce_water_flow_rate')
        list_column_BoilerAuxiliaries.remove('t_reduce_water_enthalpy')
        list_column_BoilerAuxiliaries.remove('t_reduce_water_pressure')
        list_column_BoilerAuxiliaries.remove('t_new_enthalpy')
        for index in range(len(list_column_BoilerAuxiliaries)):
            if form.get(list_column_BoilerAuxiliaries[index]) != '':
                setattr(boilerAuxiliaries,
                        list_column_BoilerAuxiliaries[index],
                        form.get(list_column_BoilerAuxiliaries[index]))
            else:
                setattr(boilerAuxiliaries,
                        list_column_BoilerAuxiliaries[index], None)
        list_column_BoilerAuxiliaries.append('r_drum_aturatedwater_enthalpy')
        list_column_BoilerAuxiliaries.append('r_work_aturatedwater_enthalpy')
        list_column_BoilerAuxiliaries.append('r_work_latentheat_vaporization')
        list_column_BoilerAuxiliaries.append('c_drum_aturatedwater_enthalpy')
        list_column_BoilerAuxiliaries.append('c_work_aturatedwater_enthalpy')
        list_column_BoilerAuxiliaries.append('c_work_steam_pecificvolume')
        list_column_BoilerAuxiliaries.append('c_work_latentheat_vaporization')
        list_column_BoilerAuxiliaries.append('t_rudece_flow_rate')
        list_column_BoilerAuxiliaries.append('t_reduce_enough_enthalpy')
        list_column_BoilerAuxiliaries.append('t_reduce_steam_enthalpy')
        list_column_BoilerAuxiliaries.append('t_reduce_water_flow_rate')
        list_column_BoilerAuxiliaries.append('t_reduce_water_enthalpy')
        list_column_BoilerAuxiliaries.append('t_reduce_water_pressure')
        list_column_BoilerAuxiliaries.append('t_new_enthalpy')

        setattr(boilerAuxiliaries, 'plan_id', plan_id)
        return boilerAuxiliaries

    # 化学水系统
    @staticmethod
    def to_chemicalWaterJson(chemicalWater):
        datas = {}
        for index in range(len(list_column_chemical_water)):
            datas[list_column_chemical_water[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(chemicalWater, list_column_chemical_water[index])))

        return datas

    @staticmethod
    def to_chemicalWater(form, plan_id):
        chemicalWater = CoalCHPChemicalWater.query.filter_by(
            plan_id=plan_id).first()
        chemicalWater = chemicalWaterBefore().specialCalculation(
            chemicalWater, form)
        # 根据页面输入的参数算出的值不被页面上原来的值覆盖 
        list_column_chemical_water.remove('m_steamwater_cycle_loss')
        list_column_chemical_water.remove('m_pollution_loss')
        list_column_chemical_water.remove('m_condensate_loss')
        list_column_chemical_water.remove('m_boiler_normal_watersupply')
        list_column_chemical_water.remove('m_increase_loss')
        list_column_chemical_water.remove('m_boiler_max_watersupply')
        list_column_chemical_water.remove('m_remove_salt_volume')
        for index in range(len(list_column_chemical_water)):
            if form.get(list_column_chemical_water[index]) != '':
                setattr(chemicalWater, list_column_chemical_water[index],
                        form.get(list_column_chemical_water[index]))
            else:
                setattr(chemicalWater, list_column_BoilerAuxiliaries[index],
                        None)
        list_column_chemical_water.append('m_steamwater_cycle_loss')
        list_column_chemical_water.append('m_pollution_loss')
        list_column_chemical_water.append('m_condensate_loss')
        list_column_chemical_water.append('m_boiler_normal_watersupply')
        list_column_chemical_water.append('m_increase_loss')
        list_column_chemical_water.append('m_boiler_max_watersupply')
        list_column_chemical_water.append('m_remove_salt_volume')

        setattr(chemicalWater, 'plan_id', plan_id)
        return chemicalWater

    # 返回烟囱Json值
    @staticmethod
    def to_ChimneyJson(Chimney):
        json = {}
        for index in range(len(list_column_chimney)):
            json[list_column_chimney[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(Chimney, list_column_chimney[index])))
        return json

    @staticmethod
    def to_ChimneyData(form, plan_id):
        chimneyData = CoalCHPChimney.query.filter_by(plan_id=plan_id).first()

        for index in range(len(list_column_chimney)):
            if form.get(list_column_chimney[index]) != '':
                setattr(chimneyData, list_column_chimney[index],
                        form.get(list_column_chimney[index]))
            else:
                setattr(chimneyData, list_column_chimney[index], None)
        return chimneyData

    # 返回汽轮机页面初期值
    @staticmethod
    def to_steamJson(steamturbine):
        datas = {}
        for index in range(len(list_column_steam)):
            if list_column_steam[index] == 'e_steam_exhaust_pressure' or list_column_steam[index] == 'c_work_pressure':
                datas[list_column_steam[index]] = format_value2(
                    "number",
                    str(getattr(steamturbine, list_column_steam[index])))
            else:
                datas[list_column_steam[index]] = format_value(
                    "number",
                    str(getattr(steamturbine, list_column_steam[index])))

        datas['e_steam_type'] = getattr(steamturbine, 'e_steam_type')
        datas['h_assume'] = getattr(steamturbine, 'h_assume')
        datas['s_parameter_flg'] = getattr(steamturbine, 's_parameter_flg')
        datas['s_steam_type_test'] = getattr(steamturbine, 's_steam_type_test')
        datas['s_temperature_pressure'] = getattr(steamturbine,
                                                  's_temperature_pressure')
        datas['s_hh_grade'] = getattr(steamturbine, 's_hh_grade')
        datas['s_lh_grade'] = getattr(steamturbine, 's_lh_grade')
        return datas

    #清理汽轮机旧记录
    @staticmethod
    def steamClear(plan_id):
        steam = CoalCHPTurbineBackpressure.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_steamClear)):
            setattr(steam, list_column_steamClear[index],
                            None)
        return steam

    # 获得汽轮机页面表单的信息
    @staticmethod
    def to_steam(form, plan_id):
        steam = CoalCHPTurbineBackpressure.query.filter_by(
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

# 取数据库值生成键值对（生成报告用）

    @staticmethod
    def getReportData(planId):
        questionnaire = CoalCHPNeedsQuestionnaire.query.filter_by(
            plan_id=planId).first()
        furnace = CoalCHPFurnaceCalculation.query.filter_by(
            plan_id=planId).first()
        handingSystem = CoalCHPCoalHandingSystem.query.filter_by(
            plan_id=planId).first()
        circulatingWater = CoalCHPCirculatingWater.query.filter_by(
            plan_id=planId).first()
        smokeAirSystem = CoalCHPSmokeAirSystem.query.filter_by(
            plan_id=planId).first()
        removalAshSlag = CoalCHPRemovalAshSlag.query.filter_by(
            plan_id=planId).first()
        circulatingWater = CoalCHPCirculatingWater.query.filter_by(
            plan_id=planId).first()
        boilerAuxiliaries = CoalCHPBoilerAuxiliaries.query.filter_by(
            plan_id=planId).first()
        d_total_design = None
        if furnace.d_total_design:
            d_total_design = furnace.d_total_design / 1000
        d_total_design_day = None
        d_ash_total_design_day = None
        d_dust_total_design_day = None
        d_total_design_year = None
        d_ash_total_design_year = None
        d_dust_total_design_year = None
        if furnace.d_total_design and furnace.d_ash_total_design and furnace.d_dust_total_design:
            d_total_design_day = furnace.d_total_design * 24
            d_ash_total_design_day = furnace.d_ash_total_design * 24
            d_dust_total_design_day = furnace.d_dust_total_design * 24
            d_total_design_year = d_total_design_day * 365
            d_ash_total_design_year = d_ash_total_design_day * 365
            d_dust_total_design_year = d_dust_total_design_day * 365
        list_report_data = {
            u'需求调查表D2':
            questionnaire.w_mean_annual_temperature_value,
            u'需求调查表D3':
            questionnaire.w_mean_summer_temperature_value,
            u'需求调查表D4':
            questionnaire.w_mean_winter_temperature_value,
            u'需求调查表D5':
            questionnaire.w_extreme_high_temperature_value,
            u'需求调查表D6':
            questionnaire.w_extreme_low_temperature_value,
            u'需求调查表D7':
            questionnaire.w_mean_annual_barometric_value,
            u'需求调查表D8':
            questionnaire.w_mean_summer_barometric_value,
            u'需求调查表D9':
            questionnaire.w_mean_winter_barometric_value,
            u'需求调查表D10':
            questionnaire.w_annual_average_relative_humidity_value,
            u'需求调查表D11':
            questionnaire.w_mean_summer_relative_humidity_value,
            u'需求调查表D12':
            questionnaire.w_mean_winter_relative_humidity_value,
            u'烟风系统计算F29数据':
            smokeAirSystem.f_fan_selection_flow,
            u'烟风系统计算F28数据':
            smokeAirSystem.f_fan_select_total_pressure,
            u'台数f':
            smokeAirSystem.f_count,
            u'烟风系统计算F45数据':
            smokeAirSystem.s_fan_selection_flow,
            u'烟风系统计算F44数据':
            smokeAirSystem.s_fan_select_total_pressure,
            u'台数s':
            smokeAirSystem.s_count,
            u'烟风系统计算F80数据':
            smokeAirSystem.r_fan_selection_flow,
            u'烟风系统计算F79数据':
            smokeAirSystem.r_fan_select_total_pressure,
            u'烟风系统计算F64数据':
            smokeAirSystem.i_fan_selection_flow,
            u'烟风系统计算F63数据':
            smokeAirSystem.i_fan_select_total_pressure,
            u'台数i':
            smokeAirSystem.i_count,
            u'锅炉本体计算G135数据':
            furnace.d_entry_smoke_actual_flow_design,
            u'输煤系统计算F7数据':
            handingSystem.b_coal_annual_consumption_design,
            u'输煤系统计算F3数据':
            handingSystem.b_boiler_daily_utilization_hours_design,
            u'输煤系统计算F5数据':
            handingSystem.b_coal_daily_consumption_design,
            # u'输煤系统计算F7数据': handingSystem.b_coal_annual_consumption_design,
            u'输煤系统计算F8数据':
            handingSystem.b_daily_coal_unbalanced_coefficient_design,
            u'输煤系统计算F9数据':
            handingSystem.b_daily_rail_coal_amount_design,
            u'输煤系统计算F37数据':
            handingSystem.t_vehicle_capacity_tonnage_design,
            u'输煤系统计算F38数据':
            handingSystem.t_daily_working_hours_design,
            u'输煤系统计算F40数据':
            handingSystem.t_vehicle_daily_incoming_times_design,
            u'输煤系统计算F41数据':
            handingSystem.t_vehicle_perhour_incoming_times_design,
            u'输煤系统计算F23数据':
            handingSystem.c_height_design,
            u'输煤系统计算F24数据':
            handingSystem.c_width_design,
            u'输煤系统计算F22数据':
            handingSystem.c_coalyard_area_design,
            u'输煤系统计算F20数据':
            handingSystem.c_coal_height_design,
            # u'输煤系统计算F40数据': handingSystem.t_vehicle_daily_incoming_times_design,
            u'输煤系统计算F15数据':
            handingSystem.c_coal_store_days_design,
            u'输煤系统计算F53数据':
            handingSystem.s_belt_width_check,
            u'输煤系统计算F50数据':
            handingSystem.s_transportsystem_output_check,
            u'输煤系统计算F55数据':
            handingSystem.s_belt_speed_check,
            u'输煤系统计算F52数据':
            handingSystem.s_belt_width_check,
            u'锅炉计算G33，单位KG转化为t':
            d_total_design,
            u'锅炉计算G37':
            furnace.d_ash_total_design,
            u'锅炉计算G38':
            furnace.d_dust_total_design,
            u'锅炉G33天':
            d_total_design_day,
            u'锅炉G37天':
            d_ash_total_design_day,
            u'锅炉G38天':
            d_dust_total_design_day,
            u'锅炉G33年':
            d_total_design_year,
            u'锅炉G37年':
            d_ash_total_design_year,
            u'锅炉G38年':
            d_dust_total_design_year,
            u'除灰除渣系统F32数据':
            removalAshSlag.s_slag_removal_system,
            u'除灰除渣系统F38数据':
            removalAshSlag.s_dia,
            # u'除灰除渣系统F32数据': removalAshSlag.s_slag_removal_system,
            u'除灰除渣系统F36数据':
            removalAshSlag.s_sludge_time,
            u'除灰除渣系统F17数据':
            removalAshSlag.r_removal_coefficient,
            u'除灰除渣系统F18数据':
            removalAshSlag.r_removal_the_ash_system,
            u'除灰除渣系统F22数据':
            removalAshSlag.r_effective_volume_ash_storage,
            u'除灰除渣系统F21数据':
            removalAshSlag.r_stored_ash,
            u'锅炉辅机系统F75数据':
            boilerAuxiliaries.m_steamwater_cycle_loss,
            u'锅炉辅机系统F76数据':
            boilerAuxiliaries.m_pollution_loss,
            u'锅炉辅机系统F84数据':
            boilerAuxiliaries.m_increase_loss,
            u'循环水系统计算F5数据':
            circulatingWater.v_circulating_ratio_summer,
            u'循环水系统计算E5数据':
            circulatingWater.v_circulating_ratio_winter,
            u'循环水系统计算EF4数据':
            circulatingWater.v_steam_exhaust_flow_select,
            u'循环水系统计算F6数据':
            circulatingWater.v_circulating_water_summer,
            u'循环水系统计算E6数据':
            circulatingWater.v_circulating_water_winter,
            u'循环水系统计算F7数据':
            circulatingWater.v_auxiliary_engine_cooling_summer,
            u'循环水系统计算F8数据':
            circulatingWater.v_total_circulating_water_summer,
            u'循环水系统计算E8数据':
            circulatingWater.v_total_circulating_water_winter,
            u'循环水系统计算E14数据':
            circulatingWater.v_evaporation_loss,
            u'循环水系统计算E16数据':
            circulatingWater.v_partial_blow_loss,
            u'循环水系统计算E19数据':
            circulatingWater.v_discharge_capacity,
            u'循环水系统计算E20数据':
            circulatingWater.v_amount_of_makeup_water_summer
        }
        return list_report_data

    @staticmethod
    def coverCoalReport(content, planId):
        datas = ToCoalCHP.getReportData(planId)
        content = content.decode('utf8')
        for key in datas:
            if datas[key]:
                content = content.replace(
                    key,
                    str(format_value("number", str(datas[key]))), len(content))
        return content

    @staticmethod
    def sortPressure(steamturbine):
        dict_group_check = [[
            float(steamturbine.i_high1_pressure)
            if steamturbine.i_high1_pressure else 0, 'i_high1_pressure',
            'i_high1_entropy', 'i_high1_temperature', 'i_high1_enthalpy',
            'i_high1_flow', 'i_steam_hh1_power', 'HH1', u'1#高压'
        ], [
            float(steamturbine.i_high2_pressure)
            if steamturbine.i_high2_pressure else 0, 'i_high2_pressure',
            'i_high2_entropy', 'i_high2_temperature', 'i_high2_enthalpy',
            'i_high2_flow', 'i_hh1_hh2_power', 'HH2', u'2#高压'
        ], [
            float(steamturbine.i_deoxidize_pressure)
            if steamturbine.i_deoxidize_pressure else 0,
            'i_deoxidize_pressure', 'i_deoxidize_entropy',
            'i_deoxidize_temperature', 'i_deoxidize_enthalpy',
            'i_deoxidize_flow', 'i_hh2_deoxidize_power', 'D', u'D除氧'
        ], [
            float(steamturbine.i_exhaust_point_pressure)
            if steamturbine.i_exhaust_point_pressure else 0,
            'i_exhaust_point_pressure', 'i_exhaust_point_temperature',
            'i_exhaust_point_entropy', 'i_exhaust_point_enthalpy',
            'i_exhaust_point_flow', 'i_deoxidize_exhaust_power', u'抽汽点', u'抽汽点'
        ], [
            float(steamturbine.i_low1_pressure)
            if steamturbine.i_low1_pressure else 0, 'i_low1_pressure',
            'i_low1_entropy', 'i_low1_temperature', 'i_low1_enthalpy',
            'i_low1_flow', 'i_exhaust_lh1_power', 'LH1', u'1#低加'
        ], [
            float(steamturbine.i_low2_pressure) if steamturbine.i_low2_pressure
            else 0, 'i_low2_pressure', 'i_low2_entropy', 'i_low2_temperature',
            'i_low2_enthalpy', 'i_low2_flow', 'i_lh1_lh2_power', 'LH2', u'2#低加'
        ], [
            float(steamturbine.i_low3_pressure) if steamturbine.i_low3_pressure
            else 0, 'i_low3_pressure', 'i_low3_entropy', 'i_low3_temperature',
            'i_low3_enthalpy', 'i_low3_flow', 'i_lh2_lh3_power', 'LH3', u'3#低加'
        ]]

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

    # 返回主要技术经济指标处理页面初期值
    @staticmethod
    def to_economicJson(economic):
        datas = {}
        for index in range(len(list_column_economic)):
            datas[list_column_economic[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(economic, list_column_economic[index])))

        return datas

    # 获得主要技术经济指标页面表单的信息
    @staticmethod
    def to_economic(form, plan_id):
        economic = CoalCHPEconomicIndicators.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_economic)):
            if form.get(list_column_economic[index]) != '':
                setattr(economic, list_column_economic[index],
                        form.get(list_column_economic[index]))
            else:
                setattr(economic, list_column_economic[index], None)
        # 表单项目计算
        economic = economic_foctory.Factory().execute(economic, form)

        return economic

    # 返回公用工程页面初期值
    @staticmethod
    def to_officialJson(official):
        datas = {}
        for index in range(len(list_column_official)):
            # 如果是字符串类型的字段则跳过此步奏
            if list_column_official[index] in [
                    'o_boiler_type', 'o_fire_way',
                    'o_steam_parameter', 'o_steam_parameter',
                    'o_steam_volumn', 'o_fuel_type', 'o_install_way'
            ]:
                datas[list_column_official[index]] = getattr(
                    official, list_column_official[index])
            else:
                print(getattr(official, list_column_official[index]))
                datas[list_column_official[index]] = format_value(
                    "number",
                    str(getattr(official, list_column_official[index])))
        # datas['o_fire_way'] = getattr(official, 'o_fire_way')
        # datas['o_install_way'] = getattr(official, 'o_install_way')
        return datas

    # 获得公用工程页面表单的信息
    @staticmethod
    def to_official(form, plan_id):
        official = CoalCHPOfficialProcess.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_official)):
            if form.get(list_column_official[index]) != '':
                setattr(official, list_column_official[index],
                        form.get(list_column_official[index]))
            else:
                setattr(official, list_column_official[index], None)

        setattr(official, 'o_fire_way', form.get('o_fire_way'))
        setattr(official, 'o_install_way', form.get('o_install_way'))
        return official

    # 返回供油泵所需要的数据
    @staticmethod
    def to_oilPumpJson(datas):
        datasNew = {}
        datasNew['c_low_calorific_value_estimation_design'] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(datas, 's_low_estimation_design')))

        datasNew['f_boiler_consumption_design'] = format_value(
                # TODO还未过滤特殊字符项
                "number", str(getattr(datas, 'f_boiler_consumption_design')))

        return datasNew

    # 返回采暖供热页面初期值
    @staticmethod
    def to_heatJson(heat):
        datas = {}
        for index in range(len(list_column_heat)):
            datas[list_column_heat[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(heat, list_column_heat[index])))

        return datas

    # 获得采暖供热页面表单的信息
    @staticmethod
    def to_heat(form, plan_id):
        heat = CoalCHPHeatSupply.query.filter_by(plan_id=plan_id).first()

        for index in range(len(list_column_heat)):
            if form.get(list_column_heat[index]) != '':
                setattr(heat, list_column_heat[index],
                        form.get(list_column_heat[index]))
            else:
                setattr(heat, list_column_heat[index], None)
        return heat

    # 汽机辅机
    @staticmethod
    def to_turbineAuxiliaryJson(turbineAuxiliary, plan_id):
        datas = {}
        for index in range(len(list_column_turbineAuxiliary)):
            if list_column_turbineAuxiliary[index] == 'm_condenser_pressure' or list_column_turbineAuxiliary[index] == 'w_condenser_higter':
                datas[list_column_turbineAuxiliary[index]] = format_value2(
                    # TODO还未过滤特殊字符项
                    "number",
                    str(
                        getattr(turbineAuxiliary, list_column_turbineAuxiliary[
                            index])))
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
        turbineAuxiliary = CoalchpTurbineAuxiliary.query.filter_by(
            plan_id=plan_id).first()
        turbineAuxiliary = CoalTurbineAuxiliaryBefore().specialCalculation(
            turbineAuxiliary, form)
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


    # 获得图片上点的信息
    @staticmethod
    def getImgInfo(imgName, planId, getimgInfoList):
        imgInfoDir = {
            'sourceimgPathName':
            GetPath.getCoalimgpath(imgName),
            'trgimgPathName':
            GetPath.getImgCoalResult(imgName, planId),
            'imgInfoList':
            getimgInfoList
        }
        return imgInfoDir

    # 生成图片的markdown路径
    @staticmethod
    def generate_img_md(imgName, planId, imgDescrib):
        obj = GetimgInfoList()
        getimgInfoList = getattr(obj, imgName+"_List")(planId)
        imgInfoDir = ToCoalCHP.getImgInfo(imgName, planId, getimgInfoList)
        imageProcesse(imgInfoDir)
        path = GetPath.getImgCoalResult(imgName, planId)
        if os.path.exists(path):
            imgInfo_p1_a = u'''##### ![](http://''' + config['ipandport'].APP_IP + u''':''' + config['ipandport'].APP_PORT + u'''/coalimgpreview/''' + str(planId) + '''/''' + imgName + '''_''' + str(planId) + u'''.png)
##### ''' + imgDescrib + u'''-图示\n'''
        else:
            raise MyException(imgName,
                              imgDescrib + u"生成资源图找不到,请检查数据或者网络是否有误。",
                              path + imgDescrib + u"生成资源图找不到,请查看生成代码，或者目录结构是否完整。",
                              path)
        return imgInfo_p1_a

    # 根据需求逻辑生成对应的图片
    @staticmethod
    def generate_img(planId, content, flag):
        templateContent = content + u'# 附件一 出图\n' 
        imgList = []
        if flag == 2:
            imgList = [{"imgName": "p_ash", "imgDescrib": u"原则性除灰系统图"} 
                       , {"imgName": "p_slag", "imgDescrib": u"原则性除渣系统图"}
                       ]
        elif flag == 0:
            imgList = ToCoalCHP.get_img_list(planId)
        # imgList = [{"imgName": "rl_p1_a", "imgDescrib": u"原则性上料系统图-1"} 
        #            , {"imgName": "rl_p1_b", "imgDescrib": u"原则性上料系统图-2"} 
        #            , {"imgName": "p1_cfb_dry", "imgDescrib": u"原则性燃烧系统图-1"} 
        #            , {"imgName": "p2_cfb_wet", "imgDescrib": u"原则性燃烧系统图-2"} 
        #            , {"imgName": "p1_a", "imgDescrib": u"原则性热力系统图-1"} 
        #            , {"imgName": "p1_b", "imgDescrib": u"原则性热力系统图-2"} 
        #            , {"imgName": "p2_a", "imgDescrib": u"原则性热力系统图-3"} 
        #            , {"imgName": "p2_b", "imgDescrib": u"原则性热力系统图-4"} 
        #            , {"imgName": "p3_a", "imgDescrib": u"原则性热力系统图-5"} 
        #            , {"imgName": "p3_b", "imgDescrib": u"原则性热力系统图-6"} 
        #            , {"imgName": "p4_a", "imgDescrib": u"原则性热力系统图-7"} 
        #            , {"imgName": "p4_b", "imgDescrib": u"原则性热力系统图-8"} 
        #            , {"imgName": "p5_a", "imgDescrib": u"原则性热力系统图-9"} 
        #            , {"imgName": "p5_b", "imgDescrib": u"原则性热力系统图-10"} 
        #            , {"imgName": "p1_chemical", "imgDescrib": u"原则性化学水处理系统图-1"} 
        #            , {"imgName": "p2_chemical", "imgDescrib": u"原则性化学水处理系统图-2"} 
        #            , {"imgName": "p_ash", "imgDescrib": u"原则性除灰系统图"} 
        #            , {"imgName": "p_slag", "imgDescrib": u"原则性除渣系统图"}
        #            ]
        else:
            imgList = ToCoalCHP.get_img_list(planId)
            imgList.append({"imgName": "p_ash", "imgDescrib": u"原则性除灰系统图"})
            imgList.append({"imgName": "p_slag", "imgDescrib": u"原则性除渣系统图"})
            
        for index in range(len(imgList)):
            imgMD = ToCoalCHP.generate_img_md(imgList[index]["imgName"],
                                              planId,
                                              imgList[index]["imgDescrib"])
            templateContent += imgMD
        return templateContent

    # 根据逻辑数据获取需要生成的图片列表
    @staticmethod
    def get_img_list(plan_id):
        imgList = []
        turbineBackpressure = CoalCHPTurbineBackpressure.search_turbineBackpressure(plan_id)
        furnaceCalculation = CoalCHPFurnaceCalculation.search_furnace_calculation(plan_id)
        circulatingWater = CoalCHPCirculatingWater.search_circulating_water(plan_id)
        chemicalWater = CoalCHPChemicalWater.search_chemical_water(plan_id)

        removeOxyen = None
        highGrade = None
        lowGrade = None
        waterTemperature = None
        circleWaterSelect = None
        sulfurVolunm = None
        chemicalMethod = None
        coal_capacity = None

        if turbineBackpressure.s_temperature_pressure:
            # 除氧
            removeOxyen = float(format_value("number", str(turbineBackpressure.s_temperature_pressure)))
        if turbineBackpressure.s_hh_grade is not None:
            # 高加级数
            highGrade = turbineBackpressure.s_hh_grade
        if turbineBackpressure.s_lh_grade:
            # 低加级数
            lowGrade = float(format_value("number", str(turbineBackpressure.s_lh_grade)))
        if furnaceCalculation.f_water_temperature_design:
            # 给水温度
            waterTemperature = float(format_value("number", str(furnaceCalculation.f_water_temperature_design)))
        if circulatingWater.circleWaterSelect:
            # 循环水系统配置
            circleWaterSelect = float(format_value("number", str(circulatingWater.circleWaterSelect)))
            
        if furnaceCalculation.s_sulfur_design:
            # 脱硫脱硝工艺--含硫量
            sulfurVolunm = float(furnaceCalculation.s_sulfur_design)

        if chemicalWater.m_process_route:
            # 化学水工艺
            chemicalMethod = float(chemicalWater.m_process_route)

        if furnaceCalculation.f_boiler_consumption_design:
            coal_capacity = furnaceCalculation.f_boiler_consumption_design/1000

        # 总耗煤量<60t/h,采用单路，>=60t/h,采用双路
        if coal_capacity and coal_capacity < 60:
            imgList.append({"imgName": "rl_p1_b", "imgDescrib": u"原则性上料系统图"})
        if coal_capacity and coal_capacity >= 60:
            imgList.append({"imgName": "rl_p1_a", "imgDescrib": u"原则性上料系统图"})
        # p1-a 1、给水温度：215℃；2、回热系统配置：3低加+1除氧+2高加；3、循环水系统配置：自然通风双曲线冷却塔
        if waterTemperature == 215 and removeOxyen and lowGrade == 3 and highGrade == 2 and circleWaterSelect == 1:
            imgList.append({"imgName": "p1_a", "imgDescrib": u"原则性热力系统图"})
        # p1-b 1、给水温度：215℃；2、回热系统配置：3低加+1除氧+2高加；3、循环水系统配置：逆流式机械通风冷却塔
        if waterTemperature == 215 and removeOxyen and lowGrade == 3 and highGrade == 2 and circleWaterSelect == 2:
            imgList.append({"imgName": "p1_b", "imgDescrib": u"原则性热力系统图"})
        # p2-a 1、给水温度：158℃；2、回热系统配置：2低加+1除氧；3、循环水系统配置：自然通风双曲线冷却塔
        if waterTemperature == 158 and removeOxyen and lowGrade == 2 and highGrade == 0 and circleWaterSelect == 1:
            imgList.append({"imgName": "p2_a", "imgDescrib": u"原则性热力系统图"})
        # p2-b 1、给水温度：158℃；2、回热系统配置：2低加+1除氧；3、循环水系统配置：逆流式机械通风冷却塔
        if waterTemperature == 158 and removeOxyen and lowGrade == 2 and highGrade == 0 and circleWaterSelect == 2:
            imgList.append({"imgName": "p2_b", "imgDescrib": u"原则性热力系统图"})
        # 1、给水温度：150℃；2、回热系统配置：1低加+1除氧+1高加；3、循环水系统配置：自然通风双曲线冷却塔
        if waterTemperature == 150 and removeOxyen and lowGrade == 1 and highGrade == 1 and circleWaterSelect == 1:
            imgList.append({"imgName": "p3_a", "imgDescrib": u"原则性热力系统图"})
        # 1、给水温度：150℃；2、回热系统配置：1低加+1除氧+1高加；3、循环水系统配置：逆流式机械通风冷却塔
        if waterTemperature == 150 and removeOxyen and lowGrade == 1 and highGrade == 1 and circleWaterSelect == 2:
            imgList.append({"imgName": "p3_b", "imgDescrib": u"原则性热力系统图"})
        # 1、给水温度：215℃；2、回热系统配置：2低加+1除氧+2高加；3、循环水系统配置：自然通风双曲线冷却塔
        if waterTemperature == 215 and removeOxyen and lowGrade == 2 and highGrade == 2 and circleWaterSelect == 1:
            imgList.append({"imgName": "p4_a", "imgDescrib": u"原则性热力系统图"})
        # 1、给水温度：215℃；2、回热系统配置：2低加+1除氧+2高加；3、循环水系统配置：逆流式机械通风冷却塔
        if waterTemperature == 215 and removeOxyen and lowGrade == 2 and highGrade == 0 and circleWaterSelect == 2:
            imgList.append({"imgName": "p4_b", "imgDescrib": u"原则性热力系统图"})
        # 1、给水温度：104℃；2、回热系统配置：1低加+1除氧；3、循环水系统配置：自然通风双曲线冷却塔
        if waterTemperature == 215 and removeOxyen and lowGrade == 1 and highGrade == 0 and circleWaterSelect == 1:
            imgList.append({"imgName": "p5_a", "imgDescrib": u"原则性热力系统图"})
        # 1、给水温度：104℃；2、回热系统配置：1低加+1除氧；3、循环水系统配置：逆流式机械通风冷却塔
        if waterTemperature == 215 and removeOxyen and lowGrade == 1 and highGrade == 2 and circleWaterSelect == 2:
            imgList.append({"imgName": "p5_b", "imgDescrib": u"原则性热力系统图"})
        # 循环流化床锅炉（采用干法、半干法脱硫工艺）-- 含硫量＜2%,环保条件容许的情况下啊，优先采用半干法，干法脱硫
        if sulfurVolunm and float(sulfurVolunm) < 2:
            imgList.append({"imgName": "p1_cfb_dry", "imgDescrib": u"原则性燃烧系统图"})
        # 循环流化床锅炉（采用湿法脱硫工艺）-- 含硫量≥2%宜优先采用石灰石石膏湿法脱硫
        if sulfurVolunm and float(sulfurVolunm) >= 2:
            imgList.append({"imgName": "p2_cfb_wet", "imgDescrib": u"原则性燃烧系统图"})
        # 预处理 + 两级反渗透（两级RO）+ 填充床电渗析（EDI）处理
        if chemicalMethod and chemicalMethod == 1:
            imgList.append({"imgName": "p1_chemical", "imgDescrib": u"原则性化学水处理系统图"})
        # 预处理 + 两级反渗透（两级RO）+ 混床处理
        if chemicalMethod and chemicalMethod == 2:
            imgList.append({"imgName": "p2_chemical", "imgDescrib": u"原则性化学水处理系统图"})

        # imgList.append({"imgName": "p_ash", "imgDescrib": u"原则性除灰系统图"})
        # imgList.append({"imgName": "p_slag", "imgDescrib": u"原则性除渣系统图"})
        return imgList

    # 获得存放ImgDict对象的img列表
    @staticmethod
    def getPathList(planId, targetpath):
        # 获得图像存储目录
        path = GetPath.getImgCoalResultDir(planId)
        imglist = []
        imgLists = []
        if targetpath == "html":
            imgLists = [{"imgName": "p_ash", "imgDescrib": u"原则性除灰系统图"} 
                        , {"imgName": "p_slag", "imgDescrib": u"原则性除渣系统图"}
                        ]
        else:
            imgLists = ToCoalCHP.get_img_list(planId)
# 遍历目录下的所有文件
        for i in os.listdir(path):
            if targetpath == "html" and len(imglist) == 2:
                break
            path_file = os.path.join(path, i)  # 取文件绝对路径
            if os.path.isfile(path_file):
                dirname, filename = os.path.split(path_file)
                for index in range(len(imgLists)):
                    chineseName = None
                    if filename is not None and filename.find(imgLists[index]["imgName"]) != -1:
                        chineseName = imgLists[index]["imgDescrib"]
                        filenameprefix = imgLists[index]["imgName"]
                # chineseName, filenameprefix = self.getChineseName(filename)
                    if chineseName is not None:
                        imgDir = {}
                        netPath = GetPath.getImgCoalNetPath(filenameprefix, planId)
                        dirname, netfilename = os.path.split(netPath)
                        imgDir['chineseName'] = chineseName
                        imgDir['netPath'] = netPath
                        imgDir['filename'] = filename
                        imglist.append(imgDir)
        return imglist

    @staticmethod
    # 根据plan_id删除照片
    def deleteFile(plan_id):
        imgPath = GetPath.getImgCoalResultDir(plan_id)
        if imgPath is not None and os.path.exists(imgPath):
            gl.del_file(imgPath)

    @staticmethod
    def getmdtitledict():
        mdtitledict = {"a": u"一、锅炉专业主要设备清册",
                       "b": u"二、汽轮机专业主要设备清册",
                       "c": u"三、输煤专业主要设备清册",
                       "d": u"四、除灰专业主要设备清册",
                       "e": u"五、除渣专业主要设备清册",
                       "f": u"六、供排水系统主要设备清册",
                       "f11": u"6.1、循环水系统",
                       "f12": u"6.1、循环水系统",
                       "f2": u"6.2、补给水系统",
                       "f3": u"6.3、排水系统",
                       "f4": u"6.4、消防系统",
                       "f5": u"6.5、其它设备",
                       "g": u"七、化水专业主要设备清册",
                       "g1": u"7.1、原水预处理系统",
                       "g2": u"7.2、除盐水系统",
                       "g3": u"7.3、化学加药系统",
                       "g4": u"7.4、水汽取样系统",
                       "g5": u"7.5、循环水加药系统",
                       "g6": u"7.6、循环水补水软化装置",
                       "g7": u"7.7、实验室仪器仪表",
                       "h": u"八、电气专业主要设备清册",
                       "h1": u"8.1、电气一次部分",
                       "h2": u"8.2、电气110kV户内GIS装备",
                       "h3": u"8.3、电气二次部分",
                       "i": u"九、热工控制主要设备及清册",
                       "i1": u"9.1、机炉控制系统",
                       "i2": u"9.2、辅助车间控制系统及仪表"
                       }
        return mdtitledict

    ''' 
    查询各个表取值替换设备表的json
    分表模块调用
    '''
    @staticmethod
    def replaceDeviceJson(planId):
        furnace = CoalCHPFurnaceCalculation.query.filter_by(
            plan_id=planId).first()
        handingSystem = CoalCHPCoalHandingSystem.query.filter_by(
            plan_id=planId).first()
        smokeAirSystem = CoalCHPSmokeAirSystem.query.filter_by(
            plan_id=planId).first()
        boilerAuxiliaries = CoalCHPBoilerAuxiliaries.query.filter_by(
            plan_id=planId).first()
        turbineBackpressure = CoalCHPTurbineBackpressure.query.filter_by(
            plan_id=planId).first()
        turbineAuxiliary = CoalchpTurbineAuxiliary.query.filter_by(
            plan_id=planId).first()
        removalAshSlag = CoalCHPRemovalAshSlag.query.filter_by(
            plan_id=planId).first()
        circulatingWater = CoalCHPCirculatingWater.query.filter_by(
            plan_id=planId).first()
        chemicalWater = CoalCHPChemicalWater.query.filter_by(
            plan_id=planId).first()
        circulatingRoute = circulatingWater.circleWaterSelect
        replaceList = {}
        replaceList = ToCoalCHP.replaceFurnace(furnace, replaceList)
        replaceList = ToCoalCHP.replaceSmokeAir(smokeAirSystem, replaceList)
        replaceList = ToCoalCHP.replaceHandingSystem(handingSystem, replaceList)
        replaceList = ToCoalCHP.replaceTurbineBackpressure(turbineBackpressure, replaceList)
        replaceList = ToCoalCHP.replaceTurbineAuxiliary(turbineAuxiliary, replaceList)
        replaceList = ToCoalCHP.replaceBoilerAuxiliaries(boilerAuxiliaries, replaceList)
        replaceList = ToCoalCHP.replaceRemovalAshSlag(removalAshSlag, replaceList)
        replaceList = ToCoalCHP.replaceCirculatingWater(circulatingWater, replaceList)
        replaceList = ToCoalCHP.replaceChemicalWater(chemicalWater, replaceList)
         # 替换数量
        countList = {}
        countList = ToCoalCHP.replaceHandingCount(handingSystem, countList)
        countList = ToCoalCHP.replaceSmokeAirCount(smokeAirSystem, countList)
        equipmentList = EquipmentList.search_equipmentList(planId)
        data = json.loads(equipmentList.equipment_content)
        equipmentCount = len(data['equipment_name'])
        deleteIndex = None
        for j in range(0, equipmentCount):
            for key in replaceList:
                if key == data['equipment_uid'][j]:
                    data['equipment_content'][j] = replaceList[key]
            for k in countList:
                if k == data['equipment_uid'][j]:
                    data['equipment_count'][j] = str(countList[k])
            # 逆流式机械通风冷却塔 == 2
            if circulatingRoute and circulatingRoute == 2:
                if "101" == data['equipment_uid'][j]:
                    deleteIndex = j
                # 判断是否被删完，如果存在则不创建，否则会影响列表正常保存
            # 双曲线自然通风冷却塔 == 1
            elif circulatingRoute and circulatingRoute == 1:
               if "103" == data['equipment_uid'][j]:
                    deleteIndex = j
        if ToCoalCHP.isExit(data):
            ToCoalCHP.addDevice(circulatingRoute, circulatingWater, data)
        # 得到当前已知选中，需要删掉的工艺
        if deleteIndex:
            del data['equipment_uid'][deleteIndex]
            del data['equipment_name'][deleteIndex]
            del data['equipment_content'][deleteIndex]
            del data['equipment_count'][deleteIndex]
            del data['equipment_type'][deleteIndex]
            del data['equipment_unit'][deleteIndex]
            del data['equipment_remark'][deleteIndex]
        equipmentList.equipment_content = json.dumps(data)
        EquipmentList.insert_equipmentList(equipmentList)
    

    ''' 判断循环水工艺方式是否被切换过，即不存在 '''
    @staticmethod
    def isExit(data):
        equipmentCount = len(data['equipment_name'])
        result = True
        for j in range(0, equipmentCount):
            if "101" == data['equipment_uid'][j]:
                result = False
            if "103" == data['equipment_uid'][j]:
                result = False
        return result

    ''' 添加循环水设备 '''
    @staticmethod
    def addDevice(circulatingRoute, circulatingWater, data):
        if circulatingRoute == 1:
            data['equipment_uid'].append(u"101")
            data['equipment_name'].append(u"双曲线自然通风冷却塔")
            data['equipment_content'].append(getstrcolm(circulatingWater.p_select_f)+u"m2,△t=8～12℃")
            data['equipment_count'].append(u"3")
            data['equipment_type'].append(u"f11")
            data['equipment_unit'].append(u"台")
            data['equipment_remark'].append(u"")
        else:
            data['equipment_uid'].append(u"103")
            data['equipment_name'].append(u"逆流式机械通风冷却塔")
            data['equipment_content'].append(u"处理水量"+getstrcolm(circulatingWater.p_select_s)+u"m3/h，N=XXkW，U=380V")
            data['equipment_count'].append(u"3")
            data['equipment_type'].append(u"f12")
            data['equipment_unit'].append(u"台")
            data['equipment_remark'].append(u"")


    ''' 替换锅炉表 '''
    @staticmethod
    def replaceFurnace(furnace, replaceList):
        # （锅炉计算!G19）t/h （锅炉计算!G20）MPa （锅炉计算! G21 ）℃
        replaceList["2"] = getstrcolm(furnace.f_steam_flow_design)+u"t/h " + getstrcolm(furnace.f_steam_pressure_design) +u"MPa "+getstrcolm(furnace.f_steam_temperature_design) +u"℃"
        # 处理烟气量：（锅炉计算!G135）m3/h 出口浓度<30mg/m3
        replaceList["13"] = u"处理烟气量：" + getstrcolm(furnace.d_entry_smoke_actual_flow_design) +u"m3/h 出口浓度<30mg/m3"
        return replaceList
    

    ''' 替换烟风计算表 '''
    @staticmethod
    def replaceSmokeAir(smokeAirSystem, replaceList):
        # "Q=（烟风计算!F29）m3/h 全压：（烟风计算!F28）Pa"
        replaceList["5"] = u"Q="+getstrcolm(smokeAirSystem.f_fan_selection_flow)+u"m3/h 全压："+getstrcolm(smokeAirSystem.f_fan_select_total_pressure)+u"Pa"
        # "（烟风计算!G34）KW"
        replaceList["6"] = getstrcolm(smokeAirSystem.f_motor_power)+u"KW"
        # Q=（烟风计算!F45）m3/h 全压：（烟风计算!F44）Pa
        replaceList["7"] = u"Q="+getstrcolm(smokeAirSystem.s_fan_selection_flow)+u"m3/h 全压："+getstrcolm(smokeAirSystem.s_fan_select_total_pressure)+u"Pa"
        # （烟风计算!G50）KW
        replaceList["8"] = getstrcolm(smokeAirSystem.s_motor_power)+u"KW"
        # Q=（烟风计算!F80）m3/h 全压：（烟风计算!F79）Pa
        replaceList["9"] = u"Q="+getstrcolm(smokeAirSystem.r_fan_selection_flow)+u"m3/h 全压："+getstrcolm(smokeAirSystem.r_fan_select_total_pressure)+u"Pa"
        # （烟风计算!G85）KW
        replaceList["10"] = getstrcolm(smokeAirSystem.r_motor_power)+u"KW"
        # Q=（烟风计算!F64）m3/h 全压：（烟风计算!F63）Pa
        replaceList["11"] = u"Q="+getstrcolm(smokeAirSystem.i_fan_selection_flow)+u"m3/h 全压："+getstrcolm(smokeAirSystem.i_fan_select_total_pressure)+u"Pa"
        # （烟风计算!G69）KW
        replaceList["12"] = getstrcolm(smokeAirSystem.i_motor_power) +u"KW"
        return replaceList

    ''' 替换输煤系统表 '''
    @staticmethod
    def replaceHandingSystem(handingSystem, replaceList):
        # 出力（输煤系统！F65）t/h
        replaceList["3"] = u"出力"+getstrcolm(handingSystem.g_equipment_sets_design)+u"t/h"
        # （输煤系统！F29）m3
        replaceList["4"] = getstrcolm(handingSystem.e_effective_cubage_selected_design)+u"m3"
        # 带宽（输煤系统！F53）mm，带速（输煤系统！F55）m/s，输送量（输煤系统！F50）t/h
        replaceList["47"] = u"带宽"+getstrcolm(handingSystem.s_belt_width_design)+u"mm，带速"+getstrcolm(handingSystem.s_belt_speed_design)+u"m/s，输送量"+getstrcolm(handingSystem.s_transportsystem_output_design)+u"t/h"
        # 生产能力（输煤系统！F50）t/h
        replaceList["48"] = u"生产能力"+getstrcolm(handingSystem.s_transportsystem_output_design)+u"t/h"
        # 可逆式型，破碎能力（输煤系统！F50）t/h，进料粒度≤300mm，出料粒度≤10mm，防护等级IP54 绝缘等级 F
        replaceList["49"] = u"可逆式型，破碎能力"+getstrcolm(handingSystem.s_transportsystem_output_design)+u"t/h，进料粒度≤300mm，出料粒度≤10mm，防护等级IP54 绝缘等级 F"
        # 给煤能力（输煤系统！F50）t/h,给煤粒度0-300mm，双振幅4mm，安装角度0-10°
        replaceList["50"] = u"给煤能力"+getstrcolm(handingSystem.s_transportsystem_output_design)+u"t/h,给煤粒度0-300mm，双振幅4mm，安装角度0-10°"
        # B=（输煤系统！F53）mm
        replaceList["53"] = u"B="+getstrcolm(handingSystem.s_belt_width_design)+u"mm"
        # B=（输煤系统！F53）mm
        replaceList["54"] = u"B="+getstrcolm(handingSystem.s_belt_width_design)+u"mm"
        # 带宽B=（输煤系统！F53）mm，带速（输煤系统！F55）m/s
        replaceList["55"] = u"带宽B="+getstrcolm(handingSystem.s_belt_width_design)+u"mm，带速"+getstrcolm(handingSystem.s_belt_speed_design)+u"m/s"
        # 带宽B=（输煤系统！F53）mm，带速（输煤系统！F55）m/s
        replaceList["56"] = u"带宽B="+getstrcolm(handingSystem.s_belt_width_design)+u"mm，带速"+getstrcolm(handingSystem.s_belt_speed_design)+u"m/s"
        return replaceList

    ''' 替换输煤数量 '''
    @staticmethod
    def replaceHandingCount(handingSystem, countList):
        countList["3"] = toMyInt(getstrcolm(handingSystem.g_equipment_sets_design))
        countList["4"] = toMyInt(getstrcolm(handingSystem.e_coal_bunker_counts_design))
        return countList

    ''' 替换输煤数量 '''
    @staticmethod
    def replaceSmokeAirCount(smokeAirSystem, countList):
        countList["5"] = toMyInt(getstrcolm(smokeAirSystem.f_count))
        countList["6"] = toMyInt(getstrcolm(smokeAirSystem.f_count))
        countList["7"] = toMyInt(getstrcolm(smokeAirSystem.s_count))
        countList["8"] = toMyInt(getstrcolm(smokeAirSystem.s_count))
        countList["11"] = toMyInt(getstrcolm(smokeAirSystem.s_count))
        countList["12"] = toMyInt(getstrcolm(smokeAirSystem.s_count))
        return countList

    ''' 替换汽轮机表 '''
    @staticmethod
    def replaceTurbineBackpressure(turbineBackpressure, replaceList):
        # P=（汽轮机计算！F5）MPa，T=（汽轮机计算！F6）℃　Q=（汽轮机计算！F7）t/h
        replaceList["22"] = u"P="+getstrcolm(turbineBackpressure.e_steam_pressure)+u"MPa，T="+getstrcolm(turbineBackpressure.e_steam_temperature)+u"℃　Q="+getstrcolm(turbineBackpressure.e_steam_flow)+u"t/h"
        return replaceList

    ''' 替换汽机辅机表 '''
    @staticmethod
    def replaceTurbineAuxiliary(turbineAuxiliary, replaceList):
        # 排汽参数：Q=（汽机辅机计算！G18）t/h，P=（汽机辅机计算！G19）MPa，T=（汽机辅机计算！G21）℃
        replaceList["23"] = u"排汽参数：Q="+getstrcolm(turbineAuxiliary.m_condenser_pressure)+u"t/h，P="+getstrcolm(turbineAuxiliary.m_steam_enthalpy)+u"MPa，T="+getstrcolm(turbineAuxiliary.m_saturation_temperature)+u"℃"
        # Q=（汽机辅机系统！G8）m3/h，H=（汽机辅机系统！G7）
        replaceList["33"] = u"Q="+getstrcolm(turbineAuxiliary.w_flow_amount)+u"m3/h，H="+getstrcolm(turbineAuxiliary.w_condensate_pump_lift)
        # P=（汽机辅机系统！G13）KW
        replaceList["34"] = u"P="+getstrcolm(turbineAuxiliary.w_auxiliary_motor_power)+u"KW"
        # 工作压力：（汽机辅机计算！G44）MPa；扬程：（汽机辅机计算！G48）m；
        replaceList["35"] = u"工作压力："+getstrcolm(turbineAuxiliary.f_air_ejector_pressure)+u"MPa；扬程："+getstrcolm(turbineAuxiliary.f_total_lift)+u"m"
        # （汽机辅机计算！G54）KW
        replaceList["36"] = getstrcolm(turbineAuxiliary.f_auxiliary_motor_power)+u"KW"
        return replaceList


    ''' 替换汽机辅机表 '''
    @staticmethod
    def replaceBoilerAuxiliaries(boilerAuxiliaries, replaceList):
        # Q=（锅炉辅机系统！F65）m3/h，H=（锅炉辅机系统！F65）m；
        replaceList["17"] = u"Q="+getstrcolm(boilerAuxiliaries.p_flow)+u"m3/h，H="+getstrcolm(boilerAuxiliaries.p_flow)+u"m；"
        # P=（锅炉辅机系统！F70）KW
        replaceList["18"] = u"P="+getstrcolm(boilerAuxiliaries.p_auxiliary_motor_power)+u"KW"
        # （锅炉辅机系统计算！E42）m3
        replaceList["19"] = getstrcolm(boilerAuxiliaries.c_volume)+u"m3"
        # （锅炉辅机系统计算！E25）m3
        replaceList["20"] = getstrcolm(boilerAuxiliaries.r_volume)+u"m3"
        # V=（锅炉辅机计算！F91）m³
        replaceList["38"] = getstrcolm(boilerAuxiliaries.s_volume)+u"m3"
        # 减压减温后蒸汽量：(锅炉辅机！F119)t/h 进出汽压力：(锅炉辅机！F107)/(锅炉辅机！F115)MPa(g) 进出汽温度：(锅炉辅机！F106)/ (锅炉辅机！F114)℃ 减温水温度：(锅炉辅机！F110)℃，流量(锅炉辅机！F113) m3/h
        replaceList["42"] = u"减压减温后蒸汽量："+getstrcolm(boilerAuxiliaries.t_rudece_flow_rate)+u"t/h 进出汽压力："+getstrcolm(boilerAuxiliaries.t_new_pressure)+u"/"+getstrcolm(boilerAuxiliaries.t_reduce_steam_pressure)+u"MPa(g) 进出汽温度："+getstrcolm(boilerAuxiliaries.t_new_steam_temperature)+u" / "+getstrcolm(boilerAuxiliaries.t_reduce_steam_temperature)+u"℃ 减温水温度："+getstrcolm(boilerAuxiliaries.t_reduce_water_temperature)+u"℃，流量"+getstrcolm(boilerAuxiliaries.t_reduce_water_flow_rate)+u"m3/h"
        return replaceList


    ''' 替换除灰除渣系统表 '''
    @staticmethod
    def replaceRemovalAshSlag(removalAshSlag, replaceList):
        # Q=（除灰除渣系统计算！F27）m³/min
        replaceList["73"] = u"Q="+getstrcolm(removalAshSlag.g_air_transport_ash_system)+u"m³/min"
        # Q=（除灰除渣系统计算！F27）m³/min
        replaceList["74"] = u"Q="+getstrcolm(removalAshSlag.g_air_transport_ash_system)+u"m³/min"
        # Q=（除灰除渣系统！F33）t/h
        replaceList["91"] = u"Q="+getstrcolm(removalAshSlag.s_high_temperature_belt_conveyor)+u"t/h"
        return replaceList
    
    
    ''' 替换循环水系统表 '''
    @staticmethod
    def replaceCirculatingWater(circulatingWater, replaceList):
        # 冷却面积：(循环水系统！K22)m2，△t=8～12℃
        replaceList["101"] = getstrcolm(circulatingWater.p_select_f)+u"m2,△t=8～12℃"
        # 逆流式，处理水量(循环水系统！FK26)m3/h，N=XXkW，U=380V
        replaceList["103"] = u"处理水量"+getstrcolm(circulatingWater.p_select_s)+u"m3/h，N=XXkW，U=380V"
        # Q=(循环水系统！E36)m3/h，H=(循环水系统！E35)m，
        replaceList["104"] = u"Q="+getstrcolm(circulatingWater.c_flow)+u"m3/h，H="+getstrcolm(circulatingWater.c_pumping_head)+"m"
        # P=(循环水系统！E42)kW，R=990r/min，10kV/380V
        replaceList["105"] = u"P="+getstrcolm(circulatingWater.c_forklift_parameters_power)+u"kW，R=990r/min，10kV/380V"
        return replaceList

    
    ''' 替换 化学水系统表 '''
    @staticmethod
    def replaceChemicalWater(chemicalWater, replaceList):
        if chemicalWater.m_output:
            m_output = chemicalWater.m_output
            # 产水量(锅炉补给水处理能力！F86) /95%/85%/2m3/h
            replaceList["142"] = u"Q="+str(format_value("number", str(m_output))/0.95/0.85/2)+u"m3/h"
            # Q=(锅炉补给水处理能力！F86) /95%/85%/75%/2m3/h，H=130-140 m；U=380V
            replaceList["143"] = u"Q="+str(format_value("number", str(m_output))/0.95/0.85/0.75/2)+u"m3/h，H=130-140 m；U=380V"
            # V=(锅炉补给水处理能力！F86) /95%/85%*1h(停留时间)m3
            replaceList["144"] = u"Q="+str(format_value("number", str(m_output))/0.95/0.85)+u"h(停留时间)m3"
            # Q=(锅炉补给水处理能力！F86) /95%/85%/2m3/h，U=380V
            replaceList["145"] = u"Q="+str(format_value("number", str(m_output))/0.95/0.85/2)+u"m3/h，U=380V"
            # 产水量(锅炉补给水处理能力！F86) /95%/2m3/h
            replaceList["146"] = u"Q="+str(format_value("number", str(m_output))/0.95/2)+u"m3/h"
            # Q=(锅炉补给水处理能力！F86) /95%/85%/75%/2m3/h，H=130-140m；U=380V
            replaceList["147"] = u"Q="+str(format_value("number", str(m_output))/0.95/0.85/0.75/2)+u"m3/h，H=130-140m；U=380V"
            # V=(锅炉补给水处理能力！F86) /95%*1h(停留时间)m3
            replaceList["148"] = u"Q="+str(format_value("number", str(m_output))/0.95)+u"h(停留时间)m3"
            # Q=(锅炉补给水处理能力！F86)/ 95%/2m3/h，U=380V
            replaceList["149"] = u"Q="+str(format_value("number", str(m_output))/0.95/2)+u"m3/h，U=380V"
            # 产水量(锅炉补给水处理能力！F86)/ 2m3/h
            replaceList["150"] = u"Q="+str(format_value("number", str(m_output))/2)+u"m3/h"
            # V=(关联除氧水箱容积)/2m3
            replaceList["151"] = u"Q="+str(format_value("number", str(m_output))*5/2)+ u"m3"
        else:
            # 产水量(锅炉补给水处理能力！F86) /95%/85%/2m3c
            replaceList["142"] = u"Q= /h"
            # Q=(锅炉补给水处理能力！F86) /95%/85%/75%/2m3/h，H=130-140 m；U=380V
            replaceList["143"] = u"Q= m3/h，H=130-140 m；U=380V"
            # V=(锅炉补给水处理能力！F86) /95%/85%*1h(停留时间)m3
            replaceList["144"] = u"Q= h(停留时间)m3"
            # Q=(锅炉补给水处理能力！F86) /95%/85%/2m3/h，U=380V
            replaceList["145"] = u"Q= m3/h，U=380V"
            # 产水量(锅炉补给水处理能力！F86) /95%/2m3/h
            replaceList["146"] = u"Q= m3/h"
            # Q=(锅炉补给水处理能力！F86) /95%/85%/75%/2m3/h，H=130-140m；U=380V
            replaceList["147"] = u"Q= m3/h，H=130-140m；U=380V"
            # V=(锅炉补给水处理能力！F86) /95%*1h(停留时间)m3
            replaceList["148"] = u"Q= h(停留时间)m3"
            # Q=(锅炉补给水处理能力！F86)/ 95%/2m3/h，U=380V
            replaceList["149"] = u"Q= m3/h，U=380V"
            # 产水量(锅炉补给水处理能力！F86)/ 2m3/h
            replaceList["150"] = u"Q= m3/h"
            # V=(关联除氧水箱容积)/2m3
            replaceList["151"] = u"Q= m3"
        return replaceList