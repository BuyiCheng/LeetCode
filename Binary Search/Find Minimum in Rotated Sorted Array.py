# _*_ coding: utf-8 _*_
"""
# @Time : 10/20/2021 9:28 PM
# @Author : byc
# @File : Find Minimum in Rotated Sorted Array.py
# @Description :
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[0]:
                r = m
            else:
                l = m + 1
        return nums[l]
