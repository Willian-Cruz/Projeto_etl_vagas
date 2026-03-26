# 🚀 Pipeline de Dados de Vagas (Python + SQL)

Projeto de Engenharia de Dados que implementa um pipeline ETL completo para coleta, transformação e armazenamento de dados de vagas de emprego.

---

## 📌 Objetivo

Construir um pipeline de dados que simula um fluxo real de engenharia de dados:

- Extração de dados (simulando API)
- Transformação e limpeza
- Carga em banco de dados SQL
- Preparação para análise

---

## 🧱 Arquitetura do Projeto
projeto_vagas/
<br>│
<br>├── data/
<br>│ ├── raw/ # Dados brutos
<br>│ ├── processed/ # Dados tratados
<br>│
<br>├── scripts/
<br>│ ├── extract.py # Extração de dados
<br>│ ├── transform.py # Limpeza e transformação
<br>│ ├── load.py # Carga no banco
<br>│
<br>├── database/
<br>│ ├── schema.sql # Estrutura do banco
<br>│ ├── vagas.db # Banco SQLite
<br>│
<br>├── main.py # Orquestração do pipeline
<br>└── README.md


---

## ⚙️ Tecnologias Utilizadas

- Python
- Pandas
- SQLite
- SQL

---

## 🔄 Pipeline ETL

### 1. Extract
Coleta de dados simulando uma API de vagas e armazenamento em CSV.

### 2. Transform
- Remoção de duplicados  
- Tratamento de valores nulos  
- Criação de novas colunas (ex: nível da vaga)

### 3. Load
Carga dos dados tratados em banco de dados SQLite.

---

## ▶️ Como Executar o Projeto

### 1. Clonar repositório
```bash
git clone https://github.com/seu-usuario/projeto_vagas.git
cd projeto_vagas
```
### 2. Criar ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3.Instalar dependências
```pip install pandas```

### 4. Executar pipeline
```python main.py```
