from kafka import KafkaConsumer
import os
import signal
import sys

# Set up the consumer with Kafka bootstrap server from environment variable
bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
consumer = KafkaConsumer(
    'user2-topic',
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    group_id='user1-group',
    enable_auto_commit=True
)

def receive_message():
    for message in consumer:
        print(f"Message from User 2: {message.value.decode('utf-8')}")

def signal_handler(sig, frame):
    print('Shutting down gracefully')
    consumer.close()
    sys.exit(0)

# Register signal handlers for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Start the consumer loop
receive_message()
