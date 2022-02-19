
drop table if exists stg.earnings_monthly_snapshot;
create table stg.earnings_monthly_snapshot as 
select 
	date(concat("REF_DATE", '-01')) as month_begin_date,
	"GEO" as geo,
	"North American Industry Classification System (NAICS)" as industry,
	"VALUE" as avg_weekly_earnings
from src.monthly_earnings me 
where true 
	and me."Estimate" = 'Average weekly earnings including overtime for all employees'