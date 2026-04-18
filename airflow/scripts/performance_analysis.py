import pandas as pd
import time

BASE_PATH = "/opt/airflow/data"
PROCESSED_PATH = f"{BASE_PATH}/processed"

start_time = time.time()
df = pd.read_csv(f"{PROCESSED_PATH}/final_data.csv")
end_time = time.time()

print("\n Load Time:", end_time - start_time)

print("\nMemory BEFORE:")
print(df.memory_usage(deep=True))

opt_start = time.time()

df["route"] = df["route"].astype("category")
df["city"] = df["city"].astype("category")
df["vehicle_type"] = df["vehicle_type"].astype("category")
df["price_category"] = df["price_category"].astype("category")

opt_end = time.time()

print("\n Optimization Time:", opt_end - opt_start)

print("\nMemory AFTER:")
print(df.memory_usage(deep=True))

start = time.time()
df.groupby("route")["price"].sum()
end = time.time()

print("\n Aggregation Time:", end - start)

print("\n PERFORMANCE ANALYSIS COMPLETE")