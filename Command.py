# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Command(object):
    def execute(self):
        raise NotImplementedError


class MacroCommand(Command):
    def __init__(self):
        self.commands = []

    def execute(self):
        for i in self.commands:
            i.execute()

    def appends(self, cmd):
        self.commands.append(cmd)
        print("命令添加成功")

    def undo(self):
        if len(self.commands):
            self.commands.pop()
            print("命令删除成功")

    def clear(self):
        while len(self.commands):
            self.commands.pop()
        print("所有命令清除成功")


class RunCommand(Command):
    def execute(self):
        print("执行[跑]命令中...")


class JumpCommand(Command):
    def execute(self):
        print("执行[跳]命令中...")


class RollCommand(Command):
    def execute(self):
        print("执行[滚]命令中...")


def main():
    execs = MacroCommand()

    execs.appends(RunCommand())
    execs.execute()
    print("\n")

    execs.appends(JumpCommand())
    execs.appends(RollCommand())
    execs.execute()
    print("\n")

    execs.undo()
    execs.execute()
    print("\n")

    execs.clear()
    execs.execute()


if "__main__" == __name__:
    main()
