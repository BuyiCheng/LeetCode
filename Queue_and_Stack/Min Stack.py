# _*_ coding: utf-8 _*_
"""
# @Time : 10/5/2021 8:54 PM
# @Author : byc
# @File : Min Stack.py
# @Description :
"""
from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque([])

    def push(self, val: int) -> None:
        min_val = val
        if self.stack:
            min_val = min(self.stack[-1][1], val)
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]