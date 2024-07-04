import os
import google.generativeai as genai
import pathlib
import logging
from logging.handlers import RotatingFileHandler

def main():
    GOOGLE_API_KEY = os.getenv('Gemini_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    print("Gemini CLI Chatbot")
    print("Type 'exit' to end the conversation.")

    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[])

    # Configure logging
    log_path = pathlib.Path("history.log")
    logger = logging.getLogger("GeminiChat")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        log_path, maxBytes=1024 * 1024, backupCount=5  # 1 MB per file, keep 5 backups
    )
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = chat.send_message(user_input)

        # Log the conversation
        logger.info(f"You: {user_input}")
        logger.info(f"Bot: {response.text}")

        print("Bot:", response.text)

if __name__ == "__main__":
    main()
