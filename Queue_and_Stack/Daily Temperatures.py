# _*_ coding: utf-8 _*_
"""
# @Time : 10/5/2021 11:55 PM
# @Author : byc
# @File : Daily Temperatures.py
# @Description :
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        stack_t = list()
        m = 0
        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            if len(stack) == 0:
                stack.append((t, 0))
                m = max(t, m)
                continue
            if stack[-1][0] > t:
                stack.append((t, 1))
            else:
                if m <= t:
                    stack.append((t, 0))
                    m = t
                else:
                    step = 1
                    while stack[-1][0] <t:
                        stack_t.append(stack.pop())
                        step += 1
                    if stack[-1][0] == t:
                        step += stack[-1][1]
                    while stack_t:
                        stack.append(stack_t.pop())
                    stack.append((t, step))
        return [s[1] for s in stack[::-1]]