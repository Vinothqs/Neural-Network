import streamlit as st
import pandas as pd

# Load churn prediction results
df = pd.read_csv("churn_prediction_results.csv")

# App layout
st.set_page_config(page_title="Churn Prediction Dashboard", layout="wide")
st.title("📚 Neural Networks for the Publishing Industry")
st.header("📊 Customer Churn Prediction Dashboard")
st.markdown("This dashboard visualizes churn prediction results using a rule-based churn model.")

# Sidebar filters
st.sidebar.header("🔎 Filter Options")

# Order Count Slider
order_min = int(df["order_count"].min())
order_max = int(df["order_count"].max())

if order_min != order_max:
    min_order, max_order = st.sidebar.slider(
        "Order Count Range",
        min_value=order_min,
        max_value=order_max,
        value=(order_min, order_max)
    )
    df = df[(df["order_count"] >= min_order) & (df["order_count"] <= max_order)]
else:
    st.sidebar.info(f"⚠️ Order count slider disabled (value = {order_min})")

# Shipping Variation Slider
ship_min = float(df["shipping_variation"].min())
ship_max = float(df["shipping_variation"].max())

if ship_min != ship_max:
    min_ship, max_ship = st.sidebar.slider(
        "Shipping Variation Range",
        min_value=ship_min,
        max_value=ship_max,
        value=(ship_min, ship_max)
    )
    df = df[(df["shipping_variation"] >= min_ship) & (df["shipping_variation"] <= max_ship)]
else:
    st.sidebar.info(f"⚠️ Shipping variation slider disabled (value = {ship_min})")

# Filter by actual churn
churn_filter = st.sidebar.multiselect(
    "Actual Churn Status",
    options=sorted(df["churn"].unique()),
    default=sorted(df["churn"].unique())
)
df = df[df["churn"].isin(churn_filter)]

# Filter by predicted churn
predicted_filter = st.sidebar.multiselect(
    "Predicted Churn Status",
    options=sorted(df["predicted_churn"].unique()),
    default=sorted(df["predicted_churn"].unique())
)
df = df[df["predicted_churn"].isin(predicted_filter)]

# Show filtered data
st.subheader("📋 Filtered Prediction Results")
st.dataframe(df.head(20))

# Metrics
col1, col2 = st.columns(2)
with col1:
    st.metric("Actual Churned Customers", int(df["churn"].sum()))
with col2:
    st.metric("Predicted Churned Customers", int(df["predicted_churn"].sum()))

# Visuals
st.subheader("📈 Actual Churn Distribution")
st.bar_chart(df["churn"].value_counts().rename({0: "Not Churned", 1: "Churned"}))

st.subheader("🤖 Predicted Churn Distribution")
st.bar_chart(df["predicted_churn"].value_counts().rename({0: "Predicted Not Churned", 1: "Predicted Churned"}))

# Download button
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download Filtered Data as CSV", data=csv, file_name="filtered_churn_data.csv", mime='text/csv')