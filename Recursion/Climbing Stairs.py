# _*_ coding: utf-8 _*_
"""
# @Time : 10/29/2021 9:56 PM
# @Author : byc
# @File : Climbing Stairs.py
# @Description :
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()
        return self.climb(n, cache)

    def climb(self, n, cache):
        if n == 0 or n == 1:
            return 1
        if n in cache:
            return cache[n]
        val = self.climb(n - 1, cache) + self.climb(n - 2, cache)
        cache[n] = val
        return val