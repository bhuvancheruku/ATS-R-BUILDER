import streamlit as st
import PyPDF2
import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def get_keywords(text):
    words = nltk.word_tokenize(text.lower())
    filtered = [word for word in words if word.isalnum() and word not in stopwords.words('english')]
    return Counter(filtered)

def compare_keywords(resume_keywords, jd_keywords):
    resume_set = set(resume_keywords)
    jd_set = set(jd_keywords)

    used = list(resume_set.intersection(jd_set))
    missing = list(jd_set.difference(resume_set))
    match_score = round((len(used) / len(jd_set)) * 100, 2) if jd_set else 0

    return used, missing, match_score

def ats_keyword_scanner():
    st.title("📊 ATS Keyword Scanner")

    uploaded_resume = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Paste the Job Description here")

    if uploaded_resume and job_description:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(uploaded_resume)
            resume_keywords = get_keywords(resume_text)
            jd_keywords = get_keywords(job_description)

            used, missing, score = compare_keywords(resume_keywords, jd_keywords)

        st.success(f"🔍 Match Score: {score}%")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("✅ Used Keywords")
            st.write(used if used else "None")
        with col2:
            st.subheader("❌ Missing Keywords")
            st.write(missing if missing else "None")

        if score < 70:
            st.warning("📢 Improve your resume by adding more relevant keywords!")
