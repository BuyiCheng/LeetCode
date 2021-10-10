# _*_ coding: utf-8 _*_
"""
# @Time : 10/10/2021 10:37 AM
# @Author : byc
# @File : 01 Matrix.py
# @Description :
"""
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h, w = len(mat), len(mat[0])
        dist = list()
        for _ in range(h): dist.append([-1] * w)
        stack = deque([])
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 0:
                    stack.append((i, j))
                    dist[i][j] = 0
        step = 0
        while stack:
            length = len(stack)
            step += 1
            for _ in range(len(stack)):
                e = stack.popleft()
                for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = e[0] + d[0], e[1] + d[1]
                    if 0 <= new_i < h and 0 <= new_j < w:
                        if dist[new_i][new_j] == -1:
                            stack.append((new_i, new_j))
                            dist[new_i][new_j] = step
        return dist


