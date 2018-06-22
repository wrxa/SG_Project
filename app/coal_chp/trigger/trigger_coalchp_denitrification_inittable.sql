CREATE OR REPLACE FUNCTION coalchp_desulfurization_denitrification()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段s_desulfrization_before_so2:脱硫前烟气中的SO2含量,的计算1-----------------------------------
  IF OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_calcu_coal_consume != NEW.s_calcu_coal_consume OR OLD.s_aflame_generate_so2 != NEW.s_aflame_generate_so2 THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_before_so2=2*NEW.s_aflame_generate_so2*NEW.s_calcu_coal_consume*NEW.s_sulfur_design/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_aflame_generate_so2 ISNULL OR OLD.s_calcu_coal_consume ISNULL OR OLD.s_sulfur_design ISNULL) AND NEW.s_aflame_generate_so2 NOTNULL AND NEW.s_calcu_coal_consume NOTNULL AND NEW.s_sulfur_design NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_before_so2=2*NEW.s_aflame_generate_so2*NEW.s_calcu_coal_consume*NEW.s_sulfur_design/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_no_desulfurization_so2:未脱硫前SO2浓度（标态）,的计算2-----------------------------------
  IF OLD.s_desulfrization_before_so2 != NEW.s_desulfrization_before_so2 OR OLD.s_fan_smoke_flow != NEW.s_fan_smoke_flow THEN
     update coalchp_desulfurization_denitrification set 

     s_no_desulfurization_so2=NEW.s_desulfrization_before_so2/NEW.s_fan_smoke_flow*10^6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_fan_smoke_flow ISNULL OR OLD.s_desulfrization_before_so2 ISNULL) AND NEW.s_fan_smoke_flow NOTNULL AND NEW.s_desulfrization_before_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     s_no_desulfurization_so2=NEW.s_desulfrization_before_so2/NEW.s_fan_smoke_flow*10^6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_desulfrization_after_so2:脱硫后SO2浓度（标态）,的计算3-----------------------------------
  IF OLD.s_no_desulfurization_so2 != NEW.s_no_desulfurization_so2 OR OLD.s_desulfurization_efficiency != NEW.s_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_after_so2=(1-NEW.s_desulfurization_efficiency/100)*NEW.s_no_desulfurization_so2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_desulfurization_efficiency ISNULL OR OLD.s_no_desulfurization_so2 ISNULL) AND NEW.s_desulfurization_efficiency NOTNULL AND NEW.s_no_desulfurization_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_after_so2=(1-NEW.s_desulfurization_efficiency/100)*NEW.s_no_desulfurization_so2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_desulfrization_after_discharge_so2:脱硫后SO2排放量（标态）,的计算4-----------------------------------
  IF OLD.s_desulfrization_before_so2 != NEW.s_desulfrization_before_so2 OR OLD.s_desulfurization_efficiency != NEW.s_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_after_discharge_so2=(1-NEW.s_desulfurization_efficiency/100)*NEW.s_desulfrization_before_so2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_desulfurization_efficiency ISNULL OR OLD.s_desulfrization_before_so2 ISNULL) AND NEW.s_desulfurization_efficiency NOTNULL AND NEW.s_desulfrization_before_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     s_desulfrization_after_discharge_so2=(1-NEW.s_desulfurization_efficiency/100)*NEW.s_desulfrization_before_so2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_furnace_concentration:炉内脱硫后SO2浓度,的计算5-----------------------------------
  IF OLD.s_no_desulfurization_so2 != NEW.s_no_desulfurization_so2 OR OLD.s_desulfurization_efficiency != NEW.s_desulfurization_efficiency OR OLD.r_furnace_rate != NEW.r_furnace_rate THEN
     update coalchp_desulfurization_denitrification set 

     r_furnace_concentration=(1-NEW.s_desulfurization_efficiency/100*NEW.r_furnace_rate/100)*NEW.s_no_desulfurization_so2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_furnace_rate ISNULL OR OLD.s_desulfurization_efficiency ISNULL OR OLD.s_no_desulfurization_so2 ISNULL) AND NEW.r_furnace_rate NOTNULL AND NEW.s_desulfurization_efficiency NOTNULL AND NEW.s_no_desulfurization_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_furnace_concentration=(1-NEW.s_desulfurization_efficiency/100*NEW.r_furnace_rate/100)*NEW.s_no_desulfurization_so2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_others_mass:脱除SO2质量,的计算6-----------------------------------
  IF OLD.s_desulfrization_before_so2 != NEW.s_desulfrization_before_so2 OR OLD.s_desulfurization_efficiency != NEW.s_desulfurization_efficiency OR OLD.r_furnace_rate != NEW.r_furnace_rate THEN
     update coalchp_desulfurization_denitrification set 

     r_others_mass=NEW.s_desulfrization_before_so2*NEW.s_desulfurization_efficiency/100*NEW.r_furnace_rate/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_furnace_rate ISNULL OR OLD.s_desulfurization_efficiency ISNULL OR OLD.s_desulfrization_before_so2 ISNULL) AND NEW.r_furnace_rate NOTNULL AND NEW.s_desulfurization_efficiency NOTNULL AND NEW.s_desulfrization_before_so2 NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_others_mass=NEW.s_desulfrization_before_so2*NEW.s_desulfurization_efficiency/100*NEW.r_furnace_rate/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_others_mole:脱除SO2摩尔量,的计算7-----------------------------------
  IF OLD.r_others_mass != NEW.r_others_mass THEN
     update coalchp_desulfurization_denitrification set 

     r_others_mole=NEW.r_others_mass/64
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_others_mass ISNULL) AND NEW.r_others_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_others_mole=NEW.r_others_mass/64
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_nees_caco3_mole:反应所需CaCO3摩尔量,的计算8-----------------------------------
  IF OLD.r_others_mole != NEW.r_others_mole OR OLD.r_calcium_sulfur_rate != NEW.r_calcium_sulfur_rate THEN
     update coalchp_desulfurization_denitrification set 

     r_nees_caco3_mole=NEW.r_calcium_sulfur_rate*NEW.r_others_mole
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_calcium_sulfur_rate ISNULL OR OLD.r_others_mole ISNULL) AND NEW.r_calcium_sulfur_rate NOTNULL AND NEW.r_others_mole NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_nees_caco3_mole=NEW.r_calcium_sulfur_rate*NEW.r_others_mole
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_nees_caco3_mass:反应所需CaCO3质量,的计算9-----------------------------------
  IF OLD.r_nees_caco3_mole != NEW.r_nees_caco3_mole THEN
     update coalchp_desulfurization_denitrification set 

     r_nees_caco3_mass=NEW.r_nees_caco3_mole*100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_nees_caco3_mole ISNULL) AND NEW.r_nees_caco3_mole NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_nees_caco3_mass=NEW.r_nees_caco3_mole*100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_use_caco3_mass:参加反应CaCO3质量,的计算10-----------------------------------
  IF OLD.r_calcium_sulfur_rate != NEW.r_calcium_sulfur_rate OR OLD.r_nees_caco3_mass != NEW.r_nees_caco3_mass THEN
     update coalchp_desulfurization_denitrification set 

     r_use_caco3_mass=NEW.r_nees_caco3_mass/NEW.r_calcium_sulfur_rate
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_nees_caco3_mass ISNULL OR OLD.r_calcium_sulfur_rate ISNULL) AND NEW.r_nees_caco3_mass NOTNULL AND NEW.r_calcium_sulfur_rate NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_use_caco3_mass=NEW.r_nees_caco3_mass/NEW.r_calcium_sulfur_rate
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_generate_coco3_mass:反应生成CaSO4质量,的计算11-----------------------------------
  IF OLD.r_use_caco3_mass != NEW.r_use_caco3_mass THEN
     update coalchp_desulfurization_denitrification set 

     r_generate_coco3_mass=NEW.r_use_caco3_mass/100*136
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_use_caco3_mass ISNULL) AND NEW.r_use_caco3_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_generate_coco3_mass=NEW.r_use_caco3_mass/100*136
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_add_mass:反应后质量增加,的计算12-----------------------------------
  IF OLD.r_use_caco3_mass != NEW.r_use_caco3_mass OR OLD.r_generate_coco3_mass != NEW.r_generate_coco3_mass THEN
     update coalchp_desulfurization_denitrification set 

     r_add_mass=NEW.r_generate_coco3_mass-NEW.r_use_caco3_mass
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_generate_coco3_mass ISNULL OR OLD.r_use_caco3_mass ISNULL) AND NEW.r_generate_coco3_mass NOTNULL AND NEW.r_use_caco3_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_add_mass=NEW.r_generate_coco3_mass-NEW.r_use_caco3_mass
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_coco3_consume:石灰石耗量,的计算13-----------------------------------
  IF OLD.r_nees_caco3_mass != NEW.r_nees_caco3_mass OR OLD.r_caco3_pure != NEW.r_caco3_pure THEN
     update coalchp_desulfurization_denitrification set 

     r_coco3_consume=100*NEW.r_nees_caco3_mass/NEW.r_caco3_pure
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_caco3_pure ISNULL OR OLD.r_nees_caco3_mass ISNULL) AND NEW.r_caco3_pure NOTNULL AND NEW.r_nees_caco3_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_coco3_consume=100*NEW.r_nees_caco3_mass/NEW.r_caco3_pure
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_generate_grey:炉内脱硫产生的灰渣量,的计算14-----------------------------------
  IF OLD.r_add_mass != NEW.r_add_mass OR OLD.r_coco3_consume != NEW.r_coco3_consume THEN
     update coalchp_desulfurization_denitrification set 

     r_generate_grey=NEW.r_coco3_consume+NEW.r_add_mass
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_coco3_consume ISNULL OR OLD.r_add_mass ISNULL) AND NEW.r_coco3_consume NOTNULL AND NEW.r_add_mass NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_generate_grey=NEW.r_coco3_consume+NEW.r_add_mass
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_storage_output:石灰石粉仓出力,的计算15-----------------------------------
  IF OLD.r_coco3_consume != NEW.r_coco3_consume OR OLD.r_storage_time != NEW.r_storage_time THEN
     update coalchp_desulfurization_denitrification set 

     r_storage_output=NEW.r_storage_time*22*NEW.r_coco3_consume
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_storage_time ISNULL OR OLD.r_coco3_consume ISNULL) AND NEW.r_storage_time NOTNULL AND NEW.r_coco3_consume NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_storage_output=NEW.r_storage_time*22*NEW.r_coco3_consume
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_storage_volume:石灰石粉仓体积,的计算16-----------------------------------
  IF OLD.r_storage_output != NEW.r_storage_output OR OLD.r_storage_density != NEW.r_storage_density OR OLD.r_storage_fullness != NEW.r_storage_fullness THEN
     update coalchp_desulfurization_denitrification set 

     r_storage_volume=NEW.r_storage_output/NEW.r_storage_density/NEW.r_storage_fullness
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_storage_fullness ISNULL OR OLD.r_storage_density ISNULL OR OLD.r_storage_output ISNULL) AND NEW.r_storage_fullness NOTNULL AND NEW.r_storage_density NOTNULL AND NEW.r_storage_output NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_storage_volume=NEW.r_storage_output/NEW.r_storage_density/NEW.r_storage_fullness
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_height:高,的计算17-----------------------------------
  IF OLD.r_storage_volume != NEW.r_storage_volume OR OLD.r_diameter != NEW.r_diameter THEN
     update coalchp_desulfurization_denitrification set 

     r_height=NEW.r_storage_volume/3.14/(NEW.r_diameter/2)^2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_diameter ISNULL OR OLD.r_storage_volume ISNULL) AND NEW.r_diameter NOTNULL AND NEW.r_storage_volume NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     r_height=NEW.r_storage_volume/3.14/(NEW.r_diameter/2)^2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_limestone_consume:石灰石消耗量,的计算18-----------------------------------
  IF OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_calcu_coal_consume != NEW.s_calcu_coal_consume OR OLD.d_limestone_pure != NEW.d_limestone_pure OR OLD.d_proportion_ca_s != NEW.d_proportion_ca_s OR OLD.d_desulfurization_efficiency != NEW.d_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     d_limestone_consume=100/32*NEW.s_sulfur_design/100*NEW.s_calcu_coal_consume*NEW.d_desulfurization_efficiency/100*NEW.d_proportion_ca_s/NEW.d_limestone_pure
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_desulfurization_efficiency ISNULL OR OLD.d_proportion_ca_s ISNULL OR OLD.d_limestone_pure ISNULL OR OLD.s_calcu_coal_consume ISNULL OR OLD.s_sulfur_design ISNULL) AND NEW.d_desulfurization_efficiency NOTNULL AND NEW.d_proportion_ca_s NOTNULL AND NEW.d_limestone_pure NOTNULL AND NEW.s_calcu_coal_consume NOTNULL AND NEW.s_sulfur_design NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_limestone_consume=100/32*NEW.s_sulfur_design/100*NEW.s_calcu_coal_consume*NEW.d_desulfurization_efficiency/100*NEW.d_proportion_ca_s/NEW.d_limestone_pure
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_gengrate_coca4:生成CaSO4量,的计算19-----------------------------------
  IF OLD.s_sulfur_design != NEW.s_sulfur_design OR OLD.s_calcu_coal_consume != NEW.s_calcu_coal_consume OR OLD.d_limestone_pure != NEW.d_limestone_pure OR OLD.d_proportion_ca_s != NEW.d_proportion_ca_s OR OLD.d_desulfurization_efficiency != NEW.d_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     d_gengrate_coca4=136/32*NEW.s_sulfur_design/100*NEW.s_calcu_coal_consume*NEW.d_desulfurization_efficiency/100*NEW.d_proportion_ca_s/NEW.d_limestone_pure
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_desulfurization_efficiency ISNULL OR OLD.d_proportion_ca_s ISNULL OR OLD.d_limestone_pure ISNULL OR OLD.s_calcu_coal_consume ISNULL OR OLD.s_sulfur_design ISNULL) AND NEW.d_desulfurization_efficiency NOTNULL AND NEW.d_proportion_ca_s NOTNULL AND NEW.d_limestone_pure NOTNULL AND NEW.s_calcu_coal_consume NOTNULL AND NEW.s_sulfur_design NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_gengrate_coca4=136/32*NEW.s_sulfur_design/100*NEW.s_calcu_coal_consume*NEW.d_desulfurization_efficiency/100*NEW.d_proportion_ca_s/NEW.d_limestone_pure
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段n_input_smoke:引风机进口烟气容积流量（标况）,的计算20-----------------------------------
  IF OLD.s_fan_smoke_flow != NEW.s_fan_smoke_flow THEN
     update coalchp_desulfurization_denitrification set 

     n_input_smoke=NEW.s_fan_smoke_flow
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_fan_smoke_flow ISNULL) AND NEW.s_fan_smoke_flow NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     n_input_smoke=NEW.s_fan_smoke_flow
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段n_before_nox_discharge:脱硝前NOX排放量,的计算21-----------------------------------
  IF OLD.n_before_nox_concentration != NEW.n_before_nox_concentration OR OLD.n_input_smoke != NEW.n_input_smoke THEN
     update coalchp_desulfurization_denitrification set 

     n_before_nox_discharge=NEW.n_before_nox_concentration*NEW.n_input_smoke*10^(-6)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.n_input_smoke ISNULL OR OLD.n_before_nox_concentration ISNULL) AND NEW.n_input_smoke NOTNULL AND NEW.n_before_nox_concentration NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     n_before_nox_discharge=NEW.n_before_nox_concentration*NEW.n_input_smoke*10^(-6)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段n_after_nox_concentration:脱硝后NOX浓度,的计算22-----------------------------------
  IF OLD.n_before_nox_concentration != NEW.n_before_nox_concentration OR OLD.n_desulfurization_efficiency != NEW.n_desulfurization_efficiency THEN
     update coalchp_desulfurization_denitrification set 

     n_after_nox_concentration=(1-NEW.n_desulfurization_efficiency/100)*NEW.n_before_nox_concentration
     where plan_id=NEW.plan_id;

  ELSIF (OLD.n_desulfurization_efficiency ISNULL OR OLD.n_before_nox_concentration ISNULL) AND NEW.n_desulfurization_efficiency NOTNULL AND NEW.n_before_nox_concentration NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     n_after_nox_concentration=(1-NEW.n_desulfurization_efficiency/100)*NEW.n_before_nox_concentration
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段n_after_nox_discharge:脱硝后NOX排放量,的计算23-----------------------------------
  IF OLD.n_desulfurization_efficiency != NEW.n_desulfurization_efficiency OR OLD.n_before_nox_discharge != NEW.n_before_nox_discharge THEN
     update coalchp_desulfurization_denitrification set 

     n_after_nox_discharge=(1-NEW.n_desulfurization_efficiency/100)*NEW.n_before_nox_discharge
     where plan_id=NEW.plan_id;

  ELSIF (OLD.n_before_nox_discharge ISNULL OR OLD.n_desulfurization_efficiency ISNULL) AND NEW.n_before_nox_discharge NOTNULL AND NEW.n_desulfurization_efficiency NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     n_after_nox_discharge=(1-NEW.n_desulfurization_efficiency/100)*NEW.n_before_nox_discharge
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_denitration_quality:炉内脱硝量,的计算24-----------------------------------
  IF OLD.n_before_nox_discharge != NEW.n_before_nox_discharge OR OLD.n_after_nox_discharge != NEW.n_after_nox_discharge OR OLD.d_denitration_percentage != NEW.d_denitration_percentage THEN
     update coalchp_desulfurization_denitrification set 

     d_denitration_quality=(NEW.n_before_nox_discharge-NEW.n_after_nox_discharge)*NEW.d_denitration_percentage/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_denitration_percentage ISNULL OR OLD.n_after_nox_discharge ISNULL OR OLD.n_before_nox_discharge ISNULL) AND NEW.d_denitration_percentage NOTNULL AND NEW.n_after_nox_discharge NOTNULL AND NEW.n_before_nox_discharge NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_denitration_quality=(NEW.n_before_nox_discharge-NEW.n_after_nox_discharge)*NEW.d_denitration_percentage/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_after_nox_discharge:炉内脱硝后NOX排放量,的计算25-----------------------------------
  IF OLD.n_before_nox_discharge != NEW.n_before_nox_discharge OR OLD.d_denitration_quality != NEW.d_denitration_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_after_nox_discharge=NEW.n_before_nox_discharge-NEW.d_denitration_quality
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_denitration_quality ISNULL OR OLD.n_before_nox_discharge ISNULL) AND NEW.d_denitration_quality NOTNULL AND NEW.n_before_nox_discharge NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_after_nox_discharge=NEW.n_before_nox_discharge-NEW.d_denitration_quality
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_denitration_molar:炉内脱硝摩尔量,的计算26-----------------------------------
  IF OLD.d_denitration_quality != NEW.d_denitration_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_denitration_molar=NEW.d_denitration_quality/46
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_denitration_quality ISNULL) AND NEW.d_denitration_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_denitration_molar=NEW.d_denitration_quality/46
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_escape_quality:氨逃逸量,的计算27-----------------------------------
  IF OLD.n_input_smoke != NEW.n_input_smoke OR OLD.d_escape_rate != NEW.d_escape_rate THEN
     update coalchp_desulfurization_denitrification set 

     d_escape_quality=NEW.d_escape_rate*NEW.n_input_smoke/10^6
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_escape_rate ISNULL OR OLD.n_input_smoke ISNULL) AND NEW.d_escape_rate NOTNULL AND NEW.n_input_smoke NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_escape_quality=NEW.d_escape_rate*NEW.n_input_smoke/10^6
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_escape_quality_urea:逃逸氨折算尿素量,的计算28-----------------------------------
  IF OLD.d_escape_quality != NEW.d_escape_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_escape_quality_urea=NEW.d_escape_quality/34*60
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_escape_quality ISNULL) AND NEW.d_escape_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_escape_quality_urea=NEW.d_escape_quality/34*60
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_urea_nox_molar:尿素/NOX摩尔比,的计算29-----------------------------------
  IF OLD.d_nh3nox_molar != NEW.d_nh3nox_molar THEN
     update coalchp_desulfurization_denitrification set 

     d_urea_nox_molar=NEW.d_nh3nox_molar/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_nh3nox_molar ISNULL) AND NEW.d_nh3nox_molar NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_urea_nox_molar=NEW.d_nh3nox_molar/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_theory_urea:理论尿素消耗量,的计算30-----------------------------------
  IF OLD.d_denitration_quality != NEW.d_denitration_quality OR OLD.d_urea_nox_molar != NEW.d_urea_nox_molar OR OLD.d_urea_nox_quality != NEW.d_urea_nox_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_theory_urea=NEW.d_denitration_quality*NEW.d_urea_nox_quality*NEW.d_urea_nox_molar
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_urea_nox_quality ISNULL OR OLD.d_urea_nox_molar ISNULL OR OLD.d_denitration_quality ISNULL) AND NEW.d_urea_nox_quality NOTNULL AND NEW.d_urea_nox_molar NOTNULL AND NEW.d_denitration_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_theory_urea=NEW.d_denitration_quality*NEW.d_urea_nox_quality*NEW.d_urea_nox_molar
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_use_urea:尿素用量(一台炉),的计算31-----------------------------------
  IF OLD.d_denitration_quality != NEW.d_denitration_quality OR OLD.d_escape_quality_urea != NEW.d_escape_quality_urea OR OLD.d_urea_nox_molar != NEW.d_urea_nox_molar OR OLD.d_urea_nox_quality != NEW.d_urea_nox_quality THEN
     update coalchp_desulfurization_denitrification set 

     d_use_urea=NEW.d_denitration_quality*NEW.d_urea_nox_quality*NEW.d_urea_nox_molar+NEW.d_escape_quality_urea
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_urea_nox_quality ISNULL OR OLD.d_urea_nox_molar ISNULL OR OLD.d_escape_quality_urea ISNULL OR OLD.d_denitration_quality ISNULL) AND NEW.d_urea_nox_quality NOTNULL AND NEW.d_urea_nox_molar NOTNULL AND NEW.d_escape_quality_urea NOTNULL AND NEW.d_denitration_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_use_urea=NEW.d_denitration_quality*NEW.d_urea_nox_quality*NEW.d_urea_nox_molar+NEW.d_escape_quality_urea
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_water_urea:尿素溶液消耗水量(一台炉),的计算32-----------------------------------
  IF OLD.d_use_urea != NEW.d_use_urea THEN
     update coalchp_desulfurization_denitrification set 

     d_water_urea=NEW.d_use_urea*95/5
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_use_urea ISNULL) AND NEW.d_use_urea NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_water_urea=NEW.d_use_urea*95/5
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段d_capacity_urea:尿素仓库容量,的计算33-----------------------------------
  IF OLD.d_use_urea != NEW.d_use_urea OR OLD.d_days_urea != NEW.d_days_urea THEN
     update coalchp_desulfurization_denitrification set 

     d_capacity_urea=NEW.d_days_urea*NEW.d_use_urea*24/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_days_urea ISNULL OR OLD.d_use_urea ISNULL) AND NEW.d_days_urea NOTNULL AND NEW.d_use_urea NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     d_capacity_urea=NEW.d_days_urea*NEW.d_use_urea*24/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_denitration_percentage:烟气脱硝百分比,的计算34-----------------------------------
  IF OLD.d_denitration_percentage != NEW.d_denitration_percentage THEN
     update coalchp_desulfurization_denitrification set 

     g_denitration_percentage=100-NEW.d_denitration_percentage
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_denitration_percentage ISNULL) AND NEW.d_denitration_percentage NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_denitration_percentage=100-NEW.d_denitration_percentage
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_after_nox_discharge:烟气脱硝后NOX排放量,的计算35-----------------------------------
  IF OLD.n_after_nox_discharge != NEW.n_after_nox_discharge THEN
     update coalchp_desulfurization_denitrification set 

     g_after_nox_discharge=NEW.n_after_nox_discharge
     where plan_id=NEW.plan_id;

  ELSIF (OLD.n_after_nox_discharge ISNULL) AND NEW.n_after_nox_discharge NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_after_nox_discharge=NEW.n_after_nox_discharge
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_denitration_quality:烟气脱硝量,的计算36-----------------------------------
  IF OLD.n_after_nox_discharge != NEW.n_after_nox_discharge OR OLD.d_after_nox_discharge != NEW.d_after_nox_discharge THEN
     update coalchp_desulfurization_denitrification set 

     g_denitration_quality=NEW.d_after_nox_discharge-NEW.n_after_nox_discharge
     where plan_id=NEW.plan_id;

  ELSIF (OLD.d_after_nox_discharge ISNULL OR OLD.n_after_nox_discharge ISNULL) AND NEW.d_after_nox_discharge NOTNULL AND NEW.n_after_nox_discharge NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_denitration_quality=NEW.d_after_nox_discharge-NEW.n_after_nox_discharge
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_escape_quality:氨逃逸量,的计算37-----------------------------------
  IF OLD.n_input_smoke != NEW.n_input_smoke OR OLD.g_escape_rate != NEW.g_escape_rate THEN
     update coalchp_desulfurization_denitrification set 

     g_escape_quality=NEW.g_escape_rate*NEW.n_input_smoke/10^6*10^3/22.4*17/10^3
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_escape_rate ISNULL OR OLD.n_input_smoke ISNULL) AND NEW.g_escape_rate NOTNULL AND NEW.n_input_smoke NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_escape_quality=NEW.g_escape_rate*NEW.n_input_smoke/10^6*10^3/22.4*17/10^3
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_escape_quality_urea:逃逸氨折算尿素量,的计算38-----------------------------------
  IF OLD.g_escape_quality != NEW.g_escape_quality THEN
     update coalchp_desulfurization_denitrification set 

     g_escape_quality_urea=NEW.g_escape_quality/34*60
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_escape_quality ISNULL) AND NEW.g_escape_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_escape_quality_urea=NEW.g_escape_quality/34*60
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_urea_nox_molar:尿素/NOX摩尔比,的计算39-----------------------------------
  IF OLD.g_nh3nox_molar != NEW.g_nh3nox_molar THEN
     update coalchp_desulfurization_denitrification set 

     g_urea_nox_molar=NEW.g_nh3nox_molar/2
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_nh3nox_molar ISNULL) AND NEW.g_nh3nox_molar NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_urea_nox_molar=NEW.g_nh3nox_molar/2
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_theory_urea:理论尿素消耗量,的计算40-----------------------------------
  IF OLD.g_denitration_quality != NEW.g_denitration_quality OR OLD.g_urea_nox_molar != NEW.g_urea_nox_molar OR OLD.g_urea_nox_quality != NEW.g_urea_nox_quality THEN
     update coalchp_desulfurization_denitrification set 

     g_theory_urea=NEW.g_denitration_quality*NEW.g_urea_nox_molar*NEW.g_urea_nox_quality
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_urea_nox_quality ISNULL OR OLD.g_urea_nox_molar ISNULL OR OLD.g_denitration_quality ISNULL) AND NEW.g_urea_nox_quality NOTNULL AND NEW.g_urea_nox_molar NOTNULL AND NEW.g_denitration_quality NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_theory_urea=NEW.g_denitration_quality*NEW.g_urea_nox_molar*NEW.g_urea_nox_quality
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_use_urea:尿素用量(一台炉),的计算41-----------------------------------
  IF OLD.g_escape_quality_urea != NEW.g_escape_quality_urea OR OLD.g_theory_urea != NEW.g_theory_urea THEN
     update coalchp_desulfurization_denitrification set 

     g_use_urea=NEW.g_escape_quality_urea+NEW.g_theory_urea
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_theory_urea ISNULL OR OLD.g_escape_quality_urea ISNULL) AND NEW.g_theory_urea NOTNULL AND NEW.g_escape_quality_urea NOTNULL THEN
     update coalchp_desulfurization_denitrification set 

     g_use_urea=NEW.g_escape_quality_urea+NEW.g_theory_urea
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_desulfurization_denitrification" AFTER UPDATE OF
"s_sulfur_design",
"s_calcu_coal_consume",
"s_aflame_generate_so2",
"s_desulfrization_before_so2",
"s_fan_smoke_flow",
"s_no_desulfurization_so2",
"s_desulfurization_efficiency",
"r_furnace_rate",
"r_others_mass",
"r_others_mole",
"r_calcium_sulfur_rate",
"r_nees_caco3_mole",
"r_nees_caco3_mass",
"r_use_caco3_mass",
"r_generate_coco3_mass",
"r_add_mass",
"r_caco3_pure",
"r_coco3_consume",
"r_storage_time",
"r_storage_output",
"r_storage_density",
"r_storage_fullness",
"r_storage_volume",
"r_diameter",
"d_limestone_pure",
"d_proportion_ca_s",
"d_desulfurization_efficiency",
"n_before_nox_concentration",
"n_input_smoke",
"n_desulfurization_efficiency",
"n_before_nox_discharge",
"n_after_nox_discharge",
"d_denitration_percentage",
"d_denitration_quality",
"d_after_nox_discharge",
"d_escape_rate",
"d_escape_quality",
"d_escape_quality_urea",
"d_nh3nox_molar",
"d_urea_nox_molar",
"d_urea_nox_quality",
"d_use_urea",
"d_days_urea",
"g_denitration_quality",
"g_escape_rate",
"g_escape_quality",
"g_escape_quality_urea",
"g_nh3nox_molar",
"g_urea_nox_molar",
"g_urea_nox_quality",
"g_theory_urea"
ON "public"."coalchp_desulfurization_denitrification"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_desulfurization_denitrification"();
