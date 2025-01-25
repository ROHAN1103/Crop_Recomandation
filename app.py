import streamlit as st
import numpy as np
import pandas as pd
import joblib
import math

@st.cache_resource
def load_model_and_scaler():
    model = joblib.load(open("model.pkl", "rb"))  # Replace with your model file name
    scaler = joblib.load(open("scaler.pkl", "rb"))  # Replace with your scaler file name
    return model, scaler

# Load model and scaler
model, scaler = load_model_and_scaler()

crop=['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
pd.DataFrame(crop)

# Streamlit app
st.title(" Crop Recomandation App")
st.write("Recomanding the crop based on its features!")

# Input fields for the features
feature_1 = st.number_input("Nitrogen", min_value=0.0, max_value=140.0, value=70.0)
feature_2 = st.number_input("Phosphorus", min_value=0.0, max_value=145.0, value=72.5)
feature_3 = st.number_input("Pottasium", min_value=0.0, max_value=210.0, value=105.0)
feature_4 = st.number_input("Temperature", min_value=0.0, max_value=45.0, value=22.0)
feature_5 = st.number_input("Humidity", min_value=0.0, max_value=100.0, value=50.0)
feature_6 = st.number_input("pH", min_value=0.0, max_value=10.0, value=6.0)
feature_7 = st.number_input("Rainfall", min_value=0.0, max_value=300.0, value=50.0)

# Prepare the features
to_scaled = np.array([[feature_4, feature_5, feature_6, feature_7]])
scaled_features4 = scaler.transform([[feature_4]])
scaled_features5 = scaler.transform([[feature_5]])
scaled_features6 = scaler.transform([[feature_6]])
scaled_features7 = scaler.transform([[feature_7]])


input_features = np.array([[(feature_1 / 140), (feature_2 / 145), (feature_3 / 210)]])
combined_features = np.concatenate((input_features, scaled_features4, scaled_features5, scaled_features6, scaled_features7), axis=1)
st.write(combined_features)
# Predict button
if st.button("Predict"):
    st.write(combined_features)
    answer = model.predict(combined_features)
    x=np.ceil(answer)
    y=int(x)
    st.write(crop[y])