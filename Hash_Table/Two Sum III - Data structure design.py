# _*_ coding: utf-8 _*_
"""
# @Time : 10/18/2021 3:43 PM
# @Author : byc
# @File : Two Sum III - Data structure design.py
# @Description :
"""
from collections import defaultdict


class TwoSum:

    def __init__(self):
        self.m = defaultdict(int)

    def add(self, number: int) -> None:
        self.m[number] += 1

    def find(self, value: int) -> bool:

        for k in self.m.keys():
            v = value - k
            if v in self.m.keys():
                if k == v and self.m[v] <= 1:
                    continue
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)