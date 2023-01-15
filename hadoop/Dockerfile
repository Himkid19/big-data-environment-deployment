FROM registry.cn-hangzhou.aliyuncs.com/hadoop_test/hadoop_base

MAINTAINER acer <419832308@qq.com>

USER root

# 1. 安装 OpenSSH, OpenSSL, bzip2-devel
# 2. 同时配置SSH免密钥登陆
# RUN yum install -y openssh openssh-server openssh-clients openssl openssl-devel bzip2-devel && \
#     yum clean all && \
#     ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
#     cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    
ADD config/other/ssh_config /root/.ssh/config
RUN chmod 600 /root/.ssh/config && \
    chown root:root /root/.ssh/config

ADD config/hadoop/* $HADOOP_HOME/etc/hadoop/

#建立HDFS目录，日志目录. 格式化NameNode
RUN mkdir -p /works/hadoop/dfs/name && \ 
   mkdir -p /works/hadoop/dfs/data && \
   mkdir -p /works/hadoop/dfs/namesecondary && \
   mkdir $HADOOP_HOME/logs && \
   $HADOOP_HOME/bin/hdfs namenode -format

CMD [ "sh", "-c", "service sshd start; bash"]