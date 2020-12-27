docker build -t judger:test .
docker run -d --network=host --name=JudgeServer judger:test