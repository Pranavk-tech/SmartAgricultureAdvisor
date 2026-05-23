import streamlit as st

st.set_page_config(
    layout="wide"
)

st.title("🧪 Fertilizer Recommendation")

st.write(
"""
Get fertilizer suggestions based on soil nutrients
"""
)

c1,c2=st.columns(2)

with c1:

    N=st.slider(
        "Nitrogen (N)",
        0,
        150,
        50
    )

    P=st.slider(
        "Phosphorus (P)",
        0,
        150,
        50
    )

with c2:

    K=st.slider(
        "Potassium (K)",
        0,
        150,
        50
    )

    ph=st.slider(
        "Soil pH",
        0.0,
        14.0,
        7.0
    )


if st.button(
    "Recommend Fertilizer"
):

    recommendations=[]

    if N<40:
        recommendations.append(
            "Nitrogen low → Use Urea"
        )

    elif N>100:
        recommendations.append(
            "Nitrogen high → Reduce nitrogen fertilizer"
        )

    if P<40:
        recommendations.append(
            "Phosphorus low → Use DAP"
        )

    elif P>100:
        recommendations.append(
            "Phosphorus high → Avoid excess phosphate"
        )

    if K<40:
        recommendations.append(
            "Potassium low → Use Potash"
        )

    elif K>100:
        recommendations.append(
            "Potassium high → Reduce potassium fertilizer"
        )

    if ph<6:

        recommendations.append(
            "Acidic soil → Add lime"
        )

    elif ph>8:

        recommendations.append(
            "Alkaline soil → Add organic compost"
        )

    st.subheader(
        "Recommendations"
    )

    for item in recommendations:

        st.success(
            item
        )

    if len(recommendations)==0:

        st.success(
            "Soil nutrients look balanced"
        )

st.write("---")

st.subheader(
"General Fertilizer Guide"
)

st.info("""

Nitrogen (N)
• Leaf growth
• Green vegetation

Phosphorus (P)
• Root growth
• Flowering

Potassium (K)
• Disease resistance
• Strong crop development

""")