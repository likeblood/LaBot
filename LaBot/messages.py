from telegram.ext.dispatcher import run_async

import text_for_LaBot
import pars_check # used for check_format


@run_async
def unknown(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.uknown_text)


@run_async
def save(bot, update):
	file_id = update.message.document.file_id
	file = bot.get_file(file_id)
	try:
		name = update.message.document.file_name
		if not(pars_check.check_format(name)):
			raise ValueError("")
		
		# parse number and allocate in the necessary directory
		lab_number = int(name[name.rfind('_') + 1 : name.rfind('.')])
		if lab_number == 7:
			new_path = '/Users/ba/Documents/LabsBot/labs/lab_7/' + update.message.document.file_name
		elif lab_number == 8:
			new_path = '/Users/ba/Documents/LabsBot/labs/lab_8/' + update.message.document.file_name			
		elif lab_number == 9:
			new_path = '/Users/ba/Documents/LabsBot/labs/lab_9/' + update.message.document.file_name			
		elif lab_number == 10:
			new_path = '/Users/ba/Documents/LabsBot/labs/lab_10/' + update.message.document.file_name			
		elif lab_number == 11:
			new_path = '/Users/ba/Documents/LabsBot/labs/lab_11/' + update.message.document.file_name			
		elif lab_number == 12:
			new_path = '/Users/ba/Documents/LabsBot/labs/lab_12/' + update.message.document.file_name
		else:
			bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.unsaved_text, parse_mode='Markdown')
		file.download(new_path)
		bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.save_text)

	except:
		bot.send_message(chat_id=update.message.chat_id, text=text_for_LaBot.unsaved_text, parse_mode='Markdown')
