import streamlit as st
import requests

# Flask API URL (Change if deployed)

API_URL = "https://31a0-103-115-236-19.ngrok-free.app"

# Streamlit UI
st.title("📑IITM Project Report Maintenance")



# Department selection with dropdown
departments = ["HUMAN FACE RECOGNITION AND MOVEMENT RECOGNITION","TELUGU DATA AUGMENTATION","BERT FINETUNING","ENGLISH AUGMENTATION","T5 FINETUNING","ASR TELUGU"]  # Example departments
selected_department = st.selectbox("Project Domain", departments)

# Member selection based on department
members = {
    "HUMAN FACE RECOGNITION AND MOVEMENT RECOGNITION": ["VARATHARAJAN","SURENDAR KRISHANA","RUBAN B","KAVINESH K","ARUNHARIHARAN","PAVITHRAN G","PRAVEEN S"],
    "TELUGU DATA AUGMENTATION": ["MADHAN J","ABINITHI G","MATHIARASI E","CHARAN B","SRI VISHNU TS"],
    "BERT FINETUNING": ["THRISHA S","MUTHU DEEPAK V","DHARANISRI"],
    "ENGLISH AUGMENTATION": ["ANUSH S","KIRITHIKA G","NANDHAKUMAR R","SUSEE KARTHIKA A","DINESH S","EZHILANAND V","SUBASREE R","VARUN A K"],
    "T5 FINETUNING":["KAVIN R" ,"KARMUGILAN G R"],
    "ASR TELUGU":["VASANTH S" ,"KAVIN R","MADHAN J","GOWTHAM S"]
    
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


