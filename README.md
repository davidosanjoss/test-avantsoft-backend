# 🧩 Avantsoft Challenge – Loja de Brinquedos API

Projeto desenvolvido como parte de um processo seletivo para a empresa **Avantsoft**.

## 📌 Tecnologias utilizadas

- **Python 3.13** + **Django 5.2**
- **Django REST Framework**
- **PostgreSQL 16**
- **Poetry** para gerenciamento de dependências
- **Docker + Docker Compose** (ambientes dev e prod)
- **JWT** para autenticação
- **Pytest** para testes automatizados

## 🚀 Funcionalidades da API

- CRUD de clientes (com filtros por nome e e-mail)
- CRUD de vendas por cliente
- Estatísticas:
    - Total de vendas por dia
    - Cliente com maior volume de vendas
    - Cliente com maior média por venda
    - Cliente com maior frequência de compra (dias únicos com vendas)
- Autenticação JWT protegendo todas as rotas
- Paginação e normalização de dados conforme estrutura especificada
- Testes automatizados cobrindo views e integrações

## 🧪 Como rodar localmente com Docker

### ✅ Requisitos:

- Docker e Docker Compose
- Python 3.13 (apenas se não usar Docker)
- Poetry

### ▶️ Subir ambiente de desenvolvimento:

```bash
make up-dev
```

### 🔧 Aplicar migrações e criar superusuário:

```bash
make migrate
make createsuperuser
```

## 🌐 Endpoints principais

| Método | Rota                             | Descrição                                 |
|--------|----------------------------------|-------------------------------------------|
| GET    | `/api/clients/`                  | Listar clientes (com paginação e filtros) |
| POST   | `/api/clients/`                  | Criar cliente                             |
| PATCH  | `/api/clients/<id>/`             | Editar cliente                            |
| DELETE | `/api/clients/<id>/`             | Deletar cliente                           |
| GET    | `/api/statistics/top-customers/` | Estatísticas de clientes                  |
| GET    | `/api/statistics/daily-sales/`   | Total de vendas por dia                   |

## 🧾 Execução dos testes

```bash
make test
```

## 📁 Estrutura de pastas

```
avantsoft-backend/
├── clients/
├── sales/
├── core/
├── tests/
│   └── test_clients_crud.py
│   └── test_sales_crud.py
│   └── test_views.py
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── Makefile
├── .env.dev
├── .env.prod
└── README.md
```

## 📦 Extras

- Arquivos estáticos são servidos automaticamente via Nginx em produção
- Ambiente separado para dev/prod com `.env` e `Makefile`

## 👨‍💻 Autor

Desenvolvido por [Seu Nome Aqui] para o desafio técnico da Avantsoft.