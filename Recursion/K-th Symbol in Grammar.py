# _*_ coding: utf-8 _*_
"""
# @Time : 10/30/2021 5:01 PM
# @Author : byc
# @File : K-th Symbol in Grammar.py
# @Description :
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        parent = self.kthGrammar(n - 1, k // 2 + k % 2)
        isOdd = k % 2 == 1
        if parent == 0:
            return 0 if isOdd else 1
        else:
            return 1 if isOdd else 0
