# Kafka Messaging Demo

This is a simple two-way messaging application using Apache Kafka. It demonstrates how to send and receive messages between two users using Kafka producers and consumers.

## Prerequisites

- Apache Kafka and Zookeeper installed and running.
- Python 3.6 or higher.
- `kafka-python` library installed.

## Setup

### 1. Start Zookeeper and Kafka

Start Zookeeper:
```bash
zookeeper-server-start.sh config/zookeeper.properties
```

Start Kafka:
```bash
kafka-server-start.sh config/server.properties
```

### 2. Create Kafka Topics

Create two topics, one for each user:
```bash
kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic user1-topic
kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic user2-topic
```

### 3. Set Up Python Environment

Create and activate a virtual environment:
```bash
python -m venv kafka-env
source kafka-env/bin/activate  # On Windows use `kafka-env\Scripts\activate`
```

Install the required Python package:
```bash
pip install kafka-python
```

## Running the Application

### Start User 1 Script

In one terminal, run the producer script for User 1:
```bash
python producer.py
```

### Start User 2 Script

In another terminal, run the consumer script for User 2:
```bash
python consumer.py
```

Now, you can send and receive messages between User 1 and User 2. The input prompt will always show `(User 1):` for User 1 and `(User 2):` for User 2, with received messages displayed alongside.

## Notes

- Type `exit` to quit the application.
- Ensure Zookeeper and Kafka are running before starting the scripts.
- Modify the scripts as needed for your use case.

Enjoy your two-way messaging application using Apache Kafka!
```
