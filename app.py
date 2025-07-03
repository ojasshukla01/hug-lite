import streamlit as st
import json
from datetime import time
from streamlit_folium import st_folium
import folium
import os

st.set_page_config(page_title="HUG Lite", page_icon="🤗", layout="wide")
st.image("assets/logo.png", width=120)

st.title("🤗 HUG Lite – Care Job Posting")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("📝 Post a Care Job")
    with st.form("job_form"):
        title = st.text_input("Job Title")
        job_type = st.selectbox("Type", ["Transport", "Babysitting", "Tutoring"])
        location = st.text_input("Location")
        job_time = st.time_input("Time", value=time(8, 0))
        submit = st.form_submit_button("Submit Job")

        if submit:
            job_data = {
                "title": title,
                "type": job_type,
                "location": location,
                "time": job_time.strftime("%H:%M")
            }
            os.makedirs("data", exist_ok=True)
            with open("data/submitted_jobs.json", "a") as f:
                f.write(json.dumps(job_data) + "\n")
            st.success(f"✅ Job '{title}' posted successfully!")

with col2:
    st.subheader("🗺️ Simulated Transport Tracker")
    m = folium.Map(location=[-33.8688, 151.2093], zoom_start=12)
    folium.Marker([-33.8688, 151.2093], tooltip="Pickup Point").add_to(m)
    st_folium(m, width=700, height=400)

st.divider()

st.subheader("🤝 Select from Your Trusted Network")

try:
    with open("data/dummy_users.json") as f:
        users = json.load(f)
    selected = st.multiselect(
        "Choose carers to notify:",
        [u["name"] for u in users],
    )
    if selected:
        st.info(f"🔔 Notified: {', '.join(selected)}")
except FileNotFoundError:
    st.warning("⚠️ No dummy users found.")
