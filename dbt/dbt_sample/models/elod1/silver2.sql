
{{ config(materialized='table') }}

-- average spend from the latest three transactions

with t_labelled as(
    select
        personid,
        sum_price,
        row_number() over(partition by personid order by unixtime desc nulls last) as rowix
    from {{ ref('silver1') }}
)
select
    personid,
    avg(sum_price) as avg_spend
from t_labelled
where rowix <= 3
group by personid
