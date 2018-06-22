----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_needs_questionnaire的c_carbon_content_received_design字段，和表biomasschp_boiler_calculation的s_carbon_design字段，即：biomasschp_boiler_calculation.c_carbon_content_received_design=biomasschp_needs_questionnaire.s_carbon_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_carbon_content_received_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_carbon_content_received_design=biomasschp_needs_questionnaire.s_carbon_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_carbon_content_received_check字段，和表biomasschp_boiler_calculation的s_carbon_check字段，即：biomasschp_boiler_calculation.c_carbon_content_received_check=biomasschp_needs_questionnaire.s_carbon_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_carbon_content_received_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_carbon_content_received_check=biomasschp_needs_questionnaire.s_carbon_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_hydrogen_content_received_design字段，和表biomasschp_boiler_calculation的s_hydrogen_design字段，即：biomasschp_boiler_calculation.c_hydrogen_content_received_design=biomasschp_needs_questionnaire.s_hydrogen_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_hydrogen_content_received_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_hydrogen_content_received_design=biomasschp_needs_questionnaire.s_hydrogen_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_hydrogen_content_received_check字段，和表biomasschp_boiler_calculation的s_hydrogen_check字段，即：biomasschp_boiler_calculation.c_hydrogen_content_received_check=biomasschp_needs_questionnaire.s_hydrogen_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_hydrogen_content_received_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_hydrogen_content_received_check=biomasschp_needs_questionnaire.s_hydrogen_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_oxygen_content_received_design字段，和表biomasschp_boiler_calculation的s_oxygen_design字段，即：biomasschp_boiler_calculation.c_oxygen_content_received_design=biomasschp_needs_questionnaire.s_oxygen_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_oxygen_content_received_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_oxygen_content_received_design=biomasschp_needs_questionnaire.s_oxygen_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_oxygen_content_received_check字段，和表biomasschp_boiler_calculation的s_oxygen_check字段，即：biomasschp_boiler_calculation.c_oxygen_content_received_check=biomasschp_needs_questionnaire.s_oxygen_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_oxygen_content_received_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_oxygen_content_received_check=biomasschp_needs_questionnaire.s_oxygen_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_nitrogen_content_design字段，和表biomasschp_boiler_calculation的s_nitrogen_design字段，即：biomasschp_boiler_calculation.c_nitrogen_content_design=biomasschp_needs_questionnaire.s_nitrogen_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_nitrogen_content_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_nitrogen_content_design=biomasschp_needs_questionnaire.s_nitrogen_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_nitrogen_content_check字段，和表biomasschp_boiler_calculation的s_nitrogen_check字段，即：biomasschp_boiler_calculation.c_nitrogen_content_check=biomasschp_needs_questionnaire.s_nitrogen_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_nitrogen_content_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_nitrogen_content_check=biomasschp_needs_questionnaire.s_nitrogen_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_sulfur_content_received_design字段，和表biomasschp_boiler_calculation的s_sulfur_design字段，即：biomasschp_boiler_calculation.c_sulfur_content_received_design=biomasschp_needs_questionnaire.s_sulfur_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_sulfur_content_received_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_sulfur_content_received_design=biomasschp_needs_questionnaire.s_sulfur_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_sulfur_content_received_check字段，和表biomasschp_boiler_calculation的s_sulfur_check字段，即：biomasschp_boiler_calculation.c_sulfur_content_received_check=biomasschp_needs_questionnaire.s_sulfur_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_sulfur_content_received_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_sulfur_content_received_check=biomasschp_needs_questionnaire.s_sulfur_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_ash_content_received_design字段，和表biomasschp_boiler_calculation的s_grey_design字段，即：biomasschp_boiler_calculation.c_ash_content_received_design=biomasschp_needs_questionnaire.s_grey_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_ash_content_received_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_ash_content_received_design=biomasschp_needs_questionnaire.s_grey_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_ash_content_received_check字段，和表biomasschp_boiler_calculation的s_grey_check字段，即：biomasschp_boiler_calculation.c_ash_content_received_check=biomasschp_needs_questionnaire.s_grey_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_ash_content_received_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_ash_content_received_check=biomasschp_needs_questionnaire.s_grey_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_water_content_received_design字段，和表biomasschp_boiler_calculation的s_total_moisture_design字段，即：biomasschp_boiler_calculation.c_water_content_received_design=biomasschp_needs_questionnaire.s_total_moisture_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_water_content_received_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_water_content_received_design=biomasschp_needs_questionnaire.s_total_moisture_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_water_content_received_check字段，和表biomasschp_boiler_calculation的s_total_moisture_check字段，即：biomasschp_boiler_calculation.c_water_content_received_check=biomasschp_needs_questionnaire.s_total_moisture_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_water_content_received_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_water_content_received_check=biomasschp_needs_questionnaire.s_total_moisture_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_base_volatile_obtained_design字段，和表biomasschp_boiler_calculation的s_daf_design字段，即：biomasschp_boiler_calculation.c_base_volatile_obtained_design=biomasschp_needs_questionnaire.s_daf_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_base_volatile_obtained_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_base_volatile_obtained_design=biomasschp_needs_questionnaire.s_daf_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_base_volatile_obtained_check字段，和表biomasschp_boiler_calculation的s_daf_check字段，即：biomasschp_boiler_calculation.c_base_volatile_obtained_check=biomasschp_needs_questionnaire.s_daf_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_base_volatile_obtained_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_base_volatile_obtained_check=biomasschp_needs_questionnaire.s_daf_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_base_heat_received_user_design字段，和表biomasschp_boiler_calculation的s_quantity_design字段，即：biomasschp_boiler_calculation.c_base_heat_received_user_design=biomasschp_needs_questionnaire.s_quantity_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_base_heat_received_user_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_base_heat_received_user_design=biomasschp_needs_questionnaire.s_quantity_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_base_heat_received_user_check字段，和表biomasschp_boiler_calculation的s_quantity_check字段，即：biomasschp_boiler_calculation.c_base_heat_received_user_check=biomasschp_needs_questionnaire.s_quantity_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_base_heat_received_user_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_base_heat_received_user_check=biomasschp_needs_questionnaire.s_quantity_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_hot_temperature_design字段，和表biomasschp_boiler_calculation的l_max_temperature字段，即：biomasschp_boiler_calculation.a_hot_temperature_design=biomasschp_needs_questionnaire.l_max_temperature
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_a_hot_temperature_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set a_hot_temperature_design=biomasschp_needs_questionnaire.l_max_temperature
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_hot_temperature_check字段，和表biomasschp_boiler_calculation的l_max_temperature字段，即：biomasschp_boiler_calculation.a_hot_temperature_check=biomasschp_needs_questionnaire.l_max_temperature
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_a_hot_temperature_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set a_hot_temperature_check=biomasschp_needs_questionnaire.l_max_temperature
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_humidity_design字段，和表biomasschp_boiler_calculation的l_humidity字段，即：biomasschp_boiler_calculation.a_humidity_design=biomasschp_needs_questionnaire.l_humidity
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_a_humidity_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set a_humidity_design=biomasschp_needs_questionnaire.l_humidity
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_humidity_check字段，和表biomasschp_boiler_calculation的l_humidity字段，即：biomasschp_boiler_calculation.a_humidity_check=biomasschp_needs_questionnaire.l_humidity
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_a_humidity_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set a_humidity_check=biomasschp_needs_questionnaire.l_humidity
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_pressure_design字段，和表biomasschp_boiler_calculation的l_pressure字段，即：biomasschp_boiler_calculation.a_pressure_design=biomasschp_needs_questionnaire.l_pressure
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_a_pressure_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set a_pressure_design=biomasschp_needs_questionnaire.l_pressure
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_pressure_check字段，和表biomasschp_boiler_calculation的l_pressure字段，即：biomasschp_boiler_calculation.a_pressure_check=biomasschp_needs_questionnaire.l_pressure
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_a_pressure_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set a_pressure_check=biomasschp_needs_questionnaire.l_pressure
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_temperature_design字段，和表biomasschp_boiler_calculation的l_temperature字段，即：biomasschp_boiler_calculation.a_temperature_design=biomasschp_needs_questionnaire.l_temperature
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_a_temperature_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set a_temperature_design=biomasschp_needs_questionnaire.l_temperature
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_temperature_check字段，和表biomasschp_boiler_calculation的l_temperature字段，即：biomasschp_boiler_calculation.a_temperature_check=biomasschp_needs_questionnaire.l_temperature
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_a_temperature_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set a_temperature_check=biomasschp_needs_questionnaire.l_temperature
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当s_carbon_design有更新时触发biomasschp_boiler_calculation.c_carbon_content_received_design=biomasschp_needs_questionnaire.s_carbon_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_0" AFTER UPDATE OF "s_carbon_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_carbon_content_received_design"();


