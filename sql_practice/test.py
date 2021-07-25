import sqlite3


with open('data.txt') as f:
    data = f.read()

con = sqlite3.connect('test_db.db')
cur = con.cursor()

cur.execute(f'CREATE TABLE IF NOT EXISTS locations_test (date TEXT, price TEXT, link TEXT PRIMARY KEY)')
for item in data:
    cur.execute('INSERT '
con.commit()

cur.execute('SELECT * FROM locations_test')