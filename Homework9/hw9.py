import random
import telebot
from telebot import types



# #token = "5663035159:AAG7NbFtjo9FAyCramt5lLrj6i_SQAA50UI"
# # t.me/gb_homework9_bot
# bot = telebot.TeleBot(token, parse_mode=None)
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Привет ✌️ " + message.from_user.first_name)
#     button_message(message)
#
#
# @bot.message_handler(commands=['button'])
# def button_message(message):
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     item1 = types.InlineKeyboardButton(text="Поиграем ?", callback_data='action1')
#     item2 = types.InlineKeyboardButton(text="Посчитаем ?", callback_data='action2')
#
#     keyboard.add(item1, item2)
#     bot.reply_to(message, 'Выберите чем займемся', reply_markup=keyboard)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if call.data == 'action1':
#         global count
#         count = 1
#         global number_bot
#         number_bot = random.randint(0, 1000)
#         bot.send_message(call.message.chat.id, 'Я загадал число от 1 до 1000, отгадай какое')
#         number_user = bot.send_message(call.message.chat.id, 'Введите число')
#         bot.register_next_step_handler(number_user, game)
#
#     elif call.data == 'action2':
#         expression = bot.send_message(call.message.chat.id, 'Введите выражение')
#         bot.register_next_step_handler(expression, calk)
#
#
# def game(message):
#     user_bot = message.text
#     global number_bot
#     global count
#     if not user_bot.isdigit():
#         bot.reply_to(message, 'Вы ввели не цифры, введите пожалуйста цифры')
#         bot.register_next_step_handler(message, game)
#     else:
#         user_bot = int(user_bot)
#         if user_bot < number_bot:
#             count += 1
#             bot.reply_to(message, 'Больше')
#             bot.register_next_step_handler(message, game)
#         elif user_bot > number_bot:
#             count += 1
#             bot.reply_to(message, 'Меньше')
#             bot.register_next_step_handler(message, game)
#         else:
#             bot.reply_to(message, f'Вы угадали с {count} раз')
#             button_message(message)
#
#
# def calk(message):
#     expres = message.text
#     try:
#         eval(expres)
#     except:
#         bot.reply_to(message, 'Вы ввели не математическое выражение')
#         button_message(message)
#     else:
#         bot.reply_to(message, f'Результат выражения {expres} = {eval(expres)} ')
#         button_message(message)
#
# bot.infinity_polling()