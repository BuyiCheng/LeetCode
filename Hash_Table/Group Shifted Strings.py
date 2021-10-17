# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 7:34 PM
# @Author : byc
# @File : Group Shifted Strings.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strings:
            if len(s) == 1:
                m[(-1,)].append(s)
            else:
                tmp = []
                for i in range(1, len(s)):
                    tmp.append((ord(s[i])-ord(s[i-1])+26)%26)
                m[tuple(tmp)].append(s)
        result = []
        for v in m.values():
            result.append(v)
        return result