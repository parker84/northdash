SELECT * FROM stg.earnings_monthly_snapshot
WHERE TRUE 
    AND month_begin_date BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    AND geo = '{geo}'  
    AND industry = 'Industrial aggregate excluding unclassified businesses [11-91N]'
ORDER BY month_begin_date desc