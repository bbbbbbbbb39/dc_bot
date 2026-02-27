import os
import telebot
import re

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(TOKEN)

# Заборонені слова (буде ловити і великі і малі)
FORBIDDEN_PATTERNS = [
    r"\bреб_перу\b",
    r"\bреб\b"
]

@bot.message_handler(func=lambda message: True)
def filter_and_forward(message):
    if message.text:
        text = message.text.lower()

        for pattern in FORBIDDEN_PATTERNS:
            if re.search(pattern, text):
                print("Заборонене слово знайдено")
                return

        bot.forward_message(CHANNEL_ID, message.chat.id, message.message_id)

bot.infinity_polling()
