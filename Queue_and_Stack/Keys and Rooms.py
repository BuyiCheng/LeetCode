# _*_ coding: utf-8 _*_
"""
# @Time : 10/10/2021 11:06 AM
# @Author : byc
# @File : Keys and Rooms.py
# @Description :
"""
from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = deque([0])
        while stack:
            e = stack.popleft()
            visited.add(e)
            for r in rooms[e]:
                if r not in visited:
                    stack.append(r)
                    visited.add(r)
        if len(visited) == len(rooms):
            return True
        else:
            return False