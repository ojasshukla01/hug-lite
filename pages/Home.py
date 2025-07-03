import streamlit as st
from components.header import show_logo
show_logo()

st.set_page_config(page_title="HUG Lite Home", layout="centered")

st.markdown("<h1 style='text-align:center; color:#673AB7;'>🤗 Welcome to HUG Lite</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px; padding:20px;'>
    <p>🧡 A trusted care network for parents, carers, and families.</p>
    <p>🚗 Share pickups, 🧸 book babysitters, and 👨‍👩‍👧‍👦 simplify your daily juggle.</p>
    <br>
    <a href='/Signup' style='font-size:20px;'>👉 New here? Sign up!</a> or <a href='/app' style='font-size:20px;'>🔐 Login</a>
</div>
""", unsafe_allow_html=True)

if not st.session_state.get("user_role"):
    st.sidebar.empty()  # Hide all links
