# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:22 PM
# @Author : byc
# @File : Max Consecutive Ones II.py
# @Description :
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s, e = 0, 0
        length, max_len = 0, 0
        p_zeros = -1
        while e < len(nums):
            if nums[e] == 0:
                if p_zeros != -1:
                    s = p_zeros + 1
                p_zeros = e
            length = e - s + 1
            max_len = length if length > max_len else max_len
            e += 1
        return max_len

