import streamlit as st

def onboarding_interface():
    st.header("📋 Onboarding – Let’s Get to Know You!")
    exam_date = st.date_input("📅 Enter your exam date")
    study_hours = st.slider("⏱️ Daily available study hours", 1, 12, 4)
    preference = st.radio("📚 Preferred study mode", ["Morning", "Evening", "Late Night"])

    uploaded_syllabus = st.file_uploader("📄 Upload your syllabus (TXT format preferred)", type=["txt"])
    syllabus_text = uploaded_syllabus.read().decode('utf-8') if uploaded_syllabus else ""

    return exam_date, study_hours, preference, syllabus_text
