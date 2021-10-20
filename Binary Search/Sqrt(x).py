# _*_ coding: utf-8 _*_
"""
# @Time : 10/20/2021 12:11 PM
# @Author : byc
# @File : Sqrt(x).py
# @Description :
"""
class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x
        while l <= r:
            mid = int((l+r)/2)
            if mid * mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif (mid+1) * (mid+1) <= x:
                l = mid + 1
            else:
                r = mid - 1
        return -1