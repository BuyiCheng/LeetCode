# _*_ coding: utf-8 _*_
"""
# @Time : 10/18/2021 3:47 PM
# @Author : byc
# @File : Insert Delete GetRandom O(1).py
# @Description :
"""
import random


class RandomizedSet:

    def __init__(self):
        self.d = dict()
        self.l = list()

    def insert(self, val: int) -> bool:
        if val in self.l:
            return False
        self.l.append(val)
        self.d[val] = len(self.l) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            if len(self.l) > 1:
                i = self.d[val]
                last = self.l[-1]
                self.l[i] = last
                self.d[last] = i
            self.l.pop()
            self.d.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.l)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()