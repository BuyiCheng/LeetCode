# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:15 PM
# @Author : byc
# @File : Shortest Path in Binary Matrix.py
# @Description :
"""
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        start, end = (0, 0), (len(grid) - 1, len(grid[0]) - 1)
        if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
            return -1
        visited = {(0, 0)}
        directs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        stack = deque([(0, 0)])
        level = 0
        while stack:
            length = len(stack)
            level += 1
            for _ in range(length):
                e = stack.popleft()
                if e == end: return level
                for d in directs:
                    new_p = (e[0] + d[0], e[1] + d[1])
                    if new_p not in visited and start[0] <= new_p[0] <= end[0] and start[1] <= new_p[1] <= end[1] and \
                            grid[new_p[0]][new_p[1]] != 1:
                        stack.append(new_p)
                        visited.add(new_p)
        return -1