--该触发器用于：当s_carbon_check有更新时触发biomasschp_boiler_calculation.c_carbon_content_received_check=biomasschp_needs_questionnaire.s_carbon_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_1" AFTER UPDATE OF "s_carbon_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_carbon_content_received_check"();


--该触发器用于：当s_hydrogen_design有更新时触发biomasschp_boiler_calculation.c_hydrogen_content_received_design=biomasschp_needs_questionnaire.s_hydrogen_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_2" AFTER UPDATE OF "s_hydrogen_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_hydrogen_content_received_design"();


--该触发器用于：当s_hydrogen_check有更新时触发biomasschp_boiler_calculation.c_hydrogen_content_received_check=biomasschp_needs_questionnaire.s_hydrogen_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_3" AFTER UPDATE OF "s_hydrogen_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_hydrogen_content_received_check"();


--该触发器用于：当s_oxygen_design有更新时触发biomasschp_boiler_calculation.c_oxygen_content_received_design=biomasschp_needs_questionnaire.s_oxygen_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_4" AFTER UPDATE OF "s_oxygen_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_oxygen_content_received_design"();


--该触发器用于：当s_oxygen_check有更新时触发biomasschp_boiler_calculation.c_oxygen_content_received_check=biomasschp_needs_questionnaire.s_oxygen_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_5" AFTER UPDATE OF "s_oxygen_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_oxygen_content_received_check"();


--该触发器用于：当s_nitrogen_design有更新时触发biomasschp_boiler_calculation.c_nitrogen_content_design=biomasschp_needs_questionnaire.s_nitrogen_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_6" AFTER UPDATE OF "s_nitrogen_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_nitrogen_content_design"();


--该触发器用于：当s_nitrogen_check有更新时触发biomasschp_boiler_calculation.c_nitrogen_content_check=biomasschp_needs_questionnaire.s_nitrogen_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_7" AFTER UPDATE OF "s_nitrogen_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_nitrogen_content_check"();


--该触发器用于：当s_sulfur_design有更新时触发biomasschp_boiler_calculation.c_sulfur_content_received_design=biomasschp_needs_questionnaire.s_sulfur_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_8" AFTER UPDATE OF "s_sulfur_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_sulfur_content_received_design"();


--该触发器用于：当s_sulfur_check有更新时触发biomasschp_boiler_calculation.c_sulfur_content_received_check=biomasschp_needs_questionnaire.s_sulfur_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_9" AFTER UPDATE OF "s_sulfur_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_sulfur_content_received_check"();


--该触发器用于：当s_grey_design有更新时触发biomasschp_boiler_calculation.c_ash_content_received_design=biomasschp_needs_questionnaire.s_grey_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_10" AFTER UPDATE OF "s_grey_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_ash_content_received_design"();


--该触发器用于：当s_grey_check有更新时触发biomasschp_boiler_calculation.c_ash_content_received_check=biomasschp_needs_questionnaire.s_grey_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_11" AFTER UPDATE OF "s_grey_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_ash_content_received_check"();


--该触发器用于：当s_total_moisture_design有更新时触发biomasschp_boiler_calculation.c_water_content_received_design=biomasschp_needs_questionnaire.s_total_moisture_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_12" AFTER UPDATE OF "s_total_moisture_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_water_content_received_design"();


--该触发器用于：当s_total_moisture_check有更新时触发biomasschp_boiler_calculation.c_water_content_received_check=biomasschp_needs_questionnaire.s_total_moisture_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_13" AFTER UPDATE OF "s_total_moisture_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_water_content_received_check"();


--该触发器用于：当s_daf_design有更新时触发biomasschp_boiler_calculation.c_base_volatile_obtained_design=biomasschp_needs_questionnaire.s_daf_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_14" AFTER UPDATE OF "s_daf_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_base_volatile_obtained_design"();


--该触发器用于：当s_daf_check有更新时触发biomasschp_boiler_calculation.c_base_volatile_obtained_check=biomasschp_needs_questionnaire.s_daf_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_15" AFTER UPDATE OF "s_daf_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_base_volatile_obtained_check"();


--该触发器用于：当s_quantity_design有更新时触发biomasschp_boiler_calculation.c_base_heat_received_user_design=biomasschp_needs_questionnaire.s_quantity_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_16" AFTER UPDATE OF "s_quantity_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_base_heat_received_user_design"();


--该触发器用于：当s_quantity_check有更新时触发biomasschp_boiler_calculation.c_base_heat_received_user_check=biomasschp_needs_questionnaire.s_quantity_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_17" AFTER UPDATE OF "s_quantity_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_base_heat_received_user_check"();


--该触发器用于：当l_max_temperature有更新时触发biomasschp_boiler_calculation.a_hot_temperature_design=biomasschp_needs_questionnaire.l_max_temperature
CREATE TRIGGER "biomasschp_needs_questionnaire_a_18" AFTER UPDATE OF "l_max_temperature" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_a_hot_temperature_design"();


--该触发器用于：当l_max_temperature有更新时触发biomasschp_boiler_calculation.a_hot_temperature_check=biomasschp_needs_questionnaire.l_max_temperature
CREATE TRIGGER "biomasschp_needs_questionnaire_a_19" AFTER UPDATE OF "l_max_temperature" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_a_hot_temperature_check"();


--该触发器用于：当l_humidity有更新时触发biomasschp_boiler_calculation.a_humidity_design=biomasschp_needs_questionnaire.l_humidity
CREATE TRIGGER "biomasschp_needs_questionnaire_a_20" AFTER UPDATE OF "l_humidity" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_a_humidity_design"();


