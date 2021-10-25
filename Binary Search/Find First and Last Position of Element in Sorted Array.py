# _*_ coding: utf-8 _*_
"""
# @Time : 10/21/2021 11:04 PM
# @Author : byc
# @File : Find First and Last Position of Element in Sorted Array.py
# @Description :
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if (m==l or nums[m-1]!=target) and nums[m]==target:
                left = m
                break
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if (m==r or nums[m+1]!=target) and nums[m]==target:
                right = m
                break
            if nums[m] > target:
                r = m -1
            else:
                l = m + 1
        return [left, right]
