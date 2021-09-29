# _*_ coding: utf-8 _*_
"""
# @Time : 9/29/2021 3:32 PM
# @Author : byc
# @File : Remove Element.py
# @Description :
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j