# _*_ coding: utf-8 _*_
"""
# @Time : 10/3/2021 3:05 PM
# @Author : byc
# @File : Number of Islands.py
# @Description :
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # four directions
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # height and width of grid
        h, w = len(grid), len(grid[0])
        # display the status of cells h * w
        visited = []
        for _ in range(len(grid)): visited.append([False]*w)
        num_island = 0
        # traverse all cells
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # if this cell is island and not visited
                if grid[i][j] == '1' and visited[i][j] == False:
                    num_island += 1
                    q = [(i, j)]
                    visited[i][j] = True
                    # DFS
                    while len(q) > 0:
                        e = q.pop()
                        neighbors = [(e[0] + d[0], e[1] + d[1]) for d in directions]
                        for n in neighbors:
                            if 0 <= n[0] < h and 0<= n[1] < w and grid[n[0]][n[1]] == '1' and visited[n[0]][n[1]] == False:
                                visited[n[0]][n[1]] = True
                                q.append(n)
        return num_island