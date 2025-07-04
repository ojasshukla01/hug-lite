import streamlit as st
from components.header import show_logo

st.set_page_config(page_title="Contact Us", layout="centered")
show_logo()

st.title("📞 Contact Us")

st.markdown("""
For questions, feedback, or support, feel free to reach out:

- 📧 Email: [simon@thehugapp.com.au](mailto:simon@thehugapp.com.au)
- 🌐 Website: [www.thehugapp.com.au](https://www.thehugapp.com.au)
- 📍 Address: 3/7 Alfred Street, Highett, Victoria 3190
""")
