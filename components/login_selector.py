# components/login_selector.py
import streamlit as st

def login_selector():
    return st.session_state.get("user_role")
