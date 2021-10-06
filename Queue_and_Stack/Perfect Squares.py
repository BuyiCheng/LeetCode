# _*_ coding: utf-8 _*_
"""
# @Time : 10/5/2021 8:24 PM
# @Author : byc
# @File : Perfect Squares.py
# @Description :
"""
import math
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 1:
            return 1
        q = deque([n])
        visited = set()
        step = 0
        while q:
            step += 1
            length = len(q)
            for _ in range(length):
                e = q.popleft()
                m = int(math.sqrt(e))
                for i in range(1, m + 1):
                    val = e - i ** 2
                    if val == 0:
                        return step
                    else:
                        if val not in visited:
                            q.append(val)
                        visited.add(val)
        return -1
