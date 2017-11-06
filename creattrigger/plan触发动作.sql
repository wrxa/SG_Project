CREATE OR REPLACE FUNCTION plan_id_insert()
RETURNS TRIGGER AS
$BODY$
DECLARE
  NEWIDD integer;

BEGIN
    NEWIDD = NEW.id;
		IF TG_OP='INSERT' THEN
		   INSERT INTO ccpp_ccpp (plan_id) VALUES (NEWIDD);
		   INSERT INTO ccpp_needs_questionnaire (plan_id) VALUES (NEWIDD);
       RETURN NULL;
	  END IF;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;

DELETE FROM pg_trigger WHERE tgname='plan_a_000001';
--删除级联记录
CREATE TRIGGER plan_a_000001
AFTER INSERT ON plan
FOR EACH ROW EXECUTE PROCEDURE plan_id_insert();
