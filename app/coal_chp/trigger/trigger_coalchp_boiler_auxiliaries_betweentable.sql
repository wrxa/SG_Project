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


