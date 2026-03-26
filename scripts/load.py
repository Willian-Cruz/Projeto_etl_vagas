import pandas as pd
import sqlite3

def load():
    conn = sqlite3.connect("../data/vagas.db")

    df = pd.read_csv("../data/raw_data/processed/vagas_tratadas.csv")

    df.to_sql("vagas", conn, if_exists="replace", index=False)

    conn.close()

    print("Dados carregados no banco!")

if __name__ == "__main__":
    load()