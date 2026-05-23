import streamlit as st

st.set_page_config(
    page_title="State Insights",
    page_icon="📍",
    layout="wide"
)

st.title("📍 State Agriculture Insights")

state_data={

"Andhra Pradesh":{"crop":"Rice, Cotton","rainfall":"912 mm","soil":"Red Soil"},
"Arunachal Pradesh":{"crop":"Rice, Maize","rainfall":"2782 mm","soil":"Mountain Soil"},
"Assam":{"crop":"Rice, Tea","rainfall":"2818 mm","soil":"Alluvial Soil"},
"Bihar":{"crop":"Rice, Wheat, Maize","rainfall":"1205 mm","soil":"Alluvial Soil"},
"Chhattisgarh":{"crop":"Rice","rainfall":"1292 mm","soil":"Red Soil"},
"Goa":{"crop":"Rice, Coconut","rainfall":"3005 mm","soil":"Laterite Soil"},
"Gujarat":{"crop":"Cotton, Groundnut","rainfall":"852 mm","soil":"Black Soil"},
"Haryana":{"crop":"Wheat, Rice","rainfall":"617 mm","soil":"Alluvial Soil"},
"Himachal Pradesh":{"crop":"Apple, Maize","rainfall":"1251 mm","soil":"Mountain Soil"},
"Jharkhand":{"crop":"Rice","rainfall":"1200 mm","soil":"Red Soil"},
"Karnataka":{"crop":"Ragi, Rice","rainfall":"1248 mm","soil":"Red Soil"},
"Kerala":{"crop":"Coconut, Rubber","rainfall":"3055 mm","soil":"Laterite Soil"},
"Madhya Pradesh":{"crop":"Soybean, Wheat","rainfall":"1017 mm","soil":"Black Soil"},
"Maharashtra":{"crop":"Cotton, Sugarcane","rainfall":"1136 mm","soil":"Black Soil"},
"Manipur":{"crop":"Rice","rainfall":"1467 mm","soil":"Mountain Soil"},
"Meghalaya":{"crop":"Rice, Potato","rainfall":"2818 mm","soil":"Laterite Soil"},
"Mizoram":{"crop":"Rice","rainfall":"2540 mm","soil":"Mountain Soil"},
"Nagaland":{"crop":"Rice","rainfall":"1801 mm","soil":"Mountain Soil"},
"Odisha":{"crop":"Rice","rainfall":"1451 mm","soil":"Red Soil"},
"Punjab":{"crop":"Wheat, Rice","rainfall":"649 mm","soil":"Alluvial Soil"},
"Rajasthan":{"crop":"Wheat, Bajra","rainfall":"531 mm","soil":"Desert Soil"},
"Sikkim":{"crop":"Cardamom","rainfall":"2739 mm","soil":"Mountain Soil"},
"Tamil Nadu":{"crop":"Rice, Banana","rainfall":"945 mm","soil":"Red Soil"},
"Telangana":{"crop":"Cotton, Rice","rainfall":"906 mm","soil":"Black Soil"},
"Tripura":{"crop":"Rice","rainfall":"2200 mm","soil":"Laterite Soil"},
"Uttar Pradesh":{"crop":"Wheat, Sugarcane","rainfall":"990 mm","soil":"Alluvial Soil"},
"Uttarakhand":{"crop":"Rice, Wheat","rainfall":"1400 mm","soil":"Mountain Soil"},
"West Bengal":{"crop":"Rice, Jute","rainfall":"1750 mm","soil":"Alluvial Soil"},

"Andaman and Nicobar Islands":{"crop":"Coconut","rainfall":"3000 mm","soil":"Laterite Soil"},
"Chandigarh":{"crop":"Wheat","rainfall":"1110 mm","soil":"Alluvial Soil"},
"Dadra and Nagar Haveli and Daman and Diu":{"crop":"Rice","rainfall":"2000 mm","soil":"Black Soil"},
"Delhi":{"crop":"Wheat","rainfall":"800 mm","soil":"Alluvial Soil"},
"Jammu and Kashmir":{"crop":"Apple, Rice","rainfall":"1115 mm","soil":"Mountain Soil"},
"Ladakh":{"crop":"Barley","rainfall":"100 mm","soil":"Mountain Soil"},
"Lakshadweep":{"crop":"Coconut","rainfall":"1600 mm","soil":"Sandy Soil"},
"Puducherry":{"crop":"Rice","rainfall":"1200 mm","soil":"Red Soil"}

}

selected=st.selectbox(

"Select State/UT",

list(state_data.keys())

)

data=state_data[selected]

c1,c2,c3=st.columns(3)

with c1:

    st.metric(
    "Major Crop",
    data["crop"]
    )

with c2:

    st.metric(
    "Average Rainfall",
    data["rainfall"]
    )

with c3:

    st.metric(
    "Soil Type",
    data["soil"]
    )

st.write("---")

st.success(
f"Showing agricultural insights for {selected}"
)