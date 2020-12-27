FROM ubuntu:18.04
MAINTAINER Dyswan
ADD . ./JudgeServer
WORKDIR /JudgeServer
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install --assume-yes apt-utils
RUN apt-get install python3 -y
RUN apt-get update && apt-get install python3-pip -y
RUN apt-get install libatomic1 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libz-dev -y
RUN apt-get install time -y
RUN apt-get install cmake -y
RUN apt-get install openjdk-8-jdk -y
RUN apt-get install libseccomp-dev -y && cd ./JudgerCore && mkdir build && cd build && cmake .. && make && make install && cd ../bindings/Python && python3 setup.py install
RUN pip3 install thrift
CMD ["python3", "server.py"]