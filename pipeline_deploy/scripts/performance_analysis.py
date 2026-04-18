import pandas as pd
import time

# -----------------------------------
# LOAD LARGE DATASET
# -----------------------------------

start_time = time.time()

df = pd.read_csv("data/processed/final_data.csv")

end_time = time.time()

print("\n Time to load data:", end_time - start_time, "seconds")


# -----------------------------------
# MEMORY USAGE BEFORE OPTIMIZATION
# -----------------------------------

print("\n Memory Usage BEFORE Optimization:")
print(df.memory_usage(deep=True))


# -----------------------------------
# OPTIMIZATION
# -----------------------------------

opt_start = time.time()

# Convert string columns to category (huge memory saving)
df["route"] = df["route"].astype("category")
df["city"] = df["city"].astype("category")
df["vehicle_type"] = df["vehicle_type"].astype("category")
df["price_category"] = df["price_category"].astype("category")

opt_end = time.time()

print("\n Optimization Time:", opt_end - opt_start, "seconds")


# -----------------------------------
# MEMORY USAGE AFTER OPTIMIZATION
# -----------------------------------

print("\n Memory Usage AFTER Optimization:")
print(df.memory_usage(deep=True))


# -----------------------------------
# PERFORMANCE COMPARISON
# -----------------------------------

# Before optimization (simulate)
start = time.time()
df.groupby("route")["price"].sum()
end = time.time()

print("\n Aggregation Time (Optimized):", end - start, "seconds")


# -----------------------------------
# RESULT SUMMARY
# -----------------------------------

print("\n PERFORMANCE ANALYSIS COMPLETE")