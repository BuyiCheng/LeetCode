# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 2:41 PM
# @Author : byc
# @File : Array Partition I.py
# @Description :
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        s = 0
        for i in range(0, len(nums) - 1, 2):
            s += nums[i]
        return s
