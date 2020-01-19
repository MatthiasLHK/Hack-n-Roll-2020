from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
updater = Updater(token='923574552:AAGDJY1M7KvGu-sz_Ths5qj1Z5kfQsjELCQ', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



def start(update, context):
    reply_keyboard = [['Boy', '/start', 'Other']]

    update.message.reply_text(
        'Hi! My name is Professor Bot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'Are you a boy or a girl?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER


# def start(bot, update):
#     kb = [[telegram.KeyboardButton('/command1')],
#           [telegram.KeyboardButton('/command2')]]
#     kb_markup = telegram.ReplyKeyboardMarkup(kb)
#     bot.send_message(chat_id=update.message.chat_id,
#                      text="your message",
#                      reply_markup=kb_markup)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()