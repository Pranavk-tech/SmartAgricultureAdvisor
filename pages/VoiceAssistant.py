import streamlit as st
from voice_utils import speech_to_text
from voice_utils import text_to_speech

st.title("🎤 Smart Agriculture Voice Assistant")

def get_response(question):

    question=question.lower()

    if "crop" in question:

        return "Recommended crops depend on soil nutrients and weather conditions."

    elif "weather" in question:

        return "Open the weather page for live weather updates."

    elif "disease" in question:

        return "Please open disease detection and upload crop images."

    elif "market" in question:

        return "Open market analysis for crop prices."

    else:

        return "Please ask another farming question."


if st.button("🎙 Start Listening"):

    question=speech_to_text()

    st.success(
        f"You said: {question}"
    )

    response=get_response(question)

    st.info(
        f"🤖 {response}"
    )

    audio_file=text_to_speech(
        response
    )

    audio=open(
        audio_file,
        "rb"
    )

    st.audio(
        audio.read(),
        format="audio/mp3"
    )