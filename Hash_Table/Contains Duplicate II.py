# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 3:01 PM
# @Author : byc
# @File : Contains Duplicate II.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = list()
        hmap = defaultdict(int)
        start, end = 0, 0
        for e in nums:
            hmap[e] += 1
            if end > k:
                hmap[nums[start]] -= 1
                start += 1
            if hmap[e] == 2:
                return True
            end += 1
        return False





