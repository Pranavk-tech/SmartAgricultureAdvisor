import streamlit as st

st.set_page_config(
    layout="wide"
)

st.title("📘 Smart Agriculture Advisor")

st.write("---")

st.header("🌱 Project Overview")

st.write("""
Smart Agriculture Advisor is an AI-powered farming platform
designed to help farmers make data-driven decisions.
""")

st.write("---")

st.subheader("✨ Features")

features=[

"Crop Recommendation",

"Disease Detection",

"Weather Forecast",

"Yield Prediction",

"Market Analysis",

"State Insights",

"AI Assistant",

"Crop Calendar",

"Government Schemes",

"Analytics Dashboard"

]

for f in features:

    st.success(f)

st.write("---")

st.subheader("🧠 Models Used")

st.info(
"""
Random Forest → Yield Prediction

CNN → Disease Detection
"""
)

st.write("---")

st.subheader("📊 Dataset")

st.write(
"""
Dataset Size: 588,000+ rows

Sources:

• Crop recommendation dataset

• Climate dataset

• Market dataset

• Agriculture dataset
"""
)

st.write("---")

st.subheader("🔌 APIs")

st.write("""

OpenWeather API

""")

st.write("---")

st.subheader("🚀 Technologies")

st.write("""

Python

Streamlit

Pandas

Scikit-learn

TensorFlow

Plotly

""")