# _*_ coding: utf-8 _*_
"""
# @Time : 10/18/2021 3:42 PM
# @Author : byc
# @File : Longest Substring Without Repeating Characters.py
# @Description :
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        hashs = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] in hashs:
                while s[l] != s[r]:
                    hashs.remove(s[l])
                    l += 1
                l += 1
            hashs.add(s[r])
            r += 1
            max_len = max_len if max_len > (r - l) else (r - l)
        return max_len

