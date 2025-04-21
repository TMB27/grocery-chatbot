# telegram_bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
from chatbot import get_response  # This is where get_response is imported from

load_dotenv()

# Replace this with your Telegram Bot API Token
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")

async def handle_message(update: Update, context):
    user_text = update.message.text  # User's message
    reply = get_response(user_text)  # Get chatbot response
    await update.message.reply_text(reply)  # Send the response to the user

def main():
    # Ensure the TELEGRAM_API_KEY is loaded
    if not TELEGRAM_API_KEY:
        raise ValueError("TELEGRAM_API_KEY is not set in the environment variables.")

    # Set up the bot
    application = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    # Add handler for text messages
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(text_handler)

    # Run the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
