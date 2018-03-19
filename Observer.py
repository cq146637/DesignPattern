# -*- coding: utf-8 -*-
__author__ = 'CQ'


class ObserverBase(object):
    '''被观察对象基类'''

    def __init__(self):
        self._observerd_list = []

    def attach(self, observe_subject):
        '''
        添加观察者
        :param observe_subject:
        :return:
        '''
        if observe_subject not in self._observerd_list:
            self._observerd_list.append(observe_subject)
            print("[%s]已经将[%s]加入观察队列..." % (self.name, observe_subject.name))

    def detach(self,observe_subject):
        '''
        解除观察关系
        :param observe_subject:
        :return:
        '''
        try:
            self._observerd_list.remove(observe_subject)
            print("不再观察[%s]" % observe_subject)
        except ValueError:
            pass

    def notify(self):
        '''
        通知所有观察者
        :return:
        '''
        for objserver in self._observerd_list:
            objserver.update(self)


class Observer(ObserverBase):
    '''被观察者类'''

    def __init__(self, name):
        super(Observer, self).__init__()
        self.name = name
        self._msg = ''

    @property
    def msg(self):
        '''
        当前状况
        :return:
        '''
        return self._msg

    @msg.setter
    def msg(self,content):
        self._msg = content
        self.notify()


class GCDViewer(object):
    def __init__(self, name="共军观察者"):
        self.name = name

    def update(self, observer_subject):
        print("共军:收到[%s]消息[%s] "%(observer_subject.name,observer_subject.msg))


class GMDViewer(object):
    def __init__(self, name="国军观察者"):
        self.name = name

    def update(self, observer_subject):
        print("国军:收到[%s]消息[%s] " % (observer_subject.name,observer_subject.msg))


def main():
    observer1 = Observer("共军放哨者")
    observer2 = Observer("国军放哨者")

    gongjun1 = GCDViewer()
    guojun1 = GMDViewer()

    observer1.attach(gongjun1)
    observer1.attach(guojun1)

    observer2.attach(guojun1)

    observer1.msg = "\033[32;1m敌人来了...\033[0m"

    observer2.msg = "\033[31;1m前方发现敌人,请紧急撤离,不要告诉共军\033[0m"


if __name__ == "__main__":
    main()
