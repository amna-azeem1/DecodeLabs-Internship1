# Cognix – A Rule-Based Chatbot

Cognix is a professional, rule-based chatbot built as an educational semester project.
It answers predefined questions using **keyword matching and dictionary lookups only** —
no AI APIs, machine learning, or NLP models are involved.

## Features
- **Input sanitization**: sanitize the input using `.lower()` and `.script()`
- **Dictionary-based rule engine**: intents and keywords stored in a single Python dictionary instead of long if/else chains.
- **Fallback Mechanism** : provides fallback responses when input does not match with predefined keywords using `.get()`.
- **10+ intents**: greetings, chatbot identity, capabilities, AI, Machine Learning, Python,
  HTML, CSS, JavaScript, motivation, and more.
  **clean exit**: break command
- **web interface**: built with Flask (backend) + HTML/CSS/JS (frontend).
- **Dark & light theme toggle**
- **Welcome screen** with clickable suggestion prompts
- **Typing indicator** ("Cognix is typing...") and message timestamps
- **Responsive, full-screen layout**

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript (vanilla, no frameworks)
- **Logic**: Pure rule-based keyword matching (dictionary-driven)

## Project Structure

```
chatbot_project/
├── app.py              # Flask server connecting UI to chatbot logic
├── chatbot_logic.py     # Rule-based intents dictionary and response logic
└── templates/
    └── index.html       # Chat UI (HTML, CSS, JS)
```

## How to Run

1. Clone this repository:
   ```bash
   git clone : https://github.com/amna-azeem1/DecodeLabs-Internship1.git
   cd cognix-chatbot
   ```

2. Install Flask:
   ```bash
   pip install flask
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser at `http://127.0.0.1:5000`

## How It Works

User input is normalized with `.lower()` and checked against a dictionary of intents
(`INTENTS`), where each intent maps to a list of keyword variants and a single response.
If no keyword matches, Cognix returns a polite fallback message asking the user to rephrase.

## Author

Amna Azeem
