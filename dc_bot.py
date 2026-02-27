import os
import telebot
import re

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

# Канали куди пересилати
CHANNELS = [
    -1003733535025,   # перший канал
    -1003837938772,   # другий канал (встав сюди ID)
]

# Загальний список заборонених слів
FORBIDDEN_PATTERNS = [
    r"\bреб_перу\b",
    r"\bреб\b",
    r"\blima\b",
    r"\bperu\b"
]

@bot.message_handler(func=lambda message: True)
def filter_and_forward(message):

    if not message.text:
        return

    text = message.text.lower()

    # Перевірка на заборонені слова
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, text):
            print("Повідомлення заблоковано фільтром")
            return

    # Якщо все чисто — пересилаємо в усі канали
    for channel_id in CHANNELS:
        bot.forward_message(channel_id, message.chat.id, message.message_id)

bot.infinity_polling()
