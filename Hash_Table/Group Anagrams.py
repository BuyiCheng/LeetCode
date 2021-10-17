# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 7:33 PM
# @Author : byc
# @File : Group Anagrams.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            m[''.join(sorted(s))].append(s)
        result = []
        for v in m.values():
            result.append(v)
        return result
