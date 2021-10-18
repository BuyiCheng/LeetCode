# _*_ coding: utf-8 _*_
"""
# @Time : 10/18/2021 3:45 PM
# @Author : byc
# @File : Top K Frequent Elements.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for e in nums:
            m[e] += 1
        s = sorted(m.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in s[:k]]