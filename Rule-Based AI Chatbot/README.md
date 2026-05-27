# Project 1: Rule-Based AI Chatbot

## Objective
Create a simple rule-based chatbot that responds to predefined user inputs.

## Features
- Handles greetings such as `hi`, `hello`, and `hey`
- Handles exit commands such as `bye`, `exit`, and `quit`
- Uses `if/elif/else` decision-making logic
- Runs inside a continuous `while True` loop
- Sanitizes input using `.lower().strip()`
- Uses a dictionary knowledge base with more than 5 predefined intents
- Gives a fallback response for unknown questions

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run:

```bash
python chatbot.py
```

## Sample Conversation
```text
You: hello
Bot: Hello! I am your rule-based AI chatbot. How can I help you today?

You: what is ai
Bot: AI stands for Artificial Intelligence. It allows machines to simulate intelligent behavior.

You: bye
Bot: Goodbye! Thanks for chatting with me.
```
