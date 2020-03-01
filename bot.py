# -*- coding: utf-8 -*-
from glob import glob
import logging
from random import choice

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)


def greet_user(bot, update):
	text = 'Вызван /start'
	logging.info(text)
	update.message.reply_text(text)


def talk_to_me(bot, update):
	user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
	print(update.message)
	logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
		         update.message.chat.id, update.me ssage.text)
	update.message.reply_text(user_text)


def send_cat_picture(bot, update):
	cat_list = glob('img/cat*.jpg')
	cat_pic = choice('cat_list')
	bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))


def main():
	mybot = Updater(settings.API_KEY)

	logging.info('Бот запущен')

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(CommandHandler('cat', send_cat_picture))	

	dp.add_handler(MessageHandler(Filters.text, talk_to_me))


	mybot.start_polling()
	mybot.idle()


main()	

