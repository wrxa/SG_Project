CREATE OR REPLACE FUNCTION ccpp_questionnaire_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段total:总计,的计算1-----------------------------------
  IF OLD.methane_design != NEW.methane_design OR OLD.carbon6_design != NEW.carbon6_design OR OLD.hydrogen_design != NEW.hydrogen_design OR OLD.helium_design != NEW.helium_design OR OLD.nitrogen_design != NEW.nitrogen_design OR OLD.carbon_monoxide_design != NEW.carbon_monoxide_design OR OLD.carbon_dioxide_design != NEW.carbon_dioxide_design OR OLD.hydrogen_sulfide_design != NEW.hydrogen_sulfide_design OR OLD.oxygen_design != NEW.oxygen_design OR OLD.water_design != NEW.water_design OR OLD.ethane_design != NEW.ethane_design OR OLD.ethylene_design != NEW.ethylene_design OR OLD.propylene_design != NEW.propylene_design OR OLD.propane_design != NEW.propane_design OR OLD.butene_design != NEW.butene_design OR OLD.i_isobutane_design != NEW.i_isobutane_design OR OLD.n_isobutane_design != NEW.n_isobutane_design OR OLD.pentane_design != NEW.pentane_design THEN
     update ccpp_questionnaire set 

     total_design=(NEW.methane_design)+(NEW.ethane_design)+(NEW.ethylene_design)+(NEW.propylene_design)+(NEW.propane_design)+(NEW.butene_design)+(NEW.i_isobutane_design)+(NEW.n_isobutane_design)+(NEW.pentane_design)+(NEW.carbon6_design)+(NEW.hydrogen_design)+(NEW.helium_design)+(NEW.nitrogen_design)+(NEW.carbon_monoxide_design)+(NEW.carbon_dioxide_design)+(NEW.hydrogen_sulfide_design)+(NEW.oxygen_design)+(NEW.water_design)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.water_design ISNULL OR OLD.oxygen_design ISNULL OR OLD.hydrogen_sulfide_design ISNULL OR OLD.carbon_dioxide_design ISNULL OR OLD.carbon_monoxide_design ISNULL OR OLD.nitrogen_design ISNULL OR OLD.helium_design ISNULL OR OLD.hydrogen_design ISNULL OR OLD.carbon6_design ISNULL OR OLD.pentane_design ISNULL OR OLD.n_isobutane_design ISNULL OR OLD.i_isobutane_design ISNULL OR OLD.butene_design ISNULL OR OLD.propane_design ISNULL OR OLD.propylene_design ISNULL OR OLD.ethylene_design ISNULL OR OLD.ethane_design ISNULL OR OLD.methane_design ISNULL) AND NEW.water_design NOTNULL AND NEW.oxygen_design NOTNULL AND NEW.hydrogen_sulfide_design NOTNULL AND NEW.carbon_dioxide_design NOTNULL AND NEW.carbon_monoxide_design NOTNULL AND NEW.nitrogen_design NOTNULL AND NEW.helium_design NOTNULL AND NEW.hydrogen_design NOTNULL AND NEW.carbon6_design NOTNULL AND NEW.pentane_design NOTNULL AND NEW.n_isobutane_design NOTNULL AND NEW.i_isobutane_design NOTNULL AND NEW.butene_design NOTNULL AND NEW.propane_design NOTNULL AND NEW.propylene_design NOTNULL AND NEW.ethylene_design NOTNULL AND NEW.ethane_design NOTNULL AND NEW.methane_design NOTNULL THEN
     update ccpp_questionnaire set 

     total_design=(NEW.methane_design)+(NEW.ethane_design)+(NEW.ethylene_design)+(NEW.propylene_design)+(NEW.propane_design)+(NEW.butene_design)+(NEW.i_isobutane_design)+(NEW.n_isobutane_design)+(NEW.pentane_design)+(NEW.carbon6_design)+(NEW.hydrogen_design)+(NEW.helium_design)+(NEW.nitrogen_design)+(NEW.carbon_monoxide_design)+(NEW.carbon_dioxide_design)+(NEW.hydrogen_sulfide_design)+(NEW.oxygen_design)+(NEW.water_design)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "ccpp_questionnaire_design" AFTER UPDATE OF
"methane_design",
"carbon6_design",
"hydrogen_design",
"helium_design",
"nitrogen_design",
"carbon_monoxide_design",
"carbon_dioxide_design",
"hydrogen_sulfide_design",
"oxygen_design",
"water_design",
"ethane_design",
"ethylene_design",
"propylene_design",
"propane_design",
"butene_design",
"i_isobutane_design",
"n_isobutane_design",
"pentane_design"
ON "public"."ccpp_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_questionnaire_design"();

