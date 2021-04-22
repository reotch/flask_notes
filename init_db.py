import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('INSERT INTO notes (content) VALUES (?)', ('# Note number One',))
cur.execute('INSERT INTO notes (content) VALUES (?)', ('_Another note_',))
cur.execute('INSERT INTO notes (content) VALUES (?)', ('`code code code`',))

connection.commit()
connection.close()
