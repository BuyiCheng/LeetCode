# _*_ coding: utf-8 _*_
"""
# @Time : 12/8/2021 5:03 PM
# @Author : byc
# @File : Number of Connected Components in an Undirected Graph.py
# @Description :
"""
from typing import List


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        val = rootY
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootX:
                    self.root[i] = val


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0], e[1])

        return len(set(uf.root))