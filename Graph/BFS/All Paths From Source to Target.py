# _*_ coding: utf-8 _*_
"""
# @Time : 12/24/2021 7:10 PM
# @Author : byc
# @File : All Paths From Source to Target.py
# @Description :
"""
from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start, end = 0, len(graph)-1
        stack = deque([[start]])
        paths = []
        while stack:
            length = len(stack)
            for _ in range(length):
                path = stack.popleft()
                neighbors = graph[path[-1]]
                for n in neighbors:
                    new_path = path + [n]
                    if n == end:
                        paths.append(new_path)
                    else:
                        stack.append(new_path)
        return paths