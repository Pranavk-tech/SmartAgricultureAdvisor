import streamlit as st
from utils import load_master_data
import plotly.express as px

st.set_page_config(
    layout="wide"
)

st.title("📊 Agriculture Analytics")

df=load_master_data()

if df.empty:

    st.error(
        "Dataset not found"
    )

else:

    numeric=df.select_dtypes(
        include=["int64","float64"]
    ).columns.tolist()

    text=df.select_dtypes(
        include=["object"]
    ).columns.tolist()

    c1,c2=st.columns(2)

    with c1:

        if len(text)>0:

            category=st.selectbox(
                "Choose category",
                text
            )

            chart=(
                df[category]
                .astype(str)
                .value_counts()
                .head(10)
            )

            fig=px.bar(
                x=chart.index,
                y=chart.values,
                labels={
                    "x":category,
                    "y":"Count"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with c2:

        if len(numeric)>=2:

            x=st.selectbox(
                "X Axis",
                numeric
            )

            y=st.selectbox(
                "Y Axis",
                numeric,
                index=1
            )

            fig2=px.scatter(
                df,
                x=x,
                y=y
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

    st.write("---")

    st.subheader(
        "Correlation Analysis"
    )

    if len(numeric)>=2:

        corr=df[numeric].corr()

        fig3=px.imshow(
            corr,
            text_auto=True
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    st.write("---")

    st.subheader(
        "Dataset Statistics"
    )

    st.dataframe(
        df.describe(),
        use_container_width=True
    )