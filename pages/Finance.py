import streamlit as st

st.set_page_config(
    layout="wide"
)

st.title("💰 Agriculture Finance Planner")

st.write("""
Estimate farming costs, income, and profit
""")

c1,c2=st.columns(2)

with c1:

    land=st.number_input(
        "Land Area (acres)",
        min_value=1,
        value=1
    )

    seed=st.number_input(
        "Seed Cost (₹)",
        min_value=0,
        value=5000
    )

    fertilizer=st.number_input(
        "Fertilizer Cost (₹)",
        min_value=0,
        value=3000
    )

with c2:

    labor=st.number_input(
        "Labor Cost (₹)",
        min_value=0,
        value=5000
    )

    irrigation=st.number_input(
        "Irrigation Cost (₹)",
        min_value=0,
        value=2000
    )

    expected_income=st.number_input(
        "Expected Income (₹)",
        min_value=0,
        value=25000
    )


if st.button(
    "Calculate"
):

    total_cost=(
        seed+
        fertilizer+
        labor+
        irrigation
    )

    profit=(
        expected_income-
        total_cost
    )

    c1,c2,c3=st.columns(3)

    with c1:

        st.metric(
            "Total Cost",
            f"₹{total_cost:,}"
        )

    with c2:

        st.metric(
            "Expected Income",
            f"₹{expected_income:,}"
        )

    with c3:

        st.metric(
            "Estimated Profit",
            f"₹{profit:,}"
        )

    st.write("---")

    if profit>0:

        st.success(
            "Estimated profit is positive"
        )

    else:

        st.error(
            "Estimated loss expected"
        )

st.write("---")

st.subheader(
    "Farmer Financial Tips"
)

st.info("""

• Track yearly expenses

• Compare crop profitability

• Use crop insurance

• Explore government subsidies

• Maintain emergency reserves

""")