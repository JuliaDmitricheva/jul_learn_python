import logging 
# Импортируем нужные компоненты c  github
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import Jul_lesson1_bot_settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(asctime)s - %(message)s',
			level=logging.INFO,
			filename='Jul_lesson1_bot.log'
			)


def greet_user(bot, update):
	mytext = """Привет {}! 
	Я  простой учебный бот. Понимаю только /start
	""".format(update.message.chat.first_name)
	update.message.reply_text(mytext)
	print(update)


def chat(bot, update):
	user_text=update.message.text
	logging.info(user_text)
	update.message.reply_text(user_text)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
	updater = Updater(Jul_lesson1_bot_settings.TELEGRAM_API_KEY)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, chat))
	updater.start_polling()
	updater.idle()


# Вызываем функцию - эта строчка собственно запускает бота
if __name__ == '__main__':
	logging.info("Bot started")
	main()
