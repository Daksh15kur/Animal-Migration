import streamlit as st
import pickle
import pandas as pd


# 1. Load the Model
with open('random_forest.pkl', 'rb') as file:
    model = pickle.load(file)

# 2. Define Prediction Function
def predict(input_data):
    prediction = model.predict(input_data)
    return prediction[0]

# 3. Create Streamlit App
st.title("Animal Migration Prediction App")

# 4. Input Fields with Ranges
tempmax = st.number_input("Enter tempmax (20-40):", min_value=20.0, max_value=40.0)
tempmin = st.number_input("Enter tempmin (10-30):", min_value=10.0, max_value=30.0)
temp = st.number_input("Enter temp (15-35):", min_value=15.0, max_value=35.0)
feelslikemax = st.number_input("Enter feelslikemax (20-45):", min_value=20.0, max_value=45.0)
feelslikemin = st.number_input("Enter feelslikemin (10-35):", min_value=10.0, max_value=35.0)
dew = st.number_input("Enter dew (5-25):", min_value=5.0, max_value=25.0)
humidity = st.number_input("Enter humidity (30-90):", min_value=30.0, max_value=90.0)
precip = st.number_input("Enter precip (0-50):", min_value=0.0, max_value=50.0)
precipprob = st.number_input("Enter precipprob (0-100):", min_value=0.0, max_value=100.0)
precipcover = st.number_input("Enter precipcover (0-100):", min_value=0.0, max_value=100.0)
windgust = st.number_input("Enter windgust (0-60):", min_value=0.0, max_value=60.0)
solarradiation = st.number_input("Enter solarradiation (0-300):", min_value=0.0, max_value=300.0)
solarenergy = st.number_input("Enter solarenergy (0-30):", min_value=0.0, max_value=30.0)

# 5. Create Input DataFrame
input_df = pd.DataFrame({
    'tempmax': [tempmax], 'tempmin': [tempmin], 'temp': [temp],
    'feelslikemax': [feelslikemax], 'feelslikemin': [feelslikemin],
    'dew': [dew], 'humidity': [humidity], 'precip': [precip],
    'precipprob': [precipprob], 'precipcover': [precipcover],
    'windgust': [windgust], 'solarradiation': [solarradiation],
    'solarenergy': [solarenergy]
})

# 6. Prediction Button and Output
if st.button("Predict"):
    result = predict(input_df)
    st.success(f"The prediction is: {result}")
