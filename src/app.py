import telebot
import requests
import sys

file_obj = open("../.secrets","r")

token = sys.argv[1]
print(token)

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    r = requests.post(url = "http://localhost:5000/api/v1/emojify", data = message.text.encode('utf-8')) 
    if r.status_code == 200:
        bot.send_message(message.from_user.id, r.text.encode('utf-8'))
    else:
        return bot.send_message(message.from_user.id, "error".encode('utf-8'))

bot.polling(none_stop=True, interval=0)


