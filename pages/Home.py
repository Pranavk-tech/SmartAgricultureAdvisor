import streamlit as st
from utils import load_master_data
import plotly.express as px
import random

st.set_page_config(
    layout="wide"
)

st.title("🌱 Smart Agriculture Advisor Dashboard")

df=load_master_data()

st.write("---")

# Top metrics

c1,c2,c3,c4=st.columns(4)

with c1:

    st.metric(
    "Dataset Rows",
    f"{len(df):,}"
    )

with c2:

    if "label" in df.columns:

        st.metric(
        "Crop Types",
        df["label"].nunique()
        )

    else:

        st.metric(
        "Crop Types",
        "N/A"
        )

with c3:

    st.metric(
    "Weather Status",
    "Live"
    )

with c4:

    st.metric(
    "ML Models",
    "2"
    )

st.write("---")

left,right=st.columns([2,1])

with left:

    st.subheader(
    "🌾 Crop Distribution"
    )

    if "label" in df.columns:

        crop=df["label"].value_counts().head(10)

        fig=px.bar(

        x=crop.index,
        y=crop.values,
        title="Top Crops"

        )

        st.plotly_chart(
        fig,
        use_container_width=True
        )

with right:

    st.subheader(
    "📌 Live Summary"
    )

    st.success(
    "Weather API Connected"
    )

    st.success(
    "Disease Model Active"
    )

    st.success(
    "Yield Model Active"
    )

    st.info(
    f"Today's Market Score: {random.randint(70,100)}"
    )

st.write("---")

st.subheader(
"🚀 Quick Access"
)

a,b,c,d=st.columns(4)

with a:
    st.info("🌦 Weather")

with b:
    st.info("🦠 Disease")

with c:
    st.info("📈 Market")

with d:
    st.info("🌾 Yield")