# _*_ coding: utf-8 _*_
"""
# @Time : 10/20/2021 12:12 PM
# @Author : byc
# @File : Guess Number Higher or Lower.py
# @Description :
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guess(num):
    pass
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = int((l+r)/2)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                l = mid + 1
            else:
                r = mid - 1