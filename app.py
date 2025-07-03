import streamlit as st
import json
from datetime import time
from streamlit_folium import st_folium
import folium
import os

# Import login and helper modules
from components.login_selector import login_selector
from utils.helpers import read_jobs, write_jobs, delete_job, update_job_status

# Set page config and branding
st.set_page_config(page_title="HUG Lite", page_icon="🤗", layout="wide")
st.image("assets/logo.png", width=120)

# Simulated login using session state
role = login_selector()

# Tabs for Hug App features
tabs = st.tabs(["Care Jobs", "Hug Plus", "Shifta", "Freelancer"])

with tabs[0]:
    st.subheader("💼 Care Job Section")

    if role == "Parent":
        care_view = st.radio("Choose view:", ["📋 Post Job", "📊 Manage Jobs"], horizontal=True)

        if care_view == "📋 Post Job":
            col1, col2 = st.columns([1, 1.2])

            with col1:
                st.subheader("📝 Post a Care Job")
                with st.form("job_form"):
                    title = st.text_input("Job Title")
                    job_type = st.selectbox("Type", ["Transport", "Babysitting", "Tutoring"])
                    location = st.text_input("Location")
                    job_time = st.time_input("Time", value=time(8, 0))
                    paid = st.checkbox("Require a paid carer?")
                    rate = st.number_input("Proposed hourly rate ($)", min_value=0.0, value=27.0) if paid else None
                    submit = st.form_submit_button("Submit Job")

                    if submit:
                        job_data = {
                            "title": title,
                            "type": job_type,
                            "location": location,
                            "time": job_time.strftime("%H:%M"),
                            "paid": paid,
                            "rate": rate,
                            "status": "Pending"
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

        elif care_view == "📊 Manage Jobs":
            st.subheader("📊 Manage Your Posted Jobs")

            jobs = read_jobs()
            status_filter = st.selectbox("Filter by status:", ["All", "Pending", "Accepted", "Completed"])

            for i, job in enumerate(jobs):
                if status_filter != "All" and job.get("status") != status_filter:
                    continue

                st.markdown(f"**🔹 {job.get('title', 'Untitled')}** — {job.get('type')} at {job.get('location')} @ {job.get('time')}")
                try:
                    rate = float(job.get("rate", 0.0))
                    rate_str = f"{rate:.2f}"
                except:
                    rate_str = "N/A"
                st.markdown(f"💵 {'Paid – $'+rate_str+'/hr' if job.get('paid') else 'Unpaid'} | Status: {job.get('status')}")

                colA, colB = st.columns([1, 1])
                with colA:
                    if st.button(f"✅ Mark Completed #{i}", key=f"comp_{i}"):
                        update_job_status(i, "Completed")
                        st.rerun()
                with colB:
                    if st.button(f"🗑️ Delete Job #{i}", key=f"del_{i}"):
                        delete_job(i)
                        st.rerun()
                st.markdown("---")

    elif role == "Carer":
        st.subheader("📋 Available Jobs")
        jobs = read_jobs()
        if not jobs:
            st.info("No jobs available yet.")
        else:
            for i, job in enumerate(jobs):
                with st.container():
                    title = job.get("title", "Untitled")
                    job_type = job.get("type", "Unknown")
                    location = job.get("location", "N/A")
                    time_val = job.get("time", "N/A")
                    is_paid = job.get("paid", False)
                    try:
                        rate = float(job.get("rate", 0.0))
                        rate = format(rate, ".2f")
                    except:
                        rate = "N/A"
                    status = job.get("status", "Pending")

                    st.markdown(f"**🔹 {title}** — {job_type} in {location} at {time_val}")
                    st.markdown(f"💵 {'Paid – $'+str(rate)+'/hr' if is_paid else 'Unpaid'}")

                    if status == "Pending":
                        if st.button(f"Accept Job #{i+1}", key=f"acc_{i}"):
                            jobs[i]["status"] = "Accepted"
                            write_jobs(jobs)
                            st.success("✅ Job accepted! Please refresh.")
                            st.stop()
                    else:
                        st.markdown(f"✅ Status: {status}")
                    st.divider()

with tabs[1]:
    st.subheader("📦 Hug Plus")
    st.info("Premium care management – Coming soon!")

with tabs[2]:
    st.subheader("🕒 Hug Shifta")
    st.info("Shift-based scheduling for working parents – Coming soon!")

with tabs[3]:
    st.subheader("💼 Hug Freelancer")
    st.info("Care economy platform for verified carers – Coming soon!")
