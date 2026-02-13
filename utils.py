import ollama
from config import openai_client, gemini_model


def generate_response(provider, prompt, model_name):

    if provider == "ollama":
        response = ollama.chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]

    elif provider == "openai":
        response = openai_client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    elif provider == "gemini":
        response = gemini_model.generate_content(prompt)
        return response.text

    else:
        return "Invalid provider"
