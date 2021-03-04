# codeRunner服务器
基于gRPC构建的服务器，可以支持单文件编译运行

## 使用

构建镜像
```
docker build -t judger:test .
```
### 单服务构建
在后台运行容器
```
docker run -d --network=host --name=JudgeServer judger:test
```

### 负载均衡运行
```
docker-compose up --scale codeRunner=3 -d
```