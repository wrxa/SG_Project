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



