# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 2:57 PM
# @Author : byc
# @File : Isomorphic Strings.py
# @Description :
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)): return False
        maps = dict()
        for i in range(len(s)):
            if s[i] in maps:
                if t[i] != maps[s[i]]: return False
            else:
                maps[s[i]] = t[i]
        return True