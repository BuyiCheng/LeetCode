# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:11 PM
# @Author : byc
# @File : Find Numbers with Even Number of Digits.py
# @Description :
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n_even = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                n_even += 1
        return n_even