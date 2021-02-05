import sys
sys.path.append('./proto')

from concurrent import futures
from utils import runner
from config import Language
import grpc
import codeRunner_pb2 as codeRunner
import codeRunner_pb2_grpc as codeRunner_grpc
class codeRunnerHandler(codeRunner_grpc.codeRunnerServicer):
    def __init__(self):
        self.num = 0
        self.log = {}

    def judge(self, codeRunnerRequest, context):
        # self.num += 1
        language_ = codeRunnerRequest.language_

        if language_ == codeLanguage.Cpp:
            language_ = Language.Cpp
        elif language_ == codeLanguage.Java:
            language_ = Language.Java 
        code_ = codeRunnerRequest.code_
        input_ = codeRunnerRequest.input_
        res = codeRunnerRespone()
        (type_, res.result_) = runner(language_, code_, input_,  "test")
        res.type_ = resultType._NAMES_TO_VALUES[type_.name]
        return res

if __name__=="__main__":
    handler = codeRunnerHandler()
    server = grpc.Server(futures.ThreadPoolExecutor(max_workers=10))
    codeRunner_pb2_grpc.add_codeRunnerServicer_to_server(
        codeRunnerHandler(), server)
    server.add_insecure_port('[::]8233')
    server.start()
    print("Starting python server...")
    server.wait_for_termination()
