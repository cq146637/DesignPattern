# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Shape(object):
    def draw(self):
        # 该方法如果没有被重写将会弹出异常
        raise NotImplementedError


class Circle(Shape):
    def draw(self):
        print("draw circle...")


class Square(Shape):
    def draw(self):
        print("draw square...")


class ShapeFactory(object):
    def create(self, shape):
        if shape == "circle":
            return Circle()
        elif shape == "square":
            return Square()
        else:
            return None


def main():
    fac = ShapeFactory()
    obj = fac.create("square")
    obj.draw()


if "__main__" == __name__:
    main()
