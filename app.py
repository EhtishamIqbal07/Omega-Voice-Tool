import streamlit as st
import os
from TTS.api import TTS

st.title("Omega Voice Clone Tool")

# Model load karne ka function
@st.cache_resource
def load_tts_engine():
    # XTTS v2 model load karna
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")
    return tts

# Engine load karein
try:
    with st.spinner("Loading AI Voice Engine..."):
        tts = load_tts_engine()
        st.success("Engine Ready!")
except Exception as e:
    st.error(f"Engine Load Error: {e}")

text_input = st.text_area("Enter text:", "Hello, welcome to Omega Voice Tool.")

if st.button("Generate Audio"):
    if text_input:
        # Reference file ka sahi path
        ref_wav = "reference.wav"
        
        if os.path.exists(ref_wav):
            with st.spinner("Generating audio..."):
                try:
                    tts.tts_to_file(text=text_input,
                                    file_path="output.wav",
                                    speaker_wav=ref_wav,
                                    language="en")
                    st.audio("output.wav")
                except Exception as e:
                    st.error(f"Generation Error: {e}")
        else:
            st.error(f"Error: {ref_wav} file not found in directory!")
    else:
        st.error("Please enter some text first.")