# app.py
# Cognix - Flask server connecting the rule-based logic to the web UI

from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message", "")
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
