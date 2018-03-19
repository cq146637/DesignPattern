# -*- coding: utf-8 -*-
__author__ = 'CQ'


class TravelStrategy(object):
    def set_sail(self):
        raise NotImplementedError


class AirplaneStrategy(TravelStrategy):
    def set_sail(self):
        print("\033[32;1m坐飞机去旅行...\033[0m")


class TrainStrategy(TravelStrategy):
    def set_sail(self):
        print("\033[32;1m坐火车去旅行...\033[0m")


class CarStrategy(TravelStrategy):
    def set_sail(self):
        print("\033[32;1m开轿车去旅行...\033[0m")


class BicycleStrategy(TravelStrategy):
    def set_sail(self):
        print("\033[32;1m骑自行车去旅行...\033[0m")


class FootStrategy(TravelStrategy):
    def set_sail(self):
        print("\033[32;1m徒步去旅行...\033[0m")


class ShipStrategy(TravelStrategy):
    def set_sail(self):
        print("\033[32;1m做船去旅行...\033[0m")


class TravelManager(object):
    def __init__(self, travel_strategy):
        self.travel_strategy = travel_strategy

    def set_strategy(self, travel_strategy):
        self.travel_strategy = travel_strategy

    def travel(self):
        return self.travel_strategy.set_sail()


def main():
    travel = TravelManager(AirplaneStrategy())
    travel.travel()

    travel.set_strategy(TrainStrategy())
    travel.travel()

    travel.set_strategy(ShipStrategy())
    travel.travel()

    travel.set_strategy(CarStrategy())
    travel.travel()

    travel.set_strategy(BicycleStrategy())
    travel.travel()

    travel.set_strategy(FootStrategy())
    travel.travel()


if "__main__" == __name__:
    main()
