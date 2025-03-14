import streamlit as st


# Streamlit UI
st.title("📑 Phonics Kit Project Report Maintenance")

# Department selection with dropdown
departments = [
    "Audio Input & Speech Recognition",
    "Pronunciation Analysis",
    "Conversational Response System",
    "Audio Recording & Cloud Storage",
    "Web Portal for Feedback Access"
]  # Updated department names

selected_department = st.selectbox("Project Task", departments)

# Task description display based on department
tasks = {
    "Audio Input & Speech Recognition": '''Task: Capture audio input from the microphone and transcribe it into text.
Recommended Algorithm: Whisper (OpenAI) or DeepSpeech (Mozilla)
✅ Why? Whisper offers highly accurate transcription, even for noisy environments, and supports multiple languages. DeepSpeech is lightweight and ideal for real-time processing.

Description of Algorithm (Whisper):

Uses an encoder-decoder transformer model.
The encoder maps audio features into a latent space.
The decoder predicts text tokens by learning audio patterns.
It uses beam search decoding to improve transcription accuracy.''',
    "Pronunciation Analysis": " Detect pronunciation mistakes and provide corrective feedback.",
    "Conversational Response System": " Deliver engaging conversational responses for correct pronunciation.",
    "Audio Recording & Cloud Storage": " Record all audio sessions and upload them securely to the cloud.",
    "Web Portal for Feedback Access": " Provide a secure web interface for feedback access."
}

selected_task = st.text_area("Task Description", tasks.get(selected_department, ""))

