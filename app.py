from modules.onboarding import onboarding_interface
from modules.topic_analyzer import extract_topics_from_syllabus
from modules.plan_generator import generate_study_plan
from modules.revision_engine import schedule_revisions
from modules.dashboard import show_dashboard

import streamlit as st

def main():
    st.title("IntelliPlan Study Planner")

    exam_date, study_hours, preference, syllabus_text = onboarding_interface()

    if syllabus_text:
        topics = extract_topics_from_syllabus(syllabus_text)
        plan_df = generate_study_plan(study_hours=study_hours, start_date=st.date.today(), end_date=exam_date, topics=topics)
        full_plan_df = schedule_revisions(plan_df)

        show_dashboard(full_plan_df)

if __name__ == "__main__":
    main()
