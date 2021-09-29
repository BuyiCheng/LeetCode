# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 3:43 PM
# @Author : byc
# @File : Max Consecutive Ones.py
# @Description :
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        len_ones = 0
        head = -1
        for tail in range(len(nums)):
            if nums[tail] == 0:
                head = tail
            if (tail-head) > len_ones: len_ones = tail - head
        return len_ones