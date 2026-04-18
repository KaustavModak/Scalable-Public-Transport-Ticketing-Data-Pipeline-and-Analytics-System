import sys
import os
import pandas as pd

BASE_PATH = "/opt/airflow/data"
PROCESSED_PATH = f"{BASE_PATH}/processed"

sys.path.append("/opt/airflow")

from modules.transform import normalize_price, add_features, aggregate
from modules.validator import check_nulls, detect_anomalies, check_duplicates

df = pd.read_csv(f"{PROCESSED_PATH}/merged_data.csv")

print("\n Data Loaded")

print("\nNulls:")
print(check_nulls(df))

print("\nDuplicates:")
print(check_duplicates(df).shape)

print("\nAnomalies:")
print(detect_anomalies(df).shape)

df = normalize_price(df)
df = add_features(df)

print("\n Transformation Done")

print("\nAggregation:")
print(aggregate(df))

df.to_csv(f"{PROCESSED_PATH}/final_data.csv", index=False)

print("\n Final data saved")