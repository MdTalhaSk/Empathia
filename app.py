import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

# Load environment variables from .env
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the chatbot using the API key
genai.configure(api_key=api_key)

# Flask app setup
app = Flask(__name__)

# Initialize the chatbot model
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="you are a chatbot that provides mental health and emotional support to students.",
)

# Start chat session
chat_session = model.start_chat(history=[])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if user_message:
        # Send the user's message to the chatbot and get the response
        response = chat_session.send_message(user_message)
        return jsonify({"response": response.text})

    return jsonify({"response": "I didn't understand that, could you try again?"})

if __name__ == "__main__":
    app.run(debug=True)
