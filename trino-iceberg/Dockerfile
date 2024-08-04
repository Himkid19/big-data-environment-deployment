FROM ubuntu

USER root

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

ADD . /src
COPY requirements.txt .

RUN pip3 install -r requirements.txt