-- dbt/models/marts/mart_dim_produtos.sql

select
    product_id,
    title as product_name,
    category,
    price,
    rating_rate,
    rating_count
from {{ ref('stg_products') }}
