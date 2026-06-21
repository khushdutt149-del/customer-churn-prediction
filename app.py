import streamlit as st
import pandas as pd
import pickle

# Load model
with open("customer_churn_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Customer Churn Prediction")

st.title("📊 Customer Churn Prediction System")
st.write("Enter customer details below")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.number_input("Tenure", min_value=0)

phone = st.selectbox("Phone Service", ["Yes", "No"])

multiple = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly = st.number_input("Monthly Charges", min_value=0.0)
total = st.number_input("Total Charges", min_value=0.0)

if st.button("Predict Churn"):

    data = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": senior,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if phone == "Yes" else 0,

        "MultipleLines": {
            "No": 0,
            "No phone service": 1,
            "Yes": 2
        }[multiple],

        "InternetService": {
            "DSL": 0,
            "Fiber optic": 1,
            "No": 2
        }[internet],

        "OnlineSecurity": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[online_security],

        "OnlineBackup": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[online_backup],

        "DeviceProtection": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[device_protection],

        "TechSupport": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[tech_support],

        "StreamingTV": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[streaming_tv],

        "StreamingMovies": {
            "No": 0,
            "No internet service": 1,
            "Yes": 2
        }[streaming_movies],

        "Contract": {
            "Month-to-month": 0,
            "One year": 1,
            "Two year": 2
        }[contract],

        "PaperlessBilling": 1 if paperless == "Yes" else 0,

        "PaymentMethod": {
            "Bank transfer (automatic)": 0,
            "Credit card (automatic)": 1,
            "Electronic check": 2,
            "Mailed check": 3
        }[payment],

        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    if prediction == 1:
        st.error(
            f"⚠️ Customer likely to Churn ({probability[1]*100:.2f}%)"
        )
    else:
        st.success(
            f"✅ Customer likely to Stay ({probability[0]*100:.2f}%)"
        )