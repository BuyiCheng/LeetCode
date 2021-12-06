# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 5:14 PM
# @Author : byc
# @File : Minimum Cost to Connect Sticks.py
# @Description :
"""
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        import heapq
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            new = x + y
            cost += new
            heapq.heappush(sticks, new)
        return cost