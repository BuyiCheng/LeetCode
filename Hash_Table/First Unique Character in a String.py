# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 2:59 PM
# @Author : byc
# @File : First Unique Character in a String.py
# @Description :
"""
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        non_repeat = list()
        for k, v in hashmap.items():
            if v == 1:
                non_repeat.append(k)
        if len(non_repeat) == 0:
            return -1
        for i, c in enumerate(s):
            if c in non_repeat:
                return i
