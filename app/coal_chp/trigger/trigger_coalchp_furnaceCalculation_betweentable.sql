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
--用于同步表：coalchp_desulfurization_denitrification的d_boiler_total_design字段，和表coalchp_furnace_calculation的r_generate_grey字段，即：coalchp_furnace_calculation.d_boiler_total_design=coalchp_desulfurization_denitrification.r_generate_grey
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_d_boiler_total_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set d_boiler_total_design=coalchp_desulfurization_denitrification.r_generate_grey
  from coalchp_desulfurization_denitrification where coalchp_desulfurization_denitrification.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_desulfurization_denitrification的d_boiler_total_check字段，和表coalchp_furnace_calculation的r_generate_grey字段，即：coalchp_furnace_calculation.d_boiler_total_check=coalchp_desulfurization_denitrification.r_generate_grey
CREATE OR REPLACE FUNCTION coalchp_furnace_calculation_d_boiler_total_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_furnace_calculation set d_boiler_total_check=coalchp_desulfurization_denitrification.r_generate_grey
  from coalchp_desulfurization_denitrification where coalchp_desulfurization_denitrification.plan_id=coalchp_furnace_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当r_generate_grey有更新时触发coalchp_furnace_calculation.d_boiler_total_design=coalchp_desulfurization_denitrification.r_generate_grey
CREATE TRIGGER "coalchp_desulfurization_denitrification_a_0" AFTER UPDATE OF "r_generate_grey" ON "public"."coalchp_desulfurization_denitrification"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_d_boiler_total_design"();


--该触发器用于：当r_generate_grey有更新时触发coalchp_furnace_calculation.d_boiler_total_check=coalchp_desulfurization_denitrification.r_generate_grey
CREATE TRIGGER "coalchp_desulfurization_denitrification_a_1" AFTER UPDATE OF "r_generate_grey" ON "public"."coalchp_desulfurization_denitrification"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_furnace_calculation_d_boiler_total_check"();


