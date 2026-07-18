import streamlit as st
import os
from huggingface_hub import hf_hub_download

# Page Configuration
st.set_page_config(page_title="AI Voice Cloning Studio", layout="centered")

st.title("Omega Voice Clone Tool")
st.write("Voice cloning model is loading from HuggingFace...")

# 1. HuggingFace se model automatic download/load karein
@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="Ehtisham01/Omega-Voice-Tool-Updated", 
        filename="model.pth"
    )
    return model_path

try:
    model_path = load_model()
    st.success(f"Model successfully loaded!")
    st.write(f"Model Path: {model_path}")
    
    # Yahan apna baaki ka UI ka code likhein (maslan input fields etc.)
    st.info("System is ready for processing.")

except Exception as e:
    st.error(f"Error loading model: {e}")

# Environment Variables
os.environ['DEVICE'] = "cpu" # Streamlit cloud par aksar CPU hi hota hai
os.environ['OUTPUT'] = "output/"
os.environ['SPEAKER'] = "speakers/"