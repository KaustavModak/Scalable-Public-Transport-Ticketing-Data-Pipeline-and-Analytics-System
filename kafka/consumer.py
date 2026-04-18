from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'tickets_partitioned',
    bootstrap_servers='localhost:9092',
    group_id='ticket-consumer-group',   # required for offsets
    auto_offset_reset='earliest',       # start from beginning if new
    enable_auto_commit=True,            # Kafka tracks progress
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer started...\n")

for message in consumer:
    print(f"""
Received:
Partition: {message.partition}
Offset: {message.offset}
Key: {message.key.decode('utf-8')}
Value: {message.value}
""")