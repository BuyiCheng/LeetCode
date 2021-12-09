# _*_ coding: utf-8 _*_
"""
# @Time : 12/8/2021 5:03 PM
# @Author : byc
# @File : Graph Valid Tree.py
# @Description :
"""
from typing import List


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0], e[1])
        for i in range(n - 1):
            if not uf.isConnected(i, i + 1):
                return False
        if len(edges) == n - 1:
            return True
