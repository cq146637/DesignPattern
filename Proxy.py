# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Printable(object):
    def setPrinterName(self, name):
        raise NotImplementedError

    def getPrinterName(self):
        raise NotImplementedError

    def print(self, string):
        raise NotImplementedError


class Printer(Printable):
    def __init__(self, name):
        self.name = name

    def setPrinterName(self, name):
        self.name = name

    def getPrinterName(self):
        return self.name

    def print(self, string):
        print("----------%s----------" % self.name)
        print(string)


class PrinterProxy(Printable):
    def __init__(self, name, printer=None):
        self.name = name
        self.real = printer

    def setPrinterName(self, name):
        if self.real is not None:
            self.real.setPrinterName(name)
        self.name = name

    def getPrinterName(self):
        return self.name

    def print(self, string):
        self.realize()
        self.real.print(string)

    def realize(self):
        if self.real is None:
            print("设置被代理人%s..." % self.name)
            self.real = Printer(self.name)


def main():
    p1 = Printer("Alice")
    p2 = PrinterProxy("Bob")

    # 使用打印机打印资料
    p1.print("打印资料中...\n")

    # 使用打印机代理打印资料,未指定被代理人，自动创建被代理人
    p2.print("打印代理打印资料中...\n")

    # 修改被代理人
    p2.setPrinterName("Seven")
    p2.print("打印代理继续打印资料中...\n")

    # 删除被代理人，自动创建被代理人
    p2.real = None
    p2.setPrinterName("Alex")
    p2.print("打印代理继续继续打印资料中...")


if "__main__" == __name__:
    main()
