#!/usr/bin/python3
# -*- coding: utf-8 -*-
import glob
import os
import telebot
import urllib
import json
import logging

from subprocess import call

# log settings
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('someTestBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

TOKEN = "1459207785:AAEGNH4SiP3Xy9IocrZ1LOo3w5IZ48FlGGM"


bot = telebot.TeleBot(TOKEN)

# help text
help_string = []
help_string.append("Escolha uma opção:\n\n")
help_string.append("/start - Diga olá;\n")
help_string.append("/help - Mostra ajuda;\n")
help_string.append("/server - Status do servidor;\n")
help_string.append("/cups - Status do cups.")


@bot.message_handler(commands=['start'])
def send_start(message):
    # send a simple message
    bot.send_message(message.chat.id, "Olá " + message.from_user.first_name + ", eu sou o ABDI_BOT, em que posso ajudar? digite /help para ajuda.")

@bot.message_handler(commands=['help'])
def send_help(message):
    # send a message with Markdown
     
    bot.send_message(message.chat.id, "".join(help_string), parse_mode="Markdown")
    message = message.text
    print(message)

@bot.message_handler(commands=['server'])
def send_server(message):
    try:
        lsdir = os.listdir("/home")
        # path to script that gathers server info
        call(["/home/danilo/Documents/ProjetosPython/status.sh"])
        # read the file with results
        status = open("/home/danilo/Documents/ProjetosPython/status.txt", "rb").read()
        bot.send_message(message.chat.id, status, parse_mode="Markdown")
        bot.send_message(message.chat.id, lsdir, parse_mode="Markdown")
    except Exception as e:
        logger.exception(str(e))
        bot.send_message(message.chat.id, "Error while getting a server status. Check the log for details.")

#print(bot.get_me())


@bot.message_handler(commands=['cups'])
def send_welcome(message):
    statuscups = os.system("systemctl status atd")
    if statuscups == 0:
        bot.reply_to(message," Status do cups OK!! ", parse_mode="Markdown") 

"""

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


print(bot.get_me())
#lastChatId = message[-1].chat.id
#print(lastChatID)

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start'])
def send_welcome(message):
    ls = os.listdir('/tmp')
    bot.send_message(message.chat.id, "Olá " + message.from_user.first_name + " ,seja bem vindo, em que posso ajudar? Digite /ajuda para mais opções!! ")

    
    #print(ls)


@bot.message_handler(commands=['ajuda'])
def handle_ajuda(message):
    bot.send_message(message.chat.id, message.from_user.first_name + ":\nComandos disponíveis: \n"
                                                                     "df \n"
                                                                     "ls \n" )

    message = message.text
    print(message)

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

"""
bot.polling()
