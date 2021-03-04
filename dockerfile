FROM ubuntu:18.04
MAINTAINER Dyswan
ADD . ./JudgeServer
WORKDIR /JudgeServer
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
&& apt-get install --assume-yes apt-utils \
&& apt-get install python3 -y \
&& apt-get update && apt-get install python3-pip -y \
&& pip3 install -i https://mirrors.aliyun.com/pypi/simple grpcio \
&& pip3 install -i https://mirrors.aliyun.com/pypi/simple grpcio-tools \
&& apt-get install libatomic1 -y \
&& apt-get install libssl-dev -y \
&& apt-get install libz-dev -y \
&& apt-get install time -y \
&& apt-get install cmake -y \
&& apt-get install openjdk-8-jdk -y \
&& apt-get install libseccomp-dev -y && cd ./JudgerCore && mkdir build && cd build && cmake .. && make && make install && cd ../bindings/Python && python3 setup.py install
CMD ["python3", "server.py"]
# FROM judger:base
# MAINTAINER Dyswan
# ADD . ./JudgeServer
# WORKDIR /JudgeServer
# RUN cd ./JudgerCore && mkdir build && cd build && cmake .. && make && make install && cd ../bindings/Python && python3 setup.py install
# CMD ["python3", "server.py"]