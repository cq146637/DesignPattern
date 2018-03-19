# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Aggregate(object):
    '''
    表示集合的接口
    '''
    def iterator(self):
        raise NotImplementedError


class Iterator(object):
    '''
    遍历集合的接口
    '''
    def hasNext(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError


class Book(object):
    '''
    表示书的类
    '''
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class BookShelf(Aggregate):
    '''
    表示书架的类，用于存放书
    '''
    def __init__(self, max_size):
        self.max = max_size
        self.books = [None for i in range(self.max)]
        self.last = 0

    def getBookAt(self, index):
        return self.books[index]

    def appendBook(self, book):
        self.books[self.last] = book
        self.last += 1

    def getLength(self):
        return self.last

    def iterator(self):
        return BookShelfIterator(self)


class BookShelfIterator(Iterator):
    '''
    遍历书架的类
    '''
    def __init__(self, bookShelf):
        self.__bookShelf = bookShelf
        self.__index = 0

    def hasNext(self):
        if self.__index < self.__bookShelf.getLength():
            return True
        else:
            return False

    def next(self):
        book = self.__bookShelf.getBookAt(self.__index)
        self.__index += 1
        return book


def main():
    # 实例化一个书架，大小为10本书
    bookShelf = BookShelf(10)
    bookShelf.appendBook(Book("《C语言从研发到脱发》"))
    bookShelf.appendBook(Book("《C++从入门到放弃》"))
    bookShelf.appendBook(Book("《Java从跨平台到跨行业》"))
    bookShelf.appendBook(Book("《Ios开发从入门到下架》"))
    bookShelf.appendBook(Book("《Android开发大全--从开始到转行》"))
    bookShelf.appendBook(Book("《PHP由初学至搬砖》"))
    bookShelf.appendBook(Book("《黑客攻防:从入门到入狱》"))
    bookShelf.appendBook(Book("《MySql从删库到跑路》"))
    bookShelf.appendBook(Book("《服务器运维管理从网络异常到硬盘全红》"))
    bookShelf.appendBook(Book("《服务器运维管理从网维到网管》"))
    it = bookShelf.iterator()
    while it.hasNext():
        book = it.next()
        print(book.getName())


if '__main__' == __name__:
    main()
