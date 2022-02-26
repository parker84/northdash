SELECT * FROM stg.emissions_yearly_snapshot
WHERE TRUE 
    AND year_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    AND geo = '{geo}'  
    AND sector = 'Total, industries and households'
ORDER BY year_begin_date desc