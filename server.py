import sys
sys.path.append('./gen-py')

import json
from codeRunner import codeRunner
from codeRunner.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from utils import runner
import socket
from config import Language, Type


class codeRunnerHandler:
    def __init__(self):
        self.num = 0
        self.log = {}

    def judge(self, codeRunnerRequest):
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
    processor = codeRunner.Processor(handler)
    #transport = TSocket.TServerSocket('172.16.0.4', 8233)
    transport = TSocket.TServerSocket('0.0.0.0', 8233)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting python server...")
    server.serve()
