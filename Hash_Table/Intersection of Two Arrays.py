# _*_ coding: utf-8 _*_
"""
# @Time : 10/11/2021 1:38 PM
# @Author : byc
# @File : Intersection of Two Arrays.py
# @Description :
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        intersection = list()
        for n1 in set(nums1):
            d[n1] = 1
        for n2 in set(nums2):
            if n2 in d:
                intersection.append(n2)
        return intersection
