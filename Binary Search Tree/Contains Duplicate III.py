# _*_ coding: utf-8 _*_
"""
# @Time : 12/3/2021 8:39 PM
# @Author : byc
# @File : Contains Duplicate III.py
# @Description :
"""
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums = sorted([(e, i) for i, e in enumerate(nums)])
        # print(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j][0] - nums[i][0] <= t:
                    if abs(nums[j][1] - nums[i][1]) <= k:
                        return True
                else:
                    break
        return False