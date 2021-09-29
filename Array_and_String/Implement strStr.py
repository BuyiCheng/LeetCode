# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 11:12 AM
# @Author : byc
# @File : Implement strStr.py
# @Description :
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle, len_stack  = len(needle), len(haystack)
        if len_needle == 0:
            return 0
        i = 0
        while i <= (len_stack - len_needle):
            if haystack[i:i+len_needle] == needle:
                return i
            i += 1
        return -1