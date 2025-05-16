import streamlit as st
from auth import create_tables as auth_create_tables, register_user, verify_user
from exam import create_tables as exam_create_tables, add_exam, view_exams

# Initialize database tables for both auth and exams
auth_create_tables()
exam_create_tables()

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

def login():
    st.title("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type='password', key="login_pass")
    if st.button("Login"):
        if verify_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password.")

def register():
    st.title("Register")
    username = st.text_input("Choose a username", key="reg_user")
    password = st.text_input("Choose a password", type='password', key="reg_pass")
    if st.button("Register"):
        if register_user(username, password):
            st.success("Registration successful! Please login.")
        else:
            st.error("Username already exists.")

def dashboard():
    st.title("📘 IntelliPlan Dashboard")
    st.write(f"Welcome, **{st.session_state.username}**! Plan your exams below:")
    
    st.subheader("📝 Add Exam")
    add_exam(st.session_state.username)
    
    st.subheader("📅 Your Exams")
    view_exams(st.session_state.username)

    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.experimental_rerun()

def main():
    st.sidebar.title("📚 IntelliPlan")
    if st.session_state.logged_in:
        dashboard()
    else:
        page = st.sidebar.radio("Navigation", ["Login", "Register"])
        if page == "Login":
            login()
        elif page == "Register":
            register()

if __name__ == "__main__":
    main()
