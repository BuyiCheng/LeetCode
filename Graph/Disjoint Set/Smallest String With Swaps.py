# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:07 PM
# @Author : byc
# @File : Smallest String With Swaps.py
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


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for p in pairs:
            uf.union(p[0], p[1])
        comp = dict()
        for i in range(len(uf.root)):
            root = uf.find(i)
            if root not in comp:
                comp[root] = [i]
            else:
                comp[root].append(i)
        index_pair = []
        for l in comp.values():
            indices = sorted(l)
            ss = sorted([s[i] for i in l])
            index_pair += list(zip(indices, ss))
        index_pair.sort(key=lambda x: x[0])
        return ''.join([x[1] for x in index_pair])

