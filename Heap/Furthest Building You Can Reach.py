# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 5:15 PM
# @Author : byc
# @File : Furthest Building You Can Reach.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        n_b = 0
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff < 0:
                continue
            if len(heap) < ladders:
                heapq.heappush(heap, diff)
            else:
                n_b += heapq.heappushpop(heap, diff)
                if n_b > bricks:
                    return i - 1
        return len(heights) - 1
