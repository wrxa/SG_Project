CREATE OR REPLACE FUNCTION gaspowergeneration_turbine_of_pts()
RETURNS TRIGGER AS
$BODY$
DECLARE
  hhgrade int;
  lhgrade int;
  steamtype int;
BEGIN
  hhgrade = NEW.s_hh_grade;
  lhgrade = NEW.s_lh_grade;
  steamtype =  NEW.s_steam_type_test;
  
----------------------实现字段e_exhaust_point_entropy:11熵,的计算1-----------------------------------
  IF OLD.e_steam_entropy != NEW.e_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_point_entropy=(NEW.e_steam_entropy)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_steam_entropy ISNULL) AND NEW.e_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_point_entropy=(NEW.e_steam_entropy)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_exhaust_after_steam:14抽汽后蒸汽量,的计算2-----------------------------------
  IF OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_steam_flow != NEW.e_steam_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_after_steam=(NEW.e_steam_flow)-(NEW.e_exhaust_point_flow)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_exhaust_point_flow ISNULL OR OLD.e_steam_flow ISNULL) AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_steam_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_after_steam=(NEW.e_steam_flow)-(NEW.e_exhaust_point_flow)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_exhaust_after_pressure:15压力,的计算3-----------------------------------
  IF OLD.e_exhaust_point_pressure != NEW.e_exhaust_point_pressure THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_after_pressure=(NEW.e_exhaust_point_pressure)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_exhaust_point_pressure ISNULL) AND NEW.e_exhaust_point_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_after_pressure=(NEW.e_exhaust_point_pressure)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_exhaust_after_enthalpy:16焓,的计算4-----------------------------------
  IF OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_after_enthalpy=(NEW.e_exhaust_point_enthalpy)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_exhaust_point_enthalpy ISNULL) AND NEW.e_exhaust_point_enthalpy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_after_enthalpy=(NEW.e_exhaust_point_enthalpy)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_exhaust_after_entropy:17熵,的计算5-----------------------------------
  IF OLD.e_steam_entropy != NEW.e_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_after_entropy=(NEW.e_steam_entropy)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_steam_entropy ISNULL) AND NEW.e_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_exhaust_after_entropy=(NEW.e_steam_entropy)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_backpressure_flow:背压流量,的计算6-----------------------------------
  IF OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_steam_flow != NEW.e_steam_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     e_backpressure_flow=(NEW.e_steam_flow)-(NEW.e_exhaust_point_flow)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_exhaust_point_flow ISNULL OR OLD.e_steam_flow ISNULL) AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_steam_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_backpressure_flow=(NEW.e_steam_flow)-(NEW.e_exhaust_point_flow)
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段e_gross_generation:20总发电量,的计算7-----------------------------------
  IF steamtype = 1 AND (OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_turbine_efficiency != NEW.e_turbine_efficiency OR OLD.e_steam_exhaust_enthalpy != NEW.e_steam_exhaust_enthalpy OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.e_steam_flow != NEW.e_steam_flow OR OLD.e_steam_entropy != NEW.e_steam_entropy OR OLD.e_steam_enthalpy != NEW.e_steam_enthalpy) THEN
     update gaspowergeneration_turbine_of_pts set 

     e_gross_generation=(NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy)))
     where plan_id=NEW.plan_id;

  ELSIF steamtype = 1 AND (OLD.e_steam_exhaust_enthalpy ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_steam_enthalpy ISNULL OR OLD.e_steam_entropy ISNULL OR OLD.e_steam_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL OR OLD.e_turbine_efficiency ISNULL) AND NEW.e_steam_exhaust_enthalpy NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_steam_enthalpy NOTNULL AND NEW.e_steam_entropy NOTNULL AND NEW.e_steam_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL AND NEW.e_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_gross_generation=(NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy)))
     where plan_id=NEW.plan_id;

  ELSIF steamtype = 2 AND (OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_turbine_efficiency != NEW.e_turbine_efficiency OR OLD.e_backpressure_enthalpy != NEW.e_backpressure_enthalpy OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.e_steam_flow != NEW.e_steam_flow OR OLD.e_steam_entropy != NEW.e_steam_entropy OR OLD.e_steam_enthalpy != NEW.e_steam_enthalpy) THEN
     update gaspowergeneration_turbine_of_pts set 

     e_gross_generation=(NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_backpressure_enthalpy)))
     where plan_id=NEW.plan_id;
     
  ELSIF steamtype = 2 AND (OLD.e_backpressure_enthalpy ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_steam_enthalpy ISNULL OR OLD.e_steam_entropy ISNULL OR OLD.e_steam_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL OR OLD.e_turbine_efficiency ISNULL) AND NEW.e_backpressure_enthalpy NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_steam_enthalpy NOTNULL AND NEW.e_steam_entropy NOTNULL AND NEW.e_steam_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL AND NEW.e_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_gross_generation=(NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_backpressure_enthalpy)))
     where plan_id=NEW.plan_id;
  END IF;

