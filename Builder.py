# -*- coding: utf-8 -*-
__author__ = 'CQ'


class AnimalBuilder(object):
    def __init__(self, name, category=""):
        self.name = name
        self.category = category

    def buildHead(self):
        raise NotImplementedError

    def buildBody(self):
        raise NotImplementedError

    def buildLimb(self):
        raise NotImplementedError

    def getInfo(self):
        raise NotImplementedError


class Bird(AnimalBuilder):
    def __init__(self, name):
        super(Bird, self).__init__(name)

    def buildHead(self):
        print("创造了鸟的头部")

    def buildBody(self):
        print("创造了鸟的身体")

    def buildLimb(self):
        print("创造了鸟的四肢")

    def getInfo(self):
        print("这只鸟是一只%s" % self.name)


class Fox(AnimalBuilder):
    def __init__(self, name):
        super(Fox, self).__init__(name)

    def buildHead(self):
        print("创造了狐狸的头部")

    def buildBody(self):
        print("创造了狐狸的身体")

    def buildLimb(self):
        print("创造了狐狸的四肢")

    def getInfo(self):
        print("这只狐狸是一只%s" % self.name)


class AnimalDirector(object):
    def __init__(self, animal):
        self.__animal = animal

    def createAniaml(self):
        self.__animal.buildHead()
        self.__animal.buildBody()
        self.__animal.buildLimb()

    def setAnimal(self, animal):
        self.__animal = animal


def main():
    bird = Bird("猫头鹰")
    director = AnimalDirector(bird)
    director.createAniaml()
    bird.getInfo()

    fox = Fox("北极狐")
    director.setAnimal(fox)
    director.createAniaml()
    fox.getInfo()


if "__main__" == __name__:
    main()
