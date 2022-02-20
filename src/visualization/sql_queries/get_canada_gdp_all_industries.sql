SELECT 
    year_begin_date,
    SUM(gdp) as gdp
FROM stg.provincial_gdp_yearly_snapshot
WHERE TRUE 
    AND year_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    AND industry = 'All industries [T001]'
GROUP BY 1
ORDER BY 1 desc