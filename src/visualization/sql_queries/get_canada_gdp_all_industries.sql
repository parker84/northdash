SELECT * FROM stg.canada_gdp_yearly_snapshot
WHERE TRUE 
    AND month_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    AND industry = 'All industries [T001]'
ORDER BY month_begin_date desc