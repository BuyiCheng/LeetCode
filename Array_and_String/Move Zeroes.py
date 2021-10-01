# _*_ coding: utf-8 _*_
"""
# @Time : 9/30/2021 9:37 PM
# @Author : byc
# @File : Move Zeroes.py
# @Description :
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s_p = 0
        num_zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros += 1
            else:
                nums[s_p] = nums[i]
                s_p += 1

        for i in range(s_p, len(nums)):
            nums[i] = 0