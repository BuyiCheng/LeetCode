# _*_ coding: utf-8 _*_
"""
# @Time : 11/11/2021 8:34 PM
# @Author : byc
# @File : Letter Combinations of a Phone Number.py
# @Description :
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        letter_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                     '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def backtrack(i, l):
            if i == len(digits):
                result.append(''.join(l))
                return
            for s in letter_map[digits[i]]:
                l.append(s)
                backtrack(i+1, l)
                l.pop()
        result = []
        backtrack(0, [])
        return result