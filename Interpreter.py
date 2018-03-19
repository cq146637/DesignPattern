# -*- coding: utf-8 -*-
__author__ = 'CQ'

'''
通过编写一段迷你程序的解释器实现解释器模式
以下是命令解释：
<program> ::= program <command list>
    <program>是程序定义字符
    program关键字后面跟着的命令列表<command list>
    ::= 的左边表示定义的名字，右边表示定义的内容

<command list> ::= <command>* end
    <command list>是指重复0次以上<command>后，接着一个end关键字
    '*'表示前面的内容循环0次以上

<command> ::= <repeat command> | <primitive command>
    <command>是指<repeat command>或<primitive command>

<repeat command> ::= repeat <number><command list>
    <repeat command>是指repeat关键字后面跟着循环次数和循环命令列表
    <command>中可以出现<command list>，反之也可以出现，这称为递归定义

<primitive command>
    它指go或right或left

<number>
    即重复次数，自然数
'''
import sys
import re


class Node(object):
    '''
    表示语法树“节点”的类
    '''
    def parse(self, context):
        raise NotImplementedError


class ProgramNode(Node):
    '''
    对应处理<program>的类
    '''
    def __init__(self):
        self.commandListNode = None

    def parse(self, context):
        context.skipToken("program")
        self.commandListNode = CommandListNode()
        self.commandListNode.parse(context)

    def __str__(self):
        return "[ program "+self.commandListNode.__str__()+"]"


class CommandListNode(Node):
    '''
    对应处理<command list>的类
    '''
    def __init__(self):
        self.list1 = []

    def parse(self, context):
        while True:
            if context.currentToken() == None:
                print("Missing 'end'")
                sys.exit(0)
            elif context.currentToken() == "end":
                context.skipToken("end")
                break
            else:
                commandNode = CommandNode()
                commandNode.parse(context)
                self.list1.append(commandNode)

    def __str__(self):
        string = ""
        for node in self.list1:
            string += node.node.__str__()
        return string


class CommandNode(Node):
    '''
    对应处理<command>的类
    '''
    def __init__(self):
        self.node = None

    def parse(self, context):
        if context.currentToken() == "repeat":
            self.node = RepeatCommandNode()
            self.node.parse(context)
        else:
            self.node = PrimitiveCommandNode()
            self.node.parse(context)

    def __str__(self):
        return self.node


class RepeatCommandNode(Node):
    '''
    对应处理<repeat command>的类
    '''
    def __init__(self):
        self.number = None
        self.commandListNode = None

    def parse(self, context):
        context.skipToken("repeat")
        self.number = context.currentNumber()
        context.nextToken()
        self.commandListNode = CommandListNode()
        self.commandListNode.parse(context)

    def __str__(self):
        return "[ repeat "+str(self.number)+" "+self.commandListNode.__str__()+"] "


class PrimitiveCommandNode(Node):
    '''
    对应处理<primitive command>的类
    '''
    def __init__(self):
        self.name = None

    def parse(self, context):
        self.name = context.currentToken()
        context.skipToken(self.name)
        if self.name != "go" and self.name != "right" and self.name != "left":
            print(self.name, "is undefined")

    def __str__(self):
        return self.name+" "


class Context(object):
    def __init__(self, text, index=0):
        self.__currentToken = None      # 存放当前命令名例：program
        self.__tokenizer = text         # 存放整条迷你命令例：program end
        self.index = index              # 当前获取到第几条命令例:program end 如果当前获取到end，则index=2
        self.nextToken()

    def nextToken(self):
        if self.hasMoreToken(self.__tokenizer):
            self.__currentToken = self.getNextToken(self.__tokenizer)
        else:
            self.__currentToken = None
        return self.__currentToken

    def hasMoreToken(self, tokenizer):
        res = False
        find_list = re.findall("(\w*?\s)", tokenizer)
        if self.index < len(find_list):
            res = True
        return res

    def getNextToken(self, tokenizer):
        find_list = re.findall("(\w*?\s)", tokenizer)
        res = find_list[self.index]
        temp = list(res)
        res = "".join(temp[0:-1])
        self.index += 1
        return res

    def currentToken(self):
        return self.__currentToken

    def skipToken(self, token):
        if token != self.__currentToken:
            print("Warning: "+token+" is expected,but ", self.__currentToken, " is found.")
            sys.exit(0)
        self.nextToken()

    def currentNumber(self):
        number = 0
        try:
            number = int(self.__currentToken)
        except Exception as e:
            print("Warning: ", e)
        return number


def main():
    file = open("program.txt", 'r')
    for i in file.readlines():
        print("text = ", i)
        node = ProgramNode()
        node.parse(Context(i))
        print("node =", node)
        print("--------------------")
    file.close()


if '__main__' == __name__:
    main()
