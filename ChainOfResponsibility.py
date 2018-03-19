# -*- coding: utf-8 -*-
__author__ = 'CQ'


class BaseHandler(object):
    '''  处理基类  '''
    def successor(self, successor):
        # 与下一个责任者关联
        self._successor = successor


class RequestHandlerL1(BaseHandler):
    ''' 第一级请求处理者 '''
    name = "导员"

    def handle(self, request):
        if request < 2:
            print("审批者[%s],请假天数[%s],审批结果[审批通过]" % (self.name, request))
        else:
            print("\033[31;1m[%s]无权审批,交给下一个审批者\033[0m" %self.name)
            self._successor.handle(request)


class RequestHandlerL2(BaseHandler):
    '''第二级请求处理者'''
    name = "班主任"

    def handle(self, request):
        if request < 7:
            print("审批者[%s],请假天数[%s],审批结果[审批通过]" % (self.name, request))
        else:
            print("\033[31;1m[%s]无权审批,交给下一个审批者\033[0m" % self.name)
            self._successor.handle(request)


class RequestHandlerL3(BaseHandler):
    '''第三级请求处理者'''
    name = "教学院长"

    def handle(self, request):
        if request < 15:
            print("审批者[%s],请假天数[%s],审批结果[审批通过]" % (self.name, request))
        else:
            print("\033[31;1m[%s]无权审批,交给下一个审批者\033[0m" % self.name)
            self._successor.handle(request)


class RequestHandlerL4(BaseHandler):
    '''第四级请求处理者'''
    name = "校长"

    def handle(self, request):
        if request < 90:
            print("审批者[%s],请假天数[%s],审批结果[审批通过]" % (self.name, request))
        else:
            print("\033[31;1m[%s]请假天数太多了,不批\033[0m" % self.name)
            #self._successor.handle(request)


class RequestAPI(object):
    h1 = RequestHandlerL1()
    h2 = RequestHandlerL2()
    h3 = RequestHandlerL3()
    h4 = RequestHandlerL4()

    h1.successor(h2)
    h2.successor(h3)
    h3.successor(h4)

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def handle(self):
        # 出责任链最低级开始
        self.h1.handle(self.days)

    def setDays(self, days):
        self.days = days


def main():
    r1 = RequestAPI("老王", 1)
    r1.handle()
    print(r1.__dict__, "\n")

    r1.setDays(5)
    r1.handle()
    print(r1.__dict__, "\n")

    r1.setDays(10)
    r1.handle()
    print(r1.__dict__, "\n")

    r1.setDays(30)
    r1.handle()
    print(r1.__dict__, "\n")

    r1.setDays(100)
    r1.handle()
    print(r1.__dict__, "\n")


if "__main__" == __name__:
    main()
