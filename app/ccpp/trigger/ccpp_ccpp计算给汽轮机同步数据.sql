----------------------创建触发函数-----------------------------------
--用于同步表：ccpp_ccpp的e_steam_temperature字段，和表ccpp_turbine的high_steam_temperature_design字段，即：ccpp_turbine.e_steam_temperature=ccpp_ccpp.high_steam_temperature_design
CREATE OR REPLACE FUNCTION ccpp_turbine_e_steam_temperature()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_turbine set e_steam_temperature=ccpp_ccpp.high_steam_temperature_design
  from ccpp_ccpp where ccpp_ccpp.plan_id=ccpp_turbine.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：ccpp_ccpp的e_steam_pressure字段，和表ccpp_turbine的high_steam_pressure_design字段，即：ccpp_turbine.e_steam_pressure=ccpp_ccpp.high_steam_pressure_design
CREATE OR REPLACE FUNCTION ccpp_turbine_e_steam_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_turbine set e_steam_pressure=ccpp_ccpp.high_steam_pressure_design
  from ccpp_ccpp where ccpp_ccpp.plan_id=ccpp_turbine.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：ccpp_ccpp的e_steam_flow字段，和表ccpp_turbine的high_gas_production_design字段，即：ccpp_turbine.e_steam_flow=ccpp_ccpp.high_gas_production_design
CREATE OR REPLACE FUNCTION ccpp_turbine_e_steam_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_turbine set e_steam_flow=ccpp_ccpp.high_gas_production_design
  from ccpp_ccpp where ccpp_ccpp.plan_id=ccpp_turbine.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当high_steam_temperature_design有更新时触发ccpp_turbine.e_steam_temperature=ccpp_ccpp.high_steam_temperature_design
CREATE TRIGGER "ccpp_ccpp_a_100" AFTER UPDATE OF "high_steam_temperature_design" ON "public"."ccpp_ccpp"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_turbine_e_steam_temperature"();


--该触发器用于：当high_steam_pressure_design有更新时触发ccpp_turbine.e_steam_pressure=ccpp_ccpp.high_steam_pressure_design
CREATE TRIGGER "ccpp_ccpp_a_101" AFTER UPDATE OF "high_steam_pressure_design" ON "public"."ccpp_ccpp"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_turbine_e_steam_pressure"();


--该触发器用于：当high_gas_production_design有更新时触发ccpp_turbine.e_steam_flow=ccpp_ccpp.high_gas_production_design
CREATE TRIGGER "ccpp_ccpp_a_102" AFTER UPDATE OF "high_gas_production_design" ON "public"."ccpp_ccpp"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_turbine_e_steam_flow"();


