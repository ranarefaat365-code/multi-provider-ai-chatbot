from llm_service import ask_ai

messages = [
    {
        "role": "system",
        "content": "You are a friendly AI tutor. Explain things simply."
    }
]

print("AI Assistant is ready!")
print("Type 'exit' to stop.\n")


while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    ai_response = ask_ai(messages)

    messages.append({
        "role": "assistant",
        "content": ai_response
    })

    print(f"\nAI: {ai_response}\n")
