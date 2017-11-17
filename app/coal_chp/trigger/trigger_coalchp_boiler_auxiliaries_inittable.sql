CREATE OR REPLACE FUNCTION coalchp_boiler_auxiliaries()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段r_sewage_quantity:定期排污水量,的计算1-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation OR OLD.r_emission_rate != NEW.r_emission_rate THEN
     update coalchp_boiler_auxiliaries set 

     r_sewage_quantity=NEW.r_boiler_evaporation*1000*NEW.r_emission_rate
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_emission_rate ISNULL OR OLD.r_boiler_evaporation ISNULL) AND NEW.r_emission_rate NOTNULL AND NEW.r_boiler_evaporation NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     r_sewage_quantity=NEW.r_boiler_evaporation*1000*NEW.r_emission_rate
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_volume:排污扩容容积,的计算2-----------------------------------
  IF OLD.r_emission_time != NEW.r_emission_time OR OLD.r_sewage_quantity != NEW.r_sewage_quantity OR OLD.r_drum_aturatedwater_enthalpy != NEW.r_drum_aturatedwater_enthalpy OR OLD.r_work_aturatedwater_enthalpy != NEW.r_work_aturatedwater_enthalpy OR OLD.r_work_latentheat_vaporization != NEW.r_work_latentheat_vaporization OR OLD.r_ultimate_strength != NEW.r_ultimate_strength OR OLD.r_affluence_coefficient != NEW.r_affluence_coefficient THEN
     update coalchp_boiler_auxiliaries set 

     r_volume=60*NEW.r_sewage_quantity*(NEW.r_drum_aturatedwater_enthalpy-NEW.r_work_aturatedwater_enthalpy)/NEW.r_emission_time/NEW.r_ultimate_strength/NEW.r_work_latentheat_vaporization*NEW.r_affluence_coefficient
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_affluence_coefficient ISNULL OR OLD.r_ultimate_strength ISNULL OR OLD.r_work_latentheat_vaporization ISNULL OR OLD.r_work_aturatedwater_enthalpy ISNULL OR OLD.r_drum_aturatedwater_enthalpy ISNULL OR OLD.r_sewage_quantity ISNULL OR OLD.r_emission_time ISNULL) AND NEW.r_affluence_coefficient NOTNULL AND NEW.r_ultimate_strength NOTNULL AND NEW.r_work_latentheat_vaporization NOTNULL AND NEW.r_work_aturatedwater_enthalpy NOTNULL AND NEW.r_drum_aturatedwater_enthalpy NOTNULL AND NEW.r_sewage_quantity NOTNULL AND NEW.r_emission_time NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     r_volume=60*NEW.r_sewage_quantity*(NEW.r_drum_aturatedwater_enthalpy-NEW.r_work_aturatedwater_enthalpy)/NEW.r_emission_time/NEW.r_ultimate_strength/NEW.r_work_latentheat_vaporization*NEW.r_affluence_coefficient
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_boiler_evaporation:锅炉蒸发量,的计算3-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation THEN
     update coalchp_boiler_auxiliaries set 

     c_boiler_evaporation=NEW.r_boiler_evaporation
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_boiler_evaporation ISNULL) AND NEW.r_boiler_evaporation NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     c_boiler_evaporation=NEW.r_boiler_evaporation
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_sewage_quantity:连续排污水量,的计算4-----------------------------------
  IF OLD.c_boiler_evaporation != NEW.c_boiler_evaporation OR OLD.c_emission_rate != NEW.c_emission_rate THEN
     update coalchp_boiler_auxiliaries set 

     c_sewage_quantity=NEW.c_boiler_evaporation*1000*NEW.c_emission_rate
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_emission_rate ISNULL OR OLD.c_boiler_evaporation ISNULL) AND NEW.c_emission_rate NOTNULL AND NEW.c_boiler_evaporation NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     c_sewage_quantity=NEW.c_boiler_evaporation*1000*NEW.c_emission_rate
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_drum_pressure:汽包压力,的计算5-----------------------------------
  IF OLD.r_drum_pressure != NEW.r_drum_pressure THEN
     update coalchp_boiler_auxiliaries set 

     c_drum_pressure=NEW.r_drum_pressure
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_drum_pressure ISNULL) AND NEW.r_drum_pressure NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     c_drum_pressure=NEW.r_drum_pressure
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_vaporization_capacity:排污水汽化量,的计算6-----------------------------------
  IF OLD.c_sewage_quantity != NEW.c_sewage_quantity OR OLD.c_drum_aturatedwater_enthalpy != NEW.c_drum_aturatedwater_enthalpy OR OLD.c_work_aturatedwater_enthalpy != NEW.c_work_aturatedwater_enthalpy OR OLD.c_steam_dryness != NEW.c_steam_dryness OR OLD.c_affluence_coefficient != NEW.c_affluence_coefficient THEN
     update coalchp_boiler_auxiliaries set 

     c_vaporization_capacity=NEW.c_sewage_quantity*(NEW.c_drum_aturatedwater_enthalpy-NEW.c_work_aturatedwater_enthalpy)/NEW.c_steam_dryness/NEW.c_affluence_coefficient
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_affluence_coefficient ISNULL OR OLD.c_steam_dryness ISNULL OR OLD.c_work_aturatedwater_enthalpy ISNULL OR OLD.c_drum_aturatedwater_enthalpy ISNULL OR OLD.c_sewage_quantity ISNULL) AND NEW.c_affluence_coefficient NOTNULL AND NEW.c_steam_dryness NOTNULL AND NEW.c_work_aturatedwater_enthalpy NOTNULL AND NEW.c_drum_aturatedwater_enthalpy NOTNULL AND NEW.c_sewage_quantity NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     c_vaporization_capacity=NEW.c_sewage_quantity*(NEW.c_drum_aturatedwater_enthalpy-NEW.c_work_aturatedwater_enthalpy)/NEW.c_steam_dryness/NEW.c_affluence_coefficient
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段c_specifications:选取,的计算7-----------------------------------
  IF OLD.c_work_steam_pecificvolume != NEW.c_work_steam_pecificvolume OR OLD.c_ultimate_strength != NEW.c_ultimate_strength OR OLD.c_vaporization_capacity != NEW.c_vaporization_capacity OR OLD.c_volume != NEW.c_volume THEN
     update coalchp_boiler_auxiliaries set 

     c_specifications=(1+0.25)*NEW.c_vaporization_capacity*NEW.c_work_steam_pecificvolume/NEW.c_ultimate_strength*NEW.c_volume
     where plan_id=NEW.plan_id;

  ELSIF (OLD.c_volume ISNULL OR OLD.c_vaporization_capacity ISNULL OR OLD.c_ultimate_strength ISNULL OR OLD.c_work_steam_pecificvolume ISNULL) AND NEW.c_volume NOTNULL AND NEW.c_vaporization_capacity NOTNULL AND NEW.c_ultimate_strength NOTNULL AND NEW.c_work_steam_pecificvolume NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     c_specifications=(1+0.25)*NEW.c_vaporization_capacity*NEW.c_work_steam_pecificvolume/NEW.c_ultimate_strength*NEW.c_volume
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_boiler_dosage_startup:锅炉启动时加药量,的计算8-----------------------------------
  IF OLD.d_boiler_watersystem_volume != NEW.d_boiler_watersystem_volume OR OLD.d_phosphate_content != NEW.d_phosphate_content OR OLD.d_water_hardness != NEW.d_water_hardness OR OLD.d_purity != NEW.d_purity THEN
     update coalchp_boiler_auxiliaries set 

     d_boiler_dosage_startup=NEW.d_boiler_watersystem_volume*(NEW.d_phosphate_content+28.5*NEW.d_water_hardness)/250/NEW.d_purity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_purity ISNULL OR OLD.d_water_hardness ISNULL OR OLD.d_phosphate_content ISNULL OR OLD.d_boiler_watersystem_volume ISNULL) AND NEW.d_purity NOTNULL AND NEW.d_water_hardness NOTNULL AND NEW.d_phosphate_content NOTNULL AND NEW.d_boiler_watersystem_volume NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     d_boiler_dosage_startup=NEW.d_boiler_watersystem_volume*(NEW.d_phosphate_content+28.5*NEW.d_water_hardness)/250/NEW.d_purity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_boiler_sewage_quantity:锅炉排污量,的计算9-----------------------------------
  IF OLD.c_emission_rate != NEW.c_emission_rate OR OLD.d_boiler_water_supply != NEW.d_boiler_water_supply THEN
     update coalchp_boiler_auxiliaries set 

     d_boiler_sewage_quantity=NEW.d_boiler_water_supply*NEW.c_emission_rate
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_boiler_water_supply ISNULL OR OLD.c_emission_rate ISNULL) AND NEW.d_boiler_water_supply NOTNULL AND NEW.c_emission_rate NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     d_boiler_sewage_quantity=NEW.d_boiler_water_supply*NEW.c_emission_rate
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_boiler_dosage_run:运行时加药量,的计算10-----------------------------------
  IF OLD.d_phosphate_content != NEW.d_phosphate_content OR OLD.d_water_hardness != NEW.d_water_hardness OR OLD.d_purity != NEW.d_purity OR OLD.d_boiler_water_supply != NEW.d_boiler_water_supply OR OLD.d_boiler_sewage_quantity != NEW.d_boiler_sewage_quantity THEN
     update coalchp_boiler_auxiliaries set 

     d_boiler_dosage_run=(28.5*NEW.d_water_hardness*NEW.d_boiler_water_supply+NEW.d_phosphate_content*NEW.d_boiler_sewage_quantity)/250/NEW.d_purity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_boiler_sewage_quantity ISNULL OR OLD.d_boiler_water_supply ISNULL OR OLD.d_purity ISNULL OR OLD.d_water_hardness ISNULL OR OLD.d_phosphate_content ISNULL) AND NEW.d_boiler_sewage_quantity NOTNULL AND NEW.d_boiler_water_supply NOTNULL AND NEW.d_purity NOTNULL AND NEW.d_water_hardness NOTNULL AND NEW.d_phosphate_content NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     d_boiler_dosage_run=(28.5*NEW.d_water_hardness*NEW.d_boiler_water_supply+NEW.d_phosphate_content*NEW.d_boiler_sewage_quantity)/250/NEW.d_purity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_solution_quantity_run:运行时汽包内加入的溶液量,的计算11-----------------------------------
  IF OLD.d_boiler_dosage_run != NEW.d_boiler_dosage_run OR OLD.d_na3po4_concentration != NEW.d_na3po4_concentration OR OLD.d_na3po4_density != NEW.d_na3po4_density THEN
     update coalchp_boiler_auxiliaries set 

     d_solution_quantity_run=(NEW.d_boiler_dosage_run)/(10*NEW.d_na3po4_concentration*NEW.d_na3po4_density)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_na3po4_density ISNULL OR OLD.d_na3po4_concentration ISNULL OR OLD.d_boiler_dosage_run ISNULL) AND NEW.d_na3po4_density NOTNULL AND NEW.d_na3po4_concentration NOTNULL AND NEW.d_boiler_dosage_run NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     d_solution_quantity_run=(NEW.d_boiler_dosage_run)/(10*NEW.d_na3po4_concentration*NEW.d_na3po4_density)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_feedpump_total_head:给水泵总扬程,的计算12-----------------------------------
  IF OLD.p_inlet_pressure != NEW.p_inlet_pressure OR OLD.p_deaerator_pressure != NEW.p_deaerator_pressure OR OLD.p_water_supply_resistance != NEW.p_water_supply_resistance OR OLD.p_water_inlet_resistance != NEW.p_water_inlet_resistance OR OLD.p_center_altitude_difference != NEW.p_center_altitude_difference OR OLD.p_deaerator_altitude_difference != NEW.p_deaerator_altitude_difference THEN
     update coalchp_boiler_auxiliaries set 

     p_feedpump_total_head=(NEW.p_inlet_pressure-NEW.p_deaerator_pressure)*102+1.2*(NEW.p_water_supply_resistance+NEW.p_water_inlet_resistance)+NEW.p_center_altitude_difference-NEW.p_deaerator_altitude_difference
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_deaerator_altitude_difference ISNULL OR OLD.p_center_altitude_difference ISNULL OR OLD.p_water_inlet_resistance ISNULL OR OLD.p_water_supply_resistance ISNULL OR OLD.p_deaerator_pressure ISNULL OR OLD.p_inlet_pressure ISNULL) AND NEW.p_deaerator_altitude_difference NOTNULL AND NEW.p_center_altitude_difference NOTNULL AND NEW.p_water_inlet_resistance NOTNULL AND NEW.p_water_supply_resistance NOTNULL AND NEW.p_deaerator_pressure NOTNULL AND NEW.p_inlet_pressure NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     p_feedpump_total_head=(NEW.p_inlet_pressure-NEW.p_deaerator_pressure)*102+1.2*(NEW.p_water_supply_resistance+NEW.p_water_inlet_resistance)+NEW.p_center_altitude_difference-NEW.p_deaerator_altitude_difference
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_specifications:给水泵选用规格,的计算13-----------------------------------
  IF OLD.p_feedpump_total_head != NEW.p_feedpump_total_head OR OLD.p_flow != NEW.p_flow THEN
     update coalchp_boiler_auxiliaries set 

     p_specifications=1.15*1000*9.8*NEW.p_feedpump_total_head*1.15*NEW.p_flow/3600/1000/0.7/0.98/0.9
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_flow ISNULL OR OLD.p_feedpump_total_head ISNULL) AND NEW.p_flow NOTNULL AND NEW.p_feedpump_total_head NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     p_specifications=1.15*1000*9.8*NEW.p_feedpump_total_head*1.15*NEW.p_flow/3600/1000/0.7/0.98/0.9
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_boiler_evaporation:锅炉蒸发量,的计算14-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation THEN
     update coalchp_boiler_auxiliaries set 

     m_boiler_evaporation=NEW.r_boiler_evaporation
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_boiler_evaporation ISNULL) AND NEW.r_boiler_evaporation NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     m_boiler_evaporation=NEW.r_boiler_evaporation
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_steamwater_cycle_loss:厂内汽水循环损失,的计算15-----------------------------------
  IF OLD.m_boiler_evaporation != NEW.m_boiler_evaporation OR OLD.m_makeup_steam != NEW.m_makeup_steam THEN
     update coalchp_boiler_auxiliaries set 

     m_steamwater_cycle_loss=0.03*(NEW.m_boiler_evaporation+NEW.m_makeup_steam)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_makeup_steam ISNULL OR OLD.m_boiler_evaporation ISNULL) AND NEW.m_makeup_steam NOTNULL AND NEW.m_boiler_evaporation NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     m_steamwater_cycle_loss=0.03*(NEW.m_boiler_evaporation+NEW.m_makeup_steam)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_pollution_loss:排污损失,的计算16-----------------------------------
  IF OLD.m_boiler_evaporation != NEW.m_boiler_evaporation OR OLD.m_makeup_steam != NEW.m_makeup_steam THEN
     update coalchp_boiler_auxiliaries set 

     m_pollution_loss=0.02*(NEW.m_boiler_evaporation+NEW.m_makeup_steam)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_makeup_steam ISNULL OR OLD.m_boiler_evaporation ISNULL) AND NEW.m_makeup_steam NOTNULL AND NEW.m_boiler_evaporation NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     m_pollution_loss=0.02*(NEW.m_boiler_evaporation+NEW.m_makeup_steam)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_condensate_loss:换热凝结水损失,的计算17-----------------------------------
  IF OLD.m_condensing_capacity != NEW.m_condensing_capacity THEN
     update coalchp_boiler_auxiliaries set 

     m_condensate_loss=0.02*NEW.m_condensing_capacity
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_condensing_capacity ISNULL) AND NEW.m_condensing_capacity NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     m_condensate_loss=0.02*NEW.m_condensing_capacity
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_boiler_normal_watersupply:锅炉正常补水量,的计算18-----------------------------------
  IF OLD.m_steamwater_cycle_loss != NEW.m_steamwater_cycle_loss OR OLD.m_pollution_loss != NEW.m_pollution_loss OR OLD.m_condensate_loss != NEW.m_condensate_loss THEN
     update coalchp_boiler_auxiliaries set 

     m_boiler_normal_watersupply=NEW.m_steamwater_cycle_loss+NEW.m_pollution_loss+NEW.m_condensate_loss
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_condensate_loss ISNULL OR OLD.m_pollution_loss ISNULL OR OLD.m_steamwater_cycle_loss ISNULL) AND NEW.m_condensate_loss NOTNULL AND NEW.m_pollution_loss NOTNULL AND NEW.m_steamwater_cycle_loss NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     m_boiler_normal_watersupply=NEW.m_steamwater_cycle_loss+NEW.m_pollution_loss+NEW.m_condensate_loss
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_increase_loss:启动或事故增加损失,的计算19-----------------------------------
  IF OLD.m_boiler_evaporation != NEW.m_boiler_evaporation OR OLD.m_makeup_steam != NEW.m_makeup_steam THEN
     update coalchp_boiler_auxiliaries set 

     m_increase_loss=0.1*(NEW.m_boiler_evaporation+NEW.m_makeup_steam)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_makeup_steam ISNULL OR OLD.m_boiler_evaporation ISNULL) AND NEW.m_makeup_steam NOTNULL AND NEW.m_boiler_evaporation NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     m_increase_loss=0.1*(NEW.m_boiler_evaporation+NEW.m_makeup_steam)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段m_boiler_max_watersupply:锅炉最大补水量,的计算20-----------------------------------
  IF OLD.m_boiler_normal_watersupply != NEW.m_boiler_normal_watersupply OR OLD.m_increase_loss != NEW.m_increase_loss THEN
     update coalchp_boiler_auxiliaries set 

     m_boiler_max_watersupply=NEW.m_increase_loss+NEW.m_boiler_normal_watersupply
     where plan_id=NEW.plan_id;

  ELSIF (OLD.m_increase_loss ISNULL OR OLD.m_boiler_normal_watersupply ISNULL) AND NEW.m_increase_loss NOTNULL AND NEW.m_boiler_normal_watersupply NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     m_boiler_max_watersupply=NEW.m_increase_loss+NEW.m_boiler_normal_watersupply
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_boiler_evaporation:锅炉蒸发量,的计算21-----------------------------------
  IF OLD.r_boiler_evaporation != NEW.r_boiler_evaporation THEN
     update coalchp_boiler_auxiliaries set 

     s_boiler_evaporation=NEW.r_boiler_evaporation
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_boiler_evaporation ISNULL) AND NEW.r_boiler_evaporation NOTNULL THEN
     update coalchp_boiler_auxiliaries set 

     s_boiler_evaporation=NEW.r_boiler_evaporation
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_boiler_auxiliaries" AFTER UPDATE OF
"r_boiler_evaporation",
"r_emission_time",
"r_emission_rate",
"r_sewage_quantity",
"r_drum_pressure",
"r_drum_aturatedwater_enthalpy",
"r_work_aturatedwater_enthalpy",
"r_work_latentheat_vaporization",
"r_ultimate_strength",
"r_affluence_coefficient",
"c_boiler_evaporation",
"c_emission_rate",
"c_sewage_quantity",
"c_drum_aturatedwater_enthalpy",
"c_work_aturatedwater_enthalpy",
"c_work_steam_pecificvolume",
"c_steam_dryness",
"c_ultimate_strength",
"c_vaporization_capacity",
"c_affluence_coefficient",
"c_volume",
"d_boiler_watersystem_volume",
"d_phosphate_content",
"d_water_hardness",
"d_purity",
"d_boiler_water_supply",
"d_boiler_sewage_quantity",
"d_boiler_dosage_run",
"d_na3po4_concentration",
"d_na3po4_density",
"p_inlet_pressure",
"p_deaerator_pressure",
"p_water_supply_resistance",
"p_water_inlet_resistance",
"p_center_altitude_difference",
"p_deaerator_altitude_difference",
"p_feedpump_total_head",
"p_flow",
"m_boiler_evaporation",
"m_makeup_steam",
"m_steamwater_cycle_loss",
"m_pollution_loss",
"m_condensing_capacity",
"m_condensate_loss",
"m_boiler_normal_watersupply",
"m_increase_loss"
ON "public"."coalchp_boiler_auxiliaries"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_boiler_auxiliaries"();
