import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("placement_model.pkl")

# App title
st.title("🎓 Placement Predictor")

st.write("Enter details below:")

# Inputs
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("IQ", min_value=0, max_value=200, step=1)

# Predict
if st.button("Predict"):
    input_data = np.array([[cgpa, iq]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Student is likely to be Placed")
    else:
        st.error("❌ Student is NOT likely to be Placed")