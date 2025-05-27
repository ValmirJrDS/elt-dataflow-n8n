import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


def extract_and_load_carts():
    url = "https://dummyjson.com/carts?limit=100"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Erro na requisição: {response.status_code}")

    data = response.json()
    carts = data['carts']

    df = pd.json_normalize(carts)

    engine = create_engine('postgresql://postgres:postgres@postgres:5432/db_raw')

    df.to_sql('carts_raw', engine, if_exists='replace', index=False)
    print("✅ Dados de Carrinhos carregados com sucesso!")


if __name__ == "__main__":
    extract_and_load_carts()
