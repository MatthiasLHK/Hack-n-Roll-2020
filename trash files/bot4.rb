require 'telegram/bot'

token = '1003609645:AAHQ9HPHbwGGVQvJ19xD7cs3USVZWsBgq0E'

Telegram::Bot::Client.run(token) do |bot|
bot.listen do |message|
  case message
  when Telegram::Bot::Types::CallbackQuery
    # Here you can handle your callbacks from inline buttons
    if message.data == 'touch'
      bot.api.send_message(chat_id: message.from.id, text: "/pl")
    end
  when Telegram::Bot::Types::Message
    kb = [
      Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Go to Google', url: 'https://google.com'),
      Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Touch me', callback_data: 'touch'),
      Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Switch to inline', switch_inline_query: 'some text')
    ]
    markup = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: kb)
    bot.api.send_message(chat_id: message.chat.id, text: 'Make a choice', reply_markup: markup)
  end
end
end

