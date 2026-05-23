import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import streamlit as st
import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
from PIL import Image
import pyttsx3
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder
import io

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Smart Agriculture Advisor",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>

.main{
background-color:#f5fff5;
}

h1{
color:green;
text-align:center;
}

.stButton>button{
width:100%;
height:45px;
border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

# -------------------------
# LOAD MODELS
# -------------------------

crop_model = joblib.load(
    "models/crop_model.pkl"
)

disease_model = tf.keras.models.load_model(
    "models/disease_model.h5"
)

# -------------------------
# DISEASE LABELS
# -------------------------

disease_classes=[

"Pepper__bell___Bacterial_spot",
"Pepper__bell___healthy",
"Potato___Early_blight",
"Potato___Late_blight",
"Potato___healthy",
"Tomato_Bacterial_spot",
"Tomato_Early_blight",
"Tomato_Late_blight",
"Tomato_Leaf_Mold",
"Tomato_Septoria_leaf_spot",
"Tomato_Spider_mites_Two_spotted_spider_mite",
"Tomato__Target_Spot",
"Tomato__Tomato_YellowLeaf__Curl_Virus",
"Tomato__Tomato_mosaic_virus",
"Tomato_healthy"

]

# -------------------------
# TREATMENTS
# -------------------------

treatments={

"Tomato_Early_blight":
"Remove infected leaves and apply fungicide.",

"Tomato_Late_blight":
"Apply fungicide and remove infected parts.",

"Tomato_healthy":
"Plant is healthy.",

"Potato___Early_blight":
"Apply fungicide and remove affected leaves.",

"Potato___Late_blight":
"Use resistant varieties and fungicides."

}

# -------------------------
# TITLE
# -------------------------

st.markdown(
"<h1>🌱 Smart Agriculture Advisor</h1>",
unsafe_allow_html=True
)

tab1,tab2,tab3=st.tabs(
[
"Crop Recommendation",
"Disease Detection",
"Farmer Assistant"
]
)

# -------------------------
# CROP RECOMMENDATION
# -------------------------

with tab1:

    st.header("Crop Recommendation")

    N=st.number_input("Nitrogen",0,150)
    P=st.number_input("Phosphorus",0,150)
    K=st.number_input("Potassium",0,150)

    temperature=st.number_input(
    "Temperature",
    0.0,50.0
    )

    humidity=st.number_input(
    "Humidity",
    0.0,100.0
    )

    ph=st.number_input(
    "Soil pH",
    0.0,14.0
    )

    rainfall=st.number_input(
    "Rainfall",
    0.0,500.0
    )

    if st.button("Predict Crop"):

        data=pd.DataFrame({

        "N":[N],
        "P":[P],
        "K":[K],
        "temperature":[temperature],
        "humidity":[humidity],
        "ph":[ph],
        "rainfall":[rainfall]

        })

        result=crop_model.predict(
        data
        )

        st.success(
        f"Recommended Crop: {result[0]}"
        )

# -------------------------
# DISEASE DETECTION
# -------------------------

with tab2:

    st.header("Leaf Disease Detection")

    option=st.radio(
    "Choose Input",
    ["Upload Image","Camera"]
    )

    uploaded=None

    if option=="Upload Image":

        uploaded=st.file_uploader(
        "Upload Image",
        type=["jpg","jpeg","png"]
        )

    else:

        uploaded=st.camera_input(
        "Take Picture"
        )

    if uploaded:

        image=Image.open(
        uploaded
        )

        image=image.convert(
        "RGB"
        )

        st.image(image,width=300)

        img=image.resize(
        (128,128)
        )

        img=np.array(img)/255.0

        img=np.expand_dims(
        img,
        axis=0
        )

        prediction=disease_model.predict(
        img
        )

        index=np.argmax(
        prediction
        )

        confidence=np.max(
        prediction
        )*100

        disease=disease_classes[index]

        st.success(
        f"Disease: {disease}"
        )

        st.write(
        f"Confidence: {confidence:.2f}%"
        )

        if disease in treatments:

            st.info(
            treatments[disease]
            )

# -------------------------
# CHATBOT + VOICE
# -------------------------

with tab3:

    st.header("🤖 Farmer Assistant")

    def get_response(question):

        q=question.lower()

        knowledge={

        "rice":"Rice requires high water and warm temperatures.",

        "wheat":"Wheat grows well in cool climates.",

        "tomato":"Tomatoes need moderate watering.",

        "potato":"Potatoes prefer cool conditions.",

        "fertilizer":"Use fertilizer based on soil nutrients.",

        "water":"Water needs depend on crop and weather.",

        "soil":"Healthy soil requires balanced nutrients.",

        "yield":"Yield improves with irrigation and fertilizer.",

        "weather":"Weather affects crop growth.",

        "disease":"Use Disease Detection tab."
        }

        for key in knowledge:

            if key in q:

                return knowledge[key]

        return "I do not have information for this question."

    question=st.text_input(
    "Ask question"
    )

    if st.button("Ask"):

        answer=get_response(question)

        st.success(answer)

        engine=pyttsx3.init()

        engine.say(answer)

        engine.runAndWait()

    st.write("---")

    st.subheader("🎤 Voice Input")

    audio=audio_recorder()

    if audio:

        recognizer=sr.Recognizer()

        try:

            audio_file=sr.AudioFile(
            io.BytesIO(audio)
            )

            with audio_file as source:

                data=recognizer.record(
                source
                )

                text=recognizer.recognize_google(
                data
                )

                st.write(
                f"You said: {text}"
                )

                answer=get_response(
                text
                )

                st.success(answer)

                engine=pyttsx3.init()

                engine.say(answer)

                engine.runAndWait()

        except Exception as e:

            st.error(e)