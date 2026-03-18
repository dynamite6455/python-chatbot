import requests
import time

def slow(text, speed=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()

def get_ai_response(user_input):
    url = "https://chatgpt.com"
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful and creative AI model."},
            {"role": "user", "content": user_input}
        ],
        "model": "openai", # Uses a free-tier compatible model
        "jsonMode": False
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Connection error: {e}"

slow("---Aryplayz1213's AI Chatbot Started (Type 'quit', 'exit', or 'bye' to stop) ---")

while True:
    user_message = input("You: ")
    
    if user_message.lower() in ["quit", "exit", "bye", "Quit", "Exit", "Bye"]:
        slow("Bot: Finally, peace!")
        break
        
    ai_text = get_ai_response(user_message)
    slow(f"Bot: {ai_text}")