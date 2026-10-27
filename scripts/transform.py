"""Transformação: remove duplicados, trata nulos e cria a coluna de nível."""
import os

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_FILE = os.path.join(BASE_DIR, "data", "raw_data", "vagas.csv")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")


def classificar_nivel(titulo: str) -> str:
    """Regra simples de exemplo: analistas como Júnior, demais cargos como Sênior."""
    return "Júnior" if "Analista" in titulo else "Sênior"


def transform() -> str:
    print("Iniciando transformação...")

    df = pd.read_csv(RAW_FILE)
    linhas_antes = len(df)

    df = df.drop_duplicates()
    df["localizacao"] = df["localizacao"].fillna("Não identificado")
    df["nivel"] = df["titulo"].apply(classificar_nivel)

    os.makedirs(PROCESSED_DIR, exist_ok=True)
    caminho = os.path.join(PROCESSED_DIR, "vagas_tratadas.csv")
    df.to_csv(caminho, index=False)

    print(f"Transformação concluída: {linhas_antes} -> {len(df)} linhas em {caminho}")
    return caminho


if __name__ == "__main__":
    transform()
