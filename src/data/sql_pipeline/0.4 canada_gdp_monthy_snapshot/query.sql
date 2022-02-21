
drop table if exists stg.canada_gdp_monthy_snapshot;
create table stg.canada_gdp_monthy_snapshot as 
select 
	date(concat("REF_DATE", '-01')) as month_begin_date,
	"North American Industry Classification System (NAICS)" as industry,
	cast("VALUE" as float) * 1000000 as gdp
from src.monthly_gdp mg 
where true 
	and mg."GEO" = 'Canada'
	and mg."Seasonal adjustment" = 'Seasonally adjusted at annual rates'
	and mg."Prices" = '2012 constant prices'