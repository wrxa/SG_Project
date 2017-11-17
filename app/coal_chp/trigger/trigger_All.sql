CREATE OR REPLACE FUNCTION plan_id_insert()
RETURNS TRIGGER AS
$BODY$
DECLARE
  NEWIDD integer;
  MODULEID varchar(200);

BEGIN
    NEWIDD = NEW.id;
    MODULEID = NEW.module_id;
-- 燃煤热电联产
		IF TG_OP='INSERT' AND MODULEID='coalCHP' THEN

		    INSERT INTO coalchp_needs_questionnaire (plan_id) VALUES (NEWIDD);
		    INSERT INTO coalchp_furnace_calculation (plan_id) VALUES (NEWIDD);
		    INSERT INTO coalchp_coal_handingsystem (plan_id) VALUES (NEWIDD);
		    INSERT INTO coalchp_removal_ash_slag_system (plan_id) VALUES (NEWIDD);
		    INSERT INTO coalchp_desulfurization_denitrification (plan_id) VALUES (NEWIDD);
		    INSERT INTO coalchp_circulating_water (plan_id) VALUES (NEWIDD);
		    INSERT INTO coalchp_smoke_air_system (plan_id) VALUES (NEWIDD);
        INSERT INTO coalchp_boiler_auxiliaries (plan_id) VALUES (NEWIDD);
		    RETURN NULL;
-- 生物质热电联产
		ELSEIF TG_OP='INSERT' AND MODULEID='biomassCHP' THEN

		    INSERT INTO biomasschp_needs_questionnaire (plan_id) VALUES (NEWIDD);
		    INSERT INTO biomasschp_boiler_calculation (plan_id) VALUES (NEWIDD);
		    INSERT INTO biomasschp_fuel_st (plan_id) VALUES (NEWIDD);
		    INSERT INTO biomasschp_des_den (plan_id) VALUES (NEWIDD);
		    INSERT INTO biomasschp_das_remove (plan_id) VALUES (NEWIDD);
			RETURN NULL;
-- CCPP
		ELSEIF TG_OP='INSERT' AND MODULEID='CCPP' THEN

		  INSERT INTO ccpp_questionnaire (plan_id) VALUES (NEWIDD);
			INSERT INTO ccpp_ccpp (plan_id) VALUES (NEWIDD);
			RETURN NULL;
-- 煤气发电
		ELSEIF TG_OP='INSERT' AND MODULEID='gasPowerGeneration' THEN

			INSERT INTO gaspowergeneration_needsquestionnaire (plan_id) VALUES (NEWIDD);


			RETURN NULL;
		END IF;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;

CREATE TRIGGER plan_a_000001
AFTER INSERT ON plan
FOR EACH ROW EXECUTE PROCEDURE plan_id_insert();

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


CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段s_desulfrization_before_so2:脱硫前烟气中的SO2含量,的计算1-----------------------------------
  IF OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_calcu_coal_consume != NEW.s_calcu_coal_consume OR OLD.s_aflame_generate_so2 != NEW.s_aflame_generate_so2 THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_before_so2=2*NEW.s_aflame_generate_so2*NEW.s_calcu_coal_consume*NEW.s_sulfur_design/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_aflame_generate_so2 ISNULL OR OLD.s_calcu_coal_consume ISNULL OR OLD.s_sulfur_design ISNULL) AND NEW.s_aflame_generate_so2 NOTNULL AND NEW.s_calcu_coal_consume NOTNULL AND NEW.s_sulfur_design NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_before_so2=2*NEW.s_aflame_generate_so2*NEW.s_calcu_coal_consume*NEW.s_sulfur_design/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_no_desulfurization_so2:未脱硫前SO2浓度（标态）,的计算2-----------------------------------
  IF OLD.s_desulfrization_before_so2 != NEW.s_desulfrization_before_so2 OR OLD.s_fan_smoke_flow != NEW.s_fan_smoke_flow THEN
     update coalchp_desulfurization_denitrification set 

     s_no_desulfurization_so2=NEW.s_desulfrization_before_so2/NEW.s_fan_smoke_flow*10^6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_fan_smoke_flow ISNULL OR OLD.s_desulfrization_before_so2 ISNULL) AND NEW.s_fan_smoke_flow NOTNULL AND NEW.s_desulfrization_before_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     s_no_desulfurization_so2=NEW.s_desulfrization_before_so2/NEW.s_fan_smoke_flow*10^6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_desulfrization_after_so2:脱硫后SO2浓度（标态）,的计算3-----------------------------------
  IF OLD.s_no_desulfurization_so2 != NEW.s_no_desulfurization_so2 OR OLD.s_desulfurization_efficiency != NEW.s_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_after_so2=(1-NEW.s_desulfurization_efficiency/100)*NEW.s_no_desulfurization_so2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_desulfurization_efficiency ISNULL OR OLD.s_no_desulfurization_so2 ISNULL) AND NEW.s_desulfurization_efficiency NOTNULL AND NEW.s_no_desulfurization_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_after_so2=(1-NEW.s_desulfurization_efficiency/100)*NEW.s_no_desulfurization_so2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_desulfrization_after_discharge_so2:脱硫后SO2排放量（标态）,的计算4-----------------------------------
  IF OLD.s_desulfrization_before_so2 != NEW.s_desulfrization_before_so2 OR OLD.s_desulfurization_efficiency != NEW.s_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_after_discharge_so2=(1-NEW.s_desulfurization_efficiency/100)*NEW.s_desulfrization_before_so2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_desulfurization_efficiency ISNULL OR OLD.s_desulfrization_before_so2 ISNULL) AND NEW.s_desulfurization_efficiency NOTNULL AND NEW.s_desulfrization_before_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_after_discharge_so2=(1-NEW.s_desulfurization_efficiency/100)*NEW.s_desulfrization_before_so2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_furnace_concentration:炉内脱硫后SO2浓度,的计算5-----------------------------------
  IF OLD.s_no_desulfurization_so2 != NEW.s_no_desulfurization_so2 OR OLD.s_desulfurization_efficiency != NEW.s_desulfurization_efficiency OR OLD.r_furnace_rate != NEW.r_furnace_rate THEN
     update coalchp_desulfurization_denitrification set 

     r_furnace_concentration=(1-NEW.s_desulfurization_efficiency/100*NEW.r_furnace_rate/100)*NEW.s_no_desulfurization_so2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_furnace_rate ISNULL OR OLD.s_desulfurization_efficiency ISNULL OR OLD.s_no_desulfurization_so2 ISNULL) AND NEW.r_furnace_rate NOTNULL AND NEW.s_desulfurization_efficiency NOTNULL AND NEW.s_no_desulfurization_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_furnace_concentration=(1-NEW.s_desulfurization_efficiency/100*NEW.r_furnace_rate/100)*NEW.s_no_desulfurization_so2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_others_mass:脱除SO2质量,的计算6-----------------------------------
  IF OLD.s_desulfrization_before_so2 != NEW.s_desulfrization_before_so2 OR OLD.s_desulfurization_efficiency != NEW.s_desulfurization_efficiency OR OLD.r_furnace_rate != NEW.r_furnace_rate THEN
     update coalchp_desulfurization_denitrification set 

     r_others_mass=NEW.s_desulfrization_before_so2*NEW.s_desulfurization_efficiency/100*NEW.r_furnace_rate/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_furnace_rate ISNULL OR OLD.s_desulfurization_efficiency ISNULL OR OLD.s_desulfrization_before_so2 ISNULL) AND NEW.r_furnace_rate NOTNULL AND NEW.s_desulfurization_efficiency NOTNULL AND NEW.s_desulfrization_before_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_others_mass=NEW.s_desulfrization_before_so2*NEW.s_desulfurization_efficiency/100*NEW.r_furnace_rate/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_others_mole:脱除SO2摩尔量,的计算7-----------------------------------
  IF OLD.r_others_mass != NEW.r_others_mass THEN
     update coalchp_desulfurization_denitrification set 

     r_others_mole=NEW.r_others_mass/64
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_others_mass ISNULL) AND NEW.r_others_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_others_mole=NEW.r_others_mass/64
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_nees_caco3_mole:反应所需CaCO3摩尔量,的计算8-----------------------------------
  IF OLD.r_others_mole != NEW.r_others_mole OR OLD.r_calcium_sulfur_rate != NEW.r_calcium_sulfur_rate THEN
     update coalchp_desulfurization_denitrification set 

     r_nees_caco3_mole=NEW.r_calcium_sulfur_rate*NEW.r_others_mole
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_calcium_sulfur_rate ISNULL OR OLD.r_others_mole ISNULL) AND NEW.r_calcium_sulfur_rate NOTNULL AND NEW.r_others_mole NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_nees_caco3_mole=NEW.r_calcium_sulfur_rate*NEW.r_others_mole
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_nees_caco3_mass:反应所需CaCO3质量,的计算9-----------------------------------
  IF OLD.r_nees_caco3_mole != NEW.r_nees_caco3_mole THEN
     update coalchp_desulfurization_denitrification set 

     r_nees_caco3_mass=NEW.r_nees_caco3_mole*100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_nees_caco3_mole ISNULL) AND NEW.r_nees_caco3_mole NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_nees_caco3_mass=NEW.r_nees_caco3_mole*100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_use_caco3_mass:参加反应CaCO3质量,的计算10-----------------------------------
  IF OLD.r_calcium_sulfur_rate != NEW.r_calcium_sulfur_rate OR OLD.r_nees_caco3_mass != NEW.r_nees_caco3_mass THEN
     update coalchp_desulfurization_denitrification set 

     r_use_caco3_mass=NEW.r_nees_caco3_mass/NEW.r_calcium_sulfur_rate
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_nees_caco3_mass ISNULL OR OLD.r_calcium_sulfur_rate ISNULL) AND NEW.r_nees_caco3_mass NOTNULL AND NEW.r_calcium_sulfur_rate NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_use_caco3_mass=NEW.r_nees_caco3_mass/NEW.r_calcium_sulfur_rate
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_generate_coco3_mass:反应生成CaSO4质量,的计算11-----------------------------------
  IF OLD.r_use_caco3_mass != NEW.r_use_caco3_mass THEN
     update coalchp_desulfurization_denitrification set 

     r_generate_coco3_mass=NEW.r_use_caco3_mass/100*136
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_use_caco3_mass ISNULL) AND NEW.r_use_caco3_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_generate_coco3_mass=NEW.r_use_caco3_mass/100*136
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_add_mass:反应后质量增加,的计算12-----------------------------------
  IF OLD.r_use_caco3_mass != NEW.r_use_caco3_mass OR OLD.r_generate_coco3_mass != NEW.r_generate_coco3_mass THEN
     update coalchp_desulfurization_denitrification set 

     r_add_mass=NEW.r_generate_coco3_mass-NEW.r_use_caco3_mass
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_generate_coco3_mass ISNULL OR OLD.r_use_caco3_mass ISNULL) AND NEW.r_generate_coco3_mass NOTNULL AND NEW.r_use_caco3_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_add_mass=NEW.r_generate_coco3_mass-NEW.r_use_caco3_mass
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_coco3_consume:石灰石耗量,的计算13-----------------------------------
  IF OLD.r_nees_caco3_mass != NEW.r_nees_caco3_mass OR OLD.r_caco3_pure != NEW.r_caco3_pure THEN
     update coalchp_desulfurization_denitrification set 

     r_coco3_consume=100*NEW.r_nees_caco3_mass/NEW.r_caco3_pure
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_caco3_pure ISNULL OR OLD.r_nees_caco3_mass ISNULL) AND NEW.r_caco3_pure NOTNULL AND NEW.r_nees_caco3_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_coco3_consume=100*NEW.r_nees_caco3_mass/NEW.r_caco3_pure
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_generate_grey:炉内脱硫产生的灰渣量,的计算14-----------------------------------
  IF OLD.r_add_mass != NEW.r_add_mass OR OLD.r_coco3_consume != NEW.r_coco3_consume THEN
     update coalchp_desulfurization_denitrification set 

     r_generate_grey=NEW.r_coco3_consume+NEW.r_add_mass
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_coco3_consume ISNULL OR OLD.r_add_mass ISNULL) AND NEW.r_coco3_consume NOTNULL AND NEW.r_add_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_generate_grey=NEW.r_coco3_consume+NEW.r_add_mass
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_storage_output:石灰石粉仓出力,的计算15-----------------------------------
  IF OLD.r_coco3_consume != NEW.r_coco3_consume OR OLD.r_storage_time != NEW.r_storage_time THEN
     update coalchp_desulfurization_denitrification set 

     r_storage_output=NEW.r_storage_time*22*NEW.r_coco3_consume
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_storage_time ISNULL OR OLD.r_coco3_consume ISNULL) AND NEW.r_storage_time NOTNULL AND NEW.r_coco3_consume NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_storage_output=NEW.r_storage_time*22*NEW.r_coco3_consume
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_storage_volume:石灰石粉仓体积,的计算16-----------------------------------
  IF OLD.r_storage_output != NEW.r_storage_output OR OLD.r_storage_density != NEW.r_storage_density OR OLD.r_storage_fullness != NEW.r_storage_fullness THEN
     update coalchp_desulfurization_denitrification set 

     r_storage_volume=NEW.r_storage_output/NEW.r_storage_density/NEW.r_storage_fullness
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_storage_fullness ISNULL OR OLD.r_storage_density ISNULL OR OLD.r_storage_output ISNULL) AND NEW.r_storage_fullness NOTNULL AND NEW.r_storage_density NOTNULL AND NEW.r_storage_output NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_storage_volume=NEW.r_storage_output/NEW.r_storage_density/NEW.r_storage_fullness
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_height:高,的计算17-----------------------------------
  IF OLD.r_storage_volume != NEW.r_storage_volume OR OLD.r_diameter != NEW.r_diameter THEN
     update coalchp_desulfurization_denitrification set 

     r_height=NEW.r_storage_volume/3.14/(NEW.r_diameter/2)^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_diameter ISNULL OR OLD.r_storage_volume ISNULL) AND NEW.r_diameter NOTNULL AND NEW.r_storage_volume NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_height=NEW.r_storage_volume/3.14/(NEW.r_diameter/2)^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_limestone_consume:石灰石消耗量,的计算18-----------------------------------
  IF OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_calcu_coal_consume != NEW.s_calcu_coal_consume OR OLD.d_limestone_pure != NEW.d_limestone_pure OR OLD.d_proportion_ca_s != NEW.d_proportion_ca_s OR OLD.d_desulfurization_efficiency != NEW.d_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     d_limestone_consume=100/32*NEW.s_sulfur_design/100*NEW.s_calcu_coal_consume*NEW.d_desulfurization_efficiency/100*NEW.d_proportion_ca_s/NEW.d_limestone_pure
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_desulfurization_efficiency ISNULL OR OLD.d_proportion_ca_s ISNULL OR OLD.d_limestone_pure ISNULL OR OLD.s_calcu_coal_consume ISNULL OR OLD.s_sulfur_design ISNULL) AND NEW.d_desulfurization_efficiency NOTNULL AND NEW.d_proportion_ca_s NOTNULL AND NEW.d_limestone_pure NOTNULL AND NEW.s_calcu_coal_consume NOTNULL AND NEW.s_sulfur_design NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_limestone_consume=100/32*NEW.s_sulfur_design/100*NEW.s_calcu_coal_consume*NEW.d_desulfurization_efficiency/100*NEW.d_proportion_ca_s/NEW.d_limestone_pure
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_gengrate_coca4:生成CaSO4量,的计算19-----------------------------------
  IF OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_calcu_coal_consume != NEW.s_calcu_coal_consume OR OLD.d_limestone_pure != NEW.d_limestone_pure OR OLD.d_proportion_ca_s != NEW.d_proportion_ca_s OR OLD.d_desulfurization_efficiency != NEW.d_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     d_gengrate_coca4=136/32*NEW.s_sulfur_design/100*NEW.s_calcu_coal_consume*NEW.d_desulfurization_efficiency/100*NEW.d_proportion_ca_s/NEW.d_limestone_pure
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_desulfurization_efficiency ISNULL OR OLD.d_proportion_ca_s ISNULL OR OLD.d_limestone_pure ISNULL OR OLD.s_calcu_coal_consume ISNULL OR OLD.s_sulfur_design ISNULL) AND NEW.d_desulfurization_efficiency NOTNULL AND NEW.d_proportion_ca_s NOTNULL AND NEW.d_limestone_pure NOTNULL AND NEW.s_calcu_coal_consume NOTNULL AND NEW.s_sulfur_design NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_gengrate_coca4=136/32*NEW.s_sulfur_design/100*NEW.s_calcu_coal_consume*NEW.d_desulfurization_efficiency/100*NEW.d_proportion_ca_s/NEW.d_limestone_pure
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段n_input_smoke:引风机进口烟气容积流量（标况）,的计算20-----------------------------------
  IF OLD.s_fan_smoke_flow != NEW.s_fan_smoke_flow THEN
     update coalchp_desulfurization_denitrification set 

     n_input_smoke=NEW.s_fan_smoke_flow
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_fan_smoke_flow ISNULL) AND NEW.s_fan_smoke_flow NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     n_input_smoke=NEW.s_fan_smoke_flow
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段n_before_nox_discharge:脱硝前NOX排放量,的计算21-----------------------------------
  IF OLD.n_before_nox_concentration != NEW.n_before_nox_concentration OR OLD.n_input_smoke != NEW.n_input_smoke THEN
     update coalchp_desulfurization_denitrification set 

     n_before_nox_discharge=NEW.n_before_nox_concentration*NEW.n_input_smoke*10^-6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.n_input_smoke ISNULL OR OLD.n_before_nox_concentration ISNULL) AND NEW.n_input_smoke NOTNULL AND NEW.n_before_nox_concentration NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     n_before_nox_discharge=NEW.n_before_nox_concentration*NEW.n_input_smoke*10^-6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段n_after_nox_concentration:脱硝后NOX浓度,的计算22-----------------------------------
  IF OLD.n_before_nox_concentration != NEW.n_before_nox_concentration OR OLD.n_desulfurization_efficiency != NEW.n_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     n_after_nox_concentration=(1-NEW.n_desulfurization_efficiency/100)*NEW.n_before_nox_concentration
     where plan_id=NEW.plan_id;

  ELSIF (OLD.n_desulfurization_efficiency ISNULL OR OLD.n_before_nox_concentration ISNULL) AND NEW.n_desulfurization_efficiency NOTNULL AND NEW.n_before_nox_concentration NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     n_after_nox_concentration=(1-NEW.n_desulfurization_efficiency/100)*NEW.n_before_nox_concentration
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段n_after_nox_discharge:脱硝后NOX排放量,的计算23-----------------------------------
  IF OLD.n_desulfurization_efficiency != NEW.n_desulfurization_efficiency OR OLD.n_before_nox_discharge != NEW.n_before_nox_discharge THEN
     update coalchp_desulfurization_denitrification set 

     n_after_nox_discharge=(1-NEW.n_desulfurization_efficiency/100)*NEW.n_before_nox_discharge
     where plan_id=NEW.plan_id;

  ELSIF (OLD.n_before_nox_discharge ISNULL OR OLD.n_desulfurization_efficiency ISNULL) AND NEW.n_before_nox_discharge NOTNULL AND NEW.n_desulfurization_efficiency NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     n_after_nox_discharge=(1-NEW.n_desulfurization_efficiency/100)*NEW.n_before_nox_discharge
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_denitration_quality:炉内脱硝量,的计算24-----------------------------------
  IF OLD.n_before_nox_discharge != NEW.n_before_nox_discharge OR OLD.n_after_nox_discharge != NEW.n_after_nox_discharge OR OLD.d_denitration_percentage != NEW.d_denitration_percentage THEN
     update coalchp_desulfurization_denitrification set 

     d_denitration_quality=(NEW.n_before_nox_discharge-NEW.n_after_nox_discharge)*NEW.d_denitration_percentage/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_denitration_percentage ISNULL OR OLD.n_after_nox_discharge ISNULL OR OLD.n_before_nox_discharge ISNULL) AND NEW.d_denitration_percentage NOTNULL AND NEW.n_after_nox_discharge NOTNULL AND NEW.n_before_nox_discharge NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_denitration_quality=(NEW.n_before_nox_discharge-NEW.n_after_nox_discharge)*NEW.d_denitration_percentage/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_after_nox_discharge:炉内脱硝后NOX排放量,的计算25-----------------------------------
  IF OLD.n_before_nox_discharge != NEW.n_before_nox_discharge OR OLD.d_denitration_quality != NEW.d_denitration_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_after_nox_discharge=NEW.n_before_nox_discharge-NEW.d_denitration_quality
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_denitration_quality ISNULL OR OLD.n_before_nox_discharge ISNULL) AND NEW.d_denitration_quality NOTNULL AND NEW.n_before_nox_discharge NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_after_nox_discharge=NEW.n_before_nox_discharge-NEW.d_denitration_quality
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_denitration_molar:炉内脱硝摩尔量,的计算26-----------------------------------
  IF OLD.d_denitration_quality != NEW.d_denitration_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_denitration_molar=NEW.d_denitration_quality/46
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_denitration_quality ISNULL) AND NEW.d_denitration_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_denitration_molar=NEW.d_denitration_quality/46
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_escape_quality:氨逃逸量,的计算27-----------------------------------
  IF OLD.n_input_smoke != NEW.n_input_smoke OR OLD.d_escape_rate != NEW.d_escape_rate THEN
     update coalchp_desulfurization_denitrification set 

     d_escape_quality=NEW.d_escape_rate*NEW.n_input_smoke/10^6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_escape_rate ISNULL OR OLD.n_input_smoke ISNULL) AND NEW.d_escape_rate NOTNULL AND NEW.n_input_smoke NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_escape_quality=NEW.d_escape_rate*NEW.n_input_smoke/10^6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_escape_quality_urea:逃逸氨折算尿素量,的计算28-----------------------------------
  IF OLD.d_escape_quality != NEW.d_escape_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_escape_quality_urea=NEW.d_escape_quality/34*60
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_escape_quality ISNULL) AND NEW.d_escape_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_escape_quality_urea=NEW.d_escape_quality/34*60
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_urea_nox_molar:尿素/NOX摩尔比,的计算29-----------------------------------
  IF OLD.d_nh3nox_molar != NEW.d_nh3nox_molar THEN
     update coalchp_desulfurization_denitrification set 

     d_urea_nox_molar=NEW.d_nh3nox_molar/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_nh3nox_molar ISNULL) AND NEW.d_nh3nox_molar NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_urea_nox_molar=NEW.d_nh3nox_molar/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_theory_urea:理论尿素消耗量,的计算30-----------------------------------
  IF OLD.d_denitration_quality != NEW.d_denitration_quality OR OLD.d_urea_nox_molar != NEW.d_urea_nox_molar OR OLD.d_urea_nox_quality != NEW.d_urea_nox_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_theory_urea=NEW.d_denitration_quality*NEW.d_urea_nox_quality*NEW.d_urea_nox_molar
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_urea_nox_quality ISNULL OR OLD.d_urea_nox_molar ISNULL OR OLD.d_denitration_quality ISNULL) AND NEW.d_urea_nox_quality NOTNULL AND NEW.d_urea_nox_molar NOTNULL AND NEW.d_denitration_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_theory_urea=NEW.d_denitration_quality*NEW.d_urea_nox_quality*NEW.d_urea_nox_molar
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_use_urea:尿素用量(一台炉),的计算31-----------------------------------
  IF OLD.d_denitration_quality != NEW.d_denitration_quality OR OLD.d_escape_quality_urea != NEW.d_escape_quality_urea OR OLD.d_urea_nox_molar != NEW.d_urea_nox_molar OR OLD.d_urea_nox_quality != NEW.d_urea_nox_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_use_urea=NEW.d_denitration_quality*NEW.d_urea_nox_quality*NEW.d_urea_nox_molar+NEW.d_escape_quality_urea
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_urea_nox_quality ISNULL OR OLD.d_urea_nox_molar ISNULL OR OLD.d_escape_quality_urea ISNULL OR OLD.d_denitration_quality ISNULL) AND NEW.d_urea_nox_quality NOTNULL AND NEW.d_urea_nox_molar NOTNULL AND NEW.d_escape_quality_urea NOTNULL AND NEW.d_denitration_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_use_urea=NEW.d_denitration_quality*NEW.d_urea_nox_quality*NEW.d_urea_nox_molar+NEW.d_escape_quality_urea
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_water_urea:尿素溶液消耗水量(一台炉),的计算32-----------------------------------
  IF OLD.d_use_urea != NEW.d_use_urea THEN
     update coalchp_desulfurization_denitrification set 

     d_water_urea=NEW.d_use_urea*95/5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_use_urea ISNULL) AND NEW.d_use_urea NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_water_urea=NEW.d_use_urea*95/5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_capacity_urea:尿素仓库容量,的计算33-----------------------------------
  IF OLD.d_use_urea != NEW.d_use_urea OR OLD.d_days_urea != NEW.d_days_urea THEN
     update coalchp_desulfurization_denitrification set 

     d_capacity_urea=NEW.d_days_urea*NEW.d_use_urea*24/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_days_urea ISNULL OR OLD.d_use_urea ISNULL) AND NEW.d_days_urea NOTNULL AND NEW.d_use_urea NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_capacity_urea=NEW.d_days_urea*NEW.d_use_urea*24/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_denitration_percentage:烟气脱硝百分比,的计算34-----------------------------------
  IF OLD.d_denitration_percentage != NEW.d_denitration_percentage THEN
     update coalchp_desulfurization_denitrification set 

     g_denitration_percentage=100-NEW.d_denitration_percentage
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_denitration_percentage ISNULL) AND NEW.d_denitration_percentage NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_denitration_percentage=100-NEW.d_denitration_percentage
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_after_nox_discharge:烟气脱硝后NOX排放量,的计算35-----------------------------------
  IF OLD.n_after_nox_discharge != NEW.n_after_nox_discharge THEN
     update coalchp_desulfurization_denitrification set 

     g_after_nox_discharge=NEW.n_after_nox_discharge
     where plan_id=NEW.plan_id;

  ELSIF (OLD.n_after_nox_discharge ISNULL) AND NEW.n_after_nox_discharge NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_after_nox_discharge=NEW.n_after_nox_discharge
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_denitration_quality:烟气脱硝量,的计算36-----------------------------------
  IF OLD.n_after_nox_discharge != NEW.n_after_nox_discharge OR OLD.d_after_nox_discharge != NEW.d_after_nox_discharge THEN
     update coalchp_desulfurization_denitrification set 

     g_denitration_quality=NEW.d_after_nox_discharge-NEW.n_after_nox_discharge
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_after_nox_discharge ISNULL OR OLD.n_after_nox_discharge ISNULL) AND NEW.d_after_nox_discharge NOTNULL AND NEW.n_after_nox_discharge NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_denitration_quality=NEW.d_after_nox_discharge-NEW.n_after_nox_discharge
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_escape_quality:氨逃逸量,的计算37-----------------------------------
  IF OLD.n_input_smoke != NEW.n_input_smoke OR OLD.g_escape_rate != NEW.g_escape_rate THEN
     update coalchp_desulfurization_denitrification set 

     g_escape_quality=NEW.g_escape_rate*NEW.n_input_smoke/10^6*10^3/22.4*17/10^3
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_escape_rate ISNULL OR OLD.n_input_smoke ISNULL) AND NEW.g_escape_rate NOTNULL AND NEW.n_input_smoke NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_escape_quality=NEW.g_escape_rate*NEW.n_input_smoke/10^6*10^3/22.4*17/10^3
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_escape_quality_urea:逃逸氨折算尿素量,的计算38-----------------------------------
  IF OLD.g_escape_quality != NEW.g_escape_quality THEN
     update coalchp_desulfurization_denitrification set 

     g_escape_quality_urea=NEW.g_escape_quality/34*60
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_escape_quality ISNULL) AND NEW.g_escape_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_escape_quality_urea=NEW.g_escape_quality/34*60
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_urea_nox_molar:尿素/NOX摩尔比,的计算39-----------------------------------
  IF OLD.g_nh3nox_molar != NEW.g_nh3nox_molar THEN
     update coalchp_desulfurization_denitrification set 

     g_urea_nox_molar=NEW.g_nh3nox_molar/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_nh3nox_molar ISNULL) AND NEW.g_nh3nox_molar NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_urea_nox_molar=NEW.g_nh3nox_molar/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_theory_urea:理论尿素消耗量,的计算40-----------------------------------
  IF OLD.g_denitration_quality != NEW.g_denitration_quality OR OLD.g_urea_nox_molar != NEW.g_urea_nox_molar OR OLD.g_urea_nox_quality != NEW.g_urea_nox_quality THEN
     update coalchp_desulfurization_denitrification set 

     g_theory_urea=NEW.g_denitration_quality*NEW.g_urea_nox_molar*NEW.g_urea_nox_quality
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_urea_nox_quality ISNULL OR OLD.g_urea_nox_molar ISNULL OR OLD.g_denitration_quality ISNULL) AND NEW.g_urea_nox_quality NOTNULL AND NEW.g_urea_nox_molar NOTNULL AND NEW.g_denitration_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_theory_urea=NEW.g_denitration_quality*NEW.g_urea_nox_molar*NEW.g_urea_nox_quality
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_use_urea:尿素用量(一台炉),的计算41-----------------------------------
  IF OLD.g_escape_quality_urea != NEW.g_escape_quality_urea OR OLD.g_theory_urea != NEW.g_theory_urea THEN
     update coalchp_desulfurization_denitrification set 

     g_use_urea=NEW.g_escape_quality_urea+NEW.g_theory_urea
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_theory_urea ISNULL OR OLD.g_escape_quality_urea ISNULL) AND NEW.g_theory_urea NOTNULL AND NEW.g_escape_quality_urea NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_use_urea=NEW.g_escape_quality_urea+NEW.g_theory_urea
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_desulfurization_denitrification" AFTER UPDATE OF
"s_sulfur_design",
"s_calcu_coal_consume",
"s_aflame_generate_so2",
"s_desulfrization_before_so2",
"s_fan_smoke_flow",
"s_no_desulfurization_so2",
"s_desulfurization_efficiency",
"r_furnace_rate",
"r_others_mass",
"r_others_mole",
"r_calcium_sulfur_rate",
"r_nees_caco3_mole",
"r_nees_caco3_mass",
"r_use_caco3_mass",
"r_generate_coco3_mass",
"r_add_mass",
"r_caco3_pure",
"r_coco3_consume",
"r_storage_time",
"r_storage_output",
"r_storage_density",
"r_storage_fullness",
"r_storage_volume",
"r_diameter",
"d_limestone_pure",
"d_proportion_ca_s",
"d_desulfurization_efficiency",
"n_before_nox_concentration",
"n_input_smoke",
"n_desulfurization_efficiency",
"n_before_nox_discharge",
"n_after_nox_discharge",
"d_denitration_percentage",
"d_denitration_quality",
"d_after_nox_discharge",
"d_escape_rate",
"d_escape_quality",
"d_escape_quality_urea",
"d_nh3nox_molar",
"d_urea_nox_molar",
"d_urea_nox_quality",
"d_use_urea",
"d_days_urea",
"g_denitration_quality",
"g_escape_rate",
"g_escape_quality",
"g_escape_quality_urea",
"g_nh3nox_molar",
"g_urea_nox_molar",
"g_urea_nox_quality",
"g_theory_urea"
ON "public"."coalchp_desulfurization_denitrification"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification"();

CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段s_sum:总和,的计算1-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     s_sum_check=NEW.s_carbon_check+NEW.s_hydrogen_check+NEW.s_oxygen_check+NEW.s_nitrogen_check+NEW.s_sulfur_check+NEW.s_grey_check+NEW.s_water_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_water_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.s_water_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_sum_check=NEW.s_carbon_check+NEW.s_hydrogen_check+NEW.s_oxygen_check+NEW.s_nitrogen_check+NEW.s_sulfur_check+NEW.s_grey_check+NEW.s_water_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_low_1:收到基低位发热量计算得到,的计算2-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check THEN
     update coalchp_furnace_calculation set 

     s_low_1_check=NEW.s_low_check/4.1868
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_low_check ISNULL) AND NEW.s_low_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_low_1_check=NEW.s_low_check/4.1868
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_low_estimation:低位发热量估算,的计算3-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     s_low_estimation_check=339*NEW.s_carbon_check+1030*NEW.s_hydrogen_check-109*(NEW.s_oxygen_check-NEW.s_sulfur_check)-25*NEW.s_water_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_low_estimation_check=339*NEW.s_carbon_check+1030*NEW.s_hydrogen_check-109*(NEW.s_oxygen_check-NEW.s_sulfur_check)-25*NEW.s_water_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_high_estimation:高位发热量估算,的计算4-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     s_high_estimation_check=339*NEW.s_carbon_check+1256*NEW.s_hydrogen_check-109*(NEW.s_oxygen_check-NEW.s_sulfur_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_high_estimation_check=339*NEW.s_carbon_check+1256*NEW.s_hydrogen_check-109*(NEW.s_oxygen_check-NEW.s_sulfur_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_boiler_pressure:锅筒压力,的计算5-----------------------------------
  IF OLD.f_steam_pressure_check != NEW.f_steam_pressure_check THEN
     update coalchp_furnace_calculation set 

     f_boiler_pressure_check=NEW.f_steam_pressure_check*1.1
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_steam_pressure_check ISNULL) AND NEW.f_steam_pressure_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     f_boiler_pressure_check=NEW.f_steam_pressure_check*1.1
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_boiler_consumption:锅炉燃料消耗量,的计算6-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check THEN
     update coalchp_furnace_calculation set 

     f_boiler_consumption_check=NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL) AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     f_boiler_consumption_check=NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_calculation_consumption:计算燃料消耗量,的计算7-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check THEN
     update coalchp_furnace_calculation set 

     f_calculation_consumption_check=(NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL) AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     f_calculation_consumption_check=(NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_total:灰渣总量,的计算8-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     d_total_check=(NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(NEW.s_grey_check/100+NEW.s_low_check*NEW.f_unburned_loss_check/3387000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_grey_check ISNULL) AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_grey_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_total_check=(NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(NEW.s_grey_check/100+NEW.s_low_check*NEW.f_unburned_loss_check/3387000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_dust_share:底渣份额,的计算9-----------------------------------
  IF OLD.d_ash_share_check != NEW.d_ash_share_check THEN
     update coalchp_furnace_calculation set 

     d_dust_share_check=1-NEW.d_ash_share_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_ash_share_check ISNULL) AND NEW.d_ash_share_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_dust_share_check=1-NEW.d_ash_share_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_ash_total:灰量,的计算10-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.d_boiler_total_check != NEW.d_boiler_total_check OR OLD.d_ash_share_check != NEW.d_ash_share_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     d_ash_total_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(NEW.s_grey_check/100+NEW.s_low_check*NEW.f_unburned_loss_check/3387000))+NEW.d_boiler_total_check)*NEW.d_ash_share_check/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_ash_share_check ISNULL OR OLD.d_boiler_total_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_grey_check ISNULL) AND NEW.d_ash_share_check NOTNULL AND NEW.d_boiler_total_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_grey_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_ash_total_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(NEW.s_grey_check/100+NEW.s_low_check*NEW.f_unburned_loss_check/3387000))+NEW.d_boiler_total_check)*NEW.d_ash_share_check/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_dust_total:渣量,的计算11-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.d_boiler_total_check != NEW.d_boiler_total_check OR OLD.d_ash_share_check != NEW.d_ash_share_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     d_dust_total_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(NEW.s_grey_check/100+NEW.s_low_check*NEW.f_unburned_loss_check/3387000))+NEW.d_boiler_total_check)*(1-NEW.d_ash_share_check)/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_ash_share_check ISNULL OR OLD.d_boiler_total_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_grey_check ISNULL) AND NEW.d_ash_share_check NOTNULL AND NEW.d_boiler_total_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_grey_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_dust_total_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(NEW.s_grey_check/100+NEW.s_low_check*NEW.f_unburned_loss_check/3387000))+NEW.d_boiler_total_check)*(1-NEW.d_ash_share_check)/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_air_volumn:理论干空气量,的计算12-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     a_air_volumn_check=0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_air_volumn_check=0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_steam_perssure:水蒸气分压力,的计算13-----------------------------------
  IF OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check THEN
     update coalchp_furnace_calculation set 

     a_steam_perssure_check=NEW.a_humidity_check*NEW.a_saturation_pressure_check/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_humidity_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_steam_perssure_check=NEW.a_humidity_check*NEW.a_saturation_pressure_check/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_air_humidity:空气的绝对湿度（含湿量）,的计算14-----------------------------------
  IF OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check THEN
     update coalchp_furnace_calculation set 

     a_air_humidity_check=622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_air_humidity_check=622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_standard_air_humidity:标况下湿空气密度,的计算15-----------------------------------
  IF OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check THEN
     update coalchp_furnace_calculation set 

     a_standard_air_humidity_check=(1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_standard_air_humidity_check=(1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_wet_air_volumn:理论湿空气量,的计算16-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     a_wet_air_volumn_check=(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_wet_air_volumn_check=(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_nitrogen_volume:理论氮气容积,的计算17-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     s_nitrogen_volume_check=0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_nitrogen_volume_check=0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_dioxide_volume:理论二氧化物容积,的计算18-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     s_dioxide_volume_check=1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.s_sulfur_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_dioxide_volume_check=1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_steam_volume:理论水蒸汽容积,的计算19-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     s_steam_volume_check=0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_steam_volume_check=0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_smoke_volume:理论烟气容积,的计算20-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     s_smoke_volume_check=(0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_smoke_volume_check=(0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_1kg_weight:1kg燃料生成理论湿烟气的重量,的计算21-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     s_1kg_weight_check=1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_1kg_weight_check=1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_wet_smoke_density:标况下理论湿烟气密度,的计算22-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     s_wet_smoke_density_check=(1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))/((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_wet_smoke_density_check=(1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))/((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_wind_air:旋风分离器出口过剩空气系数,的计算23-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check THEN
     update coalchp_furnace_calculation set 

     p_wind_air_check=NEW.p_boiler_air_check+NEW.p_wind_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_wind_air_check=NEW.p_boiler_air_check+NEW.p_wind_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_hign_air:高过出口过剩空气系数,的计算24-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check THEN
     update coalchp_furnace_calculation set 

     p_hign_air_check=NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_hign_air_check=NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_low_air:低过出口过剩空气系数,的计算25-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check THEN
     update coalchp_furnace_calculation set 

     p_low_air_check=NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_low_air_check=NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_fule_air:省燃料器出口过剩空气系数,的计算26-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check THEN
     update coalchp_furnace_calculation set 

     p_fule_air_check=NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_fule_air_check=NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_heater_air:空预器出口过剩空气系数,的计算27-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check THEN
     update coalchp_furnace_calculation set 

     p_heater_air_check=NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_heater_air_check=NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_dust_exit:除尘器进口过剩空气系数,的计算28-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check THEN
     update coalchp_furnace_calculation set 

     p_dust_exit_check=NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_dust_exit_check=NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_dust_entry:除尘器出口过剩空气系数,的计算29-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check THEN
     update coalchp_furnace_calculation set 

     p_dust_entry_check=NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_dust_entry_check=NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_fans_air:引风机入口过剩空气系数,的计算30-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check THEN
     update coalchp_furnace_calculation set 

     p_fans_air_check=NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_fans_air_check=NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_1kg_volume:61Kg燃料产生的空预器出口湿烟气容积,的计算31-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     p_1kg_volume_check=((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_1kg_volume_check=((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_1kg_quality:61Kg燃料产生的空预器出口湿烟气质量,的计算32-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     p_1kg_quality_check=1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_1kg_quality_check=1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_theory_air_quality:理论空气量（体积,湿）,的计算33-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     a_theory_air_quality_check=((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_theory_air_quality_check=((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_boiler_air:炉膛出口过剩空气系数,的计算34-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check THEN
     update coalchp_furnace_calculation set 

     a_boiler_air_check=NEW.p_boiler_air_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_boiler_air_check ISNULL) AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_boiler_air_check=NEW.p_boiler_air_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_actual_air:实际空气量（体积,湿）,的计算35-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     a_actual_air_check=(NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_actual_air_check=(NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_calculation_consumption:计算燃料消耗量,的计算36-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check THEN
     update coalchp_furnace_calculation set 

     a_calculation_consumption_check=((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL) AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_calculation_consumption_check=((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_actual_air_total:实际空气总量（体积，湿）,的计算37-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     a_actual_air_total_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_actual_air_total_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_cwind_temperature_calculation:冷风温度（计算温度）,的计算38-----------------------------------
  IF OLD.p_heater_first_entry_check != NEW.p_heater_first_entry_check THEN
     update coalchp_furnace_calculation set 

     a_cwind_temperature_calculation_check=NEW.p_heater_first_entry_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_first_entry_check ISNULL) AND NEW.p_heater_first_entry_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_cwind_temperature_calculation_check=NEW.p_heater_first_entry_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_local_pressure:当地年平均气压,的计算39-----------------------------------
  IF OLD.a_pressure_check != NEW.a_pressure_check THEN
     update coalchp_furnace_calculation set 

     a_local_pressure_check=NEW.a_pressure_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_pressure_check ISNULL) AND NEW.a_pressure_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_local_pressure_check=NEW.a_pressure_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_cwind_standard:冷一次风量（湿-标准态）,的计算40-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_standard_check=NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_standard_check=NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_cwind_actual:冷一次风量（湿-实态）,的计算41-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_heater_first_entry_check != NEW.p_heater_first_entry_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_actual_check=(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_first_entry_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_first_entry_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_actual_check=(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_standard_air_density:标况下湿空气密度1,的计算42-----------------------------------
  IF OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check THEN
     update coalchp_furnace_calculation set 

     a_first_standard_air_density_check=((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_standard_air_density_check=((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_cwind_flow:冷一次风量（质量流量）,的计算43-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_flow_check=(((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_flow_check=(((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_cwind_density:冷一次风湿空气密度（湿-实态）,的计算44-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_heater_first_entry_check != NEW.p_heater_first_entry_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_density_check=((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_first_entry_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_first_entry_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_density_check=((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_check:校核,的计算45-----------------------------------
  IF OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.p_heater_first_entry_check != NEW.p_heater_first_entry_check THEN
     update coalchp_furnace_calculation set 

     a_check_check=(((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*273/(273+(NEW.p_heater_first_entry_check))*(NEW.a_pressure_check)/101.325
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_first_entry_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL) AND NEW.p_heater_first_entry_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_check_check=(((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*273/(273+(NEW.p_heater_first_entry_check))*(NEW.a_pressure_check)/101.325
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_hwind_temperatue:热一次风温度,的计算46-----------------------------------
  IF OLD.p_heater_first_exit_check != NEW.p_heater_first_exit_check THEN
     update coalchp_furnace_calculation set 

     a_first_hwind_temperatue_check=NEW.p_heater_first_exit_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_first_exit_check ISNULL) AND NEW.p_heater_first_exit_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_hwind_temperatue_check=NEW.p_heater_first_exit_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_hwind_flow:热一次风量（湿-实态）,的计算47-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_heater_first_exit_check != NEW.p_heater_first_exit_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_first_hwind_flow_check=(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_exit_check))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_first_exit_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_first_exit_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_hwind_flow_check=(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_exit_check))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_wet_air_density:湿空气密度（湿-实态）1,的计算48-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_heater_first_exit_check != NEW.p_heater_first_exit_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_first_wet_air_density_check=((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_exit_check))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_first_exit_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_first_exit_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_wet_air_density_check=((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_exit_check))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_wind_volume:二次风份额,的计算49-----------------------------------
  IF OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_second_wind_volume_check=100-NEW.a_first_wind_volume_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_wind_volume_check=100-NEW.a_first_wind_volume_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_cwind_temperature:冷风温度,的计算50-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_heater_first_entry_check != NEW.p_heater_first_entry_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_cwind_temperature_check=(((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_first_entry_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_first_entry_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_cwind_temperature_check=(((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_cwind_standard:冷二次风量（湿-标准态）,的计算51-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_standard_check=(100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_standard_check=(100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_cwind_actual:冷二次风量（湿-实态）,的计算52-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_heater_first_entry_check != NEW.p_heater_first_entry_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_actual_check=((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))*(273+((((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check)))))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_first_entry_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_first_entry_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_actual_check=((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))*(273+((((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check)))))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_standard_air_density:标况下湿空气密度2,的计算53-----------------------------------
  IF OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check THEN
     update coalchp_furnace_calculation set 

     a_second_standard_air_density_check=(((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL) AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_standard_air_density_check=(((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_cwind_flow:冷二次风量（质量流量）,的计算54-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_flow_check=((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804))))*((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_flow_check=((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804))))*((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_cwind_density:冷二次风湿空气密度（湿-实态）,的计算55-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_heater_first_entry_check != NEW.p_heater_first_entry_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_density_check=(((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804))))*((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))))/(((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))*(273+((((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check)))))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_first_entry_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_first_entry_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_density_check=(((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804))))*((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))))/(((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))*(273+((((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804)))*(NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100))/((NEW.a_first_wind_volume_check*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))/100)*(273+(NEW.p_heater_first_entry_check))/273*101.325/(NEW.a_pressure_check)))))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_hwind_temperatue:热二次风温度,的计算56-----------------------------------
  IF OLD.p_heater_second_exit_check != NEW.p_heater_second_exit_check THEN
     update coalchp_furnace_calculation set 

     a_second_hwind_temperatue_check=NEW.p_heater_second_exit_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_second_exit_check ISNULL) AND NEW.p_heater_second_exit_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_hwind_temperatue_check=NEW.p_heater_second_exit_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_hwind_flow:热二次风量（湿-实态）,的计算57-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_heater_second_exit_check != NEW.p_heater_second_exit_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_second_hwind_flow_check=((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))*(273+(NEW.p_heater_second_exit_check))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_second_exit_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_second_exit_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_hwind_flow_check=((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))*(273+(NEW.p_heater_second_exit_check))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_wet_air_density:湿空气密度（湿-实态）2,的计算58-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_heater_second_exit_check != NEW.p_heater_second_exit_check OR OLD.a_first_wind_volume_check != NEW.a_first_wind_volume_check THEN
     update coalchp_furnace_calculation set 

     a_second_wet_air_density_check=(((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804))))*((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))))/(((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))*(273+(NEW.p_heater_second_exit_check))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_check ISNULL OR OLD.p_heater_second_exit_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.a_first_wind_volume_check NOTNULL AND NEW.p_heater_second_exit_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_wet_air_density_check=(((((1+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/0.804))))*((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))))))/(((100-NEW.a_first_wind_volume_check)/100*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((NEW.p_boiler_air_check)*(((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))))))*(273+(NEW.p_heater_second_exit_check))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_1kg_volume:标况下空预器出口1Kg燃料湿烟气容积,的计算59-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     h_1kg_volume_check=(((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_1kg_volume_check=(((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_1kg_quality:空预器出口1Kg燃料产生的湿烟气质量,的计算60-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     h_1kg_quality_check=(1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_1kg_quality_check=(1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_calculation_consumption:计算燃料消耗量,的计算61-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check THEN
     update coalchp_furnace_calculation set 

     h_calculation_consumption_check=((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL) AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_calculation_consumption_check=((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_standard_smoke_flow:标况下空预器出口烟气容积流量,的计算62-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     h_standard_smoke_flow_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_standard_smoke_flow_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_smoke_flow:空预器出口烟气质量流量,的计算63-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     h_smoke_flow_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_smoke_flow_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_smoke_temperature:锅炉空预器出口排烟温度,的计算64-----------------------------------
  IF OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     h_smoke_temperature_check=NEW.p_smoke_temperature_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_smoke_temperature_check ISNULL) AND NEW.p_smoke_temperature_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_smoke_temperature_check=NEW.p_smoke_temperature_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_smoke_volume:空预器出口烟气容积量(实态）,的计算65-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     h_smoke_volume_check=((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))))*(273+(NEW.p_smoke_temperature_check))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_smoke_temperature_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_smoke_volume_check=((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))))*(273+(NEW.p_smoke_temperature_check))/273*101.325/(NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_smoke_density:烟气密度（实态）,的计算66-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     h_smoke_density_check=((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))/(((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))))*(273+(NEW.p_smoke_temperature_check))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_smoke_temperature_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_smoke_density_check=((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((1-NEW.s_grey_check/100+(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/1000)*1.293*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))/(((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))*((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))))*(273+(NEW.p_smoke_temperature_check))/273*101.325/(NEW.a_pressure_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_exit_air:空预器出口过剩空气系数,的计算67-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check THEN
     update coalchp_furnace_calculation set 

     d_exit_air_check=(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_exit_air_check=(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_wind_parameter:空预器至除尘器烟道漏风系数,的计算68-----------------------------------
  IF OLD.p_plus_air_check != NEW.p_plus_air_check THEN
     update coalchp_furnace_calculation set 

     d_wind_parameter_check=NEW.p_plus_air_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_check ISNULL) AND NEW.p_plus_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_wind_parameter_check=NEW.p_plus_air_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_air:除尘器进口过剩空气系数,的计算69-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check THEN
     update coalchp_furnace_calculation set 

     d_entry_air_check=(NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_air_check=(NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_somke_temperature:除尘器进口处烟气温度,的计算70-----------------------------------
  IF OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     d_entry_somke_temperature_check=(((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_somke_temperature_check=(((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_standard_1kg_volume:标况下除尘器进口处1kg燃料湿烟气容积,的计算71-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     d_standard_1kg_volume_check=((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_standard_1kg_volume_check=((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_1kg_quality:除尘器进口处1kg燃料湿烟气质量,的计算72-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     d_entry_1kg_quality_check=1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_1kg_quality_check=1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_standard_smoke_flow:标况下除尘器进口烟气容积流量,的计算73-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     d_standard_smoke_flow_check=(((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_standard_smoke_flow_check=(((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_somke_flow:除尘器进口处烟气质量流量,的计算74-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     d_entry_somke_flow_check=(1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_somke_flow_check=(1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_smoke_actual_flow:除尘器进口处烟气容积流量(实态）,的计算75-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     d_entry_smoke_actual_flow_check=((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*101.325/273/NEW.a_pressure_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_smoke_actual_flow_check=((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*101.325/273/NEW.a_pressure_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_wind_parameter:除尘器漏风系数,的计算76-----------------------------------
  IF OLD.p_dust_check != NEW.p_dust_check THEN
     update coalchp_furnace_calculation set 

     e_wind_parameter_check=NEW.p_dust_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_check ISNULL) AND NEW.p_dust_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_wind_parameter_check=NEW.p_dust_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_air_parameter:除尘器出口过剩空气系数,的计算77-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check THEN
     update coalchp_furnace_calculation set 

     e_air_parameter_check=(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_air_parameter_check=(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_smoke_temperature:除尘器出口烟气温度,的计算78-----------------------------------
  IF OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     e_smoke_temperature_check=((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_smoke_temperature_check=((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_standard_1kg_volume:标况下除尘器出口处1kg燃料湿烟气容积,的计算79-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     e_standard_1kg_volume_check=(((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_standard_1kg_volume_check=(((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_1kg_quality:除尘器出口处1kg燃料湿烟气质量,的计算80-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     e_1kg_quality_check=1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_1kg_quality_check=1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_standard_smoke_flow:标况下除尘器出口湿烟气容积流量,的计算81-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     e_standard_smoke_flow_check=((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_standard_smoke_flow_check=((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_smoke_flow:除尘器出口处湿烟气质量流量,的计算82-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     e_smoke_flow_check=(1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_smoke_flow_check=(1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_smoke_actual_flow:除尘器出口处湿烟气容积流量(实态）,的计算83-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     e_smoke_actual_flow_check=(((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))))/273*101.325/NEW.a_pressure_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_smoke_actual_flow_check=(((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))))/273*101.325/NEW.a_pressure_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_smoke_actual_density:烟气密度（实态）,的计算84-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     e_smoke_actual_density_check=((1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))/((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))))/273*101.325/NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_smoke_actual_density_check=((1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))/((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))))/273*101.325/NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_wind_parameter:除尘器出口至引风机烟道漏风系数,的计算85-----------------------------------
  IF OLD.p_plus_dust_check != NEW.p_plus_dust_check THEN
     update coalchp_furnace_calculation set 

     i_wind_parameter_check=NEW.p_plus_dust_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL) AND NEW.p_plus_dust_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_wind_parameter_check=NEW.p_plus_dust_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_air_parameter:引风机入口过剩空气系数,的计算86-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check THEN
     update coalchp_furnace_calculation set 

     i_air_parameter_check=(NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_air_parameter_check=(NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_temperature:引风机入口烟气温度,的计算87-----------------------------------
  IF OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     i_smoke_temperature_check=(((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))+(NEW.p_plus_dust_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_temperature_check=(((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))+(NEW.p_plus_dust_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_standard_1kg_volume:标况下引风机进口处1kg燃料湿烟气容积,的计算88-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     i_standard_1kg_volume_check=((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_standard_1kg_volume_check=((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_1kg_quality:引风机进口处1kg燃料湿烟气质量,的计算89-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     i_1kg_quality_check=1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_1kg_quality_check=1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_standard_smoke_flow1:标况下引风机进口湿烟气容积流量1,的计算90-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     i_standard_smoke_flow1_check=(((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_standard_smoke_flow1_check=(((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_standard_smoke_flow2:标况下引风机进口湿烟气容积流量2,的计算91-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     i_standard_smoke_flow2_check=((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))/3600
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_standard_smoke_flow2_check=((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))/3600
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_flow:引风机进口处湿烟气质量流量,的计算92-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     i_smoke_flow_check=(1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_flow_check=(1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_actual_flow1:引风机进口处湿烟气容积流量(实态）1,的计算93-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_flow1_check=((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+((((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))+(NEW.p_plus_dust_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))))/273*101.325/NEW.a_pressure_check
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_flow1_check=((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+((((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))+(NEW.p_plus_dust_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))))/273*101.325/NEW.a_pressure_check
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_actual_flow2:引风机进口处湿烟气容积流量(实态）2,的计算94-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_flow2_check=(((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+((((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))+(NEW.p_plus_dust_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))))/273*101.325/NEW.a_pressure_check)/3600
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_flow2_check=(((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+((((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))+(NEW.p_plus_dust_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))))/273*101.325/NEW.a_pressure_check)/3600
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_actual_density:烟气密度（实态）,的计算95-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.d_cold_air_temperature_check != NEW.d_cold_air_temperature_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.p_smoke_temperature_check != NEW.p_smoke_temperature_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_density_check=((1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))/(((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+((((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))+(NEW.p_plus_dust_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))))/273*101.325/NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_check ISNULL OR OLD.p_smoke_temperature_check ISNULL OR OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.d_cold_air_temperature_check NOTNULL AND NEW.p_smoke_temperature_check NOTNULL AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_density_check=((1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))/(((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))*(273+((((NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))*(((((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))*NEW.p_smoke_temperature_check+(NEW.p_plus_air_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_air_check)+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))+(NEW.p_plus_dust_check)*NEW.d_cold_air_temperature_check)/((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))))/273*101.325/NEW.a_pressure_check)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_wet_smoke_actual_density:引风机处计算湿烟气密度（标况）,的计算96-----------------------------------
  IF OLD.s_water_check != NEW.s_water_check OR OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.a_humidity_check != NEW.a_humidity_check OR OLD.a_pressure_check != NEW.a_pressure_check OR OLD.a_saturation_pressure_check != NEW.a_saturation_pressure_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check OR OLD.s_grey_check != NEW.s_grey_check THEN
     update coalchp_furnace_calculation set 

     i_wet_smoke_actual_density_check=((1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))/((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.a_saturation_pressure_check ISNULL OR OLD.a_pressure_check ISNULL OR OLD.a_humidity_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_water_check ISNULL OR OLD.s_grey_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.a_saturation_pressure_check NOTNULL AND NEW.a_pressure_check NOTNULL AND NEW.a_humidity_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_water_check NOTNULL AND NEW.s_grey_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_wet_smoke_actual_density_check=((1-NEW.s_grey_check/100+1.293*(1+(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))/100)*((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))/((((((((0.111*NEW.s_hydrogen_check+0.0124*NEW.s_water_check+1.293*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))/0.804/1000)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)+(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check))+((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.0161*((NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))+(NEW.p_plus_air_check)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)))))+0.0161*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))+((NEW.p_plus_dust_check)+0.0161)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))*(1+0.0016*(622*(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100)/(NEW.a_pressure_check-(NEW.a_humidity_check*NEW.a_saturation_pressure_check/100))))))*(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_oxygen_vol:烟气中的氧量,的计算97-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     go_oxygen_vol_check=0.21*(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_oxygen_vol_check=0.21*(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_theoretica_vol:理论干烟气容积,的计算98-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     go_theoretica_vol_check=(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_theoretica_vol_check=(0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_theoretica_flow:理论干空气量,的计算99-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     go_theoretica_flow_check=(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.s_sulfur_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_theoretica_flow_check=(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_calculation_consumption:计算燃料消耗量,的计算100-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check THEN
     update coalchp_furnace_calculation set 

     go_calculation_consumption_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL) AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_calculation_consumption_check=(((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_air_parameter:引风机入口过剩空气系数,的计算101-----------------------------------
  IF OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check THEN
     update coalchp_furnace_calculation set 

     go_air_parameter_check=(NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_air_parameter_check=(NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_standard_1kg_volume:121Kg燃料产生的引风机进口干烟气容积,的计算102-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     go_standard_1kg_volume_check=((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_standard_1kg_volume_check=((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_smoke_flow:引风机进口干烟气容积流量,的计算103-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     go_smoke_flow_check=(((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_smoke_flow_check=(((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_drygas_oxygen_vol:干烟气中含氧量,的计算104-----------------------------------
  IF OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     go_drygas_oxygen_vol_check=(0.21*(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))/(((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))*100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_drygas_oxygen_vol_check=(0.21*(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))/(((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))*100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_total_combustion_product_vol:总燃烧产物6%O2干体积,的计算105-----------------------------------
  IF OLD.s_low_check != NEW.s_low_check OR OLD.f_steam_flow_check != NEW.f_steam_flow_check OR OLD.f_steam_enthalpy_check != NEW.f_steam_enthalpy_check OR OLD.f_saturated_water_enthalpy_check != NEW.f_saturated_water_enthalpy_check OR OLD.f_water_enthalpy_check != NEW.f_water_enthalpy_check OR OLD.f_boiler_efficiency_check != NEW.f_boiler_efficiency_check OR OLD.f_unburned_loss_check != NEW.f_unburned_loss_check OR OLD.f_blowdown_rate_check != NEW.f_blowdown_rate_check OR OLD.s_carbon_check != NEW.s_carbon_check OR OLD.s_hydrogen_check != NEW.s_hydrogen_check OR OLD.p_boiler_air_check != NEW.p_boiler_air_check OR OLD.p_wind_check != NEW.p_wind_check OR OLD.s_oxygen_check != NEW.s_oxygen_check OR OLD.p_high_check != NEW.p_high_check OR OLD.p_low_check != NEW.p_low_check OR OLD.p_fule_check != NEW.p_fule_check OR OLD.p_heater_check != NEW.p_heater_check OR OLD.p_plus_air_check != NEW.p_plus_air_check OR OLD.s_nitrogen_check != NEW.s_nitrogen_check OR OLD.p_dust_check != NEW.p_dust_check OR OLD.p_plus_dust_check != NEW.p_plus_dust_check OR OLD.s_sulfur_check != NEW.s_sulfur_check THEN
     update coalchp_furnace_calculation set 

     go_total_combustion_product_vol_check=((((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))))*(21-((0.21*(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))/(((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))*100))/(21-6)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_check ISNULL OR OLD.p_dust_check ISNULL OR OLD.p_plus_air_check ISNULL OR OLD.p_heater_check ISNULL OR OLD.p_fule_check ISNULL OR OLD.p_low_check ISNULL OR OLD.p_high_check ISNULL OR OLD.p_wind_check ISNULL OR OLD.p_boiler_air_check ISNULL OR OLD.f_blowdown_rate_check ISNULL OR OLD.f_unburned_loss_check ISNULL OR OLD.f_boiler_efficiency_check ISNULL OR OLD.f_water_enthalpy_check ISNULL OR OLD.f_saturated_water_enthalpy_check ISNULL OR OLD.f_steam_enthalpy_check ISNULL OR OLD.f_steam_flow_check ISNULL OR OLD.s_low_check ISNULL OR OLD.s_sulfur_check ISNULL OR OLD.s_nitrogen_check ISNULL OR OLD.s_oxygen_check ISNULL OR OLD.s_hydrogen_check ISNULL OR OLD.s_carbon_check ISNULL) AND NEW.p_plus_dust_check NOTNULL AND NEW.p_dust_check NOTNULL AND NEW.p_plus_air_check NOTNULL AND NEW.p_heater_check NOTNULL AND NEW.p_fule_check NOTNULL AND NEW.p_low_check NOTNULL AND NEW.p_high_check NOTNULL AND NEW.p_wind_check NOTNULL AND NEW.p_boiler_air_check NOTNULL AND NEW.f_blowdown_rate_check NOTNULL AND NEW.f_unburned_loss_check NOTNULL AND NEW.f_boiler_efficiency_check NOTNULL AND NEW.f_water_enthalpy_check NOTNULL AND NEW.f_saturated_water_enthalpy_check NOTNULL AND NEW.f_steam_enthalpy_check NOTNULL AND NEW.f_steam_flow_check NOTNULL AND NEW.s_low_check NOTNULL AND NEW.s_sulfur_check NOTNULL AND NEW.s_nitrogen_check NOTNULL AND NEW.s_oxygen_check NOTNULL AND NEW.s_hydrogen_check NOTNULL AND NEW.s_carbon_check NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_total_combustion_product_vol_check=((((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))*((((NEW.f_steam_flow_check*1000/NEW.f_boiler_efficiency_check*((NEW.f_steam_enthalpy_check-NEW.f_water_enthalpy_check)+NEW.f_blowdown_rate_check*(NEW.f_saturated_water_enthalpy_check-NEW.f_water_enthalpy_check))/NEW.s_low_check)*(1-NEW.f_unburned_loss_check)))))*(21-((0.21*(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check)))/(((0.79*(0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))+0.008*NEW.s_nitrogen_check)+(1.866*(NEW.s_carbon_check+0.375*NEW.s_sulfur_check)/100))+(((NEW.p_plus_dust_check+(NEW.p_dust_check+(NEW.p_plus_air_check+(NEW.p_heater_check+(NEW.p_fule_check+(NEW.p_low_check+(NEW.p_high_check+(NEW.p_boiler_air_check+NEW.p_wind_check)))))))))-1)*((0.0889*NEW.s_carbon_check+0.265*NEW.s_hydrogen_check-0.0333*(NEW.s_oxygen_check-NEW.s_sulfur_check))))*100))/(21-6)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_furnace_calculation_check" AFTER UPDATE OF
"s_water_check",
"d_cold_air_temperature_check",
"s_low_check",
"f_steam_flow_check",
"f_steam_pressure_check",
"f_steam_enthalpy_check",
"f_saturated_water_enthalpy_check",
"f_water_enthalpy_check",
"f_boiler_efficiency_check",
"f_unburned_loss_check",
"f_blowdown_rate_check",
"d_boiler_total_check",
"d_ash_share_check",
"s_carbon_check",
"a_humidity_check",
"a_pressure_check",
"a_saturation_pressure_check",
"s_hydrogen_check",
"p_boiler_air_check",
"p_wind_check",
"s_oxygen_check",
"p_high_check",
"p_low_check",
"p_fule_check",
"p_heater_check",
"p_plus_air_check",
"s_nitrogen_check",
"p_dust_check",
"p_plus_dust_check",
"p_heater_first_entry_check",
"s_sulfur_check",
"p_heater_first_exit_check",
"p_heater_second_exit_check",
"p_smoke_temperature_check",
"s_grey_check",
"a_first_wind_volume_check"
ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_check"();
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段s_sum:总和,的计算1-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     s_sum_design=NEW.s_carbon_design+NEW.s_hydrogen_design+NEW.s_oxygen_design+NEW.s_nitrogen_design+NEW.s_sulfur_design+NEW.s_grey_design+NEW.s_water_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_water_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.s_water_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_sum_design=NEW.s_carbon_design+NEW.s_hydrogen_design+NEW.s_oxygen_design+NEW.s_nitrogen_design+NEW.s_sulfur_design+NEW.s_grey_design+NEW.s_water_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_low_1:收到基低位发热量计算得到,的计算2-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design THEN
     update coalchp_furnace_calculation set 

     s_low_1_design=NEW.s_low_design/4.1868
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_low_design ISNULL) AND NEW.s_low_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_low_1_design=NEW.s_low_design/4.1868
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_low_estimation:低位发热量估算,的计算3-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     s_low_estimation_design=339*NEW.s_carbon_design+1030*NEW.s_hydrogen_design-109*(NEW.s_oxygen_design-NEW.s_sulfur_design)-25*NEW.s_water_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_low_estimation_design=339*NEW.s_carbon_design+1030*NEW.s_hydrogen_design-109*(NEW.s_oxygen_design-NEW.s_sulfur_design)-25*NEW.s_water_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_high_estimation:高位发热量估算,的计算4-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     s_high_estimation_design=339*NEW.s_carbon_design+1256*NEW.s_hydrogen_design-109*(NEW.s_oxygen_design-NEW.s_sulfur_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_high_estimation_design=339*NEW.s_carbon_design+1256*NEW.s_hydrogen_design-109*(NEW.s_oxygen_design-NEW.s_sulfur_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_boiler_pressure:锅筒压力,的计算5-----------------------------------
  IF OLD.f_steam_pressure_design != NEW.f_steam_pressure_design THEN
     update coalchp_furnace_calculation set 

     f_boiler_pressure_design=NEW.f_steam_pressure_design*1.1
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_steam_pressure_design ISNULL) AND NEW.f_steam_pressure_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     f_boiler_pressure_design=NEW.f_steam_pressure_design*1.1
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_boiler_consumption:锅炉燃料消耗量,的计算6-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design THEN
     update coalchp_furnace_calculation set 

     f_boiler_consumption_design=NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL) AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     f_boiler_consumption_design=NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段f_calculation_consumption:计算燃料消耗量,的计算7-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design THEN
     update coalchp_furnace_calculation set 

     f_calculation_consumption_design=(NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL) AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     f_calculation_consumption_design=(NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_total:灰渣总量,的计算8-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     d_total_design=(NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(NEW.s_grey_design/100+NEW.s_low_design*NEW.f_unburned_loss_design/3387000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_grey_design ISNULL) AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_grey_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_total_design=(NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(NEW.s_grey_design/100+NEW.s_low_design*NEW.f_unburned_loss_design/3387000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_dust_share:底渣份额,的计算9-----------------------------------
  IF OLD.d_ash_share_design != NEW.d_ash_share_design THEN
     update coalchp_furnace_calculation set 

     d_dust_share_design=1-NEW.d_ash_share_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_ash_share_design ISNULL) AND NEW.d_ash_share_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_dust_share_design=1-NEW.d_ash_share_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_ash_total:灰量,的计算10-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.d_boiler_total_design != NEW.d_boiler_total_design OR OLD.d_ash_share_design != NEW.d_ash_share_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     d_ash_total_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(NEW.s_grey_design/100+NEW.s_low_design*NEW.f_unburned_loss_design/3387000))+NEW.d_boiler_total_design)*NEW.d_ash_share_design/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_ash_share_design ISNULL OR OLD.d_boiler_total_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_grey_design ISNULL) AND NEW.d_ash_share_design NOTNULL AND NEW.d_boiler_total_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_grey_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_ash_total_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(NEW.s_grey_design/100+NEW.s_low_design*NEW.f_unburned_loss_design/3387000))+NEW.d_boiler_total_design)*NEW.d_ash_share_design/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_dust_total:渣量,的计算11-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.d_boiler_total_design != NEW.d_boiler_total_design OR OLD.d_ash_share_design != NEW.d_ash_share_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     d_dust_total_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(NEW.s_grey_design/100+NEW.s_low_design*NEW.f_unburned_loss_design/3387000))+NEW.d_boiler_total_design)*(1-NEW.d_ash_share_design)/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_ash_share_design ISNULL OR OLD.d_boiler_total_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_grey_design ISNULL) AND NEW.d_ash_share_design NOTNULL AND NEW.d_boiler_total_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_grey_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_dust_total_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(NEW.s_grey_design/100+NEW.s_low_design*NEW.f_unburned_loss_design/3387000))+NEW.d_boiler_total_design)*(1-NEW.d_ash_share_design)/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_air_volumn:理论干空气量,的计算12-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     a_air_volumn_design=0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_air_volumn_design=0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_steam_perssure:水蒸气分压力,的计算13-----------------------------------
  IF OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design THEN
     update coalchp_furnace_calculation set 

     a_steam_perssure_design=NEW.a_humidity_design*NEW.a_saturation_pressure_design/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_humidity_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_steam_perssure_design=NEW.a_humidity_design*NEW.a_saturation_pressure_design/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_air_humidity:空气的绝对湿度（含湿量）,的计算14-----------------------------------
  IF OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design THEN
     update coalchp_furnace_calculation set 

     a_air_humidity_design=622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_air_humidity_design=622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_standard_air_humidity:标况下湿空气密度,的计算15-----------------------------------
  IF OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design THEN
     update coalchp_furnace_calculation set 

     a_standard_air_humidity_design=(1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_standard_air_humidity_design=(1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_wet_air_volumn:理论湿空气量,的计算16-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     a_wet_air_volumn_design=(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_wet_air_volumn_design=(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_nitrogen_volume:理论氮气容积,的计算17-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     s_nitrogen_volume_design=0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_nitrogen_volume_design=0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_dioxide_volume:理论二氧化物容积,的计算18-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     s_dioxide_volume_design=1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.s_sulfur_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_dioxide_volume_design=1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_steam_volume:理论水蒸汽容积,的计算19-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     s_steam_volume_design=0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_steam_volume_design=0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_smoke_volume:理论烟气容积,的计算20-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     s_smoke_volume_design=(0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_smoke_volume_design=(0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_1kg_weight:1kg燃料生成理论湿烟气的重量,的计算21-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     s_1kg_weight_design=1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_1kg_weight_design=1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_wet_smoke_density:标况下理论湿烟气密度,的计算22-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     s_wet_smoke_density_design=(1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))/((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     s_wet_smoke_density_design=(1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))/((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_wind_air:旋风分离器出口过剩空气系数,的计算23-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design THEN
     update coalchp_furnace_calculation set 

     p_wind_air_design=NEW.p_boiler_air_design+NEW.p_wind_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_wind_air_design=NEW.p_boiler_air_design+NEW.p_wind_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_hign_air:高过出口过剩空气系数,的计算24-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design THEN
     update coalchp_furnace_calculation set 

     p_hign_air_design=NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_hign_air_design=NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_low_air:低过出口过剩空气系数,的计算25-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design THEN
     update coalchp_furnace_calculation set 

     p_low_air_design=NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_low_air_design=NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_fule_air:省燃料器出口过剩空气系数,的计算26-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design THEN
     update coalchp_furnace_calculation set 

     p_fule_air_design=NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_fule_air_design=NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_heater_air:空预器出口过剩空气系数,的计算27-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design THEN
     update coalchp_furnace_calculation set 

     p_heater_air_design=NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_heater_air_design=NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_dust_exit:除尘器进口过剩空气系数,的计算28-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design THEN
     update coalchp_furnace_calculation set 

     p_dust_exit_design=NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_dust_exit_design=NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_dust_entry:除尘器出口过剩空气系数,的计算29-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design THEN
     update coalchp_furnace_calculation set 

     p_dust_entry_design=NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_dust_entry_design=NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_fans_air:引风机入口过剩空气系数,的计算30-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design THEN
     update coalchp_furnace_calculation set 

     p_fans_air_design=NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_fans_air_design=NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_1kg_volume:61Kg燃料产生的空预器出口湿烟气容积,的计算31-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     p_1kg_volume_design=((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_1kg_volume_design=((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段p_1kg_quality:61Kg燃料产生的空预器出口湿烟气质量,的计算32-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     p_1kg_quality_design=1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     p_1kg_quality_design=1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_theory_air_quality:理论空气量（体积,湿）,的计算33-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     a_theory_air_quality_design=((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_theory_air_quality_design=((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_boiler_air:炉膛出口过剩空气系数,的计算34-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design THEN
     update coalchp_furnace_calculation set 

     a_boiler_air_design=NEW.p_boiler_air_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_boiler_air_design ISNULL) AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_boiler_air_design=NEW.p_boiler_air_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_actual_air:实际空气量（体积,湿）,的计算35-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     a_actual_air_design=(NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_actual_air_design=(NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_calculation_consumption:计算燃料消耗量,的计算36-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design THEN
     update coalchp_furnace_calculation set 

     a_calculation_consumption_design=((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL) AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_calculation_consumption_design=((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_actual_air_total:实际空气总量（体积，湿）,的计算37-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     a_actual_air_total_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_actual_air_total_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_cwind_temperature_calculation:冷风温度（计算温度）,的计算38-----------------------------------
  IF OLD.p_heater_first_entry_design != NEW.p_heater_first_entry_design THEN
     update coalchp_furnace_calculation set 

     a_cwind_temperature_calculation_design=NEW.p_heater_first_entry_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_first_entry_design ISNULL) AND NEW.p_heater_first_entry_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_cwind_temperature_calculation_design=NEW.p_heater_first_entry_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_local_pressure:当地年平均气压,的计算39-----------------------------------
  IF OLD.a_pressure_design != NEW.a_pressure_design THEN
     update coalchp_furnace_calculation set 

     a_local_pressure_design=NEW.a_pressure_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_pressure_design ISNULL) AND NEW.a_pressure_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_local_pressure_design=NEW.a_pressure_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_cwind_standard:冷一次风量（湿-标准态）,的计算40-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_standard_design=NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_standard_design=NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_cwind_actual:冷一次风量（湿-实态）,的计算41-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_heater_first_entry_design != NEW.p_heater_first_entry_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_actual_design=(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_first_entry_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_first_entry_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_actual_design=(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_standard_air_density:标况下湿空气密度1,的计算42-----------------------------------
  IF OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design THEN
     update coalchp_furnace_calculation set 

     a_first_standard_air_density_design=((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_standard_air_density_design=((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_cwind_flow:冷一次风量（质量流量）,的计算43-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_flow_design=(((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_flow_design=(((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_cwind_density:冷一次风湿空气密度（湿-实态）,的计算44-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_heater_first_entry_design != NEW.p_heater_first_entry_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_density_design=((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_first_entry_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_first_entry_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_cwind_density_design=((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_check:校核,的计算45-----------------------------------
  IF OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.p_heater_first_entry_design != NEW.p_heater_first_entry_design THEN
     update coalchp_furnace_calculation set 

     a_check_design=(((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*273/(273+(NEW.p_heater_first_entry_design))*(NEW.a_pressure_design)/101.325
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_first_entry_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL) AND NEW.p_heater_first_entry_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_check_design=(((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*273/(273+(NEW.p_heater_first_entry_design))*(NEW.a_pressure_design)/101.325
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_hwind_temperatue:热一次风温度,的计算46-----------------------------------
  IF OLD.p_heater_first_exit_design != NEW.p_heater_first_exit_design THEN
     update coalchp_furnace_calculation set 

     a_first_hwind_temperatue_design=NEW.p_heater_first_exit_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_first_exit_design ISNULL) AND NEW.p_heater_first_exit_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_hwind_temperatue_design=NEW.p_heater_first_exit_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_hwind_flow:热一次风量（湿-实态）,的计算47-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_heater_first_exit_design != NEW.p_heater_first_exit_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_first_hwind_flow_design=(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_exit_design))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_first_exit_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_first_exit_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_hwind_flow_design=(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_exit_design))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_first_wet_air_density:湿空气密度（湿-实态）1,的计算48-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_heater_first_exit_design != NEW.p_heater_first_exit_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_first_wet_air_density_design=((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_exit_design))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_first_exit_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_first_exit_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_first_wet_air_density_design=((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_exit_design))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_wind_volume:二次风份额,的计算49-----------------------------------
  IF OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_second_wind_volume_design=100-NEW.a_first_wind_volume_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_wind_volume_design=100-NEW.a_first_wind_volume_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_cwind_temperature:冷风温度,的计算50-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_heater_first_entry_design != NEW.p_heater_first_entry_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_cwind_temperature_design=(((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_first_entry_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_first_entry_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_cwind_temperature_design=(((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_cwind_standard:冷二次风量（湿-标准态）,的计算51-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_standard_design=(100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_standard_design=(100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_cwind_actual:冷二次风量（湿-实态）,的计算52-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_heater_first_entry_design != NEW.p_heater_first_entry_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_actual_design=((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))*(273+((((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design)))))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_first_entry_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_first_entry_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_actual_design=((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))*(273+((((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design)))))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_standard_air_density:标况下湿空气密度2,的计算53-----------------------------------
  IF OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design THEN
     update coalchp_furnace_calculation set 

     a_second_standard_air_density_design=(((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL) AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_standard_air_density_design=(((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_cwind_flow:冷二次风量（质量流量）,的计算54-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_flow_design=((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804))))*((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_flow_design=((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804))))*((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_cwind_density:冷二次风湿空气密度（湿-实态）,的计算55-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_heater_first_entry_design != NEW.p_heater_first_entry_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_density_design=(((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804))))*((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))))/(((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))*(273+((((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design)))))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_first_entry_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_first_entry_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_cwind_density_design=(((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804))))*((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))))/(((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))*(273+((((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804)))*(NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100))/((NEW.a_first_wind_volume_design*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))/100)*(273+(NEW.p_heater_first_entry_design))/273*101.325/(NEW.a_pressure_design)))))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_hwind_temperatue:热二次风温度,的计算56-----------------------------------
  IF OLD.p_heater_second_exit_design != NEW.p_heater_second_exit_design THEN
     update coalchp_furnace_calculation set 

     a_second_hwind_temperatue_design=NEW.p_heater_second_exit_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_second_exit_design ISNULL) AND NEW.p_heater_second_exit_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_hwind_temperatue_design=NEW.p_heater_second_exit_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_hwind_flow:热二次风量（湿-实态）,的计算57-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_heater_second_exit_design != NEW.p_heater_second_exit_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_second_hwind_flow_design=((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))*(273+(NEW.p_heater_second_exit_design))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_second_exit_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_second_exit_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_hwind_flow_design=((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))*(273+(NEW.p_heater_second_exit_design))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_second_wet_air_density:湿空气密度（湿-实态）2,的计算58-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_heater_second_exit_design != NEW.p_heater_second_exit_design OR OLD.a_first_wind_volume_design != NEW.a_first_wind_volume_design THEN
     update coalchp_furnace_calculation set 

     a_second_wet_air_density_design=(((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804))))*((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))))/(((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))*(273+(NEW.p_heater_second_exit_design))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_first_wind_volume_design ISNULL OR OLD.p_heater_second_exit_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.a_first_wind_volume_design NOTNULL AND NEW.p_heater_second_exit_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     a_second_wet_air_density_design=(((((1+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))/(1/1.293+0.001*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/0.804))))*((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))))))/(((100-NEW.a_first_wind_volume_design)/100*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((NEW.p_boiler_air_design)*(((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))))))*(273+(NEW.p_heater_second_exit_design))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_1kg_volume:标况下空预器出口1Kg燃料湿烟气容积,的计算59-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     h_1kg_volume_design=(((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_1kg_volume_design=(((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_1kg_quality:空预器出口1Kg燃料产生的湿烟气质量,的计算60-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     h_1kg_quality_design=(1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_1kg_quality_design=(1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_calculation_consumption:计算燃料消耗量,的计算61-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design THEN
     update coalchp_furnace_calculation set 

     h_calculation_consumption_design=((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL) AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_calculation_consumption_design=((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_standard_smoke_flow:标况下空预器出口烟气容积流量,的计算62-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     h_standard_smoke_flow_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_standard_smoke_flow_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_smoke_flow:空预器出口烟气质量流量,的计算63-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     h_smoke_flow_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_smoke_flow_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_smoke_temperature:锅炉空预器出口排烟温度,的计算64-----------------------------------
  IF OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     h_smoke_temperature_design=NEW.p_smoke_temperature_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_smoke_temperature_design ISNULL) AND NEW.p_smoke_temperature_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_smoke_temperature_design=NEW.p_smoke_temperature_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_smoke_volume:空预器出口烟气容积量(实态）,的计算65-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     h_smoke_volume_design=((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))))*(273+(NEW.p_smoke_temperature_design))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_smoke_temperature_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_smoke_volume_design=((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))))*(273+(NEW.p_smoke_temperature_design))/273*101.325/(NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段h_smoke_density:烟气密度（实态）,的计算66-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     h_smoke_density_design=((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))/(((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))))*(273+(NEW.p_smoke_temperature_design))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_smoke_temperature_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     h_smoke_density_design=((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((1-NEW.s_grey_design/100+(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/1000)*1.293*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))/(((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))*((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))))*(273+(NEW.p_smoke_temperature_design))/273*101.325/(NEW.a_pressure_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_exit_air:空预器出口过剩空气系数,的计算67-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design THEN
     update coalchp_furnace_calculation set 

     d_exit_air_design=(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_exit_air_design=(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_wind_parameter:空预器至除尘器烟道漏风系数,的计算68-----------------------------------
  IF OLD.p_plus_air_design != NEW.p_plus_air_design THEN
     update coalchp_furnace_calculation set 

     d_wind_parameter_design=NEW.p_plus_air_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_design ISNULL) AND NEW.p_plus_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_wind_parameter_design=NEW.p_plus_air_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_air:除尘器进口过剩空气系数,的计算69-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design THEN
     update coalchp_furnace_calculation set 

     d_entry_air_design=(NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_air_design=(NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_somke_temperature:除尘器进口处烟气温度,的计算70-----------------------------------
  IF OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     d_entry_somke_temperature_design=(((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_somke_temperature_design=(((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_standard_1kg_volume:标况下除尘器进口处1kg燃料湿烟气容积,的计算71-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     d_standard_1kg_volume_design=((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_standard_1kg_volume_design=((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_1kg_quality:除尘器进口处1kg燃料湿烟气质量,的计算72-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     d_entry_1kg_quality_design=1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_1kg_quality_design=1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_standard_smoke_flow:标况下除尘器进口烟气容积流量,的计算73-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     d_standard_smoke_flow_design=(((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_standard_smoke_flow_design=(((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_somke_flow:除尘器进口处烟气质量流量,的计算74-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     d_entry_somke_flow_design=(1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_somke_flow_design=(1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_entry_smoke_actual_flow:除尘器进口处烟气容积流量(实态）,的计算75-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     d_entry_smoke_actual_flow_design=((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*101.325/273/NEW.a_pressure_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     d_entry_smoke_actual_flow_design=((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*101.325/273/NEW.a_pressure_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_wind_parameter:除尘器漏风系数,的计算76-----------------------------------
  IF OLD.p_dust_design != NEW.p_dust_design THEN
     update coalchp_furnace_calculation set 

     e_wind_parameter_design=NEW.p_dust_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_design ISNULL) AND NEW.p_dust_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_wind_parameter_design=NEW.p_dust_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_air_parameter:除尘器出口过剩空气系数,的计算77-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design THEN
     update coalchp_furnace_calculation set 

     e_air_parameter_design=(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_air_parameter_design=(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_smoke_temperature:除尘器出口烟气温度,的计算78-----------------------------------
  IF OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     e_smoke_temperature_design=((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_smoke_temperature_design=((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_standard_1kg_volume:标况下除尘器出口处1kg燃料湿烟气容积,的计算79-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     e_standard_1kg_volume_design=(((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_standard_1kg_volume_design=(((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_1kg_quality:除尘器出口处1kg燃料湿烟气质量,的计算80-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     e_1kg_quality_design=1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_1kg_quality_design=1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_standard_smoke_flow:标况下除尘器出口湿烟气容积流量,的计算81-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     e_standard_smoke_flow_design=((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_standard_smoke_flow_design=((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_smoke_flow:除尘器出口处湿烟气质量流量,的计算82-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     e_smoke_flow_design=(1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_smoke_flow_design=(1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_smoke_actual_flow:除尘器出口处湿烟气容积流量(实态）,的计算83-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     e_smoke_actual_flow_design=(((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))))/273*101.325/NEW.a_pressure_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_smoke_actual_flow_design=(((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))))/273*101.325/NEW.a_pressure_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段e_smoke_actual_density:烟气密度（实态）,的计算84-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     e_smoke_actual_density_design=((1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))/((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))))/273*101.325/NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     e_smoke_actual_density_design=((1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))/((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))))/273*101.325/NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_wind_parameter:除尘器出口至引风机烟道漏风系数,的计算85-----------------------------------
  IF OLD.p_plus_dust_design != NEW.p_plus_dust_design THEN
     update coalchp_furnace_calculation set 

     i_wind_parameter_design=NEW.p_plus_dust_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL) AND NEW.p_plus_dust_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_wind_parameter_design=NEW.p_plus_dust_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_air_parameter:引风机入口过剩空气系数,的计算86-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design THEN
     update coalchp_furnace_calculation set 

     i_air_parameter_design=(NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_air_parameter_design=(NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_temperature:引风机入口烟气温度,的计算87-----------------------------------
  IF OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     i_smoke_temperature_design=(((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))+(NEW.p_plus_dust_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_temperature_design=(((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))+(NEW.p_plus_dust_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_standard_1kg_volume:标况下引风机进口处1kg燃料湿烟气容积,的计算88-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     i_standard_1kg_volume_design=((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_standard_1kg_volume_design=((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_1kg_quality:引风机进口处1kg燃料湿烟气质量,的计算89-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     i_1kg_quality_design=1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_1kg_quality_design=1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_standard_smoke_flow1:标况下引风机进口湿烟气容积流量1,的计算90-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     i_standard_smoke_flow1_design=(((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_standard_smoke_flow1_design=(((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_standard_smoke_flow2:标况下引风机进口湿烟气容积流量2,的计算91-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     i_standard_smoke_flow2_design=((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))/3600
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_standard_smoke_flow2_design=((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))/3600
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_flow:引风机进口处湿烟气质量流量,的计算92-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     i_smoke_flow_design=(1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_flow_design=(1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_actual_flow1:引风机进口处湿烟气容积流量(实态）1,的计算93-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_flow1_design=((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+((((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))+(NEW.p_plus_dust_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))))/273*101.325/NEW.a_pressure_design
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_flow1_design=((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+((((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))+(NEW.p_plus_dust_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))))/273*101.325/NEW.a_pressure_design
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_actual_flow2:引风机进口处湿烟气容积流量(实态）2,的计算94-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_flow2_design=(((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+((((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))+(NEW.p_plus_dust_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))))/273*101.325/NEW.a_pressure_design)/3600
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_flow2_design=(((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+((((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))+(NEW.p_plus_dust_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))))/273*101.325/NEW.a_pressure_design)/3600
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_smoke_actual_density:烟气密度（实态）,的计算95-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.d_cold_air_temperature_design != NEW.d_cold_air_temperature_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.p_smoke_temperature_design != NEW.p_smoke_temperature_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_density_design=((1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))/(((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+((((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))+(NEW.p_plus_dust_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))))/273*101.325/NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_cold_air_temperature_design ISNULL OR OLD.p_smoke_temperature_design ISNULL OR OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.d_cold_air_temperature_design NOTNULL AND NEW.p_smoke_temperature_design NOTNULL AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_smoke_actual_density_design=((1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))/(((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))*(273+((((NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))*(((((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))*NEW.p_smoke_temperature_design+(NEW.p_plus_air_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_air_design)+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))+(NEW.p_plus_dust_design)*NEW.d_cold_air_temperature_design)/((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))))/273*101.325/NEW.a_pressure_design)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段i_wet_smoke_actual_density:引风机处计算湿烟气密度（标况）,的计算96-----------------------------------
  IF OLD.s_water_design != NEW.s_water_design OR OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.a_humidity_design != NEW.a_humidity_design OR OLD.a_pressure_design != NEW.a_pressure_design OR OLD.a_saturation_pressure_design != NEW.a_saturation_pressure_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_grey_design != NEW.s_grey_design THEN
     update coalchp_furnace_calculation set 

     i_wet_smoke_actual_density_design=((1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))/((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.a_saturation_pressure_design ISNULL OR OLD.a_pressure_design ISNULL OR OLD.a_humidity_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_water_design ISNULL OR OLD.s_grey_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.a_saturation_pressure_design NOTNULL AND NEW.a_pressure_design NOTNULL AND NEW.a_humidity_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_water_design NOTNULL AND NEW.s_grey_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     i_wet_smoke_actual_density_design=((1-NEW.s_grey_design/100+1.293*(1+(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))/100)*((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))/((((((((0.111*NEW.s_hydrogen_design+0.0124*NEW.s_water_design+1.293*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))/0.804/1000)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)+(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design))+((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.0161*((NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))+(NEW.p_plus_air_design)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)))))+0.0161*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))+((NEW.p_plus_dust_design)+0.0161)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))*(1+0.0016*(622*(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100)/(NEW.a_pressure_design-(NEW.a_humidity_design*NEW.a_saturation_pressure_design/100))))))*(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_oxygen_vol:烟气中的氧量,的计算97-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     go_oxygen_vol_design=0.21*(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_oxygen_vol_design=0.21*(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_theoretica_vol:理论干烟气容积,的计算98-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     go_theoretica_vol_design=(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_theoretica_vol_design=(0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_theoretica_flow:理论干空气量,的计算99-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     go_theoretica_flow_design=(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sulfur_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.s_sulfur_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_theoretica_flow_design=(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_calculation_consumption:计算燃料消耗量,的计算100-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design THEN
     update coalchp_furnace_calculation set 

     go_calculation_consumption_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL) AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_calculation_consumption_design=(((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_air_parameter:引风机入口过剩空气系数,的计算101-----------------------------------
  IF OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design THEN
     update coalchp_furnace_calculation set 

     go_air_parameter_design=(NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_air_parameter_design=(NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design))))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_standard_1kg_volume:121Kg燃料产生的引风机进口干烟气容积,的计算102-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     go_standard_1kg_volume_design=((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_standard_1kg_volume_design=((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_smoke_flow:引风机进口干烟气容积流量,的计算103-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     go_smoke_flow_design=(((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_smoke_flow_design=(((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_drygas_oxygen_vol:干烟气中含氧量,的计算104-----------------------------------
  IF OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     go_drygas_oxygen_vol_design=(0.21*(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))/(((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))*100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_drygas_oxygen_vol_design=(0.21*(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))/(((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))*100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段go_total_combustion_product_vol:总燃烧产物6%O2干体积,的计算105-----------------------------------
  IF OLD.s_low_design != NEW.s_low_design OR OLD.f_steam_flow_design != NEW.f_steam_flow_design OR OLD.f_steam_enthalpy_design != NEW.f_steam_enthalpy_design OR OLD.f_saturated_water_enthalpy_design != NEW.f_saturated_water_enthalpy_design OR OLD.f_water_enthalpy_design != NEW.f_water_enthalpy_design OR OLD.f_boiler_efficiency_design != NEW.f_boiler_efficiency_design OR OLD.f_unburned_loss_design != NEW.f_unburned_loss_design OR OLD.f_blowdown_rate_design != NEW.f_blowdown_rate_design OR OLD.s_carbon_design != NEW.s_carbon_design OR OLD.s_hydrogen_design != NEW.s_hydrogen_design OR OLD.p_boiler_air_design != NEW.p_boiler_air_design OR OLD.p_wind_design != NEW.p_wind_design OR OLD.s_oxygen_design != NEW.s_oxygen_design OR OLD.p_high_design != NEW.p_high_design OR OLD.p_low_design != NEW.p_low_design OR OLD.p_fule_design != NEW.p_fule_design OR OLD.p_heater_design != NEW.p_heater_design OR OLD.p_plus_air_design != NEW.p_plus_air_design OR OLD.s_nitrogen_design != NEW.s_nitrogen_design OR OLD.p_dust_design != NEW.p_dust_design OR OLD.p_plus_dust_design != NEW.p_plus_dust_design OR OLD.s_sulfur_design != NEW.s_sulfur_design THEN
     update coalchp_furnace_calculation set 

     go_total_combustion_product_vol_design=((((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))))*(21-((0.21*(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))/(((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))*100))/(21-6)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.p_plus_dust_design ISNULL OR OLD.p_dust_design ISNULL OR OLD.p_plus_air_design ISNULL OR OLD.p_heater_design ISNULL OR OLD.p_fule_design ISNULL OR OLD.p_low_design ISNULL OR OLD.p_high_design ISNULL OR OLD.p_wind_design ISNULL OR OLD.p_boiler_air_design ISNULL OR OLD.f_blowdown_rate_design ISNULL OR OLD.f_unburned_loss_design ISNULL OR OLD.f_boiler_efficiency_design ISNULL OR OLD.f_water_enthalpy_design ISNULL OR OLD.f_saturated_water_enthalpy_design ISNULL OR OLD.f_steam_enthalpy_design ISNULL OR OLD.f_steam_flow_design ISNULL OR OLD.s_low_design ISNULL OR OLD.s_sulfur_design ISNULL OR OLD.s_nitrogen_design ISNULL OR OLD.s_oxygen_design ISNULL OR OLD.s_hydrogen_design ISNULL OR OLD.s_carbon_design ISNULL) AND NEW.p_plus_dust_design NOTNULL AND NEW.p_dust_design NOTNULL AND NEW.p_plus_air_design NOTNULL AND NEW.p_heater_design NOTNULL AND NEW.p_fule_design NOTNULL AND NEW.p_low_design NOTNULL AND NEW.p_high_design NOTNULL AND NEW.p_wind_design NOTNULL AND NEW.p_boiler_air_design NOTNULL AND NEW.f_blowdown_rate_design NOTNULL AND NEW.f_unburned_loss_design NOTNULL AND NEW.f_boiler_efficiency_design NOTNULL AND NEW.f_water_enthalpy_design NOTNULL AND NEW.f_saturated_water_enthalpy_design NOTNULL AND NEW.f_steam_enthalpy_design NOTNULL AND NEW.f_steam_flow_design NOTNULL AND NEW.s_low_design NOTNULL AND NEW.s_sulfur_design NOTNULL AND NEW.s_nitrogen_design NOTNULL AND NEW.s_oxygen_design NOTNULL AND NEW.s_hydrogen_design NOTNULL AND NEW.s_carbon_design NOTNULL THEN
     update coalchp_furnace_calculation set 

     go_total_combustion_product_vol_design=((((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))*((((NEW.f_steam_flow_design*1000/NEW.f_boiler_efficiency_design*((NEW.f_steam_enthalpy_design-NEW.f_water_enthalpy_design)+NEW.f_blowdown_rate_design*(NEW.f_saturated_water_enthalpy_design-NEW.f_water_enthalpy_design))/NEW.s_low_design)*(1-NEW.f_unburned_loss_design)))))*(21-((0.21*(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design)))/(((0.79*(0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))+0.008*NEW.s_nitrogen_design)+(1.866*(NEW.s_carbon_design+0.375*NEW.s_sulfur_design)/100))+(((NEW.p_plus_dust_design+(NEW.p_dust_design+(NEW.p_plus_air_design+(NEW.p_heater_design+(NEW.p_fule_design+(NEW.p_low_design+(NEW.p_high_design+(NEW.p_boiler_air_design+NEW.p_wind_design)))))))))-1)*((0.0889*NEW.s_carbon_design+0.265*NEW.s_hydrogen_design-0.0333*(NEW.s_oxygen_design-NEW.s_sulfur_design))))*100))/(21-6)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_furnace_calculation_design" AFTER UPDATE OF
"s_water_design",
"d_cold_air_temperature_design",
"s_low_design",
"f_steam_flow_design",
"f_steam_pressure_design",
"f_steam_enthalpy_design",
"f_saturated_water_enthalpy_design",
"f_water_enthalpy_design",
"f_boiler_efficiency_design",
"f_unburned_loss_design",
"f_blowdown_rate_design",
"d_boiler_total_design",
"d_ash_share_design",
"s_carbon_design",
"a_humidity_design",
"a_pressure_design",
"a_saturation_pressure_design",
"s_hydrogen_design",
"p_boiler_air_design",
"p_wind_design",
"s_oxygen_design",
"p_high_design",
"p_low_design",
"p_fule_design",
"p_heater_design",
"p_plus_air_design",
"s_nitrogen_design",
"p_dust_design",
"p_plus_dust_design",
"p_heater_first_entry_design",
"s_sulfur_design",
"p_heater_first_exit_design",
"p_heater_second_exit_design",
"p_smoke_temperature_design",
"s_grey_design",
"a_first_wind_volume_design"
ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_design"();

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

CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段a_dust_collector_inlet_:除尘器入口（锅炉出口）飞灰量,的计算1-----------------------------------
  IF OLD.a_total_ash_residue_after != NEW.a_total_ash_residue_after OR OLD.a_fly_ash_content != NEW.a_fly_ash_content THEN
     update coalchp_removal_ash_slag_system set 

     a_dust_collector_inlet_=NEW.a_fly_ash_content*NEW.a_total_ash_residue_after
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_fly_ash_content ISNULL OR OLD.a_total_ash_residue_after ISNULL) AND NEW.a_fly_ash_content NOTNULL AND NEW.a_total_ash_residue_after NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_dust_collector_inlet_=NEW.a_fly_ash_content*NEW.a_total_ash_residue_after
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_the_smoke_concentration:标况下除尘器进口烟气浓度,的计算2-----------------------------------
  IF OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ OR OLD.a_the_imported_smoke_volume != NEW.a_the_imported_smoke_volume THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration=NEW.a_dust_collector_inlet_*10^6/NEW.a_the_imported_smoke_volume
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_the_imported_smoke_volume ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_the_imported_smoke_volume NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration=NEW.a_dust_collector_inlet_*10^6/NEW.a_the_imported_smoke_volume
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_the_smoke_concentration_solid:除尘器进口处烟气浓度(实态）,的计算3-----------------------------------
  IF OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ OR OLD.a_the_smoke_volume_flow != NEW.a_the_smoke_volume_flow THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration_solid=NEW.a_dust_collector_inlet_*10^6/NEW.a_the_smoke_volume_flow
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_the_smoke_volume_flow ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_the_smoke_volume_flow NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration_solid=NEW.a_dust_collector_inlet_*10^6/NEW.a_the_smoke_volume_flow
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_the_smoke_concentration_chimney:除尘器（烟囱）出口烟气浓度（标况）,的计算4-----------------------------------
  IF OLD.a_collection_efficiency != NEW.a_collection_efficiency OR OLD.a_the_smoke_concentration != NEW.a_the_smoke_concentration THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration_chimney=NEW.a_the_smoke_concentration*(1-NEW.a_collection_efficiency/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_collection_efficiency ISNULL OR OLD.a_the_smoke_concentration ISNULL) AND NEW.a_collection_efficiency NOTNULL AND NEW.a_the_smoke_concentration NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration_chimney=NEW.a_the_smoke_concentration*(1-NEW.a_collection_efficiency/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_dust_collector_stack:除尘器（烟囱）出口烟气飞灰量（标况）,的计算5-----------------------------------
  IF OLD.a_collection_efficiency != NEW.a_collection_efficiency OR OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ THEN
     update coalchp_removal_ash_slag_system set 

     a_dust_collector_stack=NEW.a_dust_collector_inlet_*(1-NEW.a_collection_efficiency/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_collection_efficiency ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_collection_efficiency NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_dust_collector_stack=NEW.a_dust_collector_inlet_*(1-NEW.a_collection_efficiency/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_ash_under_dust_collector:除尘器下灰量,的计算6-----------------------------------
  IF OLD.a_collection_efficiency != NEW.a_collection_efficiency OR OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ THEN
     update coalchp_removal_ash_slag_system set 

     a_ash_under_dust_collector=NEW.a_dust_collector_inlet_*NEW.a_collection_efficiency/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_collection_efficiency ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_collection_efficiency NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_ash_under_dust_collector=NEW.a_dust_collector_inlet_*NEW.a_collection_efficiency/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_flue_gas_concentratio:烟囱出口烟气浓度（实态）,的计算7-----------------------------------
  IF OLD.a_collection_efficiency != NEW.a_collection_efficiency OR OLD.a_the_imported_smoke_real_state != NEW.a_the_imported_smoke_real_state OR OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ THEN
     update coalchp_removal_ash_slag_system set 

     a_flue_gas_concentratio=NEW.a_dust_collector_inlet_*(1-NEW.a_collection_efficiency/100)*10^6/NEW.a_the_imported_smoke_real_state
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_the_imported_smoke_real_state ISNULL OR OLD.a_collection_efficiency ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_the_imported_smoke_real_state NOTNULL AND NEW.a_collection_efficiency NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_flue_gas_concentratio=NEW.a_dust_collector_inlet_*(1-NEW.a_collection_efficiency/100)*10^6/NEW.a_the_imported_smoke_real_state
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_removal_the_ash_system:除灰系统出力,的计算8-----------------------------------
  IF OLD.a_ash_under_dust_collector != NEW.a_ash_under_dust_collector OR OLD.r_removal_coefficient != NEW.r_removal_coefficient THEN
     update coalchp_removal_ash_slag_system set 

     r_removal_the_ash_system=NEW.a_ash_under_dust_collector*NEW.r_removal_coefficient/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_removal_coefficient ISNULL OR OLD.a_ash_under_dust_collector ISNULL) AND NEW.r_removal_coefficient NOTNULL AND NEW.a_ash_under_dust_collector NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     r_removal_the_ash_system=NEW.a_ash_under_dust_collector*NEW.r_removal_coefficient/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_effective_volume_ash_storage:灰库有效体积,的计算9-----------------------------------
  IF OLD.a_ash_under_dust_collector != NEW.a_ash_under_dust_collector OR OLD.r_dry_ash_accumulation_density != NEW.r_dry_ash_accumulation_density OR OLD.r_slag_accumulation_coefficient != NEW.r_slag_accumulation_coefficient OR OLD.r_stored_ash != NEW.r_stored_ash THEN
     update coalchp_removal_ash_slag_system set 

     r_effective_volume_ash_storage=NEW.a_ash_under_dust_collector/1000*NEW.r_stored_ash*22/NEW.r_dry_ash_accumulation_density/NEW.r_slag_accumulation_coefficient
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_stored_ash ISNULL OR OLD.r_slag_accumulation_coefficient ISNULL OR OLD.r_dry_ash_accumulation_density ISNULL OR OLD.a_ash_under_dust_collector ISNULL) AND NEW.r_stored_ash NOTNULL AND NEW.r_slag_accumulation_coefficient NOTNULL AND NEW.r_dry_ash_accumulation_density NOTNULL AND NEW.a_ash_under_dust_collector NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     r_effective_volume_ash_storage=NEW.a_ash_under_dust_collector/1000*NEW.r_stored_ash*22/NEW.r_dry_ash_accumulation_density/NEW.r_slag_accumulation_coefficient
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_height:高度,的计算10-----------------------------------
  IF OLD.r_effective_volume_ash_storage != NEW.r_effective_volume_ash_storage OR OLD.r_dia != NEW.r_dia THEN
     update coalchp_removal_ash_slag_system set 

     r_height=NEW.r_effective_volume_ash_storage/(3.14*(NEW.r_dia/2)^2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_dia ISNULL OR OLD.r_effective_volume_ash_storage ISNULL) AND NEW.r_dia NOTNULL AND NEW.r_effective_volume_ash_storage NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     r_height=NEW.r_effective_volume_ash_storage/(3.14*(NEW.r_dia/2)^2)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_air_transport_ash_system:输灰系统耗气量,的计算11-----------------------------------
  IF OLD.r_removal_the_ash_system != NEW.r_removal_the_ash_system OR OLD.g_grey_gas != NEW.g_grey_gas THEN
     update coalchp_removal_ash_slag_system set 

     g_air_transport_ash_system=1.2*NEW.r_removal_the_ash_system*16.67/NEW.g_grey_gas/1.293
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_grey_gas ISNULL OR OLD.r_removal_the_ash_system ISNULL) AND NEW.g_grey_gas NOTNULL AND NEW.r_removal_the_ash_system NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     g_air_transport_ash_system=1.2*NEW.r_removal_the_ash_system*16.67/NEW.g_grey_gas/1.293
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_output_cold_single_stage:冷渣机的出力（单台）,的计算12-----------------------------------
  IF OLD.s_slag_amount != NEW.s_slag_amount THEN
     update coalchp_removal_ash_slag_system set 

     s_output_cold_single_stage=2.5*NEW.s_slag_amount
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_slag_amount ISNULL) AND NEW.s_slag_amount NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_output_cold_single_stage=2.5*NEW.s_slag_amount
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_slag_removal_system:除渣系统出力,的计算13-----------------------------------
  IF OLD.s_output_cold_single_stage != NEW.s_output_cold_single_stage OR OLD.s_cold_single_stage_count != NEW.s_cold_single_stage_count THEN
     update coalchp_removal_ash_slag_system set 

     s_slag_removal_system=2.5*NEW.s_output_cold_single_stage*NEW.s_cold_single_stage_count
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_cold_single_stage_count ISNULL OR OLD.s_output_cold_single_stage ISNULL) AND NEW.s_cold_single_stage_count NOTNULL AND NEW.s_output_cold_single_stage NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_slag_removal_system=2.5*NEW.s_output_cold_single_stage*NEW.s_cold_single_stage_count
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_high_temperature_belt_conveyor:耐高温带式输送机出力,的计算14-----------------------------------
  IF OLD.s_slag_removal_system != NEW.s_slag_removal_system THEN
     update coalchp_removal_ash_slag_system set 

     s_high_temperature_belt_conveyor=NEW.s_slag_removal_system
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_slag_removal_system ISNULL) AND NEW.s_slag_removal_system NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_high_temperature_belt_conveyor=NEW.s_slag_removal_system
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_slag_storage_volume_effective:渣库有效体积,的计算15-----------------------------------
  IF OLD.s_slag_amount != NEW.s_slag_amount OR OLD.s_cold_slag_accumulation_density != NEW.s_cold_slag_accumulation_density OR OLD.s_slag_accumulation_coefficient != NEW.s_slag_accumulation_coefficient OR OLD.s_sludge_time != NEW.s_sludge_time THEN
     update coalchp_removal_ash_slag_system set 

     s_slag_storage_volume_effective=NEW.s_slag_amount*NEW.s_sludge_time*22/NEW.s_cold_slag_accumulation_density/NEW.s_slag_accumulation_coefficient
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sludge_time ISNULL OR OLD.s_slag_accumulation_coefficient ISNULL OR OLD.s_cold_slag_accumulation_density ISNULL OR OLD.s_slag_amount ISNULL) AND NEW.s_sludge_time NOTNULL AND NEW.s_slag_accumulation_coefficient NOTNULL AND NEW.s_cold_slag_accumulation_density NOTNULL AND NEW.s_slag_amount NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_slag_storage_volume_effective=NEW.s_slag_amount*NEW.s_sludge_time*22/NEW.s_cold_slag_accumulation_density/NEW.s_slag_accumulation_coefficient
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_height:高度,的计算16-----------------------------------
  IF OLD.s_slag_storage_volume_effective != NEW.s_slag_storage_volume_effective OR OLD.s_dia != NEW.s_dia THEN
     update coalchp_removal_ash_slag_system set 

     s_height=NEW.s_slag_storage_volume_effective/(3.14*(NEW.s_dia/2)^2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_dia ISNULL OR OLD.s_slag_storage_volume_effective ISNULL) AND NEW.s_dia NOTNULL AND NEW.s_slag_storage_volume_effective NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_height=NEW.s_slag_storage_volume_effective/(3.14*(NEW.s_dia/2)^2)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_removal_ash_slag_system" AFTER UPDATE OF
"a_collection_efficiency",
"a_ash_under_dust_collector",
"a_the_imported_smoke_real_state",
"r_removal_coefficient",
"r_removal_the_ash_system",
"r_dry_ash_accumulation_density",
"r_slag_accumulation_coefficient",
"r_stored_ash",
"r_effective_volume_ash_storage",
"r_dia",
"g_grey_gas",
"s_slag_amount",
"a_total_ash_residue_after",
"s_output_cold_single_stage",
"s_cold_single_stage_count",
"s_slag_removal_system",
"s_cold_slag_accumulation_density",
"s_slag_accumulation_coefficient",
"s_sludge_time",
"s_slag_storage_volume_effective",
"s_dia",
"a_fly_ash_content",
"a_dust_collector_inlet_",
"a_the_imported_smoke_volume",
"a_the_smoke_volume_flow",
"a_the_smoke_concentration"
ON "public"."coalchp_removal_ash_slag_system"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system"();

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

----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_furnace_calculation的r_boiler_evaporation字段，和表coalchp_boiler_auxiliaries的f_steam_flow_design字段，即：coalchp_boiler_auxiliaries.r_boiler_evaporation=coalchp_furnace_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION coalchp_boiler_auxiliaries_r_boiler_evaporation()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_boiler_auxiliaries set r_boiler_evaporation=coalchp_furnace_calculation.f_steam_flow_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的r_drum_pressure字段，和表coalchp_boiler_auxiliaries的f_saturated_water_enthalpy_design字段，即：coalchp_boiler_auxiliaries.r_drum_pressure=coalchp_furnace_calculation.f_saturated_water_enthalpy_design
CREATE OR REPLACE FUNCTION coalchp_boiler_auxiliaries_r_drum_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_boiler_auxiliaries set r_drum_pressure=coalchp_furnace_calculation.f_saturated_water_enthalpy_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的m_condensing_capacity字段，和表coalchp_boiler_auxiliaries的f_steam_pressure_design字段，即：coalchp_boiler_auxiliaries.m_condensing_capacity=coalchp_furnace_calculation.f_steam_pressure_design
CREATE OR REPLACE FUNCTION coalchp_boiler_auxiliaries_m_condensing_capacity()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_boiler_auxiliaries set m_condensing_capacity=coalchp_furnace_calculation.f_steam_pressure_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当f_steam_flow_design有更新时触发coalchp_boiler_auxiliaries.r_boiler_evaporation=coalchp_furnace_calculation.f_steam_flow_design
CREATE TRIGGER "coalchp_furnace_calculation_a_13" AFTER UPDATE OF "f_steam_flow_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_boiler_auxiliaries_r_boiler_evaporation"();


--该触发器用于：当f_saturated_water_enthalpy_design有更新时触发coalchp_boiler_auxiliaries.r_drum_pressure=coalchp_furnace_calculation.f_saturated_water_enthalpy_design
CREATE TRIGGER "coalchp_furnace_calculation_a_14" AFTER UPDATE OF "f_saturated_water_enthalpy_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_boiler_auxiliaries_r_drum_pressure"();


--该触发器用于：当f_steam_pressure_design有更新时触发coalchp_boiler_auxiliaries.m_condensing_capacity=coalchp_furnace_calculation.f_steam_pressure_design
CREATE TRIGGER "coalchp_furnace_calculation_a_15" AFTER UPDATE OF "f_steam_pressure_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_boiler_auxiliaries_m_condensing_capacity"();


----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_furnace_calculation的s_sulfur_design字段，和表coalchp_desulfurization_denitrification的s_sulfur_design字段，即：coalchp_desulfurization_denitrification.s_sulfur_design=coalchp_furnace_calculation.s_sulfur_design
CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification_s_sulfur_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_desulfurization_denitrification set s_sulfur_design=coalchp_furnace_calculation.s_sulfur_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_desulfurization_denitrification.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的s_calcu_coal_consume字段，和表coalchp_desulfurization_denitrification的f_calculation_consumption_design字段，即：coalchp_desulfurization_denitrification.s_calcu_coal_consume=coalchp_furnace_calculation.f_calculation_consumption_design
CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification_s_calcu_coal_consume()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_desulfurization_denitrification set s_calcu_coal_consume=coalchp_furnace_calculation.f_calculation_consumption_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_desulfurization_denitrification.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的s_fan_smoke_flow字段，和表coalchp_desulfurization_denitrification的i_standard_smoke_flow1_design字段，即：coalchp_desulfurization_denitrification.s_fan_smoke_flow=coalchp_furnace_calculation.i_standard_smoke_flow1_design
CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification_s_fan_smoke_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_desulfurization_denitrification set s_fan_smoke_flow=coalchp_furnace_calculation.i_standard_smoke_flow1_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_desulfurization_denitrification.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;



----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_needs_questionnaire的n_env_after_nox_concentration字段，和表coalchp_desulfurization_denitrification的op_flue_gas_nox_limits_value字段，即：coalchp_desulfurization_denitrification.n_env_after_nox_concentration=coalchp_needs_questionnaire.op_flue_gas_nox_limits_value
CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification_n_env_after_nox_concent()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_desulfurization_denitrification set n_env_after_nox_concentration=coalchp_needs_questionnaire.op_flue_gas_nox_limits_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_desulfurization_denitrification.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_needs_questionnaire的s_carbon_design字段，和表coalchp_furnace_calculation的s_carbon_design字段，即：coalchp_furnace_calculation.s_carbon_design=coalchp_needs_questionnaire.s_carbon_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_carbon_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_carbon_design=coalchp_needs_questionnaire.s_carbon_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_hydrogen_design字段，和表coalchp_furnace_calculation的s_hydrogen_design字段，即：coalchp_furnace_calculation.s_hydrogen_design=coalchp_needs_questionnaire.s_hydrogen_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_hydrogen_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_hydrogen_design=coalchp_needs_questionnaire.s_hydrogen_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_oxygen_design字段，和表coalchp_furnace_calculation的s_oxygen_design字段，即：coalchp_furnace_calculation.s_oxygen_design=coalchp_needs_questionnaire.s_oxygen_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_oxygen_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_oxygen_design=coalchp_needs_questionnaire.s_oxygen_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_nitrogen_design字段，和表coalchp_furnace_calculation的s_nitrogen_design字段，即：coalchp_furnace_calculation.s_nitrogen_design=coalchp_needs_questionnaire.s_nitrogen_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_nitrogen_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_nitrogen_design=coalchp_needs_questionnaire.s_nitrogen_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_sulfur_design字段，和表coalchp_furnace_calculation的s_sulfur_design字段，即：coalchp_furnace_calculation.s_sulfur_design=coalchp_needs_questionnaire.s_sulfur_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_sulfur_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_sulfur_design=coalchp_needs_questionnaire.s_sulfur_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_water_design字段，和表coalchp_furnace_calculation的s_water_design字段，即：coalchp_furnace_calculation.s_water_design=coalchp_needs_questionnaire.s_water_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_water_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_water_design=coalchp_needs_questionnaire.s_water_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_grey_design字段，和表coalchp_furnace_calculation的s_grey_design字段，即：coalchp_furnace_calculation.s_grey_design=coalchp_needs_questionnaire.s_grey_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_grey_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_grey_design=coalchp_needs_questionnaire.s_grey_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_daf_design字段，和表coalchp_furnace_calculation的s_daf_design字段，即：coalchp_furnace_calculation.s_daf_design=coalchp_needs_questionnaire.s_daf_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_daf_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_daf_design=coalchp_needs_questionnaire.s_daf_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_grindability_design字段，和表coalchp_furnace_calculation的s_low_design字段，即：coalchp_furnace_calculation.s_grindability_design=coalchp_needs_questionnaire.s_low_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_grindability_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_grindability_design=coalchp_needs_questionnaire.s_low_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_low_design字段，和表coalchp_furnace_calculation的s_low_design字段，即：coalchp_furnace_calculation.s_low_design=coalchp_needs_questionnaire.s_low_design
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_low_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_low_design=coalchp_needs_questionnaire.s_low_design
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_carbon_check字段，和表coalchp_furnace_calculation的s_carbon_check字段，即：coalchp_furnace_calculation.s_carbon_check=coalchp_needs_questionnaire.s_carbon_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_carbon_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_carbon_check=coalchp_needs_questionnaire.s_carbon_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_hydrogen_check字段，和表coalchp_furnace_calculation的s_hydrogen_check字段，即：coalchp_furnace_calculation.s_hydrogen_check=coalchp_needs_questionnaire.s_hydrogen_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_hydrogen_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_hydrogen_check=coalchp_needs_questionnaire.s_hydrogen_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_oxygen_check字段，和表coalchp_furnace_calculation的s_oxygen_check字段，即：coalchp_furnace_calculation.s_oxygen_check=coalchp_needs_questionnaire.s_oxygen_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_oxygen_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_oxygen_check=coalchp_needs_questionnaire.s_oxygen_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_nitrogen_check字段，和表coalchp_furnace_calculation的s_nitrogen_check字段，即：coalchp_furnace_calculation.s_nitrogen_check=coalchp_needs_questionnaire.s_nitrogen_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_nitrogen_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_nitrogen_check=coalchp_needs_questionnaire.s_nitrogen_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_sulfur_check字段，和表coalchp_furnace_calculation的s_sulfur_check字段，即：coalchp_furnace_calculation.s_sulfur_check=coalchp_needs_questionnaire.s_sulfur_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_sulfur_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_sulfur_check=coalchp_needs_questionnaire.s_sulfur_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_water_check字段，和表coalchp_furnace_calculation的s_water_check字段，即：coalchp_furnace_calculation.s_water_check=coalchp_needs_questionnaire.s_water_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_water_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_water_check=coalchp_needs_questionnaire.s_water_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_grey_check字段，和表coalchp_furnace_calculation的s_grey_check字段，即：coalchp_furnace_calculation.s_grey_check=coalchp_needs_questionnaire.s_grey_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_grey_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_grey_check=coalchp_needs_questionnaire.s_grey_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_daf_check字段，和表coalchp_furnace_calculation的s_daf_check字段，即：coalchp_furnace_calculation.s_daf_check=coalchp_needs_questionnaire.s_daf_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_daf_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_daf_check=coalchp_needs_questionnaire.s_daf_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_grindability_check字段，和表coalchp_furnace_calculation的s_grindability_check字段，即：coalchp_furnace_calculation.s_grindability_check=coalchp_needs_questionnaire.s_grindability_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_grindability_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_grindability_check=coalchp_needs_questionnaire.s_grindability_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的s_low_check字段，和表coalchp_furnace_calculation的s_low_check字段，即：coalchp_furnace_calculation.s_low_check=coalchp_needs_questionnaire.s_low_check
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_s_low_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set s_low_check=coalchp_needs_questionnaire.s_low_check
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的a_humidity_design字段，和表coalchp_furnace_calculation的w_annual_average_relative_humidity_value字段，即：coalchp_furnace_calculation.a_humidity_design=coalchp_needs_questionnaire.w_annual_average_relative_humidity_value
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_a_humidity_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set a_humidity_design=coalchp_needs_questionnaire.w_annual_average_relative_humidity_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的a_pressure_design字段，和表coalchp_furnace_calculation的w_mean_annual_barometric_value字段，即：coalchp_furnace_calculation.a_pressure_design=coalchp_needs_questionnaire.w_mean_annual_barometric_value
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_a_pressure_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set a_pressure_design=coalchp_needs_questionnaire.w_mean_annual_barometric_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的a_temperature_design字段，和表coalchp_furnace_calculation的w_mean_annual_temperature_value字段，即：coalchp_furnace_calculation.a_temperature_design=coalchp_needs_questionnaire.w_mean_annual_temperature_value
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_a_temperature_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set a_temperature_design=coalchp_needs_questionnaire.w_mean_annual_temperature_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的a_temperature_check字段，和表coalchp_furnace_calculation的w_mean_annual_temperature_value字段，即：coalchp_furnace_calculation.a_temperature_check=coalchp_needs_questionnaire.w_mean_annual_temperature_value
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_a_temperature_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set a_temperature_check=coalchp_needs_questionnaire.w_mean_annual_temperature_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的a_pressure_check字段，和表coalchp_furnace_calculation的w_mean_annual_barometric_value字段，即：coalchp_furnace_calculation.a_pressure_check=coalchp_needs_questionnaire.w_mean_annual_barometric_value
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_a_pressure_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set a_pressure_check=coalchp_needs_questionnaire.w_mean_annual_barometric_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的a_humidity_check字段，和表coalchp_furnace_calculation的w_annual_average_relative_humidity_value字段，即：coalchp_furnace_calculation.a_humidity_check=coalchp_needs_questionnaire.w_annual_average_relative_humidity_value
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_a_humidity_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set a_humidity_check=coalchp_needs_questionnaire.w_annual_average_relative_humidity_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的a_hot_temperature_check字段，和表coalchp_furnace_calculation的w_mean_summer_temperature_value字段，即：coalchp_furnace_calculation.a_hot_temperature_check=coalchp_needs_questionnaire.w_mean_summer_temperature_value
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_a_hot_temperature_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set a_hot_temperature_check=coalchp_needs_questionnaire.w_mean_summer_temperature_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的a_hot_temperature_design字段，和表coalchp_furnace_calculation的w_mean_summer_temperature_value字段，即：coalchp_furnace_calculation.a_hot_temperature_design=coalchp_needs_questionnaire.w_mean_summer_temperature_value
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_a_hot_temperature_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set a_hot_temperature_design=coalchp_needs_questionnaire.w_mean_summer_temperature_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当s_carbon_design有更新时触发coalchp_furnace_calculation.s_carbon_design=coalchp_needs_questionnaire.s_carbon_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_0" AFTER UPDATE OF "s_carbon_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_carbon_design"();


--该触发器用于：当s_hydrogen_design有更新时触发coalchp_furnace_calculation.s_hydrogen_design=coalchp_needs_questionnaire.s_hydrogen_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_1" AFTER UPDATE OF "s_hydrogen_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_hydrogen_design"();


--该触发器用于：当s_oxygen_design有更新时触发coalchp_furnace_calculation.s_oxygen_design=coalchp_needs_questionnaire.s_oxygen_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_2" AFTER UPDATE OF "s_oxygen_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_oxygen_design"();


--该触发器用于：当s_nitrogen_design有更新时触发coalchp_furnace_calculation.s_nitrogen_design=coalchp_needs_questionnaire.s_nitrogen_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_3" AFTER UPDATE OF "s_nitrogen_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_nitrogen_design"();


--该触发器用于：当s_sulfur_design有更新时触发coalchp_furnace_calculation.s_sulfur_design=coalchp_needs_questionnaire.s_sulfur_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_4" AFTER UPDATE OF "s_sulfur_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_sulfur_design"();


--该触发器用于：当s_water_design有更新时触发coalchp_furnace_calculation.s_water_design=coalchp_needs_questionnaire.s_water_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_5" AFTER UPDATE OF "s_water_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_water_design"();


--该触发器用于：当s_grey_design有更新时触发coalchp_furnace_calculation.s_grey_design=coalchp_needs_questionnaire.s_grey_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_6" AFTER UPDATE OF "s_grey_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_grey_design"();


--该触发器用于：当s_daf_design有更新时触发coalchp_furnace_calculation.s_daf_design=coalchp_needs_questionnaire.s_daf_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_7" AFTER UPDATE OF "s_daf_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_daf_design"();


--该触发器用于：当s_low_design有更新时触发coalchp_furnace_calculation.s_grindability_design=coalchp_needs_questionnaire.s_low_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_8" AFTER UPDATE OF "s_low_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_grindability_design"();


--该触发器用于：当s_low_design有更新时触发coalchp_furnace_calculation.s_low_design=coalchp_needs_questionnaire.s_low_design
CREATE TRIGGER "coalchp_needs_questionnaire_a_9" AFTER UPDATE OF "s_low_design" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_low_design"();


--该触发器用于：当s_carbon_check有更新时触发coalchp_furnace_calculation.s_carbon_check=coalchp_needs_questionnaire.s_carbon_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_10" AFTER UPDATE OF "s_carbon_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_carbon_check"();


--该触发器用于：当s_hydrogen_check有更新时触发coalchp_furnace_calculation.s_hydrogen_check=coalchp_needs_questionnaire.s_hydrogen_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_11" AFTER UPDATE OF "s_hydrogen_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_hydrogen_check"();


--该触发器用于：当s_oxygen_check有更新时触发coalchp_furnace_calculation.s_oxygen_check=coalchp_needs_questionnaire.s_oxygen_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_12" AFTER UPDATE OF "s_oxygen_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_oxygen_check"();


--该触发器用于：当s_nitrogen_check有更新时触发coalchp_furnace_calculation.s_nitrogen_check=coalchp_needs_questionnaire.s_nitrogen_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_13" AFTER UPDATE OF "s_nitrogen_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_nitrogen_check"();


--该触发器用于：当s_sulfur_check有更新时触发coalchp_furnace_calculation.s_sulfur_check=coalchp_needs_questionnaire.s_sulfur_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_14" AFTER UPDATE OF "s_sulfur_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_sulfur_check"();


--该触发器用于：当s_water_check有更新时触发coalchp_furnace_calculation.s_water_check=coalchp_needs_questionnaire.s_water_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_15" AFTER UPDATE OF "s_water_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_water_check"();


--该触发器用于：当s_grey_check有更新时触发coalchp_furnace_calculation.s_grey_check=coalchp_needs_questionnaire.s_grey_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_16" AFTER UPDATE OF "s_grey_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_grey_check"();


--该触发器用于：当s_daf_check有更新时触发coalchp_furnace_calculation.s_daf_check=coalchp_needs_questionnaire.s_daf_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_17" AFTER UPDATE OF "s_daf_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_daf_check"();


--该触发器用于：当s_grindability_check有更新时触发coalchp_furnace_calculation.s_grindability_check=coalchp_needs_questionnaire.s_grindability_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_18" AFTER UPDATE OF "s_grindability_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_grindability_check"();


--该触发器用于：当s_low_check有更新时触发coalchp_furnace_calculation.s_low_check=coalchp_needs_questionnaire.s_low_check
CREATE TRIGGER "coalchp_needs_questionnaire_a_19" AFTER UPDATE OF "s_low_check" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_s_low_check"();


--该触发器用于：当w_annual_average_relative_humidity_value有更新时触发coalchp_furnace_calculation.a_humidity_design=coalchp_needs_questionnaire.w_annual_average_relative_humidity_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_20" AFTER UPDATE OF "w_annual_average_relative_humidity_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_a_humidity_design"();


--该触发器用于：当w_mean_annual_barometric_value有更新时触发coalchp_furnace_calculation.a_pressure_design=coalchp_needs_questionnaire.w_mean_annual_barometric_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_21" AFTER UPDATE OF "w_mean_annual_barometric_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_a_pressure_design"();


--该触发器用于：当w_mean_annual_temperature_value有更新时触发coalchp_furnace_calculation.a_temperature_design=coalchp_needs_questionnaire.w_mean_annual_temperature_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_22" AFTER UPDATE OF "w_mean_annual_temperature_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_a_temperature_design"();


--该触发器用于：当w_mean_annual_temperature_value有更新时触发coalchp_furnace_calculation.a_temperature_check=coalchp_needs_questionnaire.w_mean_annual_temperature_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_23" AFTER UPDATE OF "w_mean_annual_temperature_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_a_temperature_check"();


--该触发器用于：当w_mean_annual_barometric_value有更新时触发coalchp_furnace_calculation.a_pressure_check=coalchp_needs_questionnaire.w_mean_annual_barometric_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_24" AFTER UPDATE OF "w_mean_annual_barometric_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_a_pressure_check"();


--该触发器用于：当w_annual_average_relative_humidity_value有更新时触发coalchp_furnace_calculation.a_humidity_check=coalchp_needs_questionnaire.w_annual_average_relative_humidity_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_25" AFTER UPDATE OF "w_annual_average_relative_humidity_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_a_humidity_check"();


--该触发器用于：当w_mean_summer_temperature_value有更新时触发coalchp_furnace_calculation.a_hot_temperature_check=coalchp_needs_questionnaire.w_mean_summer_temperature_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_26" AFTER UPDATE OF "w_mean_summer_temperature_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_a_hot_temperature_check"();


--该触发器用于：当w_mean_summer_temperature_value有更新时触发coalchp_furnace_calculation.a_hot_temperature_design=coalchp_needs_questionnaire.w_mean_summer_temperature_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_27" AFTER UPDATE OF "w_mean_summer_temperature_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_a_hot_temperature_design"();


--该触发器用于：当op_flue_gas_nox_limits_value有更新时触发coalchp_desulfurization_denitrification.n_env_after_nox_concentration=coalchp_needs_questionnaire.op_flue_gas_nox_limits_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_28" AFTER UPDATE OF "op_flue_gas_nox_limits_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification_n_env_after_nox_concent"();


----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_furnace_calculation的b_boiler_rated_coal_capacity_design字段，和表coalchp_coal_handingsystem的f_boiler_consumption_design字段，即：coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_design=coalchp_furnace_calculation.f_boiler_consumption_design
CREATE OR REPLACE FUNCTION coalchp_coal_handingsystem_b_boiler_rated_coal_capacity_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_coal_handingsystem set b_boiler_rated_coal_capacity_design=coalchp_furnace_calculation.f_boiler_consumption_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_coal_handingsystem.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的b_boiler_rated_coal_capacity_check字段，和表coalchp_coal_handingsystem的f_boiler_consumption_check字段，即：coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_check=coalchp_furnace_calculation.f_boiler_consumption_check
CREATE OR REPLACE FUNCTION coalchp_coal_handingsystem_b_boiler_rated_coal_capacity_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_coal_handingsystem set b_boiler_rated_coal_capacity_check=coalchp_furnace_calculation.f_boiler_consumption_check
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_coal_handingsystem.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_furnace_calculation的a_total_ash_residue_after字段，和表coalchp_removal_ash_slag_system的d_total_design字段，即：coalchp_removal_ash_slag_system.a_total_ash_residue_after=coalchp_furnace_calculation.d_total_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_a_total_ash_residue_after()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set a_total_ash_residue_after=coalchp_furnace_calculation.d_total_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的a_the_imported_smoke_volume字段，和表coalchp_removal_ash_slag_system的d_standard_smoke_flow_design字段，即：coalchp_removal_ash_slag_system.a_the_imported_smoke_volume=coalchp_furnace_calculation.d_standard_smoke_flow_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_a_the_imported_smoke_volume()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set a_the_imported_smoke_volume=coalchp_furnace_calculation.d_standard_smoke_flow_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的a_the_smoke_volume_flow字段，和表coalchp_removal_ash_slag_system的d_entry_smoke_actual_flow_design字段，即：coalchp_removal_ash_slag_system.a_the_smoke_volume_flow=coalchp_furnace_calculation.d_entry_smoke_actual_flow_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_a_the_smoke_volume_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set a_the_smoke_volume_flow=coalchp_furnace_calculation.d_entry_smoke_actual_flow_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的a_the_imported_smoke_real_state字段，和表coalchp_removal_ash_slag_system的i_smoke_actual_flow1_design字段，即：coalchp_removal_ash_slag_system.a_the_imported_smoke_real_state=coalchp_furnace_calculation.i_smoke_actual_flow1_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_a_the_imported_smoke_real_state()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set a_the_imported_smoke_real_state=coalchp_furnace_calculation.i_smoke_actual_flow1_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的s_slag_amount字段，和表coalchp_removal_ash_slag_system的d_dust_total_design字段，即：coalchp_removal_ash_slag_system.s_slag_amount=coalchp_furnace_calculation.d_dust_total_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_s_slag_amount()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set s_slag_amount=coalchp_furnace_calculation.d_dust_total_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当d_total_design有更新时触发coalchp_removal_ash_slag_system.a_total_ash_residue_after=coalchp_furnace_calculation.d_total_design
CREATE TRIGGER "coalchp_furnace_calculation_a_0" AFTER UPDATE OF "d_total_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_a_total_ash_residue_after"();


--该触发器用于：当d_standard_smoke_flow_design有更新时触发coalchp_removal_ash_slag_system.a_the_imported_smoke_volume=coalchp_furnace_calculation.d_standard_smoke_flow_design
CREATE TRIGGER "coalchp_furnace_calculation_a_1" AFTER UPDATE OF "d_standard_smoke_flow_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_a_the_imported_smoke_volume"();


--该触发器用于：当d_entry_smoke_actual_flow_design有更新时触发coalchp_removal_ash_slag_system.a_the_smoke_volume_flow=coalchp_furnace_calculation.d_entry_smoke_actual_flow_design
CREATE TRIGGER "coalchp_furnace_calculation_a_2" AFTER UPDATE OF "d_entry_smoke_actual_flow_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_a_the_smoke_volume_flow"();


--该触发器用于：当i_smoke_actual_flow1_design有更新时触发coalchp_removal_ash_slag_system.a_the_imported_smoke_real_state=coalchp_furnace_calculation.i_smoke_actual_flow1_design
CREATE TRIGGER "coalchp_furnace_calculation_a_3" AFTER UPDATE OF "i_smoke_actual_flow1_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_a_the_imported_smoke_real_state"();


--该触发器用于：当d_dust_total_design有更新时触发coalchp_removal_ash_slag_system.s_slag_amount=coalchp_furnace_calculation.d_dust_total_design
CREATE TRIGGER "coalchp_furnace_calculation_a_4" AFTER UPDATE OF "d_dust_total_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_s_slag_amount"();

----------------------创建触发器-----------------------------------

--该触发器用于：当f_boiler_consumption_design有更新时触发coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_design=coalchp_furnace_calculation.f_boiler_consumption_design
CREATE TRIGGER "coalchp_furnace_calculation_a_5" AFTER UPDATE OF "f_boiler_consumption_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_coal_handingsystem_b_boiler_rated_coal_capacity_design"();


--该触发器用于：当f_boiler_consumption_check有更新时触发coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_check=coalchp_furnace_calculation.f_boiler_consumption_check
CREATE TRIGGER "coalchp_furnace_calculation_a_6" AFTER UPDATE OF "f_boiler_consumption_check" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_coal_handingsystem_b_boiler_rated_coal_capacity_check"();


--该触发器用于：当s_sulfur_design有更新时触发coalchp_desulfurization_denitrification.s_sulfur_design=coalchp_furnace_calculation.s_sulfur_design
CREATE TRIGGER "coalchp_furnace_calculation_a_7" AFTER UPDATE OF "s_sulfur_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification_s_sulfur_design"();


--该触发器用于：当f_calculation_consumption_design有更新时触发coalchp_desulfurization_denitrification.s_calcu_coal_consume=coalchp_furnace_calculation.f_calculation_consumption_design
CREATE TRIGGER "coalchp_furnace_calculation_a_8" AFTER UPDATE OF "f_calculation_consumption_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification_s_calcu_coal_consume"();


--该触发器用于：当i_standard_smoke_flow1_design有更新时触发coalchp_desulfurization_denitrification.s_fan_smoke_flow=coalchp_furnace_calculation.i_standard_smoke_flow1_design
CREATE TRIGGER "coalchp_furnace_calculation_a_9" AFTER UPDATE OF "i_standard_smoke_flow1_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification_s_fan_smoke_flow"();


----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_furnace_calculation的p_standard_of_flow_f字段，和表coalchp_smoke_air_system的a_first_cwind_standard_design字段，即：coalchp_smoke_air_system.p_standard_of_flow_f=coalchp_furnace_calculation.a_first_cwind_standard_design
CREATE OR REPLACE FUNCTION coalchp_smoke_air_system_p_standard_of_flow_f()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_smoke_air_system set p_standard_of_flow_f=coalchp_furnace_calculation.a_first_cwind_standard_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_smoke_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的p_standard_of_flow_s字段，和表coalchp_smoke_air_system的a_second_cwind_standard_design字段，即：coalchp_smoke_air_system.p_standard_of_flow_s=coalchp_furnace_calculation.a_second_cwind_standard_design
CREATE OR REPLACE FUNCTION coalchp_smoke_air_system_p_standard_of_flow_s()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_smoke_air_system set p_standard_of_flow_s=coalchp_furnace_calculation.a_second_cwind_standard_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_smoke_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的p_standard_of_flow_t字段，和表coalchp_smoke_air_system的i_standard_smoke_flow1_design字段，即：coalchp_smoke_air_system.p_standard_of_flow_t=coalchp_furnace_calculation.i_standard_smoke_flow1_design
CREATE OR REPLACE FUNCTION coalchp_smoke_air_system_p_standard_of_flow_t()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_smoke_air_system set p_standard_of_flow_t=coalchp_furnace_calculation.i_standard_smoke_flow1_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_smoke_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当a_first_cwind_standard_design有更新时触发coalchp_smoke_air_system.p_standard_of_flow_f=coalchp_furnace_calculation.a_first_cwind_standard_design
CREATE TRIGGER "coalchp_furnace_calculation_a_10" AFTER UPDATE OF "a_first_cwind_standard_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_smoke_air_system_p_standard_of_flow_f"();


--该触发器用于：当a_second_cwind_standard_design有更新时触发coalchp_smoke_air_system.p_standard_of_flow_s=coalchp_furnace_calculation.a_second_cwind_standard_design
CREATE TRIGGER "coalchp_furnace_calculation_a_11" AFTER UPDATE OF "a_second_cwind_standard_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_smoke_air_system_p_standard_of_flow_s"();


--该触发器用于：当i_standard_smoke_flow1_design有更新时触发coalchp_smoke_air_system.p_standard_of_flow_t=coalchp_furnace_calculation.i_standard_smoke_flow1_design
CREATE TRIGGER "coalchp_furnace_calculation_a_12" AFTER UPDATE OF "i_standard_smoke_flow1_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_smoke_air_system_p_standard_of_flow_t"();

----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_needs_questionnaire的a_altitude字段，和表coalchp_smoke_air_system的w_altitude_value字段，即：coalchp_smoke_air_system.a_altitude=coalchp_needs_questionnaire.w_altitude_value
CREATE OR REPLACE FUNCTION coalchp_smoke_air_system_a_altitude()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_smoke_air_system set a_altitude=coalchp_needs_questionnaire.w_altitude_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_smoke_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_needs_questionnaire的p_local_atmosphere_f字段，和表coalchp_smoke_air_system的w_mean_annual_barometric_value字段，即：coalchp_smoke_air_system.p_local_atmosphere_f=coalchp_needs_questionnaire.w_mean_annual_barometric_value
CREATE OR REPLACE FUNCTION coalchp_smoke_air_system_p_local_atmosphere_f()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_smoke_air_system set p_local_atmosphere_f=coalchp_needs_questionnaire.w_mean_annual_barometric_value*1000
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_smoke_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当w_altitude_value有更新时触发coalchp_smoke_air_system.a_altitude=coalchp_needs_questionnaire.w_altitude_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_29" AFTER UPDATE OF "w_altitude_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_smoke_air_system_a_altitude"();


--该触发器用于：当w_mean_annual_barometric_value有更新时触发coalchp_smoke_air_system.p_local_atmosphere_f=coalchp_needs_questionnaire.w_mean_annual_barometric_value
CREATE TRIGGER "coalchp_needs_questionnaire_a_30" AFTER UPDATE OF "w_mean_annual_barometric_value" ON "public"."coalchp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_smoke_air_system_p_local_atmosphere_f"();

