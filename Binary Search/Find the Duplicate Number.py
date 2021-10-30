# _*_ coding: utf-8 _*_
"""
# @Time : 10/29/2021 7:01 PM
# @Author : byc
# @File : Find the Duplicate Number.py
# @Description :
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # while nums[0] != nums[nums[0]]:
        #     nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        # return nums[0]
        low = fast = nums[0]
        while True:
            low = nums[low]
            fast = nums[nums[fast]]
            if low == fast:
                break
        low = nums[0]
        while low != fast:
            low = nums[low]
            fast = nums[fast]
        return low
