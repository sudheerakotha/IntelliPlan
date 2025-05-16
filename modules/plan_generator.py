import pandas as pd
from datetime import timedelta

def generate_study_plan(start_date, end_date, topics, daily_hours):
    total_days = (end_date - start_date).days + 1
    hours_per_topic = daily_hours
    schedule = []

    for i, topic in enumerate(topics):
        day = start_date + timedelta(days=i % total_days)
        schedule.append({"Date": day, "Topic": topic.strip(), "Hours": hours_per_topic})

    return pd.DataFrame(schedule)
