import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout="wide")

st.title("📈 Agriculture Market Dashboard")

file_path="data/market/market_prices.csv.csv"

if not os.path.exists(file_path):

    st.error(
    "Market dataset not found"
    )

else:

    df=pd.read_csv(file_path)

    st.success(
    "Market data loaded successfully"
    )

    st.write("---")

    c1,c2,c3=st.columns(3)

    with c1:

        st.metric(
        "Total Records",
        len(df)
        )

    with c2:

        st.metric(
        "Columns",
        len(df.columns)
        )

    with c3:

        numeric=df.select_dtypes(
        include=["int64","float64"]
        )

        st.metric(
        "Numeric Fields",
        len(numeric.columns)
        )

    st.write("---")

    st.subheader(
    "Dataset Preview"
    )

    st.dataframe(
    df.head(50),
    use_container_width=True
    )

    numeric=df.select_dtypes(
    include=["int64","float64"]
    )

    if len(numeric.columns)>0:

        ycol=st.selectbox(
        "Select field",
        numeric.columns
        )

        fig=px.line(
        df,
        y=ycol,
        title=f"{ycol} Trend"
        )

        st.plotly_chart(
        fig,
        use_container_width=True
        )