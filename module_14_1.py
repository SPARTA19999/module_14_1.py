import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)

''')
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(? ,? ,? , ?)",
                   (f"User{i}", f"example{i}@gmail.com", 10*i, 1000))

for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ?", (500,))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id =?", (i,))
connection.commit()
cursor.execute("SELECT * FROM Users WHERE age != 60")
for j in cursor.fetchall():
    print(f"Имя: {j[1]} | Почта: {j[2]} | Возраст: {j[3]} | Баланс: {j[4]}")
connection.close()