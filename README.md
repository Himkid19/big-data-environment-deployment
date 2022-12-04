# process_of_spark_deployment
## 目的
记录学习spark过程和积累知识

## 目标
- 通过简单流程配置搭建分布式可扩充的spark集群
## 搭建记录
### step1: 购置服务器
华为云云服务器
### step2: 2022-12-03 服务器环境部署
[部署参考资料](https://zhuanlan.zhihu.com/p/421375012)
1. 服务器安装好docker，docker-compose
2. 拉取spark镜像
```
docker pull bitnami/spark:3
```
3. 创建并编写docker-compose.yml，构造1主两从的spark集群环境，方便调试
4. 执行docker-compose up -d
5. 服务器安全组配置```:8080```对外，即可通过```公网ip:8080```查看spark页面
