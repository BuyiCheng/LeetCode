# _*_ coding: utf-8 _*_
"""
# @Time : 10/24/2021 8:17 PM
# @Author : byc
# @File : Pow(x, n).py
# @Description :
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n
        if n < 0:
            n = -n
            x = 1 / x
        return self.ppow(x, n)

    def ppow(self, num, n):
        if n == 0:
            return 1
        temp = self.ppow(num, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return num * temp * temp
