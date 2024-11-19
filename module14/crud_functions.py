import sqlite3


def initiate_db():
  conn = sqlite3.connect('not_telegram.db')
  cursor = conn.cursor()
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
  );
  ''')
  cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Пирожок', 'Пирожок с вареньем', 50)")
  cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Протеин', 'Белок 50%', 3000)")
  cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Креатинин', 'Запивать водой', 1500)")
  cursor.execute("INSERT INTO Products (title, description, price) VALUES ('Кока-кола', '2 литра бутылка', 200)")
  conn.commit()
  conn.close()


def get_all_products():
  conn = sqlite3.connect('not_telegram.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Products')
  products = cursor.fetchall()
  conn.close()
  return products
