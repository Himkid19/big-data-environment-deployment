## 环境准备
- Hadoop 3.2.0
- Hive 3.1.2
- mysql 8.0.1
- mysql-connector-java-5.1.49.jar
- hive_jdbc_2.5.15.1040


## 步骤
[参考](https://zhuanlan.zhihu.com/p/242658224)
1. 拉hadoop镜像
```docker pull registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base```
2. 建立hadoop用的内部网络
```docker network create --driver=bridge --subnet={内网ip}/16  hadoop```
3. 创建master/slave1/slave2容器
- master
```docker run -it --network hadoop -h Master --name Master -p 9870:9870 -p 8088:8088 -p 10000:10000 registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base bash```
- slave1/slave2
```docker run -it --network hadoop -h Slave1 --name Slave1 registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base bash```
```docker run -it --network hadoop -h Slave2 --name Slave2 registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base bash```
- 查看各个容器内的host映射
```vim etc/hosts```
查看分配的ip是多少
- 修改3个容器内的hosts映射：
```
{上一步中得到的ip}	Master
{上一步中得到的ip}	Slave1
{上一步中得到的ip}	Slave2
```
4. 启动hadoop
虽然容器里面已经把hadoop路径配置在系统变量里面，但每次进入需要运行source /etc/profile才能生效使用
```
# 让hadoop生效
source /etc/profile
#进入后格式化hdfs
hadoop namenode -format
# 启动全部
/usr/local/hadoop/sbin# ./start-all.sh
```