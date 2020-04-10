from telegram.ext import Filters


LaBot_files = (	 Filters.document &
				~Filters.document.category("audio") & 
				~Filters.document.category("video"))

unknown_files = (Filters.text & 
				~Filters.command &
				~LaBot_files)
	