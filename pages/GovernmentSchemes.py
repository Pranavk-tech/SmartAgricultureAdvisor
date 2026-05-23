import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide"
)

st.title("🏛 Government Schemes")

st.write("""
Government schemes and benefits for farmers
""")

schemes=[

{
"Scheme":"PM-KISAN",
"Benefit":"₹6000 yearly financial support",
"Eligibility":"Small and marginal farmers"
},

{
"Scheme":"PMFBY",
"Benefit":"Crop insurance coverage",
"Eligibility":"All eligible farmers"
},

{
"Scheme":"Kisan Credit Card",
"Benefit":"Low-interest agricultural loans",
"Eligibility":"Farmers with land records"
},

{
"Scheme":"Soil Health Card",
"Benefit":"Soil testing and recommendations",
"Eligibility":"All farmers"
},

{
"Scheme":"National Agriculture Market (eNAM)",
"Benefit":"Online crop marketplace",
"Eligibility":"Registered farmers"
},

{
"Scheme":"Micro Irrigation Fund",
"Benefit":"Support for drip irrigation",
"Eligibility":"Farmers using water-saving systems"
}

]

df=pd.DataFrame(
    schemes
)

search=st.text_input(
    "Search Scheme"
)

if search:

    filtered=df[
        df["Scheme"]
        .str.contains(
            search,
            case=False
        )
    ]

    st.dataframe(
        filtered,
        use_container_width=True
    )

else:

    st.dataframe(
        df,
        use_container_width=True
    )

st.write("---")

selected=st.selectbox(
    "Select Scheme",
    df["Scheme"]
)

details=df[
    df["Scheme"]==selected
].iloc[0]

st.subheader(
    selected
)

st.success(
    f"Benefit: {details['Benefit']}"
)

st.info(
    f"Eligibility: {details['Eligibility']}"
)

st.write("---")

st.subheader(
"Farmer Guidance"
)

st.markdown("""

✅ Keep Aadhaar linked

✅ Keep land records updated

✅ Check state agriculture portals

✅ Apply before deadlines

""")