from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer


admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])

topic_names = ['topic1', 'topic2']


def create_topics(topic_names):

    existing_topic_list = consumer.topics()
    print(list(consumer.topics()))
    topic_list = []
    for topic in topic_names:
        if topic not in existing_topic_list:
            print('Topic : {} added '.format(topic))
            topic_list.append(NewTopic(name=topic, num_partitions=3, replication_factor=3))
        else:
            print('Topic : {topic} already exist ')
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    print("Topic Created Successfully")

consumer = KafkaConsumer(
    bootstrap_servers = ['localhost:9092'],
    )
create_topics(topic_names)