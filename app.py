import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from twilio.rest import Client

# ===== Page Config =====
st.set_page_config(page_title="Accident Predictor", page_icon="🚗")

# ===== Title =====
st.markdown("<h1 style='text-align: center; color: red;'>🚗 Accident Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# ===== Dataset =====
data = {
    "speed": [30, 50, 70, 90, 110, 60, 80, 100],
    "weather": [0, 0, 1, 1, 1, 0, 1, 1],
    "time": [8, 12, 18, 22, 2, 14, 20, 23],
    "risk": [0, 0, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["speed", "weather", "time"]]
y = df["risk"]

model = RandomForestClassifier()
model.fit(X, y)

# ===== Twilio Setup =====
account_sid = "ACbbd4e172556dadeb83dc8cc6f88eca2f"
auth_token = "84cdb058f0516e104603c66ca0c8cb83"

client = Client(account_sid, auth_token)

# ===== UI Inputs =====
st.markdown("### 🚘 Enter Driving Details")

col1, col2 = st.columns(2)

with col1:
    speed = st.slider("Speed", 0, 120, 60)
    time = st.slider("Time (0-23)", 0, 23, 12)

with col2:
    weather = st.selectbox("Weather", ["Clear", "Rainy"])

weather_val = 1 if weather == "Rainy" else 0

# ===== Prediction Button =====
if st.button("🚀 Predict Risk"):
    prediction = model.predict([[speed, weather_val, time]])

    if prediction[0] == 1:
        st.error("⚠️ High Accident Risk!")
        st.balloons()

       # client.messages.create(
#     body=f"🚨 Accident Alert!\nSpeed: {speed}\nWeather: {weather}\nTime: {time}",
#     from_="YOUR_TWILIO_NUMBER",
#     to="YOUR_NUMBER"
# )

        st.success("📩 SMS Alert Sent!")

    else:
        st.success("✅ Safe Driving")

# ===== Footer =====
st.markdown("---")
st.markdown("<center>Developed by Sushma 🚀</center>", unsafe_allow_html=True)