--该触发器用于：当l_humidity有更新时触发biomasschp_boiler_calculation.a_humidity_check=biomasschp_needs_questionnaire.l_humidity
CREATE TRIGGER "biomasschp_needs_questionnaire_a_21" AFTER UPDATE OF "l_humidity" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_a_humidity_check"();


--该触发器用于：当l_pressure有更新时触发biomasschp_boiler_calculation.a_pressure_design=biomasschp_needs_questionnaire.l_pressure
CREATE TRIGGER "biomasschp_needs_questionnaire_a_22" AFTER UPDATE OF "l_pressure" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_a_pressure_design"();


--该触发器用于：当l_pressure有更新时触发biomasschp_boiler_calculation.a_pressure_check=biomasschp_needs_questionnaire.l_pressure
CREATE TRIGGER "biomasschp_needs_questionnaire_a_23" AFTER UPDATE OF "l_pressure" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_a_pressure_check"();


--该触发器用于：当l_temperature有更新时触发biomasschp_boiler_calculation.a_temperature_design=biomasschp_needs_questionnaire.l_temperature
CREATE TRIGGER "biomasschp_needs_questionnaire_a_24" AFTER UPDATE OF "l_temperature" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_a_temperature_design"();


--该触发器用于：当l_temperature有更新时触发biomasschp_boiler_calculation.a_temperature_check=biomasschp_needs_questionnaire.l_temperature
CREATE TRIGGER "biomasschp_needs_questionnaire_a_25" AFTER UPDATE OF "l_temperature" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_a_temperature_check"();


----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_boiler_calculation的b_rated_fuel_consumption_design字段，和表biomasschp_fuel_st的f_boiler_consumption_design字段，即：biomasschp_fuel_st.b_rated_fuel_consumption_design=biomasschp_boiler_calculation.f_boiler_consumption_design
CREATE OR REPLACE FUNCTION biomasschp_fuel_st_b_rated_fuel_consumption_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_fuel_st set b_rated_fuel_consumption_design=biomasschp_boiler_calculation.f_boiler_consumption_design/1000
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_fuel_st.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的b_rated_fuel_consumption_check字段，和表biomasschp_fuel_st的f_boiler_consumption_check字段，即：biomasschp_fuel_st.b_rated_fuel_consumption_check=biomasschp_boiler_calculation.f_boiler_consumption_check
CREATE OR REPLACE FUNCTION biomasschp_fuel_st_b_rated_fuel_consumption_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_fuel_st set b_rated_fuel_consumption_check=biomasschp_boiler_calculation.f_boiler_consumption_check/1000
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_fuel_st.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当f_boiler_consumption_design有更新时触发biomasschp_fuel_st.b_rated_fuel_consumption_design=biomasschp_boiler_calculation.f_boiler_consumption_design
CREATE TRIGGER "biomasschp_boiler_calculation_a_0" AFTER UPDATE OF "f_boiler_consumption_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_fuel_st_b_rated_fuel_consumption_design"();


--该触发器用于：当f_boiler_consumption_check有更新时触发biomasschp_fuel_st.b_rated_fuel_consumption_check=biomasschp_boiler_calculation.f_boiler_consumption_check
CREATE TRIGGER "biomasschp_boiler_calculation_a_1" AFTER UPDATE OF "f_boiler_consumption_check" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_fuel_st_b_rated_fuel_consumption_check"();


----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_needs_questionnaire的s_sulfur_content_received字段，和表biomasschp_des_den的s_sulfur_design字段，即：biomasschp_des_den.s_sulfur_content_received=biomasschp_needs_questionnaire.s_sulfur_design
CREATE OR REPLACE FUNCTION biomasschp_des_den_s_sulfur_content_received()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_des_den set s_sulfur_content_received=biomasschp_needs_questionnaire.s_sulfur_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_des_den.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当s_sulfur_design有更新时触发biomasschp_des_den.s_sulfur_content_received=biomasschp_needs_questionnaire.s_sulfur_design
CREATE TRIGGER "biomasschp_needs_questionnaire_b_0" AFTER UPDATE OF "s_sulfur_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_des_den_s_sulfur_content_received"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_boiler_calculation的s_feed_consumption字段，和表biomasschp_des_den的f_calculation_consumption_design字段，即：biomasschp_des_den.s_feed_consumption=biomasschp_boiler_calculation.f_calculation_consumption_design
CREATE OR REPLACE FUNCTION biomasschp_des_den_s_feed_consumption()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_des_den set s_feed_consumption=biomasschp_boiler_calculation.f_calculation_consumption_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_des_den.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的s_input_smoke字段，和表biomasschp_des_den的i_standard_smoke_flow1_design字段，即：biomasschp_des_den.s_input_smoke=biomasschp_boiler_calculation.i_standard_smoke_flow1_design
CREATE OR REPLACE FUNCTION biomasschp_des_den_s_input_smoke()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_des_den set s_input_smoke=biomasschp_boiler_calculation.i_standard_smoke_flow1_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_des_den.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当f_calculation_consumption_design有更新时触发biomasschp_des_den.s_feed_consumption=biomasschp_boiler_calculation.f_calculation_consumption_design
CREATE TRIGGER "biomasschp_boiler_calculation_b_0" AFTER UPDATE OF "f_calculation_consumption_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_des_den_s_feed_consumption"();


--该触发器用于：当i_standard_smoke_flow1_design有更新时触发biomasschp_des_den.s_input_smoke=biomasschp_boiler_calculation.i_standard_smoke_flow1_design
CREATE TRIGGER "biomasschp_boiler_calculation_b_1" AFTER UPDATE OF "i_standard_smoke_flow1_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_des_den_s_input_smoke"();






----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_boiler_calculation的d_total_ash字段，和表biomasschp_das_remove的d_total_design字段，即：biomasschp_das_remove.d_total_ash=biomasschp_boiler_calculation.d_total_design
CREATE OR REPLACE FUNCTION biomasschp_das_remove_d_total_ash()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_das_remove set d_total_ash=biomasschp_boiler_calculation.d_total_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_das_remove.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的d_flyash_fraction字段，和表biomasschp_das_remove的d_ash_share_design字段，即：biomasschp_das_remove.d_flyash_fraction=biomasschp_boiler_calculation.d_ash_share_design
CREATE OR REPLACE FUNCTION biomasschp_das_remove_d_flyash_fraction()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_das_remove set d_flyash_fraction=biomasschp_boiler_calculation.d_ash_share_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_das_remove.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的d_standard_smoke_flow字段，和表biomasschp_das_remove的d_standard_smoke_flow_design字段，即：biomasschp_das_remove.d_standard_smoke_flow=biomasschp_boiler_calculation.d_standard_smoke_flow_design
CREATE OR REPLACE FUNCTION biomasschp_das_remove_d_standard_smoke_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_das_remove set d_standard_smoke_flow=biomasschp_boiler_calculation.d_standard_smoke_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_das_remove.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的d_actual_smoke_flow字段，和表biomasschp_das_remove的d_entry_smoke_actual_flow_design字段，即：biomasschp_das_remove.d_actual_smoke_flow=biomasschp_boiler_calculation.d_entry_smoke_actual_flow_design
CREATE OR REPLACE FUNCTION biomasschp_das_remove_d_actual_smoke_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_das_remove set d_actual_smoke_flow=biomasschp_boiler_calculation.d_entry_smoke_actual_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_das_remove.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的d_entry_smoke_volume字段，和表biomasschp_das_remove的i_smoke_actual_flow1_design字段，即：biomasschp_das_remove.d_entry_smoke_volume=biomasschp_boiler_calculation.i_smoke_actual_flow1_design
CREATE OR REPLACE FUNCTION biomasschp_das_remove_d_entry_smoke_volume()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_das_remove set d_entry_smoke_volume=biomasschp_boiler_calculation.i_smoke_actual_flow1_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_das_remove.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的s_slag_quantity字段，和表biomasschp_das_remove的d_dust_total_design字段，即：biomasschp_das_remove.s_slag_quantity=biomasschp_boiler_calculation.d_dust_total_design
CREATE OR REPLACE FUNCTION biomasschp_das_remove_s_slag_quantity()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_das_remove set s_slag_quantity=biomasschp_boiler_calculation.d_dust_total_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_das_remove.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当d_total_design有更新时触发biomasschp_das_remove.d_total_ash=biomasschp_boiler_calculation.d_total_design
CREATE TRIGGER "biomasschp_boiler_calculation_c_0" AFTER UPDATE OF "d_total_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_das_remove_d_total_ash"();


