-------------INSERT INTO biomasschp_turbine_auxiliary (plan_id) VALUES (NEWIDD);

CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段w_condensate_pump_lift:凝结水泵的设计扬程,的计算1-----------------------------------
  IF OLD.w_deaerator_working_pressure != NEW.w_deaerator_working_pressure OR OLD.w_deaerator_difference != NEW.w_deaerator_difference OR OLD.w_deaerator_need_pressure != NEW.w_deaerator_need_pressure OR OLD.w_condenser_higter != NEW.w_condenser_higter OR OLD.w_hot_well_resistance != NEW.w_hot_well_resistance THEN
     update biomasschp_turbine_auxiliary set 

     w_condensate_pump_lift=101.97*(1.15*(NEW.w_deaerator_working_pressure)-(NEW.w_condenser_higter))+(NEW.w_deaerator_difference)+(NEW.w_deaerator_need_pressure)+(NEW.w_hot_well_resistance)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.w_hot_well_resistance ISNULL OR OLD.w_condenser_higter ISNULL OR OLD.w_deaerator_need_pressure ISNULL OR OLD.w_deaerator_difference ISNULL OR OLD.w_deaerator_working_pressure ISNULL) AND NEW.w_hot_well_resistance NOTNULL AND NEW.w_condenser_higter NOTNULL AND NEW.w_deaerator_need_pressure NOTNULL AND NEW.w_deaerator_difference NOTNULL AND NEW.w_deaerator_working_pressure NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     w_condensate_pump_lift=101.97*(1.15*(NEW.w_deaerator_working_pressure)-(NEW.w_condenser_higter))+(NEW.w_deaerator_difference)+(NEW.w_deaerator_need_pressure)+(NEW.w_hot_well_resistance)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段w_auxiliary_motor_power:配套电机功率,的计算2-----------------------------------
  IF OLD.w_mechanical_transmission_efficiency != NEW.w_mechanical_transmission_efficiency OR OLD.w_motor_efficiency != NEW.w_motor_efficiency OR OLD.w_motor_reserve_coefficient != NEW.w_motor_reserve_coefficient OR OLD.w_deaerator_working_pressure != NEW.w_deaerator_working_pressure OR OLD.w_deaerator_difference != NEW.w_deaerator_difference OR OLD.w_deaerator_need_pressure != NEW.w_deaerator_need_pressure OR OLD.w_condenser_higter != NEW.w_condenser_higter OR OLD.w_hot_well_resistance != NEW.w_hot_well_resistance OR OLD.w_flow_amount != NEW.w_flow_amount OR OLD.w_pump_efficiency != NEW.w_pump_efficiency THEN
     update biomasschp_turbine_auxiliary set 

     w_auxiliary_motor_power=(NEW.w_motor_reserve_coefficient)*1000*9.8*(101.97*(1.15*(NEW.w_deaerator_working_pressure)-(NEW.w_condenser_higter))+(NEW.w_deaerator_difference)+(NEW.w_deaerator_need_pressure)+(NEW.w_hot_well_resistance))*1.15*(NEW.w_flow_amount)/3600/1000/(NEW.w_pump_efficiency)/(NEW.w_mechanical_transmission_efficiency)/(NEW.w_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.w_motor_reserve_coefficient ISNULL OR OLD.w_motor_efficiency ISNULL OR OLD.w_mechanical_transmission_efficiency ISNULL OR OLD.w_pump_efficiency ISNULL OR OLD.w_flow_amount ISNULL OR OLD.w_hot_well_resistance ISNULL OR OLD.w_condenser_higter ISNULL OR OLD.w_deaerator_need_pressure ISNULL OR OLD.w_deaerator_difference ISNULL OR OLD.w_deaerator_working_pressure ISNULL) AND NEW.w_motor_reserve_coefficient NOTNULL AND NEW.w_motor_efficiency NOTNULL AND NEW.w_mechanical_transmission_efficiency NOTNULL AND NEW.w_pump_efficiency NOTNULL AND NEW.w_flow_amount NOTNULL AND NEW.w_hot_well_resistance NOTNULL AND NEW.w_condenser_higter NOTNULL AND NEW.w_deaerator_need_pressure NOTNULL AND NEW.w_deaerator_difference NOTNULL AND NEW.w_deaerator_working_pressure NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     w_auxiliary_motor_power=(NEW.w_motor_reserve_coefficient)*1000*9.8*(101.97*(1.15*(NEW.w_deaerator_working_pressure)-(NEW.w_condenser_higter))+(NEW.w_deaerator_difference)+(NEW.w_deaerator_need_pressure)+(NEW.w_hot_well_resistance))*1.15*(NEW.w_flow_amount)/3600/1000/(NEW.w_pump_efficiency)/(NEW.w_mechanical_transmission_efficiency)/(NEW.w_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_condensate_temperature:凝结水温度,的计算3-----------------------------------
  IF OLD.m_saturation_temperature != NEW.m_saturation_temperature OR OLD.m_supercooling != NEW.m_supercooling THEN
     update biomasschp_turbine_auxiliary set 

     m_condensate_temperature=(NEW.m_saturation_temperature)-(NEW.m_supercooling)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_supercooling ISNULL OR OLD.m_saturation_temperature ISNULL) AND NEW.m_supercooling NOTNULL AND NEW.m_saturation_temperature NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_condensate_temperature=(NEW.m_saturation_temperature)-(NEW.m_supercooling)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_calculation_index:计算指数,的计算4-----------------------------------
  IF OLD.m_cooling_water_inlet_temperature != NEW.m_cooling_water_inlet_temperature OR OLD.m_cooling_pipe_coefficient != NEW.m_cooling_pipe_coefficient OR OLD.m_correction_coefficient != NEW.m_correction_coefficient THEN
     update biomasschp_turbine_auxiliary set 

     m_calculation_index=0.122*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*(1+0.15*(NEW.m_cooling_water_inlet_temperature))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_correction_coefficient ISNULL OR OLD.m_cooling_pipe_coefficient ISNULL OR OLD.m_cooling_water_inlet_temperature ISNULL) AND NEW.m_correction_coefficient NOTNULL AND NEW.m_cooling_pipe_coefficient NOTNULL AND NEW.m_cooling_water_inlet_temperature NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_calculation_index=0.122*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*(1+0.15*(NEW.m_cooling_water_inlet_temperature))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_flow_speed_correction:冷却管内流速的修正系数,的计算5-----------------------------------
  IF OLD.m_cooling_water_inlet_temperature != NEW.m_cooling_water_inlet_temperature OR OLD.m_cooling_pipe_coefficient != NEW.m_cooling_pipe_coefficient OR OLD.m_correction_coefficient != NEW.m_correction_coefficient OR OLD.m_cooling_flow != NEW.m_cooling_flow OR OLD.m_cooling_type != NEW.m_cooling_type THEN
     update biomasschp_turbine_auxiliary set 

     m_flow_speed_correction=(1.1*(NEW.m_cooling_flow)/((NEW.m_cooling_type)*1000)^(1/4))^((0.122*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*(1+0.15*(NEW.m_cooling_water_inlet_temperature))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_cooling_type ISNULL OR OLD.m_cooling_flow ISNULL OR OLD.m_correction_coefficient ISNULL OR OLD.m_cooling_pipe_coefficient ISNULL OR OLD.m_cooling_water_inlet_temperature ISNULL) AND NEW.m_cooling_type NOTNULL AND NEW.m_cooling_flow NOTNULL AND NEW.m_correction_coefficient NOTNULL AND NEW.m_cooling_pipe_coefficient NOTNULL AND NEW.m_cooling_water_inlet_temperature NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_flow_speed_correction=(1.1*(NEW.m_cooling_flow)/((NEW.m_cooling_type)*1000)^(1/4))^((0.122*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*(1+0.15*(NEW.m_cooling_water_inlet_temperature))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_inlet_temperature:冷却水进口温度修正系数,的计算6-----------------------------------
  IF OLD.m_cooling_water_inlet_temperature != NEW.m_cooling_water_inlet_temperature OR OLD.m_cooling_pipe_coefficient != NEW.m_cooling_pipe_coefficient OR OLD.m_correction_coefficient != NEW.m_correction_coefficient OR OLD.m_correction_condensers != NEW.m_correction_condensers THEN
     update biomasschp_turbine_auxiliary set 

     m_inlet_temperature=1-(NEW.m_correction_condensers)*((NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient))^0.5/1000*(35-(NEW.m_cooling_water_inlet_temperature))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_correction_condensers ISNULL OR OLD.m_correction_coefficient ISNULL OR OLD.m_cooling_pipe_coefficient ISNULL OR OLD.m_cooling_water_inlet_temperature ISNULL) AND NEW.m_correction_condensers NOTNULL AND NEW.m_correction_coefficient NOTNULL AND NEW.m_cooling_pipe_coefficient NOTNULL AND NEW.m_cooling_water_inlet_temperature NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_inlet_temperature=1-(NEW.m_correction_condensers)*((NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient))^0.5/1000*(35-(NEW.m_cooling_water_inlet_temperature))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_total_heat_transfer:总传热系数,的计算7-----------------------------------
  IF OLD.m_cooling_water_inlet_temperature != NEW.m_cooling_water_inlet_temperature OR OLD.m_cooling_pipe_coefficient != NEW.m_cooling_pipe_coefficient OR OLD.m_correction_coefficient != NEW.m_correction_coefficient OR OLD.m_cooling_flow != NEW.m_cooling_flow OR OLD.m_cooling_type != NEW.m_cooling_type OR OLD.m_correction_condensers != NEW.m_correction_condensers OR OLD.m_flow_count != NEW.m_flow_count OR OLD.m_consideration_change != NEW.m_consideration_change THEN
     update biomasschp_turbine_auxiliary set 

     m_total_heat_transfer=4.07*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*((1.1*(NEW.m_cooling_flow)/((NEW.m_cooling_type)*1000)^(1/4))^((0.122*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*(1+0.15*(NEW.m_cooling_water_inlet_temperature)))))*(1-(NEW.m_correction_condensers)*((NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient))^0.5/1000*(35-(NEW.m_cooling_water_inlet_temperature))^2)*(NEW.m_flow_count)*(NEW.m_consideration_change)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_consideration_change ISNULL OR OLD.m_flow_count ISNULL OR OLD.m_correction_condensers ISNULL OR OLD.m_cooling_type ISNULL OR OLD.m_cooling_flow ISNULL OR OLD.m_correction_coefficient ISNULL OR OLD.m_cooling_pipe_coefficient ISNULL OR OLD.m_cooling_water_inlet_temperature ISNULL) AND NEW.m_consideration_change NOTNULL AND NEW.m_flow_count NOTNULL AND NEW.m_correction_condensers NOTNULL AND NEW.m_cooling_type NOTNULL AND NEW.m_cooling_flow NOTNULL AND NEW.m_correction_coefficient NOTNULL AND NEW.m_cooling_pipe_coefficient NOTNULL AND NEW.m_cooling_water_inlet_temperature NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_total_heat_transfer=4.07*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*((1.1*(NEW.m_cooling_flow)/((NEW.m_cooling_type)*1000)^(1/4))^((0.122*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*(1+0.15*(NEW.m_cooling_water_inlet_temperature)))))*(1-(NEW.m_correction_condensers)*((NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient))^0.5/1000*(35-(NEW.m_cooling_water_inlet_temperature))^2)*(NEW.m_flow_count)*(NEW.m_consideration_change)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_condenser_heat_load:凝汽器热负荷,的计算8-----------------------------------
  IF OLD.m_condensate_amount != NEW.m_condensate_amount OR OLD.m_steam_enthalpy != NEW.m_steam_enthalpy OR OLD.m_condensate_enthalpy != NEW.m_condensate_enthalpy THEN
     update biomasschp_turbine_auxiliary set 

     m_condenser_heat_load=(NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_condensate_enthalpy ISNULL OR OLD.m_steam_enthalpy ISNULL OR OLD.m_condensate_amount ISNULL) AND NEW.m_condensate_enthalpy NOTNULL AND NEW.m_steam_enthalpy NOTNULL AND NEW.m_condensate_amount NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_condenser_heat_load=(NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_circulating_water:循环水量,的计算9-----------------------------------
  IF OLD.m_condensate_amount != NEW.m_condensate_amount OR OLD.m_cycle_ratio != NEW.m_cycle_ratio THEN
     update biomasschp_turbine_auxiliary set 

     m_circulating_water=(NEW.m_cycle_ratio)*(NEW.m_condensate_amount)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_cycle_ratio ISNULL OR OLD.m_condensate_amount ISNULL) AND NEW.m_cycle_ratio NOTNULL AND NEW.m_condensate_amount NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_circulating_water=(NEW.m_cycle_ratio)*(NEW.m_condensate_amount)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_cooling_water_rise:冷却水温,的计算10-----------------------------------
  IF OLD.m_condensate_amount != NEW.m_condensate_amount OR OLD.m_steam_enthalpy != NEW.m_steam_enthalpy OR OLD.m_condensate_enthalpy != NEW.m_condensate_enthalpy OR OLD.m_cycle_ratio != NEW.m_cycle_ratio THEN
     update biomasschp_turbine_auxiliary set 

     m_cooling_water_rise=((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_cycle_ratio ISNULL OR OLD.m_condensate_enthalpy ISNULL OR OLD.m_steam_enthalpy ISNULL OR OLD.m_condensate_amount ISNULL) AND NEW.m_cycle_ratio NOTNULL AND NEW.m_condensate_enthalpy NOTNULL AND NEW.m_steam_enthalpy NOTNULL AND NEW.m_condensate_amount NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_cooling_water_rise=((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_cooling_outlet_temperature:冷却水出口温度,的计算11-----------------------------------
  IF OLD.m_condensate_amount != NEW.m_condensate_amount OR OLD.m_steam_enthalpy != NEW.m_steam_enthalpy OR OLD.m_cooling_water_inlet_temperature != NEW.m_cooling_water_inlet_temperature OR OLD.m_condensate_enthalpy != NEW.m_condensate_enthalpy OR OLD.m_cycle_ratio != NEW.m_cycle_ratio THEN
     update biomasschp_turbine_auxiliary set 

     m_cooling_outlet_temperature=(NEW.m_cooling_water_inlet_temperature)+(((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_cycle_ratio ISNULL OR OLD.m_condensate_enthalpy ISNULL OR OLD.m_cooling_water_inlet_temperature ISNULL OR OLD.m_steam_enthalpy ISNULL OR OLD.m_condensate_amount ISNULL) AND NEW.m_cycle_ratio NOTNULL AND NEW.m_condensate_enthalpy NOTNULL AND NEW.m_cooling_water_inlet_temperature NOTNULL AND NEW.m_steam_enthalpy NOTNULL AND NEW.m_condensate_amount NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_cooling_outlet_temperature=(NEW.m_cooling_water_inlet_temperature)+(((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_logarithmic_mean_difference:对数平均温差,的计算12-----------------------------------
  IF OLD.m_condensate_amount != NEW.m_condensate_amount OR OLD.m_steam_enthalpy != NEW.m_steam_enthalpy OR OLD.m_cooling_water_inlet_temperature != NEW.m_cooling_water_inlet_temperature OR OLD.m_saturation_temperature != NEW.m_saturation_temperature OR OLD.m_condensate_enthalpy != NEW.m_condensate_enthalpy OR OLD.m_cycle_ratio != NEW.m_cycle_ratio THEN
     update biomasschp_turbine_auxiliary set 

     m_logarithmic_mean_difference=(((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868)/ln(((NEW.m_saturation_temperature)-(NEW.m_cooling_water_inlet_temperature))/((NEW.m_saturation_temperature)-((NEW.m_cooling_water_inlet_temperature)+(((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_cycle_ratio ISNULL OR OLD.m_condensate_enthalpy ISNULL OR OLD.m_saturation_temperature ISNULL OR OLD.m_cooling_water_inlet_temperature ISNULL OR OLD.m_steam_enthalpy ISNULL OR OLD.m_condensate_amount ISNULL) AND NEW.m_cycle_ratio NOTNULL AND NEW.m_condensate_enthalpy NOTNULL AND NEW.m_saturation_temperature NOTNULL AND NEW.m_cooling_water_inlet_temperature NOTNULL AND NEW.m_steam_enthalpy NOTNULL AND NEW.m_condensate_amount NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_logarithmic_mean_difference=(((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868)/ln(((NEW.m_saturation_temperature)-(NEW.m_cooling_water_inlet_temperature))/((NEW.m_saturation_temperature)-((NEW.m_cooling_water_inlet_temperature)+(((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_area_cooling_surface:冷却面积,的计算13-----------------------------------
  IF OLD.m_condensate_amount != NEW.m_condensate_amount OR OLD.m_steam_enthalpy != NEW.m_steam_enthalpy OR OLD.m_cooling_water_inlet_temperature != NEW.m_cooling_water_inlet_temperature OR OLD.m_saturation_temperature != NEW.m_saturation_temperature OR OLD.m_condensate_enthalpy != NEW.m_condensate_enthalpy OR OLD.m_cooling_pipe_coefficient != NEW.m_cooling_pipe_coefficient OR OLD.m_correction_coefficient != NEW.m_correction_coefficient OR OLD.m_cooling_flow != NEW.m_cooling_flow OR OLD.m_cooling_type != NEW.m_cooling_type OR OLD.m_correction_condensers != NEW.m_correction_condensers OR OLD.m_flow_count != NEW.m_flow_count OR OLD.m_consideration_change != NEW.m_consideration_change OR OLD.m_cycle_ratio != NEW.m_cycle_ratio THEN
     update biomasschp_turbine_auxiliary set 

     m_area_cooling_surface=((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/(4.07*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*((1.1*(NEW.m_cooling_flow)/((NEW.m_cooling_type)*1000)^(1/4))^((0.122*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*(1+0.15*(NEW.m_cooling_water_inlet_temperature)))))*(1-(NEW.m_correction_condensers)*((NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient))^0.5/1000*(35-(NEW.m_cooling_water_inlet_temperature))^2)*(NEW.m_flow_count)*(NEW.m_consideration_change))/((((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868)/ln(((NEW.m_saturation_temperature)-(NEW.m_cooling_water_inlet_temperature))/((NEW.m_saturation_temperature)-((NEW.m_cooling_water_inlet_temperature)+(((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_cycle_ratio ISNULL OR OLD.m_consideration_change ISNULL OR OLD.m_flow_count ISNULL OR OLD.m_correction_condensers ISNULL OR OLD.m_cooling_type ISNULL OR OLD.m_cooling_flow ISNULL OR OLD.m_correction_coefficient ISNULL OR OLD.m_cooling_pipe_coefficient ISNULL OR OLD.m_condensate_enthalpy ISNULL OR OLD.m_saturation_temperature ISNULL OR OLD.m_cooling_water_inlet_temperature ISNULL OR OLD.m_steam_enthalpy ISNULL OR OLD.m_condensate_amount ISNULL) AND NEW.m_cycle_ratio NOTNULL AND NEW.m_consideration_change NOTNULL AND NEW.m_flow_count NOTNULL AND NEW.m_correction_condensers NOTNULL AND NEW.m_cooling_type NOTNULL AND NEW.m_cooling_flow NOTNULL AND NEW.m_correction_coefficient NOTNULL AND NEW.m_cooling_pipe_coefficient NOTNULL AND NEW.m_condensate_enthalpy NOTNULL AND NEW.m_saturation_temperature NOTNULL AND NEW.m_cooling_water_inlet_temperature NOTNULL AND NEW.m_steam_enthalpy NOTNULL AND NEW.m_condensate_amount NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     m_area_cooling_surface=((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/(4.07*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*((1.1*(NEW.m_cooling_flow)/((NEW.m_cooling_type)*1000)^(1/4))^((0.122*(NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient)*(1+0.15*(NEW.m_cooling_water_inlet_temperature)))))*(1-(NEW.m_correction_condensers)*((NEW.m_cooling_pipe_coefficient)*(NEW.m_correction_coefficient))^0.5/1000*(35-(NEW.m_cooling_water_inlet_temperature))^2)*(NEW.m_flow_count)*(NEW.m_consideration_change))/((((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868)/ln(((NEW.m_saturation_temperature)-(NEW.m_cooling_water_inlet_temperature))/((NEW.m_saturation_temperature)-((NEW.m_cooling_water_inlet_temperature)+(((NEW.m_condensate_amount)*((NEW.m_steam_enthalpy)-(NEW.m_condensate_enthalpy)))/((NEW.m_cycle_ratio)*(NEW.m_condensate_amount))/4.1868)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_total_lift:总扬程,的计算14-----------------------------------
  IF OLD.f_air_ejector_pressure != NEW.f_air_ejector_pressure OR OLD.f_water_tank_pressure != NEW.f_water_tank_pressure OR OLD.f_water_difference != NEW.f_water_difference OR OLD.f_ejection_pump_loss != NEW.f_ejection_pump_loss THEN
     update biomasschp_turbine_auxiliary set 

     f_total_lift=102*((NEW.f_air_ejector_pressure)-(NEW.f_water_tank_pressure))+(NEW.f_water_difference)+(NEW.f_ejection_pump_loss)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_ejection_pump_loss ISNULL OR OLD.f_water_difference ISNULL OR OLD.f_water_tank_pressure ISNULL OR OLD.f_air_ejector_pressure ISNULL) AND NEW.f_ejection_pump_loss NOTNULL AND NEW.f_water_difference NOTNULL AND NEW.f_water_tank_pressure NOTNULL AND NEW.f_air_ejector_pressure NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     f_total_lift=102*((NEW.f_air_ejector_pressure)-(NEW.f_water_tank_pressure))+(NEW.f_water_difference)+(NEW.f_ejection_pump_loss)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_auxiliary_motor_power:配套电机功率,的计算15-----------------------------------
  IF OLD.f_air_ejector_pressure != NEW.f_air_ejector_pressure OR OLD.f_water_tank_pressure != NEW.f_water_tank_pressure OR OLD.f_water_difference != NEW.f_water_difference OR OLD.f_ejection_pump_loss != NEW.f_ejection_pump_loss OR OLD.f_flow_amount != NEW.f_flow_amount OR OLD.f_pump_efficiency != NEW.f_pump_efficiency OR OLD.f_mechanical_transmission_efficiency != NEW.f_mechanical_transmission_efficiency OR OLD.f_motor_efficiency != NEW.f_motor_efficiency OR OLD.f_motor_reserve_coefficient != NEW.f_motor_reserve_coefficient THEN
     update biomasschp_turbine_auxiliary set 

     f_auxiliary_motor_power=(NEW.f_motor_reserve_coefficient)*1000*9.8*(102*((NEW.f_air_ejector_pressure)-(NEW.f_water_tank_pressure))+(NEW.f_water_difference)+(NEW.f_ejection_pump_loss))*1.15*(NEW.f_flow_amount)/3600/1000/(NEW.f_pump_efficiency)/(NEW.f_mechanical_transmission_efficiency)/(NEW.f_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_motor_reserve_coefficient ISNULL OR OLD.f_motor_efficiency ISNULL OR OLD.f_mechanical_transmission_efficiency ISNULL OR OLD.f_pump_efficiency ISNULL OR OLD.f_flow_amount ISNULL OR OLD.f_ejection_pump_loss ISNULL OR OLD.f_water_difference ISNULL OR OLD.f_water_tank_pressure ISNULL OR OLD.f_air_ejector_pressure ISNULL) AND NEW.f_motor_reserve_coefficient NOTNULL AND NEW.f_motor_efficiency NOTNULL AND NEW.f_mechanical_transmission_efficiency NOTNULL AND NEW.f_pump_efficiency NOTNULL AND NEW.f_flow_amount NOTNULL AND NEW.f_ejection_pump_loss NOTNULL AND NEW.f_water_difference NOTNULL AND NEW.f_water_tank_pressure NOTNULL AND NEW.f_air_ejector_pressure NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     f_auxiliary_motor_power=(NEW.f_motor_reserve_coefficient)*1000*9.8*(102*((NEW.f_air_ejector_pressure)-(NEW.f_water_tank_pressure))+(NEW.f_water_difference)+(NEW.f_ejection_pump_loss))*1.15*(NEW.f_flow_amount)/3600/1000/(NEW.f_pump_efficiency)/(NEW.f_mechanical_transmission_efficiency)/(NEW.f_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_total_lift:总扬程,的计算16-----------------------------------
  IF OLD.c_water_tank_pressure != NEW.c_water_tank_pressure OR OLD.c_recirculating_tube_pressure != NEW.c_recirculating_tube_pressure OR OLD.c_water_difference != NEW.c_water_difference OR OLD.c_ejection_pump_loss != NEW.c_ejection_pump_loss THEN
     update biomasschp_turbine_auxiliary set 

     c_total_lift=102*((NEW.c_recirculating_tube_pressure)-(NEW.c_water_tank_pressure))+(NEW.c_water_difference)+(NEW.c_ejection_pump_loss)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_ejection_pump_loss ISNULL OR OLD.c_water_difference ISNULL OR OLD.c_recirculating_tube_pressure ISNULL OR OLD.c_water_tank_pressure ISNULL) AND NEW.c_ejection_pump_loss NOTNULL AND NEW.c_water_difference NOTNULL AND NEW.c_recirculating_tube_pressure NOTNULL AND NEW.c_water_tank_pressure NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     c_total_lift=102*((NEW.c_recirculating_tube_pressure)-(NEW.c_water_tank_pressure))+(NEW.c_water_difference)+(NEW.c_ejection_pump_loss)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_auxiliary_motor_power:配套电机功率,的计算17-----------------------------------
  IF OLD.c_water_tank_pressure != NEW.c_water_tank_pressure OR OLD.c_recirculating_tube_pressure != NEW.c_recirculating_tube_pressure OR OLD.c_water_difference != NEW.c_water_difference OR OLD.c_ejection_pump_loss != NEW.c_ejection_pump_loss OR OLD.c_flow_amount != NEW.c_flow_amount OR OLD.c_pump_efficiency != NEW.c_pump_efficiency OR OLD.c_mechanical_transmission_efficiency != NEW.c_mechanical_transmission_efficiency OR OLD.c_motor_efficiency != NEW.c_motor_efficiency OR OLD.c_motor_reserve_coefficient != NEW.c_motor_reserve_coefficient THEN
     update biomasschp_turbine_auxiliary set 

     c_auxiliary_motor_power=(NEW.c_motor_reserve_coefficient)*1000*9.8*(102*((NEW.c_recirculating_tube_pressure)-(NEW.c_water_tank_pressure))+(NEW.c_water_difference)+(NEW.c_ejection_pump_loss))*1.15*(NEW.c_flow_amount)/3600/1000/(NEW.c_pump_efficiency)/(NEW.c_mechanical_transmission_efficiency)/(NEW.c_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_motor_reserve_coefficient ISNULL OR OLD.c_motor_efficiency ISNULL OR OLD.c_mechanical_transmission_efficiency ISNULL OR OLD.c_pump_efficiency ISNULL OR OLD.c_flow_amount ISNULL OR OLD.c_ejection_pump_loss ISNULL OR OLD.c_water_difference ISNULL OR OLD.c_recirculating_tube_pressure ISNULL OR OLD.c_water_tank_pressure ISNULL) AND NEW.c_motor_reserve_coefficient NOTNULL AND NEW.c_motor_efficiency NOTNULL AND NEW.c_mechanical_transmission_efficiency NOTNULL AND NEW.c_pump_efficiency NOTNULL AND NEW.c_flow_amount NOTNULL AND NEW.c_ejection_pump_loss NOTNULL AND NEW.c_water_difference NOTNULL AND NEW.c_recirculating_tube_pressure NOTNULL AND NEW.c_water_tank_pressure NOTNULL THEN
     update biomasschp_turbine_auxiliary set 

     c_auxiliary_motor_power=(NEW.c_motor_reserve_coefficient)*1000*9.8*(102*((NEW.c_recirculating_tube_pressure)-(NEW.c_water_tank_pressure))+(NEW.c_water_difference)+(NEW.c_ejection_pump_loss))*1.15*(NEW.c_flow_amount)/3600/1000/(NEW.c_pump_efficiency)/(NEW.c_mechanical_transmission_efficiency)/(NEW.c_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "biomasschp_turbine_auxiliary" AFTER UPDATE OF
"w_mechanical_transmission_efficiency",
"w_motor_efficiency",
"w_motor_reserve_coefficient",
"m_condensate_amount",
"m_steam_enthalpy",
"w_deaerator_working_pressure",
"m_cooling_water_inlet_temperature",
"m_saturation_temperature",
"m_supercooling",
"m_condensate_enthalpy",
"m_cooling_pipe_coefficient",
"m_correction_coefficient",
"m_cooling_flow",
"m_cooling_type",
"w_deaerator_difference",
"m_correction_condensers",
"m_flow_count",
"m_consideration_change",
"m_cycle_ratio",
"w_deaerator_need_pressure",
"f_air_ejector_pressure",
"f_water_tank_pressure",
"f_water_difference",
"f_ejection_pump_loss",
"f_flow_amount",
"w_condenser_higter",
"f_pump_efficiency",
"f_mechanical_transmission_efficiency",
"f_motor_efficiency",
"f_motor_reserve_coefficient",
"c_water_tank_pressure",
"c_recirculating_tube_pressure",
"c_water_difference",
"w_hot_well_resistance",
"c_ejection_pump_loss",
"c_flow_amount",
"c_pump_efficiency",
"c_mechanical_transmission_efficiency",
"c_motor_efficiency",
"c_motor_reserve_coefficient",
"w_flow_amount",
"w_pump_efficiency"
ON "public"."biomasschp_turbine_auxiliary"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_turbine_backpressure的w_deaerator_working_pressure字段，和表biomasschp_turbine_auxiliary的d_work_pressure字段，即：biomasschp_turbine_auxiliary.w_deaerator_working_pressure=biomasschp_turbine_backpressure.d_work_pressure
CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary_w_deaerator_working_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_auxiliary set w_deaerator_working_pressure=biomasschp_turbine_backpressure.d_work_pressure
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_turbine_auxiliary.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_turbine_backpressure的w_condenser_higter字段，和表biomasschp_turbine_auxiliary的e_steam_exhaust_pressure字段，即：biomasschp_turbine_auxiliary.w_condenser_higter=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary_w_condenser_higter()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_auxiliary set w_condenser_higter=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_turbine_auxiliary.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_turbine_backpressure的m_condenser_pressure字段，和表biomasschp_turbine_auxiliary的e_steam_exhaust_pressure字段，即：biomasschp_turbine_auxiliary.m_condenser_pressure=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary_m_condenser_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_auxiliary set m_condenser_pressure=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_turbine_auxiliary.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_turbine_backpressure的m_steam_enthalpy字段，和表biomasschp_turbine_auxiliary的i_steam_exhaust_enthalpy_actual字段，即：biomasschp_turbine_auxiliary.m_steam_enthalpy=biomasschp_turbine_backpressure.i_steam_exhaust_enthalpy_actual
CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary_m_steam_enthalpy()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_auxiliary set m_steam_enthalpy=biomasschp_turbine_backpressure.i_steam_exhaust_enthalpy_actual
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_turbine_auxiliary.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当d_work_pressure有更新时触发biomasschp_turbine_auxiliary.w_deaerator_working_pressure=biomasschp_turbine_backpressure.d_work_pressure
CREATE TRIGGER "biomasschp_turbine_backpressure_a_0" AFTER UPDATE OF "d_work_pressure" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary_w_deaerator_working_pressure"();


--该触发器用于：当e_steam_exhaust_pressure有更新时触发biomasschp_turbine_auxiliary.w_condenser_higter=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
CREATE TRIGGER "biomasschp_turbine_backpressure_a_1" AFTER UPDATE OF "e_steam_exhaust_pressure" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary_w_condenser_higter"();


--该触发器用于：当e_steam_exhaust_pressure有更新时触发biomasschp_turbine_auxiliary.m_condenser_pressure=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
CREATE TRIGGER "biomasschp_turbine_backpressure_a_2" AFTER UPDATE OF "e_steam_exhaust_pressure" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary_m_condenser_pressure"();


--该触发器用于：当i_steam_exhaust_enthalpy_actual有更新时触发biomasschp_turbine_auxiliary.m_steam_enthalpy=biomasschp_turbine_backpressure.i_steam_exhaust_enthalpy_actual
CREATE TRIGGER "biomasschp_turbine_backpressure_a_3" AFTER UPDATE OF "i_steam_exhaust_enthalpy_actual" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary_m_steam_enthalpy"();


