import streamlit as st
import pickle
import pandas as pd

# Load the Model
@st.cache_resource
def load_model():
    with open('random_forest.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

# Define Prediction Function
def predict(input_data):
    try:
        prediction = model.predict(input_data)
        return prediction[0]
    except Exception as e:
        return f"Error: {e}"

# Streamlit App UI
st.title("Animal Migration Prediction App")
st.markdown("Enter weather parameters to predict animal migration patterns.")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    tempmax = st.number_input("Temp Max (20-40):", min_value=20.0, max_value=40.0)
    tempmin = st.number_input("Temp Min (10-30):", min_value=10.0, max_value=30.0)
    temp = st.number_input("Temp (15-35):", min_value=15.0, max_value=35.0)
    feelslikemax = st.number_input("Feels Like Max (20-45):", min_value=20.0, max_value=45.0)
    feelslikemin = st.number_input("Feels Like Min (10-35):", min_value=10.0, max_value=35.0)
    dew = st.number_input("Dew (5-25):", min_value=5.0, max_value=25.0)
    humidity = st.number_input("Humidity (30-90):", min_value=30.0, max_value=90.0)

with col2:
    precip = st.number_input("Precipitation (0-50):", min_value=0.0, max_value=50.0)
    precipprob = st.number_input("Precip Probability (0-100):", min_value=0.0, max_value=100.0)
    precipcover = st.number_input("Precip Cover (0-100):", min_value=0.0, max_value=100.0)
    windgust = st.number_input("Wind Gust (0-60):", min_value=0.0, max_value=60.0)
    solarradiation = st.number_input("Solar Radiation (0-300):", min_value=0.0, max_value=300.0)
    solarenergy = st.number_input("Solar Energy (0-30):", min_value=0.0, max_value=30.0)

# Create Input DataFrame
input_df = pd.DataFrame({
    'tempmax': [tempmax], 'tempmin': [tempmin], 'temp': [temp],
    'feelslikemax': [feelslikemax], 'feelslikemin': [feelslikemin],
    'dew': [dew], 'humidity': [humidity], 'precip': [precip],
    'precipprob': [precipprob], 'precipcover': [precipcover],
    'windgust': [windgust], 'solarradiation': [solarradiation],
    'solarenergy': [solarenergy]
})

# Prediction Button
if st.button("Predict"):
    result = predict(input_df)
    st.success(f"The predicted migration status is: {result}")
