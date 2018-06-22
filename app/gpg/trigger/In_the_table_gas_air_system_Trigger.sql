CREATE OR REPLACE FUNCTION gaspowergeneration_gas_air_system()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段c2s_standard_flux_air:标况流量风,的计算1-----------------------------------
  IF OLD.c2s_standard_pressure_air != NEW.c2s_standard_pressure_air OR OLD.c2s_condition_temperature_air != NEW.c2s_condition_temperature_air OR OLD.c2s_condition_flux_air != NEW.c2s_condition_flux_air OR OLD.c2s_local_atmosphere_air != NEW.c2s_local_atmosphere_air OR OLD.c2s_standard_temperature_air != NEW.c2s_standard_temperature_air THEN
     update gaspowergeneration_gas_air_system set 

     c2s_standard_flux_air=NEW.c2s_condition_flux_air*(NEW.c2s_local_atmosphere_air/NEW.c2s_standard_pressure_air)*((NEW.c2s_standard_temperature_air+273)/(NEW.c2s_condition_temperature_air+273))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c2s_standard_pressure_air ISNULL OR OLD.c2s_standard_temperature_air ISNULL OR OLD.c2s_local_atmosphere_air ISNULL OR OLD.c2s_condition_flux_air ISNULL OR OLD.c2s_condition_temperature_air ISNULL) AND NEW.c2s_standard_pressure_air NOTNULL AND NEW.c2s_standard_temperature_air NOTNULL AND NEW.c2s_local_atmosphere_air NOTNULL AND NEW.c2s_condition_flux_air NOTNULL AND NEW.c2s_condition_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     c2s_standard_flux_air=NEW.c2s_condition_flux_air*(NEW.c2s_local_atmosphere_air/NEW.c2s_standard_pressure_air)*((NEW.c2s_standard_temperature_air+273)/(NEW.c2s_condition_temperature_air+273))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c2s_standard_flux_smoke:标况流量烟,的计算2-----------------------------------
  IF OLD.c2s_standard_pressure_smoke != NEW.c2s_standard_pressure_smoke OR OLD.c2s_condition_temperature_smoke != NEW.c2s_condition_temperature_smoke OR OLD.c2s_condition_flux_smoke != NEW.c2s_condition_flux_smoke OR OLD.c2s_local_atmosphere_smoke != NEW.c2s_local_atmosphere_smoke OR OLD.c2s_standard_temperature_smoke != NEW.c2s_standard_temperature_smoke THEN
     update gaspowergeneration_gas_air_system set 

     c2s_standard_flux_smoke=NEW.c2s_condition_flux_smoke*(NEW.c2s_local_atmosphere_smoke/NEW.c2s_standard_pressure_smoke)*((NEW.c2s_standard_temperature_smoke+273)/(NEW.c2s_condition_temperature_smoke+273))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c2s_standard_pressure_smoke ISNULL OR OLD.c2s_standard_temperature_smoke ISNULL OR OLD.c2s_local_atmosphere_smoke ISNULL OR OLD.c2s_condition_flux_smoke ISNULL OR OLD.c2s_condition_temperature_smoke ISNULL) AND NEW.c2s_standard_pressure_smoke NOTNULL AND NEW.c2s_standard_temperature_smoke NOTNULL AND NEW.c2s_local_atmosphere_smoke NOTNULL AND NEW.c2s_condition_flux_smoke NOTNULL AND NEW.c2s_condition_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     c2s_standard_flux_smoke=NEW.c2s_condition_flux_smoke*(NEW.c2s_local_atmosphere_smoke/NEW.c2s_standard_pressure_smoke)*((NEW.c2s_standard_temperature_smoke+273)/(NEW.c2s_condition_temperature_smoke+273))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s2c_condition_flux_air:工况流量风,的计算3-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     s2c_condition_flux_air=NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     s2c_condition_flux_air=NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s2c_condition_flux_smoke:工况流量烟,的计算4-----------------------------------
  IF OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     s2c_condition_flux_smoke=NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     s2c_condition_flux_smoke=NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s2c_condition_flux_gas:工况流量煤气,的计算5-----------------------------------
  IF OLD.s2c_standard_temperature_gas != NEW.s2c_standard_temperature_gas OR OLD.s2c_standard_pressure_gas != NEW.s2c_standard_pressure_gas OR OLD.s2c_standard_flux_gas != NEW.s2c_standard_flux_gas OR OLD.s2c_condition_temperature_gas != NEW.s2c_condition_temperature_gas OR OLD.s2c_local_atmosphere_gas != NEW.s2c_local_atmosphere_gas THEN
     update gaspowergeneration_gas_air_system set 

     s2c_condition_flux_gas=NEW.s2c_standard_flux_gas*(NEW.s2c_standard_pressure_gas/NEW.s2c_local_atmosphere_gas)*((NEW.s2c_condition_temperature_gas+273)/(NEW.s2c_standard_temperature_gas+273))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_gas ISNULL OR OLD.s2c_condition_temperature_gas ISNULL OR OLD.s2c_standard_flux_gas ISNULL OR OLD.s2c_standard_pressure_gas ISNULL OR OLD.s2c_standard_temperature_gas ISNULL) AND NEW.s2c_local_atmosphere_gas NOTNULL AND NEW.s2c_condition_temperature_gas NOTNULL AND NEW.s2c_standard_flux_gas NOTNULL AND NEW.s2c_standard_pressure_gas NOTNULL AND NEW.s2c_standard_temperature_gas NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     s2c_condition_flux_gas=NEW.s2c_standard_flux_gas*(NEW.s2c_standard_pressure_gas/NEW.s2c_local_atmosphere_gas)*((NEW.s2c_condition_temperature_gas+273)/(NEW.s2c_standard_temperature_gas+273))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_local_atmosphere:当地大气压,的计算6-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     blower_local_atmosphere=NEW.s2c_local_atmosphere_air
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_local_atmosphere=NEW.s2c_local_atmosphere_air
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_condition_smoke_flux:烟风流量（工况）,的计算7-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     blower_condition_smoke_flux=(NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_condition_smoke_flux=(NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_fan_total_pressure:风机全压,的计算8-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.blower_air_temperature != NEW.blower_air_temperature OR OLD.blower_wind_resistance != NEW.blower_wind_resistance OR OLD.blower_fan_temperature != NEW.blower_fan_temperature THEN
     update gaspowergeneration_gas_air_system set 

     blower_fan_total_pressure=NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.blower_fan_temperature ISNULL OR OLD.blower_wind_resistance ISNULL OR OLD.blower_air_temperature ISNULL OR OLD.s2c_local_atmosphere_air ISNULL) AND NEW.blower_fan_temperature NOTNULL AND NEW.blower_wind_resistance NOTNULL AND NEW.blower_air_temperature NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_fan_total_pressure=NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_fan_selected_total_pressure:风机选用全压,的计算9-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.blower_air_temperature != NEW.blower_air_temperature OR OLD.blower_wind_resistance != NEW.blower_wind_resistance OR OLD.blower_fan_temperature != NEW.blower_fan_temperature THEN
     update gaspowergeneration_gas_air_system set 

     blower_fan_selected_total_pressure=(NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature)))*1.15
     where plan_id=NEW.plan_id;

  ELSIF (OLD.blower_fan_temperature ISNULL OR OLD.blower_wind_resistance ISNULL OR OLD.blower_air_temperature ISNULL OR OLD.s2c_local_atmosphere_air ISNULL) AND NEW.blower_fan_temperature NOTNULL AND NEW.blower_wind_resistance NOTNULL AND NEW.blower_air_temperature NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_fan_selected_total_pressure=(NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature)))*1.15
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_fan_selected_flux:风机选用流量,的计算10-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     blower_fan_selected_flux=((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_fan_selected_flux=((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_fan_shaft_power:风机轴功率,的计算11-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.blower_air_temperature != NEW.blower_air_temperature OR OLD.blower_wind_resistance != NEW.blower_wind_resistance OR OLD.blower_fan_temperature != NEW.blower_fan_temperature OR OLD.blower_fan_pressure_efficiency != NEW.blower_fan_pressure_efficiency OR OLD.blower_transmission_efficiency != NEW.blower_transmission_efficiency THEN
     update gaspowergeneration_gas_air_system set 

     blower_fan_shaft_power=((NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature)))*1.15)*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1)/NEW.blower_fan_pressure_efficiency/NEW.blower_transmission_efficiency/3600/9.81/102
     where plan_id=NEW.plan_id;

  ELSIF (OLD.blower_transmission_efficiency ISNULL OR OLD.blower_fan_pressure_efficiency ISNULL OR OLD.blower_fan_temperature ISNULL OR OLD.blower_wind_resistance ISNULL OR OLD.blower_air_temperature ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.blower_transmission_efficiency NOTNULL AND NEW.blower_fan_pressure_efficiency NOTNULL AND NEW.blower_fan_temperature NOTNULL AND NEW.blower_wind_resistance NOTNULL AND NEW.blower_air_temperature NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_fan_shaft_power=((NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature)))*1.15)*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1)/NEW.blower_fan_pressure_efficiency/NEW.blower_transmission_efficiency/3600/9.81/102
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_motor_power:电机功率,的计算12-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.blower_air_temperature != NEW.blower_air_temperature OR OLD.blower_wind_resistance != NEW.blower_wind_resistance OR OLD.blower_fan_temperature != NEW.blower_fan_temperature OR OLD.blower_fan_pressure_efficiency != NEW.blower_fan_pressure_efficiency OR OLD.blower_transmission_efficiency != NEW.blower_transmission_efficiency OR OLD.blower_motor_efficiency != NEW.blower_motor_efficiency OR OLD.blower_motor_safe_margin != NEW.blower_motor_safe_margin THEN
     update gaspowergeneration_gas_air_system set 

     blower_motor_power=NEW.blower_motor_safe_margin*(((NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature)))*1.15)*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1)/NEW.blower_fan_pressure_efficiency/NEW.blower_transmission_efficiency/3600/9.81/102)/NEW.blower_motor_efficiency
     where plan_id=NEW.plan_id;

  ELSIF (OLD.blower_motor_safe_margin ISNULL OR OLD.blower_motor_efficiency ISNULL OR OLD.blower_transmission_efficiency ISNULL OR OLD.blower_fan_pressure_efficiency ISNULL OR OLD.blower_fan_temperature ISNULL OR OLD.blower_wind_resistance ISNULL OR OLD.blower_air_temperature ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.blower_motor_safe_margin NOTNULL AND NEW.blower_motor_efficiency NOTNULL AND NEW.blower_transmission_efficiency NOTNULL AND NEW.blower_fan_pressure_efficiency NOTNULL AND NEW.blower_fan_temperature NOTNULL AND NEW.blower_wind_resistance NOTNULL AND NEW.blower_air_temperature NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_motor_power=NEW.blower_motor_safe_margin*(((NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature)))*1.15)*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1)/NEW.blower_fan_pressure_efficiency/NEW.blower_transmission_efficiency/3600/9.81/102)/NEW.blower_motor_efficiency
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_specification_power:选用规格功率,的计算13-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.blower_air_temperature != NEW.blower_air_temperature OR OLD.blower_wind_resistance != NEW.blower_wind_resistance OR OLD.blower_fan_temperature != NEW.blower_fan_temperature OR OLD.blower_fan_pressure_efficiency != NEW.blower_fan_pressure_efficiency OR OLD.blower_transmission_efficiency != NEW.blower_transmission_efficiency OR OLD.blower_motor_efficiency != NEW.blower_motor_efficiency OR OLD.blower_motor_safe_margin != NEW.blower_motor_safe_margin THEN
     update gaspowergeneration_gas_air_system set 

     blower_specification_power=0.5*(NEW.blower_motor_safe_margin*(((NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature)))*1.15)*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1)/NEW.blower_fan_pressure_efficiency/NEW.blower_transmission_efficiency/3600/9.81/102)/NEW.blower_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.blower_motor_safe_margin ISNULL OR OLD.blower_motor_efficiency ISNULL OR OLD.blower_transmission_efficiency ISNULL OR OLD.blower_fan_pressure_efficiency ISNULL OR OLD.blower_fan_temperature ISNULL OR OLD.blower_wind_resistance ISNULL OR OLD.blower_air_temperature ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.blower_motor_safe_margin NOTNULL AND NEW.blower_motor_efficiency NOTNULL AND NEW.blower_transmission_efficiency NOTNULL AND NEW.blower_fan_pressure_efficiency NOTNULL AND NEW.blower_fan_temperature NOTNULL AND NEW.blower_wind_resistance NOTNULL AND NEW.blower_air_temperature NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_specification_power=0.5*(NEW.blower_motor_safe_margin*(((NEW.blower_wind_resistance*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.blower_air_temperature+273)/(NEW.blower_fan_temperature+273))*1.293/(1.293*273/(273+NEW.blower_air_temperature)))*1.15)*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1)/NEW.blower_fan_pressure_efficiency/NEW.blower_transmission_efficiency/3600/9.81/102)/NEW.blower_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段blower_specification_flux:选用规格流量,的计算14-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     blower_specification_flux=0.5*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     blower_specification_flux=0.5*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2*1.1)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_local_atmosphere:当地大气压,的计算15-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     induced_local_atmosphere=NEW.s2c_local_atmosphere_air
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_local_atmosphere=NEW.s2c_local_atmosphere_air
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_condition_smoke_flux:烟风流量（工况）,的计算16-----------------------------------
  IF OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     induced_condition_smoke_flux=(NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_condition_smoke_flux=(NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_fan_total_pressure:风机全压,的计算17-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.induced_smoke_temperature != NEW.induced_smoke_temperature OR OLD.induced_total_pressure != NEW.induced_total_pressure OR OLD.induced_fan_temperature != NEW.induced_fan_temperature OR OLD.induced_smoke_density != NEW.induced_smoke_density THEN
     update gaspowergeneration_gas_air_system set 

     induced_fan_total_pressure=NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_smoke_density ISNULL OR OLD.induced_fan_temperature ISNULL OR OLD.induced_total_pressure ISNULL OR OLD.induced_smoke_temperature ISNULL OR OLD.s2c_local_atmosphere_air ISNULL) AND NEW.induced_smoke_density NOTNULL AND NEW.induced_fan_temperature NOTNULL AND NEW.induced_total_pressure NOTNULL AND NEW.induced_smoke_temperature NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_fan_total_pressure=NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_fan_selected_total_pressure:风机选用全压,的计算18-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.induced_smoke_temperature != NEW.induced_smoke_temperature OR OLD.induced_total_pressure != NEW.induced_total_pressure OR OLD.induced_fan_temperature != NEW.induced_fan_temperature OR OLD.induced_smoke_density != NEW.induced_smoke_density THEN
     update gaspowergeneration_gas_air_system set 

     induced_fan_selected_total_pressure=(NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density)*1.15
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_smoke_density ISNULL OR OLD.induced_fan_temperature ISNULL OR OLD.induced_total_pressure ISNULL OR OLD.induced_smoke_temperature ISNULL OR OLD.s2c_local_atmosphere_air ISNULL) AND NEW.induced_smoke_density NOTNULL AND NEW.induced_fan_temperature NOTNULL AND NEW.induced_total_pressure NOTNULL AND NEW.induced_smoke_temperature NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_fan_selected_total_pressure=(NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density)*1.15
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_fan_selected_flux:风机选用流量,的计算19-----------------------------------
  IF OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     induced_fan_selected_flux=((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_fan_selected_flux=((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_fan_shaft_power:风机轴功率,的计算20-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke OR OLD.induced_smoke_temperature != NEW.induced_smoke_temperature OR OLD.induced_total_pressure != NEW.induced_total_pressure OR OLD.induced_fan_temperature != NEW.induced_fan_temperature OR OLD.induced_smoke_density != NEW.induced_smoke_density OR OLD.induced_fan_efficiency != NEW.induced_fan_efficiency OR OLD.induced_transmission_efficiency != NEW.induced_transmission_efficiency THEN
     update gaspowergeneration_gas_air_system set 

     induced_fan_shaft_power=((NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density)*1.15)*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1)/NEW.induced_fan_efficiency/NEW.induced_transmission_efficiency/3600/102/9.81
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_transmission_efficiency ISNULL OR OLD.induced_fan_efficiency ISNULL OR OLD.induced_smoke_density ISNULL OR OLD.induced_fan_temperature ISNULL OR OLD.induced_total_pressure ISNULL OR OLD.induced_smoke_temperature ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL OR OLD.s2c_local_atmosphere_air ISNULL) AND NEW.induced_transmission_efficiency NOTNULL AND NEW.induced_fan_efficiency NOTNULL AND NEW.induced_smoke_density NOTNULL AND NEW.induced_fan_temperature NOTNULL AND NEW.induced_total_pressure NOTNULL AND NEW.induced_smoke_temperature NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_fan_shaft_power=((NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density)*1.15)*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1)/NEW.induced_fan_efficiency/NEW.induced_transmission_efficiency/3600/102/9.81
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_motor_power:电机功率,的计算21-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke OR OLD.induced_smoke_temperature != NEW.induced_smoke_temperature OR OLD.induced_total_pressure != NEW.induced_total_pressure OR OLD.induced_fan_temperature != NEW.induced_fan_temperature OR OLD.induced_smoke_density != NEW.induced_smoke_density OR OLD.induced_fan_efficiency != NEW.induced_fan_efficiency OR OLD.induced_transmission_efficiency != NEW.induced_transmission_efficiency OR OLD.induced_motor_efficiency != NEW.induced_motor_efficiency OR OLD.induced_motor_safe_margin != NEW.induced_motor_safe_margin THEN
     update gaspowergeneration_gas_air_system set 

     induced_motor_power=NEW.induced_motor_safe_margin*(((NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density)*1.15)*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1)/NEW.induced_fan_efficiency/NEW.induced_transmission_efficiency/3600/102/9.81)/NEW.induced_motor_efficiency
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_motor_safe_margin ISNULL OR OLD.induced_motor_efficiency ISNULL OR OLD.induced_transmission_efficiency ISNULL OR OLD.induced_fan_efficiency ISNULL OR OLD.induced_smoke_density ISNULL OR OLD.induced_fan_temperature ISNULL OR OLD.induced_total_pressure ISNULL OR OLD.induced_smoke_temperature ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL OR OLD.s2c_local_atmosphere_air ISNULL) AND NEW.induced_motor_safe_margin NOTNULL AND NEW.induced_motor_efficiency NOTNULL AND NEW.induced_transmission_efficiency NOTNULL AND NEW.induced_fan_efficiency NOTNULL AND NEW.induced_smoke_density NOTNULL AND NEW.induced_fan_temperature NOTNULL AND NEW.induced_total_pressure NOTNULL AND NEW.induced_smoke_temperature NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_motor_power=NEW.induced_motor_safe_margin*(((NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density)*1.15)*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1)/NEW.induced_fan_efficiency/NEW.induced_transmission_efficiency/3600/102/9.81)/NEW.induced_motor_efficiency
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_specification_power:选用规格功率,的计算22-----------------------------------
  IF OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke OR OLD.induced_smoke_temperature != NEW.induced_smoke_temperature OR OLD.induced_total_pressure != NEW.induced_total_pressure OR OLD.induced_fan_temperature != NEW.induced_fan_temperature OR OLD.induced_smoke_density != NEW.induced_smoke_density OR OLD.induced_fan_efficiency != NEW.induced_fan_efficiency OR OLD.induced_transmission_efficiency != NEW.induced_transmission_efficiency OR OLD.induced_motor_efficiency != NEW.induced_motor_efficiency OR OLD.induced_motor_safe_margin != NEW.induced_motor_safe_margin THEN
     update gaspowergeneration_gas_air_system set 

     induced_specification_power=0.5*(NEW.induced_motor_safe_margin*(((NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density)*1.15)*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1)/NEW.induced_fan_efficiency/NEW.induced_transmission_efficiency/3600/102/9.81)/NEW.induced_motor_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_motor_safe_margin ISNULL OR OLD.induced_motor_efficiency ISNULL OR OLD.induced_transmission_efficiency ISNULL OR OLD.induced_fan_efficiency ISNULL OR OLD.induced_smoke_density ISNULL OR OLD.induced_fan_temperature ISNULL OR OLD.induced_total_pressure ISNULL OR OLD.induced_smoke_temperature ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL OR OLD.s2c_local_atmosphere_air ISNULL) AND NEW.induced_motor_safe_margin NOTNULL AND NEW.induced_motor_efficiency NOTNULL AND NEW.induced_transmission_efficiency NOTNULL AND NEW.induced_fan_efficiency NOTNULL AND NEW.induced_smoke_density NOTNULL AND NEW.induced_fan_temperature NOTNULL AND NEW.induced_total_pressure NOTNULL AND NEW.induced_smoke_temperature NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_specification_power=0.5*(NEW.induced_motor_safe_margin*(((NEW.induced_total_pressure*(101325/(NEW.s2c_local_atmosphere_air))*((NEW.induced_smoke_temperature+273)/(NEW.induced_fan_temperature+273))*1.293/NEW.induced_smoke_density)*1.15)*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1)/NEW.induced_fan_efficiency/NEW.induced_transmission_efficiency/3600/102/9.81)/NEW.induced_motor_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_specification_flux:选用规格流量,的计算23-----------------------------------
  IF OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     induced_specification_flux=0.5*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     induced_specification_flux=0.5*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2*1.1)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段gas_tube_medium_flux:介质流量,的计算24-----------------------------------
  IF OLD.s2c_standard_temperature_gas != NEW.s2c_standard_temperature_gas OR OLD.s2c_standard_pressure_gas != NEW.s2c_standard_pressure_gas OR OLD.s2c_standard_flux_gas != NEW.s2c_standard_flux_gas OR OLD.s2c_condition_temperature_gas != NEW.s2c_condition_temperature_gas OR OLD.s2c_local_atmosphere_gas != NEW.s2c_local_atmosphere_gas THEN
     update gaspowergeneration_gas_air_system set 

     gas_tube_medium_flux=(NEW.s2c_standard_flux_gas*(NEW.s2c_standard_pressure_gas/NEW.s2c_local_atmosphere_gas)*((NEW.s2c_condition_temperature_gas+273)/(NEW.s2c_standard_temperature_gas+273)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_gas ISNULL OR OLD.s2c_condition_temperature_gas ISNULL OR OLD.s2c_standard_flux_gas ISNULL OR OLD.s2c_standard_pressure_gas ISNULL OR OLD.s2c_standard_temperature_gas ISNULL) AND NEW.s2c_local_atmosphere_gas NOTNULL AND NEW.s2c_condition_temperature_gas NOTNULL AND NEW.s2c_standard_flux_gas NOTNULL AND NEW.s2c_standard_pressure_gas NOTNULL AND NEW.s2c_standard_temperature_gas NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     gas_tube_medium_flux=(NEW.s2c_standard_flux_gas*(NEW.s2c_standard_pressure_gas/NEW.s2c_local_atmosphere_gas)*((NEW.s2c_condition_temperature_gas+273)/(NEW.s2c_standard_temperature_gas+273)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段gas_tube_calculated_cross_sectional_area:计算截面积,的计算25-----------------------------------
  IF OLD.s2c_standard_temperature_gas != NEW.s2c_standard_temperature_gas OR OLD.s2c_standard_pressure_gas != NEW.s2c_standard_pressure_gas OR OLD.s2c_standard_flux_gas != NEW.s2c_standard_flux_gas OR OLD.s2c_condition_temperature_gas != NEW.s2c_condition_temperature_gas OR OLD.s2c_local_atmosphere_gas != NEW.s2c_local_atmosphere_gas OR OLD.gas_tube_flow_velocity != NEW.gas_tube_flow_velocity THEN
     update gaspowergeneration_gas_air_system set 

     gas_tube_calculated_cross_sectional_area=((NEW.s2c_standard_flux_gas*(NEW.s2c_standard_pressure_gas/NEW.s2c_local_atmosphere_gas)*((NEW.s2c_condition_temperature_gas+273)/(NEW.s2c_standard_temperature_gas+273))))/3600/NEW.gas_tube_flow_velocity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.gas_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_gas ISNULL OR OLD.s2c_condition_temperature_gas ISNULL OR OLD.s2c_standard_flux_gas ISNULL OR OLD.s2c_standard_pressure_gas ISNULL OR OLD.s2c_standard_temperature_gas ISNULL) AND NEW.gas_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_gas NOTNULL AND NEW.s2c_condition_temperature_gas NOTNULL AND NEW.s2c_standard_flux_gas NOTNULL AND NEW.s2c_standard_pressure_gas NOTNULL AND NEW.s2c_standard_temperature_gas NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     gas_tube_calculated_cross_sectional_area=((NEW.s2c_standard_flux_gas*(NEW.s2c_standard_pressure_gas/NEW.s2c_local_atmosphere_gas)*((NEW.s2c_condition_temperature_gas+273)/(NEW.s2c_standard_temperature_gas+273))))/3600/NEW.gas_tube_flow_velocity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段gas_tube_calculated_diameter:计算管道直径,的计算26-----------------------------------
  IF OLD.s2c_standard_temperature_gas != NEW.s2c_standard_temperature_gas OR OLD.s2c_standard_pressure_gas != NEW.s2c_standard_pressure_gas OR OLD.s2c_standard_flux_gas != NEW.s2c_standard_flux_gas OR OLD.s2c_condition_temperature_gas != NEW.s2c_condition_temperature_gas OR OLD.s2c_local_atmosphere_gas != NEW.s2c_local_atmosphere_gas OR OLD.gas_tube_flow_velocity != NEW.gas_tube_flow_velocity THEN
     update gaspowergeneration_gas_air_system set 

     gas_tube_calculated_diameter=(4*(((NEW.s2c_standard_flux_gas*(NEW.s2c_standard_pressure_gas/NEW.s2c_local_atmosphere_gas)*((NEW.s2c_condition_temperature_gas+273)/(NEW.s2c_standard_temperature_gas+273))))/3600/NEW.gas_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.gas_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_gas ISNULL OR OLD.s2c_condition_temperature_gas ISNULL OR OLD.s2c_standard_flux_gas ISNULL OR OLD.s2c_standard_pressure_gas ISNULL OR OLD.s2c_standard_temperature_gas ISNULL) AND NEW.gas_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_gas NOTNULL AND NEW.s2c_condition_temperature_gas NOTNULL AND NEW.s2c_standard_flux_gas NOTNULL AND NEW.s2c_standard_pressure_gas NOTNULL AND NEW.s2c_standard_temperature_gas NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     gas_tube_calculated_diameter=(4*(((NEW.s2c_standard_flux_gas*(NEW.s2c_standard_pressure_gas/NEW.s2c_local_atmosphere_gas)*((NEW.s2c_condition_temperature_gas+273)/(NEW.s2c_standard_temperature_gas+273))))/3600/NEW.gas_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段coldwind_tube_medium_flux:介质流量,的计算27-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     coldwind_tube_medium_flux=(NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     coldwind_tube_medium_flux=(NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段coldwind_tube_calculated_cross_sectional_area:计算截面积,的计算28-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.coldwind_tube_flow_velocity != NEW.coldwind_tube_flow_velocity THEN
     update gaspowergeneration_gas_air_system set 

     coldwind_tube_calculated_cross_sectional_area=((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))/2)/3600/NEW.coldwind_tube_flow_velocity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.coldwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.coldwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     coldwind_tube_calculated_cross_sectional_area=((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))/2)/3600/NEW.coldwind_tube_flow_velocity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段coldwind_tube_calculated_diameter:计算当量管道直径,的计算29-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.coldwind_tube_flow_velocity != NEW.coldwind_tube_flow_velocity THEN
     update gaspowergeneration_gas_air_system set 

     coldwind_tube_calculated_diameter=(4*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))/2)/3600/NEW.coldwind_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.coldwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.coldwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     coldwind_tube_calculated_diameter=(4*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))/2)/3600/NEW.coldwind_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段coldwind_tube_width:宽,的计算30-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.coldwind_tube_flow_velocity != NEW.coldwind_tube_flow_velocity OR OLD.coldwind_tube_length != NEW.coldwind_tube_length THEN
     update gaspowergeneration_gas_air_system set 

     coldwind_tube_width=(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))/2)/3600/NEW.coldwind_tube_flow_velocity)/NEW.coldwind_tube_length
     where plan_id=NEW.plan_id;

  ELSIF (OLD.coldwind_tube_length ISNULL OR OLD.coldwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.coldwind_tube_length NOTNULL AND NEW.coldwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     coldwind_tube_width=(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))/2)/3600/NEW.coldwind_tube_flow_velocity)/NEW.coldwind_tube_length
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hotwind_tube_medium_flux:介质流量,的计算31-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     hotwind_tube_medium_flux=(NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     hotwind_tube_medium_flux=(NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hotwind_tube_calculated_cross_sectional_area:计算截面积,的计算32-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.hotwind_tube_flow_velocity != NEW.hotwind_tube_flow_velocity THEN
     update gaspowergeneration_gas_air_system set 

     hotwind_tube_calculated_cross_sectional_area=((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/3600/NEW.hotwind_tube_flow_velocity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hotwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.hotwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     hotwind_tube_calculated_cross_sectional_area=((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/3600/NEW.hotwind_tube_flow_velocity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hotwind_tube_calculated_diameter:计算当量管道直径,的计算33-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.hotwind_tube_flow_velocity != NEW.hotwind_tube_flow_velocity THEN
     update gaspowergeneration_gas_air_system set 

     hotwind_tube_calculated_diameter=(4*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/3600/NEW.hotwind_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hotwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.hotwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     hotwind_tube_calculated_diameter=(4*(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/3600/NEW.hotwind_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hotwind_tube_width:宽,的计算34-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air OR OLD.hotwind_tube_flow_velocity != NEW.hotwind_tube_flow_velocity OR OLD.hotwind_tube_length != NEW.hotwind_tube_length THEN
     update gaspowergeneration_gas_air_system set 

     hotwind_tube_width=(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/3600/NEW.hotwind_tube_flow_velocity)/NEW.hotwind_tube_length
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hotwind_tube_length ISNULL OR OLD.hotwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.hotwind_tube_length NOTNULL AND NEW.hotwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     hotwind_tube_width=(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/3600/NEW.hotwind_tube_flow_velocity)/NEW.hotwind_tube_length
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段total_smoke_tube_medium_flux:介质流量,的计算35-----------------------------------
  IF OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     total_smoke_tube_medium_flux=(NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     total_smoke_tube_medium_flux=(NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段total_smoke_tube_calculated_cross_sectional_area:计算截面积,的计算36-----------------------------------
  IF OLD.total_smoke_tube_flow_velocity != NEW.total_smoke_tube_flow_velocity OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     total_smoke_tube_calculated_cross_sectional_area=((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/3600/NEW.total_smoke_tube_flow_velocity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.total_smoke_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.total_smoke_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     total_smoke_tube_calculated_cross_sectional_area=((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/3600/NEW.total_smoke_tube_flow_velocity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段total_smoke_tube_calculated_diameter:计算当量管道直径,的计算37-----------------------------------
  IF OLD.total_smoke_tube_flow_velocity != NEW.total_smoke_tube_flow_velocity OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     total_smoke_tube_calculated_diameter=(4*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/3600/NEW.total_smoke_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.total_smoke_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.total_smoke_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     total_smoke_tube_calculated_diameter=(4*(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/3600/NEW.total_smoke_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段total_smoke_tube_width:宽,的计算38-----------------------------------
  IF OLD.total_smoke_tube_flow_velocity != NEW.total_smoke_tube_flow_velocity OR OLD.total_smoke_tube_length != NEW.total_smoke_tube_length OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     total_smoke_tube_width=(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/3600/NEW.total_smoke_tube_flow_velocity)/NEW.total_smoke_tube_length
     where plan_id=NEW.plan_id;

  ELSIF (OLD.total_smoke_tube_length ISNULL OR OLD.total_smoke_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.total_smoke_tube_length NOTNULL AND NEW.total_smoke_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     total_smoke_tube_width=(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/3600/NEW.total_smoke_tube_flow_velocity)/NEW.total_smoke_tube_length
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段branch_smoke_tube_medium_flux:介质流量,的计算39-----------------------------------
  IF OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     branch_smoke_tube_medium_flux=((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     branch_smoke_tube_medium_flux=((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段branch_smoke_tube_calculated_cross_sectional_area:计算截面积,的计算40-----------------------------------
  IF OLD.branch_smoke_tube_flow_velocity != NEW.branch_smoke_tube_flow_velocity OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     branch_smoke_tube_calculated_cross_sectional_area=(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2)/3600/NEW.branch_smoke_tube_flow_velocity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.branch_smoke_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.branch_smoke_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     branch_smoke_tube_calculated_cross_sectional_area=(((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2)/3600/NEW.branch_smoke_tube_flow_velocity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段branch_smoke_tube_calculated_diameter:计算当量管道直径,的计算41-----------------------------------
  IF OLD.branch_smoke_tube_flow_velocity != NEW.branch_smoke_tube_flow_velocity OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     branch_smoke_tube_calculated_diameter=(4*((((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2)/3600/NEW.branch_smoke_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.branch_smoke_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.branch_smoke_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     branch_smoke_tube_calculated_diameter=(4*((((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2)/3600/NEW.branch_smoke_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段branch_smoke_tube_width:宽,的计算42-----------------------------------
  IF OLD.branch_smoke_tube_flow_velocity != NEW.branch_smoke_tube_flow_velocity OR OLD.branch_smoke_tube_length != NEW.branch_smoke_tube_length OR OLD.s2c_standard_temperature_smoke != NEW.s2c_standard_temperature_smoke OR OLD.s2c_standard_pressure_smoke != NEW.s2c_standard_pressure_smoke OR OLD.s2c_standard_flux_smoke != NEW.s2c_standard_flux_smoke OR OLD.s2c_condition_temperature_smoke != NEW.s2c_condition_temperature_smoke OR OLD.s2c_local_atmosphere_smoke != NEW.s2c_local_atmosphere_smoke THEN
     update gaspowergeneration_gas_air_system set 

     branch_smoke_tube_width=((((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2)/3600/NEW.branch_smoke_tube_flow_velocity)/NEW.branch_smoke_tube_length
     where plan_id=NEW.plan_id;

  ELSIF (OLD.branch_smoke_tube_length ISNULL OR OLD.branch_smoke_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_smoke ISNULL OR OLD.s2c_condition_temperature_smoke ISNULL OR OLD.s2c_standard_flux_smoke ISNULL OR OLD.s2c_standard_pressure_smoke ISNULL OR OLD.s2c_standard_temperature_smoke ISNULL) AND NEW.branch_smoke_tube_length NOTNULL AND NEW.branch_smoke_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_smoke NOTNULL AND NEW.s2c_condition_temperature_smoke NOTNULL AND NEW.s2c_standard_flux_smoke NOTNULL AND NEW.s2c_standard_pressure_smoke NOTNULL AND NEW.s2c_standard_temperature_smoke NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     branch_smoke_tube_width=((((NEW.s2c_standard_flux_smoke*(NEW.s2c_standard_pressure_smoke/NEW.s2c_local_atmosphere_smoke)*((NEW.s2c_condition_temperature_smoke+273)/(NEW.s2c_standard_temperature_smoke+273))))/2)/3600/NEW.branch_smoke_tube_flow_velocity)/NEW.branch_smoke_tube_length
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_hotwind_tube_medium_flux:介质流量,的计算43-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     main_hotwind_tube_medium_flux=((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     main_hotwind_tube_medium_flux=((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_hotwind_tube_calculated_cross_sectional_area:计算截面积,的计算44-----------------------------------
  IF OLD.main_hotwind_tube_flow_velocity != NEW.main_hotwind_tube_flow_velocity OR OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     main_hotwind_tube_calculated_cross_sectional_area=(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2)/3600/NEW.main_hotwind_tube_flow_velocity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_hotwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.main_hotwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     main_hotwind_tube_calculated_cross_sectional_area=(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2)/3600/NEW.main_hotwind_tube_flow_velocity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_hotwind_tube_calculated_diameter:计算管道直径,的计算45-----------------------------------
  IF OLD.main_hotwind_tube_flow_velocity != NEW.main_hotwind_tube_flow_velocity OR OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     main_hotwind_tube_calculated_diameter=(4*((((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2)/3600/NEW.main_hotwind_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_hotwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.main_hotwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     main_hotwind_tube_calculated_diameter=(4*((((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2)/3600/NEW.main_hotwind_tube_flow_velocity)/3.14)^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段branch_hotwind_tube_medium_flux:介质流量,的计算46-----------------------------------
  IF OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     branch_hotwind_tube_medium_flux=(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2)/3
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     branch_hotwind_tube_medium_flux=(((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2)/3
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段branch_hotwind_tube_calculated_cross_sectional_area:计算截面积,的计算47-----------------------------------
  IF OLD.branch_hotwind_tube_flow_velocity != NEW.branch_hotwind_tube_flow_velocity OR OLD.s2c_standard_temperature_air != NEW.s2c_standard_temperature_air OR OLD.s2c_standard_pressure_air != NEW.s2c_standard_pressure_air OR OLD.s2c_standard_flux_air != NEW.s2c_standard_flux_air OR OLD.s2c_condition_temperature_air != NEW.s2c_condition_temperature_air OR OLD.s2c_local_atmosphere_air != NEW.s2c_local_atmosphere_air THEN
     update gaspowergeneration_gas_air_system set 

     branch_hotwind_tube_calculated_cross_sectional_area=((((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2)/3)/3600/NEW.branch_hotwind_tube_flow_velocity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.branch_hotwind_tube_flow_velocity ISNULL OR OLD.s2c_local_atmosphere_air ISNULL OR OLD.s2c_condition_temperature_air ISNULL OR OLD.s2c_standard_flux_air ISNULL OR OLD.s2c_standard_pressure_air ISNULL OR OLD.s2c_standard_temperature_air ISNULL) AND NEW.branch_hotwind_tube_flow_velocity NOTNULL AND NEW.s2c_local_atmosphere_air NOTNULL AND NEW.s2c_condition_temperature_air NOTNULL AND NEW.s2c_standard_flux_air NOTNULL AND NEW.s2c_standard_pressure_air NOTNULL AND NEW.s2c_standard_temperature_air NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     branch_hotwind_tube_calculated_cross_sectional_area=((((NEW.s2c_standard_flux_air*(NEW.s2c_standard_pressure_air/NEW.s2c_local_atmosphere_air)*((NEW.s2c_condition_temperature_air+273)/(NEW.s2c_standard_temperature_air+273))))/2)/3)/3600/NEW.branch_hotwind_tube_flow_velocity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段standard_calculated_smoke_density:标态下烟气密度,的计算48-----------------------------------
  IF OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature THEN
     update gaspowergeneration_gas_air_system set 

     standard_calculated_smoke_density=NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_inlet_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.local_atmosphere ISNULL) AND NEW.chimney_inlet_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.local_atmosphere NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     standard_calculated_smoke_density=NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_average_temperature:烟囱内平均温度,的计算49-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter THEN
     update gaspowergeneration_gas_air_system set 

     chimney_average_temperature=NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.chimney_height NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_average_temperature=NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_draft:烟囱抽力,的计算50-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_air_density != NEW.standard_air_density OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.outdoor_air_temperature != NEW.outdoor_air_temperature OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter THEN
     update gaspowergeneration_gas_air_system set 

     chimney_draft=9.8*NEW.chimney_height*(NEW.standard_air_density*273/(273+NEW.outdoor_air_temperature)-(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature))*273/(273+(NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height)))*NEW.local_atmosphere/101325
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.outdoor_air_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.standard_air_density ISNULL OR OLD.local_atmosphere ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.outdoor_air_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.standard_air_density NOTNULL AND NEW.local_atmosphere NOTNULL AND NEW.chimney_height NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_draft=9.8*NEW.chimney_height*(NEW.standard_air_density*273/(273+NEW.outdoor_air_temperature)-(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature))*273/(273+(NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height)))*NEW.local_atmosphere/101325
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_outlet_temperature:烟囱出口温度,的计算51-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter THEN
     update gaspowergeneration_gas_air_system set 

     chimney_outlet_temperature=(NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.chimney_height NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_outlet_temperature=(NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_outlet_inner_diameter:烟囱出口内径,的计算52-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter OR OLD.smoke_amount != NEW.smoke_amount OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow THEN
     update gaspowergeneration_gas_air_system set 

     chimney_outlet_inner_diameter=(NEW.smoke_amount*(((NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height))+273)/(3600*273*0.785*NEW.chimney_outlet_flow))^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_flow ISNULL OR OLD.smoke_amount ISNULL OR OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_outlet_flow NOTNULL AND NEW.smoke_amount NOTNULL AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.chimney_height NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_outlet_inner_diameter=(NEW.smoke_amount*(((NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height))+273)/(3600*273*0.785*NEW.chimney_outlet_flow))^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_experience_base_diameter:经验烟囱基础内径,的计算53-----------------------------------
  IF OLD.chimney_outlet_selected_inner_diameter != NEW.chimney_outlet_selected_inner_diameter THEN
     update gaspowergeneration_gas_air_system set 

     chimney_experience_base_diameter=NEW.chimney_outlet_selected_inner_diameter+2*NEW.chimney_outlet_selected_inner_diameter*0.02
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_selected_inner_diameter ISNULL) AND NEW.chimney_outlet_selected_inner_diameter NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_experience_base_diameter=NEW.chimney_outlet_selected_inner_diameter+2*NEW.chimney_outlet_selected_inner_diameter*0.02
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_load_smoke_amount:低负荷下烟气量,的计算54-----------------------------------
  IF OLD.smoke_amount != NEW.smoke_amount THEN
     update gaspowergeneration_gas_air_system set 

     low_load_smoke_amount=0.3*NEW.smoke_amount
     where plan_id=NEW.plan_id;

  ELSIF (OLD.smoke_amount ISNULL) AND NEW.smoke_amount NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     low_load_smoke_amount=0.3*NEW.smoke_amount
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_load_flow_30_percent:30%低负荷校核流速,的计算55-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter OR OLD.smoke_amount != NEW.smoke_amount OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow OR OLD.low_load_smoke_temperature != NEW.low_load_smoke_temperature THEN
     update gaspowergeneration_gas_air_system set 

     low_load_flow_30_percent=(0.3*NEW.smoke_amount)*(273+NEW.low_load_smoke_temperature)/(((NEW.smoke_amount*(((NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height))+273)/(3600*273*0.785*NEW.chimney_outlet_flow))^0.5))^2/3600/273/0.7854
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_load_smoke_temperature ISNULL OR OLD.chimney_outlet_flow ISNULL OR OLD.smoke_amount ISNULL OR OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.chimney_height ISNULL) AND NEW.low_load_smoke_temperature NOTNULL AND NEW.chimney_outlet_flow NOTNULL AND NEW.smoke_amount NOTNULL AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.chimney_height NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     low_load_flow_30_percent=(0.3*NEW.smoke_amount)*(273+NEW.low_load_smoke_temperature)/(((NEW.smoke_amount*(((NEW.chimney_inlet_temperature-0.5*NEW.chimney_temperature_drop_per_meter*NEW.chimney_height))+273)/(3600*273*0.785*NEW.chimney_outlet_flow))^0.5))^2/3600/273/0.7854
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_average_velocity:烟囱内平均流速,的计算56-----------------------------------
  IF OLD.chimney_outlet_flow != NEW.chimney_outlet_flow THEN
     update gaspowergeneration_gas_air_system set 

     chimney_average_velocity=NEW.chimney_outlet_flow
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_flow ISNULL) AND NEW.chimney_outlet_flow NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_average_velocity=NEW.chimney_outlet_flow
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_average_diameter:烟囱平均直径,的计算57-----------------------------------
  IF OLD.chimney_outlet_selected_inner_diameter != NEW.chimney_outlet_selected_inner_diameter THEN
     update gaspowergeneration_gas_air_system set 

     chimney_average_diameter=((NEW.chimney_outlet_selected_inner_diameter+2*NEW.chimney_outlet_selected_inner_diameter*0.02)+NEW.chimney_outlet_selected_inner_diameter)/2/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_selected_inner_diameter ISNULL) AND NEW.chimney_outlet_selected_inner_diameter NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_average_diameter=((NEW.chimney_outlet_selected_inner_diameter+2*NEW.chimney_outlet_selected_inner_diameter*0.02)+NEW.chimney_outlet_selected_inner_diameter)/2/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_friction_resistance:烟囱摩擦阻力,的计算58-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow OR OLD.chimney_outlet_selected_inner_diameter != NEW.chimney_outlet_selected_inner_diameter OR OLD.chimney_resistance_coefficient != NEW.chimney_resistance_coefficient THEN
     update gaspowergeneration_gas_air_system set 

     chimney_friction_resistance=NEW.chimney_resistance_coefficient*NEW.chimney_height*(NEW.chimney_outlet_flow)*(NEW.chimney_outlet_flow)/(((NEW.chimney_outlet_selected_inner_diameter+2*NEW.chimney_outlet_selected_inner_diameter*0.02)+NEW.chimney_outlet_selected_inner_diameter)/2/1000)/2*(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_resistance_coefficient ISNULL OR OLD.chimney_outlet_selected_inner_diameter ISNULL OR OLD.chimney_outlet_flow ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.local_atmosphere ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_resistance_coefficient NOTNULL AND NEW.chimney_outlet_selected_inner_diameter NOTNULL AND NEW.chimney_outlet_flow NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.local_atmosphere NOTNULL AND NEW.chimney_height NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_friction_resistance=NEW.chimney_resistance_coefficient*NEW.chimney_height*(NEW.chimney_outlet_flow)*(NEW.chimney_outlet_flow)/(((NEW.chimney_outlet_selected_inner_diameter+2*NEW.chimney_outlet_selected_inner_diameter*0.02)+NEW.chimney_outlet_selected_inner_diameter)/2/1000)/2*(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_outlet_resistance:烟囱出口阻力,的计算59-----------------------------------
  IF OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow OR OLD.chimney_outlet_resistance_coefficient != NEW.chimney_outlet_resistance_coefficient THEN
     update gaspowergeneration_gas_air_system set 

     chimney_outlet_resistance=NEW.chimney_outlet_resistance_coefficient*(NEW.chimney_outlet_flow)*(NEW.chimney_outlet_flow)/2*(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_resistance_coefficient ISNULL OR OLD.chimney_outlet_flow ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.local_atmosphere ISNULL) AND NEW.chimney_outlet_resistance_coefficient NOTNULL AND NEW.chimney_outlet_flow NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.local_atmosphere NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_outlet_resistance=NEW.chimney_outlet_resistance_coefficient*(NEW.chimney_outlet_flow)*(NEW.chimney_outlet_flow)/2*(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_total_resistance:烟囱总阻力,的计算60-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow OR OLD.chimney_outlet_selected_inner_diameter != NEW.chimney_outlet_selected_inner_diameter OR OLD.chimney_resistance_coefficient != NEW.chimney_resistance_coefficient OR OLD.chimney_outlet_resistance_coefficient != NEW.chimney_outlet_resistance_coefficient THEN
     update gaspowergeneration_gas_air_system set 

     chimney_total_resistance=(NEW.chimney_outlet_resistance_coefficient*(NEW.chimney_outlet_flow)*(NEW.chimney_outlet_flow)/2*(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature)))+(NEW.chimney_resistance_coefficient*NEW.chimney_height*(NEW.chimney_outlet_flow)*(NEW.chimney_outlet_flow)/(((NEW.chimney_outlet_selected_inner_diameter+2*NEW.chimney_outlet_selected_inner_diameter*0.02)+NEW.chimney_outlet_selected_inner_diameter)/2/1000)/2*(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_resistance_coefficient ISNULL OR OLD.chimney_resistance_coefficient ISNULL OR OLD.chimney_outlet_selected_inner_diameter ISNULL OR OLD.chimney_outlet_flow ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.local_atmosphere ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_outlet_resistance_coefficient NOTNULL AND NEW.chimney_resistance_coefficient NOTNULL AND NEW.chimney_outlet_selected_inner_diameter NOTNULL AND NEW.chimney_outlet_flow NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.local_atmosphere NOTNULL AND NEW.chimney_height NOTNULL THEN
     update gaspowergeneration_gas_air_system set 

     chimney_total_resistance=(NEW.chimney_outlet_resistance_coefficient*(NEW.chimney_outlet_flow)*(NEW.chimney_outlet_flow)/2*(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature)))+(NEW.chimney_resistance_coefficient*NEW.chimney_height*(NEW.chimney_outlet_flow)*(NEW.chimney_outlet_flow)/(((NEW.chimney_outlet_selected_inner_diameter+2*NEW.chimney_outlet_selected_inner_diameter*0.02)+NEW.chimney_outlet_selected_inner_diameter)/2/1000)/2*(NEW.standard_average_smoke_density*273*NEW.local_atmosphere/101325/(273+NEW.chimney_inlet_temperature)))
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_gas_air_system" AFTER UPDATE OF
"c2s_standard_pressure_air",
"total_smoke_tube_flow_velocity",
"total_smoke_tube_length",
"c2s_standard_pressure_smoke",
"branch_smoke_tube_flow_velocity",
"branch_smoke_tube_length",
"main_hotwind_tube_flow_velocity",
"branch_hotwind_tube_flow_velocity",
"chimney_height",
"local_atmosphere",
"standard_air_density",
"standard_average_smoke_density",
"outdoor_air_temperature",
"chimney_inlet_temperature",
"chimney_temperature_drop_per_meter",
"smoke_amount",
"s2c_standard_temperature_air",
"chimney_outlet_flow",
"chimney_outlet_selected_inner_diameter",
"low_load_smoke_temperature",
"chimney_resistance_coefficient",
"s2c_standard_pressure_air",
"chimney_outlet_resistance_coefficient",
"s2c_standard_flux_air",
"s2c_condition_temperature_air",
"s2c_local_atmosphere_air",
"c2s_condition_temperature_air",
"s2c_standard_temperature_smoke",
"s2c_standard_pressure_smoke",
"s2c_standard_flux_smoke",
"s2c_condition_temperature_smoke",
"s2c_local_atmosphere_smoke",
"s2c_standard_temperature_gas",
"s2c_standard_pressure_gas",
"s2c_standard_flux_gas",
"c2s_condition_flux_air",
"s2c_condition_temperature_gas",
"s2c_local_atmosphere_gas",
"blower_air_temperature",
"blower_wind_resistance",
"c2s_condition_temperature_smoke",
"blower_fan_temperature",
"blower_fan_pressure_efficiency",
"blower_transmission_efficiency",
"blower_motor_efficiency",
"blower_motor_safe_margin",
"c2s_condition_flux_smoke",
"induced_smoke_temperature",
"induced_total_pressure",
"c2s_local_atmosphere_air",
"induced_fan_temperature",
"induced_smoke_density",
"induced_fan_efficiency",
"induced_transmission_efficiency",
"induced_motor_efficiency",
"induced_motor_safe_margin",
"c2s_local_atmosphere_smoke",
"gas_tube_flow_velocity",
"c2s_standard_temperature_air",
"coldwind_tube_flow_velocity",
"coldwind_tube_length",
"c2s_standard_temperature_smoke",
"hotwind_tube_flow_velocity",
"hotwind_tube_length"
ON "public"."gaspowergeneration_gas_air_system"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_gas_air_system"();

