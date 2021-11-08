# _*_ coding: utf-8 _*_
"""
# @Time : 11/7/2021 8:51 PM
# @Author : byc
# @File : Combinations.py
# @Description :
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(i, comb):
            if len(comb) == k:
                result.append(comb[:])
            for e in range(i, n+1):
                if i in comb: continue
                comb.append(e)
                backtrack(e+1, comb)
                comb.remove(e)
        result = []
        backtrack(1, [])
        return result