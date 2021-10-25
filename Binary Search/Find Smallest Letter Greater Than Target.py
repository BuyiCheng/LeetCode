# _*_ coding: utf-8 _*_
"""
# @Time : 10/24/2021 8:18 PM
# @Author : byc
# @File : Find Smallest Letter Greater Than Target.py
# @Description :
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        while l < r:
            m = l + (r - l) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m
        return letters[l % len(letters)]



