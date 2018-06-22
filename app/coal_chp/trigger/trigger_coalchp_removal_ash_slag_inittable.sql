CREATE OR REPLACE FUNCTION coalchp_removal_ash_slag_system()
RETURNS TRIGGER AS
$BODY$
BEGIN
----------------------实现字段a_dust_collector_inlet_:除尘器入口（锅炉出口）飞灰量,的计算1-----------------------------------
  IF OLD.a_total_ash_residue_after != NEW.a_total_ash_residue_after OR OLD.a_fly_ash_content != NEW.a_fly_ash_content THEN
     update coalchp_removal_ash_slag_system set 

     a_dust_collector_inlet_=NEW.a_fly_ash_content*NEW.a_total_ash_residue_after
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_fly_ash_content ISNULL OR OLD.a_total_ash_residue_after ISNULL) AND NEW.a_fly_ash_content NOTNULL AND NEW.a_total_ash_residue_after NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_dust_collector_inlet_=NEW.a_fly_ash_content*NEW.a_total_ash_residue_after
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_the_smoke_concentration:标况下除尘器进口烟气浓度,的计算2-----------------------------------
  IF OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ OR OLD.a_the_imported_smoke_volume != NEW.a_the_imported_smoke_volume THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration=NEW.a_dust_collector_inlet_*10^6/NEW.a_the_imported_smoke_volume
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_the_imported_smoke_volume ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_the_imported_smoke_volume NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration=NEW.a_dust_collector_inlet_*10^6/NEW.a_the_imported_smoke_volume
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_the_smoke_concentration_solid:除尘器进口处烟气浓度(实态）,的计算3-----------------------------------
  IF OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ OR OLD.a_the_smoke_volume_flow != NEW.a_the_smoke_volume_flow THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration_solid=NEW.a_dust_collector_inlet_*10^6/NEW.a_the_smoke_volume_flow
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_the_smoke_volume_flow ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_the_smoke_volume_flow NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration_solid=NEW.a_dust_collector_inlet_*10^6/NEW.a_the_smoke_volume_flow
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_the_smoke_concentration_chimney:除尘器（烟囱）出口烟气浓度（标况）,的计算4-----------------------------------
  IF OLD.a_collection_efficiency != NEW.a_collection_efficiency OR OLD.a_the_smoke_concentration != NEW.a_the_smoke_concentration THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration_chimney=NEW.a_the_smoke_concentration*(1-NEW.a_collection_efficiency/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_collection_efficiency ISNULL OR OLD.a_the_smoke_concentration ISNULL) AND NEW.a_collection_efficiency NOTNULL AND NEW.a_the_smoke_concentration NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_the_smoke_concentration_chimney=NEW.a_the_smoke_concentration*(1-NEW.a_collection_efficiency/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_dust_collector_stack:除尘器（烟囱）出口烟气飞灰量（标况）,的计算5-----------------------------------
  IF OLD.a_collection_efficiency != NEW.a_collection_efficiency OR OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ THEN
     update coalchp_removal_ash_slag_system set 

     a_dust_collector_stack=NEW.a_dust_collector_inlet_*(1-NEW.a_collection_efficiency/100)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_collection_efficiency ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_collection_efficiency NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_dust_collector_stack=NEW.a_dust_collector_inlet_*(1-NEW.a_collection_efficiency/100)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_ash_under_dust_collector:除尘器下灰量,的计算6-----------------------------------
  IF OLD.a_collection_efficiency != NEW.a_collection_efficiency OR OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ THEN
     update coalchp_removal_ash_slag_system set 

     a_ash_under_dust_collector=NEW.a_dust_collector_inlet_*NEW.a_collection_efficiency/100
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_collection_efficiency ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_collection_efficiency NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_ash_under_dust_collector=NEW.a_dust_collector_inlet_*NEW.a_collection_efficiency/100
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段a_flue_gas_concentratio:烟囱出口烟气浓度（实态）,的计算7-----------------------------------
  IF OLD.a_collection_efficiency != NEW.a_collection_efficiency OR OLD.a_the_imported_smoke_real_state != NEW.a_the_imported_smoke_real_state OR OLD.a_dust_collector_inlet_ != NEW.a_dust_collector_inlet_ THEN
     update coalchp_removal_ash_slag_system set 

     a_flue_gas_concentratio=NEW.a_dust_collector_inlet_*(1-NEW.a_collection_efficiency/100)*10^6/NEW.a_the_imported_smoke_real_state
     where plan_id=NEW.plan_id;

  ELSIF (OLD.a_the_imported_smoke_real_state ISNULL OR OLD.a_collection_efficiency ISNULL OR OLD.a_dust_collector_inlet_ ISNULL) AND NEW.a_the_imported_smoke_real_state NOTNULL AND NEW.a_collection_efficiency NOTNULL AND NEW.a_dust_collector_inlet_ NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     a_flue_gas_concentratio=NEW.a_dust_collector_inlet_*(1-NEW.a_collection_efficiency/100)*10^6/NEW.a_the_imported_smoke_real_state
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_removal_the_ash_system:除灰系统出力,的计算8-----------------------------------
  IF OLD.a_ash_under_dust_collector != NEW.a_ash_under_dust_collector OR OLD.r_removal_coefficient != NEW.r_removal_coefficient THEN
     update coalchp_removal_ash_slag_system set 

     r_removal_the_ash_system=NEW.a_ash_under_dust_collector*NEW.r_removal_coefficient/1000
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_removal_coefficient ISNULL OR OLD.a_ash_under_dust_collector ISNULL) AND NEW.r_removal_coefficient NOTNULL AND NEW.a_ash_under_dust_collector NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     r_removal_the_ash_system=NEW.a_ash_under_dust_collector*NEW.r_removal_coefficient/1000
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_effective_volume_ash_storage:灰库有效体积,的计算9-----------------------------------
  IF OLD.a_ash_under_dust_collector != NEW.a_ash_under_dust_collector OR OLD.r_dry_ash_accumulation_density != NEW.r_dry_ash_accumulation_density OR OLD.r_slag_accumulation_coefficient != NEW.r_slag_accumulation_coefficient OR OLD.r_stored_ash != NEW.r_stored_ash THEN
     update coalchp_removal_ash_slag_system set 

     r_effective_volume_ash_storage=NEW.a_ash_under_dust_collector/1000*NEW.r_stored_ash*22/NEW.r_dry_ash_accumulation_density/NEW.r_slag_accumulation_coefficient
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_stored_ash ISNULL OR OLD.r_slag_accumulation_coefficient ISNULL OR OLD.r_dry_ash_accumulation_density ISNULL OR OLD.a_ash_under_dust_collector ISNULL) AND NEW.r_stored_ash NOTNULL AND NEW.r_slag_accumulation_coefficient NOTNULL AND NEW.r_dry_ash_accumulation_density NOTNULL AND NEW.a_ash_under_dust_collector NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     r_effective_volume_ash_storage=NEW.a_ash_under_dust_collector/1000*NEW.r_stored_ash*22/NEW.r_dry_ash_accumulation_density/NEW.r_slag_accumulation_coefficient
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段r_height:高度,的计算10-----------------------------------
  IF OLD.r_effective_volume_ash_storage != NEW.r_effective_volume_ash_storage OR OLD.r_dia != NEW.r_dia THEN
     update coalchp_removal_ash_slag_system set 

     r_height=NEW.r_effective_volume_ash_storage/(3.14*(NEW.r_dia/2)^2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.r_dia ISNULL OR OLD.r_effective_volume_ash_storage ISNULL) AND NEW.r_dia NOTNULL AND NEW.r_effective_volume_ash_storage NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     r_height=NEW.r_effective_volume_ash_storage/(3.14*(NEW.r_dia/2)^2)
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段g_air_transport_ash_system:输灰系统耗气量,的计算11-----------------------------------
  IF OLD.r_removal_the_ash_system != NEW.r_removal_the_ash_system OR OLD.g_grey_gas != NEW.g_grey_gas THEN
     update coalchp_removal_ash_slag_system set 

     g_air_transport_ash_system=1.2*NEW.r_removal_the_ash_system*16.67/NEW.g_grey_gas/1.293
     where plan_id=NEW.plan_id;

  ELSIF (OLD.g_grey_gas ISNULL OR OLD.r_removal_the_ash_system ISNULL) AND NEW.g_grey_gas NOTNULL AND NEW.r_removal_the_ash_system NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     g_air_transport_ash_system=1.2*NEW.r_removal_the_ash_system*16.67/NEW.g_grey_gas/1.293
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_output_cold_single_stage:冷渣机的出力（单台）,的计算12-----------------------------------
  IF OLD.s_slag_amount != NEW.s_slag_amount THEN
     update coalchp_removal_ash_slag_system set 

     s_output_cold_single_stage=2.5*NEW.s_slag_amount
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_slag_amount ISNULL) AND NEW.s_slag_amount NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_output_cold_single_stage=2.5*NEW.s_slag_amount
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_slag_removal_system:除渣系统出力,的计算13-----------------------------------
  IF OLD.s_output_cold_single_stage != NEW.s_output_cold_single_stage OR OLD.s_cold_single_stage_count != NEW.s_cold_single_stage_count THEN
     update coalchp_removal_ash_slag_system set 

     s_slag_removal_system=2.5*NEW.s_output_cold_single_stage*NEW.s_cold_single_stage_count
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_cold_single_stage_count ISNULL OR OLD.s_output_cold_single_stage ISNULL) AND NEW.s_cold_single_stage_count NOTNULL AND NEW.s_output_cold_single_stage NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_slag_removal_system=2.5*NEW.s_output_cold_single_stage*NEW.s_cold_single_stage_count
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_high_temperature_belt_conveyor:耐高温带式输送机出力,的计算14-----------------------------------
  IF OLD.s_slag_removal_system != NEW.s_slag_removal_system THEN
     update coalchp_removal_ash_slag_system set 

     s_high_temperature_belt_conveyor=NEW.s_slag_removal_system
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_slag_removal_system ISNULL) AND NEW.s_slag_removal_system NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_high_temperature_belt_conveyor=NEW.s_slag_removal_system
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_slag_storage_volume_effective:渣库有效体积,的计算15-----------------------------------
  IF OLD.s_slag_amount != NEW.s_slag_amount OR OLD.s_cold_slag_accumulation_density != NEW.s_cold_slag_accumulation_density OR OLD.s_slag_accumulation_coefficient != NEW.s_slag_accumulation_coefficient OR OLD.s_sludge_time != NEW.s_sludge_time THEN
     update coalchp_removal_ash_slag_system set 

     s_slag_storage_volume_effective=NEW.s_slag_amount*NEW.s_sludge_time*22/NEW.s_cold_slag_accumulation_density/NEW.s_slag_accumulation_coefficient
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_sludge_time ISNULL OR OLD.s_slag_accumulation_coefficient ISNULL OR OLD.s_cold_slag_accumulation_density ISNULL OR OLD.s_slag_amount ISNULL) AND NEW.s_sludge_time NOTNULL AND NEW.s_slag_accumulation_coefficient NOTNULL AND NEW.s_cold_slag_accumulation_density NOTNULL AND NEW.s_slag_amount NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_slag_storage_volume_effective=NEW.s_slag_amount*NEW.s_sludge_time*22/NEW.s_cold_slag_accumulation_density/NEW.s_slag_accumulation_coefficient
     where plan_id=NEW.plan_id;

  END IF;
