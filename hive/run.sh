#启动Hadoop
source /etc/profile && hadoop namenode -format   
start-dfs.sh && start-yarn.sh
#启动hive链接mysql数据库
schematool -initSchema -dbType mysql
#启动HiveServer
nohup hiveserver2 &