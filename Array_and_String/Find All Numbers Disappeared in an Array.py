# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:25 PM
# @Author : byc
# @File : Find All Numbers Disappeared in an Array.py
# @Description :
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        expected = [i for i in range(1, len(nums) + 1)]
        diff = set(expected).difference(set(nums))
        return list(diff)

