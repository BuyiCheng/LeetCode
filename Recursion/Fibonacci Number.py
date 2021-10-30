# _*_ coding: utf-8 _*_
"""
# @Time : 10/29/2021 9:56 PM
# @Author : byc
# @File : Fibonacci Number.py
# @Description :
"""


class Solution:
    def fib(self, n: int) -> int:
        cache = dict()
        return self.fib_1(n, cache)

    def fib_1(self, n, cache):
        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1
        if n in cache:
            return cache[n]
        val = self.fib_1(n - 1, cache) + self.fib_1(n - 2, cache)
        cache[n] = val
        return val
