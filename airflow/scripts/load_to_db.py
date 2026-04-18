import pandas as pd
from sqlalchemy import create_engine

BASE_PATH = "/opt/airflow/data"
PROCESSED_PATH = f"{BASE_PATH}/processed"

# Postgres connection (matches docker-compose)
engine = create_engine("postgresql+psycopg2://airflow:airflow@postgres:5432/airflow")

df = pd.read_csv(f"{PROCESSED_PATH}/final_data.csv")

df.to_sql(
    "tickets",
    engine,
    if_exists="replace",
    index=False,
    chunksize=10000
)

print(" Data loaded into Postgres")