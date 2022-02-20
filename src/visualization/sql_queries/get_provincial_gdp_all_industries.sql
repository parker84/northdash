SELECT * FROM stg.provincial_gdp_yearly_snapshot
WHERE TRUE 
    AND year_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    AND geo = '{geo}'  
    AND industry = 'All industries [T001]'
    AND gdp is not null
ORDER BY year_begin_date desc