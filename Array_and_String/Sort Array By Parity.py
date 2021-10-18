# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:19 PM
# @Author : byc
# @File : Sort Array By Parity.py
# @Description :
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        return nums