"""
Project 1: Rule-Based AI Chatbot
Industrial Training Kit

Goal:
Create a simple rule-based chatbot that responds to predefined user inputs.

"""

def clean_text(text):
    """Sanitize user input by removing extra spaces and converting to lowercase."""
    return text.lower().strip()


def get_bot_response(user_input):
    """
    Decide the bot response using rule-based logic.
    This uses:
    - if/elif conditions for greetings and exit handling
    - a dictionary knowledge base for direct intent matching
    - a fallback response for unknown inputs
    """

    # Greeting rules
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]

    if user_input in greetings:
        return "Hello! I am your rule-based AI chatbot. How can I help you today?"

    # Exit rules
    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye! Thanks for chatting with me."

    # Knowledge base: 5+ predefined intents
    responses = {
        "what is your name": "My name is LogicBot, a simple rule-based AI chatbot.",
        "who created you": "I was created as part of an Artificial Intelligence Project 1 task.",
        "what can you do": "I can answer predefined questions, greet users, and exit cleanly.",
        "what is ai": "AI stands for Artificial Intelligence. It allows machines to simulate intelligent behavior.",
        "what is rule based ai": "Rule-based AI uses fixed rules and conditions to make decisions.",
        "help": "Try asking: 'what is ai', 'what can you do', 'what is your name', or type 'bye' to exit.",
        "thank you": "You're welcome!",
        "thanks": "You're welcome!"
    }

    # Dictionary lookup with fallback response
    else:
        return responses.get(
            user_input,
            "Sorry, I do not understand that yet. Type 'help' to see what I can answer."
        )


def main():
    """Run the chatbot in a continuous loop until the user gives an exit command."""
    print("=" * 50)
    print("🤖 LogicBot: Rule-Based AI Chatbot")
    print("=" * 50)
    print("Type 'help' for options or 'bye' / 'exit' to stop.\n")

    while True:
        raw_input_text = input("You: ")
        user_input = clean_text(raw_input_text)

        # Skip empty input
        if user_input == "":
            print("Bot: Please type something so I can respond.\n")
            continue

        bot_response = get_bot_response(user_input)
        print("Bot:", bot_response, "\n")

        # Clean break command
        if user_input in ["bye", "exit", "quit", "goodbye"]:
            break


if __name__ == "__main__":
    main()
