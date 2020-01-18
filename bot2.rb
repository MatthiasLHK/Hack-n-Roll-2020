require 'telegram/bot'

token = '1003609645:AAHQ9HPHbwGGVQvJ19xD7cs3USVZWsBgq0E'

Telegram::Bot::Client.run(token) do |bot|
 bot.listen do |message|
  case message.text
  when '/start'
    bot.api.send_message(chat_id: message.chat.id, text: "Hello, #{message.from.first_name}")
     # helper = Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Play', callback_data: 'play')
     # helper2 = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: helper)
     # bot.api.send_message(chat_id: message.chat.id, text: "Hello, #{message.from.first_name}",reply_markup: helper2)
    
  when Telegram::Bot::Types::CallbackQuery
    # Here you can handle your callbacks from inline buttons
    if message.data == 'touch'
      bot.api.send_message(chat_id: message.from.id, text: "Don't touch me!")
    end
    # if message.data == 'play'
    #   bot.api.send_message(chat_id: message.from.id, text: "play")
    # end

  when '/play'
    kb = [
      Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Go to Google', url: 'https://google.com'),
      Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Touch me', callback_data: 'touch'),
      Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Switch to inline', switch_inline_query: 'Function not added.')
    ]
    markup = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: kb)
    bot.api.send_message(chat_id: message.chat.id, text: 'Make a choice', reply_markup: markup)
  end
end
end





