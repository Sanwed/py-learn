import email
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


def get_all():
  cursor.execute('SELECT * FROM Users')
  return cursor.fetchall()


def add_users(amount):
  for i in range(1, len(get_all()) + 1):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))


def update_even(new_balance):
  for i in range(1, len(get_all()) + 1):
    if i % 2 == 0:
      cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (new_balance, i))


def delete_every_third():
  for i in range(1, len(get_all()) + 1):
    if i % 3 == 0:
      cursor.execute('DELETE FROM Users WHERE id = ?', (i,))


def show_all_exclude_age(age):
  cursor.execute('SELECT * FROM Users WHERE age < ?', (age,))
  users = cursor.fetchall()

  for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')


add_users(10)
update_even(500)
delete_every_third()
show_all_exclude_age(60)

connection.commit()
connection.close()
