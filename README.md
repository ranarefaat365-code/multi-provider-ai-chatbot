# AI Assistant

A beginner-friendly AI chatbot with two interfaces (terminal + web) and one
shared "brain" that can talk to **Gemini**, **OpenAI**, or a local **Ollama**
model — switchable from a single setting.

## What's inside

| File | Job |
|------|-----|
| `cli_chat.py` | Terminal chatbot |
| `app.py` | Web chatbot (Streamlit) |
| `llm_service.py` | The brain — routes messages to the chosen AI provider |
| `.env` | Your private settings + API key (never uploaded) |
| `.env.example` | A safe template showing which settings to create |

## How it works

Every AI chat is a growing list of messages:

```python
[
    {"role": "system",    "content": "You are a friendly tutor."},
    {"role": "user",      "content": "Explain AI simply."},
    {"role": "assistant", "content": "AI is..."}
]
```

Both interfaces run the same loop: read input → add user message → ask the AI →
add the reply → repeat. `llm_service.py` decides which provider answers based on
`LLM_PROVIDER` in `.env`.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill in your real key:
   ```bash
   cp .env.example .env
   ```
3. Run the terminal version:
   ```bash
   python cli_chat.py
   ```
   Or the web version:
   ```bash
   streamlit run app.py
   ```

## Providers

- **Gemini** (default): needs a free API key from Google AI Studio.
- **OpenAI**: needs an OpenAI API key.
- **Ollama**: runs a model locally, no key needed (install from ollama.com).

Switch provider by editing `LLM_PROVIDER` in `.env`.

---
