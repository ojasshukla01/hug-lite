import streamlit as st
import json
from datetime import time, datetime
from streamlit_folium import st_folium
from utils.reviews import save_review
import folium
import os

from components.login_selector import login_selector
from utils.helpers import read_jobs, write_jobs, delete_job, update_job_status

st.set_page_config(page_title="HUG Lite", page_icon="🫷", layout="wide")
st.image("assets/logo.png", width=120)

# Utility for avatars
def get_initials(name):
    parts = name.strip().split()
    return "".join(p[0].upper() for p in parts[:2]) if parts else "U"

def avatar_html(initials, bg="#4CAF50"):
    return f"""
    <div style='
        background:{bg};
        color:white;
        border-radius:50%;
        width:42px;
        height:42px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-weight:bold;
        font-size:16px;
        margin: 4px 0;
    '>{initials}</div>
    """

# Notifications
if "notifications" not in st.session_state:
    st.session_state.notifications = []
    
if not st.session_state.get("user_role"):
    st.sidebar.empty()  # Hide all links

if st.session_state.get("is_admin"):
    st.markdown("🛡️ **Admin Mode**", unsafe_allow_html=True)
    

role = login_selector()

if not role:
    st.warning("🔐 Please log in to access the app.")
    st.stop()

st.sidebar.markdown("---")
st.sidebar.page_link("pages/calendar.py", label="🗖️ View Calendar")

if st.session_state.notifications:
    st.sidebar.markdown("🔔 **Notifications**")
    for note in st.session_state.notifications:
        st.sidebar.info(note)
    if st.sidebar.button("🗑️ Clear Notifications"):
        st.session_state.notifications = []

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
                            "status": "Pending",
                            "accepted_by": None,
                            "parent": st.session_state.get("display_name", "Parent User"),
                            "timestamp": datetime.now().isoformat()
                        }
                        os.makedirs("data", exist_ok=True)
                        with open("data/submitted_jobs.json", "a") as f:
                            f.write(json.dumps(job_data) + "\n")
                        st.success(f"✅ Job '{title}' posted successfully!")
                        st.session_state.notifications.append(f"🔀 New job posted: {title} in {location} at {job_time.strftime('%I:%M %p')}")

            with col2:
                st.subheader("🗸️ Simulated Transport Tracker")
                m = folium.Map(location=[-33.8688, 151.2093], zoom_start=12)
                folium.Marker([-33.8688, 151.2093], tooltip="Pickup Point").add_to(m)
                st_folium(m, width=700, height=400)

            st.markdown("""
            <style>
            .fab {
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
            }
            </style>
            <a href="#job_form" class="fab">+</a>
            """, unsafe_allow_html=True)

        elif care_view == "📊 Manage Jobs":
            st.subheader("📊 Manage Your Posted Jobs")
            jobs = read_jobs()
            status_filter = st.selectbox("Filter by status:", ["All", "Pending", "Accepted", "Completed"])
            for i, job in enumerate(jobs):
                if status_filter != "All" and job.get("status") != status_filter:
                    continue

                title = job.get("title", "Untitled")
                location = job.get("location", "N/A")
                time_val = job.get("time", "N/A")
                initials = get_initials(job.get("accepted_by", "N/A"))
                job_type = job.get("type", "General")
                status = job.get("status", "Pending")
                is_paid = job.get("paid", False)
                rate = float(job.get("rate", 0.0)) if is_paid else 0
                bg_color = "#3F51B5" if is_paid else "#BDBDBD"

                with st.container():
                    cols = st.columns([0.2, 0.8])
                    with cols[0]:
                        st.markdown(avatar_html(initials, bg=bg_color), unsafe_allow_html=True)
                    with cols[1]:
                        st.markdown(f"""
                        <div style='border:1px solid #ddd; border-radius:10px; padding:12px; background-color:#f4f4f4'>
                            <h5>{title} <span style='color:gray;'>({job_type})</span></h5>
                            <p>📍 {location} | 🕒 {time_val} | 💵 {f"${rate}/hr" if is_paid else "Unpaid"}</p>
                            <p>Status: <b>{status}</b></p>
                        """, unsafe_allow_html=True)
                        if job.get("accepted_by"):
                            st.markdown(f"👤 Accepted by: {job['accepted_by']}")

                        colA, colB = st.columns([1, 1])
                        with colA:
                            if st.button(f"✅ Mark Completed #{i}", key=f"comp_{i}"):
                                update_job_status(i, "Completed")
                                st.rerun()
                        with colB:
                            if st.button(f"🗑️ Delete Job #{i}", key=f"del_{i}"):
                                delete_job(i)
                                st.rerun()

                        if job.get("status") == "Completed" and not job.get("reviewed"):
                            st.markdown("**📝 Leave a Review:**")
                            rating = st.slider("Star Rating", 1, 5, 4, key=f"rate_{i}")
                            review = st.text_area("Write a short review", key=f"review_{i}")
                            if st.button("Submit Review", key=f"submit_review_{i}"):
                                save_review(i, rating, review)
                                job["reviewed"] = True
                                write_jobs(jobs)
                                st.success("✅ Review submitted!")
                                st.rerun()
                        st.markdown("</div>", unsafe_allow_html=True)

    elif role == "Carer":
        st.subheader("📋 Available Jobs")
        jobs = read_jobs()
        locations = sorted(set(job.get("location") for job in jobs if job.get("location")))
        paid_options = ["All", "Paid", "Unpaid"]
        st.markdown("### 🔍 Filter Jobs")
        selected_location = st.selectbox("Location", ["All"] + locations)
        selected_paid = st.selectbox("Payment Type", paid_options)

        for i, job in enumerate(jobs):
            if selected_location != "All" and job.get("location") != selected_location:
                continue
            if selected_paid == "Paid" and not job.get("paid"):
                continue
            if selected_paid == "Unpaid" and job.get("paid"):
                continue

            title = job.get("title", "Untitled")
            location = job.get("location", "N/A")
            time_val = job.get("time", "N/A")
            parent = job.get("parent", "User")
            initials = get_initials(parent)
            job_type = job.get("type", "General")
            status = job.get("status", "Pending")
            accepted_by = job.get("accepted_by", "")
            is_paid = job.get("paid", False)
            rate = float(job.get("rate", 0.0)) if is_paid else 0
            bg_color = "#2196F3" if is_paid else "#9E9E9E"

            with st.container():
                cols = st.columns([0.2, 0.8])
                with cols[0]:
                    st.markdown(avatar_html(initials, bg=bg_color), unsafe_allow_html=True)
                with cols[1]:
                    st.markdown(f"""
                        <div style='border:1px solid #ddd; border-radius:10px; padding:12px; background-color:#f9f9f9'>
                            <h5 style='margin-bottom:6px;'>{title} <span style='color:gray;'>({job_type})</span></h5>
                            <p style='margin:2px 0;'>📍 {location}</p>
                            <p style='margin:2px 0;'>🕒 {time_val} | 💵 {f"${rate}/hr" if is_paid else "Unpaid"}</p>
                    """, unsafe_allow_html=True)

                    if status == "Pending":
                        if st.button(f"✅ Accept Job #{i+1}", key=f"acc_{i}"):
                            jobs[i]["status"] = "Accepted"
                            carer_name = st.session_state.get("carer_name", "Anonymous Carer")
                            jobs[i]["accepted_by"] = carer_name
                            write_jobs(jobs)
                            st.success(f"✅ You accepted this job.")
                            st.session_state.notifications.append(f"✅ {carer_name} accepted '{title}' in {location}")
                            st.stop()
                    elif status == "Accepted":
                        st.markdown(f"✅ Accepted by **{accepted_by or 'Someone'}**")
                    else:
                        st.markdown(f"✅ Status: {status}")
                    st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:
    st.subheader("📦 Hug Plus")
    st.info("Premium care management – Coming soon!")

with tabs[2]:
    st.subheader("🥒 Hug Shifta")
    st.info("Shift-based scheduling for working parents – Coming soon!")

with tabs[3]:
    st.subheader("💼 Hug Freelancer")
    st.info("Care economy platform for verified carers – Coming soon!")