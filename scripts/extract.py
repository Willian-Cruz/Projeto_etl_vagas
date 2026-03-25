import pandas as pd

def extract():
    dados = [{"titulo":"Analista de Dados", "empresa":"Empresa A", "localidade":"São Paulo","salario":5000},
             {"titulo":"Analista de Dados", "empresa":"Empresa A", "localidade":"São Paulo","salario":5000},
             {"titulo":"Analista de Dados", "empresa":"Empresa A", "localidade":"São Paulo","salario":5000},
            ]
    df = pd.DataFrame(dados)

    df.csv("data/raw/vagas.csv", index=False)
    print("Dados extraídos com sucesso!")

if __name__ == "__main__":
    extract()