--该触发器用于：当d_ash_share_design有更新时触发biomasschp_das_remove.d_flyash_fraction=biomasschp_boiler_calculation.d_ash_share_design
CREATE TRIGGER "biomasschp_boiler_calculation_c_1" AFTER UPDATE OF "d_ash_share_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_das_remove_d_flyash_fraction"();


--该触发器用于：当d_standard_smoke_flow_design有更新时触发biomasschp_das_remove.d_standard_smoke_flow=biomasschp_boiler_calculation.d_standard_smoke_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_c_2" AFTER UPDATE OF "d_standard_smoke_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_das_remove_d_standard_smoke_flow"();


--该触发器用于：当d_entry_smoke_actual_flow_design有更新时触发biomasschp_das_remove.d_actual_smoke_flow=biomasschp_boiler_calculation.d_entry_smoke_actual_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_c_3" AFTER UPDATE OF "d_entry_smoke_actual_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_das_remove_d_actual_smoke_flow"();


--该触发器用于：当i_smoke_actual_flow1_design有更新时触发biomasschp_das_remove.d_entry_smoke_volume=biomasschp_boiler_calculation.i_smoke_actual_flow1_design
CREATE TRIGGER "biomasschp_boiler_calculation_c_4" AFTER UPDATE OF "i_smoke_actual_flow1_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_das_remove_d_entry_smoke_volume"();


--该触发器用于：当d_dust_total_design有更新时触发biomasschp_das_remove.s_slag_quantity=biomasschp_boiler_calculation.d_dust_total_design
CREATE TRIGGER "biomasschp_boiler_calculation_c_5" AFTER UPDATE OF "d_dust_total_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_das_remove_s_slag_quantity"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_boiler_calculation的f_working_flow字段，和表biomasschp_boiler_auxiliaries的a_first_cwind_actual_design字段，即：biomasschp_boiler_auxiliaries.f_working_flow=biomasschp_boiler_calculation.a_first_cwind_actual_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_f_working_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set f_working_flow=biomasschp_boiler_calculation.a_first_cwind_actual_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的s_working_flow字段，和表biomasschp_boiler_auxiliaries的a_second_cwind_actual_design字段，即：biomasschp_boiler_auxiliaries.s_working_flow=biomasschp_boiler_calculation.a_second_cwind_actual_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_s_working_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set s_working_flow=biomasschp_boiler_calculation.a_second_cwind_actual_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的a_working_flow字段，和表biomasschp_boiler_auxiliaries的i_smoke_actual_flow1_design字段，即：biomasschp_boiler_auxiliaries.a_working_flow=biomasschp_boiler_calculation.i_smoke_actual_flow1_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_a_working_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set a_working_flow=biomasschp_boiler_calculation.i_smoke_actual_flow1_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的bf_standard_flow字段，和表biomasschp_boiler_auxiliaries的a_first_cwind_standard_design字段，即：biomasschp_boiler_auxiliaries.bf_standard_flow=biomasschp_boiler_calculation.a_first_cwind_standard_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_bf_standard_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set bf_standard_flow=biomasschp_boiler_calculation.a_first_cwind_standard_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的bs_standard_flow字段，和表biomasschp_boiler_auxiliaries的a_second_cwind_standard_design字段，即：biomasschp_boiler_auxiliaries.bs_standard_flow=biomasschp_boiler_calculation.a_second_cwind_standard_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_bs_standard_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set bs_standard_flow=biomasschp_boiler_calculation.a_second_cwind_standard_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的ba_standard_flow字段，和表biomasschp_boiler_auxiliaries的i_standard_smoke_flow1_design字段，即：biomasschp_boiler_auxiliaries.ba_standard_flow=biomasschp_boiler_calculation.i_standard_smoke_flow1_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_ba_standard_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set ba_standard_flow=biomasschp_boiler_calculation.i_standard_smoke_flow1_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的r_boiler_evaporation字段，和表biomasschp_boiler_auxiliaries的f_steam_flow_design字段，即：biomasschp_boiler_auxiliaries.r_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_r_boiler_evaporation()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set r_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的c_boiler_evaporation字段，和表biomasschp_boiler_auxiliaries的f_steam_flow_design字段，即：biomasschp_boiler_auxiliaries.c_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_c_boiler_evaporation()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set c_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的r_drum_pressure字段，和表biomasschp_boiler_auxiliaries的f_boiler_pressure_design字段，即：biomasschp_boiler_auxiliaries.r_drum_pressure=biomasschp_boiler_calculation.f_boiler_pressure_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_r_drum_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set r_drum_pressure=biomasschp_boiler_calculation.f_boiler_pressure_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的c_drum_pressure字段，和表biomasschp_boiler_auxiliaries的f_boiler_pressure_design字段，即：biomasschp_boiler_auxiliaries.c_drum_pressure=biomasschp_boiler_calculation.f_boiler_pressure_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_c_drum_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set c_drum_pressure=biomasschp_boiler_calculation.f_boiler_pressure_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的r_drum_aturatedwater_enthalpy字段，和表biomasschp_boiler_auxiliaries的f_saturated_water_enthalpy_design字段，即：biomasschp_boiler_auxiliaries.r_drum_aturatedwater_enthalpy=biomasschp_boiler_calculation.f_saturated_water_enthalpy_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_r_drum_aturatedwater_enthalpy()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set r_drum_aturatedwater_enthalpy=biomasschp_boiler_calculation.f_saturated_water_enthalpy_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的c_drum_aturatedwater_enthalpy字段，和表biomasschp_boiler_auxiliaries的f_saturated_water_enthalpy_design字段，即：biomasschp_boiler_auxiliaries.c_drum_aturatedwater_enthalpy=biomasschp_boiler_calculation.f_saturated_water_enthalpy_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_c_drum_aturatedwater_enthalpy()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set c_drum_aturatedwater_enthalpy=biomasschp_boiler_calculation.f_saturated_water_enthalpy_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当a_first_cwind_actual_design有更新时触发biomasschp_boiler_auxiliaries.f_working_flow=biomasschp_boiler_calculation.a_first_cwind_actual_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_0" AFTER UPDATE OF "a_first_cwind_actual_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_f_working_flow"();


