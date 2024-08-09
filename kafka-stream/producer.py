from kafka import KafkaProducer
import os
import signal
import sys

# Set up the producer with Kafka bootstrap server from environment variable
bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

def send_message():
    print("Enter message to send. Type 'exit' to quit.")
    while True:
        message = input("")
        if message.lower() == 'exit':
            break
        producer.send('user1-topic', value=message.encode('utf-8'))
        producer.flush()

def signal_handler(sig, frame):
    print('Shutting down gracefully')
    producer.close()
    sys.exit(0)

# Register signal handlers for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Start the producer loop
send_message()
