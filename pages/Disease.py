import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

st.set_page_config(layout="wide")

st.title("🦠 Plant Disease Detection")

uploaded=st.file_uploader(
    "Upload leaf image",
    type=["jpg","jpeg","png"]
)

model_path="models/disease_model.h5"

# Automatically read class names from dataset folders
dataset_path="disease_dataset"

if os.path.exists(dataset_path):

    classes=sorted([

        folder for folder in os.listdir(dataset_path)

        if os.path.isdir(
            os.path.join(
                dataset_path,
                folder
            )
        )

    ])

else:

    classes=[]

if uploaded:

    img=Image.open(uploaded)

    st.image(
        img,
        width=300
    )

    if not os.path.exists(model_path):

        st.error(
        "Disease model not found"
        )

    elif len(classes)==0:

        st.error(
        "Disease dataset folders not found"
        )

    else:

        model=load_model(
            model_path
        )

        img=img.resize(
            (128,128)
        )

        arr=np.array(img)

        arr=arr/255.0

        arr=np.expand_dims(
            arr,
            axis=0
        )

        prediction=model.predict(arr)

        index=np.argmax(prediction)

        result=classes[index]

        confidence=round(
            np.max(prediction)*100,
            2
        )

        st.success(
            f"Prediction: {result}"
        )

        st.progress(
            int(confidence)
        )

        st.write(
            f"Confidence: {confidence}%"
        )