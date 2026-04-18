import pandas as pd
import numpy as np

# Generate 2 datasets (for merging)
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

df1.to_csv("data/raw/data1.csv", index=False)
df2.to_csv("data/raw/data2.csv", index=False)

print("Two datasets created")