import os
import telebot

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(TOKEN)

FORBIDDEN_WORDS = ["казино", "спам", "реклама"]

@bot.message_handler(func=lambda message: True)
def filter_and_forward(message):
    if message.text:
        text = message.text.lower()

        for word in FORBIDDEN_WORDS:
            if word in text:
                print("Заборонене слово знайдено")
                return

        bot.forward_message(CHANNEL_ID, message.chat.id, message.message_id)

bot.infinity_polling()
