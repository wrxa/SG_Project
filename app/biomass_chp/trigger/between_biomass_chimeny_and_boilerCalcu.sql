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


