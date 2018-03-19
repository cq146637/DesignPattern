# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Singleton(object):
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def main():
    person = Singleton("alex")
    person2 = Singleton("bob")

    print(person.name)
    print(person2.name)


if "__main__" == __name__:
    main()
