import numpy as np
import pickle
import streamlit as st
weather_model = pickle.load(open("weather_model.sav", "rb"))
def Predict(input_data):
    input_data_num = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_num.reshape(1, -1)
    prediction = weather_model.predict(input_data_reshaped)

    if prediction == 0:
        return "Weather is Cloudy"
    elif prediction == 1:
        return "Weather is Rainy"
    else:
        return "Weather is Sunny"
st.title("Weather Prediction")

col1, col2 = st.columns(2)

with col1:
    Temperature = st.text_input("Enter Temperature (°C)")
    Humidity = st.text_input("Enter Humidity (%)")
    WindSpeed = st.text_input("Enter Wind Speed (km/h)")
    Precipitation = st.text_input("Enter Precipitation")
    CloudCover = st.text_input("Cloud Cover (1: Clear, 2: Partly Cloudy, 3: Overcast)")

with col2:
    AtmosphericPressure = st.text_input("Atmospheric Pressure (hPa)")
    UVIndex = st.text_input("UV Index")
    Season = st.text_input("Season (1: Winter, 2: Spring, 3: Summer)")
    Visibility = st.text_input("Visibility (km)")
    Location = st.text_input("Location (1: Inland, 2: Mountain, 3: Coastal)")
if st.button('Predict Weather'):
    try:
        input_data = (
            float(Temperature), float(Humidity), float(WindSpeed), float(Precipitation), float(CloudCover),
            float(AtmosphericPressure), float(UVIndex), float(Season), float(Visibility), float(Location)
        )
        w_pre = Predict(input_data)
        st.success(w_pre)
    except ValueError:
        st.error("Please enter numeric.")
