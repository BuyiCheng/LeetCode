# _*_ coding: utf-8 _*_
"""
# @Time : 10/16/2021 2:57 PM
# @Author : byc
# @File : Two Sum.py
# @Description :
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            v = target - nums[i]
            if v in hashmap.keys():
                return [hashmap[v], i]
            else:
                hashmap[nums[i]] = i



