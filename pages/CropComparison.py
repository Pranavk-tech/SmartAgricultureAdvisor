import streamlit as st
from utils import load_master_data
import plotly.express as px

st.set_page_config(
    layout="wide"
)

st.title("🌾 Crop Comparison")

df=load_master_data()

if df.empty:

    st.error(
    "Dataset not found"
    )

else:

    if "label" not in df.columns:

        st.error(
        "Crop label column missing"
        )

    else:

        crops=sorted(
        df["label"]
        .dropna()
        .unique()
        )

        c1,c2=st.columns(2)

        with c1:

            crop1=st.selectbox(
            "Select Crop 1",
            crops
            )

        with c2:

            crop2=st.selectbox(
            "Select Crop 2",
            crops,
            index=1
            )

        data1=df[
        df["label"]==crop1
        ]

        data2=df[
        df["label"]==crop2
        ]

        cols=[

        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"

        ]

        avg1=data1[cols].mean()
        avg2=data2[cols].mean()

        compare={

        "Feature":cols,
        crop1:avg1.values,
        crop2:avg2.values

        }

        compare_df=compare

        fig=px.bar(

        compare_df,
        x="Feature",
        y=[crop1,crop2],
        barmode="group",
        title="Crop Requirement Comparison"
        )

        st.plotly_chart(
        fig,
        use_container_width=True
        )

        st.dataframe(
        compare_df,
        use_container_width=True
        )