import logging

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters

import commands
import messages

from settings import TOKEN


def error(bot, update):
    logger.warning('Update "%s" caused error "%s"', update, bot.error)

# logs for LaBot
# Enable logging to handle uncaught exceptions
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='LaBot.log')
logger = logging.getLogger(__name__)


def main():
	updater = Updater(token=TOKEN)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('start', 			commands.start), 1)
	dp.add_handler(CommandHandler('help', 			commands.help ), 1)
	dp.add_handler(CommandHandler('showdeadlines', commands.show_deadlines), 1)

	dp.add_handler(MessageHandler(Filters.text & ~Filters.command, messages.unknown))
	dp.add_handler(MessageHandler(Filters.document.mime_type("application/pdf"), messages.save))

	dp.add_error_handler(error)

	print("\nrunning...\n")

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