--该触发器用于：当a_second_cwind_actual_design有更新时触发biomasschp_boiler_auxiliaries.s_working_flow=biomasschp_boiler_calculation.a_second_cwind_actual_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_1" AFTER UPDATE OF "a_second_cwind_actual_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_s_working_flow"();


--该触发器用于：当i_smoke_actual_flow1_design有更新时触发biomasschp_boiler_auxiliaries.a_working_flow=biomasschp_boiler_calculation.i_smoke_actual_flow1_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_2" AFTER UPDATE OF "i_smoke_actual_flow1_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_a_working_flow"();


--该触发器用于：当a_first_cwind_standard_design有更新时触发biomasschp_boiler_auxiliaries.bf_standard_flow=biomasschp_boiler_calculation.a_first_cwind_standard_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_3" AFTER UPDATE OF "a_first_cwind_standard_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_bf_standard_flow"();


--该触发器用于：当a_second_cwind_standard_design有更新时触发biomasschp_boiler_auxiliaries.bs_standard_flow=biomasschp_boiler_calculation.a_second_cwind_standard_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_4" AFTER UPDATE OF "a_second_cwind_standard_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_bs_standard_flow"();


--该触发器用于：当i_standard_smoke_flow1_design有更新时触发biomasschp_boiler_auxiliaries.ba_standard_flow=biomasschp_boiler_calculation.i_standard_smoke_flow1_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_5" AFTER UPDATE OF "i_standard_smoke_flow1_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_ba_standard_flow"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_boiler_auxiliaries.r_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_6" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_r_boiler_evaporation"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_boiler_auxiliaries.c_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_7" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_c_boiler_evaporation"();


--该触发器用于：当f_boiler_pressure_design有更新时触发biomasschp_boiler_auxiliaries.r_drum_pressure=biomasschp_boiler_calculation.f_boiler_pressure_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_8" AFTER UPDATE OF "f_boiler_pressure_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_r_drum_pressure"();


--该触发器用于：当f_boiler_pressure_design有更新时触发biomasschp_boiler_auxiliaries.c_drum_pressure=biomasschp_boiler_calculation.f_boiler_pressure_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_9" AFTER UPDATE OF "f_boiler_pressure_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_c_drum_pressure"();


--该触发器用于：当f_saturated_water_enthalpy_design有更新时触发biomasschp_boiler_auxiliaries.r_drum_aturatedwater_enthalpy=biomasschp_boiler_calculation.f_saturated_water_enthalpy_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_10" AFTER UPDATE OF "f_saturated_water_enthalpy_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_r_drum_aturatedwater_enthalpy"();


--该触发器用于：当f_saturated_water_enthalpy_design有更新时触发biomasschp_boiler_auxiliaries.c_drum_aturatedwater_enthalpy=biomasschp_boiler_calculation.f_saturated_water_enthalpy_design
CREATE TRIGGER "biomasschp_boiler_calculation_d_11" AFTER UPDATE OF "f_saturated_water_enthalpy_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_c_drum_aturatedwater_enthalpy"();


----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_boiler_calculation的o_steam_flow字段，和表biomasschp_water_treatment的f_steam_flow_design字段，即：biomasschp_water_treatment.o_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_water_treatment_o_steam_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_water_treatment set o_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_water_treatment.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的o_loss_factory字段，和表biomasschp_water_treatment的f_steam_flow_design字段，即：biomasschp_water_treatment.o_loss_factory=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_water_treatment_o_loss_factory()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_water_treatment set o_loss_factory=biomasschp_boiler_calculation.f_steam_flow_design*0.03
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_water_treatment.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的o_boiler_blowdown_loss字段，和表biomasschp_water_treatment的f_steam_flow_design字段，即：biomasschp_water_treatment.o_boiler_blowdown_loss=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_water_treatment_o_boiler_blowdown_loss()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_water_treatment set o_boiler_blowdown_loss=biomasschp_boiler_calculation.f_steam_flow_design*0.02
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_water_treatment.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的o_start_accident_increase_loss字段，和表biomasschp_water_treatment的f_steam_flow_design字段，即：biomasschp_water_treatment.o_start_accident_increase_loss=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_water_treatment_o_start_accident_increase_loss()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_water_treatment set o_start_accident_increase_loss=biomasschp_boiler_calculation.f_steam_flow_design*0.1
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_water_treatment.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_water_treatment.o_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_f_0" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_water_treatment_o_steam_flow"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_water_treatment.o_loss_factory=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_f_1" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_water_treatment_o_loss_factory"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_water_treatment.o_boiler_blowdown_loss=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_f_2" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_water_treatment_o_boiler_blowdown_loss"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_water_treatment.o_start_accident_increase_loss=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_f_3" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_water_treatment_o_start_accident_increase_loss"();


----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_des_den的d_boiler_total_design字段，和表biomasschp_boiler_calculation的c_ash字段，即：biomasschp_boiler_calculation.d_boiler_total_design=biomasschp_des_den.c_ash
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_d_boiler_total_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set d_boiler_total_design=biomasschp_des_den.c_ash
  from biomasschp_des_den where biomasschp_des_den.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_des_den的d_boiler_total_check字段，和表biomasschp_boiler_calculation的c_ash字段，即：biomasschp_boiler_calculation.d_boiler_total_check=biomasschp_des_den.c_ash
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_d_boiler_total_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set d_boiler_total_check=biomasschp_des_den.c_ash
  from biomasschp_des_den where biomasschp_des_den.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当c_ash有更新时触发biomasschp_boiler_calculation.d_boiler_total_design=biomasschp_des_den.c_ash
CREATE TRIGGER "biomasschp_des_den_f_0" AFTER UPDATE OF "c_ash" ON "public"."biomasschp_des_den"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_d_boiler_total_design"();


--该触发器用于：当c_ash有更新时触发biomasschp_boiler_calculation.d_boiler_total_check=biomasschp_des_den.c_ash
CREATE TRIGGER "biomasschp_des_den_f_1" AFTER UPDATE OF "c_ash" ON "public"."biomasschp_des_den"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_d_boiler_total_check"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_needs_questionnaire的a_altitude字段，和表biomasschp_boiler_auxiliaries的l_altitude字段，即：biomasschp_boiler_auxiliaries.a_altitude=biomasschp_needs_questionnaire.l_altitude
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_a_altitude()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set a_altitude=biomasschp_needs_questionnaire.l_altitude
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_atmosphere字段，和表biomasschp_boiler_auxiliaries的l_pressure字段，即：biomasschp_boiler_auxiliaries.a_atmosphere=biomasschp_needs_questionnaire.l_pressure
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_a_atmosphere()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set a_atmosphere=biomasschp_needs_questionnaire.l_pressure*1000
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当l_altitude有更新时触发biomasschp_boiler_auxiliaries.a_altitude=biomasschp_needs_questionnaire.l_altitude
CREATE TRIGGER "biomasschp_needs_questionnaire_e_2" AFTER UPDATE OF "l_altitude" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_a_altitude"();


