# Gemini_Chatbot

This project implements a chatbot using the Gemini-1.5-flash model, integrated with Google AI Studio and deployed using Flask.

## Project Structure 📂

- **frontend/**
  - **templates/**
    - `index.html`: HTML file for the chatbot UI.
  - **static/**
    - `style.css`: CSS file for styling the chatbot UI.
    - `script.js`: JavaScript file for handling frontend interactions.

- **backend/**
  - `app.py`: Flask application for serving the chatbot UI and backend logic.

- **AI service/**
  - `gemini_response.py`: Python script handling AI logic, utilizing the Gemini API.

## Setup 🛠️

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Gemini-chatbot.git
   cd Gemini-chatbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate #On windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration 🔑

1. Obtain an API key from Google Cloud and save it in a `.env` file:
   ```
   GOOGLE_API_KEY="your_api_key"
   ```

2. Ensure the API key is securely stored and not exposed in version control.

### Running the Application ▶️

1. Start the Flask backend:
   ```bash
   python backend/app.py
   ```

2. Access the chatbot UI in your browser:
   ```
   http://localhost:5000
   ```

## Usage 🚀

- Open the chatbot UI and interact with it. Messages are processed by the backend, which communicates with the Gemini AI service.

## License 📜

This project is licensed under the MIT License





https://github.com/user-attachments/assets/f4e05c94-796e-4e46-8467-cd8e3f67214d



