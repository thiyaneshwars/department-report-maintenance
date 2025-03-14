import streamlit as st

# Streamlit UI
st.title("📑 Project T2T")

# Department selection with dropdown
departments = [
    "Audio Input & Speech Recognition",
    "Pronunciation Analysis",
    "Conversational Response System",
    "Audio Recording & Cloud Storage",
    "Web Portal for Feedback Access"
]  # Updated department names
st.markdown("**Project Task**", unsafe_allow_html=True)
selected_department = st.selectbox( " ",departments)



# Task description display based on department
tasks = {
    "Audio Input & Speech Recognition": '''
    **Task:** Capture audio input from the microphone and transcribe it into text.

    **Recommended Algorithm:** Whisper (OpenAI) or DeepSpeech (Mozilla)

    **Why?** Whisper offers highly accurate transcription, even for noisy environments, and supports multiple languages. DeepSpeech is lightweight and ideal for real-time processing.

    **Description of Algorithm (Whisper):**
    - Uses an encoder-decoder transformer model.
    - The encoder maps audio features into a latent space.
    - The decoder predicts text tokens by learning audio patterns.
    - It uses beam search decoding to improve transcription accuracy.
    ''',

    "Pronunciation Analysis": '''
    **Task:** Analyze user pronunciation and identify errors.

    **Recommended Algorithm:** Dynamic Time Warping (DTW) or Phoneme Recognition (CMUdict + Phonemizer)

    **Why?** DTW effectively compares audio sequences by aligning time-series data, while CMUdict provides precise phoneme mapping.

    **Description of Algorithm (DTW):**
    - Extracts MFCC (Mel-frequency cepstral coefficients) features from both reference and user speech.
    - Measures the cumulative distance between corresponding audio frames.
    - Identifies timing errors, phoneme mismatches, and speech rhythm issues.
    - Offers flexibility for varying speech speeds and patterns.
    ''',

    "Conversational Response System": '''
    **Task:** Provide real-time conversational responses similar to Google Assistant or Alexa.

    **Recommended Algorithm:** Rasa NLU or Dialogflow

    **Why?** Rasa NLU offers flexible customization, strong intent recognition, and context-aware responses.

    **Description of Algorithm (Rasa NLU):**
    - Uses intent classification to identify the user's request.
    - Utilizes entity extraction to identify key terms like names, numbers, or locations.
    - Implements transformer-based embeddings for improved conversational flow.
    - Ensures seamless back-and-forth dialogue with dynamic response generation.
    ''',

    "Audio Recording & Cloud Storage": '''
    **Task:** Record audio feedback and securely store it in the cloud.

    **Recommended Tools:** FFmpeg (Recording) + AWS S3/Firebase (Cloud Storage)

    **Why?** FFmpeg efficiently handles noise reduction and format conversion, while AWS S3/Firebase ensures secure data storage.

    **Description of Process:**
    - Captures audio in high-quality formats like .wav or .mp3.
    - Applies denoising filters for cleaner audio storage.
    - Ensures encrypted cloud uploads for secure data access.
    ''',

    "Web Portal for Feedback Access": '''
    **Task:** Provide teachers, doctors, and parents access to pronunciation feedback via a web interface.

    **Recommended Frameworks:** Flask/Django (Backend) + React.js/Next.js (Frontend)

    **Why?** Flask/Django ensures fast API development, while React.js/Next.js offers a smooth and interactive user experience.

    **Description of Process:**
    - Provides a secure login portal for authorized users.
    - Displays recorded audio files, pronunciation scores, and improvement tips.
    - Uses REST APIs to connect the database, cloud storage, and user interface seamlessly.
    '''
}
st.markdown(tasks.get(selected_department, ""), unsafe_allow_html=True)

# Enlarged text area for better visibility
#selected_task = st.text_area("Task Description", tasks.get(selected_department, ""), height=300)
