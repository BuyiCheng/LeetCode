# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 3:13 PM
# @Author : byc
# @File : Two Sum II - Input array is sorted.py
# @Description :
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return i+1, j+1
            else:
                if s < target:
                    i += 1
                else:
                    j -= 1