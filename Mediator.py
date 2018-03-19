# -*- coding: utf-8 -*-
__author__ = 'CQ'


'''
本例子使用博物馆通过门禁案例，描述仲裁者模式
工作人员想要进入博物馆首先要在大门口刷门禁卡才能进入，
其次想要进入楼宇内要在一楼门禁刷门禁卡，但是，必须再刷过大门口的门禁后，该门禁才能刷卡通过。
而后进入各个楼层的藏物展览厅内，要在展览厅门口刷门禁，但是，前提是大门口门禁刷过并且楼宇门禁也刷过，该门禁才能刷卡通过
可见个个门禁间有依赖关系，前一个门禁影响后一个门禁，如果我们在门禁间单独创建关联函数，至少要维护n-1个关系
现在门禁数量只有3个，如果以后要扩展呢？n-1个关联函数都必须要重写，是不是很麻烦？

这个时候引用仲裁者模式尤为重要！
'''


class Mediator(object):
    '''
    仲裁者抽象类
    '''
    def addColleagues(self, colleague):
        raise NotImplementedError

    def colleagueChange(self, colleague):
        raise NotImplementedError


class Colleague(object):
    '''
    组员抽象类
    '''
    def setMediator(self, mediator):
        raise NotImplementedError

    def setColleagueAllowable(self, boolean):
        raise NotImplementedError


class ColleagueGate(Colleague):
    '''
    组员：大门
    '''
    def __init__(self, mediator=None):
        self.mediator = mediator
        self.allowable = False

    def setMediator(self, mediator):
        self.mediator = mediator

    def setColleagueAllowable(self, boolean):
        self.allowable = boolean
        self.mediator.colleagueChange(self)
        return self.mediator.permit(self)


class ColleagueEntrance(Colleague):
    '''
    组员：楼宇门
    '''
    def __init__(self, mediator=None):
        self.mediator = mediator
        self.allowable = False

    def setMediator(self, mediator):
        self.mediator = mediator

    def setColleagueAllowable(self, boolean):
        self.allowable = boolean
        self.mediator.colleagueChange(self)
        return self.mediator.permit(self)


class ColleagueDoor(Colleague):
    '''
    组员：展览厅门
    '''
    def __init__(self, mediator=None):
        self.mediator = mediator
        self.allowable = False

    def setMediator(self, mediator):
        self.mediator = mediator

    def setColleagueAllowable(self, boolean):
        self.allowable = boolean
        self.mediator.colleagueChange(self)
        return self.mediator.permit(self)


class MediatorEntrance(Mediator):
    '''
    仲裁者类
    '''
    def __init__(self):
        self.allows = {}

    def addColleagues(self, colleague):
        colleague.setMediator(self)
        self.allows[colleague.__class__] = [len(self.allows) + 1]
        self.allows[colleague.__class__].append(False)

    def colleagueChange(self, colleague):
        '''
        接收组员的变化信息，并处理
        :param colleague:
        :return:
        '''
        '''
        :param colleague:
        :return:
        '''
        self.allows[colleague.__class__][1] = colleague.allowable

    def permit(self, colleague):
        '''
        反馈给组员信息
        :param colleague:
        :return: True or False
        '''
        per = True
        for k in self.allows.values():
            if k[0] < self.allows[colleague.__class__][0]:
                if not k[1]:
                    per = False
        return per

    def restore(self):
        for i in self.allows.values():
            i[1] = False


def main():
    med = MediatorEntrance()

    gate = ColleagueGate()
    entrance = ColleagueEntrance()
    door = ColleagueDoor()

    med.addColleagues(gate)
    med.addColleagues(entrance)
    med.addColleagues(door)

    print("工作者进入大门")
    print("\033[32;1m>>", gate.setColleagueAllowable(True), "\033[0m")

    print("工作者进入楼宇门")
    print("\033[32;1m>>", entrance.setColleagueAllowable(True), "\033[0m")

    print("工作者进入展览厅门")
    print("\033[32;1m>>", door.setColleagueAllowable(True), "\033[0m")

    # 还原门禁
    med.restore()

    print("偷窃者翻过围墙进入庭院")
    print("偷窃者使用偷来的门禁刷楼宇门")
    print("\033[31;1m>>", entrance.setColleagueAllowable(True), "\033[0m")

    # 还原门禁
    med.restore()

    print("偷窃者翻过围墙进入庭院")
    print("偷窃者爬入楼宇进入楼层走道")
    print("偷窃者使用偷来的门禁刷楼宇门")
    print("\033[31;1m>>", entrance.setColleagueAllowable(True), "\033[0m")


if "__main__" == __name__:
    main()
