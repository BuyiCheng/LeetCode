# _*_ coding: utf-8 _*_
"""
# @Time : 10/29/2021 6:59 PM
# @Author : byc
# @File : Find Minimum in Rotated Sorted Array II.py
# @Description :
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m]<nums[r]:
                r = m
            elif nums[m] == nums[r]:
                r -= 1
            else:
                l = m + 1
        return nums[l]