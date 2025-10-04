
{{ config(materialized='table') }}

-- reference to a seed
select "Manufacturer", count(*) from {{ ref('car_sales') }} group by 1
