
{{ config(materialized='table') }}

-- reference to a seed: ref['car_sales']. Here we use a source
select "Manufacturer", count(*) from {{ source('bsg','car_sales') }} group by 1
