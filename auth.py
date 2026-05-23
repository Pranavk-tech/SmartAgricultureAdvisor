import streamlit as st

users={

    "admin":"Pranav123",
    "farmer":"Farm123"

}

def login():

    st.title("🔐 Login")

    username=st.text_input(
        "Username"
    )

    password=st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        username=username.strip()
        password=password.strip()

        if username in users:

            if users[username]==password:

                st.session_state["logged_in"]=True
                st.session_state["user"]=username

                st.success(
                "Login successful"
                )

                st.rerun()

            else:

                st.error(
                "Wrong password"
                )

        else:

            st.error(
            f"User not found: {username}"
            )