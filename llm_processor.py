import requests
import json

# Set your Groq API key here
GROQ_API_KEY = "Set your Groq API key here"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  

def process_text(text):
    """Sends text to Groq's LLM API and returns the processed response."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",  # Update this if you have access to a different model
        "messages": [
            {"role": "system", "content": "Summarize the given text."},
            {"role": "user", "content": text}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"Error processing text: {str(e)}"

# Example test
if __name__ == "__main__":
    sample_text = "This is a test text to check how Groq API processes it."
    print(process_text(sample_text))
