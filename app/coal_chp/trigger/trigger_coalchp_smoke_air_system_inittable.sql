CREATE OR REPLACE FUNCTION coalchp_smoke_air_system()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段a_atmospheric_pressure:大气压,的计算1-----------------------------------
  IF OLD.a_altitude != NEW.a_altitude THEN
     update coalchp_smoke_air_system set 

     a_atmospheric_pressure=1013.25*(1-NEW.a_altitude/44330)^5.255*100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_altitude ISNULL) AND NEW.a_altitude NOTNULL THEN
     update coalchp_smoke_air_system set 

     a_atmospheric_pressure=1013.25*(1-NEW.a_altitude/44330)^5.255*100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_local_atmosphere:当地大气压,的计算3-----------------------------------
  IF OLD.p_local_atmosphere_f != NEW.p_local_atmosphere_f THEN
     update coalchp_smoke_air_system set 

     f_local_atmosphere=NEW.p_local_atmosphere_f,
     p_local_atmosphere_s=NEW.p_local_atmosphere_f,
     p_local_atmosphere_t=NEW.p_local_atmosphere_f
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_local_atmosphere_f ISNULL) AND NEW.p_local_atmosphere_f NOTNULL THEN
     update coalchp_smoke_air_system set 

     f_local_atmosphere=NEW.p_local_atmosphere_f,
     p_local_atmosphere_s=NEW.p_local_atmosphere_f,
     p_local_atmosphere_t=NEW.p_local_atmosphere_f
     where plan_id=NEW.plan_id;

  END IF;
  ----------------------实现字段p_operational_point_flow_f:工况流量,的计算2-----------------------------------
  IF OLD.p_the_case_temperature_f != NEW.p_the_case_temperature_f OR OLD.p_standard_of_pressure_f != NEW.p_standard_of_pressure_f OR OLD.p_standard_of_flow_f != NEW.p_standard_of_flow_f OR OLD.p_temperature_case_f != NEW.p_temperature_case_f OR OLD.p_local_atmosphere_f != NEW.p_local_atmosphere_f
     OR OLD.p_the_case_temperature_s != NEW.p_the_case_temperature_s OR OLD.p_standard_of_pressure_s != NEW.p_standard_of_pressure_s OR OLD.p_standard_of_flow_s != NEW.p_standard_of_flow_s OR OLD.p_temperature_case_s != NEW.p_temperature_case_s OR OLD.p_local_atmosphere_s != NEW.p_local_atmosphere_f
     OR OLD.p_the_case_temperature_t != NEW.p_the_case_temperature_t OR OLD.p_standard_of_pressure_t != NEW.p_standard_of_pressure_t OR OLD.p_standard_of_flow_t != NEW.p_standard_of_flow_t OR OLD.p_temperature_case_t != NEW.p_temperature_case_t OR OLD.p_local_atmosphere_t != NEW.p_local_atmosphere_f
  THEN
     update coalchp_smoke_air_system set 

     p_operational_point_flow_f=NEW.p_standard_of_flow_f*(NEW.p_standard_of_pressure_f/NEW.p_local_atmosphere_f)*((NEW.p_temperature_case_f+273)/(NEW.p_the_case_temperature_f+273))
     ,p_operational_point_flow_s=NEW.p_standard_of_flow_s*(NEW.p_standard_of_pressure_s/NEW.p_local_atmosphere_s)*((NEW.p_temperature_case_s+273)/(NEW.p_the_case_temperature_s+273))
     ,p_operational_point_flow_t=NEW.p_standard_of_flow_t*(NEW.p_standard_of_pressure_t/NEW.p_local_atmosphere_t)*((NEW.p_temperature_case_t+273)/(NEW.p_the_case_temperature_t+273))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_local_atmosphere_f ISNULL OR OLD.p_temperature_case_f ISNULL OR OLD.p_standard_of_flow_f ISNULL OR OLD.p_standard_of_pressure_f ISNULL OR OLD.p_the_case_temperature_f ISNULL) AND NEW.p_local_atmosphere_f NOTNULL AND NEW.p_temperature_case_f NOTNULL AND NEW.p_standard_of_flow_f NOTNULL AND NEW.p_standard_of_pressure_f NOTNULL AND NEW.p_the_case_temperature_f NOTNULL 
				 AND (OLD.p_local_atmosphere_s ISNULL OR OLD.p_temperature_case_s ISNULL OR OLD.p_standard_of_flow_s ISNULL OR OLD.p_standard_of_pressure_s ISNULL OR OLD.p_the_case_temperature_s ISNULL) AND NEW.p_local_atmosphere_s NOTNULL AND NEW.p_temperature_case_s NOTNULL AND NEW.p_standard_of_flow_s NOTNULL AND NEW.p_standard_of_pressure_s NOTNULL AND NEW.p_the_case_temperature_s NOTNULL 
				 AND (OLD.p_local_atmosphere_t ISNULL OR OLD.p_temperature_case_t ISNULL OR OLD.p_standard_of_flow_t ISNULL OR OLD.p_standard_of_pressure_t ISNULL OR OLD.p_the_case_temperature_t ISNULL) AND NEW.p_local_atmosphere_t NOTNULL AND NEW.p_temperature_case_t NOTNULL AND NEW.p_standard_of_flow_t NOTNULL AND NEW.p_standard_of_pressure_t NOTNULL AND NEW.p_the_case_temperature_t NOTNULL 
	THEN
     update coalchp_smoke_air_system set 

     p_operational_point_flow_f=NEW.p_standard_of_flow_f*(NEW.p_standard_of_pressure_f/NEW.p_local_atmosphere_f)*((NEW.p_temperature_case_f+273)/(NEW.p_the_case_temperature_f+273))
     ,p_operational_point_flow_s=NEW.p_standard_of_flow_s*(NEW.p_standard_of_pressure_s/NEW.p_local_atmosphere_s)*((NEW.p_temperature_case_s+273)/(NEW.p_the_case_temperature_s+273))
     ,p_operational_point_flow_t=NEW.p_standard_of_flow_t*(NEW.p_standard_of_pressure_t/NEW.p_local_atmosphere_t)*((NEW.p_temperature_case_t+273)/(NEW.p_the_case_temperature_t+273))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_fan_total_pressure:风机全压,的计算4-----------------------------------
  IF OLD.f_air_temperature != NEW.f_air_temperature OR OLD.f_boiler_body_resistance != NEW.f_boiler_body_resistance OR OLD.f_duct_resistance != NEW.f_duct_resistance OR OLD.f_local_atmosphere != NEW.f_local_atmosphere OR OLD.f_nameplate_medium_temperature != NEW.f_nameplate_medium_temperature THEN
     update coalchp_smoke_air_system set 

     f_fan_total_pressure=NEW.f_boiler_body_resistance+NEW.f_duct_resistance*(101325/NEW.f_local_atmosphere)*((NEW.f_air_temperature+273)/(NEW.f_nameplate_medium_temperature+273))*1.293/(1.293*273/(273+NEW.f_air_temperature))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_nameplate_medium_temperature ISNULL OR OLD.f_local_atmosphere ISNULL OR OLD.f_duct_resistance ISNULL OR OLD.f_boiler_body_resistance ISNULL OR OLD.f_air_temperature ISNULL) AND NEW.f_nameplate_medium_temperature NOTNULL AND NEW.f_local_atmosphere NOTNULL AND NEW.f_duct_resistance NOTNULL AND NEW.f_boiler_body_resistance NOTNULL AND NEW.f_air_temperature NOTNULL THEN
     update coalchp_smoke_air_system set 

     f_fan_total_pressure=NEW.f_boiler_body_resistance+NEW.f_duct_resistance*(101325/NEW.f_local_atmosphere)*((NEW.f_air_temperature+273)/(NEW.f_nameplate_medium_temperature+273))*1.293/(1.293*273/(273+NEW.f_air_temperature))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_fan_select_total_pressure:风机选用全压,的计算5-----------------------------------
  IF OLD.f_fan_total_pressure != NEW.f_fan_total_pressure THEN
     update coalchp_smoke_air_system set 

     f_fan_select_total_pressure=NEW.f_fan_total_pressure*1.2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_fan_total_pressure ISNULL) AND NEW.f_fan_total_pressure NOTNULL THEN
     update coalchp_smoke_air_system set 

     f_fan_select_total_pressure=NEW.f_fan_total_pressure*1.2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_fan_selection_flow:风机选用流量,的计算6-----------------------------------
  IF OLD.f_smoke_flow_rate_condition != NEW.f_smoke_flow_rate_condition THEN
     update coalchp_smoke_air_system set 

     f_fan_selection_flow=NEW.f_smoke_flow_rate_condition*1.3
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_smoke_flow_rate_condition ISNULL) AND NEW.f_smoke_flow_rate_condition NOTNULL THEN
     update coalchp_smoke_air_system set 

     f_fan_selection_flow=NEW.f_smoke_flow_rate_condition*1.3
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_fan_shaft_power:风机轴功率,的计算7-----------------------------------
  IF OLD.f_fan_select_total_pressure != NEW.f_fan_select_total_pressure OR OLD.f_fan_selection_flow != NEW.f_fan_selection_flow OR OLD.f_fan_power != NEW.f_fan_power THEN
     update coalchp_smoke_air_system set 

     f_fan_shaft_power=NEW.f_fan_select_total_pressure*NEW.f_fan_selection_flow/NEW.f_fan_power/3600/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_fan_power ISNULL OR OLD.f_fan_selection_flow ISNULL OR OLD.f_fan_select_total_pressure ISNULL) AND NEW.f_fan_power NOTNULL AND NEW.f_fan_selection_flow NOTNULL AND NEW.f_fan_select_total_pressure NOTNULL THEN
     update coalchp_smoke_air_system set 

     f_fan_shaft_power=NEW.f_fan_select_total_pressure*NEW.f_fan_selection_flow/NEW.f_fan_power/3600/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_motor_power:电机功率,的计算8-----------------------------------
  IF OLD.f_electric_motor_power != NEW.f_electric_motor_power OR OLD.f_fan_shaft_power != NEW.f_fan_shaft_power OR OLD.f_fan_security_volumn != NEW.f_fan_security_volumn THEN
     update coalchp_smoke_air_system set 

     f_motor_power=NEW.f_fan_security_volumn*NEW.f_fan_shaft_power/NEW.f_electric_motor_power
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_fan_security_volumn ISNULL OR OLD.f_fan_shaft_power ISNULL OR OLD.f_electric_motor_power ISNULL) AND NEW.f_fan_security_volumn NOTNULL AND NEW.f_fan_shaft_power NOTNULL AND NEW.f_electric_motor_power NOTNULL THEN
     update coalchp_smoke_air_system set 

     f_motor_power=NEW.f_fan_security_volumn*NEW.f_fan_shaft_power/NEW.f_electric_motor_power
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_local_atmosphere:当地大气压,的计算9-----------------------------------
  IF OLD.p_local_atmosphere_f != NEW.p_local_atmosphere_f THEN
     update coalchp_smoke_air_system set 

     s_local_atmosphere=NEW.p_local_atmosphere_f
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_local_atmosphere_f ISNULL) AND NEW.p_local_atmosphere_f NOTNULL THEN
     update coalchp_smoke_air_system set 

     s_local_atmosphere=NEW.p_local_atmosphere_f
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_fan_total_pressure:风机全压,的计算10-----------------------------------
  IF OLD.s_boiler_body_resistance != NEW.s_boiler_body_resistance OR OLD.s_duct_resistance != NEW.s_duct_resistance OR OLD.s_local_atmosphere != NEW.s_local_atmosphere THEN
     update coalchp_smoke_air_system set 

     s_fan_total_pressure=NEW.s_boiler_body_resistance+NEW.s_duct_resistance*(101325/NEW.s_local_atmosphere)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_local_atmosphere ISNULL OR OLD.s_duct_resistance ISNULL OR OLD.s_boiler_body_resistance ISNULL) AND NEW.s_local_atmosphere NOTNULL AND NEW.s_duct_resistance NOTNULL AND NEW.s_boiler_body_resistance NOTNULL THEN
     update coalchp_smoke_air_system set 

     s_fan_total_pressure=NEW.s_boiler_body_resistance+NEW.s_duct_resistance*(101325/NEW.s_local_atmosphere)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_fan_select_total_pressure:风机选用全压,的计算11-----------------------------------
  IF OLD.s_fan_total_pressure != NEW.s_fan_total_pressure THEN
     update coalchp_smoke_air_system set 

     s_fan_select_total_pressure=NEW.s_fan_total_pressure*1.2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_fan_total_pressure ISNULL) AND NEW.s_fan_total_pressure NOTNULL THEN
     update coalchp_smoke_air_system set 

     s_fan_select_total_pressure=NEW.s_fan_total_pressure*1.2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_fan_selection_flow:风机选用流量,的计算12-----------------------------------
  IF OLD.s_smoke_flow_rate_condition != NEW.s_smoke_flow_rate_condition THEN
     update coalchp_smoke_air_system set 

     s_fan_selection_flow=NEW.s_smoke_flow_rate_condition*1.3
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_smoke_flow_rate_condition ISNULL) AND NEW.s_smoke_flow_rate_condition NOTNULL THEN
     update coalchp_smoke_air_system set 

     s_fan_selection_flow=NEW.s_smoke_flow_rate_condition*1.3
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_fan_shaft_power:风机轴功率,的计算13-----------------------------------
  IF OLD.s_fan_select_total_pressure != NEW.s_fan_select_total_pressure OR OLD.s_fan_selection_flow != NEW.s_fan_selection_flow OR OLD.s_fan_power != NEW.s_fan_power THEN
     update coalchp_smoke_air_system set 

     s_fan_shaft_power=NEW.s_fan_select_total_pressure*NEW.s_fan_selection_flow/NEW.s_fan_power/3600/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_fan_power ISNULL OR OLD.s_fan_selection_flow ISNULL OR OLD.s_fan_select_total_pressure ISNULL) AND NEW.s_fan_power NOTNULL AND NEW.s_fan_selection_flow NOTNULL AND NEW.s_fan_select_total_pressure NOTNULL THEN
     update coalchp_smoke_air_system set 

     s_fan_shaft_power=NEW.s_fan_select_total_pressure*NEW.s_fan_selection_flow/NEW.s_fan_power/3600/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_motor_power:电机功率,的计算14-----------------------------------
  IF OLD.s_electric_motor_power != NEW.s_electric_motor_power OR OLD.s_fan_shaft_power != NEW.s_fan_shaft_power OR OLD.s_fan_security_volumn != NEW.s_fan_security_volumn THEN
     update coalchp_smoke_air_system set 

     s_motor_power=NEW.s_fan_security_volumn*NEW.s_fan_shaft_power/NEW.s_electric_motor_power
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_fan_security_volumn ISNULL OR OLD.s_fan_shaft_power ISNULL OR OLD.s_electric_motor_power ISNULL) AND NEW.s_fan_security_volumn NOTNULL AND NEW.s_fan_shaft_power NOTNULL AND NEW.s_electric_motor_power NOTNULL THEN
     update coalchp_smoke_air_system set 

     s_motor_power=NEW.s_fan_security_volumn*NEW.s_fan_shaft_power/NEW.s_electric_motor_power
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_local_atmosphere:当地大气压,的计算15-----------------------------------
  IF OLD.p_local_atmosphere_f != NEW.p_local_atmosphere_f THEN
     update coalchp_smoke_air_system set 

     i_local_atmosphere=NEW.p_local_atmosphere_f
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_local_atmosphere_f ISNULL) AND NEW.p_local_atmosphere_f NOTNULL THEN
     update coalchp_smoke_air_system set 

     i_local_atmosphere=NEW.p_local_atmosphere_f
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_fan_total_pressure:风机全压,的计算16-----------------------------------
  IF OLD.i_boiler_body_resistance != NEW.i_boiler_body_resistance OR OLD.i_denitration != NEW.i_denitration OR OLD.i_duster != NEW.i_duster OR OLD.i_duct_resistance != NEW.i_duct_resistance OR OLD.i_resistance_desulfurization_fan != NEW.i_resistance_desulfurization_fan OR OLD.i_local_atmosphere != NEW.i_local_atmosphere THEN
     update coalchp_smoke_air_system set 

     i_fan_total_pressure=NEW.i_boiler_body_resistance+(NEW.i_duct_resistance+NEW.i_denitration+NEW.i_duster+NEW.i_resistance_desulfurization_fan)*(101325/NEW.i_local_atmosphere)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_local_atmosphere ISNULL OR OLD.i_resistance_desulfurization_fan ISNULL OR OLD.i_duct_resistance ISNULL OR OLD.i_duster ISNULL OR OLD.i_denitration ISNULL OR OLD.i_boiler_body_resistance ISNULL) AND NEW.i_local_atmosphere NOTNULL AND NEW.i_resistance_desulfurization_fan NOTNULL AND NEW.i_duct_resistance NOTNULL AND NEW.i_duster NOTNULL AND NEW.i_denitration NOTNULL AND NEW.i_boiler_body_resistance NOTNULL THEN
     update coalchp_smoke_air_system set 

     i_fan_total_pressure=NEW.i_boiler_body_resistance+(NEW.i_duct_resistance+NEW.i_denitration+NEW.i_duster+NEW.i_resistance_desulfurization_fan)*(101325/NEW.i_local_atmosphere)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_fan_select_total_pressure:风机选用全压,的计算17-----------------------------------
  IF OLD.i_fan_total_pressure != NEW.i_fan_total_pressure THEN
     update coalchp_smoke_air_system set 

     i_fan_select_total_pressure=NEW.i_fan_total_pressure*1.2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_fan_total_pressure ISNULL) AND NEW.i_fan_total_pressure NOTNULL THEN
     update coalchp_smoke_air_system set 

     i_fan_select_total_pressure=NEW.i_fan_total_pressure*1.2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_fan_selection_flow:风机选用流量,的计算18-----------------------------------
  IF OLD.i_smoke_flow_rate_condition != NEW.i_smoke_flow_rate_condition THEN
     update coalchp_smoke_air_system set 

     i_fan_selection_flow=NEW.i_smoke_flow_rate_condition*1.1
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_smoke_flow_rate_condition ISNULL) AND NEW.i_smoke_flow_rate_condition NOTNULL THEN
     update coalchp_smoke_air_system set 

     i_fan_selection_flow=NEW.i_smoke_flow_rate_condition*1.1
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_fan_shaft_power:风机轴功率,的计算19-----------------------------------
  IF OLD.i_fan_select_total_pressure != NEW.i_fan_select_total_pressure OR OLD.i_fan_selection_flow != NEW.i_fan_selection_flow OR OLD.i_fan_power != NEW.i_fan_power THEN
     update coalchp_smoke_air_system set 

     i_fan_shaft_power=NEW.i_fan_select_total_pressure*NEW.i_fan_selection_flow/NEW.i_fan_power/3600/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_fan_power ISNULL OR OLD.i_fan_selection_flow ISNULL OR OLD.i_fan_select_total_pressure ISNULL) AND NEW.i_fan_power NOTNULL AND NEW.i_fan_selection_flow NOTNULL AND NEW.i_fan_select_total_pressure NOTNULL THEN
     update coalchp_smoke_air_system set 

     i_fan_shaft_power=NEW.i_fan_select_total_pressure*NEW.i_fan_selection_flow/NEW.i_fan_power/3600/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_motor_power:电机功率,的计算20-----------------------------------
  IF OLD.i_electric_motor_power != NEW.i_electric_motor_power OR OLD.i_fan_shaft_power != NEW.i_fan_shaft_power OR OLD.i_fan_security_volumn != NEW.i_fan_security_volumn THEN
     update coalchp_smoke_air_system set 

     i_motor_power=NEW.i_fan_security_volumn*NEW.i_fan_shaft_power/NEW.i_electric_motor_power
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_fan_security_volumn ISNULL OR OLD.i_fan_shaft_power ISNULL OR OLD.i_electric_motor_power ISNULL) AND NEW.i_fan_security_volumn NOTNULL AND NEW.i_fan_shaft_power NOTNULL AND NEW.i_electric_motor_power NOTNULL THEN
     update coalchp_smoke_air_system set 

     i_motor_power=NEW.i_fan_security_volumn*NEW.i_fan_shaft_power/NEW.i_electric_motor_power
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_local_atmosphere:当地大气压,的计算21-----------------------------------
  IF OLD.p_local_atmosphere_f != NEW.p_local_atmosphere_f THEN
     update coalchp_smoke_air_system set 

     r_local_atmosphere=NEW.p_local_atmosphere_f
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_local_atmosphere_f ISNULL) AND NEW.p_local_atmosphere_f NOTNULL THEN
     update coalchp_smoke_air_system set 

     r_local_atmosphere=NEW.p_local_atmosphere_f
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_fan_total_pressure:风机全压,的计算22-----------------------------------
  IF OLD.r_boiler_body_resistance != NEW.r_boiler_body_resistance OR OLD.r_duct_resistance != NEW.r_duct_resistance OR OLD.r_local_atmosphere != NEW.r_local_atmosphere THEN
     update coalchp_smoke_air_system set 

     r_fan_total_pressure=NEW.r_boiler_body_resistance+NEW.r_duct_resistance*(101325/NEW.r_local_atmosphere)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_local_atmosphere ISNULL OR OLD.r_duct_resistance ISNULL OR OLD.r_boiler_body_resistance ISNULL) AND NEW.r_local_atmosphere NOTNULL AND NEW.r_duct_resistance NOTNULL AND NEW.r_boiler_body_resistance NOTNULL THEN
     update coalchp_smoke_air_system set 

     r_fan_total_pressure=NEW.r_boiler_body_resistance+NEW.r_duct_resistance*(101325/NEW.r_local_atmosphere)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_fan_select_total_pressure:风机选用全压,的计算23-----------------------------------
  IF OLD.r_fan_total_pressure != NEW.r_fan_total_pressure THEN
     update coalchp_smoke_air_system set 

     r_fan_select_total_pressure=NEW.r_fan_total_pressure*1.2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_fan_total_pressure ISNULL) AND NEW.r_fan_total_pressure NOTNULL THEN
     update coalchp_smoke_air_system set 

     r_fan_select_total_pressure=NEW.r_fan_total_pressure*1.2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_fan_selection_flow:风机选用流量,的计算24-----------------------------------
  IF OLD.r_smoke_flow_rate_condition != NEW.r_smoke_flow_rate_condition THEN
     update coalchp_smoke_air_system set 

     r_fan_selection_flow=NEW.r_smoke_flow_rate_condition*1.3
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_smoke_flow_rate_condition ISNULL) AND NEW.r_smoke_flow_rate_condition NOTNULL THEN
     update coalchp_smoke_air_system set 

     r_fan_selection_flow=NEW.r_smoke_flow_rate_condition*1.3
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_fan_shaft_power:风机轴功率,的计算25-----------------------------------
  IF OLD.r_fan_select_total_pressure != NEW.r_fan_select_total_pressure OR OLD.r_fan_selection_flow != NEW.r_fan_selection_flow OR OLD.r_fan_power != NEW.r_fan_power THEN
     update coalchp_smoke_air_system set 

     r_fan_shaft_power=NEW.r_fan_select_total_pressure*NEW.r_fan_selection_flow/NEW.r_fan_power/3600/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_fan_power ISNULL OR OLD.r_fan_selection_flow ISNULL OR OLD.r_fan_select_total_pressure ISNULL) AND NEW.r_fan_power NOTNULL AND NEW.r_fan_selection_flow NOTNULL AND NEW.r_fan_select_total_pressure NOTNULL THEN
     update coalchp_smoke_air_system set 

     r_fan_shaft_power=NEW.r_fan_select_total_pressure*NEW.r_fan_selection_flow/NEW.r_fan_power/3600/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_motor_power:电机功率,的计算26-----------------------------------
  IF OLD.r_electric_motor_power != NEW.r_electric_motor_power OR OLD.r_fan_shaft_power != NEW.r_fan_shaft_power OR OLD.r_fan_security_volumn != NEW.r_fan_security_volumn THEN
     update coalchp_smoke_air_system set 

     r_motor_power=NEW.r_fan_security_volumn*NEW.r_fan_shaft_power/NEW.r_electric_motor_power
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_fan_security_volumn ISNULL OR OLD.r_fan_shaft_power ISNULL OR OLD.r_electric_motor_power ISNULL) AND NEW.r_fan_security_volumn NOTNULL AND NEW.r_fan_shaft_power NOTNULL AND NEW.r_electric_motor_power NOTNULL THEN
     update coalchp_smoke_air_system set 

     r_motor_power=NEW.r_fan_security_volumn*NEW.r_fan_shaft_power/NEW.r_electric_motor_power
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_smoke_air_system" AFTER UPDATE OF
"p_the_case_temperature_f",
"p_the_case_temperature_t",
"p_the_case_temperature_s",
"p_standard_of_pressure_f",
"p_standard_of_pressure_s",
"p_standard_of_pressure_t",
"p_temperature_case_f",
"p_temperature_case_s",
"p_temperature_case_t",
"p_standard_of_flow_f",
"p_standard_of_flow_s",
"p_standard_of_flow_t",
"p_local_atmosphere_f",
"p_local_atmosphere_s",
"p_local_atmosphere_t",
"a_altitude",
"f_air_temperature",
"f_boiler_body_resistance",
"f_duct_resistance",
"f_local_atmosphere",
"f_smoke_flow_rate_condition",
"f_nameplate_medium_temperature",
"f_fan_total_pressure",
"f_fan_select_total_pressure",
"f_fan_selection_flow",
"f_fan_power",
"f_electric_motor_power",
"f_fan_shaft_power",
"f_fan_security_volumn",
"s_boiler_body_resistance",
"s_duct_resistance",
"s_local_atmosphere",
"s_smoke_flow_rate_condition",
"s_fan_total_pressure",
"s_fan_select_total_pressure",
"s_fan_selection_flow",
"s_fan_power",
"s_electric_motor_power",
"s_fan_shaft_power",
"s_fan_security_volumn",
"i_boiler_body_resistance",
"i_denitration",
"i_duster",
"i_duct_resistance",
"i_resistance_desulfurization_fan",
"i_local_atmosphere",
"i_smoke_flow_rate_condition",
"i_fan_total_pressure",
"i_fan_select_total_pressure",
"i_fan_selection_flow",
"i_fan_power",
"i_electric_motor_power",
"i_fan_shaft_power",
"i_fan_security_volumn",
"r_boiler_body_resistance",
"r_duct_resistance",
"r_local_atmosphere",
"r_smoke_flow_rate_condition",
"r_fan_total_pressure",
"r_fan_select_total_pressure",
"r_fan_selection_flow",
"r_fan_power",
"r_electric_motor_power",
"r_fan_shaft_power",
"r_fan_security_volumn"
ON "public"."coalchp_smoke_air_system"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_smoke_air_system"();
