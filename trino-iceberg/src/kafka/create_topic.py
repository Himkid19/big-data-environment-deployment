from kafka import KafkaProducer, KafkaConsumer, KafkaClient, KafkaAdminClient
from kafka.errors import kafka_errors
from kafka.admin import NewTopic
import traceback
import json


def create_topic(
        topic='topic', 
        num_partitions=3, 
        configs=None, 
    timeout_ms=3000, 
    brokers=['localhost:9092'],
                 no_partition_change=True):
    client = KafkaClient(bootstrap_servers=brokers)

    if topic not in client.cluster.topics(exclude_internal_topics=True):  # Topic不存在

        request = client.CreateTopicsRequest_v0(
            create_topic_requests=[(
                topic,
                num_partitions,
                -1,  # replication unset.
                [],  # Partition assignment.
                [(key, value) for key, value in configs.items()],  # Configs
            )],
            timeout=timeout_ms
        )

        future = client.send(2, request)  # 2是Controller,发送给其他Node都创建失败。
        client.poll(timeout_ms=timeout_ms, future=future, sleep=False)  # 这里

        result = future.value
        # error_code = result.topic_error_codes[0][1]
        print("CREATE TOPIC RESPONSE: ", result)  # 0 success, 41 NOT_CONTROLLER, 36 ALREADY_EXISTS
        client.close()
    else:  # Topic已经存在
        print("Topic already exists!")
        return


if __name__ == '__main__':
    admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092"
    )
    topic_list = []
    topic_list.append(NewTopic(name="test_1", num_partitions=3, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)