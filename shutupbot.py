from bot import telegram_chatbot
import gtrans

from telegram.ext import Updater
updater = Updater(token='1064559294:AAEA2YdE86Max_VqL6UEVnPIEr6OUQuIAqE' , use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

bot = telegram_chatbot("config.cfg")


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please enter /chatme!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def chatme(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Shut up")

chatme_handler = CommandHandler('chatme', chatme)
dispatcher.add_handler(chatme_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling()