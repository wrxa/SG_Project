CREATE OR REPLACE FUNCTION biomasschp_chimney()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段standard_calculated_smoke_density:标态下烟气密度,的计算1-----------------------------------
  IF OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature THEN
     update biomasschp_chimney set 

     standard_calculated_smoke_density=(NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_inlet_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.local_atmosphere ISNULL) AND NEW.chimney_inlet_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.local_atmosphere NOTNULL THEN
     update biomasschp_chimney set 

     standard_calculated_smoke_density=(NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_average_temperature:烟囱内平均温度,的计算2-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter THEN
     update biomasschp_chimney set 

     chimney_average_temperature=(NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.chimney_height NOTNULL THEN
     update biomasschp_chimney set 

     chimney_average_temperature=(NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_draft:烟囱抽力,的计算3-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_air_density != NEW.standard_air_density OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.outdoor_air_temperature != NEW.outdoor_air_temperature OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter THEN
     update biomasschp_chimney set 

     chimney_draft=9.8*(NEW.chimney_height)*((NEW.standard_air_density)*273/(273+(NEW.outdoor_air_temperature))-((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature)))*273/(273+((NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height))))*(NEW.local_atmosphere)/101325
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.outdoor_air_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.standard_air_density ISNULL OR OLD.local_atmosphere ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.outdoor_air_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.standard_air_density NOTNULL AND NEW.local_atmosphere NOTNULL AND NEW.chimney_height NOTNULL THEN
     update biomasschp_chimney set 

     chimney_draft=9.8*(NEW.chimney_height)*((NEW.standard_air_density)*273/(273+(NEW.outdoor_air_temperature))-((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature)))*273/(273+((NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height))))*(NEW.local_atmosphere)/101325
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_outlet_temperature:烟囱出口温度,的计算4-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter THEN
     update biomasschp_chimney set 

     chimney_outlet_temperature=((NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.chimney_height NOTNULL THEN
     update biomasschp_chimney set 

     chimney_outlet_temperature=((NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_outlet_inner_diameter:烟囱出口内径,的计算5-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter OR OLD.smoke_amount != NEW.smoke_amount OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow THEN
     update biomasschp_chimney set 

     chimney_outlet_inner_diameter=((NEW.smoke_amount)*((((NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height)))+273)/(3600*273*0.785*(NEW.chimney_outlet_flow)))^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_flow ISNULL OR OLD.smoke_amount ISNULL OR OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_outlet_flow NOTNULL AND NEW.smoke_amount NOTNULL AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.chimney_height NOTNULL THEN
     update biomasschp_chimney set 

     chimney_outlet_inner_diameter=((NEW.smoke_amount)*((((NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height)))+273)/(3600*273*0.785*(NEW.chimney_outlet_flow)))^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_experience_base_diameter:经验烟囱基础内径,的计算6-----------------------------------
  IF OLD.chimney_outlet_selected_inner_diameter != NEW.chimney_outlet_selected_inner_diameter THEN
     update biomasschp_chimney set 

     chimney_experience_base_diameter=(NEW.chimney_outlet_selected_inner_diameter)+2*(NEW.chimney_outlet_selected_inner_diameter)*0.02
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_selected_inner_diameter ISNULL) AND NEW.chimney_outlet_selected_inner_diameter NOTNULL THEN
     update biomasschp_chimney set 

     chimney_experience_base_diameter=(NEW.chimney_outlet_selected_inner_diameter)+2*(NEW.chimney_outlet_selected_inner_diameter)*0.02
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_load_smoke_amount:低负荷下烟气量,的计算7-----------------------------------
  IF OLD.smoke_amount != NEW.smoke_amount THEN
     update biomasschp_chimney set 

     low_load_smoke_amount=0.3*(NEW.smoke_amount)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.smoke_amount ISNULL) AND NEW.smoke_amount NOTNULL THEN
     update biomasschp_chimney set 

     low_load_smoke_amount=0.3*(NEW.smoke_amount)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段low_load_flow_30_percent:30%低负荷校核流速,的计算8-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_temperature_drop_per_meter != NEW.chimney_temperature_drop_per_meter OR OLD.smoke_amount != NEW.smoke_amount OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow OR OLD.low_load_smoke_temperature != NEW.low_load_smoke_temperature THEN
     update biomasschp_chimney set 

     low_load_flow_30_percent=(0.3*(NEW.smoke_amount))*(273+(NEW.low_load_smoke_temperature))/((((NEW.smoke_amount)*((((NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height)))+273)/(3600*273*0.785*(NEW.chimney_outlet_flow)))^0.5))^2/3600/273/0.7854
     where plan_id=NEW.plan_id;

  ELSIF (OLD.low_load_smoke_temperature ISNULL OR OLD.chimney_outlet_flow ISNULL OR OLD.smoke_amount ISNULL OR OLD.chimney_temperature_drop_per_meter ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.chimney_height ISNULL) AND NEW.low_load_smoke_temperature NOTNULL AND NEW.chimney_outlet_flow NOTNULL AND NEW.smoke_amount NOTNULL AND NEW.chimney_temperature_drop_per_meter NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.chimney_height NOTNULL THEN
     update biomasschp_chimney set 

     low_load_flow_30_percent=(0.3*(NEW.smoke_amount))*(273+(NEW.low_load_smoke_temperature))/((((NEW.smoke_amount)*((((NEW.chimney_inlet_temperature)-0.5*(NEW.chimney_temperature_drop_per_meter)*(NEW.chimney_height)))+273)/(3600*273*0.785*(NEW.chimney_outlet_flow)))^0.5))^2/3600/273/0.7854
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_average_velocity:烟囱内平均流速,的计算9-----------------------------------
  IF OLD.chimney_outlet_flow != NEW.chimney_outlet_flow THEN
     update biomasschp_chimney set 

     chimney_average_velocity=(NEW.chimney_outlet_flow)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_flow ISNULL) AND NEW.chimney_outlet_flow NOTNULL THEN
     update biomasschp_chimney set 

     chimney_average_velocity=(NEW.chimney_outlet_flow)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_average_diameter:烟囱平均直径,的计算10-----------------------------------
  IF OLD.chimney_outlet_selected_inner_diameter != NEW.chimney_outlet_selected_inner_diameter THEN
     update biomasschp_chimney set 

     chimney_average_diameter=(((NEW.chimney_outlet_selected_inner_diameter)+2*(NEW.chimney_outlet_selected_inner_diameter)*0.02)+(NEW.chimney_outlet_selected_inner_diameter))/2/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_selected_inner_diameter ISNULL) AND NEW.chimney_outlet_selected_inner_diameter NOTNULL THEN
     update biomasschp_chimney set 

     chimney_average_diameter=(((NEW.chimney_outlet_selected_inner_diameter)+2*(NEW.chimney_outlet_selected_inner_diameter)*0.02)+(NEW.chimney_outlet_selected_inner_diameter))/2/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_friction_resistance:烟囱摩擦阻力,的计算11-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow OR OLD.chimney_outlet_selected_inner_diameter != NEW.chimney_outlet_selected_inner_diameter OR OLD.chimney_resistance_coefficient != NEW.chimney_resistance_coefficient THEN
     update biomasschp_chimney set 

     chimney_friction_resistance=(NEW.chimney_resistance_coefficient)*(NEW.chimney_height)*((NEW.chimney_outlet_flow))*((NEW.chimney_outlet_flow))/((((NEW.chimney_outlet_selected_inner_diameter)+2*(NEW.chimney_outlet_selected_inner_diameter)*0.02)+(NEW.chimney_outlet_selected_inner_diameter))/2/1000)/2*((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_resistance_coefficient ISNULL OR OLD.chimney_outlet_selected_inner_diameter ISNULL OR OLD.chimney_outlet_flow ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.local_atmosphere ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_resistance_coefficient NOTNULL AND NEW.chimney_outlet_selected_inner_diameter NOTNULL AND NEW.chimney_outlet_flow NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.local_atmosphere NOTNULL AND NEW.chimney_height NOTNULL THEN
     update biomasschp_chimney set 

     chimney_friction_resistance=(NEW.chimney_resistance_coefficient)*(NEW.chimney_height)*((NEW.chimney_outlet_flow))*((NEW.chimney_outlet_flow))/((((NEW.chimney_outlet_selected_inner_diameter)+2*(NEW.chimney_outlet_selected_inner_diameter)*0.02)+(NEW.chimney_outlet_selected_inner_diameter))/2/1000)/2*((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_outlet_resistance:烟囱出口阻力,的计算12-----------------------------------
  IF OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow OR OLD.chimney_outlet_resistance_coefficient != NEW.chimney_outlet_resistance_coefficient THEN
     update biomasschp_chimney set 

     chimney_outlet_resistance=(NEW.chimney_outlet_resistance_coefficient)*((NEW.chimney_outlet_flow))*((NEW.chimney_outlet_flow))/2*((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_resistance_coefficient ISNULL OR OLD.chimney_outlet_flow ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.local_atmosphere ISNULL) AND NEW.chimney_outlet_resistance_coefficient NOTNULL AND NEW.chimney_outlet_flow NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.local_atmosphere NOTNULL THEN
     update biomasschp_chimney set 

     chimney_outlet_resistance=(NEW.chimney_outlet_resistance_coefficient)*((NEW.chimney_outlet_flow))*((NEW.chimney_outlet_flow))/2*((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段chimney_total_resistance:烟囱总阻力,的计算13-----------------------------------
  IF OLD.chimney_height != NEW.chimney_height OR OLD.local_atmosphere != NEW.local_atmosphere OR OLD.standard_average_smoke_density != NEW.standard_average_smoke_density OR OLD.chimney_inlet_temperature != NEW.chimney_inlet_temperature OR OLD.chimney_outlet_flow != NEW.chimney_outlet_flow OR OLD.chimney_outlet_selected_inner_diameter != NEW.chimney_outlet_selected_inner_diameter OR OLD.chimney_resistance_coefficient != NEW.chimney_resistance_coefficient OR OLD.chimney_outlet_resistance_coefficient != NEW.chimney_outlet_resistance_coefficient THEN
     update biomasschp_chimney set 

     chimney_total_resistance=((NEW.chimney_outlet_resistance_coefficient)*((NEW.chimney_outlet_flow))*((NEW.chimney_outlet_flow))/2*((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature))))+((NEW.chimney_resistance_coefficient)*(NEW.chimney_height)*((NEW.chimney_outlet_flow))*((NEW.chimney_outlet_flow))/((((NEW.chimney_outlet_selected_inner_diameter)+2*(NEW.chimney_outlet_selected_inner_diameter)*0.02)+(NEW.chimney_outlet_selected_inner_diameter))/2/1000)/2*((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.chimney_outlet_resistance_coefficient ISNULL OR OLD.chimney_resistance_coefficient ISNULL OR OLD.chimney_outlet_selected_inner_diameter ISNULL OR OLD.chimney_outlet_flow ISNULL OR OLD.chimney_inlet_temperature ISNULL OR OLD.standard_average_smoke_density ISNULL OR OLD.local_atmosphere ISNULL OR OLD.chimney_height ISNULL) AND NEW.chimney_outlet_resistance_coefficient NOTNULL AND NEW.chimney_resistance_coefficient NOTNULL AND NEW.chimney_outlet_selected_inner_diameter NOTNULL AND NEW.chimney_outlet_flow NOTNULL AND NEW.chimney_inlet_temperature NOTNULL AND NEW.standard_average_smoke_density NOTNULL AND NEW.local_atmosphere NOTNULL AND NEW.chimney_height NOTNULL THEN
     update biomasschp_chimney set 

     chimney_total_resistance=((NEW.chimney_outlet_resistance_coefficient)*((NEW.chimney_outlet_flow))*((NEW.chimney_outlet_flow))/2*((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature))))+((NEW.chimney_resistance_coefficient)*(NEW.chimney_height)*((NEW.chimney_outlet_flow))*((NEW.chimney_outlet_flow))/((((NEW.chimney_outlet_selected_inner_diameter)+2*(NEW.chimney_outlet_selected_inner_diameter)*0.02)+(NEW.chimney_outlet_selected_inner_diameter))/2/1000)/2*((NEW.standard_average_smoke_density)*273*(NEW.local_atmosphere)/101325/(273+(NEW.chimney_inlet_temperature))))
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "biomasschp_chimney" AFTER UPDATE OF
"chimney_height",
"local_atmosphere",
"standard_air_density",
"standard_average_smoke_density",
"outdoor_air_temperature",
"chimney_inlet_temperature",
"chimney_temperature_drop_per_meter",
"smoke_amount",
"chimney_outlet_flow",
"chimney_outlet_selected_inner_diameter",
"low_load_smoke_temperature",
"chimney_resistance_coefficient",
"chimney_outlet_resistance_coefficient"
ON "public"."biomasschp_chimney"
FOR EACH ROW
EXECUTE PROCEDURE "biomasschp_chimney"();