----------------------实现字段s_height:高度,的计算16-----------------------------------
  IF OLD.s_slag_storage_volume_effective != NEW.s_slag_storage_volume_effective OR OLD.s_dia != NEW.s_dia THEN
     update coalchp_removal_ash_slag_system set 

     s_height=NEW.s_slag_storage_volume_effective/(3.14*(NEW.s_dia/2)^2)
     where plan_id=NEW.plan_id;

  ELSIF (OLD.s_dia ISNULL OR OLD.s_slag_storage_volume_effective ISNULL) AND NEW.s_dia NOTNULL AND NEW.s_slag_storage_volume_effective NOTNULL THEN
     update coalchp_removal_ash_slag_system set 

     s_height=NEW.s_slag_storage_volume_effective/(3.14*(NEW.s_dia/2)^2)
     where plan_id=NEW.plan_id;

  END IF;
RETURN NULL;
END;
$BODY$
LANGUAGE 'plpgsql' VOLATILE;


--创建触发器
CREATE TRIGGER "coalchp_removal_ash_slag_system" AFTER UPDATE OF
"a_collection_efficiency",
"a_ash_under_dust_collector",
"a_the_imported_smoke_real_state",
"r_removal_coefficient",
"r_removal_the_ash_system",
"r_dry_ash_accumulation_density",
"r_slag_accumulation_coefficient",
"r_stored_ash",
"r_effective_volume_ash_storage",
"r_dia",
"g_grey_gas",
"s_slag_amount",
"a_total_ash_residue_after",
"s_output_cold_single_stage",
"s_cold_single_stage_count",
"s_slag_removal_system",
"s_cold_slag_accumulation_density",
"s_slag_accumulation_coefficient",
"s_sludge_time",
"s_slag_storage_volume_effective",
"s_dia",
"a_fly_ash_content",
"a_dust_collector_inlet_",
"a_the_imported_smoke_volume",
"a_the_smoke_volume_flow",
"a_the_smoke_concentration"
ON "public"."coalchp_removal_ash_slag_system"
FOR EACH ROW
EXECUTE PROCEDURE "coalchp_removal_ash_slag_system"();
