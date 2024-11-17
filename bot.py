VERSION = '0.0.1'

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
import telebot
import time

import config
# from modules.scripts import *
# from modules.commands import *

bot = telebot.TeleBot(config.API)  # создание бота


def keyboard_login():
    btn_sign = InlineKeyboardButton("Войти", callback_data='sign')
    btn_login = InlineKeyboardButton("Зарегестрироваться", callback_data='login')
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(btn_login, btn_sign)
    return keyboard


# КОМАНДЫ
@bot.message_handler(commands=['start'])  # обработка команды start
def start(message):
    user_id = message.chat.id
    text = "Добро пожаловать\!"
    keyboard = keyboard_login()
    bot.send_message(user_id, text, reply_markup=keyboard, parse_mode="MarkdownV2")


# ОБРАБОТКА ВЫЗОВОВ
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):  # работа с вызовами inline кнопок
    pass


# @bot.message_handler(func=lambda message: True)
# def handle_text_message(message): # удаляет сообщения от пользователя
#     bot.delete_message(message.chat.id, message.message_id)
        

print(f"бот запущен...")
def start_polling():
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)  # Установите таймаут для перезапуска
        except Exception as e:
            print(f"Ошибка при подключении: {e}")
            time.sleep(1)  # Пауза перед повторным подключением

if __name__ == "__main__":
    start_polling()