--该触发器用于：当l_pressure有更新时触发biomasschp_boiler_auxiliaries.a_atmosphere=biomasschp_needs_questionnaire.l_pressure
CREATE TRIGGER "biomasschp_needs_questionnaire_e_3" AFTER UPDATE OF "l_pressure" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_a_atmosphere"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_boiler_calculation的e_steam_flow字段，和表biomasschp_turbine_backpressure的f_steam_flow_design字段，即：biomasschp_turbine_backpressure.e_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_turbine_backpressure_e_steam_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_backpressure set e_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_turbine_backpressure.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的e_throttle_flow字段，和表biomasschp_turbine_backpressure的f_steam_flow_design字段，即：biomasschp_turbine_backpressure.e_throttle_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_turbine_backpressure_e_throttle_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_backpressure set e_throttle_flow=biomasschp_boiler_calculation.f_steam_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_turbine_backpressure.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的i_steam_flow字段，和表biomasschp_turbine_backpressure的f_steam_flow_design字段，即：biomasschp_turbine_backpressure.i_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_turbine_backpressure_i_steam_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_backpressure set i_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_turbine_backpressure.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;

--用于同步表：biomasschp_boiler_calculation的hh1_water_temperature字段，和表biomasschp_turbine_backpressure的f_water_temperature_design字段，即：biomasschp_turbine_backpressure.hh1_water_temperature=biomasschp_boiler_calculation.f_water_temperature_design
CREATE OR REPLACE FUNCTION biomasschp_turbine_backpressure_hh1_water_temperature()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_backpressure set hh1_water_temperature=biomasschp_boiler_calculation.f_water_temperature_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_turbine_backpressure.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_turbine_backpressure.e_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_g_0" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_backpressure_e_steam_flow"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_turbine_backpressure.e_throttle_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_g_1" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_backpressure_e_throttle_flow"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_turbine_backpressure.i_steam_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_g_2" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_backpressure_i_steam_flow"();


--该触发器用于：当f_water_temperature_design有更新时触发biomasschp_turbine_backpressure.hh1_water_temperature=biomasschp_boiler_calculation.f_water_temperature_design
CREATE TRIGGER "biomasschp_boiler_calculation_g_3" AFTER UPDATE OF "f_water_temperature_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_backpressure_hh1_water_temperature"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_needs_questionnaire的heat_area字段，和表biomasschp_heat_supply的t_recent_heating_area字段，即：biomasschp_heat_supply.heat_area=biomasschp_needs_questionnaire.t_recent_heating_area
CREATE OR REPLACE FUNCTION biomasschp_heat_supply_heat_area()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_heat_supply set heat_area=biomasschp_needs_questionnaire.t_recent_heating_area*10000
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_heat_supply.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的use_flow字段，和表biomasschp_heat_supply的t_recent_steam_flow_range字段，即：biomasschp_heat_supply.use_flow=biomasschp_needs_questionnaire.t_recent_steam_flow_range
CREATE OR REPLACE FUNCTION biomasschp_heat_supply_use_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_heat_supply set use_flow=biomasschp_needs_questionnaire.t_recent_steam_flow_range
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_heat_supply.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当t_recent_heating_area有更新时触发biomasschp_heat_supply.heat_area=biomasschp_needs_questionnaire.t_recent_heating_area
CREATE TRIGGER "biomasschp_needs_questionnaire_h_0" AFTER UPDATE OF "t_recent_heating_area" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_heat_supply_heat_area"();


--该触发器用于：当t_recent_steam_flow_range有更新时触发biomasschp_heat_supply.use_flow=biomasschp_needs_questionnaire.t_recent_steam_flow_range
CREATE TRIGGER "biomasschp_needs_questionnaire_h_1" AFTER UPDATE OF "t_recent_steam_flow_range" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_heat_supply_use_flow"();


----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_turbine_backpressure的hidden_turbine字段，和表biomasschp_heat_supply的e_exhaust_point_enthalpy字段，即：biomasschp_heat_supply.hidden_turbine=biomasschp_turbine_backpressure.e_exhaust_point_enthalpy
CREATE OR REPLACE FUNCTION biomasschp_heat_supply_hidden_turbine()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_heat_supply set hidden_turbine=biomasschp_turbine_backpressure.e_exhaust_point_enthalpy
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_heat_supply.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当e_exhaust_point_enthalpy有更新时触发biomasschp_heat_supply.hidden_turbine=biomasschp_turbine_backpressure.e_exhaust_point_enthalpy
CREATE TRIGGER "biomasschp_turbine_backpressure_h_3" AFTER UPDATE OF "e_exhaust_point_enthalpy" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_heat_supply_hidden_turbine"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_boiler_calculation的local_atmosphere字段，和表biomasschp_chimney的(a_pressure_design)*1000字段，即：biomasschp_chimney.local_atmosphere=biomasschp_boiler_calculation.(a_pressure_design)*1000
CREATE OR REPLACE FUNCTION biomasschp_chimney_local_atmosphere()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_chimney set local_atmosphere=(biomasschp_boiler_calculation.a_pressure_design)*1000
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_chimney.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的standard_air_density字段，和表biomasschp_chimney的a_standard_air_humidity_design字段，即：biomasschp_chimney.standard_air_density=biomasschp_boiler_calculation.a_standard_air_humidity_design
CREATE OR REPLACE FUNCTION biomasschp_chimney_standard_air_density()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_chimney set standard_air_density=biomasschp_boiler_calculation.a_standard_air_humidity_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_chimney.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的standard_average_smoke_density字段，和表biomasschp_chimney的s_wet_smoke_density_design字段，即：biomasschp_chimney.standard_average_smoke_density=biomasschp_boiler_calculation.s_wet_smoke_density_design
CREATE OR REPLACE FUNCTION biomasschp_chimney_standard_average_smoke_density()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_chimney set standard_average_smoke_density=biomasschp_boiler_calculation.s_wet_smoke_density_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_chimney.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的chimney_inlet_temperature字段，和表biomasschp_chimney的p_smoke_temperature_design字段，即：biomasschp_chimney.chimney_inlet_temperature=biomasschp_boiler_calculation.p_smoke_temperature_design
CREATE OR REPLACE FUNCTION biomasschp_chimney_chimney_inlet_temperature()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_chimney set chimney_inlet_temperature=biomasschp_boiler_calculation.p_smoke_temperature_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_chimney.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的smoke_amount字段，和表biomasschp_chimney的go_smoke_flow_design字段，即：biomasschp_chimney.smoke_amount=biomasschp_boiler_calculation.go_smoke_flow_design
CREATE OR REPLACE FUNCTION biomasschp_chimney_smoke_amount()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_chimney set smoke_amount=biomasschp_boiler_calculation.go_smoke_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_chimney.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当(a_pressure_design)*1000有更新时触发biomasschp_chimney.local_atmosphere=biomasschp_boiler_calculation.(a_pressure_design)*1000
CREATE TRIGGER "biomasschp_boiler_calculation_B_0" AFTER UPDATE OF "a_pressure_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_chimney_local_atmosphere"();


--该触发器用于：当a_standard_air_humidity_design有更新时触发biomasschp_chimney.standard_air_density=biomasschp_boiler_calculation.a_standard_air_humidity_design
CREATE TRIGGER "biomasschp_boiler_calculation_B_1" AFTER UPDATE OF "a_standard_air_humidity_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_chimney_standard_air_density"();


