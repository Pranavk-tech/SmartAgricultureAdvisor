import streamlit as st
import joblib
import numpy as np
import os

st.set_page_config(layout="wide")

st.title("🌾 Yield Prediction")

model_path="models/yield_model.pkl"

if not os.path.exists(model_path):

    st.error(
    "Yield model not found"
    )

    st.info(
    "Run: python train_yield_model.py"
    )

else:

    model=joblib.load(
    model_path
    )

    c1,c2=st.columns(2)

    with c1:

        N=st.slider(
        "Nitrogen",
        0,
        150,
        50
        )

        P=st.slider(
        "Phosphorus",
        0,
        150,
        50
        )

        K=st.slider(
        "Potassium",
        0,
        150,
        50
        )

        temp=st.slider(
        "Temperature",
        0,
        50,
        25
        )

    with c2:

        humidity=st.slider(
        "Humidity",
        0,
        100,
        60
        )

        ph=st.slider(
        "pH",
        0.0,
        14.0,
        7.0
        )

        rainfall=st.slider(
        "Rainfall",
        0,
        500,
        100
        )

    if st.button(
    "Predict Yield"
    ):

        input_data=np.array([[

        N,
        P,
        K,
        temp,
        humidity,
        ph,
        rainfall

        ]])

        prediction=model.predict(
        input_data
        )

        st.success(
        f"Predicted Yield: {round(prediction[0],2)}"
        )