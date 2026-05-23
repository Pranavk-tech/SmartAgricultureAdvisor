import streamlit as st
from auth import login
from translator_utils import translate_text

st.set_page_config(
    page_title="Smart Agriculture Advisor",
    page_icon="🌱",
    layout="wide"
)

# Load CSS

try:

    with open("style.css") as f:

        st.markdown(
        f"""
        <style>
        {f.read()}
        </style>
        """,
        unsafe_allow_html=True
        )

except:
    pass


# Login state

if "logged_in" not in st.session_state:

    st.session_state["logged_in"]=False


# Login page

if not st.session_state["logged_in"]:

    login()

    st.stop()


# Language selector

languages=[

"English",
"Hindi",
"Kannada",
"Tamil",
"Telugu",
"Malayalam",
"Marathi",
"Gujarati",
"Punjabi",
"Bengali",
"Odia",
"Urdu",
"Assamese",
"Konkani",
"Sanskrit",
"Kashmiri",
"Manipuri",
"Nepali"

]

language=st.sidebar.selectbox(

"🌐 Select Language",
languages

)

st.session_state["language"]=language


# Dashboard Title

st.title(

translate_text(
"🌱 Smart Agriculture Advisor",
language
)

)

st.write("---")


# Welcome message

st.success(

translate_text(
f"Welcome {st.session_state['user']}",
language
)

)


# Information cards

c1,c2,c3=st.columns(3)

with c1:

    st.info(

    translate_text(
    "🌦 Live Weather Updates",
    language
    )

    )

with c2:

    st.info(

    translate_text(
    "🌾 Crop Recommendation System",
    language
    )

    )

with c3:

    st.info(

    translate_text(
    "📈 Market Insights",
    language
    )

    )


st.write("---")


st.subheader(

translate_text(
"🚀 Smart Features",
language
)

)

st.markdown(

translate_text(
"""
✔ Disease Detection

✔ Yield Prediction

✔ Weather Forecast

✔ Market Analysis

✔ AI Assistant

✔ State Insights

✔ Government Schemes

✔ Profit Recommendation
""",
language
)

)


st.write("---")


# Logout

if st.button(

translate_text(
"Logout",
language
)

):

    st.session_state["logged_in"]=False

    st.rerun()