from enum import Enum

class Language(Enum):
    Cpp = 0
    Java = 1

class Type(Enum):
    Sucess = 0
    Compile_Error = 1
    Runtime_Error = 2
    Time_Limit_Exceeded = 3
    Memory_Limit_Exceeded = 4
    System_Error = 5
