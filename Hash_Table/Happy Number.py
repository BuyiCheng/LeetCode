# _*_ coding: utf-8 _*_
"""
# @Time : 10/11/2021 1:39 PM
# @Author : byc
# @File : Happy Number.py
# @Description :
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        s = {n}
        while True:
            if n == 1:
                return True
            n = self.convertNum(n)
            if n in s:
                return False
            s.add(n)

    def convertNum(self, n):
        new_n = 0
        while n > 0:
            n, reminder = n // 10, n % 10
            new_n += reminder ** 2
        return new_n