CREATE OR REPLACE FUNCTION plan_id_insert()
RETURNS TRIGGER AS
$BODY$
DECLARE
  NEWIDD integer;
  MODULEID varchar(200);

BEGIN
    NEWIDD = NEW.id;
    MODULEID = NEW.module_id;
-- 燃煤热电联产
		IF TG_OP='INSERT' AND MODULEID='coalCHP' THEN

		    INSERT INTO coalchp_needs_questionnaire (plan_id) VALUES (NEWIDD);
		    INSERT INTO coalchp_furnace_calculation (plan_id) VALUES (NEWIDD);
		    RETURN NULL;
-- 生物质热电联产
		ELSEIF TG_OP='INSERT' AND MODULEID='biomassCHP' THEN

		    INSERT INTO biomasschp_needs_questionnaire (plan_id) VALUES (NEWIDD);
		    INSERT INTO biomasschp_boiler_calculation (plan_id) VALUES (NEWIDD);
		    INSERT INTO biomasschp_fuel_st (plan_id) VALUES (NEWIDD);
		    INSERT INTO biomasschp_des_den (plan_id) VALUES (NEWIDD);
		    INSERT INTO biomasschp_das_remove (plan_id) VALUES (NEWIDD);
			RETURN NULL;
-- CCPP
		ELSEIF TG_OP='INSERT' AND MODULEID='CCPP' THEN

		  INSERT INTO ccpp_questionnaire (plan_id) VALUES (NEWIDD);
			INSERT INTO ccpp_ccpp (plan_id) VALUES (NEWIDD);
			RETURN NULL;
-- 煤气发电
		ELSEIF TG_OP='INSERT' AND MODULEID='gasPowerGeneration' THEN

			INSERT INTO gaspowergeneration_needsquestionnaire (plan_id) VALUES (NEWIDD);


			RETURN NULL;
		END IF;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;

CREATE TRIGGER plan_a_000001
AFTER INSERT ON plan
FOR EACH ROW EXECUTE PROCEDURE plan_id_insert();
