# _*_ coding: utf-8 _*_
"""
# @Time : 10/24/2021 8:15 PM
# @Author : byc
# @File : Search in a Sorted Array of Unknown Size.py
# @Description :
"""
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l, r = 0, 10 ** 4 - 1
        while l <= r:
            mid = l + (r - l) // 2
            if reader.get(mid) == target:
                return mid
            if target > reader.get(mid):
                l = mid + 1
            else:
                r = mid - 1

        return -1