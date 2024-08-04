from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment
# sql-client jar包需要不一样 出现了依赖的报错
flink_home = '/opt/flink'
kafka_connector_jar_path = flink_home + '/lib/flink-sql-connector-kafka_2.11-1.14.4.jar'

env = StreamExecutionEnvironment.get_execution_environment()
env.add_jars(f"file:///D:/acer_project/py-kafka-flink/jars/flink-sql-connector-kafka_2.11-1.14.4.jar")

t_env = StreamTableEnvironment.create(stream_execution_environment=env)

t_env.execute_sql("""
       create table my_source (
        createTime varchar,
        orderId varchar,
        payAmount bigint,
        payPlatform varchar,
        probinceId varchar
        ) with (
        'connector' = 'kafka',
        'topic' = 'payment_msg',
        'properties.bootstrap.servers' = 'localhost:9092',
        'format' = 'json',
        'scan.startup.mode' = 'group-offsets',
        'properties.group.id' = 'test_real_time_cal1'
        )
    """)

ds = t_env.to_append_stream(
    t_env.from_path('my_source'),
    Types.ROW([Types.STRING(), Types.STRING(), Types.STRING(), Types.STRING(), Types.STRING()]))

ds.print()