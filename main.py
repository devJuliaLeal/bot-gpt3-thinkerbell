import telebot
import openai
from imports import (cute, joke, API_TOKEN, BOT_TOKEN, portugues)
openai.api_key = API_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def handle_chat(message):
    question = message.text[6:]
    response = openai.Completion.create(engine="text-davinci-003", prompt=question + cute, temperature=0.9,
                                        max_tokens=1999)
    answer = response['choices'][0]['text']
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['N'])
def handle_chat(message):
    question = message.text[6:]
    response = openai.Completion.create(engine="text-davinci-003", prompt=question , temperature=0.9,
                                        max_tokens=1999)
    answer = response ['choices'][0]['text']
    bot.send_message(message.cha.id, answer)


@bot.message_handler(commands=['J'])
def handle_chat(message):
    question = message.text[6:]
    response = openai.Completion.create(engine="text-davinci-003", prompt=question + joke, temperature=0.9,
                                        max_tokens=1999)
    answer = response['choices'][0]['text']
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['BR'])
def text_handler(message):
    question = message.text[6:]
    response = openai.Completion.create(engine="text-curie-001", prompt=question + portugues, temperature=0.85,
                                        max_tokens=1024)
    answer = response['choices'][0]['text']
    bot.send_message(message.chat.id, answer)


bot.polling()