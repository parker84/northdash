drop table if exists stg.prices_monthly_snapshot;
create table stg.prices_monthly_snapshot as 
select 
	date(concat("REF_DATE", '-01')) as month_begin_date,
	"GEO" as geo,
	"Products and product groups" as product_group,
	cast("VALUE" as float) as consumer_price_index
from src.monthly_prices 
where true
	AND "UOM" = '2002=100'