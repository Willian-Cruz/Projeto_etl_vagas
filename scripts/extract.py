"""Extração: simula a resposta de uma API de vagas e grava o CSV bruto."""
import os

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw_data")


def extract() -> str:
    print("Iniciando extração...")

    # Dados simulados de uma API de vagas. Inclui de propósito uma vaga
    # duplicada e uma sem localização para exercitar a etapa de transformação.
    dados = [
        {"titulo": "Analista de Dados", "empresa": "Empresa A", "localizacao": "São Paulo", "salario": 5000},
        {"titulo": "Engenheiro de Dados", "empresa": "Empresa B", "localizacao": "Remoto", "salario": 8000},
        {"titulo": "Cientista de Dados", "empresa": "Empresa C", "localizacao": None, "salario": 9000},
        {"titulo": "Engenheiro de Dados", "empresa": "Empresa B", "localizacao": "Remoto", "salario": 8000},
    ]
    df = pd.DataFrame(dados)

    os.makedirs(RAW_DIR, exist_ok=True)
    caminho = os.path.join(RAW_DIR, "vagas.csv")
    df.to_csv(caminho, index=False)

    print(f"Extração concluída: {len(df)} linhas em {caminho}")
    return caminho


if __name__ == "__main__":
    extract()
