# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:21 PM
# @Author : byc
# @File : Height Checker.py
# @Description :
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        diff = 0
        for i in range(len(s)):
            if s[i] != heights[i]:
                diff += 1
        return diff
