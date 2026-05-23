import streamlit as st
import requests

st.set_page_config(
    page_title="Weather",
    layout="wide"
)

st.title("🌦 India Weather Dashboard")

API_KEY=st.secrets["OPENWEATHER_API_KEY"]

state_capitals={

"Andhra Pradesh":"Amaravati",
"Arunachal Pradesh":"Itanagar",
"Assam":"Dispur",
"Bihar":"Patna",
"Chhattisgarh":"Raipur",
"Goa":"Panaji",
"Gujarat":"Gandhinagar",
"Haryana":"Chandigarh",
"Himachal Pradesh":"Shimla",
"Jharkhand":"Ranchi",
"Karnataka":"Bengaluru",
"Kerala":"Thiruvananthapuram",
"Madhya Pradesh":"Bhopal",
"Maharashtra":"Mumbai",
"Manipur":"Imphal",
"Meghalaya":"Shillong",
"Mizoram":"Aizawl",
"Nagaland":"Kohima",
"Odisha":"Bhubaneswar",
"Punjab":"Chandigarh",
"Rajasthan":"Jaipur",
"Sikkim":"Gangtok",
"Tamil Nadu":"Chennai",
"Telangana":"Hyderabad",
"Tripura":"Agartala",
"Uttar Pradesh":"Lucknow",
"Uttarakhand":"Dehradun",
"West Bengal":"Kolkata",

"Andaman and Nicobar Islands":"Port Blair",
"Chandigarh":"Chandigarh",
"Dadra and Nagar Haveli and Daman and Diu":"Daman",
"Delhi":"New Delhi",
"Jammu and Kashmir":"Srinagar",
"Ladakh":"Leh",
"Lakshadweep":"Kavaratti",
"Puducherry":"Puducherry"
}

selected=st.selectbox(
"Select State / UT",
list(state_capitals.keys())
)

city=state_capitals[selected]

if st.button("Get Weather"):

    url=(
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={city},IN"
    f"&appid={API_KEY}"
    f"&units=metric"
    )

    try:

        response=requests.get(url)

        data=response.json()

        if data["cod"]==200:

            temp=data["main"]["temp"]
            humidity=data["main"]["humidity"]
            pressure=data["main"]["pressure"]
            wind=data["wind"]["speed"]
            desc=data["weather"][0]["description"]

            c1,c2,c3,c4=st.columns(4)

            with c1:
                st.metric(
                "Temperature",
                f"{temp}°C"
                )

            with c2:
                st.metric(
                "Humidity",
                f"{humidity}%"
                )

            with c3:
                st.metric(
                "Pressure",
                pressure
                )

            with c4:
                st.metric(
                "Wind",
                f"{wind} m/s"
                )

            st.success(
            f"Condition: {desc}"
            )

            st.write("---")

            st.subheader(
            "🌱 Farming Advice"
            )

            if humidity>80:

                st.warning(
                "High humidity → Monitor fungal diseases"
                )

            elif temp>35:

                st.warning(
                "High temperature → Increase irrigation"
                )

            elif temp<15:

                st.warning(
                "Low temperature → Protect crops"
                )

            else:

                st.success(
                "Weather suitable for farming activities"
                )

        else:

            st.error(
            "Weather not available"
            )

    except Exception as e:

        st.error(e)