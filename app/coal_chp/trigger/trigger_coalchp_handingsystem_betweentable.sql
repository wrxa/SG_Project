----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_furnace_calculation的b_boiler_rated_coal_capacity_design字段，和表coalchp_coal_handingsystem的f_boiler_consumption_design字段，即：coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_design=coalchp_furnace_calculation.f_boiler_consumption_design
CREATE OR REPLACE FUNCTION coalchp_coal_handingsystem_b_boiler_rated_coal_capacity_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_coal_handingsystem set b_boiler_rated_coal_capacity_design=coalchp_furnace_calculation.f_boiler_consumption_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_coal_handingsystem.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的b_boiler_rated_coal_capacity_check字段，和表coalchp_coal_handingsystem的f_boiler_consumption_check字段，即：coalchp_coal_handingsystem.b_boiler_rated_coal_capacity_check=coalchp_furnace_calculation.f_boiler_consumption_check
CREATE OR REPLACE FUNCTION coalchp_coal_handingsystem_b_boiler_rated_coal_capacity_check()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_coal_handingsystem set b_boiler_rated_coal_capacity_check=coalchp_furnace_calculation.f_boiler_consumption_check
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_coal_handingsystem.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;




