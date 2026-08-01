# 🧾 RP Database — Camada de Persistência para Automação Fiscal (Projeto Conceitual)

> **Projeto experimental / MVP conceitual**, desenvolvido para estudar modelagem de banco de dados e Python aplicados a um cenário de automação (RPA) de leitura de invoices e documentos fiscais. Não utiliza nomenclaturas, colunas ou credenciais reais de nenhuma empresa — toda a estrutura foi construída como exercício de arquitetura e modelagem.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![ORM](https://img.shields.io/badge/ORM-SQLAlchemy-D71F00?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conceitual%20%2F%20MVP-blue)

---

## 🚀 Sobre o Projeto

Este repositório nasceu de um desafio prático: modelar a camada de persistência de uma automação (RPA) responsável por extrair dados de invoices e documentos fiscais e armazená-los de forma estruturada.

Diferente de uma API tradicional, o foco aqui **não é expor endpoints**, mas sim validar a lógica de acesso a dados isoladamente:

- **Conexão desacoplada** — um `Connector` dedicado, responsável apenas por abrir/gerenciar a conexão com o banco.
- **CRUDs lógicos** — métodos de criação, leitura, atualização e remoção implementados diretamente sobre o ORM, sem camada de DTO ou de endpoint.
- **Captura de erros via Logs** — em vez de deixar exceptions estourarem no fluxo principal, os erros são capturados e registrados em log, simulando o comportamento esperado de uma automação rodando em background.
- **Payloads de teste** — inputs de exemplo para simular o retorno de uma automação real, usados para validar os métodos de CRUD sem depender de um RPA completo rodando.

Foi neste projeto que comecei a migrar o foco de front-end (React) para estudo de modelagem de dados e Python.

## 🛠️ Stack Utilizada

| Camada | Tecnologia | Uso |
|---|---|---|
| Linguagem | Python | Lógica de conexão, CRUDs e captura de erros |
| ORM | SQLAlchemy (ou equivalente) | Modelagem das tabelas e relacionamento entre entidades |
| Persistência | Banco relacional | Armazenamento estruturado dos dados extraídos |
| Observabilidade | Logging (módulo `logging`) | Registro de falhas e eventos, sem uso de exceptions expostas |

## 📂 Estrutura do Projeto

```
RP_database/
├── database/        # Modelos, Connector e lógica de CRUD
├── logs/             # Arquivos de log gerados pela captura de erros
├── requirements.txt  # Dependências do projeto
└── .env.example       # Variáveis de ambiente (placeholders fictícios)
```

## ⚙️ Conceito de Arquitetura

### 1. Connector

Camada única responsável por abrir e encerrar a conexão com o banco, isolando o restante da aplicação de detalhes de driver/engine.

### 2. CRUDs Lógicos (sem DTO / sem endpoint)

Os métodos de CRUD operam diretamente sobre os modelos do ORM. A ideia foi validar a lógica de persistência de forma isolada, sem a complexidade de uma camada HTTP — simulando exatamente o que uma automação RPA faria ao processar um documento e gravar o resultado no banco.

### 3. Captura de Erros via Log

Em vez de propagar exceptions, cada operação de banco captura falhas e registra o evento na pasta `logs/`, com informações suficientes para diagnóstico posterior — um padrão comum em automações que rodam sem supervisão direta.

### 4. Payloads de Teste

Para simular o output de uma automação real de leitura de invoices/documentos fiscais, o projeto inclui exemplos de payloads usados como entrada para os métodos de CRUD, permitindo testar a persistência sem depender do RPA completo.

## 📦 Instalação e Setup

### Pré-requisitos

- Python (3.x)
- Banco de dados relacional configurado localmente ou via container

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/th1agOx/RP_database.git
cd RP_database

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

Configure o arquivo `.env` a partir do `.env.example`, com os dados de conexão do seu banco local:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=rp_database_dev
DB_USER=usuario_fake
DB_PASSWORD=senha_fake
```

## 📄 Licença

Projeto desenvolvido para fins de **estudo e portfólio pessoal**. Sinta-se à vontade para explorar o código como referência de modelagem e arquitetura de persistência de dados.
