import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Customer Success Dashboard", page_icon="📊", layout="wide")

st.title("Customer Success Dashboard")
st.caption("Fictional B2B SaaS customer data for learning and portfolio use. All accounts and metrics are synthetic.")

@st.cache_data
def load_data(uploaded_file=None):
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    else:
        data_path = Path(__file__).parent / "data" / "fictional_customers.csv"
        data = pd.read_csv(data_path)
    data["renewal_date"] = pd.to_datetime(data["renewal_date"], errors="coerce")
    return data

uploaded_file = st.sidebar.file_uploader("Optional: upload a customer CSV", type=["csv"])
df = load_data(uploaded_file)

st.sidebar.header("Filters")
segments = sorted(df["customer_segment"].dropna().unique())
selected_segments = st.sidebar.multiselect("Customer segment", segments, default=segments)
industries = sorted(df["industry"].dropna().unique())
selected_industries = st.sidebar.multiselect("Industry", industries, default=industries)
health_options = ["Healthy", "Needs Attention", "At Risk"]
selected_health = st.sidebar.multiselect("Health status", health_options, default=health_options)

filtered = df[
    df["customer_segment"].isin(selected_segments)
    & df["industry"].isin(selected_industries)
    & df["health_status"].isin(selected_health)
].copy()

if filtered.empty:
    st.warning("No customers match these filters. Adjust the filters in the sidebar.")
    st.stop()

total_arr = filtered["current_arr_usd"].sum()
avg_adoption = filtered["product_adoption_pct"].mean()
at_risk_count = (filtered["health_status"] == "At Risk").sum()
upcoming = filtered[filtered["days_to_renewal"] <= 90]
upcoming_arr = upcoming["current_arr_usd"].sum()
expansion_pipeline = filtered.loc[
    filtered["expansion_status"].isin(["Qualified", "Proposal"]),
    "expansion_potential_usd"
].sum()

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Customers", f"{len(filtered):,}")
c2.metric("Current ARR", f"${total_arr:,.0f}")
c3.metric("Average Adoption", f"{avg_adoption:.1f}%")
c4.metric("At-Risk Accounts", f"{at_risk_count:,}")
c5.metric("ARR Renewing in 90 Days", f"${upcoming_arr:,.0f}")

st.divider()

left, middle, right = st.columns([1, 1.2, 1])
with left:
    st.subheader("Customer Health")
    health_counts = (
        filtered["health_status"]
        .value_counts()
        .reindex(["Healthy", "Needs Attention", "At Risk"], fill_value=0)
        .rename_axis("Health Status")
        .reset_index(name="Customers")
    )
    fig = px.pie(health_counts, names="Health Status", values="Customers", hole=0.55)
    fig.update_layout(margin=dict(t=10, b=10, l=5, r=5), legend_title_text="")
    st.plotly_chart(fig, use_container_width=True)

with middle:
    st.subheader("Average Adoption by Segment")
    adoption = (
        filtered.groupby("customer_segment", as_index=False)["product_adoption_pct"]
        .mean()
        .sort_values("product_adoption_pct", ascending=False)
    )
    fig = px.bar(adoption, x="customer_segment", y="product_adoption_pct",
                 labels={"customer_segment": "Segment", "product_adoption_pct": "Average adoption (%)"},
                 text_auto=".1f")
    fig.update_layout(yaxis_range=[0, 100], margin=dict(t=10, b=10, l=5, r=5))
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Expansion Pipeline")
    st.metric("Qualified + Proposal Potential", f"${expansion_pipeline:,.0f}")
    pipeline = (
        filtered[filtered["expansion_status"].isin(["Qualified", "Proposal"])]
        .groupby("expansion_status", as_index=False)["expansion_potential_usd"]
        .sum()
    )
    if not pipeline.empty:
        fig = px.bar(pipeline, x="expansion_status", y="expansion_potential_usd",
                     labels={"expansion_status": "Stage", "expansion_potential_usd": "Potential ($)"},
                     text_auto=",.0f")
        fig.update_layout(margin=dict(t=10, b=10, l=5, r=5))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No qualified or proposal-stage opportunities match these filters.")

st.divider()

st.subheader("Renewals Coming Up in the Next 90 Days")
renewal_view = upcoming.sort_values("days_to_renewal")[
    ["company_name", "customer_segment", "current_arr_usd", "renewal_date",
     "days_to_renewal", "health_score", "health_status", "renewal_risk"]
].copy()
renewal_view = renewal_view.rename(columns={
    "company_name": "Customer",
    "customer_segment": "Segment",
    "current_arr_usd": "Current ARR ($)",
    "renewal_date": "Renewal Date",
    "days_to_renewal": "Days to Renewal",
    "health_score": "Health Score",
    "health_status": "Health Status",
    "renewal_risk": "Renewal Risk"
})
st.dataframe(renewal_view, use_container_width=True, hide_index=True)

st.subheader("Accounts to Review First")
priority = filtered.copy()
priority["priority_reason"] = priority.apply(
    lambda r: "At risk and renewal within 90 days"
    if r["health_status"] == "At Risk" and r["days_to_renewal"] <= 90
    else "At risk"
    if r["health_status"] == "At Risk"
    else "Declining usage + low executive engagement"
    if r["login_trend"] == "Declining" and r["executive_engagement"] == "Low"
    else "Low adoption"
    if r["product_adoption_pct"] < 50
    else "Review",
    axis=1
)
priority = priority[
    (priority["health_status"] == "At Risk")
    | ((priority["login_trend"] == "Declining") & (priority["executive_engagement"] == "Low"))
    | (priority["product_adoption_pct"] < 50)
].sort_values(["days_to_renewal", "health_score"])
priority_view = priority[
    ["company_name", "current_arr_usd", "product_adoption_pct", "login_trend",
     "executive_engagement", "days_to_renewal", "health_score", "priority_reason"]
].rename(columns={
    "company_name": "Customer",
    "current_arr_usd": "Current ARR ($)",
    "product_adoption_pct": "Adoption (%)",
    "login_trend": "Usage Trend",
    "executive_engagement": "Executive Engagement",
    "days_to_renewal": "Days to Renewal",
    "health_score": "Health Score",
    "priority_reason": "Suggested Review Reason"
})
st.dataframe(priority_view, use_container_width=True, hide_index=True)

with st.expander("View all filtered customer records"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)

st.caption("Health scores and renewal-risk labels are simplified rules for practice, not validated predictions. ARR renewal totals show current ARR for accounts with renewals in the next 90 days; they are not a forecast of retained revenue.")
