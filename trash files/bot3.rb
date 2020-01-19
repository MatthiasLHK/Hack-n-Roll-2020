require 'telegram/bot'

token = '1003609645:AAHQ9HPHbwGGVQvJ19xD7cs3USVZWsBgq0E'

Telegram::Bot::Client.run(token) do |bot|
  bot.listen do |message|
    case message.text
      when '/start'
        bot.api.send_message(chat_id: message.chat.id, text: "Hello, #{message.from.first_name}")
      when '/play'
        kb = [
          Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Go to Google', url: 'https://google.com'),
          Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Play', callback_data: 'start'),
          Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Switch to inline', switch_inline_query: 'Function not added.')
        ]
        markup = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: kb)
        bot.api.send_message(chat_id: message.chat.id, text: 'Make a choice', reply_markup: markup)
        
  bot.listen do |message|
    puts message
      case message
        when Telegram::Bot::Types::CallbackQuery
              # Here you can handle your callbacks from inline buttons
          if message.data == 'start'
                # bot.api.send_message(chat_id: message.from.id, text: "/start")
                
            b = [
              Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Choice 1', url: 'https://google.com'),
              Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Choice 2', callback_data: 'test'),
              Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Choice 3', switch_inline_query: 'Function not added.')
            ]
            mark1 = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: b)
            bot.api.send_message(chat_id: message.chat.id, text: 'Make a choice', reply_markup: mark1)
            end
        end
      end
    end
  end
end



