import streamlit as st
import json
import os
from components.header import show_logo
show_logo()

st.set_page_config(page_title="Sign Up", layout="centered")
st.title("📝 Sign Up to HUG Lite")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
role = st.selectbox("I am a...", ["Parent", "Carer"])

if st.button("Create Account"):
    os.makedirs("data", exist_ok=True)
    user_file = "data/dummy_users.json"

    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            users = json.load(f)
    else:
        users = []

    if any(u.get("email") == email for u in users if isinstance(u, dict)):
        st.error("User already exists. Try logging in.")
    else:
        users.append({
            "name": name,
            "email": email,
            "password": password,
            "role": role
        })
        with open(user_file, "w") as f:
            json.dump(users, f, indent=2)
        st.success("✅ Account created. Please log in.")

try:
    with open(user_file, "r") as f:
        users = json.load(f)
    users = [u for u in users if isinstance(u, dict) and "email" in u]
except:
    users = []
    
if "user_role" not in st.session_state:
    st.warning("🔒 Please log in to access this page.")
    st.stop()

if "user_role" in st.session_state:
    st.warning("⚠️ You're already logged in.")
    st.stop()
