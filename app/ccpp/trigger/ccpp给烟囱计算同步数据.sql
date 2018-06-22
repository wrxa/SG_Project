----------------------创建触发函数-----------------------------------
--用于同步表：ccpp_ccpp的flue_gas_quantity字段，和表ccpp_chimney_calculate的high_engine_exhuast_gas_flux_design字段，即：ccpp_chimney_calculate.flue_gas_quantity=ccpp_ccpp.high_engine_exhuast_gas_flux_design
CREATE OR REPLACE FUNCTION ccpp_chimney_calculate_flue_gas_quantity()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update ccpp_chimney_calculate set flue_gas_quantity=ccpp_ccpp.high_engine_exhuast_gas_flux_design
  from ccpp_ccpp where ccpp_ccpp.plan_id=ccpp_chimney_calculate.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


----------------------创建触发器-----------------------------------

--该触发器用于：当high_engine_exhuast_gas_flux_design有更新时触发ccpp_chimney_calculate.flue_gas_quantity=ccpp_ccpp.high_engine_exhuast_gas_flux_design
CREATE TRIGGER "ccpp_ccpp_a_0" AFTER UPDATE OF "high_engine_exhuast_gas_flux_design" ON "public"."ccpp_ccpp"
FOR EACH ROW
EXECUTE PROCEDURE "ccpp_chimney_calculate_flue_gas_quantity"();