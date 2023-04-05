import telebot

bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)

def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()




@bot.message_handler(filters)
def function_name(message):
	bot.reply_to(message, "This is a message handler")

@bot.callback_query_handler(func=lambda call: True)
def test_callback(call): # <- passes a CallbackQuery type object to your function
    logger.info(call)
