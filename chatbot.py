def get_ai_response(messages):
    user_message = messages[-1]["content"]
    return f"🤖 (Mock AI) You asked: '{user_message}'. AI is disabled because API quota is exceeded."