----------------------实现字段e_steam_extraction:21去除抽汽后,的计算8-----------------------------------
  IF steamtype = 1 AND (OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_turbine_efficiency != NEW.e_turbine_efficiency OR OLD.e_steam_exhaust_enthalpy != NEW.e_steam_exhaust_enthalpy OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_hot_data != NEW.e_hot_data OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.e_steam_flow != NEW.e_steam_flow OR OLD.e_steam_entropy != NEW.e_steam_entropy OR OLD.e_steam_enthalpy != NEW.e_steam_enthalpy) THEN
     update gaspowergeneration_turbine_of_pts set 

     e_steam_extraction=(NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy))))/1000
     where plan_id=NEW.plan_id;

  ELSIF steamtype = 1 AND (OLD.e_hot_data ISNULL OR OLD.e_steam_exhaust_enthalpy ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_steam_enthalpy ISNULL OR OLD.e_steam_entropy ISNULL OR OLD.e_steam_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL OR OLD.e_turbine_efficiency ISNULL) AND NEW.e_hot_data NOTNULL AND NEW.e_steam_exhaust_enthalpy NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_steam_enthalpy NOTNULL AND NEW.e_steam_entropy NOTNULL AND NEW.e_steam_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL AND NEW.e_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_steam_extraction=(NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy))))/1000
     where plan_id=NEW.plan_id;
  ELSIF steamtype = 2 AND (OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_turbine_efficiency != NEW.e_turbine_efficiency OR OLD.e_backpressure_enthalpy != NEW.e_backpressure_enthalpy OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_hot_data != NEW.e_hot_data OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.e_steam_flow != NEW.e_steam_flow OR OLD.e_steam_entropy != NEW.e_steam_entropy OR OLD.e_steam_enthalpy != NEW.e_steam_enthalpy) THEN
     update gaspowergeneration_turbine_of_pts set 

     e_steam_extraction=(NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_backpressure_enthalpy))))/1000
     where plan_id=NEW.plan_id;

  ELSIF steamtype = 2 AND (OLD.e_hot_data ISNULL OR OLD.e_backpressure_enthalpy ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_steam_enthalpy ISNULL OR OLD.e_steam_entropy ISNULL OR OLD.e_steam_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL OR OLD.e_turbine_efficiency ISNULL) AND NEW.e_hot_data NOTNULL AND NEW.e_backpressure_enthalpy NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_steam_enthalpy NOTNULL AND NEW.e_steam_entropy NOTNULL AND NEW.e_steam_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL AND NEW.e_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_steam_extraction=(NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_backpressure_enthalpy))))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_steam_extraction_select:22选定,的计算9-----------------------------------
  IF steamtype = 1 AND (OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_turbine_efficiency != NEW.e_turbine_efficiency OR OLD.e_steam_exhaust_enthalpy != NEW.e_steam_exhaust_enthalpy OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_hot_data != NEW.e_hot_data OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.e_steam_flow != NEW.e_steam_flow OR OLD.e_steam_entropy != NEW.e_steam_entropy OR OLD.e_steam_enthalpy != NEW.e_steam_enthalpy) THEN
     update gaspowergeneration_turbine_of_pts set 

     e_steam_extraction_select=((NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy))))/1000)
     where plan_id=NEW.plan_id;

  ELSIF steamtype = 1 AND (OLD.e_hot_data ISNULL OR OLD.e_steam_exhaust_enthalpy ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_steam_enthalpy ISNULL OR OLD.e_steam_entropy ISNULL OR OLD.e_steam_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL OR OLD.e_turbine_efficiency ISNULL) AND NEW.e_hot_data NOTNULL AND NEW.e_steam_exhaust_enthalpy NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_steam_enthalpy NOTNULL AND NEW.e_steam_entropy NOTNULL AND NEW.e_steam_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL AND NEW.e_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_steam_extraction_select=((NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy))))/1000)
     where plan_id=NEW.plan_id;
  ELSIF steamtype = 2 AND (OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_turbine_efficiency != NEW.e_turbine_efficiency OR OLD.e_backpressure_enthalpy != NEW.e_backpressure_enthalpy OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_hot_data != NEW.e_hot_data OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.e_steam_flow != NEW.e_steam_flow OR OLD.e_steam_entropy != NEW.e_steam_entropy OR OLD.e_steam_enthalpy != NEW.e_steam_enthalpy) THEN
     update gaspowergeneration_turbine_of_pts set 

     e_steam_extraction_select=((NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_backpressure_enthalpy))))/1000)
     where plan_id=NEW.plan_id;

  ELSIF steamtype = 2 AND (OLD.e_hot_data ISNULL OR OLD.e_backpressure_enthalpy ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_steam_enthalpy ISNULL OR OLD.e_steam_entropy ISNULL OR OLD.e_steam_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL OR OLD.e_turbine_efficiency ISNULL) AND NEW.e_hot_data NOTNULL AND NEW.e_backpressure_enthalpy NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_steam_enthalpy NOTNULL AND NEW.e_steam_entropy NOTNULL AND NEW.e_steam_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL AND NEW.e_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     e_steam_extraction_select=((NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_backpressure_enthalpy))))/1000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_mechanical_efficiency:101机械效率,的计算10-----------------------------------
  IF OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency THEN
     update gaspowergeneration_turbine_of_pts set 

     i_mechanical_efficiency=(NEW.e_mechanical_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_mechanical_efficiency ISNULL) AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_mechanical_efficiency=(NEW.e_mechanical_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_generator_efficiency:102发电机效率,的计算11-----------------------------------
  IF OLD.e_generator_efficiency != NEW.e_generator_efficiency THEN
     update gaspowergeneration_turbine_of_pts set 

     i_generator_efficiency=(NEW.e_generator_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_generator_efficiency ISNULL) AND NEW.e_generator_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_generator_efficiency=(NEW.e_generator_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_steam_pressure:103主蒸汽压力,的计算12-----------------------------------
  IF OLD.e_steam_pressure != NEW.e_steam_pressure THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_pressure=(NEW.e_steam_pressure)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_steam_pressure ISNULL) AND NEW.e_steam_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_pressure=(NEW.e_steam_pressure)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_steam_temperature:104温度,的计算13-----------------------------------
  IF OLD.e_steam_temperature != NEW.e_steam_temperature THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_temperature=(NEW.e_steam_temperature)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_steam_temperature ISNULL) AND NEW.e_steam_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_temperature=(NEW.e_steam_temperature)
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段i_high1_pressure:1081号高压压力,的计算-----------------------------------
  IF OLD.hh1_work_pressure != NEW.hh1_work_pressure OR OLD.hh1_pressure_loss != NEW.hh1_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high1_pressure=((NEW.hh1_work_pressure)/(1-(NEW.hh1_pressure_loss)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh1_pressure_loss ISNULL OR OLD.hh1_work_pressure ISNULL) AND NEW.hh1_pressure_loss NOTNULL AND NEW.hh1_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high1_pressure=((NEW.hh1_work_pressure)/(1-(NEW.hh1_pressure_loss)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_high1_entropy:109熵,的计算14-----------------------------------
  IF OLD.i_steam_entropy != NEW.i_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high1_entropy=(NEW.i_steam_entropy)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_entropy ISNULL) AND NEW.i_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high1_entropy=(NEW.i_steam_entropy)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_high1_flow:112流量,的计算15-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high1_flow=(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high1_flow=(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_steam_hh1_power:113主汽至HH1功率,的计算16-----------------------------------
  IF OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_steam_enthalpy != NEW.i_steam_enthalpy OR OLD.i_high1_enthalpy != NEW.i_high1_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_hh1_power=((NEW.i_steam_flow))*((NEW.i_steam_enthalpy)-(NEW.i_high1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_high1_enthalpy ISNULL OR OLD.i_steam_enthalpy ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL) AND NEW.i_high1_enthalpy NOTNULL AND NEW.i_steam_enthalpy NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_hh1_power=((NEW.i_steam_flow))*((NEW.i_steam_enthalpy)-(NEW.i_high1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_high2_pressure:1142号高压压力,的计算17-----------------------------------
  IF OLD.hh2_work_pressure != NEW.hh2_work_pressure OR OLD.hh2_pressure_loss != NEW.hh2_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high2_pressure=((NEW.hh2_work_pressure)/(1-(NEW.hh2_pressure_loss)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh2_pressure_loss ISNULL OR OLD.hh2_work_pressure ISNULL) AND NEW.hh2_pressure_loss NOTNULL AND NEW.hh2_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high2_pressure=((NEW.hh2_work_pressure)/(1-(NEW.hh2_pressure_loss)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_high2_entropy:115熵,的计算18-----------------------------------
  IF OLD.i_steam_entropy != NEW.i_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high2_entropy=((NEW.i_steam_entropy))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_entropy ISNULL) AND NEW.i_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high2_entropy=((NEW.i_steam_entropy))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_high2_flow:118流量,的计算19-----------------------------------
  IF OLD.hh2_extraction_amount != NEW.hh2_extraction_amount THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high2_flow=(NEW.hh2_extraction_amount)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh2_extraction_amount ISNULL) AND NEW.hh2_extraction_amount NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_high2_flow=(NEW.hh2_extraction_amount)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_hh1_hh2_power:119HH1至HH2功率,的计算20-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_high1_enthalpy != NEW.i_high1_enthalpy OR OLD.i_high2_enthalpy != NEW.i_high2_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_hh1_hh2_power=((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)))*((NEW.i_high1_enthalpy)-(NEW.i_high2_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_high2_enthalpy ISNULL OR OLD.i_high1_enthalpy ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_high2_enthalpy NOTNULL AND NEW.i_high1_enthalpy NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_hh1_hh2_power=((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)))*((NEW.i_high1_enthalpy)-(NEW.i_high2_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_deoxidize_pressure:120D除氧压力,的计算21-----------------------------------
  IF OLD.d_work_pressure != NEW.d_work_pressure OR OLD.d_pressure_loss != NEW.d_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     i_deoxidize_pressure=((NEW.d_work_pressure)/(1-(NEW.d_pressure_loss)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_pressure_loss ISNULL OR OLD.d_work_pressure ISNULL) AND NEW.d_pressure_loss NOTNULL AND NEW.d_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_deoxidize_pressure=((NEW.d_work_pressure)/(1-(NEW.d_pressure_loss)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_deoxidize_entropy:121熵,的计算22-----------------------------------
  IF OLD.i_steam_entropy != NEW.i_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_deoxidize_entropy=(((NEW.i_steam_entropy)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_entropy ISNULL) AND NEW.i_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_deoxidize_entropy=(((NEW.i_steam_entropy)))
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段i_deoxidize_flow:124流量,的计算24-----------------------------------
  IF OLD.d_extraction_amount != NEW.d_extraction_amount THEN
     update gaspowergeneration_turbine_of_pts set 

     i_deoxidize_flow=NEW.d_extraction_amount
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_extraction_amount ISNULL) AND NEW.d_extraction_amount NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_deoxidize_flow=NEW.d_extraction_amount
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段i_hh2_deoxidize_power:125HH2至D功率,的计算23-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_extraction_amount != NEW.hh2_extraction_amount OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_high2_enthalpy != NEW.i_high2_enthalpy OR OLD.i_deoxidize_enthalpy != NEW.i_deoxidize_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_hh2_deoxidize_power=((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount)))*((NEW.i_high2_enthalpy)-(NEW.i_deoxidize_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_amount ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_deoxidize_enthalpy ISNULL OR OLD.i_high2_enthalpy ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_amount NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_deoxidize_enthalpy NOTNULL AND NEW.i_high2_enthalpy NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_hh2_deoxidize_power=((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount)))*((NEW.i_high2_enthalpy)-(NEW.i_deoxidize_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_exhaust_point_pressure:126抽汽点压力,的计算24-----------------------------------
  IF OLD.e_exhaust_point_pressure != NEW.e_exhaust_point_pressure THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_pressure=(NEW.e_exhaust_point_pressure)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_exhaust_point_pressure ISNULL) AND NEW.e_exhaust_point_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_pressure=(NEW.e_exhaust_point_pressure)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_exhaust_point_temperature:127温度,的计算25-----------------------------------
  IF OLD.e_exhaust_point_temperature != NEW.e_exhaust_point_temperature THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_temperature=(NEW.e_exhaust_point_temperature)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_exhaust_point_temperature ISNULL) AND NEW.e_exhaust_point_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_temperature=(NEW.e_exhaust_point_temperature)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_exhaust_point_entropy:128熵,的计算26-----------------------------------
  IF OLD.i_steam_entropy != NEW.i_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_entropy=(NEW.i_steam_entropy)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_entropy ISNULL) AND NEW.i_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_entropy=(NEW.i_steam_entropy)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_exhaust_point_enthalpy:129焓,的计算27-----------------------------------
  IF OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_enthalpy=((NEW.e_exhaust_point_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_exhaust_point_enthalpy ISNULL) AND NEW.e_exhaust_point_enthalpy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_enthalpy=((NEW.e_exhaust_point_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_exhaust_point_flow:130流量,的计算28-----------------------------------
  IF OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_flow=(NEW.e_exhaust_point_flow)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_exhaust_point_flow ISNULL) AND NEW.e_exhaust_point_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_point_flow=(NEW.e_exhaust_point_flow)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_deoxidize_exhaust_power:131D至抽汽功率,的计算29-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_extraction_amount != NEW.hh2_extraction_amount OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_deoxidize_enthalpy != NEW.i_deoxidize_enthalpy OR OLD.i_deoxidize_flow != NEW.i_deoxidize_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     i_deoxidize_exhaust_power=((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((NEW.i_deoxidize_enthalpy)-(((NEW.e_exhaust_point_enthalpy))))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_amount ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_deoxidize_flow ISNULL OR OLD.i_deoxidize_enthalpy ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_amount NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_deoxidize_flow NOTNULL AND NEW.i_deoxidize_enthalpy NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_deoxidize_exhaust_power=((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((NEW.i_deoxidize_enthalpy)-(((NEW.e_exhaust_point_enthalpy))))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_low1_pressure:1321号低加压力,的计算30-----------------------------------
  IF OLD.lh1_work_pressure != NEW.lh1_work_pressure OR OLD.lh1_pressure_loss != NEW.lh1_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low1_pressure=((NEW.lh1_work_pressure)/(1-(NEW.lh1_pressure_loss)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh1_pressure_loss ISNULL OR OLD.lh1_work_pressure ISNULL) AND NEW.lh1_pressure_loss NOTNULL AND NEW.lh1_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low1_pressure=((NEW.lh1_work_pressure)/(1-(NEW.lh1_pressure_loss)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_low1_entropy:133熵,的计算31-----------------------------------
  IF OLD.i_steam_entropy != NEW.i_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low1_entropy=((((NEW.i_steam_entropy))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_entropy ISNULL) AND NEW.i_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low1_entropy=((((NEW.i_steam_entropy))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_low1_flow:136流量,的计算32-----------------------------------
  IF OLD.lh1_extraction_amount != NEW.lh1_extraction_amount THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low1_flow=(NEW.lh1_extraction_amount)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh1_extraction_amount ISNULL) AND NEW.lh1_extraction_amount NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low1_flow=(NEW.lh1_extraction_amount)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_exhaust_lh1_power:137抽汽至LH1功率,的计算33-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_extraction_amount != NEW.hh2_extraction_amount OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_deoxidize_flow != NEW.i_deoxidize_flow OR OLD.i_low1_enthalpy != NEW.i_low1_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_lh1_power=((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((((NEW.e_exhaust_point_enthalpy)))-(NEW.i_low1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_amount ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_low1_enthalpy ISNULL OR OLD.i_deoxidize_flow ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_amount NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_low1_enthalpy NOTNULL AND NEW.i_deoxidize_flow NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_exhaust_lh1_power=((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((((NEW.e_exhaust_point_enthalpy)))-(NEW.i_low1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_low2_pressure:1382号低加压力,的计算34-----------------------------------
  IF OLD.lh2_work_pressure != NEW.lh2_work_pressure OR OLD.lh2_pressure_loss != NEW.lh2_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low2_pressure=((NEW.lh2_work_pressure)/(1-(NEW.lh2_pressure_loss)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh2_pressure_loss ISNULL OR OLD.lh2_work_pressure ISNULL) AND NEW.lh2_pressure_loss NOTNULL AND NEW.lh2_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low2_pressure=((NEW.lh2_work_pressure)/(1-(NEW.lh2_pressure_loss)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_low2_entropy:139熵,的计算35-----------------------------------
  IF OLD.i_steam_entropy != NEW.i_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low2_entropy=((((NEW.i_steam_entropy))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_entropy ISNULL) AND NEW.i_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low2_entropy=((((NEW.i_steam_entropy))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_low2_flow:142流量,的计算36-----------------------------------
  IF OLD.lh2_extraction_amount != NEW.lh2_extraction_amount THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low2_flow=(NEW.lh2_extraction_amount)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh2_extraction_amount ISNULL) AND NEW.lh2_extraction_amount NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_low2_flow=(NEW.lh2_extraction_amount)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_lh1_lh2_power:143LH1至LH2功率,的计算37-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_extraction_amount != NEW.hh2_extraction_amount OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.lh1_extraction_amount != NEW.lh1_extraction_amount OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_deoxidize_flow != NEW.i_deoxidize_flow OR OLD.i_low1_enthalpy != NEW.i_low1_enthalpy OR OLD.i_low2_enthalpy != NEW.i_low2_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_lh1_lh2_power=((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount)))*((NEW.i_low1_enthalpy)-(NEW.i_low2_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh1_extraction_amount ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_amount ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_low2_enthalpy ISNULL OR OLD.i_low1_enthalpy ISNULL OR OLD.i_deoxidize_flow ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL) AND NEW.lh1_extraction_amount NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_amount NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_low2_enthalpy NOTNULL AND NEW.i_low1_enthalpy NOTNULL AND NEW.i_deoxidize_flow NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_lh1_lh2_power=((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount)))*((NEW.i_low1_enthalpy)-(NEW.i_low2_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_steam_exhaust_entropy:145熵,的计算38-----------------------------------
  IF OLD.i_steam_entropy != NEW.i_steam_entropy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_exhaust_entropy=(((((NEW.i_steam_entropy)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_entropy ISNULL) AND NEW.i_steam_entropy NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_exhaust_entropy=(((((NEW.i_steam_entropy)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_steam_exhaust_enthalpy_actual:147实际焓,的计算39-----------------------------------
  IF OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_low2_enthalpy != NEW.i_low2_enthalpy OR OLD.i_steam_exhaust_enthalpy != NEW.i_steam_exhaust_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_exhaust_enthalpy_actual=(NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_exhaust_enthalpy ISNULL OR OLD.i_low2_enthalpy ISNULL OR OLD.i_turbine_efficiency ISNULL) AND NEW.i_steam_exhaust_enthalpy NOTNULL AND NEW.i_low2_enthalpy NOTNULL AND NEW.i_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_exhaust_enthalpy_actual=(NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_steam_exhaust_dry:150干度,的计算40-----------------------------------
  IF OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_low2_enthalpy != NEW.i_low2_enthalpy OR OLD.i_steam_exhaust_enthalpy != NEW.i_steam_exhaust_enthalpy OR OLD.i_steam_exhaust_enthalpy_steam != NEW.i_steam_exhaust_enthalpy_steam OR OLD.i_steam_exhaust_enthalpy_water != NEW.i_steam_exhaust_enthalpy_water THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_exhaust_dry=1-(((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency))-(NEW.i_steam_exhaust_enthalpy_water))/((NEW.i_steam_exhaust_enthalpy_steam)-(NEW.i_steam_exhaust_enthalpy_water))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.i_steam_exhaust_enthalpy_water ISNULL OR OLD.i_steam_exhaust_enthalpy_steam ISNULL OR OLD.i_steam_exhaust_enthalpy ISNULL OR OLD.i_low2_enthalpy ISNULL OR OLD.i_turbine_efficiency ISNULL) AND NEW.i_steam_exhaust_enthalpy_water NOTNULL AND NEW.i_steam_exhaust_enthalpy_steam NOTNULL AND NEW.i_steam_exhaust_enthalpy NOTNULL AND NEW.i_low2_enthalpy NOTNULL AND NEW.i_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_exhaust_dry=1-(((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency))-(NEW.i_steam_exhaust_enthalpy_water))/((NEW.i_steam_exhaust_enthalpy_steam)-(NEW.i_steam_exhaust_enthalpy_water))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_steam_exhaust_flow:151流量,的计算41-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_extraction_amount != NEW.hh2_extraction_amount OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.lh1_extraction_amount != NEW.lh1_extraction_amount OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.lh2_extraction_amount != NEW.lh2_extraction_amount OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_deoxidize_flow != NEW.i_deoxidize_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_exhaust_flow=(NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)+((NEW.e_exhaust_point_flow))-((NEW.lh1_extraction_amount))-((NEW.lh2_extraction_amount))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh2_extraction_amount ISNULL OR OLD.lh1_extraction_amount ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_amount ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_deoxidize_flow ISNULL OR OLD.i_steam_flow ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_exhaust_point_flow ISNULL) AND NEW.lh2_extraction_amount NOTNULL AND NEW.lh1_extraction_amount NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_amount NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_deoxidize_flow NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_exhaust_point_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_steam_exhaust_flow=(NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)+((NEW.e_exhaust_point_flow))-((NEW.lh1_extraction_amount))-((NEW.lh2_extraction_amount))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_lh2_steam_power:152LH2至乏汽功率,的计算42-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_extraction_amount != NEW.hh2_extraction_amount OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.lh1_extraction_amount != NEW.lh1_extraction_amount OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.lh2_extraction_amount != NEW.lh2_extraction_amount OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_deoxidize_flow != NEW.i_deoxidize_flow OR OLD.i_low2_enthalpy != NEW.i_low2_enthalpy OR OLD.i_steam_exhaust_enthalpy != NEW.i_steam_exhaust_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_lh2_steam_power=((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount))-((NEW.lh2_extraction_amount)))*((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency)))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh2_extraction_amount ISNULL OR OLD.lh1_extraction_amount ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_amount ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_steam_exhaust_enthalpy ISNULL OR OLD.i_low2_enthalpy ISNULL OR OLD.i_deoxidize_flow ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL) AND NEW.lh2_extraction_amount NOTNULL AND NEW.lh1_extraction_amount NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_amount NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_steam_exhaust_enthalpy NOTNULL AND NEW.i_low2_enthalpy NOTNULL AND NEW.i_deoxidize_flow NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_lh2_steam_power=((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount))-((NEW.lh2_extraction_amount)))*((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency)))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_total_power:153总功率,的计算43-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_extraction_amount != NEW.hh2_extraction_amount OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.lh1_extraction_amount != NEW.lh1_extraction_amount OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.lh2_extraction_amount != NEW.lh2_extraction_amount OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_steam_enthalpy != NEW.i_steam_enthalpy OR OLD.i_high1_enthalpy != NEW.i_high1_enthalpy OR OLD.i_high2_enthalpy != NEW.i_high2_enthalpy OR OLD.i_deoxidize_enthalpy != NEW.i_deoxidize_enthalpy OR OLD.i_deoxidize_flow != NEW.i_deoxidize_flow OR OLD.i_low1_enthalpy != NEW.i_low1_enthalpy OR OLD.i_low2_enthalpy != NEW.i_low2_enthalpy OR OLD.i_steam_exhaust_enthalpy != NEW.i_steam_exhaust_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_total_power=((((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount))-((NEW.lh2_extraction_amount)))*((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency)))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount)))*((NEW.i_low1_enthalpy)-(NEW.i_low2_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((((NEW.e_exhaust_point_enthalpy)))-(NEW.i_low1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount)))*((NEW.i_high2_enthalpy)-(NEW.i_deoxidize_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)))*((NEW.i_high1_enthalpy)-(NEW.i_high2_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow))*((NEW.i_steam_enthalpy)-(NEW.i_high1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((NEW.i_deoxidize_enthalpy)-(((NEW.e_exhaust_point_enthalpy))))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh2_extraction_amount ISNULL OR OLD.lh1_extraction_amount ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_amount ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_steam_exhaust_enthalpy ISNULL OR OLD.i_low2_enthalpy ISNULL OR OLD.i_low1_enthalpy ISNULL OR OLD.i_deoxidize_flow ISNULL OR OLD.i_deoxidize_enthalpy ISNULL OR OLD.i_high2_enthalpy ISNULL OR OLD.i_high1_enthalpy ISNULL OR OLD.i_steam_enthalpy ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL) AND NEW.lh2_extraction_amount NOTNULL AND NEW.lh1_extraction_amount NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_amount NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_steam_exhaust_enthalpy NOTNULL AND NEW.i_low2_enthalpy NOTNULL AND NEW.i_low1_enthalpy NOTNULL AND NEW.i_deoxidize_flow NOTNULL AND NEW.i_deoxidize_enthalpy NOTNULL AND NEW.i_high2_enthalpy NOTNULL AND NEW.i_high1_enthalpy NOTNULL AND NEW.i_steam_enthalpy NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_total_power=((((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount))-((NEW.lh2_extraction_amount)))*((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency)))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount)))*((NEW.i_low1_enthalpy)-(NEW.i_low2_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((((NEW.e_exhaust_point_enthalpy)))-(NEW.i_low1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount)))*((NEW.i_high2_enthalpy)-(NEW.i_deoxidize_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)))*((NEW.i_high1_enthalpy)-(NEW.i_high2_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow))*((NEW.i_steam_enthalpy)-(NEW.i_high1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((NEW.i_deoxidize_enthalpy)-(((NEW.e_exhaust_point_enthalpy))))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_calculation_error:154计算误差,的计算44-----------------------------------
  IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_extraction_amount != NEW.hh2_extraction_amount OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_exhaust_point_enthalpy != NEW.e_exhaust_point_enthalpy OR OLD.lh1_extraction_amount != NEW.lh1_extraction_amount OR OLD.e_exhaust_point_flow != NEW.e_exhaust_point_flow OR OLD.lh2_extraction_amount != NEW.lh2_extraction_amount OR OLD.e_turbine_efficiency != NEW.e_turbine_efficiency OR OLD.e_steam_exhaust_enthalpy != NEW.e_steam_exhaust_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow OR OLD.e_mechanical_efficiency != NEW.e_mechanical_efficiency OR OLD.e_hot_data != NEW.e_hot_data OR OLD.e_generator_efficiency != NEW.e_generator_efficiency OR OLD.i_turbine_efficiency != NEW.i_turbine_efficiency OR OLD.i_steam_flow != NEW.i_steam_flow OR OLD.i_steam_enthalpy != NEW.i_steam_enthalpy OR OLD.i_high1_enthalpy != NEW.i_high1_enthalpy OR OLD.i_high2_enthalpy != NEW.i_high2_enthalpy OR OLD.i_deoxidize_enthalpy != NEW.i_deoxidize_enthalpy OR OLD.i_deoxidize_flow != NEW.i_deoxidize_flow OR OLD.e_steam_flow != NEW.e_steam_flow OR OLD.i_low1_enthalpy != NEW.i_low1_enthalpy OR OLD.e_steam_entropy != NEW.e_steam_entropy OR OLD.i_low2_enthalpy != NEW.i_low2_enthalpy OR OLD.i_steam_exhaust_enthalpy != NEW.i_steam_exhaust_enthalpy OR OLD.e_steam_enthalpy != NEW.e_steam_enthalpy THEN
     update gaspowergeneration_turbine_of_pts set 

     i_calculation_error=((((((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount))-((NEW.lh2_extraction_amount)))*((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency)))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount)))*((NEW.i_low1_enthalpy)-(NEW.i_low2_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((((NEW.e_exhaust_point_enthalpy)))-(NEW.i_low1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount)))*((NEW.i_high2_enthalpy)-(NEW.i_deoxidize_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)))*((NEW.i_high1_enthalpy)-(NEW.i_high2_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow))*((NEW.i_steam_enthalpy)-(NEW.i_high1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((NEW.i_deoxidize_enthalpy)-(((NEW.e_exhaust_point_enthalpy))))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)))-(((NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy))))/1000))*1000)/(((NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy))))/1000))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh2_extraction_amount ISNULL OR OLD.lh1_extraction_amount ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_amount ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.i_steam_exhaust_enthalpy ISNULL OR OLD.i_low2_enthalpy ISNULL OR OLD.i_low1_enthalpy ISNULL OR OLD.i_deoxidize_flow ISNULL OR OLD.i_deoxidize_enthalpy ISNULL OR OLD.i_high2_enthalpy ISNULL OR OLD.i_high1_enthalpy ISNULL OR OLD.i_steam_enthalpy ISNULL OR OLD.i_steam_flow ISNULL OR OLD.i_turbine_efficiency ISNULL OR OLD.e_hot_data ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_exhaust_enthalpy ISNULL OR OLD.e_exhaust_point_flow ISNULL OR OLD.e_exhaust_point_enthalpy ISNULL OR OLD.e_steam_enthalpy ISNULL OR OLD.e_steam_entropy ISNULL OR OLD.e_steam_flow ISNULL OR OLD.e_generator_efficiency ISNULL OR OLD.e_mechanical_efficiency ISNULL OR OLD.e_turbine_efficiency ISNULL) AND NEW.lh2_extraction_amount NOTNULL AND NEW.lh1_extraction_amount NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_amount NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.i_steam_exhaust_enthalpy NOTNULL AND NEW.i_low2_enthalpy NOTNULL AND NEW.i_low1_enthalpy NOTNULL AND NEW.i_deoxidize_flow NOTNULL AND NEW.i_deoxidize_enthalpy NOTNULL AND NEW.i_high2_enthalpy NOTNULL AND NEW.i_high1_enthalpy NOTNULL AND NEW.i_steam_enthalpy NOTNULL AND NEW.i_steam_flow NOTNULL AND NEW.i_turbine_efficiency NOTNULL AND NEW.e_hot_data NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_exhaust_enthalpy NOTNULL AND NEW.e_exhaust_point_flow NOTNULL AND NEW.e_exhaust_point_enthalpy NOTNULL AND NEW.e_steam_enthalpy NOTNULL AND NEW.e_steam_entropy NOTNULL AND NEW.e_steam_flow NOTNULL AND NEW.e_generator_efficiency NOTNULL AND NEW.e_mechanical_efficiency NOTNULL AND NEW.e_turbine_efficiency NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     i_calculation_error=((((((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount))-((NEW.lh2_extraction_amount)))*((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-((NEW.i_low2_enthalpy)-(NEW.i_steam_exhaust_enthalpy))*(NEW.i_turbine_efficiency)))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow)-((NEW.lh1_extraction_amount)))*((NEW.i_low1_enthalpy)-(NEW.i_low2_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((NEW.e_exhaust_point_flow))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((((NEW.e_exhaust_point_enthalpy)))-(NEW.i_low1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount)))*((NEW.i_high2_enthalpy)-(NEW.i_deoxidize_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)))*((NEW.i_high1_enthalpy)-(NEW.i_high2_enthalpy))*((NEW.e_generator_efficiency))*((NEW.e_mechanical_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow))*((NEW.i_steam_enthalpy)-(NEW.i_high1_enthalpy))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)+(((NEW.i_steam_flow)-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))-((NEW.hh2_extraction_amount))-(NEW.i_deoxidize_flow))*((NEW.i_deoxidize_enthalpy)-(((NEW.e_exhaust_point_enthalpy))))*((NEW.e_mechanical_efficiency))*((NEW.e_generator_efficiency))*(NEW.i_turbine_efficiency)/3.6)))-(((NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy))))/1000))*1000)/(((NEW.e_hot_data)*((NEW.e_turbine_efficiency)*(NEW.e_mechanical_efficiency)*(NEW.e_generator_efficiency)/3.6*((NEW.e_steam_flow)*((NEW.e_steam_enthalpy)-((NEW.e_steam_entropy)))+((NEW.e_steam_flow)-(NEW.e_exhaust_point_flow))*(((NEW.e_exhaust_point_enthalpy))-(NEW.e_steam_exhaust_enthalpy))))/1000))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_pressure:27压力,的计算45-----------------------------------
  IF OLD.d_work_pressure != NEW.d_work_pressure THEN
     update gaspowergeneration_turbine_of_pts set 

     h_pressure=2*(NEW.d_work_pressure)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_work_pressure ISNULL) AND NEW.d_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     h_pressure=2*(NEW.d_work_pressure)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_amount:29量,的计算46-----------------------------------
  IF OLD.e_steam_water_loss != NEW.e_steam_water_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     h_amount=(NEW.e_steam_water_loss)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_steam_water_loss ISNULL) AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     h_amount=(NEW.e_steam_water_loss)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hh1_saturated_water_temperature:33饱和水温度,的计算47-----------------------------------
  IF OLD.hh1_water_temperature != NEW.hh1_water_temperature OR OLD.hh1_top_difference != NEW.hh1_top_difference THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_saturated_water_temperature=(NEW.hh1_water_temperature)+(NEW.hh1_top_difference)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh1_top_difference ISNULL OR OLD.hh1_water_temperature ISNULL) AND NEW.hh1_top_difference NOTNULL AND NEW.hh1_water_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_saturated_water_temperature=(NEW.hh1_water_temperature)+(NEW.hh1_top_difference)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hh1_extraction_pressure:37抽汽压力,的计算48-----------------------------------
  IF OLD.hh1_work_pressure != NEW.hh1_work_pressure OR OLD.hh1_pressure_loss != NEW.hh1_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_pressure=(NEW.hh1_work_pressure)/(1-(NEW.hh1_pressure_loss))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh1_pressure_loss ISNULL OR OLD.hh1_work_pressure ISNULL) AND NEW.hh1_pressure_loss NOTNULL AND NEW.hh1_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_pressure=(NEW.hh1_work_pressure)/(1-(NEW.hh1_pressure_loss))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hh1_extraction_amount:39抽汽量,的计算49-----------------------------------
  IF hhgrade != 0 AND OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade != 0 AND (OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hh2_saturated_water_temperature:43饱和水温度,的计算50-----------------------------------
  IF OLD.hh2_water_temperature != NEW.hh2_water_temperature OR OLD.hh2_top_difference != NEW.hh2_top_difference THEN
     update gaspowergeneration_turbine_of_pts set 

     hh2_saturated_water_temperature=(NEW.hh2_water_temperature)+(NEW.hh2_top_difference)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh2_top_difference ISNULL OR OLD.hh2_water_temperature ISNULL) AND NEW.hh2_top_difference NOTNULL AND NEW.hh2_water_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh2_saturated_water_temperature=(NEW.hh2_water_temperature)+(NEW.hh2_top_difference)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hh2_extraction_pressure:47抽汽压力,的计算51-----------------------------------
  IF OLD.hh2_work_pressure != NEW.hh2_work_pressure OR OLD.hh2_pressure_loss != NEW.hh2_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     hh2_extraction_pressure=(NEW.hh2_work_pressure)/(1-(NEW.hh2_pressure_loss))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh2_pressure_loss ISNULL OR OLD.hh2_work_pressure ISNULL) AND NEW.hh2_pressure_loss NOTNULL AND NEW.hh2_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh2_extraction_pressure=(NEW.hh2_work_pressure)/(1-(NEW.hh2_pressure_loss))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_extraction_pressure:54抽汽压力,的计算52-----------------------------------
  IF OLD.d_work_pressure != NEW.d_work_pressure OR OLD.d_pressure_loss != NEW.d_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     d_extraction_pressure=(NEW.d_work_pressure)/(1-(NEW.d_pressure_loss))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_pressure_loss ISNULL OR OLD.d_work_pressure ISNULL) AND NEW.d_pressure_loss NOTNULL AND NEW.d_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     d_extraction_pressure=(NEW.d_work_pressure)/(1-(NEW.d_pressure_loss))
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段lh1_saturated_water_temperature:60饱和水温度,的计算54-----------------------------------
  IF OLD.lh1_water_temperature != NEW.lh1_water_temperature OR OLD.lh1_top_difference != NEW.lh1_top_difference THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_saturated_water_temperature=(NEW.lh1_water_temperature)+(NEW.lh1_top_difference)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh1_top_difference ISNULL OR OLD.lh1_water_temperature ISNULL) AND NEW.lh1_top_difference NOTNULL AND NEW.lh1_water_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_saturated_water_temperature=(NEW.lh1_water_temperature)+(NEW.lh1_top_difference)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段lh1_extraction_pressure:64抽汽压力,的计算55-----------------------------------
  IF OLD.lh1_work_pressure != NEW.lh1_work_pressure OR OLD.lh1_pressure_loss != NEW.lh1_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_pressure=(NEW.lh1_work_pressure)/(1-(NEW.lh1_pressure_loss))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh1_pressure_loss ISNULL OR OLD.lh1_work_pressure ISNULL) AND NEW.lh1_pressure_loss NOTNULL AND NEW.lh1_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_pressure=(NEW.lh1_work_pressure)/(1-(NEW.lh1_pressure_loss))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段lh2_saturated_water_temperature:70饱和水温度,的计算56-----------------------------------
  IF OLD.lh2_water_temperature != NEW.lh2_water_temperature OR OLD.lh2_top_difference != NEW.lh2_top_difference THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_saturated_water_temperature=(NEW.lh2_water_temperature)+(NEW.lh2_top_difference)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh2_top_difference ISNULL OR OLD.lh2_water_temperature ISNULL) AND NEW.lh2_top_difference NOTNULL AND NEW.lh2_water_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_saturated_water_temperature=(NEW.lh2_water_temperature)+(NEW.lh2_top_difference)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段lh2_extraction_pressure:74抽汽压力,的计算57-----------------------------------
  IF OLD.lh2_work_pressure != NEW.lh2_work_pressure OR OLD.lh2_pressure_loss != NEW.lh2_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_pressure=(NEW.lh2_work_pressure)/(1-(NEW.lh2_pressure_loss))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh2_pressure_loss ISNULL OR OLD.lh2_work_pressure ISNULL) AND NEW.lh2_pressure_loss NOTNULL AND NEW.lh2_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_pressure=(NEW.lh2_work_pressure)/(1-(NEW.lh2_pressure_loss))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_work_pressure:79工作压力,的计算58-----------------------------------
  IF steamtype = 1 AND (OLD.e_steam_exhaust_pressure != NEW.e_steam_exhaust_pressure) THEN
     update gaspowergeneration_turbine_of_pts set 

     c_work_pressure=(NEW.e_steam_exhaust_pressure)
     where plan_id=NEW.plan_id;

  ELSIF steamtype = 1 AND (OLD.e_steam_exhaust_pressure ISNULL) AND NEW.e_steam_exhaust_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     c_work_pressure=(NEW.e_steam_exhaust_pressure)
     where plan_id=NEW.plan_id;
     
  ELSIF steamtype = 2 AND (OLD.e_backpressure_pressure != NEW.e_backpressure_pressure) THEN
     update gaspowergeneration_turbine_of_pts set 

     c_work_pressure=(NEW.e_backpressure_pressure)
     where plan_id=NEW.plan_id;
     
  ELSIF steamtype = 2 AND (OLD.e_backpressure_pressure ISNULL) AND NEW.e_backpressure_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     c_work_pressure=(NEW.e_backpressure_pressure)
     where plan_id=NEW.plan_id;
  
  END IF;
----------------------实现字段hh3_saturated_water_temperature:83饱和水温度,的计算59-----------------------------------
  IF OLD.hh3_water_temperature != NEW.hh3_water_temperature OR OLD.hh3_top_difference != NEW.hh3_top_difference THEN
     update gaspowergeneration_turbine_of_pts set 

     hh3_saturated_water_temperature=(NEW.hh3_water_temperature)+(NEW.hh3_top_difference)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh3_top_difference ISNULL OR OLD.hh3_water_temperature ISNULL) AND NEW.hh3_top_difference NOTNULL AND NEW.hh3_water_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh3_saturated_water_temperature=(NEW.hh3_water_temperature)+(NEW.hh3_top_difference)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段hh3_extraction_pressure:87抽汽压力,的计算60-----------------------------------
  IF OLD.hh3_work_pressure != NEW.hh3_work_pressure OR OLD.hh3_pressure_loss != NEW.hh3_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     hh3_extraction_pressure=(NEW.hh3_work_pressure)/(1-(NEW.hh3_pressure_loss))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.hh3_pressure_loss ISNULL OR OLD.hh3_work_pressure ISNULL) AND NEW.hh3_pressure_loss NOTNULL AND NEW.hh3_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh3_extraction_pressure=(NEW.hh3_work_pressure)/(1-(NEW.hh3_pressure_loss))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段lh3_saturated_water_temperature:93饱和水温度,的计算61-----------------------------------
  IF OLD.lh3_water_temperature != NEW.lh3_water_temperature OR OLD.lh3_top_difference != NEW.lh3_top_difference THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_saturated_water_temperature=(NEW.lh3_water_temperature)+(NEW.lh3_top_difference)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh3_top_difference ISNULL OR OLD.lh3_water_temperature ISNULL) AND NEW.lh3_top_difference NOTNULL AND NEW.lh3_water_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_saturated_water_temperature=(NEW.lh3_water_temperature)+(NEW.lh3_top_difference)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段lh3_extraction_pressure:97抽汽压力,的计算62-----------------------------------
  IF OLD.lh3_work_pressure != NEW.lh3_work_pressure OR OLD.lh3_pressure_loss != NEW.lh3_pressure_loss THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_extraction_pressure=(NEW.lh3_work_pressure)/(1-(NEW.lh3_pressure_loss))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.lh3_pressure_loss ISNULL OR OLD.lh3_work_pressure ISNULL) AND NEW.lh3_pressure_loss NOTNULL AND NEW.lh3_work_pressure NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_extraction_pressure=(NEW.lh3_work_pressure)/(1-(NEW.lh3_pressure_loss))
     where plan_id=NEW.plan_id;

  END IF;

   
--------------------实现字段hh2_water_temperature:给水出水温度HH2-----------------------------------
   IF hhgrade != 0 AND OLD.hh1_water_temperature != NEW.hh1_water_temperature OR OLD.d_water_temperature != NEW.d_water_temperature THEN
	update gaspowergeneration_turbine_of_pts set 

	hh2_water_temperature=round((NEW.hh1_water_temperature-(NEW.hh1_water_temperature-NEW.d_water_temperature)/hhgrade), 0)
	where plan_id=NEW.plan_id;
 
   ELSIF hhgrade != 0 AND (OLD.hh1_water_temperature ISNULL OR OLD.d_water_temperature ISNULL) AND NEW.hh1_water_temperature NOTNULL AND NEW.d_water_temperature NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	hh2_water_temperature=round((NEW.hh1_water_temperature-(NEW.hh1_water_temperature-NEW.d_water_temperature)/hhgrade), 0)
	where plan_id=NEW.plan_id;
 
   END IF;
   


   
 ----------------------实现字段lh1_water_temperature:给水出水温度LH1-----------------------------------
   IF OLD.d_water_temperature != NEW.d_water_temperature OR OLD.c_water_temperature != NEW.c_water_temperature THEN
	update gaspowergeneration_turbine_of_pts set 

	lh1_water_temperature=round((NEW.d_water_temperature-(NEW.d_water_temperature-NEW.c_water_temperature)/(lhgrade+1)),0)
	where plan_id=NEW.plan_id;
   ELSIF (OLD.c_water_temperature ISNULL OR OLD.d_water_temperature ISNULL) AND NEW.c_water_temperature NOTNULL AND NEW.d_water_temperature NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	lh1_water_temperature=round((NEW.d_water_temperature-(NEW.d_water_temperature-NEW.c_water_temperature)/(lhgrade+1)),0)
	where plan_id=NEW.plan_id;
   END IF;
   
   
 ----------------------实现字段lh2_water_temperature:给水出水温度LH2-----------------------------------
   IF OLD.lh1_water_temperature != NEW.lh1_water_temperature OR OLD.d_water_temperature != NEW.d_water_temperature  OR OLD.c_water_temperature != NEW.c_water_temperature THEN
	update gaspowergeneration_turbine_of_pts set 

	lh2_water_temperature=round((NEW.lh1_water_temperature-(NEW.d_water_temperature-NEW.c_water_temperature)/(lhgrade+1)), 0)
	where plan_id=NEW.plan_id;
    ELSIF (OLD.lh1_water_temperature ISNULL OR OLD.d_water_temperature ISNULL OR OLD.c_water_temperature ISNULL) AND NEW.lh1_water_temperature NOTNULL AND NEW.d_water_temperature NOTNULL AND NEW.c_water_temperature NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	lh2_water_temperature=round((NEW.lh1_water_temperature-(NEW.d_water_temperature-NEW.c_water_temperature)/(lhgrade+1)), 0)
	where plan_id=NEW.plan_id;
     
    END IF;
    
 ----------------------实现字段lh3_water_temperature:给水出水温度LH3-----------------------------------
   IF OLD.lh2_water_temperature != NEW.lh2_water_temperature OR OLD.d_water_temperature != NEW.d_water_temperature  OR OLD.c_water_temperature != NEW.c_water_temperature THEN
	update gaspowergeneration_turbine_of_pts set 

	lh3_water_temperature=round((NEW.lh2_water_temperature-(NEW.d_water_temperature-NEW.c_water_temperature)/(lhgrade+1)), 0)
	where plan_id=NEW.plan_id;
    ELSIF (OLD.lh2_water_temperature ISNULL OR OLD.d_water_temperature ISNULL OR OLD.c_water_temperature ISNULL) AND NEW.lh2_water_temperature NOTNULL AND NEW.d_water_temperature NOTNULL AND NEW.c_water_temperature NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	lh3_water_temperature=round((NEW.lh2_water_temperature-(NEW.d_water_temperature-NEW.c_water_temperature)/(lhgrade+1)), 0)
	where plan_id=NEW.plan_id;
    END IF;
    
 
 ----------------------实现字段hh2_water_enthalpy:给水出口焓HH2-----------------------------------
   IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy THEN
	update gaspowergeneration_turbine_of_pts set 

	hh2_water_enthalpy=(NEW.hh1_water_enthalpy-(NEW.hh1_water_enthalpy-NEW.d_water_enthalpy)/hhgrade)
	where plan_id=NEW.plan_id;
 
   ELSIF (OLD.hh1_water_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL) AND NEW.hh1_water_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	hh2_water_enthalpy=(NEW.hh1_water_enthalpy-(NEW.hh1_water_enthalpy-NEW.d_water_enthalpy)/hhgrade)
	where plan_id=NEW.plan_id;
 
   END IF;
   
 ----------------------实现字段hh3_water_enthalpy:给水出口焓HH3-----------------------------------
   IF OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy  OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy THEN
	update gaspowergeneration_turbine_of_pts set 

	hh3_water_enthalpy=(NEW.hh2_water_enthalpy-(NEW.hh1_water_enthalpy-NEW.d_water_enthalpy)/hhgrade)
	where plan_id=NEW.plan_id;
   ELSIF (OLD.hh1_water_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL) AND NEW.hh1_water_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	hh3_water_enthalpy=(NEW.hh2_water_enthalpy-(NEW.hh1_water_enthalpy-NEW.d_water_enthalpy)/hhgrade)
	where plan_id=NEW.plan_id;
   END IF;
   
 ----------------------实现字段lh1_water_enthalpy:给水出口焓LH1-----------------------------------
   IF OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy THEN
	update gaspowergeneration_turbine_of_pts set 

	lh1_water_enthalpy=(NEW.d_water_enthalpy-(NEW.d_water_enthalpy-NEW.c_water_enthalpy)/(lhgrade+1))
	where plan_id=NEW.plan_id;
   ELSIF (OLD.c_water_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL) AND NEW.c_water_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	lh1_water_enthalpy=(NEW.d_water_enthalpy-(NEW.d_water_enthalpy-NEW.c_water_enthalpy)/(lhgrade+1))
	where plan_id=NEW.plan_id;
   END IF;
   
   
 ----------------------实现字段lh2_water_enthalpy:给水出口焓LH2-----------------------------------
   IF OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy  OR OLD.c_water_enthalpy != NEW.c_water_enthalpy THEN
	update gaspowergeneration_turbine_of_pts set 

	lh2_water_enthalpy=(NEW.lh1_water_enthalpy-(NEW.d_water_enthalpy-NEW.c_water_enthalpy)/(lhgrade+1))
	where plan_id=NEW.plan_id;
    ELSIF (OLD.lh1_water_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.c_water_enthalpy ISNULL) AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.c_water_enthalpy NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	lh2_water_enthalpy=(NEW.lh1_water_enthalpy-(NEW.d_water_enthalpy-NEW.c_water_enthalpy)/(lhgrade+1))
	where plan_id=NEW.plan_id;
     
    END IF;
    
 ----------------------实现字段lh3_water_enthalpy:给水出口焓LH3-----------------------------------
   IF OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy  OR OLD.c_water_enthalpy != NEW.c_water_enthalpy THEN
	update gaspowergeneration_turbine_of_pts set 

	lh3_water_enthalpy=(NEW.lh2_water_enthalpy-(NEW.d_water_enthalpy-NEW.c_water_enthalpy)/(lhgrade+1))
	where plan_id=NEW.plan_id;
    ELSIF (OLD.lh2_water_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.c_water_enthalpy ISNULL) AND NEW.lh2_water_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.c_water_enthalpy NOTNULL THEN
	update gaspowergeneration_turbine_of_pts set 

	lh3_water_enthalpy=(NEW.lh2_water_enthalpy-(NEW.d_water_enthalpy-NEW.c_water_enthalpy)/(lhgrade+1))
	where plan_id=NEW.plan_id;
    END IF;


----------------------实现字段hh1_extraction_amount:39抽汽量,的计算49-----------------------------------
  IF hhgrade = 2 AND OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.hh2_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND (OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.hh2_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 1 AND OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 1 AND (OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND (OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;
  END IF;
----------------------实现字段hh2_extraction_amount:49抽汽量,的计算52-----------------------------------
  IF hhgrade = 2 AND OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy OR OLD.hh2_saturated_water_enthalpy != NEW.hh2_saturated_water_enthalpy OR OLD.hh2_extraction_enthalpy != NEW.hh2_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     hh2_extraction_amount=(((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.d_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.hh2_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND (OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_enthalpy ISNULL OR OLD.hh2_saturated_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL) AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_enthalpy NOTNULL AND NEW.hh2_saturated_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh2_extraction_amount=(((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.d_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.hh2_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  END IF;



----------------------实现字段lh1_extraction_amount:66抽汽量,的计算57(HH0&1)-----------------------------------
  IF (hhgrade = 1) AND lhgrade = 1 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.c_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 1 AND (OLD.c_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.c_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.c_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 2 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 2 AND (OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 3 AND (OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段lh2_extraction_amount:76抽汽量,的计算60(HH0&1)-----------------------------------
  IF (hhgrade = 1) AND lhgrade = 2 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 2 AND (OLD.c_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.c_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.lh3_water_enthalpy != NEW.lh3_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 3 AND (OLD.lh3_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh3_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段lh3_extraction_amount:99抽汽量,的计算66(HH0&1)-----------------------------------
  IF (hhgrade = 1) AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.lh3_water_enthalpy != NEW.lh3_water_enthalpy OR OLD.lh3_saturated_water_enthalpy != NEW.lh3_saturated_water_enthalpy OR OLD.lh3_extraction_enthalpy != NEW.lh3_extraction_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh3_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*((((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))*((NEW.lh2_saturated_water_enthalpy)-(NEW.lh3_saturated_water_enthalpy)))/0.98/((NEW.lh3_extraction_enthalpy)-(NEW.lh3_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF (hhgrade = 1) AND lhgrade = 3 AND (OLD.lh3_extraction_enthalpy ISNULL OR OLD.lh3_saturated_water_enthalpy ISNULL OR OLD.lh3_water_enthalpy ISNULL OR OLD.c_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh3_extraction_enthalpy NOTNULL AND NEW.lh3_saturated_water_enthalpy NOTNULL AND NEW.lh3_water_enthalpy NOTNULL AND NEW.c_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh3_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*((((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))*((NEW.lh2_saturated_water_enthalpy)-(NEW.lh3_saturated_water_enthalpy)))/0.98/((NEW.lh3_extraction_enthalpy)-(NEW.lh3_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段lh1_extraction_amount:66抽汽量,的计算57(HH2)-----------------------------------
  IF hhgrade = 2 AND lhgrade = 1 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy OR OLD.hh2_saturated_water_enthalpy != NEW.hh2_saturated_water_enthalpy OR OLD.hh2_extraction_enthalpy != NEW.hh2_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.c_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 1 AND (OLD.c_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_enthalpy ISNULL OR OLD.hh2_saturated_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.c_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_enthalpy NOTNULL AND NEW.hh2_saturated_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.c_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 2 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy OR OLD.hh2_saturated_water_enthalpy != NEW.hh2_saturated_water_enthalpy OR OLD.hh2_extraction_enthalpy != NEW.hh2_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 2 AND (OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_enthalpy ISNULL OR OLD.hh2_saturated_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_enthalpy NOTNULL AND NEW.hh2_saturated_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy OR OLD.hh2_saturated_water_enthalpy != NEW.hh2_saturated_water_enthalpy OR OLD.hh2_extraction_enthalpy != NEW.hh2_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 3 AND (OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_enthalpy ISNULL OR OLD.hh2_saturated_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_enthalpy NOTNULL AND NEW.hh2_saturated_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段lh2_extraction_amount:76抽汽量,的计算60(HH2)-----------------------------------
  IF hhgrade = 2 AND lhgrade = 2 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy OR OLD.hh2_saturated_water_enthalpy != NEW.hh2_saturated_water_enthalpy OR OLD.hh2_extraction_enthalpy != NEW.hh2_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 2 AND (OLD.c_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_enthalpy ISNULL OR OLD.hh2_saturated_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.c_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_enthalpy NOTNULL AND NEW.hh2_saturated_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy OR OLD.hh2_saturated_water_enthalpy != NEW.hh2_saturated_water_enthalpy OR OLD.hh2_extraction_enthalpy != NEW.hh2_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.lh3_water_enthalpy != NEW.lh3_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 3 AND (OLD.lh3_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_enthalpy ISNULL OR OLD.hh2_saturated_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh3_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_enthalpy NOTNULL AND NEW.hh2_saturated_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段lh3_extraction_amount:99抽汽量,的计算66(HH2)-----------------------------------
  IF hhgrade = 2 AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy OR OLD.hh2_saturated_water_enthalpy != NEW.hh2_saturated_water_enthalpy OR OLD.hh2_extraction_enthalpy != NEW.hh2_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.lh3_water_enthalpy != NEW.lh3_water_enthalpy OR OLD.lh3_saturated_water_enthalpy != NEW.lh3_saturated_water_enthalpy OR OLD.lh3_extraction_enthalpy != NEW.lh3_extraction_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh3_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*((((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(


NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))*((NEW.lh2_saturated_water_enthalpy)-(NEW.lh3_saturated_water_enthalpy)))/0.98/((NEW.lh3_extraction_enthalpy)-(NEW.lh3_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND lhgrade = 3 AND (OLD.lh3_extraction_enthalpy ISNULL OR OLD.lh3_saturated_water_enthalpy ISNULL OR OLD.lh3_water_enthalpy ISNULL OR OLD.c_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_enthalpy ISNULL OR OLD.hh2_saturated_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh3_extraction_enthalpy NOTNULL AND NEW.lh3_saturated_water_enthalpy NOTNULL AND NEW.lh3_water_enthalpy NOTNULL AND NEW.c_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_enthalpy NOTNULL AND NEW.hh2_saturated_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh3_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*((((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(


NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))*((NEW.lh2_saturated_water_enthalpy)-(NEW.lh3_saturated_water_enthalpy)))/0.98/((NEW.lh3_extraction_enthalpy)-(NEW.lh3_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;

----------------------实现字段hh1_water_temperature:30给水出水温度,的计算47-----------------------------------
  IF hhgrade = 0 AND OLD.d_water_temperature != NEW.d_water_temperature THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_water_temperature=(NEW.d_water_temperature)
     where plan_id=NEW.plan_id;


  ELSIF hhgrade = 0 AND (OLD.d_water_temperature ISNULL) AND NEW.d_water_temperature NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     hh1_water_temperature=(NEW.d_water_temperature)
     where plan_id=NEW.plan_id;

  END IF;

  IF hhgrade = 0 AND OLD.d_water_temperature != NEW.d_water_temperature THEN

		 update gaspowergeneration_turbine_of_pts set 
     hh1_extraction_amount=0
		 where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND (OLD.d_water_temperature ISNULL) AND NEW.d_water_temperature NOTNULL THEN

		 update gaspowergeneration_turbine_of_pts set 
     hh1_extraction_amount=0
		 where plan_id=NEW.plan_id;
  END IF;

----------------------实现字段d_extraction_amount:56抽汽量,的计算55-----------------------------------
  IF hhgrade = 2 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.hh2_water_enthalpy != NEW.hh2_water_enthalpy OR OLD.hh2_saturated_water_enthalpy != NEW.hh2_saturated_water_enthalpy OR OLD.hh2_extraction_enthalpy != NEW.hh2_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     d_extraction_amount=((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy)))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 2 AND (OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh2_extraction_enthalpy ISNULL OR OLD.hh2_saturated_water_enthalpy ISNULL OR OLD.hh2_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh2_extraction_enthalpy NOTNULL AND NEW.hh2_saturated_water_enthalpy NOTNULL AND NEW.hh2_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     d_extraction_amount=((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)+((((NEW.e_throttle_flow))*((NEW.hh2_water_enthalpy)-(NEW.hh1_water_enthalpy))-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)*0.98*((NEW.hh2_saturated_water_enthalpy)-(NEW.hh1_saturated_water_enthalpy)))/((NEW.hh2_extraction_enthalpy)-(NEW.hh2_saturated_water_enthalpy))/0.98))*((NEW.hh2_saturated_water_enthalpy)-(NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy)))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 1 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.hh1_water_enthalpy != NEW.hh1_water_enthalpy OR OLD.hh1_saturated_water_enthalpy != NEW.hh1_saturated_water_enthalpy OR OLD.hh1_extraction_enthalpy != NEW.hh1_extraction_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     d_extraction_amount=((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy)))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 1 AND (OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.hh1_extraction_enthalpy ISNULL OR OLD.hh1_saturated_water_enthalpy ISNULL OR OLD.hh1_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.hh1_extraction_enthalpy NOTNULL AND NEW.hh1_saturated_water_enthalpy NOTNULL AND NEW.hh1_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     d_extraction_amount=((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-((((NEW.e_throttle_flow))*((NEW.hh1_water_enthalpy)-(NEW.d_water_enthalpy))/((NEW.hh1_extraction_enthalpy)-(NEW.hh1_saturated_water_enthalpy))/0.98))*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy)))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     d_extraction_amount=((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy)))
     where plan_id=NEW.plan_id;
		 update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=0
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND (OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     d_extraction_amount=((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy)))
     where plan_id=NEW.plan_id;
	   update gaspowergeneration_turbine_of_pts set 

     hh1_extraction_amount=0
     where plan_id=NEW.plan_id;
  END IF;

----------------------实现字段lh1_extraction_amount:66抽汽量,的计算58-----------------------------------
  IF hhgrade = 0 AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 3 AND (OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 2 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 2 AND (OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 1 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.c_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 1 AND (OLD.c_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.c_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh1_extraction_amount=((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.c_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98
     where plan_id=NEW.plan_id;

  END IF;
  
  ----------------------实现字段lh2_extraction_amount:76抽汽量,的计算61-----------------------------------
  IF hhgrade = 0 AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.lh3_water_enthalpy != NEW.lh3_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 3 AND (OLD.lh3_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh3_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 2 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 2 AND (OLD.c_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.c_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh2_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;
  
  ----------------------实现字段lh3_extraction_amount:99抽汽量,的计算67-----------------------------------
 IF hhgrade = 0 AND lhgrade = 3 AND OLD.h_enthalpy != NEW.h_enthalpy OR OLD.d_water_enthalpy != NEW.d_water_enthalpy OR OLD.d_extraction_enthalpy != NEW.d_extraction_enthalpy OR OLD.lh1_water_enthalpy != NEW.lh1_water_enthalpy OR OLD.lh1_saturated_water_enthalpy != NEW.lh1_saturated_water_enthalpy OR OLD.lh1_extraction_enthalpy != NEW.lh1_extraction_enthalpy OR OLD.lh2_water_enthalpy != NEW.lh2_water_enthalpy OR OLD.lh2_saturated_water_enthalpy != NEW.lh2_saturated_water_enthalpy OR OLD.lh2_extraction_enthalpy != NEW.lh2_extraction_enthalpy OR OLD.c_water_enthalpy != NEW.c_water_enthalpy OR OLD.lh3_water_enthalpy != NEW.lh3_water_enthalpy OR OLD.lh3_saturated_water_enthalpy != NEW.lh3_saturated_water_enthalpy OR OLD.lh3_extraction_enthalpy != NEW.lh3_extraction_enthalpy OR OLD.e_steam_water_loss != NEW.e_steam_water_loss OR OLD.e_throttle_flow != NEW.e_throttle_flow THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh3_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*((((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))*((NEW.lh2_saturated_water_enthalpy)-(NEW.lh3_saturated_water_enthalpy)))/0.98/((NEW.lh3_extraction_enthalpy)-(NEW.lh3_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  ELSIF hhgrade = 0 AND lhgrade = 3 AND (OLD.lh3_extraction_enthalpy ISNULL OR OLD.lh3_saturated_water_enthalpy ISNULL OR OLD.lh3_water_enthalpy ISNULL OR OLD.c_water_enthalpy ISNULL OR OLD.lh2_extraction_enthalpy ISNULL OR OLD.lh2_saturated_water_enthalpy ISNULL OR OLD.lh2_water_enthalpy ISNULL OR OLD.lh1_extraction_enthalpy ISNULL OR OLD.lh1_saturated_water_enthalpy ISNULL OR OLD.lh1_water_enthalpy ISNULL OR OLD.d_extraction_enthalpy ISNULL OR OLD.d_water_enthalpy ISNULL OR OLD.h_enthalpy ISNULL OR OLD.e_throttle_flow ISNULL OR OLD.e_steam_water_loss ISNULL) AND NEW.lh3_extraction_enthalpy NOTNULL AND NEW.lh3_saturated_water_enthalpy NOTNULL AND NEW.lh3_water_enthalpy NOTNULL AND NEW.c_water_enthalpy NOTNULL AND NEW.lh2_extraction_enthalpy NOTNULL AND NEW.lh2_saturated_water_enthalpy NOTNULL AND NEW.lh2_water_enthalpy NOTNULL AND NEW.lh1_extraction_enthalpy NOTNULL AND NEW.lh1_saturated_water_enthalpy NOTNULL AND NEW.lh1_water_enthalpy NOTNULL AND NEW.d_extraction_enthalpy NOTNULL AND NEW.d_water_enthalpy NOTNULL AND NEW.h_enthalpy NOTNULL AND NEW.e_throttle_flow NOTNULL AND NEW.e_steam_water_loss NOTNULL THEN
     update gaspowergeneration_turbine_of_pts set 

     lh3_extraction_amount=(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh3_water_enthalpy)-(NEW.c_water_enthalpy))-0.98*((((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh2_water_enthalpy)-(NEW.lh3_water_enthalpy))-0.98*(((NEW.e_throttle_flow)-(((NEW.e_throttle_flow)*(NEW.e_steam_water_loss)*((NEW.d_water_enthalpy)-(NEW.h_enthalpy))+((NEW.e_throttle_flow)-(NEW.e_throttle_flow)*(NEW.e_steam_water_loss))*((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))-0*((NEW.d_water_enthalpy))*0.98)/(((NEW.d_extraction_enthalpy)-(NEW.d_water_enthalpy))*0.98+((NEW.d_water_enthalpy)-(NEW.lh1_water_enthalpy))))-((NEW.e_steam_water_loss))*((NEW.e_throttle_flow)))*((NEW.lh1_water_enthalpy)-(NEW.lh2_water_enthalpy))/((NEW.lh1_extraction_enthalpy)-(NEW.lh1_saturated_water_enthalpy))/0.98)*((NEW.lh1_saturated_water_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))/0.98/((NEW.lh2_extraction_enthalpy)-(NEW.lh2_saturated_water_enthalpy)))*((NEW.lh2_saturated_water_enthalpy)-(NEW.lh3_saturated_water_enthalpy)))/0.98/((NEW.lh3_extraction_enthalpy)-(NEW.lh3_saturated_water_enthalpy))
     where plan_id=NEW.plan_id;

  END IF;
   
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_turbine_of_pts" AFTER UPDATE OF
"e_turbine_efficiency",
"e_mechanical_efficiency",
"e_generator_efficiency",
"e_steam_type",
"e_steam_pressure",
"e_steam_temperature",
"e_steam_flow",
"e_steam_entropy",
"e_steam_enthalpy",
"e_exhaust_point_pressure",
"e_exhaust_point_temperature",
"e_exhaust_point_entropy",
"e_exhaust_point_enthalpy",
"e_exhaust_point_flow",
"e_exhaust_after_steam",
"e_exhaust_after_pressure",
"e_exhaust_after_enthalpy",
"e_exhaust_after_entropy",
"e_steam_exhaust_pressure",
"e_steam_exhaust_enthalpy",
"e_backpressure_pressure",
"e_backpressure_temperature",
"e_backpressure_enthalpy",
"e_backpressure_flow",
"e_gross_generation",
"e_hot_data",
"e_steam_extraction",
"e_steam_extraction_select",
"e_steam_water_loss",
"e_throttle_flow",
"h_assume",
"h_temperature",
"h_pressure",
"h_enthalpy",
"h_amount",
"hh1_water_temperature",
"hh1_water_enthalpy",
"hh1_top_difference",
"hh1_saturated_water_temperature",
"hh1_saturated_water_enthalpy",
"hh1_work_pressure",
"hh1_pressure_loss",
"hh1_extraction_pressure",
"hh1_extraction_enthalpy",
"hh1_extraction_amount",
"hh2_water_temperature",
"hh2_water_enthalpy",
"hh2_top_difference",
"hh2_saturated_water_temperature",
"hh2_saturated_water_enthalpy",
"hh2_work_pressure",
"hh2_pressure_loss",
"hh2_extraction_pressure",
"hh2_extraction_enthalpy",
"hh2_extraction_amount",
"hh3_water_temperature",
"hh3_water_enthalpy",
"hh3_top_difference",
"hh3_saturated_water_temperature",
"hh3_saturated_water_enthalpy",
"hh3_work_pressure",
"hh3_pressure_loss",
"hh3_extraction_pressure",
"hh3_extraction_enthalpy",
"hh3_extraction_amount",
"d_water_temperature",
"d_water_enthalpy",
"d_work_pressure",
"d_pressure_loss",
"d_extraction_pressure",
"d_extraction_enthalpy",
"d_extraction_amount",
"lh1_water_temperature",
"lh1_water_enthalpy",
"lh1_top_difference",
"lh1_saturated_water_temperature",
"lh1_saturated_water_enthalpy",
"lh1_work_pressure",
"lh1_pressure_loss",
"lh1_extraction_pressure",
"lh1_extraction_enthalpy",
"lh1_extraction_amount",
"lh2_water_temperature",
"lh2_water_enthalpy",
"lh2_top_difference",
"lh2_saturated_water_temperature",
"lh2_saturated_water_enthalpy",
"lh2_work_pressure",
"lh2_pressure_loss",
"lh2_extraction_pressure",
"lh2_extraction_enthalpy",
"lh2_extraction_amount",
"lh3_water_temperature",
"lh3_water_enthalpy",
"lh3_top_difference",
"lh3_saturated_water_temperature",
"lh3_saturated_water_enthalpy",
"lh3_work_pressure",
"lh3_pressure_loss",
"lh3_extraction_pressure",
"lh3_extraction_enthalpy",
"lh3_extraction_amount",
"c_water_temperature",
"c_water_enthalpy",
"c_work_pressure",
"c_pressure_loss",
"c_extraction_pressure",
"c_extraction_enthalpy",
"c_extraction_amount",
"i_turbine_efficiency",
"i_mechanical_efficiency",
"i_generator_efficiency",
"i_steam_pressure",
"i_steam_temperature",
"i_steam_flow",
"i_steam_entropy",
"i_steam_enthalpy",
"i_high1_pressure",
"i_high1_entropy",
"i_high1_temperature",
"i_high1_enthalpy",
"i_high1_flow",
"i_steam_hh1_power",
"i_high2_pressure",
"i_high2_entropy",
"i_high2_temperature",
"i_high2_enthalpy",
"i_high2_flow",
"i_hh1_hh2_power",
"i_deoxidize_pressure",
"i_deoxidize_entropy",
"i_deoxidize_temperature",
"i_deoxidize_enthalpy",
"i_deoxidize_flow",
"i_hh2_deoxidize_power",
"i_exhaust_point_pressure",
"i_exhaust_point_temperature",
"i_exhaust_point_entropy",
"i_exhaust_point_enthalpy",
"i_exhaust_point_flow",
"i_deoxidize_exhaust_power",
"i_low1_pressure",
"i_low1_entropy",
"i_low1_temperature",
"i_low1_enthalpy",
"i_low1_flow",
"i_exhaust_lh1_power",
"i_low2_pressure",
"i_low2_entropy",
"i_low2_temperature",
"i_low2_enthalpy",
"i_low2_flow",
"i_lh1_lh2_power",
"i_steam_exhaust_pressure",
"i_steam_exhaust_entropy",
"i_steam_exhaust_enthalpy",
"i_steam_exhaust_enthalpy_actual",
"i_steam_exhaust_enthalpy_steam",
"i_steam_exhaust_enthalpy_water",
"i_steam_exhaust_dry",
"i_steam_exhaust_flow",
"i_lh2_steam_power",
"i_total_power",
"i_calculation_error"
ON "public"."gaspowergeneration_turbine_of_pts"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_turbine_of_pts"();