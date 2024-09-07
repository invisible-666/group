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
Привет, напиши одну из этих комманд
/joke, /info\
""")

# Handle '/joke'
@bot.message_handler(commands=['joke'])
def send_welcome(message):
    bot.reply_to(message, """\
В Англии не играют в шахматы, потому что у них нет королевы!\
""")
    
# Handle '/info'
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я бот, который может выдать вам информацию о жителях Армении,
но так же я знаю пару шуток, которые вы можете получить прописав /joke\
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
##############################################################################################################################
#Может быть этот код без logik.py и без confing.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import sqlite3

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, напиши одну из этих комманд
/joke, /info\
""")

# Handle '/joke'
@bot.message_handler(commands=['joke'])
def send_welcome(message):
    bot.reply_to(message, """\
В Англии не играют в шахматы, потому что у них нет королевы!\
""")
    
# Handle '/info'
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я бот, который может выдать вам информацию о жителях Армении,
но так же я знаю пару шуток, которые вы можете получить прописав /joke\
""")
    
# Handle '/admin'
@bot.message_handler(commands=['admin'])
def send_welcome(message):
    bot.reply_to(message, """\
Меня создал человек по имени Егор и ему 17 лет\
""")

# Функция для поиска данных в базе данных
def find_in_db(search_text: str):
    conn = sqlite3.connect('over.db')
    c = conn.cursor()
    c.execute('SELECT * FROM data WHERE text_column = ?', (search_text,))
    result = c.fetchone()
    conn.close()
    return result

# Обработчик сообщений
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    result = find_in_db(text)
    
    if result:
        # Если запись найдена, отправляем её пользователю
        update.message.reply_text(f'Найденная запись: {result}')
    else:
        # Если запись не найдена, отправляем соответствующее сообщение
        update.message.reply_text('Такая строчка не существует')

def main():
    # Вставьте сюда токен вашего бота
    TOKEN = '6785089720:AAHwi9nr-uS926XH7GK0hdtCwIODe1U5S4M'

    updater = Updater(TOKEN)

    dp = updater.dispatcher

    # Обработчик сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
