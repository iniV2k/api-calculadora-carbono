# 🌍 Calculadora de Pegada de Carbono - API (Back-end)

Este é o repositório do back-end para o projeto de Calculadora de Pegada de Carbono, desenvolvido como Atividade Prática Supervisionada (APS).

Esta API é construída em Python usando o framework Flask e serve os dados de cálculo e fatores de emissão para o front-end em React.

**API de Produção :** `https://api-calculadora-carbono.onrender.com`

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Flask:** Para criar o servidor e as rotas da API.
* **Flask-CORS:** Para permitir a comunicação com o front-end.
* **Gunicorn:** Para servir a aplicação em produção.

---

## Endpoints da API

### 1. Calcular Pegada
* **Rota:** `POST /api/calcular`
* **Descrição:** Recebe um JSON com os dados do formulário (transporte, moradia, alimentação) e retorna um JSON com o cálculo detalhado da pegada de carbono anual.

### 2. Obter Fatores de Emissão
* **Rota:** `GET /api/fatores`
* **Descrição:** Retorna um JSON com o dicionário `FATORES_EMISSAO`, usado para exibir os dados na página de Metodologia do front-end.

---

## 🚀 Como Rodar Localmente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/iniV2k/api-calculadora-carbono.git
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv .venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Crie o arquivo `.env`:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione as variáveis locais:
    ```.env
    DEBUG=True
    ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
    ```

5.  **Rode o servidor de desenvolvimento:**
    ```bash
    python app.py
    ```
    A API estará rodando em `http://localhost:5000`.