from utils import generate_response

def chunk_text(text, size=1000):
    """
    Split text into smaller chunks of given size.
    """
    return [text[i:i+size] for i in range(0, len(text), size)]

def summarize_text(provider, model_name, text):
    """
    Summarize large text efficiently by chunking.
    Works with local TinyLlama, Phi, or cloud providers.
    """
    # -----------------------------
    # Chunk text if it's large
    # -----------------------------
    chunks = chunk_text(text, size=1000)  # 1000 characters per chunk
    summaries = []

    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i+1}/{len(chunks)}...")

        prompt = f"""
        Summarize the following text clearly in structured bullet points:

        {chunk}
        """

        # Generate response for each chunk
        summary = generate_response(provider, prompt, model_name)
        summaries.append(summary)

    # -----------------------------
    # Combine summaries into final summary
    # -----------------------------
    combined = "\n".join(summaries)

    final_prompt = f"""
    Create a final concise and well-structured summary from these chunk summaries.
    Provide:
    - Key points in bullet format
    - Short overall summary at the end

    {combined}
    """

    final_summary = generate_response(provider, final_prompt, model_name)

    return final_summary
