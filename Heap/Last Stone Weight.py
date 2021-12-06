# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 5:08 PM
# @Author : byc
# @File : Last Stone Weight.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -abs(x-y))
        if len(heap) > 0:
            return -heap[0]
        return 0