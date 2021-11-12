# _*_ coding: utf-8 _*_
"""
# @Time : 11/11/2021 8:33 PM
# @Author : byc
# @File : Permutations.py
# @Description :
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) == 1:
        #     return [nums]
        # currPerms = []
        # for i in range(len(nums)):
        #     perms = self.permute(nums[:i] + nums[i+1:])
        #     for perm in perms:
        #         currPerms.append([nums[i]] + perm)
        # return currPerms
        def backtrack(first):
            if first == len(nums):
                result.append(nums[:])
            for i in range(first, len(nums)):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        result = []
        backtrack(0)
        return result