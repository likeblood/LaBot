import logging
from settings import INFO_CHANNEL, DROPBOX_TOKEN
from telegram.ext.dispatcher import run_async
from database import TransferData, User

import text_for_LaBot
import pars_check  # used for check_format


# logs for LaBot
# Enable logging to handle uncaught exceptions
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO,
#                     filename='LaBot.log')

logger = logging.getLogger(__name__)
dropb = TransferData(DROPBOX_TOKEN)

@run_async
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.uknown_text)


@run_async
def save(bot, update):
    file_id = update.message.document.file_id
    file = bot.get_file(file_id)
    try:
        name = update.message.document.file_name
        user = User.from_chatid(bot, update.message.chat_id)
        logger.info(f"Recieved file {name} from {user.full_name}")
        if not (pars_check.check_format(name)):
            bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.unsaved_text, parse_mode='Markdown')
            return None

        # parse number and allocate in the necessary directory
        lab_number = int(name[name.rfind('_') + 1: name.rfind('.')])


        if lab_number == 7:
            new_path = 'labs/lab_7/' + update.message.document.file_name
        elif lab_number == 8:
            new_path = 'labs/lab_8/' + update.message.document.file_name
        elif lab_number == 9:
            new_path = 'labs/lab_9/' + update.message.document.file_name
        elif lab_number == 10:
            new_path = 'labs/lab_10/' + update.message.document.file_name
        elif lab_number == 11:
            new_path = 'labs/lab_11/' + update.message.document.file_name
        elif lab_number == 12:
            new_path = 'labs/lab_12/' + update.message.document.file_name
        else:
            bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.unsaved_text, parse_mode='Markdown')
        file.download(new_path)
        if not dropb.upload_file(new_path, "/" + new_path):
            bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.sth_wrong, parse_mode='Markdown')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Файл ' + '<*' + name + '*>' + text_for_LaBot.save_text,
                             parse_mode='Markdown')

        bot.send_message(chat_id=INFO_CHANNEL,
                         text=(f"Пользователь {user.full_name} загрузил файл { name }"))

    except Exception:
        bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.sth_wrong, parse_mode='Markdown')
        logger.error('Something wrong', exc_info=True)
