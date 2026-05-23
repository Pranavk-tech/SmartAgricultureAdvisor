import streamlit as st

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Smart Agriculture Assistant")

question=st.text_input(
"Ask your farming question"
)

def generate_response(q):

    q=q.lower()

    if "crop" in q:

        return """
🌾 Crop Recommendation

Go to Crop Recommendation page.

You can get recommendations based on:

✔ Soil nutrients
✔ Weather
✔ Rainfall
✔ Temperature
"""

    elif "weather" in q:

        return """
🌦 Weather Information

Go to Weather page.

You can see:

✔ Temperature
✔ Humidity
✔ Rainfall
✔ Forecast
"""

    elif "disease" in q:

        return """
🍃 Disease Detection

Go to Disease Detection page.

Upload leaf images for prediction.
"""

    elif "yield" in q:

        return """
📈 Yield Prediction

Estimate crop production using ML.
"""

    elif "market" in q:

        return """
💹 Market Analysis

Check:

✔ Crop prices
✔ Trends
✔ Demand
"""

    elif "scheme" in q:

        return """
🏛 Government Schemes

View available farmer schemes.
"""

    else:

        return """
I couldn't understand.

Try:

Crop recommendation

Weather

Disease detection

Yield prediction

Market analysis
"""


if st.button("Ask AI"):

    with st.spinner("Thinking..."):

        response=generate_response(
        question
        )

    st.success(response)