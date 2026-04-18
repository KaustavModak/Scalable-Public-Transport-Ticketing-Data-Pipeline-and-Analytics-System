import pandas as pd
import numpy as np
import os

BASE_PATH = "/opt/airflow/data"
RAW_PATH = f"{BASE_PATH}/raw"

os.makedirs(RAW_PATH, exist_ok=True)

n = 500_000

def create_data(start_id):
    return pd.DataFrame({
        "ticket_id": np.arange(start_id, start_id + n),
        "user_id": np.random.randint(100, 1000, n),
        "route": np.random.choice(['A-B','B-C','C-D','D-E'], n),
        "price": np.random.randint(30, 100, n),
        "city": np.random.choice(['Delhi','Kolkata','Mumbai'], n),
        "vehicle_type": np.random.choice(['Bus','Metro','Train'], n)
    })

df1 = create_data(1)
df2 = create_data(n+1)

df1.to_csv(f"{RAW_PATH}/data1.csv", index=False)
df2.to_csv(f"{RAW_PATH}/data2.csv", index=False)

print(" Two datasets created")