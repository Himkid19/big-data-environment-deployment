## 部署Hadoop测试集群

<pre><code>
#[创建容器]
docker-compose up -d
#[格式化HDFS。第一次启动集群前，需要先格式化HDFS；以后每次启动集群时，都不需要再次格式化HDFS]
docker-compose exec hadoop-master hdfs namenode -format
#[使环境变量生效]
docker-compose exec hadoop-master source /etc/profile
#[启动HDFS]
docker-compose exec spark-master start-dfs.sh
#[启动YARN]
docker-compose exec spark-master start-yarn.sh
#[启动Spark]
docker-compose exec spark-master start-all.sh
</code></pre>

查看 ```localhost:8080``` 查看hadoop是否正常运行