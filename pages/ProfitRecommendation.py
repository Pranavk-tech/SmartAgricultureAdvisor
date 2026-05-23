import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide"
)

st.title("💰 Smart Crop Profit Recommendation")

df=pd.read_csv(
"data/profit_data.csv"
)

crop=st.selectbox(
"Select Crop",
df["crop"]
)

yield_value=st.number_input(
"Expected Yield (tons/hectare)",
min_value=1.0,
value=3.0
)

if st.button(
"Calculate Profit"
):

    row=df[
    df["crop"]==crop
    ].iloc[0]

    cost=row["cost_per_hectare"]

    revenue=row["market_price"]

    profit=revenue-cost

    c1,c2,c3=st.columns(3)

    with c1:

        st.metric(
        "Estimated Cost",
        f"₹{cost:,.0f}"
        )

    with c2:

        st.metric(
        "Estimated Revenue",
        f"₹{revenue:,.0f}"
        )

    with c3:

        st.metric(
        "Expected Profit",
        f"₹{profit:,.0f}"
        )

    st.success(
    f"Recommended crop profitability calculated for {crop}"
    )