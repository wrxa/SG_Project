CREATE OR REPLACE FUNCTION gaspowergeneration_circulating_water_system()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段steam_exhaust_flux_summer:夏季乏汽流量,的计算1-----------------------------------
  IF OLD.steam_exhaust_flux_winter != NEW.steam_exhaust_flux_winter THEN
     update gaspowergeneration_circulating_water_system set 

     steam_exhaust_flux_summer=(NEW.steam_exhaust_flux_winter)+10
     where plan_id=NEW.plan_id;

  ELSIF (OLD.steam_exhaust_flux_winter ISNULL) AND NEW.steam_exhaust_flux_winter NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     steam_exhaust_flux_summer=(NEW.steam_exhaust_flux_winter)+10
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段circulation_water_flow_winter:循环水量冬季,的计算2-----------------------------------
  IF OLD.steam_exhaust_flux_selected != NEW.steam_exhaust_flux_selected OR OLD.circulation_ratio_winter != NEW.circulation_ratio_winter THEN
     update gaspowergeneration_circulating_water_system set 

     circulation_water_flow_winter=(NEW.steam_exhaust_flux_selected)*(NEW.circulation_ratio_winter)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulation_ratio_winter ISNULL OR OLD.steam_exhaust_flux_selected ISNULL) AND NEW.circulation_ratio_winter NOTNULL AND NEW.steam_exhaust_flux_selected NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     circulation_water_flow_winter=(NEW.steam_exhaust_flux_selected)*(NEW.circulation_ratio_winter)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段circulation_water_flow_summer:循环水量夏季,的计算3-----------------------------------
  IF OLD.steam_exhaust_flux_selected != NEW.steam_exhaust_flux_selected OR OLD.circulation_ratio_summer != NEW.circulation_ratio_summer THEN
     update gaspowergeneration_circulating_water_system set 

     circulation_water_flow_summer=(NEW.steam_exhaust_flux_selected)*(NEW.circulation_ratio_summer)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulation_ratio_summer ISNULL OR OLD.steam_exhaust_flux_selected ISNULL) AND NEW.circulation_ratio_summer NOTNULL AND NEW.steam_exhaust_flux_selected NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     circulation_water_flow_summer=(NEW.steam_exhaust_flux_selected)*(NEW.circulation_ratio_summer)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段total_circulation_water_flow_winter:总循环水量冬季,的计算4-----------------------------------
  IF OLD.auxiliary_cooling_water_flow_winter != NEW.auxiliary_cooling_water_flow_winter OR OLD.steam_exhaust_flux_selected != NEW.steam_exhaust_flux_selected OR OLD.circulation_ratio_winter != NEW.circulation_ratio_winter THEN
     update gaspowergeneration_circulating_water_system set 

     total_circulation_water_flow_winter=((NEW.steam_exhaust_flux_selected)*(NEW.circulation_ratio_winter))+(NEW.auxiliary_cooling_water_flow_winter)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.auxiliary_cooling_water_flow_winter ISNULL OR OLD.circulation_ratio_winter ISNULL OR OLD.steam_exhaust_flux_selected ISNULL) AND NEW.auxiliary_cooling_water_flow_winter NOTNULL AND NEW.circulation_ratio_winter NOTNULL AND NEW.steam_exhaust_flux_selected NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     total_circulation_water_flow_winter=((NEW.steam_exhaust_flux_selected)*(NEW.circulation_ratio_winter))+(NEW.auxiliary_cooling_water_flow_winter)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段total_circulation_water_flow_summer:总循环水量夏季,的计算5-----------------------------------
  IF OLD.auxiliary_cooling_water_flow_summer != NEW.auxiliary_cooling_water_flow_summer OR OLD.steam_exhaust_flux_selected != NEW.steam_exhaust_flux_selected OR OLD.circulation_ratio_summer != NEW.circulation_ratio_summer THEN
     update gaspowergeneration_circulating_water_system set 

     total_circulation_water_flow_summer=((NEW.steam_exhaust_flux_selected)*(NEW.circulation_ratio_summer))+(NEW.auxiliary_cooling_water_flow_summer)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.auxiliary_cooling_water_flow_summer ISNULL OR OLD.circulation_ratio_summer ISNULL OR OLD.steam_exhaust_flux_selected ISNULL) AND NEW.auxiliary_cooling_water_flow_summer NOTNULL AND NEW.circulation_ratio_summer NOTNULL AND NEW.steam_exhaust_flux_selected NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     total_circulation_water_flow_summer=((NEW.steam_exhaust_flux_selected)*(NEW.circulation_ratio_summer))+(NEW.auxiliary_cooling_water_flow_summer)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段spray_area:喷淋面积,的计算6-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow OR OLD.spray_density != NEW.spray_density THEN
     update gaspowergeneration_circulating_water_system set 

     spray_area=(NEW.selected_total_circulation_water_flow)/(NEW.spray_density)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.spray_density ISNULL OR OLD.selected_total_circulation_water_flow ISNULL) AND NEW.spray_density NOTNULL AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     spray_area=(NEW.selected_total_circulation_water_flow)/(NEW.spray_density)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段evaporation_loss_rate:蒸发损失率,的计算7-----------------------------------
  IF OLD.in_out_water_temperature_difference != NEW.in_out_water_temperature_difference OR OLD.dry_bulb_k_coefficient != NEW.dry_bulb_k_coefficient THEN
     update gaspowergeneration_circulating_water_system set 

     evaporation_loss_rate=(NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.dry_bulb_k_coefficient ISNULL OR OLD.in_out_water_temperature_difference ISNULL) AND NEW.dry_bulb_k_coefficient NOTNULL AND NEW.in_out_water_temperature_difference NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     evaporation_loss_rate=(NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段evaporation_loss:蒸发损失,的计算8-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow OR OLD.in_out_water_temperature_difference != NEW.in_out_water_temperature_difference OR OLD.dry_bulb_k_coefficient != NEW.dry_bulb_k_coefficient THEN
     update gaspowergeneration_circulating_water_system set 

     evaporation_loss=((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))*(NEW.selected_total_circulation_water_flow)/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.dry_bulb_k_coefficient ISNULL OR OLD.in_out_water_temperature_difference ISNULL OR OLD.selected_total_circulation_water_flow ISNULL) AND NEW.dry_bulb_k_coefficient NOTNULL AND NEW.in_out_water_temperature_difference NOTNULL AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     evaporation_loss=((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))*(NEW.selected_total_circulation_water_flow)/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段wind_blow_loss:风吹损失,的计算9-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow OR OLD.wind_blow_loss_rate != NEW.wind_blow_loss_rate THEN
     update gaspowergeneration_circulating_water_system set 

     wind_blow_loss=(NEW.wind_blow_loss_rate)*(NEW.selected_total_circulation_water_flow)/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.wind_blow_loss_rate ISNULL OR OLD.selected_total_circulation_water_flow ISNULL) AND NEW.wind_blow_loss_rate NOTNULL AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     wind_blow_loss=(NEW.wind_blow_loss_rate)*(NEW.selected_total_circulation_water_flow)/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段discharge_rate:排污损失率,的计算10-----------------------------------
  IF OLD.in_out_water_temperature_difference != NEW.in_out_water_temperature_difference OR OLD.dry_bulb_k_coefficient != NEW.dry_bulb_k_coefficient OR OLD.wind_blow_loss_rate != NEW.wind_blow_loss_rate OR OLD.concentration_rate != NEW.concentration_rate THEN
     update gaspowergeneration_circulating_water_system set 

     discharge_rate=(((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))-(NEW.wind_blow_loss_rate)*((NEW.concentration_rate)-1))/((NEW.concentration_rate)-1)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.concentration_rate ISNULL OR OLD.wind_blow_loss_rate ISNULL OR OLD.dry_bulb_k_coefficient ISNULL OR OLD.in_out_water_temperature_difference ISNULL) AND NEW.concentration_rate NOTNULL AND NEW.wind_blow_loss_rate NOTNULL AND NEW.dry_bulb_k_coefficient NOTNULL AND NEW.in_out_water_temperature_difference NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     discharge_rate=(((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))-(NEW.wind_blow_loss_rate)*((NEW.concentration_rate)-1))/((NEW.concentration_rate)-1)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段discharge_capacity:排污量,的计算11-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow OR OLD.in_out_water_temperature_difference != NEW.in_out_water_temperature_difference OR OLD.dry_bulb_k_coefficient != NEW.dry_bulb_k_coefficient OR OLD.wind_blow_loss_rate != NEW.wind_blow_loss_rate OR OLD.concentration_rate != NEW.concentration_rate THEN
     update gaspowergeneration_circulating_water_system set 

     discharge_capacity=((((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))-(NEW.wind_blow_loss_rate)*((NEW.concentration_rate)-1))/((NEW.concentration_rate)-1))*(NEW.selected_total_circulation_water_flow)/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.concentration_rate ISNULL OR OLD.wind_blow_loss_rate ISNULL OR OLD.dry_bulb_k_coefficient ISNULL OR OLD.in_out_water_temperature_difference ISNULL OR OLD.selected_total_circulation_water_flow ISNULL) AND NEW.concentration_rate NOTNULL AND NEW.wind_blow_loss_rate NOTNULL AND NEW.dry_bulb_k_coefficient NOTNULL AND NEW.in_out_water_temperature_difference NOTNULL AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     discharge_capacity=((((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))-(NEW.wind_blow_loss_rate)*((NEW.concentration_rate)-1))/((NEW.concentration_rate)-1))*(NEW.selected_total_circulation_water_flow)/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段supply_water_amount:补充水量,的计算12-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow OR OLD.in_out_water_temperature_difference != NEW.in_out_water_temperature_difference OR OLD.dry_bulb_k_coefficient != NEW.dry_bulb_k_coefficient OR OLD.wind_blow_loss_rate != NEW.wind_blow_loss_rate OR OLD.concentration_rate != NEW.concentration_rate THEN
     update gaspowergeneration_circulating_water_system set 

     supply_water_amount=(((((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))-(NEW.wind_blow_loss_rate)*((NEW.concentration_rate)-1))/((NEW.concentration_rate)-1))*(NEW.selected_total_circulation_water_flow)/100)+((NEW.wind_blow_loss_rate)*(NEW.selected_total_circulation_water_flow)/100)+(((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))*(NEW.selected_total_circulation_water_flow)/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.concentration_rate ISNULL OR OLD.wind_blow_loss_rate ISNULL OR OLD.dry_bulb_k_coefficient ISNULL OR OLD.in_out_water_temperature_difference ISNULL OR OLD.selected_total_circulation_water_flow ISNULL) AND NEW.concentration_rate NOTNULL AND NEW.wind_blow_loss_rate NOTNULL AND NEW.dry_bulb_k_coefficient NOTNULL AND NEW.in_out_water_temperature_difference NOTNULL AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     supply_water_amount=(((((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))-(NEW.wind_blow_loss_rate)*((NEW.concentration_rate)-1))/((NEW.concentration_rate)-1))*(NEW.selected_total_circulation_water_flow)/100)+((NEW.wind_blow_loss_rate)*(NEW.selected_total_circulation_water_flow)/100)+(((NEW.dry_bulb_k_coefficient)*(NEW.in_out_water_temperature_difference))*(NEW.selected_total_circulation_water_flow)/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段circulating_pool_water_amount:循环水池15-25分钟循环水量,的计算13-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow THEN
     update gaspowergeneration_circulating_water_system set 

     circulating_pool_water_amount=(NEW.selected_total_circulation_water_flow)/60*15
     where plan_id=NEW.plan_id;

  ELSIF (OLD.selected_total_circulation_water_flow ISNULL) AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     circulating_pool_water_amount=(NEW.selected_total_circulation_water_flow)/60*15
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段circulating_pool_size_checked:校核循环水池尺寸,的计算14-----------------------------------
  IF OLD.circulating_pool_size_deep != NEW.circulating_pool_size_deep OR OLD.circulating_pool_size_length != NEW.circulating_pool_size_length OR OLD.circulating_pool_size_width != NEW.circulating_pool_size_width THEN
     update gaspowergeneration_circulating_water_system set 

     circulating_pool_size_checked=(NEW.circulating_pool_size_deep)*(NEW.circulating_pool_size_length)*(NEW.circulating_pool_size_width)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulating_pool_size_width ISNULL OR OLD.circulating_pool_size_length ISNULL OR OLD.circulating_pool_size_deep ISNULL) AND NEW.circulating_pool_size_width NOTNULL AND NEW.circulating_pool_size_length NOTNULL AND NEW.circulating_pool_size_deep NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     circulating_pool_size_checked=(NEW.circulating_pool_size_deep)*(NEW.circulating_pool_size_length)*(NEW.circulating_pool_size_width)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段condenser_circulating_water_inlet_pressure:凝汽器循环水进水工作压力,的计算15-----------------------------------
  IF OLD.condenser_friction != NEW.condenser_friction OR OLD.circulating_backwater_pressure != NEW.circulating_backwater_pressure THEN
     update gaspowergeneration_circulating_water_system set 

     condenser_circulating_water_inlet_pressure=(NEW.circulating_backwater_pressure)+(NEW.condenser_friction)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.circulating_backwater_pressure ISNULL OR OLD.condenser_friction ISNULL) AND NEW.circulating_backwater_pressure NOTNULL AND NEW.condenser_friction NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     condenser_circulating_water_inlet_pressure=(NEW.circulating_backwater_pressure)+(NEW.condenser_friction)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段total_pumping_lift:总扬程,的计算16-----------------------------------
  IF OLD.condenser_friction != NEW.condenser_friction OR OLD.circulating_backwater_pressure != NEW.circulating_backwater_pressure OR OLD.circulating_water_reservoir_pressure != NEW.circulating_water_reservoir_pressure OR OLD.circulation_pump_outlet_to_condenser_inlet_height_difference != NEW.circulation_pump_outlet_to_condenser_inlet_height_difference OR OLD.reservoir_to_pump_inlet_height_difference != NEW.reservoir_to_pump_inlet_height_difference OR OLD.pipe_loss != NEW.pipe_loss OR OLD.y_filter_loss != NEW.y_filter_loss THEN
     update gaspowergeneration_circulating_water_system set 

     total_pumping_lift=102*(((NEW.circulating_backwater_pressure)+(NEW.condenser_friction))-(NEW.circulating_water_reservoir_pressure))+(NEW.circulation_pump_outlet_to_condenser_inlet_height_difference)-(NEW.reservoir_to_pump_inlet_height_difference)+((NEW.pipe_loss)+(NEW.y_filter_loss))*1.2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.y_filter_loss ISNULL OR OLD.pipe_loss ISNULL OR OLD.reservoir_to_pump_inlet_height_difference ISNULL OR OLD.circulation_pump_outlet_to_condenser_inlet_height_difference ISNULL OR OLD.circulating_water_reservoir_pressure ISNULL OR OLD.circulating_backwater_pressure ISNULL OR OLD.condenser_friction ISNULL) AND NEW.y_filter_loss NOTNULL AND NEW.pipe_loss NOTNULL AND NEW.reservoir_to_pump_inlet_height_difference NOTNULL AND NEW.circulation_pump_outlet_to_condenser_inlet_height_difference NOTNULL AND NEW.circulating_water_reservoir_pressure NOTNULL AND NEW.circulating_backwater_pressure NOTNULL AND NEW.condenser_friction NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     total_pumping_lift=102*(((NEW.circulating_backwater_pressure)+(NEW.condenser_friction))-(NEW.circulating_water_reservoir_pressure))+(NEW.circulation_pump_outlet_to_condenser_inlet_height_difference)-(NEW.reservoir_to_pump_inlet_height_difference)+((NEW.pipe_loss)+(NEW.y_filter_loss))*1.2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_flow:流量,的计算17-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow THEN
     update gaspowergeneration_circulating_water_system set 

     pump_flow=(NEW.selected_total_circulation_water_flow)/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.selected_total_circulation_water_flow ISNULL) AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     pump_flow=(NEW.selected_total_circulation_water_flow)/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_matching_motor_power:配套电机功率,的计算18-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow OR OLD.condenser_friction != NEW.condenser_friction OR OLD.circulating_backwater_pressure != NEW.circulating_backwater_pressure OR OLD.circulating_water_reservoir_pressure != NEW.circulating_water_reservoir_pressure OR OLD.circulation_pump_outlet_to_condenser_inlet_height_difference != NEW.circulation_pump_outlet_to_condenser_inlet_height_difference OR OLD.reservoir_to_pump_inlet_height_difference != NEW.reservoir_to_pump_inlet_height_difference OR OLD.pipe_loss != NEW.pipe_loss OR OLD.y_filter_loss != NEW.y_filter_loss OR OLD.pump_efficiency != NEW.pump_efficiency OR OLD.pump_transmission_efficiency != NEW.pump_transmission_efficiency OR OLD.pump_motor_efficiency != NEW.pump_motor_efficiency OR OLD.pump_motor_spare_coefficient != NEW.pump_motor_spare_coefficient THEN
     update gaspowergeneration_circulating_water_system set 

     pump_matching_motor_power=(NEW.pump_motor_spare_coefficient)*1000*9.8*(102*(((NEW.circulating_backwater_pressure)+(NEW.condenser_friction))-(NEW.circulating_water_reservoir_pressure))+(NEW.circulation_pump_outlet_to_condenser_inlet_height_difference)-(NEW.reservoir_to_pump_inlet_height_difference)+((NEW.pipe_loss)+(NEW.y_filter_loss))*1.2)*((NEW.selected_total_circulation_water_flow)/2)/3600/1000/(NEW.pump_efficiency)/(NEW.pump_transmission_efficiency)/(NEW.pump_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_motor_spare_coefficient ISNULL OR OLD.pump_motor_efficiency ISNULL OR OLD.pump_transmission_efficiency ISNULL OR OLD.pump_efficiency ISNULL OR OLD.y_filter_loss ISNULL OR OLD.pipe_loss ISNULL OR OLD.reservoir_to_pump_inlet_height_difference ISNULL OR OLD.circulation_pump_outlet_to_condenser_inlet_height_difference ISNULL OR OLD.circulating_water_reservoir_pressure ISNULL OR OLD.circulating_backwater_pressure ISNULL OR OLD.condenser_friction ISNULL OR OLD.selected_total_circulation_water_flow ISNULL) AND NEW.pump_motor_spare_coefficient NOTNULL AND NEW.pump_motor_efficiency NOTNULL AND NEW.pump_transmission_efficiency NOTNULL AND NEW.pump_efficiency NOTNULL AND NEW.y_filter_loss NOTNULL AND NEW.pipe_loss NOTNULL AND NEW.reservoir_to_pump_inlet_height_difference NOTNULL AND NEW.circulation_pump_outlet_to_condenser_inlet_height_difference NOTNULL AND NEW.circulating_water_reservoir_pressure NOTNULL AND NEW.circulating_backwater_pressure NOTNULL AND NEW.condenser_friction NOTNULL AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     pump_matching_motor_power=(NEW.pump_motor_spare_coefficient)*1000*9.8*(102*(((NEW.circulating_backwater_pressure)+(NEW.condenser_friction))-(NEW.circulating_water_reservoir_pressure))+(NEW.circulation_pump_outlet_to_condenser_inlet_height_difference)-(NEW.reservoir_to_pump_inlet_height_difference)+((NEW.pipe_loss)+(NEW.y_filter_loss))*1.2)*((NEW.selected_total_circulation_water_flow)/2)/3600/1000/(NEW.pump_efficiency)/(NEW.pump_transmission_efficiency)/(NEW.pump_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段selected_pump_model_power:选用型号-功率,的计算19-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow OR OLD.condenser_friction != NEW.condenser_friction OR OLD.circulating_backwater_pressure != NEW.circulating_backwater_pressure OR OLD.circulating_water_reservoir_pressure != NEW.circulating_water_reservoir_pressure OR OLD.circulation_pump_outlet_to_condenser_inlet_height_difference != NEW.circulation_pump_outlet_to_condenser_inlet_height_difference OR OLD.reservoir_to_pump_inlet_height_difference != NEW.reservoir_to_pump_inlet_height_difference OR OLD.pipe_loss != NEW.pipe_loss OR OLD.y_filter_loss != NEW.y_filter_loss OR OLD.pump_efficiency != NEW.pump_efficiency OR OLD.pump_transmission_efficiency != NEW.pump_transmission_efficiency OR OLD.pump_motor_efficiency != NEW.pump_motor_efficiency OR OLD.pump_motor_spare_coefficient != NEW.pump_motor_spare_coefficient THEN
     update gaspowergeneration_circulating_water_system set 

     selected_pump_model_power=((NEW.pump_motor_spare_coefficient)*1000*9.8*(102*(((NEW.circulating_backwater_pressure)+(NEW.condenser_friction))-(NEW.circulating_water_reservoir_pressure))+(NEW.circulation_pump_outlet_to_condenser_inlet_height_difference)-(NEW.reservoir_to_pump_inlet_height_difference)+((NEW.pipe_loss)+(NEW.y_filter_loss))*1.2)*((NEW.selected_total_circulation_water_flow)/2)/3600/1000/(NEW.pump_efficiency)/(NEW.pump_transmission_efficiency)/(NEW.pump_motor_efficiency))/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_motor_spare_coefficient ISNULL OR OLD.pump_motor_efficiency ISNULL OR OLD.pump_transmission_efficiency ISNULL OR OLD.pump_efficiency ISNULL OR OLD.y_filter_loss ISNULL OR OLD.pipe_loss ISNULL OR OLD.reservoir_to_pump_inlet_height_difference ISNULL OR OLD.circulation_pump_outlet_to_condenser_inlet_height_difference ISNULL OR OLD.circulating_water_reservoir_pressure ISNULL OR OLD.circulating_backwater_pressure ISNULL OR OLD.condenser_friction ISNULL OR OLD.selected_total_circulation_water_flow ISNULL) AND NEW.pump_motor_spare_coefficient NOTNULL AND NEW.pump_motor_efficiency NOTNULL AND NEW.pump_transmission_efficiency NOTNULL AND NEW.pump_efficiency NOTNULL AND NEW.y_filter_loss NOTNULL AND NEW.pipe_loss NOTNULL AND NEW.reservoir_to_pump_inlet_height_difference NOTNULL AND NEW.circulation_pump_outlet_to_condenser_inlet_height_difference NOTNULL AND NEW.circulating_water_reservoir_pressure NOTNULL AND NEW.circulating_backwater_pressure NOTNULL AND NEW.condenser_friction NOTNULL AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     selected_pump_model_power=((NEW.pump_motor_spare_coefficient)*1000*9.8*(102*(((NEW.circulating_backwater_pressure)+(NEW.condenser_friction))-(NEW.circulating_water_reservoir_pressure))+(NEW.circulation_pump_outlet_to_condenser_inlet_height_difference)-(NEW.reservoir_to_pump_inlet_height_difference)+((NEW.pipe_loss)+(NEW.y_filter_loss))*1.2)*((NEW.selected_total_circulation_water_flow)/2)/3600/1000/(NEW.pump_efficiency)/(NEW.pump_transmission_efficiency)/(NEW.pump_motor_efficiency))/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段selected_pump_model_flow:选用型号-流量,的计算20-----------------------------------
  IF OLD.selected_total_circulation_water_flow != NEW.selected_total_circulation_water_flow THEN
     update gaspowergeneration_circulating_water_system set 

     selected_pump_model_flow=((NEW.selected_total_circulation_water_flow)/2)/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.selected_total_circulation_water_flow ISNULL) AND NEW.selected_total_circulation_water_flow NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     selected_pump_model_flow=((NEW.selected_total_circulation_water_flow)/2)/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段selected_pump_model_lift:选用型号-扬程,的计算21-----------------------------------
  IF OLD.condenser_friction != NEW.condenser_friction OR OLD.circulating_backwater_pressure != NEW.circulating_backwater_pressure OR OLD.circulating_water_reservoir_pressure != NEW.circulating_water_reservoir_pressure OR OLD.circulation_pump_outlet_to_condenser_inlet_height_difference != NEW.circulation_pump_outlet_to_condenser_inlet_height_difference OR OLD.reservoir_to_pump_inlet_height_difference != NEW.reservoir_to_pump_inlet_height_difference OR OLD.pipe_loss != NEW.pipe_loss OR OLD.y_filter_loss != NEW.y_filter_loss THEN
     update gaspowergeneration_circulating_water_system set 

     selected_pump_model_lift=(102*(((NEW.circulating_backwater_pressure)+(NEW.condenser_friction))-(NEW.circulating_water_reservoir_pressure))+(NEW.circulation_pump_outlet_to_condenser_inlet_height_difference)-(NEW.reservoir_to_pump_inlet_height_difference)+((NEW.pipe_loss)+(NEW.y_filter_loss))*1.2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.y_filter_loss ISNULL OR OLD.pipe_loss ISNULL OR OLD.reservoir_to_pump_inlet_height_difference ISNULL OR OLD.circulation_pump_outlet_to_condenser_inlet_height_difference ISNULL OR OLD.circulating_water_reservoir_pressure ISNULL OR OLD.circulating_backwater_pressure ISNULL OR OLD.condenser_friction ISNULL) AND NEW.y_filter_loss NOTNULL AND NEW.pipe_loss NOTNULL AND NEW.reservoir_to_pump_inlet_height_difference NOTNULL AND NEW.circulation_pump_outlet_to_condenser_inlet_height_difference NOTNULL AND NEW.circulating_water_reservoir_pressure NOTNULL AND NEW.circulating_backwater_pressure NOTNULL AND NEW.condenser_friction NOTNULL THEN
     update gaspowergeneration_circulating_water_system set 

     selected_pump_model_lift=(102*(((NEW.circulating_backwater_pressure)+(NEW.condenser_friction))-(NEW.circulating_water_reservoir_pressure))+(NEW.circulation_pump_outlet_to_condenser_inlet_height_difference)-(NEW.reservoir_to_pump_inlet_height_difference)+((NEW.pipe_loss)+(NEW.y_filter_loss))*1.2)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_circulating_water_system" AFTER UPDATE OF
"auxiliary_cooling_water_flow_winter",
"auxiliary_cooling_water_flow_summer",
"selected_total_circulation_water_flow",
"spray_density",
"in_out_water_temperature_difference",
"dry_bulb_k_coefficient",
"wind_blow_loss_rate",
"concentration_rate",
"circulating_pool_size_deep",
"steam_exhaust_flux_winter",
"circulating_pool_size_length",
"circulating_pool_size_width",
"condenser_friction",
"circulating_backwater_pressure",
"circulating_water_reservoir_pressure",
"circulation_pump_outlet_to_condenser_inlet_height_difference",
"reservoir_to_pump_inlet_height_difference",
"pipe_loss",
"y_filter_loss",
"pump_efficiency",
"pump_transmission_efficiency",
"pump_motor_efficiency",
"pump_motor_spare_coefficient",
"steam_exhaust_flux_selected",
"circulation_ratio_winter",
"circulation_ratio_summer"
ON "public"."gaspowergeneration_circulating_water_system"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_circulating_water_system"();

