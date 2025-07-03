import streamlit as st
from streamlit_calendar import calendar
from utils.helpers import read_jobs
from datetime import datetime
from components.header import show_logo
show_logo()

st.set_page_config(page_title="📆 Calendar View", layout="wide")

st.title("📅 Job Calendar")

# Load jobs
jobs = read_jobs("data/submitted_jobs.json")

events = []
for job in jobs:
    try:
        job_type = job.get("job_type", "Unknown")
        child_name = job.get("child_name", "N/A")
        date = job.get("date", "2025-01-01")
        time_start = job.get("time_start", "09:00")
        time_end = job.get("time_end", "10:00")
        location = job.get("location", "Unknown")
        parent = job.get("parent", "N/A")
        accepted_by = job.get("accepted_by")

        # Determine color
        job_datetime = datetime.strptime(f"{date}T{time_end}", "%Y-%m-%dT%H:%M")
        if job_datetime < datetime.now():
            color = "#dc3545"  # red = expired
        elif accepted_by:
            color = "#28a745"  # green = accepted
        else:
            color = "#ffc107"  # yellow = pending

        icon = "🚗" if job_type.lower() == "pickup" else "🏠" if job_type.lower() == "dropoff" else "📌"

        event = {
            "title": f"{icon} {job_type.title()} - {child_name}",
            "start": f"{date}T{time_start}",
            "end": f"{date}T{time_end}",
            "color": color,
            "extendedProps": {
                "Status": "Accepted" if accepted_by else "Pending",
                "Accepted By": accepted_by or "—",
                "Parent": parent,
                "Location": location
            }
        }
        events.append(event)
    except Exception as e:
        st.warning(f"⚠️ Skipped malformed job entry: {e}")

# Calendar config
calendar_options = {
    "initialView": "timeGridWeek",
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "dayGridMonth,timeGridWeek,timeGridDay"
    },
    "eventTimeFormat": {
        "hour": 'numeric',
        "minute": '2-digit',
        "meridiem": True
    },
    "eventDisplay": "block",
    "nowIndicator": True,
    "slotMinTime": "06:00:00",
    "slotMaxTime": "21:00:00",
    "height": "auto",
    "events": events,
}

calendar_result = calendar(
    events=events,
    options=calendar_options,
    key="hug_lite_calendar"
)

# Optional debug info
with st.expander("📋 View raw calendar events"):
    st.json(events)

if "user_role" not in st.session_state:
    st.warning("🔒 Please log in to access this page.")
    st.stop()