import streamlit as st
import pickle
import numpy as np
import os

st.title("Medical Insurance Cost Predictor")

st.write("Enter the details below to predict insurance charges.")

# Check if model exists

MODEL_PATH = "insurance_model.pkl"

if not os.path.exists(MODEL_PATH):
st.error("Model file 'insurance_model.pkl' not found. Upload it to the same directory as app.py.")
else:
model = pickle.load(open(MODEL_PATH, "rb"))

```
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)

smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox("Region", ["Southwest", "Southeast", "Northwest", "Northeast"])

smoker = 1 if smoker == "Yes" else 0

region_map = {
    "Southwest": 0,
    "Southeast": 1,
    "Northwest": 2,
    "Northeast": 3
}

region = region_map[region]

if st.button("Predict Insurance Cost"):
    try:
        sample = np.array([[age, bmi, smoker, region]])
        prediction = model.predict(sample)
        st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")
```
