import _judger
import os
from config import Language, Type

def compileCPP(id,code,judgername):
    file = open("%s.cpp" % judgername, "w",encoding='utf-8')
    file.write(code)
    file.close()
    result = os.system("timeout 10 g++ %s.cpp -fmax-errors=3 -o %s.out -O2 -std=c++14 2>%sce.txt" %(judgername, judgername, judgername))
    if result:
        try:
            filece = open("%sce.txt" % judgername, "r")
            msg = str(filece.read())
            if msg == "": msg = "Compile timeout! Maybe you define too big arrays!"
            filece.close()
        except:
            msg = str("Fatal Compile error!")
        return False
    return True

def compileJava(id,code,judgername):
    file = open("Main.java", "w",encoding='utf-8')
    file.write(code)
    file.close()

    isExists = os.path.exists(judgername)
    if not isExists:
        os.makedirs(judgername)

    result = os.system("javac Main.java -d %s 2>%sce.txt" % (judgername, judgername))

    if result:
        try:
            filece = open("%sce.txt" % judgername, "r")
            msg = str(filece.read())
            filece.close()
        except:
            msg = str("Fatal Compile error!")
        return False
    return True

def judgeCPP(timelimit, memorylimit, inputpath, outputpath, errorpath, judgername):
    return _judger.run(max_cpu_time=_judger.UNLIMITED,
                        max_real_time=_judger.UNLIMITED,
                        max_memory=_judger.UNLIMITED,
                        max_process_number=_judger.UNLIMITED,
                        max_output_size=_judger.UNLIMITED,
                        max_stack=_judger.UNLIMITED,
                        # five args above can be _judger.UNLIMITED
                        exe_path=judgername+".out",
                        input_path=inputpath,
                        output_path=outputpath,
                        error_path=errorpath,
                        args=[],
                        # can be empty list
                        env=[],
                        log_path=judgername+"judger.log",
                        # can be None
                        seccomp_rule_name="general",
                        uid=0,
                        gid=0
                        )

def judgeJava(timelimit, memorylimit, inputpath, outputpath, errorpath, judgername):
    return _judger.run(max_cpu_time=timelimit,
                        max_real_time=timelimit*10,
                        max_memory=memorylimit * 1024 * 1024,
                        max_process_number=10,
                        max_output_size=32 * 1024 * 1024,
                        max_stack=32 * 1024 * 1024,
                        # five args above can be _judger.UNLIMITED
                        exe_path="/usr/bin/java",
                        input_path=inputpath,
                        output_path=outputpath,
                        error_path=errorpath,
                        args=["-cp",judgername,"-Djava.security.policy==policy","-Djava.awt.headless=true","Main"],
                        # can be empty list
                        env=[],
                        log_path=judgername+"judger.log",
                        # can be None
                        seccomp_rule_name=None,
                        memory_limit_check_only=1,
                        uid=0,
                        gid=0
                        )

def runner(lang, code, Input, judgername):
    ret = []
    timelimit = 10000
    memorylimit = 512
    if lang == Language.Cpp: 
        if compileCPP(id,code,judgername) == False:
            filece = open("%sce.txt" % judgername, "r")
            msg = str(filece.read())
            filece.close()
            return (Type.Compile_Error, msg)
    elif lang == Language.Java: 
        if compileJava(id,code,judgername) == False: 
            filece = open("%sce.txt" % judgername, "r")
            msg = str(filece.read())
            filece.close()
            return (Type.Compile_Error, msg)
    else:
        return (Type.Compile_Error, "language is not support")
    
    file = open("%s.in"%judgername, "w",encoding='utf-8')
    file.write(Input)
    file.close()

    if lang == Language.Cpp: 
        ret = judgeCPP(timelimit, memorylimit, "./%s.in" %judgername, judgername+"temp.out", judgername+"error.out", judgername)
    elif lang == Language.Java: 
        ret = judgeJava(timelimit*3, memorylimit, "./%s.in"%judgername, judgername+"temp.out", judgername+"error.out", judgername)

    if ret["result"] == 2 or ret["result"] == 1:
        return (Type.Time_Limit_Exceeded, "")
    elif ret["result"] == 3:
        return (Type.Memory_Limit_Exceeded, "")
    elif ret["result"] == 4:
        return (Type.Runtime_Error, "")
    elif ret["result"] == 5:
        return (Type.System_Error, "")
    else:
        fileout = open(judgername+"temp.out", "r")
        msg = str(fileout.read())
        return (Type.Sucess, msg)
    return msg



if __name__ == "__main__":
    code='''#include <iostream>
using namespace std;
int main(){
    //while(1){
    cout<<"1"<<endl;
    //}
}
    '''
    print(code)
    print(runner(Language.Cpp, code, "","./workplace/test"))
            