CREATE OR REPLACE FUNCTION ccpp_questionnaire_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段total:总计,的计算1-----------------------------------
  IF OLD.methane_check != NEW.methane_check OR OLD.carbon6_check != NEW.carbon6_check OR OLD.hydrogen_check != NEW.hydrogen_check OR OLD.helium_check != NEW.helium_check OR OLD.nitrogen_check != NEW.nitrogen_check OR OLD.carbon_monoxide_check != NEW.carbon_monoxide_check OR OLD.carbon_dioxide_check != NEW.carbon_dioxide_check OR OLD.hydrogen_sulfide_check != NEW.hydrogen_sulfide_check OR OLD.oxygen_check != NEW.oxygen_check OR OLD.water_check != NEW.water_check OR OLD.ethane_check != NEW.ethane_check OR OLD.ethylene_check != NEW.ethylene_check OR OLD.propylene_check != NEW.propylene_check OR OLD.propane_check != NEW.propane_check OR OLD.butene_check != NEW.butene_check OR OLD.i_isobutane_check != NEW.i_isobutane_check OR OLD.n_isobutane_check != NEW.n_isobutane_check OR OLD.pentane_check != NEW.pentane_check THEN
     update ccpp_questionnaire set 

     total_check=(NEW.methane_check)+(NEW.ethane_check)+(NEW.ethylene_check)+(NEW.propylene_check)+(NEW.propane_check)+(NEW.butene_check)+(NEW.i_isobutane_check)+(NEW.n_isobutane_check)+(NEW.pentane_check)+(NEW.carbon6_check)+(NEW.hydrogen_check)+(NEW.helium_check)+(NEW.nitrogen_check)+(NEW.carbon_monoxide_check)+(NEW.carbon_dioxide_check)+(NEW.hydrogen_sulfide_check)+(NEW.oxygen_check)+(NEW.water_check)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.water_check ISNULL OR OLD.oxygen_check ISNULL OR OLD.hydrogen_sulfide_check ISNULL OR OLD.carbon_dioxide_check ISNULL OR OLD.carbon_monoxide_check ISNULL OR OLD.nitrogen_check ISNULL OR OLD.helium_check ISNULL OR OLD.hydrogen_check ISNULL OR OLD.carbon6_check ISNULL OR OLD.pentane_check ISNULL OR OLD.n_isobutane_check ISNULL OR OLD.i_isobutane_check ISNULL OR OLD.butene_check ISNULL OR OLD.propane_check ISNULL OR OLD.propylene_check ISNULL OR OLD.ethylene_check ISNULL OR OLD.ethane_check ISNULL OR OLD.methane_check ISNULL) AND NEW.water_check NOTNULL AND NEW.oxygen_check NOTNULL AND NEW.hydrogen_sulfide_check NOTNULL AND NEW.carbon_dioxide_check NOTNULL AND NEW.carbon_monoxide_check NOTNULL AND NEW.nitrogen_check NOTNULL AND NEW.helium_check NOTNULL AND NEW.hydrogen_check NOTNULL AND NEW.carbon6_check NOTNULL AND NEW.pentane_check NOTNULL AND NEW.n_isobutane_check NOTNULL AND NEW.i_isobutane_check NOTNULL AND NEW.butene_check NOTNULL AND NEW.propane_check NOTNULL AND NEW.propylene_check NOTNULL AND NEW.ethylene_check NOTNULL AND NEW.ethane_check NOTNULL AND NEW.methane_check NOTNULL THEN
     update ccpp_questionnaire set 

     total_check=(NEW.methane_check)+(NEW.ethane_check)+(NEW.ethylene_check)+(NEW.propylene_check)+(NEW.propane_check)+(NEW.butene_check)+(NEW.i_isobutane_check)+(NEW.n_isobutane_check)+(NEW.pentane_check)+(NEW.carbon6_check)+(NEW.hydrogen_check)+(NEW.helium_check)+(NEW.nitrogen_check)+(NEW.carbon_monoxide_check)+(NEW.carbon_dioxide_check)+(NEW.hydrogen_sulfide_check)+(NEW.oxygen_check)+(NEW.water_check)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "ccpp_questionnaire_check" AFTER UPDATE OF
"methane_check",
"carbon6_check",
"hydrogen_check",
"helium_check",
"nitrogen_check",
"carbon_monoxide_check",
"carbon_dioxide_check",
"hydrogen_sulfide_check",
"oxygen_check",
"water_check",
"ethane_check",
"ethylene_check",
"propylene_check",
"propane_check",
"butene_check",
"i_isobutane_check",
"n_isobutane_check",
"pentane_check"
ON "public"."ccpp_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_questionnaire_check"();
