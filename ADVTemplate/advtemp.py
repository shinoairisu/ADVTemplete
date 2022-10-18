# -*- coding: UTF-8 -*-
import json

__loadmode = False  #是否是load模式
__datas = {}
__history = []
__value = {
}  #set get都是这里的数据。如果使用call，将此处数据复制给__datas["values"]保存。用jump就不管。load时将__datas["values"]复制到此处
__datas["jump"] = []  #jump栈
__datas["base"] = "main"  #起始点
__datas["regs"] = {}  #注册函数栈 就是所谓的标签
__datas["tag"] = 0  #load标签，遇到save和jump+1，遇到call变回0
__datas["values"] = {}  #全局变量 不用这个就无法获取变量
__datas["nextFunc"] = None  #call调用后会改变这里
__datas["callparam"] = {}  #call使用的parameter存在这里
__datas["char"] = ""  #上一个说话的人
__datas["option"] = []  #每次的选择栈


def jump(stageName: str, to: str, parameters: dict = {}):
    """
    跳跃到另一个函数
    stageName是本场景的名字,也就是本场景的 parameters["name"]
    """
    __datas["tag"] += 1
    parameters["name"] = to
    __datas["jump"].append(stageName)
    __datas["regs"][str](parameters)
    return 66156


def jumpResult(jumptag, parameters):
    """
    jump函数的返回值,必须在jump后面调用。不在jump后调用会出错。
    """
    if jumptag != 66156:
        raise Exception("You can't use this function not after jump")
    if __datas["nextFunc"] != None:  #如果下一层有call，就需要此处进行一次处理
        nextf = __datas["nextFunc"]
        __datas["nextFunc"] = None
        __datas["regs"][nextf](parameters)
    if parameters["name"] != __datas["jump"][-1]:
        return True


def call(stageName: str, to: str, parameters: dict = {}):
    """
    清理调用栈到另一个函数
    stageName是本场景的名字,也就是本场景的 parameters["name"]
    """
    __datas["jump"].clear()
    __datas["tag"] += 0
    __datas["base"] = stageName
    __datas["nextFunc"] = to


def os(speak: str):  #旁白
    """
    旁白
    """
    if __loadmode == True:
        return
    __history.append({"O.S.": speak})
    print("O.S. : ", speak)


def chara(speak: str, charName: str = None):
    """
    人物说话
    """
    if __loadmode == True:
        return
    if charName == None:
        charName = __datas["char"]
    else:
        __datas["char"] = charName
    __history.append({charName: speak})
    print(f"{charName} : ", speak)


def getValue(name):
    return __value[name]


def setValue(name, value):
    __value[name] = value


def wait(name):
    input("")


def gethistory():
    return __history.copy()


def ignore():
    pass