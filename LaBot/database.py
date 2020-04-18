#
#	NOW there is no need to use database
#

import logging
import dropbox

# Enable logging to handle uncaught exceptions
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='LaBot.log')
logger = logging.getLogger(__name__)


class User:
    _first_name = ""
    _last_name = ""
    _username = ""
    _chat_id = 0

    def __init__(self, first_name, last_name, username, chat_id):
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._chat_id = chat_id
        self._full_name = ""
        if(self._first_name is not None):
            self._full_name += self._first_name

        if self._last_name is not None:
            if len(self._full_name) > 0:
                self._full_name += " "
            self._full_name += self._last_name

        if self._username is not None:
            if len(self._full_name) > 0:
                self._full_name += f"(@{self._username})"
            else:
                self._full_name += f"@{self._username}"

        if len(self._full_name) == 0:
            self._full_name += f"{self._chat_id}"

    @property
    def full_name(self):
        return self._full_name

    @staticmethod
    def from_chatid(bot, chat_id):
        user = {}
        chat = bot.get_chat(chat_id)
        user["first_name"] = chat.first_name
        user["last_name"] = chat.last_name
        user["username"] = chat.username
        user["chat_id"] = chat_id
        return User(**user)


# https://stackoverflow.com/questions/23894221/upload-file-to-my-dropbox-from-python-script
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        try:
            logger.info(f"Loading {file_from} on Dropbox")
            with open(file_from, 'rb') as f:
                dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
            return True
        except Exception:
            logger.error('Something wrong with Dropbox', exc_info=True)
            return False
