import sys
sys.path.append('./proto')

from concurrent import futures
from utils import runner
from config import Language, Type
import grpc
import codeRunner_pb2 as codeRunner
import codeRunner_pb2_grpc as codeRunner_grpc

class codeRunnerHandler(codeRunner_grpc.codeRunnerServicer):
    def __init__(self):
        self.num = 0
        self.log = {}

    def judge(self, codeRunnerRequest, context):
        # self.num += 1
        print("getCode----")
        language_ = codeRunnerRequest.language_
        if language_ == codeRunner.codeLanguage.Cpp:
            language_ = Language.Cpp
        elif language_ == codeRunner.codeLanguage.Java:
            language_ = Language.Java 
        code_ = codeRunnerRequest.code_
        input_ = codeRunnerRequest.input_
        (type_, result_) = runner(language_, code_, input_,  "./workplace/Main")
        res = codeRunner.codeRunnerRespone()
        if type_ is Type.Sucess:
            res.type_ = codeRunner.resultType.Sucess
        elif type_ is Type.Sucess:
            res.type_ = codeRunner.resultType.Runtime_Error
        elif type_ is Type.Runtime_Error:
            res.type_ = codeRunner.resultType.Runtime_Error
        elif type_ is Type.Time_Limit_Exceeded:
            res.type_ = codeRunner.resultType.Time_Limit_Exceeded
        elif type_ is Type.Memory_Limit_Exceeded:
            res.type_ = codeRunner.resultType.Memory_Limit_Exceeded
        else:
            res.type_ = codeRunner.resultType.System_Error
        res.result_ = result_
        return res

if __name__=="__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    codeRunner_grpc.add_codeRunnerServicer_to_server(
        codeRunnerHandler(), server)
    server.add_insecure_port('[::]:8233')
    server.start()
    print("Starting python server...")
    server.wait_for_termination()
