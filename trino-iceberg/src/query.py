import trino

if __name__ == '__main__':
    conn = trino.dbapi.connect(
        host='localhost',
        port=8080,
        user='root',
        catalog='iceberg',
        schema = 'hdfs',
    )

    cursor = conn.cursor()
    cursor.execute("select * from acer_json_from_hive")
    rows = cursor.fetchmany(size = 3)

    print(rows)

    cursor.close()
    conn.close()