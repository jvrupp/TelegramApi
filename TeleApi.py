import telebot
import requests
import time


KEY_API = "6206804529:AAEryDMxTu_y377rPGYvxR36wQz8pdqK8v4"

bot = telebot.TeleBot(KEY_API)

def get_values():
    resp=requests.get("http://127.0.0.1:8000/output/")


    return resp.json()


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    print(chat_id)    
    while True:
        message = get_values()['response']
        time.sleep(1)
        bot.send_message(chat_id, f'Olá, bem-vindo ao meu bot! {message}')

bot.polling()


