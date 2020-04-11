import logging

from telegram.ext.dispatcher import run_async
import text_for_LaBot

logger = logging.getLogger(__name__)

@run_async
def start(bot, update):
    logger.info(f"Chat {update.message.chat_id} used command /start")
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_for_LaBot.start_text)


@run_async
def help(bot, update):
    logger.info(f"Chat {update.message.chat_id} used command /help")
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_for_LaBot.help_text,
                     parse_mode='Markdown')


@run_async
def show_deadlines(bot, update):
    logger.info(f"Chat {update.message.chat_id} used command /showdeadlines")
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_for_LaBot.deadlines_text,
                     parse_mode='Markdown')
