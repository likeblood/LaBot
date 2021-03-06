import logging

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters

import commands
import messages
import customFilters

from settings import TOKEN


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

# logs for LaBot
# Enable logging to handle uncaught exceptions

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='LaBot.log')

logger = logging.getLogger(__name__)

def main():
	logger.info("Initializing bot")
	updater = Updater(token=TOKEN)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('start', 			commands.start), 1)
	dp.add_handler(CommandHandler('help', 			commands.help ), 1)
	dp.add_handler(CommandHandler('showdeadlines',  commands.show_deadlines), 1)

	dp.add_handler(MessageHandler(customFilters.unknown_files, 	messages.unknown))
	dp.add_handler(MessageHandler(  customFilters.LaBot_files, 	messages.save))

	dp.add_error_handler(error)

	print("\nrunning...\n")
	logger.info("The bot is enabled")

	updater.start_polling()
	updater.idle()
	logger.info("The bot is disabled")


if __name__ == '__main__':
	main()
