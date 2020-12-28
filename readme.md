# codeRunner服务器
基于thrift构建的服务器，可以用单文件编译运行

## 使用
构建镜像
```
docker build -t judger:test .
```
在后台运行容器
```
docker run -d --network=host --name=JudgeServer judger:test
```