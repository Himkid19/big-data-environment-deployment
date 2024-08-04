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