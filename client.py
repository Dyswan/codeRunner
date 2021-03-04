from __future__ import print_function
import logging
import sys


import grpc
import codeRunner_pb2 as codeRunner
import codeRunner_pb2_grpc as codeRunner_grpc

def run():
    # 使用with语法保证channel自动close
    with grpc.insecure_channel('0.0.0.0:8233') as channel:
        # 客户端通过stub来实现rpc通信
        stub = codeRunner_grpc.codeRunnerStub(channel)
        Input = ""
        code='''#include <iostream>
        using namespace std;
        int main(){
            printf("hello world\\n");
        }
            '''
        request = codeRunner.codeRunnerRequest(\
            language_ = codeRunner.codeLanguage.Cpp,
            code_ = code,
            input_ = Input
            )
        # 客户端必须使用定义好的类型，这里是HelloRequest类型
        response = stub.judge(request = request)
        print ("hello client received: " , response.result_)
# 1613637295
if __name__ == "__main__":
    logging.basicConfig()
    run()