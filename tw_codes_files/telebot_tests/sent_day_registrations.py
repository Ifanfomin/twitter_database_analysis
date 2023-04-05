import telebot
import sqlite3

conn = sqlite3.connect(r'D:\projects\dbase\twitterdb\tw_db_2mln\twitter_2mln.db')
cur = conn.cursor()

bot = telebot.TeleBot("TOKEN", parse_mode=None)


def send_day_registrations(message):

    #тут нужно достать из отправленного боту текста день
    
    query = 'SELECT count() FROM accounts WHERE created_at LIKE "%' + day + '%"'
    cur.execute(query)
    day_registrations = cur.fetchall
    
    bot.reply_to(message, "Howdy, how are you doing?")


bot.infinity_polling()
