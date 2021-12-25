# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:16 PM
# @Author : byc
# @File : Rotting Oranges.py
# @Description :
"""
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_oranges = 0
        visited = set()
        stack = deque([])

        h, w = len(grid), len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] != 0:
                    num_oranges += 1
                    if grid[i][j] == 2:
                        stack.append((i, j))
                        visited.add((i, j))

        directs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        minutes = 0
        if len(visited) == num_oranges: return minutes
        while stack:
            length = len(stack)
            for _ in range(length):
                e = stack.popleft()
                for d in directs:
                    new_p = (e[0] + d[0], e[1] + d[1])
                    if new_p not in visited and 0 <= new_p[0] < h and 0 <= new_p[1] < w and grid[new_p[0]][
                        new_p[1]] == 1:
                        stack.append(new_p)
                        visited.add(new_p)
            minutes += 1
            if len(visited) == num_oranges: return minutes
        return -1