import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import date

# Load model
model = joblib.load("best_churn_model.pkl")

# Streamlit setup
st.set_page_config(page_title="Churn Predictor", layout="centered")
st.title("📚 Neural Networks for the Publishing Industry")
st.subheader("🎯 Customer Churn Prediction")

st.markdown("Fill in the customer details below to predict if they are likely to churn.")

# Input form
with st.form("prediction_form"):
    buying_duration_days = st.slider("🛒 How many days has the customer been buying books?", 0, 1000, 300)
    days_since_last_order = st.slider("📆 Days since the customer last visited?", 0, 1000, 250)
    order_date = st.date_input("🗓️ Select a recent order date", date.today())
    price = st.slider("💵 Price of the book bought", 0.0, 5000.0, 300.0, step=10.0)
    order_count = st.slider("📦 Number of orders by customer", 0, 50, 3)

    submit = st.form_submit_button("🔍 Predict")

if submit:
    # Prepare dummy features for the model (example: use selected relevant ones)
    input_data = np.array([[order_count, 2, 1, days_since_last_order]])  # example: shipping_variation=2, address_count=1

    # Optional: Debug info
    st.write("📦 Input to model:", input_data)

    # Predict
    prediction = model.predict(input_data)[0]

    st.markdown("---")
    st.subheader("📢 Prediction Result")
    if prediction == 1:
        st.error("⚠️ The customer is **likely to churn**.")
    else:
        st.success("✅ The customer is **not likely to churn**.")

    # Show summary of user inputs
    st.markdown("### 🔍 Customer Input Summary")
    st.write({
        "Buying Duration (days)": buying_duration_days,
        "Days Since Last Order": days_since_last_order,
        "Order Date": order_date.strftime("%Y-%m-%d"),
        "Book Price": price,
        "Order Count": order_count
    })

# Footer
st.markdown("---")
st.caption("Built by Vinoth Kumar | Powered by Streamlit & Machine Learning")