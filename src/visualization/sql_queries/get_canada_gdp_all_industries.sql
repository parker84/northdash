WITH 

gdp_canada_all_industries as (
    SELECT 
        month_begin_date,
        gdp
    FROM stg.canada_gdp_monthly_snapshot
    WHERE TRUE 
        AND industry = 'All industries [T001]'
        AND month_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    ORDER BY month_begin_date desc
)

, population_canada as (
    SELECT 
        month_begin_date,
        population
    FROM stg.population_monthly_snapshot
    WHERE TRUE 
        AND geo = 'Canada'
        AND age_group = '15 years and over'
        AND sex = 'Both sexes'
)

SELECT 
    gcai.month_begin_date,
    gcai.gdp,
    gcai.gdp / pop.population as gdp_per_capita
FROM gdp_canada_all_industries as gcai
LEFT JOIN population_canada as pop USING (month_begin_date)
order by 1 desc