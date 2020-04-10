import logging

from telegram.ext.dispatcher import run_async
import text_for_LaBot


@run_async
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_for_LaBot.start_text)


@run_async
def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_for_LaBot.help_text)


@run_async
def show_deadlines(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=text_for_LaBot.deadlines_text,
                     parse_mode='Markdown')
