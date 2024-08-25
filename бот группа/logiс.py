import sqlite3

# Подключение к базе данных .db
conn = sqlite3.connect('over.db')
cursor = conn.cursor()

# Пример создания таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    ID INTEGER PRIMARY KEY,
                    NOMER TEXT NULL,
                    NAME TEXT NOT NULL,
                    ADRESS TEXT NULL,
                    PASWW TEXT NOT NULL
                )''')

# Пример вставки данных
#cursor.execute('''INSERT INTO users (username, first_name, last_name)
#                  VALUES (?, ?, ?)''', ('user1', 'John', 'Doe'))

# Пример выполнения запроса
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закрытие соединения
conn.commit()
conn.close()
