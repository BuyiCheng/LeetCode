# _*_ coding: utf-8 _*_
"""
# @Time : 10/11/2021 1:36 PM
# @Author : byc
# @File : Contains Duplicate.py
# @Description :
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)