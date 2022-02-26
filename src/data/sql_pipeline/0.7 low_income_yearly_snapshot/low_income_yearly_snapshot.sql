drop table if exists stg.low_income_yearly_snapshot;
create table stg.low_income_yearly_snapshot as 
select 
	date(concat("REF_DATE", '-01-01')) as year_begin_date,
	"GEO" as geo,
	"Persons in low income" as demographic,
	cast("VALUE" as float) as low_income_rate
from src.yearly_low_income 
where true
	and "Statistics" = 'Percentage of persons in low income'
	and "Low income lines" = 'Low income measure after tax'