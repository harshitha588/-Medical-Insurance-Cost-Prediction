
import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("insurance_model.pkl","rb"))

st.title("Medical Insurance Cost Predictor")

st.write("Enter the details below to predict insurance charges.")

age = st.number_input("Age",18,100,30)
bmi = st.number_input("BMI",10.0,50.0,25.0)

smoker = st.selectbox("Smoker",["No","Yes"])
region = st.selectbox("Region",["Southwest","Southeast","Northwest","Northeast"])

# Convert values
smoker = 1 if smoker == "Yes" else 0

region_map = {
"Southwest":0,
"Southeast":1,
"Northwest":2,
"Northeast":3
}

region = region_map[region]

if st.button("Predict Insurance Cost"):
    
    sample = np.array([[age,bmi,smoker,region]])
    
    prediction = model.predict(sample)
    
    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")
