#chat_bot logic
INTENTS = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "good morning", "good evening"],
        "response": "Hello! Welcome to Cognix. How can I assist you today?"
    },
    "how_are_you": {
        "keywords": ["how are you"],
        "response": "I'm great, thanks for asking!"
    },
    "who_are_you": {
        "keywords": ["who are you"],
        "response": "I am Cognix, a rule-based chatbot designed to answer predefined questions and provide basic information."
    },
    "joke":{
        "keywords":["tell me a joke"],
        "response": "what do you call a sick eagle? An Illegal..."

    },
    "weather":
    {
        "keywords":["hows the weather"],
        "response": "it feels sunny"

    },
    "what_is_cognix": {
        "keywords": ["what is cognix"],
        "response": "Cognix is a rule-based chatbot that responds using predefined rules and keyword matching."
    },
    "capabilities": {
        "keywords": ["what can you do", "how you can assist me"],
        "response": "I can answer predefined computer science questions, introduce myself, greet users, and provide motivational messages."
    },
    "your_name": {
        "keywords": ["what is your name", "your name"],
        "response": "My name is Cognix."
    },
    "thanks": {
        "keywords": ["thanks", "thank you"],
        "response": "You're welcome! I'm always happy to help."
    },
    "bye": {
        "keywords": ["bye", "goodbye", "see you", "take care"],
        "response": "Goodbye! Have a wonderful day."
    },
    "ai": {
        "keywords": ["ai", "artificial intelligence"],
        "response": "Artificial Intelligence is the simulation of human intelligence by computers to perform tasks such as learning, reasoning, and problem solving."
    },
    "machine_learning": {
        "keywords": ["machine learning", "ml"],
        "response": "Machine Learning is a branch of AI that enables computers to learn from data without being explicitly programmed."
    },
    "python": {
        "keywords": ["python"],
        "response": "Python is a high-level, easy-to-learn programming language used in web development, AI, automation, and data science."
    },
    "html": {
        "keywords": ["html"],
        "response": "HTML stands for HyperText Markup Language. It is used to create the structure of web pages."
    },
    "css": {
        "keywords": ["css"],
        "response": "CSS stands for Cascading Style Sheets. It is used to style and design web pages."
    },
    "motivate": {
        "keywords": ["motivate me", "motivation"],
        "response": "Believe in yourself. Every expert was once a beginner. Keep learning and never give up."
    },
    "stressed": {
        "keywords": ["im stressed", "stressed"],
        "response": "Take a short break, breathe, and focus on one task at a time. Small progress leads to big success."
    },
    "quote":{
        "keywords":["quote"],
        "response":"its never too late to start over!"
    }
}

DEFAULT_RESPONSE = "I'm sorry, I don't understand that. Please try asking something else."


def get_response(user_input: str) -> str:
    user_input = user_input.lower().strip()

    if not user_input:
        return DEFAULT_RESPONSE

    for intent_name, intent_data in INTENTS.items():
        keywords = intent_data.get("keywords", [])
        for keyword in keywords:
            if keyword in user_input:
                return intent_data.get("response", DEFAULT_RESPONSE)

    return DEFAULT_RESPONSE


def is_bye(user_input: str) -> bool:
    user_input = user_input.lower().strip()
    return any(keyword in user_input for keyword in INTENTS["bye"]["keywords"])
