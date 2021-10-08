# _*_ coding: utf-8 _*_
"""
# @Time : 10/7/2021 10:08 PM
# @Author : byc
# @File : Flood Fill.py
# @Description :
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = {(sr, sc)}
        stack = [(sr, sc)]
        h, w = len(image), len(image[0])
        val = image[sr][sc]
        while stack:
            e = stack.pop()
            for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_sr = e[0] + d[0]
                new_sc = e[1] + d[1]
                if 0 <= new_sr < h and 0 <= new_sc < w:
                    if image[new_sr][new_sc] == val and (new_sr, new_sc) not in visited:
                        stack.append((new_sr, new_sc))
                        visited.add((new_sr, new_sc))
        for v in visited:
            image[v[0]][v[1]] = newColor
        return image