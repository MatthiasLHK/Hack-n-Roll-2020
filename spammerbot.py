from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token='993591730:AAEWkQn61FSgGaucfRmNf-cWbUBocReIkUo', use_context=True)

dispatcher = updater.dispatcher

def spam(update, context):
    for x in range(20):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oi !! Reply faster please !!")



spam_handler = CommandHandler('spam', spam)
dispatcher.add_handler(spam_handler)

updater.start_polling()
updater.idle()