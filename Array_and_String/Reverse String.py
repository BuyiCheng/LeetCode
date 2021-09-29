# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 12:01 PM
# @Author : byc
# @File : Reverse String.py
# @Description :
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1