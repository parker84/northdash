SELECT * FROM stg.low_income_yearly_snapshot
WHERE TRUE 
    AND year_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    AND geo = '{geo}'  
    AND demographic = 'All persons'
ORDER BY year_begin_date desc