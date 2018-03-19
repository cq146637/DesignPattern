# -*- coding: utf-8 -*-
__author__ = 'CQ'
from copy import copy, deepcopy


class Model(object):
    def __init__(self, mid):
        self.id = mid

    def display(self):
        raise NotImplementedError

    def clone(self):
        raise NotImplementedError

    def deepClone(self):
        raise NotImplementedError


class Materials(object):
    def __init__(self, name):
        self.name = name


class Teapot(Model):
    def __init__(self, name, mid, materials="塑料"):
        self.name = name
        self.materials = Materials(materials)
        super(Teapot, self).__init__(mid)

    def display(self):
        print(">> name:%s  id:%s  materials:%s" % (self.name, self.id, self.materials.name))

    def clone(self):
        return copy(self)

    def deepClone(self):
        return deepcopy(self)


class Manager(object):
    def __init__(self):
        self.dicts = {}

    def register(self, name, model):
        self.dicts[name] = model

    def create(self, model_name):
        return self.dicts[model_name].clone()

    def deepCreate(self, model_name):
        return self.dicts[model_name].deepClone()


def main():
    manager = Manager()
    blue = Teapot("blue model", "001")
    red = Teapot("red model", "002")
    white = Teapot("white model", "003")

    manager.register(blue.name, blue)
    manager.register(red.name, red)
    manager.register(white.name, white)

    blue_teapot = manager.create("blue model")
    blue_teapot.name = "blue rosewood teapot"

    blue2_teapot = manager.deepCreate("blue model")
    blue2_teapot.name = "blue stainless steel teapot"

    blue_teapot.materials.name = "花梨木"
    blue2_teapot.materials.name = "不锈钢"

    blue.display()
    blue_teapot.display()
    blue2_teapot.display()


if '__main__' == __name__:
    main()
