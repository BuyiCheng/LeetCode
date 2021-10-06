# _*_ coding: utf-8 _*_
"""
# @Time : 10/3/2021 4:46 PM
# @Author : byc
# @File : Open the Lock.py
# @Description :
"""
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = deque(['0000'])
        stride = -1
        while q:
            stride += 1
            length = len(q)
            for _ in range(length):
                e = q.popleft()
                if e == target:
                    return stride
                if e not in visited:
                    visited.add(e)
                    for n in self.get_neighbors(e):
                        q.append(n)
        return -1

    def get_neighbors(self, node):
        node = list(node)
        ns = list()
        for i in range(len(node)):
            tmp1 = node[:]
            tmp1[i] = '0' if tmp1[i] == '9' else str(int(tmp1[i]) + 1)
            ns.append(''.join(tmp1))
            tmp2 = node[:]
            tmp2[i] = '9' if tmp2[i] == '0' else str(int(tmp2[i]) - 1)
            ns.append(''.join(tmp2))
        return ns