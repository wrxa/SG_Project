----------------------创建触发函数-----------------------------------
--用于同步表：ccpp_questionnaire的engine_demand_power_design字段，和表ccpp_ccpp的electric_load_demand字段，即：ccpp_ccpp.engine_demand_power_design=ccpp_questionnaire.electric_load_demand
CREATE OR REPLACE FUNCTION ccpp_ccpp_engine_demand_power_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_ccpp set engine_demand_power_design=ccpp_questionnaire.electric_load_demand
  from ccpp_questionnaire where ccpp_questionnaire.plan_id=ccpp_ccpp.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：ccpp_questionnaire的high_steam_pressure_design字段，和表ccpp_ccpp的steam_pressure_level_1字段，即：ccpp_ccpp.high_steam_pressure_design=ccpp_questionnaire.steam_pressure_level_1
CREATE OR REPLACE FUNCTION ccpp_ccpp_high_steam_pressure_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_ccpp set high_steam_pressure_design=ccpp_questionnaire.steam_pressure_level_1
  from ccpp_questionnaire where ccpp_questionnaire.plan_id=ccpp_ccpp.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：ccpp_questionnaire的sp_steam_pressure_design字段，和表ccpp_ccpp的steam_pressure_level_1字段，即：ccpp_ccpp.sp_steam_pressure_design=ccpp_questionnaire.steam_pressure_level_1
CREATE OR REPLACE FUNCTION ccpp_ccpp_sp_steam_pressure_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_ccpp set sp_steam_pressure_design=ccpp_questionnaire.steam_pressure_level_1
  from ccpp_questionnaire where ccpp_questionnaire.plan_id=ccpp_ccpp.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：ccpp_questionnaire的sp_steam_temperature_design字段，和表ccpp_ccpp的steam_temperature_level_1字段，即：ccpp_ccpp.sp_steam_temperature_design=ccpp_questionnaire.steam_temperature_level_1
CREATE OR REPLACE FUNCTION ccpp_ccpp_sp_steam_temperature_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_ccpp set sp_steam_temperature_design=ccpp_questionnaire.steam_temperature_level_1
  from ccpp_questionnaire where ccpp_questionnaire.plan_id=ccpp_ccpp.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：ccpp_questionnaire的low_calorific_gas_design字段，和表ccpp_ccpp的low_calorific_gas_design字段，即：ccpp_ccpp.low_calorific_gas_design=ccpp_questionnaire.low_calorific_gas_design
CREATE OR REPLACE FUNCTION ccpp_ccpp_low_calorific_gas_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_ccpp set low_calorific_gas_design=ccpp_questionnaire.low_calorific_gas_design
  from ccpp_questionnaire where ccpp_questionnaire.plan_id=ccpp_ccpp.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当electric_load_demand有更新时触发ccpp_ccpp.engine_demand_power_design=ccpp_questionnaire.electric_load_demand
CREATE TRIGGER "ccpp_questionnaire_a_0" AFTER UPDATE OF "electric_load_demand" ON "public"."ccpp_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_ccpp_engine_demand_power_design"();


--该触发器用于：当steam_pressure_level_1有更新时触发ccpp_ccpp.high_steam_pressure_design=ccpp_questionnaire.steam_pressure_level_1
CREATE TRIGGER "ccpp_questionnaire_a_1" AFTER UPDATE OF "steam_pressure_level_1" ON "public"."ccpp_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_ccpp_high_steam_pressure_design"();


--该触发器用于：当steam_pressure_level_1有更新时触发ccpp_ccpp.sp_steam_pressure_design=ccpp_questionnaire.steam_pressure_level_1
CREATE TRIGGER "ccpp_questionnaire_a_2" AFTER UPDATE OF "steam_pressure_level_1" ON "public"."ccpp_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_ccpp_sp_steam_pressure_design"();


--该触发器用于：当steam_temperature_level_1有更新时触发ccpp_ccpp.sp_steam_temperature_design=ccpp_questionnaire.steam_temperature_level_1
CREATE TRIGGER "ccpp_questionnaire_a_3" AFTER UPDATE OF "steam_temperature_level_1" ON "public"."ccpp_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_ccpp_sp_steam_temperature_design"();


--该触发器用于：当low_calorific_gas_design有更新时触发ccpp_ccpp.low_calorific_gas_design=ccpp_questionnaire.low_calorific_gas_design
CREATE TRIGGER "ccpp_questionnaire_a_4" AFTER UPDATE OF "low_calorific_gas_design" ON "public"."ccpp_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_ccpp_low_calorific_gas_design"();


