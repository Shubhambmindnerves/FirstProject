import streamlit as st
from summarizer import summarize_text
from youtube_utils import get_transcript
from pdf_utils import create_pdf

st.set_page_config(page_title="YouSumm AI", layout="wide")

st.title("🚀 Multi-Model YouTube & Text Summarizer")

# -----------------------------
# Provider Selection
# -----------------------------
provider = st.sidebar.selectbox(
    "Select Provider",
    ["ollama", "openai", "gemini"]
)

# -----------------------------
# Model Selection
# -----------------------------
if provider == "ollama":
    model_name = st.sidebar.selectbox(
        "Select Local Model",
        ["phi", "tinyllama"]  # Only installed models
    )


elif provider == "openai":
    model_name = st.sidebar.selectbox(
        "Select OpenAI Model",
        ["gpt-4o-mini"]
    )

elif provider == "gemini":
    model_name = "gemini-pro"


tab1, tab2 = st.tabs(["Text Summarize", "YouTube Summarize"])

# -----------------------------------
# TEXT SUMMARIZE
# -----------------------------------
with tab1:
    text_input = st.text_area("Paste your text here")

    if st.button("Summarize Text"):
        if text_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarize_text(provider, model_name, text_input)

            st.write(summary)

            pdf_buffer = create_pdf(summary)

            st.download_button(
                label="📥 Download PDF",
                data=pdf_buffer,
                file_name="summary.pdf",
                mime="application/pdf"
            )


# -----------------------------------
# YOUTUBE SUMMARIZE
# -----------------------------------
with tab2:
    youtube_url = st.text_input("Enter YouTube URL")

    if st.button("Summarize Video"):
        if youtube_url.strip() == "":
            st.warning("Please enter YouTube URL.")
        else:
            with st.spinner("Fetching transcript..."):
                transcript = get_transcript(youtube_url)

            if not transcript:
                st.error("Transcript not available or invalid URL.")
            else:
                with st.spinner("Summarizing video..."):
                    summary = summarize_text(provider, model_name, transcript)

                st.write(summary)

                pdf_buffer = create_pdf(summary)

                st.download_button(
                    label="📥 Download PDF",
                    data=pdf_buffer,
                    file_name="video_summary.pdf",
                    mime="application/pdf"
                )
