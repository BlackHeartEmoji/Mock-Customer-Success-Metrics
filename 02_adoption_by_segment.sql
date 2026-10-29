-- Compare average product adoption by customer segment.
SELECT
    customer_segment,
    COUNT(*) AS customer_count,
    ROUND(AVG(product_adoption_pct), 1) AS avg_adoption_pct,
    ROUND(AVG(health_score), 1) AS avg_health_score
FROM fictional_customers
GROUP BY customer_segment
ORDER BY avg_adoption_pct DESC;
