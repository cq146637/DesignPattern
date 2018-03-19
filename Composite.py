# -*- coding: utf-8 -*-
__author__ = 'CQ'


class Entry(object):
    def getName(self):
        raise NotImplementedError

    def getSize(self):
        raise NotImplementedError

    def printList(self, prefix):
        raise NotImplementedError

    def add(self, entry):
        pass


class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def printList(self, prefix):
        print("file:[%s/%s] --> size:%s\n" % (prefix, self.name, self.getSize()))


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = []

    def getName(self):
        return self.name

    def getSize(self):
        size = 0
        for i in self.directory:
            size += i.getSize()
        return size

    def printList(self, prefix=""):
        prefix += "/"+self.name
        print("[%s] --> size:%s " % (prefix, self.getSize()))
        for i in self.directory:
            i.printList(prefix)

    def add(self, entry):
        self.directory.append(entry)


def main():
    print("-----------Prepare the root file directory...")

    rootdir = Directory("root")
    bindir = Directory("bin")
    tmpdir = Directory("tmp")
    usrdir = Directory("usr")

    rootdir.add(bindir)
    rootdir.add(tmpdir)
    rootdir.add(usrdir)

    bindir.add(File("httpd", 2000))
    usrdir.add(File("python", 5000))

    rootdir.printList()

    print("\n-------------Prepare the usr file directory...")

    javadir = Directory("java")
    godir = Directory("go")
    phpdir = Directory("php")

    usrdir.add(javadir)
    usrdir.add(godir)
    usrdir.add(phpdir)

    javadir.add(File("hello.java", 20))
    godir.add(File("hello.go", 100))
    phpdir.add(File("hello.php", 50))

    rootdir.printList()


if "__main__" == __name__:
    main()
