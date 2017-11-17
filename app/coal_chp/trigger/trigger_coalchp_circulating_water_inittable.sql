CREATE OR REPLACE FUNCTION coalchp_circulating_water()
RETURNS TRIGGER AS
$BODY$
BEGIN

----------------------v_steam_exhaust_flow_summer:乏汽流量(夏季),的计算1-----------------------------------
  IF OLD.v_steam_exhaust_flow_winter != NEW.v_steam_exhaust_flow_winter THEN
     update coalchp_circulating_water set 

     v_steam_exhaust_flow_summer=NEW.v_steam_exhaust_flow_winter+10
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_steam_exhaust_flow_winter ISNULL) AND NEW.v_steam_exhaust_flow_winter NOTNULL THEN
     update coalchp_circulating_water set 

     v_steam_exhaust_flow_summer=NEW.v_steam_exhaust_flow_winter+10
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_circulating_water_winter:循环水量,的计算1-----------------------------------
  IF OLD.v_steam_exhaust_flow_select != NEW.v_steam_exhaust_flow_select OR OLD.v_circulating_ratio_winter != NEW.v_circulating_ratio_winter THEN
     update coalchp_circulating_water set 

     v_circulating_water_winter=NEW.v_steam_exhaust_flow_select*NEW.v_circulating_ratio_winter
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_circulating_ratio_winter ISNULL OR OLD.v_steam_exhaust_flow_select ISNULL) AND NEW.v_circulating_ratio_winter NOTNULL AND NEW.v_steam_exhaust_flow_select NOTNULL THEN
     update coalchp_circulating_water set 

     v_circulating_water_winter=NEW.v_steam_exhaust_flow_select*NEW.v_circulating_ratio_winter
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_circulating_water_summer:循环水量,的计算1-----------------------------------
  IF OLD.v_steam_exhaust_flow_select != NEW.v_steam_exhaust_flow_select OR OLD.v_circulating_ratio_summer != NEW.v_circulating_ratio_summer THEN
     update coalchp_circulating_water set 

     v_circulating_water_summer=NEW.v_steam_exhaust_flow_select*NEW.v_circulating_ratio_summer
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_circulating_ratio_summer ISNULL OR OLD.v_steam_exhaust_flow_select ISNULL) AND NEW.v_circulating_ratio_summer NOTNULL AND NEW.v_steam_exhaust_flow_select NOTNULL THEN
     update coalchp_circulating_water set 

     v_circulating_water_summer=NEW.v_steam_exhaust_flow_select*NEW.v_circulating_ratio_summer
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_total_circulating_water_winter:总循环水量,的计算2-----------------------------------
  IF OLD.v_circulating_water_winter != NEW.v_circulating_water_winter OR OLD.v_auxiliary_engine_cooling_winter != NEW.v_auxiliary_engine_cooling_winter THEN
     update coalchp_circulating_water set 

     v_total_circulating_water_winter=NEW.v_circulating_water_winter+NEW.v_auxiliary_engine_cooling_winter
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_auxiliary_engine_cooling_winter ISNULL OR OLD.v_circulating_water_winter ISNULL) AND NEW.v_auxiliary_engine_cooling_winter NOTNULL AND NEW.v_circulating_water_winter NOTNULL THEN
     update coalchp_circulating_water set 

     v_total_circulating_water_winter=NEW.v_circulating_water_winter+NEW.v_auxiliary_engine_cooling_winter
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_total_circulating_water_summer:总循环水量,的计算2-----------------------------------
  IF OLD.v_circulating_water_summer != NEW.v_circulating_water_summer OR OLD.v_auxiliary_engine_cooling_summer != NEW.v_auxiliary_engine_cooling_summer THEN
     update coalchp_circulating_water set 

     v_total_circulating_water_summer=NEW.v_circulating_water_winter+NEW.v_auxiliary_engine_cooling_summer
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_auxiliary_engine_cooling_summer ISNULL OR OLD.v_circulating_water_winter ISNULL) AND NEW.v_auxiliary_engine_cooling_summer NOTNULL AND NEW.v_circulating_water_winter NOTNULL THEN
     update coalchp_circulating_water set 

     v_total_circulating_water_winter=NEW.v_circulating_water_winter+NEW.v_auxiliary_engine_cooling_summer
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_evaporation_loss_rate:蒸发损失率,的计算3-----------------------------------
  IF OLD.v_enter_the_outlet_temperature_difference != NEW.v_enter_the_outlet_temperature_difference OR OLD.v_k != NEW.v_k THEN
     update coalchp_circulating_water set 

     v_evaporation_loss_rate=NEW.v_k*NEW.v_enter_the_outlet_temperature_difference
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_k ISNULL OR OLD.v_enter_the_outlet_temperature_difference ISNULL) AND NEW.v_k NOTNULL AND NEW.v_enter_the_outlet_temperature_difference NOTNULL THEN
     update coalchp_circulating_water set 

     v_evaporation_loss_rate=NEW.v_k*NEW.v_enter_the_outlet_temperature_difference
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_evaporation_loss:蒸发损失,的计算4-----------------------------------
  IF OLD.v_evaporation_loss_rate != NEW.v_evaporation_loss_rate OR OLD.v_total_circulating_water_select != NEW.v_total_circulating_water_select THEN
     update coalchp_circulating_water set 

     v_evaporation_loss=NEW.v_evaporation_loss_rate*NEW.v_total_circulating_water_select/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_evaporation_loss_rate ISNULL OR OLD.v_total_circulating_water_select ISNULL) AND NEW.v_evaporation_loss_rate NOTNULL AND NEW.v_total_circulating_water_select NOTNULL THEN
     update coalchp_circulating_water set 

     v_evaporation_loss=NEW.v_evaporation_loss_rate*NEW.v_total_circulating_water_select/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_partial_blow_loss:分吹损失,的计算5-----------------------------------
  IF OLD.v_blowing_loss_rate != NEW.v_blowing_loss_rate OR OLD.v_total_circulating_water_select != NEW.v_total_circulating_water_select THEN
     update coalchp_circulating_water set 

     v_partial_blow_loss=NEW.v_blowing_loss_rate*NEW.v_total_circulating_water_select/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_blowing_loss_rate ISNULL OR OLD.v_total_circulating_water_select ISNULL) AND NEW.v_blowing_loss_rate NOTNULL AND NEW.v_total_circulating_water_select NOTNULL THEN
     update coalchp_circulating_water set 

     v_partial_blow_loss=NEW.v_blowing_loss_rate*NEW.v_total_circulating_water_select/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_discharge_loss:排污损失率,的计算6-----------------------------------
  IF OLD.v_evaporation_loss_rate != NEW.v_evaporation_loss_rate OR OLD.v_blowing_loss_rate != NEW.v_blowing_loss_rate OR OLD.v_concentrate_ratio != NEW.v_concentrate_ratio THEN
     update coalchp_circulating_water set 

     v_discharge_loss=(NEW.v_evaporation_loss_rate-NEW.v_blowing_loss_rate*(NEW.v_concentrate_ratio-1))/(NEW.v_concentrate_ratio-1)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_concentrate_ratio ISNULL OR OLD.v_blowing_loss_rate ISNULL OR OLD.v_evaporation_loss_rate ISNULL) AND NEW.v_concentrate_ratio NOTNULL AND NEW.v_blowing_loss_rate NOTNULL AND NEW.v_evaporation_loss_rate NOTNULL THEN
     update coalchp_circulating_water set 

     v_discharge_loss=(NEW.v_evaporation_loss_rate-NEW.v_blowing_loss_rate*(NEW.v_concentrate_ratio-1))/(NEW.v_concentrate_ratio-1)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_discharge_capacity:排污量,的计算7-----------------------------------
  IF OLD.v_discharge_loss != NEW.v_discharge_loss OR OLD.v_total_circulating_water_select != NEW.v_total_circulating_water_select THEN
     update coalchp_circulating_water set 

     v_discharge_capacity=NEW.v_discharge_loss*NEW.v_total_circulating_water_select/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_discharge_loss ISNULL OR OLD.v_total_circulating_water_select ISNULL) AND NEW.v_discharge_loss NOTNULL AND NEW.v_total_circulating_water_select NOTNULL THEN
     update coalchp_circulating_water set 

     v_discharge_capacity=NEW.v_discharge_loss*NEW.v_total_circulating_water_select/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_amount_of_makeup_water_winter:补充水量,的计算8-----------------------------------
  IF OLD.v_evaporation_loss != NEW.v_evaporation_loss OR OLD.v_partial_blow_loss != NEW.v_partial_blow_loss OR OLD.v_discharge_capacity != NEW.v_discharge_capacity THEN
     update coalchp_circulating_water set 

     v_amount_of_makeup_water_winter=NEW.v_discharge_capacity+NEW.v_partial_blow_loss+NEW.v_evaporation_loss
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_discharge_capacity ISNULL OR OLD.v_partial_blow_loss ISNULL OR OLD.v_evaporation_loss ISNULL) AND NEW.v_discharge_capacity NOTNULL AND NEW.v_partial_blow_loss NOTNULL AND NEW.v_evaporation_loss NOTNULL THEN
     update coalchp_circulating_water set 

     v_amount_of_makeup_water_winter=NEW.v_discharge_capacity+NEW.v_partial_blow_loss+NEW.v_evaporation_loss
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_amount_of_makeup_water_summer:补充水量,的计算8-----------------------------------
  IF OLD.v_partial_blow_loss != NEW.v_partial_blow_loss OR OLD.v_amount_of_makeup_water_winter != NEW.v_amount_of_makeup_water_winter THEN
     update coalchp_circulating_water set 

     v_amount_of_makeup_water_summer=NEW.v_amount_of_makeup_water_winter/NEW.v_partial_blow_loss
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_partial_blow_loss ISNULL OR OLD.v_amount_of_makeup_water_winter ISNULL) AND NEW.v_partial_blow_loss NOTNULL AND NEW.v_amount_of_makeup_water_winter NOTNULL THEN
     update coalchp_circulating_water set 

     v_amount_of_makeup_water_summer=NEW.v_amount_of_makeup_water_winter/NEW.v_partial_blow_loss
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_circulating_pool_size:循环水池尺寸,的计算9-----------------------------------
  IF OLD.v_total_circulating_water_select != NEW.v_total_circulating_water_select THEN
     update coalchp_circulating_water set 

     v_circulating_pool_size=NEW.v_total_circulating_water_select/60*15
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_total_circulating_water_select ISNULL) AND NEW.v_total_circulating_water_select NOTNULL THEN
     update coalchp_circulating_water set 

     v_circulating_pool_size=NEW.v_total_circulating_water_select/60*15
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段v_check_circulating_pool_size:校核循环水池尺寸,的计算10-----------------------------------
  IF OLD.v_circulating_pool_long != NEW.v_circulating_pool_long OR OLD.v_circulating_pool_wide != NEW.v_circulating_pool_wide OR OLD.v_circulating_pool_hight != NEW.v_circulating_pool_hight THEN
     update coalchp_circulating_water set 

     v_check_circulating_pool_size=NEW.v_circulating_pool_long*NEW.v_circulating_pool_wide*NEW.v_circulating_pool_hight
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_circulating_pool_hight ISNULL OR OLD.v_circulating_pool_wide ISNULL OR OLD.v_circulating_pool_long ISNULL) AND NEW.v_circulating_pool_hight NOTNULL AND NEW.v_circulating_pool_wide NOTNULL AND NEW.v_circulating_pool_long NOTNULL THEN
     update coalchp_circulating_water set 

     v_check_circulating_pool_size=NEW.v_circulating_pool_long*NEW.v_circulating_pool_wide*NEW.v_circulating_pool_hight
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_pressure_condenser:凝汽器循环水进水工作压力,的计算11-----------------------------------
  IF OLD.c_condenser_tube_friction != NEW.c_condenser_tube_friction OR OLD.c_circulating_water_pressure != NEW.c_circulating_water_pressure THEN
     update coalchp_circulating_water set 

     c_pressure_condenser=NEW.c_circulating_water_pressure+NEW.c_condenser_tube_friction
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_circulating_water_pressure ISNULL OR OLD.c_condenser_tube_friction ISNULL) AND NEW.c_circulating_water_pressure NOTNULL AND NEW.c_condenser_tube_friction NOTNULL THEN
     update coalchp_circulating_water set 

     c_pressure_condenser=NEW.c_circulating_water_pressure+NEW.c_condenser_tube_friction
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_pumping_head:总扬程,的计算12-----------------------------------
  IF OLD.c_pressure_condenser != NEW.c_pressure_condenser OR OLD.c_circulating_pool_pressure != NEW.c_circulating_pool_pressure OR OLD.c_circulation_height_difference != NEW.c_circulation_height_difference OR OLD.c_height_difference_inlet != NEW.c_height_difference_inlet OR OLD.c_pipe_losses != NEW.c_pipe_losses OR OLD.c_y_losses != NEW.c_y_losses THEN
     update coalchp_circulating_water set 

     c_pumping_head=102*(NEW.c_pressure_condenser-NEW.c_circulating_pool_pressure)+NEW.c_circulation_height_difference-NEW.c_height_difference_inlet+(NEW.c_pipe_losses+NEW.c_y_losses)*1.2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_y_losses ISNULL OR OLD.c_pipe_losses ISNULL OR OLD.c_height_difference_inlet ISNULL OR OLD.c_circulation_height_difference ISNULL OR OLD.c_circulating_pool_pressure ISNULL OR OLD.c_pressure_condenser ISNULL) AND NEW.c_y_losses NOTNULL AND NEW.c_pipe_losses NOTNULL AND NEW.c_height_difference_inlet NOTNULL AND NEW.c_circulation_height_difference NOTNULL AND NEW.c_circulating_pool_pressure NOTNULL AND NEW.c_pressure_condenser NOTNULL THEN
     update coalchp_circulating_water set 

     c_pumping_head=102*(NEW.c_pressure_condenser-NEW.c_circulating_pool_pressure)+NEW.c_circulation_height_difference-NEW.c_height_difference_inlet+(NEW.c_pipe_losses+NEW.c_y_losses)*1.2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_flow:流量,的计算13-----------------------------------
  IF OLD.v_total_circulating_water_select != NEW.v_total_circulating_water_select THEN
     update coalchp_circulating_water set 

     c_flow=NEW.v_total_circulating_water_select/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.v_total_circulating_water_select ISNULL) AND NEW.v_total_circulating_water_select NOTNULL THEN
     update coalchp_circulating_water set 

     c_flow=NEW.v_total_circulating_water_select/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_supporting_motor_power:配套电机功率,的计算14-----------------------------------
  IF OLD.c_pumping_head != NEW.c_pumping_head OR OLD.c_flow != NEW.c_flow OR OLD.c_pump_power != NEW.c_pump_power OR OLD.c_mechine_power != NEW.c_mechine_power OR OLD.c_motor_power != NEW.c_motor_power OR OLD.c_motor_backup_coefficient != NEW.c_motor_backup_coefficient THEN
     update coalchp_circulating_water set 

     c_supporting_motor_power=NEW.c_motor_backup_coefficient*1000*9.8*NEW.c_pumping_head*NEW.c_flow/3600/1000/NEW.c_pump_power/NEW.c_mechine_power/NEW.c_motor_power
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_motor_backup_coefficient ISNULL OR OLD.c_motor_power ISNULL OR OLD.c_mechine_power ISNULL OR OLD.c_pump_power ISNULL OR OLD.c_flow ISNULL OR OLD.c_pumping_head ISNULL) AND NEW.c_motor_backup_coefficient NOTNULL AND NEW.c_motor_power NOTNULL AND NEW.c_mechine_power NOTNULL AND NEW.c_pump_power NOTNULL AND NEW.c_flow NOTNULL AND NEW.c_pumping_head NOTNULL THEN
     update coalchp_circulating_water set 

     c_supporting_motor_power=NEW.c_motor_backup_coefficient*1000*9.8*NEW.c_pumping_head*NEW.c_flow/3600/1000/NEW.c_pump_power/NEW.c_mechine_power/NEW.c_motor_power
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_forklift_parameters_power:选用型号功率,的计算15-----------------------------------
  IF OLD.c_supporting_motor_power != NEW.c_supporting_motor_power THEN
     update coalchp_circulating_water set 

     c_forklift_parameters_power=NEW.c_supporting_motor_power/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_supporting_motor_power ISNULL) AND NEW.c_supporting_motor_power NOTNULL THEN
     update coalchp_circulating_water set 

     c_forklift_parameters_power=NEW.c_supporting_motor_power/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_forklift_parameters_flow:选用型号流量,的计算16-----------------------------------
  IF OLD.c_flow != NEW.c_flow THEN
     update coalchp_circulating_water set 

     c_forklift_parameters_flow=NEW.c_flow/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_flow ISNULL) AND NEW.c_flow NOTNULL THEN
     update coalchp_circulating_water set 

     c_forklift_parameters_flow=NEW.c_flow/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_forklift_parameters_lift:选用型号扬程,的计算17-----------------------------------
  IF OLD.c_pumping_head != NEW.c_pumping_head THEN
     update coalchp_circulating_water set 

     c_forklift_parameters_lift=NEW.c_pumping_head
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_pumping_head ISNULL) AND NEW.c_pumping_head NOTNULL THEN
     update coalchp_circulating_water set 

     c_forklift_parameters_lift=NEW.c_pumping_head
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_circulating_water" AFTER UPDATE OF
"v_steam_exhaust_flow_winter",
"v_enter_the_outlet_temperature_difference",
"v_k",
"v_evaporation_loss_rate",
"v_evaporation_loss",
"v_blowing_loss_rate",
"v_partial_blow_loss",
"v_concentrate_ratio",
"v_discharge_loss",
"v_discharge_capacity",
"v_circulating_pool_long",
"v_circulating_pool_wide",
"v_circulating_pool_hight",
"c_pressure_condenser",
"c_condenser_tube_friction",
"c_circulating_water_pressure",
"c_circulating_pool_pressure",
"c_circulation_height_difference",
"c_height_difference_inlet",
"c_pipe_losses",
"c_y_losses",
"c_pumping_head",
"c_flow",
"c_pump_power",
"c_mechine_power",
"c_motor_power",
"v_steam_exhaust_flow_select",
"c_motor_backup_coefficient",
"c_supporting_motor_power",
"v_circulating_ratio_winter",
"v_circulating_water_winter",
"v_auxiliary_engine_cooling_winter",
"v_total_circulating_water_select"
ON "public"."coalchp_circulating_water"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_circulating_water"();
