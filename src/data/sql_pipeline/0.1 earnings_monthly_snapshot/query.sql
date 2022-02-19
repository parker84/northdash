
drop table if exists stg.earnings_monthly_snapshot;
create table stg.earnings_monthly_snapshot as 
select 
	date(concat("REF_DATE", '-01')) as month_begin_date,
	"GEO" as geo,
	"VALUE" as avg_weekly_earnings
from src.monthly_earnings me 
where true 
	and me."Estimate" = 'Average weekly earnings including overtime for all employees'
	and me."North American Industry Classification System (NAICS)" = 'Industrial aggregate excluding unclassified businesses [11-91N]'