--该触发器用于：当s_wet_smoke_density_design有更新时触发biomasschp_chimney.standard_average_smoke_density=biomasschp_boiler_calculation.s_wet_smoke_density_design
CREATE TRIGGER "biomasschp_boiler_calculation_B_2" AFTER UPDATE OF "s_wet_smoke_density_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_chimney_standard_average_smoke_density"();


--该触发器用于：当p_smoke_temperature_design有更新时触发biomasschp_chimney.chimney_inlet_temperature=biomasschp_boiler_calculation.p_smoke_temperature_design
CREATE TRIGGER "biomasschp_boiler_calculation_B_3" AFTER UPDATE OF "p_smoke_temperature_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_chimney_chimney_inlet_temperature"();


--该触发器用于：当go_smoke_flow_design有更新时触发biomasschp_chimney.smoke_amount=biomasschp_boiler_calculation.go_smoke_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_B_4" AFTER UPDATE OF "go_smoke_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_chimney_smoke_amount"();


----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_needs_questionnaire的d_fuel_bulk_density_design字段，和表biomasschp_fuel_st的s_fuel_density_design字段，即：biomasschp_fuel_st.d_fuel_bulk_density_design=biomasschp_needs_questionnaire.s_fuel_density_design
CREATE OR REPLACE FUNCTION biomasschp_fuel_st_d_fuel_bulk_density_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_fuel_st set d_fuel_bulk_density_design=biomasschp_needs_questionnaire.s_fuel_density_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_fuel_st.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的s_fuel_bulk_density_design字段，和表biomasschp_fuel_st的s_fuel_density_design字段，即：biomasschp_fuel_st.s_fuel_bulk_density_design=biomasschp_needs_questionnaire.s_fuel_density_design
CREATE OR REPLACE FUNCTION biomasschp_fuel_st_s_fuel_bulk_density_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_fuel_st set s_fuel_bulk_density_design=biomasschp_needs_questionnaire.s_fuel_density_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_fuel_st.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的f_loose_density字段，和表biomasschp_fuel_st的s_fuel_density_design字段，即：biomasschp_fuel_st.f_loose_density=biomasschp_needs_questionnaire.s_fuel_density_design
CREATE OR REPLACE FUNCTION biomasschp_fuel_st_f_loose_density()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_fuel_st set f_loose_density=biomasschp_needs_questionnaire.s_fuel_density_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_fuel_st.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的d_fuel_bulk_density_check字段，和表biomasschp_fuel_st的s_fuel_density_check字段，即：biomasschp_fuel_st.d_fuel_bulk_density_check=biomasschp_needs_questionnaire.s_fuel_density_check
CREATE OR REPLACE FUNCTION biomasschp_fuel_st_d_fuel_bulk_density_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_fuel_st set d_fuel_bulk_density_check=biomasschp_needs_questionnaire.s_fuel_density_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_fuel_st.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的s_fuel_bulk_density_check字段，和表biomasschp_fuel_st的s_fuel_density_check字段，即：biomasschp_fuel_st.s_fuel_bulk_density_check=biomasschp_needs_questionnaire.s_fuel_density_check
CREATE OR REPLACE FUNCTION biomasschp_fuel_st_s_fuel_bulk_density_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_fuel_st set s_fuel_bulk_density_check=biomasschp_needs_questionnaire.s_fuel_density_check
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_fuel_st.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当s_fuel_density_design有更新时触发biomasschp_fuel_st.d_fuel_bulk_density_design=biomasschp_needs_questionnaire.s_fuel_density_design
CREATE TRIGGER "biomasschp_needs_questionnaire_i_0" AFTER UPDATE OF "s_fuel_density_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_fuel_st_d_fuel_bulk_density_design"();


--该触发器用于：当s_fuel_density_design有更新时触发biomasschp_fuel_st.s_fuel_bulk_density_design=biomasschp_needs_questionnaire.s_fuel_density_design
CREATE TRIGGER "biomasschp_needs_questionnaire_i_1" AFTER UPDATE OF "s_fuel_density_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_fuel_st_s_fuel_bulk_density_design"();


--该触发器用于：当s_fuel_density_design有更新时触发biomasschp_fuel_st.f_loose_density=biomasschp_needs_questionnaire.s_fuel_density_design
CREATE TRIGGER "biomasschp_needs_questionnaire_i_2" AFTER UPDATE OF "s_fuel_density_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_fuel_st_f_loose_density"();


--该触发器用于：当s_fuel_density_check有更新时触发biomasschp_fuel_st.d_fuel_bulk_density_check=biomasschp_needs_questionnaire.s_fuel_density_check
CREATE TRIGGER "biomasschp_needs_questionnaire_i_3" AFTER UPDATE OF "s_fuel_density_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_fuel_st_d_fuel_bulk_density_check"();


--该触发器用于：当s_fuel_density_check有更新时触发biomasschp_fuel_st.s_fuel_bulk_density_check=biomasschp_needs_questionnaire.s_fuel_density_check
CREATE TRIGGER "biomasschp_needs_questionnaire_i_4" AFTER UPDATE OF "s_fuel_density_check" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_fuel_st_s_fuel_bulk_density_check"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_needs_questionnaire的s_env_after_so2字段，和表biomasschp_des_den的o_flue_gas_sox_limits字段，即：biomasschp_des_den.s_env_after_so2=biomasschp_needs_questionnaire.o_flue_gas_sox_limits
CREATE OR REPLACE FUNCTION biomasschp_des_den_s_env_after_so2()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_des_den set s_env_after_so2=biomasschp_needs_questionnaire.o_flue_gas_sox_limits
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_des_den.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的n_env_after_nox_concentration字段，和表biomasschp_des_den的o_flue_gas_nox_limits字段，即：biomasschp_des_den.n_env_after_nox_concentration=biomasschp_needs_questionnaire.o_flue_gas_nox_limits
CREATE OR REPLACE FUNCTION biomasschp_des_den_n_env_after_nox_concentration()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_des_den set n_env_after_nox_concentration=biomasschp_needs_questionnaire.o_flue_gas_nox_limits
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_des_den.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当o_flue_gas_sox_limits有更新时触发biomasschp_des_den.s_env_after_so2=biomasschp_needs_questionnaire.o_flue_gas_sox_limits
CREATE TRIGGER "biomasschp_needs_questionnaire_i_5" AFTER UPDATE OF "o_flue_gas_sox_limits" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_des_den_s_env_after_so2"();


