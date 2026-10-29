-- Prioritize qualified/proposal expansion opportunities.
SELECT
    customer_id,
    company_name,
    customer_segment,
    current_arr_usd,
    expansion_potential_usd,
    expansion_status,
    health_status
FROM fictional_customers
WHERE expansion_status IN ('Qualified', 'Proposal')
ORDER BY expansion_potential_usd DESC;
