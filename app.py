import streamlit as st
from llm_service import ask_ai

st.set_page_config(
    page_title="Day 1 AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Day 1 AI Assistant")
st.write("Ask me anything about AI, Python, productivity, or learning.")

SYSTEM_PROMPT = """
You are a friendly AI tutor for beginner students.
Explain concepts clearly.
Use simple examples.
Avoid unnecessary jargon.
When possible, give short practical examples.
"""

# list = ["",""], tuple = ("",""), set{"",""}, dic = [{"name": , key:value },{}]
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_prompt = st.chat_input("Ask your question...")

if user_prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = ask_ai(st.session_state.messages)
            st.markdown(ai_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })
