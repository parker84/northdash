
drop table if exists stg.emissions_yearly_snapshot;
create table stg.emissions_yearly_snapshot as 
select 
	date(concat("REF_DATE", '-01-01')) as year_begin_date,
	ye."GEO" as geo,
	ye."Sector" as sector,
	"VALUE" as yearly_kilotonnes
from src.yearly_emissions as ye 
where true 
	and ye."UOM" = 'Kilotonnes'