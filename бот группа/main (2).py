#Импортируем все необходимые библиоеки
from telebot import TeleBot
from confing import *
import sqlite3
##############################################################

#Соединяемся с бд
connection = sqlite3.connect('over.db')

#Соединяем код с ботом с помощью токена
bot = TeleBot(TOKEN)

#комманды бота
###############################################################
# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
привет напиши одну из этих комманд
/joke, /info\
""")

# Handle '/joke'
@bot.message_handler(commands=['joke'])
def send_welcome(message):
    bot.reply_to(message, """\
В Англии не играют в шахматы потомучто у них нет королевы!\
""")
    
# Handle '/info'
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, """\
Я просто робот который знает всего лиш
одну шутку про королевы но также я могу
отпровлять информацию про жителей в Армении\
""")
    
# Handle '/admin'
@bot.message_handler(commands=['admin'])
def send_welcome(message):
    bot.reply_to(message, """\
Меня создал человек по имени Егор и ему 17 лет\
""")
###############################################################

#Главная команда чтобы вывести данные о человеке



###############################################################
#Выводим все сообщения
bot.infinity_polling()
###############################################################
#Завершаем работу с бд
connection.close()
#конец кода