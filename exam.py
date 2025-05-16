import sqlite3
import streamlit as st

def add_exam(username):
    st.subheader("Add New Exam")
    exam_name = st.text_input("Exam Name")
    date = st.date_input("Exam Date")
    if st.button("Save Exam"):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS exams (username TEXT, exam_name TEXT, date TEXT)")
        c.execute("INSERT INTO exams (username, exam_name, date) VALUES (?, ?, ?)", (username, exam_name, str(date)))
        conn.commit()
        conn.close()
        st.success("Exam saved!")

def view_exams(username):
    st.subheader("Your Exams")
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT exam_name, date FROM exams WHERE username = ?", (username,))
    exams = c.fetchall()
    conn.close()
    for exam in exams:
        st.write(f"{exam[0]} on {exam[1]}")
