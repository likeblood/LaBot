import logging
from telegram.ext.dispatcher import run_async

import text_for_LaBot
import pars_check  # used for check_format

# logs for LaBot
# Enable logging to handle uncaught exceptions
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='LaBot.log')
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

@run_async
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.uknown_text)


@run_async
def save(bot, update):
<<<<<<< HEAD
<<<<<<< HEAD
	file_id = update.message.document.file_id
	file = bot.get_file(file_id)
	try:
		name = update.message.document.file_name
		if not(pars_check.check_format(name)):
			raise ValueError("")
		
		# parse number and allocate in the necessary directory
		lab_number = int(name[name.rfind('_') + 1 : name.rfind('.')])
		if lab_number == 7:
			new_path = '~/LaBot/labs/lab_7/' + update.message.document.file_name
		elif lab_number == 8:
			new_path = '~/LaBot/labs/lab_8/' + update.message.document.file_name			
		elif lab_number == 9:
			new_path = '~/LaBot/labs/lab_9/' + update.message.document.file_name			
		elif lab_number == 10:
			new_path = '~/LaBot/labs/lab_10/' + update.message.document.file_name			
		elif lab_number == 11:
			new_path = '~/LaBot/labs/lab_11/' + update.message.document.file_name			
		elif lab_number == 12:
			new_path = '~/LaBot/labs/lab_12/' + update.message.document.file_name
		else:
			bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.unsaved_text, parse_mode='Markdown')
		file.download(new_path)
		bot.send_message(chat_id=update.message.chat_id, text='Файл ' + '<*' + name + '*>' + text_for_LaBot.save_text, parse_mode='Markdown')

	except:
		bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.unsaved_text, parse_mode='Markdown')
=======
=======
>>>>>>> f61f08e1f0f6bf4ae1c9a5db0a3cba078774ace8
    file_id = update.message.document.file_id
    file = bot.get_file(file_id)
    try:
        name = update.message.document.file_name
        logger.info(f"Recieved file {name} from chat {update.message.chat_id}")
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
        bot.send_message(chat_id=update.message.chat_id, text='Файл ' + '<*' + name + '*>' + text_for_LaBot.save_text,
                         parse_mode='Markdown')

    except Exception:
        bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.sth_wrong, parse_mode='Markdown')
        logger.error('Something wrong', exc_info=True)
<<<<<<< HEAD
>>>>>>> f61f08e1f0f6bf4ae1c9a5db0a3cba078774ace8
=======
>>>>>>> f61f08e1f0f6bf4ae1c9a5db0a3cba078774ace8
