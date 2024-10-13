import telebot
from config import token
from random import choice

API_TOKEN = '7702403200:AAHA7_1HpF3Et0akp_q3g_RumYTHSUmX2pU'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)


@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)


@bot.message_handler(commands=['fact'])
def coin_handler(message):
    fact = choice(["У среднестатистического человека меньше 2 рук", "У среднестатистического человека меньше 2 ног"])
    bot.reply_to(message, fact)


@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message: #проверка на то, что эта команда была вызвана в ответ на сообщение 
        chat_id = message.chat.id # сохранение id чата
         # сохранение id и статуса пользователя, отправившего сообщение
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
         # проверка пользователя
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # пользователь с user_id будет забанен в чате с chat_id
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")


@bot.message_handler(commands=['go'])
def go_pokemon(message):
    pokemon = 'Let`s go play!'
    bot.send_message(message, pokemon)


bot.infinity_polling()