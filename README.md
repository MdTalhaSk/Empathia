# Empathia

## Project Overview

**Empathia** is a mental health and emotional support chatbot designed to provide assistance to students. Using Google's Generative AI model, it offers supportive and thoughtful conversations aimed at improving mental well-being. The chatbot can be accessed both through a web interface and directly from the terminal.

## Features

- AI-powered chatbot for mental health and emotional support
- Web-based interface built with Flask
- Interactive command-line version for terminal usage
- Customizable AI response settings (temperature, tokens, etc.)

## Technologies Used

- **Google Generative AI**: Utilizes Google's powerful language model for natural language processing and generation.
- **Flask**: A lightweight web framework for Python to provide a web-based interface.
- **HTML/JavaScript**: For building the chat interface in the web version.
- **dotenv**: For securely managing the API key using environment variables.

## Installation

To set up and run the project locally, follow the steps below:

### Prerequisites

- Python 3.7 or higher
- Google Generative AI API Key
- Pip (Python package installer)

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/empathia.git
cd empathia
```
### Step 2: Set Up Environment Variables
Create a .env file in the root directory of the project and add your Google API key as follows:
```env
GOOGLE_API_KEY=your_google_api_key_here
```
## Step 3: Install Dependencies
Install the required Python libraries using the following command:
```
bash
pip install -r requirements.txt
```
Ensure your requirements.txt contains the following dependencies:
```
Flask
google-generativeai
python-dotenv
```
## Step 4: Running the Web App
To run the web-based chatbot interface, use the following command:
```
bash
python app.py
```
This will start a local server. You can access the chatbot in your browser at ```http://127.0.0.1:5000/.```
## Step 5: Running the Terminal Chatbot
If you want to run the chatbot in the terminal, use this command:
```
bash
python chatbot.py
```
This will open an interactive chat in your terminal. Type ```exit``` to end the session.
Usage
## Web Interface
Navigate to ```http://127.0.0.1:5000/``` in your web browser.
Enter a message in the input field and click ```Send```.
The chatbot will respond with emotional support based on your input
