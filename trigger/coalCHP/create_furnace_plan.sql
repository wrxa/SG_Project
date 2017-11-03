CREATE OR REPLACE FUNCTION plan_id_insert()
RETURNS TRIGGER AS
$BODY$
DECLARE
  NEWIDD integer;

BEGIN
    NEWIDD = NEW.id;
		IF TG_OP='INSERT' THEN
		   INSERT INTO coalchp_needs_questionnaire (plan_id) VALUES (NEWIDD);
		   INSERT INTO coalchp_furnace_calculation (plan_id) VALUES (NEWIDD);
       RETURN NULL;
	  END IF;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;

--删除级联记录
CREATE TRIGGER plan_a_000001
AFTER INSERT ON plan
FOR EACH ROW EXECUTE PROCEDURE plan_id_insert();
