import sqlite3
from datetime import date

DB_PATH = "intelliplan.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Exams
    c.execute('''
        CREATE TABLE IF NOT EXISTS exams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            exam_date DATE,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    # Subjects
    c.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exam_id INTEGER,
            name TEXT,
            FOREIGN KEY(exam_id) REFERENCES exams(id)
        )
    ''')
    # Topics
    c.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER,
            name TEXT,
            priority INTEGER,  -- 1 (highest) to 5 (lowest)
            difficulty INTEGER, -- 1 (easy) to 5 (hard)
            FOREIGN KEY(subject_id) REFERENCES subjects(id)
        )
    ''')
    conn.commit()
    conn.close()

# Exam functions (same)
def add_exam(user_id, exam_name, exam_date):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO exams (user_id, name, exam_date) VALUES (?, ?, ?)",
              (user_id, exam_name, exam_date))
    conn.commit()
    conn.close()

def get_exams(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name, exam_date FROM exams WHERE user_id = ? ORDER BY exam_date ASC", (user_id,))
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "exam_date": r[2]} for r in rows]

# Subjects
def add_subject(exam_id, subject_name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO subjects (exam_id, name) VALUES (?, ?)", (exam_id, subject_name))
    conn.commit()
    conn.close()

def get_subjects(exam_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name FROM subjects WHERE exam_id = ?", (exam_id,))
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]

# Topics
def add_topic(subject_id, topic_name, priority, difficulty):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO topics (subject_id, name, priority, difficulty) VALUES (?, ?, ?, ?)",
              (subject_id, topic_name, priority, difficulty))
    conn.commit()
    conn.close()

def get_topics(subject_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name, priority, difficulty FROM topics WHERE subject_id = ?", (subject_id,))
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "priority": r[2], "difficulty": r[3]} for r in rows]
