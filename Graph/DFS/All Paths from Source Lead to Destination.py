# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:13 PM
# @Author : byc
# @File : All Paths from Source Lead to Destination.py
# @Description :
"""
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        v2e = dict([(i, []) for i in range(n)])
        for e in edges:
            v2e[e[0]].append(e[1])
        stack = [[source]]
        while stack:
            p = stack.pop()
            nexts = v2e[p[-1]]
            if not nexts:
                if p[-1] != destination: return False
            for n in nexts:
                if n in p: return False
                stack.append(p + [n])
        return True

