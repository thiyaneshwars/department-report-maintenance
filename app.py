import streamlit as st
import requests

# Flask API URL (Change if deployed)
API_URL = "  http://localhost:5000"

# Streamlit UI
st.title("📑 Department Report Maintenance")

# Input fields for report submission
st.subheader("Submit a New Report")
department = st.text_input("Department")
member = st.text_input("Member Name")
task = st.text_area("Task Description")

if st.button("Submit Report"):
    if department and member and task:
        response = requests.post(f"{API_URL}/add_report", json={
            "department": department,
            "member": member,
            "task": task
        })
        st.success(response.json().get("message"))
    else:
        st.warning("Please fill all fields!")

# Fetch and display reports
st.subheader("📋 Submitted Reports")


