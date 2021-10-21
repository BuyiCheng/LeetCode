# _*_ coding: utf-8 _*_
"""
# @Time : 10/20/2021 9:27 PM
# @Author : byc
# @File : First Bad Version.py
# @Description :
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m + 1):
                if not isBadVersion(m):
                    return m + 1
                else:
                    r = m
            else:
                l = m + 1
        return l


