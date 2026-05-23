import streamlit as st
from pdf_generator import create_pdf

st.title("📄 Agriculture Report Generator")

farmer=st.text_input(
"Farmer Name"
)

crop=st.text_input(
"Crop"
)

state=st.text_input(
"State"
)

recommendation=st.text_area(
"Recommendation"
)

if st.button(
"Generate PDF"
):

    report={

    "Farmer":farmer,
    "Crop":crop,
    "State":state,
    "Recommendation":recommendation

    }

    create_pdf(
    report,
    "report.pdf"
    )

    with open(
    "report.pdf",
    "rb"
    ) as f:

        st.download_button(
        "⬇ Download PDF",
        f,
        file_name="AgricultureReport.pdf"
        )