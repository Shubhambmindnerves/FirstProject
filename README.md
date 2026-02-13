# YouSumm - YouTube Video Summarizer (GenAI)

YouSumm is a Python-based **YouTube video summarizer** app with a **Streamlit UI**.  
It supports multiple AI providers: **Ollama (local models)**, **OpenAI**, and **Google Gemini**.  

Users can input **YouTube video URLs** or plain text, and get **structured summaries**.  
Summaries can also be downloaded as **PDF**.

---

## Features

- ✅ Summarize **YouTube video transcripts** or text
- ✅ Supports **multiple AI providers**:
  - Ollama (`tinyllama`, `phi`) — local models, free
  - OpenAI (`gpt-4o-mini`, `gpt-4`, etc.)
  - Gemini API (Google’s GenAI)
- ✅ Chunking for **long texts / transcripts**
- ✅ PDF download of summaries
- ✅ Streamlit UI with **model selection**
- ✅ Local CPU friendly using **tinyllama**
- ✅ Handles long transcripts efficiently

---

## Installation

1. Clone the repo:
git clone https://github.com/Shubhambmindnerves/FirstProject.git
cd YouSumm
Create virtual environment:

python -m venv .venv
source .venv/Scripts/activate   # Windows
# or
source .venv/bin/activate       # Linux/Mac
Install requirements:

pip install -r requirements.txt
Install Ollama and pull local models:

# Make sure Ollama is installed
ollama list        # to see installed models
ollama pull phi    # pull local model phi
ollama pull tinyllama  # optional small fast model
Usage
Run the Streamlit app:

streamlit run app.py
Open the browser (Streamlit will provide a URL, usually http://localhost:8501)

Steps in the app:

Select Provider: Ollama / OpenAI / Gemini

Select Model: e.g., tinyllama or phi

Enter YouTube URL or text

Click Summarize

(Optional) Download PDF of summary

Project Structure
YouSumm/
│
├─ app.py             # Main Streamlit app
├─ utils.py           # Helper functions (model calls, PDF creation)
├─ summarize.py       # Text summarization with chunking
├─ youtube_utils.py   # YouTube transcript extraction
├─ requirements.txt   # Python dependencies
├─ README.md          # Project documentation
├─ .gitignore         # Ignore files/folders in git
└─ .venv/             # Virtual environment (ignored)
