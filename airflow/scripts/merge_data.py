import pandas as pd
import os

BASE_PATH = "/opt/airflow/data"
RAW_PATH = f"{BASE_PATH}/raw"
PROCESSED_PATH = f"{BASE_PATH}/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

df1 = pd.read_csv(f"{RAW_PATH}/data1.csv")
df2 = pd.read_csv(f"{RAW_PATH}/data2.csv")

df = pd.concat([df1, df2])

df['price'].fillna(df['price'].mean(), inplace=True)

df.to_csv(f"{PROCESSED_PATH}/merged_data.csv", index=False)

print(" Merged dataset created (1M rows)")