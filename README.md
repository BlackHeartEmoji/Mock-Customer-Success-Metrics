# Fictional Customer Success Metrics

A practice dataset for exploring customer health, product adoption, renewals, retention, and expansion in a fictional B2B SaaS business.

**All company names, customer records, and metrics are fictional.** The dataset is for learning and portfolio demonstration only.

## What's included

- `data/fictional_customers.csv`: 50 fictional accounts and their customer success metrics.
- `docs/metric_definitions.md`: Field definitions and the health-score methodology.
- `sql/`: Example queries for customer success analysis.
- `analysis_summary.md`: A starter summary of the sample dataset.

## Suggested uses

- Practice SQL queries against account-level data.
- Analyze adoption and engagement signals.
- Identify customers that may need attention before renewal.
- Explore potential expansion opportunities.
- Build a simple Python notebook or dashboard.

## Quick start

Open the CSV in Excel or Google Sheets, or load it in Python:

```python
import pandas as pd

customers = pd.read_csv("data/fictional_customers.csv")
print(customers.head())
print(customers["health_status"].value_counts())
```

## Dataset reference date

Renewal timing is calculated from **October 29, 2026**. If you reuse the dataset later, update the reference date and recalculate `days_to_renewal` and `renewal_status`.

## Notes

This is a synthetic dataset, not a benchmark for real customer success teams. The health score and renewal-risk label are simple examples intended to make the data useful for learning. They are not a validated churn prediction model.


## Interactive dashboard

An interactive dashboard is included in `app.py`. It uses Streamlit and Plotly to display customer health, adoption, renewal timing, and expansion opportunity metrics.

See `docs/run_dashboard.md` for setup instructions. GitHub stores the app's code, but running it locally or deploying it to a hosting service is required to view it as an interactive app.
