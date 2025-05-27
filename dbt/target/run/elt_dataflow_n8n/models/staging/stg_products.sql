
  create view "dbt_data"."dbt_valmir"."stg_products__dbt_tmp"
    
    
  as (
    -- dbt/models/staging/stg_products.sql

with source as (
    select
        id as product_id,
        title,
        price,
        category,
        description,
        rating_rate,
        rating_count
    from raw.products
)

select * from source
  );