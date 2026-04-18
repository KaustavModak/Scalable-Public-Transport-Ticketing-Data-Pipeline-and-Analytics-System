from kafka import KafkaProducer
import json
import pandas as pd
import time

# Create producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: str(k).encode('utf-8')
)

# Load data
df = pd.read_csv("data/processed/final_data.csv")

# Send data
for _, row in df.iterrows():
    data = row.to_dict()

    # Use city as key → ensures partitioning
    key = data['city']

    producer.send(
        'tickets_partitioned',
        key=key,
        value=data
    )

    print(f"Sent to partition (by city={key}): {data}")
    time.sleep(1)

producer.flush()