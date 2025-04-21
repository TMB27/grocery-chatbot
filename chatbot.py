# chatbot.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables (important for API keys)
load_dotenv()

# Use your OpenRouter API key here
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Define the model you want to use from OpenRouter
MODEL = "openrouter/deepseek-chat"  # you can replace with mixtral, gpt-3.5, etc.

def get_response(user_message):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourdomain.com",  # Replace with your project domain
        "X-Title": "Grocery Chatbot"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful grocery ordering assistant."},
         {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    # Debugging: Log the payload and headers
    print("Payload:", payload)
    print("Headers:", headers)

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for HTTP issues
        result = response.json()

        # Check if 'choices' key exists in the response
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        elif "error" in result:
            return f"Error from API: {result['error']['message']}"
        else:
            return "Sorry, I couldn't understand your request. Please try again."

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "Sorry, there was an issue connecting to the AI service."

    except Exception as e:
        print("Unexpected Error:", e)
        return "Sorry, something went wrong while generating a response."
