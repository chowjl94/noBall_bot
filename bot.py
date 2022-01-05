import os
from dotenv import load_dotenv, find_dotenv
import requests
import telebot
import logging

load_dotenv(find_dotenv())

API_KEY = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
BASE = os.getenv('URI_BASE')


bot = telebot.TeleBot(API_KEY)

  

@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id, 'CHECKING ....')
    #photo = open('cricketball.jpg','rb')
    video = open('noball.MOV','rb')
    #bot.send_photo(CHAT_ID,photo)
    bot.send_video(CHAT_ID,video)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.send_message(message.chat.id, 'Welcome to No ball Detector')

print('bot is up')
bot.infinity_polling()
