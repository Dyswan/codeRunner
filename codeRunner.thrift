enum codeLanguage{
    Cpp = 0
    Java = 1
}
enum resultType{
    Sucess = 0
    Compile_Error = 1
    Runtime_Error = 2
    Time_Limit_Exceeded = 3
    Memory_Limit_Exceeded = 4
    System_Error = 5
}
struct codeRunnerRequest{
    1: codeLanguage language_, 
    2: string code_, 
    3: string input_
}
struct codeRunnerRespone{
    1:resultType type_,
    2:string result_
}
service codeRunner{
    codeRunnerRespone judge(1:codeRunnerRequest req)
}