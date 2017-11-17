# -*- coding: utf-8 -*-
from ..model.coalchpModels import CoalCHPNeedsQuestionnaire, CoalCHPComponent,\
     CoalCHPFurnaceCalculation, CoalCHPCoalHandingSystem,\
     CoalCHPRemovalAshSlag, CoalCHPDesulfurization, CoalCHPCirculatingWater,\
     CoalCHPSmokeAirSystem, CoalCHPBoilerAuxiliaries
from flask_login import current_user
from ...models import Company, Plan, Module
from execution_strategy import Furnace_calculationBefore,\
     boilerAuxiliariesBefore

list_column_questionnaire = [
    's_fuel_design', 's_fuel_check', 's_carbon_design', 's_carbon_check',
    's_hydrogen_design', 's_hydrogen_check', 's_oxygen_design',
    's_oxygen_check', 's_nitrogen_design', 's_nitrogen_check',
    's_sulfur_design', 's_sulfur_check', 's_water_design', 's_water_check',
    's_grey_design', 's_grey_check', 's_daf_design', 's_daf_check',
    's_grindability_design', 's_grindability_check', 's_low_design',
    's_low_check', 'w_altitude_value', 'w_mean_annual_temperature_value',
    'w_mean_summer_temperature_value', 'w_mean_winter_temperature_value',
    'w_mean_annual_barometric_value', 'w_mean_summer_barometric_value',
    'w_mean_winter_barometric_value',
    'w_annual_average_relative_humidity_value',
    'ihl_steam_pressure_level_value', 'ihl_steam_temperature_level_value',
    'ihl_steam_time_value', 'ihl_recent_steam_flow_range_value',
    'ihl_forward_steam_flow_range_value', 'ihl_condensate_water_iron_value',
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
    'go_total_combustion_product_vol_check'
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
    'v_auxiliary_engine_cooling_summer',
    'v_total_circulating_water_winter', 'v_total_circulating_water_summer',
    'v_total_circulating_water_select',
    'v_enter_the_outlet_temperature_difference', 'v_dry_bulb_temperature',
    'v_k', 'v_evaporation_loss_rate', 'v_evaporation_loss',
    'v_blowing_loss_rate', 'v_partial_blow_loss', 'v_concentrate_ratio',
    'v_discharge_loss', 'v_discharge_capacity',
    'v_amount_of_makeup_water_winter', 'v_amount_of_makeup_water_summer',
    'v_circulating_pool_size', 'v_circulating_pool_long',
    'v_circulating_pool_wide', 'v_circulating_pool_hight',
    'v_check_circulating_pool_size', 'c_pressure_condenser',
    'c_condenser_tube_friction', 'c_circulating_water_pressure',
    'c_circulating_pool_pressure', 'c_circulation_height_difference',
    'c_height_difference_inlet', 'c_pipe_losses', 'c_y_losses',
    'c_pumping_head', 'c_flow', 'c_pump_power', 'c_mechine_power',
    'c_motor_power', 'c_motor_backup_coefficient', 'c_supporting_motor_power',
    'c_forklift_parameters_power', 'c_forklift_parameters_flow',
    'c_forklift_parameters_lift'
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
    'r_motor_power'
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
    'm_boiler_evaporation', 'm_makeup_steam', 'm_steamwater_cycle_loss',
    'm_pollution_loss', 'm_condensing_capacity', 'm_condensate_loss',
    'm_boiler_normal_watersupply', 'm_increase_loss',
    'm_boiler_max_watersupply', 's_boiler_evaporation', 's_storage_time',
    's_volume', 's_size_length', 's_size_diameter'
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
        result = float(str(float(values)).rstrip('0'))
    else:
        result = values
    return result


class ToCoalCHP():
    @staticmethod
    def create_plan(companyName, companyLocation):
        # 新增公司信息
        company = Company.query.filter_by(company_name=companyName).first()
        if not company:
            company = Company()
            company.company_name = companyName
            Company.insert_company(company)
        newCompany = Company.query.filter_by(company_name=companyName).first()
        companyId = newCompany.id
        # 创建方案
        plan = Plan.query.filter_by(company_id=companyId).first()
        if not plan:
            plan = Plan()
            plan.user_id = current_user.id
            plan.company_id = companyId
            plan.module_id = Module.coalCHP
            Plan.insert_plan(plan)
        plan.company_location = companyLocation
        newPlan = Plan.query.filter_by(company_id=companyId).first()
        return newPlan.id

    @staticmethod
    def to_questionnaire(form, plan_id):
        questionnaire = CoalCHPNeedsQuestionnaire.query.filter_by(
            plan_id=plan_id).first()

        for index in range(len(list_column_questionnaire)):
            if form.get(list_column_questionnaire[index]) != '':
                setattr(questionnaire, list_column_questionnaire[index],
                        form.get(list_column_questionnaire[index]))
        return questionnaire

    @staticmethod
    def to_questionnaireJson(questionnaire):
        datas = {}
        planId = getattr(questionnaire, 'plan_id')
        plan = Plan.search_planById(planId)
        companyName = Company.search_companyById(plan.company_id).company_name
        companyLocation = plan.company_location
        for index in range(len(list_column_questionnaire)):
            datas[list_column_questionnaire[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(getattr(questionnaire, list_column_questionnaire[index])))
        datas['company_name'] = companyName
        datas['company_location'] = companyLocation
        datas['planId'] = planId
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
            datas[list_column_furnace[index]] = format_value(
                # TODO还未过滤特殊字符项
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
        setattr(smokeAirSystem, 'plan_id', plan_id)
        return smokeAirSystem

    @staticmethod
    def to_boilerAuxiliariesJson(boilerAuxiliaries):
        datas = {}
        for index in range(len(list_column_BoilerAuxiliaries)):
            datas[list_column_BoilerAuxiliaries[index]] = format_value(
                # TODO还未过滤特殊字符项
                "number",
                str(
                    getattr(boilerAuxiliaries, list_column_BoilerAuxiliaries[
                        index])))
        return datas

    @staticmethod
    def to_boilerAuxiliaries(form, plan_id):
        boilerAuxiliaries = CoalCHPBoilerAuxiliaries.query.filter_by(
            plan_id=plan_id).first()
        boilerAuxiliaries = boilerAuxiliariesBefore().specialCalculation(
            boilerAuxiliaries, form)

        list_column_BoilerAuxiliaries.remove('c_work_pressure')
        list_column_BoilerAuxiliaries.remove('r_work_pressure')
        list_column_BoilerAuxiliaries.remove('r_drum_pressure')

        for index in range(len(list_column_BoilerAuxiliaries)):
            if form.get(list_column_BoilerAuxiliaries[index]) != '':
                setattr(boilerAuxiliaries,
                        list_column_BoilerAuxiliaries[index],
                        form.get(list_column_BoilerAuxiliaries[index]))
        list_column_BoilerAuxiliaries.append('c_work_pressure')
        list_column_BoilerAuxiliaries.append('r_work_pressure')
        list_column_BoilerAuxiliaries.append('r_drum_pressure')
        setattr(boilerAuxiliaries, 'plan_id', plan_id)
        return boilerAuxiliaries

    @staticmethod
    def drop_plan(plan_id):
        CoalCHPNeedsQuestionnaire.delete_questionnaire(plan_id)
        CoalCHPFurnaceCalculation.delete_furnace_calculation(plan_id)
        CoalCHPCoalHandingSystem.delete_handing_system(plan_id)
        CoalCHPRemovalAshSlag.delete_smoke_air_system(plan_id)
        CoalCHPDesulfurization.delete_desulfurization(plan_id)
        CoalCHPCirculatingWater.delete_circulating_water(plan_id)
        CoalCHPSmokeAirSystem.delete_smoke_air_system(plan_id)
        CoalCHPBoilerAuxiliaries.delete_boiler_auxiliaries(plan_id)
        Plan.delete_plan(plan_id)

    @staticmethod
    def to_planJson(plans):
        datas = []
        for plan in plans:
            planData = {}
            planData['id'] = getattr(plan, 'id')
            planData['company_id'] = getattr(plan, 'company_id')
            planData['user_id'] = getattr(plan, 'user_id')
            planData['company_location'] = getattr(plan, 'company_location')
            datas.append(planData)
        return datas

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

