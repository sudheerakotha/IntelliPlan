import streamlit as st
import pandas as pd
import random

def show_dashboard(study_df):
    st.subheader("📊 Study Plan Overview")
    st.dataframe(study_df)

    completed = st.slider("Mark % of topics completed", 0, 100, 25)
    st.progress(completed / 100.0)

    quotes = [
        "🚀 Progress, not perfection!",
        "📚 Every day is a step forward.",
        "💪 You’re doing amazing!"
    ]
    st.success(random.choice(quotes))
