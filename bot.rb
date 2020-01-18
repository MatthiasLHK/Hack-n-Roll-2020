require 'telegram_bot'

token = '1003609645:AAHQ9HPHbwGGVQvJ19xD7cs3USVZWsBgq0E'

bot = TelegramBot.new(token: token)

bot.get_updates(fail_silently: true) do |message|
  puts "@#{message.from.username}: #{message.text}"
  command = message.get_command_for(bot)


  message.reply do |reply|
    case message.text
    when /start/i
      reply.text = "All I can do is say hello. try the /greet command."
    when /greet/i
      reply.text = "Hello, #{message.from.first_name}"
    when /play/i
      reply.text = "What is the captial of England?"
    else
      reply.text = "I have no idea what #{command.inspect} means."
    end 
    puts "sending #{reply.text.inspect} to @#{message.from.username}"
    reply.send_with(bot)
  end
end
