import streamlit as st
from auth import create_tables as auth_create_tables, register_user, verify_user
from models import create_tables as models_create_tables, add_exam, get_exams, add_subject, get_subjects, add_topic, get_topics
from scheduler import generate_study_plan_with_topics
from ai_insights import generate_ai_insights
from datetime import datetime

# Initialize DB tables once
auth_create_tables()
models_create_tables()

def main():
    st.title("🧠 IntelliPlan Study Scheduler with AI Insights")

    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        st.subheader("Create New Account")
        username = st.text_input("Username")
        name = st.text_input("Full Name")
        password = st.text_input("Password", type='password')
        if st.button("Register"):
            if register_user(username, password, name):
                st.success("You have successfully registered! Please login.")
            else:
                st.error("Username already exists.")

    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            user = verify_user(username, password)
            if user:
                st.success(f"Welcome {user['name']}!")

                # --- Exams ---
                exams = get_exams(user['id'])
                st.subheader("Your Exams")
                if exams:
                    for exam in exams:
                        st.write(f"- **{exam['name']}** on {exam['exam_date']}")
                else:
                    st.write("No exams added yet.")

                with st.form("add_exam_form", clear_on_submit=True):
                    st.write("Add a new Exam")
                    exam_name = st.text_input("Exam Name", key="exam_name")
                    exam_date = st.date_input("Exam Date", key="exam_date")
                    submitted = st.form_submit_button("Add Exam")
                    if submitted and exam_name:
                        add_exam(user['id'], exam_name, exam_date)
                        st.success("Exam added! Please refresh or re-login to see updates.")

                # --- Subjects ---
                st.subheader("Manage Subjects and Topics")
                if exams:
                    exam_for_subject = st.selectbox("Select Exam to manage subjects", exams, format_func=lambda e: e['name'])
                    if exam_for_subject:
                        subjects = get_subjects(exam_for_subject['id'])
                        for subj in subjects:
                            st.write(f"Subject: {subj['name']}")
                            topics = get_topics(subj['id'])
                            for t in topics:
                                st.write(f" - {t['name']} (Priority: {t['priority']}, Difficulty: {t['difficulty']})")
                        with st.form("add_subject_form", clear_on_submit=True):
                            subject_name = st.text_input("Add Subject")
                            add_subj_submitted = st.form_submit_button("Add Subject")
                            if add_subj_submitted and subject_name:
                                add_subject(exam_for_subject['id'], subject_name)
                                st.success(f"Subject '{subject_name}' added to exam '{exam_for_subject['name']}'!")

                        if subjects:
                            subject_for_topic = st.selectbox("Select Subject to add topics", subjects, format_func=lambda s: s['name'])
                            if subject_for_topic:
                                with st.form("add_topic_form", clear_on_submit=True):
                                    topic_name = st.text_input("Topic Name")
                                    priority = st.slider("Priority (1=High, 5=Low)", 1, 5, 3)
                                    difficulty = st.slider("Difficulty (1=Easy, 5=Hard)", 1, 5, 3)
                                    add_topic_submitted = st.form_submit_button("Add Topic")
                                    if add_topic_submitted and topic_name:
                                        add_topic(subject_for_topic['id'], topic_name, priority, difficulty)
                                        st.success(f"Topic '{topic_name}' added!")

                # --- AI Insights ---
                st.subheader("AI Insights")
                # Prepare data for insights
                subjects_map = {}
                topics_map = {}

                for exam in exams:
                    subjects_map[exam['id']] = get_subjects(exam['id'])
                    for subject in subjects_map[exam['id']]:
                        topics_map[subject['id']] = get_topics(subject['id'])

                insights = generate_ai_insights(exams, subjects_map, topics_map)
                for insight in insights:
                    st.info(insight)

                # --- Study Plan ---
                st.subheader("Personalized Study Plan")
                plan = generate_study_plan_with_topics(exams, subjects_map, topics_map)
                if plan:
                    for day in sorted(plan.keys()):
                        st.write(f"📅 {day}:")
                        for session in plan[day]:
                            st.write(f"- {session}")
                else:
                    st.write("No study plan available yet. Add exams and topics!")

            else:
                st.error("Invalid username or password.")

if __name__ == "__main__":
    main()
