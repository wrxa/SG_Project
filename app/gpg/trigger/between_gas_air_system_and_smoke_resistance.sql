----------------------创建触发函数-----------------------------------
--用于同步表：gaspowergeneration_gas_air_system的air_preheater_outlet_smoke_amount字段，和表gaspowergeneration_smoke_resistance的s2c_condition_flux_smoke字段，即：gaspowergeneration_smoke_resistance.air_preheater_outlet_smoke_amount=gaspowergeneration_gas_air_system.s2c_condition_flux_smoke
CREATE OR REPLACE FUNCTION gaspowergeneration_smoke_resistance_air_preheater_outlet_smoke_amount()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_smoke_resistance set air_preheater_outlet_smoke_amount=gaspowergeneration_gas_air_system.s2c_condition_flux_smoke
  from gaspowergeneration_gas_air_system where gaspowergeneration_gas_air_system.plan_id=gaspowergeneration_smoke_resistance.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当s2c_condition_flux_smoke有更新时触发gaspowergeneration_smoke_resistance.air_preheater_outlet_smoke_amount=gaspowergeneration_gas_air_system.s2c_condition_flux_smoke
CREATE TRIGGER "gaspowergeneration_gas_air_system_A_0" AFTER UPDATE OF "s2c_condition_flux_smoke" ON "public"."gaspowergeneration_gas_air_system"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_smoke_resistance_air_preheater_outlet_smoke_amount"();


