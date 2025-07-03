import streamlit as st
from components.header import show_logo

st.set_page_config(page_title="About Us")
show_logo()
st.title("🤝 About HUG Lite")

st.markdown("""
HUG Lite is a trusted care scheduling platform built for modern families.  
We help parents, carers, and community members connect through simple tools for:
- Booking care jobs
- Coordinating pickups/dropoffs
- Managing child-related responsibilities

Built with ❤️ for busy humans.
""")
