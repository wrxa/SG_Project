CREATE OR REPLACE FUNCTION gaspowergeneration_smoke_resistance()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段air_preheater_dynamic_pressure_head:动压头,的计算1-----------------------------------
  IF OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_dynamic_pressure_head=(((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_dynamic_pressure_head=(((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_smoke_tube_area:烟管截面积,的计算2-----------------------------------
  IF OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_smoke_tube_area=(NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_smoke_tube_area=(NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_width:宽,的计算3-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_width=((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_width=((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_duct_perimeter:风管周长,的计算4-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_duct_perimeter=2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_duct_perimeter=2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_tube_equivalent_diameter:管道当量直径,的计算5-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_tube_equivalent_diameter=4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_tube_equivalent_diameter=4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_gas_kinetic_viscosity:气体运动粘度,的计算6-----------------------------------
  IF OLD.air_preheater_outlet_calculated_temperature != NEW.air_preheater_outlet_calculated_temperature THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_gas_kinetic_viscosity=((34.94-23.08)*((NEW.air_preheater_outlet_calculated_temperature)-100)/100+23.08)/1000000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_outlet_calculated_temperature ISNULL) AND NEW.air_preheater_outlet_calculated_temperature NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_gas_kinetic_viscosity=((34.94-23.08)*((NEW.air_preheater_outlet_calculated_temperature)-100)/100+23.08)/1000000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_reynolds_number:雷诺数,的计算7-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_outlet_calculated_temperature != NEW.air_preheater_outlet_calculated_temperature OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_reynolds_number=(NEW.air_preheater_flow_velocity)*(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))))/(((34.94-23.08)*((NEW.air_preheater_outlet_calculated_temperature)-100)/100+23.08)/1000000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL OR OLD.air_preheater_outlet_calculated_temperature ISNULL) AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL AND NEW.air_preheater_outlet_calculated_temperature NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_reynolds_number=(NEW.air_preheater_flow_velocity)*(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))))/(((34.94-23.08)*((NEW.air_preheater_outlet_calculated_temperature)-100)/100+23.08)/1000000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_relative_tube_roughness:管道内壁相对粗糙度,的计算8-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_absolute_tube_roughness != NEW.air_preheater_absolute_tube_roughness OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_relative_tube_roughness=(NEW.air_preheater_absolute_tube_roughness)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_absolute_tube_roughness ISNULL OR OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_absolute_tube_roughness NOTNULL AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_relative_tube_roughness=(NEW.air_preheater_absolute_tube_roughness)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_560_relative_tube_roughness:560/△1,的计算9-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_absolute_tube_roughness != NEW.air_preheater_absolute_tube_roughness OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_560_relative_tube_roughness=560/((NEW.air_preheater_absolute_tube_roughness)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_absolute_tube_roughness ISNULL OR OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_absolute_tube_roughness NOTNULL AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_560_relative_tube_roughness=560/((NEW.air_preheater_absolute_tube_roughness)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_frictional_resistance:摩擦阻力,的计算10-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_frictional_resistance_coefficient != NEW.air_preheater_frictional_resistance_coefficient OR OLD.air_preheater_ducting_length != NEW.air_preheater_ducting_length OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_frictional_resistance=(NEW.air_preheater_ducting_length)*((NEW.air_preheater_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_ducting_length ISNULL OR OLD.air_preheater_frictional_resistance_coefficient ISNULL OR OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_ducting_length NOTNULL AND NEW.air_preheater_frictional_resistance_coefficient NOTNULL AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_frictional_resistance=(NEW.air_preheater_ducting_length)*((NEW.air_preheater_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_unit_length_frictional_resistance:单位长度摩擦阻力,的计算11-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_frictional_resistance_coefficient != NEW.air_preheater_frictional_resistance_coefficient OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_unit_length_frictional_resistance=(NEW.air_preheater_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_frictional_resistance_coefficient ISNULL OR OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_frictional_resistance_coefficient NOTNULL AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_unit_length_frictional_resistance=(NEW.air_preheater_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_local_resistance:局部阻力,的计算12-----------------------------------
  IF OLD.air_preheater_air_elbow_local_resistance_coefficient != NEW.air_preheater_air_elbow_local_resistance_coefficient OR OLD.air_preheater_powder_concentration_corrected_coefficient != NEW.air_preheater_powder_concentration_corrected_coefficient OR OLD.air_preheater_slow_air_local_resistance_coefficient != NEW.air_preheater_slow_air_local_resistance_coefficient OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient != NEW.air_preheater_slow_powder_concentration_corrected_coefficient OR OLD.air_preheater_reducer_tube != NEW.air_preheater_reducer_tube OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_local_resistance=((((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)))+(((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))))+(NEW.air_preheater_reducer_tube))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_reducer_tube ISNULL OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_slow_air_local_resistance_coefficient ISNULL OR OLD.air_preheater_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_air_elbow_local_resistance_coefficient ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.air_preheater_reducer_tube NOTNULL AND NEW.air_preheater_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_slow_air_local_resistance_coefficient NOTNULL AND NEW.air_preheater_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_air_elbow_local_resistance_coefficient NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_local_resistance=((((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)))+(((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))))+(NEW.air_preheater_reducer_tube))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_local_resistance_coefficient:局部阻力系数,的计算13-----------------------------------
  IF OLD.air_preheater_air_elbow_local_resistance_coefficient != NEW.air_preheater_air_elbow_local_resistance_coefficient OR OLD.air_preheater_powder_concentration_corrected_coefficient != NEW.air_preheater_powder_concentration_corrected_coefficient OR OLD.air_preheater_slow_air_local_resistance_coefficient != NEW.air_preheater_slow_air_local_resistance_coefficient OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient != NEW.air_preheater_slow_powder_concentration_corrected_coefficient OR OLD.air_preheater_reducer_tube != NEW.air_preheater_reducer_tube THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_local_resistance_coefficient=(((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)))+(((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))))+(NEW.air_preheater_reducer_tube)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_reducer_tube ISNULL OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_slow_air_local_resistance_coefficient ISNULL OR OLD.air_preheater_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_air_elbow_local_resistance_coefficient ISNULL) AND NEW.air_preheater_reducer_tube NOTNULL AND NEW.air_preheater_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_slow_air_local_resistance_coefficient NOTNULL AND NEW.air_preheater_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_air_elbow_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_local_resistance_coefficient=(((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)))+(((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))))+(NEW.air_preheater_reducer_tube)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_90_outlet_sharp_turn_elbow:1个90度空预器出口变径急转弯头,的计算14-----------------------------------
  IF OLD.air_preheater_air_elbow_local_resistance_coefficient != NEW.air_preheater_air_elbow_local_resistance_coefficient OR OLD.air_preheater_powder_concentration_corrected_coefficient != NEW.air_preheater_powder_concentration_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_90_outlet_sharp_turn_elbow=((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_air_elbow_local_resistance_coefficient ISNULL) AND NEW.air_preheater_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_air_elbow_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_90_outlet_sharp_turn_elbow=((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_powder_local_resistance_coefficient:含粉气体局部阻力系数,的计算15-----------------------------------
  IF OLD.air_preheater_air_elbow_local_resistance_coefficient != NEW.air_preheater_air_elbow_local_resistance_coefficient OR OLD.air_preheater_powder_concentration_corrected_coefficient != NEW.air_preheater_powder_concentration_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_powder_local_resistance_coefficient=(NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_air_elbow_local_resistance_coefficient ISNULL) AND NEW.air_preheater_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_air_elbow_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_powder_local_resistance_coefficient=(NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_90_section_slow_turn_elbow:1个90度等截面缓转弯头,的计算16-----------------------------------
  IF OLD.air_preheater_slow_air_local_resistance_coefficient != NEW.air_preheater_slow_air_local_resistance_coefficient OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient != NEW.air_preheater_slow_powder_concentration_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_90_section_slow_turn_elbow=((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_slow_air_local_resistance_coefficient ISNULL) AND NEW.air_preheater_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_slow_air_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_90_section_slow_turn_elbow=((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_slow_powder_local_resistance_coefficient:含粉气体局部阻力系数,的计算17-----------------------------------
  IF OLD.air_preheater_slow_air_local_resistance_coefficient != NEW.air_preheater_slow_air_local_resistance_coefficient OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient != NEW.air_preheater_slow_powder_concentration_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_slow_powder_local_resistance_coefficient=(NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_slow_air_local_resistance_coefficient ISNULL) AND NEW.air_preheater_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_slow_air_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_slow_powder_local_resistance_coefficient=(NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段air_preheater_to_deduster_total_resistance:空预器出口至除尘器入口总阻力,的计算18-----------------------------------
  IF OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_frictional_resistance_coefficient != NEW.air_preheater_frictional_resistance_coefficient OR OLD.air_preheater_ducting_length != NEW.air_preheater_ducting_length OR OLD.air_preheater_air_elbow_local_resistance_coefficient != NEW.air_preheater_air_elbow_local_resistance_coefficient OR OLD.air_preheater_powder_concentration_corrected_coefficient != NEW.air_preheater_powder_concentration_corrected_coefficient OR OLD.air_preheater_slow_air_local_resistance_coefficient != NEW.air_preheater_slow_air_local_resistance_coefficient OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient != NEW.air_preheater_slow_powder_concentration_corrected_coefficient OR OLD.air_preheater_reducer_tube != NEW.air_preheater_reducer_tube OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_to_deduster_total_resistance=(((((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)))+(((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))))+(NEW.air_preheater_reducer_tube))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.air_preheater_ducting_length)*((NEW.air_preheater_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.air_preheater_reducer_tube ISNULL OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_slow_air_local_resistance_coefficient ISNULL OR OLD.air_preheater_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_air_elbow_local_resistance_coefficient ISNULL OR OLD.air_preheater_ducting_length ISNULL OR OLD.air_preheater_frictional_resistance_coefficient ISNULL OR OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.air_preheater_reducer_tube NOTNULL AND NEW.air_preheater_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_slow_air_local_resistance_coefficient NOTNULL AND NEW.air_preheater_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_air_elbow_local_resistance_coefficient NOTNULL AND NEW.air_preheater_ducting_length NOTNULL AND NEW.air_preheater_frictional_resistance_coefficient NOTNULL AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     air_preheater_to_deduster_total_resistance=(((((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)))+(((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))))+(NEW.air_preheater_reducer_tube))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.air_preheater_ducting_length)*((NEW.air_preheater_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_dynamic_pressure_head:动压头,的计算19-----------------------------------
  IF OLD.deduster_density != NEW.deduster_density OR OLD.deduster_flow_velocity != NEW.deduster_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_dynamic_pressure_head=((NEW.deduster_density))*((NEW.deduster_flow_velocity))^2/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_flow_velocity ISNULL OR OLD.deduster_density ISNULL) AND NEW.deduster_flow_velocity NOTNULL AND NEW.deduster_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_dynamic_pressure_head=((NEW.deduster_density))*((NEW.deduster_flow_velocity))^2/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_smoke_tube_area:烟管截面积,的计算20-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_smoke_tube_area=((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_smoke_tube_area=((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_width:宽,的计算21-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_width=(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_width=(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_duct_perimeter:风管周长,的计算22-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_duct_perimeter=2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_duct_perimeter=2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_tube_equivalent_diameter:管道当量直径,的计算23-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_tube_equivalent_diameter=4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_tube_equivalent_diameter=4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_gas_kinetic_viscosity:气体运动粘度,的计算24-----------------------------------
  IF OLD.deduster_outlet_calculated_temperature != NEW.deduster_outlet_calculated_temperature THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_gas_kinetic_viscosity=((34.94-23.08)*((NEW.deduster_outlet_calculated_temperature)-100)/100+23.08)/1000000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_outlet_calculated_temperature ISNULL) AND NEW.deduster_outlet_calculated_temperature NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_gas_kinetic_viscosity=((34.94-23.08)*((NEW.deduster_outlet_calculated_temperature)-100)/100+23.08)/1000000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_reynolds_number:雷诺数,的计算25-----------------------------------
  IF OLD.deduster_outlet_calculated_temperature != NEW.deduster_outlet_calculated_temperature OR OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_reynolds_number=(NEW.air_preheater_flow_velocity)*(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))))/(((34.94-23.08)*((NEW.deduster_outlet_calculated_temperature)-100)/100+23.08)/1000000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.deduster_outlet_calculated_temperature ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.deduster_outlet_calculated_temperature NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_reynolds_number=(NEW.air_preheater_flow_velocity)*(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))))/(((34.94-23.08)*((NEW.deduster_outlet_calculated_temperature)-100)/100+23.08)/1000000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_relative_tube_roughness:管道内壁相对粗糙度,的计算26-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.deduster_absolute_tube_roughness != NEW.deduster_absolute_tube_roughness OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_relative_tube_roughness=(NEW.deduster_absolute_tube_roughness)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_absolute_tube_roughness ISNULL OR OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_absolute_tube_roughness NOTNULL AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_relative_tube_roughness=(NEW.deduster_absolute_tube_roughness)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_560_relative_tube_roughness:560/△1,的计算27-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.deduster_absolute_tube_roughness != NEW.deduster_absolute_tube_roughness OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_560_relative_tube_roughness=560/((NEW.deduster_absolute_tube_roughness)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_absolute_tube_roughness ISNULL OR OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_absolute_tube_roughness NOTNULL AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_560_relative_tube_roughness=560/((NEW.deduster_absolute_tube_roughness)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_frictional_resistance:摩擦阻力,的计算28-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.deduster_frictional_resistance_coefficient != NEW.deduster_frictional_resistance_coefficient OR OLD.deduster_ducting_length != NEW.deduster_ducting_length OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_frictional_resistance=(NEW.deduster_ducting_length)*((NEW.deduster_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_ducting_length ISNULL OR OLD.deduster_frictional_resistance_coefficient ISNULL OR OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_ducting_length NOTNULL AND NEW.deduster_frictional_resistance_coefficient NOTNULL AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_frictional_resistance=(NEW.deduster_ducting_length)*((NEW.deduster_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_unit_length_frictional_resistance:单位长度摩擦阻力,的计算29-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.deduster_frictional_resistance_coefficient != NEW.deduster_frictional_resistance_coefficient OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_unit_length_frictional_resistance=(NEW.deduster_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_frictional_resistance_coefficient ISNULL OR OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_frictional_resistance_coefficient NOTNULL AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_unit_length_frictional_resistance=(NEW.deduster_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_local_resistance:局部阻力,的计算30-----------------------------------
  IF OLD.deduster_slow_air_local_resistance_coefficient != NEW.deduster_slow_air_local_resistance_coefficient OR OLD.deduster_slow_powder_concentration_corrected_coefficient != NEW.deduster_slow_powder_concentration_corrected_coefficient OR OLD.deduster_corrected_turning_angle_coefficient != NEW.deduster_corrected_turning_angle_coefficient OR OLD.deduster_section_corrected_height_width_ratio_coefficient != NEW.deduster_section_corrected_height_width_ratio_coefficient OR OLD.deduster_section_original_resistance_coefficient_with_roughness != NEW.deduster_section_original_resistance_coefficient_with_roughness OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.deduster_section_slow_powder_corrected_coefficient != NEW.deduster_section_slow_powder_corrected_coefficient OR OLD.deduster_inlet_bellows != NEW.deduster_inlet_bellows OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_local_resistance=((((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)))+((((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)))+(NEW.deduster_inlet_bellows))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_inlet_bellows ISNULL OR OLD.deduster_section_slow_powder_corrected_coefficient ISNULL OR OLD.deduster_section_original_resistance_coefficient_with_roughness ISNULL OR OLD.deduster_section_corrected_height_width_ratio_coefficient ISNULL OR OLD.deduster_corrected_turning_angle_coefficient ISNULL OR OLD.deduster_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.deduster_slow_air_local_resistance_coefficient ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_inlet_bellows NOTNULL AND NEW.deduster_section_slow_powder_corrected_coefficient NOTNULL AND NEW.deduster_section_original_resistance_coefficient_with_roughness NOTNULL AND NEW.deduster_section_corrected_height_width_ratio_coefficient NOTNULL AND NEW.deduster_corrected_turning_angle_coefficient NOTNULL AND NEW.deduster_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.deduster_slow_air_local_resistance_coefficient NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_local_resistance=((((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)))+((((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)))+(NEW.deduster_inlet_bellows))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_local_resistance_coefficient:局部阻力系数,的计算31-----------------------------------
  IF OLD.deduster_slow_air_local_resistance_coefficient != NEW.deduster_slow_air_local_resistance_coefficient OR OLD.deduster_slow_powder_concentration_corrected_coefficient != NEW.deduster_slow_powder_concentration_corrected_coefficient OR OLD.deduster_corrected_turning_angle_coefficient != NEW.deduster_corrected_turning_angle_coefficient OR OLD.deduster_section_corrected_height_width_ratio_coefficient != NEW.deduster_section_corrected_height_width_ratio_coefficient OR OLD.deduster_section_original_resistance_coefficient_with_roughness != NEW.deduster_section_original_resistance_coefficient_with_roughness OR OLD.deduster_section_slow_powder_corrected_coefficient != NEW.deduster_section_slow_powder_corrected_coefficient OR OLD.deduster_inlet_bellows != NEW.deduster_inlet_bellows THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_local_resistance_coefficient=(((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)))+((((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)))+(NEW.deduster_inlet_bellows)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_inlet_bellows ISNULL OR OLD.deduster_section_slow_powder_corrected_coefficient ISNULL OR OLD.deduster_section_original_resistance_coefficient_with_roughness ISNULL OR OLD.deduster_section_corrected_height_width_ratio_coefficient ISNULL OR OLD.deduster_corrected_turning_angle_coefficient ISNULL OR OLD.deduster_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.deduster_slow_air_local_resistance_coefficient ISNULL) AND NEW.deduster_inlet_bellows NOTNULL AND NEW.deduster_section_slow_powder_corrected_coefficient NOTNULL AND NEW.deduster_section_original_resistance_coefficient_with_roughness NOTNULL AND NEW.deduster_section_corrected_height_width_ratio_coefficient NOTNULL AND NEW.deduster_corrected_turning_angle_coefficient NOTNULL AND NEW.deduster_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.deduster_slow_air_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_local_resistance_coefficient=(((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)))+((((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)))+(NEW.deduster_inlet_bellows)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_90_outlet_slow_turn_elbow:1个90度除尘器出口缓转弯头,的计算32-----------------------------------
  IF OLD.deduster_slow_air_local_resistance_coefficient != NEW.deduster_slow_air_local_resistance_coefficient OR OLD.deduster_slow_powder_concentration_corrected_coefficient != NEW.deduster_slow_powder_concentration_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_90_outlet_slow_turn_elbow=((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.deduster_slow_air_local_resistance_coefficient ISNULL) AND NEW.deduster_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.deduster_slow_air_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_90_outlet_slow_turn_elbow=((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_slow_powder_local_resistance_coefficient:含粉气体局部阻力系数,的计算33-----------------------------------
  IF OLD.deduster_slow_air_local_resistance_coefficient != NEW.deduster_slow_air_local_resistance_coefficient OR OLD.deduster_slow_powder_concentration_corrected_coefficient != NEW.deduster_slow_powder_concentration_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_slow_powder_local_resistance_coefficient=(NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.deduster_slow_air_local_resistance_coefficient ISNULL) AND NEW.deduster_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.deduster_slow_air_local_resistance_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_slow_powder_local_resistance_coefficient=(NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_90_section_slow_turn_elbow:1个90度等截面缓转弯头,的计算34-----------------------------------
  IF OLD.deduster_corrected_turning_angle_coefficient != NEW.deduster_corrected_turning_angle_coefficient OR OLD.deduster_section_corrected_height_width_ratio_coefficient != NEW.deduster_section_corrected_height_width_ratio_coefficient OR OLD.deduster_section_original_resistance_coefficient_with_roughness != NEW.deduster_section_original_resistance_coefficient_with_roughness OR OLD.deduster_section_slow_powder_corrected_coefficient != NEW.deduster_section_slow_powder_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_90_section_slow_turn_elbow=(((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_section_slow_powder_corrected_coefficient ISNULL OR OLD.deduster_section_original_resistance_coefficient_with_roughness ISNULL OR OLD.deduster_section_corrected_height_width_ratio_coefficient ISNULL OR OLD.deduster_corrected_turning_angle_coefficient ISNULL) AND NEW.deduster_section_slow_powder_corrected_coefficient NOTNULL AND NEW.deduster_section_original_resistance_coefficient_with_roughness NOTNULL AND NEW.deduster_section_corrected_height_width_ratio_coefficient NOTNULL AND NEW.deduster_corrected_turning_angle_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_90_section_slow_turn_elbow=(((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_section_slow_powder_local_resistance_coefficient:含粉气体局部阻力系数,的计算35-----------------------------------
  IF OLD.deduster_corrected_turning_angle_coefficient != NEW.deduster_corrected_turning_angle_coefficient OR OLD.deduster_section_corrected_height_width_ratio_coefficient != NEW.deduster_section_corrected_height_width_ratio_coefficient OR OLD.deduster_section_original_resistance_coefficient_with_roughness != NEW.deduster_section_original_resistance_coefficient_with_roughness OR OLD.deduster_section_slow_powder_corrected_coefficient != NEW.deduster_section_slow_powder_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_section_slow_powder_local_resistance_coefficient=((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_section_slow_powder_corrected_coefficient ISNULL OR OLD.deduster_section_original_resistance_coefficient_with_roughness ISNULL OR OLD.deduster_section_corrected_height_width_ratio_coefficient ISNULL OR OLD.deduster_corrected_turning_angle_coefficient ISNULL) AND NEW.deduster_section_slow_powder_corrected_coefficient NOTNULL AND NEW.deduster_section_original_resistance_coefficient_with_roughness NOTNULL AND NEW.deduster_section_corrected_height_width_ratio_coefficient NOTNULL AND NEW.deduster_corrected_turning_angle_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_section_slow_powder_local_resistance_coefficient=((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_section_slow_air_local_resistance_coefficient:纯空气局部阻力系数,的计算36-----------------------------------
  IF OLD.deduster_corrected_turning_angle_coefficient != NEW.deduster_corrected_turning_angle_coefficient OR OLD.deduster_section_corrected_height_width_ratio_coefficient != NEW.deduster_section_corrected_height_width_ratio_coefficient OR OLD.deduster_section_original_resistance_coefficient_with_roughness != NEW.deduster_section_original_resistance_coefficient_with_roughness THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_section_slow_air_local_resistance_coefficient=(NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_section_original_resistance_coefficient_with_roughness ISNULL OR OLD.deduster_section_corrected_height_width_ratio_coefficient ISNULL OR OLD.deduster_corrected_turning_angle_coefficient ISNULL) AND NEW.deduster_section_original_resistance_coefficient_with_roughness NOTNULL AND NEW.deduster_section_corrected_height_width_ratio_coefficient NOTNULL AND NEW.deduster_corrected_turning_angle_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_section_slow_air_local_resistance_coefficient=(NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段deduster_to_induced_draft_total_resistance:除尘器出口至引风机入口总阻力,的计算37-----------------------------------
  IF OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.deduster_frictional_resistance_coefficient != NEW.deduster_frictional_resistance_coefficient OR OLD.deduster_ducting_length != NEW.deduster_ducting_length OR OLD.deduster_slow_air_local_resistance_coefficient != NEW.deduster_slow_air_local_resistance_coefficient OR OLD.deduster_slow_powder_concentration_corrected_coefficient != NEW.deduster_slow_powder_concentration_corrected_coefficient OR OLD.deduster_corrected_turning_angle_coefficient != NEW.deduster_corrected_turning_angle_coefficient OR OLD.deduster_section_corrected_height_width_ratio_coefficient != NEW.deduster_section_corrected_height_width_ratio_coefficient OR OLD.deduster_section_original_resistance_coefficient_with_roughness != NEW.deduster_section_original_resistance_coefficient_with_roughness OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.deduster_section_slow_powder_corrected_coefficient != NEW.deduster_section_slow_powder_corrected_coefficient OR OLD.deduster_inlet_bellows != NEW.deduster_inlet_bellows OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_to_induced_draft_total_resistance=(((((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)))+((((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)))+(NEW.deduster_inlet_bellows))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.deduster_ducting_length)*((NEW.deduster_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.deduster_inlet_bellows ISNULL OR OLD.deduster_section_slow_powder_corrected_coefficient ISNULL OR OLD.deduster_section_original_resistance_coefficient_with_roughness ISNULL OR OLD.deduster_section_corrected_height_width_ratio_coefficient ISNULL OR OLD.deduster_corrected_turning_angle_coefficient ISNULL OR OLD.deduster_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.deduster_slow_air_local_resistance_coefficient ISNULL OR OLD.deduster_ducting_length ISNULL OR OLD.deduster_frictional_resistance_coefficient ISNULL OR OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.deduster_inlet_bellows NOTNULL AND NEW.deduster_section_slow_powder_corrected_coefficient NOTNULL AND NEW.deduster_section_original_resistance_coefficient_with_roughness NOTNULL AND NEW.deduster_section_corrected_height_width_ratio_coefficient NOTNULL AND NEW.deduster_corrected_turning_angle_coefficient NOTNULL AND NEW.deduster_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.deduster_slow_air_local_resistance_coefficient NOTNULL AND NEW.deduster_ducting_length NOTNULL AND NEW.deduster_frictional_resistance_coefficient NOTNULL AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     deduster_to_induced_draft_total_resistance=(((((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)))+((((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)))+(NEW.deduster_inlet_bellows))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.deduster_ducting_length)*((NEW.deduster_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_dynamic_pressure_head:动压头,的计算38-----------------------------------
  IF OLD.induced_draft_density != NEW.induced_draft_density OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_dynamic_pressure_head=((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_density ISNULL) AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_dynamic_pressure_head=((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_smoke_tube_area:烟管截面积,的计算39-----------------------------------
  IF OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_smoke_tube_area=(NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL) AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_smoke_tube_area=(NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_height:高,的计算40-----------------------------------
  IF OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_height=((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL) AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_height=((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_duct_perimeter:风管周长,的计算41-----------------------------------
  IF OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_duct_perimeter=2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL) AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_duct_perimeter=2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_tube_equivalent_diameter:管道当量直径,的计算42-----------------------------------
  IF OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_tube_equivalent_diameter=4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL) AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_tube_equivalent_diameter=4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_gas_kinetic_viscosity:气体运动粘度,的计算43-----------------------------------
  IF OLD.induced_draft_inlet_calculated_temperature != NEW.induced_draft_inlet_calculated_temperature THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_gas_kinetic_viscosity=((34.94-23.08)*((NEW.induced_draft_inlet_calculated_temperature)-100)/100+23.08)/1000000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_inlet_calculated_temperature ISNULL) AND NEW.induced_draft_inlet_calculated_temperature NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_gas_kinetic_viscosity=((34.94-23.08)*((NEW.induced_draft_inlet_calculated_temperature)-100)/100+23.08)/1000000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_reynolds_number:雷诺数,的计算44-----------------------------------
  IF OLD.induced_draft_inlet_calculated_temperature != NEW.induced_draft_inlet_calculated_temperature OR OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_reynolds_number=(NEW.induced_draft_flow_velocity)*(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))))/(((34.94-23.08)*((NEW.induced_draft_inlet_calculated_temperature)-100)/100+23.08)/1000000)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL OR OLD.induced_draft_inlet_calculated_temperature ISNULL) AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL AND NEW.induced_draft_inlet_calculated_temperature NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_reynolds_number=(NEW.induced_draft_flow_velocity)*(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))))/(((34.94-23.08)*((NEW.induced_draft_inlet_calculated_temperature)-100)/100+23.08)/1000000)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_relative_tube_roughness:管道内壁相对粗糙度,的计算45-----------------------------------
  IF OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width OR OLD.induced_draft_absolute_tube_roughness != NEW.induced_draft_absolute_tube_roughness THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_relative_tube_roughness=(NEW.induced_draft_absolute_tube_roughness)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_absolute_tube_roughness ISNULL OR OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL) AND NEW.induced_draft_absolute_tube_roughness NOTNULL AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_relative_tube_roughness=(NEW.induced_draft_absolute_tube_roughness)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_560_relative_tube_roughness:560/△1,的计算46-----------------------------------
  IF OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width OR OLD.induced_draft_absolute_tube_roughness != NEW.induced_draft_absolute_tube_roughness THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_560_relative_tube_roughness=560/((NEW.induced_draft_absolute_tube_roughness)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_absolute_tube_roughness ISNULL OR OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL) AND NEW.induced_draft_absolute_tube_roughness NOTNULL AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_560_relative_tube_roughness=560/((NEW.induced_draft_absolute_tube_roughness)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_frictional_resistance:摩擦阻力,的计算47-----------------------------------
  IF OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_density != NEW.induced_draft_density OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width OR OLD.induced_draft_frictional_resistance_coefficient != NEW.induced_draft_frictional_resistance_coefficient OR OLD.induced_draft_ducting_length != NEW.induced_draft_ducting_length THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_frictional_resistance=(NEW.induced_draft_ducting_length)*((NEW.induced_draft_frictional_resistance_coefficient)*(((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_ducting_length ISNULL OR OLD.induced_draft_frictional_resistance_coefficient ISNULL OR OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_density ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL) AND NEW.induced_draft_ducting_length NOTNULL AND NEW.induced_draft_frictional_resistance_coefficient NOTNULL AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_density NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_frictional_resistance=(NEW.induced_draft_ducting_length)*((NEW.induced_draft_frictional_resistance_coefficient)*(((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_unit_length_frictional_resistance:单位长度摩擦阻力,的计算48-----------------------------------
  IF OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_density != NEW.induced_draft_density OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width OR OLD.induced_draft_frictional_resistance_coefficient != NEW.induced_draft_frictional_resistance_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_unit_length_frictional_resistance=(NEW.induced_draft_frictional_resistance_coefficient)*(((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_frictional_resistance_coefficient ISNULL OR OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_density ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL) AND NEW.induced_draft_frictional_resistance_coefficient NOTNULL AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_density NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_unit_length_frictional_resistance=(NEW.induced_draft_frictional_resistance_coefficient)*(((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_local_resistance:局部阻力,的计算49-----------------------------------
  IF OLD.induced_draft_corrected_turning_angle_coefficient != NEW.induced_draft_corrected_turning_angle_coefficient OR OLD.induced_draft_corrected_height_width_ratio_coefficient != NEW.induced_draft_corrected_height_width_ratio_coefficient OR OLD.induced_draft_original_resistance_coefficient_with_roughness != NEW.induced_draft_original_resistance_coefficient_with_roughness OR OLD.induced_draft_powder_concentration_corrected_coefficient != NEW.induced_draft_powder_concentration_corrected_coefficient OR OLD.brick_chimney_inlet != NEW.brick_chimney_inlet OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity OR OLD.induced_draft_outlet_plate_gate != NEW.induced_draft_outlet_plate_gate OR OLD.induced_draft_outlet_diffuser_tube != NEW.induced_draft_outlet_diffuser_tube THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_local_resistance=((NEW.induced_draft_outlet_plate_gate)+(NEW.induced_draft_outlet_diffuser_tube)+((((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)))+(NEW.brick_chimney_inlet))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.brick_chimney_inlet ISNULL OR OLD.induced_draft_powder_concentration_corrected_coefficient ISNULL OR OLD.induced_draft_original_resistance_coefficient_with_roughness ISNULL OR OLD.induced_draft_corrected_height_width_ratio_coefficient ISNULL OR OLD.induced_draft_corrected_turning_angle_coefficient ISNULL OR OLD.induced_draft_outlet_diffuser_tube ISNULL OR OLD.induced_draft_outlet_plate_gate ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.brick_chimney_inlet NOTNULL AND NEW.induced_draft_powder_concentration_corrected_coefficient NOTNULL AND NEW.induced_draft_original_resistance_coefficient_with_roughness NOTNULL AND NEW.induced_draft_corrected_height_width_ratio_coefficient NOTNULL AND NEW.induced_draft_corrected_turning_angle_coefficient NOTNULL AND NEW.induced_draft_outlet_diffuser_tube NOTNULL AND NEW.induced_draft_outlet_plate_gate NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_local_resistance=((NEW.induced_draft_outlet_plate_gate)+(NEW.induced_draft_outlet_diffuser_tube)+((((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)))+(NEW.brick_chimney_inlet))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_local_resistance_coefficient:局部阻力系数,的计算50-----------------------------------
  IF OLD.induced_draft_corrected_turning_angle_coefficient != NEW.induced_draft_corrected_turning_angle_coefficient OR OLD.induced_draft_corrected_height_width_ratio_coefficient != NEW.induced_draft_corrected_height_width_ratio_coefficient OR OLD.induced_draft_original_resistance_coefficient_with_roughness != NEW.induced_draft_original_resistance_coefficient_with_roughness OR OLD.induced_draft_powder_concentration_corrected_coefficient != NEW.induced_draft_powder_concentration_corrected_coefficient OR OLD.brick_chimney_inlet != NEW.brick_chimney_inlet OR OLD.induced_draft_outlet_plate_gate != NEW.induced_draft_outlet_plate_gate OR OLD.induced_draft_outlet_diffuser_tube != NEW.induced_draft_outlet_diffuser_tube THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_local_resistance_coefficient=(NEW.induced_draft_outlet_plate_gate)+(NEW.induced_draft_outlet_diffuser_tube)+((((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)))+(NEW.brick_chimney_inlet)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.brick_chimney_inlet ISNULL OR OLD.induced_draft_powder_concentration_corrected_coefficient ISNULL OR OLD.induced_draft_original_resistance_coefficient_with_roughness ISNULL OR OLD.induced_draft_corrected_height_width_ratio_coefficient ISNULL OR OLD.induced_draft_corrected_turning_angle_coefficient ISNULL OR OLD.induced_draft_outlet_diffuser_tube ISNULL OR OLD.induced_draft_outlet_plate_gate ISNULL) AND NEW.brick_chimney_inlet NOTNULL AND NEW.induced_draft_powder_concentration_corrected_coefficient NOTNULL AND NEW.induced_draft_original_resistance_coefficient_with_roughness NOTNULL AND NEW.induced_draft_corrected_height_width_ratio_coefficient NOTNULL AND NEW.induced_draft_corrected_turning_angle_coefficient NOTNULL AND NEW.induced_draft_outlet_diffuser_tube NOTNULL AND NEW.induced_draft_outlet_plate_gate NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_local_resistance_coefficient=(NEW.induced_draft_outlet_plate_gate)+(NEW.induced_draft_outlet_diffuser_tube)+((((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)))+(NEW.brick_chimney_inlet)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_45_90_slow_turn_elbow:1个45度缓转弯头（钢烟道）/1个90度缓转弯头（砖烟道）,的计算51-----------------------------------
  IF OLD.induced_draft_corrected_turning_angle_coefficient != NEW.induced_draft_corrected_turning_angle_coefficient OR OLD.induced_draft_corrected_height_width_ratio_coefficient != NEW.induced_draft_corrected_height_width_ratio_coefficient OR OLD.induced_draft_original_resistance_coefficient_with_roughness != NEW.induced_draft_original_resistance_coefficient_with_roughness OR OLD.induced_draft_powder_concentration_corrected_coefficient != NEW.induced_draft_powder_concentration_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_45_90_slow_turn_elbow=(((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_powder_concentration_corrected_coefficient ISNULL OR OLD.induced_draft_original_resistance_coefficient_with_roughness ISNULL OR OLD.induced_draft_corrected_height_width_ratio_coefficient ISNULL OR OLD.induced_draft_corrected_turning_angle_coefficient ISNULL) AND NEW.induced_draft_powder_concentration_corrected_coefficient NOTNULL AND NEW.induced_draft_original_resistance_coefficient_with_roughness NOTNULL AND NEW.induced_draft_corrected_height_width_ratio_coefficient NOTNULL AND NEW.induced_draft_corrected_turning_angle_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_45_90_slow_turn_elbow=(((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_powder_local_resistance_coefficient:含粉气体局部阻力系数,的计算52-----------------------------------
  IF OLD.induced_draft_corrected_turning_angle_coefficient != NEW.induced_draft_corrected_turning_angle_coefficient OR OLD.induced_draft_corrected_height_width_ratio_coefficient != NEW.induced_draft_corrected_height_width_ratio_coefficient OR OLD.induced_draft_original_resistance_coefficient_with_roughness != NEW.induced_draft_original_resistance_coefficient_with_roughness OR OLD.induced_draft_powder_concentration_corrected_coefficient != NEW.induced_draft_powder_concentration_corrected_coefficient THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_powder_local_resistance_coefficient=((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_powder_concentration_corrected_coefficient ISNULL OR OLD.induced_draft_original_resistance_coefficient_with_roughness ISNULL OR OLD.induced_draft_corrected_height_width_ratio_coefficient ISNULL OR OLD.induced_draft_corrected_turning_angle_coefficient ISNULL) AND NEW.induced_draft_powder_concentration_corrected_coefficient NOTNULL AND NEW.induced_draft_original_resistance_coefficient_with_roughness NOTNULL AND NEW.induced_draft_corrected_height_width_ratio_coefficient NOTNULL AND NEW.induced_draft_corrected_turning_angle_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_powder_local_resistance_coefficient=((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_air_local_resistance_coefficient:纯空气局部阻力系数,的计算53-----------------------------------
  IF OLD.induced_draft_corrected_turning_angle_coefficient != NEW.induced_draft_corrected_turning_angle_coefficient OR OLD.induced_draft_corrected_height_width_ratio_coefficient != NEW.induced_draft_corrected_height_width_ratio_coefficient OR OLD.induced_draft_original_resistance_coefficient_with_roughness != NEW.induced_draft_original_resistance_coefficient_with_roughness THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_air_local_resistance_coefficient=(NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.induced_draft_original_resistance_coefficient_with_roughness ISNULL OR OLD.induced_draft_corrected_height_width_ratio_coefficient ISNULL OR OLD.induced_draft_corrected_turning_angle_coefficient ISNULL) AND NEW.induced_draft_original_resistance_coefficient_with_roughness NOTNULL AND NEW.induced_draft_corrected_height_width_ratio_coefficient NOTNULL AND NEW.induced_draft_corrected_turning_angle_coefficient NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_air_local_resistance_coefficient=(NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段induced_draft_to_chimney_total_resistance:引风机出口至烟囱入口总阻力,的计算54-----------------------------------
  IF OLD.induced_draft_corrected_turning_angle_coefficient != NEW.induced_draft_corrected_turning_angle_coefficient OR OLD.induced_draft_corrected_height_width_ratio_coefficient != NEW.induced_draft_corrected_height_width_ratio_coefficient OR OLD.induced_draft_original_resistance_coefficient_with_roughness != NEW.induced_draft_original_resistance_coefficient_with_roughness OR OLD.induced_draft_powder_concentration_corrected_coefficient != NEW.induced_draft_powder_concentration_corrected_coefficient OR OLD.brick_chimney_inlet != NEW.brick_chimney_inlet OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_density != NEW.induced_draft_density OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width OR OLD.induced_draft_frictional_resistance_coefficient != NEW.induced_draft_frictional_resistance_coefficient OR OLD.induced_draft_ducting_length != NEW.induced_draft_ducting_length OR OLD.induced_draft_outlet_plate_gate != NEW.induced_draft_outlet_plate_gate OR OLD.induced_draft_outlet_diffuser_tube != NEW.induced_draft_outlet_diffuser_tube THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_to_chimney_total_resistance=(((NEW.induced_draft_outlet_plate_gate)+(NEW.induced_draft_outlet_diffuser_tube)+((((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)))+(NEW.brick_chimney_inlet))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.induced_draft_ducting_length)*((NEW.induced_draft_frictional_resistance_coefficient)*(((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.brick_chimney_inlet ISNULL OR OLD.induced_draft_powder_concentration_corrected_coefficient ISNULL OR OLD.induced_draft_original_resistance_coefficient_with_roughness ISNULL OR OLD.induced_draft_corrected_height_width_ratio_coefficient ISNULL OR OLD.induced_draft_corrected_turning_angle_coefficient ISNULL OR OLD.induced_draft_outlet_diffuser_tube ISNULL OR OLD.induced_draft_outlet_plate_gate ISNULL OR OLD.induced_draft_ducting_length ISNULL OR OLD.induced_draft_frictional_resistance_coefficient ISNULL OR OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_density ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL) AND NEW.brick_chimney_inlet NOTNULL AND NEW.induced_draft_powder_concentration_corrected_coefficient NOTNULL AND NEW.induced_draft_original_resistance_coefficient_with_roughness NOTNULL AND NEW.induced_draft_corrected_height_width_ratio_coefficient NOTNULL AND NEW.induced_draft_corrected_turning_angle_coefficient NOTNULL AND NEW.induced_draft_outlet_diffuser_tube NOTNULL AND NEW.induced_draft_outlet_plate_gate NOTNULL AND NEW.induced_draft_ducting_length NOTNULL AND NEW.induced_draft_frictional_resistance_coefficient NOTNULL AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_density NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     induced_draft_to_chimney_total_resistance=(((NEW.induced_draft_outlet_plate_gate)+(NEW.induced_draft_outlet_diffuser_tube)+((((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)))+(NEW.brick_chimney_inlet))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.induced_draft_ducting_length)*((NEW.induced_draft_frictional_resistance_coefficient)*(((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width)))))))
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段smoke_chimney_total_resistance:烟道总阻力,的计算55-----------------------------------
  IF OLD.induced_draft_corrected_turning_angle_coefficient != NEW.induced_draft_corrected_turning_angle_coefficient OR OLD.induced_draft_corrected_height_width_ratio_coefficient != NEW.induced_draft_corrected_height_width_ratio_coefficient OR OLD.induced_draft_original_resistance_coefficient_with_roughness != NEW.induced_draft_original_resistance_coefficient_with_roughness OR OLD.induced_draft_powder_concentration_corrected_coefficient != NEW.induced_draft_powder_concentration_corrected_coefficient OR OLD.brick_chimney_inlet != NEW.brick_chimney_inlet OR OLD.air_preheater_length != NEW.air_preheater_length OR OLD.air_preheater_frictional_resistance_coefficient != NEW.air_preheater_frictional_resistance_coefficient OR OLD.air_preheater_ducting_length != NEW.air_preheater_ducting_length OR OLD.air_preheater_air_elbow_local_resistance_coefficient != NEW.air_preheater_air_elbow_local_resistance_coefficient OR OLD.air_preheater_powder_concentration_corrected_coefficient != NEW.air_preheater_powder_concentration_corrected_coefficient OR OLD.air_preheater_slow_air_local_resistance_coefficient != NEW.air_preheater_slow_air_local_resistance_coefficient OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient != NEW.air_preheater_slow_powder_concentration_corrected_coefficient OR OLD.air_preheater_reducer_tube != NEW.air_preheater_reducer_tube OR OLD.deduster_flow_velocity != NEW.deduster_flow_velocity OR OLD.deduster_length != NEW.deduster_length OR OLD.deduster_frictional_resistance_coefficient != NEW.deduster_frictional_resistance_coefficient OR OLD.deduster_ducting_length != NEW.deduster_ducting_length OR OLD.air_preheater_outlet_smoke_amount != NEW.air_preheater_outlet_smoke_amount OR OLD.deduster_slow_air_local_resistance_coefficient != NEW.deduster_slow_air_local_resistance_coefficient OR OLD.deduster_slow_powder_concentration_corrected_coefficient != NEW.deduster_slow_powder_concentration_corrected_coefficient OR OLD.deduster_corrected_turning_angle_coefficient != NEW.deduster_corrected_turning_angle_coefficient OR OLD.deduster_section_corrected_height_width_ratio_coefficient != NEW.deduster_section_corrected_height_width_ratio_coefficient OR OLD.deduster_section_original_resistance_coefficient_with_roughness != NEW.deduster_section_original_resistance_coefficient_with_roughness OR OLD.air_preheater_density != NEW.air_preheater_density OR OLD.deduster_section_slow_powder_corrected_coefficient != NEW.deduster_section_slow_powder_corrected_coefficient OR OLD.deduster_inlet_bellows != NEW.deduster_inlet_bellows OR OLD.induced_draft_inlet_smoke_amount != NEW.induced_draft_inlet_smoke_amount OR OLD.induced_draft_density != NEW.induced_draft_density OR OLD.induced_draft_flow_velocity != NEW.induced_draft_flow_velocity OR OLD.air_preheater_flow_velocity != NEW.air_preheater_flow_velocity OR OLD.induced_draft_width != NEW.induced_draft_width OR OLD.induced_draft_frictional_resistance_coefficient != NEW.induced_draft_frictional_resistance_coefficient OR OLD.induced_draft_ducting_length != NEW.induced_draft_ducting_length OR OLD.induced_draft_outlet_plate_gate != NEW.induced_draft_outlet_plate_gate OR OLD.induced_draft_outlet_diffuser_tube != NEW.induced_draft_outlet_diffuser_tube THEN
     update gaspowergeneration_smoke_resistance set 

     smoke_chimney_total_resistance=((((NEW.induced_draft_outlet_plate_gate)+(NEW.induced_draft_outlet_diffuser_tube)+((((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)))+(NEW.brick_chimney_inlet))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.induced_draft_ducting_length)*((NEW.induced_draft_frictional_resistance_coefficient)*(((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width))))))))+((((((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)))+((((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)))+(NEW.deduster_inlet_bellows))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.deduster_ducting_length)*((NEW.deduster_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length))))))))+((((((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)))+(((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))))+(NEW.air_preheater_reducer_tube))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.air_preheater_ducting_length)*((NEW.air_preheater_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length))))))))
     where plan_id=NEW.plan_id;

  ELSIF (OLD.brick_chimney_inlet ISNULL OR OLD.induced_draft_powder_concentration_corrected_coefficient ISNULL OR OLD.induced_draft_original_resistance_coefficient_with_roughness ISNULL OR OLD.induced_draft_corrected_height_width_ratio_coefficient ISNULL OR OLD.induced_draft_corrected_turning_angle_coefficient ISNULL OR OLD.induced_draft_outlet_diffuser_tube ISNULL OR OLD.induced_draft_outlet_plate_gate ISNULL OR OLD.induced_draft_ducting_length ISNULL OR OLD.induced_draft_frictional_resistance_coefficient ISNULL OR OLD.induced_draft_width ISNULL OR OLD.induced_draft_flow_velocity ISNULL OR OLD.induced_draft_density ISNULL OR OLD.induced_draft_inlet_smoke_amount ISNULL OR OLD.deduster_inlet_bellows ISNULL OR OLD.deduster_section_slow_powder_corrected_coefficient ISNULL OR OLD.deduster_section_original_resistance_coefficient_with_roughness ISNULL OR OLD.deduster_section_corrected_height_width_ratio_coefficient ISNULL OR OLD.deduster_corrected_turning_angle_coefficient ISNULL OR OLD.deduster_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.deduster_slow_air_local_resistance_coefficient ISNULL OR OLD.deduster_ducting_length ISNULL OR OLD.deduster_frictional_resistance_coefficient ISNULL OR OLD.deduster_length ISNULL OR OLD.deduster_flow_velocity ISNULL OR OLD.air_preheater_reducer_tube ISNULL OR OLD.air_preheater_slow_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_slow_air_local_resistance_coefficient ISNULL OR OLD.air_preheater_powder_concentration_corrected_coefficient ISNULL OR OLD.air_preheater_air_elbow_local_resistance_coefficient ISNULL OR OLD.air_preheater_ducting_length ISNULL OR OLD.air_preheater_frictional_resistance_coefficient ISNULL OR OLD.air_preheater_length ISNULL OR OLD.air_preheater_flow_velocity ISNULL OR OLD.air_preheater_density ISNULL OR OLD.air_preheater_outlet_smoke_amount ISNULL) AND NEW.brick_chimney_inlet NOTNULL AND NEW.induced_draft_powder_concentration_corrected_coefficient NOTNULL AND NEW.induced_draft_original_resistance_coefficient_with_roughness NOTNULL AND NEW.induced_draft_corrected_height_width_ratio_coefficient NOTNULL AND NEW.induced_draft_corrected_turning_angle_coefficient NOTNULL AND NEW.induced_draft_outlet_diffuser_tube NOTNULL AND NEW.induced_draft_outlet_plate_gate NOTNULL AND NEW.induced_draft_ducting_length NOTNULL AND NEW.induced_draft_frictional_resistance_coefficient NOTNULL AND NEW.induced_draft_width NOTNULL AND NEW.induced_draft_flow_velocity NOTNULL AND NEW.induced_draft_density NOTNULL AND NEW.induced_draft_inlet_smoke_amount NOTNULL AND NEW.deduster_inlet_bellows NOTNULL AND NEW.deduster_section_slow_powder_corrected_coefficient NOTNULL AND NEW.deduster_section_original_resistance_coefficient_with_roughness NOTNULL AND NEW.deduster_section_corrected_height_width_ratio_coefficient NOTNULL AND NEW.deduster_corrected_turning_angle_coefficient NOTNULL AND NEW.deduster_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.deduster_slow_air_local_resistance_coefficient NOTNULL AND NEW.deduster_ducting_length NOTNULL AND NEW.deduster_frictional_resistance_coefficient NOTNULL AND NEW.deduster_length NOTNULL AND NEW.deduster_flow_velocity NOTNULL AND NEW.air_preheater_reducer_tube NOTNULL AND NEW.air_preheater_slow_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_slow_air_local_resistance_coefficient NOTNULL AND NEW.air_preheater_powder_concentration_corrected_coefficient NOTNULL AND NEW.air_preheater_air_elbow_local_resistance_coefficient NOTNULL AND NEW.air_preheater_ducting_length NOTNULL AND NEW.air_preheater_frictional_resistance_coefficient NOTNULL AND NEW.air_preheater_length NOTNULL AND NEW.air_preheater_flow_velocity NOTNULL AND NEW.air_preheater_density NOTNULL AND NEW.air_preheater_outlet_smoke_amount NOTNULL THEN
     update gaspowergeneration_smoke_resistance set 

     smoke_chimney_total_resistance=((((NEW.induced_draft_outlet_plate_gate)+(NEW.induced_draft_outlet_diffuser_tube)+((((NEW.induced_draft_corrected_turning_angle_coefficient)*(NEW.induced_draft_corrected_height_width_ratio_coefficient)*(NEW.induced_draft_original_resistance_coefficient_with_roughness))*(NEW.induced_draft_powder_concentration_corrected_coefficient)))+(NEW.brick_chimney_inlet))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.induced_draft_ducting_length)*((NEW.induced_draft_frictional_resistance_coefficient)*(((NEW.induced_draft_density))*((NEW.induced_draft_flow_velocity))^2/2)/(4*((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(2*((NEW.induced_draft_width)+(((NEW.induced_draft_inlet_smoke_amount)/(NEW.induced_draft_flow_velocity)/3600)/(NEW.induced_draft_width))))))))+((((((NEW.deduster_slow_air_local_resistance_coefficient)*(NEW.deduster_slow_powder_concentration_corrected_coefficient)))+((((NEW.deduster_corrected_turning_angle_coefficient)*(NEW.deduster_section_corrected_height_width_ratio_coefficient)*(NEW.deduster_section_original_resistance_coefficient_with_roughness))*(NEW.deduster_section_slow_powder_corrected_coefficient)))+(NEW.deduster_inlet_bellows))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.deduster_ducting_length)*((NEW.deduster_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*(((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(2*((NEW.deduster_length)+((((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(NEW.deduster_flow_velocity)/3600)/(NEW.deduster_length))))))))+((((((NEW.air_preheater_air_elbow_local_resistance_coefficient)*(NEW.air_preheater_powder_concentration_corrected_coefficient)))+(((NEW.air_preheater_slow_air_local_resistance_coefficient)*(1+(NEW.air_preheater_slow_powder_concentration_corrected_coefficient))))+(NEW.air_preheater_reducer_tube))*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2))+((NEW.air_preheater_ducting_length)*((NEW.air_preheater_frictional_resistance_coefficient)*((((NEW.air_preheater_density))*((NEW.air_preheater_flow_velocity))^2)/2)/(4*((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(2*((NEW.air_preheater_length)+(((NEW.air_preheater_outlet_smoke_amount)/(NEW.air_preheater_flow_velocity)/3600)/(NEW.air_preheater_length))))))))
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "gaspowergeneration_smoke_resistance" AFTER UPDATE OF
"induced_draft_corrected_turning_angle_coefficient",
"induced_draft_corrected_height_width_ratio_coefficient",
"induced_draft_original_resistance_coefficient_with_roughness",
"induced_draft_powder_concentration_corrected_coefficient",
"brick_chimney_inlet",
"air_preheater_length",
"air_preheater_absolute_tube_roughness",
"air_preheater_frictional_resistance_coefficient",
"air_preheater_ducting_length",
"air_preheater_air_elbow_local_resistance_coefficient",
"air_preheater_powder_concentration_corrected_coefficient",
"air_preheater_slow_air_local_resistance_coefficient",
"air_preheater_slow_powder_concentration_corrected_coefficient",
"air_preheater_reducer_tube",
"deduster_outlet_calculated_temperature",
"deduster_density",
"deduster_flow_velocity",
"deduster_length",
"air_preheater_outlet_calculated_temperature",
"deduster_absolute_tube_roughness",
"deduster_frictional_resistance_coefficient",
"deduster_ducting_length",
"air_preheater_outlet_smoke_amount",
"deduster_slow_air_local_resistance_coefficient",
"deduster_slow_powder_concentration_corrected_coefficient",
"deduster_corrected_turning_angle_coefficient",
"deduster_section_corrected_height_width_ratio_coefficient",
"deduster_section_original_resistance_coefficient_with_roughness",
"air_preheater_density",
"deduster_section_slow_powder_corrected_coefficient",
"deduster_inlet_bellows",
"induced_draft_inlet_calculated_temperature",
"induced_draft_inlet_smoke_amount",
"induced_draft_density",
"induced_draft_flow_velocity",
"air_preheater_flow_velocity",
"induced_draft_width",
"induced_draft_absolute_tube_roughness",
"induced_draft_frictional_resistance_coefficient",
"induced_draft_ducting_length",
"induced_draft_outlet_plate_gate",
"induced_draft_outlet_diffuser_tube"
ON "public"."gaspowergeneration_smoke_resistance"
FOR EACH ROW
EXECUTE PROCEDURE "gaspowergeneration_smoke_resistance"();

