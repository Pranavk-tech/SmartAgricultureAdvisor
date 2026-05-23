import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime


# ==========================
# DATASET LOADER
# ==========================

@st.cache_data

def load_data(path):

    try:

        df=pd.read_csv(path)

        return df

    except Exception as e:

        st.error(
        f"Dataset Error: {e}"
        )

        return None


# ==========================
# MODEL LOADER
# ==========================

@st.cache_resource

def load_model(path):

    try:

        model=joblib.load(path)

        return model

    except Exception as e:

        st.error(
        f"Model Error: {e}"
        )

        return None


# ==========================
# SAVE USER HISTORY
# ==========================

def save_history(

user,
page,
result

):

    try:

        file="data/history.csv"

        row={

        "Date":datetime.now(),

        "User":user,

        "Page":page,

        "Result":result

        }

        new_df=pd.DataFrame([row])

        if os.path.exists(file):

            old_df=pd.read_csv(file)

            final_df=pd.concat(
                [old_df,new_df],
                ignore_index=True
            )

        else:

            final_df=new_df


        final_df.to_csv(

        file,
        index=False

        )


    except Exception as e:

        st.warning(
        f"History save failed: {e}"
        )


# ==========================
# LOADING ANIMATION
# ==========================

def loading(message):

    return st.spinner(message)



# ==========================
# SAFE EXECUTION
# ==========================

def safe_run(function):

    try:

        return function()

    except Exception as e:

        st.error(
        f"Error: {e}"
        )

        return None



# ==========================
# FOOTER
# ==========================

def footer():

    st.write("---")

    st.caption("""

🌱 Smart Agriculture Advisor v2.0

Built using:

• Python
• Streamlit
• Machine Learning
• TensorFlow
• Scikit-Learn
• AI + Analytics

""")
# ==========================
# MASTER DATA LOADER
# ==========================

@st.cache_data
def load_master_data():

    try:

        df=load_data(
            "data/Crop_recommendation.csv"
        )

        return df

    except Exception as e:

        st.error(
        f"Master data loading error: {e}"
        )

        return pd.DataFrame()