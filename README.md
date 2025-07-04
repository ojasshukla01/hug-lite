
# HUG Lite - Care Network App

Welcome to **HUG Lite**, a streamlined care network app built with Streamlit. Designed for parents, carers, and families to post, discover, and manage care jobs.

🔗 **Live App**: https://hug-lite.streamlit.app/

---

## 🌟 Features

- 👪 Parent & Carer login/signup system
- 📋 Post & manage care jobs (transport, babysitting, tutoring)
- 📍 Interactive job map with Folium
- 🧮 Hourly pay, acceptance, completion, and review flow
- 🔐 Admin mode and job overview
- 🧑‍🎨 Avatar initials + logout via dropdown
- 📱 Mobile-friendly responsive UI

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/hug-lite.git
cd hug-lite

# Create virtual env
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🗂 Folder Structure

```
hug-lite/
├── app.py                  # Main launcher
├── pages/
│   ├── Home.py
│   ├── About.py
│   ├── Contact.py
│   ├── Dashboard.py
│   └── user_dashboard.py
├── components/
│   └── header.py           # Logo + topbar
├── utils/
│   ├── auth.py             # Auth logic
│   ├── helpers.py          # Job CRUD
│   └── reviews.py
├── data/
│   ├── dummy_users.json
│   └── submitted_jobs.json
├── assets/
│   └── logo.png
└── requirements.txt
```

---

## 🔐 Default Logins

| Role   | Email              | Password |
|--------|--------------------|----------|
| Parent | kinjal@mail.com    | 123      |
| Carer  | priya@mail.com     | 123      |
| Admin  | admin@mail.com     | 123      |

---

## 🤝 Credits

Built with ❤️ using [Streamlit](https://streamlit.io), [Folium](https://python-visualization.github.io/folium/), and open-source tools.

---

## 📜 License

MIT License.
