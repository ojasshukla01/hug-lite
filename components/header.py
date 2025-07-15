import streamlit as st
import random

def show_logo():
    cols = st.columns([1, 4])
    with cols[0]:
        st.image("assets/logo.png", width=120)

def show_topbar():
    if not st.session_state.get("authenticated"):
        return

    initials = "".join(p[0].upper() for p in st.session_state.get("display_name", "U").split()[:2])

    if "avatar_color" not in st.session_state:
        st.session_state.avatar_color = random.choice([
            "#673AB7", "#3F51B5", "#2196F3", "#009688", "#4CAF50",
            "#FF5722", "#795548", "#607D8B", "#9C27B0", "#E91E63"
        ])
    avatar_color = st.session_state.avatar_color

    st.markdown(f"""
        <style>
        .dropdown {{
            position: absolute;
            top: 20px;
            right: 20px;
            display: inline-block;
            z-index: 9999;
        }}
        .dropbtn {{
            background-color: {avatar_color};
            color: white;
            border: none;
            border-radius: 50%;
            width: 42px;
            height: 42px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
        }}
        .dropdown-content {{
            display: none;
            position: absolute;
            right: 0;
            background-color: white;
            min-width: 120px;
            border-radius: 6px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
        }}
        .dropdown-content a {{
            display: block;
            padding: 10px 14px;
            text-decoration: none;
            font-size: 14px;
            color: black;
        }}
        .dropdown:hover .dropdown-content {{
            display: block;
        }}
        .fab {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background-color: #673AB7;
            color: white;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            font-size: 30px;
            text-align: center;
            line-height: 60px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        }}
        </style>
        <a href="#job_form" class="fab">+</a>
        <div class="dropdown">
            <button class="dropbtn">{initials}</button>
            <div class="dropdown-content">
                <a href="#" onclick="window.location.href='?menu=profile'; return false;" style="
                    display: block;
                    padding: 10px 14px;
                    text-decoration: none;
                    font-size: 14px;
                    color: black;
                ">👤 Profile</a>
                <a href="#" onclick="window.location.href='?menu=logout'; return false;" style="
                    display: block;
                    padding: 10px 14px;
                    text-decoration: none;
                    font-size: 14px;
                    color: black;
                ">🚪 Logout</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Handle query param logic
    menu_action = st.query_params.get("menu")

    if menu_action == "logout":
        st.query_params.clear()
        st.session_state.clear()
        st.switch_page("pages/Home.py")

    elif menu_action == "profile":
        st.query_params.clear()
        st.info("👤 Profile page coming soon...")

    if not st.session_state.get("authenticated"):
        return