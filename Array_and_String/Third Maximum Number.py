# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:24 PM
# @Author : byc
# @File : Third Maximum Number.py
# @Description :
"""
import heapq
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3: return max(nums)
        heap = nums[:3]
        heapq.heapify(heap)
        for n in nums[3:]:
            if len(heap) < 3:
                heap.append()
            else:
                heapq.heappushpop(heap, n)
        return heap[0]