import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute(f'''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')
    # for i in range(1, 5):
    #     cursor.execute("INSERT INTO Users(title, description, price) VALUES (?, ?, ?)",
    #                    (f"Бад{i}", f"Описание к продукту {i}", i*10))

    connection.commit()


def get_all_products():
    return cursor.execute(f'''
SELECT * FROM Users
''')


# connection.commit()
# connection.close()
