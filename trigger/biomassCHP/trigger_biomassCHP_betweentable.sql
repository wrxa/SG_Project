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


--用于同步表：biomasschp_needs_questionnaire的c_base_volatile_obtained_design字段，和表biomasschp_boiler_calculation的s_grey_design字段，即：biomasschp_boiler_calculation.c_base_volatile_obtained_design=biomasschp_needs_questionnaire.s_grey_design
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_base_volatile_obtained_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_base_volatile_obtained_design=biomasschp_needs_questionnaire.s_grey_design
  from biomasschp_needs_questionnaire where biomasschp_needs_questionnaire.plan_id=biomasschp_boiler_calculation.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：biomasschp_needs_questionnaire的c_base_volatile_obtained_check字段，和表biomasschp_boiler_calculation的s_grey_check字段，即：biomasschp_boiler_calculation.c_base_volatile_obtained_check=biomasschp_needs_questionnaire.s_grey_check
CREATE OR REPLACE FUNCTION biomasschp_boiler_calculation_c_base_volatile_obtained_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update biomasschp_boiler_calculation set c_base_volatile_obtained_check=biomasschp_needs_questionnaire.s_grey_check
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


--该触发器用于：当s_grey_design有更新时触发biomasschp_boiler_calculation.c_base_volatile_obtained_design=biomasschp_needs_questionnaire.s_grey_design
CREATE TRIGGER "biomasschp_needs_questionnaire_a_14" AFTER UPDATE OF "s_grey_design" ON "public"."biomasschp_needs_questionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_boiler_calculation_c_base_volatile_obtained_design"();


--该触发器用于：当s_grey_check有更新时触发biomasschp_boiler_calculation.c_base_volatile_obtained_check=biomasschp_needs_questionnaire.s_grey_check
CREATE TRIGGER "biomasschp_needs_questionnaire_a_15" AFTER UPDATE OF "s_grey_check" ON "public"."biomasschp_needs_questionnaire"
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
  update biomasschp_fuel_st set b_rated_fuel_consumption_design=biomasschp_boiler_calculation.f_boiler_consumption_design
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
  update biomasschp_fuel_st set b_rated_fuel_consumption_check=biomasschp_boiler_calculation.f_boiler_consumption_check
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

