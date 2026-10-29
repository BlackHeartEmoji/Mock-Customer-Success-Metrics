-- Find at-risk customers with renewals within the next 90 days.
SELECT
    customer_id,
    company_name,
    customer_segment,
    current_arr_usd,
    health_score,
    days_to_renewal,
    renewal_risk
FROM fictional_customers
WHERE renewal_risk = 'High'
  AND days_to_renewal <= 90
ORDER BY days_to_renewal ASC;
