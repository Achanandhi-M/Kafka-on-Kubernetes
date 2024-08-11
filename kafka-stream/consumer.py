from kafka import KafkaProducer
from kafka import KafkaConsumer
import threading

# Set up the producer
producer = KafkaProducer(bootstrap_servers='10.43.72.142:9092')

# Set up the consumer
consumer = KafkaConsumer(
    'user1-topic',
    bootstrap_servers='10.43.72.142:9092',
    auto_offset_reset='earliest',
    group_id='user2-group',
    enable_auto_commit=True
)

def send_message():
    print("Enter message to send . Type 'exit' to quit.")
    while True:
        message = input("")
        if message.lower() == 'exit':
            break
        producer.send('user2-topic', value=message.encode('utf-8'))
        producer.flush()

def receive_message():
    for message in consumer:
        print(f"Message from User 1: {message.value.decode('utf-8')}")

# Start the consumer thread
consumer_thread = threading.Thread(target=receive_message)
consumer_thread.start()

# Start the producer loop
send_message()