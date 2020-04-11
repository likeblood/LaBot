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
                dbx.files_upload(f.read(), file_to)
            return True
        except Exception:
            logger.error('Something wrong with Dropbox', exc_info=True)
            return False
