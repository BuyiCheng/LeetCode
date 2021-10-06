# _*_ coding: utf-8 _*_
"""
# @Time : 10/3/2021 2:29 PM
# @Author : byc
# @File : Walls and Gates.py
# @Description :
"""
from typing import List


class Solution:

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        h, w = len(rooms), len(rooms[0])
        gates = list()
        for i in range(h):
            for j in range(w):
                if rooms[i][j] == 0:
                    gates.append((i, j))
        while len(gates) > 0:
            g = gates.pop()
            rx, ry = g[0], g[1]

            neighbors = set()
            neighbors.add((rx - 1, ry))
            neighbors.add((rx + 1, ry))
            neighbors.add((rx, ry - 1))
            neighbors.add((rx, ry + 1))
            for n in neighbors:
                if 0 <= n[0] < h and 0 <= n[1] < w:
                    room = rooms[n[0]][n[1]]
                    if room == -1 or room == 0:
                        continue
                    else:
                        if rooms[g[0]][g[1]] + 1 < room:
                            rooms[n[0]][n[1]] = rooms[g[0]][g[1]] + 1
                            gates.append((n[0], n[1]))