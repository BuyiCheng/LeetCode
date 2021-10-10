# _*_ coding: utf-8 _*_
"""
# @Time : 10/10/2021 1:09 PM
# @Author : byc
# @File : Rotate Array.py
# @Description :
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]