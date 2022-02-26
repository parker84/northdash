drop table if exists stg.population_monthly_snapshot;
create table stg.population_monthly_snapshot as 
select 
	date(concat("REF_DATE", '-01')) as month_begin_date,
	"GEO" as geo,
	"Age group" as age_group,
	"Sex" as sex,
	cast("VALUE" as float) * 1000 as population
from src.monthly_labour_force mlf 
where true
	and "Statistics" = 'Estimate'
	and "Data type" = 'Seasonally adjusted'
	and "UOM" = 'Persons'
	and "Labour force characteristics" = 'Population'