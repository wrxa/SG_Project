----------------------创建触发函数-----------------------------------
--用于同步表：gaspowergeneration_needsquestionnaire的c2s_local_atmosphere_air字段，和表gaspowergeneration_gas_air_system的atmosphere_pressure_a字段，即：gaspowergeneration_gas_air_system.c2s_local_atmosphere_air=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE OR REPLACE FUNCTION gaspowergeneration_gas_air_system_c2s_local_atmosphere_air()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_gas_air_system set c2s_local_atmosphere_air=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a*1000
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_gas_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的c2s_local_atmosphere_smoke字段，和表gaspowergeneration_gas_air_system的atmosphere_pressure_a字段，即：gaspowergeneration_gas_air_system.c2s_local_atmosphere_smoke=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE OR REPLACE FUNCTION gaspowergeneration_gas_air_system_c2s_local_atmosphere_smoke()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_gas_air_system set c2s_local_atmosphere_smoke=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a*1000
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_gas_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的s2c_local_atmosphere_air字段，和表gaspowergeneration_gas_air_system的atmosphere_pressure_a字段，即：gaspowergeneration_gas_air_system.s2c_local_atmosphere_air=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE OR REPLACE FUNCTION gaspowergeneration_gas_air_system_s2c_local_atmosphere_air()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_gas_air_system set s2c_local_atmosphere_air=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a*1000
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_gas_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的s2c_local_atmosphere_smoke字段，和表gaspowergeneration_gas_air_system的atmosphere_pressure_a字段，即：gaspowergeneration_gas_air_system.s2c_local_atmosphere_smoke=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE OR REPLACE FUNCTION gaspowergeneration_gas_air_system_s2c_local_atmosphere_smoke()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_gas_air_system set s2c_local_atmosphere_smoke=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a*1000
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_gas_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的s2c_local_atmosphere_gas字段，和表gaspowergeneration_gas_air_system的atmosphere_pressure_a字段，即：gaspowergeneration_gas_air_system.s2c_local_atmosphere_gas=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE OR REPLACE FUNCTION gaspowergeneration_gas_air_system_s2c_local_atmosphere_gas()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_gas_air_system set s2c_local_atmosphere_gas=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a*1000
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_gas_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的blower_local_atmosphere字段，和表gaspowergeneration_gas_air_system的atmosphere_pressure_a字段，即：gaspowergeneration_gas_air_system.blower_local_atmosphere=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE OR REPLACE FUNCTION gaspowergeneration_gas_air_system_blower_local_atmosphere()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_gas_air_system set blower_local_atmosphere=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a*1000
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_gas_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：gaspowergeneration_needsquestionnaire的induced_local_atmosphere字段，和表gaspowergeneration_gas_air_system的atmosphere_pressure_a字段，即：gaspowergeneration_gas_air_system.induced_local_atmosphere=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE OR REPLACE FUNCTION gaspowergeneration_gas_air_system_induced_local_atmosphere()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update gaspowergeneration_gas_air_system set induced_local_atmosphere=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a*1000
  from gaspowergeneration_needsquestionnaire where gaspowergeneration_needsquestionnaire.plan_id=gaspowergeneration_gas_air_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当atmosphere_pressure_a有更新时触发gaspowergeneration_gas_air_system.c2s_local_atmosphere_air=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_b_0" AFTER UPDATE OF "atmosphere_pressure_a" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_gas_air_system_c2s_local_atmosphere_air"();


--该触发器用于：当atmosphere_pressure_a有更新时触发gaspowergeneration_gas_air_system.c2s_local_atmosphere_smoke=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_b_1" AFTER UPDATE OF "atmosphere_pressure_a" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_gas_air_system_c2s_local_atmosphere_smoke"();


--该触发器用于：当atmosphere_pressure_a有更新时触发gaspowergeneration_gas_air_system.s2c_local_atmosphere_air=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_b_2" AFTER UPDATE OF "atmosphere_pressure_a" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_gas_air_system_s2c_local_atmosphere_air"();


--该触发器用于：当atmosphere_pressure_a有更新时触发gaspowergeneration_gas_air_system.s2c_local_atmosphere_smoke=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_b_3" AFTER UPDATE OF "atmosphere_pressure_a" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_gas_air_system_s2c_local_atmosphere_smoke"();


--该触发器用于：当atmosphere_pressure_a有更新时触发gaspowergeneration_gas_air_system.s2c_local_atmosphere_gas=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_b_4" AFTER UPDATE OF "atmosphere_pressure_a" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_gas_air_system_s2c_local_atmosphere_gas"();


--该触发器用于：当atmosphere_pressure_a有更新时触发gaspowergeneration_gas_air_system.blower_local_atmosphere=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_b_5" AFTER UPDATE OF "atmosphere_pressure_a" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_gas_air_system_blower_local_atmosphere"();


--该触发器用于：当atmosphere_pressure_a有更新时触发gaspowergeneration_gas_air_system.induced_local_atmosphere=gaspowergeneration_needsquestionnaire.atmosphere_pressure_a
CREATE TRIGGER "gaspowergeneration_needsquestionnaire_b_6" AFTER UPDATE OF "atmosphere_pressure_a" ON "public"."gaspowergeneration_needsquestionnaire"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_gas_air_system_induced_local_atmosphere"();


