from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer
from pyflink.datastream.connectors.jdbc import JdbcSink
from pyflink.datastream.formats.json import JsonRowDeserializationSchema
from pyflink.common import WatermarkStrategy, Row

# 消费的数据打印出来是None值
env = StreamExecutionEnvironment.get_execution_environment()
# the sql connector for kafka is used here as it's a fat jar and could avoid dependency issues
env.add_jars("file:///D:/acer_project/py-kafka-flink/jars/flink-sql-connector-kafka_2.11-1.14.4.jar", "file:///D:/acer_project/py-kafka-flink/jars/flink-sql-connector-kafka_2.11-1。14.4.jar")


row_type_info = Types.ROW_NAMED(['createTime', 'orderId', 'payAmount', 'payPlatform', 'provinceId', 'chain'], [Types.STRING(), Types.STRING(), Types.STRING(), Types.STRING(), Types.STRING(), Types.STRING()])
json_format = JsonRowDeserializationSchema.builder().type_info(row_type_info).build()

kafka_consumer = FlinkKafkaConsumer(
    topics='payment_msg',
    deserialization_schema=json_format,
    properties={'bootstrap.servers': 'localhost:9092', 'group.id': 'test_group'})

ds = env.add_source(kafka_consumer)

with ds.execute_and_collect() as results:
    for result in results:
        print(result)
