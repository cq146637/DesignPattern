# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Visitor(object):
    def visit(self, file_or_dir):
        raise NotImplementedError


class Element(object):
    def accept(self, visitor):
        raise NotImplementedError


class Entry(Element):
    def getName(self):
        raise NotImplementedError

    def getSize(self):
        raise NotImplementedError

    def add(self, entry):
        pass

    def __str__(self):
        return self.getName() + " (" + str(self.getSize()) + ")"


class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def accept(self, visitor):
        visitor.visit(self)


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.dirs = []
        self.index = -1

    def getName(self):
        return self.name

    def getSize(self):
        size = 0
        for i in self.dirs:
            size += i.getSize()
        return size

    def add(self, entry):
        self.dirs.append(entry)
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.dirs) - 1 == self.index:
            self.index = -1
            raise StopIteration
        else:
            self.index += 1
            return self.dirs[self.index]

    def accept(self, visitor):
        visitor.visit(self)


class ListVisitor(Visitor):
    currentdir = ""
    def visit(self, file_or_dir):
        if isinstance(file_or_dir, File):
            print(self.currentdir + "/", file_or_dir, sep="")
        else:
            print(self.currentdir + "/", file_or_dir, sep="")
            savedir = self.currentdir
            self.currentdir += "/" + file_or_dir.getName()
            for ever_dir in file_or_dir:
                ever_dir.accept(self)
            self.currentdir = savedir


def main():
    print("Making root entries...")
    root_dir = Directory("root")
    bin_dir = Directory("bin")
    tmp_dir = Directory("tmp")
    usr_dir = Directory("usr")

    root_dir.add(bin_dir)
    root_dir.add(tmp_dir)
    root_dir.add(usr_dir)

    bin_dir.add(File("file1", 10000))
    bin_dir.add(File("file2", 10000))

    root_dir.accept(ListVisitor())

    print("\n")
    print("Making root entries...")
    taobao_dir = Directory("taobao")
    jingdong_dir = Directory("jingdong")
    tianmao_dir = Directory("tianmao")

    usr_dir.add(taobao_dir)
    usr_dir.add(jingdong_dir)
    usr_dir.add(tianmao_dir)

    taobao_dir.add(File("file3.java", 100))
    taobao_dir.add(File("file4.php", 200))
    jingdong_dir.add(File("file5.go", 400))
    jingdong_dir.add(File("file6.sh", 600))
    tianmao_dir.add(File("file7.c", 700))

    root_dir.accept(ListVisitor())

if "__main__" == __name__:
    main()
