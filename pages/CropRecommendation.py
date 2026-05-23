
import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Crop Recommendation",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Smart Crop Recommendation")

st.write(
"Enter soil and climate values to get crop recommendations."
)

st.write("---")

# Load model safely

try:

    model=joblib.load(
        "models/crop_model.pkl"
    )

except:

    st.error(
    "Crop model not found.\nPlace crop_model.pkl inside models folder."
    )

    st.stop()


# Input section

c1,c2,c3=st.columns(3)

with c1:

    N=st.number_input(
        "Nitrogen (N)",
        min_value=0,
        max_value=200,
        value=50
    )

    P=st.number_input(
        "Phosphorus (P)",
        min_value=0,
        max_value=200,
        value=50
    )

    K=st.number_input(
        "Potassium (K)",
        min_value=0,
        max_value=200,
        value=50
    )


with c2:

    temperature=st.number_input(
        "Temperature (°C)",
        value=25.0
    )

    humidity=st.number_input(
        "Humidity (%)",
        value=70.0
    )


with c3:

    ph=st.number_input(
        "Soil pH",
        value=6.5
    )

    rainfall=st.number_input(
        "Rainfall (mm)",
        value=150.0
    )


st.write("---")


if st.button("🚀 Recommend Crop"):

    try:

        input_data=np.array([[

            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall

        ]])

        prediction=model.predict(
            input_data
        )

        crop=prediction[0]

        st.success(
            f"🌱 Recommended Crop: {crop}"
        )

        st.write("---")

        st.subheader(
            "🧠 Why this crop was recommended"
        )

        reasons=[]

        if N>50:

            reasons.append(
            "✔ Nitrogen level suitable"
            )

        if P>40:

            reasons.append(
            "✔ Phosphorus level suitable"
            )

        if K>40:

            reasons.append(
            "✔ Potassium level suitable"
            )

        if 20<=temperature<=35:

            reasons.append(
            "✔ Temperature range is ideal"
            )

        if humidity>60:

            reasons.append(
            "✔ Humidity level favorable"
            )

        if 5<=ph<=8:

            reasons.append(
            "✔ Soil pH appropriate"
            )

        if rainfall>100:

            reasons.append(
            "✔ Rainfall level sufficient"
            )

        for r in reasons:

            st.write(r)

        st.write("---")

        st.info(
        "Prediction generated using AI model + soil and climate data."
        )

    except Exception as e:

        st.error(
        f"Prediction Error: {e}"
        )