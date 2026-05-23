import speech_recognition as sr
from gtts import gTTS

def speech_to_text():

    r=sr.Recognizer()

    with sr.Microphone() as source:

        audio=r.listen(source)

    try:

        text=r.recognize_google(audio)

        return text

    except:

        return "Could not understand speech"


def text_to_speech(text):

    tts=gTTS(
        text=text,
        lang='en'
    )

    tts.save(
        "response.mp3"
    )

    return "response.mp3"