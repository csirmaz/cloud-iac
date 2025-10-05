
-- This is a data test
-- https://docs.getdbt.com/docs/build/data-tests

select * from {{ ref('car_sales') }} where "Year of manufacture" < 1900
