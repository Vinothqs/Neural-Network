
# 📚 Neural Networks for the Publishing Industry

This project uses machine learning to help a publishing company understand and predict customer churn. It transforms SQL data into structured CSV files, builds a churn prediction model, and presents the results in an easy-to-use Streamlit dashboard.

---

## 🎯 Objectives

- Predict if a customer will stop purchasing (churn)
- Train multiple ML models and choose the best one
- Build an interactive dashboard to visualize predictions

---

## 🛠️ Tools & Tech

- Python, Pandas, Streamlit
- Optional: Scikit-learn or manual rule-based models
- Data preprocessing, feature engineering, CSV generation

---

## 📂 Dataset Summary

The project starts with 13 `.sql` files and converts them to `.csv`. These include:
- Customers, Orders, Books, Authors, Addresses, etc.

---

## 🧠 Machine Learning

- Feature Engineering: Order count, shipping method variation
- Model Training: Tried multiple models
- Output: `churn_prediction_results.csv`

---

## 📊 Dashboard

Built using Streamlit, the dashboard allows filtering by:
- Order count range
- Churn prediction label (Churned / Not Churned)

To launch the dashboard:

```bash
streamlit run app.py
```

---

## ✅ Project Outcome

- Churn prediction CSV created
- Streamlit dashboard working with filters
- End-to-end ML pipeline completed

---

## 👤 Author

Vinoth Kumar  
GitHub: [vinothqs](https://github.com/vinothqs)

