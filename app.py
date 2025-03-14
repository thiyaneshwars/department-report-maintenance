import streamlit as st
import requests

# Flask API URL (Change if deployed)

API_URL = " https://ada5-103-115-236-19.ngrok-free.app"

# Streamlit UI
st.title("📑IITM Project Report Maintenance")



# Department selection with dropdown
departments = [" Audio Input & Speech Recognition","Pronunciation Analysis","Conversational Response System","Audio Recording & Cloud Storage","Web Portal for Feedback Access"]  # Example departments
selected_department = st.selectbox("Project Domain", departments)

# Member selection based on department
members = {
    "Audio Input & Speech Recognition": ["Module 1: Audio Input & Speech Recognition
Objective: Capture audio input from a microphone and transcribe it into text.
Algorithm/Tools:
Whisper by OpenAI - A robust speech recognition model trained on diverse datasets, ensuring high accuracy in noisy environments. It supports multiple languages and provides strong transcription performance.
VOSK - An efficient offline speech recognition system that requires minimal resources, making it ideal for lightweight devices and real-time applications.
Steps:
Capture audio using sounddevice or pyaudio.
Use Whisper or VOSK to convert audio into text.
Store the transcribed text for further processing.
"],
    "Pronunciation Analysis": ["Objective: Detect pronunciation mistakes and provide corrective feedback.

Algorithm/Tools:

Levenshtein Distance (Edit Distance Algorithm) - Measures the number of single-character edits (insertions, deletions, substitutions) needed to change one word into another. It’s highly effective for detecting pronunciation errors by comparing expected and actual phoneme sequences.

G2P (Grapheme-to-Phoneme Conversion) - Maps written text (graphemes) into corresponding phonetic representations (phonemes). This helps analyze how words should sound versus how they were spoken.

CMU Pronouncing Dictionary (CMUdict) - A reliable phonetic dictionary that offers precise phoneme sequences for English words, useful for comparing correct vs. incorrect pronunciation.

Steps:

Convert transcribed text into phonemes using Phonemizer or CMUdict.

Compare the expected phoneme sequence with the actual phoneme sequence.

Use Levenshtein Distance to calculate differences.

Provide immediate feedback (e.g., visual indicator or sound cue) when a mistake occurs.

"],
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


