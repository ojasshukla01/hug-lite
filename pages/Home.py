import streamlit as st
import json
import os
from components.header import show_logo

# Set config
st.set_page_config(page_title="HUG Lite - Home", layout="centered")
show_logo()

# ---- Static Welcome Info ----
st.markdown("<h1 style='text-align:center; color:#673AB7;'>🤗 Welcome to HUG Lite</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; font-size:18px; padding:20px;'>
    <p>🧡 A trusted care network for parents, carers, and families.</p>
    <p>🚗 Share pickups, 🧸 book babysitters, and 👨‍👩‍👧‍👦 simplify your daily juggle.</p>
</div>
""", unsafe_allow_html=True)

# ---- If already logged in ----
if st.session_state.get("authenticated"):
    st.success(f"🎉 Logged in as {st.session_state.get('display_name')} ({st.session_state.get('user_role')})")
    st.markdown("<h3 style='text-align:center;'>Use the left menu to access your dashboard.</h3>", unsafe_allow_html=True)
    st.stop()

# ---- Login & Signup Tabs ----
tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])

# ------------------ LOGIN ------------------ #
with tab1:
    st.subheader("🔐 Login")
    login_email = st.text_input("Email", key="login_email")
    login_pass = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_btn"):
        try:
            with open("data/dummy_users.json") as f:
                users = json.load(f)
        except:
            users = []

        user = next((u for u in users if u.get("email") == login_email and u.get("password") == login_pass), None)

        if user:
            st.session_state.user_role = user["role"]
            st.session_state.display_name = user["name"]
            st.session_state.username = user["email"]
            st.session_state.is_admin = user["role"].lower() == "admin"
            st.session_state.authenticated = True
            st.success(f"✅ Welcome back, {user['name']} ({user['role']})")
            st.switch_page("pages/user_dashboard.py")
        else:
            st.error("❌ Invalid email or password")

# ------------------ SIGNUP ------------------ #
with tab2:
    st.subheader("📝 Create Your Account")
    signup_name = st.text_input("Full Name", key="signup_name")
    signup_email = st.text_input("Email", key="signup_email")
    signup_pass = st.text_input("Password", type="password", key="signup_password")
    signup_role = st.selectbox("I am a...", ["Parent", "Carer"], key="signup_role")

    if st.button("Create Account", key="signup_btn"):
        if not signup_name or not signup_email or not signup_pass:
            st.warning("⚠️ Please fill all fields.")
        else:
            user_file = "data/dummy_users.json"
            os.makedirs("data", exist_ok=True)

            try:
                with open(user_file, "r") as f:
                    users = json.load(f)
            except:
                users = []

            if any(u.get("email") == signup_email for u in users):
                st.error("⚠️ Email already exists. Try logging in.")
            else:
                users.append({
                    "name": signup_name,
                    "email": signup_email,
                    "password": signup_pass,
                    "role": signup_role
                })
                with open(user_file, "w") as f:
                    json.dump(users, f, indent=2)
                st.success("✅ Account created! You can now login.")

