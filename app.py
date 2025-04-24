import streamlit as st
from components import login, dashboard, resume_builder

st.set_page_config(page_title="Neon ATS", layout="centered")
st.markdown('<style>' + open('./styles/neon.css').read() + '</style>', unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'login'

if st.session_state.page == 'login':
    login.login_ui()
elif st.session_state.page == 'dashboard':
    dashboard.dashboard_ui()
elif st.session_state.page == 'resume_builder':
    resume_builder.builder_ui()

