import os
import requests
import telebot
import keep_alive
from dotenv import load_dotenv



BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
url = os.getenv("URL")
key1 = os.getenv("TELEGRAM_KEY")
key2 = os.getenv("MAILGUN_KEY")
bot = telebot.TeleBot(key1)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to h1n0's telegram group, I will forward any messages you type here, try and send one long message as opposed to lots of one liners")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    content = message.text
    userjson = message.from_user
    from1 = userjson.username
    requests.post(
    url,
    auth=("api", key2),
    data={"from": "Telegram Bot <telegrambot@<MAILGUN_DOMAIN>>",
          "to": ["reciever@gmail.com"],
          "subject": "Telegram msg from " + from1,
          "text": content})
    bot.reply_to(message, "Email Sent!!")

keep_alive.keep_alive()
bot.polling()
