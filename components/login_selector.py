import streamlit as st
import json

def login_selector():
    st.sidebar.markdown("## 🔐 Login")

    # If already logged in
    if "user_role" in st.session_state:
        user = st.session_state.get("display_name", "User")
        initials = "".join([w[0].upper() for w in user.split()[:2]])
        st.sidebar.success(f"✅ Logged in as {st.session_state['user_role']}")
        st.sidebar.markdown(f"**🧑‍💼 {user} ({initials})**")
        return st.session_state["user_role"]

    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    user_file = "data/dummy_users.json"

    if st.sidebar.button("Login"):
        try:
            with open(user_file, "r") as f:
                users = json.load(f)
        except:
            users = []

        match = next((u for u in users if u.get("email") == email and u.get("password") == password), None)
        if match:
            st.session_state.user_role = match["role"]
            st.session_state.username = match["email"]
            st.session_state.display_name = match["name"]
            st.session_state.is_admin = match["role"].lower() == "admin"
            st.sidebar.success(f"✅ Logged in as {match['role']}")
            st.rerun()
        else:
            st.sidebar.error("❌ Invalid credentials.")
    return None
