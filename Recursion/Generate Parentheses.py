# _*_ coding: utf-8 _*_
"""
# @Time : 11/7/2021 8:54 PM
# @Author : byc
# @File : Generate Parentheses.py
# @Description :
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(n_l, n_r, stack=[]):
            if n_r == n:
                result.append(''.join(stack))
            if n_l < n:
                stack.append('(')
                generate(n_l + 1, n_r, stack)
                stack.pop()
            if n_r < n_l:
                stack.append(')')
                generate(n_l, n_r + 1, stack)
                stack.pop()

        result = list()
        generate(0, 0)
        return result
