import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()

cur.execute("INSERT INTO artist (name, lastname) VALUES (?, ?)",
            ('Dua', 'Lipa'))

cur.execute("INSERT INTO production (production_name, production_owner) VALUES (?, ?)",
            ('Dua', 'Lipa'))

cur.execute("INSERT INTO album (album_name, artist_id, production_id) VALUES (?, ?, ?)",
            ('Dua', 'Lipa', '1'))

connection.commit()
connection.close()