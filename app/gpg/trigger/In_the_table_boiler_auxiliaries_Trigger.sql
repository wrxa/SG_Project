CREATE OR REPLACE FUNCTION gaspowergeneration_boiler_auxiliaries()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段r_sewage_quantity:定期排污水量,的计算1-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation OR OLD.r_emission_rate != NEW.r_emission_rate THEN
     update gaspowergeneration_boiler_auxiliaries set 

     r_sewage_quantity=(NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_emission_rate ISNULL OR OLD.r_boiler_evaporation ISNULL) AND NEW.r_emission_rate NOTNULL AND NEW.r_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     r_sewage_quantity=(NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_volume:排污扩容容积,的计算2-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation OR OLD.r_emission_time != NEW.r_emission_time OR OLD.r_emission_rate != NEW.r_emission_rate OR OLD.r_drum_aturatedwater_enthalpy != NEW.r_drum_aturatedwater_enthalpy OR OLD.r_work_aturatedwater_enthalpy != NEW.r_work_aturatedwater_enthalpy OR OLD.r_work_latentheat_vaporization != NEW.r_work_latentheat_vaporization OR OLD.r_ultimate_strength != NEW.r_ultimate_strength OR OLD.r_affluence_coefficient != NEW.r_affluence_coefficient THEN
     update gaspowergeneration_boiler_auxiliaries set 

     r_volume=60*((NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate))*((NEW.r_drum_aturatedwater_enthalpy)-(NEW.r_work_aturatedwater_enthalpy))/(NEW.r_emission_time)/(NEW.r_ultimate_strength)/(NEW.r_work_latentheat_vaporization)*(NEW.r_affluence_coefficient)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_affluence_coefficient ISNULL OR OLD.r_ultimate_strength ISNULL OR OLD.r_work_latentheat_vaporization ISNULL OR OLD.r_work_aturatedwater_enthalpy ISNULL OR OLD.r_drum_aturatedwater_enthalpy ISNULL OR OLD.r_emission_rate ISNULL OR OLD.r_emission_time ISNULL OR OLD.r_boiler_evaporation ISNULL) AND NEW.r_affluence_coefficient NOTNULL AND NEW.r_ultimate_strength NOTNULL AND NEW.r_work_latentheat_vaporization NOTNULL AND NEW.r_work_aturatedwater_enthalpy NOTNULL AND NEW.r_drum_aturatedwater_enthalpy NOTNULL AND NEW.r_emission_rate NOTNULL AND NEW.r_emission_time NOTNULL AND NEW.r_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     r_volume=60*((NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate))*((NEW.r_drum_aturatedwater_enthalpy)-(NEW.r_work_aturatedwater_enthalpy))/(NEW.r_emission_time)/(NEW.r_ultimate_strength)/(NEW.r_work_latentheat_vaporization)*(NEW.r_affluence_coefficient)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_sewage_quantity:连续排污水量,的计算3-----------------------------------
  IF OLD.c_boiler_evaporation != NEW.c_boiler_evaporation OR OLD.c_emission_rate != NEW.c_emission_rate THEN
     update gaspowergeneration_boiler_auxiliaries set 

     c_sewage_quantity=(NEW.c_boiler_evaporation)*1000*(NEW.c_emission_rate)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_emission_rate ISNULL OR OLD.c_boiler_evaporation ISNULL) AND NEW.c_emission_rate NOTNULL AND NEW.c_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     c_sewage_quantity=(NEW.c_boiler_evaporation)*1000*(NEW.c_emission_rate)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_vaporization_capacity:排污水汽化量,的计算4-----------------------------------
  IF OLD.c_drum_aturatedwater_enthalpy != NEW.c_drum_aturatedwater_enthalpy OR OLD.c_work_aturatedwater_enthalpy != NEW.c_work_aturatedwater_enthalpy OR OLD.c_work_latentheat_vaporization != NEW.c_work_latentheat_vaporization OR OLD.c_steam_dryness != NEW.c_steam_dryness THEN
     update gaspowergeneration_boiler_auxiliaries set 

     c_vaporization_capacity=((NEW.c_drum_aturatedwater_enthalpy)*0.98-(NEW.c_work_aturatedwater_enthalpy))/((NEW.c_steam_dryness)*(NEW.c_work_latentheat_vaporization))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_steam_dryness ISNULL OR OLD.c_work_latentheat_vaporization ISNULL OR OLD.c_work_aturatedwater_enthalpy ISNULL OR OLD.c_drum_aturatedwater_enthalpy ISNULL) AND NEW.c_steam_dryness NOTNULL AND NEW.c_work_latentheat_vaporization NOTNULL AND NEW.c_work_aturatedwater_enthalpy NOTNULL AND NEW.c_drum_aturatedwater_enthalpy NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     c_vaporization_capacity=((NEW.c_drum_aturatedwater_enthalpy)*0.98-(NEW.c_work_aturatedwater_enthalpy))/((NEW.c_steam_dryness)*(NEW.c_work_latentheat_vaporization))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_volume:排污扩容汽容积,的计算5-----------------------------------
  IF OLD.c_boiler_evaporation != NEW.c_boiler_evaporation OR OLD.c_emission_rate != NEW.c_emission_rate OR OLD.c_drum_aturatedwater_enthalpy != NEW.c_drum_aturatedwater_enthalpy OR OLD.c_work_aturatedwater_enthalpy != NEW.c_work_aturatedwater_enthalpy OR OLD.c_work_steam_pecificvolume != NEW.c_work_steam_pecificvolume OR OLD.c_work_latentheat_vaporization != NEW.c_work_latentheat_vaporization OR OLD.c_steam_dryness != NEW.c_steam_dryness OR OLD.c_ultimate_strength != NEW.c_ultimate_strength OR OLD.c_affluence_coefficient != NEW.c_affluence_coefficient THEN
     update gaspowergeneration_boiler_auxiliaries set 

     c_volume=((NEW.c_boiler_evaporation)*1000*(NEW.c_emission_rate))*(((NEW.c_drum_aturatedwater_enthalpy)*0.98-(NEW.c_work_aturatedwater_enthalpy))/((NEW.c_steam_dryness)*(NEW.c_work_latentheat_vaporization)))*(NEW.c_work_steam_pecificvolume)/(NEW.c_ultimate_strength)*(NEW.c_affluence_coefficient)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_affluence_coefficient ISNULL OR OLD.c_ultimate_strength ISNULL OR OLD.c_steam_dryness ISNULL OR OLD.c_work_latentheat_vaporization ISNULL OR OLD.c_work_steam_pecificvolume ISNULL OR OLD.c_work_aturatedwater_enthalpy ISNULL OR OLD.c_drum_aturatedwater_enthalpy ISNULL OR OLD.c_emission_rate ISNULL OR OLD.c_boiler_evaporation ISNULL) AND NEW.c_affluence_coefficient NOTNULL AND NEW.c_ultimate_strength NOTNULL AND NEW.c_steam_dryness NOTNULL AND NEW.c_work_latentheat_vaporization NOTNULL AND NEW.c_work_steam_pecificvolume NOTNULL AND NEW.c_work_aturatedwater_enthalpy NOTNULL AND NEW.c_drum_aturatedwater_enthalpy NOTNULL AND NEW.c_emission_rate NOTNULL AND NEW.c_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     c_volume=((NEW.c_boiler_evaporation)*1000*(NEW.c_emission_rate))*(((NEW.c_drum_aturatedwater_enthalpy)*0.98-(NEW.c_work_aturatedwater_enthalpy))/((NEW.c_steam_dryness)*(NEW.c_work_latentheat_vaporization)))*(NEW.c_work_steam_pecificvolume)/(NEW.c_ultimate_strength)*(NEW.c_affluence_coefficient)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_boiler_dosage_startup:锅炉启动时加药量,的计算6-----------------------------------
  IF OLD.d_boiler_watersystem_volume != NEW.d_boiler_watersystem_volume OR OLD.d_phosphate_content != NEW.d_phosphate_content OR OLD.d_water_hardness != NEW.d_water_hardness OR OLD.d_purity != NEW.d_purity THEN
     update gaspowergeneration_boiler_auxiliaries set 

     d_boiler_dosage_startup=(NEW.d_boiler_watersystem_volume)*((NEW.d_phosphate_content)+28.5*(NEW.d_water_hardness))/250/(NEW.d_purity)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_purity ISNULL OR OLD.d_water_hardness ISNULL OR OLD.d_phosphate_content ISNULL OR OLD.d_boiler_watersystem_volume ISNULL) AND NEW.d_purity NOTNULL AND NEW.d_water_hardness NOTNULL AND NEW.d_phosphate_content NOTNULL AND NEW.d_boiler_watersystem_volume NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     d_boiler_dosage_startup=(NEW.d_boiler_watersystem_volume)*((NEW.d_phosphate_content)+28.5*(NEW.d_water_hardness))/250/(NEW.d_purity)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_boiler_sewage_quantity:锅炉排污量,的计算7-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation OR OLD.r_emission_time != NEW.r_emission_time OR OLD.r_emission_rate != NEW.r_emission_rate OR OLD.r_drum_aturatedwater_enthalpy != NEW.r_drum_aturatedwater_enthalpy OR OLD.r_work_aturatedwater_enthalpy != NEW.r_work_aturatedwater_enthalpy OR OLD.r_work_latentheat_vaporization != NEW.r_work_latentheat_vaporization OR OLD.r_ultimate_strength != NEW.r_ultimate_strength OR OLD.r_affluence_coefficient != NEW.r_affluence_coefficient OR OLD.d_boiler_water_supply != NEW.d_boiler_water_supply THEN
     update gaspowergeneration_boiler_auxiliaries set 

     d_boiler_sewage_quantity=(NEW.d_boiler_water_supply)*(60*((NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate))*((NEW.r_drum_aturatedwater_enthalpy)-(NEW.r_work_aturatedwater_enthalpy))/(NEW.r_emission_time)/(NEW.r_ultimate_strength)/(NEW.r_work_latentheat_vaporization)*(NEW.r_affluence_coefficient))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_boiler_water_supply ISNULL OR OLD.r_affluence_coefficient ISNULL OR OLD.r_ultimate_strength ISNULL OR OLD.r_work_latentheat_vaporization ISNULL OR OLD.r_work_aturatedwater_enthalpy ISNULL OR OLD.r_drum_aturatedwater_enthalpy ISNULL OR OLD.r_emission_rate ISNULL OR OLD.r_emission_time ISNULL OR OLD.r_boiler_evaporation ISNULL) AND NEW.d_boiler_water_supply NOTNULL AND NEW.r_affluence_coefficient NOTNULL AND NEW.r_ultimate_strength NOTNULL AND NEW.r_work_latentheat_vaporization NOTNULL AND NEW.r_work_aturatedwater_enthalpy NOTNULL AND NEW.r_drum_aturatedwater_enthalpy NOTNULL AND NEW.r_emission_rate NOTNULL AND NEW.r_emission_time NOTNULL AND NEW.r_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     d_boiler_sewage_quantity=(NEW.d_boiler_water_supply)*(60*((NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate))*((NEW.r_drum_aturatedwater_enthalpy)-(NEW.r_work_aturatedwater_enthalpy))/(NEW.r_emission_time)/(NEW.r_ultimate_strength)/(NEW.r_work_latentheat_vaporization)*(NEW.r_affluence_coefficient))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_boiler_dosage_run:运行时加药量,的计算8-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation OR OLD.r_emission_time != NEW.r_emission_time OR OLD.r_emission_rate != NEW.r_emission_rate OR OLD.r_drum_aturatedwater_enthalpy != NEW.r_drum_aturatedwater_enthalpy OR OLD.r_work_aturatedwater_enthalpy != NEW.r_work_aturatedwater_enthalpy OR OLD.r_work_latentheat_vaporization != NEW.r_work_latentheat_vaporization OR OLD.r_ultimate_strength != NEW.r_ultimate_strength OR OLD.r_affluence_coefficient != NEW.r_affluence_coefficient OR OLD.d_phosphate_content != NEW.d_phosphate_content OR OLD.d_water_hardness != NEW.d_water_hardness OR OLD.d_purity != NEW.d_purity OR OLD.d_boiler_water_supply != NEW.d_boiler_water_supply THEN
     update gaspowergeneration_boiler_auxiliaries set 

     d_boiler_dosage_run=(28.5*(NEW.d_water_hardness)*(NEW.d_boiler_water_supply)+(NEW.d_phosphate_content)*((NEW.d_boiler_water_supply)*(60*((NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate))*((NEW.r_drum_aturatedwater_enthalpy)-(NEW.r_work_aturatedwater_enthalpy))/(NEW.r_emission_time)/(NEW.r_ultimate_strength)/(NEW.r_work_latentheat_vaporization)*(NEW.r_affluence_coefficient))))/250/(NEW.d_purity)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_boiler_water_supply ISNULL OR OLD.d_purity ISNULL OR OLD.d_water_hardness ISNULL OR OLD.d_phosphate_content ISNULL OR OLD.r_affluence_coefficient ISNULL OR OLD.r_ultimate_strength ISNULL OR OLD.r_work_latentheat_vaporization ISNULL OR OLD.r_work_aturatedwater_enthalpy ISNULL OR OLD.r_drum_aturatedwater_enthalpy ISNULL OR OLD.r_emission_rate ISNULL OR OLD.r_emission_time ISNULL OR OLD.r_boiler_evaporation ISNULL) AND NEW.d_boiler_water_supply NOTNULL AND NEW.d_purity NOTNULL AND NEW.d_water_hardness NOTNULL AND NEW.d_phosphate_content NOTNULL AND NEW.r_affluence_coefficient NOTNULL AND NEW.r_ultimate_strength NOTNULL AND NEW.r_work_latentheat_vaporization NOTNULL AND NEW.r_work_aturatedwater_enthalpy NOTNULL AND NEW.r_drum_aturatedwater_enthalpy NOTNULL AND NEW.r_emission_rate NOTNULL AND NEW.r_emission_time NOTNULL AND NEW.r_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     d_boiler_dosage_run=(28.5*(NEW.d_water_hardness)*(NEW.d_boiler_water_supply)+(NEW.d_phosphate_content)*((NEW.d_boiler_water_supply)*(60*((NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate))*((NEW.r_drum_aturatedwater_enthalpy)-(NEW.r_work_aturatedwater_enthalpy))/(NEW.r_emission_time)/(NEW.r_ultimate_strength)/(NEW.r_work_latentheat_vaporization)*(NEW.r_affluence_coefficient))))/250/(NEW.d_purity)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_solution_quantity_run:运行时汽包内加入的溶液量,的计算9-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation OR OLD.r_emission_time != NEW.r_emission_time OR OLD.r_emission_rate != NEW.r_emission_rate OR OLD.r_drum_aturatedwater_enthalpy != NEW.r_drum_aturatedwater_enthalpy OR OLD.r_work_aturatedwater_enthalpy != NEW.r_work_aturatedwater_enthalpy OR OLD.r_work_latentheat_vaporization != NEW.r_work_latentheat_vaporization OR OLD.r_ultimate_strength != NEW.r_ultimate_strength OR OLD.r_affluence_coefficient != NEW.r_affluence_coefficient OR OLD.d_phosphate_content != NEW.d_phosphate_content OR OLD.d_water_hardness != NEW.d_water_hardness OR OLD.d_purity != NEW.d_purity OR OLD.d_boiler_water_supply != NEW.d_boiler_water_supply OR OLD.d_na3po4_concentration != NEW.d_na3po4_concentration OR OLD.d_na3po4_density != NEW.d_na3po4_density THEN
     update gaspowergeneration_boiler_auxiliaries set 

     d_solution_quantity_run=(((28.5*(NEW.d_water_hardness)*(NEW.d_boiler_water_supply)+(NEW.d_phosphate_content)*((NEW.d_boiler_water_supply)*(60*((NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate))*((NEW.r_drum_aturatedwater_enthalpy)-(NEW.r_work_aturatedwater_enthalpy))/(NEW.r_emission_time)/(NEW.r_ultimate_strength)/(NEW.r_work_latentheat_vaporization)*(NEW.r_affluence_coefficient))))/250/(NEW.d_purity)))/(10*(NEW.d_na3po4_concentration)*(NEW.d_na3po4_density))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_na3po4_density ISNULL OR OLD.d_na3po4_concentration ISNULL OR OLD.d_boiler_water_supply ISNULL OR OLD.d_purity ISNULL OR OLD.d_water_hardness ISNULL OR OLD.d_phosphate_content ISNULL OR OLD.r_affluence_coefficient ISNULL OR OLD.r_ultimate_strength ISNULL OR OLD.r_work_latentheat_vaporization ISNULL OR OLD.r_work_aturatedwater_enthalpy ISNULL OR OLD.r_drum_aturatedwater_enthalpy ISNULL OR OLD.r_emission_rate ISNULL OR OLD.r_emission_time ISNULL OR OLD.r_boiler_evaporation ISNULL) AND NEW.d_na3po4_density NOTNULL AND NEW.d_na3po4_concentration NOTNULL AND NEW.d_boiler_water_supply NOTNULL AND NEW.d_purity NOTNULL AND NEW.d_water_hardness NOTNULL AND NEW.d_phosphate_content NOTNULL AND NEW.r_affluence_coefficient NOTNULL AND NEW.r_ultimate_strength NOTNULL AND NEW.r_work_latentheat_vaporization NOTNULL AND NEW.r_work_aturatedwater_enthalpy NOTNULL AND NEW.r_drum_aturatedwater_enthalpy NOTNULL AND NEW.r_emission_rate NOTNULL AND NEW.r_emission_time NOTNULL AND NEW.r_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     d_solution_quantity_run=(((28.5*(NEW.d_water_hardness)*(NEW.d_boiler_water_supply)+(NEW.d_phosphate_content)*((NEW.d_boiler_water_supply)*(60*((NEW.r_boiler_evaporation)*1000*(NEW.r_emission_rate))*((NEW.r_drum_aturatedwater_enthalpy)-(NEW.r_work_aturatedwater_enthalpy))/(NEW.r_emission_time)/(NEW.r_ultimate_strength)/(NEW.r_work_latentheat_vaporization)*(NEW.r_affluence_coefficient))))/250/(NEW.d_purity)))/(10*(NEW.d_na3po4_concentration)*(NEW.d_na3po4_density))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_feedpump_total_head:给水泵总扬程,的计算10-----------------------------------
  IF OLD.p_inlet_pressure != NEW.p_inlet_pressure OR OLD.p_deaerator_pressure != NEW.p_deaerator_pressure OR OLD.p_water_supply_resistance != NEW.p_water_supply_resistance OR OLD.p_water_inlet_resistance != NEW.p_water_inlet_resistance OR OLD.p_center_altitude_difference != NEW.p_center_altitude_difference OR OLD.p_deaerator_altitude_difference != NEW.p_deaerator_altitude_difference THEN
     update gaspowergeneration_boiler_auxiliaries set 

     p_feedpump_total_head=((NEW.p_inlet_pressure)-(NEW.p_deaerator_pressure))*102+1.2*((NEW.p_water_supply_resistance)+(NEW.p_water_inlet_resistance))+(NEW.p_center_altitude_difference)-(NEW.p_deaerator_altitude_difference)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_deaerator_altitude_difference ISNULL OR OLD.p_center_altitude_difference ISNULL OR OLD.p_water_inlet_resistance ISNULL OR OLD.p_water_supply_resistance ISNULL OR OLD.p_deaerator_pressure ISNULL OR OLD.p_inlet_pressure ISNULL) AND NEW.p_deaerator_altitude_difference NOTNULL AND NEW.p_center_altitude_difference NOTNULL AND NEW.p_water_inlet_resistance NOTNULL AND NEW.p_water_supply_resistance NOTNULL AND NEW.p_deaerator_pressure NOTNULL AND NEW.p_inlet_pressure NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     p_feedpump_total_head=((NEW.p_inlet_pressure)-(NEW.p_deaerator_pressure))*102+1.2*((NEW.p_water_supply_resistance)+(NEW.p_water_inlet_resistance))+(NEW.p_center_altitude_difference)-(NEW.p_deaerator_altitude_difference)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_auxiliary_motor_power:配套电机功率,的计算11-----------------------------------
  IF OLD.p_inlet_pressure != NEW.p_inlet_pressure OR OLD.p_deaerator_pressure != NEW.p_deaerator_pressure OR OLD.p_water_supply_resistance != NEW.p_water_supply_resistance OR OLD.p_water_inlet_resistance != NEW.p_water_inlet_resistance OR OLD.p_center_altitude_difference != NEW.p_center_altitude_difference OR OLD.p_deaerator_altitude_difference != NEW.p_deaerator_altitude_difference OR OLD.p_flow != NEW.p_flow THEN
     update gaspowergeneration_boiler_auxiliaries set 

     p_auxiliary_motor_power=1.15*1000*9.8*(((NEW.p_inlet_pressure)-(NEW.p_deaerator_pressure))*102+1.2*((NEW.p_water_supply_resistance)+(NEW.p_water_inlet_resistance))+(NEW.p_center_altitude_difference)-(NEW.p_deaerator_altitude_difference))*1.15*(NEW.p_flow)/3600/1000/0.7/0.98/0.9
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_flow ISNULL OR OLD.p_deaerator_altitude_difference ISNULL OR OLD.p_center_altitude_difference ISNULL OR OLD.p_water_inlet_resistance ISNULL OR OLD.p_water_supply_resistance ISNULL OR OLD.p_deaerator_pressure ISNULL OR OLD.p_inlet_pressure ISNULL) AND NEW.p_flow NOTNULL AND NEW.p_deaerator_altitude_difference NOTNULL AND NEW.p_center_altitude_difference NOTNULL AND NEW.p_water_inlet_resistance NOTNULL AND NEW.p_water_supply_resistance NOTNULL AND NEW.p_deaerator_pressure NOTNULL AND NEW.p_inlet_pressure NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     p_auxiliary_motor_power=1.15*1000*9.8*(((NEW.p_inlet_pressure)-(NEW.p_deaerator_pressure))*102+1.2*((NEW.p_water_supply_resistance)+(NEW.p_water_inlet_resistance))+(NEW.p_center_altitude_difference)-(NEW.p_deaerator_altitude_difference))*1.15*(NEW.p_flow)/3600/1000/0.7/0.98/0.9
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_steamwater_cycle_loss:厂内汽水循环损失,的计算12-----------------------------------
  IF OLD.m_boiler_evaporation != NEW.m_boiler_evaporation OR OLD.m_makeup_steam != NEW.m_makeup_steam THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_steamwater_cycle_loss=0.03*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_makeup_steam ISNULL OR OLD.m_boiler_evaporation ISNULL) AND NEW.m_makeup_steam NOTNULL AND NEW.m_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_steamwater_cycle_loss=0.03*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_pollution_loss:排污损失,的计算13-----------------------------------
  IF OLD.m_boiler_evaporation != NEW.m_boiler_evaporation OR OLD.m_makeup_steam != NEW.m_makeup_steam THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_pollution_loss=0.02*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_makeup_steam ISNULL OR OLD.m_boiler_evaporation ISNULL) AND NEW.m_makeup_steam NOTNULL AND NEW.m_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_pollution_loss=0.02*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_condensate_loss:换热凝结水损失,的计算14-----------------------------------
  IF OLD.m_condensing_capacity != NEW.m_condensing_capacity THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_condensate_loss=0.02*(NEW.m_condensing_capacity)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_condensing_capacity ISNULL) AND NEW.m_condensing_capacity NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_condensate_loss=0.02*(NEW.m_condensing_capacity)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_boiler_normal_watersupply:锅炉正常补水量,的计算15-----------------------------------
  IF OLD.m_boiler_evaporation != NEW.m_boiler_evaporation OR OLD.m_makeup_steam != NEW.m_makeup_steam OR OLD.m_condensing_capacity != NEW.m_condensing_capacity THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_boiler_normal_watersupply=(0.03*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+(0.02*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+(0.02*(NEW.m_condensing_capacity))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_condensing_capacity ISNULL OR OLD.m_makeup_steam ISNULL OR OLD.m_boiler_evaporation ISNULL) AND NEW.m_condensing_capacity NOTNULL AND NEW.m_makeup_steam NOTNULL AND NEW.m_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_boiler_normal_watersupply=(0.03*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+(0.02*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+(0.02*(NEW.m_condensing_capacity))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_increase_loss:启动或事故增加损失,的计算16-----------------------------------
  IF OLD.m_boiler_evaporation != NEW.m_boiler_evaporation OR OLD.m_makeup_steam != NEW.m_makeup_steam THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_increase_loss=0.1*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_makeup_steam ISNULL OR OLD.m_boiler_evaporation ISNULL) AND NEW.m_makeup_steam NOTNULL AND NEW.m_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_increase_loss=0.1*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_boiler_max_watersupply:锅炉最大补水量,的计算17-----------------------------------
  IF OLD.m_boiler_evaporation != NEW.m_boiler_evaporation OR OLD.m_makeup_steam != NEW.m_makeup_steam OR OLD.m_condensing_capacity != NEW.m_condensing_capacity THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_boiler_max_watersupply=(0.1*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+((0.03*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+(0.02*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+(0.02*(NEW.m_condensing_capacity)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_condensing_capacity ISNULL OR OLD.m_makeup_steam ISNULL OR OLD.m_boiler_evaporation ISNULL) AND NEW.m_condensing_capacity NOTNULL AND NEW.m_makeup_steam NOTNULL AND NEW.m_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     m_boiler_max_watersupply=(0.1*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+((0.03*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+(0.02*((NEW.m_boiler_evaporation)+(NEW.m_makeup_steam)))+(0.02*(NEW.m_condensing_capacity)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_volume:容积,的计算18-----------------------------------
  IF OLD.s_boiler_evaporation != NEW.s_boiler_evaporation OR OLD.s_storage_time != NEW.s_storage_time THEN
     update gaspowergeneration_boiler_auxiliaries set 

     s_volume=(NEW.s_boiler_evaporation)*(NEW.s_storage_time)/60
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_storage_time ISNULL OR OLD.s_boiler_evaporation ISNULL) AND NEW.s_storage_time NOTNULL AND NEW.s_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     s_volume=(NEW.s_boiler_evaporation)*(NEW.s_storage_time)/60
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_size_diameter:直径,的计算19-----------------------------------
  IF OLD.s_boiler_evaporation != NEW.s_boiler_evaporation OR OLD.s_storage_time != NEW.s_storage_time OR OLD.s_size_length != NEW.s_size_length THEN
     update gaspowergeneration_boiler_auxiliaries set 

     s_size_diameter=2*sqrt(((NEW.s_boiler_evaporation)*(NEW.s_storage_time)/60)/(NEW.s_size_length)/3.14)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_size_length ISNULL OR OLD.s_storage_time ISNULL OR OLD.s_boiler_evaporation ISNULL) AND NEW.s_size_length NOTNULL AND NEW.s_storage_time NOTNULL AND NEW.s_boiler_evaporation NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     s_size_diameter=2*sqrt(((NEW.s_boiler_evaporation)*(NEW.s_storage_time)/60)/(NEW.s_size_length)/3.14)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_design_flux:设计流量,的计算20-----------------------------------
  IF OLD.s_max_feedwater_amount != NEW.s_max_feedwater_amount OR OLD.s_local_atmosphere_density != NEW.s_local_atmosphere_density THEN
     update gaspowergeneration_boiler_auxiliaries set 

     s_design_flux=(NEW.s_max_feedwater_amount)*1000/(NEW.s_local_atmosphere_density)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_local_atmosphere_density ISNULL OR OLD.s_max_feedwater_amount ISNULL) AND NEW.s_local_atmosphere_density NOTNULL AND NEW.s_max_feedwater_amount NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     s_design_flux=(NEW.s_max_feedwater_amount)*1000/(NEW.s_local_atmosphere_density)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_pump_install_height:泵安装高度,的计算21-----------------------------------
  IF OLD.s_net_positive_suction_head != NEW.s_net_positive_suction_head OR OLD.s_total_resistance != NEW.s_total_resistance OR OLD.s_inlet_speed != NEW.s_inlet_speed OR OLD.s_added_height != NEW.s_added_height THEN
     update gaspowergeneration_boiler_auxiliaries set 

     s_pump_install_height=10.09-(NEW.s_net_positive_suction_head)+(NEW.s_total_resistance)+(NEW.s_inlet_speed)*(NEW.s_inlet_speed)/2/9.8+(NEW.s_added_height)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_added_height ISNULL OR OLD.s_inlet_speed ISNULL OR OLD.s_total_resistance ISNULL OR OLD.s_net_positive_suction_head ISNULL) AND NEW.s_added_height NOTNULL AND NEW.s_inlet_speed NOTNULL AND NEW.s_total_resistance NOTNULL AND NEW.s_net_positive_suction_head NOTNULL THEN
     update gaspowergeneration_boiler_auxiliaries set 

     s_pump_install_height=10.09-(NEW.s_net_positive_suction_head)+(NEW.s_total_resistance)+(NEW.s_inlet_speed)*(NEW.s_inlet_speed)/2/9.8+(NEW.s_added_height)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_boiler_auxiliaries" AFTER UPDATE OF
"r_boiler_evaporation",
"r_emission_time",
"r_emission_rate",
"r_drum_aturatedwater_enthalpy",
"r_work_aturatedwater_enthalpy",
"r_work_latentheat_vaporization",
"r_ultimate_strength",
"r_affluence_coefficient",
"c_boiler_evaporation",
"c_emission_rate",
"c_drum_aturatedwater_enthalpy",
"c_work_aturatedwater_enthalpy",
"c_work_steam_pecificvolume",
"c_work_latentheat_vaporization",
"c_steam_dryness",
"c_ultimate_strength",
"c_affluence_coefficient",
"d_boiler_watersystem_volume",
"d_phosphate_content",
"d_water_hardness",
"d_purity",
"d_boiler_water_supply",
"d_na3po4_concentration",
"d_na3po4_density",
"p_inlet_pressure",
"p_deaerator_pressure",
"p_water_supply_resistance",
"p_water_inlet_resistance",
"p_center_altitude_difference",
"p_deaerator_altitude_difference",
"p_flow",
"m_boiler_evaporation",
"m_makeup_steam",
"m_condensing_capacity",
"s_boiler_evaporation",
"s_storage_time",
"s_size_length",
"s_max_feedwater_amount",
"s_local_atmosphere_density",
"s_net_positive_suction_head",
"s_total_resistance",
"s_inlet_speed",
"s_added_height"
ON "public"."gaspowergeneration_boiler_auxiliaries"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_boiler_auxiliaries"();

