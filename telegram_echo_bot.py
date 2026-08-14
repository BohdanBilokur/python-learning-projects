import telebot

BOT_TOKEN = "Your_Bot_Token"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message(message.chat.id, message.text)


bot.infinity_polling()

