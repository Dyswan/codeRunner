import sys
sys.path.append('./gen-py')
import json 
from codeRunner import codeRunner
from codeRunner.ttypes import *
from codeRunner.constants import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


transport = TSocket.TSocket('127.0.0.1', 8000)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = codeRunner.Client(protocol)
# Connect!
transport.open()

Input = ""
code='''#include <iostream>
using namespace std;
int main(){
    printf("hello world\\n");
}
    '''

req = codeRunnerRequest(language_ = codeLanguage.Cpp, code_= code, input_= "")
# print(req)
res = client.judge(req)
print(res.result_)
transport.close()