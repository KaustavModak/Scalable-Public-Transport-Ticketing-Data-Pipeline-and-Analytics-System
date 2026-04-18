import pandas as pd
from sqlalchemy import create_engine

# Create engine
engine = create_engine("mysql+mysqlconnector://root:root@localhost/transport")

# Load data
df = pd.read_csv("data/processed/final_data.csv")

# IMPORTANT: Use chunks for large data (1M rows)
df.to_sql("tickets", engine, if_exists="append", index=False, chunksize=10000)

print("Data loaded successfully")