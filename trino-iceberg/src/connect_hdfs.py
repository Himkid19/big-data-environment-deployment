from pyhdfs import HdfsClient

client = HdfsClient(hosts='localhost:50070', user_name='root')
client.copy_from_local('d:/acer_project/trino-iceberg/src/pydemo.txt', '/pydemo')

