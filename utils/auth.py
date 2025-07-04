import streamlit as st

def login():
    st.warning("🔒 Please log in to access the app.")
    st.stop()

def auth_guard():
    if not st.session_state.get("authenticated", False):
        st.warning("🔒 Please log in to access the app.")
        st.switch_page("pages/Home.py")
        st.stop()


def get_logged_in_user():
    """Returns True if user is logged in, else None."""
    return st.session_state.get("authenticated", False)

