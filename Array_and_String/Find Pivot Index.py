# _*_ coding: utf-8 _*_
"""
# @Time : 9/28/2021 6:46 PM
# @Author : byc
# @File : Find Pivot Index.py
# @Description :
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_n = sum(nums)
        left_sum = 0
        for i, e in enumerate(nums):
            right_sum = sum_n - e - left_sum
            if left_sum == right_sum:
                return i
            left_sum = left_sum + e
        return -1