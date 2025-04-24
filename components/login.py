# components/login.py

import streamlit as st

def login_ui():
    st.markdown("""
        <div style='text-align: center; margin-bottom: 3rem;'>
            <h1 style='color: #00ffe0; font-family: Orbitron;'>🔐 LOGIN</h1>
            <p style='color: #888;'>Glad you're back, hacker 😎</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        remember = st.checkbox("Remember me", value=True)
        login_btn = st.form_submit_button("Login")

        if login_btn:
            if username and password:
                st.success("Welcome back, " + username)
                st.balloons()
                st.session_state.page = 'dashboard'  # move to dashboard
            else:
                st.error("Please fill in both fields.")

    st.markdown("""
        <p style='text-align:center; margin-top:2rem;'>Or login with</p>
        <div style='display: flex; justify-content: center; gap: 20px; margin-top: 1rem;'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/512px-Google_%22G%22_Logo.svg.png' width='40'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/4/4f/Github-icon.svg' width='40'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/0/05/Facebook_Logo_%282019%29.png' width='40'>
        </div>
        <div style='text-align: center; margin-top: 2rem; color: #aaa;'>
            <small>Don't have an account? <a style='color:#00fff0;' href='#'>Signup</a></small>
        </div>
    """, unsafe_allow_html=True)
