# Run the Customer Success Dashboard

This is a beginner-friendly interactive dashboard built with Streamlit and Plotly.

## What it shows
- Customer count and current ARR
- Average product adoption
- At-risk account count
- ARR associated with renewals in the next 90 days
- Customer health distribution
- Adoption by segment
- Qualified and proposal-stage expansion potential
- Renewal list and accounts to review first
- Filters for customer segment, industry, and health status

## Run it on your computer

You need Python installed.

1. Extract the project ZIP.
2. Open Terminal and navigate into the extracted `fictional_customer_success_metrics` folder.
3. Create a virtual environment (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the dashboard:

   ```bash
   streamlit run app.py
   ```

6. Streamlit should open the dashboard in your browser. If it doesn't, Terminal will show a local address, usually `http://localhost:8501`.

## If you're new to Terminal
You can skip this for now and upload the files to GitHub first. GitHub stores the code, but it does not automatically run a Streamlit app just because the files are uploaded. To share a live dashboard, you can later deploy it with a service such as Streamlit Community Cloud.

## Notes
- The data is fictional.
- The app can use the included CSV or a different CSV with the same column names.
- The dashboard is an educational prototype, not a production customer success system.
