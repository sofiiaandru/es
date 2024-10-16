
import telebot
import random
from telebot import types


token = "7272556876:AAGsAAYAWqIbeKH6v5mtMJwA6IrqTp8kILE"
bot = telebot.TeleBot(token)

emojis = {
    "yes_no": ["🔮", "🎱", "✨"],
    "percentage": ["📊", "📈", "🧮"],
    "responses": ["😄", "🤔", "😳"]
}


# Обробка команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔮 Так/Ні")
    btn2 = types.KeyboardButton("📊 Відсотки")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Привіт!  Обери спосіб передбачення:", reply_markup=markup)

# Обробка текстових повідомлень
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "🔮 Так/Ні":
        bot.send_message(message.chat.id, f"{random.choice(emojis['yes_no'])} Напиши своє питання, і я дам відповідь 'Так' або 'Ні'")
        bot.register_next_step_handler(message, yes_no_prediction)
    elif message.text == "📊 Відсотки":
        bot.send_message(message.chat.id, f"{random.choice(emojis['percentage'])} Напиши своє питання")
        bot.register_next_step_handler(message, percentage_prediction)
    else:
        bot.send_message(message.chat.id, "Будь ласка, обери спосіб передбачення з меню.")

# Функція для передбачення "Так/Ні"
def yes_no_prediction(message):
    responses = ["Так", "Ні", "Мабуть"]
    response = random.choice(responses)
    emoji = random.choice(emojis['responses'])
    bot.send_message(message.chat.id, f"{emoji} Відповідь: {response}")


# Функція для передбачення "Відсотки"
def percentage_prediction(message):
    percent = random.randint(1, 101)
    emoji = random.choice(emojis['percentage'])
    bot.send_message(message.chat.id, f"{emoji} Шанс: {percent}%")
    


# Запуск бота
bot.polling(none_stop=True)