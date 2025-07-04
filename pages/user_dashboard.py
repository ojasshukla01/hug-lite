# pages/user_dashboard.py

import streamlit as st
from utils.auth import auth_guard

# 🚫 Block access unless logged in
auth_guard()

# ✅ Immediately redirect to Dashboard
st.switch_page("pages/Dashboard.py")
