CREATE OR REPLACE FUNCTION gaspowergeneration_turbine_auxiliary_system()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段condensate_pump_design_lift:凝结水泵的设计扬程,的计算1-----------------------------------
  IF OLD.deaerator_work_pressure != NEW.deaerator_work_pressure OR OLD.deaerator_condensation_well_pressure_difference != NEW.deaerator_condensation_well_pressure_difference OR OLD.deaerator_condensation_spray_pressure != NEW.deaerator_condensation_spray_pressure OR OLD.condenser_maximum_vacuum != NEW.condenser_maximum_vacuum OR OLD.deaerator_condensation_well_pipe_resistance != NEW.deaerator_condensation_well_pipe_resistance THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     condensate_pump_design_lift=101.97*(1.15*(NEW.deaerator_work_pressure)-(NEW.condenser_maximum_vacuum))+(NEW.deaerator_condensation_well_pressure_difference)+(NEW.deaerator_condensation_spray_pressure)+(NEW.deaerator_condensation_well_pipe_resistance)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deaerator_condensation_well_pipe_resistance ISNULL OR OLD.condenser_maximum_vacuum ISNULL OR OLD.deaerator_condensation_spray_pressure ISNULL OR OLD.deaerator_condensation_well_pressure_difference ISNULL OR OLD.deaerator_work_pressure ISNULL) AND NEW.deaerator_condensation_well_pipe_resistance NOTNULL AND NEW.condenser_maximum_vacuum NOTNULL AND NEW.deaerator_condensation_spray_pressure NOTNULL AND NEW.deaerator_condensation_well_pressure_difference NOTNULL AND NEW.deaerator_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     condensate_pump_design_lift=101.97*(1.15*(NEW.deaerator_work_pressure)-(NEW.condenser_maximum_vacuum))+(NEW.deaerator_condensation_well_pressure_difference)+(NEW.deaerator_condensation_spray_pressure)+(NEW.deaerator_condensation_well_pipe_resistance)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段condensate_pump_motor_power:配套电机功率,的计算2-----------------------------------
  IF OLD.condensate_pump_transmission_efficiency != NEW.condensate_pump_transmission_efficiency OR OLD.condensate_pump_motor_efficiency != NEW.condensate_pump_motor_efficiency OR OLD.condensate_pump_motor_spare_coefficient != NEW.condensate_pump_motor_spare_coefficient OR OLD.deaerator_work_pressure != NEW.deaerator_work_pressure OR OLD.deaerator_condensation_well_pressure_difference != NEW.deaerator_condensation_well_pressure_difference OR OLD.deaerator_condensation_spray_pressure != NEW.deaerator_condensation_spray_pressure OR OLD.condenser_maximum_vacuum != NEW.condenser_maximum_vacuum OR OLD.deaerator_condensation_well_pipe_resistance != NEW.deaerator_condensation_well_pipe_resistance OR OLD.condensate_pump_flow != NEW.condensate_pump_flow OR OLD.condensate_pump_efficiency != NEW.condensate_pump_efficiency THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     condensate_pump_motor_power=(NEW.condensate_pump_motor_spare_coefficient)*1000*9.8*(101.97*(1.15*(NEW.deaerator_work_pressure)-(NEW.condenser_maximum_vacuum))+(NEW.deaerator_condensation_well_pressure_difference)+(NEW.deaerator_condensation_spray_pressure)+(NEW.deaerator_condensation_well_pipe_resistance))*1.15*(NEW.condensate_pump_flow)/3600/1000/(NEW.condensate_pump_efficiency)/(NEW.condensate_pump_transmission_efficiency)/(NEW.condensate_pump_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.condensate_pump_motor_spare_coefficient ISNULL OR OLD.condensate_pump_motor_efficiency ISNULL OR OLD.condensate_pump_transmission_efficiency ISNULL OR OLD.condensate_pump_efficiency ISNULL OR OLD.condensate_pump_flow ISNULL OR OLD.deaerator_condensation_well_pipe_resistance ISNULL OR OLD.condenser_maximum_vacuum ISNULL OR OLD.deaerator_condensation_spray_pressure ISNULL OR OLD.deaerator_condensation_well_pressure_difference ISNULL OR OLD.deaerator_work_pressure ISNULL) AND NEW.condensate_pump_motor_spare_coefficient NOTNULL AND NEW.condensate_pump_motor_efficiency NOTNULL AND NEW.condensate_pump_transmission_efficiency NOTNULL AND NEW.condensate_pump_efficiency NOTNULL AND NEW.condensate_pump_flow NOTNULL AND NEW.deaerator_condensation_well_pipe_resistance NOTNULL AND NEW.condenser_maximum_vacuum NOTNULL AND NEW.deaerator_condensation_spray_pressure NOTNULL AND NEW.deaerator_condensation_well_pressure_difference NOTNULL AND NEW.deaerator_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     condensate_pump_motor_power=(NEW.condensate_pump_motor_spare_coefficient)*1000*9.8*(101.97*(1.15*(NEW.deaerator_work_pressure)-(NEW.condenser_maximum_vacuum))+(NEW.deaerator_condensation_well_pressure_difference)+(NEW.deaerator_condensation_spray_pressure)+(NEW.deaerator_condensation_well_pipe_resistance))*1.15*(NEW.condensate_pump_flow)/3600/1000/(NEW.condensate_pump_efficiency)/(NEW.condensate_pump_transmission_efficiency)/(NEW.condensate_pump_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段jet_pump_total_lift:总扬程,的计算3-----------------------------------
  IF OLD.extractor_work_pressure != NEW.extractor_work_pressure OR OLD.ejection_tank_work_pressure != NEW.ejection_tank_work_pressure OR OLD.extractor_ejection_waterline_height_difference != NEW.extractor_ejection_waterline_height_difference OR OLD.jet_pump_pipe_loss != NEW.jet_pump_pipe_loss THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     jet_pump_total_lift=102*((NEW.extractor_work_pressure)-(NEW.ejection_tank_work_pressure))+(NEW.extractor_ejection_waterline_height_difference)+(NEW.jet_pump_pipe_loss)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.jet_pump_pipe_loss ISNULL OR OLD.extractor_ejection_waterline_height_difference ISNULL OR OLD.ejection_tank_work_pressure ISNULL OR OLD.extractor_work_pressure ISNULL) AND NEW.jet_pump_pipe_loss NOTNULL AND NEW.extractor_ejection_waterline_height_difference NOTNULL AND NEW.ejection_tank_work_pressure NOTNULL AND NEW.extractor_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     jet_pump_total_lift=102*((NEW.extractor_work_pressure)-(NEW.ejection_tank_work_pressure))+(NEW.extractor_ejection_waterline_height_difference)+(NEW.jet_pump_pipe_loss)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段jet_pump_motor_power:配套电机功率,的计算4-----------------------------------
  IF OLD.extractor_work_pressure != NEW.extractor_work_pressure OR OLD.ejection_tank_work_pressure != NEW.ejection_tank_work_pressure OR OLD.extractor_ejection_waterline_height_difference != NEW.extractor_ejection_waterline_height_difference OR OLD.jet_pump_pipe_loss != NEW.jet_pump_pipe_loss OR OLD.jet_pump_flow != NEW.jet_pump_flow OR OLD.jet_pump_efficiency != NEW.jet_pump_efficiency OR OLD.jet_pump_transmission_efficiency != NEW.jet_pump_transmission_efficiency OR OLD.jet_pump_motor_efficiency != NEW.jet_pump_motor_efficiency OR OLD.jet_pump_motor_spare_coefficient != NEW.jet_pump_motor_spare_coefficient THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     jet_pump_motor_power=(NEW.jet_pump_motor_spare_coefficient)*1000*9.8*(102*((NEW.extractor_work_pressure)-(NEW.ejection_tank_work_pressure))+(NEW.extractor_ejection_waterline_height_difference)+(NEW.jet_pump_pipe_loss))*1.15*(NEW.jet_pump_flow)/3600/1000/(NEW.jet_pump_efficiency)/(NEW.jet_pump_transmission_efficiency)/(NEW.jet_pump_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.jet_pump_motor_spare_coefficient ISNULL OR OLD.jet_pump_motor_efficiency ISNULL OR OLD.jet_pump_transmission_efficiency ISNULL OR OLD.jet_pump_efficiency ISNULL OR OLD.jet_pump_flow ISNULL OR OLD.jet_pump_pipe_loss ISNULL OR OLD.extractor_ejection_waterline_height_difference ISNULL OR OLD.ejection_tank_work_pressure ISNULL OR OLD.extractor_work_pressure ISNULL) AND NEW.jet_pump_motor_spare_coefficient NOTNULL AND NEW.jet_pump_motor_efficiency NOTNULL AND NEW.jet_pump_transmission_efficiency NOTNULL AND NEW.jet_pump_efficiency NOTNULL AND NEW.jet_pump_flow NOTNULL AND NEW.jet_pump_pipe_loss NOTNULL AND NEW.extractor_ejection_waterline_height_difference NOTNULL AND NEW.ejection_tank_work_pressure NOTNULL AND NEW.extractor_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     jet_pump_motor_power=(NEW.jet_pump_motor_spare_coefficient)*1000*9.8*(102*((NEW.extractor_work_pressure)-(NEW.ejection_tank_work_pressure))+(NEW.extractor_ejection_waterline_height_difference)+(NEW.jet_pump_pipe_loss))*1.15*(NEW.jet_pump_flow)/3600/1000/(NEW.jet_pump_efficiency)/(NEW.jet_pump_transmission_efficiency)/(NEW.jet_pump_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段cooling_jet_pump_total_lift:总扬程,的计算5-----------------------------------
  IF OLD.cooling_ejection_tank_work_pressure != NEW.cooling_ejection_tank_work_pressure OR OLD.cooling_circulating_water_to_header_pressure != NEW.cooling_circulating_water_to_header_pressure OR OLD.cooling_extractor_ejection_waterline_height_difference != NEW.cooling_extractor_ejection_waterline_height_difference OR OLD.cooling_jet_pump_pipe_loss != NEW.cooling_jet_pump_pipe_loss THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_jet_pump_total_lift=102*((NEW.cooling_circulating_water_to_header_pressure)-(NEW.cooling_ejection_tank_work_pressure))+(NEW.cooling_extractor_ejection_waterline_height_difference)+(NEW.cooling_jet_pump_pipe_loss)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.cooling_jet_pump_pipe_loss ISNULL OR OLD.cooling_extractor_ejection_waterline_height_difference ISNULL OR OLD.cooling_circulating_water_to_header_pressure ISNULL OR OLD.cooling_ejection_tank_work_pressure ISNULL) AND NEW.cooling_jet_pump_pipe_loss NOTNULL AND NEW.cooling_extractor_ejection_waterline_height_difference NOTNULL AND NEW.cooling_circulating_water_to_header_pressure NOTNULL AND NEW.cooling_ejection_tank_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_jet_pump_total_lift=102*((NEW.cooling_circulating_water_to_header_pressure)-(NEW.cooling_ejection_tank_work_pressure))+(NEW.cooling_extractor_ejection_waterline_height_difference)+(NEW.cooling_jet_pump_pipe_loss)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段cooling_jet_pump_motor_power:配套电机功率,的计算6-----------------------------------
  IF OLD.cooling_ejection_tank_work_pressure != NEW.cooling_ejection_tank_work_pressure OR OLD.cooling_circulating_water_to_header_pressure != NEW.cooling_circulating_water_to_header_pressure OR OLD.cooling_extractor_ejection_waterline_height_difference != NEW.cooling_extractor_ejection_waterline_height_difference OR OLD.cooling_jet_pump_pipe_loss != NEW.cooling_jet_pump_pipe_loss OR OLD.cooling_jet_pump_flow != NEW.cooling_jet_pump_flow OR OLD.cooling_jet_pump_efficiency != NEW.cooling_jet_pump_efficiency OR OLD.cooling_jet_pump_transmission_efficiency != NEW.cooling_jet_pump_transmission_efficiency OR OLD.cooling_jet_pump_motor_efficiency != NEW.cooling_jet_pump_motor_efficiency OR OLD.cooling_jet_pump_motor_spare_coefficient != NEW.cooling_jet_pump_motor_spare_coefficient THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_jet_pump_motor_power=(NEW.cooling_jet_pump_motor_spare_coefficient)*1000*9.8*(102*((NEW.cooling_circulating_water_to_header_pressure)-(NEW.cooling_ejection_tank_work_pressure))+(NEW.cooling_extractor_ejection_waterline_height_difference)+(NEW.cooling_jet_pump_pipe_loss))*1.15*(NEW.cooling_jet_pump_flow)/3600/1000/(NEW.cooling_jet_pump_efficiency)/(NEW.cooling_jet_pump_transmission_efficiency)/(NEW.cooling_jet_pump_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.cooling_jet_pump_motor_spare_coefficient ISNULL OR OLD.cooling_jet_pump_motor_efficiency ISNULL OR OLD.cooling_jet_pump_transmission_efficiency ISNULL OR OLD.cooling_jet_pump_efficiency ISNULL OR OLD.cooling_jet_pump_flow ISNULL OR OLD.cooling_jet_pump_pipe_loss ISNULL OR OLD.cooling_extractor_ejection_waterline_height_difference ISNULL OR OLD.cooling_circulating_water_to_header_pressure ISNULL OR OLD.cooling_ejection_tank_work_pressure ISNULL) AND NEW.cooling_jet_pump_motor_spare_coefficient NOTNULL AND NEW.cooling_jet_pump_motor_efficiency NOTNULL AND NEW.cooling_jet_pump_transmission_efficiency NOTNULL AND NEW.cooling_jet_pump_efficiency NOTNULL AND NEW.cooling_jet_pump_flow NOTNULL AND NEW.cooling_jet_pump_pipe_loss NOTNULL AND NEW.cooling_extractor_ejection_waterline_height_difference NOTNULL AND NEW.cooling_circulating_water_to_header_pressure NOTNULL AND NEW.cooling_ejection_tank_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_jet_pump_motor_power=(NEW.cooling_jet_pump_motor_spare_coefficient)*1000*9.8*(102*((NEW.cooling_circulating_water_to_header_pressure)-(NEW.cooling_ejection_tank_work_pressure))+(NEW.cooling_extractor_ejection_waterline_height_difference)+(NEW.cooling_jet_pump_pipe_loss))*1.15*(NEW.cooling_jet_pump_flow)/3600/1000/(NEW.cooling_jet_pump_efficiency)/(NEW.cooling_jet_pump_transmission_efficiency)/(NEW.cooling_jet_pump_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段condensate_water_temperature:凝结水温度,的计算7-----------------------------------
  IF OLD.saturation_temperature != NEW.saturation_temperature OR OLD.supercooling_degree != NEW.supercooling_degree THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     condensate_water_temperature=(NEW.saturation_temperature)-(NEW.supercooling_degree)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.supercooling_degree ISNULL OR OLD.saturation_temperature ISNULL) AND NEW.supercooling_degree NOTNULL AND NEW.saturation_temperature NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     condensate_water_temperature=(NEW.saturation_temperature)-(NEW.supercooling_degree)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段calculate_exponent:计算指数,的计算8-----------------------------------
  IF OLD.cooling_water_inlet_temperature != NEW.cooling_water_inlet_temperature OR OLD.cooling_pipe_clean_coefficient != NEW.cooling_pipe_clean_coefficient OR OLD.cooling_pipe_correct_coefficient != NEW.cooling_pipe_correct_coefficient THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     calculate_exponent=0.122*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*(1+0.15*(NEW.cooling_water_inlet_temperature))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.cooling_pipe_correct_coefficient ISNULL OR OLD.cooling_pipe_clean_coefficient ISNULL OR OLD.cooling_water_inlet_temperature ISNULL) AND NEW.cooling_pipe_correct_coefficient NOTNULL AND NEW.cooling_pipe_clean_coefficient NOTNULL AND NEW.cooling_water_inlet_temperature NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     calculate_exponent=0.122*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*(1+0.15*(NEW.cooling_water_inlet_temperature))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段cooling_pipe_flow_velocity_correct_coefficient:冷却管内流速的修正系数,的计算9-----------------------------------
  IF OLD.cooling_water_inlet_temperature != NEW.cooling_water_inlet_temperature OR OLD.cooling_pipe_clean_coefficient != NEW.cooling_pipe_clean_coefficient OR OLD.cooling_pipe_correct_coefficient != NEW.cooling_pipe_correct_coefficient OR OLD.cooling_pipe_flow_velocity != NEW.cooling_pipe_flow_velocity OR OLD.cooling_pipe_diameter != NEW.cooling_pipe_diameter THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_pipe_flow_velocity_correct_coefficient=(1.1*(NEW.cooling_pipe_flow_velocity)/((NEW.cooling_pipe_diameter)*1000)^(0.25))^((0.122*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*(1+0.15*(NEW.cooling_water_inlet_temperature))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.cooling_pipe_diameter ISNULL OR OLD.cooling_pipe_flow_velocity ISNULL OR OLD.cooling_pipe_correct_coefficient ISNULL OR OLD.cooling_pipe_clean_coefficient ISNULL OR OLD.cooling_water_inlet_temperature ISNULL) AND NEW.cooling_pipe_diameter NOTNULL AND NEW.cooling_pipe_flow_velocity NOTNULL AND NEW.cooling_pipe_correct_coefficient NOTNULL AND NEW.cooling_pipe_clean_coefficient NOTNULL AND NEW.cooling_water_inlet_temperature NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_pipe_flow_velocity_correct_coefficient=(1.1*(NEW.cooling_pipe_flow_velocity)/((NEW.cooling_pipe_diameter)*1000)^(0.25))^((0.122*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*(1+0.15*(NEW.cooling_water_inlet_temperature))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段cooling_water_inlet_temperature_correct_coefficient:冷却水进口温度修正系数,的计算10-----------------------------------
  IF OLD.cooling_water_inlet_temperature != NEW.cooling_water_inlet_temperature OR OLD.cooling_pipe_clean_coefficient != NEW.cooling_pipe_clean_coefficient OR OLD.cooling_pipe_correct_coefficient != NEW.cooling_pipe_correct_coefficient OR OLD.condenser_steam_load_correct_coefficient != NEW.condenser_steam_load_correct_coefficient THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_water_inlet_temperature_correct_coefficient=1-(NEW.condenser_steam_load_correct_coefficient)*sqrt((NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient))/1000*(35-(NEW.cooling_water_inlet_temperature))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.condenser_steam_load_correct_coefficient ISNULL OR OLD.cooling_pipe_correct_coefficient ISNULL OR OLD.cooling_pipe_clean_coefficient ISNULL OR OLD.cooling_water_inlet_temperature ISNULL) AND NEW.condenser_steam_load_correct_coefficient NOTNULL AND NEW.cooling_pipe_correct_coefficient NOTNULL AND NEW.cooling_pipe_clean_coefficient NOTNULL AND NEW.cooling_water_inlet_temperature NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_water_inlet_temperature_correct_coefficient=1-(NEW.condenser_steam_load_correct_coefficient)*sqrt((NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient))/1000*(35-(NEW.cooling_water_inlet_temperature))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段total_heat_transfer_coefficient:总传热系数,的计算11-----------------------------------
  IF OLD.cooling_water_inlet_temperature != NEW.cooling_water_inlet_temperature OR OLD.cooling_pipe_clean_coefficient != NEW.cooling_pipe_clean_coefficient OR OLD.cooling_pipe_correct_coefficient != NEW.cooling_pipe_correct_coefficient OR OLD.cooling_pipe_flow_velocity != NEW.cooling_pipe_flow_velocity OR OLD.cooling_pipe_diameter != NEW.cooling_pipe_diameter OR OLD.condenser_steam_load_correct_coefficient != NEW.condenser_steam_load_correct_coefficient OR OLD.cooling_water_pass_correct_coefficient != NEW.cooling_water_pass_correct_coefficient OR OLD.condenser_steam_load_change_correct_coefficient != NEW.condenser_steam_load_change_correct_coefficient THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     total_heat_transfer_coefficient=4.07*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*((1.1*(NEW.cooling_pipe_flow_velocity)/((NEW.cooling_pipe_diameter)*1000)^(0.25))^((0.122*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*(1+0.15*(NEW.cooling_water_inlet_temperature)))))*(1-(NEW.condenser_steam_load_correct_coefficient)*sqrt((NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient))/1000*(35-(NEW.cooling_water_inlet_temperature))^2)*(NEW.cooling_water_pass_correct_coefficient)*(NEW.condenser_steam_load_change_correct_coefficient)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.condenser_steam_load_change_correct_coefficient ISNULL OR OLD.cooling_water_pass_correct_coefficient ISNULL OR OLD.condenser_steam_load_correct_coefficient ISNULL OR OLD.cooling_pipe_diameter ISNULL OR OLD.cooling_pipe_flow_velocity ISNULL OR OLD.cooling_pipe_correct_coefficient ISNULL OR OLD.cooling_pipe_clean_coefficient ISNULL OR OLD.cooling_water_inlet_temperature ISNULL) AND NEW.condenser_steam_load_change_correct_coefficient NOTNULL AND NEW.cooling_water_pass_correct_coefficient NOTNULL AND NEW.condenser_steam_load_correct_coefficient NOTNULL AND NEW.cooling_pipe_diameter NOTNULL AND NEW.cooling_pipe_flow_velocity NOTNULL AND NEW.cooling_pipe_correct_coefficient NOTNULL AND NEW.cooling_pipe_clean_coefficient NOTNULL AND NEW.cooling_water_inlet_temperature NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     total_heat_transfer_coefficient=4.07*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*((1.1*(NEW.cooling_pipe_flow_velocity)/((NEW.cooling_pipe_diameter)*1000)^(0.25))^((0.122*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*(1+0.15*(NEW.cooling_water_inlet_temperature)))))*(1-(NEW.condenser_steam_load_correct_coefficient)*sqrt((NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient))/1000*(35-(NEW.cooling_water_inlet_temperature))^2)*(NEW.cooling_water_pass_correct_coefficient)*(NEW.condenser_steam_load_change_correct_coefficient)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段condenser_heat_load:凝汽器热负荷,的计算12-----------------------------------
  IF OLD.condenser_flow_amount != NEW.condenser_flow_amount OR OLD.turbine_exhaust_enthalpy != NEW.turbine_exhaust_enthalpy OR OLD.condensate_water_enthalpy != NEW.condensate_water_enthalpy THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     condenser_heat_load=(NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.condensate_water_enthalpy ISNULL OR OLD.turbine_exhaust_enthalpy ISNULL OR OLD.condenser_flow_amount ISNULL) AND NEW.condensate_water_enthalpy NOTNULL AND NEW.turbine_exhaust_enthalpy NOTNULL AND NEW.condenser_flow_amount NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     condenser_heat_load=(NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段circulating_water_amount:循环水量,的计算13-----------------------------------
  IF OLD.condenser_flow_amount != NEW.condenser_flow_amount OR OLD.circulation_ratio != NEW.circulation_ratio THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     circulating_water_amount=(NEW.circulation_ratio)*(NEW.condenser_flow_amount)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulation_ratio ISNULL OR OLD.condenser_flow_amount ISNULL) AND NEW.circulation_ratio NOTNULL AND NEW.condenser_flow_amount NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     circulating_water_amount=(NEW.circulation_ratio)*(NEW.condenser_flow_amount)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段cooling_water_temperature_rise:冷却水温升,的计算14-----------------------------------
  IF OLD.condenser_flow_amount != NEW.condenser_flow_amount OR OLD.turbine_exhaust_enthalpy != NEW.turbine_exhaust_enthalpy OR OLD.condensate_water_enthalpy != NEW.condensate_water_enthalpy OR OLD.circulation_ratio != NEW.circulation_ratio THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_water_temperature_rise=((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulation_ratio ISNULL OR OLD.condensate_water_enthalpy ISNULL OR OLD.turbine_exhaust_enthalpy ISNULL OR OLD.condenser_flow_amount ISNULL) AND NEW.circulation_ratio NOTNULL AND NEW.condensate_water_enthalpy NOTNULL AND NEW.turbine_exhaust_enthalpy NOTNULL AND NEW.condenser_flow_amount NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_water_temperature_rise=((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段cooling_water_outlet_temperature:冷却水出口温度,的计算15-----------------------------------
  IF OLD.condenser_flow_amount != NEW.condenser_flow_amount OR OLD.turbine_exhaust_enthalpy != NEW.turbine_exhaust_enthalpy OR OLD.cooling_water_inlet_temperature != NEW.cooling_water_inlet_temperature OR OLD.condensate_water_enthalpy != NEW.condensate_water_enthalpy OR OLD.circulation_ratio != NEW.circulation_ratio THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_water_outlet_temperature=(NEW.cooling_water_inlet_temperature)+(((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulation_ratio ISNULL OR OLD.condensate_water_enthalpy ISNULL OR OLD.cooling_water_inlet_temperature ISNULL OR OLD.turbine_exhaust_enthalpy ISNULL OR OLD.condenser_flow_amount ISNULL) AND NEW.circulation_ratio NOTNULL AND NEW.condensate_water_enthalpy NOTNULL AND NEW.cooling_water_inlet_temperature NOTNULL AND NEW.turbine_exhaust_enthalpy NOTNULL AND NEW.condenser_flow_amount NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_water_outlet_temperature=(NEW.cooling_water_inlet_temperature)+(((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段logarithmic_average_temperature_difference:对数平均温差,的计算16-----------------------------------
  IF OLD.condenser_flow_amount != NEW.condenser_flow_amount OR OLD.turbine_exhaust_enthalpy != NEW.turbine_exhaust_enthalpy OR OLD.cooling_water_inlet_temperature != NEW.cooling_water_inlet_temperature OR OLD.saturation_temperature != NEW.saturation_temperature OR OLD.condensate_water_enthalpy != NEW.condensate_water_enthalpy OR OLD.circulation_ratio != NEW.circulation_ratio THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     logarithmic_average_temperature_difference=(((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868)/ln(((NEW.saturation_temperature)-(NEW.cooling_water_inlet_temperature))/((NEW.saturation_temperature)-((NEW.cooling_water_inlet_temperature)+(((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulation_ratio ISNULL OR OLD.condensate_water_enthalpy ISNULL OR OLD.saturation_temperature ISNULL OR OLD.cooling_water_inlet_temperature ISNULL OR OLD.turbine_exhaust_enthalpy ISNULL OR OLD.condenser_flow_amount ISNULL) AND NEW.circulation_ratio NOTNULL AND NEW.condensate_water_enthalpy NOTNULL AND NEW.saturation_temperature NOTNULL AND NEW.cooling_water_inlet_temperature NOTNULL AND NEW.turbine_exhaust_enthalpy NOTNULL AND NEW.condenser_flow_amount NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     logarithmic_average_temperature_difference=(((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868)/ln(((NEW.saturation_temperature)-(NEW.cooling_water_inlet_temperature))/((NEW.saturation_temperature)-((NEW.cooling_water_inlet_temperature)+(((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段cooling_area:冷却面积,的计算17-----------------------------------
  IF OLD.condenser_flow_amount != NEW.condenser_flow_amount OR OLD.turbine_exhaust_enthalpy != NEW.turbine_exhaust_enthalpy OR OLD.cooling_water_inlet_temperature != NEW.cooling_water_inlet_temperature OR OLD.saturation_temperature != NEW.saturation_temperature OR OLD.condensate_water_enthalpy != NEW.condensate_water_enthalpy OR OLD.cooling_pipe_clean_coefficient != NEW.cooling_pipe_clean_coefficient OR OLD.cooling_pipe_correct_coefficient != NEW.cooling_pipe_correct_coefficient OR OLD.cooling_pipe_flow_velocity != NEW.cooling_pipe_flow_velocity OR OLD.cooling_pipe_diameter != NEW.cooling_pipe_diameter OR OLD.condenser_steam_load_correct_coefficient != NEW.condenser_steam_load_correct_coefficient OR OLD.cooling_water_pass_correct_coefficient != NEW.cooling_water_pass_correct_coefficient OR OLD.condenser_steam_load_change_correct_coefficient != NEW.condenser_steam_load_change_correct_coefficient OR OLD.circulation_ratio != NEW.circulation_ratio THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_area=((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/(4.07*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*((1.1*(NEW.cooling_pipe_flow_velocity)/((NEW.cooling_pipe_diameter)*1000)^(0.25))^((0.122*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*(1+0.15*(NEW.cooling_water_inlet_temperature)))))*(1-(NEW.condenser_steam_load_correct_coefficient)*sqrt((NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient))/1000*(35-(NEW.cooling_water_inlet_temperature))^2)*(NEW.cooling_water_pass_correct_coefficient)*(NEW.condenser_steam_load_change_correct_coefficient))/((((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868)/ln(((NEW.saturation_temperature)-(NEW.cooling_water_inlet_temperature))/((NEW.saturation_temperature)-((NEW.cooling_water_inlet_temperature)+(((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulation_ratio ISNULL OR OLD.condenser_steam_load_change_correct_coefficient ISNULL OR OLD.cooling_water_pass_correct_coefficient ISNULL OR OLD.condenser_steam_load_correct_coefficient ISNULL OR OLD.cooling_pipe_diameter ISNULL OR OLD.cooling_pipe_flow_velocity ISNULL OR OLD.cooling_pipe_correct_coefficient ISNULL OR OLD.cooling_pipe_clean_coefficient ISNULL OR OLD.condensate_water_enthalpy ISNULL OR OLD.saturation_temperature ISNULL OR OLD.cooling_water_inlet_temperature ISNULL OR OLD.turbine_exhaust_enthalpy ISNULL OR OLD.condenser_flow_amount ISNULL) AND NEW.circulation_ratio NOTNULL AND NEW.condenser_steam_load_change_correct_coefficient NOTNULL AND NEW.cooling_water_pass_correct_coefficient NOTNULL AND NEW.condenser_steam_load_correct_coefficient NOTNULL AND NEW.cooling_pipe_diameter NOTNULL AND NEW.cooling_pipe_flow_velocity NOTNULL AND NEW.cooling_pipe_correct_coefficient NOTNULL AND NEW.cooling_pipe_clean_coefficient NOTNULL AND NEW.condensate_water_enthalpy NOTNULL AND NEW.saturation_temperature NOTNULL AND NEW.cooling_water_inlet_temperature NOTNULL AND NEW.turbine_exhaust_enthalpy NOTNULL AND NEW.condenser_flow_amount NOTNULL THEN
     update gaspowergeneration_turbine_auxiliary_system set 

     cooling_area=((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/(4.07*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*((1.1*(NEW.cooling_pipe_flow_velocity)/((NEW.cooling_pipe_diameter)*1000)^(0.25))^((0.122*(NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient)*(1+0.15*(NEW.cooling_water_inlet_temperature)))))*(1-(NEW.condenser_steam_load_correct_coefficient)*sqrt((NEW.cooling_pipe_clean_coefficient)*(NEW.cooling_pipe_correct_coefficient))/1000*(35-(NEW.cooling_water_inlet_temperature))^2)*(NEW.cooling_water_pass_correct_coefficient)*(NEW.condenser_steam_load_change_correct_coefficient))/((((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868)/ln(((NEW.saturation_temperature)-(NEW.cooling_water_inlet_temperature))/((NEW.saturation_temperature)-((NEW.cooling_water_inlet_temperature)+(((NEW.condenser_flow_amount)*((NEW.turbine_exhaust_enthalpy)-(NEW.condensate_water_enthalpy)))/((NEW.circulation_ratio)*(NEW.condenser_flow_amount))/4.1868)))))
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_turbine_auxiliary_system" AFTER UPDATE OF
"condensate_pump_transmission_efficiency",
"condensate_pump_motor_efficiency",
"condensate_pump_motor_spare_coefficient",
"extractor_work_pressure",
"ejection_tank_work_pressure",
"extractor_ejection_waterline_height_difference",
"deaerator_work_pressure",
"jet_pump_pipe_loss",
"jet_pump_flow",
"jet_pump_efficiency",
"jet_pump_transmission_efficiency",
"jet_pump_motor_efficiency",
"jet_pump_motor_spare_coefficient",
"deaerator_condensation_well_pressure_difference",
"cooling_ejection_tank_work_pressure",
"cooling_circulating_water_to_header_pressure",
"cooling_extractor_ejection_waterline_height_difference",
"cooling_jet_pump_pipe_loss",
"cooling_jet_pump_flow",
"cooling_jet_pump_efficiency",
"cooling_jet_pump_transmission_efficiency",
"cooling_jet_pump_motor_efficiency",
"cooling_jet_pump_motor_spare_coefficient",
"deaerator_condensation_spray_pressure",
"condenser_flow_amount",
"turbine_exhaust_enthalpy",
"cooling_water_inlet_temperature",
"saturation_temperature",
"supercooling_degree",
"condenser_maximum_vacuum",
"condensate_water_enthalpy",
"cooling_pipe_clean_coefficient",
"cooling_pipe_correct_coefficient",
"cooling_pipe_flow_velocity",
"cooling_pipe_diameter",
"condenser_steam_load_correct_coefficient",
"cooling_water_pass_correct_coefficient",
"deaerator_condensation_well_pipe_resistance",
"condenser_steam_load_change_correct_coefficient",
"circulation_ratio",
"condensate_pump_flow",
"condensate_pump_efficiency"
ON "public"."gaspowergeneration_turbine_auxiliary_system"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_turbine_auxiliary_system"();

