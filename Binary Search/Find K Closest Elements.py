# _*_ coding: utf-8 _*_
"""
# @Time : 10/24/2021 8:12 PM
# @Author : byc
# @File : Find K Closest Elements.py
# @Description :
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l + k]


