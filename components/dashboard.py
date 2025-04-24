# components/dashboard.py

import streamlit as st
from datetime import datetime

def dashboard_ui():
    st.markdown("""
        <div style='text-align: center; margin-bottom: 3rem;'>
            <h1 style='color: #00ffea; font-family: Orbitron;'>📂 Dashboard</h1>
            <p style='color: #888;'>Your hacker workspace is live</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="display:flex; justify-content: center; margin-bottom: 2rem;">
            <button onclick="document.getElementById('create_btn').click()" style='
                padding: 1em 2em;
                background: linear-gradient(to right, #4a00e0, #00f7ff);
                color: white;
                font-size: 1em;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                box-shadow: 0 0 15px #00f7ff;
                transition: 0.3s;
            '>➕ Create New Resume</button>
        </div>
    """, unsafe_allow_html=True)

    # Streamlit native button (for logic)
    if st.button("Create New Resume", key="create_btn"):
        st.session_state.page = "resume_builder"

    st.markdown("---")

    st.markdown("<h3 style='color:#00ffc8;'>📝 Recent Resumes</h3>", unsafe_allow_html=True)

    # Mock Data (replace with DB later)
    resumes = [
        {"title": "Full Stack Dev", "date": "2025-04-20", "score": "87%"},
        {"title": "Data Analyst", "date": "2025-03-18", "score": "91%"},
        {"title": "Cybersecurity Intern", "date": "2025-02-05", "score": "84%"}
    ]

    for res in resumes:
        st.markdown(f"""
            <div style='
                background-color: #1a1a1a;
                padding: 1rem;
                border-left: 4px solid #00f7ff;
                margin-bottom: 1rem;
                border-radius: 10px;
            '>
                <strong style='color:#0ff;'>{res['title']}</strong><br>
                <small style='color:#ccc;'>Created on: {res['date']} | ATS Score: {res['score']}</small>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state.page = "login"
        st.success("Logged out successfully.")
