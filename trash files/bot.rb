import telegram from telegram 
import ReplyKeyboardMarkup

bot = telegram.Bot('<token>')

menu_keyboard = [['MenuItem1'], ['MenuItem2']]
menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)

bot.send_message(chat_id=<chat_id>, text='Some text here', reply_markup=menu_markup)