import streamlit as st
from components.header import show_logo

st.set_page_config(page_title="About HUG Lite", layout="centered")
show_logo()

st.title("ℹ️ About HUG Lite")
st.markdown("""
Welcome to **HUG Lite** – a trusted care network for parents, carers, and families.

Our mission is to make it easy to:
- 🚗 Coordinate pickups
- 🧸 Book babysitters
- 👨‍👩‍👧‍👦 Share child care responsibilities

Whether you're a busy parent, a reliable carer, or a freelancer, HUG Lite is designed to help you manage the daily juggle with ease.
""")
