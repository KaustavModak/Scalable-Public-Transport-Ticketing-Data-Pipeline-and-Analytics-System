import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd

# Import custom modules
from modules.transform import normalize_price, add_features, aggregate
from modules.validator import check_nulls, detect_anomalies, check_duplicates

# LOAD MERGED DATA (1M rows)

df = pd.read_csv("data/processed/merged_data.csv")

print("\n Data Loaded Successfully (1M rows)")

# VALIDATION

print("\n Checking Null Values:")
print(check_nulls(df))

print("\n Checking Duplicates:")
print(check_duplicates(df).shape)

print("\n Checking Anomalies:")
print(detect_anomalies(df).shape)

# TRANSFORMATION

# Normalize price
df = normalize_price(df)

# Add new feature
df = add_features(df)

print("\n Transformation Completed")

# AGGREGATION

print("\n Revenue by Route:")
print(aggregate(df))

# SAVE PROCESSED DATA

df.to_csv("data/processed/final_data.csv", index=False)

print("\n Final processed data saved as final_data.csv")