import telebot

bot = telebot.TeleBot("Your_Bot_Token") # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def send_echo(message):
		#bot.reply_to(message, message.text)
		
		bot.send_message(message.chat.id, message.text)


bot.infinity_polling()

