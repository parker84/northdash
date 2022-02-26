
drop table if exists stg.provincial_gdp_yearly_snapshot;
create table stg.provincial_gdp_yearly_snapshot as 
select 
	date(concat("REF_DATE", '-01-01')) as year_begin_date,
	"GEO" as geo,
	"North American Industry Classification System (NAICS)" as industry,
	cast("VALUE" as float) * 1000000 as gdp
from src.yearly_gdp yg 
where true 
	and yg."UOM" = 'Dollars'
	and yg."Value" = 'Current dollars'