import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("heart_model.pkl")

# Page Config
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

# Title
st.title("❤️ Heart Disease Prediction System")

st.markdown(
    """
    This application predicts the likelihood of heart disease
    using a Machine Learning model.
    """
)

st.divider()

# Sidebar
st.sidebar.header("About")
st.sidebar.write(
    "Built using Logistic Regression and Streamlit."
)

# Inputs
age = st.number_input("Age", min_value=1, max_value=120)

sex = st.selectbox(
    "Sex",
    ["Female", "Male"]
)

cp = st.selectbox(
    "Chest Pain Type",
    [0, 1, 2, 3]
)

trestbps = st.number_input(
    "Resting Blood Pressure"
)

chol = st.number_input(
    "Cholesterol"
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    [0, 1]
)

restecg = st.selectbox(
    "Rest ECG",
    [0, 1, 2]
)

thalach = st.number_input(
    "Maximum Heart Rate"
)

exang = st.selectbox(
    "Exercise Induced Angina",
    [0, 1]
)

oldpeak = st.number_input(
    "Oldpeak",
    step=0.1
)

slope = st.selectbox(
    "Slope",
    [0, 1, 2]
)

ca = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3]
)

thal = st.selectbox(
    "Thalassemia",
    [0, 1, 2, 3]
)

# Convert sex to numeric
sex_value = 1 if sex == "Male" else 0

# Prediction button
# Prediction button
# Prediction button
if st.button("Predict"):

    input_data = np.array([[
        age,
        sex_value,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    prediction = model.predict(input_data)

    st.divider()

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")