--该触发器用于：当o_flue_gas_nox_limits有更新时触发biomasschp_des_den.n_env_after_nox_concentration=biomasschp_needs_questionnaire.o_flue_gas_nox_limits
CREATE TRIGGER "biomasschp_needs_questionnaire_i_6" AFTER UPDATE OF "o_flue_gas_nox_limits" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_des_den_n_env_after_nox_concentration"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_needs_questionnaire的d_env_particulate字段，和表biomasschp_das_remove的o_flue_gas_dust_limits字段，即：biomasschp_das_remove.d_env_particulate=biomasschp_needs_questionnaire.o_flue_gas_dust_limits
CREATE OR REPLACE FUNCTION biomasschp_das_remove_d_env_particulate()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_das_remove set d_env_particulate=biomasschp_needs_questionnaire.o_flue_gas_dust_limits
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_das_remove.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的a_bulk_density字段，和表biomasschp_das_remove的s_ash_density_design字段，即：biomasschp_das_remove.a_bulk_density=biomasschp_needs_questionnaire.s_ash_density_design
CREATE OR REPLACE FUNCTION biomasschp_das_remove_a_bulk_density()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_das_remove set a_bulk_density=biomasschp_needs_questionnaire.s_ash_density_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_das_remove.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当o_flue_gas_dust_limits有更新时触发biomasschp_das_remove.d_env_particulate=biomasschp_needs_questionnaire.o_flue_gas_dust_limits
CREATE TRIGGER "biomasschp_needs_questionnaire_i_7" AFTER UPDATE OF "o_flue_gas_dust_limits" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_das_remove_d_env_particulate"();


--该触发器用于：当s_ash_density_design有更新时触发biomasschp_das_remove.a_bulk_density=biomasschp_needs_questionnaire.s_ash_density_design
CREATE TRIGGER "biomasschp_needs_questionnaire_i_8" AFTER UPDATE OF "s_ash_density_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_das_remove_a_bulk_density"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_boiler_calculation的f_boiler_use_pressure字段，和表biomasschp_boiler_auxiliaries的f_steam_pressure_design字段，即：biomasschp_boiler_auxiliaries.f_boiler_use_pressure=biomasschp_boiler_calculation.f_steam_pressure_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_f_boiler_use_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set f_boiler_use_pressure=biomasschp_boiler_calculation.f_steam_pressure_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的f_flow字段，和表biomasschp_boiler_auxiliaries的f_steam_flow_design字段，即：biomasschp_boiler_auxiliaries.f_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_f_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set f_flow=biomasschp_boiler_calculation.f_steam_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_boiler_calculation的f_boiler_evaporation字段，和表biomasschp_boiler_auxiliaries的f_steam_flow_design字段，即：biomasschp_boiler_auxiliaries.f_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_f_boiler_evaporation()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set f_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
  from biomasschp_boiler_calculation where biomasschp_boiler_calculation.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当f_steam_pressure_design有更新时触发biomasschp_boiler_auxiliaries.f_boiler_use_pressure=biomasschp_boiler_calculation.f_steam_pressure_design
CREATE TRIGGER "biomasschp_boiler_calculation_i_9" AFTER UPDATE OF "f_steam_pressure_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_f_boiler_use_pressure"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_boiler_auxiliaries.f_flow=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_i_10" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_f_flow"();


--该触发器用于：当f_steam_flow_design有更新时触发biomasschp_boiler_auxiliaries.f_boiler_evaporation=biomasschp_boiler_calculation.f_steam_flow_design
CREATE TRIGGER "biomasschp_boiler_calculation_i_11" AFTER UPDATE OF "f_steam_flow_design" ON "public"."biomasschp_boiler_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_f_boiler_evaporation"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_turbine_backpressure的f_deaerator_work_pressure字段，和表biomasschp_boiler_auxiliaries的d_work_pressure字段，即：biomasschp_boiler_auxiliaries.f_deaerator_work_pressure=biomasschp_turbine_backpressure.d_work_pressure
CREATE OR REPLACE FUNCTION biomasschp_boiler_auxiliaries_f_deaerator_work_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_auxiliaries set f_deaerator_work_pressure=biomasschp_turbine_backpressure.d_work_pressure
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_boiler_auxiliaries.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当d_work_pressure有更新时触发biomasschp_boiler_auxiliaries.f_deaerator_work_pressure=biomasschp_turbine_backpressure.d_work_pressure
CREATE TRIGGER "biomasschp_turbine_backpressure_i_12" AFTER UPDATE OF "d_work_pressure" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_auxiliaries_f_deaerator_work_pressure"();

----------------------创建触发函数-----------------------------------
--用于同步表：biomasschp_turbine_backpressure的w_deaerator_working_pressure字段，和表biomasschp_turbine_auxiliary的d_work_pressure字段，即：biomasschp_turbine_auxiliary.w_deaerator_working_pressure=biomasschp_turbine_backpressure.d_work_pressure
CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary_w_deaerator_working_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_auxiliary set w_deaerator_working_pressure=biomasschp_turbine_backpressure.d_work_pressure
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_turbine_auxiliary.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_turbine_backpressure的w_condenser_higter字段，和表biomasschp_turbine_auxiliary的e_steam_exhaust_pressure字段，即：biomasschp_turbine_auxiliary.w_condenser_higter=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary_w_condenser_higter()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_auxiliary set w_condenser_higter=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_turbine_auxiliary.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_turbine_backpressure的m_condenser_pressure字段，和表biomasschp_turbine_auxiliary的e_steam_exhaust_pressure字段，即：biomasschp_turbine_auxiliary.m_condenser_pressure=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary_m_condenser_pressure()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_auxiliary set m_condenser_pressure=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_turbine_auxiliary.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_turbine_backpressure的m_steam_enthalpy字段，和表biomasschp_turbine_auxiliary的i_steam_exhaust_enthalpy_actual字段，即：biomasschp_turbine_auxiliary.m_steam_enthalpy=biomasschp_turbine_backpressure.i_steam_exhaust_enthalpy_actual
CREATE OR REPLACE FUNCTION biomasschp_turbine_auxiliary_m_steam_enthalpy()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_turbine_auxiliary set m_steam_enthalpy=biomasschp_turbine_backpressure.i_steam_exhaust_enthalpy_actual
  from biomasschp_turbine_backpressure where biomasschp_turbine_backpressure.plan_id=biomasschp_turbine_auxiliary.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当d_work_pressure有更新时触发biomasschp_turbine_auxiliary.w_deaerator_working_pressure=biomasschp_turbine_backpressure.d_work_pressure
CREATE TRIGGER "biomasschp_turbine_backpressure_a_0" AFTER UPDATE OF "d_work_pressure" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary_w_deaerator_working_pressure"();


--该触发器用于：当e_steam_exhaust_pressure有更新时触发biomasschp_turbine_auxiliary.w_condenser_higter=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
CREATE TRIGGER "biomasschp_turbine_backpressure_a_1" AFTER UPDATE OF "e_steam_exhaust_pressure" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary_w_condenser_higter"();


--该触发器用于：当e_steam_exhaust_pressure有更新时触发biomasschp_turbine_auxiliary.m_condenser_pressure=biomasschp_turbine_backpressure.e_steam_exhaust_pressure
CREATE TRIGGER "biomasschp_turbine_backpressure_a_2" AFTER UPDATE OF "e_steam_exhaust_pressure" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary_m_condenser_pressure"();


--该触发器用于：当i_steam_exhaust_enthalpy_actual有更新时触发biomasschp_turbine_auxiliary.m_steam_enthalpy=biomasschp_turbine_backpressure.i_steam_exhaust_enthalpy_actual
CREATE TRIGGER "biomasschp_turbine_backpressure_a_3" AFTER UPDATE OF "i_steam_exhaust_enthalpy_actual" ON "public"."biomasschp_turbine_backpressure"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_turbine_auxiliary_m_steam_enthalpy"();