# -*- coding: utf-8 -*-
__author__ = 'CQ'


class AbstractDevice(object):
    def powerOn(self):
        raise NotImplementedError

    def knobDown(self):
        raise NotImplementedError

    def startingUp(self):
        raise NotImplementedError


class Servers(AbstractDevice):
    def powerOn(self):
        print("插上服务器电源线")

    def knobDown(self):
        print("按下服务器开机按钮")

    def startingUp(self):
        self.powerOn()
        self.knobDown()


class Computer(AbstractDevice):
    def powerOn(self):
        print("插上电脑电源线")

    def knobDown(self):
        print("按下电脑开机按钮")

    def startingUp(self):
        self.powerOn()
        self.knobDown()


def main():
    s = Servers()
    c = Computer()

    s.startingUp()
    c.startingUp()


if "__main__" == __name__:
    main()