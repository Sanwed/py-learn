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
  for i in range(1, amount):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))


def update_odd(new_balance):
  cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = 1', (new_balance,))


def delete_every_third():
  cursor.execute('DELETE FROM Users WHERE id % 3 = 1')


def delete_by_id(id):
  cursor.execute('DELETE FROM Users WHERE id = ?', (id,))


def show_all_exclude_age(age):
  cursor.execute('SELECT * FROM Users WHERE age != ?', (age,))
  users = cursor.fetchall()

  for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')


def count():
  users_count = cursor.execute('SELECT COUNT(*) FROM Users')
  return users_count.fetchone()[0]


def count_balance():
  balances = cursor.execute('SELECT SUM(balance) FROM Users')
  return balances.fetchone()[0]


add_users(10)
update_odd(500)
delete_every_third()
show_all_exclude_age(60)
delete_by_id(6)
total_users = count()
all_balances = count_balance()
print(all_balances / total_users)

connection.commit()
connection.close()
