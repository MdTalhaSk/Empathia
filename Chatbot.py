import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the Generative AI API
genai.configure(api_key=api_key)

# Create the model configuration
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="you are a chatbot that provides mental health and emotional support to students.",
)

# Start the chat session
chat_session = model.start_chat(history=[])

# Interactive loop to keep chatting with the user
print("Welcome to the chatbot! Type 'exit' to end the conversation.")

while True:
    # Get input from the user
    user_input = input("You: ")

    # Break the loop if the user types 'exit'
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Take care.")
        break

    # Send the user's message to the chatbot
    response = chat_session.send_message(user_input)

    # Print the chatbot's response
    print(f"Chatbot: {response.text}")
