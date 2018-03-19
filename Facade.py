# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Stock():
    def __init__(self, name="股票"):
        self.name = name

    def buy(self):
        print('买 ' + self.name)

    def sell(self):
        print('卖 ' + self.name)


class ETF():
    def __init__(self, name="指数型基金"):
        self.name = name

    def buy(self):
        print('买 ' + self.name)

    def sell(self):
        print('卖 ' + self.name)


class Future():
    def __init__(self, name="期货"):
        self.name = name

    def buy(self):
        print('买 ' + self.name)

    def sell(self):
        print('卖 ' + self.name)


class NationDebt():
    def __init__(self, name="国债"):
        self.name = name

    def buy(self):
        print('买 ' + self.name)

    def sell(self):
        print('卖 ' + self.name)


class Option():
    def __init__(self, name="权证"):
        self.name = name

    def buy(self):
        print('买 ' + self.name)

    def sell(self):
        print('卖 ' + self.name)


# 基金类
class Fund():
    def __init__(self):
        self.stock = Stock()
        self.etf = ETF()
        self.future = Future()
        self.debt = NationDebt()
        self.option = Option()

    def buyFund(self):
        self.stock.buy()
        self.etf.buy()
        self.debt.buy()
        self.future.buy()
        self.option.buy()

    def sellFund(self):
        self.stock.sell()
        self.etf.sell()
        self.future.sell()
        self.debt.sell()
        self.option.sell()


def main():
    myfund = Fund()
    myfund.buyFund()
    myfund.sellFund()


if __name__ == '__main__':
    main()
