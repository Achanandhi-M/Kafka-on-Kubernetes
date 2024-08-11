# Kafka on Kubernetes (K3s) Setup Guide

This guide provides instructions on how to deploy Kafka on a Kubernetes cluster using K3s, and how to run a simple Kafka producer and consumer in Python.

## Prerequisites

- A Kubernetes cluster (K3s recommended).
- `kubectl` configured to interact with your Kubernetes cluster.
- Python 3 installed with the `kafka-python` library.

## Step 1: Deploy Zookeeper

1. Create a Kubernetes YAML file for deploying Zookeeper.
2. Apply the YAML file to your Kubernetes cluster using the command:
   ```bash
   kubectl apply -f <your-zookeeper-deployment.yaml>
   ```
3. Verify that the Zookeeper service and pod are running in the `kafka` namespace.

## Step 2: Deploy Kafka Broker

1. Create a Kubernetes YAML file for deploying the Kafka broker.
2. Apply the YAML file to your Kubernetes cluster using the command:
   ```bash
   kubectl apply -f <your-kafka-deployment.yaml>
   ```
3. Verify that the Kafka service and pod are running in the `kafka` namespace.

## Step 3: Set Up Python Kafka Producer and Consumer

1. Ensure that the `kafka-python` library is installed. If not, install it using:
   ```bash
   pip install kafka-python
   ```
2. Create two Python scripts: one for User 1 and one for User 2.
3. In each script, configure the producer and consumer to connect to your Kafka broker.

## Step 4: Run the Scripts

1. Run the Python script for User 1 in one terminal.
2. Run the Python script for User 2 in another terminal.
3. Start sending and receiving messages between User 1 and User 2.

## Step 5: Clean Up

1. To clean up your Kubernetes resources, delete the Kafka and Zookeeper deployments:
   ```bash
   kubectl delete -f <your-kafka-deployment.yaml>
   kubectl delete -f <your-zookeeper-deployment.yaml>
   ```