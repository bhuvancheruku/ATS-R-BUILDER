# components/resume_builder.py

import streamlit as st

def builder_ui():
    if 'step' not in st.session_state:
        st.session_state.step = 1

    st.markdown("<h1 style='color:#00ffea;'>🧩 Build Your Resume</h1>", unsafe_allow_html=True)
    
    # Progress Bar
    st.progress(st.session_state.step / 5)
    
    # Step 1: Personal Info
    if st.session_state.step == 1:
        st.subheader("Step 1: Personal Details")
        name = st.text_input("Full Name")
        role = st.text_input("Job Role (e.g., Full Stack Developer)")
        summary = st.text_area("Professional Summary (2-3 lines)")

        if st.button("Next ➡️"):
            st.session_state.step += 1

    # Step 2: Education
    if st.session_state.step == 2:
        st.subheader("Step 2: Education")
        st.text_input("Degree (e.g., B.Tech CSE)")
        st.text_input("College")
        st.text_input("Duration (e.g., 2019-2023)")
        st.text_input("CGPA/Percentage")

        if st.button("⬅️ Back"):
            st.session_state.step -= 1
        if st.button("Next ➡️"):
            st.session_state.step += 1

    # Step 3: Experience
    if st.session_state.step == 3:
        st.subheader("Step 3: Experience")
        st.text_input("Role")
        st.text_input("Company")
        st.text_input("Duration")
        st.text_area("Responsibilities (bullet points)")

        if st.button("⬅️ Back"):
            st.session_state.step -= 1
        if st.button("Next ➡️"):
            st.session_state.step += 1

    # Step 4: Skills & Projects
    if st.session_state.step == 4:
        st.subheader("Step 4: Skills & Projects")
        st.text_input("Skills (comma-separated)")
        st.text_input("Project Title")
        st.text_area("Project Description")
        st.text_input("Project Link")

        if st.button("⬅️ Back"):
            st.session_state.step -= 1
        if st.button("Next ➡️"):
            st.session_state.step += 1

    # Step 5: Customize + Download
    if st.session_state.step == 5:
        st.subheader("Step 5: Preview & Download")
        template = st.selectbox("Choose Template", ["Hacker Theme", "Classic"])
        color = st.color_picker("Accent Color", "#00FF41")

        if st.button("⬅️ Back"):
            st.session_state.step -= 1

        if st.button("Generate Resume ⚡"):
            # TODO: Resume Generation Logic
            st.success("Resume Generated Successfully! 🎉")
            st.download_button("Download PDF", b"PDF_BYTES", "resume.pdf")
