CREATE OR REPLACE FUNCTION gaspowergeneration_steam_water_pipe()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段main_steam_nominal_pressure_c:公称压力,的计算1-----------------------------------
  IF OLD.main_steam_design_pressure_c != NEW.main_steam_design_pressure_c OR OLD.main_steam_temperature_stress_c != NEW.main_steam_temperature_stress_c OR OLD.main_steam_20c_stress_c != NEW.main_steam_20c_stress_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_nominal_pressure_c=(NEW.main_steam_design_pressure_c)*(NEW.main_steam_20c_stress_c)/(NEW.main_steam_temperature_stress_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_20c_stress_c ISNULL OR OLD.main_steam_temperature_stress_c ISNULL OR OLD.main_steam_design_pressure_c ISNULL) AND NEW.main_steam_20c_stress_c NOTNULL AND NEW.main_steam_temperature_stress_c NOTNULL AND NEW.main_steam_design_pressure_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_nominal_pressure_c=(NEW.main_steam_design_pressure_c)*(NEW.main_steam_20c_stress_c)/(NEW.main_steam_temperature_stress_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_inner_diamete_c:管子内径,的计算2-----------------------------------
  IF OLD.main_steam_selected_velocity_c != NEW.main_steam_selected_velocity_c OR OLD.main_steam_meida_specific_volume_c != NEW.main_steam_meida_specific_volume_c OR OLD.main_steam_pipe_mass_flow_c != NEW.main_steam_pipe_mass_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_inner_diamete_c=594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_meida_specific_volume_c ISNULL OR OLD.main_steam_selected_velocity_c ISNULL OR OLD.main_steam_pipe_mass_flow_c ISNULL) AND NEW.main_steam_meida_specific_volume_c NOTNULL AND NEW.main_steam_selected_velocity_c NOTNULL AND NEW.main_steam_pipe_mass_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_inner_diamete_c=594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_pipe_min_thickness_c:直管最小壁厚,的计算3-----------------------------------
  IF OLD.main_steam_selected_velocity_c != NEW.main_steam_selected_velocity_c OR OLD.main_steam_meida_specific_volume_c != NEW.main_steam_meida_specific_volume_c OR OLD.main_steam_temperature_correct_coefficient_c != NEW.main_steam_temperature_correct_coefficient_c OR OLD.main_steam_stress_correct_coefficient_c != NEW.main_steam_stress_correct_coefficient_c OR OLD.main_steam_additional_thickness_c != NEW.main_steam_additional_thickness_c OR OLD.main_steam_design_pressure_c != NEW.main_steam_design_pressure_c OR OLD.main_steam_temperature_stress_c != NEW.main_steam_temperature_stress_c OR OLD.main_steam_pipe_mass_flow_c != NEW.main_steam_pipe_mass_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_pipe_min_thickness_c=((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_additional_thickness_c ISNULL OR OLD.main_steam_stress_correct_coefficient_c ISNULL OR OLD.main_steam_temperature_correct_coefficient_c ISNULL OR OLD.main_steam_meida_specific_volume_c ISNULL OR OLD.main_steam_selected_velocity_c ISNULL OR OLD.main_steam_pipe_mass_flow_c ISNULL OR OLD.main_steam_temperature_stress_c ISNULL OR OLD.main_steam_design_pressure_c ISNULL) AND NEW.main_steam_additional_thickness_c NOTNULL AND NEW.main_steam_stress_correct_coefficient_c NOTNULL AND NEW.main_steam_temperature_correct_coefficient_c NOTNULL AND NEW.main_steam_meida_specific_volume_c NOTNULL AND NEW.main_steam_selected_velocity_c NOTNULL AND NEW.main_steam_pipe_mass_flow_c NOTNULL AND NEW.main_steam_temperature_stress_c NOTNULL AND NEW.main_steam_design_pressure_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_pipe_min_thickness_c=((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_negative_deviation_added_value_c:壁厚负偏差附加值,的计算4-----------------------------------
  IF OLD.main_steam_selected_velocity_c != NEW.main_steam_selected_velocity_c OR OLD.main_steam_meida_specific_volume_c != NEW.main_steam_meida_specific_volume_c OR OLD.main_steam_temperature_correct_coefficient_c != NEW.main_steam_temperature_correct_coefficient_c OR OLD.main_steam_stress_correct_coefficient_c != NEW.main_steam_stress_correct_coefficient_c OR OLD.main_steam_additional_thickness_c != NEW.main_steam_additional_thickness_c OR OLD.main_steam_negative_deviation_coefficient_c != NEW.main_steam_negative_deviation_coefficient_c OR OLD.main_steam_design_pressure_c != NEW.main_steam_design_pressure_c OR OLD.main_steam_temperature_stress_c != NEW.main_steam_temperature_stress_c OR OLD.main_steam_pipe_mass_flow_c != NEW.main_steam_pipe_mass_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_negative_deviation_added_value_c=(((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))*(NEW.main_steam_negative_deviation_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_negative_deviation_coefficient_c ISNULL OR OLD.main_steam_additional_thickness_c ISNULL OR OLD.main_steam_stress_correct_coefficient_c ISNULL OR OLD.main_steam_temperature_correct_coefficient_c ISNULL OR OLD.main_steam_meida_specific_volume_c ISNULL OR OLD.main_steam_selected_velocity_c ISNULL OR OLD.main_steam_pipe_mass_flow_c ISNULL OR OLD.main_steam_temperature_stress_c ISNULL OR OLD.main_steam_design_pressure_c ISNULL) AND NEW.main_steam_negative_deviation_coefficient_c NOTNULL AND NEW.main_steam_additional_thickness_c NOTNULL AND NEW.main_steam_stress_correct_coefficient_c NOTNULL AND NEW.main_steam_temperature_correct_coefficient_c NOTNULL AND NEW.main_steam_meida_specific_volume_c NOTNULL AND NEW.main_steam_selected_velocity_c NOTNULL AND NEW.main_steam_pipe_mass_flow_c NOTNULL AND NEW.main_steam_temperature_stress_c NOTNULL AND NEW.main_steam_design_pressure_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_negative_deviation_added_value_c=(((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))*(NEW.main_steam_negative_deviation_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_calculate_thickness_c:计算壁厚,的计算5-----------------------------------
  IF OLD.main_steam_selected_velocity_c != NEW.main_steam_selected_velocity_c OR OLD.main_steam_meida_specific_volume_c != NEW.main_steam_meida_specific_volume_c OR OLD.main_steam_temperature_correct_coefficient_c != NEW.main_steam_temperature_correct_coefficient_c OR OLD.main_steam_stress_correct_coefficient_c != NEW.main_steam_stress_correct_coefficient_c OR OLD.main_steam_additional_thickness_c != NEW.main_steam_additional_thickness_c OR OLD.main_steam_negative_deviation_coefficient_c != NEW.main_steam_negative_deviation_coefficient_c OR OLD.main_steam_design_pressure_c != NEW.main_steam_design_pressure_c OR OLD.main_steam_temperature_stress_c != NEW.main_steam_temperature_stress_c OR OLD.main_steam_pipe_mass_flow_c != NEW.main_steam_pipe_mass_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_calculate_thickness_c=(((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))+((((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))*(NEW.main_steam_negative_deviation_coefficient_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_negative_deviation_coefficient_c ISNULL OR OLD.main_steam_additional_thickness_c ISNULL OR OLD.main_steam_stress_correct_coefficient_c ISNULL OR OLD.main_steam_temperature_correct_coefficient_c ISNULL OR OLD.main_steam_meida_specific_volume_c ISNULL OR OLD.main_steam_selected_velocity_c ISNULL OR OLD.main_steam_pipe_mass_flow_c ISNULL OR OLD.main_steam_temperature_stress_c ISNULL OR OLD.main_steam_design_pressure_c ISNULL) AND NEW.main_steam_negative_deviation_coefficient_c NOTNULL AND NEW.main_steam_additional_thickness_c NOTNULL AND NEW.main_steam_stress_correct_coefficient_c NOTNULL AND NEW.main_steam_temperature_correct_coefficient_c NOTNULL AND NEW.main_steam_meida_specific_volume_c NOTNULL AND NEW.main_steam_selected_velocity_c NOTNULL AND NEW.main_steam_pipe_mass_flow_c NOTNULL AND NEW.main_steam_temperature_stress_c NOTNULL AND NEW.main_steam_design_pressure_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_calculate_thickness_c=(((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))+((((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))*(NEW.main_steam_negative_deviation_coefficient_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_calculate_outer_diameter_c:计算外径,的计算6-----------------------------------
  IF OLD.main_steam_selected_velocity_c != NEW.main_steam_selected_velocity_c OR OLD.main_steam_meida_specific_volume_c != NEW.main_steam_meida_specific_volume_c OR OLD.main_steam_temperature_correct_coefficient_c != NEW.main_steam_temperature_correct_coefficient_c OR OLD.main_steam_stress_correct_coefficient_c != NEW.main_steam_stress_correct_coefficient_c OR OLD.main_steam_additional_thickness_c != NEW.main_steam_additional_thickness_c OR OLD.main_steam_negative_deviation_coefficient_c != NEW.main_steam_negative_deviation_coefficient_c OR OLD.main_steam_design_pressure_c != NEW.main_steam_design_pressure_c OR OLD.main_steam_temperature_stress_c != NEW.main_steam_temperature_stress_c OR OLD.main_steam_pipe_mass_flow_c != NEW.main_steam_pipe_mass_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_calculate_outer_diameter_c=((((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))+((((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))*(NEW.main_steam_negative_deviation_coefficient_c)))*2+(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_negative_deviation_coefficient_c ISNULL OR OLD.main_steam_additional_thickness_c ISNULL OR OLD.main_steam_stress_correct_coefficient_c ISNULL OR OLD.main_steam_temperature_correct_coefficient_c ISNULL OR OLD.main_steam_meida_specific_volume_c ISNULL OR OLD.main_steam_selected_velocity_c ISNULL OR OLD.main_steam_pipe_mass_flow_c ISNULL OR OLD.main_steam_temperature_stress_c ISNULL OR OLD.main_steam_design_pressure_c ISNULL) AND NEW.main_steam_negative_deviation_coefficient_c NOTNULL AND NEW.main_steam_additional_thickness_c NOTNULL AND NEW.main_steam_stress_correct_coefficient_c NOTNULL AND NEW.main_steam_temperature_correct_coefficient_c NOTNULL AND NEW.main_steam_meida_specific_volume_c NOTNULL AND NEW.main_steam_selected_velocity_c NOTNULL AND NEW.main_steam_pipe_mass_flow_c NOTNULL AND NEW.main_steam_temperature_stress_c NOTNULL AND NEW.main_steam_design_pressure_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_calculate_outer_diameter_c=((((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))+((((NEW.main_steam_design_pressure_c)*(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))+2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)*(NEW.main_steam_additional_thickness_c)+2*(NEW.main_steam_temperature_correct_coefficient_c)*(NEW.main_steam_design_pressure_c)*(NEW.main_steam_additional_thickness_c))/(2*(NEW.main_steam_temperature_stress_c)*(NEW.main_steam_stress_correct_coefficient_c)-2*(NEW.main_steam_design_pressure_c)*(1-(NEW.main_steam_temperature_correct_coefficient_c))))*(NEW.main_steam_negative_deviation_coefficient_c)))*2+(594.7*sqrt((NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(NEW.main_steam_selected_velocity_c)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_selected_inner_diameter_c:取值------内径,的计算7-----------------------------------
  IF OLD.main_steam_selected_outer_diameter_c != NEW.main_steam_selected_outer_diameter_c OR OLD.main_steam_selected_thickness_c != NEW.main_steam_selected_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_selected_inner_diameter_c=(NEW.main_steam_selected_outer_diameter_c)-2*(NEW.main_steam_selected_thickness_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_selected_thickness_c ISNULL OR OLD.main_steam_selected_outer_diameter_c ISNULL) AND NEW.main_steam_selected_thickness_c NOTNULL AND NEW.main_steam_selected_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_selected_inner_diameter_c=(NEW.main_steam_selected_outer_diameter_c)-2*(NEW.main_steam_selected_thickness_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_backstepping_velocity_c:反推流速,的计算8-----------------------------------
  IF OLD.main_steam_meida_specific_volume_c != NEW.main_steam_meida_specific_volume_c OR OLD.main_steam_selected_outer_diameter_c != NEW.main_steam_selected_outer_diameter_c OR OLD.main_steam_selected_thickness_c != NEW.main_steam_selected_thickness_c OR OLD.main_steam_pipe_mass_flow_c != NEW.main_steam_pipe_mass_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_backstepping_velocity_c=(NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(((NEW.main_steam_selected_outer_diameter_c)-2*(NEW.main_steam_selected_thickness_c))/594.7)^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_selected_thickness_c ISNULL OR OLD.main_steam_selected_outer_diameter_c ISNULL OR OLD.main_steam_meida_specific_volume_c ISNULL OR OLD.main_steam_pipe_mass_flow_c ISNULL) AND NEW.main_steam_selected_thickness_c NOTNULL AND NEW.main_steam_selected_outer_diameter_c NOTNULL AND NEW.main_steam_meida_specific_volume_c NOTNULL AND NEW.main_steam_pipe_mass_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_backstepping_velocity_c=(NEW.main_steam_pipe_mass_flow_c)*(NEW.main_steam_meida_specific_volume_c)/(((NEW.main_steam_selected_outer_diameter_c)-2*(NEW.main_steam_selected_thickness_c))/594.7)^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_calculate_velocity_c:计算流速--主蒸汽分管,的计算9-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_c != NEW.main_steam_msv_c OR OLD.main_steam_pipe_outer_diameter_c != NEW.main_steam_pipe_outer_diameter_c OR OLD.main_steam_pipe_thickness_c != NEW.main_steam_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_calculate_velocity_c=0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_thickness_c ISNULL OR OLD.main_steam_pipe_outer_diameter_c ISNULL OR OLD.main_steam_msv_c ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_pipe_thickness_c NOTNULL AND NEW.main_steam_pipe_outer_diameter_c NOTNULL AND NEW.main_steam_msv_c NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_calculate_velocity_c=0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_dynamic_head_c:动压头--主蒸汽分管,的计算10-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_c != NEW.main_steam_msv_c OR OLD.main_steam_pipe_outer_diameter_c != NEW.main_steam_pipe_outer_diameter_c OR OLD.main_steam_pipe_thickness_c != NEW.main_steam_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_dynamic_head_c=((0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2))^2/2/(NEW.main_steam_msv_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_thickness_c ISNULL OR OLD.main_steam_pipe_outer_diameter_c ISNULL OR OLD.main_steam_msv_c ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_pipe_thickness_c NOTNULL AND NEW.main_steam_pipe_outer_diameter_c NOTNULL AND NEW.main_steam_msv_c NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_dynamic_head_c=((0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2))^2/2/(NEW.main_steam_msv_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_pipe_inner_diameter_c:内径--主蒸汽分管,的计算11-----------------------------------
  IF OLD.main_steam_pipe_outer_diameter_c != NEW.main_steam_pipe_outer_diameter_c OR OLD.main_steam_pipe_thickness_c != NEW.main_steam_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_pipe_inner_diameter_c=(NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_thickness_c ISNULL OR OLD.main_steam_pipe_outer_diameter_c ISNULL) AND NEW.main_steam_pipe_thickness_c NOTNULL AND NEW.main_steam_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_pipe_inner_diameter_c=(NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_friction_resistance_c:摩擦阻力--主蒸汽分管,的计算12-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_c != NEW.main_steam_msv_c OR OLD.main_steam_pipe_outer_diameter_c != NEW.main_steam_pipe_outer_diameter_c OR OLD.main_steam_pipe_thickness_c != NEW.main_steam_pipe_thickness_c OR OLD.main_steam_resistance_coefficient_c != NEW.main_steam_resistance_coefficient_c OR OLD.main_steam_pipe_length_c != NEW.main_steam_pipe_length_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_friction_resistance_c=((NEW.main_steam_resistance_coefficient_c)*(((0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2))^2/2/(NEW.main_steam_msv_c))/((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))*(NEW.main_steam_pipe_length_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_length_c ISNULL OR OLD.main_steam_resistance_coefficient_c ISNULL OR OLD.main_steam_pipe_thickness_c ISNULL OR OLD.main_steam_pipe_outer_diameter_c ISNULL OR OLD.main_steam_msv_c ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_pipe_length_c NOTNULL AND NEW.main_steam_resistance_coefficient_c NOTNULL AND NEW.main_steam_pipe_thickness_c NOTNULL AND NEW.main_steam_pipe_outer_diameter_c NOTNULL AND NEW.main_steam_msv_c NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_friction_resistance_c=((NEW.main_steam_resistance_coefficient_c)*(((0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2))^2/2/(NEW.main_steam_msv_c))/((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))*(NEW.main_steam_pipe_length_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_reynolds_c:雷诺数--主蒸汽分管,的计算13-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_c != NEW.main_steam_msv_c OR OLD.main_steam_media_viscosity_c != NEW.main_steam_media_viscosity_c OR OLD.main_steam_pipe_outer_diameter_c != NEW.main_steam_pipe_outer_diameter_c OR OLD.main_steam_pipe_thickness_c != NEW.main_steam_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_reynolds_c=(0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2)*((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c))/(NEW.main_steam_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_thickness_c ISNULL OR OLD.main_steam_pipe_outer_diameter_c ISNULL OR OLD.main_steam_media_viscosity_c ISNULL OR OLD.main_steam_msv_c ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_pipe_thickness_c NOTNULL AND NEW.main_steam_pipe_outer_diameter_c NOTNULL AND NEW.main_steam_media_viscosity_c NOTNULL AND NEW.main_steam_msv_c NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_reynolds_c=(0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2)*((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c))/(NEW.main_steam_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_relative_roughness_c:相对粗糙度--主蒸汽分管,的计算14-----------------------------------
  IF OLD.main_steam_pipe_outer_diameter_c != NEW.main_steam_pipe_outer_diameter_c OR OLD.main_steam_pipe_thickness_c != NEW.main_steam_pipe_thickness_c OR OLD.main_steam_equivalent_roughness_c != NEW.main_steam_equivalent_roughness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_relative_roughness_c=(NEW.main_steam_equivalent_roughness_c)/((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_equivalent_roughness_c ISNULL OR OLD.main_steam_pipe_thickness_c ISNULL OR OLD.main_steam_pipe_outer_diameter_c ISNULL) AND NEW.main_steam_equivalent_roughness_c NOTNULL AND NEW.main_steam_pipe_thickness_c NOTNULL AND NEW.main_steam_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_relative_roughness_c=(NEW.main_steam_equivalent_roughness_c)/((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_unit_length_resistance_c:单位长度摩擦阻力--主蒸汽分管,的计算15-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_c != NEW.main_steam_msv_c OR OLD.main_steam_pipe_outer_diameter_c != NEW.main_steam_pipe_outer_diameter_c OR OLD.main_steam_pipe_thickness_c != NEW.main_steam_pipe_thickness_c OR OLD.main_steam_resistance_coefficient_c != NEW.main_steam_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_unit_length_resistance_c=(NEW.main_steam_resistance_coefficient_c)*(((0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2))^2/2/(NEW.main_steam_msv_c))/((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_resistance_coefficient_c ISNULL OR OLD.main_steam_pipe_thickness_c ISNULL OR OLD.main_steam_pipe_outer_diameter_c ISNULL OR OLD.main_steam_msv_c ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_resistance_coefficient_c NOTNULL AND NEW.main_steam_pipe_thickness_c NOTNULL AND NEW.main_steam_pipe_outer_diameter_c NOTNULL AND NEW.main_steam_msv_c NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_unit_length_resistance_c=(NEW.main_steam_resistance_coefficient_c)*(((0.3537*(NEW.main_steam_rated_flow_c)*(NEW.main_steam_msv_c)/(((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c)))^2))^2/2/(NEW.main_steam_msv_c))/((NEW.main_steam_pipe_outer_diameter_c)-2*(NEW.main_steam_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_rated_flow_m:额定流量--主蒸汽母管,的计算16-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_rated_flow_m=(NEW.main_steam_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_rated_flow_m=(NEW.main_steam_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_media_viscosity_m:介质运动粘度--主蒸汽母管,的计算17-----------------------------------
  IF OLD.main_steam_media_viscosity_c != NEW.main_steam_media_viscosity_c THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_media_viscosity_m=(NEW.main_steam_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_media_viscosity_c ISNULL) AND NEW.main_steam_media_viscosity_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_media_viscosity_m=(NEW.main_steam_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_calculate_velocity_m:计算流速--主蒸汽母管,的计算18-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_m != NEW.main_steam_msv_m OR OLD.main_steam_pipe_outer_diameter_m != NEW.main_steam_pipe_outer_diameter_m OR OLD.main_steam_pipe_thickness_m != NEW.main_steam_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_calculate_velocity_m=0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_thickness_m ISNULL OR OLD.main_steam_pipe_outer_diameter_m ISNULL OR OLD.main_steam_msv_m ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_pipe_thickness_m NOTNULL AND NEW.main_steam_pipe_outer_diameter_m NOTNULL AND NEW.main_steam_msv_m NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_calculate_velocity_m=0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_dynamic_head_m:动压头--主蒸汽母管,的计算19-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_m != NEW.main_steam_msv_m OR OLD.main_steam_pipe_outer_diameter_m != NEW.main_steam_pipe_outer_diameter_m OR OLD.main_steam_pipe_thickness_m != NEW.main_steam_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_dynamic_head_m=((0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2))^2/2/(NEW.main_steam_msv_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_thickness_m ISNULL OR OLD.main_steam_pipe_outer_diameter_m ISNULL OR OLD.main_steam_msv_m ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_pipe_thickness_m NOTNULL AND NEW.main_steam_pipe_outer_diameter_m NOTNULL AND NEW.main_steam_msv_m NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_dynamic_head_m=((0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2))^2/2/(NEW.main_steam_msv_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_pipe_inner_diameter_m:内径--主蒸汽母管,的计算20-----------------------------------
  IF OLD.main_steam_pipe_outer_diameter_m != NEW.main_steam_pipe_outer_diameter_m OR OLD.main_steam_pipe_thickness_m != NEW.main_steam_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_pipe_inner_diameter_m=(NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_thickness_m ISNULL OR OLD.main_steam_pipe_outer_diameter_m ISNULL) AND NEW.main_steam_pipe_thickness_m NOTNULL AND NEW.main_steam_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_pipe_inner_diameter_m=(NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_friction_resistance_m:摩擦阻力--主蒸汽母管,的计算21-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_m != NEW.main_steam_msv_m OR OLD.main_steam_pipe_outer_diameter_m != NEW.main_steam_pipe_outer_diameter_m OR OLD.main_steam_pipe_thickness_m != NEW.main_steam_pipe_thickness_m OR OLD.main_steam_resistance_coefficient_m != NEW.main_steam_resistance_coefficient_m OR OLD.main_steam_pipe_length_m != NEW.main_steam_pipe_length_m THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_friction_resistance_m=((NEW.main_steam_resistance_coefficient_m)*(((0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2))^2/2/(NEW.main_steam_msv_m))/((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))*(NEW.main_steam_pipe_length_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_length_m ISNULL OR OLD.main_steam_resistance_coefficient_m ISNULL OR OLD.main_steam_pipe_thickness_m ISNULL OR OLD.main_steam_pipe_outer_diameter_m ISNULL OR OLD.main_steam_msv_m ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_pipe_length_m NOTNULL AND NEW.main_steam_resistance_coefficient_m NOTNULL AND NEW.main_steam_pipe_thickness_m NOTNULL AND NEW.main_steam_pipe_outer_diameter_m NOTNULL AND NEW.main_steam_msv_m NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_friction_resistance_m=((NEW.main_steam_resistance_coefficient_m)*(((0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2))^2/2/(NEW.main_steam_msv_m))/((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))*(NEW.main_steam_pipe_length_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_reynolds_m:雷诺数--主蒸汽母管,的计算22-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_media_viscosity_c != NEW.main_steam_media_viscosity_c OR OLD.main_steam_msv_m != NEW.main_steam_msv_m OR OLD.main_steam_pipe_outer_diameter_m != NEW.main_steam_pipe_outer_diameter_m OR OLD.main_steam_pipe_thickness_m != NEW.main_steam_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_reynolds_m=(0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2)*((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m))/((NEW.main_steam_media_viscosity_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_pipe_thickness_m ISNULL OR OLD.main_steam_pipe_outer_diameter_m ISNULL OR OLD.main_steam_msv_m ISNULL OR OLD.main_steam_media_viscosity_c ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_pipe_thickness_m NOTNULL AND NEW.main_steam_pipe_outer_diameter_m NOTNULL AND NEW.main_steam_msv_m NOTNULL AND NEW.main_steam_media_viscosity_c NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_reynolds_m=(0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2)*((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m))/((NEW.main_steam_media_viscosity_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_relative_roughness_m:相对粗糙度--主蒸汽母管,的计算23-----------------------------------
  IF OLD.main_steam_pipe_outer_diameter_m != NEW.main_steam_pipe_outer_diameter_m OR OLD.main_steam_pipe_thickness_m != NEW.main_steam_pipe_thickness_m OR OLD.main_steam_equivalent_roughness_m != NEW.main_steam_equivalent_roughness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_relative_roughness_m=(NEW.main_steam_equivalent_roughness_m)/((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_equivalent_roughness_m ISNULL OR OLD.main_steam_pipe_thickness_m ISNULL OR OLD.main_steam_pipe_outer_diameter_m ISNULL) AND NEW.main_steam_equivalent_roughness_m NOTNULL AND NEW.main_steam_pipe_thickness_m NOTNULL AND NEW.main_steam_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_relative_roughness_m=(NEW.main_steam_equivalent_roughness_m)/((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段main_steam_unit_length_resistance_m:单位长度摩擦阻力--主蒸汽母管,的计算24-----------------------------------
  IF OLD.main_steam_rated_flow_c != NEW.main_steam_rated_flow_c OR OLD.main_steam_msv_m != NEW.main_steam_msv_m OR OLD.main_steam_pipe_outer_diameter_m != NEW.main_steam_pipe_outer_diameter_m OR OLD.main_steam_pipe_thickness_m != NEW.main_steam_pipe_thickness_m OR OLD.main_steam_resistance_coefficient_m != NEW.main_steam_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_unit_length_resistance_m=(NEW.main_steam_resistance_coefficient_m)*(((0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2))^2/2/(NEW.main_steam_msv_m))/((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.main_steam_resistance_coefficient_m ISNULL OR OLD.main_steam_pipe_thickness_m ISNULL OR OLD.main_steam_pipe_outer_diameter_m ISNULL OR OLD.main_steam_msv_m ISNULL OR OLD.main_steam_rated_flow_c ISNULL) AND NEW.main_steam_resistance_coefficient_m NOTNULL AND NEW.main_steam_pipe_thickness_m NOTNULL AND NEW.main_steam_pipe_outer_diameter_m NOTNULL AND NEW.main_steam_msv_m NOTNULL AND NEW.main_steam_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     main_steam_unit_length_resistance_m=(NEW.main_steam_resistance_coefficient_m)*(((0.3537*((NEW.main_steam_rated_flow_c)*4)*(NEW.main_steam_msv_m)/(((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m)))^2))^2/2/(NEW.main_steam_msv_m))/((NEW.main_steam_pipe_outer_diameter_m)-2*(NEW.main_steam_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deoxidized_steam_calculate_velocity:计算流速--除氧加热蒸汽,的计算25-----------------------------------
  IF OLD.deoxidized_steam_rated_flow != NEW.deoxidized_steam_rated_flow OR OLD.deoxidized_steam_msv != NEW.deoxidized_steam_msv OR OLD.deoxidized_steam_pipe_outer_diameter != NEW.deoxidized_steam_pipe_outer_diameter OR OLD.deoxidized_steam_pipe_thickness != NEW.deoxidized_steam_pipe_thickness THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_calculate_velocity=0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deoxidized_steam_pipe_thickness ISNULL OR OLD.deoxidized_steam_pipe_outer_diameter ISNULL OR OLD.deoxidized_steam_msv ISNULL OR OLD.deoxidized_steam_rated_flow ISNULL) AND NEW.deoxidized_steam_pipe_thickness NOTNULL AND NEW.deoxidized_steam_pipe_outer_diameter NOTNULL AND NEW.deoxidized_steam_msv NOTNULL AND NEW.deoxidized_steam_rated_flow NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_calculate_velocity=0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deoxidized_steam_dynamic_head:动压头--除氧加热蒸汽,的计算26-----------------------------------
  IF OLD.deoxidized_steam_rated_flow != NEW.deoxidized_steam_rated_flow OR OLD.deoxidized_steam_msv != NEW.deoxidized_steam_msv OR OLD.deoxidized_steam_pipe_outer_diameter != NEW.deoxidized_steam_pipe_outer_diameter OR OLD.deoxidized_steam_pipe_thickness != NEW.deoxidized_steam_pipe_thickness THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_dynamic_head=((0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2))^2/2/(NEW.deoxidized_steam_msv)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deoxidized_steam_pipe_thickness ISNULL OR OLD.deoxidized_steam_pipe_outer_diameter ISNULL OR OLD.deoxidized_steam_msv ISNULL OR OLD.deoxidized_steam_rated_flow ISNULL) AND NEW.deoxidized_steam_pipe_thickness NOTNULL AND NEW.deoxidized_steam_pipe_outer_diameter NOTNULL AND NEW.deoxidized_steam_msv NOTNULL AND NEW.deoxidized_steam_rated_flow NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_dynamic_head=((0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2))^2/2/(NEW.deoxidized_steam_msv)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deoxidized_steam_pipe_inner_diameter:内径--除氧加热蒸汽,的计算27-----------------------------------
  IF OLD.deoxidized_steam_pipe_outer_diameter != NEW.deoxidized_steam_pipe_outer_diameter OR OLD.deoxidized_steam_pipe_thickness != NEW.deoxidized_steam_pipe_thickness THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_pipe_inner_diameter=(NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deoxidized_steam_pipe_thickness ISNULL OR OLD.deoxidized_steam_pipe_outer_diameter ISNULL) AND NEW.deoxidized_steam_pipe_thickness NOTNULL AND NEW.deoxidized_steam_pipe_outer_diameter NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_pipe_inner_diameter=(NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deoxidized_steam_friction_resistance:摩擦阻力--除氧加热蒸汽,的计算28-----------------------------------
  IF OLD.deoxidized_steam_rated_flow != NEW.deoxidized_steam_rated_flow OR OLD.deoxidized_steam_msv != NEW.deoxidized_steam_msv OR OLD.deoxidized_steam_pipe_outer_diameter != NEW.deoxidized_steam_pipe_outer_diameter OR OLD.deoxidized_steam_pipe_thickness != NEW.deoxidized_steam_pipe_thickness OR OLD.deoxidized_steam_resistance_coefficient != NEW.deoxidized_steam_resistance_coefficient OR OLD.deoxidized_steam_pipe_length != NEW.deoxidized_steam_pipe_length THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_friction_resistance=((NEW.deoxidized_steam_resistance_coefficient)*(((0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2))^2/2/(NEW.deoxidized_steam_msv))/((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))*(NEW.deoxidized_steam_pipe_length)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deoxidized_steam_pipe_length ISNULL OR OLD.deoxidized_steam_resistance_coefficient ISNULL OR OLD.deoxidized_steam_pipe_thickness ISNULL OR OLD.deoxidized_steam_pipe_outer_diameter ISNULL OR OLD.deoxidized_steam_msv ISNULL OR OLD.deoxidized_steam_rated_flow ISNULL) AND NEW.deoxidized_steam_pipe_length NOTNULL AND NEW.deoxidized_steam_resistance_coefficient NOTNULL AND NEW.deoxidized_steam_pipe_thickness NOTNULL AND NEW.deoxidized_steam_pipe_outer_diameter NOTNULL AND NEW.deoxidized_steam_msv NOTNULL AND NEW.deoxidized_steam_rated_flow NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_friction_resistance=((NEW.deoxidized_steam_resistance_coefficient)*(((0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2))^2/2/(NEW.deoxidized_steam_msv))/((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))*(NEW.deoxidized_steam_pipe_length)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deoxidized_steam_reynolds:雷诺数--除氧加热蒸汽,的计算29-----------------------------------
  IF OLD.deoxidized_steam_rated_flow != NEW.deoxidized_steam_rated_flow OR OLD.deoxidized_steam_msv != NEW.deoxidized_steam_msv OR OLD.deoxidized_steam_media_viscosity != NEW.deoxidized_steam_media_viscosity OR OLD.deoxidized_steam_pipe_outer_diameter != NEW.deoxidized_steam_pipe_outer_diameter OR OLD.deoxidized_steam_pipe_thickness != NEW.deoxidized_steam_pipe_thickness THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_reynolds=(0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2)*((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness))/(NEW.deoxidized_steam_media_viscosity)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deoxidized_steam_pipe_thickness ISNULL OR OLD.deoxidized_steam_pipe_outer_diameter ISNULL OR OLD.deoxidized_steam_media_viscosity ISNULL OR OLD.deoxidized_steam_msv ISNULL OR OLD.deoxidized_steam_rated_flow ISNULL) AND NEW.deoxidized_steam_pipe_thickness NOTNULL AND NEW.deoxidized_steam_pipe_outer_diameter NOTNULL AND NEW.deoxidized_steam_media_viscosity NOTNULL AND NEW.deoxidized_steam_msv NOTNULL AND NEW.deoxidized_steam_rated_flow NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_reynolds=(0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2)*((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness))/(NEW.deoxidized_steam_media_viscosity)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deoxidized_steam_relative_roughness:相对粗糙度--除氧加热蒸汽,的计算30-----------------------------------
  IF OLD.deoxidized_steam_pipe_outer_diameter != NEW.deoxidized_steam_pipe_outer_diameter OR OLD.deoxidized_steam_pipe_thickness != NEW.deoxidized_steam_pipe_thickness OR OLD.deoxidized_steam_equivalent_roughness != NEW.deoxidized_steam_equivalent_roughness THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_relative_roughness=(NEW.deoxidized_steam_equivalent_roughness)/((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deoxidized_steam_equivalent_roughness ISNULL OR OLD.deoxidized_steam_pipe_thickness ISNULL OR OLD.deoxidized_steam_pipe_outer_diameter ISNULL) AND NEW.deoxidized_steam_equivalent_roughness NOTNULL AND NEW.deoxidized_steam_pipe_thickness NOTNULL AND NEW.deoxidized_steam_pipe_outer_diameter NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_relative_roughness=(NEW.deoxidized_steam_equivalent_roughness)/((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deoxidized_steam_unit_length_resistance:单位长度摩擦阻力--除氧加热蒸汽,的计算31-----------------------------------
  IF OLD.deoxidized_steam_rated_flow != NEW.deoxidized_steam_rated_flow OR OLD.deoxidized_steam_msv != NEW.deoxidized_steam_msv OR OLD.deoxidized_steam_pipe_outer_diameter != NEW.deoxidized_steam_pipe_outer_diameter OR OLD.deoxidized_steam_pipe_thickness != NEW.deoxidized_steam_pipe_thickness OR OLD.deoxidized_steam_resistance_coefficient != NEW.deoxidized_steam_resistance_coefficient THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_unit_length_resistance=(NEW.deoxidized_steam_resistance_coefficient)*(((0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2))^2/2/(NEW.deoxidized_steam_msv))/((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deoxidized_steam_resistance_coefficient ISNULL OR OLD.deoxidized_steam_pipe_thickness ISNULL OR OLD.deoxidized_steam_pipe_outer_diameter ISNULL OR OLD.deoxidized_steam_msv ISNULL OR OLD.deoxidized_steam_rated_flow ISNULL) AND NEW.deoxidized_steam_resistance_coefficient NOTNULL AND NEW.deoxidized_steam_pipe_thickness NOTNULL AND NEW.deoxidized_steam_pipe_outer_diameter NOTNULL AND NEW.deoxidized_steam_msv NOTNULL AND NEW.deoxidized_steam_rated_flow NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     deoxidized_steam_unit_length_resistance=(NEW.deoxidized_steam_resistance_coefficient)*(((0.3537*(NEW.deoxidized_steam_rated_flow)*(NEW.deoxidized_steam_msv)/(((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness)))^2))^2/2/(NEW.deoxidized_steam_msv))/((NEW.deoxidized_steam_pipe_outer_diameter)-2*(NEW.deoxidized_steam_pipe_thickness))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_calculate_velocity_c:计算流速--低压给水分管,的计算32-----------------------------------
  IF OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c OR OLD.l_feedwater_msv_c != NEW.l_feedwater_msv_c OR OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_calculate_velocity_c=0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL OR OLD.l_feedwater_msv_c ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.l_feedwater_msv_c NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_calculate_velocity_c=0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_dynamic_head_c:动压头--低压给水分管,的计算33-----------------------------------
  IF OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c OR OLD.l_feedwater_msv_c != NEW.l_feedwater_msv_c OR OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_dynamic_head_c=((0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.l_feedwater_msv_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL OR OLD.l_feedwater_msv_c ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.l_feedwater_msv_c NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_dynamic_head_c=((0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.l_feedwater_msv_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_pipe_inner_diameter_c:内径--低压给水分管,的计算34-----------------------------------
  IF OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_pipe_inner_diameter_c=(NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL) AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_pipe_inner_diameter_c=(NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_friction_resistance_c:摩擦阻力--低压给水分管,的计算35-----------------------------------
  IF OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c OR OLD.l_feedwater_msv_c != NEW.l_feedwater_msv_c OR OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c OR OLD.l_feedwater_resistance_coefficient_c != NEW.l_feedwater_resistance_coefficient_c OR OLD.l_feedwater_pipe_length_c != NEW.l_feedwater_pipe_length_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_friction_resistance_c=((NEW.l_feedwater_resistance_coefficient_c)*(((0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.l_feedwater_msv_c))/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))*(NEW.l_feedwater_pipe_length_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_length_c ISNULL OR OLD.l_feedwater_resistance_coefficient_c ISNULL OR OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL OR OLD.l_feedwater_msv_c ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_pipe_length_c NOTNULL AND NEW.l_feedwater_resistance_coefficient_c NOTNULL AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.l_feedwater_msv_c NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_friction_resistance_c=((NEW.l_feedwater_resistance_coefficient_c)*(((0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.l_feedwater_msv_c))/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))*(NEW.l_feedwater_pipe_length_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_reynolds_c:雷诺数--低压给水分管,的计算36-----------------------------------
  IF OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c OR OLD.l_feedwater_msv_c != NEW.l_feedwater_msv_c OR OLD.l_feedwater_media_viscosity_c != NEW.l_feedwater_media_viscosity_c OR OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_reynolds_c=(0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2)*((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))/(NEW.l_feedwater_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL OR OLD.l_feedwater_media_viscosity_c ISNULL OR OLD.l_feedwater_msv_c ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.l_feedwater_media_viscosity_c NOTNULL AND NEW.l_feedwater_msv_c NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_reynolds_c=(0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2)*((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))/(NEW.l_feedwater_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_relative_roughness_c:相对粗糙度--低压给水分管,的计算37-----------------------------------
  IF OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c OR OLD.l_feedwater_equivalent_roughness_c != NEW.l_feedwater_equivalent_roughness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_relative_roughness_c=(NEW.l_feedwater_equivalent_roughness_c)/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_equivalent_roughness_c ISNULL OR OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL) AND NEW.l_feedwater_equivalent_roughness_c NOTNULL AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_relative_roughness_c=(NEW.l_feedwater_equivalent_roughness_c)/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_unit_length_resistance_c:单位长度摩擦阻力--低压给水分管,的计算38-----------------------------------
  IF OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c OR OLD.l_feedwater_msv_c != NEW.l_feedwater_msv_c OR OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c OR OLD.l_feedwater_resistance_coefficient_c != NEW.l_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_unit_length_resistance_c=(NEW.l_feedwater_resistance_coefficient_c)*(((0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.l_feedwater_msv_c))/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_resistance_coefficient_c ISNULL OR OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL OR OLD.l_feedwater_msv_c ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_resistance_coefficient_c NOTNULL AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.l_feedwater_msv_c NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_unit_length_resistance_c=(NEW.l_feedwater_resistance_coefficient_c)*(((0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.l_feedwater_msv_c))/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_local_resistance_c:局部阻力--低压给水分管,的计算39-----------------------------------
  IF OLD.l_feedwater_90elbow_count_c != NEW.l_feedwater_90elbow_count_c OR OLD.l_feedwater_triplet_count_c != NEW.l_feedwater_triplet_count_c OR OLD.l_feedwater_converging_spec_c != NEW.l_feedwater_converging_spec_c OR OLD.l_feedwater_converging_angle_c != NEW.l_feedwater_converging_angle_c OR OLD.l_feedwater_converging_diameter_radio_c != NEW.l_feedwater_converging_diameter_radio_c OR OLD.l_feedwater_filter_c != NEW.l_feedwater_filter_c OR OLD.l_feedwater_sluice_count_c != NEW.l_feedwater_sluice_count_c OR OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c OR OLD.l_feedwater_msv_c != NEW.l_feedwater_msv_c OR OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c OR OLD.l_feedwater_equivalent_roughness_c != NEW.l_feedwater_equivalent_roughness_c OR OLD.l_feedwater_resistance_coefficient_c != NEW.l_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_local_resistance_c=(((((2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4))*(NEW.l_feedwater_triplet_count_c))*(NEW.l_feedwater_90elbow_count_c))+(60*(NEW.l_feedwater_equivalent_roughness_c))+(NEW.l_feedwater_converging_spec_c)+(NEW.l_feedwater_filter_c)+((8*(NEW.l_feedwater_resistance_coefficient_c))*(NEW.l_feedwater_sluice_count_c))+((NEW.l_feedwater_rated_flow_c)*4))*(((0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.l_feedwater_msv_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_sluice_count_c ISNULL OR OLD.l_feedwater_filter_c ISNULL OR OLD.l_feedwater_converging_diameter_radio_c ISNULL OR OLD.l_feedwater_converging_angle_c ISNULL OR OLD.l_feedwater_converging_spec_c ISNULL OR OLD.l_feedwater_triplet_count_c ISNULL OR OLD.l_feedwater_90elbow_count_c ISNULL OR OLD.l_feedwater_resistance_coefficient_c ISNULL OR OLD.l_feedwater_equivalent_roughness_c ISNULL OR OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL OR OLD.l_feedwater_msv_c ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_sluice_count_c NOTNULL AND NEW.l_feedwater_filter_c NOTNULL AND NEW.l_feedwater_converging_diameter_radio_c NOTNULL AND NEW.l_feedwater_converging_angle_c NOTNULL AND NEW.l_feedwater_converging_spec_c NOTNULL AND NEW.l_feedwater_triplet_count_c NOTNULL AND NEW.l_feedwater_90elbow_count_c NOTNULL AND NEW.l_feedwater_resistance_coefficient_c NOTNULL AND NEW.l_feedwater_equivalent_roughness_c NOTNULL AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.l_feedwater_msv_c NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_local_resistance_c=(((((2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4))*(NEW.l_feedwater_triplet_count_c))*(NEW.l_feedwater_90elbow_count_c))+(60*(NEW.l_feedwater_equivalent_roughness_c))+(NEW.l_feedwater_converging_spec_c)+(NEW.l_feedwater_filter_c)+((8*(NEW.l_feedwater_resistance_coefficient_c))*(NEW.l_feedwater_sluice_count_c))+((NEW.l_feedwater_rated_flow_c)*4))*(((0.3537*(NEW.l_feedwater_rated_flow_c)*(NEW.l_feedwater_msv_c)/(((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.l_feedwater_msv_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_total_local_resistance_coefficient_c:局部阻力系数合计--低压给水分管,的计算40-----------------------------------
  IF OLD.l_feedwater_90elbow_count_c != NEW.l_feedwater_90elbow_count_c OR OLD.l_feedwater_triplet_count_c != NEW.l_feedwater_triplet_count_c OR OLD.l_feedwater_converging_spec_c != NEW.l_feedwater_converging_spec_c OR OLD.l_feedwater_converging_angle_c != NEW.l_feedwater_converging_angle_c OR OLD.l_feedwater_converging_diameter_radio_c != NEW.l_feedwater_converging_diameter_radio_c OR OLD.l_feedwater_filter_c != NEW.l_feedwater_filter_c OR OLD.l_feedwater_sluice_count_c != NEW.l_feedwater_sluice_count_c OR OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c OR OLD.l_feedwater_equivalent_roughness_c != NEW.l_feedwater_equivalent_roughness_c OR OLD.l_feedwater_resistance_coefficient_c != NEW.l_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_total_local_resistance_coefficient_c=((((2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4))*(NEW.l_feedwater_triplet_count_c))*(NEW.l_feedwater_90elbow_count_c))+(60*(NEW.l_feedwater_equivalent_roughness_c))+(NEW.l_feedwater_converging_spec_c)+(NEW.l_feedwater_filter_c)+((8*(NEW.l_feedwater_resistance_coefficient_c))*(NEW.l_feedwater_sluice_count_c))+((NEW.l_feedwater_rated_flow_c)*4)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_sluice_count_c ISNULL OR OLD.l_feedwater_filter_c ISNULL OR OLD.l_feedwater_converging_diameter_radio_c ISNULL OR OLD.l_feedwater_converging_angle_c ISNULL OR OLD.l_feedwater_converging_spec_c ISNULL OR OLD.l_feedwater_triplet_count_c ISNULL OR OLD.l_feedwater_90elbow_count_c ISNULL OR OLD.l_feedwater_resistance_coefficient_c ISNULL OR OLD.l_feedwater_equivalent_roughness_c ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_sluice_count_c NOTNULL AND NEW.l_feedwater_filter_c NOTNULL AND NEW.l_feedwater_converging_diameter_radio_c NOTNULL AND NEW.l_feedwater_converging_angle_c NOTNULL AND NEW.l_feedwater_converging_spec_c NOTNULL AND NEW.l_feedwater_triplet_count_c NOTNULL AND NEW.l_feedwater_90elbow_count_c NOTNULL AND NEW.l_feedwater_resistance_coefficient_c NOTNULL AND NEW.l_feedwater_equivalent_roughness_c NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_total_local_resistance_coefficient_c=((((2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4))*(NEW.l_feedwater_triplet_count_c))*(NEW.l_feedwater_90elbow_count_c))+(60*(NEW.l_feedwater_equivalent_roughness_c))+(NEW.l_feedwater_converging_spec_c)+(NEW.l_feedwater_filter_c)+((8*(NEW.l_feedwater_resistance_coefficient_c))*(NEW.l_feedwater_sluice_count_c))+((NEW.l_feedwater_rated_flow_c)*4)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_elbow_resistance_coefficient_c:弯头阻力系数--低压给水分管,的计算41-----------------------------------
  IF OLD.l_feedwater_90elbow_count_c != NEW.l_feedwater_90elbow_count_c OR OLD.l_feedwater_triplet_count_c != NEW.l_feedwater_triplet_count_c OR OLD.l_feedwater_converging_angle_c != NEW.l_feedwater_converging_angle_c OR OLD.l_feedwater_converging_diameter_radio_c != NEW.l_feedwater_converging_diameter_radio_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_elbow_resistance_coefficient_c=(((2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4))*(NEW.l_feedwater_triplet_count_c))*(NEW.l_feedwater_90elbow_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_converging_diameter_radio_c ISNULL OR OLD.l_feedwater_converging_angle_c ISNULL OR OLD.l_feedwater_triplet_count_c ISNULL OR OLD.l_feedwater_90elbow_count_c ISNULL) AND NEW.l_feedwater_converging_diameter_radio_c NOTNULL AND NEW.l_feedwater_converging_angle_c NOTNULL AND NEW.l_feedwater_triplet_count_c NOTNULL AND NEW.l_feedwater_90elbow_count_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_elbow_resistance_coefficient_c=(((2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4))*(NEW.l_feedwater_triplet_count_c))*(NEW.l_feedwater_90elbow_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_elbow_radius_to_inner_diameter_c:弯头半径/内径--低压给水分管,的计算42-----------------------------------
  IF OLD.l_feedwater_elbow_radius_c != NEW.l_feedwater_elbow_radius_c OR OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_elbow_radius_to_inner_diameter_c=(NEW.l_feedwater_elbow_radius_c)/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_elbow_radius_c ISNULL OR OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL) AND NEW.l_feedwater_elbow_radius_c NOTNULL AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_elbow_radius_to_inner_diameter_c=(NEW.l_feedwater_elbow_radius_c)/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_90elbow_resistance_coefficient_c:单个90º弯头阻力系数--低压给水分管,的计算43-----------------------------------
  IF OLD.l_feedwater_pipe_outer_diameter_c != NEW.l_feedwater_pipe_outer_diameter_c OR OLD.l_feedwater_pipe_thickness_c != NEW.l_feedwater_pipe_thickness_c OR OLD.l_feedwater_equivalent_roughness_c != NEW.l_feedwater_equivalent_roughness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_90elbow_resistance_coefficient_c=14*((NEW.l_feedwater_equivalent_roughness_c)/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))/1000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_equivalent_roughness_c ISNULL OR OLD.l_feedwater_pipe_thickness_c ISNULL OR OLD.l_feedwater_pipe_outer_diameter_c ISNULL) AND NEW.l_feedwater_equivalent_roughness_c NOTNULL AND NEW.l_feedwater_pipe_thickness_c NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_90elbow_resistance_coefficient_c=14*((NEW.l_feedwater_equivalent_roughness_c)/((NEW.l_feedwater_pipe_outer_diameter_c)-2*(NEW.l_feedwater_pipe_thickness_c))/1000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_triplet_resistance_coefficient_c:三通阻力系数--低压给水分管,的计算44-----------------------------------
  IF OLD.l_feedwater_triplet_count_c != NEW.l_feedwater_triplet_count_c OR OLD.l_feedwater_converging_angle_c != NEW.l_feedwater_converging_angle_c OR OLD.l_feedwater_converging_diameter_radio_c != NEW.l_feedwater_converging_diameter_radio_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_triplet_resistance_coefficient_c=((2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4))*(NEW.l_feedwater_triplet_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_converging_diameter_radio_c ISNULL OR OLD.l_feedwater_converging_angle_c ISNULL OR OLD.l_feedwater_triplet_count_c ISNULL) AND NEW.l_feedwater_converging_diameter_radio_c NOTNULL AND NEW.l_feedwater_converging_angle_c NOTNULL AND NEW.l_feedwater_triplet_count_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_triplet_resistance_coefficient_c=((2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4))*(NEW.l_feedwater_triplet_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_single_triplet_resistance_coefficient_c:单个三通阻力系数--低压给水分管,的计算45-----------------------------------
  IF OLD.l_feedwater_equivalent_roughness_c != NEW.l_feedwater_equivalent_roughness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_single_triplet_resistance_coefficient_c=60*(NEW.l_feedwater_equivalent_roughness_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_equivalent_roughness_c ISNULL) AND NEW.l_feedwater_equivalent_roughness_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_single_triplet_resistance_coefficient_c=60*(NEW.l_feedwater_equivalent_roughness_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_reducer_resistance_coefficient_c:异径管的阻力系数--低压给水分管,的计算46-----------------------------------
  IF OLD.l_feedwater_converging_angle_c != NEW.l_feedwater_converging_angle_c OR OLD.l_feedwater_converging_diameter_radio_c != NEW.l_feedwater_converging_diameter_radio_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_reducer_resistance_coefficient_c=(2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_converging_diameter_radio_c ISNULL OR OLD.l_feedwater_converging_angle_c ISNULL) AND NEW.l_feedwater_converging_diameter_radio_c NOTNULL AND NEW.l_feedwater_converging_angle_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_reducer_resistance_coefficient_c=(2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_converging_resistance_coefficient_c:渐缩管（相应于小管径的阻力系数）--低压给水分管,的计算47-----------------------------------
  IF OLD.l_feedwater_converging_angle_c != NEW.l_feedwater_converging_angle_c OR OLD.l_feedwater_converging_diameter_radio_c != NEW.l_feedwater_converging_diameter_radio_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_converging_resistance_coefficient_c=2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_converging_diameter_radio_c ISNULL OR OLD.l_feedwater_converging_angle_c ISNULL) AND NEW.l_feedwater_converging_diameter_radio_c NOTNULL AND NEW.l_feedwater_converging_angle_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_converging_resistance_coefficient_c=2.6*sin((NEW.l_feedwater_converging_angle_c)*3.14/180)*(1-((NEW.l_feedwater_converging_diameter_radio_c))^2)/((NEW.l_feedwater_converging_diameter_radio_c))^4
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_valve_resistance_coefficient_c:阀门的局部阻力系数--低压给水分管,的计算48-----------------------------------
  IF OLD.l_feedwater_filter_c != NEW.l_feedwater_filter_c OR OLD.l_feedwater_sluice_count_c != NEW.l_feedwater_sluice_count_c OR OLD.l_feedwater_check_resistance_coefficient_c != NEW.l_feedwater_check_resistance_coefficient_c OR OLD.l_feedwater_plate_resistance_coefficient_c != NEW.l_feedwater_plate_resistance_coefficient_c OR OLD.l_feedwater_resistance_coefficient_c != NEW.l_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_valve_resistance_coefficient_c=(NEW.l_feedwater_filter_c)+((8*(NEW.l_feedwater_resistance_coefficient_c))*(NEW.l_feedwater_sluice_count_c))+(NEW.l_feedwater_check_resistance_coefficient_c)+(NEW.l_feedwater_plate_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_plate_resistance_coefficient_c ISNULL OR OLD.l_feedwater_check_resistance_coefficient_c ISNULL OR OLD.l_feedwater_sluice_count_c ISNULL OR OLD.l_feedwater_filter_c ISNULL OR OLD.l_feedwater_resistance_coefficient_c ISNULL) AND NEW.l_feedwater_plate_resistance_coefficient_c NOTNULL AND NEW.l_feedwater_check_resistance_coefficient_c NOTNULL AND NEW.l_feedwater_sluice_count_c NOTNULL AND NEW.l_feedwater_filter_c NOTNULL AND NEW.l_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_valve_resistance_coefficient_c=(NEW.l_feedwater_filter_c)+((8*(NEW.l_feedwater_resistance_coefficient_c))*(NEW.l_feedwater_sluice_count_c))+(NEW.l_feedwater_check_resistance_coefficient_c)+(NEW.l_feedwater_plate_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_sluice_resistance_coefficient_c:闸阀阻力系数--低压给水分管,的计算49-----------------------------------
  IF OLD.l_feedwater_sluice_count_c != NEW.l_feedwater_sluice_count_c OR OLD.l_feedwater_resistance_coefficient_c != NEW.l_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_sluice_resistance_coefficient_c=(8*(NEW.l_feedwater_resistance_coefficient_c))*(NEW.l_feedwater_sluice_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_sluice_count_c ISNULL OR OLD.l_feedwater_resistance_coefficient_c ISNULL) AND NEW.l_feedwater_sluice_count_c NOTNULL AND NEW.l_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_sluice_resistance_coefficient_c=(8*(NEW.l_feedwater_resistance_coefficient_c))*(NEW.l_feedwater_sluice_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_single_sluice_resistance_coefficient_c:单个闸阀阻力系数--低压给水分管,的计算50-----------------------------------
  IF OLD.l_feedwater_resistance_coefficient_c != NEW.l_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_single_sluice_resistance_coefficient_c=8*(NEW.l_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_resistance_coefficient_c ISNULL) AND NEW.l_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_single_sluice_resistance_coefficient_c=8*(NEW.l_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_rated_flow_m:额定流量--低压给水母管,的计算51-----------------------------------
  IF OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_rated_flow_m=(NEW.l_feedwater_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_rated_flow_m=(NEW.l_feedwater_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_media_viscosity_m:介质运动粘度--低压给水母管,的计算52-----------------------------------
  IF OLD.l_feedwater_media_viscosity_c != NEW.l_feedwater_media_viscosity_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_media_viscosity_m=(NEW.l_feedwater_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_media_viscosity_c ISNULL) AND NEW.l_feedwater_media_viscosity_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_media_viscosity_m=(NEW.l_feedwater_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_calculate_velocity_m:计算流速--低压给水母管,的计算53-----------------------------------
  IF OLD.l_feedwater_msv_m != NEW.l_feedwater_msv_m OR OLD.l_feedwater_pipe_outer_diameter_m != NEW.l_feedwater_pipe_outer_diameter_m OR OLD.l_feedwater_pipe_thickness_m != NEW.l_feedwater_pipe_thickness_m OR OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_calculate_velocity_m=0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_thickness_m ISNULL OR OLD.l_feedwater_pipe_outer_diameter_m ISNULL OR OLD.l_feedwater_msv_m ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_pipe_thickness_m NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.l_feedwater_msv_m NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_calculate_velocity_m=0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_dynamic_head_m:动压头--低压给水母管,的计算54-----------------------------------
  IF OLD.l_feedwater_msv_m != NEW.l_feedwater_msv_m OR OLD.l_feedwater_pipe_outer_diameter_m != NEW.l_feedwater_pipe_outer_diameter_m OR OLD.l_feedwater_pipe_thickness_m != NEW.l_feedwater_pipe_thickness_m OR OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_dynamic_head_m=((0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2))^2/2/(NEW.l_feedwater_msv_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_thickness_m ISNULL OR OLD.l_feedwater_pipe_outer_diameter_m ISNULL OR OLD.l_feedwater_msv_m ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_pipe_thickness_m NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.l_feedwater_msv_m NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_dynamic_head_m=((0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2))^2/2/(NEW.l_feedwater_msv_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_pipe_inner_diameter_m:内径--低压给水母管,的计算55-----------------------------------
  IF OLD.l_feedwater_pipe_outer_diameter_m != NEW.l_feedwater_pipe_outer_diameter_m OR OLD.l_feedwater_pipe_thickness_m != NEW.l_feedwater_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_pipe_inner_diameter_m=(NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_thickness_m ISNULL OR OLD.l_feedwater_pipe_outer_diameter_m ISNULL) AND NEW.l_feedwater_pipe_thickness_m NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_pipe_inner_diameter_m=(NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_friction_resistance_m:摩擦阻力--低压给水母管,的计算56-----------------------------------
  IF OLD.l_feedwater_msv_m != NEW.l_feedwater_msv_m OR OLD.l_feedwater_pipe_outer_diameter_m != NEW.l_feedwater_pipe_outer_diameter_m OR OLD.l_feedwater_pipe_thickness_m != NEW.l_feedwater_pipe_thickness_m OR OLD.l_feedwater_resistance_coefficient_m != NEW.l_feedwater_resistance_coefficient_m OR OLD.l_feedwater_pipe_length_m != NEW.l_feedwater_pipe_length_m OR OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_friction_resistance_m=((NEW.l_feedwater_resistance_coefficient_m)*(((0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2))^2/2/(NEW.l_feedwater_msv_m))/((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))*(NEW.l_feedwater_pipe_length_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_length_m ISNULL OR OLD.l_feedwater_resistance_coefficient_m ISNULL OR OLD.l_feedwater_pipe_thickness_m ISNULL OR OLD.l_feedwater_pipe_outer_diameter_m ISNULL OR OLD.l_feedwater_msv_m ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_pipe_length_m NOTNULL AND NEW.l_feedwater_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_pipe_thickness_m NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.l_feedwater_msv_m NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_friction_resistance_m=((NEW.l_feedwater_resistance_coefficient_m)*(((0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2))^2/2/(NEW.l_feedwater_msv_m))/((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))*(NEW.l_feedwater_pipe_length_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_reynolds_m:雷诺数--低压给水母管,的计算57-----------------------------------
  IF OLD.l_feedwater_msv_m != NEW.l_feedwater_msv_m OR OLD.l_feedwater_pipe_outer_diameter_m != NEW.l_feedwater_pipe_outer_diameter_m OR OLD.l_feedwater_pipe_thickness_m != NEW.l_feedwater_pipe_thickness_m OR OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c OR OLD.l_feedwater_media_viscosity_c != NEW.l_feedwater_media_viscosity_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_reynolds_m=(0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2)*((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m))/((NEW.l_feedwater_media_viscosity_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_pipe_thickness_m ISNULL OR OLD.l_feedwater_pipe_outer_diameter_m ISNULL OR OLD.l_feedwater_msv_m ISNULL OR OLD.l_feedwater_media_viscosity_c ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_pipe_thickness_m NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.l_feedwater_msv_m NOTNULL AND NEW.l_feedwater_media_viscosity_c NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_reynolds_m=(0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2)*((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m))/((NEW.l_feedwater_media_viscosity_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_relative_roughness_m:相对粗糙度--低压给水母管,的计算58-----------------------------------
  IF OLD.l_feedwater_pipe_outer_diameter_m != NEW.l_feedwater_pipe_outer_diameter_m OR OLD.l_feedwater_pipe_thickness_m != NEW.l_feedwater_pipe_thickness_m OR OLD.l_feedwater_equivalent_roughness_m != NEW.l_feedwater_equivalent_roughness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_relative_roughness_m=(NEW.l_feedwater_equivalent_roughness_m)/((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_equivalent_roughness_m ISNULL OR OLD.l_feedwater_pipe_thickness_m ISNULL OR OLD.l_feedwater_pipe_outer_diameter_m ISNULL) AND NEW.l_feedwater_equivalent_roughness_m NOTNULL AND NEW.l_feedwater_pipe_thickness_m NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_relative_roughness_m=(NEW.l_feedwater_equivalent_roughness_m)/((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_unit_length_resistance_m:单位长度摩擦阻力--低压给水母管,的计算59-----------------------------------
  IF OLD.l_feedwater_msv_m != NEW.l_feedwater_msv_m OR OLD.l_feedwater_pipe_outer_diameter_m != NEW.l_feedwater_pipe_outer_diameter_m OR OLD.l_feedwater_pipe_thickness_m != NEW.l_feedwater_pipe_thickness_m OR OLD.l_feedwater_resistance_coefficient_m != NEW.l_feedwater_resistance_coefficient_m OR OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_unit_length_resistance_m=(NEW.l_feedwater_resistance_coefficient_m)*(((0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2))^2/2/(NEW.l_feedwater_msv_m))/((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_resistance_coefficient_m ISNULL OR OLD.l_feedwater_pipe_thickness_m ISNULL OR OLD.l_feedwater_pipe_outer_diameter_m ISNULL OR OLD.l_feedwater_msv_m ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_pipe_thickness_m NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.l_feedwater_msv_m NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_unit_length_resistance_m=(NEW.l_feedwater_resistance_coefficient_m)*(((0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2))^2/2/(NEW.l_feedwater_msv_m))/((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_local_resistance_m:局部阻力--低压给水母管,的计算60-----------------------------------
  IF OLD.l_feedwater_msv_m != NEW.l_feedwater_msv_m OR OLD.l_feedwater_pipe_outer_diameter_m != NEW.l_feedwater_pipe_outer_diameter_m OR OLD.l_feedwater_pipe_thickness_m != NEW.l_feedwater_pipe_thickness_m OR OLD.l_feedwater_resistance_coefficient_m != NEW.l_feedwater_resistance_coefficient_m OR OLD.l_feedwater_90elbow_resistance_coefficient_m != NEW.l_feedwater_90elbow_resistance_coefficient_m OR OLD.l_feedwater_90elbow_count_m != NEW.l_feedwater_90elbow_count_m OR OLD.l_feedwater_triplet_count_m != NEW.l_feedwater_triplet_count_m OR OLD.l_feedwater_reducer_resistance_coefficient_m != NEW.l_feedwater_reducer_resistance_coefficient_m OR OLD.l_feedwater_in_out_resistance_coefficient_m != NEW.l_feedwater_in_out_resistance_coefficient_m OR OLD.l_feedwater_filter_m != NEW.l_feedwater_filter_m OR OLD.l_feedwater_sluice_resistance_coefficient_m != NEW.l_feedwater_sluice_resistance_coefficient_m OR OLD.l_feedwater_check_resistance_coefficient_m != NEW.l_feedwater_check_resistance_coefficient_m OR OLD.l_feedwater_regulating_resistance_coefficient_m != NEW.l_feedwater_regulating_resistance_coefficient_m OR OLD.l_feedwater_plate_resistance_coefficient_m != NEW.l_feedwater_plate_resistance_coefficient_m OR OLD.l_feedwater_rated_flow_c != NEW.l_feedwater_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_local_resistance_m=(((NEW.l_feedwater_90elbow_count_m)*(NEW.l_feedwater_90elbow_resistance_coefficient_m))+((NEW.l_feedwater_triplet_count_m)*(20*(NEW.l_feedwater_resistance_coefficient_m)))+(NEW.l_feedwater_reducer_resistance_coefficient_m)+(NEW.l_feedwater_in_out_resistance_coefficient_m)+((NEW.l_feedwater_filter_m)+(NEW.l_feedwater_sluice_resistance_coefficient_m)+(NEW.l_feedwater_check_resistance_coefficient_m)+(NEW.l_feedwater_regulating_resistance_coefficient_m))+(NEW.l_feedwater_plate_resistance_coefficient_m))*(((0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2))^2/2/(NEW.l_feedwater_msv_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_plate_resistance_coefficient_m ISNULL OR OLD.l_feedwater_regulating_resistance_coefficient_m ISNULL OR OLD.l_feedwater_check_resistance_coefficient_m ISNULL OR OLD.l_feedwater_sluice_resistance_coefficient_m ISNULL OR OLD.l_feedwater_filter_m ISNULL OR OLD.l_feedwater_in_out_resistance_coefficient_m ISNULL OR OLD.l_feedwater_reducer_resistance_coefficient_m ISNULL OR OLD.l_feedwater_triplet_count_m ISNULL OR OLD.l_feedwater_90elbow_count_m ISNULL OR OLD.l_feedwater_90elbow_resistance_coefficient_m ISNULL OR OLD.l_feedwater_resistance_coefficient_m ISNULL OR OLD.l_feedwater_pipe_thickness_m ISNULL OR OLD.l_feedwater_pipe_outer_diameter_m ISNULL OR OLD.l_feedwater_msv_m ISNULL OR OLD.l_feedwater_rated_flow_c ISNULL) AND NEW.l_feedwater_plate_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_regulating_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_check_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_sluice_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_filter_m NOTNULL AND NEW.l_feedwater_in_out_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_reducer_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_triplet_count_m NOTNULL AND NEW.l_feedwater_90elbow_count_m NOTNULL AND NEW.l_feedwater_90elbow_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_pipe_thickness_m NOTNULL AND NEW.l_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.l_feedwater_msv_m NOTNULL AND NEW.l_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_local_resistance_m=(((NEW.l_feedwater_90elbow_count_m)*(NEW.l_feedwater_90elbow_resistance_coefficient_m))+((NEW.l_feedwater_triplet_count_m)*(20*(NEW.l_feedwater_resistance_coefficient_m)))+(NEW.l_feedwater_reducer_resistance_coefficient_m)+(NEW.l_feedwater_in_out_resistance_coefficient_m)+((NEW.l_feedwater_filter_m)+(NEW.l_feedwater_sluice_resistance_coefficient_m)+(NEW.l_feedwater_check_resistance_coefficient_m)+(NEW.l_feedwater_regulating_resistance_coefficient_m))+(NEW.l_feedwater_plate_resistance_coefficient_m))*(((0.3537*((NEW.l_feedwater_rated_flow_c)*4)*(NEW.l_feedwater_msv_m)/(((NEW.l_feedwater_pipe_outer_diameter_m)-2*(NEW.l_feedwater_pipe_thickness_m)))^2))^2/2/(NEW.l_feedwater_msv_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_total_local_resistance_coefficient_m:局部阻力系数合计--低压给水母管,的计算61-----------------------------------
  IF OLD.l_feedwater_resistance_coefficient_m != NEW.l_feedwater_resistance_coefficient_m OR OLD.l_feedwater_90elbow_resistance_coefficient_m != NEW.l_feedwater_90elbow_resistance_coefficient_m OR OLD.l_feedwater_90elbow_count_m != NEW.l_feedwater_90elbow_count_m OR OLD.l_feedwater_triplet_count_m != NEW.l_feedwater_triplet_count_m OR OLD.l_feedwater_reducer_resistance_coefficient_m != NEW.l_feedwater_reducer_resistance_coefficient_m OR OLD.l_feedwater_in_out_resistance_coefficient_m != NEW.l_feedwater_in_out_resistance_coefficient_m OR OLD.l_feedwater_filter_m != NEW.l_feedwater_filter_m OR OLD.l_feedwater_sluice_resistance_coefficient_m != NEW.l_feedwater_sluice_resistance_coefficient_m OR OLD.l_feedwater_check_resistance_coefficient_m != NEW.l_feedwater_check_resistance_coefficient_m OR OLD.l_feedwater_regulating_resistance_coefficient_m != NEW.l_feedwater_regulating_resistance_coefficient_m OR OLD.l_feedwater_plate_resistance_coefficient_m != NEW.l_feedwater_plate_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_total_local_resistance_coefficient_m=((NEW.l_feedwater_90elbow_count_m)*(NEW.l_feedwater_90elbow_resistance_coefficient_m))+((NEW.l_feedwater_triplet_count_m)*(20*(NEW.l_feedwater_resistance_coefficient_m)))+(NEW.l_feedwater_reducer_resistance_coefficient_m)+(NEW.l_feedwater_in_out_resistance_coefficient_m)+((NEW.l_feedwater_filter_m)+(NEW.l_feedwater_sluice_resistance_coefficient_m)+(NEW.l_feedwater_check_resistance_coefficient_m)+(NEW.l_feedwater_regulating_resistance_coefficient_m))+(NEW.l_feedwater_plate_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_plate_resistance_coefficient_m ISNULL OR OLD.l_feedwater_regulating_resistance_coefficient_m ISNULL OR OLD.l_feedwater_check_resistance_coefficient_m ISNULL OR OLD.l_feedwater_sluice_resistance_coefficient_m ISNULL OR OLD.l_feedwater_filter_m ISNULL OR OLD.l_feedwater_in_out_resistance_coefficient_m ISNULL OR OLD.l_feedwater_reducer_resistance_coefficient_m ISNULL OR OLD.l_feedwater_triplet_count_m ISNULL OR OLD.l_feedwater_90elbow_count_m ISNULL OR OLD.l_feedwater_90elbow_resistance_coefficient_m ISNULL OR OLD.l_feedwater_resistance_coefficient_m ISNULL) AND NEW.l_feedwater_plate_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_regulating_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_check_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_sluice_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_filter_m NOTNULL AND NEW.l_feedwater_in_out_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_reducer_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_triplet_count_m NOTNULL AND NEW.l_feedwater_90elbow_count_m NOTNULL AND NEW.l_feedwater_90elbow_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_total_local_resistance_coefficient_m=((NEW.l_feedwater_90elbow_count_m)*(NEW.l_feedwater_90elbow_resistance_coefficient_m))+((NEW.l_feedwater_triplet_count_m)*(20*(NEW.l_feedwater_resistance_coefficient_m)))+(NEW.l_feedwater_reducer_resistance_coefficient_m)+(NEW.l_feedwater_in_out_resistance_coefficient_m)+((NEW.l_feedwater_filter_m)+(NEW.l_feedwater_sluice_resistance_coefficient_m)+(NEW.l_feedwater_check_resistance_coefficient_m)+(NEW.l_feedwater_regulating_resistance_coefficient_m))+(NEW.l_feedwater_plate_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_elbow_resistance_coefficient_m:弯头阻力系数--低压给水母管,的计算62-----------------------------------
  IF OLD.l_feedwater_90elbow_resistance_coefficient_m != NEW.l_feedwater_90elbow_resistance_coefficient_m OR OLD.l_feedwater_90elbow_count_m != NEW.l_feedwater_90elbow_count_m THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_elbow_resistance_coefficient_m=(NEW.l_feedwater_90elbow_count_m)*(NEW.l_feedwater_90elbow_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_90elbow_count_m ISNULL OR OLD.l_feedwater_90elbow_resistance_coefficient_m ISNULL) AND NEW.l_feedwater_90elbow_count_m NOTNULL AND NEW.l_feedwater_90elbow_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_elbow_resistance_coefficient_m=(NEW.l_feedwater_90elbow_count_m)*(NEW.l_feedwater_90elbow_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_triplet_resistance_coefficient_m:三通阻力系数--低压给水母管,的计算63-----------------------------------
  IF OLD.l_feedwater_resistance_coefficient_m != NEW.l_feedwater_resistance_coefficient_m OR OLD.l_feedwater_triplet_count_m != NEW.l_feedwater_triplet_count_m THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_triplet_resistance_coefficient_m=(NEW.l_feedwater_triplet_count_m)*(20*(NEW.l_feedwater_resistance_coefficient_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_triplet_count_m ISNULL OR OLD.l_feedwater_resistance_coefficient_m ISNULL) AND NEW.l_feedwater_triplet_count_m NOTNULL AND NEW.l_feedwater_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_triplet_resistance_coefficient_m=(NEW.l_feedwater_triplet_count_m)*(20*(NEW.l_feedwater_resistance_coefficient_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_single_triplet_resistance_coefficient_m:单个三通阻力系数--低压给水母管,的计算64-----------------------------------
  IF OLD.l_feedwater_resistance_coefficient_m != NEW.l_feedwater_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_single_triplet_resistance_coefficient_m=20*(NEW.l_feedwater_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_resistance_coefficient_m ISNULL) AND NEW.l_feedwater_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_single_triplet_resistance_coefficient_m=20*(NEW.l_feedwater_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段l_feedwater_valve_resistance_coefficient_m:阀门的局部阻力系数--低压给水母管,的计算65-----------------------------------
  IF OLD.l_feedwater_filter_m != NEW.l_feedwater_filter_m OR OLD.l_feedwater_sluice_resistance_coefficient_m != NEW.l_feedwater_sluice_resistance_coefficient_m OR OLD.l_feedwater_check_resistance_coefficient_m != NEW.l_feedwater_check_resistance_coefficient_m OR OLD.l_feedwater_regulating_resistance_coefficient_m != NEW.l_feedwater_regulating_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_valve_resistance_coefficient_m=(NEW.l_feedwater_filter_m)+(NEW.l_feedwater_sluice_resistance_coefficient_m)+(NEW.l_feedwater_check_resistance_coefficient_m)+(NEW.l_feedwater_regulating_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_regulating_resistance_coefficient_m ISNULL OR OLD.l_feedwater_check_resistance_coefficient_m ISNULL OR OLD.l_feedwater_sluice_resistance_coefficient_m ISNULL OR OLD.l_feedwater_filter_m ISNULL) AND NEW.l_feedwater_regulating_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_check_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_sluice_resistance_coefficient_m NOTNULL AND NEW.l_feedwater_filter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     l_feedwater_valve_resistance_coefficient_m=(NEW.l_feedwater_filter_m)+(NEW.l_feedwater_sluice_resistance_coefficient_m)+(NEW.l_feedwater_check_resistance_coefficient_m)+(NEW.l_feedwater_regulating_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_work_press_c:运行压力(表压)--高压给水分管,的计算66-----------------------------------
  IF OLD.l_feedwater_work_press_c != NEW.l_feedwater_work_press_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_work_press_c=7.7+(NEW.l_feedwater_work_press_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_work_press_c ISNULL) AND NEW.l_feedwater_work_press_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_work_press_c=7.7+(NEW.l_feedwater_work_press_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_calculate_velocity_c:计算流速--高压给水分管,的计算67-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_c != NEW.h_feedwater_msv_c OR OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_calculate_velocity_c=0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL OR OLD.h_feedwater_msv_c ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.h_feedwater_msv_c NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_calculate_velocity_c=0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_dynamic_head_c:动压头--高压给水分管,的计算68-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_c != NEW.h_feedwater_msv_c OR OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_dynamic_head_c=((0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.h_feedwater_msv_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL OR OLD.h_feedwater_msv_c ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.h_feedwater_msv_c NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_dynamic_head_c=((0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.h_feedwater_msv_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_pipe_inner_diameter_c:内径--高压给水分管,的计算69-----------------------------------
  IF OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_pipe_inner_diameter_c=(NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL) AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_pipe_inner_diameter_c=(NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_friction_resistance_c:摩擦阻力--高压给水分管,的计算70-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_c != NEW.h_feedwater_msv_c OR OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c OR OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c OR OLD.h_feedwater_pipe_length_c != NEW.h_feedwater_pipe_length_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_friction_resistance_c=((NEW.h_feedwater_resistance_coefficient_c)*(((0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.h_feedwater_msv_c))/((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))*(NEW.h_feedwater_pipe_length_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_length_c ISNULL OR OLD.h_feedwater_resistance_coefficient_c ISNULL OR OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL OR OLD.h_feedwater_msv_c ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_pipe_length_c NOTNULL AND NEW.h_feedwater_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.h_feedwater_msv_c NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_friction_resistance_c=((NEW.h_feedwater_resistance_coefficient_c)*(((0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.h_feedwater_msv_c))/((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))*(NEW.h_feedwater_pipe_length_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_reynolds_c:雷诺数--高压给水分管,的计算71-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_c != NEW.h_feedwater_msv_c OR OLD.h_feedwater_media_viscosity_c != NEW.h_feedwater_media_viscosity_c OR OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_reynolds_c=(0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2)*((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c))/(NEW.h_feedwater_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL OR OLD.h_feedwater_media_viscosity_c ISNULL OR OLD.h_feedwater_msv_c ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.h_feedwater_media_viscosity_c NOTNULL AND NEW.h_feedwater_msv_c NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_reynolds_c=(0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2)*((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c))/(NEW.h_feedwater_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_relative_roughness_c:相对粗糙度--高压给水分管,的计算72-----------------------------------
  IF OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c OR OLD.h_feedwater_equivalent_roughness_c != NEW.h_feedwater_equivalent_roughness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_relative_roughness_c=(NEW.h_feedwater_equivalent_roughness_c)/((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_equivalent_roughness_c ISNULL OR OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL) AND NEW.h_feedwater_equivalent_roughness_c NOTNULL AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_relative_roughness_c=(NEW.h_feedwater_equivalent_roughness_c)/((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_unit_length_resistance_c:单位长度摩擦阻力--高压给水分管,的计算73-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_c != NEW.h_feedwater_msv_c OR OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c OR OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_unit_length_resistance_c=(NEW.h_feedwater_resistance_coefficient_c)*(((0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.h_feedwater_msv_c))/((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_resistance_coefficient_c ISNULL OR OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL OR OLD.h_feedwater_msv_c ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.h_feedwater_msv_c NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_unit_length_resistance_c=(NEW.h_feedwater_resistance_coefficient_c)*(((0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.h_feedwater_msv_c))/((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_local_resistance_c:局部阻力--高压给水分管,的计算74-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_c != NEW.h_feedwater_msv_c OR OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c OR OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c OR OLD.h_feedwater_90elbow_count_c != NEW.h_feedwater_90elbow_count_c OR OLD.h_feedwater_triplet_count_c != NEW.h_feedwater_triplet_count_c OR OLD.h_feedwater_increasing_angle_c != NEW.h_feedwater_increasing_angle_c OR OLD.h_feedwater_increasing_diameter_radio_c != NEW.h_feedwater_increasing_diameter_radio_c OR OLD.h_feedwater_in_out_resistance_coefficient_c != NEW.h_feedwater_in_out_resistance_coefficient_c OR OLD.h_feedwater_filter_c != NEW.h_feedwater_filter_c OR OLD.h_feedwater_sluice_count_c != NEW.h_feedwater_sluice_count_c OR OLD.h_feedwater_check_count_c != NEW.h_feedwater_check_count_c OR OLD.h_feedwater_regulating_resistance_coefficient_c != NEW.h_feedwater_regulating_resistance_coefficient_c OR OLD.h_feedwater_plate_resistance_coefficient_c != NEW.h_feedwater_plate_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_local_resistance_c=(((NEW.h_feedwater_90elbow_count_c)*(14*(NEW.h_feedwater_resistance_coefficient_c)))+((NEW.h_feedwater_triplet_count_c)*(60*(NEW.h_feedwater_resistance_coefficient_c)))+((2.6*sin((NEW.h_feedwater_increasing_angle_c)*3.14/180)*(1-((NEW.h_feedwater_increasing_diameter_radio_c))^2)^2/((NEW.h_feedwater_increasing_diameter_radio_c))^4))+(NEW.h_feedwater_in_out_resistance_coefficient_c)+((NEW.h_feedwater_filter_c)+((8*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_sluice_count_c))+((600*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_check_count_c))+(NEW.h_feedwater_regulating_resistance_coefficient_c))+(NEW.h_feedwater_plate_resistance_coefficient_c))*(((0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.h_feedwater_msv_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_plate_resistance_coefficient_c ISNULL OR OLD.h_feedwater_regulating_resistance_coefficient_c ISNULL OR OLD.h_feedwater_check_count_c ISNULL OR OLD.h_feedwater_sluice_count_c ISNULL OR OLD.h_feedwater_filter_c ISNULL OR OLD.h_feedwater_in_out_resistance_coefficient_c ISNULL OR OLD.h_feedwater_increasing_diameter_radio_c ISNULL OR OLD.h_feedwater_increasing_angle_c ISNULL OR OLD.h_feedwater_triplet_count_c ISNULL OR OLD.h_feedwater_90elbow_count_c ISNULL OR OLD.h_feedwater_resistance_coefficient_c ISNULL OR OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL OR OLD.h_feedwater_msv_c ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_plate_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_regulating_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_check_count_c NOTNULL AND NEW.h_feedwater_sluice_count_c NOTNULL AND NEW.h_feedwater_filter_c NOTNULL AND NEW.h_feedwater_in_out_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_increasing_diameter_radio_c NOTNULL AND NEW.h_feedwater_increasing_angle_c NOTNULL AND NEW.h_feedwater_triplet_count_c NOTNULL AND NEW.h_feedwater_90elbow_count_c NOTNULL AND NEW.h_feedwater_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL AND NEW.h_feedwater_msv_c NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_local_resistance_c=(((NEW.h_feedwater_90elbow_count_c)*(14*(NEW.h_feedwater_resistance_coefficient_c)))+((NEW.h_feedwater_triplet_count_c)*(60*(NEW.h_feedwater_resistance_coefficient_c)))+((2.6*sin((NEW.h_feedwater_increasing_angle_c)*3.14/180)*(1-((NEW.h_feedwater_increasing_diameter_radio_c))^2)^2/((NEW.h_feedwater_increasing_diameter_radio_c))^4))+(NEW.h_feedwater_in_out_resistance_coefficient_c)+((NEW.h_feedwater_filter_c)+((8*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_sluice_count_c))+((600*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_check_count_c))+(NEW.h_feedwater_regulating_resistance_coefficient_c))+(NEW.h_feedwater_plate_resistance_coefficient_c))*(((0.3537*(NEW.h_feedwater_rated_flow_c)*(NEW.h_feedwater_msv_c)/(((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c)))^2))^2/2/(NEW.h_feedwater_msv_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_total_local_resistance_coefficient_c:局部阻力系数合计--高压给水分管,的计算75-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c OR OLD.h_feedwater_90elbow_count_c != NEW.h_feedwater_90elbow_count_c OR OLD.h_feedwater_triplet_count_c != NEW.h_feedwater_triplet_count_c OR OLD.h_feedwater_increasing_angle_c != NEW.h_feedwater_increasing_angle_c OR OLD.h_feedwater_increasing_diameter_radio_c != NEW.h_feedwater_increasing_diameter_radio_c OR OLD.h_feedwater_in_out_resistance_coefficient_c != NEW.h_feedwater_in_out_resistance_coefficient_c OR OLD.h_feedwater_filter_c != NEW.h_feedwater_filter_c OR OLD.h_feedwater_sluice_count_c != NEW.h_feedwater_sluice_count_c OR OLD.h_feedwater_check_count_c != NEW.h_feedwater_check_count_c OR OLD.h_feedwater_regulating_resistance_coefficient_c != NEW.h_feedwater_regulating_resistance_coefficient_c OR OLD.h_feedwater_plate_resistance_coefficient_c != NEW.h_feedwater_plate_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_total_local_resistance_coefficient_c=((NEW.h_feedwater_90elbow_count_c)*(14*(NEW.h_feedwater_resistance_coefficient_c)))+((NEW.h_feedwater_triplet_count_c)*(60*(NEW.h_feedwater_resistance_coefficient_c)))+((2.6*sin((NEW.h_feedwater_increasing_angle_c)*3.14/180)*(1-((NEW.h_feedwater_increasing_diameter_radio_c))^2)^2/((NEW.h_feedwater_increasing_diameter_radio_c))^4))+(NEW.h_feedwater_in_out_resistance_coefficient_c)+((NEW.h_feedwater_filter_c)+((8*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_sluice_count_c))+((600*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_check_count_c))+(NEW.h_feedwater_regulating_resistance_coefficient_c))+(NEW.h_feedwater_plate_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_plate_resistance_coefficient_c ISNULL OR OLD.h_feedwater_regulating_resistance_coefficient_c ISNULL OR OLD.h_feedwater_check_count_c ISNULL OR OLD.h_feedwater_sluice_count_c ISNULL OR OLD.h_feedwater_filter_c ISNULL OR OLD.h_feedwater_in_out_resistance_coefficient_c ISNULL OR OLD.h_feedwater_increasing_diameter_radio_c ISNULL OR OLD.h_feedwater_increasing_angle_c ISNULL OR OLD.h_feedwater_triplet_count_c ISNULL OR OLD.h_feedwater_90elbow_count_c ISNULL OR OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_plate_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_regulating_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_check_count_c NOTNULL AND NEW.h_feedwater_sluice_count_c NOTNULL AND NEW.h_feedwater_filter_c NOTNULL AND NEW.h_feedwater_in_out_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_increasing_diameter_radio_c NOTNULL AND NEW.h_feedwater_increasing_angle_c NOTNULL AND NEW.h_feedwater_triplet_count_c NOTNULL AND NEW.h_feedwater_90elbow_count_c NOTNULL AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_total_local_resistance_coefficient_c=((NEW.h_feedwater_90elbow_count_c)*(14*(NEW.h_feedwater_resistance_coefficient_c)))+((NEW.h_feedwater_triplet_count_c)*(60*(NEW.h_feedwater_resistance_coefficient_c)))+((2.6*sin((NEW.h_feedwater_increasing_angle_c)*3.14/180)*(1-((NEW.h_feedwater_increasing_diameter_radio_c))^2)^2/((NEW.h_feedwater_increasing_diameter_radio_c))^4))+(NEW.h_feedwater_in_out_resistance_coefficient_c)+((NEW.h_feedwater_filter_c)+((8*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_sluice_count_c))+((600*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_check_count_c))+(NEW.h_feedwater_regulating_resistance_coefficient_c))+(NEW.h_feedwater_plate_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_elbow_resistance_coefficient_c:弯头阻力系数--高压给水分管,的计算76-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c OR OLD.h_feedwater_90elbow_count_c != NEW.h_feedwater_90elbow_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_elbow_resistance_coefficient_c=(NEW.h_feedwater_90elbow_count_c)*(14*(NEW.h_feedwater_resistance_coefficient_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_90elbow_count_c ISNULL OR OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_90elbow_count_c NOTNULL AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_elbow_resistance_coefficient_c=(NEW.h_feedwater_90elbow_count_c)*(14*(NEW.h_feedwater_resistance_coefficient_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_elbow_radius_to_inner_diameter_c:弯头半径/内径--高压给水分管,的计算77-----------------------------------
  IF OLD.h_feedwater_pipe_outer_diameter_c != NEW.h_feedwater_pipe_outer_diameter_c OR OLD.h_feedwater_pipe_thickness_c != NEW.h_feedwater_pipe_thickness_c OR OLD.h_feedwater_elbow_radius_c != NEW.h_feedwater_elbow_radius_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_elbow_radius_to_inner_diameter_c=(NEW.h_feedwater_elbow_radius_c)/((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_elbow_radius_c ISNULL OR OLD.h_feedwater_pipe_thickness_c ISNULL OR OLD.h_feedwater_pipe_outer_diameter_c ISNULL) AND NEW.h_feedwater_elbow_radius_c NOTNULL AND NEW.h_feedwater_pipe_thickness_c NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_elbow_radius_to_inner_diameter_c=(NEW.h_feedwater_elbow_radius_c)/((NEW.h_feedwater_pipe_outer_diameter_c)-2*(NEW.h_feedwater_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_90elbow_resistance_coefficient_c:单个90º弯头阻力系数--高压给水分管,的计算78-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_90elbow_resistance_coefficient_c=14*(NEW.h_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_90elbow_resistance_coefficient_c=14*(NEW.h_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_triplet_resistance_coefficient_c:三通阻力系数--高压给水分管,的计算79-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c OR OLD.h_feedwater_triplet_count_c != NEW.h_feedwater_triplet_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_triplet_resistance_coefficient_c=(NEW.h_feedwater_triplet_count_c)*(60*(NEW.h_feedwater_resistance_coefficient_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_triplet_count_c ISNULL OR OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_triplet_count_c NOTNULL AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_triplet_resistance_coefficient_c=(NEW.h_feedwater_triplet_count_c)*(60*(NEW.h_feedwater_resistance_coefficient_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_single_triplet_resistance_coefficient_c:单个三通阻力系数--高压给水分管,的计算80-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_single_triplet_resistance_coefficient_c=60*(NEW.h_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_single_triplet_resistance_coefficient_c=60*(NEW.h_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_reducer_resistance_coefficient_c:异径管的阻力系数--高压给水分管,的计算81-----------------------------------
  IF OLD.h_feedwater_increasing_angle_c != NEW.h_feedwater_increasing_angle_c OR OLD.h_feedwater_increasing_diameter_radio_c != NEW.h_feedwater_increasing_diameter_radio_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_reducer_resistance_coefficient_c=(2.6*sin((NEW.h_feedwater_increasing_angle_c)*3.14/180)*(1-((NEW.h_feedwater_increasing_diameter_radio_c))^2)^2/((NEW.h_feedwater_increasing_diameter_radio_c))^4)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_increasing_diameter_radio_c ISNULL OR OLD.h_feedwater_increasing_angle_c ISNULL) AND NEW.h_feedwater_increasing_diameter_radio_c NOTNULL AND NEW.h_feedwater_increasing_angle_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_reducer_resistance_coefficient_c=(2.6*sin((NEW.h_feedwater_increasing_angle_c)*3.14/180)*(1-((NEW.h_feedwater_increasing_diameter_radio_c))^2)^2/((NEW.h_feedwater_increasing_diameter_radio_c))^4)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_increasing_resistance_coefficient_c:渐扩管（相应于大管径的阻力系数）--高压给水分管,的计算82-----------------------------------
  IF OLD.h_feedwater_increasing_angle_c != NEW.h_feedwater_increasing_angle_c OR OLD.h_feedwater_increasing_diameter_radio_c != NEW.h_feedwater_increasing_diameter_radio_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_increasing_resistance_coefficient_c=2.6*sin((NEW.h_feedwater_increasing_angle_c)*3.14/180)*(1-((NEW.h_feedwater_increasing_diameter_radio_c))^2)^2/((NEW.h_feedwater_increasing_diameter_radio_c))^4
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_increasing_diameter_radio_c ISNULL OR OLD.h_feedwater_increasing_angle_c ISNULL) AND NEW.h_feedwater_increasing_diameter_radio_c NOTNULL AND NEW.h_feedwater_increasing_angle_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_increasing_resistance_coefficient_c=2.6*sin((NEW.h_feedwater_increasing_angle_c)*3.14/180)*(1-((NEW.h_feedwater_increasing_diameter_radio_c))^2)^2/((NEW.h_feedwater_increasing_diameter_radio_c))^4
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_valve_resistance_coefficient_c:阀门的局部阻力系数--高压给水分管,的计算83-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c OR OLD.h_feedwater_filter_c != NEW.h_feedwater_filter_c OR OLD.h_feedwater_sluice_count_c != NEW.h_feedwater_sluice_count_c OR OLD.h_feedwater_check_count_c != NEW.h_feedwater_check_count_c OR OLD.h_feedwater_regulating_resistance_coefficient_c != NEW.h_feedwater_regulating_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_valve_resistance_coefficient_c=(NEW.h_feedwater_filter_c)+((8*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_sluice_count_c))+((600*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_check_count_c))+(NEW.h_feedwater_regulating_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_regulating_resistance_coefficient_c ISNULL OR OLD.h_feedwater_check_count_c ISNULL OR OLD.h_feedwater_sluice_count_c ISNULL OR OLD.h_feedwater_filter_c ISNULL OR OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_regulating_resistance_coefficient_c NOTNULL AND NEW.h_feedwater_check_count_c NOTNULL AND NEW.h_feedwater_sluice_count_c NOTNULL AND NEW.h_feedwater_filter_c NOTNULL AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_valve_resistance_coefficient_c=(NEW.h_feedwater_filter_c)+((8*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_sluice_count_c))+((600*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_check_count_c))+(NEW.h_feedwater_regulating_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_sluice_resistance_coefficient_c:闸阀阻力系数--高压给水分管,的计算84-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c OR OLD.h_feedwater_sluice_count_c != NEW.h_feedwater_sluice_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_sluice_resistance_coefficient_c=(8*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_sluice_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_sluice_count_c ISNULL OR OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_sluice_count_c NOTNULL AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_sluice_resistance_coefficient_c=(8*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_sluice_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_single_sluice_resistance_coefficient_c:单个闸阀阻力系数--高压给水分管,的计算85-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_single_sluice_resistance_coefficient_c=8*(NEW.h_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_single_sluice_resistance_coefficient_c=8*(NEW.h_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_check_resistance_coefficient_c:止回阀阻力系数--高压给水分管,的计算86-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c OR OLD.h_feedwater_check_count_c != NEW.h_feedwater_check_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_check_resistance_coefficient_c=(600*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_check_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_check_count_c ISNULL OR OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_check_count_c NOTNULL AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_check_resistance_coefficient_c=(600*(NEW.h_feedwater_resistance_coefficient_c))*(NEW.h_feedwater_check_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_single_check_resistance_coefficient_c:单个止回阀阻力系数--高压给水分管,的计算87-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_c != NEW.h_feedwater_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_single_check_resistance_coefficient_c=600*(NEW.h_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_resistance_coefficient_c ISNULL) AND NEW.h_feedwater_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_single_check_resistance_coefficient_c=600*(NEW.h_feedwater_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_work_press_m:运行压力(表压)--高压给水母管,的计算88-----------------------------------
  IF OLD.l_feedwater_work_press_m != NEW.l_feedwater_work_press_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_work_press_m=7.7+(NEW.l_feedwater_work_press_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.l_feedwater_work_press_m ISNULL) AND NEW.l_feedwater_work_press_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_work_press_m=7.7+(NEW.l_feedwater_work_press_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_rated_flow_m:额定流量--高压给水母管,的计算89-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_rated_flow_m=(NEW.h_feedwater_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_rated_flow_m=(NEW.h_feedwater_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_media_viscosity_m:介质运动粘度--高压给水母管,的计算90-----------------------------------
  IF OLD.h_feedwater_media_viscosity_c != NEW.h_feedwater_media_viscosity_c THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_media_viscosity_m=(NEW.h_feedwater_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_media_viscosity_c ISNULL) AND NEW.h_feedwater_media_viscosity_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_media_viscosity_m=(NEW.h_feedwater_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_calculate_velocity_m:计算流速--高压给水母管,的计算91-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_m != NEW.h_feedwater_msv_m OR OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_calculate_velocity_m=0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL OR OLD.h_feedwater_msv_m ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.h_feedwater_msv_m NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_calculate_velocity_m=0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_dynamic_head_m:动压头--高压给水母管,的计算92-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_m != NEW.h_feedwater_msv_m OR OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_dynamic_head_m=((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL OR OLD.h_feedwater_msv_m ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.h_feedwater_msv_m NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_dynamic_head_m=((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_pipe_inner_diameter_m:内径--高压给水母管,的计算93-----------------------------------
  IF OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_pipe_inner_diameter_m=(NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL) AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_pipe_inner_diameter_m=(NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_friction_resistance_m:摩擦阻力--高压给水母管,的计算94-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_m != NEW.h_feedwater_msv_m OR OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m OR OLD.h_feedwater_resistance_coefficient_m != NEW.h_feedwater_resistance_coefficient_m OR OLD.h_feedwater_pipe_length_m != NEW.h_feedwater_pipe_length_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_friction_resistance_m=((NEW.h_feedwater_resistance_coefficient_m)*(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))/((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))*(NEW.h_feedwater_pipe_length_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_length_m ISNULL OR OLD.h_feedwater_resistance_coefficient_m ISNULL OR OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL OR OLD.h_feedwater_msv_m ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_pipe_length_m NOTNULL AND NEW.h_feedwater_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.h_feedwater_msv_m NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_friction_resistance_m=((NEW.h_feedwater_resistance_coefficient_m)*(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))/((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))*(NEW.h_feedwater_pipe_length_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_reynolds_m:雷诺数--高压给水母管,的计算95-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_media_viscosity_c != NEW.h_feedwater_media_viscosity_c OR OLD.h_feedwater_msv_m != NEW.h_feedwater_msv_m OR OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_reynolds_m=(0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2)*((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m)))/((NEW.h_feedwater_media_viscosity_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL OR OLD.h_feedwater_msv_m ISNULL OR OLD.h_feedwater_media_viscosity_c ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.h_feedwater_msv_m NOTNULL AND NEW.h_feedwater_media_viscosity_c NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_reynolds_m=(0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2)*((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m)))/((NEW.h_feedwater_media_viscosity_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_relative_roughness_m:相对粗糙度--高压给水母管,的计算96-----------------------------------
  IF OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m OR OLD.h_feedwater_equivalent_roughness_m != NEW.h_feedwater_equivalent_roughness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_relative_roughness_m=(NEW.h_feedwater_equivalent_roughness_m)/((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m)))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_equivalent_roughness_m ISNULL OR OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL) AND NEW.h_feedwater_equivalent_roughness_m NOTNULL AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_relative_roughness_m=(NEW.h_feedwater_equivalent_roughness_m)/((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m)))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_unit_length_resistance_m:单位长度摩擦阻力--高压给水母管,的计算97-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_m != NEW.h_feedwater_msv_m OR OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m OR OLD.h_feedwater_resistance_coefficient_m != NEW.h_feedwater_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_unit_length_resistance_m=(NEW.h_feedwater_resistance_coefficient_m)*(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))/((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_resistance_coefficient_m ISNULL OR OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL OR OLD.h_feedwater_msv_m ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.h_feedwater_msv_m NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_unit_length_resistance_m=(NEW.h_feedwater_resistance_coefficient_m)*(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))/((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_local_resistance_m:局部阻力--高压给水母管,的计算98-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_m != NEW.h_feedwater_msv_m OR OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m OR OLD.h_feedwater_resistance_coefficient_m != NEW.h_feedwater_resistance_coefficient_m OR OLD.h_feedwater_90elbow_resistance_coefficient_m != NEW.h_feedwater_90elbow_resistance_coefficient_m OR OLD.h_feedwater_90elbow_count_m != NEW.h_feedwater_90elbow_count_m OR OLD.h_feedwater_triplet_count_m != NEW.h_feedwater_triplet_count_m OR OLD.h_feedwater_reducer_resistance_coefficient_m != NEW.h_feedwater_reducer_resistance_coefficient_m OR OLD.h_feedwater_in_out_resistance_coefficient_m != NEW.h_feedwater_in_out_resistance_coefficient_m OR OLD.h_feedwater_filter_m != NEW.h_feedwater_filter_m OR OLD.h_feedwater_sluice_resistance_coefficient_m != NEW.h_feedwater_sluice_resistance_coefficient_m OR OLD.h_feedwater_check_resistance_coefficient_m != NEW.h_feedwater_check_resistance_coefficient_m OR OLD.h_feedwater_regulating_resistance_coefficient_m != NEW.h_feedwater_regulating_resistance_coefficient_m OR OLD.h_feedwater_measuring_pressure_loss_m != NEW.h_feedwater_measuring_pressure_loss_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_local_resistance_m=(((NEW.h_feedwater_90elbow_count_m)*(NEW.h_feedwater_90elbow_resistance_coefficient_m))+((NEW.h_feedwater_triplet_count_m)*(20*(NEW.h_feedwater_resistance_coefficient_m)))+(NEW.h_feedwater_reducer_resistance_coefficient_m)+(NEW.h_feedwater_in_out_resistance_coefficient_m)+((NEW.h_feedwater_filter_m)+(NEW.h_feedwater_sluice_resistance_coefficient_m)+(NEW.h_feedwater_check_resistance_coefficient_m)+(NEW.h_feedwater_regulating_resistance_coefficient_m))+((NEW.h_feedwater_measuring_pressure_loss_m)/(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))))*(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_measuring_pressure_loss_m ISNULL OR OLD.h_feedwater_regulating_resistance_coefficient_m ISNULL OR OLD.h_feedwater_check_resistance_coefficient_m ISNULL OR OLD.h_feedwater_sluice_resistance_coefficient_m ISNULL OR OLD.h_feedwater_filter_m ISNULL OR OLD.h_feedwater_in_out_resistance_coefficient_m ISNULL OR OLD.h_feedwater_reducer_resistance_coefficient_m ISNULL OR OLD.h_feedwater_triplet_count_m ISNULL OR OLD.h_feedwater_90elbow_count_m ISNULL OR OLD.h_feedwater_90elbow_resistance_coefficient_m ISNULL OR OLD.h_feedwater_resistance_coefficient_m ISNULL OR OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL OR OLD.h_feedwater_msv_m ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_measuring_pressure_loss_m NOTNULL AND NEW.h_feedwater_regulating_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_check_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_sluice_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_filter_m NOTNULL AND NEW.h_feedwater_in_out_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_reducer_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_triplet_count_m NOTNULL AND NEW.h_feedwater_90elbow_count_m NOTNULL AND NEW.h_feedwater_90elbow_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.h_feedwater_msv_m NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_local_resistance_m=(((NEW.h_feedwater_90elbow_count_m)*(NEW.h_feedwater_90elbow_resistance_coefficient_m))+((NEW.h_feedwater_triplet_count_m)*(20*(NEW.h_feedwater_resistance_coefficient_m)))+(NEW.h_feedwater_reducer_resistance_coefficient_m)+(NEW.h_feedwater_in_out_resistance_coefficient_m)+((NEW.h_feedwater_filter_m)+(NEW.h_feedwater_sluice_resistance_coefficient_m)+(NEW.h_feedwater_check_resistance_coefficient_m)+(NEW.h_feedwater_regulating_resistance_coefficient_m))+((NEW.h_feedwater_measuring_pressure_loss_m)/(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))))*(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_total_local_resistance_coefficient_m:局部阻力系数合计--高压给水母管,的计算99-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_m != NEW.h_feedwater_msv_m OR OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m OR OLD.h_feedwater_resistance_coefficient_m != NEW.h_feedwater_resistance_coefficient_m OR OLD.h_feedwater_90elbow_resistance_coefficient_m != NEW.h_feedwater_90elbow_resistance_coefficient_m OR OLD.h_feedwater_90elbow_count_m != NEW.h_feedwater_90elbow_count_m OR OLD.h_feedwater_triplet_count_m != NEW.h_feedwater_triplet_count_m OR OLD.h_feedwater_reducer_resistance_coefficient_m != NEW.h_feedwater_reducer_resistance_coefficient_m OR OLD.h_feedwater_in_out_resistance_coefficient_m != NEW.h_feedwater_in_out_resistance_coefficient_m OR OLD.h_feedwater_filter_m != NEW.h_feedwater_filter_m OR OLD.h_feedwater_sluice_resistance_coefficient_m != NEW.h_feedwater_sluice_resistance_coefficient_m OR OLD.h_feedwater_check_resistance_coefficient_m != NEW.h_feedwater_check_resistance_coefficient_m OR OLD.h_feedwater_regulating_resistance_coefficient_m != NEW.h_feedwater_regulating_resistance_coefficient_m OR OLD.h_feedwater_measuring_pressure_loss_m != NEW.h_feedwater_measuring_pressure_loss_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_total_local_resistance_coefficient_m=((NEW.h_feedwater_90elbow_count_m)*(NEW.h_feedwater_90elbow_resistance_coefficient_m))+((NEW.h_feedwater_triplet_count_m)*(20*(NEW.h_feedwater_resistance_coefficient_m)))+(NEW.h_feedwater_reducer_resistance_coefficient_m)+(NEW.h_feedwater_in_out_resistance_coefficient_m)+((NEW.h_feedwater_filter_m)+(NEW.h_feedwater_sluice_resistance_coefficient_m)+(NEW.h_feedwater_check_resistance_coefficient_m)+(NEW.h_feedwater_regulating_resistance_coefficient_m))+((NEW.h_feedwater_measuring_pressure_loss_m)/(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_measuring_pressure_loss_m ISNULL OR OLD.h_feedwater_regulating_resistance_coefficient_m ISNULL OR OLD.h_feedwater_check_resistance_coefficient_m ISNULL OR OLD.h_feedwater_sluice_resistance_coefficient_m ISNULL OR OLD.h_feedwater_filter_m ISNULL OR OLD.h_feedwater_in_out_resistance_coefficient_m ISNULL OR OLD.h_feedwater_reducer_resistance_coefficient_m ISNULL OR OLD.h_feedwater_triplet_count_m ISNULL OR OLD.h_feedwater_90elbow_count_m ISNULL OR OLD.h_feedwater_90elbow_resistance_coefficient_m ISNULL OR OLD.h_feedwater_resistance_coefficient_m ISNULL OR OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL OR OLD.h_feedwater_msv_m ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_measuring_pressure_loss_m NOTNULL AND NEW.h_feedwater_regulating_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_check_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_sluice_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_filter_m NOTNULL AND NEW.h_feedwater_in_out_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_reducer_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_triplet_count_m NOTNULL AND NEW.h_feedwater_90elbow_count_m NOTNULL AND NEW.h_feedwater_90elbow_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.h_feedwater_msv_m NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_total_local_resistance_coefficient_m=((NEW.h_feedwater_90elbow_count_m)*(NEW.h_feedwater_90elbow_resistance_coefficient_m))+((NEW.h_feedwater_triplet_count_m)*(20*(NEW.h_feedwater_resistance_coefficient_m)))+(NEW.h_feedwater_reducer_resistance_coefficient_m)+(NEW.h_feedwater_in_out_resistance_coefficient_m)+((NEW.h_feedwater_filter_m)+(NEW.h_feedwater_sluice_resistance_coefficient_m)+(NEW.h_feedwater_check_resistance_coefficient_m)+(NEW.h_feedwater_regulating_resistance_coefficient_m))+((NEW.h_feedwater_measuring_pressure_loss_m)/(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_elbow_resistance_coefficient_m:弯头阻力系数--高压给水母管,的计算100-----------------------------------
  IF OLD.h_feedwater_90elbow_resistance_coefficient_m != NEW.h_feedwater_90elbow_resistance_coefficient_m OR OLD.h_feedwater_90elbow_count_m != NEW.h_feedwater_90elbow_count_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_elbow_resistance_coefficient_m=(NEW.h_feedwater_90elbow_count_m)*(NEW.h_feedwater_90elbow_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_90elbow_count_m ISNULL OR OLD.h_feedwater_90elbow_resistance_coefficient_m ISNULL) AND NEW.h_feedwater_90elbow_count_m NOTNULL AND NEW.h_feedwater_90elbow_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_elbow_resistance_coefficient_m=(NEW.h_feedwater_90elbow_count_m)*(NEW.h_feedwater_90elbow_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_triplet_resistance_coefficient_m:三通阻力系数--高压给水母管,的计算101-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_m != NEW.h_feedwater_resistance_coefficient_m OR OLD.h_feedwater_triplet_count_m != NEW.h_feedwater_triplet_count_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_triplet_resistance_coefficient_m=(NEW.h_feedwater_triplet_count_m)*(20*(NEW.h_feedwater_resistance_coefficient_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_triplet_count_m ISNULL OR OLD.h_feedwater_resistance_coefficient_m ISNULL) AND NEW.h_feedwater_triplet_count_m NOTNULL AND NEW.h_feedwater_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_triplet_resistance_coefficient_m=(NEW.h_feedwater_triplet_count_m)*(20*(NEW.h_feedwater_resistance_coefficient_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_single_triplet_resistance_coefficient_m:单个三通阻力系数--高压给水母管,的计算102-----------------------------------
  IF OLD.h_feedwater_resistance_coefficient_m != NEW.h_feedwater_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_single_triplet_resistance_coefficient_m=20*(NEW.h_feedwater_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_resistance_coefficient_m ISNULL) AND NEW.h_feedwater_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_single_triplet_resistance_coefficient_m=20*(NEW.h_feedwater_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_valve_resistance_coefficient_m:阀门的局部阻力系数--高压给水母管,的计算103-----------------------------------
  IF OLD.h_feedwater_filter_m != NEW.h_feedwater_filter_m OR OLD.h_feedwater_sluice_resistance_coefficient_m != NEW.h_feedwater_sluice_resistance_coefficient_m OR OLD.h_feedwater_check_resistance_coefficient_m != NEW.h_feedwater_check_resistance_coefficient_m OR OLD.h_feedwater_regulating_resistance_coefficient_m != NEW.h_feedwater_regulating_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_valve_resistance_coefficient_m=(NEW.h_feedwater_filter_m)+(NEW.h_feedwater_sluice_resistance_coefficient_m)+(NEW.h_feedwater_check_resistance_coefficient_m)+(NEW.h_feedwater_regulating_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_regulating_resistance_coefficient_m ISNULL OR OLD.h_feedwater_check_resistance_coefficient_m ISNULL OR OLD.h_feedwater_sluice_resistance_coefficient_m ISNULL OR OLD.h_feedwater_filter_m ISNULL) AND NEW.h_feedwater_regulating_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_check_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_sluice_resistance_coefficient_m NOTNULL AND NEW.h_feedwater_filter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_valve_resistance_coefficient_m=(NEW.h_feedwater_filter_m)+(NEW.h_feedwater_sluice_resistance_coefficient_m)+(NEW.h_feedwater_check_resistance_coefficient_m)+(NEW.h_feedwater_regulating_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_feedwater_plate_resistance_coefficient_m:流量测量孔板阻力系数--高压给水母管,的计算104-----------------------------------
  IF OLD.h_feedwater_rated_flow_c != NEW.h_feedwater_rated_flow_c OR OLD.h_feedwater_msv_m != NEW.h_feedwater_msv_m OR OLD.h_feedwater_pipe_outer_diameter_m != NEW.h_feedwater_pipe_outer_diameter_m OR OLD.h_feedwater_pipe_thickness_m != NEW.h_feedwater_pipe_thickness_m OR OLD.h_feedwater_measuring_pressure_loss_m != NEW.h_feedwater_measuring_pressure_loss_m THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_plate_resistance_coefficient_m=(NEW.h_feedwater_measuring_pressure_loss_m)/(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.h_feedwater_measuring_pressure_loss_m ISNULL OR OLD.h_feedwater_pipe_thickness_m ISNULL OR OLD.h_feedwater_pipe_outer_diameter_m ISNULL OR OLD.h_feedwater_msv_m ISNULL OR OLD.h_feedwater_rated_flow_c ISNULL) AND NEW.h_feedwater_measuring_pressure_loss_m NOTNULL AND NEW.h_feedwater_pipe_thickness_m NOTNULL AND NEW.h_feedwater_pipe_outer_diameter_m NOTNULL AND NEW.h_feedwater_msv_m NOTNULL AND NEW.h_feedwater_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     h_feedwater_plate_resistance_coefficient_m=(NEW.h_feedwater_measuring_pressure_loss_m)/(((0.3537*((NEW.h_feedwater_rated_flow_c)*4)*(NEW.h_feedwater_msv_m)/(((NEW.h_feedwater_pipe_outer_diameter_m)-(2*(NEW.h_feedwater_pipe_thickness_m))))^2))^2/2/(NEW.h_feedwater_msv_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_calculate_velocity_c:计算流速--凝泵入口分管,的计算105-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_calculate_velocity_c=0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL OR OLD.pump_in_msv_c ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL AND NEW.pump_in_msv_c NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_calculate_velocity_c=0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_dynamic_head_c:动压头--凝泵入口分管,的计算106-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_dynamic_head_c=((0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2))^2/2/(NEW.pump_in_msv_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL OR OLD.pump_in_msv_c ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL AND NEW.pump_in_msv_c NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_dynamic_head_c=((0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2))^2/2/(NEW.pump_in_msv_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_pipe_inner_diameter_c:内径--凝泵入口分管,的计算107-----------------------------------
  IF OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_pipe_inner_diameter_c=(NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL) AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_pipe_inner_diameter_c=(NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_friction_resistance_c:摩擦阻力--凝泵入口分管,的计算108-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c OR OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c OR OLD.pump_in_pipe_length_c != NEW.pump_in_pipe_length_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_friction_resistance_c=(NEW.pump_in_pipe_length_c)*((NEW.pump_in_resistance_coefficient_c)*(((0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2))^2/2/(NEW.pump_in_msv_c))/((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_length_c ISNULL OR OLD.pump_in_resistance_coefficient_c ISNULL OR OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL OR OLD.pump_in_msv_c ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_pipe_length_c NOTNULL AND NEW.pump_in_resistance_coefficient_c NOTNULL AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL AND NEW.pump_in_msv_c NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_friction_resistance_c=(NEW.pump_in_pipe_length_c)*((NEW.pump_in_resistance_coefficient_c)*(((0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2))^2/2/(NEW.pump_in_msv_c))/((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_reynolds_c:雷诺数--凝泵入口分管,的计算109-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_in_media_viscosity_c != NEW.pump_in_media_viscosity_c OR OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_reynolds_c=(0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2)*((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c))/(NEW.pump_in_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL OR OLD.pump_in_media_viscosity_c ISNULL OR OLD.pump_in_msv_c ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL AND NEW.pump_in_media_viscosity_c NOTNULL AND NEW.pump_in_msv_c NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_reynolds_c=(0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2)*((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c))/(NEW.pump_in_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_relative_roughness_c:相对粗糙度--凝泵入口分管,的计算110-----------------------------------
  IF OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c OR OLD.pump_in_equivalent_roughness_c != NEW.pump_in_equivalent_roughness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_relative_roughness_c=(NEW.pump_in_equivalent_roughness_c)/((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_equivalent_roughness_c ISNULL OR OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL) AND NEW.pump_in_equivalent_roughness_c NOTNULL AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_relative_roughness_c=(NEW.pump_in_equivalent_roughness_c)/((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_unit_length_resistance_c:单位长度摩擦阻力--凝泵入口分管,的计算111-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c OR OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_unit_length_resistance_c=(NEW.pump_in_resistance_coefficient_c)*(((0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2))^2/2/(NEW.pump_in_msv_c))/((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_resistance_coefficient_c ISNULL OR OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL OR OLD.pump_in_msv_c ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_resistance_coefficient_c NOTNULL AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL AND NEW.pump_in_msv_c NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_unit_length_resistance_c=(NEW.pump_in_resistance_coefficient_c)*(((0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2))^2/2/(NEW.pump_in_msv_c))/((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_local_resistance_c:局部阻力--凝泵入口分管,的计算112-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c OR OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c OR OLD.pump_in_90elbow_count_c != NEW.pump_in_90elbow_count_c OR OLD.pump_in_triplet_count_c != NEW.pump_in_triplet_count_c OR OLD.pump_in_converging_angle_c != NEW.pump_in_converging_angle_c OR OLD.pump_in_converging_diameter_radio_c != NEW.pump_in_converging_diameter_radio_c OR OLD.pump_in_in_out_resistance_coefficient_c != NEW.pump_in_in_out_resistance_coefficient_c OR OLD.pump_in_filter_c != NEW.pump_in_filter_c OR OLD.pump_in_sluice_count_c != NEW.pump_in_sluice_count_c OR OLD.pump_in_check_resistance_coefficient_c != NEW.pump_in_check_resistance_coefficient_c OR OLD.pump_in_regulating_resistance_coefficient_c != NEW.pump_in_regulating_resistance_coefficient_c OR OLD.pump_in_plate_resistance_coefficient_c != NEW.pump_in_plate_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_local_resistance_c=(((14*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_90elbow_count_c))+((60*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_triplet_count_c))+((0.8*sin((NEW.pump_in_converging_angle_c)*3.14/180)*(1-((NEW.pump_in_converging_diameter_radio_c))^2)/((NEW.pump_in_converging_diameter_radio_c))^4))+(NEW.pump_in_in_out_resistance_coefficient_c)+((NEW.pump_in_filter_c)+((8*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_sluice_count_c))+(NEW.pump_in_check_resistance_coefficient_c)+(NEW.pump_in_regulating_resistance_coefficient_c))+(NEW.pump_in_plate_resistance_coefficient_c))*(((0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2))^2/2/(NEW.pump_in_msv_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_plate_resistance_coefficient_c ISNULL OR OLD.pump_in_regulating_resistance_coefficient_c ISNULL OR OLD.pump_in_check_resistance_coefficient_c ISNULL OR OLD.pump_in_sluice_count_c ISNULL OR OLD.pump_in_filter_c ISNULL OR OLD.pump_in_in_out_resistance_coefficient_c ISNULL OR OLD.pump_in_converging_diameter_radio_c ISNULL OR OLD.pump_in_converging_angle_c ISNULL OR OLD.pump_in_triplet_count_c ISNULL OR OLD.pump_in_90elbow_count_c ISNULL OR OLD.pump_in_resistance_coefficient_c ISNULL OR OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL OR OLD.pump_in_msv_c ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_plate_resistance_coefficient_c NOTNULL AND NEW.pump_in_regulating_resistance_coefficient_c NOTNULL AND NEW.pump_in_check_resistance_coefficient_c NOTNULL AND NEW.pump_in_sluice_count_c NOTNULL AND NEW.pump_in_filter_c NOTNULL AND NEW.pump_in_in_out_resistance_coefficient_c NOTNULL AND NEW.pump_in_converging_diameter_radio_c NOTNULL AND NEW.pump_in_converging_angle_c NOTNULL AND NEW.pump_in_triplet_count_c NOTNULL AND NEW.pump_in_90elbow_count_c NOTNULL AND NEW.pump_in_resistance_coefficient_c NOTNULL AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL AND NEW.pump_in_msv_c NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_local_resistance_c=(((14*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_90elbow_count_c))+((60*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_triplet_count_c))+((0.8*sin((NEW.pump_in_converging_angle_c)*3.14/180)*(1-((NEW.pump_in_converging_diameter_radio_c))^2)/((NEW.pump_in_converging_diameter_radio_c))^4))+(NEW.pump_in_in_out_resistance_coefficient_c)+((NEW.pump_in_filter_c)+((8*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_sluice_count_c))+(NEW.pump_in_check_resistance_coefficient_c)+(NEW.pump_in_regulating_resistance_coefficient_c))+(NEW.pump_in_plate_resistance_coefficient_c))*(((0.3537*(NEW.pump_in_rated_flow_c)*(NEW.pump_in_msv_c)/(((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c)))^2))^2/2/(NEW.pump_in_msv_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_total_local_resistance_coefficient_c:局部阻力系数合计--凝泵入口分管,的计算113-----------------------------------
  IF OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c OR OLD.pump_in_90elbow_count_c != NEW.pump_in_90elbow_count_c OR OLD.pump_in_triplet_count_c != NEW.pump_in_triplet_count_c OR OLD.pump_in_converging_angle_c != NEW.pump_in_converging_angle_c OR OLD.pump_in_converging_diameter_radio_c != NEW.pump_in_converging_diameter_radio_c OR OLD.pump_in_in_out_resistance_coefficient_c != NEW.pump_in_in_out_resistance_coefficient_c OR OLD.pump_in_filter_c != NEW.pump_in_filter_c OR OLD.pump_in_sluice_count_c != NEW.pump_in_sluice_count_c OR OLD.pump_in_check_resistance_coefficient_c != NEW.pump_in_check_resistance_coefficient_c OR OLD.pump_in_regulating_resistance_coefficient_c != NEW.pump_in_regulating_resistance_coefficient_c OR OLD.pump_in_plate_resistance_coefficient_c != NEW.pump_in_plate_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_total_local_resistance_coefficient_c=((14*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_90elbow_count_c))+((60*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_triplet_count_c))+((0.8*sin((NEW.pump_in_converging_angle_c)*3.14/180)*(1-((NEW.pump_in_converging_diameter_radio_c))^2)/((NEW.pump_in_converging_diameter_radio_c))^4))+(NEW.pump_in_in_out_resistance_coefficient_c)+((NEW.pump_in_filter_c)+((8*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_sluice_count_c))+(NEW.pump_in_check_resistance_coefficient_c)+(NEW.pump_in_regulating_resistance_coefficient_c))+(NEW.pump_in_plate_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_plate_resistance_coefficient_c ISNULL OR OLD.pump_in_regulating_resistance_coefficient_c ISNULL OR OLD.pump_in_check_resistance_coefficient_c ISNULL OR OLD.pump_in_sluice_count_c ISNULL OR OLD.pump_in_filter_c ISNULL OR OLD.pump_in_in_out_resistance_coefficient_c ISNULL OR OLD.pump_in_converging_diameter_radio_c ISNULL OR OLD.pump_in_converging_angle_c ISNULL OR OLD.pump_in_triplet_count_c ISNULL OR OLD.pump_in_90elbow_count_c ISNULL OR OLD.pump_in_resistance_coefficient_c ISNULL) AND NEW.pump_in_plate_resistance_coefficient_c NOTNULL AND NEW.pump_in_regulating_resistance_coefficient_c NOTNULL AND NEW.pump_in_check_resistance_coefficient_c NOTNULL AND NEW.pump_in_sluice_count_c NOTNULL AND NEW.pump_in_filter_c NOTNULL AND NEW.pump_in_in_out_resistance_coefficient_c NOTNULL AND NEW.pump_in_converging_diameter_radio_c NOTNULL AND NEW.pump_in_converging_angle_c NOTNULL AND NEW.pump_in_triplet_count_c NOTNULL AND NEW.pump_in_90elbow_count_c NOTNULL AND NEW.pump_in_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_total_local_resistance_coefficient_c=((14*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_90elbow_count_c))+((60*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_triplet_count_c))+((0.8*sin((NEW.pump_in_converging_angle_c)*3.14/180)*(1-((NEW.pump_in_converging_diameter_radio_c))^2)/((NEW.pump_in_converging_diameter_radio_c))^4))+(NEW.pump_in_in_out_resistance_coefficient_c)+((NEW.pump_in_filter_c)+((8*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_sluice_count_c))+(NEW.pump_in_check_resistance_coefficient_c)+(NEW.pump_in_regulating_resistance_coefficient_c))+(NEW.pump_in_plate_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_elbow_resistance_coefficient_c:弯头阻力系数--凝泵入口分管,的计算114-----------------------------------
  IF OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c OR OLD.pump_in_90elbow_count_c != NEW.pump_in_90elbow_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_elbow_resistance_coefficient_c=(14*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_90elbow_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_90elbow_count_c ISNULL OR OLD.pump_in_resistance_coefficient_c ISNULL) AND NEW.pump_in_90elbow_count_c NOTNULL AND NEW.pump_in_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_elbow_resistance_coefficient_c=(14*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_90elbow_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_elbow_radius_to_inner_diameter_c:弯头半径/内径--凝泵入口分管,的计算115-----------------------------------
  IF OLD.pump_in_pipe_outer_diameter_c != NEW.pump_in_pipe_outer_diameter_c OR OLD.pump_in_pipe_thickness_c != NEW.pump_in_pipe_thickness_c OR OLD.pump_in_elbow_radius_c != NEW.pump_in_elbow_radius_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_elbow_radius_to_inner_diameter_c=(NEW.pump_in_elbow_radius_c)/((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_elbow_radius_c ISNULL OR OLD.pump_in_pipe_thickness_c ISNULL OR OLD.pump_in_pipe_outer_diameter_c ISNULL) AND NEW.pump_in_elbow_radius_c NOTNULL AND NEW.pump_in_pipe_thickness_c NOTNULL AND NEW.pump_in_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_elbow_radius_to_inner_diameter_c=(NEW.pump_in_elbow_radius_c)/((NEW.pump_in_pipe_outer_diameter_c)-2*(NEW.pump_in_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_90elbow_resistance_coefficient_c:单个90º弯头阻力系数--凝泵入口分管,的计算116-----------------------------------
  IF OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_90elbow_resistance_coefficient_c=14*(NEW.pump_in_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_resistance_coefficient_c ISNULL) AND NEW.pump_in_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_90elbow_resistance_coefficient_c=14*(NEW.pump_in_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_triplet_resistance_coefficient_c:三通阻力系数--凝泵入口分管,的计算117-----------------------------------
  IF OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c OR OLD.pump_in_triplet_count_c != NEW.pump_in_triplet_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_triplet_resistance_coefficient_c=(60*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_triplet_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_triplet_count_c ISNULL OR OLD.pump_in_resistance_coefficient_c ISNULL) AND NEW.pump_in_triplet_count_c NOTNULL AND NEW.pump_in_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_triplet_resistance_coefficient_c=(60*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_triplet_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_single_triplet_resistance_coefficient_c:单个三通阻力系数--凝泵入口分管,的计算118-----------------------------------
  IF OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_single_triplet_resistance_coefficient_c=60*(NEW.pump_in_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_resistance_coefficient_c ISNULL) AND NEW.pump_in_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_single_triplet_resistance_coefficient_c=60*(NEW.pump_in_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_reducer_resistance_coefficient_c:异径管的阻力系数--凝泵入口分管,的计算119-----------------------------------
  IF OLD.pump_in_converging_angle_c != NEW.pump_in_converging_angle_c OR OLD.pump_in_converging_diameter_radio_c != NEW.pump_in_converging_diameter_radio_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_reducer_resistance_coefficient_c=(0.8*sin((NEW.pump_in_converging_angle_c)*3.14/180)*(1-((NEW.pump_in_converging_diameter_radio_c))^2)/((NEW.pump_in_converging_diameter_radio_c))^4)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_converging_diameter_radio_c ISNULL OR OLD.pump_in_converging_angle_c ISNULL) AND NEW.pump_in_converging_diameter_radio_c NOTNULL AND NEW.pump_in_converging_angle_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_reducer_resistance_coefficient_c=(0.8*sin((NEW.pump_in_converging_angle_c)*3.14/180)*(1-((NEW.pump_in_converging_diameter_radio_c))^2)/((NEW.pump_in_converging_diameter_radio_c))^4)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_converging_resistance_coefficient_c:渐缩管（相应于小管径的阻力系数）--凝泵入口分管,的计算120-----------------------------------
  IF OLD.pump_in_converging_angle_c != NEW.pump_in_converging_angle_c OR OLD.pump_in_converging_diameter_radio_c != NEW.pump_in_converging_diameter_radio_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_converging_resistance_coefficient_c=0.8*sin((NEW.pump_in_converging_angle_c)*3.14/180)*(1-((NEW.pump_in_converging_diameter_radio_c))^2)/((NEW.pump_in_converging_diameter_radio_c))^4
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_converging_diameter_radio_c ISNULL OR OLD.pump_in_converging_angle_c ISNULL) AND NEW.pump_in_converging_diameter_radio_c NOTNULL AND NEW.pump_in_converging_angle_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_converging_resistance_coefficient_c=0.8*sin((NEW.pump_in_converging_angle_c)*3.14/180)*(1-((NEW.pump_in_converging_diameter_radio_c))^2)/((NEW.pump_in_converging_diameter_radio_c))^4
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_valve_resistance_coefficient_c:阀门的局部阻力系数--凝泵入口分管,的计算121-----------------------------------
  IF OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c OR OLD.pump_in_filter_c != NEW.pump_in_filter_c OR OLD.pump_in_sluice_count_c != NEW.pump_in_sluice_count_c OR OLD.pump_in_check_resistance_coefficient_c != NEW.pump_in_check_resistance_coefficient_c OR OLD.pump_in_regulating_resistance_coefficient_c != NEW.pump_in_regulating_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_valve_resistance_coefficient_c=(NEW.pump_in_filter_c)+((8*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_sluice_count_c))+(NEW.pump_in_check_resistance_coefficient_c)+(NEW.pump_in_regulating_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_regulating_resistance_coefficient_c ISNULL OR OLD.pump_in_check_resistance_coefficient_c ISNULL OR OLD.pump_in_sluice_count_c ISNULL OR OLD.pump_in_filter_c ISNULL OR OLD.pump_in_resistance_coefficient_c ISNULL) AND NEW.pump_in_regulating_resistance_coefficient_c NOTNULL AND NEW.pump_in_check_resistance_coefficient_c NOTNULL AND NEW.pump_in_sluice_count_c NOTNULL AND NEW.pump_in_filter_c NOTNULL AND NEW.pump_in_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_valve_resistance_coefficient_c=(NEW.pump_in_filter_c)+((8*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_sluice_count_c))+(NEW.pump_in_check_resistance_coefficient_c)+(NEW.pump_in_regulating_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_sluice_resistance_coefficient_c:闸阀阻力系数--凝泵入口分管,的计算122-----------------------------------
  IF OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c OR OLD.pump_in_sluice_count_c != NEW.pump_in_sluice_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_sluice_resistance_coefficient_c=(8*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_sluice_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_sluice_count_c ISNULL OR OLD.pump_in_resistance_coefficient_c ISNULL) AND NEW.pump_in_sluice_count_c NOTNULL AND NEW.pump_in_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_sluice_resistance_coefficient_c=(8*(NEW.pump_in_resistance_coefficient_c))*(NEW.pump_in_sluice_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_single_sluice_resistance_coefficient_c:单个闸阀阻力系数--凝泵入口分管,的计算123-----------------------------------
  IF OLD.pump_in_resistance_coefficient_c != NEW.pump_in_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_single_sluice_resistance_coefficient_c=8*(NEW.pump_in_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_resistance_coefficient_c ISNULL) AND NEW.pump_in_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_single_sluice_resistance_coefficient_c=8*(NEW.pump_in_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_rated_flow_m:额定流量--凝泵入口母管,的计算124-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_rated_flow_m=(NEW.pump_in_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_rated_flow_m=(NEW.pump_in_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_media_viscosity_m:介质运动粘度--凝泵入口母管,的计算125-----------------------------------
  IF OLD.pump_in_media_viscosity_c != NEW.pump_in_media_viscosity_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_media_viscosity_m=(NEW.pump_in_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_media_viscosity_c ISNULL) AND NEW.pump_in_media_viscosity_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_media_viscosity_m=(NEW.pump_in_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_calculate_velocity_m:计算流速--凝泵入口母管,的计算126-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_calculate_velocity_m=0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL OR OLD.pump_in_msv_m ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL AND NEW.pump_in_msv_m NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_calculate_velocity_m=0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_dynamic_head_m:动压头--凝泵入口母管,的计算127-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_dynamic_head_m=((0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2))^2/2/(NEW.pump_in_msv_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL OR OLD.pump_in_msv_m ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL AND NEW.pump_in_msv_m NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_dynamic_head_m=((0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2))^2/2/(NEW.pump_in_msv_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_pipe_inner_diameter_m:内径--凝泵入口母管,的计算128-----------------------------------
  IF OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_pipe_inner_diameter_m=(NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL) AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_pipe_inner_diameter_m=(NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_friction_resistance_m:摩擦阻力--凝泵入口母管,的计算129-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m OR OLD.pump_in_resistance_coefficient_m != NEW.pump_in_resistance_coefficient_m OR OLD.pump_in_pipe_length_m != NEW.pump_in_pipe_length_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_friction_resistance_m=(NEW.pump_in_pipe_length_m)*((NEW.pump_in_resistance_coefficient_m)*(((0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2))^2/2/(NEW.pump_in_msv_m))/((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_length_m ISNULL OR OLD.pump_in_resistance_coefficient_m ISNULL OR OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL OR OLD.pump_in_msv_m ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_pipe_length_m NOTNULL AND NEW.pump_in_resistance_coefficient_m NOTNULL AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL AND NEW.pump_in_msv_m NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_friction_resistance_m=(NEW.pump_in_pipe_length_m)*((NEW.pump_in_resistance_coefficient_m)*(((0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2))^2/2/(NEW.pump_in_msv_m))/((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_reynolds_m:雷诺数--凝泵入口母管,的计算130-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_media_viscosity_c != NEW.pump_in_media_viscosity_c OR OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_reynolds_m=(0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2)*((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m))/((NEW.pump_in_media_viscosity_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL OR OLD.pump_in_msv_m ISNULL OR OLD.pump_in_media_viscosity_c ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL AND NEW.pump_in_msv_m NOTNULL AND NEW.pump_in_media_viscosity_c NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_reynolds_m=(0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2)*((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m))/((NEW.pump_in_media_viscosity_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_relative_roughness_m:相对粗糙度--凝泵入口母管,的计算131-----------------------------------
  IF OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m OR OLD.pump_in_equivalent_roughness_m != NEW.pump_in_equivalent_roughness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_relative_roughness_m=(NEW.pump_in_equivalent_roughness_m)/((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_equivalent_roughness_m ISNULL OR OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL) AND NEW.pump_in_equivalent_roughness_m NOTNULL AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_relative_roughness_m=(NEW.pump_in_equivalent_roughness_m)/((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_unit_length_resistance_m:单位长度摩擦阻力--凝泵入口母管,的计算132-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m OR OLD.pump_in_resistance_coefficient_m != NEW.pump_in_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_unit_length_resistance_m=(NEW.pump_in_resistance_coefficient_m)*(((0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2))^2/2/(NEW.pump_in_msv_m))/((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_resistance_coefficient_m ISNULL OR OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL OR OLD.pump_in_msv_m ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_resistance_coefficient_m NOTNULL AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL AND NEW.pump_in_msv_m NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_unit_length_resistance_m=(NEW.pump_in_resistance_coefficient_m)*(((0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2))^2/2/(NEW.pump_in_msv_m))/((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_local_resistance_m:局部阻力--凝泵入口母管,的计算133-----------------------------------
  IF OLD.pump_in_rated_flow_c != NEW.pump_in_rated_flow_c OR OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m OR OLD.pump_in_resistance_coefficient_m != NEW.pump_in_resistance_coefficient_m OR OLD.pump_in_90elbow_count_m != NEW.pump_in_90elbow_count_m OR OLD.pump_in_triplet_count_m != NEW.pump_in_triplet_count_m OR OLD.pump_in_reducer_resistance_coefficient_m != NEW.pump_in_reducer_resistance_coefficient_m OR OLD.pump_in_in_out_resistance_coefficient_m != NEW.pump_in_in_out_resistance_coefficient_m OR OLD.pump_in_filter_m != NEW.pump_in_filter_m OR OLD.pump_in_sluice_resistance_coefficient_m != NEW.pump_in_sluice_resistance_coefficient_m OR OLD.pump_in_check_resistance_coefficient_m != NEW.pump_in_check_resistance_coefficient_m OR OLD.pump_in_plate_resistance_coefficient_m != NEW.pump_in_plate_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_local_resistance_m=(((14*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_90elbow_count_m))+((20*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_triplet_count_m))+(NEW.pump_in_reducer_resistance_coefficient_m)+(NEW.pump_in_in_out_resistance_coefficient_m)+((NEW.pump_in_filter_m)+(NEW.pump_in_sluice_resistance_coefficient_m)+(NEW.pump_in_check_resistance_coefficient_m))+(NEW.pump_in_plate_resistance_coefficient_m))*(((0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2))^2/2/(NEW.pump_in_msv_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_plate_resistance_coefficient_m ISNULL OR OLD.pump_in_check_resistance_coefficient_m ISNULL OR OLD.pump_in_sluice_resistance_coefficient_m ISNULL OR OLD.pump_in_filter_m ISNULL OR OLD.pump_in_in_out_resistance_coefficient_m ISNULL OR OLD.pump_in_reducer_resistance_coefficient_m ISNULL OR OLD.pump_in_triplet_count_m ISNULL OR OLD.pump_in_90elbow_count_m ISNULL OR OLD.pump_in_resistance_coefficient_m ISNULL OR OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL OR OLD.pump_in_msv_m ISNULL OR OLD.pump_in_rated_flow_c ISNULL) AND NEW.pump_in_plate_resistance_coefficient_m NOTNULL AND NEW.pump_in_check_resistance_coefficient_m NOTNULL AND NEW.pump_in_sluice_resistance_coefficient_m NOTNULL AND NEW.pump_in_filter_m NOTNULL AND NEW.pump_in_in_out_resistance_coefficient_m NOTNULL AND NEW.pump_in_reducer_resistance_coefficient_m NOTNULL AND NEW.pump_in_triplet_count_m NOTNULL AND NEW.pump_in_90elbow_count_m NOTNULL AND NEW.pump_in_resistance_coefficient_m NOTNULL AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL AND NEW.pump_in_msv_m NOTNULL AND NEW.pump_in_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_local_resistance_m=(((14*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_90elbow_count_m))+((20*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_triplet_count_m))+(NEW.pump_in_reducer_resistance_coefficient_m)+(NEW.pump_in_in_out_resistance_coefficient_m)+((NEW.pump_in_filter_m)+(NEW.pump_in_sluice_resistance_coefficient_m)+(NEW.pump_in_check_resistance_coefficient_m))+(NEW.pump_in_plate_resistance_coefficient_m))*(((0.3537*((NEW.pump_in_rated_flow_c)*4)*(NEW.pump_in_msv_m)/(((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m)))^2))^2/2/(NEW.pump_in_msv_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_total_local_resistance_coefficient_m:局部阻力系数合计--凝泵入口母管,的计算134-----------------------------------
  IF OLD.pump_in_resistance_coefficient_m != NEW.pump_in_resistance_coefficient_m OR OLD.pump_in_90elbow_count_m != NEW.pump_in_90elbow_count_m OR OLD.pump_in_triplet_count_m != NEW.pump_in_triplet_count_m OR OLD.pump_in_reducer_resistance_coefficient_m != NEW.pump_in_reducer_resistance_coefficient_m OR OLD.pump_in_in_out_resistance_coefficient_m != NEW.pump_in_in_out_resistance_coefficient_m OR OLD.pump_in_filter_m != NEW.pump_in_filter_m OR OLD.pump_in_sluice_resistance_coefficient_m != NEW.pump_in_sluice_resistance_coefficient_m OR OLD.pump_in_check_resistance_coefficient_m != NEW.pump_in_check_resistance_coefficient_m OR OLD.pump_in_plate_resistance_coefficient_m != NEW.pump_in_plate_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_total_local_resistance_coefficient_m=((14*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_90elbow_count_m))+((20*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_triplet_count_m))+(NEW.pump_in_reducer_resistance_coefficient_m)+(NEW.pump_in_in_out_resistance_coefficient_m)+((NEW.pump_in_filter_m)+(NEW.pump_in_sluice_resistance_coefficient_m)+(NEW.pump_in_check_resistance_coefficient_m))+(NEW.pump_in_plate_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_plate_resistance_coefficient_m ISNULL OR OLD.pump_in_check_resistance_coefficient_m ISNULL OR OLD.pump_in_sluice_resistance_coefficient_m ISNULL OR OLD.pump_in_filter_m ISNULL OR OLD.pump_in_in_out_resistance_coefficient_m ISNULL OR OLD.pump_in_reducer_resistance_coefficient_m ISNULL OR OLD.pump_in_triplet_count_m ISNULL OR OLD.pump_in_90elbow_count_m ISNULL OR OLD.pump_in_resistance_coefficient_m ISNULL) AND NEW.pump_in_plate_resistance_coefficient_m NOTNULL AND NEW.pump_in_check_resistance_coefficient_m NOTNULL AND NEW.pump_in_sluice_resistance_coefficient_m NOTNULL AND NEW.pump_in_filter_m NOTNULL AND NEW.pump_in_in_out_resistance_coefficient_m NOTNULL AND NEW.pump_in_reducer_resistance_coefficient_m NOTNULL AND NEW.pump_in_triplet_count_m NOTNULL AND NEW.pump_in_90elbow_count_m NOTNULL AND NEW.pump_in_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_total_local_resistance_coefficient_m=((14*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_90elbow_count_m))+((20*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_triplet_count_m))+(NEW.pump_in_reducer_resistance_coefficient_m)+(NEW.pump_in_in_out_resistance_coefficient_m)+((NEW.pump_in_filter_m)+(NEW.pump_in_sluice_resistance_coefficient_m)+(NEW.pump_in_check_resistance_coefficient_m))+(NEW.pump_in_plate_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_elbow_resistance_coefficient_m:弯头阻力系数--凝泵入口母管,的计算135-----------------------------------
  IF OLD.pump_in_resistance_coefficient_m != NEW.pump_in_resistance_coefficient_m OR OLD.pump_in_90elbow_count_m != NEW.pump_in_90elbow_count_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_elbow_resistance_coefficient_m=(14*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_90elbow_count_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_90elbow_count_m ISNULL OR OLD.pump_in_resistance_coefficient_m ISNULL) AND NEW.pump_in_90elbow_count_m NOTNULL AND NEW.pump_in_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_elbow_resistance_coefficient_m=(14*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_90elbow_count_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_elbow_radius_to_inner_diameter_m:弯头半径/内径--凝泵入口母管,的计算136-----------------------------------
  IF OLD.pump_in_pipe_outer_diameter_m != NEW.pump_in_pipe_outer_diameter_m OR OLD.pump_in_pipe_thickness_m != NEW.pump_in_pipe_thickness_m OR OLD.pump_in_elbow_radius_m != NEW.pump_in_elbow_radius_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_elbow_radius_to_inner_diameter_m=(NEW.pump_in_elbow_radius_m)/((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_elbow_radius_m ISNULL OR OLD.pump_in_pipe_thickness_m ISNULL OR OLD.pump_in_pipe_outer_diameter_m ISNULL) AND NEW.pump_in_elbow_radius_m NOTNULL AND NEW.pump_in_pipe_thickness_m NOTNULL AND NEW.pump_in_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_elbow_radius_to_inner_diameter_m=(NEW.pump_in_elbow_radius_m)/((NEW.pump_in_pipe_outer_diameter_m)-2*(NEW.pump_in_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_90elbow_resistance_coefficient_m:单个90º弯头阻力系数--凝泵入口母管,的计算137-----------------------------------
  IF OLD.pump_in_resistance_coefficient_m != NEW.pump_in_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_90elbow_resistance_coefficient_m=14*(NEW.pump_in_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_resistance_coefficient_m ISNULL) AND NEW.pump_in_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_90elbow_resistance_coefficient_m=14*(NEW.pump_in_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_triplet_resistance_coefficient_m:三通阻力系数--凝泵入口母管,的计算138-----------------------------------
  IF OLD.pump_in_resistance_coefficient_m != NEW.pump_in_resistance_coefficient_m OR OLD.pump_in_triplet_count_m != NEW.pump_in_triplet_count_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_triplet_resistance_coefficient_m=(20*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_triplet_count_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_triplet_count_m ISNULL OR OLD.pump_in_resistance_coefficient_m ISNULL) AND NEW.pump_in_triplet_count_m NOTNULL AND NEW.pump_in_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_triplet_resistance_coefficient_m=(20*(NEW.pump_in_resistance_coefficient_m))*(NEW.pump_in_triplet_count_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_single_triplet_resistance_coefficient_m:单个三通阻力系数--凝泵入口母管,的计算139-----------------------------------
  IF OLD.pump_in_resistance_coefficient_m != NEW.pump_in_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_single_triplet_resistance_coefficient_m=20*(NEW.pump_in_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_resistance_coefficient_m ISNULL) AND NEW.pump_in_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_single_triplet_resistance_coefficient_m=20*(NEW.pump_in_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_in_valve_resistance_coefficient_m:阀门的局部阻力系数--凝泵入口母管,的计算140-----------------------------------
  IF OLD.pump_in_filter_m != NEW.pump_in_filter_m OR OLD.pump_in_sluice_resistance_coefficient_m != NEW.pump_in_sluice_resistance_coefficient_m OR OLD.pump_in_check_resistance_coefficient_m != NEW.pump_in_check_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_valve_resistance_coefficient_m=(NEW.pump_in_filter_m)+(NEW.pump_in_sluice_resistance_coefficient_m)+(NEW.pump_in_check_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_check_resistance_coefficient_m ISNULL OR OLD.pump_in_sluice_resistance_coefficient_m ISNULL OR OLD.pump_in_filter_m ISNULL) AND NEW.pump_in_check_resistance_coefficient_m NOTNULL AND NEW.pump_in_sluice_resistance_coefficient_m NOTNULL AND NEW.pump_in_filter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_in_valve_resistance_coefficient_m=(NEW.pump_in_filter_m)+(NEW.pump_in_sluice_resistance_coefficient_m)+(NEW.pump_in_check_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_work_press_c:运行压力(表压)--凝泵出口分管,的计算141-----------------------------------
  IF OLD.pump_in_work_press_c != NEW.pump_in_work_press_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_work_press_c=0.36+(NEW.pump_in_work_press_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_work_press_c ISNULL) AND NEW.pump_in_work_press_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_work_press_c=0.36+(NEW.pump_in_work_press_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_msv_c:介质比容--凝泵出口分管,的计算142-----------------------------------
  IF OLD.pump_in_msv_c != NEW.pump_in_msv_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_msv_c=(NEW.pump_in_msv_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_msv_c ISNULL) AND NEW.pump_in_msv_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_msv_c=(NEW.pump_in_msv_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_media_viscosity_c:介质运动粘度--凝泵出口分管,的计算143-----------------------------------
  IF OLD.pump_in_media_viscosity_c != NEW.pump_in_media_viscosity_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_media_viscosity_c=(NEW.pump_in_media_viscosity_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_media_viscosity_c ISNULL) AND NEW.pump_in_media_viscosity_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_media_viscosity_c=(NEW.pump_in_media_viscosity_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_calculate_velocity_c:计算流速--凝泵出口分管,的计算144-----------------------------------
  IF OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_calculate_velocity_c=0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_c ISNULL) AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_calculate_velocity_c=0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_dynamic_head_c:动压头--凝泵出口分管,的计算145-----------------------------------
  IF OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_dynamic_head_c=((0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2))^2/2/((NEW.pump_in_msv_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_c ISNULL) AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_dynamic_head_c=((0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2))^2/2/((NEW.pump_in_msv_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_pipe_inner_diameter_c:内径--凝泵出口分管,的计算146-----------------------------------
  IF OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_pipe_inner_diameter_c=(NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL) AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_pipe_inner_diameter_c=(NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_friction_resistance_c:摩擦阻力--凝泵出口分管,的计算147-----------------------------------
  IF OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c OR OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c OR OLD.pump_out_pipe_length_c != NEW.pump_out_pipe_length_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_friction_resistance_c=(NEW.pump_out_pipe_length_c)*((NEW.pump_out_resistance_coefficient_c)*(((0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2))^2/2/((NEW.pump_in_msv_c)))/((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_length_c ISNULL OR OLD.pump_out_resistance_coefficient_c ISNULL OR OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_c ISNULL) AND NEW.pump_out_pipe_length_c NOTNULL AND NEW.pump_out_resistance_coefficient_c NOTNULL AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_friction_resistance_c=(NEW.pump_out_pipe_length_c)*((NEW.pump_out_resistance_coefficient_c)*(((0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2))^2/2/((NEW.pump_in_msv_c)))/((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_reynolds_c:雷诺数--凝泵出口分管,的计算148-----------------------------------
  IF OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_in_media_viscosity_c != NEW.pump_in_media_viscosity_c OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_reynolds_c=(0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2)*((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c))/((NEW.pump_in_media_viscosity_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_media_viscosity_c ISNULL OR OLD.pump_in_msv_c ISNULL) AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_media_viscosity_c NOTNULL AND NEW.pump_in_msv_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_reynolds_c=(0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2)*((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c))/((NEW.pump_in_media_viscosity_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_relative_roughness_c:相对粗糙度--凝泵出口分管,的计算149-----------------------------------
  IF OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c OR OLD.pump_out_equivalent_roughness_c != NEW.pump_out_equivalent_roughness_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_relative_roughness_c=(NEW.pump_out_equivalent_roughness_c)/((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_equivalent_roughness_c ISNULL OR OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL) AND NEW.pump_out_equivalent_roughness_c NOTNULL AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_relative_roughness_c=(NEW.pump_out_equivalent_roughness_c)/((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_unit_length_resistance_c:单位长度摩擦阻力--凝泵出口分管,的计算150-----------------------------------
  IF OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c OR OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_unit_length_resistance_c=(NEW.pump_out_resistance_coefficient_c)*(((0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2))^2/2/((NEW.pump_in_msv_c)))/((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_resistance_coefficient_c ISNULL OR OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_c ISNULL) AND NEW.pump_out_resistance_coefficient_c NOTNULL AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_unit_length_resistance_c=(NEW.pump_out_resistance_coefficient_c)*(((0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2))^2/2/((NEW.pump_in_msv_c)))/((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_local_resistance_c:局部阻力--凝泵出口分管,的计算151-----------------------------------
  IF OLD.pump_in_msv_c != NEW.pump_in_msv_c OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c OR OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c OR OLD.pump_out_90elbow_count_c != NEW.pump_out_90elbow_count_c OR OLD.pump_out_triplet_count_c != NEW.pump_out_triplet_count_c OR OLD.pump_out_reducer_resistance_coefficient_c != NEW.pump_out_reducer_resistance_coefficient_c OR OLD.pump_out_in_out_resistance_coefficient_c != NEW.pump_out_in_out_resistance_coefficient_c OR OLD.pump_out_filter_c != NEW.pump_out_filter_c OR OLD.pump_out_sluice_count_c != NEW.pump_out_sluice_count_c OR OLD.pump_out_check_count_c != NEW.pump_out_check_count_c OR OLD.pump_out_plate_resistance_coefficient_c != NEW.pump_out_plate_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_local_resistance_c=(((14*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_90elbow_count_c))+((60*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_triplet_count_c))+(NEW.pump_out_reducer_resistance_coefficient_c)+(NEW.pump_out_in_out_resistance_coefficient_c)+((NEW.pump_out_filter_c)+((8*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_sluice_count_c))+((600*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_check_count_c)))+(NEW.pump_out_plate_resistance_coefficient_c))*(((0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2))^2/2/((NEW.pump_in_msv_c)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_plate_resistance_coefficient_c ISNULL OR OLD.pump_out_check_count_c ISNULL OR OLD.pump_out_sluice_count_c ISNULL OR OLD.pump_out_filter_c ISNULL OR OLD.pump_out_in_out_resistance_coefficient_c ISNULL OR OLD.pump_out_reducer_resistance_coefficient_c ISNULL OR OLD.pump_out_triplet_count_c ISNULL OR OLD.pump_out_90elbow_count_c ISNULL OR OLD.pump_out_resistance_coefficient_c ISNULL OR OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_c ISNULL) AND NEW.pump_out_plate_resistance_coefficient_c NOTNULL AND NEW.pump_out_check_count_c NOTNULL AND NEW.pump_out_sluice_count_c NOTNULL AND NEW.pump_out_filter_c NOTNULL AND NEW.pump_out_in_out_resistance_coefficient_c NOTNULL AND NEW.pump_out_reducer_resistance_coefficient_c NOTNULL AND NEW.pump_out_triplet_count_c NOTNULL AND NEW.pump_out_90elbow_count_c NOTNULL AND NEW.pump_out_resistance_coefficient_c NOTNULL AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_local_resistance_c=(((14*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_90elbow_count_c))+((60*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_triplet_count_c))+(NEW.pump_out_reducer_resistance_coefficient_c)+(NEW.pump_out_in_out_resistance_coefficient_c)+((NEW.pump_out_filter_c)+((8*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_sluice_count_c))+((600*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_check_count_c)))+(NEW.pump_out_plate_resistance_coefficient_c))*(((0.3537*(NEW.pump_out_rated_flow_c)*((NEW.pump_in_msv_c))/(((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c)))^2))^2/2/((NEW.pump_in_msv_c)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_total_local_resistance_coefficient_c:局部阻力系数合计--凝泵出口分管,的计算152-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c OR OLD.pump_out_90elbow_count_c != NEW.pump_out_90elbow_count_c OR OLD.pump_out_triplet_count_c != NEW.pump_out_triplet_count_c OR OLD.pump_out_reducer_resistance_coefficient_c != NEW.pump_out_reducer_resistance_coefficient_c OR OLD.pump_out_in_out_resistance_coefficient_c != NEW.pump_out_in_out_resistance_coefficient_c OR OLD.pump_out_filter_c != NEW.pump_out_filter_c OR OLD.pump_out_sluice_count_c != NEW.pump_out_sluice_count_c OR OLD.pump_out_check_count_c != NEW.pump_out_check_count_c OR OLD.pump_out_plate_resistance_coefficient_c != NEW.pump_out_plate_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_total_local_resistance_coefficient_c=((14*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_90elbow_count_c))+((60*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_triplet_count_c))+(NEW.pump_out_reducer_resistance_coefficient_c)+(NEW.pump_out_in_out_resistance_coefficient_c)+((NEW.pump_out_filter_c)+((8*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_sluice_count_c))+((600*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_check_count_c)))+(NEW.pump_out_plate_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_plate_resistance_coefficient_c ISNULL OR OLD.pump_out_check_count_c ISNULL OR OLD.pump_out_sluice_count_c ISNULL OR OLD.pump_out_filter_c ISNULL OR OLD.pump_out_in_out_resistance_coefficient_c ISNULL OR OLD.pump_out_reducer_resistance_coefficient_c ISNULL OR OLD.pump_out_triplet_count_c ISNULL OR OLD.pump_out_90elbow_count_c ISNULL OR OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_plate_resistance_coefficient_c NOTNULL AND NEW.pump_out_check_count_c NOTNULL AND NEW.pump_out_sluice_count_c NOTNULL AND NEW.pump_out_filter_c NOTNULL AND NEW.pump_out_in_out_resistance_coefficient_c NOTNULL AND NEW.pump_out_reducer_resistance_coefficient_c NOTNULL AND NEW.pump_out_triplet_count_c NOTNULL AND NEW.pump_out_90elbow_count_c NOTNULL AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_total_local_resistance_coefficient_c=((14*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_90elbow_count_c))+((60*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_triplet_count_c))+(NEW.pump_out_reducer_resistance_coefficient_c)+(NEW.pump_out_in_out_resistance_coefficient_c)+((NEW.pump_out_filter_c)+((8*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_sluice_count_c))+((600*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_check_count_c)))+(NEW.pump_out_plate_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_elbow_resistance_coefficient_c:弯头阻力系数--凝泵出口分管,的计算153-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c OR OLD.pump_out_90elbow_count_c != NEW.pump_out_90elbow_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_elbow_resistance_coefficient_c=(14*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_90elbow_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_90elbow_count_c ISNULL OR OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_90elbow_count_c NOTNULL AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_elbow_resistance_coefficient_c=(14*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_90elbow_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_elbow_radius_to_inner_diameter_c:弯头半径/内径--凝泵出口分管,的计算154-----------------------------------
  IF OLD.pump_out_pipe_outer_diameter_c != NEW.pump_out_pipe_outer_diameter_c OR OLD.pump_out_pipe_thickness_c != NEW.pump_out_pipe_thickness_c OR OLD.pump_out_elbow_radius_c != NEW.pump_out_elbow_radius_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_elbow_radius_to_inner_diameter_c=(NEW.pump_out_elbow_radius_c)/((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_elbow_radius_c ISNULL OR OLD.pump_out_pipe_thickness_c ISNULL OR OLD.pump_out_pipe_outer_diameter_c ISNULL) AND NEW.pump_out_elbow_radius_c NOTNULL AND NEW.pump_out_pipe_thickness_c NOTNULL AND NEW.pump_out_pipe_outer_diameter_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_elbow_radius_to_inner_diameter_c=(NEW.pump_out_elbow_radius_c)/((NEW.pump_out_pipe_outer_diameter_c)-2*(NEW.pump_out_pipe_thickness_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_90elbow_resistance_coefficient_c:单个90º弯头阻力系数--凝泵出口分管,的计算155-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_90elbow_resistance_coefficient_c=14*(NEW.pump_out_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_90elbow_resistance_coefficient_c=14*(NEW.pump_out_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_triplet_resistance_coefficient_c:三通阻力系数--凝泵出口分管,的计算156-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c OR OLD.pump_out_triplet_count_c != NEW.pump_out_triplet_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_triplet_resistance_coefficient_c=(60*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_triplet_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_triplet_count_c ISNULL OR OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_triplet_count_c NOTNULL AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_triplet_resistance_coefficient_c=(60*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_triplet_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_single_triplet_resistance_coefficient_c:单个三通阻力系数--凝泵出口分管,的计算157-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_single_triplet_resistance_coefficient_c=60*(NEW.pump_out_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_single_triplet_resistance_coefficient_c=60*(NEW.pump_out_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_valve_resistance_coefficient_c:阀门的局部阻力系数--凝泵出口分管,的计算158-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c OR OLD.pump_out_filter_c != NEW.pump_out_filter_c OR OLD.pump_out_sluice_count_c != NEW.pump_out_sluice_count_c OR OLD.pump_out_check_count_c != NEW.pump_out_check_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_valve_resistance_coefficient_c=(NEW.pump_out_filter_c)+((8*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_sluice_count_c))+((600*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_check_count_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_check_count_c ISNULL OR OLD.pump_out_sluice_count_c ISNULL OR OLD.pump_out_filter_c ISNULL OR OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_check_count_c NOTNULL AND NEW.pump_out_sluice_count_c NOTNULL AND NEW.pump_out_filter_c NOTNULL AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_valve_resistance_coefficient_c=(NEW.pump_out_filter_c)+((8*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_sluice_count_c))+((600*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_check_count_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_sluice_resistance_coefficient_c:闸阀阻力系数--凝泵出口分管,的计算159-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c OR OLD.pump_out_sluice_count_c != NEW.pump_out_sluice_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_sluice_resistance_coefficient_c=(8*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_sluice_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_sluice_count_c ISNULL OR OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_sluice_count_c NOTNULL AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_sluice_resistance_coefficient_c=(8*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_sluice_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_single_sluice_resistance_coefficient_c:单个闸阀阻力系数--凝泵出口分管,的计算160-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_single_sluice_resistance_coefficient_c=8*(NEW.pump_out_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_single_sluice_resistance_coefficient_c=8*(NEW.pump_out_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_check_resistance_coefficient_c:止回阀阻力系数--凝泵出口分管,的计算161-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c OR OLD.pump_out_check_count_c != NEW.pump_out_check_count_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_check_resistance_coefficient_c=(600*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_check_count_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_check_count_c ISNULL OR OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_check_count_c NOTNULL AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_check_resistance_coefficient_c=(600*(NEW.pump_out_resistance_coefficient_c))*(NEW.pump_out_check_count_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_single_check_resistance_coefficient_c:单个止回阀阻力系数--凝泵出口分管,的计算162-----------------------------------
  IF OLD.pump_out_resistance_coefficient_c != NEW.pump_out_resistance_coefficient_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_single_check_resistance_coefficient_c=600*(NEW.pump_out_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_resistance_coefficient_c ISNULL) AND NEW.pump_out_resistance_coefficient_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_single_check_resistance_coefficient_c=600*(NEW.pump_out_resistance_coefficient_c)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_work_press_m:运行压力(表压)--凝泵出口母管,的计算163-----------------------------------
  IF OLD.pump_in_work_press_m != NEW.pump_in_work_press_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_work_press_m=0.36+(NEW.pump_in_work_press_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_work_press_m ISNULL) AND NEW.pump_in_work_press_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_work_press_m=0.36+(NEW.pump_in_work_press_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_rated_flow_m:额定流量--凝泵出口母管,的计算164-----------------------------------
  IF OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_rated_flow_m=(NEW.pump_out_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_rated_flow_c ISNULL) AND NEW.pump_out_rated_flow_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_rated_flow_m=(NEW.pump_out_rated_flow_c)*4
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_msv_m:介质比容--凝泵出口母管,的计算165-----------------------------------
  IF OLD.pump_in_msv_m != NEW.pump_in_msv_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_msv_m=(NEW.pump_in_msv_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_msv_m ISNULL) AND NEW.pump_in_msv_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_msv_m=(NEW.pump_in_msv_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_media_viscosity_m:介质运动粘度--凝泵出口母管,的计算166-----------------------------------
  IF OLD.pump_in_media_viscosity_c != NEW.pump_in_media_viscosity_c THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_media_viscosity_m=((NEW.pump_in_media_viscosity_c))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_in_media_viscosity_c ISNULL) AND NEW.pump_in_media_viscosity_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_media_viscosity_m=((NEW.pump_in_media_viscosity_c))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_calculate_velocity_m:计算流速--凝泵出口母管,的计算167-----------------------------------
  IF OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_calculate_velocity_m=0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_m ISNULL) AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_calculate_velocity_m=0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_dynamic_head_m:动压头--凝泵出口母管,的计算168-----------------------------------
  IF OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_dynamic_head_m=((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_m ISNULL) AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_dynamic_head_m=((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_pipe_inner_diameter_m:内径--凝泵出口母管,的计算169-----------------------------------
  IF OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_pipe_inner_diameter_m=(NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL) AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_pipe_inner_diameter_m=(NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_friction_resistance_m:摩擦阻力--凝泵出口母管,的计算170-----------------------------------
  IF OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m OR OLD.pump_out_resistance_coefficient_m != NEW.pump_out_resistance_coefficient_m OR OLD.pump_out_pipe_length_m != NEW.pump_out_pipe_length_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_friction_resistance_m=(NEW.pump_out_pipe_length_m)*((NEW.pump_out_resistance_coefficient_m)*(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))/((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_length_m ISNULL OR OLD.pump_out_resistance_coefficient_m ISNULL OR OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_m ISNULL) AND NEW.pump_out_pipe_length_m NOTNULL AND NEW.pump_out_resistance_coefficient_m NOTNULL AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_friction_resistance_m=(NEW.pump_out_pipe_length_m)*((NEW.pump_out_resistance_coefficient_m)*(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))/((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_reynolds_m:雷诺数--凝泵出口母管,的计算171-----------------------------------
  IF OLD.pump_in_media_viscosity_c != NEW.pump_in_media_viscosity_c OR OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_reynolds_m=(0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2)*((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m))/(((NEW.pump_in_media_viscosity_c)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_m ISNULL OR OLD.pump_in_media_viscosity_c ISNULL) AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_m NOTNULL AND NEW.pump_in_media_viscosity_c NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_reynolds_m=(0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2)*((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m))/(((NEW.pump_in_media_viscosity_c)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_relative_roughness_m:相对粗糙度--凝泵出口母管,的计算172-----------------------------------
  IF OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m OR OLD.pump_out_equivalent_roughness_m != NEW.pump_out_equivalent_roughness_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_relative_roughness_m=(NEW.pump_out_equivalent_roughness_m)/((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m))/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_equivalent_roughness_m ISNULL OR OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL) AND NEW.pump_out_equivalent_roughness_m NOTNULL AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_relative_roughness_m=(NEW.pump_out_equivalent_roughness_m)/((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m))/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_unit_length_resistance_m:单位长度摩擦阻力--凝泵出口母管,的计算173-----------------------------------
  IF OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m OR OLD.pump_out_resistance_coefficient_m != NEW.pump_out_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_unit_length_resistance_m=(NEW.pump_out_resistance_coefficient_m)*(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))/((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_resistance_coefficient_m ISNULL OR OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_m ISNULL) AND NEW.pump_out_resistance_coefficient_m NOTNULL AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_unit_length_resistance_m=(NEW.pump_out_resistance_coefficient_m)*(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))/((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_local_resistance_m:局部阻力--凝泵出口母管,的计算174-----------------------------------
  IF OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m OR OLD.pump_out_resistance_coefficient_m != NEW.pump_out_resistance_coefficient_m OR OLD.pump_out_90elbow_count_m != NEW.pump_out_90elbow_count_m OR OLD.pump_out_triplet_count_m != NEW.pump_out_triplet_count_m OR OLD.pump_out_reducer_resistance_coefficient_m != NEW.pump_out_reducer_resistance_coefficient_m OR OLD.pump_out_in_out_resistance_coefficient_m != NEW.pump_out_in_out_resistance_coefficient_m OR OLD.pump_out_filter_m != NEW.pump_out_filter_m OR OLD.pump_out_sluice_resistance_coefficient_m != NEW.pump_out_sluice_resistance_coefficient_m OR OLD.pump_out_check_resistance_coefficient_m != NEW.pump_out_check_resistance_coefficient_m OR OLD.pump_out_measuring_pressure_loss_m != NEW.pump_out_measuring_pressure_loss_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_local_resistance_m=(((14*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_90elbow_count_m))+((20*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_triplet_count_m))+(NEW.pump_out_reducer_resistance_coefficient_m)+(NEW.pump_out_in_out_resistance_coefficient_m)+((NEW.pump_out_filter_m)+(NEW.pump_out_sluice_resistance_coefficient_m)+(NEW.pump_out_check_resistance_coefficient_m))+((NEW.pump_out_measuring_pressure_loss_m)/(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))))*(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_measuring_pressure_loss_m ISNULL OR OLD.pump_out_check_resistance_coefficient_m ISNULL OR OLD.pump_out_sluice_resistance_coefficient_m ISNULL OR OLD.pump_out_filter_m ISNULL OR OLD.pump_out_in_out_resistance_coefficient_m ISNULL OR OLD.pump_out_reducer_resistance_coefficient_m ISNULL OR OLD.pump_out_triplet_count_m ISNULL OR OLD.pump_out_90elbow_count_m ISNULL OR OLD.pump_out_resistance_coefficient_m ISNULL OR OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_m ISNULL) AND NEW.pump_out_measuring_pressure_loss_m NOTNULL AND NEW.pump_out_check_resistance_coefficient_m NOTNULL AND NEW.pump_out_sluice_resistance_coefficient_m NOTNULL AND NEW.pump_out_filter_m NOTNULL AND NEW.pump_out_in_out_resistance_coefficient_m NOTNULL AND NEW.pump_out_reducer_resistance_coefficient_m NOTNULL AND NEW.pump_out_triplet_count_m NOTNULL AND NEW.pump_out_90elbow_count_m NOTNULL AND NEW.pump_out_resistance_coefficient_m NOTNULL AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_local_resistance_m=(((14*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_90elbow_count_m))+((20*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_triplet_count_m))+(NEW.pump_out_reducer_resistance_coefficient_m)+(NEW.pump_out_in_out_resistance_coefficient_m)+((NEW.pump_out_filter_m)+(NEW.pump_out_sluice_resistance_coefficient_m)+(NEW.pump_out_check_resistance_coefficient_m))+((NEW.pump_out_measuring_pressure_loss_m)/(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))))*(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_total_local_resistance_coefficient_m:局部阻力系数合计--凝泵出口母管,的计算175-----------------------------------
  IF OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m OR OLD.pump_out_resistance_coefficient_m != NEW.pump_out_resistance_coefficient_m OR OLD.pump_out_90elbow_count_m != NEW.pump_out_90elbow_count_m OR OLD.pump_out_triplet_count_m != NEW.pump_out_triplet_count_m OR OLD.pump_out_reducer_resistance_coefficient_m != NEW.pump_out_reducer_resistance_coefficient_m OR OLD.pump_out_in_out_resistance_coefficient_m != NEW.pump_out_in_out_resistance_coefficient_m OR OLD.pump_out_filter_m != NEW.pump_out_filter_m OR OLD.pump_out_sluice_resistance_coefficient_m != NEW.pump_out_sluice_resistance_coefficient_m OR OLD.pump_out_check_resistance_coefficient_m != NEW.pump_out_check_resistance_coefficient_m OR OLD.pump_out_measuring_pressure_loss_m != NEW.pump_out_measuring_pressure_loss_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_total_local_resistance_coefficient_m=((14*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_90elbow_count_m))+((20*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_triplet_count_m))+(NEW.pump_out_reducer_resistance_coefficient_m)+(NEW.pump_out_in_out_resistance_coefficient_m)+((NEW.pump_out_filter_m)+(NEW.pump_out_sluice_resistance_coefficient_m)+(NEW.pump_out_check_resistance_coefficient_m))+((NEW.pump_out_measuring_pressure_loss_m)/(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_measuring_pressure_loss_m ISNULL OR OLD.pump_out_check_resistance_coefficient_m ISNULL OR OLD.pump_out_sluice_resistance_coefficient_m ISNULL OR OLD.pump_out_filter_m ISNULL OR OLD.pump_out_in_out_resistance_coefficient_m ISNULL OR OLD.pump_out_reducer_resistance_coefficient_m ISNULL OR OLD.pump_out_triplet_count_m ISNULL OR OLD.pump_out_90elbow_count_m ISNULL OR OLD.pump_out_resistance_coefficient_m ISNULL OR OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_m ISNULL) AND NEW.pump_out_measuring_pressure_loss_m NOTNULL AND NEW.pump_out_check_resistance_coefficient_m NOTNULL AND NEW.pump_out_sluice_resistance_coefficient_m NOTNULL AND NEW.pump_out_filter_m NOTNULL AND NEW.pump_out_in_out_resistance_coefficient_m NOTNULL AND NEW.pump_out_reducer_resistance_coefficient_m NOTNULL AND NEW.pump_out_triplet_count_m NOTNULL AND NEW.pump_out_90elbow_count_m NOTNULL AND NEW.pump_out_resistance_coefficient_m NOTNULL AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_total_local_resistance_coefficient_m=((14*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_90elbow_count_m))+((20*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_triplet_count_m))+(NEW.pump_out_reducer_resistance_coefficient_m)+(NEW.pump_out_in_out_resistance_coefficient_m)+((NEW.pump_out_filter_m)+(NEW.pump_out_sluice_resistance_coefficient_m)+(NEW.pump_out_check_resistance_coefficient_m))+((NEW.pump_out_measuring_pressure_loss_m)/(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_elbow_resistance_coefficient_m:弯头阻力系数--凝泵出口母管,的计算176-----------------------------------
  IF OLD.pump_out_resistance_coefficient_m != NEW.pump_out_resistance_coefficient_m OR OLD.pump_out_90elbow_count_m != NEW.pump_out_90elbow_count_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_elbow_resistance_coefficient_m=(14*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_90elbow_count_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_90elbow_count_m ISNULL OR OLD.pump_out_resistance_coefficient_m ISNULL) AND NEW.pump_out_90elbow_count_m NOTNULL AND NEW.pump_out_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_elbow_resistance_coefficient_m=(14*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_90elbow_count_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_elbow_radius_to_inner_diameter_m:弯头半径/内径--凝泵出口母管,的计算177-----------------------------------
  IF OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m OR OLD.pump_out_elbow_radius_m != NEW.pump_out_elbow_radius_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_elbow_radius_to_inner_diameter_m=(NEW.pump_out_elbow_radius_m)/((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_elbow_radius_m ISNULL OR OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL) AND NEW.pump_out_elbow_radius_m NOTNULL AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_elbow_radius_to_inner_diameter_m=(NEW.pump_out_elbow_radius_m)/((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_90elbow_resistance_coefficient_m:单个90º弯头阻力系数--凝泵出口母管,的计算178-----------------------------------
  IF OLD.pump_out_resistance_coefficient_m != NEW.pump_out_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_90elbow_resistance_coefficient_m=14*(NEW.pump_out_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_resistance_coefficient_m ISNULL) AND NEW.pump_out_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_90elbow_resistance_coefficient_m=14*(NEW.pump_out_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_triplet_resistance_coefficient_m:三通阻力系数--凝泵出口母管,的计算179-----------------------------------
  IF OLD.pump_out_resistance_coefficient_m != NEW.pump_out_resistance_coefficient_m OR OLD.pump_out_triplet_count_m != NEW.pump_out_triplet_count_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_triplet_resistance_coefficient_m=(20*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_triplet_count_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_triplet_count_m ISNULL OR OLD.pump_out_resistance_coefficient_m ISNULL) AND NEW.pump_out_triplet_count_m NOTNULL AND NEW.pump_out_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_triplet_resistance_coefficient_m=(20*(NEW.pump_out_resistance_coefficient_m))*(NEW.pump_out_triplet_count_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_single_triplet_resistance_coefficient_m:单个三通阻力系数--凝泵出口母管,的计算180-----------------------------------
  IF OLD.pump_out_resistance_coefficient_m != NEW.pump_out_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_single_triplet_resistance_coefficient_m=20*(NEW.pump_out_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_resistance_coefficient_m ISNULL) AND NEW.pump_out_resistance_coefficient_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_single_triplet_resistance_coefficient_m=20*(NEW.pump_out_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_valve_resistance_coefficient_m:阀门的局部阻力系数--凝泵出口母管,的计算181-----------------------------------
  IF OLD.pump_out_filter_m != NEW.pump_out_filter_m OR OLD.pump_out_sluice_resistance_coefficient_m != NEW.pump_out_sluice_resistance_coefficient_m OR OLD.pump_out_check_resistance_coefficient_m != NEW.pump_out_check_resistance_coefficient_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_valve_resistance_coefficient_m=(NEW.pump_out_filter_m)+(NEW.pump_out_sluice_resistance_coefficient_m)+(NEW.pump_out_check_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_check_resistance_coefficient_m ISNULL OR OLD.pump_out_sluice_resistance_coefficient_m ISNULL OR OLD.pump_out_filter_m ISNULL) AND NEW.pump_out_check_resistance_coefficient_m NOTNULL AND NEW.pump_out_sluice_resistance_coefficient_m NOTNULL AND NEW.pump_out_filter_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_valve_resistance_coefficient_m=(NEW.pump_out_filter_m)+(NEW.pump_out_sluice_resistance_coefficient_m)+(NEW.pump_out_check_resistance_coefficient_m)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段pump_out_plate_resistance_coefficient_m:流量测量孔板阻力系数--凝泵出口母管,的计算182-----------------------------------
  IF OLD.pump_in_msv_m != NEW.pump_in_msv_m OR OLD.pump_out_rated_flow_c != NEW.pump_out_rated_flow_c OR OLD.pump_out_pipe_outer_diameter_m != NEW.pump_out_pipe_outer_diameter_m OR OLD.pump_out_pipe_thickness_m != NEW.pump_out_pipe_thickness_m OR OLD.pump_out_measuring_pressure_loss_m != NEW.pump_out_measuring_pressure_loss_m THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_plate_resistance_coefficient_m=(NEW.pump_out_measuring_pressure_loss_m)/(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.pump_out_measuring_pressure_loss_m ISNULL OR OLD.pump_out_pipe_thickness_m ISNULL OR OLD.pump_out_pipe_outer_diameter_m ISNULL OR OLD.pump_out_rated_flow_c ISNULL OR OLD.pump_in_msv_m ISNULL) AND NEW.pump_out_measuring_pressure_loss_m NOTNULL AND NEW.pump_out_pipe_thickness_m NOTNULL AND NEW.pump_out_pipe_outer_diameter_m NOTNULL AND NEW.pump_out_rated_flow_c NOTNULL AND NEW.pump_in_msv_m NOTNULL THEN
     update gaspowergeneration_steam_water_pipe set 

     pump_out_plate_resistance_coefficient_m=(NEW.pump_out_measuring_pressure_loss_m)/(((0.3537*((NEW.pump_out_rated_flow_c)*4)*((NEW.pump_in_msv_m))/(((NEW.pump_out_pipe_outer_diameter_m)-2*(NEW.pump_out_pipe_thickness_m)))^2))^2/2/((NEW.pump_in_msv_m)))
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_steam_water_pipe" AFTER UPDATE OF
"main_steam_selected_velocity_c",
"l_feedwater_elbow_radius_c",
"l_feedwater_90elbow_count_c",
"l_feedwater_triplet_count_c",
"main_steam_meida_specific_volume_c",
"l_feedwater_converging_spec_c",
"l_feedwater_converging_angle_c",
"l_feedwater_converging_diameter_radio_c",
"l_feedwater_filter_c",
"l_feedwater_sluice_count_c",
"l_feedwater_check_resistance_coefficient_c",
"l_feedwater_plate_resistance_coefficient_c",
"main_steam_temperature_correct_coefficient_c",
"l_feedwater_work_press_m",
"l_feedwater_msv_m",
"l_feedwater_pipe_outer_diameter_m",
"main_steam_stress_correct_coefficient_c",
"l_feedwater_pipe_thickness_m",
"l_feedwater_equivalent_roughness_m",
"l_feedwater_resistance_coefficient_m",
"l_feedwater_pipe_length_m",
"main_steam_additional_thickness_c",
"l_feedwater_90elbow_resistance_coefficient_m",
"l_feedwater_90elbow_count_m",
"l_feedwater_triplet_count_m",
"l_feedwater_reducer_resistance_coefficient_m",
"l_feedwater_in_out_resistance_coefficient_m",
"main_steam_negative_deviation_coefficient_c",
"l_feedwater_filter_m",
"l_feedwater_sluice_resistance_coefficient_m",
"l_feedwater_check_resistance_coefficient_m",
"l_feedwater_regulating_resistance_coefficient_m",
"l_feedwater_plate_resistance_coefficient_m",
"h_feedwater_rated_flow_c",
"h_feedwater_msv_c",
"h_feedwater_media_viscosity_c",
"h_feedwater_pipe_outer_diameter_c",
"h_feedwater_pipe_thickness_c",
"h_feedwater_equivalent_roughness_c",
"h_feedwater_resistance_coefficient_c",
"h_feedwater_pipe_length_c",
"h_feedwater_elbow_radius_c",
"h_feedwater_90elbow_count_c",
"h_feedwater_triplet_count_c",
"h_feedwater_increasing_angle_c",
"h_feedwater_increasing_diameter_radio_c",
"h_feedwater_in_out_resistance_coefficient_c",
"main_steam_selected_outer_diameter_c",
"h_feedwater_filter_c",
"h_feedwater_sluice_count_c",
"h_feedwater_check_count_c",
"h_feedwater_regulating_resistance_coefficient_c",
"h_feedwater_plate_resistance_coefficient_c",
"main_steam_selected_thickness_c",
"h_feedwater_msv_m",
"h_feedwater_pipe_outer_diameter_m",
"h_feedwater_pipe_thickness_m",
"h_feedwater_equivalent_roughness_m",
"h_feedwater_resistance_coefficient_m",
"h_feedwater_pipe_length_m",
"h_feedwater_90elbow_resistance_coefficient_m",
"h_feedwater_90elbow_count_m",
"h_feedwater_triplet_count_m",
"h_feedwater_reducer_resistance_coefficient_m",
"h_feedwater_in_out_resistance_coefficient_m",
"h_feedwater_filter_m",
"h_feedwater_sluice_resistance_coefficient_m",
"h_feedwater_check_resistance_coefficient_m",
"h_feedwater_regulating_resistance_coefficient_m",
"h_feedwater_measuring_pressure_loss_m",
"pump_in_work_press_c",
"pump_in_rated_flow_c",
"pump_in_msv_c",
"pump_in_media_viscosity_c",
"pump_in_pipe_outer_diameter_c",
"main_steam_rated_flow_c",
"pump_in_pipe_thickness_c",
"pump_in_equivalent_roughness_c",
"pump_in_resistance_coefficient_c",
"pump_in_pipe_length_c",
"main_steam_design_pressure_c",
"main_steam_msv_c",
"pump_in_elbow_radius_c",
"pump_in_90elbow_count_c",
"pump_in_triplet_count_c",
"main_steam_media_viscosity_c",
"pump_in_converging_angle_c",
"pump_in_converging_diameter_radio_c",
"pump_in_in_out_resistance_coefficient_c",
"pump_in_filter_c",
"pump_in_sluice_count_c",
"pump_in_check_resistance_coefficient_c",
"pump_in_regulating_resistance_coefficient_c",
"pump_in_plate_resistance_coefficient_c",
"pump_in_work_press_m",
"pump_in_msv_m",
"pump_in_pipe_outer_diameter_m",
"pump_in_pipe_thickness_m",
"pump_in_equivalent_roughness_m",
"pump_in_resistance_coefficient_m",
"pump_in_pipe_length_m",
"main_steam_pipe_outer_diameter_c",
"pump_in_elbow_radius_m",
"pump_in_90elbow_count_m",
"pump_in_triplet_count_m",
"main_steam_pipe_thickness_c",
"pump_in_reducer_resistance_coefficient_m",
"pump_in_in_out_resistance_coefficient_m",
"pump_in_filter_m",
"pump_in_sluice_resistance_coefficient_m",
"pump_in_check_resistance_coefficient_m",
"pump_in_plate_resistance_coefficient_m",
"pump_out_rated_flow_c",
"pump_out_pipe_outer_diameter_c",
"pump_out_pipe_thickness_c",
"pump_out_equivalent_roughness_c",
"pump_out_resistance_coefficient_c",
"pump_out_pipe_length_c",
"main_steam_equivalent_roughness_c",
"pump_out_elbow_radius_c",
"pump_out_90elbow_count_c",
"pump_out_triplet_count_c",
"pump_out_reducer_resistance_coefficient_c",
"pump_out_in_out_resistance_coefficient_c",
"main_steam_resistance_coefficient_c",
"pump_out_filter_c",
"pump_out_sluice_count_c",
"pump_out_check_count_c",
"pump_out_plate_resistance_coefficient_c",
"pump_out_pipe_outer_diameter_m",
"main_steam_pipe_length_c",
"pump_out_pipe_thickness_m",
"pump_out_equivalent_roughness_m",
"pump_out_resistance_coefficient_m",
"pump_out_pipe_length_m",
"pump_out_elbow_radius_m",
"pump_out_90elbow_count_m",
"pump_out_triplet_count_m",
"pump_out_reducer_resistance_coefficient_m",
"pump_out_in_out_resistance_coefficient_m",
"pump_out_filter_m",
"pump_out_sluice_resistance_coefficient_m",
"pump_out_check_resistance_coefficient_m",
"main_steam_msv_m",
"pump_out_measuring_pressure_loss_m",
"main_steam_pipe_outer_diameter_m",
"main_steam_pipe_thickness_m",
"main_steam_equivalent_roughness_m",
"main_steam_temperature_stress_c",
"main_steam_resistance_coefficient_m",
"main_steam_pipe_length_m",
"deoxidized_steam_rated_flow",
"deoxidized_steam_msv",
"deoxidized_steam_media_viscosity",
"main_steam_20c_stress_c",
"deoxidized_steam_pipe_outer_diameter",
"deoxidized_steam_pipe_thickness",
"deoxidized_steam_equivalent_roughness",
"deoxidized_steam_resistance_coefficient",
"deoxidized_steam_pipe_length",
"l_feedwater_work_press_c",
"l_feedwater_rated_flow_c",
"l_feedwater_msv_c",
"l_feedwater_media_viscosity_c",
"l_feedwater_pipe_outer_diameter_c",
"main_steam_pipe_mass_flow_c",
"l_feedwater_pipe_thickness_c",
"l_feedwater_equivalent_roughness_c",
"l_feedwater_resistance_coefficient_c",
"l_feedwater_pipe_length_c"
ON "public"."gaspowergeneration_steam_water_pipe"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_steam_water_pipe"();

