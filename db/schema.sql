DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS production;

CREATE TABLE artist(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lastname TEXT NOT NULL
);

CREATE TABLE production(
production_id INTEGER PRIMARY KEY AUTOINCREMENT,
production_name TEXT NOT NULL,
production_owner TEXT NOT NULL
);

CREATE TABLE album(
album_id INTEGER PRIMARY KEY AUTOINCREMENT,
album_name TEXT NOT NULL,
artist_id INTEGER NOT NULL,
production_id INTEGER NOT NULL,
FOREIGN KEY (artist_id) REFERENCES artist (id),
FOREIGN KEY (production_id) REFERENCES production (production_id)
);

CREATE TABLE song(
song_id INTEGER PRIMARY KEY AUTOINCREMENT,
song_name TEXT NOT NULL,
artist_id INTEGER NOT NULL,
album_id INTEGER NOT NULL,
FOREIGN KEY (artist_id) REFERENCES artist (id),
FOREIGN KEY (album_id) REFERENCES album (album_id)
);