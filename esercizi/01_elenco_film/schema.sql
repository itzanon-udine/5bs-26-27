DROP TABLE IF EXISTS film;

CREATE TABLE film (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    regista TEXT NOT NULL,
    anno INTEGER NOT NULL
);

INSERT INTO film (titolo, regista, anno) VALUES ('Inception', 'Christopher Nolan', 2010);
INSERT INTO film (titolo, regista, anno) VALUES ('Pulp Fiction', 'Quentin Tarantino', 1994);
INSERT INTO film (titolo, regista, anno) VALUES ('Matrix', 'Lana Wachowski', 1999);