# -*- coding: utf-8 -*-
__author__ = 'CQ'
import random


class Memento(object):
    '''
    游戏角色存档类
    '''
    def __init__(self, money, killed, hp, gnum):
        self.money = money
        self.killed = killed
        self.hp = hp
        self.gnum = gnum

    def changeKilled(self, count):
        self.killed = count

    def changeHP(self, count):
        self.hp = count

    def changeMoney(self, count):
        self.money = count

    def changeGameNum(self, count):
        self.gnum = count

class Gamer(object):
    '''
    游戏角色类
    '''
    def __init__(self, money, killed=0, hp=100, gnum=1):
        self.__money = money
        self.__killed = killed
        self.__hp = hp
        self.__gnum = gnum
        self.__memento = []

    def getMoney(self):
        return self.__money

    def getKilled(self):
        return self.__killed

    def getHP(self):
        return self.__hp

    def getGameNum(self):
        return self.__gnum

    def through(self):
        self.__gnum += 1
        money = random.randint(10, 100)
        killed = random.randint(20, 50)
        print("\033[32;1m通过关卡，金钱+%s\033[0m" % money)
        self.__money += money
        print("\033[32;1m通过关卡,消灭敌人%s\033[0m" % killed)
        self.__killed += killed

    def lossHP(self):
        _hp = random.randint(0, 20)
        print("损失生命值:%s" % _hp)
        self.__hp -= _hp
        self.isDie()

    def isDie(self):
        if self.__hp <= 0:
            self.gameOver()
        else:
            self.through()

    def gameOver(self):
        print("\033[31;1m人物死亡，通关失败\033[0m")
        self.__hp = 0

    def startGame(self):
        if self.__hp == 0:
            print("游戏角色死亡，请重新开始游戏或者读取存档")
            self.restoreMemento()
            return
        else:
            res = random.randint(0, 10)
            if res <= 2:
                self.gameOver()
            else:
                self.lossHP()

    def createMemento(self):
        self.__memento.append(Memento(self.__money, self.__killed, self.__hp, self.__gnum))

    def restoreMemento(self):
        print("读取存档...")
        self.__money = self.__memento[-1].money
        self.__killed = self.__memento[-1].killed
        self.__hp = self.__memento[-1].hp
        self.__gnum = self.__memento[-1].gnum

    def __str__(self):
        return "[游戏角色] 金钱数:%s 消灭敌人数:%s 已通过关卡:%s 当前血量:%s" % (self.__money, self.__killed, self.__gnum, self.__hp)


def main():
    print("创建游戏角色")
    role = Gamer(0)
    print("存档中...")
    m_list = []
    m_list.append(role.createMemento())
    print("开始游戏")
    for i in range(5):
        role.startGame()
        print(role)
        print("**************************************")


if '__main__' == __name__:
    main()
