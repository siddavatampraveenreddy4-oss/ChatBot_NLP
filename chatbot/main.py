# chatbot.py

def chatbot_response(user_input):
    # Convert input to lowercase to make it case-insensitive
    user_input = user_input.lower()

    # Predefined responses
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you": " iam good what about you",
        "hi": "hello how can i help you!",
        "bye": "Goodbye! Have a nice day!",
        "your name": "I'm ChatBot 🤖, your virtual assistant."
    }

    # Check if the input matches a predefined response
    for key in responses:
        if key in user_input:
            return responses[key]

    # Default response
    return "I'm not sure I understand. Can you try saying that differently?"

# Main chatbot loop
print("🤖 ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")

    if "bye" in user_input.lower():
        print("🤖 ChatBot: Goodbye! 👋")
        break

    print(f"🤖 ChatBot: {chatbot_response(user_input)}")
