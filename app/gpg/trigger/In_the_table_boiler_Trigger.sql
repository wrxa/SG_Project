CREATE OR REPLACE FUNCTION gaspowergeneration_boiler_of_pts()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段air_need_for_combustion:燃烧所需空气量,的计算1-----------------------------------
  IF OLD.excess_air_coefficient != NEW.excess_air_coefficient OR OLD.surplus_gas_bfg != NEW.surplus_gas_bfg OR OLD.bfg_gas_calorific_value != NEW.bfg_gas_calorific_value THEN
     update gaspowergeneration_boiler_of_pts set 

     air_need_for_combustion=0.209*NEW.bfg_gas_calorific_value*NEW.surplus_gas_bfg*NEW.excess_air_coefficient/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.excess_air_coefficient ISNULL OR OLD.bfg_gas_calorific_value ISNULL OR OLD.surplus_gas_bfg ISNULL) AND NEW.excess_air_coefficient NOTNULL AND NEW.bfg_gas_calorific_value NOTNULL AND NEW.surplus_gas_bfg NOTNULL THEN
     update gaspowergeneration_boiler_of_pts set 

     air_need_for_combustion=0.209*NEW.bfg_gas_calorific_value*NEW.surplus_gas_bfg*NEW.excess_air_coefficient/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段steam_output:产汽量,的计算2-----------------------------------
  IF OLD.superheated_steam_enthalpy != NEW.superheated_steam_enthalpy OR OLD.excess_air_coefficient != NEW.excess_air_coefficient OR OLD.air_enthalpy != NEW.air_enthalpy OR OLD.feedwater_enthalpy != NEW.feedwater_enthalpy OR OLD.rate_of_blowdown != NEW.rate_of_blowdown OR OLD.saturation_water_enthalpy != NEW.saturation_water_enthalpy OR OLD.surplus_gas_bfg != NEW.surplus_gas_bfg OR OLD.surplus_gas_cog != NEW.surplus_gas_cog OR OLD.bfg_gas_calorific_value != NEW.bfg_gas_calorific_value OR OLD.cog_gas_calorific_value != NEW.cog_gas_calorific_value OR OLD.boiler_efficiency != NEW.boiler_efficiency THEN
     update gaspowergeneration_boiler_of_pts set 

     steam_output=((0.209*NEW.bfg_gas_calorific_value*NEW.surplus_gas_bfg*NEW.excess_air_coefficient/1000)*NEW.air_enthalpy+NEW.surplus_gas_bfg*NEW.bfg_gas_calorific_value+NEW.surplus_gas_cog*NEW.cog_gas_calorific_value)*NEW.boiler_efficiency/(1000*((NEW.superheated_steam_enthalpy-NEW.feedwater_enthalpy)+NEW.rate_of_blowdown*(NEW.saturation_water_enthalpy-NEW.feedwater_enthalpy)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.saturation_water_enthalpy ISNULL OR OLD.rate_of_blowdown ISNULL OR OLD.feedwater_enthalpy ISNULL OR OLD.air_enthalpy ISNULL OR OLD.excess_air_coefficient ISNULL OR OLD.superheated_steam_enthalpy ISNULL OR OLD.boiler_efficiency ISNULL OR OLD.cog_gas_calorific_value ISNULL OR OLD.bfg_gas_calorific_value ISNULL OR OLD.surplus_gas_cog ISNULL OR OLD.surplus_gas_bfg ISNULL) AND NEW.saturation_water_enthalpy NOTNULL AND NEW.rate_of_blowdown NOTNULL AND NEW.feedwater_enthalpy NOTNULL AND NEW.air_enthalpy NOTNULL AND NEW.excess_air_coefficient NOTNULL AND NEW.superheated_steam_enthalpy NOTNULL AND NEW.boiler_efficiency NOTNULL AND NEW.cog_gas_calorific_value NOTNULL AND NEW.bfg_gas_calorific_value NOTNULL AND NEW.surplus_gas_cog NOTNULL AND NEW.surplus_gas_bfg NOTNULL THEN
     update gaspowergeneration_boiler_of_pts set 

     steam_output=((0.209*NEW.bfg_gas_calorific_value*NEW.surplus_gas_bfg*NEW.excess_air_coefficient/1000)*NEW.air_enthalpy+NEW.surplus_gas_bfg*NEW.bfg_gas_calorific_value+NEW.surplus_gas_cog*NEW.cog_gas_calorific_value)*NEW.boiler_efficiency/(1000*((NEW.superheated_steam_enthalpy-NEW.feedwater_enthalpy)+NEW.rate_of_blowdown*(NEW.saturation_water_enthalpy-NEW.feedwater_enthalpy)))
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_boiler_of_pts" AFTER UPDATE OF
"superheated_steam_enthalpy",
"excess_air_coefficient",
"air_enthalpy",
"feedwater_enthalpy",
"rate_of_blowdown",
"saturation_water_enthalpy",
"surplus_gas_bfg",
"surplus_gas_cog",
"bfg_gas_calorific_value",
"cog_gas_calorific_value",
"boiler_efficiency"
ON "public"."gaspowergeneration_boiler_of_pts"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_boiler_of_pts"();

