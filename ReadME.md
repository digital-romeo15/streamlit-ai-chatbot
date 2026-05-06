# Streamlit AI Chatbot with User Login

A beginner‑friendly Python web application built with Streamlit that demonstrates user authentication and a chat‑style interface designed for AI integration.

1) Designed as a learning and portfolio project
2) Easy to extend with real AI, databases, or deployment
3) Clean file structure and modular code

# Features

🔐 User Login System

Simple username/password authentication
Session‑based login and logout


💬 Chatbot Interface

ChatGPT‑style UI using Streamlit’s chat components
Message history preserved during the session


🧠 AI‑Ready Architecture

AI logic separated into its own module
Easily switch between mock responses and a real OpenAI backend


🧩 Beginner‑Friendly Structure

Clear separation of concerns
Easy to understand and extend



# Getting Started
1️) Clone the Repository
    git clone https://github.com/your-username/streamlit-chatbot.git
    cd Streamlit-chatbot

 2) # Install Dependencies

    pip install -r requirements.txt

 3) # (Optional) Configure OpenAI API
    If you want to use a real AI backend:
    Create a .env file in the project root:

    OPENAI_API_KEY=your_api_key_here


 4) # Run the Application
 
    streamlit run app.py

 5) # Default Login Credentials

    Username: admin
    Password: password123  (changeable in the auth.py) 

# Technologies Used

Python
Streamlit
python‑dotenv
(Optional) OpenAI API 


# Future Improvements

1) Password hashing and secure authentication
2) User database with SQLite
3) Persistent chat history per user
4) Improved UI / theme
5) Deployment (Streamlit Cloud, Render, etc.)


 # Learning Outcomes
This project helped me learn:

How to build UI‑driven Python applications
Session management in Streamlit
Modular code organization
Working with environment variables
Debugging real API and runtime issues


#  Author
Built as a learning and portfolio project by Romeo Fember.

