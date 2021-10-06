# _*_ coding: utf-8 _*_
"""
# @Time : 10/6/2021 12:17 AM
# @Author : byc
# @File : Evaluate Reverse Polish Notation.py
# @Description :
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        notations = ['+', '-', '*', '/']
        stack = list()
        for t in tokens:
            if t not in notations:
                stack.append(t)
            else:
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(self.calculate(int(a2), int(a1), t))
        return stack.pop()

    def calculate(self, x, y, notation):
        if notation == '+':
            return x + y
        elif notation == '-':
            return x - y
        elif notation == '*':
            return x * y
        elif notation == '/':
            return int(x / y)
        else:
            return 0