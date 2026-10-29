# Metric Definitions and Methodology

All records in this project are fictional and were created for learning and demonstration purposes. They do not represent real customers, contracts, or company results. Currency is USD.

## Account and revenue fields

- `customer_id`: Fictional unique customer identifier.
- `company_name`: Fictional company name.
- `industry`: Fictional customer's industry.
- `customer_segment`: Enterprise, Mid-Market, or Agency.
- `starting_arr_usd`: Annual recurring revenue at the start of the measurement period.
- `expansion_arr_usd`: New annual recurring revenue added through expansion during the period.
- `contraction_arr_usd`: Annual recurring revenue lost through downsell during the period, stored as a positive amount.
- `current_arr_usd`: Ending ARR, calculated as starting ARR + expansion ARR - contraction ARR.

## Adoption and engagement fields

- `licensed_users`: Number of users with a license.
- `active_users`: Number of users active in the measurement window.
- `product_adoption_pct`: Adoption rate as a percentage. In this sample, it is the active-user share, rounded to a whole percent.
- `login_trend`: Direction of login activity: Increasing, Stable, or Declining.
- `usage_change_pct_90d`: Approximate percentage change in usage over the past 90 days.
- `executive_engagement`: Qualitative assessment of executive engagement: High, Medium, or Low.
- `days_since_last_csm_contact`: Days since the last CSM interaction.
- `support_tickets_90d`: Number of support tickets in the past 90 days.

## Sentiment, renewal, and growth fields

- `nps_score`: Sample customer NPS response on the standard 0-10 scale. A single customer's score is not the same as aggregate NPS.
- `renewal_date`: Fictional contract renewal date.
- `days_to_renewal`: Days between the dataset's reference date (2026-10-29) and renewal date.
- `renewal_status`: Upcoming if renewal is within 90 days; otherwise Scheduled.
- `expansion_potential_usd`: Estimated potential expansion value. This is a fictional opportunity estimate, not booked ARR.
- `expansion_status`: No identified opportunity, Discovery, Qualified, or Proposal.

## Health score

The `health_score` is a sample 0-100 score created from five signals:

- Product adoption: adoption percentage × 0.35, up to 35 points.
- Login trend: Increasing = 25, Stable = 17, Declining = 4 points.
- Executive engagement: High = 20, Medium = 13, Low = 4 points.
- CSM contact recency: 14 days or fewer = 10, 15-30 days = 6, more than 30 days = 2 points.
- Support ticket volume: 0-2 tickets = 10, 3-5 = 6, more than 5 = 1 point.

The sum is rounded to the nearest whole number and capped at 100.

Health bands:
- Healthy: 75-100
- Needs Attention: 50-74
- At Risk: 0-49

Renewal risk is a simple rule-based label for practice, not a predictive model:
- High: At Risk health status, or renewal within 60 days with health score below 70.
- Medium: Health score below 75, or renewal within 90 days.
- Low: Otherwise.

## Important limitations

This is deliberately simplified sample data. In a real CS operation, scoring rules should be calibrated against historical outcomes and reviewed for bias and unintended effects. Health scores are indicators, not substitutes for CSM judgment. NPS is shown at the individual response level, so it should not be described as an account-level or portfolio-level NPS metric without a suitable aggregation method.
