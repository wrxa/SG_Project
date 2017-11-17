CREATE OR REPLACE FUNCTION gaspowergeneration_wind_resistance()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段intake_to_preheater_dynamic_pressure_head:动压头,的计算1-----------------------------------
  IF OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     intake_to_preheater_dynamic_pressure_head=(NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL) AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     intake_to_preheater_dynamic_pressure_head=(NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_duct_section_area:风管截面积,的计算2-----------------------------------
  IF OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_duct_section_area=(NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_duct_section_area=(NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_duct_width:宽,的计算3-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_duct_width=((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_duct_width=((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_duct_perimeter:风管周长,的计算4-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_duct_perimeter=2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_duct_perimeter=2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_duct_equivalent_diameter:管道当量直径,的计算5-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_duct_equivalent_diameter=4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_duct_equivalent_diameter=4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_reynolds_number:雷诺数,的计算6-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_gas_kinetic_viscosity != NEW.fan_inlet_gas_kinetic_viscosity OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_reynolds_number=(NEW.intake_to_preheater_flow_velocity)*(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))/(NEW.fan_inlet_gas_kinetic_viscosity)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_gas_kinetic_viscosity ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_gas_kinetic_viscosity NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_reynolds_number=(NEW.intake_to_preheater_flow_velocity)*(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))/(NEW.fan_inlet_gas_kinetic_viscosity)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_relative_tube_roughness:管道内壁相对对粗糙度,的计算7-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_absolute_tube_roughness != NEW.fan_inlet_absolute_tube_roughness OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_relative_tube_roughness=(NEW.fan_inlet_absolute_tube_roughness)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_absolute_tube_roughness ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_absolute_tube_roughness NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_relative_tube_roughness=(NEW.fan_inlet_absolute_tube_roughness)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_560_relative_tube_roughness:560/△1,的计算8-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_absolute_tube_roughness != NEW.fan_inlet_absolute_tube_roughness OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_560_relative_tube_roughness=560/((NEW.fan_inlet_absolute_tube_roughness)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_absolute_tube_roughness ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_absolute_tube_roughness NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_560_relative_tube_roughness=560/((NEW.fan_inlet_absolute_tube_roughness)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_frictional_resistance:摩擦阻力,的计算9-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_frictional_resistance_coefficient != NEW.fan_inlet_frictional_resistance_coefficient OR OLD.fan_inlet_ducting_length != NEW.fan_inlet_ducting_length OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_frictional_resistance=(NEW.fan_inlet_ducting_length)*((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_ducting_length ISNULL OR OLD.fan_inlet_frictional_resistance_coefficient ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_ducting_length NOTNULL AND NEW.fan_inlet_frictional_resistance_coefficient NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_frictional_resistance=(NEW.fan_inlet_ducting_length)*((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_unit_length_frictional_resistance:单位长度摩擦阻力,的计算10-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_frictional_resistance_coefficient != NEW.fan_inlet_frictional_resistance_coefficient OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_unit_length_frictional_resistance=(NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_frictional_resistance_coefficient ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_frictional_resistance_coefficient NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_unit_length_frictional_resistance=(NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_local_resistance:局部阻力,的计算11-----------------------------------
  IF OLD.fan_inlet_single_local_resistance_coefficient != NEW.fan_inlet_single_local_resistance_coefficient OR OLD.fan_inlet_single_bellows != NEW.fan_inlet_single_bellows OR OLD.fan_inlet_single_damper != NEW.fan_inlet_single_damper OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_local_resistance=((NEW.fan_inlet_single_local_resistance_coefficient)+(NEW.fan_inlet_single_bellows)+(NEW.fan_inlet_single_damper))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_single_damper ISNULL OR OLD.fan_inlet_single_bellows ISNULL OR OLD.fan_inlet_single_local_resistance_coefficient ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL) AND NEW.fan_inlet_single_damper NOTNULL AND NEW.fan_inlet_single_bellows NOTNULL AND NEW.fan_inlet_single_local_resistance_coefficient NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_local_resistance=((NEW.fan_inlet_single_local_resistance_coefficient)+(NEW.fan_inlet_single_bellows)+(NEW.fan_inlet_single_damper))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_local_resistance_coefficient:局部阻力系数,的计算12-----------------------------------
  IF OLD.fan_inlet_single_local_resistance_coefficient != NEW.fan_inlet_single_local_resistance_coefficient OR OLD.fan_inlet_single_bellows != NEW.fan_inlet_single_bellows OR OLD.fan_inlet_single_damper != NEW.fan_inlet_single_damper THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_local_resistance_coefficient=(NEW.fan_inlet_single_local_resistance_coefficient)+(NEW.fan_inlet_single_bellows)+(NEW.fan_inlet_single_damper)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_single_damper ISNULL OR OLD.fan_inlet_single_bellows ISNULL OR OLD.fan_inlet_single_local_resistance_coefficient ISNULL) AND NEW.fan_inlet_single_damper NOTNULL AND NEW.fan_inlet_single_bellows NOTNULL AND NEW.fan_inlet_single_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_local_resistance_coefficient=(NEW.fan_inlet_single_local_resistance_coefficient)+(NEW.fan_inlet_single_bellows)+(NEW.fan_inlet_single_damper)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_inlet_total_pressure:风机进口段总阻力,的计算13-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_frictional_resistance_coefficient != NEW.fan_inlet_frictional_resistance_coefficient OR OLD.fan_inlet_ducting_length != NEW.fan_inlet_ducting_length OR OLD.fan_inlet_single_local_resistance_coefficient != NEW.fan_inlet_single_local_resistance_coefficient OR OLD.fan_inlet_single_bellows != NEW.fan_inlet_single_bellows OR OLD.fan_inlet_single_damper != NEW.fan_inlet_single_damper OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_total_pressure=(((NEW.fan_inlet_single_local_resistance_coefficient)+(NEW.fan_inlet_single_bellows)+(NEW.fan_inlet_single_damper))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2))+((NEW.fan_inlet_ducting_length)*((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_single_damper ISNULL OR OLD.fan_inlet_single_bellows ISNULL OR OLD.fan_inlet_single_local_resistance_coefficient ISNULL OR OLD.fan_inlet_ducting_length ISNULL OR OLD.fan_inlet_frictional_resistance_coefficient ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_single_damper NOTNULL AND NEW.fan_inlet_single_bellows NOTNULL AND NEW.fan_inlet_single_local_resistance_coefficient NOTNULL AND NEW.fan_inlet_ducting_length NOTNULL AND NEW.fan_inlet_frictional_resistance_coefficient NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_inlet_total_pressure=(((NEW.fan_inlet_single_local_resistance_coefficient)+(NEW.fan_inlet_single_bellows)+(NEW.fan_inlet_single_damper))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2))+((NEW.fan_inlet_ducting_length)*((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_outlet_frictional_resistance:摩擦阻力,的计算14-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_frictional_resistance_coefficient != NEW.fan_inlet_frictional_resistance_coefficient OR OLD.fan_outlet_ducting_length != NEW.fan_outlet_ducting_length OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_frictional_resistance=(NEW.fan_outlet_ducting_length)*(((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_outlet_ducting_length ISNULL OR OLD.fan_inlet_frictional_resistance_coefficient ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_outlet_ducting_length NOTNULL AND NEW.fan_inlet_frictional_resistance_coefficient NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_frictional_resistance=(NEW.fan_outlet_ducting_length)*(((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_outlet_unit_length_frictional_resistance:单位长度摩擦阻力,的计算15-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_frictional_resistance_coefficient != NEW.fan_inlet_frictional_resistance_coefficient OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_unit_length_frictional_resistance=((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_inlet_frictional_resistance_coefficient ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_inlet_frictional_resistance_coefficient NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_unit_length_frictional_resistance=((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_outlet_local_resistance:局部阻力,的计算16-----------------------------------
  IF OLD.fan_outlet_single_increase_pipe != NEW.fan_outlet_single_increase_pipe OR OLD.fan_outlet_90_section_slow_turn_elbow != NEW.fan_outlet_90_section_slow_turn_elbow OR OLD.fan_outlet_preheater_diffuser_pipe != NEW.fan_outlet_preheater_diffuser_pipe OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_local_resistance=((NEW.fan_outlet_single_increase_pipe)+(NEW.fan_outlet_90_section_slow_turn_elbow)+(NEW.fan_outlet_preheater_diffuser_pipe))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_outlet_preheater_diffuser_pipe ISNULL OR OLD.fan_outlet_90_section_slow_turn_elbow ISNULL OR OLD.fan_outlet_single_increase_pipe ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL) AND NEW.fan_outlet_preheater_diffuser_pipe NOTNULL AND NEW.fan_outlet_90_section_slow_turn_elbow NOTNULL AND NEW.fan_outlet_single_increase_pipe NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_local_resistance=((NEW.fan_outlet_single_increase_pipe)+(NEW.fan_outlet_90_section_slow_turn_elbow)+(NEW.fan_outlet_preheater_diffuser_pipe))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_outlet_local_resistance_coefficient:局部阻力系数,的计算17-----------------------------------
  IF OLD.fan_outlet_single_increase_pipe != NEW.fan_outlet_single_increase_pipe OR OLD.fan_outlet_90_section_slow_turn_elbow != NEW.fan_outlet_90_section_slow_turn_elbow OR OLD.fan_outlet_preheater_diffuser_pipe != NEW.fan_outlet_preheater_diffuser_pipe THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_local_resistance_coefficient=(NEW.fan_outlet_single_increase_pipe)+(NEW.fan_outlet_90_section_slow_turn_elbow)+(NEW.fan_outlet_preheater_diffuser_pipe)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_outlet_preheater_diffuser_pipe ISNULL OR OLD.fan_outlet_90_section_slow_turn_elbow ISNULL OR OLD.fan_outlet_single_increase_pipe ISNULL) AND NEW.fan_outlet_preheater_diffuser_pipe NOTNULL AND NEW.fan_outlet_90_section_slow_turn_elbow NOTNULL AND NEW.fan_outlet_single_increase_pipe NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_local_resistance_coefficient=(NEW.fan_outlet_single_increase_pipe)+(NEW.fan_outlet_90_section_slow_turn_elbow)+(NEW.fan_outlet_preheater_diffuser_pipe)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段fan_outlet_to_preheater_total_pressure:风机出口至空预器总阻力,的计算18-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_frictional_resistance_coefficient != NEW.fan_inlet_frictional_resistance_coefficient OR OLD.fan_outlet_ducting_length != NEW.fan_outlet_ducting_length OR OLD.fan_outlet_single_increase_pipe != NEW.fan_outlet_single_increase_pipe OR OLD.fan_outlet_90_section_slow_turn_elbow != NEW.fan_outlet_90_section_slow_turn_elbow OR OLD.fan_outlet_preheater_diffuser_pipe != NEW.fan_outlet_preheater_diffuser_pipe OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_to_preheater_total_pressure=((NEW.fan_outlet_ducting_length)*(((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))))+(((NEW.fan_outlet_single_increase_pipe)+(NEW.fan_outlet_90_section_slow_turn_elbow)+(NEW.fan_outlet_preheater_diffuser_pipe))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.fan_outlet_preheater_diffuser_pipe ISNULL OR OLD.fan_outlet_90_section_slow_turn_elbow ISNULL OR OLD.fan_outlet_single_increase_pipe ISNULL OR OLD.fan_outlet_ducting_length ISNULL OR OLD.fan_inlet_frictional_resistance_coefficient ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.fan_outlet_preheater_diffuser_pipe NOTNULL AND NEW.fan_outlet_90_section_slow_turn_elbow NOTNULL AND NEW.fan_outlet_single_increase_pipe NOTNULL AND NEW.fan_outlet_ducting_length NOTNULL AND NEW.fan_inlet_frictional_resistance_coefficient NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     fan_outlet_to_preheater_total_pressure=((NEW.fan_outlet_ducting_length)*(((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))))+(((NEW.fan_outlet_single_increase_pipe)+(NEW.fan_outlet_90_section_slow_turn_elbow)+(NEW.fan_outlet_preheater_diffuser_pipe))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_to_boiler_temperature:计算温度,的计算19-----------------------------------
  IF OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount THEN
     update gaspowergeneration_wind_resistance set 

     preheater_to_boiler_temperature=(NEW.intake_to_preheater_amount)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.intake_to_preheater_amount ISNULL) AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_to_boiler_temperature=(NEW.intake_to_preheater_amount)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_to_boiler_dynamic_pressure_head:动压头,的计算20-----------------------------------
  IF OLD.preheater_to_boiler_density != NEW.preheater_to_boiler_density OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     preheater_to_boiler_dynamic_pressure_head=(NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_density ISNULL) AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_density NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_to_boiler_dynamic_pressure_head=(NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_duct_section_area:风管截面积（热风管分两路进入风室）,的计算21-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_section_area=(NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_section_area=(NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_duct_diameter:圆管直径(一、二次热风为圆管）,的计算22-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_diameter=(((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_diameter=(((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_duct_width:宽,的计算23-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_duct_length != NEW.preheater_outlet_duct_length THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_width=((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/(NEW.preheater_outlet_duct_length)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_duct_length ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_outlet_duct_length NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_width=((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/(NEW.preheater_outlet_duct_length)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_duct_perimeter:风管周长,的计算24-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_duct_length != NEW.preheater_outlet_duct_length THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_perimeter=2*((NEW.preheater_outlet_duct_length)+(((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/(NEW.preheater_outlet_duct_length)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_duct_length ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_outlet_duct_length NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_perimeter=2*((NEW.preheater_outlet_duct_length)+(((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/(NEW.preheater_outlet_duct_length)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_duct_equivalent_diameter:管道当量直径,的计算25-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_duct_length != NEW.preheater_outlet_duct_length THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_equivalent_diameter=4*((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/(2*((NEW.preheater_outlet_duct_length)+(((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/(NEW.preheater_outlet_duct_length))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_duct_length ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_outlet_duct_length NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_duct_equivalent_diameter=4*((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/(2*((NEW.preheater_outlet_duct_length)+(((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/(NEW.preheater_outlet_duct_length))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_gas_kinetic_viscosity:气体运动粘度,的计算26-----------------------------------
  IF OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_gas_kinetic_viscosity=((34.94-23.08)*(((NEW.intake_to_preheater_amount))-100)/100+23.08)/1000000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.intake_to_preheater_amount ISNULL) AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_gas_kinetic_viscosity=((34.94-23.08)*(((NEW.intake_to_preheater_amount))-100)/100+23.08)/1000000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_reynolds_number:雷诺数,的计算27-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_reynolds_number=(NEW.preheater_to_boiler_flow_velocity)*((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5)/(((34.94-23.08)*(((NEW.intake_to_preheater_amount))-100)/100+23.08)/1000000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_amount ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_reynolds_number=(NEW.preheater_to_boiler_flow_velocity)*((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5)/(((34.94-23.08)*(((NEW.intake_to_preheater_amount))-100)/100+23.08)/1000000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_relative_tube_roughness:管道内壁相对对粗糙度,的计算28-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_absolute_tube_roughness != NEW.preheater_outlet_absolute_tube_roughness THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_relative_tube_roughness=(NEW.preheater_outlet_absolute_tube_roughness)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_absolute_tube_roughness ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_outlet_absolute_tube_roughness NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_relative_tube_roughness=(NEW.preheater_outlet_absolute_tube_roughness)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_560_relative_tube_roughness:560/△1,的计算29-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_absolute_tube_roughness != NEW.preheater_outlet_absolute_tube_roughness THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_560_relative_tube_roughness=560/((NEW.preheater_outlet_absolute_tube_roughness)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_absolute_tube_roughness ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_outlet_absolute_tube_roughness NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_560_relative_tube_roughness=560/((NEW.preheater_outlet_absolute_tube_roughness)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_frictional_resistance:摩擦阻力,的计算30-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_density != NEW.preheater_to_boiler_density OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_frictional_resistance_coefficient != NEW.preheater_outlet_frictional_resistance_coefficient OR OLD.preheater_outlet_ducting_length != NEW.preheater_outlet_ducting_length THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_frictional_resistance=(NEW.preheater_outlet_ducting_length)*((NEW.preheater_outlet_frictional_resistance_coefficient)*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_ducting_length ISNULL OR OLD.preheater_outlet_frictional_resistance_coefficient ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_density ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_outlet_ducting_length NOTNULL AND NEW.preheater_outlet_frictional_resistance_coefficient NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_density NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_frictional_resistance=(NEW.preheater_outlet_ducting_length)*((NEW.preheater_outlet_frictional_resistance_coefficient)*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_unit_length_frictional_resistance:单位长度摩擦阻力,的计算31-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_density != NEW.preheater_to_boiler_density OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_frictional_resistance_coefficient != NEW.preheater_outlet_frictional_resistance_coefficient THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_unit_length_frictional_resistance=(NEW.preheater_outlet_frictional_resistance_coefficient)*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_frictional_resistance_coefficient ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_density ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_outlet_frictional_resistance_coefficient NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_density NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_unit_length_frictional_resistance=(NEW.preheater_outlet_frictional_resistance_coefficient)*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_local_resistance:局部阻力,的计算32-----------------------------------
  IF OLD.preheater_to_boiler_density != NEW.preheater_to_boiler_density OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_shrink_pipe != NEW.preheater_outlet_shrink_pipe OR OLD.preheater_outlet_90_sharp_turn_elbow_count != NEW.preheater_outlet_90_sharp_turn_elbow_count OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance != NEW.preheater_outlet_90_sharp_turn_elbow_resistance OR OLD.preheater_outlet_air_intake_gate != NEW.preheater_outlet_air_intake_gate OR OLD.preheater_outlet_combustor_gate != NEW.preheater_outlet_combustor_gate THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_local_resistance=((NEW.preheater_outlet_shrink_pipe)+((NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance))+(NEW.preheater_outlet_air_intake_gate)+(NEW.preheater_outlet_combustor_gate))*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_combustor_gate ISNULL OR OLD.preheater_outlet_air_intake_gate ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_count ISNULL OR OLD.preheater_outlet_shrink_pipe ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_density ISNULL) AND NEW.preheater_outlet_combustor_gate NOTNULL AND NEW.preheater_outlet_air_intake_gate NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_resistance NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_count NOTNULL AND NEW.preheater_outlet_shrink_pipe NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_density NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_local_resistance=((NEW.preheater_outlet_shrink_pipe)+((NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance))+(NEW.preheater_outlet_air_intake_gate)+(NEW.preheater_outlet_combustor_gate))*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_local_resistance_coefficient:局部阻力系数,的计算33-----------------------------------
  IF OLD.preheater_outlet_shrink_pipe != NEW.preheater_outlet_shrink_pipe OR OLD.preheater_outlet_90_sharp_turn_elbow_count != NEW.preheater_outlet_90_sharp_turn_elbow_count OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance != NEW.preheater_outlet_90_sharp_turn_elbow_resistance OR OLD.preheater_outlet_air_intake_gate != NEW.preheater_outlet_air_intake_gate OR OLD.preheater_outlet_combustor_gate != NEW.preheater_outlet_combustor_gate THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_local_resistance_coefficient=(NEW.preheater_outlet_shrink_pipe)+((NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance))+(NEW.preheater_outlet_air_intake_gate)+(NEW.preheater_outlet_combustor_gate)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_combustor_gate ISNULL OR OLD.preheater_outlet_air_intake_gate ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_count ISNULL OR OLD.preheater_outlet_shrink_pipe ISNULL) AND NEW.preheater_outlet_combustor_gate NOTNULL AND NEW.preheater_outlet_air_intake_gate NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_resistance NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_count NOTNULL AND NEW.preheater_outlet_shrink_pipe NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_local_resistance_coefficient=(NEW.preheater_outlet_shrink_pipe)+((NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance))+(NEW.preheater_outlet_air_intake_gate)+(NEW.preheater_outlet_combustor_gate)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_90_sharp_turn_elbow:6只90度等截面急转弯头,的计算34-----------------------------------
  IF OLD.preheater_outlet_90_sharp_turn_elbow_count != NEW.preheater_outlet_90_sharp_turn_elbow_count OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance != NEW.preheater_outlet_90_sharp_turn_elbow_resistance THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_90_sharp_turn_elbow=(NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_90_sharp_turn_elbow_resistance ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_count ISNULL) AND NEW.preheater_outlet_90_sharp_turn_elbow_resistance NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_count NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_90_sharp_turn_elbow=(NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段preheater_outlet_to_boiler_total_pressure:空预器出口至锅炉风室总阻力,的计算35-----------------------------------
  IF OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_density != NEW.preheater_to_boiler_density OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_frictional_resistance_coefficient != NEW.preheater_outlet_frictional_resistance_coefficient OR OLD.preheater_outlet_ducting_length != NEW.preheater_outlet_ducting_length OR OLD.preheater_outlet_shrink_pipe != NEW.preheater_outlet_shrink_pipe OR OLD.preheater_outlet_90_sharp_turn_elbow_count != NEW.preheater_outlet_90_sharp_turn_elbow_count OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance != NEW.preheater_outlet_90_sharp_turn_elbow_resistance OR OLD.preheater_outlet_air_intake_gate != NEW.preheater_outlet_air_intake_gate OR OLD.preheater_outlet_combustor_gate != NEW.preheater_outlet_combustor_gate THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_to_boiler_total_pressure=(((NEW.preheater_outlet_shrink_pipe)+((NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance))+(NEW.preheater_outlet_air_intake_gate)+(NEW.preheater_outlet_combustor_gate))*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2))+((NEW.preheater_outlet_ducting_length)*((NEW.preheater_outlet_frictional_resistance_coefficient)*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_combustor_gate ISNULL OR OLD.preheater_outlet_air_intake_gate ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_count ISNULL OR OLD.preheater_outlet_shrink_pipe ISNULL OR OLD.preheater_outlet_ducting_length ISNULL OR OLD.preheater_outlet_frictional_resistance_coefficient ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_density ISNULL OR OLD.preheater_to_boiler_amount ISNULL) AND NEW.preheater_outlet_combustor_gate NOTNULL AND NEW.preheater_outlet_air_intake_gate NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_resistance NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_count NOTNULL AND NEW.preheater_outlet_shrink_pipe NOTNULL AND NEW.preheater_outlet_ducting_length NOTNULL AND NEW.preheater_outlet_frictional_resistance_coefficient NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_density NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     preheater_outlet_to_boiler_total_pressure=(((NEW.preheater_outlet_shrink_pipe)+((NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance))+(NEW.preheater_outlet_air_intake_gate)+(NEW.preheater_outlet_combustor_gate))*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2))+((NEW.preheater_outlet_ducting_length)*((NEW.preheater_outlet_frictional_resistance_coefficient)*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段windhole_total_pressure:风道总阻力,的计算36-----------------------------------
  IF OLD.fan_inlet_duct_length != NEW.fan_inlet_duct_length OR OLD.fan_inlet_frictional_resistance_coefficient != NEW.fan_inlet_frictional_resistance_coefficient OR OLD.fan_inlet_ducting_length != NEW.fan_inlet_ducting_length OR OLD.fan_inlet_single_local_resistance_coefficient != NEW.fan_inlet_single_local_resistance_coefficient OR OLD.fan_inlet_single_bellows != NEW.fan_inlet_single_bellows OR OLD.fan_inlet_single_damper != NEW.fan_inlet_single_damper OR OLD.fan_outlet_ducting_length != NEW.fan_outlet_ducting_length OR OLD.fan_outlet_single_increase_pipe != NEW.fan_outlet_single_increase_pipe OR OLD.fan_outlet_90_section_slow_turn_elbow != NEW.fan_outlet_90_section_slow_turn_elbow OR OLD.fan_outlet_preheater_diffuser_pipe != NEW.fan_outlet_preheater_diffuser_pipe OR OLD.preheater_to_boiler_amount != NEW.preheater_to_boiler_amount OR OLD.preheater_to_boiler_density != NEW.preheater_to_boiler_density OR OLD.preheater_to_boiler_flow_velocity != NEW.preheater_to_boiler_flow_velocity OR OLD.preheater_outlet_frictional_resistance_coefficient != NEW.preheater_outlet_frictional_resistance_coefficient OR OLD.preheater_outlet_ducting_length != NEW.preheater_outlet_ducting_length OR OLD.preheater_outlet_shrink_pipe != NEW.preheater_outlet_shrink_pipe OR OLD.preheater_outlet_90_sharp_turn_elbow_count != NEW.preheater_outlet_90_sharp_turn_elbow_count OR OLD.intake_to_preheater_amount != NEW.intake_to_preheater_amount OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance != NEW.preheater_outlet_90_sharp_turn_elbow_resistance OR OLD.preheater_outlet_air_intake_gate != NEW.preheater_outlet_air_intake_gate OR OLD.preheater_outlet_combustor_gate != NEW.preheater_outlet_combustor_gate OR OLD.intake_to_preheater_density != NEW.intake_to_preheater_density OR OLD.intake_to_preheater_flow_velocity != NEW.intake_to_preheater_flow_velocity THEN
     update gaspowergeneration_wind_resistance set 

     windhole_total_pressure=((((NEW.preheater_outlet_shrink_pipe)+((NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance))+(NEW.preheater_outlet_air_intake_gate)+(NEW.preheater_outlet_combustor_gate))*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2))+((NEW.preheater_outlet_ducting_length)*((NEW.preheater_outlet_frictional_resistance_coefficient)*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5))))+(((NEW.fan_outlet_ducting_length)*(((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))))+(((NEW.fan_outlet_single_increase_pipe)+(NEW.fan_outlet_90_section_slow_turn_elbow)+(NEW.fan_outlet_preheater_diffuser_pipe))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)))+((((NEW.fan_inlet_single_local_resistance_coefficient)+(NEW.fan_inlet_single_bellows)+(NEW.fan_inlet_single_damper))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2))+((NEW.fan_inlet_ducting_length)*((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.preheater_outlet_combustor_gate ISNULL OR OLD.preheater_outlet_air_intake_gate ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_resistance ISNULL OR OLD.preheater_outlet_90_sharp_turn_elbow_count ISNULL OR OLD.preheater_outlet_shrink_pipe ISNULL OR OLD.preheater_outlet_ducting_length ISNULL OR OLD.preheater_outlet_frictional_resistance_coefficient ISNULL OR OLD.preheater_to_boiler_flow_velocity ISNULL OR OLD.preheater_to_boiler_density ISNULL OR OLD.preheater_to_boiler_amount ISNULL OR OLD.fan_outlet_preheater_diffuser_pipe ISNULL OR OLD.fan_outlet_90_section_slow_turn_elbow ISNULL OR OLD.fan_outlet_single_increase_pipe ISNULL OR OLD.fan_outlet_ducting_length ISNULL OR OLD.fan_inlet_single_damper ISNULL OR OLD.fan_inlet_single_bellows ISNULL OR OLD.fan_inlet_single_local_resistance_coefficient ISNULL OR OLD.fan_inlet_ducting_length ISNULL OR OLD.fan_inlet_frictional_resistance_coefficient ISNULL OR OLD.fan_inlet_duct_length ISNULL OR OLD.intake_to_preheater_flow_velocity ISNULL OR OLD.intake_to_preheater_density ISNULL OR OLD.intake_to_preheater_amount ISNULL) AND NEW.preheater_outlet_combustor_gate NOTNULL AND NEW.preheater_outlet_air_intake_gate NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_resistance NOTNULL AND NEW.preheater_outlet_90_sharp_turn_elbow_count NOTNULL AND NEW.preheater_outlet_shrink_pipe NOTNULL AND NEW.preheater_outlet_ducting_length NOTNULL AND NEW.preheater_outlet_frictional_resistance_coefficient NOTNULL AND NEW.preheater_to_boiler_flow_velocity NOTNULL AND NEW.preheater_to_boiler_density NOTNULL AND NEW.preheater_to_boiler_amount NOTNULL AND NEW.fan_outlet_preheater_diffuser_pipe NOTNULL AND NEW.fan_outlet_90_section_slow_turn_elbow NOTNULL AND NEW.fan_outlet_single_increase_pipe NOTNULL AND NEW.fan_outlet_ducting_length NOTNULL AND NEW.fan_inlet_single_damper NOTNULL AND NEW.fan_inlet_single_bellows NOTNULL AND NEW.fan_inlet_single_local_resistance_coefficient NOTNULL AND NEW.fan_inlet_ducting_length NOTNULL AND NEW.fan_inlet_frictional_resistance_coefficient NOTNULL AND NEW.fan_inlet_duct_length NOTNULL AND NEW.intake_to_preheater_flow_velocity NOTNULL AND NEW.intake_to_preheater_density NOTNULL AND NEW.intake_to_preheater_amount NOTNULL THEN
     update gaspowergeneration_wind_resistance set 

     windhole_total_pressure=((((NEW.preheater_outlet_shrink_pipe)+((NEW.preheater_outlet_90_sharp_turn_elbow_count)*(NEW.preheater_outlet_90_sharp_turn_elbow_resistance))+(NEW.preheater_outlet_air_intake_gate)+(NEW.preheater_outlet_combustor_gate))*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2))+((NEW.preheater_outlet_ducting_length)*((NEW.preheater_outlet_frictional_resistance_coefficient)*((NEW.preheater_to_boiler_density)*((NEW.preheater_to_boiler_flow_velocity))^2/2)/((((NEW.preheater_to_boiler_amount)/(NEW.preheater_to_boiler_flow_velocity)/3600/2)/0.785)^0.5))))+(((NEW.fan_outlet_ducting_length)*(((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))))+(((NEW.fan_outlet_single_increase_pipe)+(NEW.fan_outlet_90_section_slow_turn_elbow)+(NEW.fan_outlet_preheater_diffuser_pipe))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)))+((((NEW.fan_inlet_single_local_resistance_coefficient)+(NEW.fan_inlet_single_bellows)+(NEW.fan_inlet_single_damper))*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2))+((NEW.fan_inlet_ducting_length)*((NEW.fan_inlet_frictional_resistance_coefficient)*((NEW.intake_to_preheater_density)*((NEW.intake_to_preheater_flow_velocity))^2/2)/(4*((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(2*((NEW.fan_inlet_duct_length)+(((NEW.intake_to_preheater_amount)/3600/(NEW.intake_to_preheater_flow_velocity))/(NEW.fan_inlet_duct_length))))))))
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_wind_resistance" AFTER UPDATE OF
"fan_inlet_duct_length",
"fan_inlet_gas_kinetic_viscosity",
"fan_inlet_absolute_tube_roughness",
"fan_inlet_frictional_resistance_coefficient",
"fan_inlet_ducting_length",
"fan_inlet_single_local_resistance_coefficient",
"fan_inlet_single_bellows",
"fan_inlet_single_damper",
"fan_outlet_ducting_length",
"fan_outlet_single_increase_pipe",
"fan_outlet_90_section_slow_turn_elbow",
"fan_outlet_preheater_diffuser_pipe",
"preheater_to_boiler_amount",
"preheater_to_boiler_density",
"preheater_to_boiler_flow_velocity",
"preheater_outlet_duct_length",
"preheater_outlet_absolute_tube_roughness",
"preheater_outlet_frictional_resistance_coefficient",
"preheater_outlet_ducting_length",
"preheater_outlet_shrink_pipe",
"preheater_outlet_90_sharp_turn_elbow_count",
"intake_to_preheater_amount",
"preheater_outlet_90_sharp_turn_elbow_resistance",
"preheater_outlet_air_intake_gate",
"preheater_outlet_combustor_gate",
"intake_to_preheater_density",
"intake_to_preheater_flow_velocity"
ON "public"."gaspowergeneration_wind_resistance"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_wind_resistance"();

