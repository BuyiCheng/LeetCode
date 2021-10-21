# _*_ coding: utf-8 _*_
"""
# @Time : 10/20/2021 9:27 PM
# @Author : byc
# @File : Find Peak Element.py
# @Description :
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] > nums[m + 1]:
                r = m - 1
            else:
                l = m + 1
        return l
