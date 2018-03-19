# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Person(object):
    def speak(self):
        raise NotImplementedError

    def write(self):
        raise NotImplementedError


class Native(Person):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("%s 在用中文说话" % self.name)

    def write(self):
        print("%s 在写中文" % self.name)


class Foreigners(object):
    def __init__(self, name):
        self.name = name

    def foreignerSpeak(self):
        print("%s 在说蹩脚的中文" % self.name)

    def foreignerWrite(self):
        print("%s 在写中文" % self.name)


class Translator(Person):
    def __init__(self, foreigner=None):
        self.foreigner = foreigner

    def speak(self):
        self.foreigner.foreignerSpeak()

    def write(self):
        self.foreigner.foreignerWrite()


def main():
    p1 = Native("wang wu")
    p2 = Foreigners("alex")
    trans = Translator(p2)

    p1.speak()
    trans.speak()

    p1.write()
    trans.write()


if "__main__" == __name__:
    main()
