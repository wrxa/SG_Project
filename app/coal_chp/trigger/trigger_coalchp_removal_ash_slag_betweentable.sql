----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_furnace_calculation的a_total_ash_residue_after字段，和表coalchp_removal_ash_slag_system的d_total_design字段，即：coalchp_removal_ash_slag_system.a_total_ash_residue_after=coalchp_furnace_calculation.d_total_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_a_total_ash_residue_after()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set a_total_ash_residue_after=coalchp_furnace_calculation.d_total_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的a_the_imported_smoke_volume字段，和表coalchp_removal_ash_slag_system的d_standard_smoke_flow_design字段，即：coalchp_removal_ash_slag_system.a_the_imported_smoke_volume=coalchp_furnace_calculation.d_standard_smoke_flow_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_a_the_imported_smoke_volume()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set a_the_imported_smoke_volume=coalchp_furnace_calculation.d_standard_smoke_flow_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的a_the_smoke_volume_flow字段，和表coalchp_removal_ash_slag_system的d_entry_smoke_actual_flow_design字段，即：coalchp_removal_ash_slag_system.a_the_smoke_volume_flow=coalchp_furnace_calculation.d_entry_smoke_actual_flow_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_a_the_smoke_volume_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set a_the_smoke_volume_flow=coalchp_furnace_calculation.d_entry_smoke_actual_flow_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的a_the_imported_smoke_real_state字段，和表coalchp_removal_ash_slag_system的i_smoke_actual_flow1_design字段，即：coalchp_removal_ash_slag_system.a_the_imported_smoke_real_state=coalchp_furnace_calculation.i_smoke_actual_flow1_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_a_the_imported_smoke_real_state()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set a_the_imported_smoke_real_state=coalchp_furnace_calculation.i_smoke_actual_flow1_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的s_slag_amount字段，和表coalchp_removal_ash_slag_system的d_dust_total_design字段，即：coalchp_removal_ash_slag_system.s_slag_amount=coalchp_furnace_calculation.d_dust_total_design
CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system_s_slag_amount()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_removal_ash_slag_system set s_slag_amount=coalchp_furnace_calculation.d_dust_total_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_removal_ash_slag_system.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当d_total_design有更新时触发coalchp_removal_ash_slag_system.a_total_ash_residue_after=coalchp_furnace_calculation.d_total_design
CREATE TRIGGER "coalchp_furnace_calculation_a_0" AFTER UPDATE OF "d_total_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_a_total_ash_residue_after"();


--该触发器用于：当d_standard_smoke_flow_design有更新时触发coalchp_removal_ash_slag_system.a_the_imported_smoke_volume=coalchp_furnace_calculation.d_standard_smoke_flow_design
CREATE TRIGGER "coalchp_furnace_calculation_a_1" AFTER UPDATE OF "d_standard_smoke_flow_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_a_the_imported_smoke_volume"();


--该触发器用于：当d_entry_smoke_actual_flow_design有更新时触发coalchp_removal_ash_slag_system.a_the_smoke_volume_flow=coalchp_furnace_calculation.d_entry_smoke_actual_flow_design
CREATE TRIGGER "coalchp_furnace_calculation_a_2" AFTER UPDATE OF "d_entry_smoke_actual_flow_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_a_the_smoke_volume_flow"();


--该触发器用于：当i_smoke_actual_flow1_design有更新时触发coalchp_removal_ash_slag_system.a_the_imported_smoke_real_state=coalchp_furnace_calculation.i_smoke_actual_flow1_design
CREATE TRIGGER "coalchp_furnace_calculation_a_3" AFTER UPDATE OF "i_smoke_actual_flow1_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_a_the_imported_smoke_real_state"();


--该触发器用于：当d_dust_total_design有更新时触发coalchp_removal_ash_slag_system.s_slag_amount=coalchp_furnace_calculation.d_dust_total_design
CREATE TRIGGER "coalchp_furnace_calculation_a_4" AFTER UPDATE OF "d_dust_total_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system_s_slag_amount"();

----------------------创建触发器-----------------------------------

--该触发器用于：当f_boiler_consumption_design有更新时触发coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_design=coalchp_furnace_calculation.f_boiler_consumption_design
CREATE TRIGGER "coalchp_furnace_calculation_a_5" AFTER UPDATE OF "f_boiler_consumption_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_coal_handingsystem_b_boiler_rated_coal_capacity_design"();


--该触发器用于：当f_boiler_consumption_check有更新时触发coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_check=coalchp_furnace_calculation.f_boiler_consumption_check
CREATE TRIGGER "coalchp_furnace_calculation_a_6" AFTER UPDATE OF "f_boiler_consumption_check" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_coal_handingsystem_b_boiler_rated_coal_capacity_check"();


--该触发器用于：当s_sulfur_design有更新时触发coalchp_desulfurization_denitrification.s_sulfur_design=coalchp_furnace_calculation.s_sulfur_design
CREATE TRIGGER "coalchp_furnace_calculation_a_7" AFTER UPDATE OF "s_sulfur_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification_s_sulfur_design"();


--该触发器用于：当f_calculation_consumption_design有更新时触发coalchp_desulfurization_denitrification.s_calcu_coal_consume=coalchp_furnace_calculation.f_calculation_consumption_design
CREATE TRIGGER "coalchp_furnace_calculation_a_8" AFTER UPDATE OF "f_calculation_consumption_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification_s_calcu_coal_consume"();


--该触发器用于：当i_standard_smoke_flow1_design有更新时触发coalchp_desulfurization_denitrification.s_fan_smoke_flow=coalchp_furnace_calculation.i_standard_smoke_flow1_design
CREATE TRIGGER "coalchp_furnace_calculation_a_9" AFTER UPDATE OF "i_standard_smoke_flow1_design" ON "public"."coalchp_furnace_calculation"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification_s_fan_smoke_flow"();


