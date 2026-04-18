import pandas as pd

# Load multiple CSVs
df1 = pd.read_csv("data/raw/data1.csv")
df2 = pd.read_csv("data/raw/data2.csv")

# Merge datasets
df = pd.concat([df1, df2])

# Handle missing values
df['price'].fillna(df['price'].mean(), inplace=True)

# Save merged dataset
df.to_csv("data/processed/merged_data.csv", index=False)

print("Merged dataset (1M rows)")