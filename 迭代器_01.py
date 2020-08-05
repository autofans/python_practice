from collections.abc import Iterable, Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """__iter__方法可以使一个对象变成可迭代对象"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("88")
classmate.add("99")
classmate.add("100")

for x in classmate:
    print(x)
    time.sleep(1)

