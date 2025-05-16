import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", page_title="Intelliplan Dashboard")

# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Intelliplan",
        options=["Dashboard", "Planner", "Analytics", "Settings"],
        icons=["speedometer", "calendar", "bar-chart", "gear"],
        menu_icon="grid-3x3-gap-fill",
        default_index=0,
    )

# Top bar
st.markdown("## 📊 Welcome to Intelliplan")
st.markdown("Here's your smart planner and productivity dashboard.")

# Layout Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Tasks Completed", value="15", delta="+5 today")
with col2:
    st.metric(label="Focus Hours", value="4h", delta="+1.5h")
with col3:
    st.metric(label="Planner Streak", value="🔥 7 days")

# Tabs or Sections
tab1, tab2, tab3 = st.tabs(["📅 Daily View", "📈 Weekly Summary", "🧠 Focus Mode"])

with tab1:
    st.subheader("Today's Tasks")
    st.checkbox("✅ Meeting with team")
    st.checkbox("✅ Design mockup review")
    st.checkbox("🔲 30-min deep work")

with tab2:
    st.subheader("Weekly Analytics")
    st.line_chart({"Focus Hours": [2, 3.5, 4, 2.5, 5]})

with tab3:
    st.subheader("Focus Tools")
    st.button("Start Pomodoro")
    st.button("Open Calm Sound")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Sudheera")
