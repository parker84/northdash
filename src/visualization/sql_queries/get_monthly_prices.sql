SELECT * FROM stg.prices_monthly_snapshot
WHERE TRUE 
    AND month_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    AND geo = '{geo}'  
    AND product_group = 'All-items'
ORDER BY month_begin_date desc