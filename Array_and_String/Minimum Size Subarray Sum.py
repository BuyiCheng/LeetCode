# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 4:39 PM
# @Author : byc
# @File : Minimum Size Subarray Sum.py
# @Description :
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_len = len(nums)
        j = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                min_len = min(min_len, i+1-j)
                s -= nums[j]
                j += 1

        return min_len