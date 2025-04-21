import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open("reg.pkl", "rb"))

# Streamlit App
st.set_page_config(page_title="Power Generation Predictor", layout="centered")
st.title("🔋 Power Generation Predictor")
st.write("Enter the environmental data to predict power generation.")

# User Inputs
distance = st.number_input("🌞 Distance to Solar Noon", value=0.0)
temp = st.number_input("🌡️ Temperature", value=0.0)
wind_dir = st.number_input("🧭 Wind Direction", value=0.0)
wind_speed = st.number_input("💨 Wind Speed", value=0.0)
sky_cover = st.number_input("☁️ Sky Cover", value=0.0)
visibility = st.number_input("🔭 Visibility", value=0.0)
humidity = st.number_input("💧 Humidity", value=0.0)
avg_wind = st.number_input("🌬️ Avg Wind Speed (Period)", value=0.0)
avg_pressure = st.number_input("🌡️ Avg Pressure (Period)", value=0.0)

# Predict button
if st.button("Predict Power"):
    input_df = pd.DataFrame([[distance, temp, wind_dir, wind_speed, sky_cover,
                              visibility, humidity, avg_wind, avg_pressure]],
                            columns=[
                                'distance_to_solar_noon', 'temperature', 'wind_direction',
                                'wind_speed', 'sky_cover', 'visibility', 'humidity',
                                'average_wind_speed_period_', 'average_pressure_period_'
                            ])

    # Rename columns to match training data
    input_df.rename(columns={
        'distance_to_solar_noon': 'distance-to-solar-noon',
        'wind_direction': 'wind-direction',
        'wind_speed': 'wind-speed',
        'sky_cover': 'sky-cover',
        'average_wind_speed_period_': 'average-wind-speed-(period)',
        'average_pressure_period_': 'average-pressure-(period)'
    }, inplace=True)

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"🔋 Predicted Power Generation: **{prediction:.2f}** units")
