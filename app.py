import streamlit as st
from gtts import gTTS
import os

# Page Configuration
st.set_page_config(page_title="Omega Voice Clone Tool", layout="centered")

st.title("Omega Voice Clone Tool")

# User Input
text_input = st.text_area("Enter text to convert to voice:", "Hello, welcome to Omega Voice Tool.")

# Generation Logic
if st.button("Generate Audio"):
    if text_input:
        with st.spinner("Generating audio..."):
            try:
                # gTTS processing
                tts = gTTS(text=text_input, lang='en')
                tts.save("output.mp3")
                
                # Play the generated audio
                st.audio("output.mp3")
                st.success("Audio generated successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter some text first.")