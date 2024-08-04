FROM trinodb/trino:408

USER root

ENV TRINO_HOME=/opt/trino

COPY config/* $TRINO_HOME/conf/
COPY catalog/ /etc/trino/catalog/

EXPOSE 8080