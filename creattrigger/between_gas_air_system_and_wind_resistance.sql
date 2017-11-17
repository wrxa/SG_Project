----------------------创建触发函数-----------------------------------
--用于同步表：gaspowergeneration_gas_air_system的intake_to_preheater_amount字段，和表gaspowergeneration_wind_resistance的s2c_condition_flux_air字段，即：gaspowergeneration_wind_resistance.intake_to_preheater_amount=gaspowergeneration_gas_air_system.s2c_condition_flux_air
CREATE OR REPLACE FUNCTION gaspowergeneration_wind_resistance_intake_to_preheater_amount()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_wind_resistance set intake_to_preheater_amount=gaspowergeneration_gas_air_system.s2c_condition_flux_air
  from gaspowergeneration_gas_air_system where gaspowergeneration_gas_air_system.plan_id=gaspowergeneration_wind_resistance.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当s2c_condition_flux_air有更新时触发gaspowergeneration_wind_resistance.intake_to_preheater_amount=gaspowergeneration_gas_air_system.s2c_condition_flux_air
CREATE TRIGGER "gaspowergeneration_gas_air_system_B_0" AFTER UPDATE OF "s2c_condition_flux_air" ON "public"."gaspowergeneration_gas_air_system"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_wind_resistance_intake_to_preheater_amount"();


