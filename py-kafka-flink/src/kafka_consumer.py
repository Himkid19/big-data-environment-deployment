from kafka import KafkaConsumer
import json

def consumer_demo():
    consumer = KafkaConsumer(
        'payment_msg', 
        bootstrap_servers='localhost:9092',
        group_id='test'
    )
    for message in consumer:
        print(message)

if __name__ == '__main__':
    consumer_demo()
