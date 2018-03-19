# -*- coding: utf-8 -*-
__author__ = 'CQ'


class FlyweightBase(object):
    _instances = dict()

    def __init__(self, *args, **kwargs):
        # 继承的子类必须初始化
        raise NotImplementedError

    def __new__(cls, *args, **kwargs):
        # print(cls._instances,type(cls))
        return cls._instances.setdefault(
            (cls, args, tuple(kwargs.items())),
            super(FlyweightBase, cls).__new__(cls)
        )
        # setdefault返回父类的new方法，当实例化的类是同一类，并且传递的参数一样时，则返回以前半实例化的new方法对象（内存中已经存在）
        # 将触发BoardShoes子类或Sneaker子类的构造方法

    def display(self):
        raise NotImplementedError


class BoardShoes(FlyweightBase):
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand

    def display(self):
        print("This pair of %s-yard board shoes is %s" % (self.size, self.brand))


class Sneaker(FlyweightBase):
    def __init__(self, size, brand):
        self.size = size
        self.brand = brand

    def display(self):
        print("This pair of %s-yard sneakers is %s" % (self.size, self.brand))


def main():
    shoes1 = BoardShoes(40, "Nike")
    shoes2 = BoardShoes(40, "Nike")
    shoes3 = Sneaker(40, "Adidas")

    shoes1.display()
    print(">>id:", id(shoes1), "\n")

    shoes2.display()
    print(">>id:", id(shoes2), "\n")

    shoes3.display()
    print(">>id:", id(shoes3), "\n")


if "__main__" == __name__:
    main()
