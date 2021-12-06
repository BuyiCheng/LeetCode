# _*_ coding: utf-8 _*_
"""
# @Time : 12/5/2021 4:56 PM
# @Author : byc
# @File : Kth Largest Element in an Array.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-e for e in nums]
        heapq.heapify(heap)
        last = -heap[-1]
        for _ in range(k - 1):
            if len(heap) > 0:
                heapq.heappop(heap)
        if len(heap) > 0:
            return -1 * heapq.heappop(heap)
        else:
            return last
