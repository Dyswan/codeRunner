构建镜像
```
docker build -t judger:test .
```
在后台运行容器
```
docker run -d --network=host --name=JudgeServer judger:test
```