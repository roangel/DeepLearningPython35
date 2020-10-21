FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install numpy theano

COPY . /usr/src/dockertest

WORKDIR /usr/src/dockertest

CMD ["python3", "test_network1.py"]
