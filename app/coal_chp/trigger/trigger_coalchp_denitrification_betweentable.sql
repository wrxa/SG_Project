----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_furnace_calculation的s_sulfur_design字段，和表coalchp_desulfurization_denitrification的s_sulfur_design字段，即：coalchp_desulfurization_denitrification.s_sulfur_design=coalchp_furnace_calculation.s_sulfur_design
CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification_s_sulfur_design()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_desulfurization_denitrification set s_sulfur_design=coalchp_furnace_calculation.s_sulfur_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_desulfurization_denitrification.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的s_calcu_coal_consume字段，和表coalchp_desulfurization_denitrification的f_calculation_consumption_design字段，即：coalchp_desulfurization_denitrification.s_calcu_coal_consume=coalchp_furnace_calculation.f_calculation_consumption_design
CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification_s_calcu_coal_consume()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_desulfurization_denitrification set s_calcu_coal_consume=coalchp_furnace_calculation.f_calculation_consumption_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_desulfurization_denitrification.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--用于同步表：coalchp_furnace_calculation的s_fan_smoke_flow字段，和表coalchp_desulfurization_denitrification的i_standard_smoke_flow1_design字段，即：coalchp_desulfurization_denitrification.s_fan_smoke_flow=coalchp_furnace_calculation.i_standard_smoke_flow1_design
CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification_s_fan_smoke_flow()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_desulfurization_denitrification set s_fan_smoke_flow=coalchp_furnace_calculation.i_standard_smoke_flow1_design
  from coalchp_furnace_calculation where coalchp_furnace_calculation.plan_id=coalchp_desulfurization_denitrification.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;



----------------------创建触发函数-----------------------------------
--用于同步表：coalchp_needs_questionnaire的n_env_after_nox_concentration字段，和表coalchp_desulfurization_denitrification的op_flue_gas_nox_limits_value字段，即：coalchp_desulfurization_denitrification.n_env_after_nox_concentration=coalchp_needs_questionnaire.op_flue_gas_nox_limits_value
CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification_n_env_after_nox_concent()
RETURNS TRIGGER AS
$BODY$
BEGIN
  update coalchp_desulfurization_denitrification set n_env_after_nox_concentration=coalchp_needs_questionnaire.op_flue_gas_nox_limits_value
  from coalchp_needs_questionnaire where coalchp_needs_questionnaire.plan_id=coalchp_desulfurization_denitrification.plan_id;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;











