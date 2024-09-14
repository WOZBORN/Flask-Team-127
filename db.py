import sqlite3

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

cursor.execute('''
create table IF NOT EXISTS users (
  id text PRIMARY KEY,
  tg_id int,
  username text
 );
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS games (
  id integer PRIMARY KEY AUTOINCREMENT,
  status integer not NULL,
  created_at integer NOT NULL DEFAULT CURRENT_TIMESTAMP,
  winner_id text
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS game_user (
  id integer PRIMARY KEY AUTOINCREMENT,
  game_id integer not NULL,
  user_id text not NULL,
  sign integer not NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS wins (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	game_id INTEGER NOT NULL,
	user_id TEXT NOT NULL,
	created_at INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS moves (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	game_id INTEGER NOT NULL,
	user_id INTEGER NOT NULL,
	row INTEGER NOT NULL,
	col INTEGER NOT NULL,
	sign TEXT NOT NULL,
	created_at INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP
);
''')
cursor.execute('''
CREATE UNIQUE INDEX game_id_col_row_moves ON moves (game_id, col, row);
''')

conn.commit()
conn.close()