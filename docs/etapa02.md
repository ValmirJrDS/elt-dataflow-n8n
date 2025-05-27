# ✅ Checkpoint – Etapa 2 Concluída

## 🔥 API Escolhida:
- **DummyJSON API** → https://dummyjson.com/docs
- Dados: Produtos, Carrinhos (Vendas), Usuários.

## 🔗 Pipeline Definido:
1. Coleta via API
2. Armazenamento no PostgreSQL (Schema: raw)
3. Transformação via dbt (Schemas: stg, mart)
4. Forecast com ML (Regressão Linear ou outro modelo simples)
5. Consumo via WhatsApp usando n8n + OpenAI + Evolution API

## 🏗️ Infraestrutura:
- Local: Docker Compose
- Produção: GCP (Compute Engine + CloudSQL + Storage opcional)

---
✔️ Ponto salvo para retorno caso necessário.
