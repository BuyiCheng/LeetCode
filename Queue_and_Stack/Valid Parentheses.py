# _*_ coding: utf-8 _*_
"""
# @Time : 10/5/2021 9:14 PM
# @Author : byc
# @File : Valid Parentheses.py
# @Description :
"""
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_d = {'}': '{', ')': '(', ']': '['}
        stack_r = deque([])
        ss = deque(list(s))
        keys = bracket_d.keys()
        while ss:
            s_e = ss.popleft()
            if s_e in keys:
                if len(stack_r) > 0 and bracket_d[s_e] == stack_r.pop():
                    continue
                else:
                    return False
            else:
                stack_r.append(s_e)
        if len(stack_r) == 0:
            return True
        else:
            return False
