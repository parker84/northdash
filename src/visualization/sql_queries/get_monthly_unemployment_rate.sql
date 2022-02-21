SELECT * FROM stg.unemployment_monthly_snapshot
WHERE TRUE 
    AND month_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    AND geo = '{geo}'  
    AND age_group = '15 years and over'
    AND sex = 'Both sexes'
    AND unemployment_rate is not null --some nulls for some provinces
ORDER BY month_begin_date desc