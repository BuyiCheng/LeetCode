# _*_ coding: utf-8 _*_
"""
# @Time : 10/6/2021 10:31 AM
# @Author : byc
# @File : Number of Islands - stack.py
# @Description :
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # four directions
        # height and width of grid
        h, w = len(grid), len(grid[0])
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    num_island += 1
                    self.DFS(i, j, h, w, grid)
        return num_island

    def DFS(self, i, j, h, w, grid):
        if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            self.DFS(i + d[0], j + d[1], h, w, grid)