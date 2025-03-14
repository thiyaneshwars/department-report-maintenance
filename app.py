import streamlit as st
import requests

# Flask API URL (Change if deployed)
API_URL = "https://ada5-103-115-236-19.ngrok-free.app"

# Streamlit UI
st.title("📑 T2T Project Report Maintenance")

# Department selection with dropdown
departments = [
    "Audio Input & Speech Recognition",
    "Pronunciation Analysis",
    "Conversational Response System",
    "Audio Recording & Cloud Storage",
    "Web Portal for Feedback Access"
]  # Updated department names

selected_department = st.selectbox("Project Domain", departments)

# Member selection based on department
members = {
    "Audio Input & Speech Recognition": ["Module 1: Audio Input & Speech Recognition - Capture audio input from a microphone and transcribe it into text."],
    "Pronunciation Analysis": ["Module 2: Pronunciation Analysis - Detect pronunciation mistakes and provide corrective feedback."],
    "Conversational Response System": ["Module 3: Conversational Response System - Deliver engaging conversational responses for correct pronunciation."],
    "Audio Recording & Cloud Storage": ["Module 4: Audio Recording & Cloud Storage - Record all audio sessions and upload them securely to the cloud."],
    "Web Portal for Feedback Access": ["Module 5: Web Portal for Feedback Access - Provide a secure web interface for feedback access."]
}

selected_member = st.selectbox("Member Name", members.get(selected_department, []))

task = st.text_area("Task Description")

if st.button("Submit Report"):
    if selected_department and selected_member and task:
        response = requests.post(f"{API_URL}/add_report", json={
            "department": selected_department,
            "member": selected_member,
            "task": task
        })
        st.success(response.json().get("message"))
    else:
        st.warning("Please fill all fields!")

