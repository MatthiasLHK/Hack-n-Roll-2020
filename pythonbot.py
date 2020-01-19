from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
query = None

# Stages
FIRST, SECOND = range(2)
# Callback data
ONE, TWO, THREE, FOUR = range(4)

temp = None

def start(update, context):
  user = update.message.from_user
  logger.info("User %s started the conversation.", user.first_name)

  keyboard = [[InlineKeyboardButton("Spammer", callback_data=str(ONE)),
                 InlineKeyboardButton("ShutupBot", callback_data=str(TWO))],
                [InlineKeyboardButton("Find A Friend", callback_data=str(THREE))],
                [InlineKeyboardButton("Exit", callback_data=str(FOUR))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  update.message.reply_text('Please choose which bot to run:', reply_markup=reply_markup)
  
  return FIRST


def start_again(update, context):
    
    query = update.callback_query
    
    bot = context.bot
    keyboard = [[InlineKeyboardButton("Spammer", callback_data=str(ONE)),
                 InlineKeyboardButton("EncikBot", callback_data=str(TWO))],
                [InlineKeyboardButton("Find A Friend", callback_data=str(THREE))],
                [InlineKeyboardButton("Exit", callback_data=str(FOUR))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Start handler, Choose a route",
        reply_markup=reply_markup
    )
    return FIRST


def level2(update, context):
  global query
  query = update.callback_query
  bot = context.bot
  keyboard = [[InlineKeyboardButton("Run", callback_data=str(ONE)),
              InlineKeyboardButton("Back", callback_data=str(TWO))]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  
  bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Start now?",
        reply_markup=reply_markup
    )
  
  return SECOND   
           
def run(update, context):    # the global synthax helps to refer to the global variable and not the block scope.
   global query
   print(query.data)
   if query.data == '0':
      context.bot.send_message(chat_id=update.effective_chat.id, text="Please click @XspammerbotX")
   elif query.data == '1':
      context.bot.send_message(chat_id=update.effective_chat.id, text="Please click @heckcarenrollbot")
   elif query.data == '2':
      context.bot.send_message(chat_id=update.effective_chat.id, text="Please click @a_a_friendBot")



def end(update, context):
   query = update.callback_query
   bot = context.bot
   bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="See you next time!"
    )
    


def button1(update, context):
  query = update.callback_query
  query.edit_message_text(text="Selected option: {}".format(query.data))

def help(update, context):
  update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    
    logger.warning('Update "%s" caused error "%s"', update, context.error)



def main():
  updater = Updater("762231694:AAEgcRk_D5HoiI0a1XZmc-FQqVb35wVo3CI", use_context=True)
  dp = updater.dispatcher


  conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [CallbackQueryHandler(level2, pattern='^' + str(ONE) + '$'),
                    CallbackQueryHandler(level2, pattern='^' + str(TWO) + '$'),
                    CallbackQueryHandler(level2, pattern='^' + str(THREE) + '$'),
                    CallbackQueryHandler(end, pattern='^' + str(FOUR) + '$')],
            SECOND: [CallbackQueryHandler(run, pattern='^' + str(ONE) + '$'),
                     CallbackQueryHandler(start_again, pattern='^' + str(TWO) + '$')]
        },
        fallbacks=[CommandHandler('start', start)]
    )



  dp.add_handler(conv_handler)
  
  dp.add_error_handler(error)

  updater.start_polling()

  updater.idle()

if __name__ == '__main__':
  main()