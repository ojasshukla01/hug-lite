HUG Lite – A Streamlit App for Trusted Care Networks 👨‍👩‍👧‍👦

Overview
--------
HUG Lite is a responsive, role-based web application built using Streamlit.
It allows parents to post and manage care jobs, carers to accept and complete them, and admins to oversee the entire platform.

Key Features
------------
🔐 Login & Signup system  
👨‍👩‍👧‍👦 Role-based access for Parent, Carer, Admin  
📱 Mobile-friendly interface with FAB (Floating Action Button)  
🎨 Random avatar with initials and hoverable logout dropdown  
📋 Dashboard with Tabs for different job types  
📍 Interactive Folium map for transport visualization  
📝 Rating & Review system after job completion  
🔔 Notification support with session-state  
📊 Admin Mode with platform metrics (total jobs, completed, paid)  
🚪 Logout support with session clearing and redirect

File Structure
--------------
- `app.py`: App entry point – handles routing and redirects
- `pages/`: Contains Streamlit multipage scripts
  - `Home.py`: Login / Signup landing page
  - `Dashboard.py`: Main dashboard for Parents, Carers, Admin
  - `About.py`, `Contact.py`: Public pages
- `components/header.py`: Contains `show_logo()` and `show_topbar()` logic
- `utils/`: Helper functions for auth, jobs, review, etc.
- `data/`: Stores user and job data in JSON files
- `assets/`: Static assets like logos and styles

Login Credentials
-----------------
Default user data is stored in `data/dummy_users.json`. Example format:
```json
[
  {
    "name": "Admin User",
    "email": "admin@example.com",
    "password": "admin123",
    "role": "Admin"
  },
  {
    "name": "Priya Verma",
    "email": "priya@example.com",
    "password": "1234",
    "role": "Carer"
  }
]
```

Getting Started
---------------
1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   streamlit run app.py

3. Navigate to `http://localhost:8501` in your browser.

Credits
-------
Built by Ojas Shukla using Streamlit and open-source Python libraries.
This project is part of an end-to-end showcase of modern data engineering + frontend UI/UX techniques.

License
-------
Free for personal or educational use. Commercial use requires permission.