# ✅ Etapa 3 — Arquitetura ELT definida

## Componentes:
- Airflow (Astro Runtime)
- dbt Core
- Postgres
- n8n

## Pipeline:
1. Extração → Airflow + Python
2. Carga → Postgres (raw)
3. Transformação → dbt (staging + marts)
4. Machine Learning → Airflow + Python
5. Consumo → n8n + OpenAI + WhatsApp

## Status: 
✔️ Docker Compose estruturado
✔️ Astro rodando
✔️ Pronto para começar o desenvolvimento das DAGs, scripts de extração e dbt models.
