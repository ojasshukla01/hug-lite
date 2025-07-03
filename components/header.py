import streamlit as st

def show_logo():
    cols = st.columns([0.85, 0.15])
    with cols[0]:
        st.image("assets/logo.png", width=120)
    with cols[1]:
        if "display_name" in st.session_state:
            initials = "".join(w[0].upper() for w in st.session_state['display_name'].split()[:2])
            st.markdown(f"""
                <div style='background:#673AB7; color:white; border-radius:50%;
                width:40px; height:40px; display:flex; align-items:center; justify-content:center;
                font-weight:bold; font-size:16px;'>{initials}</div>
            """, unsafe_allow_html=True)
