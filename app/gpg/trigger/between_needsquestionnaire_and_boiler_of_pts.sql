----------------------创建触发函数-----------------------------------
--用于同步表：gaspowergeneration_needsquestionnaire的surplus_gas_bfg字段，和表gaspowergeneration_boiler_of_pts的surplus_gas_bfg字段，即：gaspowergeneration_boiler_of_pts.surplus_gas_bfg=gaspowergeneration_needsquestionnaire.surplus_gas_bfg
CREATE OR REPLACE FUNCTION gaspowergeneration_boiler_of_pts_surplus_gas_bfg()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_boiler_of_pts set surplus_gas_bfg=gaspowergeneration_needsquestionnaire.surplus_gas_bfg
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_boiler_of_pts.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的surplus_gas_ldg字段，和表gaspowergeneration_boiler_of_pts的surplus_gas_ldg字段，即：gaspowergeneration_boiler_of_pts.surplus_gas_ldg=gaspowergeneration_needsquestionnaire.surplus_gas_ldg
CREATE OR REPLACE FUNCTION gaspowergeneration_boiler_of_pts_surplus_gas_ldg()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_boiler_of_pts set surplus_gas_ldg=gaspowergeneration_needsquestionnaire.surplus_gas_ldg
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_boiler_of_pts.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的surplus_gas_cog字段，和表gaspowergeneration_boiler_of_pts的surplus_gas_cog字段，即：gaspowergeneration_boiler_of_pts.surplus_gas_cog=gaspowergeneration_needsquestionnaire.surplus_gas_cog
CREATE OR REPLACE FUNCTION gaspowergeneration_boiler_of_pts_surplus_gas_cog()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_boiler_of_pts set surplus_gas_cog=gaspowergeneration_needsquestionnaire.surplus_gas_cog
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_boiler_of_pts.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的bfg_gas_calorific_value字段，和表gaspowergeneration_boiler_of_pts的bfg_gas_calorific_value字段，即：gaspowergeneration_boiler_of_pts.bfg_gas_calorific_value=gaspowergeneration_needsquestionnaire.bfg_gas_calorific_value
CREATE OR REPLACE FUNCTION gaspowergeneration_boiler_of_pts_bfg_gas_calorific_value()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_boiler_of_pts set bfg_gas_calorific_value=gaspowergeneration_needsquestionnaire.bfg_gas_calorific_value
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_boiler_of_pts.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的ldg_gas_calorific_value字段，和表gaspowergeneration_boiler_of_pts的ldg_gas_calorific_value字段，即：gaspowergeneration_boiler_of_pts.ldg_gas_calorific_value=gaspowergeneration_needsquestionnaire.ldg_gas_calorific_value
CREATE OR REPLACE FUNCTION gaspowergeneration_boiler_of_pts_ldg_gas_calorific_value()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_boiler_of_pts set ldg_gas_calorific_value=gaspowergeneration_needsquestionnaire.ldg_gas_calorific_value
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_boiler_of_pts.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的cog_gas_calorific_value字段，和表gaspowergeneration_boiler_of_pts的cog_gas_calorific_value字段，即：gaspowergeneration_boiler_of_pts.cog_gas_calorific_value=gaspowergeneration_needsquestionnaire.cog_gas_calorific_value
CREATE OR REPLACE FUNCTION gaspowergeneration_boiler_of_pts_cog_gas_calorific_value()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_boiler_of_pts set cog_gas_calorific_value=gaspowergeneration_needsquestionnaire.cog_gas_calorific_value
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_boiler_of_pts.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当surplus_gas_bfg有更新时触发gaspowergeneration_boiler_of_pts.surplus_gas_bfg=gaspowergeneration_needsquestionnaire.surplus_gas_bfg
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_a_0" AFTER UPDATE OF "surplus_gas_bfg" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_boiler_of_pts_surplus_gas_bfg"();


--该触发器用于：当surplus_gas_ldg有更新时触发gaspowergeneration_boiler_of_pts.surplus_gas_ldg=gaspowergeneration_needsquestionnaire.surplus_gas_ldg
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_a_1" AFTER UPDATE OF "surplus_gas_ldg" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_boiler_of_pts_surplus_gas_ldg"();


--该触发器用于：当surplus_gas_cog有更新时触发gaspowergeneration_boiler_of_pts.surplus_gas_cog=gaspowergeneration_needsquestionnaire.surplus_gas_cog
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_a_2" AFTER UPDATE OF "surplus_gas_cog" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_boiler_of_pts_surplus_gas_cog"();


--该触发器用于：当bfg_gas_calorific_value有更新时触发gaspowergeneration_boiler_of_pts.bfg_gas_calorific_value=gaspowergeneration_needsquestionnaire.bfg_gas_calorific_value
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_a_3" AFTER UPDATE OF "bfg_gas_calorific_value" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_boiler_of_pts_bfg_gas_calorific_value"();


--该触发器用于：当ldg_gas_calorific_value有更新时触发gaspowergeneration_boiler_of_pts.ldg_gas_calorific_value=gaspowergeneration_needsquestionnaire.ldg_gas_calorific_value
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_a_4" AFTER UPDATE OF "ldg_gas_calorific_value" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_boiler_of_pts_ldg_gas_calorific_value"();


--该触发器用于：当cog_gas_calorific_value有更新时触发gaspowergeneration_boiler_of_pts.cog_gas_calorific_value=gaspowergeneration_needsquestionnaire.cog_gas_calorific_value
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_a_5" AFTER UPDATE OF "cog_gas_calorific_value" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_boiler_of_pts_cog_gas_calorific_value"();


