# Rule-Based AI Chatbot
# Project 1 - DecodeLabs

print("====================================")
print(" Welcome to the Rule-Based Chatbot ")
print(" Type 'bye', 'exit', or 'quit' to stop.")
print("====================================")

# Knowledge Base (Predefined Responses)
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "My name is jaravis.",
    "who created you": "I was created as part of the to talk with user.",
    "help": "You can ask me greetings, my name, today's purpose, or type 'bye' to exit.",
    "what can you do": "I can answer simple predefined questions.",
    "good morning": "Good Morning! Have a wonderful day!",
    "good evening": "Good Evening! Hope you're doing well.",
    "thank you": "You're welcome! Happy to help."
}

# Continuous Chat Loop
while True:
    user_input = input("\nYou: ").lower().strip()

    # Exit Commands
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    # Check if input exists in knowledge base
    elif user_input in responses:
        print("Bot:", responses[user_input])

    # Default Response
    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")