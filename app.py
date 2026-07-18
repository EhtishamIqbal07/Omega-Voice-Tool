from huggingface_hub import hf_hub_download
import os
import subprocess
from loguru import logger

# 1. HuggingFace se model automatic download/load karein
model_path = hf_hub_download(
    repo_id="Ehtisham01/Omega-Voice-Tool-Updated", 
    filename="model.pth"
)
logger.info(f"Model successfully loaded from: {model_path}")

# 2. Environment variables set karein (taake code ko pata ho ke files kahan hain)
os.environ['DEVICE'] = "cuda" # Agar Streamlit par GPU na ho toh "cpu" kar dein
os.environ['OUTPUT'] = "output/"
os.environ['SPEAKER'] = "speakers/"
os.environ['MODEL_SOURCE'] = "local"
os.environ["MODEL_VERSION"] = "v2.0.2"
os.environ["LANGUAGE"] = "Auto"
os.environ["LOWVRAM_MODE"] = "false"
os.environ["DEEPSPEED"] = "false"

# 3. Streamlit app launch karein
if __name__ == "__main__":
    from xtts_webui import demo
    # Streamlit par chalane ke liye direct launch
    demo.launch(share=True, inbrowser=True)