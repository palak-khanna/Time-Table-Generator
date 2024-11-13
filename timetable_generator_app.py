import sqlite3
import pandas as pd
import streamlit as st

# Initialize the database
def initialize_database():
    conn = sqlite3.connect("timetable.db")
    cursor = conn.cursor()

    # Create tables if they don’t exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS instructors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                      );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        instructor_id INTEGER,
                        total_hours INTEGER DEFAULT 42,
                        FOREIGN KEY (instructor_id) REFERENCES instructors (id)
                      );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS schedule (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        course_id INTEGER,
                        day TEXT,
                        start_time TEXT,
                        end_time TEXT,
                        FOREIGN KEY (course_id) REFERENCES courses (id)
                      );''')
    conn.commit()
    conn.close()

# Call the function to initialize the database
initialize_database()

# Connection function
def create_connection():
    return sqlite3.connect("timetable.db")

# Add instructor to database
def add_instructor(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO instructors (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

# Add course to database
def add_course(name, instructor_name, total_hours=42):
    conn = create_connection()
    cursor = conn.cursor()
    # Fetch instructor ID based on the instructor name
    cursor.execute("SELECT id FROM instructors WHERE name = ?", (instructor_name,))
    instructor = cursor.fetchone()
    if instructor:
        instructor_id = instructor[0]
        cursor.execute("INSERT OR IGNORE INTO courses (name, instructor_id, total_hours) VALUES (?, ?, ?)",
                       (name, instructor_id, total_hours))
    conn.commit()
    conn.close()

# Display timetable function
def display_schedule():
    conn = create_connection()
    query = '''SELECT courses.name AS Course,
                      instructors.name AS Instructor,
                      schedule.day AS Day,
                      schedule.start_time AS Start,
                      schedule.end_time AS End
               FROM schedule
               JOIN courses ON schedule.course_id = courses.id
               JOIN instructors ON courses.instructor_id = instructors.id
               ORDER BY Day, Start'''
    timetable_df = pd.read_sql_query(query, conn)
    conn.close()
    return timetable_df

# Streamlit UI
st.title("Timetable Generator")

# Add Instructor Section
st.subheader("Add Instructor")
instructor_name = st.text_input("Instructor Name")
if st.button("Add Instructor"):
    if instructor_name:
        add_instructor(instructor_name)
        st.success(f"Instructor '{instructor_name}' added.")
    else:
        st.error("Please enter a name for the instructor.")

# Add Course Section
st.subheader("Add Course")
course_name = st.text_input("Course Name")
conn = create_connection()
instructor_list = pd.read_sql_query("SELECT * FROM instructors", conn)
conn.close()

if not instructor_list.empty:
    instructor_choice = st.selectbox("Assign Instructor", instructor_list["name"].tolist())
    total_hours = st.number_input("Total Hours", min_value=1, max_value=42, value=42)
    if st.button("Add Course"):
        if course_name:
            add_course(course_name, instructor_choice, total_hours)
            st.success(f"Course '{course_name}' added with Instructor '{instructor_choice}'.")
        else:
            st.error("Please enter a course name.")
else:
    st.warning("Add at least one instructor first.")

# Display Timetable Section
st.subheader("Generated Timetable")
if st.button("Show Timetable"):
    timetable_df = display_schedule()
    st.write(timetable_df if not timetable_df.empty else "No timetable generated yet.")
