import streamlit as st
import requests

# Flask API URL (Change if deployed)
API_URL = "https://ec4e-106-221-31-240.ngrok-free.app"

# Streamlit UI
st.title("📑 IITM Daily Report Maintenance")

# Input fields for report submission
st.subheader("Submit a New Report")
domain = st.text_input("Project Name")
member = st.text_input("Name")
task = st.text_area("Today's Task Description")

if st.button("Submit Report"):
    if domain and member and task:
        response = requests.post(f"{API_URL}/add_report", json={
            "domain": domain,
            "member": member,
            "task": task
        })
        st.success(response.json().get("message"))
    else:
        st.warning("Please fill all fields!")

