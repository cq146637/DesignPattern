# -*- coding: utf-8 -*-
__author__ = 'CQ'


class AbstractCollege(object):
    def __init__(self, name, major=None):
        self.name = name
        self.major = major

    def start(self):
        raise NotImplementedError


class ComputerCollege(AbstractCollege):
    def __init__(self, name="计算机学院", major=None):
        super(ComputerCollege, self).__init__(name, major)

    def start(self):
        print("\n%s的" % self.name)
        self.major.start()


class ArtCollege(AbstractCollege):
    def __init__(self, name="艺术学院", major=None):
        super(ArtCollege, self).__init__(name, major)

    def start(self):
        print("\n%s的" % self.name)
        self.major.start()


class AbstractMajor(object):
    def __init__(self, name, course=None):
        self.name = name
        self.course = course

    def start(self):
        raise NotImplementedError


class NetworkMajor(AbstractMajor):
    def __init__(self, name="网络专业", course=None):
        super(NetworkMajor, self).__init__(name, course)

    def start(self):
        print("%s的" % self.name)
        self.course.start()


class PerformMajor(AbstractMajor):
    def __init__(self, name="表演专业", course=None):
        super(PerformMajor, self).__init__(name, course)

    def start(self):
        print("%s的" % self.name)
        self.course.start()


class AbstractCourse(object):
    def __init__(self, name):
        self.name = name

    def start(self):
        raise NotImplementedError


class PythonCourse(AbstractCourse):
    def __init__(self, name="Python编程"):
        super(PythonCourse, self).__init__(name)

    def start(self):
        print("%s 课程开始了" % self.name)


class TheoryOfPerformanceCourse(AbstractCourse):
    def __init__(self, name="表演理论"):
        super(TheoryOfPerformanceCourse, self).__init__(name)

    def start(self):
        print("%s 课程开始了" % self.name)


def main():
    # 三个维度的事物以组合的方式结合在一起，互不影响，互相调用
    coll1 = ComputerCollege()
    coll2 = ArtCollege()

    maj1 = NetworkMajor()
    maj2 = PerformMajor()

    cour1 = TheoryOfPerformanceCourse()
    cour2 = PythonCourse()

    coll1.major = maj1
    coll2.major = maj2

    maj1.course = cour1
    maj2.course = cour2

    coll1.start()
    coll2.start()


if "__main__" == __name__:
    main()
