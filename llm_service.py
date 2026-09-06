import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def ask_ai(messages):
    """
    Sends messages to the selected LLM provider.

    messages should look like this:

    [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain AI in simple words."}
    ]
    """

    provider = os.getenv("LLM_PROVIDER", "ollama").lower()

    if provider == "gemini":
        return ask_gemini(messages)

    if provider == "openai":
        return ask_openai(messages)

    return ask_ollama(messages)


def ask_ollama(messages):
    url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
    model = os.getenv("OLLAMA_MODEL", "gemma3:270m")

    payload = {
        "model": model,
        "messages": messages,
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]


def ask_gemini(messages):
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url=os.getenv("GEMINI_BASE_URL")
    )
    model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message.content


def ask_openai(messages):
    client = OpenAI()
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    response = client.responses.create(
        model=model,
        input=messages
    )

    return response.output_text
