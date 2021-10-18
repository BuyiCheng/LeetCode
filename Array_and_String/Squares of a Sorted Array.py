# _*_ coding: utf-8 _*_
"""
# @Time : 10/17/2021 11:12 PM
# @Author : byc
# @File : Squares of a Sorted Array.py
# @Description :
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        result = []
        while l <= r:
            left, right = nums[l] ** 2, nums[r] ** 2
            if left <= right:
                result.append(right)
                r -= 1
            else:
                result.append(left)
                l += 1
        return result[::-1]
        # if nums[0] >= 0:
        #     return [x**2 for x in nums]
        # if nums[-1] <=0:
        #     return [x**2 for x in nums[::-1]]
        # l, r = 0, 0
        # for i in range(1, len(nums)):
        #     if nums[i-1] < 0 and nums[i] >= 0:
        #         l, r = i-1, i
        #         break
        # print(i)
        # result = []
        # while l >= 0 and r < len(nums):
        #     if nums[l]**2 <= nums[r]**2:
        #         result.append(nums[l]**2)
        #         l -= 1
        #     else:
        #         result.append(nums[r]**2)
        #         r += 1
        # if l>=0:
        #     while l >= 0:
        #         result.append(nums[l]**2)
        #         l -= 1
        # if r < len(nums):
        #     while r < len(nums):
        #         result.append(nums[r]**2)
        #         r += 1
        # return result

