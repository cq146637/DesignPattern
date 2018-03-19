# -*- coding: utf-8 -*-
__author__ = 'CQ'

'''
该实例以银行金库报警系统为例子
有一个金库，金库与警报中心相连，金库里有警铃和正常通话用的电话，金库里有时钟（监视当前时间）
金库只能在白天使用，白天使用金库的话，会在报警中心留下记录，晚上使用会向报警中心发送紧急事态通知
任何时候都可以使用警铃向报警中心发送紧急事态通知
任何时候都可以使用电话，白天使用会呼叫报警中心，晚上使用只能向报警中心留言
'''


class State(object):
    '''
    白天或晚上的状态抽象类
    '''
    def __new__(cls, *args, **kwargs):
        '''
        由于状态只有一种，不需要很多想用的状态，这里使用单例模式的方法
        只使用一个实例化对象
        '''
        if not hasattr(cls, '_instance'):
            cls._instance = super(State, cls).__new__(cls)
        return cls._instance

    def doClock(self, context, hour):
        raise NotImplementedError

    def doUse(self):
        raise NotImplementedError

    def doAlarm(self):
        raise NotImplementedError

    def doPhone(self):
        raise NotImplementedError


class DayState(State):
    '''
    状态：白天
    '''
    def doClock(self, context, hour):
        if hour < 9 or 17 <= hour:
            context.changeState(NightState())

    def doUse(self):
        print("\033[32;1m使用金库（白天）\033[0m")

    def doAlarm(self):
        print("\033[32;1m按下警铃（白天）\033[0m")

    def doPhone(self):
        print("\033[32;1m正常通话（白天）\033[0m")

    def __str__(self):
        return "[白天]"


class NightState(State):
    '''
    状态：晚上
    '''
    def doClock(self, context, hour):
        if 9 <= hour and hour < 17:
            context.changeState(DayState())

    def doUse(self):
        print("\033[31;1m紧急：晚上使用金库\033[0m")

    def doAlarm(self):
        print("\033[31;1m按下警铃（晚上）\033[0m")

    def doPhone(self):
        print("\033[31;1m晚上的通话录音\033[0m")

    def __str__(self):
        return "[晚上]"



class Context(object):
    '''
    负责管理状态和联系报警中心的接口
    '''
    def setClock(self, hour):
        raise NotImplementedError

    def changeState(self, state):
        raise NotImplementedError

    def callSecurityCenter(self, msg):
        raise NotImplementedError

    def recordLog(self, msg):
        raise NotImplementedError


class ContetApi(Context):
    '''
    实现Context接口
    '''
    def __init__(self):
        self.state = NightState()
        self.textScreen = []

    def setClock(self, hour):
        if hour < 10:
            print("现在的时间是", "0"+str(hour)+":00")
        else:
            print("现在的时间是", str(hour)+":00")
        self.state.doClock(self, hour)

    def changeState(self, state):
        print("从", self.state, "状态变为了", state, "状态。", sep="")
        self.state = state

    def callSecurityCenter(self, msg):
        self.textScreen.append("call！ "+msg+"\n")

    def recordLog(self, msg):
        self.textScreen.append("record ... "+msg+"\n")


def main():
    context = ContetApi()
    for hour in range(24):
        context.setClock(hour)
        if hour == 2 or hour == 23:
            print("-----------------------")
            context.state.doUse()
            context.callSecurityCenter("%sH 金库被抢了" % hour)
            context.state.doAlarm()
            context.callSecurityCenter("%sH 警报自动拉响" % hour)
            context.state.doPhone()
            context.recordLog('%sH 不好了金库被炸开了！呼叫支援' % hour)
            print("-----------------------")

        if hour == 12:
            print("-----------------------")
            context.state.doUse()
            context.callSecurityCenter("%sH 金库使用中" % hour)
            context.state.doAlarm()
            context.callSecurityCenter("%sH 警报被拉响" % hour)
            context.state.doPhone()
            context.recordLog('%sH 有人抢劫银行呼叫支援' % hour)
            print("-----------------------")

    print("今天的警报中心记录")
    print(context.textScreen)


if "__main__" == __name__:
    main()
