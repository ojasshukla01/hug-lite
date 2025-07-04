# hug-lite/app.py

import streamlit as st
from utils.auth import get_logged_in_user
from components.header import show_logo

st.set_page_config(page_title="HUG Lite", page_icon="🫶", layout="wide")
show_logo()

# Public sidebar pages
st.sidebar.page_link("pages/Home.py", label="🏠 Home")
st.sidebar.page_link("pages/About.py", label="ℹ️ About")
st.sidebar.page_link("pages/Contact.py", label="📞 Contact")

# Private sidebar pages (only show if user is logged in)
if get_logged_in_user():
    st.sidebar.page_link("pages/Dashboard.py", label="📋 Dashboard")
    # ❌ Don't show this since it just redirects
    # st.sidebar.page_link("pages/user_dashboard.py", label="🧰 App")

# Routing logic
if get_logged_in_user():
    st.switch_page("pages/Dashboard.py")
else:
    st.switch_page("pages/Home.py")

if not get_logged_in_user():
    st.switch_page("pages/Home.py")