-- Summarize starting ARR, expansion, contraction, and ending ARR.
SELECT
    customer_segment,
    SUM(starting_arr_usd) AS starting_arr_usd,
    SUM(expansion_arr_usd) AS expansion_arr_usd,
    SUM(contraction_arr_usd) AS contraction_arr_usd,
    SUM(current_arr_usd) AS ending_arr_usd
FROM fictional_customers
GROUP BY customer_segment
ORDER BY ending_arr_usd DESC;
