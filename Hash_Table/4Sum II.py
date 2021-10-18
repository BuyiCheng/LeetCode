# _*_ coding: utf-8 _*_
"""
# @Time : 10/18/2021 3:44 PM
# @Author : byc
# @File : 4Sum II.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        l = len(nums1)
        m = defaultdict(int)
        n = defaultdict(int)
        count = 0
        for i in range(l):
            for j in range(l):
                m[nums1[i] + nums2[j]] += 1
                n[nums3[i] + nums4[j]] += 1
        for i in m.keys():
            if -i in n:
                count += m[i] * n[-i]
        return count


