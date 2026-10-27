"""Carga: grava as vagas tratadas no banco SQLite usando database/schema.sql."""
import os
import sqlite3

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_FILE = os.path.join(BASE_DIR, "data", "processed", "vagas_tratadas.csv")
SCHEMA_FILE = os.path.join(BASE_DIR, "database", "schema.sql")
DB_FILE = os.path.join(BASE_DIR, "database", "vagas.db")


def load() -> int:
    print("Iniciando carga...")

    df = pd.read_csv(PROCESSED_FILE)

    with sqlite3.connect(DB_FILE) as conn:
        with open(SCHEMA_FILE, encoding="utf-8") as f:
            conn.executescript(f.read())

        # Carga completa: substitui o conteúdo a cada execução.
        conn.execute("DELETE FROM vagas")
        df.to_sql("vagas", conn, if_exists="append", index=False)

        total = conn.execute("SELECT COUNT(*) FROM vagas").fetchone()[0]

    print(f"Carga concluída: {total} vagas em {DB_FILE}")
    return total


if __name__ == "__main__":
    load()
