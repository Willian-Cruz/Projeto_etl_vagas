CREATE TABLE IF NOT EXISTS vagas (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo      TEXT NOT NULL,
    empresa     TEXT,
    localizacao TEXT,
    salario     REAL,
    nivel       TEXT
);
