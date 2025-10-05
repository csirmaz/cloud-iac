
{{ config(materialized='table') }}

select 1 as type_, *
from {{ ref('my_first_dbt_model') }}

