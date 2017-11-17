CREATE OR REPLACE FUNCTION coalchp_coal_handingsystem_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段b_coal_daily_consumption:日耗煤量,的计算1-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check OR OLD.b_boiler_daily_utilization_hours_check != NEW.b_boiler_daily_utilization_hours_check THEN
     update coalchp_coal_handingsystem set 

     b_coal_daily_consumption_check=NEW.b_boiler_rated_coal_capacity_check*NEW.b_boiler_daily_utilization_hours_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_boiler_daily_utilization_hours_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.b_boiler_daily_utilization_hours_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     b_coal_daily_consumption_check=NEW.b_boiler_rated_coal_capacity_check*NEW.b_boiler_daily_utilization_hours_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段b_coal_annual_consumption:年耗煤量,的计算2-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check OR OLD.b_boiler_annual_utilization_hours_check != NEW.b_boiler_annual_utilization_hours_check THEN
     update coalchp_coal_handingsystem set 

     b_coal_annual_consumption_check=NEW.b_boiler_annual_utilization_hours_check*NEW.b_boiler_rated_coal_capacity_check/10000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_boiler_annual_utilization_hours_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.b_boiler_annual_utilization_hours_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     b_coal_annual_consumption_check=NEW.b_boiler_annual_utilization_hours_check*NEW.b_boiler_rated_coal_capacity_check/10000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段b_daily_rail_coal_amount:铁路来煤日计算煤量,的计算3-----------------------------------
  IF OLD.b_coal_daily_consumption_check != NEW.b_coal_daily_consumption_check OR OLD.b_daily_coal_unbalanced_coefficient_check != NEW.b_daily_coal_unbalanced_coefficient_check THEN
     update coalchp_coal_handingsystem set 

     b_daily_rail_coal_amount_check=NEW.b_daily_coal_unbalanced_coefficient_check*NEW.b_coal_daily_consumption_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_daily_coal_unbalanced_coefficient_check ISNULL OR OLD.b_coal_daily_consumption_check ISNULL) AND NEW.b_daily_coal_unbalanced_coefficient_check NOTNULL AND NEW.b_coal_daily_consumption_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     b_daily_rail_coal_amount_check=NEW.b_daily_coal_unbalanced_coefficient_check*NEW.b_coal_daily_consumption_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段b_daily_vehicle_coal_amount:汽车来煤日计算煤量,的计算4-----------------------------------
  IF OLD.b_boiler_daily_utilization_hours_check != NEW.b_boiler_daily_utilization_hours_check OR OLD.b_boiler_annual_utilization_hours_check != NEW.b_boiler_annual_utilization_hours_check OR OLD.b_coal_annual_consumption_check != NEW.b_coal_annual_consumption_check OR OLD.b_daily_coal_unbalanced_coefficient_check != NEW.b_daily_coal_unbalanced_coefficient_check THEN
     update coalchp_coal_handingsystem set 

     b_daily_vehicle_coal_amount_check=NEW.b_daily_coal_unbalanced_coefficient_check*NEW.b_coal_annual_consumption_check*10000*NEW.b_boiler_daily_utilization_hours_check/NEW.b_boiler_annual_utilization_hours_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_daily_coal_unbalanced_coefficient_check ISNULL OR OLD.b_coal_annual_consumption_check ISNULL OR OLD.b_boiler_annual_utilization_hours_check ISNULL OR OLD.b_boiler_daily_utilization_hours_check ISNULL) AND NEW.b_daily_coal_unbalanced_coefficient_check NOTNULL AND NEW.b_coal_annual_consumption_check NOTNULL AND NEW.b_boiler_annual_utilization_hours_check NOTNULL AND NEW.b_boiler_daily_utilization_hours_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     b_daily_vehicle_coal_amount_check=NEW.b_daily_coal_unbalanced_coefficient_check*NEW.b_coal_annual_consumption_check*10000*NEW.b_boiler_daily_utilization_hours_check/NEW.b_boiler_annual_utilization_hours_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_boiler_hour_coal_capacity:锅炉每小时最大耗煤量,的计算5-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check THEN
     update coalchp_coal_handingsystem set 

     c_boiler_hour_coal_capacity_check=NEW.b_boiler_rated_coal_capacity_check*2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     c_boiler_hour_coal_capacity_check=NEW.b_boiler_rated_coal_capacity_check*2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_coalyard_store_amount:煤场存储量,的计算6-----------------------------------
  IF OLD.c_boiler_daily_working_hours_check != NEW.c_boiler_daily_working_hours_check OR OLD.c_coal_store_days_check != NEW.c_coal_store_days_check OR OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check THEN
     update coalchp_coal_handingsystem set 

     c_coalyard_store_amount_check=NEW.b_boiler_rated_coal_capacity_check*NEW.c_boiler_daily_working_hours_check*NEW.c_coal_store_days_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_coal_store_days_check ISNULL OR OLD.c_boiler_daily_working_hours_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.c_coal_store_days_check NOTNULL AND NEW.c_boiler_daily_working_hours_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     c_coalyard_store_amount_check=NEW.b_boiler_rated_coal_capacity_check*NEW.c_boiler_daily_working_hours_check*NEW.c_coal_store_days_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_coalyard_area:煤场面积,的计算7-----------------------------------
  IF OLD.c_boiler_daily_working_hours_check != NEW.c_boiler_daily_working_hours_check OR OLD.c_coal_store_days_check != NEW.c_coal_store_days_check OR OLD.c_coal_channel_occupy_coefficient_check != NEW.c_coal_channel_occupy_coefficient_check OR OLD.c_coal_shape_coefficient_check != NEW.c_coal_shape_coefficient_check OR OLD.c_coal_height_check != NEW.c_coal_height_check OR OLD.c_coal_bulk_density_check != NEW.c_coal_bulk_density_check OR OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check THEN
     update coalchp_coal_handingsystem set 

     c_coalyard_area_check=NEW.b_boiler_rated_coal_capacity_check*NEW.c_boiler_daily_working_hours_check*NEW.c_coal_channel_occupy_coefficient_check*NEW.c_coal_store_days_check/NEW.c_coal_shape_coefficient_check/NEW.c_coal_height_check/NEW.c_coal_bulk_density_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_coal_bulk_density_check ISNULL OR OLD.c_coal_height_check ISNULL OR OLD.c_coal_shape_coefficient_check ISNULL OR OLD.c_coal_channel_occupy_coefficient_check ISNULL OR OLD.c_coal_store_days_check ISNULL OR OLD.c_boiler_daily_working_hours_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.c_coal_bulk_density_check NOTNULL AND NEW.c_coal_height_check NOTNULL AND NEW.c_coal_shape_coefficient_check NOTNULL AND NEW.c_coal_channel_occupy_coefficient_check NOTNULL AND NEW.c_coal_store_days_check NOTNULL AND NEW.c_boiler_daily_working_hours_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     c_coalyard_area_check=NEW.b_boiler_rated_coal_capacity_check*NEW.c_boiler_daily_working_hours_check*NEW.c_coal_channel_occupy_coefficient_check*NEW.c_coal_store_days_check/NEW.c_coal_shape_coefficient_check/NEW.c_coal_height_check/NEW.c_coal_bulk_density_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_width:宽,的计算8-----------------------------------
  IF OLD.c_coalyard_area_check != NEW.c_coalyard_area_check OR OLD.c_height_check != NEW.c_height_check THEN
     update coalchp_coal_handingsystem set 

     c_width_check=NEW.c_coalyard_area_check/NEW.c_height_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_height_check ISNULL OR OLD.c_coalyard_area_check ISNULL) AND NEW.c_height_check NOTNULL AND NEW.c_coalyard_area_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     c_width_check=NEW.c_coalyard_area_check/NEW.c_height_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_effective_cubage_calculated:有效容积-计算,的计算9-----------------------------------
  IF OLD.c_coal_bulk_density_check != NEW.c_coal_bulk_density_check OR OLD.e_coal_bunker_counts_check != NEW.e_coal_bunker_counts_check OR OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check THEN
     update coalchp_coal_handingsystem set 

     e_effective_cubage_calculated_check=10*NEW.b_boiler_rated_coal_capacity_check/NEW.e_coal_bunker_counts_check/NEW.c_coal_bulk_density_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_coal_bunker_counts_check ISNULL OR OLD.c_coal_bulk_density_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.e_coal_bunker_counts_check NOTNULL AND NEW.c_coal_bulk_density_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     e_effective_cubage_calculated_check=10*NEW.b_boiler_rated_coal_capacity_check/NEW.e_coal_bunker_counts_check/NEW.c_coal_bulk_density_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_backstep_consumption_hours:反推消耗小时,的计算10-----------------------------------
  IF OLD.c_coal_bulk_density_check != NEW.c_coal_bulk_density_check OR OLD.e_coal_bunker_counts_check != NEW.e_coal_bunker_counts_check OR OLD.e_effective_cubage_selected_check != NEW.e_effective_cubage_selected_check OR OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check THEN
     update coalchp_coal_handingsystem set 

     e_backstep_consumption_hours_check=NEW.e_effective_cubage_selected_check*NEW.c_coal_bulk_density_check*NEW.e_coal_bunker_counts_check/NEW.b_boiler_rated_coal_capacity_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_effective_cubage_selected_check ISNULL OR OLD.e_coal_bunker_counts_check ISNULL OR OLD.c_coal_bulk_density_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.e_effective_cubage_selected_check NOTNULL AND NEW.e_coal_bunker_counts_check NOTNULL AND NEW.c_coal_bulk_density_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     e_backstep_consumption_hours_check=NEW.e_effective_cubage_selected_check*NEW.c_coal_bulk_density_check*NEW.e_coal_bunker_counts_check/NEW.b_boiler_rated_coal_capacity_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段t_transportsystem_amount:运煤系统运输量,的计算11-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check OR OLD.t_transport_unbalanced_coefficient_check != NEW.t_transport_unbalanced_coefficient_check OR OLD.t_transportsystem_effective_working_hours_check != NEW.t_transportsystem_effective_working_hours_check THEN
     update coalchp_coal_handingsystem set 

     t_transportsystem_amount_check=22*NEW.b_boiler_rated_coal_capacity_check*NEW.t_transport_unbalanced_coefficient_check/NEW.t_transportsystem_effective_working_hours_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.t_transportsystem_effective_working_hours_check ISNULL OR OLD.t_transport_unbalanced_coefficient_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.t_transportsystem_effective_working_hours_check NOTNULL AND NEW.t_transport_unbalanced_coefficient_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     t_transportsystem_amount_check=22*NEW.b_boiler_rated_coal_capacity_check*NEW.t_transport_unbalanced_coefficient_check/NEW.t_transportsystem_effective_working_hours_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段t_daily_received_coal_amount:日计算受煤量,的计算12-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check OR OLD.t_transport_unbalanced_coefficient_check != NEW.t_transport_unbalanced_coefficient_check THEN
     update coalchp_coal_handingsystem set 

     t_daily_received_coal_amount_check=NEW.b_boiler_rated_coal_capacity_check*NEW.t_transport_unbalanced_coefficient_check*2*22
     where plan_id=NEW.plan_id;

  ELSIF (OLD.t_transport_unbalanced_coefficient_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.t_transport_unbalanced_coefficient_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     t_daily_received_coal_amount_check=NEW.b_boiler_rated_coal_capacity_check*NEW.t_transport_unbalanced_coefficient_check*2*22
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段t_vehicle_daily_incoming_times:每天进厂车次,的计算13-----------------------------------
  IF OLD.t_vehicle_capacity_tonnage_check != NEW.t_vehicle_capacity_tonnage_check OR OLD.t_daily_received_coal_amount_check != NEW.t_daily_received_coal_amount_check THEN
     update coalchp_coal_handingsystem set 

     t_vehicle_daily_incoming_times_check=NEW.t_daily_received_coal_amount_check/NEW.t_vehicle_capacity_tonnage_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.t_daily_received_coal_amount_check ISNULL OR OLD.t_vehicle_capacity_tonnage_check ISNULL) AND NEW.t_daily_received_coal_amount_check NOTNULL AND NEW.t_vehicle_capacity_tonnage_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     t_vehicle_daily_incoming_times_check=NEW.t_daily_received_coal_amount_check/NEW.t_vehicle_capacity_tonnage_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段t_vehicle_perhour_incoming_times:每小时进场车次,的计算14-----------------------------------
  IF OLD.t_daily_working_hours_check != NEW.t_daily_working_hours_check OR OLD.t_vehicle_daily_incoming_times_check != NEW.t_vehicle_daily_incoming_times_check THEN
     update coalchp_coal_handingsystem set 

     t_vehicle_perhour_incoming_times_check=NEW.t_vehicle_daily_incoming_times_check/NEW.t_daily_working_hours_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.t_vehicle_daily_incoming_times_check ISNULL OR OLD.t_daily_working_hours_check ISNULL) AND NEW.t_vehicle_daily_incoming_times_check NOTNULL AND NEW.t_daily_working_hours_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     t_vehicle_perhour_incoming_times_check=NEW.t_vehicle_daily_incoming_times_check/NEW.t_daily_working_hours_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_mutil_boiler_rated_coal_capacity:多锅炉额定耗煤量,的计算15-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check THEN
     update coalchp_coal_handingsystem set 

     s_mutil_boiler_rated_coal_capacity_check=1*NEW.b_boiler_rated_coal_capacity_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_mutil_boiler_rated_coal_capacity_check=1*NEW.b_boiler_rated_coal_capacity_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_mutil_boiler_rated_coal_amount:多锅炉日额定耗煤总量,的计算16-----------------------------------
  IF OLD.s_mutil_boiler_rated_coal_capacity_check != NEW.s_mutil_boiler_rated_coal_capacity_check THEN
     update coalchp_coal_handingsystem set 

     s_mutil_boiler_rated_coal_amount_check=NEW.s_mutil_boiler_rated_coal_capacity_check*22
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_mutil_boiler_rated_coal_capacity_check ISNULL) AND NEW.s_mutil_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_mutil_boiler_rated_coal_amount_check=NEW.s_mutil_boiler_rated_coal_capacity_check*22
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_transportsystem_working_hours:输煤系统运行小时,的计算17-----------------------------------
  IF OLD.s_mutil_boiler_rated_coal_amount_check != NEW.s_mutil_boiler_rated_coal_amount_check OR OLD.s_transportsystem_output_check != NEW.s_transportsystem_output_check THEN
     update coalchp_coal_handingsystem set 

     s_transportsystem_working_hours_check=NEW.s_mutil_boiler_rated_coal_amount_check*1.5/NEW.s_transportsystem_output_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_transportsystem_output_check ISNULL OR OLD.s_mutil_boiler_rated_coal_amount_check ISNULL) AND NEW.s_transportsystem_output_check NOTNULL AND NEW.s_mutil_boiler_rated_coal_amount_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_transportsystem_working_hours_check=NEW.s_mutil_boiler_rated_coal_amount_check*1.5/NEW.s_transportsystem_output_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_shift_working_hours:每班运行小时,的计算18-----------------------------------
  IF OLD.s_mutil_boiler_rated_coal_amount_check != NEW.s_mutil_boiler_rated_coal_amount_check OR OLD.s_transportsystem_output_check != NEW.s_transportsystem_output_check THEN
     update coalchp_coal_handingsystem set 

     s_shift_working_hours_check=NEW.s_mutil_boiler_rated_coal_amount_check/3/NEW.s_transportsystem_output_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_transportsystem_output_check ISNULL OR OLD.s_mutil_boiler_rated_coal_amount_check ISNULL) AND NEW.s_transportsystem_output_check NOTNULL AND NEW.s_mutil_boiler_rated_coal_amount_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_shift_working_hours_check=NEW.s_mutil_boiler_rated_coal_amount_check/3/NEW.s_transportsystem_output_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_belt_max_transport_capacity:皮带最大输送能力,的计算19-----------------------------------
  IF OLD.s_belt_width_check != NEW.s_belt_width_check OR OLD.s_section_coefficient_check != NEW.s_section_coefficient_check OR OLD.s_belt_speed_check != NEW.s_belt_speed_check OR OLD.s_material_bulk_density_check != NEW.s_material_bulk_density_check THEN
     update coalchp_coal_handingsystem set 

     s_belt_max_transport_capacity_check=NEW.s_section_coefficient_check*NEW.s_belt_width_check*NEW.s_belt_width_check*NEW.s_belt_speed_check*NEW.s_material_bulk_density_check/1000/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_material_bulk_density_check ISNULL OR OLD.s_belt_speed_check ISNULL OR OLD.s_section_coefficient_check ISNULL OR OLD.s_belt_width_check ISNULL) AND NEW.s_material_bulk_density_check NOTNULL AND NEW.s_belt_speed_check NOTNULL AND NEW.s_section_coefficient_check NOTNULL AND NEW.s_belt_width_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_belt_max_transport_capacity_check=NEW.s_section_coefficient_check*NEW.s_belt_width_check*NEW.s_belt_width_check*NEW.s_belt_speed_check*NEW.s_material_bulk_density_check/1000/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_single_coal_feeder_output:单台给煤机出力,的计算20-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_check != NEW.b_boiler_rated_coal_capacity_check OR OLD.g_equipment_sets_check != NEW.g_equipment_sets_check OR OLD.g_surplus_check != NEW.g_surplus_check THEN
     update coalchp_coal_handingsystem set 

     g_single_coal_feeder_output_check=NEW.b_boiler_rated_coal_capacity_check/NEW.g_equipment_sets_check*NEW.g_surplus_check/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_surplus_check ISNULL OR OLD.g_equipment_sets_check ISNULL OR OLD.b_boiler_rated_coal_capacity_check ISNULL) AND NEW.g_surplus_check NOTNULL AND NEW.g_equipment_sets_check NOTNULL AND NEW.b_boiler_rated_coal_capacity_check NOTNULL THEN
     update coalchp_coal_handingsystem set 

     g_single_coal_feeder_output_check=NEW.b_boiler_rated_coal_capacity_check/NEW.g_equipment_sets_check*NEW.g_surplus_check/100
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_coal_handingsystem_check" AFTER UPDATE OF
"c_boiler_daily_working_hours_check",
"c_coal_store_days_check",
"c_coal_channel_occupy_coefficient_check",
"c_coal_shape_coefficient_check",
"c_coal_height_check",
"c_coal_bulk_density_check",
"c_coalyard_area_check",
"c_height_check",
"e_coal_bunker_counts_check",
"e_effective_cubage_selected_check",
"b_boiler_rated_coal_capacity_check",
"t_transport_unbalanced_coefficient_check",
"t_transportsystem_effective_working_hours_check",
"t_vehicle_capacity_tonnage_check",
"t_daily_working_hours_check",
"t_daily_received_coal_amount_check",
"b_boiler_daily_utilization_hours_check",
"t_vehicle_daily_incoming_times_check",
"s_mutil_boiler_rated_coal_capacity_check",
"s_mutil_boiler_rated_coal_amount_check",
"b_coal_daily_consumption_check",
"s_transportsystem_output_check",
"s_belt_width_check",
"s_section_coefficient_check",
"s_belt_speed_check",
"s_material_bulk_density_check",
"b_boiler_annual_utilization_hours_check",
"g_equipment_sets_check",
"g_surplus_check",
"b_coal_annual_consumption_check",
"b_daily_coal_unbalanced_coefficient_check"
ON "public"."coalchp_coal_handingsystem"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_coal_handingsystem_check"();
CREATE OR REPLACE FUNCTION coalchp_coal_handingsystem_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段b_coal_daily_consumption:日耗煤量,的计算1-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design OR OLD.b_boiler_daily_utilization_hours_design != NEW.b_boiler_daily_utilization_hours_design THEN
     update coalchp_coal_handingsystem set 

     b_coal_daily_consumption_design=NEW.b_boiler_rated_coal_capacity_design*NEW.b_boiler_daily_utilization_hours_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_boiler_daily_utilization_hours_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.b_boiler_daily_utilization_hours_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     b_coal_daily_consumption_design=NEW.b_boiler_rated_coal_capacity_design*NEW.b_boiler_daily_utilization_hours_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段b_coal_annual_consumption:年耗煤量,的计算2-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design OR OLD.b_boiler_annual_utilization_hours_design != NEW.b_boiler_annual_utilization_hours_design THEN
     update coalchp_coal_handingsystem set 

     b_coal_annual_consumption_design=NEW.b_boiler_annual_utilization_hours_design*NEW.b_boiler_rated_coal_capacity_design/10000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_boiler_annual_utilization_hours_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.b_boiler_annual_utilization_hours_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     b_coal_annual_consumption_design=NEW.b_boiler_annual_utilization_hours_design*NEW.b_boiler_rated_coal_capacity_design/10000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段b_daily_rail_coal_amount:铁路来煤日计算煤量,的计算3-----------------------------------
  IF OLD.b_coal_daily_consumption_design != NEW.b_coal_daily_consumption_design OR OLD.b_daily_coal_unbalanced_coefficient_design != NEW.b_daily_coal_unbalanced_coefficient_design THEN
     update coalchp_coal_handingsystem set 

     b_daily_rail_coal_amount_design=NEW.b_daily_coal_unbalanced_coefficient_design*NEW.b_coal_daily_consumption_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_daily_coal_unbalanced_coefficient_design ISNULL OR OLD.b_coal_daily_consumption_design ISNULL) AND NEW.b_daily_coal_unbalanced_coefficient_design NOTNULL AND NEW.b_coal_daily_consumption_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     b_daily_rail_coal_amount_design=NEW.b_daily_coal_unbalanced_coefficient_design*NEW.b_coal_daily_consumption_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段b_daily_vehicle_coal_amount:汽车来煤日计算煤量,的计算4-----------------------------------
  IF OLD.b_boiler_daily_utilization_hours_design != NEW.b_boiler_daily_utilization_hours_design OR OLD.b_boiler_annual_utilization_hours_design != NEW.b_boiler_annual_utilization_hours_design OR OLD.b_coal_annual_consumption_design != NEW.b_coal_annual_consumption_design OR OLD.b_daily_coal_unbalanced_coefficient_design != NEW.b_daily_coal_unbalanced_coefficient_design THEN
     update coalchp_coal_handingsystem set 

     b_daily_vehicle_coal_amount_design=NEW.b_daily_coal_unbalanced_coefficient_design*NEW.b_coal_annual_consumption_design*10000*NEW.b_boiler_daily_utilization_hours_design/NEW.b_boiler_annual_utilization_hours_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_daily_coal_unbalanced_coefficient_design ISNULL OR OLD.b_coal_annual_consumption_design ISNULL OR OLD.b_boiler_annual_utilization_hours_design ISNULL OR OLD.b_boiler_daily_utilization_hours_design ISNULL) AND NEW.b_daily_coal_unbalanced_coefficient_design NOTNULL AND NEW.b_coal_annual_consumption_design NOTNULL AND NEW.b_boiler_annual_utilization_hours_design NOTNULL AND NEW.b_boiler_daily_utilization_hours_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     b_daily_vehicle_coal_amount_design=NEW.b_daily_coal_unbalanced_coefficient_design*NEW.b_coal_annual_consumption_design*10000*NEW.b_boiler_daily_utilization_hours_design/NEW.b_boiler_annual_utilization_hours_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_boiler_hour_coal_capacity:锅炉每小时最大耗煤量,的计算5-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design THEN
     update coalchp_coal_handingsystem set 

     c_boiler_hour_coal_capacity_design=NEW.b_boiler_rated_coal_capacity_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     c_boiler_hour_coal_capacity_design=NEW.b_boiler_rated_coal_capacity_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_coalyard_store_amount:煤场存储量,的计算6-----------------------------------
  IF OLD.c_boiler_daily_working_hours_design != NEW.c_boiler_daily_working_hours_design OR OLD.c_coal_store_days_design != NEW.c_coal_store_days_design OR OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design THEN
     update coalchp_coal_handingsystem set 

     c_coalyard_store_amount_design=NEW.b_boiler_rated_coal_capacity_design*NEW.c_boiler_daily_working_hours_design*NEW.c_coal_store_days_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_coal_store_days_design ISNULL OR OLD.c_boiler_daily_working_hours_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.c_coal_store_days_design NOTNULL AND NEW.c_boiler_daily_working_hours_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     c_coalyard_store_amount_design=NEW.b_boiler_rated_coal_capacity_design*NEW.c_boiler_daily_working_hours_design*NEW.c_coal_store_days_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_coalyard_area:煤场面积,的计算7-----------------------------------
  IF OLD.c_boiler_daily_working_hours_design != NEW.c_boiler_daily_working_hours_design OR OLD.c_coal_store_days_design != NEW.c_coal_store_days_design OR OLD.c_coal_channel_occupy_coefficient_design != NEW.c_coal_channel_occupy_coefficient_design OR OLD.c_coal_shape_coefficient_design != NEW.c_coal_shape_coefficient_design OR OLD.c_coal_height_design != NEW.c_coal_height_design OR OLD.c_coal_bulk_density_design != NEW.c_coal_bulk_density_design OR OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design THEN
     update coalchp_coal_handingsystem set 

     c_coalyard_area_design=NEW.b_boiler_rated_coal_capacity_design*NEW.c_boiler_daily_working_hours_design*NEW.c_coal_channel_occupy_coefficient_design*NEW.c_coal_store_days_design/NEW.c_coal_shape_coefficient_design/NEW.c_coal_height_design/NEW.c_coal_bulk_density_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_coal_bulk_density_design ISNULL OR OLD.c_coal_height_design ISNULL OR OLD.c_coal_shape_coefficient_design ISNULL OR OLD.c_coal_channel_occupy_coefficient_design ISNULL OR OLD.c_coal_store_days_design ISNULL OR OLD.c_boiler_daily_working_hours_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.c_coal_bulk_density_design NOTNULL AND NEW.c_coal_height_design NOTNULL AND NEW.c_coal_shape_coefficient_design NOTNULL AND NEW.c_coal_channel_occupy_coefficient_design NOTNULL AND NEW.c_coal_store_days_design NOTNULL AND NEW.c_boiler_daily_working_hours_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     c_coalyard_area_design=NEW.b_boiler_rated_coal_capacity_design*NEW.c_boiler_daily_working_hours_design*NEW.c_coal_channel_occupy_coefficient_design*NEW.c_coal_store_days_design/NEW.c_coal_shape_coefficient_design/NEW.c_coal_height_design/NEW.c_coal_bulk_density_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_width:宽,的计算8-----------------------------------
  IF OLD.c_coalyard_area_design != NEW.c_coalyard_area_design OR OLD.c_height_design != NEW.c_height_design THEN
     update coalchp_coal_handingsystem set 

     c_width_design=NEW.c_coalyard_area_design/NEW.c_height_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_height_design ISNULL OR OLD.c_coalyard_area_design ISNULL) AND NEW.c_height_design NOTNULL AND NEW.c_coalyard_area_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     c_width_design=NEW.c_coalyard_area_design/NEW.c_height_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_effective_cubage_calculated:有效容积-计算,的计算9-----------------------------------
  IF OLD.c_coal_bulk_density_design != NEW.c_coal_bulk_density_design OR OLD.e_coal_bunker_counts_design != NEW.e_coal_bunker_counts_design OR OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design THEN
     update coalchp_coal_handingsystem set 

     e_effective_cubage_calculated_design=10*NEW.b_boiler_rated_coal_capacity_design/NEW.e_coal_bunker_counts_design/NEW.c_coal_bulk_density_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_coal_bunker_counts_design ISNULL OR OLD.c_coal_bulk_density_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.e_coal_bunker_counts_design NOTNULL AND NEW.c_coal_bulk_density_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     e_effective_cubage_calculated_design=10*NEW.b_boiler_rated_coal_capacity_design/NEW.e_coal_bunker_counts_design/NEW.c_coal_bulk_density_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_backstep_consumption_hours:反推消耗小时,的计算10-----------------------------------
  IF OLD.c_coal_bulk_density_design != NEW.c_coal_bulk_density_design OR OLD.e_coal_bunker_counts_design != NEW.e_coal_bunker_counts_design OR OLD.e_effective_cubage_selected_design != NEW.e_effective_cubage_selected_design OR OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design THEN
     update coalchp_coal_handingsystem set 

     e_backstep_consumption_hours_design=NEW.e_effective_cubage_selected_design*NEW.c_coal_bulk_density_design*NEW.e_coal_bunker_counts_design/NEW.b_boiler_rated_coal_capacity_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.e_effective_cubage_selected_design ISNULL OR OLD.e_coal_bunker_counts_design ISNULL OR OLD.c_coal_bulk_density_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.e_effective_cubage_selected_design NOTNULL AND NEW.e_coal_bunker_counts_design NOTNULL AND NEW.c_coal_bulk_density_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     e_backstep_consumption_hours_design=NEW.e_effective_cubage_selected_design*NEW.c_coal_bulk_density_design*NEW.e_coal_bunker_counts_design/NEW.b_boiler_rated_coal_capacity_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段t_transportsystem_amount:运煤系统运输量,的计算11-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design OR OLD.t_transport_unbalanced_coefficient_design != NEW.t_transport_unbalanced_coefficient_design OR OLD.t_transportsystem_effective_working_hours_design != NEW.t_transportsystem_effective_working_hours_design THEN
     update coalchp_coal_handingsystem set 

     t_transportsystem_amount_design=22*NEW.b_boiler_rated_coal_capacity_design*NEW.t_transport_unbalanced_coefficient_design/NEW.t_transportsystem_effective_working_hours_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.t_transportsystem_effective_working_hours_design ISNULL OR OLD.t_transport_unbalanced_coefficient_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.t_transportsystem_effective_working_hours_design NOTNULL AND NEW.t_transport_unbalanced_coefficient_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     t_transportsystem_amount_design=22*NEW.b_boiler_rated_coal_capacity_design*NEW.t_transport_unbalanced_coefficient_design/NEW.t_transportsystem_effective_working_hours_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段t_daily_received_coal_amount:日计算受煤量,的计算12-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design OR OLD.t_transport_unbalanced_coefficient_design != NEW.t_transport_unbalanced_coefficient_design THEN
     update coalchp_coal_handingsystem set 

     t_daily_received_coal_amount_design=NEW.b_boiler_rated_coal_capacity_design*NEW.t_transport_unbalanced_coefficient_design*2*22
     where plan_id=NEW.plan_id;

  ELSIF (OLD.t_transport_unbalanced_coefficient_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.t_transport_unbalanced_coefficient_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     t_daily_received_coal_amount_design=NEW.b_boiler_rated_coal_capacity_design*NEW.t_transport_unbalanced_coefficient_design*2*22
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段t_vehicle_daily_incoming_times:每天进厂车次,的计算13-----------------------------------
  IF OLD.t_vehicle_capacity_tonnage_design != NEW.t_vehicle_capacity_tonnage_design OR OLD.t_daily_received_coal_amount_design != NEW.t_daily_received_coal_amount_design THEN
     update coalchp_coal_handingsystem set 

     t_vehicle_daily_incoming_times_design=NEW.t_daily_received_coal_amount_design/NEW.t_vehicle_capacity_tonnage_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.t_daily_received_coal_amount_design ISNULL OR OLD.t_vehicle_capacity_tonnage_design ISNULL) AND NEW.t_daily_received_coal_amount_design NOTNULL AND NEW.t_vehicle_capacity_tonnage_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     t_vehicle_daily_incoming_times_design=NEW.t_daily_received_coal_amount_design/NEW.t_vehicle_capacity_tonnage_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段t_vehicle_perhour_incoming_times:每小时进场车次,的计算14-----------------------------------
  IF OLD.t_daily_working_hours_design != NEW.t_daily_working_hours_design OR OLD.t_vehicle_daily_incoming_times_design != NEW.t_vehicle_daily_incoming_times_design THEN
     update coalchp_coal_handingsystem set 

     t_vehicle_perhour_incoming_times_design=NEW.t_vehicle_daily_incoming_times_design/NEW.t_daily_working_hours_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.t_vehicle_daily_incoming_times_design ISNULL OR OLD.t_daily_working_hours_design ISNULL) AND NEW.t_vehicle_daily_incoming_times_design NOTNULL AND NEW.t_daily_working_hours_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     t_vehicle_perhour_incoming_times_design=NEW.t_vehicle_daily_incoming_times_design/NEW.t_daily_working_hours_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_mutil_boiler_rated_coal_capacity:多锅炉额定耗煤量,的计算15-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design THEN
     update coalchp_coal_handingsystem set 

     s_mutil_boiler_rated_coal_capacity_design=1*NEW.b_boiler_rated_coal_capacity_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_mutil_boiler_rated_coal_capacity_design=1*NEW.b_boiler_rated_coal_capacity_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_mutil_boiler_rated_coal_amount:多锅炉日额定耗煤总量,的计算16-----------------------------------
  IF OLD.s_mutil_boiler_rated_coal_capacity_design != NEW.s_mutil_boiler_rated_coal_capacity_design THEN
     update coalchp_coal_handingsystem set 

     s_mutil_boiler_rated_coal_amount_design=NEW.s_mutil_boiler_rated_coal_capacity_design*22
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_mutil_boiler_rated_coal_capacity_design ISNULL) AND NEW.s_mutil_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_mutil_boiler_rated_coal_amount_design=NEW.s_mutil_boiler_rated_coal_capacity_design*22
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_transportsystem_working_hours:输煤系统运行小时,的计算17-----------------------------------
  IF OLD.s_mutil_boiler_rated_coal_amount_design != NEW.s_mutil_boiler_rated_coal_amount_design OR OLD.s_transportsystem_output_design != NEW.s_transportsystem_output_design THEN
     update coalchp_coal_handingsystem set 

     s_transportsystem_working_hours_design=NEW.s_mutil_boiler_rated_coal_amount_design*1.5/NEW.s_transportsystem_output_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_transportsystem_output_design ISNULL OR OLD.s_mutil_boiler_rated_coal_amount_design ISNULL) AND NEW.s_transportsystem_output_design NOTNULL AND NEW.s_mutil_boiler_rated_coal_amount_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_transportsystem_working_hours_design=NEW.s_mutil_boiler_rated_coal_amount_design*1.5/NEW.s_transportsystem_output_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_shift_working_hours:每班运行小时,的计算18-----------------------------------
  IF OLD.s_mutil_boiler_rated_coal_amount_design != NEW.s_mutil_boiler_rated_coal_amount_design OR OLD.s_transportsystem_output_design != NEW.s_transportsystem_output_design THEN
     update coalchp_coal_handingsystem set 

     s_shift_working_hours_design=NEW.s_mutil_boiler_rated_coal_amount_design/3/NEW.s_transportsystem_output_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_transportsystem_output_design ISNULL OR OLD.s_mutil_boiler_rated_coal_amount_design ISNULL) AND NEW.s_transportsystem_output_design NOTNULL AND NEW.s_mutil_boiler_rated_coal_amount_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_shift_working_hours_design=NEW.s_mutil_boiler_rated_coal_amount_design/3/NEW.s_transportsystem_output_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_belt_max_transport_capacity:皮带最大输送能力,的计算19-----------------------------------
  IF OLD.s_belt_width_design != NEW.s_belt_width_design OR OLD.s_section_coefficient_design != NEW.s_section_coefficient_design OR OLD.s_belt_speed_design != NEW.s_belt_speed_design OR OLD.s_material_bulk_density_design != NEW.s_material_bulk_density_design THEN
     update coalchp_coal_handingsystem set 

     s_belt_max_transport_capacity_design=NEW.s_section_coefficient_design*NEW.s_belt_width_design*NEW.s_belt_width_design*NEW.s_belt_speed_design*NEW.s_material_bulk_density_design/1000/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_material_bulk_density_design ISNULL OR OLD.s_belt_speed_design ISNULL OR OLD.s_section_coefficient_design ISNULL OR OLD.s_belt_width_design ISNULL) AND NEW.s_material_bulk_density_design NOTNULL AND NEW.s_belt_speed_design NOTNULL AND NEW.s_section_coefficient_design NOTNULL AND NEW.s_belt_width_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     s_belt_max_transport_capacity_design=NEW.s_section_coefficient_design*NEW.s_belt_width_design*NEW.s_belt_width_design*NEW.s_belt_speed_design*NEW.s_material_bulk_density_design/1000/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_single_coal_feeder_output:单台给煤机出力,的计算20-----------------------------------
  IF OLD.b_boiler_rated_coal_capacity_design != NEW.b_boiler_rated_coal_capacity_design OR OLD.g_equipment_sets_design != NEW.g_equipment_sets_design OR OLD.g_surplus_design != NEW.g_surplus_design THEN
     update coalchp_coal_handingsystem set 

     g_single_coal_feeder_output_design=NEW.b_boiler_rated_coal_capacity_design/NEW.g_equipment_sets_design*NEW.g_surplus_design/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_surplus_design ISNULL OR OLD.g_equipment_sets_design ISNULL OR OLD.b_boiler_rated_coal_capacity_design ISNULL) AND NEW.g_surplus_design NOTNULL AND NEW.g_equipment_sets_design NOTNULL AND NEW.b_boiler_rated_coal_capacity_design NOTNULL THEN
     update coalchp_coal_handingsystem set 

     g_single_coal_feeder_output_design=NEW.b_boiler_rated_coal_capacity_design/NEW.g_equipment_sets_design*NEW.g_surplus_design/100
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_coal_handingsystem_design" AFTER UPDATE OF
"c_boiler_daily_working_hours_design",
"c_coal_store_days_design",
"c_coal_channel_occupy_coefficient_design",
"c_coal_shape_coefficient_design",
"c_coal_height_design",
"c_coal_bulk_density_design",
"c_coalyard_area_design",
"c_height_design",
"e_coal_bunker_counts_design",
"e_effective_cubage_selected_design",
"b_boiler_rated_coal_capacity_design",
"t_transport_unbalanced_coefficient_design",
"t_transportsystem_effective_working_hours_design",
"t_vehicle_capacity_tonnage_design",
"t_daily_working_hours_design",
"t_daily_received_coal_amount_design",
"b_boiler_daily_utilization_hours_design",
"t_vehicle_daily_incoming_times_design",
"s_mutil_boiler_rated_coal_capacity_design",
"s_mutil_boiler_rated_coal_amount_design",
"b_coal_daily_consumption_design",
"s_transportsystem_output_design",
"s_belt_width_design",
"s_section_coefficient_design",
"s_belt_speed_design",
"s_material_bulk_density_design",
"b_boiler_annual_utilization_hours_design",
"g_equipment_sets_design",
"g_surplus_design",
"b_coal_annual_consumption_design",
"b_daily_coal_unbalanced_coefficient_design"
ON "public"."coalchp_coal_handingsystem"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_coal_handingsystem_design"();
