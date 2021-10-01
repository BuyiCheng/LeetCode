# _*_ coding: utf-8 _*_
"""
# @Time : 9/30/2021 9:32 PM
# @Author : byc
# @File : Remove Duplicates from Sorted Array.py
# @Description :
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        s_p = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                s_p += 1
                nums[s_p] = nums[i]

        return s_p+1