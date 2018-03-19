# -*- coding: utf-8 -*-
__author__ = 'CQ'


'''
该案例为字符串加上边框线条装饰，实现装饰器模式
'''


class Display(object):
    '''
    用于显示字符串的抽象类
    '''
    def getColumns(self):
        '''
        获取横向字符数
        :return:
        '''
        raise NotImplementedError

    def getRows(self):
        '''
        获取纵向行数
        :return:
        '''
        raise NotImplementedError

    def getRowText(self, row):
        '''
        获取第row行的字符串
        :return:
        '''
        raise NotImplementedError

    def show(self):
        for i in range(self.getRows()):
            print(self.getRowText(i))


class StringDisplay(Display):
    '''
    用于显示单行字符串的类
    '''
    def __init__(self, string):
        self.__string = string

    def getColumns(self):
        return len(self.__string)

    def getRows(self):
        return 1

    def getRowText(self, row):
        if row == 0:
            return self.__string
        else:
            return None


class Border(Display):
    '''
    用于显示装饰边框的抽象类
    '''
    def __init__(self, display):
        self.display = display


class SideBorder(Border):
    '''
    用于显示左右边框的类
    '''
    def __init__(self, display, ch):
        super(SideBorder, self).__init__(display)
        self.borderChar = ch

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return self.display.getRows()

    def getRowText(self, row):
        return self.borderChar + self.display.getRowText(row) + self.borderChar


class FullBorder(Border):
    '''
    用于显示上下左右边框的类
    '''
    def __init__(self, display):
        super(FullBorder, self).__init__(display)

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return 1 + self.display.getRows() + 1

    def getRowText(self, row):
        if row == 0:
            return "+" + self.makeLine('-', self.display.getColumns()) + "+"
        elif row == self.display.getRows() + 1:
            return "+" + self.makeLine('-', self.display.getColumns()) + "+"
        else:
            return "|" + self.display.getRowText(row - 1) + "|"

    def makeLine(self, ch, count):
        string = ""
        for i in range(count):
            string += ch
        return string


def main():
    b1 = StringDisplay("Hello world!")
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)

    b1.show()
    print('=====================================')
    b2.show()
    print('=====================================')
    b3.show()
    print('=====================================')

    b4 = SideBorder(FullBorder(FullBorder(SideBorder(FullBorder(StringDisplay("你好，世界！")), '*'))), '/')
    b4.show()
    print('=====================================')


if '__main__' == __name__:
    main()
