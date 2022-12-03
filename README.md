# process_of_spark_deployment
## 目的
记录学习spark过程和积累知识

## 目标
- 通过简单流程配置搭建分布式可扩充的spark集群
## 搭建记录
### 购置服务器
### 2022-12-03 服务器环境部署
[部署参考资料](https://www.jianshu.com/p/d6a406da3cba)
1.编写dockerfile
```
FROM openjdk:8-alpine
RUN apk --update add wget tar bash

RUN wget https://archive.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
RUN tar -xzf spark-2.4.0-bin-hadoop2.7.tgz && \
    mv spark-2.4.0-bin-hadoop2.7 /spark && \
    rm spark-2.4.0-bin-hadoop2.7.tgz
```
2.运行docker
