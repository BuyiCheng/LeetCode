# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:09 PM
# @Author : byc
# @File : Find if Path Exists in Graph.py
# @Description :
"""
from collections import deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        vd = dict([(i, []) for i in range(n)])
        for e in edges:
            vd[e[0]].append(e[1])
            vd[e[1]].append(e[0])
        visited = set()
        q = deque([[start]])
        while q:
            for _ in range(len(q)):
                p = q.popleft()
                if p[-1] == end: return True
                if p[-1] not in visited:
                    visited.add(p[-1])
                else:
                    continue
                nts = vd[p[-1]]
                for nt in nts:
                    if nt not in p:
                        q.append(p + [nt])

        return False