# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 3:00 PM
# @Author : byc
# @File : Intersection of Two Arrays II.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        e_set = set(nums1).intersection(nums2)
        map1, map2 = defaultdict(int), defaultdict(int)
        for e in nums1:
            if e in e_set:
                map1[e] += 1
        for e in nums2:
            if e in e_set:
                map2[e] += 1
        for k in map1.keys():
            map1[k] = map1[k] if map1[k] < map2[k] else map2[k]
        result = list()
        for k, v in map1.items():
            result.extend([k] * v)
        return result
