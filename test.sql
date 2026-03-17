with event_data as (
    select f.asset_identifier, f.node_id, f.source_name, f.park_unit_id_source, f.fct_asset_event_id
    from plant_asset_events.dw.fct_asset_event__no_join_v1 f
    --where f.park_event_detected_at_local >= dateadd(month, -1, getdate())
),
gda_asset as (
    select u.park_unit_serial_number as serial_number, ut.unit_type_device, u.node_id, u.node_device_id, u.source_name, u.park_unit_id
    from src_gda.foundation.gda__tparkunit_v1 u
      left join src_gda.foundation.gda__tunittype_v1 ut on u.unit_type_id = ut.unit_type_id 
                                                       and ut.source_name = u.source_name 
                                                       and ut.node_id = u.node_id
)
select count(*) as total_rows
     , count(pa.serial_key) as mapped_rows
     , count_if(ga.unit_type_device is null) as gap_asset_type
     , count_if(pa.serial_key is null) as gap
     , total_rows - (select count(*) 
        from event_data
       ) as duplicated_rows
     , count(distinct f.asset_identifier  || '-' || ga.unit_type_device) as cnt_assets
     , count(distinct pa.serial_key || '-' || pa.asset_type)  as cnt_known_assets
     , cnt_assets - cnt_known_assets as cnt_unknown_assets
from event_data f
  left join gda_asset ga on ga.node_id = f.node_id and ga.source_name = f.source_name and ga.park_unit_id = f.park_unit_id_source
  left join fdp_asset.dw.dim_park_asset pa on f.asset_identifier::varchar = pa.serial_number and pa.asset_type = ga.unit_type_device

;