import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide"
)

st.title("📅 Crop Calendar")

st.write(
"""
Season-wise crop planning and harvesting schedule
"""
)

calendar_data={

"Kharif":[
("Rice","June-July","October-November"),
("Maize","June-July","September-October"),
("Cotton","May-June","October-January"),
("Soybean","June-July","September-October"),
("Groundnut","June-July","September-October")
],

"Rabi":[
("Wheat","October-November","March-April"),
("Barley","October-November","March-April"),
("Mustard","October-November","February-March"),
("Peas","October-November","February-March"),
("Gram","October-November","March-April")
],

"Zaid":[
("Watermelon","March-April","June"),
("Cucumber","March-April","June"),
("Pumpkin","March-April","June"),
("Muskmelon","March-April","June")
]

}

season=st.selectbox(
"Select Season",
list(calendar_data.keys())
)

rows=[]

for crop,sow,harvest in calendar_data[season]:

    rows.append({

    "Crop":crop,
    "Sowing":sow,
    "Harvesting":harvest

    })

df=pd.DataFrame(rows)

st.subheader(
f"{season} Crop Calendar"
)

st.dataframe(
df,
use_container_width=True
)

st.write("---")

st.subheader(
"🌱 Farming Tips"
)

if season=="Kharif":

    st.success("""
• Rainfall-based crops dominate

• Monitor waterlogging

• Use disease-resistant seeds
""")

elif season=="Rabi":

    st.success("""
• Irrigation management important

• Wheat and pulses perform well

• Protect crops from frost
""")

else:

    st.success("""
• Short-duration crops preferred

• Ensure irrigation availability
""")