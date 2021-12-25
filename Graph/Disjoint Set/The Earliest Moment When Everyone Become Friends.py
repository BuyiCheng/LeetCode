# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:07 PM
# @Author : byc
# @File : The Earliest Moment When Everyone Become Friends.py
# @Description :
"""
from typing import List


class UnionFind(object):
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for r in range(len(self.root)):
                if self.root[r] == rootX:
                    self.root[r] = rootY

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs, key=lambda x: x[0])
        uf = UnionFind(n)
        for log in logs:
            uf.union(log[1], log[2])
            if len(set(uf.root)) == 1:
                return log[0]
        return -1

