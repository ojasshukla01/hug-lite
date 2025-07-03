import streamlit as st
from components.header import show_logo

st.set_page_config(page_title="Contact Us")
show_logo()
st.title("📬 Contact Us")

st.markdown("""
**General Enquiries**  
📧 hello@huglite.app

**Support**  
📞 +61 123 456 789  
🌐 [www.huglite.app](https://huglite.app)

**Office**  
3/7 Alfred Street  
Highett, VIC 3190
""")
