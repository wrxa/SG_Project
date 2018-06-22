CREATE OR REPLACE FUNCTION ccpp_ccpp_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段high_engine_exhaust_gas_temperature:燃机排烟温度,的计算1-----------------------------------
  IF OLD.engine_exhaust_gas_temperature_check != NEW.engine_exhaust_gas_temperature_check THEN
     update ccpp_ccpp set 

     high_engine_exhaust_gas_temperature_check=NEW.engine_exhaust_gas_temperature_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.engine_exhaust_gas_temperature_check ISNULL) AND NEW.engine_exhaust_gas_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     high_engine_exhaust_gas_temperature_check=NEW.engine_exhaust_gas_temperature_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_steam_temperature:主蒸汽温度,的计算2-----------------------------------
  IF OLD.engine_exhaust_gas_temperature_check != NEW.engine_exhaust_gas_temperature_check OR OLD.high_terminal_temperature_difference_check != NEW.high_terminal_temperature_difference_check THEN
     update ccpp_ccpp set 

     high_steam_temperature_check=(NEW.engine_exhaust_gas_temperature_check)-NEW.high_terminal_temperature_difference_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_terminal_temperature_difference_check ISNULL OR OLD.engine_exhaust_gas_temperature_check ISNULL) AND NEW.high_terminal_temperature_difference_check NOTNULL AND NEW.engine_exhaust_gas_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     high_steam_temperature_check=(NEW.engine_exhaust_gas_temperature_check)-NEW.high_terminal_temperature_difference_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_drum_pressure:高压汽包压力,的计算3-----------------------------------
  IF OLD.high_steam_pressure_check != NEW.high_steam_pressure_check THEN
     update ccpp_ccpp set 

     high_drum_pressure_check=NEW.high_steam_pressure_check*1.05
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_steam_pressure_check ISNULL) AND NEW.high_steam_pressure_check NOTNULL THEN
     update ccpp_ccpp set 

     high_drum_pressure_check=NEW.high_steam_pressure_check*1.05
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_evaporator_influent_water_temperature:高压进蒸发器热水温度,的计算4-----------------------------------
  IF OLD.high_evaporating_temperature_check != NEW.high_evaporating_temperature_check OR OLD.high_node_temperature_check != NEW.high_node_temperature_check THEN
     update ccpp_ccpp set 

     high_evaporator_influent_water_temperature_check=NEW.high_evaporating_temperature_check-NEW.high_node_temperature_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_node_temperature_check ISNULL OR OLD.high_evaporating_temperature_check ISNULL) AND NEW.high_node_temperature_check NOTNULL AND NEW.high_evaporating_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     high_evaporator_influent_water_temperature_check=NEW.high_evaporating_temperature_check-NEW.high_node_temperature_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_evaporator_effluent_smoke_temperature:高压出蒸发器烟气温度,的计算5-----------------------------------
  IF OLD.high_evaporating_temperature_check != NEW.high_evaporating_temperature_check OR OLD.high_node_temperature_check != NEW.high_node_temperature_check OR OLD.high_proximity_temperature_difference_check != NEW.high_proximity_temperature_difference_check THEN
     update ccpp_ccpp set 

     high_evaporator_effluent_smoke_temperature_check=(NEW.high_evaporating_temperature_check-NEW.high_node_temperature_check)+NEW.high_proximity_temperature_difference_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_proximity_temperature_difference_check ISNULL OR OLD.high_node_temperature_check ISNULL OR OLD.high_evaporating_temperature_check ISNULL) AND NEW.high_proximity_temperature_difference_check NOTNULL AND NEW.high_node_temperature_check NOTNULL AND NEW.high_evaporating_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     high_evaporator_effluent_smoke_temperature_check=(NEW.high_evaporating_temperature_check-NEW.high_node_temperature_check)+NEW.high_proximity_temperature_difference_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_economizer_effluent_smoke_enthalpy:高压出省煤器烟气焓值,的计算6-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_check != NEW.high_engine_exhaust_gas_flux_check OR OLD.high_engine_exhaust_gas_energy_check != NEW.high_engine_exhaust_gas_energy_check OR OLD.high_boiler_efficiency_check != NEW.high_boiler_efficiency_check OR OLD.high_steam_enthalpy_check != NEW.high_steam_enthalpy_check OR OLD.high_evaporator_influent_water_enthalpy_check != NEW.high_evaporator_influent_water_enthalpy_check OR OLD.high_evaporator_effluent_smoke_enthalpy_check != NEW.high_evaporator_effluent_smoke_enthalpy_check OR OLD.high_economizer_influent_water_temperature_check != NEW.high_economizer_influent_water_temperature_check OR OLD.high_blowdown_rate_check != NEW.high_blowdown_rate_check THEN
     update ccpp_ccpp set 

     high_economizer_effluent_smoke_enthalpy_check=NEW.high_evaporator_effluent_smoke_enthalpy_check-((NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*(1+NEW.high_blowdown_rate_check))*(NEW.high_evaporator_influent_water_enthalpy_check-NEW.high_economizer_influent_water_temperature_check)*1000/NEW.high_boiler_efficiency_check/NEW.high_engine_exhaust_gas_flux_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_blowdown_rate_check ISNULL OR OLD.high_economizer_influent_water_temperature_check ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.high_evaporator_influent_water_enthalpy_check ISNULL OR OLD.high_steam_enthalpy_check ISNULL OR OLD.high_boiler_efficiency_check ISNULL OR OLD.high_engine_exhaust_gas_energy_check ISNULL OR OLD.high_engine_exhaust_gas_flux_check ISNULL) AND NEW.high_blowdown_rate_check NOTNULL AND NEW.high_economizer_influent_water_temperature_check NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.high_steam_enthalpy_check NOTNULL AND NEW.high_boiler_efficiency_check NOTNULL AND NEW.high_engine_exhaust_gas_energy_check NOTNULL AND NEW.high_engine_exhaust_gas_flux_check NOTNULL THEN
     update ccpp_ccpp set 

     high_economizer_effluent_smoke_enthalpy_check=NEW.high_evaporator_effluent_smoke_enthalpy_check-((NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*(1+NEW.high_blowdown_rate_check))*(NEW.high_evaporator_influent_water_enthalpy_check-NEW.high_economizer_influent_water_temperature_check)*1000/NEW.high_boiler_efficiency_check/NEW.high_engine_exhaust_gas_flux_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_economizer_influent_water_enthalpy:高压进省煤器热水焓值,的计算7-----------------------------------
  IF OLD.low_evaporat_temperature_check != NEW.low_evaporat_temperature_check THEN
     update ccpp_ccpp set 

     high_economizer_influent_water_enthalpy_check=NEW.low_evaporat_temperature_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_evaporat_temperature_check ISNULL) AND NEW.low_evaporat_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     high_economizer_influent_water_enthalpy_check=NEW.low_evaporat_temperature_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_gas_production:高压产汽量,的计算8-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_check != NEW.high_engine_exhaust_gas_flux_check OR OLD.high_engine_exhaust_gas_energy_check != NEW.high_engine_exhaust_gas_energy_check OR OLD.high_boiler_efficiency_check != NEW.high_boiler_efficiency_check OR OLD.high_steam_enthalpy_check != NEW.high_steam_enthalpy_check OR OLD.high_evaporator_influent_water_enthalpy_check != NEW.high_evaporator_influent_water_enthalpy_check OR OLD.high_evaporator_effluent_smoke_enthalpy_check != NEW.high_evaporator_effluent_smoke_enthalpy_check THEN
     update ccpp_ccpp set 

     high_gas_production_check=NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.high_evaporator_influent_water_enthalpy_check ISNULL OR OLD.high_steam_enthalpy_check ISNULL OR OLD.high_boiler_efficiency_check ISNULL OR OLD.high_engine_exhaust_gas_energy_check ISNULL OR OLD.high_engine_exhaust_gas_flux_check ISNULL) AND NEW.high_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.high_steam_enthalpy_check NOTNULL AND NEW.high_boiler_efficiency_check NOTNULL AND NEW.high_engine_exhaust_gas_energy_check NOTNULL AND NEW.high_engine_exhaust_gas_flux_check NOTNULL THEN
     update ccpp_ccpp set 

     high_gas_production_check=NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_feedwater_amount:给水量,的计算9-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_check != NEW.high_engine_exhaust_gas_flux_check OR OLD.high_engine_exhaust_gas_energy_check != NEW.high_engine_exhaust_gas_energy_check OR OLD.high_boiler_efficiency_check != NEW.high_boiler_efficiency_check OR OLD.high_steam_enthalpy_check != NEW.high_steam_enthalpy_check OR OLD.high_evaporator_influent_water_enthalpy_check != NEW.high_evaporator_influent_water_enthalpy_check OR OLD.high_evaporator_effluent_smoke_enthalpy_check != NEW.high_evaporator_effluent_smoke_enthalpy_check OR OLD.high_blowdown_rate_check != NEW.high_blowdown_rate_check THEN
     update ccpp_ccpp set 

     high_feedwater_amount_check=(NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*(1+NEW.high_blowdown_rate_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_blowdown_rate_check ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.high_evaporator_influent_water_enthalpy_check ISNULL OR OLD.high_steam_enthalpy_check ISNULL OR OLD.high_boiler_efficiency_check ISNULL OR OLD.high_engine_exhaust_gas_energy_check ISNULL OR OLD.high_engine_exhaust_gas_flux_check ISNULL) AND NEW.high_blowdown_rate_check NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.high_steam_enthalpy_check NOTNULL AND NEW.high_boiler_efficiency_check NOTNULL AND NEW.high_engine_exhaust_gas_energy_check NOTNULL AND NEW.high_engine_exhaust_gas_flux_check NOTNULL THEN
     update ccpp_ccpp set 

     high_feedwater_amount_check=(NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*(1+NEW.high_blowdown_rate_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_superheater_effluent_smoke_enthalpy:高压过热器出口烟焓,的计算10-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_check != NEW.high_engine_exhaust_gas_flux_check OR OLD.high_engine_exhaust_gas_energy_check != NEW.high_engine_exhaust_gas_energy_check OR OLD.high_boiler_efficiency_check != NEW.high_boiler_efficiency_check OR OLD.high_steam_enthalpy_check != NEW.high_steam_enthalpy_check OR OLD.high_evaporator_influent_water_enthalpy_check != NEW.high_evaporator_influent_water_enthalpy_check OR OLD.high_evaporator_effluent_smoke_enthalpy_check != NEW.high_evaporator_effluent_smoke_enthalpy_check OR OLD.high_evaporator_effluent_steam_enthalpy_check != NEW.high_evaporator_effluent_steam_enthalpy_check THEN
     update ccpp_ccpp set 

     high_superheater_effluent_smoke_enthalpy_check=NEW.high_engine_exhaust_gas_energy_check-(NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*1000*(NEW.high_steam_enthalpy_check-NEW.high_evaporator_effluent_steam_enthalpy_check)/NEW.high_boiler_efficiency_check/NEW.high_engine_exhaust_gas_flux_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_evaporator_effluent_steam_enthalpy_check ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.high_evaporator_influent_water_enthalpy_check ISNULL OR OLD.high_steam_enthalpy_check ISNULL OR OLD.high_boiler_efficiency_check ISNULL OR OLD.high_engine_exhaust_gas_energy_check ISNULL OR OLD.high_engine_exhaust_gas_flux_check ISNULL) AND NEW.high_evaporator_effluent_steam_enthalpy_check NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.high_steam_enthalpy_check NOTNULL AND NEW.high_boiler_efficiency_check NOTNULL AND NEW.high_engine_exhaust_gas_energy_check NOTNULL AND NEW.high_engine_exhaust_gas_flux_check NOTNULL THEN
     update ccpp_ccpp set 

     high_superheater_effluent_smoke_enthalpy_check=NEW.high_engine_exhaust_gas_energy_check-(NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*1000*(NEW.high_steam_enthalpy_check-NEW.high_evaporator_effluent_steam_enthalpy_check)/NEW.high_boiler_efficiency_check/NEW.high_engine_exhaust_gas_flux_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_influent_smoke_temperature:进烟温度,的计算11-----------------------------------
  IF OLD.high_economizer_effluent_smoke_temperature_check != NEW.high_economizer_effluent_smoke_temperature_check THEN
     update ccpp_ccpp set 

     low_influent_smoke_temperature_check=NEW.high_economizer_effluent_smoke_temperature_check-15
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_economizer_effluent_smoke_temperature_check ISNULL) AND NEW.high_economizer_effluent_smoke_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     low_influent_smoke_temperature_check=NEW.high_economizer_effluent_smoke_temperature_check-15
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_superheat_steam_temperature:低压过热蒸汽温度,的计算12-----------------------------------
  IF OLD.high_economizer_effluent_smoke_temperature_check != NEW.high_economizer_effluent_smoke_temperature_check THEN
     update ccpp_ccpp set 

     low_superheat_steam_temperature_check=NEW.high_economizer_effluent_smoke_temperature_check-20
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_economizer_effluent_smoke_temperature_check ISNULL) AND NEW.high_economizer_effluent_smoke_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     low_superheat_steam_temperature_check=NEW.high_economizer_effluent_smoke_temperature_check-20
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_evaporator_influent_water_temperature:低压进蒸发器热水温度,的计算13-----------------------------------
  IF OLD.low_evaporat_temperature_check != NEW.low_evaporat_temperature_check OR OLD.low_proximity_temperature_check != NEW.low_proximity_temperature_check THEN
     update ccpp_ccpp set 

     low_evaporator_influent_water_temperature_check=NEW.low_evaporat_temperature_check-NEW.low_proximity_temperature_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_proximity_temperature_check ISNULL OR OLD.low_evaporat_temperature_check ISNULL) AND NEW.low_proximity_temperature_check NOTNULL AND NEW.low_evaporat_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     low_evaporator_influent_water_temperature_check=NEW.low_evaporat_temperature_check-NEW.low_proximity_temperature_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_evaporator_effluent_smoke_temperature:低压出蒸发器排烟温度,的计算14-----------------------------------
  IF OLD.low_evaporat_temperature_check != NEW.low_evaporat_temperature_check OR OLD.low_proximity_temperature_check != NEW.low_proximity_temperature_check OR OLD.low_node_temperature_check != NEW.low_node_temperature_check THEN
     update ccpp_ccpp set 

     low_evaporator_effluent_smoke_temperature_check=(NEW.low_evaporat_temperature_check-NEW.low_proximity_temperature_check)+NEW.low_node_temperature_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_node_temperature_check ISNULL OR OLD.low_proximity_temperature_check ISNULL OR OLD.low_evaporat_temperature_check ISNULL) AND NEW.low_node_temperature_check NOTNULL AND NEW.low_proximity_temperature_check NOTNULL AND NEW.low_evaporat_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     low_evaporator_effluent_smoke_temperature_check=(NEW.low_evaporat_temperature_check-NEW.low_proximity_temperature_check)+NEW.low_node_temperature_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_gas_production:低压产汽量,的计算15-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_check != NEW.high_engine_exhaust_gas_flux_check OR OLD.high_boiler_efficiency_check != NEW.high_boiler_efficiency_check OR OLD.low_influent_smoke_enthalpy_check != NEW.low_influent_smoke_enthalpy_check OR OLD.low_steam_enthalpy_check != NEW.low_steam_enthalpy_check OR OLD.low_evaporator_influent_water_enthalpy_check != NEW.low_evaporator_influent_water_enthalpy_check OR OLD.low_evaporator_effluent_smoke_enthalpy_check != NEW.low_evaporator_effluent_smoke_enthalpy_check THEN
     update ccpp_ccpp set 

     low_gas_production_check=((NEW.high_engine_exhaust_gas_flux_check)*(NEW.low_influent_smoke_enthalpy_check-NEW.low_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.low_steam_enthalpy_check-NEW.low_evaporator_influent_water_enthalpy_check)/1000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.low_evaporator_influent_water_enthalpy_check ISNULL OR OLD.low_steam_enthalpy_check ISNULL OR OLD.low_influent_smoke_enthalpy_check ISNULL OR OLD.high_boiler_efficiency_check ISNULL OR OLD.high_engine_exhaust_gas_flux_check ISNULL) AND NEW.low_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.low_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.low_steam_enthalpy_check NOTNULL AND NEW.low_influent_smoke_enthalpy_check NOTNULL AND NEW.high_boiler_efficiency_check NOTNULL AND NEW.high_engine_exhaust_gas_flux_check NOTNULL THEN
     update ccpp_ccpp set 

     low_gas_production_check=((NEW.high_engine_exhaust_gas_flux_check)*(NEW.low_influent_smoke_enthalpy_check-NEW.low_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.low_steam_enthalpy_check-NEW.low_evaporator_influent_water_enthalpy_check)/1000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_superheater_effluent_smoke_enthalpy:低压过热器出口烟焓,的计算16-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_check != NEW.high_engine_exhaust_gas_flux_check OR OLD.high_boiler_efficiency_check != NEW.high_boiler_efficiency_check OR OLD.low_influent_smoke_enthalpy_check != NEW.low_influent_smoke_enthalpy_check OR OLD.low_steam_enthalpy_check != NEW.low_steam_enthalpy_check OR OLD.low_evaporator_effluent_steam_enthalpy_check != NEW.low_evaporator_effluent_steam_enthalpy_check OR OLD.low_evaporator_influent_water_enthalpy_check != NEW.low_evaporator_influent_water_enthalpy_check OR OLD.low_evaporator_effluent_smoke_enthalpy_check != NEW.low_evaporator_effluent_smoke_enthalpy_check THEN
     update ccpp_ccpp set 

     low_superheater_effluent_smoke_enthalpy_check=NEW.low_influent_smoke_enthalpy_check-(((NEW.high_engine_exhaust_gas_flux_check)*(NEW.low_influent_smoke_enthalpy_check-NEW.low_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.low_steam_enthalpy_check-NEW.low_evaporator_influent_water_enthalpy_check)/1000))*1000*(NEW.low_steam_enthalpy_check-NEW.low_evaporator_effluent_steam_enthalpy_check)/NEW.high_boiler_efficiency_check/(NEW.high_engine_exhaust_gas_flux_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.low_evaporator_influent_water_enthalpy_check ISNULL OR OLD.low_evaporator_effluent_steam_enthalpy_check ISNULL OR OLD.low_steam_enthalpy_check ISNULL OR OLD.low_influent_smoke_enthalpy_check ISNULL OR OLD.high_boiler_efficiency_check ISNULL OR OLD.high_engine_exhaust_gas_flux_check ISNULL) AND NEW.low_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.low_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.low_evaporator_effluent_steam_enthalpy_check NOTNULL AND NEW.low_steam_enthalpy_check NOTNULL AND NEW.low_influent_smoke_enthalpy_check NOTNULL AND NEW.high_boiler_efficiency_check NOTNULL AND NEW.high_engine_exhaust_gas_flux_check NOTNULL THEN
     update ccpp_ccpp set 

     low_superheater_effluent_smoke_enthalpy_check=NEW.low_influent_smoke_enthalpy_check-(((NEW.high_engine_exhaust_gas_flux_check)*(NEW.low_influent_smoke_enthalpy_check-NEW.low_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.low_steam_enthalpy_check-NEW.low_evaporator_influent_water_enthalpy_check)/1000))*1000*(NEW.low_steam_enthalpy_check-NEW.low_evaporator_effluent_steam_enthalpy_check)/NEW.high_boiler_efficiency_check/(NEW.high_engine_exhaust_gas_flux_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_economizer_pressure:低压省煤器压力,的计算17-----------------------------------
  IF OLD.low_drum_pressure_check != NEW.low_drum_pressure_check THEN
     update ccpp_ccpp set 

     low_economizer_pressure_check=NEW.low_drum_pressure_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_drum_pressure_check ISNULL) AND NEW.low_drum_pressure_check NOTNULL THEN
     update ccpp_ccpp set 

     low_economizer_pressure_check=NEW.low_drum_pressure_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_economizer_influent_water_temperature:低压进省煤器热水温度,的计算18-----------------------------------
  IF OLD.low_evaporat_temperature_check != NEW.low_evaporat_temperature_check OR OLD.low_proximity_temperature_check != NEW.low_proximity_temperature_check THEN
     update ccpp_ccpp set 

     low_economizer_influent_water_temperature_check=(NEW.low_evaporat_temperature_check-NEW.low_proximity_temperature_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_proximity_temperature_check ISNULL OR OLD.low_evaporat_temperature_check ISNULL) AND NEW.low_proximity_temperature_check NOTNULL AND NEW.low_evaporat_temperature_check NOTNULL THEN
     update ccpp_ccpp set 

     low_economizer_influent_water_temperature_check=(NEW.low_evaporat_temperature_check-NEW.low_proximity_temperature_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_economizer_effluent_smoke_enthalpy:低压省煤器排烟焓值,的计算19-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_check != NEW.high_engine_exhaust_gas_flux_check OR OLD.high_engine_exhaust_gas_energy_check != NEW.high_engine_exhaust_gas_energy_check OR OLD.high_boiler_efficiency_check != NEW.high_boiler_efficiency_check OR OLD.high_steam_enthalpy_check != NEW.high_steam_enthalpy_check OR OLD.high_evaporator_influent_water_enthalpy_check != NEW.high_evaporator_influent_water_enthalpy_check OR OLD.high_evaporator_effluent_smoke_enthalpy_check != NEW.high_evaporator_effluent_smoke_enthalpy_check OR OLD.high_blowdown_rate_check != NEW.high_blowdown_rate_check OR OLD.low_influent_smoke_enthalpy_check != NEW.low_influent_smoke_enthalpy_check OR OLD.low_steam_enthalpy_check != NEW.low_steam_enthalpy_check OR OLD.low_evaporator_influent_water_enthalpy_check != NEW.low_evaporator_influent_water_enthalpy_check OR OLD.low_evaporator_effluent_smoke_enthalpy_check != NEW.low_evaporator_effluent_smoke_enthalpy_check OR OLD.low_economizer_influent_water_enthalpy_check != NEW.low_economizer_influent_water_enthalpy_check OR OLD.low_feedwater_enthalpy_check != NEW.low_feedwater_enthalpy_check THEN
     update ccpp_ccpp set 

     low_economizer_effluent_smoke_enthalpy_check=NEW.low_evaporator_effluent_smoke_enthalpy_check-(((NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*(1+NEW.high_blowdown_rate_check))+(((NEW.high_engine_exhaust_gas_flux_check)*(NEW.low_influent_smoke_enthalpy_check-NEW.low_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.low_steam_enthalpy_check-NEW.low_evaporator_influent_water_enthalpy_check)/1000))*(1+0.02))*1000*(NEW.low_economizer_influent_water_enthalpy_check-NEW.low_feedwater_enthalpy_check)/(NEW.high_engine_exhaust_gas_flux_check)/NEW.high_boiler_efficiency_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_feedwater_enthalpy_check ISNULL OR OLD.low_economizer_influent_water_enthalpy_check ISNULL OR OLD.low_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.low_evaporator_influent_water_enthalpy_check ISNULL OR OLD.low_steam_enthalpy_check ISNULL OR OLD.low_influent_smoke_enthalpy_check ISNULL OR OLD.high_blowdown_rate_check ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.high_evaporator_influent_water_enthalpy_check ISNULL OR OLD.high_steam_enthalpy_check ISNULL OR OLD.high_boiler_efficiency_check ISNULL OR OLD.high_engine_exhaust_gas_energy_check ISNULL OR OLD.high_engine_exhaust_gas_flux_check ISNULL) AND NEW.low_feedwater_enthalpy_check NOTNULL AND NEW.low_economizer_influent_water_enthalpy_check NOTNULL AND NEW.low_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.low_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.low_steam_enthalpy_check NOTNULL AND NEW.low_influent_smoke_enthalpy_check NOTNULL AND NEW.high_blowdown_rate_check NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.high_steam_enthalpy_check NOTNULL AND NEW.high_boiler_efficiency_check NOTNULL AND NEW.high_engine_exhaust_gas_energy_check NOTNULL AND NEW.high_engine_exhaust_gas_flux_check NOTNULL THEN
     update ccpp_ccpp set 

     low_economizer_effluent_smoke_enthalpy_check=NEW.low_evaporator_effluent_smoke_enthalpy_check-(((NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*(1+NEW.high_blowdown_rate_check))+(((NEW.high_engine_exhaust_gas_flux_check)*(NEW.low_influent_smoke_enthalpy_check-NEW.low_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.low_steam_enthalpy_check-NEW.low_evaporator_influent_water_enthalpy_check)/1000))*(1+0.02))*1000*(NEW.low_economizer_influent_water_enthalpy_check-NEW.low_feedwater_enthalpy_check)/(NEW.high_engine_exhaust_gas_flux_check)/NEW.high_boiler_efficiency_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_feedwater_flux:给水流量,的计算20-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_check != NEW.high_engine_exhaust_gas_flux_check OR OLD.high_engine_exhaust_gas_energy_check != NEW.high_engine_exhaust_gas_energy_check OR OLD.high_boiler_efficiency_check != NEW.high_boiler_efficiency_check OR OLD.high_steam_enthalpy_check != NEW.high_steam_enthalpy_check OR OLD.high_evaporator_influent_water_enthalpy_check != NEW.high_evaporator_influent_water_enthalpy_check OR OLD.high_evaporator_effluent_smoke_enthalpy_check != NEW.high_evaporator_effluent_smoke_enthalpy_check OR OLD.high_blowdown_rate_check != NEW.high_blowdown_rate_check OR OLD.low_influent_smoke_enthalpy_check != NEW.low_influent_smoke_enthalpy_check OR OLD.low_steam_enthalpy_check != NEW.low_steam_enthalpy_check OR OLD.low_evaporator_influent_water_enthalpy_check != NEW.low_evaporator_influent_water_enthalpy_check OR OLD.low_evaporator_effluent_smoke_enthalpy_check != NEW.low_evaporator_effluent_smoke_enthalpy_check THEN
     update ccpp_ccpp set 

     low_feedwater_flux_check=((NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*(1+NEW.high_blowdown_rate_check))+(((NEW.high_engine_exhaust_gas_flux_check)*(NEW.low_influent_smoke_enthalpy_check-NEW.low_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.low_steam_enthalpy_check-NEW.low_evaporator_influent_water_enthalpy_check)/1000))*(1+0.02)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.low_evaporator_influent_water_enthalpy_check ISNULL OR OLD.low_steam_enthalpy_check ISNULL OR OLD.low_influent_smoke_enthalpy_check ISNULL OR OLD.high_blowdown_rate_check ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_check ISNULL OR OLD.high_evaporator_influent_water_enthalpy_check ISNULL OR OLD.high_steam_enthalpy_check ISNULL OR OLD.high_boiler_efficiency_check ISNULL OR OLD.high_engine_exhaust_gas_energy_check ISNULL OR OLD.high_engine_exhaust_gas_flux_check ISNULL) AND NEW.low_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.low_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.low_steam_enthalpy_check NOTNULL AND NEW.low_influent_smoke_enthalpy_check NOTNULL AND NEW.high_blowdown_rate_check NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_check NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_check NOTNULL AND NEW.high_steam_enthalpy_check NOTNULL AND NEW.high_boiler_efficiency_check NOTNULL AND NEW.high_engine_exhaust_gas_energy_check NOTNULL AND NEW.high_engine_exhaust_gas_flux_check NOTNULL THEN
     update ccpp_ccpp set 

     low_feedwater_flux_check=((NEW.high_engine_exhaust_gas_flux_check*(NEW.high_engine_exhaust_gas_energy_check-NEW.high_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.high_steam_enthalpy_check-NEW.high_evaporator_influent_water_enthalpy_check)/1000)*(1+NEW.high_blowdown_rate_check))+(((NEW.high_engine_exhaust_gas_flux_check)*(NEW.low_influent_smoke_enthalpy_check-NEW.low_evaporator_effluent_smoke_enthalpy_check)*NEW.high_boiler_efficiency_check/(NEW.low_steam_enthalpy_check-NEW.low_evaporator_influent_water_enthalpy_check)/1000))*(1+0.02)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
DELETE FROM pg_trigger WHERE tgname='ccpp_ccpp_check';
CREATE TRIGGER "ccpp_ccpp_check" AFTER UPDATE OF
"engine_exhaust_gas_temperature_check",
"high_engine_exhaust_gas_flux_check",
"high_engine_exhaust_gas_energy_check",
"high_boiler_efficiency_check",
"high_steam_pressure_check",
"high_terminal_temperature_difference_check",
"high_steam_enthalpy_check",
"high_evaporating_temperature_check",
"high_node_temperature_check",
"high_evaporator_influent_water_enthalpy_check",
"high_proximity_temperature_difference_check",
"high_evaporator_effluent_smoke_enthalpy_check",
"high_economizer_effluent_smoke_temperature_check",
"high_economizer_influent_water_temperature_check",
"high_blowdown_rate_check",
"high_evaporator_effluent_steam_enthalpy_check",
"low_drum_pressure_check",
"low_influent_smoke_enthalpy_check",
"low_steam_enthalpy_check",
"low_evaporat_temperature_check",
"low_evaporator_effluent_steam_enthalpy_check",
"low_proximity_temperature_check",
"low_evaporator_influent_water_enthalpy_check",
"low_node_temperature_check",
"low_evaporator_effluent_smoke_enthalpy_check",
"low_economizer_influent_water_enthalpy_check",
"low_feedwater_enthalpy_check"
ON "public"."ccpp_ccpp"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_ccpp_check"();

CREATE OR REPLACE FUNCTION ccpp_ccpp_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段high_engine_exhaust_gas_temperature:燃机排烟温度,的计算1-----------------------------------
  IF OLD.engine_exhaust_gas_temperature_design != NEW.engine_exhaust_gas_temperature_design THEN
     update ccpp_ccpp set 

     high_engine_exhaust_gas_temperature_design=NEW.engine_exhaust_gas_temperature_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.engine_exhaust_gas_temperature_design ISNULL) AND NEW.engine_exhaust_gas_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     high_engine_exhaust_gas_temperature_design=NEW.engine_exhaust_gas_temperature_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_steam_temperature:主蒸汽温度,的计算2-----------------------------------
  IF OLD.engine_exhaust_gas_temperature_design != NEW.engine_exhaust_gas_temperature_design OR OLD.high_terminal_temperature_difference_design != NEW.high_terminal_temperature_difference_design THEN
     update ccpp_ccpp set 

     high_steam_temperature_design=(NEW.engine_exhaust_gas_temperature_design)-NEW.high_terminal_temperature_difference_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_terminal_temperature_difference_design ISNULL OR OLD.engine_exhaust_gas_temperature_design ISNULL) AND NEW.high_terminal_temperature_difference_design NOTNULL AND NEW.engine_exhaust_gas_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     high_steam_temperature_design=(NEW.engine_exhaust_gas_temperature_design)-NEW.high_terminal_temperature_difference_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_drum_pressure:高压汽包压力,的计算3-----------------------------------
  IF OLD.high_steam_pressure_design != NEW.high_steam_pressure_design THEN
     update ccpp_ccpp set 

     high_drum_pressure_design=NEW.high_steam_pressure_design*1.05
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_steam_pressure_design ISNULL) AND NEW.high_steam_pressure_design NOTNULL THEN
     update ccpp_ccpp set 

     high_drum_pressure_design=NEW.high_steam_pressure_design*1.05
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_evaporator_influent_water_temperature:高压进蒸发器热水温度,的计算4-----------------------------------
  IF OLD.high_evaporating_temperature_design != NEW.high_evaporating_temperature_design OR OLD.high_node_temperature_design != NEW.high_node_temperature_design THEN
     update ccpp_ccpp set 

     high_evaporator_influent_water_temperature_design=NEW.high_evaporating_temperature_design-NEW.high_node_temperature_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_node_temperature_design ISNULL OR OLD.high_evaporating_temperature_design ISNULL) AND NEW.high_node_temperature_design NOTNULL AND NEW.high_evaporating_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     high_evaporator_influent_water_temperature_design=NEW.high_evaporating_temperature_design-NEW.high_node_temperature_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_evaporator_effluent_smoke_temperature:高压出蒸发器烟气温度,的计算5-----------------------------------
  IF OLD.high_evaporating_temperature_design != NEW.high_evaporating_temperature_design OR OLD.high_node_temperature_design != NEW.high_node_temperature_design OR OLD.high_proximity_temperature_difference_design != NEW.high_proximity_temperature_difference_design THEN
     update ccpp_ccpp set 

     high_evaporator_effluent_smoke_temperature_design=(NEW.high_evaporating_temperature_design-NEW.high_node_temperature_design)+NEW.high_proximity_temperature_difference_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_proximity_temperature_difference_design ISNULL OR OLD.high_node_temperature_design ISNULL OR OLD.high_evaporating_temperature_design ISNULL) AND NEW.high_proximity_temperature_difference_design NOTNULL AND NEW.high_node_temperature_design NOTNULL AND NEW.high_evaporating_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     high_evaporator_effluent_smoke_temperature_design=(NEW.high_evaporating_temperature_design-NEW.high_node_temperature_design)+NEW.high_proximity_temperature_difference_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_economizer_effluent_smoke_enthalpy:高压出省煤器烟气焓值,的计算6-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_design != NEW.high_engine_exhaust_gas_flux_design OR OLD.high_engine_exhaust_gas_energy_design != NEW.high_engine_exhaust_gas_energy_design OR OLD.high_boiler_efficiency_design != NEW.high_boiler_efficiency_design OR OLD.high_steam_enthalpy_design != NEW.high_steam_enthalpy_design OR OLD.high_evaporator_influent_water_enthalpy_design != NEW.high_evaporator_influent_water_enthalpy_design OR OLD.high_evaporator_effluent_smoke_enthalpy_design != NEW.high_evaporator_effluent_smoke_enthalpy_design OR OLD.high_economizer_influent_water_temperature_design != NEW.high_economizer_influent_water_temperature_design OR OLD.high_blowdown_rate_design != NEW.high_blowdown_rate_design THEN
     update ccpp_ccpp set 

     high_economizer_effluent_smoke_enthalpy_design=NEW.high_evaporator_effluent_smoke_enthalpy_design-((NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*(1+NEW.high_blowdown_rate_design))*(NEW.high_evaporator_influent_water_enthalpy_design-NEW.high_economizer_influent_water_temperature_design)*1000/NEW.high_boiler_efficiency_design/NEW.high_engine_exhaust_gas_flux_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_blowdown_rate_design ISNULL OR OLD.high_economizer_influent_water_temperature_design ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.high_evaporator_influent_water_enthalpy_design ISNULL OR OLD.high_steam_enthalpy_design ISNULL OR OLD.high_boiler_efficiency_design ISNULL OR OLD.high_engine_exhaust_gas_energy_design ISNULL OR OLD.high_engine_exhaust_gas_flux_design ISNULL) AND NEW.high_blowdown_rate_design NOTNULL AND NEW.high_economizer_influent_water_temperature_design NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.high_steam_enthalpy_design NOTNULL AND NEW.high_boiler_efficiency_design NOTNULL AND NEW.high_engine_exhaust_gas_energy_design NOTNULL AND NEW.high_engine_exhaust_gas_flux_design NOTNULL THEN
     update ccpp_ccpp set 

     high_economizer_effluent_smoke_enthalpy_design=NEW.high_evaporator_effluent_smoke_enthalpy_design-((NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*(1+NEW.high_blowdown_rate_design))*(NEW.high_evaporator_influent_water_enthalpy_design-NEW.high_economizer_influent_water_temperature_design)*1000/NEW.high_boiler_efficiency_design/NEW.high_engine_exhaust_gas_flux_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_economizer_influent_water_enthalpy:高压进省煤器热水焓值,的计算7-----------------------------------
  IF OLD.low_evaporat_temperature_design != NEW.low_evaporat_temperature_design THEN
     update ccpp_ccpp set 

     high_economizer_influent_water_enthalpy_design=NEW.low_evaporat_temperature_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_evaporat_temperature_design ISNULL) AND NEW.low_evaporat_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     high_economizer_influent_water_enthalpy_design=NEW.low_evaporat_temperature_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_gas_production:高压产汽量,的计算8-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_design != NEW.high_engine_exhaust_gas_flux_design OR OLD.high_engine_exhaust_gas_energy_design != NEW.high_engine_exhaust_gas_energy_design OR OLD.high_boiler_efficiency_design != NEW.high_boiler_efficiency_design OR OLD.high_steam_enthalpy_design != NEW.high_steam_enthalpy_design OR OLD.high_evaporator_influent_water_enthalpy_design != NEW.high_evaporator_influent_water_enthalpy_design OR OLD.high_evaporator_effluent_smoke_enthalpy_design != NEW.high_evaporator_effluent_smoke_enthalpy_design THEN
     update ccpp_ccpp set 

     high_gas_production_design=NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.high_evaporator_influent_water_enthalpy_design ISNULL OR OLD.high_steam_enthalpy_design ISNULL OR OLD.high_boiler_efficiency_design ISNULL OR OLD.high_engine_exhaust_gas_energy_design ISNULL OR OLD.high_engine_exhaust_gas_flux_design ISNULL) AND NEW.high_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.high_steam_enthalpy_design NOTNULL AND NEW.high_boiler_efficiency_design NOTNULL AND NEW.high_engine_exhaust_gas_energy_design NOTNULL AND NEW.high_engine_exhaust_gas_flux_design NOTNULL THEN
     update ccpp_ccpp set 

     high_gas_production_design=NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_feedwater_amount:给水量,的计算9-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_design != NEW.high_engine_exhaust_gas_flux_design OR OLD.high_engine_exhaust_gas_energy_design != NEW.high_engine_exhaust_gas_energy_design OR OLD.high_boiler_efficiency_design != NEW.high_boiler_efficiency_design OR OLD.high_steam_enthalpy_design != NEW.high_steam_enthalpy_design OR OLD.high_evaporator_influent_water_enthalpy_design != NEW.high_evaporator_influent_water_enthalpy_design OR OLD.high_evaporator_effluent_smoke_enthalpy_design != NEW.high_evaporator_effluent_smoke_enthalpy_design OR OLD.high_blowdown_rate_design != NEW.high_blowdown_rate_design THEN
     update ccpp_ccpp set 

     high_feedwater_amount_design=(NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*(1+NEW.high_blowdown_rate_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_blowdown_rate_design ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.high_evaporator_influent_water_enthalpy_design ISNULL OR OLD.high_steam_enthalpy_design ISNULL OR OLD.high_boiler_efficiency_design ISNULL OR OLD.high_engine_exhaust_gas_energy_design ISNULL OR OLD.high_engine_exhaust_gas_flux_design ISNULL) AND NEW.high_blowdown_rate_design NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.high_steam_enthalpy_design NOTNULL AND NEW.high_boiler_efficiency_design NOTNULL AND NEW.high_engine_exhaust_gas_energy_design NOTNULL AND NEW.high_engine_exhaust_gas_flux_design NOTNULL THEN
     update ccpp_ccpp set 

     high_feedwater_amount_design=(NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*(1+NEW.high_blowdown_rate_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段high_superheater_effluent_smoke_enthalpy:高压过热器出口烟焓,的计算10-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_design != NEW.high_engine_exhaust_gas_flux_design OR OLD.high_engine_exhaust_gas_energy_design != NEW.high_engine_exhaust_gas_energy_design OR OLD.high_boiler_efficiency_design != NEW.high_boiler_efficiency_design OR OLD.high_steam_enthalpy_design != NEW.high_steam_enthalpy_design OR OLD.high_evaporator_influent_water_enthalpy_design != NEW.high_evaporator_influent_water_enthalpy_design OR OLD.high_evaporator_effluent_smoke_enthalpy_design != NEW.high_evaporator_effluent_smoke_enthalpy_design OR OLD.high_evaporator_effluent_steam_enthalpy_design != NEW.high_evaporator_effluent_steam_enthalpy_design THEN
     update ccpp_ccpp set 

     high_superheater_effluent_smoke_enthalpy_design=NEW.high_engine_exhaust_gas_energy_design-(NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*1000*(NEW.high_steam_enthalpy_design-NEW.high_evaporator_effluent_steam_enthalpy_design)/NEW.high_boiler_efficiency_design/NEW.high_engine_exhaust_gas_flux_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_evaporator_effluent_steam_enthalpy_design ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.high_evaporator_influent_water_enthalpy_design ISNULL OR OLD.high_steam_enthalpy_design ISNULL OR OLD.high_boiler_efficiency_design ISNULL OR OLD.high_engine_exhaust_gas_energy_design ISNULL OR OLD.high_engine_exhaust_gas_flux_design ISNULL) AND NEW.high_evaporator_effluent_steam_enthalpy_design NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.high_steam_enthalpy_design NOTNULL AND NEW.high_boiler_efficiency_design NOTNULL AND NEW.high_engine_exhaust_gas_energy_design NOTNULL AND NEW.high_engine_exhaust_gas_flux_design NOTNULL THEN
     update ccpp_ccpp set 

     high_superheater_effluent_smoke_enthalpy_design=NEW.high_engine_exhaust_gas_energy_design-(NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*1000*(NEW.high_steam_enthalpy_design-NEW.high_evaporator_effluent_steam_enthalpy_design)/NEW.high_boiler_efficiency_design/NEW.high_engine_exhaust_gas_flux_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_influent_smoke_temperature:进烟温度,的计算11-----------------------------------
  IF OLD.high_economizer_effluent_smoke_temperature_design != NEW.high_economizer_effluent_smoke_temperature_design THEN
     update ccpp_ccpp set 

     low_influent_smoke_temperature_design=NEW.high_economizer_effluent_smoke_temperature_design-15
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_economizer_effluent_smoke_temperature_design ISNULL) AND NEW.high_economizer_effluent_smoke_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     low_influent_smoke_temperature_design=NEW.high_economizer_effluent_smoke_temperature_design-15
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_superheat_steam_temperature:低压过热蒸汽温度,的计算12-----------------------------------
  IF OLD.high_economizer_effluent_smoke_temperature_design != NEW.high_economizer_effluent_smoke_temperature_design THEN
     update ccpp_ccpp set 

     low_superheat_steam_temperature_design=NEW.high_economizer_effluent_smoke_temperature_design-20
     where plan_id=NEW.plan_id;

  ELSIF (OLD.high_economizer_effluent_smoke_temperature_design ISNULL) AND NEW.high_economizer_effluent_smoke_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     low_superheat_steam_temperature_design=NEW.high_economizer_effluent_smoke_temperature_design-20
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_evaporator_influent_water_temperature:低压进蒸发器热水温度,的计算13-----------------------------------
  IF OLD.low_evaporat_temperature_design != NEW.low_evaporat_temperature_design OR OLD.low_proximity_temperature_design != NEW.low_proximity_temperature_design THEN
     update ccpp_ccpp set 

     low_evaporator_influent_water_temperature_design=NEW.low_evaporat_temperature_design-NEW.low_proximity_temperature_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_proximity_temperature_design ISNULL OR OLD.low_evaporat_temperature_design ISNULL) AND NEW.low_proximity_temperature_design NOTNULL AND NEW.low_evaporat_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     low_evaporator_influent_water_temperature_design=NEW.low_evaporat_temperature_design-NEW.low_proximity_temperature_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_evaporator_effluent_smoke_temperature:低压出蒸发器排烟温度,的计算14-----------------------------------
  IF OLD.low_evaporat_temperature_design != NEW.low_evaporat_temperature_design OR OLD.low_proximity_temperature_design != NEW.low_proximity_temperature_design OR OLD.low_node_temperature_design != NEW.low_node_temperature_design THEN
     update ccpp_ccpp set 

     low_evaporator_effluent_smoke_temperature_design=(NEW.low_evaporat_temperature_design-NEW.low_proximity_temperature_design)+NEW.low_node_temperature_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_node_temperature_design ISNULL OR OLD.low_proximity_temperature_design ISNULL OR OLD.low_evaporat_temperature_design ISNULL) AND NEW.low_node_temperature_design NOTNULL AND NEW.low_proximity_temperature_design NOTNULL AND NEW.low_evaporat_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     low_evaporator_effluent_smoke_temperature_design=(NEW.low_evaporat_temperature_design-NEW.low_proximity_temperature_design)+NEW.low_node_temperature_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_gas_production:低压产汽量,的计算15-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_design != NEW.high_engine_exhaust_gas_flux_design OR OLD.high_boiler_efficiency_design != NEW.high_boiler_efficiency_design OR OLD.low_influent_smoke_enthalpy_design != NEW.low_influent_smoke_enthalpy_design OR OLD.low_steam_enthalpy_design != NEW.low_steam_enthalpy_design OR OLD.low_evaporator_influent_water_enthalpy_design != NEW.low_evaporator_influent_water_enthalpy_design OR OLD.low_evaporator_effluent_smoke_enthalpy_design != NEW.low_evaporator_effluent_smoke_enthalpy_design THEN
     update ccpp_ccpp set 

     low_gas_production_design=((NEW.high_engine_exhaust_gas_flux_design)*(NEW.low_influent_smoke_enthalpy_design-NEW.low_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.low_steam_enthalpy_design-NEW.low_evaporator_influent_water_enthalpy_design)/1000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.low_evaporator_influent_water_enthalpy_design ISNULL OR OLD.low_steam_enthalpy_design ISNULL OR OLD.low_influent_smoke_enthalpy_design ISNULL OR OLD.high_boiler_efficiency_design ISNULL OR OLD.high_engine_exhaust_gas_flux_design ISNULL) AND NEW.low_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.low_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.low_steam_enthalpy_design NOTNULL AND NEW.low_influent_smoke_enthalpy_design NOTNULL AND NEW.high_boiler_efficiency_design NOTNULL AND NEW.high_engine_exhaust_gas_flux_design NOTNULL THEN
     update ccpp_ccpp set 

     low_gas_production_design=((NEW.high_engine_exhaust_gas_flux_design)*(NEW.low_influent_smoke_enthalpy_design-NEW.low_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.low_steam_enthalpy_design-NEW.low_evaporator_influent_water_enthalpy_design)/1000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_superheater_effluent_smoke_enthalpy:低压过热器出口烟焓,的计算16-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_design != NEW.high_engine_exhaust_gas_flux_design OR OLD.high_boiler_efficiency_design != NEW.high_boiler_efficiency_design OR OLD.low_influent_smoke_enthalpy_design != NEW.low_influent_smoke_enthalpy_design OR OLD.low_steam_enthalpy_design != NEW.low_steam_enthalpy_design OR OLD.low_evaporator_effluent_steam_enthalpy_design != NEW.low_evaporator_effluent_steam_enthalpy_design OR OLD.low_evaporator_influent_water_enthalpy_design != NEW.low_evaporator_influent_water_enthalpy_design OR OLD.low_evaporator_effluent_smoke_enthalpy_design != NEW.low_evaporator_effluent_smoke_enthalpy_design THEN
     update ccpp_ccpp set 

     low_superheater_effluent_smoke_enthalpy_design=NEW.low_influent_smoke_enthalpy_design-(((NEW.high_engine_exhaust_gas_flux_design)*(NEW.low_influent_smoke_enthalpy_design-NEW.low_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.low_steam_enthalpy_design-NEW.low_evaporator_influent_water_enthalpy_design)/1000))*1000*(NEW.low_steam_enthalpy_design-NEW.low_evaporator_effluent_steam_enthalpy_design)/NEW.high_boiler_efficiency_design/(NEW.high_engine_exhaust_gas_flux_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.low_evaporator_influent_water_enthalpy_design ISNULL OR OLD.low_evaporator_effluent_steam_enthalpy_design ISNULL OR OLD.low_steam_enthalpy_design ISNULL OR OLD.low_influent_smoke_enthalpy_design ISNULL OR OLD.high_boiler_efficiency_design ISNULL OR OLD.high_engine_exhaust_gas_flux_design ISNULL) AND NEW.low_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.low_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.low_evaporator_effluent_steam_enthalpy_design NOTNULL AND NEW.low_steam_enthalpy_design NOTNULL AND NEW.low_influent_smoke_enthalpy_design NOTNULL AND NEW.high_boiler_efficiency_design NOTNULL AND NEW.high_engine_exhaust_gas_flux_design NOTNULL THEN
     update ccpp_ccpp set 

     low_superheater_effluent_smoke_enthalpy_design=NEW.low_influent_smoke_enthalpy_design-(((NEW.high_engine_exhaust_gas_flux_design)*(NEW.low_influent_smoke_enthalpy_design-NEW.low_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.low_steam_enthalpy_design-NEW.low_evaporator_influent_water_enthalpy_design)/1000))*1000*(NEW.low_steam_enthalpy_design-NEW.low_evaporator_effluent_steam_enthalpy_design)/NEW.high_boiler_efficiency_design/(NEW.high_engine_exhaust_gas_flux_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_economizer_pressure:低压省煤器压力,的计算17-----------------------------------
  IF OLD.low_drum_pressure_design != NEW.low_drum_pressure_design THEN
     update ccpp_ccpp set 

     low_economizer_pressure_design=NEW.low_drum_pressure_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_drum_pressure_design ISNULL) AND NEW.low_drum_pressure_design NOTNULL THEN
     update ccpp_ccpp set 

     low_economizer_pressure_design=NEW.low_drum_pressure_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_economizer_influent_water_temperature:低压进省煤器热水温度,的计算18-----------------------------------
  IF OLD.low_evaporat_temperature_design != NEW.low_evaporat_temperature_design OR OLD.low_proximity_temperature_design != NEW.low_proximity_temperature_design THEN
     update ccpp_ccpp set 

     low_economizer_influent_water_temperature_design=(NEW.low_evaporat_temperature_design-NEW.low_proximity_temperature_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_proximity_temperature_design ISNULL OR OLD.low_evaporat_temperature_design ISNULL) AND NEW.low_proximity_temperature_design NOTNULL AND NEW.low_evaporat_temperature_design NOTNULL THEN
     update ccpp_ccpp set 

     low_economizer_influent_water_temperature_design=(NEW.low_evaporat_temperature_design-NEW.low_proximity_temperature_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_economizer_effluent_smoke_enthalpy:低压省煤器排烟焓值,的计算19-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_design != NEW.high_engine_exhaust_gas_flux_design OR OLD.high_engine_exhaust_gas_energy_design != NEW.high_engine_exhaust_gas_energy_design OR OLD.high_boiler_efficiency_design != NEW.high_boiler_efficiency_design OR OLD.high_steam_enthalpy_design != NEW.high_steam_enthalpy_design OR OLD.high_evaporator_influent_water_enthalpy_design != NEW.high_evaporator_influent_water_enthalpy_design OR OLD.high_evaporator_effluent_smoke_enthalpy_design != NEW.high_evaporator_effluent_smoke_enthalpy_design OR OLD.high_blowdown_rate_design != NEW.high_blowdown_rate_design OR OLD.low_influent_smoke_enthalpy_design != NEW.low_influent_smoke_enthalpy_design OR OLD.low_steam_enthalpy_design != NEW.low_steam_enthalpy_design OR OLD.low_evaporator_influent_water_enthalpy_design != NEW.low_evaporator_influent_water_enthalpy_design OR OLD.low_evaporator_effluent_smoke_enthalpy_design != NEW.low_evaporator_effluent_smoke_enthalpy_design OR OLD.low_economizer_influent_water_enthalpy_design != NEW.low_economizer_influent_water_enthalpy_design OR OLD.low_feedwater_enthalpy_design != NEW.low_feedwater_enthalpy_design THEN
     update ccpp_ccpp set 

     low_economizer_effluent_smoke_enthalpy_design=NEW.low_evaporator_effluent_smoke_enthalpy_design-(((NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*(1+NEW.high_blowdown_rate_design))+(((NEW.high_engine_exhaust_gas_flux_design)*(NEW.low_influent_smoke_enthalpy_design-NEW.low_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.low_steam_enthalpy_design-NEW.low_evaporator_influent_water_enthalpy_design)/1000))*(1+0.02))*1000*(NEW.low_economizer_influent_water_enthalpy_design-NEW.low_feedwater_enthalpy_design)/(NEW.high_engine_exhaust_gas_flux_design)/NEW.high_boiler_efficiency_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_feedwater_enthalpy_design ISNULL OR OLD.low_economizer_influent_water_enthalpy_design ISNULL OR OLD.low_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.low_evaporator_influent_water_enthalpy_design ISNULL OR OLD.low_steam_enthalpy_design ISNULL OR OLD.low_influent_smoke_enthalpy_design ISNULL OR OLD.high_blowdown_rate_design ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.high_evaporator_influent_water_enthalpy_design ISNULL OR OLD.high_steam_enthalpy_design ISNULL OR OLD.high_boiler_efficiency_design ISNULL OR OLD.high_engine_exhaust_gas_energy_design ISNULL OR OLD.high_engine_exhaust_gas_flux_design ISNULL) AND NEW.low_feedwater_enthalpy_design NOTNULL AND NEW.low_economizer_influent_water_enthalpy_design NOTNULL AND NEW.low_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.low_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.low_steam_enthalpy_design NOTNULL AND NEW.low_influent_smoke_enthalpy_design NOTNULL AND NEW.high_blowdown_rate_design NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.high_steam_enthalpy_design NOTNULL AND NEW.high_boiler_efficiency_design NOTNULL AND NEW.high_engine_exhaust_gas_energy_design NOTNULL AND NEW.high_engine_exhaust_gas_flux_design NOTNULL THEN
     update ccpp_ccpp set 

     low_economizer_effluent_smoke_enthalpy_design=NEW.low_evaporator_effluent_smoke_enthalpy_design-(((NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*(1+NEW.high_blowdown_rate_design))+(((NEW.high_engine_exhaust_gas_flux_design)*(NEW.low_influent_smoke_enthalpy_design-NEW.low_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.low_steam_enthalpy_design-NEW.low_evaporator_influent_water_enthalpy_design)/1000))*(1+0.02))*1000*(NEW.low_economizer_influent_water_enthalpy_design-NEW.low_feedwater_enthalpy_design)/(NEW.high_engine_exhaust_gas_flux_design)/NEW.high_boiler_efficiency_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_feedwater_flux:给水流量,的计算20-----------------------------------
  IF OLD.high_engine_exhaust_gas_flux_design != NEW.high_engine_exhaust_gas_flux_design OR OLD.high_engine_exhaust_gas_energy_design != NEW.high_engine_exhaust_gas_energy_design OR OLD.high_boiler_efficiency_design != NEW.high_boiler_efficiency_design OR OLD.high_steam_enthalpy_design != NEW.high_steam_enthalpy_design OR OLD.high_evaporator_influent_water_enthalpy_design != NEW.high_evaporator_influent_water_enthalpy_design OR OLD.high_evaporator_effluent_smoke_enthalpy_design != NEW.high_evaporator_effluent_smoke_enthalpy_design OR OLD.high_blowdown_rate_design != NEW.high_blowdown_rate_design OR OLD.low_influent_smoke_enthalpy_design != NEW.low_influent_smoke_enthalpy_design OR OLD.low_steam_enthalpy_design != NEW.low_steam_enthalpy_design OR OLD.low_evaporator_influent_water_enthalpy_design != NEW.low_evaporator_influent_water_enthalpy_design OR OLD.low_evaporator_effluent_smoke_enthalpy_design != NEW.low_evaporator_effluent_smoke_enthalpy_design THEN
     update ccpp_ccpp set 

     low_feedwater_flux_design=((NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*(1+NEW.high_blowdown_rate_design))+(((NEW.high_engine_exhaust_gas_flux_design)*(NEW.low_influent_smoke_enthalpy_design-NEW.low_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.low_steam_enthalpy_design-NEW.low_evaporator_influent_water_enthalpy_design)/1000))*(1+0.02)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.low_evaporator_influent_water_enthalpy_design ISNULL OR OLD.low_steam_enthalpy_design ISNULL OR OLD.low_influent_smoke_enthalpy_design ISNULL OR OLD.high_blowdown_rate_design ISNULL OR OLD.high_evaporator_effluent_smoke_enthalpy_design ISNULL OR OLD.high_evaporator_influent_water_enthalpy_design ISNULL OR OLD.high_steam_enthalpy_design ISNULL OR OLD.high_boiler_efficiency_design ISNULL OR OLD.high_engine_exhaust_gas_energy_design ISNULL OR OLD.high_engine_exhaust_gas_flux_design ISNULL) AND NEW.low_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.low_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.low_steam_enthalpy_design NOTNULL AND NEW.low_influent_smoke_enthalpy_design NOTNULL AND NEW.high_blowdown_rate_design NOTNULL AND NEW.high_evaporator_effluent_smoke_enthalpy_design NOTNULL AND NEW.high_evaporator_influent_water_enthalpy_design NOTNULL AND NEW.high_steam_enthalpy_design NOTNULL AND NEW.high_boiler_efficiency_design NOTNULL AND NEW.high_engine_exhaust_gas_energy_design NOTNULL AND NEW.high_engine_exhaust_gas_flux_design NOTNULL THEN
     update ccpp_ccpp set 

     low_feedwater_flux_design=((NEW.high_engine_exhaust_gas_flux_design*(NEW.high_engine_exhaust_gas_energy_design-NEW.high_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.high_steam_enthalpy_design-NEW.high_evaporator_influent_water_enthalpy_design)/1000)*(1+NEW.high_blowdown_rate_design))+(((NEW.high_engine_exhaust_gas_flux_design)*(NEW.low_influent_smoke_enthalpy_design-NEW.low_evaporator_effluent_smoke_enthalpy_design)*NEW.high_boiler_efficiency_design/(NEW.low_steam_enthalpy_design-NEW.low_evaporator_influent_water_enthalpy_design)/1000))*(1+0.02)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
DELETE FROM pg_trigger WHERE tgname='ccpp_ccpp_design';
CREATE TRIGGER "ccpp_ccpp_design" AFTER UPDATE OF
"engine_exhaust_gas_temperature_design",
"high_engine_exhaust_gas_flux_design",
"high_engine_exhaust_gas_energy_design",
"high_boiler_efficiency_design",
"high_steam_pressure_design",
"high_terminal_temperature_difference_design",
"high_steam_enthalpy_design",
"high_evaporating_temperature_design",
"high_node_temperature_design",
"high_evaporator_influent_water_enthalpy_design",
"high_proximity_temperature_difference_design",
"high_evaporator_effluent_smoke_enthalpy_design",
"high_economizer_effluent_smoke_temperature_design",
"high_economizer_influent_water_temperature_design",
"high_blowdown_rate_design",
"high_evaporator_effluent_steam_enthalpy_design",
"low_drum_pressure_design",
"low_influent_smoke_enthalpy_design",
"low_steam_enthalpy_design",
"low_evaporat_temperature_design",
"low_evaporator_effluent_steam_enthalpy_design",
"low_proximity_temperature_design",
"low_evaporator_influent_water_enthalpy_design",
"low_node_temperature_design",
"low_evaporator_effluent_smoke_enthalpy_design",
"low_economizer_influent_water_enthalpy_design",
"low_feedwater_enthalpy_design"
ON "public"."ccpp_ccpp"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_ccpp_design"();
