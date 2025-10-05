
{{ config(materialized='incremental') }}


/*
- Incremental materialization
- Reference a source defined in the yml file
- Update the source by running the add_data.py script
*/


select
    unixtime,
    personid,
    sum(price) as sum_price
from {{ source('bsg','bronze_data') }}
{% if is_incremental() %}
    -- https://docs.getdbt.com/docs/build/incremental-models
    -- (If event_time is NULL or the table is truncated, the condition will always be true and load all records)
    where unixtime > (select coalesce(max(unixtime), 0) from {{this}})
{% endif %}
group by unixtime, personid


