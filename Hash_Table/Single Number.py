# _*_ coding: utf-8 _*_
"""
# @Time : 10/11/2021 1:37 PM
# @Author : byc
# @File : Single Number.py
# @Description :
"""
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for k, v in d.items():
            if v == 1:
                return k
