import streamlit as st
import sqlite3
import pandas as pd

# Create a SQLite database connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")
conn.commit()

# Streamlit app
st.title("Student Database App")

# Form to input student data
st.write("### Add new student")
name = st.text_input("Name:")
email = st.text_input("Email:")
if st.button("Add Student"):
    if name and email:
        cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        st.success("Student added successfully!")

# Display student data
st.write("### Student Data:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=["ID", "Name", "Email"])
st.write(df)