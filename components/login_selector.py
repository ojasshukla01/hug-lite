import streamlit as st

def login_selector():
    if "user_role" not in st.session_state:
        st.session_state.user_role = "Parent"

    st.sidebar.title("Login")
    st.session_state.user_role = st.sidebar.radio(
        "Select your role",
        ["Parent", "Carer"],
        index=["Parent", "Carer"].index(st.session_state.user_role)
    )
    st.sidebar.success(f"Logged in as: {st.session_state.user_role}")
    return st.session_state.user_role
