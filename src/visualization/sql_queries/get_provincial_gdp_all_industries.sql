WITH 

gdp_provincial_all_industries as (
    SELECT 
        year_begin_date,
        gdp
    FROM stg.provincial_gdp_yearly_snapshot
    WHERE TRUE 
        AND industry = 'All industries [T001]'
        AND geo = '{geo}'  
        AND year_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
        AND gdp is not null
    ORDER BY year_begin_date desc
)

, population_provincial as (
    SELECT 
        month_begin_date,
        population
    FROM stg.population_monthly_snapshot
    WHERE TRUE 
        AND geo = '{geo}'  
        AND age_group = '15 years and over'
        AND sex = 'Both sexes'
)

SELECT 
    gpai.year_begin_date,
    gpai.gdp,
    gpai.gdp / pop.population as gdp_per_capita
FROM gdp_provincial_all_industries as gpai
LEFT JOIN population_provincial as pop ON gpai.year_begin_date = pop.month_begin_date
order by 1 desc