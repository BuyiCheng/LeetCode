# _*_ coding: utf-8 _*_
"""
# @Time : 10/31/2021 4:22 PM
# @Author : byc
# @File : Sort an Array.py
# @Description :
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, l1, l2):
        p1 = p2 = 0
        l = list()
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] <= l2[p2]:
                l.append(l1[p1])
                p1 += 1
            else:
                l.append(l2[p2])
                p2 += 1
        l.extend(l1[p1:])
        l.extend(l2[p2:])

        return l
