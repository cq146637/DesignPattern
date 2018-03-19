# -*- coding: utf-8 -*-
__author__ = 'CQ'


class AbstractFactory(object):
    def __init__(self, name):
        self.fac_name = name

    def createCpu(self):
        raise NotImplementedError

    def createMainboard(self):
        raise NotImplementedError


class IntelFactory(AbstractFactory):
    def __init__(self, name="Intel I7-series computer"):
        super(IntelFactory, self).__init__(name)

    def createCpu(self):
        return IntelCpu('I7-6500')

    def createMainboard(self):
        return IntelMainBoard('Intel-6000')


class AmdFactory(AbstractFactory):
    def __init__(self, name="Amd 4 computer"):
            super(AmdFactory, self).__init__(name)

    def createCpu(self):
        return AmdCpu('amd444')

    def createMainboard(self):
        return AmdMainBoard('AMD-4000')


class AbstractCpu(object):
    def __init__(self, name, instructions="", arch=""):
        self.series_name = name
        self.instructions = instructions
        self.arch = arch


class IntelCpu(AbstractCpu):
    def __init__(self, series):
        super(IntelCpu, self).__init__(series)


class AmdCpu(AbstractCpu):
    def __init__(self, series):
        super(AmdCpu, self).__init__(series)


class AbstractMainboard(object):
    def __init__(self, name):
        self.series_name = name


class IntelMainBoard(AbstractMainboard):
    def __init__(self, series):
        super(IntelMainBoard, self).__init__(series)


class AmdMainBoard(AbstractMainboard):
    def __init__(self, series):
        super(AmdMainBoard, self).__init__(series)


class ComputerEngineer(object):
    def __init__(self):
        self.cpu = None
        self.mainboard = None

    def makeComputer(self, factory_obj):
        self.prepareHardwares(factory_obj)

    def prepareHardwares(self, factory_obj):
        self.cpu = factory_obj.createCpu()
        self.mainboard = factory_obj.createMainboard()

        info = '''------- computer [%s] info:

                cpu: %s
                mainboard: %s

             -------- End --------

        ''' % (factory_obj.fac_name, self.cpu.series_name, self.mainboard.series_name)
        print(info)


def main():
    engineer = ComputerEngineer()

    intel_computer = IntelFactory()
    engineer.makeComputer(intel_computer)

    amd_computer = AmdFactory()
    engineer.makeComputer(amd_computer)


if "__main__" == __name__:
    main()
