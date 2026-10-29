-- Look for combinations of declining usage and low executive engagement.
SELECT
    customer_id,
    company_name,
    product_adoption_pct,
    login_trend,
    usage_change_pct_90d,
    executive_engagement,
    days_since_last_csm_contact,
    health_status
FROM fictional_customers
WHERE login_trend = 'Declining'
  AND executive_engagement = 'Low'
ORDER BY product_adoption_pct ASC;
